"""Managed read-only test runner. Registry: view.html catalog.tool_registry (CAT-006).
No credentials, network, PG, service changes or production mutation. Exit 0 PASS,
1 failed test/inventory, 2 invalid invocation, 3 blocked by missing prerequisites. Default dry-run; --verify executes.
"""
import argparse, hashlib, json, re, subprocess, sys, shutil, tempfile, uuid
from datetime import datetime, timezone
from pathlib import Path

BASE = Path(__file__).resolve().parent
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def inventory(base, registry):
    errors = []
    records = registry['records']
    paths = [x['path'] for x in records]
    if len(set(paths)) != len(paths) or len({x['id'] for x in records}) != len(records): errors.append('DUPLICATE')
    # Scope is explicit: all executable Python/JS sources in this task, including future subfolders.
    actual = {str(p.relative_to(base)) for p in base.rglob('*') if p.is_file() and p.suffix in {'.py', '.js'}}
    for p in sorted(actual - set(paths)): errors.append('UNREGISTERED:'+p)
    for x in records:
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
        row.update(id='TEST',path='check.py',sha256=sha(p));reg={'records':[row]}
        assert inventory(b,reg)==[]
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
    return {'cases':13,'store':'temporary TEST file in execution snapshot','write_read_restore':'PASS','production':'NOT_TOUCHED'}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--verify','--execute',action='store_true',dest='verify',help='run registered read-only suites')
    ap.add_argument('--dry-run',action='store_true',help='validate inventory and print commands without running suites')
    ap.add_argument('--report',type=Path,help='save evidence JSON; use a test/evidence location')
    ap.add_argument('--ui-adapter',type=Path,help='optional local copy of VPS process-work-master-v1.js; hash recorded')
    ap.add_argument('--before-product',type=Path,help='actual previous product snapshot; validate revisions/history before submitting any write')
    args=ap.parse_args()
    source=BASE/'view.html';data=json.loads(re.search(r'<script id="tqt-composite-processes"[^>]*>(.*?)</script>',source.read_text(),re.S)[1])['catalog'];reg=data['tool_registry']
    errors=inventory(BASE,reg)
    readback=source_readback(BASE.parent/'mow-mot-moit-mout'/'UI-REVIEW-MOW001.json',data['application_preview']['record'])
    if readback['state']!='PASS': errors.append('SOURCE_READBACK_FAILED')
    report={'run_id':'TQT-'+uuid.uuid4().hex,'at':datetime.now(timezone.utc).isoformat(),'scope':reg['scope'],'registry_master':'CAT-006','case_master':'CAT-012','result_master':'CAT-015','source_sha256':sha(source),'inventory_errors':errors,'source_readback':readback,'results':[],'pg':'NOT_RUN','production_ready':False}
    if args.ui_adapter: report['ui_adapter_sha256']=sha(args.ui_adapter)
    report['prerequisite_errors']=prerequisites()
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
            if x['id']=='TQT-CHECK-005' and args.ui_adapter:argv.append(str(args.ui_adapter.resolve()))
            try:
                proc=subprocess.run(argv,cwd=BASE,text=True,capture_output=True,timeout=60)
                result={'id':x['id'],'case_set':x['case_set'],'source_sha256':x['sha256'],'argv':argv,'exit_code':proc.returncode,'stdout':proc.stdout,'stderr':proc.stderr}
            except (OSError,subprocess.TimeoutExpired) as exc: result={'id':x['id'],'exit_code':1,'error':str(exc)}
            report['results'].append(result)
    report['status']='FAIL' if errors or any(x['exit_code'] for x in report['results']) else 'BLOCKED' if report['prerequisite_errors'] else 'PASS' if args.verify and not args.dry_run else 'DRY_RUN'
    if report['status']=='DRY_RUN':report['commands']=[x['argv'] for x in reg['records'] if x['kind']!='RUNNER']
    if args.report:
        args.report.parent.mkdir(parents=True,exist_ok=True);args.report.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(report,ensure_ascii=False))
    return 1 if report['status']=='FAIL' else 3 if report['status']=='BLOCKED' else 0
if __name__=='__main__':sys.exit(main())
