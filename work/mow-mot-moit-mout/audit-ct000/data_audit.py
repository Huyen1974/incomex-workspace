#!/usr/bin/env python3
"""Probe raw missing/invalid gate inputs against the pinned CT-000.4 model.

This uses the author's engine as the system under test. It does not claim a
second implementation of the model or live PostgreSQL input validation.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

SUPPORTED_CHECKER = '9e9436cdc058cb480e08ed6dc7062e0d74b18aae43ccbd1e632342939e4ecbd2'
SUPPORTED_HTML = {
    '4d2a73a183c2ded90de6164a0e33eaf2ce47efef740edeb5157e67648fd69e83',
    'b94a70383f2e44ffadd9fa6c3e60868152eb0027c53cbb82e9ea8e1184625999',
}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--html', type=Path, required=True)
    ap.add_argument('--checker', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    a = ap.parse_args()
    report = {'scope': 'Model input validation only; no PG/Flow test.', 'probes': []}
    a.out.parent.mkdir(parents=True, exist_ok=True)
    code = 2
    try:
        checker_hash = hashlib.sha256(a.checker.read_bytes()).hexdigest()
        source_hash = hashlib.sha256(a.html.read_bytes()).hexdigest()
        report['inputs'] = {'checker_sha256': checker_hash, 'html_sha256': source_hash}
        if checker_hash != SUPPORTED_CHECKER:
            raise ValueError('Unsupported checker revision: update and review the fixture before rerunning.')
        if source_hash not in SUPPORTED_HTML:
            raise ValueError('Unsupported source revision: review source definitions before updating the fixture.')
        spec = importlib.util.spec_from_file_location('ct000_author_under_test', a.checker)
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        tables = m.cat_bang(a.html.read_text(encoding='utf-8'))
        model = m.nap(tables)
        report['static_errors'] = m.kiem_tinh(model)
        report['author_cases'] = [
            {'name': ca[0], 'result': m.chay_ca(model, *ca)} for ca in m.CA
        ]
        cases = [('control_valid', {}, False),
                 ('g2_missing_null', {'g2': None}, True),
                 ('g2_invalid_spelling', {'g2': 'DU'}, True),
                 ('g5_missing_null', {'g5': None}, True),
                 ('g5_unknown', {'g5': 'chưa biết'}, True)]
        events = m.VAO + [m.GUI, m.LAM, m.KQ('OK'), ('chấm', {}), ('chấm', {})]
        for name, raw, should_reject in cases:
            s = dict(m.MAC_DINH)
            s.update(m.AN)
            s.update(raw)
            s['st'] = 'Mới'
            trace = []
            rejected = False
            errors = []
            for ev, chosen in events:
                before = s['st']
                world = [d for n, _, d in m.the_gioi(s) if n == ev]
                if world:
                    s = dict(s, **world[0])
                    transition = ev
                else:
                    chosen = dict(chosen)
                    if ev == 'làm thao tác':
                        chosen.update(tác_nhân=s['gen_giữ'], _ai='chính')
                    f = model['FORM'].get((s['st'], ev))
                    ns = dict(s, **chosen)
                    if f is None or not m.ev_(f[1], ns):
                        rejected = True
                        break
                    new, transition = m.ap_dung(model, s, ev, chosen)
                    if new is None:
                        rejected = True
                        break
                    s = new
                errors.extend(m.vi_pham(model, s))
                trace.append({'from': before, 'event': ev, 'transition': transition, 'to': s['st']})
            accepted = s['st'] == 'Kết thúc·Đạt' and not errors and not rejected
            report['probes'].append({
                'id': name, 'raw_override': raw, 'expected_rejection': should_reject,
                'final_state': s['st'], 'invariant_errors': errors,
                'accepted': accepted, 'trace': trace,
                'status': ('UNVALIDATED_INPUT_ACCEPTED' if accepted else 'REJECTED') if should_reject else ('PASS' if accepted else 'CONTROL_FAILED'),
            })
        report['verdict'] = 'INPUT_VALIDATION_GAP' if any(p['expected_rejection'] and p['accepted'] for p in report['probes']) else 'PROBES_PASSED'
        report['limitation'] = ('These inputs demonstrate missing rejection in the executable model. '
                               'A real PG schema may reject them, but no such binding or PG execution is tested here. '
                               'g5=chưa biết is separately included because the general answer contract uses Unknown; '
                               'the aggregate g5 domain has not been supplied as a validated input contract.')
        code = 1 if report['verdict'] != 'PROBES_PASSED' or report['static_errors'] or any(x['result'] for x in report['author_cases']) else 0
    except Exception as exc:
        report['verdict'] = 'NOT_EVALUATED_REVIEW_REQUIRED'
        report['error'] = f'{type(exc).__name__}: {exc}'
    report['exit_code'] = code
    a.out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'verdict': report['verdict'], 'exit_code': code,
                      'probes': [{'id': p['id'], 'status': p['status']} for p in report['probes']]}, ensure_ascii=False))
    return code


if __name__ == '__main__':
    raise SystemExit(main())
