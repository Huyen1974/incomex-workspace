#!/usr/bin/env python3
# ==== CÔNG CỤ QUY TRÌNH · nguồn chuẩn: GitHub incomex-workspace · work/mow-mot-moit-mout/cong-cu/ ====
# Mã:           dot-walk-check   (dòng trong 🛠 của ban-duyet.html · sổ công cụ = dòng 35 CAT-006 · chưa đăng ký dot_tools)
# Thuộc:        🔁 Chung — Nhà máy dùng để kiểm quy trình của Máy; Máy dùng lại cho quy trình thương mại (đổi đầu vào, không sửa mã)
# Phạm vi kiểm: K01 · assembly.workflow · verify · loại A (chỉ đọc, không ghi gì)
# Việc:         Đi bộ kiểm đủ chỗ ghi. Đọc thẳng trang Owner duyệt (một nguồn, không chép dữ liệu vào script):
#               - danh sách master = các dòng <tr id="ml3-NN"> của bảng ★ Master list (số · mã · tên · nhóm)
#               - quy trình = các đoạn <p><b>MÃ</b> [Thuộc] Tên: bước → bước …</p> trong <details id="ml5-cho-ai">
#                 mỗi bước 👤 người / 🤖 máy: "[ghi 04 46 | đọc 03 17]"; ↪ MÃ = gọi quy trình con; "18→" = danh sách đích do dòng 18 khai
#               Kiểm: (1) số dòng ghi/đọc phải có trong danh sách master; (2) quy trình con được gọi phải có;
#               (3) dòng không quy trình nào chạm chỉ được nằm trong nhóm "Chưa áp dụng"; (4) bước 👤/🤖 phải ghi hoặc đọc ít nhất một dòng;
#               (5) mỗi quy trình có nhãn Thuộc 🏗 / ⚙️ / 🔁 / 📦.
#               Luật hiển thị của trang: bước có ghi thì còn đọc 35 · 37 (khai qua DOT) — công cụ tự cộng, trang không lặp lại.
# Đầu vào:      đường dẫn tệp hoặc URL của ban-duyet.html (bỏ trống = bản main trên GitHub)
# Đầu ra:       tóm tắt + danh sách lỗi · --json in dữ liệu máy đọc · exit 0 = không lỗi · 1 = có lỗi · 2 = không đọc được đầu vào
# Cách chạy:    python3 dot-walk-check.py [tệp|URL] [--json]
# Cần:          Python ≥ 3.8, chỉ thư viện chuẩn · không bí mật · chỉ cần mạng khi đưa URL
# Ca thử:       ban-duyet.html ở commit có tiêu đề "MMIM-C12" (tra: git log --grep MMIM-C12), URL dạng
#               https://raw.githubusercontent.com/Huyen1974/incomex-workspace/<commit>/work/mow-mot-moit-mout/ban-duyet.html
# Kết quả mong đợi: 84 dòng · 38 quy trình · 👤 60 · 🤖 62 · Thuộc ⚙️ 22 · 🏗 9 · 🔁 7 · không ai chạm 77–82 (nhóm Chưa áp dụng) · LỖI 0 · exit 0
# Nguồn gốc:    dựng lại từ walk_c11.py của phiên Cowork 26/09 (C10–C11): giữ nguyên luật kiểm; đổi đầu vào từ dữ liệu chép
#               trong script sang đọc thẳng HTML, để trang Owner duyệt là nguồn duy nhất (JEV gen-dec-1790406483-lmzuig9S93lGCP4mLxdC).
# Luật:         theo TEMPLATE-DOT-SCRIPT: không đếm cứng, không danh sách cứng, exit 0/1.
# Chép lên VPS: chỉ khi phải chạy ở đó · theo lệnh · ghi sha256 + nguồn@commit vào sổ công cụ · không sửa bản chép.
import html, json, re, sys, hashlib, urllib.request, collections

DEFAULT = 'https://raw.githubusercontent.com/Huyen1974/incomex-workspace/main/work/mow-mot-moit-mout/ban-duyet.html'
ACTORS = ('👤', '🤖', '↪')
LABELS = ('🏗', '⚙️', '⚙', '🔁', '📦')
DOT_READS = (35, 37)  # luật hiển thị: bước có ghi còn đọc danh mục DOT + thao tác DOT


def load(src):
    if re.match(r'https?://', src):
        with urllib.request.urlopen(src, timeout=60) as r:
            return r.read()
    with open(src, 'rb') as f:
        return f.read()


def strip(t):
    return html.unescape(re.sub(r'<[^>]+>', '', t)).strip()


def parse_rows(s):
    a = s.find('id="ml3"')
    b = s.find('</table>', a)
    if a < 0 or b < 0:
        raise ValueError('không thấy bảng ★ Master list (id="ml3")')
    rows, group = {}, ''
    for m in re.finditer(r'<tr([^>]*)>(.*?)</tr>', s[a:b], re.S):
        attrs, body = m.group(1), m.group(2)
        if 'class="g"' in attrs:
            group = strip(body)
            continue
        mid = re.search(r'id="ml3-(\d+)"', attrs)
        if not mid:
            continue
        cells = re.findall(r'<td[^>]*>(.*?)</td>', body, re.S)
        name = re.sub(r'<small>.*?</small>', '', cells[2], flags=re.S) if len(cells) > 2 else ''
        rows[int(mid.group(1))] = {'code': strip(cells[1]) if len(cells) > 1 else '', 'name': strip(name), 'group': group}
    return rows


def parse_refs(txt):
    txt = txt.strip()
    if txt in ('', '—', '-'):
        return []
    out = []
    for tok in txt.split():
        m = re.fullmatch(r'(\d+)(→?)', tok)
        if not m:
            raise ValueError('ký hiệu dòng lạ: %r' % tok)
        out.append((int(m.group(1)), bool(m.group(2))))
    return out


def parse_procs(s):
    a = s.find('id="ml5-cho-ai"')
    b = s.find('</details>', a)
    if a < 0 or b < 0:
        raise ValueError('không thấy khối quy trình (id="ml5-cho-ai")')
    procs = collections.OrderedDict()
    for m in re.finditer(r'<p><b>([A-Z0-9_]+\.[A-Z0-9_]+)</b>(.*?)</p>', s[a:b], re.S):
        code, rest = m.group(1), html.unescape(m.group(2)).strip()
        label = next((l for l in LABELS if rest.startswith(l)), '')
        if label:
            rest = rest[len(label):].lstrip('️').strip()
        name, _, body = rest.partition(': ')
        steps = []
        for part in re.split(r'(?:^| → )(?=(?:👤|🤖|↪) )', body):
            part = part.strip()
            if not part:
                continue
            actor, text = part[0], part[2:].strip()
            if actor == '↪':
                call = text if re.fullmatch(r'[A-Z0-9_]+\.[A-Z0-9_]+', text) else None
                steps.append({'actor': actor, 'text': text, 'call': call, 'w': [], 'r': []})
                continue
            mm = re.fullmatch(r'(.*) \[ghi (.*?) \| đọc (.*?)\]', text, re.S)
            if not mm:
                raise ValueError('%s: bước không đúng khuôn [ghi … | đọc …]: %r' % (code, text[:80]))
            steps.append({'actor': actor, 'text': mm.group(1), 'call': None,
                          'w': parse_refs(mm.group(2)), 'r': parse_refs(mm.group(3))})
        procs[code] = {'label': '⚙️' if label == '⚙' else label, 'name': name, 'steps': steps}
    return procs


def check(rows, procs):
    errs, touch = [], collections.defaultdict(set)
    for code, p in procs.items():
        if not p['label']:
            errs.append((code, 'thiếu nhãn Thuộc'))
        if not p['steps']:
            errs.append((code, 'không có bước'))
        for st in p['steps']:
            if st['actor'] == '↪':
                if st['call'] and st['call'] not in procs:
                    errs.append((code, 'gọi quy trình chưa có: ' + st['call']))
                continue
            refs = st['w'] + st['r'] + ([(d, False) for d in DOT_READS] if st['w'] else [])
            if not st['w'] and not st['r']:
                errs.append((code, 'bước không ghi, không đọc: ' + st['text'][:60]))
            for n, _ in refs:
                if n not in rows:
                    errs.append((code, 'dòng không có: %02d' % n))
                touch[n].add(code)
    orphans = [n for n in sorted(rows) if n not in touch]
    for n in orphans:
        if 'chưa áp dụng' not in rows[n]['group'].lower():
            errs.append(('dòng %02d' % n, 'không quy trình nào chạm, không ở nhóm Chưa áp dụng: ' + rows[n]['name']))
    return errs, touch, orphans


def main(argv):
    args = [a for a in argv if not a.startswith('--')]
    src = args[0] if args else DEFAULT
    try:
        raw = load(src)
        s = raw.decode('utf-8')
        rows, procs = parse_rows(s), parse_procs(s)
    except Exception as e:  # noqa: BLE001 — báo rõ rồi thoát mã 2
        print('KHÔNG ĐỌC ĐƯỢC ĐẦU VÀO:', e)
        return 2
    errs, touch, orphans = check(rows, procs)
    cnt = collections.Counter(st['actor'] for p in procs.values() for st in p['steps'])
    calls = sum(1 for p in procs.values() for st in p['steps'] if st['call'])
    lab = collections.Counter(p['label'] for p in procs.values())
    if '--json' in argv:
        print(json.dumps({'source': src, 'sha256': hashlib.sha256(raw).hexdigest(), 'rows': len(rows),
                          'procs': {c: {'label': p['label'], 'name': p['name'], 'steps': len(p['steps'])} for c, p in procs.items()},
                          'human': cnt['👤'], 'machine': cnt['🤖'], 'calls': calls, 'labels': dict(lab),
                          'orphans': orphans, 'errors': errs}, ensure_ascii=False, indent=1))
    else:
        print('dot-walk-check · nguồn:', src)
        print('sha256 đầu vào:', hashlib.sha256(raw).hexdigest()[:16], '·', len(raw), 'byte')
        print('danh sách master: %d dòng · %d nhóm' % (len(rows), len({r['group'] for r in rows.values()})))
        print('quy trình: %d · bước 👤 %d · 🤖 %d · ↪ gọi quy trình con %d · ↪ ghi chú %d'
              % (len(procs), cnt['👤'], cnt['🤖'], calls, cnt['↪'] - calls))
        print('Thuộc:', ' · '.join('%s %d' % (k, v) for k, v in lab.most_common()))
        orph_ok = [n for n in orphans if 'chưa áp dụng' in rows[n]['group'].lower()]
        print('không quy trình nào chạm:', ' '.join('%02d' % n for n in orphans) or '—',
              '(nhóm Chưa áp dụng: %d)' % len(orph_ok) if orphans else '')
        print('LỖI:', len(errs))
        for e in errs:
            print('  -', e[0], '·', e[1])
    return 1 if errs else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
