#!/usr/bin/env python3
"""Run the unmodified H7 checker against isolated mutated HTML fixtures.

No PostgreSQL, network, remote write, or modification of the source snapshots.
Only the original checker's relative HTML pathname is supplied in a temporary
working directory. Its Python code, test list, and assertions are not changed.
"""
from __future__ import annotations

import argparse
import contextlib
import difflib
import hashlib
import html
import io
import json
import os
from pathlib import Path
import re
import runpy
import subprocess
import sys
import tempfile


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "ban-duyet.html"
COLLAB = HERE / "COLLAB.md"
AUTHOR = HERE / "author_checker.py"
OUT = HERE / "mutation_outputs"


def digest(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def plain(value: str) -> str:
    return html.unescape(re.sub(r"<[^>]+>", "", value)).strip()


def body_span(document: str, name: str) -> tuple[int, int]:
    section = document.index('id="formula-ct-000-4"')
    heading = document.index('head-label">' + name + '<', section)
    end = document.index('</table>', heading)
    body = re.search(r'<tbody>(.*?)</tbody>', document[heading:end], re.S)
    if body is None:
        raise ValueError(f"No tbody for {name}")
    return heading + body.start(1), heading + body.end(1)


def edit_row(document: str, table: str, key: str,
             cells: dict[int, str] | None) -> str:
    """Replace selected text cells, or delete the row when cells is None."""
    a, b = body_span(document, table)
    body = document[a:b]
    matches = []
    for row in re.finditer(r'<tr>(.*?)</tr>', body, re.S):
        td = list(re.finditer(r'(<td[^>]*>)(.*?)(</td>)', row.group(1), re.S))
        if td and plain(td[0].group(2)) == key:
            matches.append((row, td))
    if len(matches) != 1:
        raise ValueError(f"Expected one row {table}/{key}, got {len(matches)}")
    row, td = matches[0]
    if cells is None:
        replacement = ''
    else:
        contents = row.group(1)
        for index, value in sorted(cells.items(), reverse=True):
            match = td[index]
            contents = (contents[:match.start(2)] + html.escape(value, quote=False)
                        + contents[match.end(2):])
        replacement = '<tr>' + contents + '</tr>'
    new_body = body[:row.start()] + replacement + body[row.end():]
    return document[:a] + new_body + document[b:]


def transition(document: str, key: str, action: str) -> str:
    return edit_row(document, 'Bảng Chuyển trạng thái', key, {4: action})


def empty_values(document: str) -> str:
    a, b = body_span(document, 'Bảng Giá trị')
    return document[:a] + document[b:]


def run_checker(document: str, case_id: str) -> dict:
    # Exact source path expected by H7, in a per-case isolated temporary fixture.
    with tempfile.TemporaryDirectory(prefix='h7_', dir=OUT) as tmp:
        fixture = Path(tmp) / 'work/mow-mot-moit-mout/ban-duyet.html'
        fixture.parent.mkdir(parents=True)
        fixture.write_text(document, encoding='utf-8')
        completed = subprocess.run(
            [sys.executable, str(AUTHOR)], cwd=tmp, text=True,
            capture_output=True, timeout=20, check=False,
        )
    log = completed.stdout + ('\nSTDERR:\n' + completed.stderr if completed.stderr else '')
    log_file = OUT / f'{case_id}.stdout.txt'
    log_file.write_text(log, encoding='utf-8')
    stat = re.search(r'TRẠNG THÁI (\d+) · DÒNG (\d+) · LỖI (\d+)', log)
    tests = re.search(r'CA THỬ ĐẠT (\d+) / (\d+)', log)
    result = dict(
        exit_code=completed.returncode,
        states=int(stat[1]) if stat else None,
        transition_rows=int(stat[2]) if stat else None,
        invariant_errors=int(stat[3]) if stat else None,
        tests_passed=int(tests[1]) if tests else None,
        tests_total=int(tests[2]) if tests else None,
        stdout_file=str(log_file),
    )
    # Acceptance uses the author's textual criterion, not merely exit status.
    result['author_accepts'] = bool(
        stat and tests and int(stat[3]) == 0 and int(tests[1]) == int(tests[2])
    )
    if stat is None or tests is None:
        raise RuntimeError(f'Incomplete H7 results for {case_id}; see {log_file}')
    return result


def probe_original(document: str) -> dict:
    """Inspect the original simulator without changing its code or HTML."""
    old_cwd = Path.cwd()
    with tempfile.TemporaryDirectory(prefix='h7_probe_', dir=OUT) as tmp:
        fixture = Path(tmp) / 'work/mow-mot-moit-mout/ban-duyet.html'
        fixture.parent.mkdir(parents=True)
        fixture.write_text(document, encoding='utf-8')
        try:
            os.chdir(tmp)
            with contextlib.redirect_stdout(io.StringIO()):
                namespace = runpy.run_path(str(AUTHOR))
        finally:
            os.chdir(old_cwd)
    run = namespace['run']
    probes = []
    for name, before in [
        ('P01_explicit_duoc_even_at_M', {'lan': 1, 'M': 1}),
        ('P02_explicit_duoc_after_deadline', {'lan': 0, 'M': 3, 'now': 101, 'deadline': 100}),
        ('P03_explicit_duoc_scope_full', {'lan': 0, 'M': 3, 'scope_running': 1, 'scope_limit': 1}),
    ]:
        context = dict(before)
        end, path = run('Chờ', [('xin nhận', 'được')], context)
        probes.append(dict(id=name, start='Chờ', event='xin nhận', supplied_value='được',
                           context_before=before, end=end, context_after=context, path=path))
    covered_ids = set()
    covered_pairs = set()
    per_test = []
    for name, start, steps, expected, initial, need in namespace['TR']:
        context = dict(lan=0, M=99)
        context.update(initial)
        state = start
        ids = []
        for event, value in steps:
            actual_value = value
            if event == 'xin nhận' and value is None:
                actual_value = 'hết M' if context['lan'] >= context['M'] else 'được'
            end, path = run(state, [(event, value)], context)
            tid = path[-1].split('→', 1)[0]
            if re.fullmatch(r'T\d+', tid):
                covered_ids.add(tid)
                covered_pairs.add((state, event, actual_value))
                ids.append(tid)
            state = end
        per_test.append(dict(name=name, start=start, end=state, expected=expected,
                             transition_ids=ids))
    all_ids = {row[0] for row in namespace['TT']}
    all_pairs = {(r['frm'], r['ev'], r['val']) for r in namespace['ROWS']}
    report = dict(
        probes=probes,
        note='These are simulator probes with supplied labels; unused context fields demonstrate missing raw-condition evaluation, not an exploit in live PostgreSQL.',
        coverage=dict(
            distinct_transition_ids=len(covered_ids), total_transition_ids=len(all_ids),
            covered_transition_ids=sorted(covered_ids),
            uncovered_transition_ids=sorted(all_ids - covered_ids),
            distinct_expanded_state_event_value_pairs=len(covered_pairs),
            total_expanded_state_event_value_pairs=len(all_pairs),
            expanded_rows=len(namespace['ROWS']),
            tests_starting_at_Moi=sum(t[1] == 'Mới' for t in namespace['TR']),
            tests_starting_elsewhere=sum(t[1] != 'Mới' for t in namespace['TR']),
        ),
        per_test=per_test,
    )
    (OUT / 'run_probes.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return report


def main() -> None:
    global SOURCE, COLLAB, AUTHOR, OUT
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--html', type=Path, default=SOURCE, help='Pinned HTML snapshot containing CT-000.4')
    parser.add_argument('--checker', type=Path, default=AUTHOR, help='Unmodified extracted H7 Python checker')
    parser.add_argument('--out', type=Path, default=OUT, help='Directory for audit results and diffs')
    parser.add_argument('--collab', type=Path, default=COLLAB,
                        help='Optional source COLLAB.md used to verify/extract the H7 code; skipped if absent')
    args = parser.parse_args()
    SOURCE, COLLAB, AUTHOR, OUT = (args.html.resolve(), args.collab.resolve(),
                                  args.checker.resolve(), args.out.resolve())
    OUT.mkdir(parents=True, exist_ok=True)
    source_bytes = SOURCE.read_bytes()
    collab_bytes = COLLAB.read_bytes() if COLLAB.exists() else None
    document = source_bytes.decode('utf-8')
    if collab_bytes is not None:
        collab_text = collab_bytes.decode('utf-8')
        checker_match = re.search(
            r'```python\n(.*?)\n```',
            collab_text[collab_text.index('Lệnh máy kiểm'):], re.S,
        )
        if checker_match is None:
            raise ValueError('Original H7 Python block not found')
        exact_checker = checker_match.group(1) + '\n'
        if AUTHOR.exists():
            if AUTHOR.read_text(encoding='utf-8') != exact_checker:
                raise ValueError('author_checker.py differs from original H7 code')
        else:
            AUTHOR.parent.mkdir(parents=True, exist_ok=True)
            AUTHOR.write_text(exact_checker, encoding='utf-8')
    else:
        exact_checker = AUTHOR.read_text(encoding='utf-8')

    # Each unsafe mutation keeps the topology unless the metadata itself is
    # the object under review. The bad semantics are explicit in Vietnamese.
    cases = [
        ('M01_no_capacity_lock', ['T13'], 'unsafe_action',
         'Nhận việc nhưng không khóa phạm vi, không giữ chỗ; có thể vượt trần.',
         lambda h: transition(h, 'T13', 'lần nhận +1; thế hệ +1; biên nhận «nhận»')),
        ('M02_reaper_without_guard', ['T19', 'T20'], 'unsafe_action',
         'Thu hồi không kiểm thế hệ hoặc hạn hiện tại; có thể thu hồi lượt đã được gia hạn.',
         lambda h: transition(transition(h, 'T19', 'thế hệ +1; nhả chỗ'),
                              'T20', 'thế hệ +1; nhả chỗ')),
        ('M03_unbounded_but_word_tran', ['T17'], 'unsafe_action',
         'Gia hạn vô hạn nhưng có từ trần trong câu phủ định; thử khả năng kiểm vòng.',
         lambda h: transition(h, 'T17', 'gia hạn vô hạn; không có trần')),
        ('M04_resend_unsafe', ['T24'], 'unsafe_action',
         'Lỗi tạm không an toàn vẫn gửi lại ngay với mã mới trước khi đối soát.',
         lambda h: transition(h, 'T24', 'gửi lại ngay, đổi mã thao tác, không cần đối soát trước')),
        ('M05_cancel_without_revoke', ['T90'], 'unsafe_action',
         'Nhận yêu cầu huỷ nhưng không thu hồi lượt; cho người cũ tiếp tục tác động.',
         lambda h: transition(h, 'T90', 'ghi yêu cầu huỷ; không thu hồi lượt; không tăng thế hệ; cho lượt cũ tiếp tục tác động')),
        ('M06_discard_late_evidence', ['T70'], 'unsafe_action',
         'Nhận câu trả lời đối soát nhưng bỏ bằng chứng thay vì ghi CAT-238.',
         lambda h: transition(h, 'T70', 'bỏ bằng chứng; không ghi CAT-238*')),
        ('M07_claim_guard_always_true', ['T10', 'T11', 'T12', 'T13'], 'unsafe_guard_definition',
         'Định nghĩa được nhận luôn đúng kể cả hết M, quá hạn hoặc hết chỗ.',
         lambda h: edit_row(h, 'Bảng Giá trị', 'xin nhận', {1:
             'được: luôn luôn, kể cả đã hết M, quá hạn hoặc hết chỗ; các giá trị hết M, quá hạn, hết chỗ không bao giờ được chọn'})),
        ('M08_absent_means_not_done', ['T64'], 'unsafe_guard_definition',
         'Cho phép coi tra chưa thấy là chắc chưa làm, dù lệnh cũ còn đang bay và không có chống trùng.',
         lambda h: edit_row(h, 'Bảng Giá trị', 'đối soát', {1:
             'chắc chưa làm: chỉ cần tra chưa thấy, kể cả lệnh cũ đang xử lý; chưa thấy, có chống trùng: không cần bên nhận chống trùng; đủ / một phần / sai / không kết luận giữ nguyên'})),
        ('M09_invalid_holder_and_timer', ['state:Đang chạy'], 'unsafe_state_metadata',
         'Trạng thái đang chạy tuyên bố không có người giữ và không có lịch kiểm.',
         lambda h: edit_row(h, 'Bảng Trạng thái', 'Đang chạy', {2:
             'không có người giữ', 3: 'không có lịch kiểm'})),
        ('M10_terminal_without_cleanup', ['T41'], 'unsafe_action',
         'Đi tới Đạt nhưng không ghi trạng thái đóng, bỏ bằng chứng và giữ chỗ mãi.',
         lambda h: transition(h, 'T41', 'không ghi trạng thái đóng; bỏ bằng chứng; giữ chỗ mãi')),
        ('M11_remove_all_value_definitions', ['Bảng Giá trị:all rows'], 'missing_guard_definitions',
         'Xóa tất cả hàng định nghĩa điều kiện; chỉ giữ tên miền giá trị và tuyến trong hai bảng còn lại.',
         empty_values),
        ('C01_delete_T13', ['T13'], 'positive_control',
         'Xóa tuyến nhận thành công: checker phải báo thiếu tuyến và ca thử trượt.',
         lambda h: edit_row(h, 'Bảng Chuyển trạng thái', 'T13', None)),
        ('C02_empty_holder', ['state:Đang chạy'], 'positive_control',
         'Để trống người giữ: checker phải báo invariant 6.',
         lambda h: edit_row(h, 'Bảng Trạng thái', 'Đang chạy', {2: ''})),
        ('C03_unbounded_without_word_tran', ['T17'], 'positive_control',
         'Cùng nghĩa gia hạn vô hạn nhưng không có từ trần: checker phải báo vòng.',
         lambda h: transition(h, 'T17', 'gia hạn vô hạn')),
    ]
    results = []
    baseline = run_checker(document, 'baseline')
    print('BASELINE', json.dumps(baseline, ensure_ascii=False))
    if not baseline['author_accepts']:
        raise RuntimeError('Baseline does not reproduce author acceptance')
    for case_id, targets, category, explanation, apply in cases:
        changed = apply(document)
        if changed == document:
            raise AssertionError(f'No mutation applied for {case_id}')
        diff_path = OUT / f'{case_id}.diff'
        diff_path.write_text(''.join(difflib.unified_diff(
            document.splitlines(True), changed.splitlines(True),
            fromfile='original/ban-duyet.html', tofile=f'{case_id}/ban-duyet.html', n=1,
        )), encoding='utf-8')
        result = dict(id=case_id, targets=targets, category=category,
                      explanation=explanation, diff_file=str(diff_path),
                      mutated_html_sha256=digest(changed.encode('utf-8')),
                      **run_checker(changed, case_id))
        results.append(result)
        print(case_id, 'ACCEPT' if result['author_accepts'] else 'REJECT',
              'errors=', result['invariant_errors'],
              'tests=', f"{result['tests_passed']}/{result['tests_total']}",
              'exit=', result['exit_code'])
    unsafe = [r for r in results if r['category'] != 'positive_control']
    controls = [r for r in results if r['category'] == 'positive_control']
    probes = probe_original(document)
    failure_reasons = []
    if any(r['author_accepts'] for r in unsafe):
        failure_reasons.append('unsafe_mutation_accepted')
    if any(r['author_accepts'] for r in controls):
        failure_reasons.append('positive_control_not_detected')
    if any(not r['author_accepts'] and r['exit_code'] == 0 for r in results):
        failure_reasons.append('H7_reported_failure_but_exited_zero')
    report = dict(
        provenance=dict(
            source_path=str(SOURCE), source_slice_sha256=digest(source_bytes),
            collab_path=str(COLLAB) if collab_bytes is not None else None,
            collab_slice_sha256=digest(collab_bytes) if collab_bytes is not None else None,
            author_checker_sha256=digest(exact_checker.encode('utf-8')),
            checker_verified_against_COLLAB=(collab_bytes is not None),
            adaptation='Original H7 Python unchanged; expected relative HTML path provided in isolated temporary cwd per case.',
        ),
        baseline=baseline, results=results, direct_probes=probes,
        audit_verdict=dict(
            exit_code=1 if failure_reasons else 0,
            failure_reasons=failure_reasons,
            scope='Static checker audit only; a clean baseline is not deployment or live PostgreSQL PASS.',
        ),
        totals=dict(unsafe_mutations=len(unsafe),
                    unsafe_accepted=sum(r['author_accepts'] for r in unsafe),
                    controls=len(controls),
                    controls_rejected=sum(not r['author_accepts'] for r in controls),
                    all_process_exit_codes_zero=all(r['exit_code'] == 0 for r in results)),
        source_snapshots_unchanged=(SOURCE.read_bytes() == source_bytes and
            (collab_bytes is None or COLLAB.read_bytes() == collab_bytes)),
        author_checker_unchanged=(AUTHOR.read_text(encoding='utf-8') == exact_checker),
    )
    (OUT / 'results.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    lines = [
        '# H7 mutation audit', '',
        'Baseline: ' + json.dumps(baseline, ensure_ascii=False), '',
        '| Case | Targets | Category | H7 errors | H7 tests | Exit | Author criterion |',
        '|---|---|---|---:|---|---:|---|',
    ]
    for r in results:
        lines.append(f"| {r['id']} | {', '.join(r['targets'])} | {r['category']} | {r['invariant_errors']} | {r['tests_passed']}/{r['tests_total']} | {r['exit_code']} | {'ACCEPT' if r['author_accepts'] else 'REJECT'} |")
    lines += ['', 'Totals: ' + json.dumps(report['totals'], ensure_ascii=False), '',
              'Audit verdict: ' + json.dumps(report['audit_verdict'], ensure_ascii=False), '',
              'Original source snapshots unchanged: ' + str(report['source_snapshots_unchanged']), '',
              'The accepted mutations demonstrate blind spots in the checker, not that those malicious mutations are present in the source.',
              'No deployment, PostgreSQL write, remote write, or change to the original H7 Python code was performed.']
    (OUT / 'report.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print('TOTALS', json.dumps(report['totals'], ensure_ascii=False))
    print('COVERAGE', json.dumps(probes['coverage'], ensure_ascii=False))
    for probe in probes['probes']:
        print('PROBE', json.dumps(probe, ensure_ascii=False))
    print('SOURCE_UNCHANGED', report['source_snapshots_unchanged'])
    print('AUDIT_VERDICT', json.dumps(report['audit_verdict'], ensure_ascii=False))
    # Write all evidence first, then make this audit usable as an automated gate.
    raise SystemExit(report['audit_verdict']['exit_code'])


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        print(f'AUDIT_INFRASTRUCTURE_OR_INCOMPLETE_RESULTS: {exc}', file=sys.stderr)
        raise SystemExit(2) from exc
