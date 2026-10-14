"""Managed read-only test runner. Registry: view.html catalog.tool_registry (CAT-006).
No credentials, PG, service changes or production mutation. Default UI inputs are pinned repo fixtures; --vps-ui explicitly reads public UI. Exit 0 PASS,
1 failed test/inventory, 2 invalid invocation, 3 blocked by missing prerequisites. Default dry-run; --verify executes.
"""
import sqlite3, argparse, hashlib, json, re, subprocess, sys, shutil, tempfile, uuid, unicodedata, time, math
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

BASE = Path(__file__).resolve().parent
UI_INPUT_NAMES = frozenset({'qtth006-overview-v1.js', 'definition-master-registry-v1.js', 'process-work-master-v1.js', 'ui-child-content-v1.js', 'ui-child-from-parent-v1.js'})
UI_FIXTURE_DIRECTORY = Path('evidence/ui-inputs')
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()

def ui_input_pins(registry):
    """Pins belong to CHECK005's declared inputs, never to the fixture's own content."""
    records=[x for x in registry.get('records',[]) if x.get('id')=='TQT-CHECK-005']
    pins=records[0].get('ui_inputs') if len(records)==1 else None
    errors=[]
    if not isinstance(pins,dict):return {}, ['INVALID_UI_INPUT_INVENTORY']
    for name in sorted(UI_INPUT_NAMES-set(pins)):errors.append('MISSING_UI_PIN:'+name)
    for name in sorted(set(pins)-UI_INPUT_NAMES):errors.append('UNEXPECTED_UI_PIN:'+name)
    for name in sorted(UI_INPUT_NAMES & set(pins)):
        if not isinstance(pins[name],str) or not re.fullmatch('[0-9a-f]{64}',pins[name]):errors.append('INVALID_UI_PIN:'+name)
    return pins, errors

def ui_input_preflight(folder, registry):
    """Read all five immutable inputs before inventory, self-tests or child suites."""
    pins,errors=ui_input_pins(registry);observed={}
    if errors:return {'state':'BLOCKED','errors':errors,'inputs':observed}
    for name in sorted(UI_INPUT_NAMES):
        path=folder/name
        try:
            if path.is_symlink():errors.append('UI_INPUT_SYMLINK:'+name)
            elif not path.is_file():errors.append('MISSING_UI_INPUT:'+name)
            else:
                observed[name]=sha(path)
                if observed[name]!=pins[name]:errors.append('UI_INPUT_CHANGED:'+name)
        except OSError:errors.append('UI_INPUT_UNAVAILABLE:'+name)
    return {'state':'BLOCKED' if errors else 'PASS','errors':errors,'inputs':observed}

def pinned_fixture_paths(base, registry):
    # Only these five byte-matched read-only inputs are data, not DOT executables.
    # An extra file, a symlink or a changed fixture remains in executable inventory.
    pins,errors=ui_input_pins(registry)
    if errors:return set()
    paths=set()
    for name in UI_INPUT_NAMES:
        relative=UI_FIXTURE_DIRECTORY/name;path=base/relative
        try:
            if path.is_file() and not path.is_symlink() and path.resolve().is_relative_to(base.resolve()) and sha(path)==pins[name]:paths.add(str(relative))
        except OSError:pass
    return paths
def identity_name(value):
    value=''.join(c for c in unicodedata.normalize('NFD',str(value).lower().replace('đ','d')) if not unicodedata.combining(c))
    value=re.sub(r'^(master|danh muc)\s+','',value.strip())
    return re.sub(r'[^a-z0-9]+',' ',value).strip()

def master_identity_audit(catalog, registry):
    """Indexed comparison across the joined registries, O(rows + keys), never all pairs.
    Possible duplicates block publication for review; they are never auto-deleted.
    Only an explicit alias binding authorizes merging two different IDs.
    """
    errors=[];aliases={};bindings=catalog.get('master_identity',{}).get('bindings',[])
    for binding in bindings:
        canonical=binding.get('canonical_id')
        if not canonical or not binding.get('evidence') or not binding.get('decision'):errors.append('INVALID_ALIAS_DECISION');continue
        for key in [canonical]+binding.get('aliases',[]):
            if key in aliases:errors.append('AMBIGUOUS_ALIAS:'+key)
            aliases[key]=canonical
    rows=[dict(id=x['masterId'],name=x['masterName'],url=x.get('url'),source_key=x.get('source_key'),entity_key=x.get('entity_key'),scope=x.get('identity_scope','GLOBAL'),origin='definition') for x in registry]
    rows += [dict(id=x['code'],name=x['name'],url=x.get('url'),source_key=x.get('source_key'),entity_key=x.get('entity_key'),scope=x.get('identity_scope','GLOBAL'),origin='work') for x in catalog['work_master_designs']['records']]
    buckets={};groups={};ids=set();candidate_pairs=set()
    for row in rows:
        canonical=aliases.get(row['id'],row['id']);groups.setdefault(canonical,[]).append(row)
        if row['id'] in ids:errors.append('DUPLICATE_MASTER_ID:'+row['id'])
        ids.add(row['id'])
        for kind,value in [('name',identity_name(row['name'])),('url',row['url']),('source',row['source_key']),('entity',row['entity_key'])]:
            if not value:continue
            key=(kind,row['scope'],value)
            prior=buckets.get(key)
            if prior and prior[0]!=canonical:
                pair=tuple(sorted([prior[1],row['id']]))
                if pair not in candidate_pairs:errors.append('POSSIBLE_DUPLICATE_MASTER:'+kind+':'+','.join(pair));candidate_pairs.add(pair)
            else:buckets[key]=(canonical,row['id'])
    for binding in bindings:
        group=groups.get(binding['canonical_id'],[])
        if len([x for x in group if x['id']==binding['canonical_id']])!=1:errors.append('CANONICAL_MASTER_MISSING:'+binding['canonical_id'])
        for alias in binding.get('aliases',[]):
            if alias not in ids:errors.append('ALIAS_TARGET_MISSING:'+alias)
    return {'state':'FAIL' if errors else 'PASS','errors':errors,'input_rows':len(rows),'unique_masters':len(groups),'merged':[{'canonical_id':key,'ids':[r['id'] for r in group]} for key,group in groups.items() if len(group)>1],'scope':'Definition registry + QTTH work Masters; Config entry checked by live merged-index guard. Not a full PG/VPS inventory.'}

def identity_self_test():
    base={'work_master_designs':{'records':[{'code':'CAT-006','name':'Danh mục DOT','url':'dot-new'}]},'master_identity':{'bindings':[]}}
    registry=[{'masterId':'ML-DEF-024','masterName':'Master DOT','url':'dot-old'}]
    assert master_identity_audit(base,registry)['state']=='FAIL'
    base['master_identity']['bindings']=[{'canonical_id':'ML-DEF-024','aliases':['CAT-006'],'evidence':'TEST observed same DOT entity','decision':'TEST reuse'}]
    assert master_identity_audit(base,registry)['unique_masters']==1
    assert master_identity_audit(base,registry)['state']=='PASS'
    import copy
    cases=3
    for mutate in [
        lambda c,r:c['work_master_designs']['records'].append({'code':'OTHER','name':'  DANH MỤC  dot '}),
        lambda c,r:c['work_master_designs']['records'].append({'code':'OTHER','name':'Unrelated label','url':'dot-old'}),
        lambda c,r:r.append(dict(r[0])),
        lambda c,r:r.clear(),
        lambda c,r:c['master_identity']['bindings'].append(dict(c['master_identity']['bindings'][0])),
        lambda c,r:c['master_identity']['bindings'][0].update(evidence=''),
        lambda c,r:(r[0].update(source_key='dot_tools'),c['work_master_designs']['records'].append({'code':'OTHER','name':'renamed','source_key':'dot_tools'})),
        lambda c,r:(r[0].update(entity_key='dot'),c['work_master_designs']['records'].append({'code':'OTHER','name':'renamed','entity_key':'dot'}))
    ]:
        c,r=copy.deepcopy(base),copy.deepcopy(registry);mutate(c,r);assert master_identity_audit(c,r)['state']=='FAIL';cases+=1
    assert identity_name('Master View')!=identity_name('Master List View');cases+=1
    large=[{'masterId':str(i),'masterName':'Unique '+str(i)} for i in range(10000)]
    empty={'work_master_designs':{'records':[]}};assert master_identity_audit(empty,large)['unique_masters']==10000;cases+=1
    return {'cases':cases,'scale_rows':10000,'method':'indexed keys; no pairwise scan'}
def inventory(base, registry):
    errors = []
    records = registry['records']
    paths = [x['path'] for x in records]
    if len(set(paths)) != len(paths) or len({x['id'] for x in records}) != len(records): errors.append('DUPLICATE')
    for field in ['operation_key','sha256']:
        seen={}
        for row in records:
            value=row.get(field)
            if not value:errors.append('MISSING_METADATA:'+row['id']+':'+field)
            elif value in seen:errors.append('POSSIBLE_DUPLICATE_TOOL:'+field+':'+seen[value]+','+row['id'])
            else:seen[value]=row['id']
    # Scope is explicit: all executable Python/JS sources in this task, including future subfolders.
    actual = {str(p.relative_to(base)) for p in base.rglob('*') if p.is_file() and p.suffix in {'.py', '.js'}} - pinned_fixture_paths(base,registry)
    for p in sorted(actual - set(paths)): errors.append('UNREGISTERED:'+p)
    for x in records:
        if not isinstance(x.get('timeout_seconds'),(int,float)) or isinstance(x.get('timeout_seconds'),bool) or not math.isfinite(x['timeout_seconds']) or x['timeout_seconds'] <= 0: errors.append('INVALID_TIME_BUDGET:'+x['id'])
        p = base / x['path']
        if not p.resolve().is_relative_to(base.resolve()): errors.append('OUTSIDE_SCOPE:'+x['id']); continue
        if not p.is_file(): errors.append('MISSING:'+x['id'])
        elif sha(p) != x['sha256']: errors.append('DRIFT:'+x['id'])
        for k in ['owner','purpose','preconditions','input','output','verify','rollback','secret_handling','exit_codes','case_set','master_code']:
            if not x.get(k): errors.append('MISSING_METADATA:'+x['id']+':'+k)
    return errors

def prerequisites(which=shutil.which, version=sys.version_info):
    errors=[]
    if tuple(version[:2]) < (3,11): errors.append('PYTHON_3_11_REQUIRED')
    if not which('node'): errors.append('MISSING_RUNTIME:node')
    return errors

def memory_admission(required, observed):
    if observed is not None and observed < required:return {'state':'BLOCKED','required_bytes':required,'observed_limit_bytes':observed,'reason':'INSUFFICIENT_EXEC_MEMORY_BEFORE_TESTS'}
    return {'state':'PASS' if observed is not None else 'LIMIT_UNKNOWN','required_bytes':required,'observed_limit_bytes':observed}

def observed_memory_limit():
    limits=[]
    for name in ['/sys/fs/cgroup/memory.max','/sys/fs/cgroup/memory/memory.limit_in_bytes']:
        try:
            value=Path(name).read_text().strip()
            if value.isdigit() and 0 < int(value) < 2**60:limits.append(int(value))
        except OSError:pass
    return min(limits) if limits else None

def source_readback(path, projection):
    if not path.is_file(): return {'state':'FAIL','reason':'MISSING_PRODUCT_SOURCE'}
    try:
        document=json.loads(path.read_text());actual=document['application_D24']
        rule_checks=[]
        for source in actual.get('information_contract',{}).get('rule_sources',[]):
            if 'content_sha256' not in source: continue
            value=document
            for segment in source['ref'].split('#',1)[1].strip('/').split('/'):value=value[segment]
            digest=hashlib.sha256(json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
            rule_checks.append({'ref':source['ref'],'matched':digest==source['content_sha256']})
    except (ValueError, KeyError, OSError): return {'state':'FAIL','reason':'INVALID_PRODUCT_SOURCE'}
    return {'state':'PASS' if actual==projection and all(x['matched'] for x in rule_checks) else 'FAIL','source_sha256':sha(path),'projection_equal':actual==projection,'rule_source_checks':rule_checks,'application_id':actual.get('application_id'),'trial_declarations':len(actual.get('declarations',[])) if actual.get('trial_store',{}).get('state')=='TRIAL' else 0,'scope':'SOURCE_READBACK_ONLY_NOT_BUSINESS_APPROVAL'}

def ui_input_self_test():
    import copy, contextlib, io
    cases=[]
    with tempfile.TemporaryDirectory(prefix='TQT-TEST-ui-inputs-') as tmp:
        base=Path(tmp);folder=base/UI_FIXTURE_DIRECTORY;folder.mkdir(parents=True)
        for name in UI_INPUT_NAMES:(folder/name).write_text('// TEST read-only UI input '+name+'\n')
        pins={name:sha(folder/name) for name in UI_INPUT_NAMES}
        registry={'records':[{'id':'TQT-CHECK-005','ui_inputs':pins}]}
        good=ui_input_preflight(folder,registry)
        assert good['state']=='PASS' and good['inputs']==pins
        assert ui_input_preflight(folder.resolve(),registry)==good
        cases.append('default and explicit folder use the same five pins')
        broken=copy.deepcopy(registry);broken['records'][0]['ui_inputs'].pop('process-work-master-v1.js')
        assert 'MISSING_UI_PIN:process-work-master-v1.js' in ui_input_preflight(folder,broken)['errors']
        cases.append('missing expected hash blocks before reading inputs')
        broken=copy.deepcopy(registry);broken['records'][0]['ui_inputs']['process-work-master-v1.js']='bad'
        assert 'INVALID_UI_PIN:process-work-master-v1.js' in ui_input_preflight(folder,broken)['errors']
        cases.append('malformed expected hash blocks')
        broken=copy.deepcopy(registry);broken['records'][0]['ui_inputs']['new.js']='a'*64
        assert 'UNEXPECTED_UI_PIN:new.js' in ui_input_preflight(folder,broken)['errors']
        cases.append('unknown input cannot expand the fixture exemption')
        file=folder/'process-work-master-v1.js';raw=file.read_bytes();file.unlink()
        assert 'MISSING_UI_INPUT:process-work-master-v1.js' in ui_input_preflight(folder,registry)['errors']
        cases.append('missing input blocks')
        file.write_bytes(raw+b'// changed\n')
        assert 'UI_INPUT_CHANGED:process-work-master-v1.js' in ui_input_preflight(folder,registry)['errors']
        assert str(UI_FIXTURE_DIRECTORY/file.name) not in pinned_fixture_paths(base,registry)
        cases.append('changed input blocks and remains executable inventory')
        file.write_bytes(raw)
        assert pinned_fixture_paths(base,registry)=={str(UI_FIXTURE_DIRECTORY/name) for name in UI_INPUT_NAMES}
        executable=folder/'unexpected.js';executable.write_text('throw Error("TEST must not execute");\n')
        row={k:'test' for k in ['owner','purpose','preconditions','input','output','verify','rollback','secret_handling','exit_codes','case_set','master_code']}
        check=base/'check.js';check.write_text('// TEST registered\n')
        row.update(id='TQT-CHECK-005',path='check.js',sha256=sha(check),operation_key='test',timeout_seconds=60,ui_inputs=pins)
        assert inventory(base,{'records':[row]})==['UNREGISTERED:evidence/ui-inputs/unexpected.js']
        cases.append('only pinned fixtures excluded; extra executable still rejected')
        executable.unlink();file.unlink();file.symlink_to(check)
        assert 'UI_INPUT_SYMLINK:process-work-master-v1.js' in ui_input_preflight(folder,registry)['errors']
        assert str(UI_FIXTURE_DIRECTORY/file.name) not in pinned_fixture_paths(base,registry)
        cases.append('symlink cannot hide another executable')
        file.unlink();file.write_bytes(raw)
        (base/'run-tqt-checks.py').write_text('# TEST runner identity only\n')
        # Exercise the public entry point; any expensive work here is a test failure.
        saved={name:globals()[name] for name in ('BASE','inventory','source_readback','master_identity_audit','identity_self_test','self_test','audit_self_test')}
        argv=sys.argv
        def too_late(*args,**kwargs):raise AssertionError('UI preflight failed to stop before expensive checks')
        try:
            globals()['BASE']=base
            for name in saved:
                if name!='BASE':globals()[name]=too_late
            for failure in ('MISSING_PIN','MISSING_FILE','CHANGED_FILE'):
                selected=copy.deepcopy(registry)
                if failure=='MISSING_PIN':selected['records'][0]['ui_inputs'].pop(file.name)
                elif failure=='MISSING_FILE':file.unlink()
                else:file.write_bytes(raw+b'// TEST changed\n')
                (base/'view.html').write_text('<script id="tqt-composite-processes" type="application/json">'+json.dumps({'catalog':{'tool_registry':selected}})+'</script>')
                sys.argv=['run-tqt-checks.py','--verify'];output=io.StringIO()
                with contextlib.redirect_stdout(output):code=main()
                result=json.loads(output.getvalue())
                assert code==3 and result['status']=='BLOCKED' and result['results']==[]
                assert result['ui_input_mode']=='REPO_PINNED_FIXTURES' and result['prerequisite_errors']
                file.write_bytes(raw)
                cases.append('public --verify stops before inventory/self-tests for '+failure)
        finally:
            sys.argv=argv
            globals().update(saved)
    return {'state':'PASS','cases':len(cases),'checked':cases,'network':'NOT_USED','production':'NOT_TOUCHED'}

def self_test():
    assert memory_admission(2**31,2**30)['state']=='BLOCKED'
    assert memory_admission(2**31,2**31)['state']=='PASS'
    assert memory_admission(2**31,2**32)['state']=='PASS'
    assert memory_admission(2**31,None)['state']=='LIMIT_UNKNOWN'
    with tempfile.TemporaryDirectory(prefix='tqt-check-') as tmp:
        b=Path(tmp);p=b/'check.py';p.write_text('pass\n')
        row={k:'test' for k in ['owner','purpose','preconditions','input','output','verify','rollback','secret_handling','exit_codes','case_set','master_code']}
        row.update(id='TEST',path='check.py',sha256=sha(p),operation_key='test',timeout_seconds=60);reg={'records':[row]}
        assert inventory(b,reg)==[]
        for bad in [None,0,-1,True,float('inf')]:
            broken={**row,'timeout_seconds':bad};assert 'INVALID_TIME_BUDGET:TEST' in inventory(b,{'records':[broken]})
        duplicate=dict(row,id='SECOND');reg['records'].append(duplicate)
        assert any(x.startswith('POSSIBLE_DUPLICATE_TOOL:operation_key') for x in inventory(b,reg))
        assert any(x.startswith('POSSIBLE_DUPLICATE_TOOL:sha256') for x in inventory(b,reg))
        reg['records'].pop()
        p.write_text('changed\n');assert any(x.startswith('DRIFT:') for x in inventory(b,reg))
        p.unlink();assert any(x.startswith('MISSING:') for x in inventory(b,reg))
        p.write_text('pass\n');q=b/'new.py';q.write_text('pass\n');assert any(x.startswith('UNREGISTERED:') for x in inventory(b,reg));q.unlink()
        # Actual file write/read/restore, with Master identity; TEST does not count toward MOW001 progress.
        p=b/'master-test.json';before={'environment':'TEST','records':[]};p.write_text(json.dumps(before))
        record={'master_code':'CAT-015','record_id':'TEST-'+uuid.uuid4().hex,'application_id':'TEST-MOW001-STORE','process_code':'MOW-TH-005','target_version':'TEST','revision':1,'result':'PASS'}
        p.write_text(json.dumps({**before,'records':[record]}));loaded=json.loads(p.read_text());assert loaded['records'][0]==record
        assert loaded['records'][0]['master_code']=='CAT-015'
        p.write_text(json.dumps(before));assert json.loads(p.read_text())==before
    assert prerequisites(lambda _: None, (3,11))==['MISSING_RUNTIME:node']
    assert prerequisites(lambda _: '/test/node', (3,10))==['PYTHON_3_11_REQUIRED']
    assert prerequisites(lambda _: '/test/node', (3,11))==[]
    with tempfile.TemporaryDirectory(prefix='tqt-source-') as tmp:
        f=Path(tmp)/'source.json'; f.write_text(json.dumps({'application_D24':{'application_id':'TEST'}}))
        assert source_readback(f,{'application_id':'TEST'})['state']=='PASS'
        assert source_readback(f,{'application_id':'OTHER'})['state']=='FAIL'
        assert source_readback(f.with_name('missing.json'),{})['state']=='FAIL'
    return {'cases':20,'store':'temporary TEST file in execution snapshot','write_read_restore':'PASS','production':'NOT_TOUCHED'}

def audit_self_test(audit_sources):
    global BASE
    import sqlite3
    with tempfile.TemporaryDirectory(prefix='TQT-TEST-usage-') as tmp:
        p=Path(tmp)/'ledger.sqlite';con=sqlite3.connect(p)
        con.execute('CREATE TABLE lc_event(seq INTEGER PRIMARY KEY,event_key TEXT,at REAL,actor TEXT,source TEXT,kind TEXT,tool TEXT,work_id TEXT,run_id TEXT,call_id TEXT,detail TEXT)')
        receipt={'implementation_sha256':'a'*64,'invocation_sha256':'b'*64,'result_sha256':'c'*64,'finished_at':2,'outcome':'RETURNED','observer':'agent-data-gateway'}
        tests=[('gw',receipt),('gw',{}),('gw',{**receipt,'outcome':'STARTED'}),('gw',{**receipt,'result_sha256':'bad'}),('hook',receipt),('gw',{**receipt,'observer':'self-claim'})]
        for i,(kind,r) in enumerate(tests):con.execute('INSERT INTO lc_event VALUES (?,?,?,?,?,?,?,?,?,?,?)',(i,'TEST-'+str(i),1,'TEST','TEST',kind,'workspace_read','TEST',None,None,json.dumps({'tool_receipt':r})))
        con.commit();con.close();result=usage_audit(p,'TEST');assert result['complete_receipts']==1 and result['event_count']==6
        assert usage_audit(p,'TEST','TEST-1')['events'][0]['outcome']=='OBSERVED_RESULT_UNKNOWN'
        assert usage_audit(p,'OTHER')['event_count']==0
        assert canonical_action('mcp__agent_data__workspace_read')==canonical_action('workspace_read')
        assert canonical_action('mcp__codex_apps__incomex_mcp_full_all_2_workspace_read')=='agent-data:workspace_read'
        assert canonical_action('mcp__codex_apps__jev_reference_evaluate')=='jev-reference:evaluate'
        try:usage_audit(p,'../OTHER');assert False
        except ValueError:pass
    # P36: patch behavior is tested on an isolated minimal catalog. Never clone the
    # growing real product/history repeatedly just to test an audit metadata patch.
    evidence=BASE/'UI-REVIEW-AGGREGATE.json';audit=json.loads(evidence.read_text())['host_review_P33']['audit']
    import copy
    fake=copy.deepcopy(audit);fake['observed_at']='2099-01-01T00:00:00Z'
    real_base=BASE
    with tempfile.TemporaryDirectory(prefix='TQT-TEST-audit-patch-') as tmp:
        try:
            BASE=Path(tmp)
            (BASE/'view.html').write_text('<script id="tqt-composite-processes" type="application/json">'+json.dumps({'catalog':{'tool_registry':{'audit_sources':audit_sources,'audit_projection':{}}}})+'</script>')
            (BASE/'UI-REVIEW-AGGREGATE.json').write_text(json.dumps({'host_review_P33':{'audit':audit,'external_receipts':[]}}))
            patch=audit_patch(fake);assert len(patch['operations'])==2
            for op in patch['operations']:
                old=(BASE/Path(op['path']).name).read_text();edit=op['edits'][0]
                assert old.count(edit['old_str'])==1 and op['expected_version']==hashlib.sha256(old.encode()).hexdigest()
                changed=old.replace(edit['old_str'],edit['new_str'],1)
                if op['path'].endswith('.json'):assert json.loads(changed)['host_review_P33']['audit']['observed_at']==fake['observed_at']
                else:assert json.loads(re.search(r'<script id="tqt-composite-processes"[^>]*>(.*?)</script>',changed,re.S)[1])['catalog']['tool_registry']['audit_projection']['observed_at']==fake['observed_at']
            wrong=copy.deepcopy(fake);wrong['scope']['work_id']='OTHER'
            try:audit_patch(wrong);assert False
            except ValueError:pass
        finally:BASE=real_base
    for state in ('DRY_RUN','BLOCKED','OBSERVED'):assert runner_test_receipt({'status':state,'runner_sha256':'a'*64},'TEST') is None
    assert runner_test_receipt({'status':'PASS','runner_sha256':'a'*64},'TEST')['exit_code']==0
    assert runner_test_receipt({'status':'FAIL','runner_sha256':'a'*64},'TEST')['exit_code']==1
    return {'cases':23,'state':'PASS','scope':'TEST SQLite and prepared CAS patches; no production writes'}

def runner_test_receipt(report, evidence_ref):
    # An inventory-only/dry run is neither a passed nor a failed test execution.
    if report.get('status') not in ('PASS','FAIL') or not re.fullmatch('[0-9a-f]{64}',str(report.get('runner_sha256',''))):return None
    return {'id':'TQT-CHECK-006','sha256':report['runner_sha256'],'exit_code':0 if report['status']=='PASS' else 1,'case_set':'TQT-CASE-RUNNER','evidence_ref':evidence_ref+'#status'}

def audit_projection(audit, external_receipts=()):
    digest=hashlib.sha256(json.dumps(audit,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    checks={}
    for job in audit['executions']:
        for item in job.get('subtools',[]):checks[item['id']]={**item,'job_id':job['run_id'],'source_head':job.get('source_head')}
    return {'last_checks':list(checks.values()),'observed_at':audit['observed_at'],'audit_sha256':digest,'evidence_ref':'UI-REVIEW-AGGREGATE.json#host_review_P33/audit','dot_inventory':audit['dot_inventory'],'script_inventory':audit.get('script_inventory',[]),'dot_index_check':audit.get('dot_index_check'),'by_action':audit['usage']['by_action'],'execution_count':len(audit['executions']),'event_count':audit['usage']['event_count'],'complete_receipts':audit['usage']['complete_receipts'],'external_receipts':list(external_receipts),'gaps':audit['gaps']}

def audit_patch(audit):
    """Prepare a CAS transaction for the existing two sources; caller uses workspace_transaction.
    No live mutation here. Git transaction preserves older snapshots in source history.
    """
    view=BASE/'view.html';evidence=BASE/'UI-REVIEW-AGGREGATE.json'
    old_view=view.read_text();match=re.search(r'<script id="tqt-composite-processes"[^>]*>(.*?)</script>',old_view,re.S);doc=json.loads(match[1]);reg=doc['catalog']['tool_registry']
    if audit.get('schema_version')!=1 or audit.get('scope',{}).get('work_id')!='tools-quy-trinh' or audit.get('scanner')!=reg['audit_sources']['dot_catalog']:raise ValueError('AUDIT_SCOPE_OR_PRODUCER_MISMATCH')
    if not audit.get('observed_at') or not isinstance(audit.get('dot_inventory'),list):raise ValueError('INVALID_AUDIT')
    old_evidence=evidence.read_text();saved=json.loads(old_evidence);review=saved['host_review_P33'];review['audit']=audit
    reg['audit_projection']=audit_projection(audit,review.get('external_receipts',[]))
    new_view=old_view[:match.start(1)]+json.dumps(doc,ensure_ascii=False,indent=2)+old_view[match.end(1):]
    operations=[]
    for name,old,new in [('view.html',old_view,new_view),('UI-REVIEW-AGGREGATE.json',old_evidence,json.dumps(saved,ensure_ascii=False,indent=2)+'\n')]:
        if old==new:continue
        # One bounded replacement with unique context; version guard protects the whole file.
        start=0
        while start<min(len(old),len(new)) and old[start]==new[start]:start+=1
        tail=0
        while tail<min(len(old),len(new))-start and old[-1-tail]==new[-1-tail]:tail+=1
        left=max(0,start-80);right=min(len(old),len(old)-tail+80);delta=len(new)-len(old)
        while old.count(old[left:right])!=1 and (left or right<len(old)):left=max(0,left-80);right=min(len(old),right+80)
        a,b=old[left:right],new[left:right+delta];assert a and old.count(a)==1 and old.replace(a,b,1)==new
        operations.append({'op':'edit','path':'work/tools-quy-trinh/'+name,'expected_version':hashlib.sha256(old.encode()).hexdigest(),'edits':[{'old_str':a,'new_str':b,'expected_count':1}]})
    return {'root':'workspace','message':'P33 refresh derived DOT/Tool inventory from retained evidence','operation_id':'tqt-audit-'+hashlib.sha256(json.dumps(audit,sort_keys=True).encode()).hexdigest()[:32],'operations':operations}

def canonical_action(name):
    for prefix in ('mcp__agent_data__','mcp__codex_apps__incomex_mcp_full_all_2__','mcp__codex_apps__incomex_mcp_full_all_2_'):
        if name.startswith(prefix):return 'agent-data:'+name[len(prefix):]
    if name.startswith(('workspace_','ui_')):return 'agent-data:'+name
    if 'jev' in name.lower() and name.endswith('evaluate'):return 'jev-reference:evaluate'
    if name in ('Bash','exec_command'):return 'local:shell'
    if name=='apply_patch':return 'local:apply_patch'
    return 'observed:'+name

def usage_audit(db_path, work_id, event_key=None):
    import sqlite3,collections
    if not re.fullmatch(r'[a-zA-Z0-9_-]+',work_id):raise ValueError('INVALID_WORK_ID')
    if not db_path.is_file():raise ValueError('USAGE_DB_UNAVAILABLE')
    con=sqlite3.connect('file:'+str(db_path.resolve())+'?mode=ro',uri=True);con.row_factory=sqlite3.Row
    params=[work_id];where='work_id=?'
    if event_key:where+=' AND event_key=?';params.append(event_key)
    rows=[];groups={};seen=set()
    for raw in con.execute('SELECT seq,event_key,at,actor,source,kind,tool,work_id,run_id,call_id,detail FROM lc_event WHERE '+where+' AND tool IS NOT NULL ORDER BY seq',params):
        x=dict(raw)
        if x['kind'] not in ('gw','hook'):continue
        key=x['event_key']
        if key in seen:continue
        seen.add(key);action=canonical_action(x['tool']);detail=json.loads(x['detail'] or '{}');receipt=detail.get('tool_receipt') or {}
        version=receipt.get('implementation_sha256');complete=x['kind']=='gw' and receipt.get('observer')=='agent-data-gateway' and all(re.fullmatch('[0-9a-f]{64}',str(receipt.get(k,''))) for k in ('implementation_sha256','invocation_sha256','result_sha256')) and isinstance(receipt.get('finished_at'),(int,float)) and receipt.get('outcome') in ('RETURNED','ERROR','QUEUED')
        row={'event_key':key,'action':action,'raw_tool':x['tool'],'work_id':x['work_id'],'at':x['at'],'surface':x['actor'],'source':x['source'],'kind':x['kind'],'run_id':x['run_id'],'call_id':x['call_id'],'implementation_sha256':version,'outcome':receipt.get('outcome','OBSERVED_RESULT_UNKNOWN'),'receipt':receipt or None,'complete':bool(complete),'evidence_ref':str(db_path)+'#lc_event/seq='+str(x['seq'])}
        rows.append(row);g=groups.setdefault(action,{'action':action,'gateway_events':0,'hook_events':0,'complete_receipts':0,'last_at':0,'examples':[]})
        g['gateway_events' if x['kind']=='gw' else 'hook_events']+=1;g['complete_receipts']+=int(complete);g['last_at']=max(g['last_at'],x['at'])
        if len(g['examples'])<3:g['examples'].append(key)
    orphans=[{'action':canonical_action(x['tool']),'raw_tool':x['tool'],'events':x['n']} for x in con.execute('SELECT tool,count(*) n FROM lc_event WHERE work_id IS NULL AND tool IS NOT NULL GROUP BY tool')]
    con.close()
    return {'work_id':work_id,'event_count':len(rows),'complete_receipts':sum(x['complete'] for x in rows),'events':rows,'by_action':list(groups.values()),'unassigned_events':orphans,'count_rule':'gateway and hook observations are not added as unique calls; resolved is attribution, never success','coverage':'retained lc_event for selected work only; external platforms and expired history may be missing'}

def audit_vps(args, catalog):
    import types,collections
    policy=catalog['tool_registry']['audit_sources'];scanner=Path(policy['dot_catalog']['path'])
    scanner_bytes=scanner.read_bytes()
    if hashlib.sha256(scanner_bytes).hexdigest()!=policy['dot_catalog']['sha256']:raise ValueError('DOT_CATALOG_PIN_CHANGED')
    mod=types.ModuleType('existing_dot_catalog');mod.__file__=str(scanner)
    exec(compile(scanner_bytes,str(scanner),'exec'),mod.__dict__)  # exact pinned bytes; no .pyc cache read/write
    dots=[];support=[]
    for x in mod.scan(policy['dot_bin']):
        p=Path(policy['dot_bin'])/x['name']
        row={'id':'DOT.'+x['name'],'name':x['name'],'group':x['group'],'version':x['version'],'purpose':x['purpose'],'path':str(p),'sha256':sha(p),'state':'DISCOVERED_NOT_EXECUTION_VERIFIED','self_reported_mode':x['mode'],'self_reported_tier':x['tier'],'source':'dot-dot-catalog','verification':'source file exists; no command executed'}
        (support if x['name'].startswith('TEMPLATE-') else dots).append(row)
    scripts=[]
    for source in policy.get('additional_script_sources',[]):
        folder=Path(source['path'])
        if not folder.is_dir():raise ValueError('SCRIPT_SOURCE_UNAVAILABLE:'+str(folder))
        for x in mod.scan(str(folder)):
            p=folder/x['name']
            if not (p.suffix in ('.py','.sh') or p.name.startswith('dot-')):continue
            scripts.append({'id':source['namespace']+'.'+x['name'],'name':x['name'],'group':source['label'],'version':x['version'],'purpose':x['purpose'],'path':str(p),'sha256':sha(p),'state':'DISCOVERED_NOT_EXECUTION_VERIFIED','catalog_state':'OUTSIDE_DOT_INDEX_REVIEW','source':'dot-dot-catalog/info; declared additional script scope','verification':'source file exists; no command executed'})
    # Reuse the existing TSV index; detect newly discovered, missing and changed entries.
    import csv
    index_path=Path(policy.get('dot_index',str(Path(policy['dot_bin']).parent/'00-SO-DOT.tsv')))
    index_rows=list(csv.DictReader(index_path.open(),delimiter='\t'));indexed={x['name']:x for x in index_rows}
    if len(index_rows)!=len(indexed):raise ValueError('DUPLICATE_DOT_INDEX_NAME')
    current={x['name']:x for x in dots+support};unindexed=[];changed=[]
    for name,row in current.items():
        row['catalog_state']='INDEXED' if name in indexed else 'UNINDEXED_REUSABLE_CANDIDATE'
        if name not in indexed:unindexed.append(name)
        elif indexed[name]['sha12']!=row['sha256'][:12]:changed.append(name);row['catalog_state']='INDEX_HASH_CHANGED'
    hashes={};duplicates=[]
    for row in dots+scripts:
        if row['sha256'] in hashes:duplicates.append([hashes[row['sha256']],row['id']])
        else:hashes[row['sha256']]=row['id']
    index_check={'source':str(index_path),'sha256':sha(index_path),'unindexed':unindexed,'missing':sorted(set(indexed)-set(current)),'changed':changed,'duplicate_hash_candidates':duplicates,'state':'REVIEW' if unindexed or changed or set(indexed)-set(current) or duplicates else 'MATCHED','claim':'catalog/hash match only, not execution approval'}
    usage=usage_audit(Path(args.usage_db or policy['usage_db']),args.work_id,args.usage_event)
    if args.usage_event and not usage['events']:raise ValueError('EVENT_NOT_IN_SELECTED_WORK')
    registry={x['id']:x for x in catalog['tool_registry']['records']};providers={x['id'] for x in catalog['tool_registry'].get('provider_tools',[])}
    for x in usage['by_action']:x['registration']='PROVIDER_REGISTERED' if x['action'] in providers else 'UNMAPPED_OBSERVED_CAPABILITY'
    # execution_queued already stores the command hash and source commit, without raw argv.
    queued={};journal=Path(policy['audit_journal']);bad_lines=0
    if journal.exists():
        for line in journal.open():
            try:x=json.loads(line)
            except ValueError:bad_lines+=1;continue
            if x.get('event')=='execution_queued' and (x.get('cwd','')=='work/'+args.work_id or x.get('cwd','').startswith('work/'+args.work_id+'/')):queued[x['id']]=x
    import sqlite3
    con=sqlite3.connect('file:'+str(Path(args.usage_db or policy['usage_db']).resolve())+'?mode=ro',uri=True);con.row_factory=sqlite3.Row
    jobs=[]
    for key,x in queued.items():
        saved=con.execute('SELECT status,result FROM jobs WHERE id=?',(key,)).fetchone();result=json.loads(saved['result'] or '{}') if saved else {};stream=result.get('streams',{}).get('stdout',{})
        rec={'run_id':key,'work_id':args.work_id,'action':'agent-data:workspace_exec','invocation_sha256':x.get('argv_sha256'),'source_head':result.get('source_head') or x.get('source_head'),'outcome':('EXIT_'+str(result['exit_code'])) if result.get('exit_code') is not None else 'RESULT_UNAVAILABLE','status':saved['status'] if saved else 'EXPIRED','stdout_sha256':stream.get('sha256'),'evidence_ref':policy['jobs_dir']+'/'+key+'/stdout','subtools':[]}
        out=Path(rec['evidence_ref'])
        if stream.get('sha256') and not stream.get('protected') and out.is_file() and sha(out)==stream['sha256']:
            # Parse structured runner receipts only. Never publish arbitrary stdout/argv.
            try:
                report=json.loads(out.read_text())
                runner_receipt=runner_test_receipt(report,rec['evidence_ref'])
                if runner_receipt:rec['subtools'].append(runner_receipt)
                for item in report.get('results',[]):
                    if item.get('id') in registry and re.fullmatch('[0-9a-f]{64}',item.get('source_sha256','')):
                        rec['subtools'].append({'id':item['id'],'sha256':item['source_sha256'],'exit_code':item.get('exit_code'),'case_set':item.get('case_set'),'checked_at':report.get('at'),**({'ui_inputs':report.get('ui_inputs',{})} if item['id']=='TQT-CHECK-005' else {}),'evidence_ref':rec['evidence_ref']+'#results/'+item['id']})
            except (ValueError,AttributeError,TypeError):pass
        jobs.append(rec)
    con.close()
    return {'schema_version':1,'observed_at':datetime.now(timezone.utc).isoformat(),'scope':{'dot_bin':policy['dot_bin'],'work_id':args.work_id,'pg':'NOT_READ_OR_WRITTEN','claim':'inventory and observed use, not operational approval'},'scanner':policy['dot_catalog'],'dot_inventory':dots,'supporting_templates':support,'script_inventory':scripts,'dot_index_check':index_check,'usage':usage,'executions':jobs,'journal_invalid_lines':bad_lines,'gaps':['Historical events may lack source version or result; unknown is not PASS','Unassigned platform events are not attributed to this work','No claim to capture every external platform; import provider receipts explicitly','Discovered files require review and scoped verification before use']}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--audit-patch',type=Path,help='prepare a workspace_transaction JSON from an audit receipt; no source mutation')
    ap.add_argument('--audit-vps',action='store_true',help='read existing DOT catalog and usage ledger; no DOT execution or PG')
    ap.add_argument('--work-id',default='tools-quy-trinh')
    ap.add_argument('--usage-event',help='exact existing event key to inspect')
    ap.add_argument('--usage-db',help='operator path to existing SQLite ledger, read-only')
    ap.add_argument('--verify','--execute',action='store_true',dest='verify',help='run registered read-only suites')
    ap.add_argument('--dry-run',action='store_true',help='validate inventory and print commands without running suites')
    ap.add_argument('--report',type=Path,help='save evidence JSON; use a test/evidence location')
    ap.add_argument('--ui-adapter',type=Path,help='process-work-master-v1.js in a complete pinned UI input folder')
    ap.add_argument('--ui-snapshot',type=Path,help='offline folder with all five pinned UI inputs; default: evidence/ui-inputs beside this runner')
    ap.add_argument('--vps-ui',action='store_true',help='fetch all five public UI inputs, verify registry pins, and run the complete UI checks')
    ap.add_argument('--before-product',type=Path,help='actual previous product snapshot; validate revisions/history before submitting any write')
    ap.add_argument('--master-registry',type=Path,help='fresh definition-master-registry-v1.js from the UI source')
    ap.add_argument('--master-registry-json',help='equivalent observed registry rows, JSON; no canonical copy is created')
    ap.add_argument('--identity-only',action='store_true',help='run cross-registry identity guard using Python only; no Node/PG needed')
    args=ap.parse_args()
    source=BASE/'view.html';data=json.loads(re.search(r'<script id="tqt-composite-processes"[^>]*>(.*?)</script>',source.read_text(),re.S)[1])['catalog'];reg=data['tool_registry']
    admission=memory_admission(max((x.get('minimum_exec_memory_bytes',0) for x in reg['records']),default=0),observed_memory_limit())
    if args.verify and not args.dry_run and admission['state']=='BLOCKED':
        blocked={'status':'BLOCKED','results':[],'resource_admission':admission,'pg':'NOT_RUN','production_ready':False}
        if args.report:args.report.write_text(json.dumps(blocked,ensure_ascii=False,indent=2)+'\n')
        print(json.dumps(blocked));return 3
    if args.audit_patch:
        try: patch=audit_patch(json.loads(args.audit_patch.read_text()))
        except (OSError,ValueError,KeyError) as error:print(json.dumps({'state':'BLOCKED','error':str(error)}));return 3
        if args.report:args.report.write_text(json.dumps(patch,ensure_ascii=False)+'\n')
        print(json.dumps({'state':'PATCH_READY_NOT_APPLIED','operations':len(patch['operations']),'apply_with':'workspace_transaction','pg':'NOT_RUN'}));return 0
    if args.audit_vps:
        try: result=audit_vps(args,data)
        except (OSError,ValueError,KeyError,sqlite3.Error) as error:
            print(json.dumps({'state':'BLOCKED','error':str(error)}));return 3
        if args.report:args.report.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
        print(json.dumps({'state':'OBSERVED','dot_files':len(result['dot_inventory']),'other_scripts':len(result.get('script_inventory',[])),'supporting_templates':len(result['supporting_templates']),'usage_events':result['usage']['event_count'],'complete_receipts':result['usage']['complete_receipts'],'execution_receipts':len(result['executions']),'pg':'NOT_RUN'}));return 0
    fetch_errors=[];ui_temp=None;preflight=None;input_mode=None
    if args.master_registry_json and args.verify and not args.dry_run and not args.identity_only:ap.error('--master-registry-json is for --identity-only; complete verification requires five pinned UI files')
    if not (args.ui_snapshot or args.vps_ui or args.ui_adapter or args.master_registry or args.master_registry_json):
        args.ui_snapshot=BASE/UI_FIXTURE_DIRECTORY;input_mode='REPO_PINNED_FIXTURES'
    if args.ui_snapshot:
        if args.vps_ui or args.ui_adapter or args.master_registry or args.master_registry_json:ap.error('--ui-snapshot is a complete input mode')
        preflight=ui_input_preflight(args.ui_snapshot,reg);fetch_errors.extend(preflight['errors'])
        input_mode=input_mode or 'EXPLICIT_PINNED_SNAPSHOT'
        args.master_registry=args.ui_snapshot/'definition-master-registry-v1.js';args.ui_adapter=args.ui_snapshot/'process-work-master-v1.js'
    elif args.vps_ui:
        if args.ui_adapter or args.master_registry or args.master_registry_json:ap.error('--vps-ui supplies the UI adapter and registry; do not combine input modes')
        ui_temp=tempfile.TemporaryDirectory(prefix='TQT-UI-TEST-');folder=Path(ui_temp.name)
        pins,pin_errors=ui_input_pins(reg);fetch_errors.extend(pin_errors);input_mode='EXPLICIT_PUBLIC_UI_FETCH'
        if not pin_errors:
            for name,pin in pins.items():
                try:
                    raw=urllib.request.urlopen('https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/'+name,timeout=10).read()
                    if hashlib.sha256(raw).hexdigest()!=pin:fetch_errors.append('UI_INPUT_CHANGED:'+name);continue
                    (folder/name).write_bytes(raw)
                except (OSError,ValueError) as exc:fetch_errors.append('UI_INPUT_UNAVAILABLE:'+name+':'+type(exc).__name__)
            if not fetch_errors:preflight=ui_input_preflight(folder,reg);fetch_errors.extend(preflight['errors'])
        args.master_registry=folder/'definition-master-registry-v1.js';args.ui_adapter=folder/'process-work-master-v1.js'
    elif args.ui_adapter or (args.master_registry and not args.identity_only):
        if args.master_registry_json:ap.error('do not combine file UI inputs with --master-registry-json')
        folder=(args.ui_adapter or args.master_registry).parent
        if args.ui_adapter and args.ui_adapter.name!='process-work-master-v1.js':ap.error('--ui-adapter must name process-work-master-v1.js')
        if args.master_registry and (args.master_registry.name!='definition-master-registry-v1.js' or args.master_registry.parent.resolve()!=folder.resolve()):ap.error('--master-registry must be in the same complete UI input folder')
        preflight=ui_input_preflight(folder,reg);fetch_errors.extend(preflight['errors']);input_mode='EXPLICIT_PINNED_FILES'
        args.ui_adapter=folder/'process-work-master-v1.js';args.master_registry=folder/'definition-master-registry-v1.js'
    if fetch_errors:
        # Fail before scanning executables, comparing the large product or running tests.
        blocked={'status':'BLOCKED','results':[],'inventory_errors':[],'prerequisite_errors':fetch_errors,'ui_input_mode':input_mode,'ui_input_preflight':preflight,'source_sha256':sha(source),'runner_sha256':sha(BASE/'run-tqt-checks.py'),'pg':'NOT_RUN','production_ready':False}
        if args.report:args.report.parent.mkdir(parents=True,exist_ok=True);args.report.write_text(json.dumps(blocked,ensure_ascii=False,indent=2)+'\n')
        print(json.dumps(blocked,ensure_ascii=False))
        if ui_temp:ui_temp.cleanup()
        return 3
    identity={'state':'BLOCKED','errors':['MISSING_LIVE_MASTER_REGISTRY']}
    if args.master_registry or args.master_registry_json:
        try:
            observed=json.loads(args.master_registry_json) if args.master_registry_json else json.loads(re.search(r'DEFINITION_MASTER_REGISTRY=(\[.*?\]);',args.master_registry.read_text(),re.S)[1])
            identity=master_identity_audit(data,observed)
            identity['input_sha256']=hashlib.sha256(json.dumps(observed,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()
            identity['self_test']=identity_self_test()
        except (ValueError, KeyError, TypeError, OSError) as exc:identity={'state':'FAIL','errors':['INVALID_MASTER_REGISTRY:'+str(exc)]}
    if args.identity_only:
        result={'status':identity['state'],'master_identity_check':identity,'pg':'NOT_RUN'}
        if args.report:args.report.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
        print(json.dumps(result,ensure_ascii=False));return 0 if identity['state']=='PASS' else 3 if identity['state']=='BLOCKED' else 1
    errors=inventory(BASE,reg)
    readback=source_readback(BASE.parent/'mow-mot-moit-mout'/'UI-REVIEW-MOW001.json',data['application_preview']['record'])
    if readback['state']!='PASS': errors.append('SOURCE_READBACK_FAILED')
    report={'run_id':'TQT-'+uuid.uuid4().hex,'at':datetime.now(timezone.utc).isoformat(),'scope':reg['scope'],'registry_master':'CAT-006','case_master':'CAT-012','result_master':'CAT-015','source_sha256':sha(source),'runner_sha256':sha(BASE/'run-tqt-checks.py'),'inventory_errors':errors,'source_readback':readback,'results':[],'pg':'NOT_RUN','production_ready':False}
    report['resource_admission']=admission
    report['ui_input_mode']=input_mode
    report['ui_input_preflight']=preflight
    report['master_identity_check']=identity
    if identity['state']=='FAIL':errors.append('MASTER_IDENTITY_CONFLICT')
    report['prerequisite_errors']=prerequisites()
    report['prerequisite_errors'].extend(fetch_errors)
    if args.ui_adapter:
        inputs=[args.ui_adapter]
        if args.master_registry:
            inputs.extend(args.ui_adapter.parent/n for n in ('ui-child-content-v1.js','ui-child-from-parent-v1.js','qtth006-overview-v1.js'))
            inputs.append(args.master_registry)
        report['ui_inputs']={}
        for path in inputs:
            if path.is_file():report['ui_inputs'][path.name]=sha(path)
            else:report['prerequisite_errors'].append('MISSING_UI_INPUT:'+path.name)
        if args.ui_adapter.is_file():report['ui_adapter_sha256']=sha(args.ui_adapter)
    if identity['state']=='BLOCKED':report['prerequisite_errors'].append('MISSING_LIVE_MASTER_REGISTRY')
    if args.before_product and not report['prerequisite_errors']:
        product=BASE.parent/'mow-mot-moit-mout'/'UI-REVIEW-MOW001.json'
        proc=subprocess.run(['node',str(BASE/'check-record-control.js'),str(source),'--validate-transition',str(args.before_product.resolve()),str(product)],text=True,capture_output=True,timeout=60)
        try: report['transition_check']=json.loads(proc.stdout)
        except ValueError: report['transition_check']={'state':'FAIL','errors':[proc.stderr or 'INVALID_VALIDATOR_OUTPUT']}
        report['transition_check'].update(before_sha256=sha(args.before_product),after_sha256=sha(product))
        if proc.returncode or report['transition_check']['state']!='PASS':errors.append('INVALID_TRANSITION')
    elif args.before_product:
        report['transition_check']={'state':'BLOCKED','reason':'MISSING_RUNTIME'}
    if not errors and not report['prerequisite_errors'] and args.verify and not args.dry_run:
        report['ui_input_self_test']=ui_input_self_test()
        report['runner_self_test']=self_test()
        report['usage_audit_self_test']=audit_self_test(data['tool_registry']['audit_sources'])
        projection=data['tool_registry'].get('audit_projection')
        if projection:
            evidence=json.loads((BASE/'UI-REVIEW-AGGREGATE.json').read_text())['host_review_P33']
            if projection!=audit_projection(evidence['audit'],evidence.get('external_receipts',[])):report['inventory_errors'].append('AUDIT_PROJECTION_DRIFT')
    # The complete real source has already been compared above; child suites reopen
    # it themselves. Release the parent's duplicate before their memory is admitted.
    del data
    import gc
    gc.collect()
    if not errors and not report['prerequisite_errors'] and args.verify and not args.dry_run:
        for x in reg['records']:
            if x['kind']=='RUNNER':continue
            argv=list(x['argv'])
            if x['id']=='TQT-CHECK-005' and args.ui_adapter:
                argv.append(str(args.ui_adapter.resolve()))
                if args.master_registry:argv.append(str(args.master_registry.resolve()))
            started=time.monotonic()
            try:
                proc=subprocess.run(argv,cwd=BASE,text=True,capture_output=True,timeout=x['timeout_seconds'])
                result={'id':x['id'],'case_set':x['case_set'],'source_sha256':x['sha256'],'argv':argv,'exit_code':proc.returncode,'stdout':proc.stdout,'stderr':proc.stderr}
            except (OSError,subprocess.TimeoutExpired) as exc: result={'id':x['id'],'exit_code':1,'error':str(exc)}
            result.update(elapsed_seconds=round(time.monotonic()-started,3),timeout_seconds=x['timeout_seconds'])
            report['results'].append(result)
    report['status']='FAIL' if errors or any(x['exit_code'] for x in report['results']) else 'BLOCKED' if report['prerequisite_errors'] else 'PASS' if args.verify and not args.dry_run else 'DRY_RUN'
    if report['status']=='DRY_RUN':report['commands']=[x['argv'] for x in reg['records'] if x['kind']!='RUNNER']
    if args.report:
        args.report.parent.mkdir(parents=True,exist_ok=True);args.report.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(report,ensure_ascii=False))
    if ui_temp:ui_temp.cleanup()
    return 1 if report['status']=='FAIL' else 3 if report['status']=='BLOCKED' else 0
if __name__=='__main__':sys.exit(main())
