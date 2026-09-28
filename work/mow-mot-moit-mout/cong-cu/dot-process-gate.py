#!/usr/bin/env python3
# ==== CÔNG CỤ QUY TRÌNH · nguồn chuẩn: GitHub incomex-workspace · work/mow-mot-moit-mout/cong-cu/ ====
# Mã:           dot-process-gate (CAT-006 · chưa đăng ký dot_tools)
# Thuộc:        🔁 Chung — Nhà máy dùng trước RUN; Máy dùng lại bằng đổi đầu vào
# Process dùng: CHUNG.APQUYTRINH · Áp dụng quy trình trước khi làm · D56/D57
# Phạm vi kiểm: K18 · governance.process · gate; K11 chỉ exact code/name, semantic overlap OPEN
# Việc:         E1 chặn PROCESS thiếu/sai/trùng hoặc bước sai khuôn; A02 kiểm contract v1
#               trên process opt-in và rà coverage toàn catalog, giữ E1 cho process cũ.
# Đầu vào:      --prompt PROMPT.md --catalog ban-duyet.html; chỉ đọc definition trong ml5-cho-ai
# Đầu ra:       PROCESS_GATE PASS|BLOCK; CONTRACT_AUDIT PASS|BLOCK; --json cho máy
# Cách chạy:    python3 dot-process-gate.py --prompt PROMPT.md --catalog ban-duyet.html [--json]
#               python3 dot-process-gate.py --audit-contracts --catalog ban-duyet.html [--json]
# Cần:          Python ≥ 3.8 · chỉ stdlib · không network/secret · không ghi file
# Ca thử:       A02 · PROMPT f39ca2d + catalog ba8096a + 13 fixture contract riêng
# Kết quả mong đợi: E1 PASS · process=CHUNG.APQUYTRINH · process_count=39 · exit 0
#               Không PROCESS / mã chưa có / duplicate code hoặc tên chuẩn hóa → BLOCK · exit 1
#               Không đọc được UTF-8 / không có đúng một ml5-cho-ai → BLOCK · exit 2
#               Opt-in thiếu/sai contract → BLOCK · exit 1; audit cho coverage và lỗi.
# Giới hạn:     Không chứng minh process phù hợp/lạc hậu/chồng nghĩa, tool đủ quyền/chạy được,
#               READY/SHA hợp lệ, hoặc đã hard-block gateway. P0 vẫn phải kiểm các điều này.
# Contract v1: chỉ kiểm metadata đã opt-in; không phán đúng/sai nghiệp vụ.
# --audit-contracts: thống kê coverage + lỗi toàn catalog, chỉ đọc, không cần PROMPT.
# Luật:         Gate E1 theo D56/D57; không đếm cứng 39, không thay quyền Owner/Host.
# Chép lên VPS: chỉ theo lệnh riêng; RUN A02 không chép/chạy trên VPS.
import argparse
import collections
import hashlib
import json
import re
import sys
import unicodedata
from html.parser import HTMLParser
from pathlib import Path

CODE = r'[A-Z0-9_]+\.[A-Z0-9_]+'
LABELS = ('🏗', '⚙️', '⚙', '🔁', '📦')
RIGHT_CLASSES = frozenset(('REQUESTER', 'APPROVER', 'EDITOR', 'CONFIGURATOR',
                           'ACTIVATOR', 'ASSIGNEE', 'CONTRIBUTOR', 'VIEWER'))
UI_INTENTS = frozenset(('SEARCH', 'REQUEST', 'REVIEW', 'EDIT', 'CONFIGURE',
                        'ACTIVATE', 'EXECUTE', 'ATTACH', 'VIEW'))
PROCESS_CONTRACT_ATTRS = ('data-when', 'data-input-contract', 'data-output-contract',
                          'data-return-contract', 'data-contract-source')
STEP_CONTRACT_ATTRS = ('data-step-key', 'data-right-class', 'data-state-in',
                       'data-state-out', 'data-return', 'data-ui-intent')


class CatalogParser(HTMLParser):
    """Giữ từng definition, không dùng dict làm mất mã trùng; bỏ text ngoài khối canonical."""
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.depth = 0
        self.active = None
        self.blocks = 0
        self.paragraph = None
        self.bold = False
        self.definitions = []
        self.span_stack = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'details':
            self.depth += 1
            if attrs.get('id') == 'ml5-cho-ai':
                self.blocks += 1
                self.active = self.depth
        if self.active is None:
            return
        for span in self.span_stack:
            if span is not None:
                span['empty'] = False
        if tag == 'p':
            self.paragraph = {'prefix': [], 'code': [], 'rest': [], 'seen_bold': False,
                              'attrs': attrs, 'spans': []}
            self.span_stack = []
        elif tag == 'b' and self.paragraph is not None:
            if not self.paragraph['seen_bold']:
                self.paragraph['seen_bold'] = True
                self.bold = True
        elif tag == 'span' and self.paragraph is not None:
            span = None
            if 'proc-contract' in attrs.get('class', '').split():
                span = {'attrs': attrs,
                        'offset': len(''.join(self.paragraph['rest'])),
                        'empty': True, 'closed': False}
                self.paragraph['spans'].append(span)
            self.span_stack.append(span)

    def handle_data(self, data):
        p = self.paragraph
        if self.active is None or p is None:
            return
        if data:
            for span in self.span_stack:
                if span is not None:
                    span['empty'] = False
        p['code' if self.bold else ('rest' if p['seen_bold'] else 'prefix')].append(data)

    def handle_endtag(self, tag):
        if tag == 'span' and self.span_stack:
            span = self.span_stack.pop()
            if span is not None:
                span['closed'] = True
        if tag == 'b':
            self.bold = False
        if tag == 'p' and self.paragraph is not None:
            p, self.paragraph = self.paragraph, None
            code = ''.join(p['code']).strip()
            if not ''.join(p['prefix']).strip() and re.fullmatch(CODE, code):
                raw_rest = ''.join(p['rest'])
                leading = len(raw_rest) - len(raw_rest.lstrip())
                for span in p['spans']:
                    span['offset'] -= leading
                self.definitions.append((code, raw_rest.strip(),
                                         p['attrs'], p['spans']))
            self.span_stack = []
        if tag == 'details':
            if self.depth == self.active:
                self.active = None
            self.depth -= 1


def normalized_name(name):
    return ' '.join(unicodedata.normalize('NFKC', name).casefold().split())


def parse_steps(body):
    parts = re.split(r'(?:^| → )(?=(?:👤|🤖|↪) )', body)
    count = 0
    for part in parts:
        part = part.strip()
        if not part:
            continue
        if part.startswith('↪ '):
            if not re.fullmatch(CODE, part[2:].strip()):
                return 0
        else:
            m = re.fullmatch(r'(?:👤|🤖) .+ \[ghi (.*?) \| đọc (.*?)\]', part, re.S)
            if not m:
                return 0
            refs = []
            for value in m.groups():
                if value.strip() in ('', '—', '-'):
                    continue
                tokens = value.split()
                if any(not re.fullmatch(r'\d+→?', token) for token in tokens):
                    return 0
                refs.extend(tokens)
            if not refs:
                return 0
        count += 1
    return count


def build_definitions(parser):
    definitions = []
    for process_code, rest, attrs, spans in parser.definitions:
        original_rest = rest
        label = next((label for label in LABELS if rest.startswith(label)), '')
        if label:
            rest = rest[len(label):].lstrip('\ufe0f').strip()
            # Offsets were captured before removing the visible scope label.
            removed = len(original_rest) - len(rest)
            for span in spans:
                span['offset'] -= removed
        name, separator, body = rest.partition(': ')
        definitions.append({'code': process_code, 'label': label, 'name': name.strip(),
                            'steps': parse_steps(body) if separator else 0,
                            'body': body, 'body_start': len(rest) - len(body),
                            'attrs': attrs, 'spans': spans})
    return definitions


def direct_step_ranges(body):
    boundaries = list(re.finditer(r'(?:^| → )(?=(?:👤|🤖|↪) )', body))
    return [(match.end(), boundaries[index + 1].start()
             if index + 1 < len(boundaries) else len(body))
            for index, match in enumerate(boundaries)]


def audit_contracts(definitions):
    errors = []
    opt_in = [p for p in definitions if p['attrs'].get('data-contract-v') == '1']
    unversioned = [p['code'] for p in definitions
                   if p['attrs'].get('data-contract-v') != '1']
    keys = collections.defaultdict(list)
    human_count = 0

    def add(process, reason, step=None):
        item = {'process': process, 'error': reason}
        if step is not None:
            item['step'] = step
        errors.append(item)

    for process in opt_in:
        code, attrs = process['code'], process['attrs']
        for field in PROCESS_CONTRACT_ATTRS:
            if not (attrs.get(field) or '').strip():
                add(code, 'MISSING_PROCESS_ATTR=' + field)

        ranges = direct_step_ranges(process['body'])
        human = {index: [] for index, (start, end) in enumerate(ranges, 1)
                 if process['body'][start:end].startswith('👤 ')}
        human_count += len(human)
        for span in process['spans']:
            offset = span['offset'] - process['body_start']
            match = next((index for index, (start, end) in enumerate(ranges, 1)
                          if index in human and start + len('👤 ') < offset <= end), None)
            if match is None:
                add(code, 'ORPHAN_STEP_CONTRACT')
            else:
                human[match].append(span)
            if not span['empty'] or not span['closed']:
                add(code, 'STEP_SPAN_NOT_EMPTY_OR_CLOSED', match)
            fields = span['attrs']
            for field in STEP_CONTRACT_ATTRS:
                if not (fields.get(field) or '').strip():
                    add(code, 'MISSING_STEP_ATTR=' + field, match)
            if fields.get('data-right-class') and fields['data-right-class'] not in RIGHT_CLASSES:
                add(code, 'RIGHT_CLASS_INVALID=' + fields['data-right-class'], match)
            if fields.get('data-ui-intent') and fields['data-ui-intent'] not in UI_INTENTS:
                add(code, 'UI_INTENT_INVALID=' + fields['data-ui-intent'], match)
            key = (fields.get('data-step-key') or '').strip()
            if key:
                keys[key].append(code)
        for index, spans in human.items():
            if len(spans) != 1:
                add(code, 'HUMAN_STEP_SPAN_COUNT=%d' % len(spans), index)

    for key, owners in keys.items():
        if len(owners) > 1:
            for code in sorted(set(owners)):
                add(code, 'DUPLICATE_STEP_KEY=' + key)
    return {'contract_processes': len(opt_in), 'contract_human_steps': human_count,
            'contract_errors': errors, 'unversioned_processes': unversioned}


def evaluate(prompt, catalog):
    result = {'status': 'BLOCK', 'process': '',
              'catalog_sha256': hashlib.sha256(catalog).hexdigest(),
              'prompt_sha256': hashlib.sha256(prompt).hexdigest(),
              'reason': '', 'process_count': 0}
    prompt_text, catalog_text = prompt.decode('utf-8'), catalog.decode('utf-8')
    lines = re.findall(r'^PROCESS:[^\r\n]*$', prompt_text, re.M)
    if len(lines) != 1:
        result['reason'] = 'PROCESS_LINE_COUNT=%d' % len(lines)
        return result, 1
    code = lines[0][len('PROCESS:'):].strip()
    result['process'] = code
    if not re.fullmatch(CODE, code):
        result['reason'] = 'PROCESS_CODE_FORMAT'
        return result, 1
    parser = CatalogParser()
    parser.feed(catalog_text)
    parser.close()
    if parser.blocks != 1 or parser.active is not None or parser.paragraph is not None:
        result['reason'] = 'CANONICAL_BLOCK_PARSE'
        return result, 2
    definitions = build_definitions(parser)
    result['process_count'] = len(definitions)
    codes = collections.Counter(p['code'] for p in definitions)
    duplicates = sorted(c for c, count in codes.items() if count > 1)
    if duplicates:
        result['reason'] = 'DUPLICATE_CODE=' + ','.join(duplicates)
        return result, 1
    names = collections.Counter(normalized_name(p['name']) for p in definitions)
    duplicates = sorted(n for n, count in names.items() if count > 1)
    if duplicates:
        result['reason'] = 'DUPLICATE_NAME=' + ','.join(duplicates)
        return result, 1
    target = [p for p in definitions if p['code'] == code]
    if len(target) != 1:
        result['reason'] = 'PROCESS_DEFINITION_COUNT=%d' % len(target)
        return result, 1
    if not target[0]['label']:
        result['reason'] = 'PROCESS_LABEL_INVALID'
        return result, 1
    if not target[0]['name'] or not target[0]['steps']:
        result['reason'] = 'PROCESS_STEPS_UNPARSEABLE'
        return result, 1
    contract = audit_contracts(definitions)
    target_errors = [error for error in contract['contract_errors']
                     if error['process'] == code]
    if target_errors:
        result['reason'] = 'PROCESS_CONTRACT_INVALID=' + target_errors[0]['error']
        result['contract_errors'] = target_errors
        return result, 1
    result.update(status='PASS', reason='OK', step_count=target[0]['steps'])
    return result, 0


def audit_catalog(catalog):
    result = {'status': 'BLOCK', 'process': '',
              'catalog_sha256': hashlib.sha256(catalog).hexdigest(),
              'prompt_sha256': '', 'reason': '', 'process_count': 0,
              'contract_processes': 0, 'contract_human_steps': 0,
              'contract_errors': [], 'unversioned_processes': []}
    parser = CatalogParser()
    parser.feed(catalog.decode('utf-8'))
    parser.close()
    if parser.blocks != 1 or parser.active is not None or parser.paragraph is not None:
        result['reason'] = 'CANONICAL_BLOCK_PARSE'
        return result, 2
    definitions = build_definitions(parser)
    result['process_count'] = len(definitions)
    result.update(audit_contracts(definitions))
    if result['contract_errors']:
        result['reason'] = 'CONTRACT_ERRORS=%d' % len(result['contract_errors'])
        return result, 1
    result.update(status='PASS', reason='OK')
    return result, 0


def main(argv=None):
    parser = argparse.ArgumentParser(description='P0/E1: kiểm PROCESS trước READY/RUN; chỉ đọc, không ghi.')
    parser.add_argument('--prompt', help='Bắt buộc với process gate; không cần cho --audit-contracts.')
    parser.add_argument('--catalog', required=True)
    parser.add_argument('--json', action='store_true')
    parser.add_argument('--audit-contracts', action='store_true',
                        help='Kiểm contract opt-in toàn catalog; không ghi.')
    args = parser.parse_args(argv)
    if not args.audit_contracts and not args.prompt:
        parser.error('--prompt is required unless --audit-contracts is set')
    result = {'status': 'BLOCK', 'process': '', 'catalog_sha256': '', 'prompt_sha256': '',
              'reason': 'INPUT_ERROR', 'process_count': 0}
    try:
        catalog = Path(args.catalog).read_bytes()
        result['catalog_sha256'] = hashlib.sha256(catalog).hexdigest()
        if args.audit_contracts:
            result, code = audit_catalog(catalog)
        else:
            prompt = Path(args.prompt).read_bytes()
            result['prompt_sha256'] = hashlib.sha256(prompt).hexdigest()
            result, code = evaluate(prompt, catalog)
    except (OSError, UnicodeError, ValueError) as error:
        result['reason'] = 'INPUT_PARSE_ERROR=' + str(error)
        code = 2
    if args.json:
        print(json.dumps(result, ensure_ascii=False))
    elif args.audit_contracts:
        print('CONTRACT_AUDIT %s · process_count=%d · contract_processes=%d · '
              'contract_human_steps=%d · contract_errors=%s · unversioned_processes=%s' %
              (result['status'], result['process_count'], result.get('contract_processes', 0),
               result.get('contract_human_steps', 0),
               json.dumps(result.get('contract_errors', []), ensure_ascii=False),
               json.dumps(result.get('unversioned_processes', []), ensure_ascii=False)))
    else:
        print('PROCESS_GATE %s · process=%s · catalog=%s · reason=%s' %
              (result['status'], result['process'] or '—', result['catalog_sha256'] or '—', result['reason']))
    return code


if __name__ == '__main__':
    sys.exit(main())
