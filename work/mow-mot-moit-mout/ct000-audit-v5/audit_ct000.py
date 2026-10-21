#!/usr/bin/env python3
"""Replay a version-scoped, offline CT-000 review. Never grants deployment approval."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    base = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--html', type=Path, default=base / 'snapshots/ban-duyet.html')
    parser.add_argument('--collab', type=Path, default=base / 'snapshots/COLLAB.md')
    parser.add_argument('--checker', type=Path, default=base / 'scripts/author_checker.py')
    parser.add_argument('--out', type=Path, default=base / 'audit-output')
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    input_paths = {k: getattr(args, k).resolve() for k in ('html', 'collab', 'checker')}
    summary = {
        'scope': 'Version-scoped source and checker audit; no PostgreSQL, Directus, or external side effects executed.',
        'release_verdict': 'BLOCKED_PG_AND_FLOW_NOT_EXECUTED',
        'inputs': {}, 'checks': [], 'exit_code': 2,
    }
    summary_path = args.out / 'summary.json'

    def finish(code, verdict):
        summary['exit_code'] = code
        summary['verdict'] = verdict
        summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        print(json.dumps({'verdict': verdict, 'exit_code': code,
                          'release_verdict': summary['release_verdict'],
                          'summary': str(summary_path.resolve()),
                          'checks': [{'name': c['name'], 'exit_code': c['exit_code']} for c in summary['checks']]},
                         ensure_ascii=False, indent=2))
        return code

    missing = [str(p) for p in input_paths.values() if not p.is_file()]
    if missing:
        summary['error'] = {'missing_inputs': missing}
        return finish(2, 'NOT_EVALUATED_REVIEW_REQUIRED')
    before = {k: sha256(p) for k, p in input_paths.items()}
    summary['inputs'] = {k: {'path': str(p), 'sha256': before[k]} for k, p in input_paths.items()}
    jobs = [
        ('independent', 'independent_audit.py',
         ['--html', str(input_paths['html']), '--out', str((args.out / 'independent_results.json').resolve())],
         args.out / 'independent_results.json'),
        ('semantic', 'semantic_audit.py',
         ['--html', str(input_paths['html']), '--out', str((args.out / 'semantic_report.json').resolve())],
         args.out / 'semantic_report.json'),
        ('mutation', 'mutation_audit.py',
         ['--html', str(input_paths['html']), '--collab', str(input_paths['collab']),
          '--checker', str(input_paths['checker']), '--out', str((args.out / 'mutations').resolve())],
         args.out / 'mutations/results.json'),
    ]
    unknown = False
    failures = False
    for name, filename, options, report in jobs:
        entry = {'name': name, 'report': str(report.resolve())}
        try:
            run = subprocess.run([sys.executable, str(base / 'scripts' / filename), *options],
                                 text=True, encoding='utf-8', capture_output=True, timeout=60,
                                 cwd=base)
            (args.out / f'{name}.stdout.txt').write_text(run.stdout, encoding='utf-8')
            (args.out / f'{name}.stderr.txt').write_text(run.stderr, encoding='utf-8')
            entry['exit_code'] = run.returncode
            if not report.is_file():
                raise RuntimeError('The check produced no result JSON.')
            data = json.loads(report.read_text(encoding='utf-8'))
            entry['reported_verdict'] = data.get('verdict', data.get('audit_verdict'))
            if run.returncode not in (0, 1):
                unknown = True
            elif run.returncode == 1:
                failures = True
        except (OSError, ValueError, RuntimeError, subprocess.TimeoutExpired) as exc:
            entry['exit_code'] = 2
            entry['error'] = str(exc)
            unknown = True
        summary['checks'].append(entry)

    after = {k: sha256(p) for k, p in input_paths.items()}
    summary['inputs_unchanged'] = before == after
    if before != after:
        summary['error'] = 'An input changed during the audit; no consistent verdict is available.'
        unknown = True
    if unknown:
        return finish(2, 'NOT_EVALUATED_REVIEW_REQUIRED')
    if failures:
        return finish(1, 'REJECT_CURRENT_SPEC_AND_CHECKER')
    # This package does not contain a PG/Flow integration runner. Even a future
    # all-green source check must not silently become permission to deploy.
    return finish(1, 'STATIC_CHECKS_PASSED_IMPLEMENTATION_NOT_VERIFIED')


if __name__ == '__main__':
    raise SystemExit(main())
