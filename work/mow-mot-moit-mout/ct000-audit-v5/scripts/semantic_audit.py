#!/usr/bin/env python3
"""Read-only semantic probes for the pinned CT-000 transition specification.

This deliberately does not import the author's checker or execute PG/Directus.
It parses the HTML independently, proves which named table edges form each
trace, and models only the few data operations explicitly identified below.
Prose ambiguities are labelled as such; no trace is a production runtime test.
"""
import argparse
import hashlib
import html
import json
import re
import sys
from pathlib import Path


# These hashes bind literal predicate interpretations to reviewed source cells.
# A changed definition is UNKNOWN and requires review; it is never automatically
# labelled fixed or carried forward as an old finding.
EXPECTED_DEFINITIONS = {
    'S1.deadlines': 'd300487af5a139008cb6a08a00814cfa7b9edf9c88fd574197918684827e29f9',
    'S1.TT_wait': '6da0e1b929188a789deed9215bea7718c61734e912c4df2f09ac870f8b7a368a',
    'S2.compensation_state': '2f8ea26f9fe5d1fb972b1865df79d80041a607db67a1e1ca36e3478cd0169452',
    'S2.transaction_rule': '896d77d875b3c8b80f656939e56c7fbe2e4e11c9e2799ccbdec4755645924d2b',
    'S2.compensation_outgoing': 'f6b65f04a96a13dcec7803b4a16480a730c65cd6660d47a6155e8e8595cd6df7',
    'S3.owner_assignment': '65f28942b2cdef71e2f1e09ccc255782c763a86e4093c309eacf633c2dade6e0',
    'S3.queue_filter': '457ae6aa26863ad34a0ffe2422942188b81eebaea71a155a06bfa16c7da0eaed',
    'S3.claim_classifier': '534521a217c5b38633875f42cc1ae4f00c82981ac9239bf1fb73b5925e23a906',
    'S3.cancel_entry': 'c913edaeea02b9a436f71a6c091c2bd99d617e409411573c8cad125c63417c9c',
    'S4.G1_classifier': 'a10ebfa8248a78adc1080d4bf328438591d20660371dbe93da3f04bd0b956413',
    'S4.exemption_action': 'df1d76d3f92f0c82455f9e6d669b01e4b9625e65fcc17100ca93d4724aec3639',
    'S5.effect_precondition': '281282012731302d4a8465fa52326f214aa9ee40f9f4e3246bbf94174ea65336',
    'S5.unique_intent_rule': '2c00fe656eb1cb6934b0869c1b94c913b393f82faa82dcdb0ea109220e55a93e',
    'S5.operation_receipts': '766317814ec5fe37d4d4cb1d82babcb213abaf05c52110c5694ef91c670d578d',
    'S5.safe_retry': '027c46d68d177884c5ede0d6abeb0ce3e959b9e35fd3db7c17ef5c49b29ea315',
}


def definition_digest(value):
    encoded = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()
    return hashlib.sha256(encoded).hexdigest()


def clean(value):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]*>", "", value))).strip()


def read_table(source, name):
    marker = 'head-label">' + name + '<'
    at = source.index(marker)
    fragment = source[at:source.index('</table>', at)]
    body = re.search(r'<tbody>(.*?)</tbody>', fragment, re.S).group(1)
    rows = []
    for row in re.findall(r'<tr>(.*?)</tr>', body, re.S):
        cells = [clean(c) for c in re.findall(r'<td[^>]*>(.*?)</td>', row, re.S)]
        if cells:
            rows.append(cells)
    return rows


def variants(value):
    """Return (expanded string, placeholder bindings) from table syntax."""
    match = re.search(r'\s*\[([A-Za-z]+):\s*([^]]+)\]', value)
    if match:
        key = match.group(1)
        template = value[:match.start()].strip()
        result = []
        for item in match.group(2).split(','):
            item = item.strip()
            for expanded, bindings in variants(template.replace('{' + key + '}', item)):
                result.append((expanded, dict(bindings, **{key: item})))
        return result
    return [(item.strip(), {}) for item in value.split(' + ')]


class Model:
    def __init__(self, source):
        self.source = source
        self.states = {}
        for name, kind, holder, check, domain in read_table(source, 'Bảng Trạng thái'):
            for expanded, _ in variants(name):
                events = {}
                if domain != '—':
                    for declaration in domain.split(' ; '):
                        event, values = declaration.split(':', 1)
                        events[event.strip()] = [x.strip() for x in values.split(' / ')]
                if kind != 'kết thúc':
                    events['yêu cầu huỷ'] = ['ok']
                self.states[expanded] = {'kind': kind, 'holder': holder, 'check': check, 'events': events}
        self.rows = read_table(source, 'Bảng Chuyển trạng thái')
        self.by_id = {row[0]: row for row in self.rows}
        self.edges = {}
        for tid, origins, event, values, action, dest in self.rows:
            if origins.startswith('* trừ '):
                excluded = origins[len('* trừ '):].split(', ')
                starts = [(s, {}) for s, data in self.states.items()
                          if data['kind'] != 'kết thúc' and s not in excluded]
            else:
                starts = variants(origins)
            for origin, binding in starts:
                target = dest
                for key, value in binding.items():
                    target = target.replace('{' + key + '}', value)
                if target == '(giữ nguyên)':
                    target = origin
                for value in values.split(' / '):
                    edge = {'id': tid, 'from': origin, 'event': event, 'value': value,
                            'action': action, 'to': target}
                    self.edges.setdefault((origin, event, value), []).append(edge)

    def step(self, state, tid, value=None, return_step=None):
        row = self.by_id[tid]
        event = row[2]
        value = value or row[3].split(' / ')[0]
        hits = self.edges.get((state, event, value), [])
        assert len(hits) == 1, (state, event, value, hits)
        edge = dict(hits[0])
        assert edge['id'] == tid, (edge, tid)
        assert value in self.states[state]['events'][event], edge
        if edge['to'] == 'Chấm [bước trở lại]':
            assert return_step is not None
            edge['to'] = 'Chấm ' + return_step
        assert edge['to'] in self.states, edge
        return edge

    def trace(self, start, steps):
        state = start
        path = []
        for item in steps:
            if isinstance(item, str):
                item = {'tid': item}
            edge = self.step(state, **item)
            path.append(edge)
            state = edge['to']
        return path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--html', required=True)
    parser.add_argument('--out', required=True)
    args = parser.parse_args()
    source = Path(args.html).read_text()
    model = Model(source)
    values = dict(read_table(source, 'Bảng Giá trị'))
    assert len(model.states) == 32, len(model.states)
    assert len(model.rows) == 92, len(model.rows)
    probes = []

    # S1: No inference about timeouts: list exactly which initialization sites
    # the deadline definition names, then follow a legal TT route avoiding both.
    path = model.trace('Mới', ['T01', 'T05', 'T09', 'T13', 'T27', 'T65'])
    initializes = any(e['to'] in ('Quá hạn', 'Xét huỷ') or 'tính hạn phục hồi' in e['action'] for e in path)
    assert not initializes
    assert 'hạn phục hồi' in model.states[path[-1]['to']]['check']
    probes.append({
        'id': 'S1', 'status': 'MISSING_INITIALIZATION_IN_SPEC',
        'title': 'Normal reconciliation enters a state requiring PH without a PH initialization site',
        'valuation': {'root_deadline': 100, 'now': 10, 'recovery_deadline': None,
                      'operation_intent_exists': True, 'result_known': False},
        'trace': path, 'deadline_definition': values['3 loại hạn'],
        'observed': {'final_state': path[-1]['to'], 'recovery_deadline_initialized': initializes,
                     'required_check': model.states[path[-1]['to']]['check']},
        'fix': 'Initialize the relevant recovery deadline once on first entry to any reconciliation mode, including TT; never reset it on the wait loop.'})

    # S2: A valid cancellation path reaches Bù; there is no named event for a
    # compensation whose external outcome is unknown, or for a dead worker.
    path = model.trace('Mới', ['T01', 'T05', 'T09', 'T13', 'T90', 'T77'])
    missing = [('bù', 'Chưa biết'), ('hết hạn giữ', 'có dở'), ('đến lúc kiểm', 'quá hạn PH')]
    assert all(('Bù', event, value) not in model.edges for event, value in missing)
    probes.append({
        'id': 'S2', 'status': 'MISSING_EXECUTABLE_RECOVERY_BRANCH',
        'title': 'Compensation is temporary/atomic but its external unknown/crash path is absent',
        'valuation': {'cancel_requested': True, 'original_effect_completed': True,
                      'compensation_sent': True, 'compensation_result_receipt': False,
                      'compensating_receiver_deduplicates': False},
        'trace': path, 'compensation_state': model.states['Bù'],
        'missing_event_value_pairs': missing,
        'observed': 'The table can encode xong/lỗi/không bù được, but cannot reconcile an uncertain compensation or revoke a dead compensator. Mapping uncertain to lỗi routes T80→T82 back to Bù without an explicit safe-retry/reconciliation decision.',
        'fix': 'Specify how a compensation is claimed/executed outside a transaction and how an unknown or crashed compensation reaches reconciliation for that same compensation operation, preserving cancellation mode; apply PH expiry.'})

    # S3: Exact target of Owner reassignment is Chấm G2 even when Owner was
    # reached from a failed compensation. X2's independent cancellation filter
    # prevents confidently calling this a production duplicate effect; it is
    # reported as a route/guard disagreement instead.
    path = model.trace('Mới', ['T01', 'T05', 'T09', 'T13', 'T90', 'T77', 'T81', 'T86', 'T09'])
    assert path[-1]['to'] == 'Chờ'
    probes.append({
        'id': 'S3', 'status': 'MODE_LOSS_PROVEN_GUARD_DISAGREEMENT',
        'title': 'Owner reassigning a failed compensation returns to normal G2',
        'valuation': {'cancel_requested': True, 'original_effect_completed': True,
                      'compensation_failed_or_unavailable': True,
                      'owner_decision': 'giao lại', 'all_G2_ready_after_reassignment': True},
        'trace': path,
        'observed': {'formal_target': 'Chờ', 'cancellation_cleared_by_trace': False,
                     'X2_eligible_when_cancel_flag_is_kept': False,
                     'table_claim_value_if_only_M_deadline_capacity_are_checked': 'được'},
        'limitation': 'The code proves the destinations and absence of an explicit cancellation clear; whether an implementation would block or run depends on reconciling the X2 prose prefilter with the table-only claim path. No production duplicate execution is claimed.',
        'fix': 'Owner reassignment/continue must retain the return action and recovery purpose; reassignment during Bù returns to the compensation action, not the original business G2. Any withdrawal of cancellation must be a separate explicit recorded decision.'})

    # S4: Unlike the G4 exemption ambiguity, G1 uses != Đúng.  A valid waiver
    # fails this condition whether kept separate from Sai or written as the
    # distinct value Được miễn. Model exactly that predicate, not a full gate.
    conditions = {f'G1.{i}': 'Đúng' for i in range(1, 10)}
    conditions['G1.5'] = 'Được miễn'
    literal_g1_value = 'thiếu' if any(conditions[f'G1.{i}'] != 'Đúng' for i in range(1, 9)) else 'đủ'
    assert literal_g1_value == 'thiếu'
    path = model.trace('Chờ Owner', [{'tid': 'T87', 'return_step': 'G1'}, {'tid': 'T02', 'value': literal_g1_value}])
    probes.append({
        'id': 'S4', 'status': 'LITERAL_GATE_CONTRADICTION',
        'title': 'Valid Owner waiver cannot pass the G1 missing-field predicate',
        'valuation': {'conditions': conditions, 'waiver': {'question': 'G1.5', 'scope_matches': True, 'in_force': True}},
        'trace': path, 'predicate': values['chấm G1'],
        'observed': {'classifier_output': literal_g1_value, 'final_state': path[-1]['to']},
        'fix': 'Compute effective pass = Đúng or a valid scoped waiver before every failure/unknown/missing predicate, including G1; failure predicates must ignore effectively passing questions.'})

    # S5: Model ONLY the stated unique (operation, intent) constraint and the
    # stated rule "ghi được mới làm". This is not an actual PG experiment.
    path = model.trace('Mới', ['T01', 'T05', 'T09', 'T13', 'T23', 'T13'])
    operation = 'V1:B1:1'
    intents = set()
    first_inserted = operation not in intents
    intents.add(operation)
    retry_inserted = operation not in intents
    assert first_inserted and not retry_inserted
    probes.append({
        'id': 'S5', 'status': 'DECLARED_CONSTRAINT_VS_RETRY_RULE_CONTRADICTION',
        'title': 'Same-operation retry cannot newly insert its unique intent',
        'valuation': {'operation_code_first': operation, 'operation_code_retry': operation,
                      'generation_first': 1, 'generation_retry': 2,
                      'first_intent_committed': True,
                      'first_result': 'UNAVAILABLE', 'receiver_deduplication_still_valid': True},
        'trace': path,
        'observed': {'first_intent_insert_rows': int(first_inserted),
                     'retry_intent_insert_rows_under_DO_NOTHING': int(retry_inserted),
                     'G3_ghi_duoc_moi_lam_allows_retry_effect': retry_inserted},
        'limitation': 'A small reference model of the declared UNIQUE/ON CONFLICT rule, not a PG integration test. The source does not specify a successful validated reuse/attempt-record branch.',
        'fix': 'Define a separate explicit success path for an existing matching intent: verify same operation/payload, current generation and retry safety, then append the new attempt/claim receipt; preserve the stable operation code and original unique intent.'})

    # S6: X6 exists in the surrounding prose. The finite table never names it
    # as an action, so a successful repair job needs an unspecified hook before
    # its root links can be rechecked/cleared. This is a wiring gap, not proof
    # that a future implementation cannot contain that hook.
    path = model.trace('Đang chạy', ['T21', 'T37', 'T41'])
    x6_actions = [r[0] for r in model.rows if re.search(r'\bX6\b', r[4])]
    assert not x6_actions
    probes.append({
        'id': 'S6', 'status': 'FOLLOWUP_NOT_EXECUTABLE',
        'title': 'No transition explicitly invokes X6 to recheck blocked roots after a repair',
        'valuation': {'repair_job': 'R', 'incident': 'I',
                      'root_links': {'A': 'Còn chặn', 'B': 'Còn chặn'},
                      'repair_G4_and_G5_pass': True},
        'trace': path,
        'observed': {'formal_final_state': path[-1]['to'], 'transition_action_cells_calling_X6': x6_actions},
        'limitation': 'X6 is documented in the prose. The absent piece is its explicit trigger/action linkage from the advertised sole execution table; a hidden MOW or periodic predicate could implement it, but that is not specified by these 92 rows.',
        'fix': 'Attach X6 to a specified repair-result transition, including per-root evidence/counter updates and wakeups; make that invocation part of the same formal contract and test a repair shared by two roots.'})

    # Include one current positive control so these probes do not imply the
    # basic success route or cancellation mode itself is universally broken.
    success = model.trace('Mới', ['T01', 'T05', 'T09', 'T13', 'T21', 'T37', 'T41'])
    cancel = model.trace('Mới', ['T01', 'T05', 'T09', 'T13', 'T90', 'T76', 'T66', 'T79'])
    phase = {r[0]: r for r in read_table(source, 'Bảng Giai đoạn và cổng')}
    pg = {r[0]: r for r in read_table(source, 'Bảng Yêu cầu cho PG')}
    xsteps = {r[0]: r for r in read_table(source, 'Bảng Bước xử lý lỗi (X1–X9)')}
    ledger = {r[0]: r for r in read_table(source, 'Bảng Sổ của vòng xử lý')}
    definitions = {
        'S1.deadlines': values['3 loại hạn'],
        'S1.TT_wait': model.states['Chờ người·ĐS·TT'],
        'S2.compensation_state': model.states['Bù'],
        'S2.transaction_rule': pg['4'],
        'S2.compensation_outgoing': [r for r in model.rows if r[1] == 'Bù'],
        'S3.owner_assignment': model.by_id['T86'],
        'S3.queue_filter': xsteps['X2'],
        'S3.claim_classifier': values['xin nhận'],
        'S3.cancel_entry': model.by_id['T90'],
        'S4.G1_classifier': values['chấm G1'],
        'S4.exemption_action': model.by_id['T87'],
        'S5.effect_precondition': phase['G3Thực hiện'],
        'S5.unique_intent_rule': pg['2'],
        'S5.operation_receipts': ledger['CAT-238* Sổ lệnh · lần gửi'],
        'S5.safe_retry': model.by_id['T23'],
    }
    for probe in probes:
        checks = []
        for key, expected in EXPECTED_DEFINITIONS.items():
            if key.startswith(probe['id'] + '.'):
                actual = definition_digest(definitions[key])
                checks.append({'definition': key, 'expected_sha256': expected,
                               'actual_sha256': actual, 'matches': expected == actual})
        if checks:
            probe['applicability_guards'] = checks
            if not all(check['matches'] for check in checks):
                probe['status'] = 'NOT_EVALUATED_REVIEW_REQUIRED'
                probe['observed'] = None
                probe['limitation'] = ('Source predicate/action definitions changed. '
                    'This version-scoped interpretation has not been revalidated; '
                    'neither the previous finding nor a fix is asserted.')
    unknown = [p['id'] for p in probes if p['status'] == 'NOT_EVALUATED_REVIEW_REQUIRED']
    findings = [p['id'] for p in probes if p['status'] not in
                ('NOT_EVALUATED_REVIEW_REQUIRED', 'FOLLOWUP_NOT_EXECUTABLE')]
    code = 2 if unknown else 1 if findings else 0
    report = {'input': str(Path(args.html).resolve()),
              'sha256': hashlib.sha256(source.encode()).hexdigest(),
              'method': 'Independent HTML parser + exact named-edge traces + narrowly stated data predicates; no author-checker imports, PG calls, remote writes, or invented implementation effects.',
              'table_counts': {'states': len(model.states), 'transitions': len(model.rows)},
              'positive_controls': {'success': success, 'ordinary_cancel_after_reconciliation': cancel},
              'verdict': 'NOT_EVALUATED_REVIEW_REQUIRED' if unknown else 'FINDINGS_REMAIN' if findings else 'PASS',
              'exit_code': code, 'finding_ids': findings, 'unknown_ids': unknown,
              'probes': probes}
    Path(args.out).write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'counts': report['table_counts'],
                      'positive_controls': {k: v[-1]['to'] for k, v in report['positive_controls'].items()},
                      'probes': [{'id': p['id'], 'status': p['status'],
                                  'trace': [e['id'] for e in p['trace']]} for p in probes],
                      'out': args.out, 'exit_code': code}, ensure_ascii=False, indent=2))
    return code


if __name__ == '__main__':
    try:
        result = main()
    except Exception as error:
        # Fail closed on a changed table syntax/domain/path as well as on an
        # implementation error in this audit; never turn such a failure green.
        failure = {'verdict': 'NOT_EVALUATED_REVIEW_REQUIRED', 'exit_code': 2,
                   'error': type(error).__name__ + ': ' + str(error),
                   'finding_ids': [], 'unknown_ids': ['audit_execution'], 'probes': []}
        if '--out' in sys.argv:
            try:
                Path(sys.argv[sys.argv.index('--out') + 1]).write_text(
                    json.dumps(failure, ensure_ascii=False, indent=2) + '\n')
            except Exception:
                pass
        print(json.dumps(failure, ensure_ascii=False, indent=2))
        result = 2
    sys.exit(result)
