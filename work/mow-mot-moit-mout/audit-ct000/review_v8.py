#!/usr/bin/env python3
"""Bounded CT-000 review of P77: reuse v7 harness and the registered subject.
Read-only for the workflow/checker; no PG/Flow/network/full graph search.
Exit 0: scoped probes passed; 1: findings; 2: unsupported inputs/runner error.
All findings distinguish model behavior from unverified input-adapter contracts.
"""
from __future__ import annotations
import argparse
import array
import contextlib
import copy
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import sys
import tempfile

HTML_SHA = 'b6d0b578b96a657afd032f35a1d049e0d1a4835e9acf7d011965ee8c069feb2f'
# Reviewed delta 5b8992a6 -> 42e10dbe: --kb exact-name/semicolon parsing only.
CHECKER_SHA = 'ca803b26740565ac5f625979b1535566a97306b306f895006c2bee57528c2c3f'
V7_SHA = '2d1459f4c67433845e8b4fd81deeeff4321fee1eca16aab10e5094c415175655'
START = [('khai xong', {}), ('chấm', {}), ('chấm', {}), ('xin nhận', {})]
VISIBLE = ['st', 'thế_hệ', 'gen_giữ', 'giữ_chỗ', 'lần_nhận', 'M', 'N', 'MB',
           'lần_gia_hạn', 'hết_hạn_giữ', 'g1', 'g2', 'q1', 'q2', 'chờ_duyệt',
           'g5', 'chờ_nhận', 'đã_làm', 'tổng_làm', 'đang_bay', 'kết_luận',
           'bù_bay', 'đã_bù', 'lần_bù', 'cờ_huỷ', 'quá_hạn_gốc', 'quá_hạn_PH']

def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()

def load(p: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, p)
    if spec is None or spec.loader is None:
        raise RuntimeError(f'Cannot import {p}')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

def state(s):
    return {k: s.get(k) for k in VISIBLE}

class Walk:
    """Reuse v7 Trace. Never fill missing result/human/owner credentials."""
    def __init__(self, previous, mod, model, initial=None):
        self.t = previous.Trace(mod, model, initial)
        self.events = []

    @property
    def s(self):
        return self.t.state

    def step(self, event, payload=None):
        payload = {} if payload is None else dict(payload)
        before = state(self.s)
        try:
            error = self.t.step(event, payload)
            exception = None
        except Exception as exc:
            error = None
            exception = f'{type(exc).__name__}: {exc}'
        last = self.t.events[-1] if self.t.events else {}
        result = {'event': event, 'payload': payload, 'before': before,
                  'after': state(self.s), 'error': error, 'exception': exception,
                  'transition': last.get('transition') if not exception else None}
        self.events.append(result)
        return result

    def steps(self, events):
        for event, payload in events:
            r = self.step(event, payload)
            if r['exception'] or r['error']:
                raise RuntimeError(f'Unexpected setup failure: {r}')
        return self

    def evidence(self):
        return {'trace': self.events, 'final': state(self.s),
                'subject_invariant_violations': self.t.violations}

def suite(mod, tables, model, previous):
    regressions, probes = [], []
    valid = dict(mod.TRA_LOI_DUNG)
    invalid = dict(valid, ý=None)
    def walk(initial=None):
        return Walk(previous, mod, model, initial)
    def note(code, title, passed, evidence, regression=False, kind='MODEL_COUNTEREXAMPLE'):
        dst = regressions if regression else probes
        dst.append({'id': code, 'title': title, 'kind': kind,
                    'status': 'PASS' if passed else 'FINDING', 'evidence': evidence})
    def finish_work(w):
        return w.steps([('làm thao tác', {}), ('bên nhận làm', {}),
                        ('kết quả', {'mã': 'OK', 'tác_nhân': w.s['gen_giữ']})])
    def replacement():
        w = walk().steps(START)
        old = w.s['gen_giữ']
        w.steps([('qua hạn giữ', {}), ('hết hạn giữ', {}), ('xin nhận', {})])
        return w, old

    # Independently re-test the six previously reported groups, adjusted for the
    # new input contract, rather than merely changing the source hash.
    w, old = replacement(); before = state(w.s)
    r = w.step('kết quả', {'mã': 'FAILED_PRECONDITION', 'tác_nhân': old})
    note('R01', 'Old-generation result cannot change current attempt',
         r['exception'] is None and state(w.s) == before, w.evidence(), True)
    w, old = replacement(); before = state(w.s)
    r = w.step('gia hạn', {'tác_nhân': old})
    note('R02', 'Old-generation heartbeat is rejected',
         r['exception'] is None and state(w.s) == before, w.evidence(), True)
    w = walk({'g1': 'thiếu'}).steps([('khai xong', {}), ('chấm', {})])
    r = w.step('trả lời', invalid)
    note('R03', 'Normalized empty G1 reply cannot satisfy gate',
         not r['exception'] and w.s['st'] == 'Chờ người·G1' and w.s['g1'] == 'thiếu',
         w.evidence(), True)
    for code, config, label, stages in [('R04', {'chờ_duyệt': True}, 'G4', 1),
                                         ('R05', {'chờ_nhận': True}, 'G5', 2)]:
        w = finish_work(walk(config).steps(START))
        w.steps([('chấm', {})] * stages)
        r = w.step('trả lời', invalid)
        note(code, f'Normalized empty {label} reply cannot open gate',
             not r['exception'] and w.s['st'] == f'Chờ người·{label}', w.evidence(), True)
    codes = list(mod.CODES)
    outcomes = []
    for code in codes:
        w = walk().steps(START)
        r = w.step('kết quả', {'mã': code, 'tác_nhân': w.s['gen_giữ']})
        outcomes.append({'code': code, 'error': r['error'], 'exception': r['exception'],
                         'transition': r['transition'], 'after': w.s['st']})
    note('R06', 'Declared gRPC/local/unknown/None values all have a route',
         all(not x['error'] and not x['exception'] for x in outcomes), outcomes, True,
         'INPUT_DOMAIN_REGRESSION')
    saved_ev = mod.ev_
    def fault(code, ns):
        if getattr(code, 'co_filename', '') == 'B1':
            raise RuntimeError('V8_INDEPENDENT_EVALUATOR_FAULT')
        return saved_ev(code, ns)
    try:
        mod.ev_ = fault
        classification = mod.phan_loai(tables)
    finally:
        mod.ev_ = saved_ev
    note('R07', 'Unchanged model with independent evaluator fault is CHECKER_ERROR',
         classification[0] == 'CHECKER_ERROR', classification, True, 'CHECKER_SELF_TEST')
    a = dict(mod.MAC_DINH, **mod.AN, st='Chấm G2')
    b = dict(a, st='Kết thúc·Đạt')
    edges = (array.array('i', [0, 0]), array.array('i', [0, 1]), array.array('b', [0, 0]))
    errors = mod.song([mod.dong(a), mod.dong(b)], edges, model)
    note('R08', 'Immediate-state self-loop is detected using current model metadata',
         any('tự lặp' in str(e) for e in errors), errors, True, 'CHECKER_SELF_TEST')

    saved = {k: getattr(mod, k) for k in ('MASTER_TOOL', 'BO_CONG_CU', 'THU_MUC_VIEC')}
    with tempfile.TemporaryDirectory(prefix='ct000-v8-registry-') as d:
        root = Path(d); history = []; tools = {}
        for i, tid in enumerate(saved['BO_CONG_CU']):
            p = root / f'tool{i}.py'; p.write_text('# fixture only\n')
            tools[tid] = str(p)
            history.append({'id': tid, 'path': str(p), 'sha256': sha(p), 'tool_id': tid})
        master = root/'master.html'
        data = {'catalog': {'tool_registry': {'provider_tools': [], 'memory': []}}, 'archive': history}
        master.write_text('<script id="tqt-composite-processes" type="application/json">' +
                          json.dumps(data) + '</script>')
        try:
            mod.MASTER_TOOL = str(master); mod.BO_CONG_CU = tools; mod.THU_MUC_VIEC = []
            with contextlib.redirect_stdout(io.StringIO()):
                errors = mod.kiem_ke()
            note('R09', 'Archival lookalikes cannot replace live registry entries',
                 bool(errors), errors, True, 'REGISTRY_NEGATIVE_FIXTURE')
        finally:
            for k,v in saved.items(): setattr(mod,k,v)

    # New boundary: absence is not the same as a supplied invalid token.
    w, old = replacement(); before = state(w.s)
    r = w.step('kết quả', {'mã': 'FAILED_PRECONDITION'})
    note('V8-01', 'Missing generation is silently treated as current on a result',
         state(w.s) == before, dict(w.evidence(), original_old_generation=old),
         kind='INPUT_CONTRACT_GAP')
    w, old = replacement(); before = state(w.s)
    r = w.step('gia hạn', {})
    note('V8-02', 'Missing generation renews the current attempt', state(w.s) == before,
         w.evidence(), kind='INPUT_CONTRACT_GAP')
    for code, event, payload, initial, setup in [
        ('V8-03', 'trả lời', {}, {'g1':'thiếu'}, [('khai xong',{}),('chấm',{})]),
        ('V8-04', 'kết quả', {}, {}, START)]:
        w = walk(initial).steps(setup)
        if event == 'kết quả': payload = {'tác_nhân': w.s['gen_giữ']}
        before = state(w.s); r = w.step(event, payload)
        note(code, f'Truly omitted fields in {event} have no handled validation route',
             not r['exception'] and not r['error'], w.evidence(), kind='INPUT_CONTRACT_GAP')

    # G3 human completion is a different event from G1/G4/G5 "trả lời".
    w = walk().steps(START)
    w.step('kết quả', {'mã':'HUMAN', 'tác_nhân':w.s['gen_giữ']})
    r = w.step('kết quả', {'mã':'OK', 'người_đúng':False, 'phiên_đúng':False,
                          'tác_nhân':w.s['gen_giữ']})
    if not r['exception'] and w.s['st'] == 'Chấm G4':
        w.steps([('chấm',{}),('chấm',{})])
    note('V8-05', 'Wrong-person/wrong-version G3 completion can close the work',
         w.s['st'] not in ('Chấm G4','Chấm G5','Kết thúc·Đạt'), w.evidence(),
         kind='INPUT_CONTRACT_GAP')

    # Owner decisions must verify identity/version and explicit new limits, too.
    w = walk().steps(START + [('qua hạn gốc',{}),('qua hạn giữ',{}),
                             ('hết hạn giữ',{}),('xin nhận',{}),('quá hạn',{})])
    before = state(w.s)
    r = w.step('quyết định', {'quyết':'làm tiếp','người_đúng':False,'phiên_đúng':False})
    note('V8-06', 'Wrong-person/wrong-version decision grants extra limits',
         state(w.s) == before, w.evidence(), kind='INPUT_CONTRACT_GAP')

    # Full reachable path: compensation completed just before lease reclaim.
    w = finish_work(walk({'MB':1}).steps(START))
    w.steps([('yêu cầu huỷ',{}),('xét',{}),('bắt đầu',{}),('bù làm',{}),
             ('qua hạn giữ',{}),('hết hạn giữ',{}),('bắt đầu',{})])
    note('V8-07', 'Completed final compensation is escalated as exhausted instead of closed',
         w.s['st'] == 'Kết thúc·Huỷ', w.evidence())

    # Ensure registry reuse really accounts for children in the artifact folder.
    saved = {k:getattr(mod,k) for k in ('MASTER_TOOL','BO_CONG_CU','THU_MUC_VIEC')}
    with tempfile.TemporaryDirectory(prefix='ct000-v8-manifest-') as d:
        root=Path(d); scoped=root/'work'; scoped.mkdir(); bundle=scoped/'audit-ct000'; bundle.mkdir()
        tool=bundle/'run.py'; tool.write_text('# declared tool\n')
        orphan=bundle/'unlisted_probe.py'; orphan.write_text('# fixture: omitted from manifest\n')
        mf=bundle/'manifest.json'; mf.write_text(json.dumps({'files':[{'path':'run.py','sha256':sha(tool)}]}))
        tid='python:ct000-audit'; master=root/'master.html'
        reg={'provider_tools':[{'id':tid,'path':str(tool),'sha256':sha(tool),
                                'manifest':str(mf),'manifest_sha256':sha(mf)}],
             'memory':[{'tool_id':tid}]}
        master.write_text('<script id="tqt-composite-processes" type="application/json">'+
                          json.dumps({'catalog':{'tool_registry':reg}})+'</script>')
        try:
            mod.MASTER_TOOL=str(master);mod.BO_CONG_CU={tid:str(tool)};mod.THU_MUC_VIEC=[str(scoped)]
            log=io.StringIO()
            with contextlib.redirect_stdout(log): errors=mod.kiem_ke()
            note('V8-08','Unlisted runnable artifact under audit-ct000 is skipped by inventory',
                 bool(errors), {'fixture_unlisted':str(orphan),'errors':errors,'stdout':log.getvalue()},
                 kind='REGISTRY_NEGATIVE_FIXTURE')
        finally:
            for k,v in saved.items():setattr(mod,k,v)

    # Positive controls: do not turn a rejection-only suite into a false solution.
    controls=[]
    w=walk().steps(START);w.step('gia hạn',{'tác_nhân':w.s['gen_giữ']})
    controls.append({'name':'current heartbeat works','pass':w.s['lần_gia_hạn']==1})
    w=finish_work(walk({'chờ_duyệt':True}).steps(START));w.steps([('chấm',{}),('trả lời',valid),('chấm',{}),('chấm',{})])
    controls.append({'name':'valid approval closes work','pass':w.s['st']=='Kết thúc·Đạt'})
    w=finish_work(walk({'chờ_nhận':True}).steps(START));w.steps([('chấm',{}),('chấm',{}),('trả lời',valid),('chấm',{})])
    controls.append({'name':'valid handover closes work','pass':w.s['st']=='Kết thúc·Đạt'})
    w=finish_work(walk({'MB':1}).steps(START));w.steps([('yêu cầu huỷ',{}),('xét',{}),('bắt đầu',{}),('bù làm',{}),('bù',{})])
    controls.append({'name':'completed compensation normally closes','pass':w.s['st']=='Kết thúc·Huỷ'})
    return regressions,probes,controls

def main(argv=None):
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--out',type=Path,default=Path('/tmp/ct000-audit-v8-results'))
    p.add_argument('--pack-report',action='store_true')
    args=p.parse_args(argv)
    project=Path(__file__).resolve().parent.parent
    source=project/'ban-duyet.html'; checker=project/'kiem-ct000-4.py'; prev=project/'audit-ct000/review_v7.py'
    report={'revision':'CT000-AUDIT-V8-20261022','scope':'P77 bounded regressions, adversarial input and race probes; no PG/Flow, no full graph sweep',
            'integration_status':'NOT_EXECUTED','full_sweep_status':'NOT_EXECUTED','findings':[]}
    rc=2
    try:
        paths={'html':source,'checker':checker,'reused_v7':prev}
        hashes={k:sha(v) for k,v in paths.items()}
        report['inputs']={k:{'path':str(v),'sha256':hashes[k]} for k,v in paths.items()}
        if hashes != {'html':HTML_SHA,'checker':CHECKER_SHA,'reused_v7':V7_SHA}:
            raise RuntimeError('Unsupported source: review meaning and probes before changing pins')
        previous=load(prev,'ct000_review_v7_reused');mod=load(checker,'ct000_subject_v8')
        mod.KB_CHON={'-'}
        tables=mod.cat_bang(source.read_text(encoding='utf-8'));model=mod.nap(tables)
        static=mod.kiem_tinh(model);structure,nstruct=mod.kiem_cau_truc(source.read_text(encoding='utf-8'))
        baseline=[{'name':c[0],'errors':mod.chay_ca(model,*c)} for c in mod.CA]
        report['baseline']={'static_errors':static,'structure_errors':structure,'tables_checked':nstruct,
                            'concurrency_errors':mod.dong_thoi(model),'case_count':len(baseline),
                            'passed':sum(not c['errors'] for c in baseline),'cases':baseline,'self_test_errors':mod.tu_kiem(tables)}
        report['regressions'],report['findings'],report['positive_controls']=suite(mod,tables,model,previous)
        report['inventory']=previous.real_inventory(mod,project)
        report['inputs_unchanged']=hashes=={k:sha(v) for k,v in paths.items()}
        if not report['inputs_unchanged']:raise RuntimeError('Inputs changed during review')
        bad=any(x['status']=='FINDING' for x in report['findings']+report['regressions'])
        bad=bad or any(not x['pass'] for x in report['positive_controls']) or any(c['errors'] for c in baseline)
        bad=bad or bool(static or structure or report['baseline']['concurrency_errors'] or report['baseline']['self_test_errors'])
        rc=1 if bad else 0
    except Exception as exc:
        report['error']=f'{type(exc).__name__}: {exc}'
        rc=2
    report['exit_code']=rc;report['verdict']={0:'PROBES_PASSED_WITHIN_SCOPE',1:'FINDINGS_REMAIN',2:'NOT_EVALUATED_REVIEW_REQUIRED'}[rc]
    args.out.mkdir(parents=True,exist_ok=True)
    encoded=(json.dumps(report,ensure_ascii=False,indent=2)+'\n').encode()
    dest=args.out/'v8-results.json';dest.write_bytes(encoded)
    summary={'verdict':report['verdict'],'exit_code':rc,'baseline':{k:v for k,v in report.get('baseline',{}).items() if k!='cases'},
             'regressions':[{'id':x['id'],'status':x['status']} for x in report.get('regressions',[])],
             'findings':[{'id':x['id'],'status':x['status'],'title':x['title']} for x in report['findings']],
             'positive_controls':report.get('positive_controls'), 'inventory':report.get('inventory'),
             'error':report.get('error'),'evidence_bytes':len(encoded),'evidence_sha256':hashlib.sha256(encoded).hexdigest()}
    print(json.dumps(summary,ensure_ascii=False))
    if args.pack_report:
        import gzip,base64
        print('EVIDENCE_GZIP_BASE64='+base64.b64encode(gzip.compress(encoded,mtime=0)).decode())
    return rc

if __name__=='__main__':
    raise SystemExit(main())
