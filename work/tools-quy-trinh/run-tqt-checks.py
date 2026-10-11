"""Managed read-only test runner. Registry: view.html catalog.tool_registry (CAT-006).
No credentials, network, PG, service changes or production mutation. Exit 0 PASS,
1 failed test/inventory, 2 invalid invocation. Default dry-run; --verify executes.
"""
import argparse, hashlib, json, re, subprocess, sys, tempfile, uuid
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
    return {'cases':7,'store':'temporary TEST file in execution snapshot','write_read_restore':'PASS','production':'NOT_TOUCHED'}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--verify','--execute',action='store_true',dest='verify',help='run registered read-only suites')
    ap.add_argument('--dry-run',action='store_true',help='validate inventory and print commands without running suites')
    ap.add_argument('--report',type=Path,help='save evidence JSON; use a test/evidence location')
    ap.add_argument('--ui-adapter',type=Path,help='optional local copy of VPS process-work-master-v1.js; hash recorded')
    args=ap.parse_args()
    source=BASE/'view.html';data=json.loads(re.search(r'<script id="tqt-composite-processes"[^>]*>(.*?)</script>',source.read_text(),re.S)[1])['catalog'];reg=data['tool_registry']
    errors=inventory(BASE,reg)
    if not (BASE.parent/'mow-mot-moit-mout'/'UI-REVIEW-MOW001.json').is_file(): errors.append('MISSING_PRODUCT_SOURCE')
    report={'run_id':'TQT-'+uuid.uuid4().hex,'at':datetime.now(timezone.utc).isoformat(),'scope':reg['scope'],'registry_master':'CAT-006','case_master':'CAT-012','result_master':'CAT-015','source_sha256':sha(source),'inventory_errors':errors,'results':[],'pg':'NOT_RUN','production_ready':False}
    if args.ui_adapter: report['ui_adapter_sha256']=sha(args.ui_adapter)
    if not errors and args.verify and not args.dry_run:
        report['runner_self_test']=self_test()
        for x in reg['records']:
            if x['kind']=='RUNNER':continue
            argv=list(x['argv'])
            if x['id']=='TQT-CHECK-005' and args.ui_adapter:argv.append(str(args.ui_adapter.resolve()))
            try:
                proc=subprocess.run(argv,cwd=BASE,text=True,capture_output=True,timeout=60)
                result={'id':x['id'],'case_set':x['case_set'],'source_sha256':x['sha256'],'argv':argv,'exit_code':proc.returncode,'stdout':proc.stdout,'stderr':proc.stderr}
            except (OSError,subprocess.TimeoutExpired) as exc: result={'id':x['id'],'exit_code':1,'error':str(exc)}
            report['results'].append(result)
    report['status']='FAIL' if errors or any(x['exit_code'] for x in report['results']) else 'PASS' if args.verify and not args.dry_run else 'DRY_RUN'
    if report['status']=='DRY_RUN':report['commands']=[x['argv'] for x in reg['records'] if x['kind']!='RUNNER']
    if args.report:
        args.report.parent.mkdir(parents=True,exist_ok=True);args.report.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(report,ensure_ascii=False))
    return 1 if report['status']=='FAIL' else 0
if __name__=='__main__':sys.exit(main())
