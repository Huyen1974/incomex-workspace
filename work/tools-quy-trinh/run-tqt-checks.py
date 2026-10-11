"""Managed read-only test runner. Registry: view.html catalog.tool_registry (CAT-006).
No credentials, PG, service changes or production mutation. --vps-ui reads pinned public UI inputs. Exit 0 PASS,
1 failed test/inventory, 2 invalid invocation, 3 blocked by missing prerequisites. Default dry-run; --verify executes.
"""
import argparse, hashlib, json, re, subprocess, sys, shutil, tempfile, uuid, unicodedata, time, math
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

BASE = Path(__file__).resolve().parent
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
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
    actual = {str(p.relative_to(base)) for p in base.rglob('*') if p.is_file() and p.suffix in {'.py', '.js'}}
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

def self_test():
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

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--verify','--execute',action='store_true',dest='verify',help='run registered read-only suites')
    ap.add_argument('--dry-run',action='store_true',help='validate inventory and print commands without running suites')
    ap.add_argument('--report',type=Path,help='save evidence JSON; use a test/evidence location')
    ap.add_argument('--ui-adapter',type=Path,help='optional local copy of VPS process-work-master-v1.js; hash recorded')
    ap.add_argument('--vps-ui',action='store_true',help='fetch all four public UI inputs, verify registry pins, and run the complete UI checks')
    ap.add_argument('--before-product',type=Path,help='actual previous product snapshot; validate revisions/history before submitting any write')
    ap.add_argument('--master-registry',type=Path,help='fresh definition-master-registry-v1.js from the UI source')
    ap.add_argument('--master-registry-json',help='equivalent observed registry rows, JSON; no canonical copy is created')
    ap.add_argument('--identity-only',action='store_true',help='run cross-registry identity guard using Python only; no Node/PG needed')
    args=ap.parse_args()
    source=BASE/'view.html';data=json.loads(re.search(r'<script id="tqt-composite-processes"[^>]*>(.*?)</script>',source.read_text(),re.S)[1])['catalog'];reg=data['tool_registry']
    fetch_errors=[];ui_temp=None
    if args.vps_ui:
        if args.ui_adapter or args.master_registry or args.master_registry_json:ap.error('--vps-ui supplies the UI adapter and registry; do not combine input modes')
        ui_temp=tempfile.TemporaryDirectory(prefix='TQT-UI-TEST-');folder=Path(ui_temp.name)
        pins=next(x for x in reg['records'] if x['id']=='TQT-CHECK-005').get('ui_inputs',{})
        required={'definition-master-registry-v1.js','process-work-master-v1.js','ui-child-content-v1.js','ui-child-from-parent-v1.js'}
        if set(pins)!=required:fetch_errors.append('INVALID_UI_INPUT_INVENTORY')
        else:
            for name,pin in pins.items():
                try:
                    raw=urllib.request.urlopen('https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/'+name,timeout=30).read()
                    if hashlib.sha256(raw).hexdigest()!=pin:fetch_errors.append('UI_INPUT_CHANGED:'+name);continue
                    (folder/name).write_bytes(raw)
                except (OSError,ValueError) as exc:fetch_errors.append('UI_INPUT_UNAVAILABLE:'+name+':'+type(exc).__name__)
        args.master_registry=folder/'definition-master-registry-v1.js';args.ui_adapter=folder/'process-work-master-v1.js'
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
    report={'run_id':'TQT-'+uuid.uuid4().hex,'at':datetime.now(timezone.utc).isoformat(),'scope':reg['scope'],'registry_master':'CAT-006','case_master':'CAT-012','result_master':'CAT-015','source_sha256':sha(source),'inventory_errors':errors,'source_readback':readback,'results':[],'pg':'NOT_RUN','production_ready':False}
    report['master_identity_check']=identity
    if identity['state']=='FAIL':errors.append('MASTER_IDENTITY_CONFLICT')
    report['prerequisite_errors']=prerequisites()
    report['prerequisite_errors'].extend(fetch_errors)
    if args.ui_adapter:
        inputs=[args.ui_adapter]
        if args.master_registry:
            inputs.extend(args.ui_adapter.parent/n for n in ('ui-child-content-v1.js','ui-child-from-parent-v1.js'))
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
    if not errors and args.verify and not args.dry_run:
        report['runner_self_test']=self_test()
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
