#!/usr/bin/env python3
"""Version-pinned CT-000 adversarial probes, reusing the registered checker.
No database/network/large graph sweep. Findings are model/checker observations,
not claims that production reproduced them. Exit 0: scoped probes pass;
1: findings remain; 2: not evaluated/checker error. Not a deployment approval.
"""
from __future__ import annotations
import argparse
import base64
import contextlib
import copy
import gzip
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import re
import sys
import tempfile

PINS = {
    'html': '5948c52fc293b666c550148b648fb3fc10a52d4e2ac303d19329d20bd3107a93',
    'checker': 'dbcf08b725c679fa1c8b4205cd3f2a3cd30bff0038c8392578bb25640702bf6a',
}
FIELDS = ['st', 'thế_hệ', 'gen_giữ', 'giữ_chỗ', 'lần_gia_hạn', 'g1',
          'chờ_duyệt', 'chờ_nhận', 'ý_định', 'kết_luận', 'đang_bay', 'đã_làm']

def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def load_module(path: Path):
    spec = importlib.util.spec_from_file_location('ct000_subject_v7', path)
    if spec is None or spec.loader is None:
        raise RuntimeError('Cannot load the pinned checker')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

class Trace:
    def __init__(self, mod, model, initial=None):
        self.mod, self.model = mod, model
        self.state = dict(mod.MAC_DINH)
        self.state.update(mod.AN)
        self.state.update(initial or {})
        self.state['st'] = 'Mới'
        self.events = []
        self.violations = []

    def step(self, event, payload=None):
        payload = dict(payload or {})
        old = dict(self.state)
        world = [d for name, _, d in self.mod.the_gioi(old) if name == event]
        if world:
            new, transition = dict(old), 'environment'
            new.update(world[0])
        else:
            if event == 'làm thao tác':
                payload.setdefault('_ai', 'chính')
                payload.setdefault('tác_nhân', old['gen_giữ'])
            form = self.model['FORM'].get((old['st'], event))
            if form is None:
                raise RuntimeError(f'No event {event!r} in {old["st"]!r}')
            ns = dict(old)
            ns.update(payload)
            if not self.mod.ev_(form[1], ns):
                raise RuntimeError(f'Disabled event {event!r}')
            new, transition = self.mod.ap_dung(self.model, old, event, payload)
            if new is None:
                self.events.append({'event': event, 'payload': payload, 'error': transition})
                return transition
        self.state = new
        self.violations.extend(self.mod.vi_pham(self.model, new))
        self.events.append({'event': event, 'payload': payload, 'transition': transition,
                            'before': old['st'], 'after': new['st']})
        return None

    def steps(self, events):
        for event, payload in events:
            error = self.step(event, payload)
            if error:
                raise RuntimeError(repr(error))
        return self

    def evidence(self):
        return {'trace': self.events, 'final': {k: self.state[k] for k in FIELDS},
                'subject_invariants': self.violations}

START = [('khai xong', {}), ('chấm', {}), ('chấm', {}), ('xin nhận', {})]
WORK = [('làm thao tác', {}), ('bên nhận làm', {}), ('kết quả', {'mã': 'OK'})]

def probe_suite(mod, tables, model):
    results = []
    def record(code, title, broken, evidence, kind='MODEL_COUNTEREXAMPLE'):
        results.append({'id': code, 'title': title, 'kind': kind,
                        'status': 'FINDING' if broken else 'PASS', 'evidence': evidence})

    # A legitimate old worker may report a failure after its lease was reclaimed.
    tr = Trace(mod, model).steps(START)
    stale_generation = tr.state['gen_giữ']
    tr.steps([('qua hạn giữ', {}), ('hết hạn giữ', {}), ('xin nhận', {}),
              ('làm thao tác', {}), ('bên nhận làm', {})])
    before = dict(tr.state)
    err = tr.step('kết quả', {'mã': 'FAILED_PRECONDITION', 'tác_nhân': stale_generation})
    record('V7-01', 'Late result from revoked generation changes the current attempt',
           not err and (tr.state['st'] != before['st'] or
                        tr.state['giữ_chỗ'] != before['giữ_chỗ']),
           dict(tr.evidence(), stale_generation=stale_generation,
                current_generation=before['thế_hệ']))

    tr = Trace(mod, model).steps(START)
    stale_generation = tr.state['gen_giữ']
    tr.steps([('qua hạn giữ', {}), ('hết hạn giữ', {}), ('xin nhận', {})])
    before = tr.state['lần_gia_hạn']
    err = tr.step('gia hạn', {'tác_nhân': stale_generation})
    record('V7-02', 'Heartbeat from revoked generation renews the new attempt',
           not err and tr.state['lần_gia_hạn'] != before,
           dict(tr.evidence(), stale_generation=stale_generation))

    tr = Trace(mod, model, {'g1': 'thiếu'}).steps(
        [('khai xong', {}), ('chấm', {}), ('trả lời', {}), ('chấm', {})])
    record('V7-03', 'Empty human response changes missing G1 input to sufficient',
           tr.state['g1'] == 'đủ' and tr.state['st'] == 'Chấm G2', tr.evidence(),
           'INPUT_CONTRACT_GAP')

    tr = Trace(mod, model, {'chờ_duyệt': True}).steps(
        START + WORK + [('chấm', {}), ('trả lời', {}), ('chấm', {}), ('chấm', {})])
    record('V7-04', 'Empty approval event can finish G4 and close the task',
           tr.state['st'] == 'Kết thúc·Đạt', tr.evidence(), 'INPUT_CONTRACT_GAP')

    tr = Trace(mod, model, {'chờ_nhận': True}).steps(
        START + WORK + [('chấm', {}), ('chấm', {}), ('trả lời', {}), ('chấm', {})])
    record('V7-05', 'Empty handover event becomes recipient acknowledgement',
           tr.state['st'] == 'Kết thúc·Đạt', tr.evidence(), 'INPUT_CONTRACT_GAP')

    missing = []
    grpc_codes = ('CANCELLED', 'NOT_FOUND', 'ALREADY_EXISTS', 'OUT_OF_RANGE',
                  'UNIMPLEMENTED', 'INTERNAL', 'DATA_LOSS', 'UNAUTHENTICATED')
    for code in grpc_codes:
        tr = Trace(mod, model).steps(START)
        err = tr.step('kết quả', {'mã': code})
        if err:
            missing.append({'code': code, 'error': err})
    record('V7-06', 'Eight standard gRPC codes lack a formula result/fallback',
           bool(missing), {'unhandled': missing,
                           'note': 'A separately verified normalizer could close this gap; none is executed here.'},
           'INPUT_CONTRACT_GAP')

    # Exercise the ORIGINAL main/classifier. The model is unchanged. Inject a
    # checker evaluation fault only during the single mutation run, after baseline.
    saved = {k: getattr(mod, k) for k in ('kiem_het', 'dot_bien', 'ev_', 'KB_CHON', 'GIOI')}
    saved_argv = list(sys.argv)
    calls = 0
    def fault_eval(code, ns):
        if getattr(code, 'co_filename', '') == 'B1':
            raise RuntimeError('V7_INJECTED_CHECKER_FAILURE')
        return saved['ev_'](code, ns)
    def checked(*args, **kwargs):
        nonlocal calls
        calls += 1
        mod.ev_ = fault_eval if calls >= 2 else saved['ev_']
        try:
            return saved['kiem_het'](*args, **kwargs)
        finally:
            mod.ev_ = saved['ev_']
    with tempfile.TemporaryDirectory(prefix='ct000-v7-classifier-') as tmp:
        target = Path(tmp) / 'result.json'
        try:
            mod.kiem_het = checked
            mod.dot_bien = lambda _: [('unchanged model; injected checker failure', tables)]
            sys.argv = ['kiem-ct000-4.py', '--kb', '-', '--dot-bien', '--json', str(target)]
            with contextlib.redirect_stdout(io.StringIO()):
                try:
                    mod.main()
                    exit_code = 0
                except SystemExit as exc:
                    exit_code = exc.code
            data = json.loads(target.read_text(encoding='utf-8'))
            killed = data['đột_biến']['KILLED']
            record('V7-07', 'Checker exception is counted as KILLED on unchanged model',
                   bool(killed), {'original_main_exit': exit_code,
                                  'mutations': data['đột_biến'],
                                  'note': 'Overall exit 2 remains partial; the defect is the KILLED classification.'},
                   'CHECKER_FAULT_INJECTION')
        finally:
            sys.argv = saved_argv
            for k, value in saved.items():
                setattr(mod, k, value)

    # Unit-test the claimed liveness property, not a counterexample on the real
    # workflow. A machine self-loop on an immediate state is not benign waiting.
    nodes = []
    for state in ('Chấm G2', 'Kết thúc·Đạt'):
        s = dict(mod.MAC_DINH)
        s.update(mod.AN)
        s['st'] = state
        nodes.append(mod.dong(s))
    edges = ([0, 0], [0, 1], [0, 0])
    errors = mod.song(nodes, edges)
    record('V7-08', 'Liveness helper ignores an immediate-state machine self-loop',
           not errors, {'nodes': ['Chấm G2', 'Kết thúc·Đạt'],
                        'machine_edges': [[0, 0], [0, 1]], 'reported_errors': errors,
                        'note': 'This checks a property limitation. Fairness/stuttering assumptions must be explicit.'},
           'CHECKER_PROPERTY_SELF_TEST')

    # A synthetic registry containing ONLY archival lookalikes. No live entries.
    saved = {k: getattr(mod, k) for k in ('MASTER_TOOL', 'BO_CONG_CU', 'THU_MUC_VIEC')}
    with tempfile.TemporaryDirectory(prefix='ct000-v7-registry-') as tmp:
        root = Path(tmp)
        history, tools = [], {}
        for i, tid in enumerate(('python:kiem-ct000-4', 'python:ct000-audit')):
            p = root / f'fake_{i}.py'
            p.write_text('# registry fixture, never executed\n', encoding='utf-8')
            tools[tid] = str(p)
            history.append({'id': tid, 'path': str(p), 'sha256': sha(p), 'tool_id': tid})
        master = root / 'master.html'
        master.write_text(json.dumps({'catalog': {'tool_registry': {'provider_tools': [], 'memory': []}},
                                      'archive': history}, ensure_ascii=False, indent=0), encoding='utf-8')
        try:
            mod.MASTER_TOOL = str(master)
            mod.BO_CONG_CU = tools
            mod.THU_MUC_VIEC = []
            log = io.StringIO()
            with contextlib.redirect_stdout(log):
                errors = mod.kiem_ke()
            record('V7-09', 'Inventory accepts archival strings when live registry is empty',
                   not errors, {'live_provider_tools': 0, 'live_memory': 0,
                                'reported_errors': errors, 'stdout': log.getvalue()},
                   'REGISTRY_NEGATIVE_FIXTURE')
        finally:
            for k, value in saved.items():
                setattr(mod, k, value)
    return results

def real_inventory(mod, project: Path):
    """Read actual canonical JSON records; do not infer registry membership by name."""
    master = project.parents[1] / 'work/tools-quy-trinh/view.html'
    text = master.read_text(encoding='utf-8')
    candidates = []
    for attrs, body in re.findall(r'<script\b([^>]*)>(.*?)</script\s*>', text, re.S | re.I):
        if 'application/json' not in attrs:
            continue
        try:
            data = json.loads(body)
        except json.JSONDecodeError:
            continue
        if isinstance(data, dict):
            reg = data.get('catalog', {}).get('tool_registry') if isinstance(data.get('catalog', {}), dict) else None
            if isinstance(reg, dict) and isinstance(reg.get('provider_tools'), list):
                candidates.append((attrs, reg))
    if len(candidates) != 1:
        return {'status': 'NOT_EVALUATED', 'canonical_candidates': len(candidates)}
    attrs, reg = candidates[0]
    entries = reg['provider_tools']
    ids = [r.get('id') for r in entries]
    registered = {r['path'] for r in entries if isinstance(r.get('path'), str)}
    repo = project.parents[1]
    files = list((project / 'cong-cu').glob('*.py')) + [project / 'check-ui-review.py']
    missing = [str(p.relative_to(repo)) for p in files if p.is_file() and str(p.relative_to(repo)) not in registered]
    canonical = []
    for tid in ('python:kiem-ct000-4', 'python:ct000-audit'):
        rows = [r for r in entries if r.get('id') == tid]
        info = {'id': tid, 'count': len(rows)}
        if len(rows) == 1:
            r = rows[0]
            p = repo / r['path']
            info.update(path=r['path'], sha256_matches=p.is_file() and sha(p) == r.get('sha256'))
            if r.get('manifest'):
                mf = repo / r['manifest']
                info['manifest_hash_matches'] = mf.is_file() and sha(mf) == r.get('manifest_sha256')
                if mf.is_file():
                    content = json.loads(mf.read_text(encoding='utf-8'))
                    fs = content.get('files', [])
                    info['manifest_entries'] = len(fs)
                    info['manifest_mismatches'] = [f['path'] for f in fs
                        if not (mf.parent / f['path']).is_file() or sha(mf.parent / f['path']) != f['sha256']]
        canonical.append(info)
    return {'status': 'INSPECTED', 'script_tag': attrs.strip(), 'provider_tools': len(entries),
            'duplicate_ids': sorted({x for x in ids if ids.count(x) > 1}),
            'ct000_tools': canonical, 'unregistered_scope_scripts': missing,
            'master_sha256': sha(master)}

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--html', type=Path)
    parser.add_argument('--checker', type=Path)
    parser.add_argument('--out', type=Path, default=Path('/tmp/ct000-audit-v7-results'))
    parser.add_argument('--pack-report', action='store_true', help='Print gzip/base64 evidence for bounded transport.')
    args = parser.parse_args(argv)
    project = Path(__file__).resolve().parent.parent
    source = args.html or project / 'ban-duyet.html'
    checker = args.checker or project / 'kiem-ct000-4.py'
    report = {'revision': 'CT000-AUDIT-V7-20261022', 'scope': 'bounded adversarial probes',
              'full_graph_sweep': 'NOT_EXECUTED', 'pg_flow': 'NOT_EXECUTED',
              'source_pins': PINS, 'results': []}
    code = 2
    try:
        actual = {'html': sha(source), 'checker': sha(checker)}
        report['inputs'] = actual
        if actual != PINS:
            raise RuntimeError('Source changed: semantic review required; do not only replace hashes.')
        mod = load_module(checker)
        mod.TRANG = str(source)
        text = source.read_text(encoding='utf-8')
        tables = mod.cat_bang(text)
        model = mod.nap(tables)
        static = mod.kiem_tinh(model)
        structure, table_count = mod.kiem_cau_truc(text)
        concurrency = mod.dong_thoi(model)
        cases = [{'name': ca[0], 'error': mod.chay_ca(model, *ca)} for ca in mod.CA]
        report['baseline'] = {'static_errors': static, 'structure_errors': structure,
                              'table_count': table_count, 'concurrency_error': concurrency,
                              'cases': cases, 'cases_passed': sum(c['error'] is None for c in cases)}
        report['results'] = probe_suite(mod, tables, model)
        report['inventory'] = real_inventory(mod, project)
        report['inputs_unchanged'] = actual == {'html': sha(source), 'checker': sha(checker)}
        if not report['inputs_unchanged']:
            raise RuntimeError('Inputs changed during probes')
        bad_base = bool(static or structure or concurrency or any(c['error'] for c in cases))
        code = 1 if bad_base or any(r['status'] == 'FINDING' for r in report['results']) else 0
    except Exception as exc:
        report['error'] = f'{type(exc).__name__}: {exc}'
        code = 2
    report['verdict'] = {0: 'PROBES_PASSED_WITHIN_SCOPE', 1: 'FINDINGS_REMAIN', 2: 'NOT_EVALUATED'}[code]
    report['exit_code'] = code
    args.out.mkdir(parents=True, exist_ok=True)
    raw = (json.dumps(report, ensure_ascii=False, indent=2) + '\n').encode('utf-8')
    target = args.out / 'v7-results.json'
    target.write_bytes(raw)
    print(json.dumps({'verdict': report['verdict'], 'exit_code': code,
                      'baseline_cases': report.get('baseline', {}).get('cases_passed'),
                      'findings': [{k: r[k] for k in ('id', 'status', 'title')} for r in report['results']],
                      'inventory': report.get('inventory'), 'error': report.get('error'),
                      'evidence_sha256': hashlib.sha256(raw).hexdigest()}, ensure_ascii=False))
    if args.pack_report:
        print('EVIDENCE_GZIP_BASE64=' + base64.b64encode(gzip.compress(raw, mtime=0)).decode('ascii'))
    return code

if __name__ == '__main__':
    raise SystemExit(main())
