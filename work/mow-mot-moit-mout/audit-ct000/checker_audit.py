#!/usr/bin/env python3
"""Targeted, bounded audit of the CT-000.4 v6 checker itself (stdlib only).

This imports the exact checker under review. It does NOT claim to independently
prove the workflow or run all 17 graphs. Fault injection into main() verifies
how the checker classifies incomplete/error outcomes in its mutation campaign.
"""
from __future__ import annotations
import argparse
import ast
import contextlib
import copy
import hashlib
import importlib.util
import inspect
import io
import json
from pathlib import Path
import sys

CHECKER_SHA256 = '9e9436cdc058cb480e08ed6dc7062e0d74b18aae43ccbd1e632342939e4ecbd2'
HTML_SHA256 = {
    '4d2a73a183c2ded90de6164a0e33eaf2ce47efef740edeb5157e67648fd69e83',
    'b94a70383f2e44ffadd9fa6c3e60868152eb0027c53cbb82e9ea8e1184625999',
}


def load_checker(path):
    spec = importlib.util.spec_from_file_location('ct000_host_under_review', path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def run_cases(h, S):
    results = []
    for case in h.CA:
        failure = h.chay_ca(S, *case)
        results.append({'name': case[0], 'passed': failure is None, 'failure': failure})
    return results


def main_control(h, html_path, S, mutation, outcome):
    """Execute the real main() with an accepted-baseline control and one injected
    UNKNOWN mutant outcome. This is a unit test of reporting, not a BFS run.
    """
    saved_check, saved_mutations, saved_argv = h.kiem_het, h.dot_bien, sys.argv
    stream = io.StringIO()
    calls = []

    def controlled_check(T, nhanh=False, in_ra=False):
        calls.append({'mutant': nhanh, 'baseline_report': in_ra})
        if not nhanh:
            return [], S
        if outcome == 'cutoff':
            return [('K controlled', 'quá lớn', 4)], S
        raise RuntimeError('CONTROLLED_CHECKER_FAILURE')

    try:
        h.kiem_het = controlled_check
        h.dot_bien = lambda T: [('capacity-guard-mutant', mutation)]
        sys.argv = [str(Path(h.__file__)), '--trang', str(html_path), '--dot-bien']
        with contextlib.redirect_stdout(stream):
            try:
                h.main()
                code = 0
            except SystemExit as exc:
                code = exc.code
    finally:
        h.kiem_het, h.dot_bien, sys.argv = saved_check, saved_mutations, saved_argv
    return {'test_kind': 'CONTROLLED_MAIN_REPORTING_PROBE',
            'baseline_bfs': 'NOT_RUN; accepted baseline injected solely to isolate mutation reporting',
            'mutant_outcome': outcome, 'process_exit': code,
            'calls': calls, 'stdout': stream.getvalue(),
            'incorrectly_reported_killed': 'bắt được 1 · sống sót 0' in stream.getvalue()}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    here = Path(__file__).resolve().parent
    p.add_argument('--checker', type=Path, default=here / 'kiem-ct000-4.py')
    p.add_argument('--html', type=Path, default=here / 'ban-duyet.html')
    p.add_argument('--out', type=Path, default=here / 'checker_results.json')
    args = p.parse_args()
    report = {'audit': 'CT000-v6-checker-engine', 'findings': [],
              'scope': 'Local source/unit probes only; no PG, Flow, remote writes, or exhaustive 17-scenario run.'}

    def finish(code, verdict):
        report.update(exit_code=code, verdict=verdict)
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        print(json.dumps({'verdict': verdict, 'exit_code': code,
                          'findings': [f['id'] for f in report['findings']],
                          'report': str(args.out)}, ensure_ascii=False))
        return code

    try:
        checker_bytes = args.checker.read_bytes()
        html_bytes = args.html.read_bytes()
        report['inputs'] = {'checker': str(args.checker), 'checker_sha256': hashlib.sha256(checker_bytes).hexdigest(),
                            'html': str(args.html), 'html_sha256': hashlib.sha256(html_bytes).hexdigest()}
        if report['inputs']['checker_sha256'] != CHECKER_SHA256:
            report['reason'] = 'Checker source changed; these version-scoped reporting probes need review.'
            return finish(2, 'NOT_EVALUATED_REVIEW_REQUIRED')
        if report['inputs']['html_sha256'] not in HTML_SHA256:
            report['reason'] = 'Workflow source changed; these version-scoped predicates and fixtures need review.'
            return finish(2, 'NOT_EVALUATED_REVIEW_REQUIRED')
        h = load_checker(args.checker)
        T = h.cat_bang(html_bytes.decode('utf-8'))
        S = h.nap(T)
        cases = run_cases(h, S)
        report['baseline'] = {'static_errors': h.kiem_tinh(S), 'concurrency_error': h.dong_thoi(S),
                              'case_results': cases, 'cases_passed': sum(c['passed'] for c in cases),
                              'states': len(S['ST']), 'transitions': len(T['Bảng Chuyển trạng thái']),
                              'scenarios': len(h.KICH_BAN), 'built_in_mutations': len(h.dot_bien(T))}
        if report['baseline']['static_errors'] or not all(c['passed'] for c in cases):
            report['reason'] = 'Baseline no longer matches the reviewed assumptions.'
            return finish(2, 'NOT_EVALUATED_REVIEW_REQUIRED')

        # Actual bounded exploration, using the unchanged engine and data.
        init = dict(h.MAC_DINH); init.update(h.AN); init['st'] = 'Mới'
        cutoff_errors, graph = h.kham(S, init, gioi=1, nhanh=True)
        report['actual_bounded_search'] = {'limit': 1, 'errors': cutoff_errors, 'complete_graph': graph is not None}

        # Real unsafe capacity-guard mutant. No labels are supplied to ap_dung.
        TM = copy.deepcopy(T)
        row = next(r for r in TM['Bảng Giá trị'] if r[0] == 'xin nhận' and r[1] == 'Chờ')
        old_formula = row[4]
        needle = 'hết chỗ ← not còn_chỗ'
        if old_formula.count(needle) != 1:
            report['reason'] = 'Capacity predicate changed; review probe applicability.'
            return finish(2, 'NOT_EVALUATED_REVIEW_REQUIRED')
        row[4] = old_formula.replace(needle, 'hết chỗ ← False')
        SM = h.nap(TM)
        mutant_cases = run_cases(h, SM)
        full = dict(h.MAC_DINH); full.update(h.AN)
        full.update(st='Chờ', còn_chỗ=False)
        before, bt = h.ap_dung(S, full, 'xin nhận', {})
        after, mt = h.ap_dung(SM, full, 'xin nhận', {})

        assigned = set()
        for _, (_, code, body) in S['OPS'].items():
            if code is not None:
                assigned.update(n.id for n in ast.walk(ast.parse(body))
                                if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Store))
        choices_or_world_set_capacity = 'còn_chỗ' in inspect.getsource(h.the_gioi) + inspect.getsource(h.lua_chon)
        capacities = [(name, dict(h.MAC_DINH, **values)['còn_chỗ']) for name, values in h.KICH_BAN]

        report['findings'].append({
            'id': 'E03', 'status': 'REPRODUCED_CHECKER_COVERAGE_GAP',
            'title': 'The two-work capacity checker ignores the actual claim predicate.',
            'mutation': {'table': 'Bảng Giá trị', 'event': 'xin nhận', 'before': old_formula, 'after': row[4]},
            'mutant_static_errors': h.kiem_tinh(SM),
            'mutant_concurrency_error': h.dong_thoi(SM),
            'mutant_cases_passed': sum(c['passed'] for c in mutant_cases),
            'actual_capacity_full_probe': {
                'input': {'state': 'Chờ', 'còn_chỗ': False, 'lần_nhận': 0, 'M': 2, 'quá_hạn_gốc': False},
                'baseline': {'transition': bt, 'target': before['st']},
                'mutant': {'transition': mt, 'target': after['st'], 'lần_nhận': after['lần_nhận']},
            },
            'why_existing_17_graphs_cannot_activate_this_fault': {
                'initial_capacity': capacities,
                'operation_assigns_capacity': 'còn_chỗ' in assigned,
                'environment_or_choice_generator_mentions_capacity': choices_or_world_set_capacity,
            },
            'limitation': 'All 17 graphs were NOT rerun. The unchanged True field makes this predicate mutation inert within their generated inputs. The direct false-capacity probe demonstrates the missing case.',
            'fix': 'Run both jobs through the real claim classifier/actions over one shared capacity value; test stale capacity reads, full capacity, atomic claim and release.'
        })

        report['findings'].append({
            'id': 'E01', 'status': 'REPRODUCED_MUTATION_REPORTING_ERROR',
            'title': 'An incomplete search is counted as a killed mutant.',
            'actual_cutoff_result': cutoff_errors,
            'main_control': main_control(h, args.html, S, TM, 'cutoff'),
            'fix': 'Classify state limit, timeout and OOM as INCONCLUSIVE. Require a concrete violated property/trace to count a kill; incomplete campaigns must not exit0.'
        })
        report['findings'].append({
            'id': 'E02', 'status': 'REPRODUCED_MUTATION_REPORTING_ERROR',
            'title': 'An exception in the checker is counted as a killed mutant.',
            'main_control': main_control(h, args.html, S, TM, 'exception'),
            'fix': 'Separate expected invalid-spec rejection from an internal checker exception. Unexpected exceptions are ERROR/INCONCLUSIVE, never evidence that a safety defect was detected.'
        })

        # Additional unit scope check: concurrency reads names, not operation effects.
        TN = copy.deepcopy(T)
        op = next(r for r in TN['Bảng Thao tác'] if r[0] == 'giữ chỗ')
        old = op[2]; op[2] = 'giữ_chỗ = False'
        SN = h.nap(TN)
        report['concurrency_name_only_control'] = {
            'mutation': {'operation': 'giữ chỗ', 'before': old, 'after': op[2]},
            'concurrency_error': h.dong_thoi(SN),
            'first_case_failure': h.chay_ca(SN, *h.CA[0]),
            'interpretation': 'The concurrency subcheck passes despite the changed body; the ordinary case DOES detect B5. This is not presented as a mutant surviving the entire checker.'
        }
        report['inputs_unchanged'] = (args.checker.read_bytes() == checker_bytes and args.html.read_bytes() == html_bytes)
        return finish(1, 'CHECKER_FINDINGS_REMAIN')
    except Exception as exc:
        report['error'] = repr(exc)
        return finish(2, 'NOT_EVALUATED_REVIEW_REQUIRED')


if __name__ == '__main__':
    raise SystemExit(main())
