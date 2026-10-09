#!/usr/bin/env python3
"""Validate the draft embedded in view.html; no network or production writes.

--emit-pg writes a review-only SQL package preserving IDs. SQLite tests check the
relational subset; they are NOT a PostgreSQL integration/load test.
"""
import argparse, copy, hashlib, json, re, sqlite3
from pathlib import Path

def read_model(path):
    text = Path(path).read_text()
    if path.endswith('.json'):
        return json.loads(text)
    match = re.search(r'<script id="tqt-process-model" type="application/json">(.*?)</script>', text, re.S)
    assert match, 'Missing tqt-process-model'
    return json.loads(match.group(1))

def sql_value(value):
    if value is None: return 'NULL'
    if isinstance(value, bool): return 'TRUE' if value else 'FALSE'
    if isinstance(value, (int, float)): return str(value)
    if isinstance(value, (dict, list)): value = json.dumps(value, ensure_ascii=False, sort_keys=True)
    return "'" + str(value).replace("'", "''") + "'"

def schema_sql(model, pg=False):
    lines = []
    for t in model['tables']:
        cols = []
        for name, c in t['columns'].items():
            typ = c['type'] if pg else ('INTEGER' if c['type'] in ('boolean','integer') else 'TEXT')
            cols.append(name+' '+typ+('' if c.get('nullable',False) else ' NOT NULL'))
        cols.append('PRIMARY KEY ('+', '.join(t['pk'])+')')
        cols += ['UNIQUE ('+', '.join(u)+')' for u in t['unique']]
        cols += ['CHECK ('+c+')' for c in t['checks']]
        if not pg:
            cols += ['FOREIGN KEY ('+', '.join(f['columns'])+') REFERENCES '+f['table']+' ('+', '.join(f['refs'])+') DEFERRABLE INITIALLY DEFERRED' for f in t['foreign_keys']]
        lines.append('CREATE TABLE '+t['name']+' (\n  '+',\n  '.join(cols)+'\n);')
    if pg:
        for t in model['tables']:
            for i, f in enumerate(t['foreign_keys']):
                lines.append('ALTER TABLE '+t['name']+' ADD CONSTRAINT '+t['name']+'_fk_'+str(i)+' FOREIGN KEY ('+', '.join(f['columns'])+') REFERENCES '+f['table']+' ('+', '.join(f['refs'])+') DEFERRABLE INITIALLY DEFERRED;')
    for t in model['tables']:
        for i, f in enumerate(t['foreign_keys']):
            lines.append('CREATE INDEX '+t['name']+'_ref_'+str(i)+' ON '+t['name']+' ('+', '.join(f['columns'])+');')
    lines += ['CREATE INDEX issue_review ON issue (state, review_at);', 'CREATE INDEX call_deadline ON call (delivery_state, deadline_at);', 'CREATE INDEX assessment_work ON assessment (validity, result);']
    sql='\n'.join(lines)
    if pg:
        names={t['name'] for t in model['tables']} | {c for t in model['tables'] for c in t['columns']}
        sql=re.sub(r'\b('+ '|'.join(re.escape(n) for n in sorted(names,key=len,reverse=True))+r')\b',lambda m:'"'+m.group(0)+'"',sql)
    return sql

def open_db(model):
    db = sqlite3.connect(':memory:')
    db.execute('PRAGMA foreign_keys=ON')
    db.executescript(schema_sql(model))
    db.execute('BEGIN')
    for table, rows in model['rows'].items():
        for row in rows:
            keys = list(row)
            vals = [json.dumps(row[k],ensure_ascii=False) if isinstance(row[k],(dict,list)) else row[k] for k in keys]
            db.execute('INSERT INTO '+table+' ('+','.join(keys)+') VALUES ('+','.join('?' for _ in keys)+')',vals)
    db.commit()
    return db

def structural(model):
    tables = {t['name']:t for t in model['tables']}
    maps = {name:{r['id']:r for r in rows} for name,rows in model['rows'].items()}
    for name, rows in model['rows'].items():
        assert len(maps[name])==len(rows), ('duplicate id',name)
        for row in rows:
            assert set(row)==set(tables[name]['columns']), ('columns',name,row['id'])
            for f in tables[name]['foreign_keys']:
                values = [row[c] for c in f['columns']]
                if any(v is None for v in values): continue
                assert any(all(r[k]==v for k,v in zip(f['refs'],values)) for r in model['rows'][f['table']]), ('broken FK',name,row['id'],f)
    for s in maps['step_def'].values():
        p=maps['object_version'][s['process_version_id']]
        m=maps['object_version'][s['mot_version_id']]
        assert maps['object_def'][p['object_id']]['kind']=='MOW'
        assert maps['object_def'][m['object_id']]['kind']=='MOT'
        assert maps['reference'][s['owner_ref']]['kind']=='ACTOR'
    for e in maps['edge_def'].values():
        for field in ('from_step_id','to_step_id','return_step_id'):
            if e[field]: assert maps['step_def'][e[field]]['process_version_id']==e['process_version_id'], 'edge crosses version'
    for sr in maps['step_run'].values():
        run=maps['run'][maps['round'][sr['round_id']]['run_id']]
        assert maps['step_def'][sr['step_id']]['process_version_id']==run['process_version_id'], 'step/run mismatch'
    for call in maps['call'].values():
        callee=maps['object_version'][call['callee_version_id']]
        assert maps['object_def'][callee['object_id']]['kind'] in ('MOW','MOT'), 'callee is not a process/task'
        run_id=maps['round'][maps['step_run'][call['step_run_id']]['round_id']]['run_id']
        ret=maps['round'][maps['step_run'][call['return_step_run_id']]['round_id']]['run_id']
        assert run_id==ret, 'return goes to wrong run'
        if call['child_run_id']:
            assert maps['run'][call['child_run_id']]['process_version_id']==call['callee_version_id'], 'wrong child version'
        for f in ('ack_event_id','return_event_id'):
            if call[f]:
                event=maps['event'][call[f]]
                assert event['call_id']==call['id'] and event['run_id']==run_id, 'event belongs to wrong call/run'
    for assessment in maps['assessment'].values():
        if assessment['result']=='PASS' and assessment['validity']=='CURRENT':
            assert assessment['dependency_complete'], 'unverified dependencies'
            assert any(d['assessment_id']==assessment['id'] for d in maps['dependency'].values()), 'missing dependency inventory'
    return maps

def walk(model,outcomes):
    node='DRAFT-STEP-1'; trace=[]; visited={}
    for outcome in outcomes:
        edges=[e for e in model['rows']['edge_def'] if e['from_step_id']==node and e['outcome']==outcome]
        assert len(edges)==1, ('missing/ambiguous route',node,outcome)
        edge=edges[0]; visited[edge['id']]=visited.get(edge['id'],0)+1
        if edge['max_visits'] and visited[edge['id']]>edge['max_visits']:
            return 'BLOCKED',trace+[{'edge_id':edge['id'],'reason':'loop limit','owner_ref':edge['timeout_owner_ref']}]
        trace.append({'step_id':node,'edge_id':edge['id'],'outcome':outcome,'next':edge['to_step_id'],'simulation':True})
        if edge['terminal_result']:
            assert outcome==outcomes[-1], 'outcomes after terminal'
            return edge['terminal_result'],trace
        node=edge['to_step_id']
    raise AssertionError('no terminal result')

def receive_reply(call, correlation_id, parent_state, version):
    if call['correlation_id']!=correlation_id: return 'REJECT_WRONG_CALL'
    if parent_state!='STARTED' or call['callee_version_id']!=version: return 'LATE_RESULT_REVIEW'
    if call['delivery_state']!='ACKNOWLEDGED' or not call['ack_event_id']: return 'MISSING_ACK'
    return 'APPLY_TO_RETURN_STEP'

def close_issue(impacts,resolution,authorized=False):
    if resolution=='RESOLVED': return all(x=='MET' for x in impacts)
    if resolution=='NOT_PURSUED': return authorized
    return False

def should_recheck(a,deps,current,blocker_version=None):
    if a['result']=='BLOCKED' and blocker_version==a['blocker_version']: return False
    if not a['dependency_complete']: return True
    if a['validity']!='CURRENT' or a['result'] not in ('PASS','NA'): return True
    return any(current.get(d['source_ref'])!=d['source_version'] or a['level']<d['required_level'] for d in deps)

def production_ready(model):
    return (all(d['registration']=='REGISTERED' for d in model['rows']['object_def']) and all(v['lifecycle']=='APPROVED' for v in model['rows']['object_version']) and all(r['verified'] for r in model['rows']['reference']))

def run_tests(model):
    results=[]; traces={}
    def test(name,fn):
        fn(); results.append({'id':'MODEL-TEST-'+str(len(results)+1).zfill(2),'name':name,'result':'PASS'})
    def equal(actual,expected): assert actual==expected,(actual,expected)
    def reject(fn):
        try: fn()
        except (AssertionError,sqlite3.IntegrityError): return
        raise AssertionError('invalid input accepted')
    test('Mã, khóa ngoại và phạm vi quan hệ hợp lệ',lambda:structural(model))
    db=open_db(model)
    test('Nạp toàn bộ bản ghi và đọc lại FK',lambda:equal(db.execute('PRAGMA foreign_key_check').fetchall(),[]))
    test('Chặn cấp mã Master giả cho bản nháp',lambda:equal(production_ready(model),False))
    for key,case in model['fixtures'].items():
        result,trace=walk(model,case['outcomes']);traces[key]=trace
        test('Đường '+key,lambda r=result,c=case:equal(r,c['expect']))
    test('Chặn nhánh không có nơi nhận',lambda:reject(lambda:walk(model,['recorded','missing-route'])))
    test('Vòng kiểm fail không lặp vô hạn',lambda:equal(walk(model,['recorded','reuse','bound']+['fail','bound']*4)[0],'BLOCKED'))
    test('Mới tạo Field chưa đóng hai nơi phát hiện',lambda:equal(close_issue(['UNMET','UNMET'],'RESOLVED'),False))
    test('Một nơi đạt không đóng thay nơi còn lỗi',lambda:equal(close_issue(['MET','UNMET'],'RESOLVED'),False))
    test('Mọi nơi đạt mới đóng đã giải quyết',lambda:equal(close_issue(['MET','MET'],'RESOLVED'),True))
    test('Từ chối có thẩm quyền kết thúc nhưng không đổi mục tiêu thành đạt',lambda:equal((close_issue(['UNMET'],'NOT_PURSUED',True),['UNMET']),(True,['UNMET'])))
    call=model['rows']['call'][0]
    test('Gửi chưa nhận không được trả thành đạt',lambda:equal(receive_reply(call,call['correlation_id'],'STARTED',call['callee_version_id']),'MISSING_ACK'))
    ack={**call,'delivery_state':'ACKNOWLEDGED','ack_event_id':'SIM-EVENT-ACK'}
    test('Không nhận kết quả nhầm lần gọi',lambda:equal(receive_reply(ack,'OTHER-CALL','STARTED',ack['callee_version_id']),'REJECT_WRONG_CALL'))
    test('Cha hủy: ghi kết quả muộn, không áp sang lần khác',lambda:equal(receive_reply(ack,ack['correlation_id'],'DUNG',ack['callee_version_id']),'LATE_RESULT_REVIEW'))
    test('Đúng ACK/mã/phiên mới áp về nơi gọi',lambda:equal(receive_reply(ack,ack['correlation_id'],'STARTED',ack['callee_version_id']),'APPLY_TO_RETURN_STEP'))
    # Real UNIQUE constraint rejects duplicate retries; the caller must read/reuse the existing id.
    cols=list(call);vals=[json.dumps(call[k]) if isinstance(call[k],dict) else call[k] for k in cols]
    vals[cols.index('id')]='SIM-CALL-DUP';vals[cols.index('correlation_id')]='SIM-CORR-DUP'
    test('Gửi lại cùng request_key không tạo hai call',lambda:reject(lambda:db.execute('INSERT INTO call ('+','.join(cols)+') VALUES ('+','.join('?' for _ in cols)+')',vals)))
    test('Hai nơi dùng chung một issue, giữ hai impact',lambda:equal(db.execute('SELECT COUNT(DISTINCT issue_id),COUNT(*) FROM impact').fetchone(),(1,2)))
    a=model['rows']['assessment'][0];deps=model['rows']['dependency']
    test('PASS đủ mức và đúng nguồn được dùng lại',lambda:equal(should_recheck(a,deps,{'REF-DEPENDENCY':'1'}),False))
    test('Nguồn liên quan đổi thì kiểm lại',lambda:equal(should_recheck(a,deps,{'REF-DEPENDENCY':'2'}),True))
    test('Nguồn khác đổi không bắt kiểm lại',lambda:equal(should_recheck(a,deps,{'REF-DEPENDENCY':'1','OTHER':'2'}),False))
    test('FAIL có thể còn hiệu lực nhưng vẫn cần xử lý',lambda:equal(should_recheck({**a,'result':'FAIL'},deps,{'REF-DEPENDENCY':'1'}),True))
    blocked={**a,'result':'BLOCKED','blocker_version':'offline'}
    test('BLOCKED chưa đổi điều kiện không chạy lại vô hạn',lambda:equal(should_recheck(blocked,deps,{},'offline'),False))
    test('Điều kiện mở chặn đổi thì xét lại',lambda:equal(should_recheck(blocked,deps,{},'online'),True))
    broken=copy.deepcopy(model);broken['rows']['edge_def'][0]['to_step_id']='NO-SUCH-STEP'
    test('Phát hiện FK gãy',lambda:reject(lambda:structural(broken)))
    broken=copy.deepcopy(model);broken['rows']['assessment'][0]['dependency_complete']=False
    test('Không giữ xanh khi thiếu danh sách phụ thuộc',lambda:reject(lambda:structural(broken)))
    db.close()
    return {'status':'SIMULATION_ONLY','tests':results,'traces':traces,'production_ready':False,'limitations':['Chưa kiểm PostgreSQL thật, concurrency/load hay quyền nguồn','Chưa gọi B3–B7, không tạo Field thật','Hàm mô phỏng kiểm hợp đồng dự kiến, chưa phải runtime production']}

def main():
    parser=argparse.ArgumentParser();parser.add_argument('source',nargs='?',default='view.html');parser.add_argument('--emit-pg');parser.add_argument('--report');args=parser.parse_args()
    model=read_model(args.source)
    # Identity hashes must cover a stable canonical body, not the mutable display.
    for v in model['rows']['object_version']:
        payload={'body':v['body'],'steps':[x for x in model['rows']['step_def'] if x['process_version_id']==v['id']],'edges':[x for x in model['rows']['edge_def'] if x['process_version_id']==v['id']]}
        expected=hashlib.sha256(json.dumps(payload,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
        assert v['content_hash']==expected, ('version hash mismatch',v['id'])
    report=run_tests(model)
    report['model_sha256']=hashlib.sha256(json.dumps(model,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
    if args.emit_pg:
        schema=model['pg']['schema']; assert re.fullmatch('[a-z_]+',schema)
        sql='-- DRAFT/SIMULATION ONLY. Not approved for production. Review before use.\nBEGIN;\nCREATE SCHEMA '+schema+';\nSET LOCAL search_path TO '+schema+', pg_catalog;\n'+schema_sql(model,True)+'\n'
        for table,rows in model['rows'].items():
            for row in rows: sql+='INSERT INTO "'+table+'" ('+','.join('"'+k+'"' for k in row)+') VALUES ('+','.join(sql_value(v) for v in row.values())+');\n'
        Path(args.emit_pg).write_text(sql+'COMMIT;\n')
    if args.report: Path(args.report).write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':report['status'],'passed':len(report['tests']),'model_sha256':report['model_sha256'],'production_ready':False},ensure_ascii=False))

if __name__=='__main__': main()
