#!/usr/bin/env python3
# ==== CÔNG CỤ QUY TRÌNH · nguồn chuẩn: GitHub incomex-workspace · work/mow-mot-moit-mout/cong-cu/ ====
# Mã:           dot-process-gate (CAT-006 · chưa đăng ký dot_tools)
# Thuộc:        🔁 Chung — Nhà máy dùng trước RUN; Máy dùng lại bằng đổi đầu vào
# Process dùng: CHUNG.APQUYTRINH · Áp dụng quy trình trước khi làm · D56/D57
# Phạm vi kiểm: K18 · governance.process · gate; K11 chỉ exact code/name, semantic overlap OPEN
# Việc:         Chặn PROCESS thiếu/sai/không có, definition trùng, tên chuẩn hóa trùng,
#               nhãn Thuộc sai hoặc quy trình không có bước đúng khuôn đọc/ghi/gọi.
# Đầu vào:      --prompt PROMPT.md --catalog ban-duyet.html; chỉ đọc definition trong ml5-cho-ai
# Đầu ra:       PROCESS_GATE PASS|BLOCK · process=… · catalog=sha256 · reason=…; --json cho máy
# Cách chạy:    python3 dot-process-gate.py --prompt PROMPT.md --catalog ban-duyet.html [--json]
# Cần:          Python ≥ 3.8 · chỉ stdlib · không network/secret · không ghi file
# Ca thử:       PROMPT tại fbbe0415134e87dd1fa997ff9e509dfd17021109 + catalog sau đăng ký P0 A01
# Kết quả mong đợi: PASS · process=CHUNG.APQUYTRINH · process_count=39 · exit 0
#               Không PROCESS / mã chưa có / duplicate code hoặc tên chuẩn hóa → BLOCK · exit 1
#               Không đọc được UTF-8 / không có đúng một ml5-cho-ai → BLOCK · exit 2
# Giới hạn:     Không chứng minh process phù hợp/lạc hậu/chồng nghĩa, tool đủ quyền/chạy được,
#               READY/SHA hợp lệ, hoặc đã hard-block gateway. P0 vẫn phải kiểm các điều này.
# Luật:         Gate E1 theo D56/D57; không đếm cứng 39, không thay quyền Owner/Host.
# Chép lên VPS: chỉ theo lệnh riêng; RUN A01 không chép/chạy trên VPS.
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

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'details':
            self.depth += 1
            if attrs.get('id') == 'ml5-cho-ai':
                self.blocks += 1
                self.active = self.depth
        if self.active is None:
            return
        if tag == 'p':
            self.paragraph = {'prefix': [], 'code': [], 'rest': [], 'seen_bold': False}
        elif tag == 'b' and self.paragraph is not None:
            if not self.paragraph['seen_bold']:
                self.paragraph['seen_bold'] = True
                self.bold = True

    def handle_data(self, data):
        p = self.paragraph
        if self.active is None or p is None:
            return
        p['code' if self.bold else ('rest' if p['seen_bold'] else 'prefix')].append(data)

    def handle_endtag(self, tag):
        if tag == 'b':
            self.bold = False
        if tag == 'p' and self.paragraph is not None:
            p, self.paragraph = self.paragraph, None
            code = ''.join(p['code']).strip()
            if not ''.join(p['prefix']).strip() and re.fullmatch(CODE, code):
                self.definitions.append((code, ''.join(p['rest']).strip()))
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
    definitions = []
    for process_code, rest in parser.definitions:
        label = next((label for label in LABELS if rest.startswith(label)), '')
        if label:
            rest = rest[len(label):].lstrip('\ufe0f').strip()
        name, separator, body = rest.partition(': ')
        definitions.append({'code': process_code, 'label': label, 'name': name.strip(),
                            'steps': parse_steps(body) if separator else 0})
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
    result.update(status='PASS', reason='OK', step_count=target[0]['steps'])
    return result, 0


def main(argv=None):
    parser = argparse.ArgumentParser(description='P0/E1: kiểm PROCESS trước READY/RUN; chỉ đọc, không ghi.')
    parser.add_argument('--prompt', required=True)
    parser.add_argument('--catalog', required=True)
    parser.add_argument('--json', action='store_true')
    args = parser.parse_args(argv)
    result = {'status': 'BLOCK', 'process': '', 'catalog_sha256': '', 'prompt_sha256': '',
              'reason': 'INPUT_ERROR', 'process_count': 0}
    try:
        prompt = Path(args.prompt).read_bytes()
        result['prompt_sha256'] = hashlib.sha256(prompt).hexdigest()
        catalog = Path(args.catalog).read_bytes()
        result['catalog_sha256'] = hashlib.sha256(catalog).hexdigest()
        result, code = evaluate(prompt, catalog)
    except (OSError, UnicodeError, ValueError) as error:
        result['reason'] = 'INPUT_PARSE_ERROR=' + str(error)
        code = 2
    if args.json:
        print(json.dumps(result, ensure_ascii=False))
    else:
        print('PROCESS_GATE %s · process=%s · catalog=%s · reason=%s' %
              (result['status'], result['process'] or '—', result['catalog_sha256'] or '—', result['reason']))
    return code


if __name__ == '__main__':
    sys.exit(main())
