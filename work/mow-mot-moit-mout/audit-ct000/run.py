#!/usr/bin/env python3
"""Run small, version-scoped CT-000 audit probes; never runs PG/Flow or large BFS."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys


def main():
    if '--v7' in sys.argv:
        from review_v7 import main as review_v7_main
        return review_v7_main([a for a in sys.argv[1:] if a != '--v7'])
    base = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--html', type=Path)
    parser.add_argument('--checker', type=Path)
    parser.add_argument('--snapshot', action='store_true', help='Replay the pinned reviewed version rather than current project files.')
    parser.add_argument('--out', type=Path, default=Path('/tmp/ct000-audit-v6-results'))
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    source_dir = base / 'snapshots' if args.snapshot else base.parent
    source = args.html or source_dir / 'ban-duyet.html'
    checker = args.checker or source_dir / 'kiem-ct000-4.py'
    report = {'scope': 'Small adversarial probes of the executable model and checker; no full 17-scenario sweep or live PG/Flow run.',
              'integration_status': 'NOT_EXECUTED', 'results': []}
    code = 0
    try:
        paths = {'html': source.resolve(), 'checker': checker.resolve()}
        before = {k: hashlib.sha256(v.read_bytes()).hexdigest() for k, v in paths.items()}
        report['inputs'] = {k: {'path': str(v), 'sha256': before[k]} for k, v in paths.items()}
        for name in ('flow', 'checker', 'data'):
            output = args.out / (name + '_results.json')
            command = [sys.executable, str(base / (name + '_audit.py')), '--html', str(paths['html']),
                       '--checker', str(paths['checker']), '--out', str(output.resolve())]
            done = subprocess.run(command, text=True, encoding='utf-8', capture_output=True, timeout=60)
            (args.out / (name + '.stdout.txt')).write_text(done.stdout, encoding='utf-8')
            (args.out / (name + '.stderr.txt')).write_text(done.stderr, encoding='utf-8')
            data = json.loads(output.read_text(encoding='utf-8'))
            rc = done.returncode if done.returncode in (0, 1, 2) else 2
            code = max(code, rc)
            report['results'].append({'name': name, 'exit_code': rc, 'report': output.name,
                                      'verdict': data.get('verdict', data.get('status'))})
        after = {k: hashlib.sha256(v.read_bytes()).hexdigest() for k, v in paths.items()}
        report['inputs_unchanged'] = before == after
        if before != after:
            raise RuntimeError('Inputs changed during the audit.')
    except Exception as exc:
        code = 2
        report['error'] = f'{type(exc).__name__}: {exc}'
    report['verdict'] = {0: 'PROBES_PASSED_WITHIN_SCOPE', 1: 'FINDINGS_REMAIN', 2: 'NOT_EVALUATED_REVIEW_REQUIRED'}[code]
    report['exit_code'] = code
    (args.out / 'summary.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return code


if __name__ == '__main__':
    raise SystemExit(main())
