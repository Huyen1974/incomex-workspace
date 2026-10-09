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
    test('Mọi nơi đạt mới đóng đã giải quyết',lambda:equal(close_issue(['MET','MET'],'RESOLVED',True,True),True))
    test('Từ chối có thẩm quyền kết thúc nhưng không đổi mục tiêu thành đạt',lambda:equal((close_issue(['UNMET'],'NOT_PURSUED',True,True),['UNMET']),(True,['UNMET'])))
    call=model['rows']['call'][0]
    test('Gửi chưa nhận không được trả thành đạt',lambda:equal(receive_reply(call,call['correlation_id'],'STARTED',call['callee_version_id']),'MISSING_ACK'))
    sim_ack=Simulation(model);sim_ack.ack();ack=sim_ack.model['rows']['call'][0]
    test('Không nhận kết quả nhầm lần gọi',lambda:equal(receive_reply(ack,'OTHER-CALL','STARTED',ack['callee_version_id']),'REJECT_WRONG_CALL'))
    test('Cha hủy: ghi kết quả muộn, không áp sang lần khác',lambda:equal(receive_reply(ack,ack['correlation_id'],'DUNG',ack['callee_version_id']),'LATE_RESULT_REVIEW'))
    test('Đúng ACK/mã/phiên mới áp về nơi gọi',lambda:equal(receive_reply(ack,ack['correlation_id'],'STARTED',ack['callee_version_id'],sim_ack.model),'APPLY_TO_RETURN_STEP'))
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
    test('BLOCKED chưa đổi điều kiện không chạy lại vô hạn',lambda:equal(should_recheck(blocked,deps,{'REF-DEPENDENCY':'1'},'offline'),False))
    test('Điều kiện mở chặn đổi thì xét lại',lambda:equal(should_recheck(blocked,deps,{},'online'),True))
    broken=copy.deepcopy(model);broken['rows']['edge_def'][0]['to_step_id']='NO-SUCH-STEP'
    test('Phát hiện FK gãy',lambda:reject(lambda:structural(broken)))
    broken=copy.deepcopy(model);broken['rows']['assessment'][0]['dependency_complete']=False
    test('Không giữ xanh khi thiếu danh sách phụ thuộc',lambda:reject(lambda:structural(broken)))
    db.close()
    return {'status':'SIMULATION_ONLY','tests':results,'traces':traces,'production_ready':False,'limitations':['Chưa kiểm PostgreSQL thật, concurrency/load hay quyền nguồn','Chưa gọi B3–B7, không tạo Field thật','Hàm mô phỏng kiểm hợp đồng dự kiến, chưa phải runtime production']}

# v2: the same executable rule queries are used by the simulator and emitted PG guards.
from datetime import datetime, timezone

class ContractError(AssertionError):
    pass

def require(ok, code):
    if not ok: raise ContractError(code)

def canonical(value):
    def visit(v):
        require(not isinstance(v,float), 'TQT-R-CANON-FLOAT')
        if isinstance(v,dict):
            require(all(isinstance(k,str) for k in v),'TQT-R-CANON-KEY')
            for x in v.values(): visit(x)
        elif isinstance(v,list):
            for x in v: visit(x)
    visit(value)
    return json.dumps(value,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False)

def digest(value): return hashlib.sha256(canonical(value).encode()).hexdigest()

def validate_payload(value, schema):
    require(isinstance(value,dict),'TQT-R-CONTRACT-OBJECT')
    require(set(schema['required'])<=set(value),'TQT-R-CONTRACT-MISSING')
    if not schema.get('additionalProperties',True): require(set(value)<=set(schema['properties']),'TQT-R-CONTRACT-EXTRA')
    for key,v in value.items():
        f=schema['properties'][key]
        if v is None:
            require(f.get('nullable',False),'TQT-R-CONTRACT-NULL'); continue
        types={'string':str,'array':list,'object':dict,'integer':int,'boolean':bool}
        require(type(v) is types[f['type']],'TQT-R-CONTRACT-TYPE')
        if f['type']=='string':require(len(v)>=f.get('minLength',0),'TQT-R-CONTRACT-EMPTY')
        if f['type']=='array':
            require(len(v)>=f.get('minItems',0),'TQT-R-CONTRACT-EMPTY')
            require(all(type(x) is types[f['items']] and x!='' for x in v),'TQT-R-CONTRACT-ITEM')
            require(len(set(v))==len(v),'TQT-R-CONTRACT-DUPLICATE')
        if f['type']=='object':
            require(len(v)>=f.get('minProperties',0),'TQT-R-CONTRACT-EMPTY')
            require(all(x in f['additionalValueEnum'] for x in v.values()),'TQT-R-CONTRACT-VALUE')

def complete_row(model,table,data):
    t=next(t for t in model['tables'] if t['name']==table)
    r=dict(data)
    for k,c in t['columns'].items():
        if k in r:continue
        check=next((x for x in t['checks'] if x.startswith(k+"='")),None)
        if check:r[k]=check.split("'")[1]
        elif c.get('nullable'):r[k]=None
        else:raise ContractError('MISSING_COLUMN:'+table+'.'+k)
    return r

def validate_contracts(model):
    rows=model['rows']; maps={t:{r['id']:r for r in rs} for t,rs in rows.items()}
    io=model['io_contract']
    for call in rows['call']:
        require(call['schema_version']==io['id'],'TQT-R-CONTRACT-VERSION')
        validate_payload(call['input_data'],io['input'])
        require(call['input_fingerprint']==digest({k:call[k] for k in ['schema_version','callee_version_id','input_data']}),'TQT-R-FINGERPRINT')
        issue=maps['issue'].get(call['input_data']['issue_id'])
        require(issue and issue['process_run_id']==call['run_id'],'TQT-R-CONTRACT-ISSUE')
        require(all(i in maps['impact'] and maps['impact'][i]['issue_id']==issue['id'] for i in call['input_data']['impact_ids']),'TQT-R-CONTRACT-IMPACT')
        require(all(maps['impact'][i]['origin_version']==call['input_data']['origin_version'] for i in call['input_data']['impact_ids']),'TQT-R-CONTRACT-ORIGIN')
        if call['output_data'] is not None:
            validate_payload(call['output_data'],io['output'])
            require(call['output_data']['issue_id']==issue['id'],'TQT-R-CONTRACT-OUTPUT-ISSUE')
            require(set(call['output_data']['impact_results'])==set(call['input_data']['impact_ids']),'TQT-R-CONTRACT-OUTPUT-IMPACTS')
            ref=maps['reference'].get(call['output_data']['evidence_id'])
            require(ref and ref['kind']=='SOURCE','TQT-R-CONTRACT-EVIDENCE')
        for field in ['sent_event_id','return_event_id']:
            if call[field]:
                event=maps['event'][call[field]]
                expected=call['input_data'] if field=='sent_event_id' else call['output_data']
                require(event['payload']==expected,'TQT-R-EVENT-PAYLOAD')
    for o in rows['outbox']:
        require(o['payload']==maps['event'][o['event_id']]['payload'],'TQT-R-OUTBOX-PAYLOAD')
    for edge in rows['edge_def']:
        if not edge['to_step_id']:continue
        require(set(edge['mapping'])==set(io['input']['required']),'TQT-R-MAPPING-MISSING')
        for key,binding in edge['mapping'].items():
            parts=binding['source'].split('.')
            require(len(parts)==2 and parts[0] in ['input','output'],'TQT-R-MAPPING-SOURCE')
            require(parts[1] in io[parts[0]]['properties'],'TQT-R-MAPPING-SOURCE')
            require(binding['target']=='input.'+key and binding['transform']=='identity' and binding['on_error']=='REJECT_CONTRACT','TQT-R-MAPPING-TARGET')
            require(io[parts[0]]['properties'][parts[1]]['type']==io['input']['properties'][key]['type'],'TQT-R-MAPPING-TYPE')
    for d in rows['declaration']:
        answer_rows=[a for a in rows['answer'] if a['declaration_id']==d['id']]
        require(len(d['answer_ids'])==len(set(d['answer_ids'])) and set(d['answer_ids'])=={a['id'] for a in answer_rows},'TQT-R-DECL-ANSWERS')
        require({a['scope_role'] for a in answer_rows}=={'PROCESS','TASK','TARGET','BUSINESS'},'TQT-R-DECL-SCOPES')
        require(maps['object_version'][d['process_version_id']]['kind']=='MOW' and maps['object_version'][d['task_version_id']]['kind']=='MOT','TQT-R-DECL-KIND')
        require(d['business_ids'] and d['target_context_id'],'TQT-R-DECL-CONTEXT')
        require(all(k in maps['reference'] and maps['reference'][k]['version']==v for k,v in d['source_versions'].items()),'TQT-R-DECL-SOURCES')
        require(all(i in maps['issue'] for i in d['open_issue_ids']),'TQT-R-DECL-ISSUES')
    for a in rows['answer']:
        decl=maps['declaration'][a['declaration_id']]
        kind=maps['object_version'][a['subject_version_id']]['kind']
        if a['scope_role']=='PROCESS': require(a['subject_version_id']==decl['process_version_id'],'TQT-R-ANSWER-SCOPE')
        if a['scope_role'] in ('TASK','BUSINESS'): require(a['subject_version_id']==decl['task_version_id'],'TQT-R-ANSWER-SCOPE')
        if a['scope_role']=='TARGET': require(kind==decl['target_type'],'TQT-R-ANSWER-SCOPE')
        require(a['answer_key']==digest([a['declaration_id'],a['question_ref'],a['subject_version_id'],a['scope_role']]),'TQT-R-ANSWER-KEY')
    return maps

_raw_open_db=open_db
_old_structural=structural

def validate_sql(db,model):
    for rule in model['enforcement']:
        bad=db.execute(rule['violation_sql']).fetchall()
        require(not bad,rule['id'])

def open_db(model):
    validate_contracts(model)
    db=_raw_open_db(model)
    try:validate_sql(db,model)
    except Exception: db.close(); raise
    return db

def structural(model):
    maps=_old_structural(model)
    db=open_db(model);db.close()
    return maps

def close_issue(impacts,resolution,authorized=False,evidence=False):
    if not authorized or not evidence or not impacts:return False
    return all(x=='MET' for x in impacts) if resolution=='RESOLVED' else resolution=='NOT_PURSUED'

def receive_reply(call,correlation_id,parent_state,version,model=None,now='2026-10-09T04:10:00Z'):
    if call['correlation_id']!=correlation_id:return 'REJECT_WRONG_CALL'
    if parent_state!='STARTED' or call['callee_version_id']!=version:return 'LATE_RESULT_REVIEW'
    if call['delivery_state']!='ACKNOWLEDGED' or not call['ack_event_id']:return 'MISSING_ACK'
    if model is None:return 'MISSING_EVENT_EVIDENCE'
    if now>call['deadline_at']:return 'LATE_RESULT_REVIEW'
    try:structural(model)
    except (AssertionError,sqlite3.IntegrityError):return 'INVALID_CALL_EVIDENCE'
    return 'APPLY_TO_RETURN_STEP'

_old_recheck=should_recheck
def should_recheck(a,deps,current,blocker_version=None):
    # Invalidation is evaluated even while retries remain blocked.
    if not deps or any(current.get(d['source_ref'])!=d['source_version'] for d in deps):return True
    if a['result']=='NA' and (not a.get('na_reason') or not a.get('na_approver_ref')):return True
    return _old_recheck(a,deps,current,blocker_version)

def production_ready(model):
    try:
        rows=model['rows']
        if not rows['object_def'] or not rows['object_version'] or not rows['reference']:return False
        structural(model)
        return (model['package']['state']=='FROZEN_APPROVED' and bool(model['package']['target_pg_major'])
                and all(d['registration']=='REGISTERED' for d in rows['object_def'])
                and all(v['lifecycle']=='APPROVED' for v in rows['object_version'])
                and all(r['verified'] for r in rows['reference'])
                and not any(r['id'].startswith(('DRAFT-','SIM-')) for rs in rows.values() for r in rs))
    except (AssertionError,KeyError,sqlite3.IntegrityError):return False

class Simulation:
    """Copy-on-write commit simulation; no claim of testing PostgreSQL locks.
    The DB validates the entire candidate before it replaces the persisted snapshot.
    """
    def __init__(self,model):self.model=copy.deepcopy(model);self.db=open_db(self.model)
    def transact(self,fn):
        candidate=copy.deepcopy(self.model);result=fn(candidate)
        check_history(self.model,candidate)
        db=open_db(candidate)
        self.db.close();self.db=db;self.model=candidate
        return result
    def event(self,m,kind,call=None,payload=None,issue=None,evidence=None):
        events=m['rows']['event'];seq=max([e['sequence_no'] for e in events]+[0])+1
        e=complete_row(m,'event',{'id':'SIM-EVENT-'+str(seq),'run_id':'SIM-RUN-001','call_id':call['id'] if call else None,'sequence_no':seq,'event_type':kind,'actor_ref':'REF-HOST','at':'2026-10-09T04:'+str(seq).zfill(2)+':00Z','payload':payload or {},'target_step_run_id':call['return_step_run_id'] if call else None,'callee_version_id':call['callee_version_id'] if call else None,'issue_id':issue,'evidence_ref':evidence})
        events.append(e);return e
    def ack(self):
        def op(m):
            c=m['rows']['call'][-1]
            if c['delivery_state'] in ('ACKNOWLEDGED','RETURNED'):return c['ack_event_id']
            require(c['delivery_state']=='SENT','TQT-R-CLAIM-STATE')
            e=self.event(m,'ACK',c);c.update(delivery_state='ACKNOWLEDGED',ack_event_id=e['id']);return e['id']
        return self.transact(op)
    def reply(self,outcome='verified'):
        def op(m):
            c=m['rows']['call'][-1]
            if c['delivery_state']=='RETURNED':return c['return_event_id']
            if c['delivery_state']=='EXPIRED':return self.event(m,'LATE_RETURN',c,{'outcome':outcome})['id']
            require(c['delivery_state']=='ACKNOWLEDGED','TQT-R-RETURN-NO-ACK')
            data={'issue_id':c['input_data']['issue_id'],'impact_results':{i:'UNMET' for i in c['input_data']['impact_ids']},'outcome':outcome,'evidence_id':'REF-EVIDENCE'}
            e=self.event(m,'RETURN',c,data);c.update(delivery_state='RETURNED',return_event_id=e['id'],output_data=data)
            m['rows']['outbox'].append(complete_row(m,'outbox',{'id':'SIM-OUT-'+e['id'],'event_id':e['id'],'destination_ref':c['sender_owner_ref'],'delivery_key':e['id']+':'+c['sender_owner_ref'],'payload':data,'state':'PENDING','attempts':0}));return e['id']
        return self.transact(op)
    def cancel(self):
        def op(m):
            m['rows']['run'][0]['state']='DUNG';m['rows']['step_run'][0]['state']='DUNG';m['rows']['call'][-1]['delivery_state']='EXPIRED';self.event(m,'CANCEL')
        self.transact(op)
    def retest(self,impact_id):
        def op(m):
            p=next(p for p in m['rows']['impact'] if p['id']==impact_id)
            base=copy.deepcopy(m['rows']['assessment'][0]);base.update(id='SIM-PROOF-'+impact_id,case_ref=p['case_ref'],origin_ref=p['origin_ref'],origin_version=p['origin_version'],checked_at='2026-10-09T05:00:00Z',supersedes_id=(m['rows']['assessment'][0]['id'] if p['origin_ref']=='REF-UI-A' else None))
            m['rows']['assessment'].append(base)
            dep=copy.deepcopy(m['rows']['dependency'][0]);dep.update(id='SIM-DEP-'+impact_id,assessment_id=base['id']);m['rows']['dependency'].append(dep)
            p.update(goal_result='MET',assessment_id=base['id']);self.event(m,'CHECK',issue=p['issue_id'],evidence='REF-EVIDENCE')
        self.transact(op)
    def close(self,resolution='RESOLVED',actor='REF-HOST'):
        def op(m):
            issue=m['rows']['issue'][0];require(issue['state']=='OPEN','TQT-R-ALREADY-CLOSED')
            e=self.event(m,'CLOSE',payload={'resolution':resolution,'rule_ref':issue['close_rule_ref'],'revision':issue['revision']},issue=issue['id'],evidence='REF-EVIDENCE');e['actor_ref']=actor
            issue.update(state='CLOSED',resolution=resolution,close_event_id=e['id'],revision=issue['revision']+1)
            m['rows']['run'][0].update(state='XONG',outcome=resolution)
            m['rows']['outbox'].append(complete_row(m,'outbox',{'id':'SIM-OUT-CLOSE','event_id':e['id'],'destination_ref':issue['owner_ref'],'delivery_key':e['id']+':'+issue['owner_ref'],'payload':e['payload'],'state':'PENDING','attempts':0}))
        self.transact(op)

def check_history(old,new):
    for t in ['object_version','step_def','edge_def','reference','answer','assessment','dependency','event','declaration']:
        newer={r['id']:r for r in new['rows'][t]}
        for r in old['rows'][t]:require(newer.get(r['id'])==r,'TQT-R-IMMUTABLE:'+t)
    closed={r['id'] for r in old['rows']['issue'] if r['state']=='CLOSED'}
    old_impacts={r['id'] for r in old['rows']['impact']}
    for r in new['rows']['impact']:
        require(r['id'] in old_impacts or r['issue_id'] not in closed,'TQT-R-CLOSED-IMPACT')
    for r in old['rows']['run']:
        n=next(n for n in new['rows']['run'] if n['id']==r['id']);require(n['process_version_id']==r['process_version_id'],'TQT-R-PINNED-VERSION')

def read_declaration(db,decl_id):
    db.row_factory=sqlite3.Row
    row=dict(db.execute('SELECT * FROM declaration WHERE id=?',(decl_id,)).fetchone())
    for k in ['business_ids','answer_ids','source_versions','open_issue_ids']:row[k]=json.loads(row[k])
    answers=[]
    for aid in row['answer_ids']:
        a=dict(db.execute('SELECT * FROM answer WHERE id=?',(aid,)).fetchone());a['value']=json.loads(a['value']);answers.append(a)
    return {'declaration':row,'answers':answers}


def pg_guards(model):
    # Core relational predicates are identical to the tested SQLite rule-to-enforcement map.
    sql='''
CREATE FUNCTION tqt_canon(v jsonb) RETURNS text LANGUAGE plpgsql IMMUTABLE AS $$
DECLARE result text;
BEGIN
 CASE jsonb_typeof(v)
 WHEN 'object' THEN SELECT '{'||COALESCE(string_agg(to_jsonb(key)::text||':'||tqt_canon(value),',' ORDER BY key COLLATE "C"),'')||'}' INTO result FROM jsonb_each(v);
 WHEN 'array' THEN SELECT '['||COALESCE(string_agg(tqt_canon(value),',' ORDER BY ord),'')||']' INTO result FROM jsonb_array_elements(v) WITH ORDINALITY a(value,ord);
 WHEN 'number' THEN IF v::text !~ '^-?[0-9]+$' THEN RAISE EXCEPTION 'TQT-R-CANON-FLOAT'; END IF; result:=v::text;
 ELSE result:=v::text;
 END CASE;
 RETURN result;
END $$;
CREATE FUNCTION tqt_payload_ok(v jsonb, spec jsonb) RETURNS boolean LANGUAGE plpgsql IMMUTABLE AS $$
DECLARE k text; f jsonb; x jsonb; typ text;
BEGIN
 IF v IS NULL OR jsonb_typeof(v)<>'object' THEN RETURN false; END IF;
 FOR k IN SELECT jsonb_array_elements_text(spec->'required') LOOP
  IF NOT v ? k THEN RETURN false; END IF;
 END LOOP;
 FOR k,x IN SELECT * FROM jsonb_each(v) LOOP
  f:=spec->'properties'->k;
  IF f IS NULL THEN RETURN false; END IF;
  typ:=jsonb_typeof(x);
  IF typ='null' THEN IF NOT COALESCE((f->>'nullable')::boolean,false) THEN RETURN false; END IF; CONTINUE; END IF;
  IF typ<>(f->>'type') THEN RETURN false; END IF;
  IF typ='string' AND length(x#>>'{}')<COALESCE((f->>'minLength')::integer,0) THEN RETURN false; END IF;
  IF typ='array' THEN
   IF jsonb_array_length(x)<COALESCE((f->>'minItems')::integer,0) OR EXISTS(SELECT 1 FROM jsonb_array_elements(x) z WHERE jsonb_typeof(z)<>f->>'items' OR z='""'::jsonb) THEN RETURN false; END IF;
   IF (SELECT count(*) FROM jsonb_array_elements(x))<>(SELECT count(DISTINCT z) FROM jsonb_array_elements(x) z) THEN RETURN false; END IF;
  END IF;
  IF typ='object' AND ((SELECT count(*) FROM jsonb_each(x))<COALESCE((f->>'minProperties')::integer,0) OR EXISTS(SELECT 1 FROM jsonb_each(x) z WHERE NOT (f->'additionalValueEnum') @> jsonb_build_array(z.value))) THEN RETURN false; END IF;
 END LOOP;
 RETURN true;
END $$;
CREATE FUNCTION tqt_assert_graph() RETURNS void LANGUAGE plpgsql AS $$
BEGIN
'''
    for r in model['enforcement']:
        sql+=' IF EXISTS ('+r['violation_sql']+') THEN RAISE EXCEPTION '+sql_value(r['id'])+" USING ERRCODE='23514'; END IF;\n"
    for field,schema in [('input_data','input'),('output_data','output')]:
        condition='' if field=='input_data' else 'c.output_data IS NOT NULL AND '
        sql+=' IF EXISTS (SELECT 1 FROM call c WHERE '+condition+'NOT tqt_payload_ok(c.'+field+','+sql_value(model['io_contract'][schema])+"::jsonb)) THEN RAISE EXCEPTION 'TQT-R-CONTRACT' USING ERRCODE='23514'; END IF;\n"
    sql+='''
 IF EXISTS(SELECT 1 FROM call c WHERE c.schema_version<>'TQT-IO-2' OR c.input_fingerprint<>encode(sha256(convert_to(tqt_canon(jsonb_build_object('schema_version',c.schema_version,'callee_version_id',c.callee_version_id,'input_data',c.input_data)),'UTF8')),'hex')) THEN RAISE EXCEPTION 'TQT-R-FINGERPRINT'; END IF;
 IF EXISTS(SELECT 1 FROM answer a WHERE a.answer_key<>encode(sha256(convert_to(tqt_canon(jsonb_build_array(a.declaration_id,a.question_ref,a.subject_version_id,a.scope_role)),'UTF8')),'hex')) THEN RAISE EXCEPTION 'TQT-R-ANSWER-KEY'; END IF;
 IF EXISTS(SELECT 1 FROM object_version v WHERE v.content_hash<>encode(sha256(convert_to(tqt_canon(jsonb_build_object('body',v.body,'steps',COALESCE((SELECT jsonb_agg(to_jsonb(s) ORDER BY s.order_no) FROM step_def s WHERE s.process_version_id=v.id),'[]'::jsonb),'edges',COALESCE((SELECT jsonb_agg(to_jsonb(e) ORDER BY e.order_no) FROM edge_def e WHERE e.process_version_id=v.id),'[]'::jsonb))),'UTF8')),'hex')) THEN RAISE EXCEPTION 'TQT-R-VERSION-HASH'; END IF;
 IF EXISTS(SELECT 1 FROM answer a JOIN declaration d ON d.id=a.declaration_id JOIN object_version v ON v.id=a.subject_version_id WHERE (a.scope_role='PROCESS' AND a.subject_version_id<>d.process_version_id) OR (a.scope_role IN ('TASK','BUSINESS') AND a.subject_version_id<>d.task_version_id) OR (a.scope_role='TARGET' AND v.kind<>d.target_type)) THEN RAISE EXCEPTION 'TQT-R-ANSWER-SCOPE'; END IF;
 IF EXISTS(SELECT 1 FROM outbox o JOIN event e ON e.id=o.event_id WHERE o.payload<>e.payload) THEN RAISE EXCEPTION 'TQT-R-OUTBOX-PAYLOAD'; END IF;
 IF EXISTS(SELECT 1 FROM declaration d JOIN object_version p ON p.id=d.process_version_id JOIN object_version t ON t.id=d.task_version_id WHERE p.kind<>'MOW' OR t.kind<>'MOT' OR jsonb_typeof(d.business_ids)<>'array' OR jsonb_array_length(d.business_ids)=0 OR length(d.target_context_id)=0) THEN RAISE EXCEPTION 'TQT-R-DECL-CONTEXT'; END IF;
 IF EXISTS(SELECT 1 FROM declaration d CROSS JOIN LATERAL jsonb_each_text(d.source_versions) s WHERE NOT EXISTS(SELECT 1 FROM reference r WHERE r.id=s.key AND r.version=s.value)) THEN RAISE EXCEPTION 'TQT-R-DECL-SOURCES'; END IF;
 IF EXISTS(SELECT 1 FROM declaration d CROSS JOIN LATERAL jsonb_array_elements_text(d.open_issue_ids) i WHERE NOT EXISTS(SELECT 1 FROM issue x WHERE x.id=i)) THEN RAISE EXCEPTION 'TQT-R-DECL-ISSUES'; END IF;
 IF EXISTS(SELECT 1 FROM call c JOIN issue i ON i.id=c.input_data->>'issue_id' WHERE i.process_run_id<>c.run_id)
 OR EXISTS(SELECT 1 FROM call c WHERE NOT EXISTS(SELECT 1 FROM issue i WHERE i.id=c.input_data->>'issue_id'))
 OR EXISTS(SELECT 1 FROM call c CROSS JOIN LATERAL jsonb_array_elements_text(c.input_data->'impact_ids') x WHERE NOT EXISTS(SELECT 1 FROM impact i WHERE i.id=x AND i.issue_id=c.input_data->>'issue_id' AND i.origin_version=c.input_data->>'origin_version'))
 THEN RAISE EXCEPTION 'TQT-R-CONTRACT-SCOPE' USING ERRCODE='23514'; END IF;
 IF EXISTS(SELECT 1 FROM call c JOIN event e ON e.id=c.sent_event_id WHERE e.payload<>c.input_data)
 OR EXISTS(SELECT 1 FROM call c JOIN event e ON e.id=c.return_event_id WHERE e.payload IS DISTINCT FROM c.output_data)
 THEN RAISE EXCEPTION 'TQT-R-EVENT-PAYLOAD' USING ERRCODE='23514'; END IF;
 IF EXISTS(SELECT 1 FROM call c WHERE c.output_data IS NOT NULL AND (c.output_data->>'issue_id'<>c.input_data->>'issue_id' OR NOT EXISTS(SELECT 1 FROM reference r WHERE r.id=c.output_data->>'evidence_id' AND r.kind='SOURCE') OR (SELECT array_agg(k ORDER BY k) FROM jsonb_object_keys(c.output_data->'impact_results') k) IS DISTINCT FROM (SELECT array_agg(k ORDER BY k) FROM jsonb_array_elements_text(c.input_data->'impact_ids') k)))
 THEN RAISE EXCEPTION 'TQT-R-CONTRACT-OUTPUT' USING ERRCODE='23514'; END IF;
 IF EXISTS(SELECT 1 FROM declaration d WHERE (SELECT array_agg(a.id ORDER BY a.id) FROM answer a WHERE a.declaration_id=d.id) IS DISTINCT FROM (SELECT array_agg(x ORDER BY x) FROM jsonb_array_elements_text(d.answer_ids) x) OR (SELECT count(DISTINCT a.scope_role) FROM answer a WHERE a.declaration_id=d.id)<>4)
 THEN RAISE EXCEPTION 'TQT-R-DECL-ANSWERS' USING ERRCODE='23514'; END IF;
END $$;
CREATE FUNCTION tqt_validate_trigger() RETURNS trigger LANGUAGE plpgsql AS $$ BEGIN PERFORM tqt_assert_graph(); RETURN NULL; END $$;
CREATE FUNCTION tqt_write_gate() RETURNS trigger LANGUAGE plpgsql AS $$
BEGIN
 IF current_setting('transaction_isolation')<>'serializable' THEN RAISE EXCEPTION 'TQT-R-SERIALIZABLE-REQUIRED'; END IF;
 -- Coarse draft gate. Production must replace with measured scoped locking and retest.
 PERFORM pg_advisory_xact_lock(20761009,2);
 RETURN NULL;
END $$;
CREATE FUNCTION tqt_immutable() RETURNS trigger LANGUAGE plpgsql AS $$ BEGIN RAISE EXCEPTION 'TQT-R-IMMUTABLE:%',TG_TABLE_NAME; END $$;
CREATE FUNCTION tqt_pin_run() RETURNS trigger LANGUAGE plpgsql AS $$ BEGIN IF NEW.process_version_id<>OLD.process_version_id THEN RAISE EXCEPTION 'TQT-R-PINNED-VERSION'; END IF; RETURN NEW; END $$;
CREATE FUNCTION tqt_impact_gate() RETURNS trigger LANGUAGE plpgsql AS $$
BEGIN
 IF EXISTS(SELECT 1 FROM issue WHERE id=NEW.issue_id AND state='CLOSED') THEN RAISE EXCEPTION 'TQT-R-CLOSED-IMPACT'; END IF;
 RETURN NEW;
END $$;
'''
    for t in model['tables']:
        name='"'+t['name']+'"'
        sql+='CREATE CONSTRAINT TRIGGER '+t['name']+'_validate AFTER INSERT OR UPDATE OR DELETE ON '+name+' DEFERRABLE INITIALLY DEFERRED FOR EACH ROW EXECUTE FUNCTION tqt_validate_trigger();\n'
        sql+='CREATE TRIGGER '+t['name']+'_gate BEFORE INSERT OR UPDATE OR DELETE ON '+name+' FOR EACH STATEMENT EXECUTE FUNCTION tqt_write_gate();\n'
    for t in ['object_version','step_def','edge_def','reference','answer','assessment','dependency','event','declaration']:
        sql+='CREATE TRIGGER '+t+'_immutable BEFORE UPDATE OR DELETE ON "'+t+'" FOR EACH ROW EXECUTE FUNCTION tqt_immutable();\n'
    sql+='CREATE TRIGGER run_pin BEFORE UPDATE ON run FOR EACH ROW EXECUTE FUNCTION tqt_pin_run();\nCREATE TRIGGER impact_open BEFORE INSERT ON impact FOR EACH ROW EXECUTE FUNCTION tqt_impact_gate();\n'
    sql+='''CREATE VIEW effective_assessment AS SELECT a.* FROM assessment a WHERE NOT EXISTS(SELECT 1 FROM assessment b WHERE b.supersedes_id=a.id) AND NOT EXISTS(SELECT 1 FROM event e WHERE e.event_type='INVALIDATE' AND e.assessment_id=a.id);
REVOKE ALL ON ALL TABLES IN SCHEMA tqt_model_draft FROM PUBLIC;
REVOKE EXECUTE ON ALL FUNCTIONS IN SCHEMA tqt_model_draft FROM PUBLIC;
-- No worker grants: DOT role/actor binding remains a required staging gate.
'''
    return sql
def idempotent_lookup(model,candidate):
    for c in model['rows']['call']:
        if all(c[k]==candidate[k] for k in ['run_id','callee_version_id','request_key']):
            require(c['input_fingerprint']==candidate['input_fingerprint'],'TQT-R-IDEMPOTENCY-CONFLICT')
            return c['id']
    return None

def persisted_workflow(model):
    # All stages operate against persisted candidates. Responses are explicitly simulated.
    m=copy.deepcopy(model)
    call=m['rows']['call'][0];call['callee_version_id']='DRAFT-MOT-GAP-1-V1'
    call['input_fingerprint']=digest({k:call[k] for k in ['schema_version','callee_version_id','input_data']})
    m['rows']['event'][0]['callee_version_id']=call['callee_version_id']
    sim=Simulation(m)
    for order,outcome in enumerate(model['fixtures']['success']['outcomes'],1):
        sim.ack();sim.reply(outcome)
        if order==5:
            sim.retest('SIM-IMPACT-A');sim.retest('SIM-IMPACT-B')
        if order==6:
            sim.close();break
        def advance(z):
            current=z['rows']['call'][-1]
            sr=next(s for s in z['rows']['step_run'] if s['id']==current['step_run_id'])
            edge=next(e for e in z['rows']['edge_def'] if e['from_step_id']==sr['step_id'] and e['outcome']==outcome)
            require(edge['to_step_id'] is not None,'TQT-R-MISSING-NEXT')
            nxt=next(s for s in z['rows']['step_run'] if s['step_id']==edge['to_step_id'])
            require(nxt['state']=='READY','TQT-R-NEXT-NOT-READY')
            payload={}
            for k,b in edge['mapping'].items():
                source,key=b['source'].split('.');payload[k]=current['input_data' if source=='input' else 'output_data'][key]
            sr.update(state='XONG',outcome=outcome);nxt['state']='STARTED'
            definition=next(s for s in z['rows']['step_def'] if s['id']==nxt['step_id'])
            c=copy.deepcopy(current);c.update(id='SIM-CALL-'+str(order+1),step_run_id=nxt['id'],return_step_run_id=nxt['id'],callee_version_id=definition['mot_version_id'],request_key='SIM-OP-'+str(order+1),correlation_id='SIM-CORR-'+str(order+1),input_data=payload,output_data=None,ack_event_id=None,return_event_id=None,delivery_state='SENT')
            c['input_fingerprint']=digest({k:c[k] for k in ['schema_version','callee_version_id','input_data']})
            require(idempotent_lookup(z,c) is None,'TQT-R-OP-EXISTS');z['rows']['call'].append(c)
            e=sim.event(z,'SENT',c,payload);c['sent_event_id']=e['id']
            z['rows']['outbox'].append(complete_row(z,'outbox',{'id':'SIM-OUT-'+e['id'],'event_id':e['id'],'destination_ref':c['receiver_ref'],'delivery_key':e['id']+':'+c['receiver_ref'],'payload':payload,'state':'PENDING','attempts':0}))
        sim.transact(advance)
    def finish(z):
        z['rows']['step_run'][-1].update(state='XONG',outcome='resolved')
    sim.transact(finish)
    return sim

def run_contract_tests(model):
    out=[]
    def test(name,fn):
        fn();out.append({'id':'CONTRACT-'+str(len(out)+1).zfill(2),'name':name,'result':'PASS'})
    def eq(a,b):require(a==b,'ASSERT:'+repr((a,b)))
    def reject(fn,code):
        try:fn()
        except (AssertionError,sqlite3.IntegrityError) as e:
            require(code in str(e),'WRONG_REJECTION:'+str(e)+' expected '+code);return
        raise ContractError('ACCEPTED_INVALID:'+code)
    def changed(table,index,**patch):
        x=copy.deepcopy(model);x['rows'][table][index].update(patch);return x
    test('Empty impacts cannot close',lambda:eq(close_issue([],'RESOLVED',True,True),False))
    test('No authority cannot close',lambda:eq(close_issue(['MET'],'RESOLVED',False,True),False))
    test('No evidence cannot close',lambda:eq(close_issue(['MET'],'RESOLVED',True,False),False))
    test('Empty readiness gate rejects',lambda:eq(production_ready({'rows':{'object_def':[],'object_version':[],'reference':[]}}),False))
    for payload,code in [({},'MISSING'),({'issue_id':None,'impact_ids':['SIM-IMPACT-A'],'origin_version':'1'},'NULL'),({'issue_id':1,'impact_ids':['SIM-IMPACT-A'],'origin_version':'1'},'TYPE'),({'issue_id':'SIM-ISSUE-001','impact_ids':[],'origin_version':'1'},'EMPTY'),({'issue_id':'SIM-ISSUE-001','impact_ids':['A','A'],'origin_version':'1'},'DUPLICATE')]:
        test('Input contract rejects '+code,lambda p=payload,c=code:reject(lambda:open_db(changed('call',0,input_data=p)),'TQT-R-CONTRACT-'+c))
    test('Wrong schema version',lambda:reject(lambda:open_db(changed('call',0,schema_version='OLD')),'TQT-R-CONTRACT-VERSION'))
    x=copy.deepcopy(model);x['rows']['edge_def'][0]['mapping'].pop('origin_version')
    test('Missing edge mapping',lambda:reject(lambda:open_db(x),'TQT-R-MAPPING-MISSING'))
    x2=copy.deepcopy(model);x2['rows']['edge_def'][0]['mapping']['origin_version']['source']='output.not_provided'
    test('Mapping reads undeclared output',lambda:reject(lambda:open_db(x2),'TQT-R-MAPPING-SOURCE'))
    test('Wrong actor reference kind blocked by DB FK',lambda:reject(lambda:open_db(changed('run',0,owner_ref='CH-001')),'FOREIGN KEY'))
    test('MOW passed as MOT blocked by composite FK',lambda:reject(lambda:open_db(changed('step_def',0,mot_version_id='DRAFT-MOW-GAP-001-V1')),'FOREIGN KEY'))
    test('Fake Master references blocked by FK',lambda:reject(lambda:open_db(changed('object_def',0,registration='REGISTERED',master_id='REF-HOST',master_record_id='REF-HOST')),'FOREIGN KEY'))
    test('Return to stopped destination',lambda:reject(lambda:open_db(changed('step_run',0,state='DUNG')),'TQT-R-DEST'))
    xr=copy.deepcopy(model);r=copy.deepcopy(xr['rows']['round'][0]);r.update(id='SIM-ROUND-OTHER',round_no=2);xr['rows']['round'].append(r);s=copy.deepcopy(xr['rows']['step_run'][0]);s.update(id='SIM-STEP-OTHER',round_id=r['id']);xr['rows']['step_run'].append(s);xr['rows']['call'][0]['return_step_run_id']=s['id']
    test('Return to other round of same run',lambda:reject(lambda:open_db(xr),'FOREIGN KEY'))
    sim=Simulation(model);sim.ack();acked=copy.deepcopy(sim.model)
    def bad_ack(**patch):
        z=copy.deepcopy(acked);z['rows']['event'][1].update(patch);return z
    test('Event type not ACK',lambda:reject(lambda:open_db(bad_ack(event_type='CHECK')),'TQT-R-ACK'))
    test('ACK before SENT',lambda:reject(lambda:open_db(bad_ack(at='2000-01-01T00:00:00Z')),'TQT-R-ACK'))
    test('ACK wrong target',lambda:reject(lambda:open_db(bad_ack(target_step_run_id='SIM-STEP-RUN-2')),'TQT-R-ACK'))
    test('ACK wrong version',lambda:reject(lambda:open_db(bad_ack(callee_version_id='DRAFT-MOT-GAP-3-V1')),'TQT-R-ACK'))
    no_grant=copy.deepcopy(acked);no_grant['rows']['grant_scope'][0]['enabled']=False
    test('ACK without granted authority',lambda:reject(lambda:open_db(no_grant),'TQT-R-ACK'))
    sim.reply();returned=copy.deepcopy(sim.model)
    same=copy.deepcopy(returned);same['rows']['call'][0]['return_event_id']=same['rows']['call'][0]['ack_event_id']
    test('One event cannot serve ACK and RETURN',lambda:reject(lambda:open_db(same),'TQT-R-EVENT-PAYLOAD'))
    expired=copy.deepcopy(returned);expired['rows']['call'][0]['deadline_at']='2000-01-01T00:00:00Z'
    test('Return past deadline cannot apply',lambda:reject(lambda:open_db(expired),'TQT-R-ACK'))
    test('Missing dependencies cannot retain PASS',lambda:reject(lambda:open_db({**model,'rows':{**model['rows'],'dependency':[]}}),'TQT-R-DEPS'))
    na=changed('assessment',0,result='NA')
    test('NA without reason cannot persist',lambda:reject(lambda:open_db(na),'CHECK constraint'))
    test('MET without assessment cannot persist',lambda:reject(lambda:open_db(changed('impact',0,goal_result='MET')),'TQT-R-IMPACT'))
    competing=copy.deepcopy(model);a=copy.deepcopy(competing['rows']['assessment'][0]);a.update(id='SIM-COMPETING',result='FAIL');competing['rows']['assessment'].append(a)
    test('Competing assessment heads rejected',lambda:reject(lambda:open_db(competing),'TQT-R-SUPERSEDE'))
    duplicate=copy.deepcopy(model);a=copy.deepcopy(duplicate['rows']['answer'][0]);a.update(id='SIM-DUP-A',answer_key='made-up');duplicate['rows']['answer'].append(a);duplicate['rows']['declaration'][0]['answer_ids'].append(a['id'])
    test('Changing arbitrary answer_key cannot create second answer',lambda:reject(lambda:open_db(duplicate),'TQT-R-ANSWER-KEY'))
    a['answer_key']=duplicate['rows']['answer'][0]['answer_key']
    test('Business uniqueness also enforced by DB',lambda:reject(lambda:open_db(duplicate),'UNIQUE constraint'))
    sim2=Simulation(model);sim2.ack();sim2.reply();before=digest(sim2.model)
    test('Close before retest rolls back',lambda:reject(lambda:sim2.close(),'TQT-R-CLOSE'))
    test('Rejected close leaves no event/run change',lambda:eq(digest(sim2.model),before))
    test('Claim retries reuse ACK',lambda:eq(sim2.ack(),sim2.ack()))
    test('Return retries reuse event',lambda:eq(sim2.reply(),sim2.reply()))
    sim2.retest('SIM-IMPACT-A')
    test('One of two retested still cannot close',lambda:reject(lambda:sim2.close(),'TQT-R-CLOSE'))
    sim2.retest('SIM-IMPACT-B')
    no_close_grant=copy.deepcopy(sim2.model)
    for g in no_close_grant['rows']['grant_scope']:
        if g['permission']=='CLOSE':g['enabled']=False
    denied=Simulation(no_close_grant)
    test('All passed but close grant disabled',lambda:reject(lambda:denied.close(),'TQT-R-CLOSE'))
    sim2.close()
    test('Persisted SENT ACK RETURN two retests CLOSE',lambda:eq((sim2.model['rows']['issue'][0]['resolution'],len(sim2.model['rows']['event'])),('RESOLVED',6)))
    test('Close includes durable outbox',lambda:eq(sim2.db.execute("SELECT count(*) FROM outbox WHERE event_id=(SELECT close_event_id FROM issue)").fetchone()[0],1))
    decline=Simulation(model);decline.ack();decline.reply('rejected');decline.close('NOT_PURSUED')
    test('Refusal closes without converting goals to MET',lambda:eq([p['goal_result'] for p in decline.model['rows']['impact']],['UNMET','UNMET']))
    cancelled=Simulation(model);cancelled.ack();cancelled.cancel();cancelled.reply()
    test('Late return recorded without applying to cancelled parent',lambda:eq((cancelled.model['rows']['call'][0]['output_data'],cancelled.model['rows']['event'][-1]['event_type']),(None,'LATE_RETURN')))
    old=digest(sim2.model)
    test('Assessment history cannot be overwritten',lambda:reject(lambda:sim2.transact(lambda z:z['rows']['assessment'][0].update(result='FAIL')),'TQT-R-IMMUTABLE:assessment'))
    test('Immutability failure is atomic',lambda:eq(digest(sim2.model),old))
    test('Definition version cannot be overwritten',lambda:reject(lambda:sim2.transact(lambda z:z['rows']['object_version'][0].update(body={})),'TQT-R-IMMUTABLE:object_version'))
    db=open_db(model);doc=read_declaration(db,'SIM-DECL-001')
    test('All 70 answer applications roundtrip',lambda:eq(len(doc['answers']),70))
    test('Full declaration roundtrip preserves all fields',lambda:eq(doc,{'declaration':model['rows']['declaration'][0],'answers':model['rows']['answer']}))
    restored=sqlite3.connect(':memory:');restored.executescript('\n'.join(db.iterdump()))
    test('SQL dump reload rebuilds identical declaration',lambda:eq(read_declaration(restored,'SIM-DECL-001'),doc))
    split=copy.deepcopy(model);d=copy.deepcopy(split['rows']['declaration'][0]);d.update(id='SIM-DECL-SECOND',application_key='SECOND',answer_ids=[])
    for a in list(split['rows']['answer']):
        b=copy.deepcopy(a);b.update(id='SECOND-'+a['id'],declaration_id=d['id']);b['answer_key']=digest([b['declaration_id'],b['question_ref'],b['subject_version_id'],b['scope_role']]);split['rows']['answer'].append(b);d['answer_ids'].append(b['id'])
    split['rows']['declaration'].append(d);db2=open_db(split)
    test('Two applications do not mix answers',lambda:eq((len(read_declaration(db2,'SIM-DECL-001')['answers']),len(read_declaration(db2,'SIM-DECL-SECOND')['answers'])),(70,70)))
    test('Fingerprint changes when payload changes',lambda:reject(lambda:open_db(changed('call',0,input_fingerprint='x')),'TQT-R-FINGERPRINT'))
    blocked={**model['rows']['assessment'][0],'result':'BLOCKED','blocker_version':'offline'}
    test('Blocked still detects dependency invalidation',lambda:eq(should_recheck(blocked,model['rows']['dependency'],{'REF-DEPENDENCY':'2'},'offline'),True))
    test('No floats accepted in canonical data',lambda:reject(lambda:canonical({'number':1.2}),'TQT-R-CANON-FLOAT'))
    flow=persisted_workflow(model)
    test('Six stages persisted as six returned calls and completed steps',lambda:eq((len(flow.model['rows']['call']),{c['delivery_state'] for c in flow.model['rows']['call']},{s['state'] for s in flow.model['rows']['step_run']}),(6,{'RETURNED'},{'XONG'})))
    test('Six-stage issue closes after both original locations retested',lambda:eq((flow.model['rows']['issue'][0]['resolution'],[i['goal_result'] for i in flow.model['rows']['impact']]),('RESOLVED',['MET','MET'])))
    retry=copy.deepcopy(model['rows']['call'][0]);retry.update(id='SIM-NEW-ID',step_run_id='SIM-OTHER-ATTEMPT')
    test('Logical retry across attempt reuses same call',lambda:eq(idempotent_lookup(model,retry),model['rows']['call'][0]['id']))
    retry['input_fingerprint']='different'
    test('Same operation key with changed payload conflicts',lambda:reject(lambda:idempotent_lookup(model,retry),'TQT-R-IDEMPOTENCY-CONFLICT'))
    def late_impact(z):
        p=copy.deepcopy(z['rows']['impact'][0]);p.update(id='SIM-NEW-IMPACT',occurrence_key='NEW');z['rows']['impact'].append(p)
    test('New impact after close requires explicit reopen',lambda:reject(lambda:flow.transact(late_impact),'TQT-R-CLOSED-IMPACT'))
    def no_outbox(z):z['rows']['outbox']=[o for o in z['rows']['outbox'] if o['event_id']!=z['rows']['issue'][0]['close_event_id']]
    test('Removing closure delivery is rejected',lambda:reject(lambda:flow.transact(no_outbox),'TQT-R-CLOSE'))
    return out,{'success_six_stages':flow.model['rows'],'decline':decline.model['rows'],'cancelled':cancelled.model['rows']}

def main():
    parser=argparse.ArgumentParser();parser.add_argument('source',nargs='?',default='view.html');parser.add_argument('--emit-pg');parser.add_argument('--report');parser.add_argument('--include-simulation',action='store_true');parser.add_argument('--trace');args=parser.parse_args()
    model=read_model(args.source)
    for v in model['rows']['object_version']:
        payload={'body':v['body'],'steps':[x for x in model['rows']['step_def'] if x['process_version_id']==v['id']],'edges':[x for x in model['rows']['edge_def'] if x['process_version_id']==v['id']]}
        require(v['content_hash']==digest(payload),'VERSION_HASH:'+v['id'])
    report=run_tests(model);extra,traces=run_contract_tests(model);report['tests']+=extra
    report['model_sha256']=digest(model);report['package_state']=model['package']['state']
    report['limitations']+=['PG guards generated but not executed on PostgreSQL; SERIALIZABLE/concurrency/privileges and DOT role binding remain OPEN','70 responses are sample persistence data, not approved business answers']
    if args.emit_pg:
        schema=model['pg']['schema'];require(schema=='tqt_model_draft','SCHEMA')
        sql='-- DRAFT NOT FROZEN. PostgreSQL staging via approved DOT only.\nBEGIN ISOLATION LEVEL SERIALIZABLE;\nCREATE SCHEMA '+schema+';\nSET LOCAL search_path TO '+schema+', pg_catalog;\n'+schema_sql(model,True)+'\n'
        if args.include_simulation:
            sql+='-- EXPLICIT SIMULATION DATA; never production manifest.\n'
            for table,rows in model['rows'].items():
                for row in rows: sql+='INSERT INTO "'+table+'" ('+','.join('"'+k+'"' for k in row)+') VALUES ('+','.join(sql_value(v) for v in row.values())+');\n'
        sql+=pg_guards(model)+'\nSELECT tqt_assert_graph();\nCOMMIT;\n'
        Path(args.emit_pg).write_text(sql)
        report['sql_sha256']=hashlib.sha256(sql.encode()).hexdigest();report['includes_simulation']=args.include_simulation
    if args.trace:Path(args.trace).write_text(json.dumps(traces,ensure_ascii=False,indent=2)+'\n')
    if args.report:Path(args.report).write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':report['status'],'passed':len(report['tests']),'model_sha256':report['model_sha256'],'package_state':report['package_state'],'production_ready':production_ready(model)},ensure_ascii=False))

if __name__=='__main__':main()
