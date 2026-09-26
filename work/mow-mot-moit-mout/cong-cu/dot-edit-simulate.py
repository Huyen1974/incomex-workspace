#!/usr/bin/env python3
# ==== CÔNG CỤ QUY TRÌNH · nguồn chuẩn: GitHub incomex-workspace · work/mow-mot-moit-mout/cong-cu/ ====
# Mã:           dot-edit-simulate   (dòng trong 🛠 của ban-duyet.html · sổ công cụ = dòng 35 CAT-006 · chưa đăng ký dot_tools)
# Thuộc:        🏗 Nhà máy — sửa tài liệu thiết kế trong repo (Máy ghi qua DOT/PG, không dùng công cụ này)
# Phạm vi kiểm: K03 · workspace.doc · verify (trước khi ghi) · loại A (chỉ đọc nguồn, chỉ ghi vào thư mục --out cục bộ)
# Việc:         Mô phỏng một giao dịch sửa tệp TRƯỚC khi gửi cổng ghi (fs_transaction / workspace_transaction):
#               lấy đúng bản hiện tại → áp lần lượt từng cặp old_str/new_str → mỗi old_str phải xuất hiện ĐÚNG MỘT lần
#               ở thời điểm áp → so expected_version (16 ký tự đầu sha256 của bản gốc) nếu có → ghi bản dự kiến + sha256.
#               Bản dự kiến dùng tiếp cho dot-page-shot (xem trước) và dot-push-verify (so sau khi ghi).
# Đầu vào:      OPS.json = danh sách op đúng khuôn cổng ghi: {"op":"edit","path":…,"edits":[{"old_str":…,"new_str":…}],
#               "expected_version":…} hoặc {"op":"write","path":…,"content":…}
#               Nguồn bản hiện tại: --base THƯ_MỤC (tệp ở THƯ_MỤC/<path>) hoặc --ref COMMIT|main (tải từ GitHub)
# Đầu ra:       THƯ_MỤC --out/<path> = bản dự kiến · in sha256 trước → sau · exit 0 = áp được hết · 1 = sai (old_str 0 hoặc ≥ 2 lần,
#               lệch version) · 2 = không đọc được đầu vào
# Cách chạy:    python3 dot-edit-simulate.py OPS.json (--base DIR | --ref REF) [--out DIR] [--repo OWNER/REPO]
#               python3 dot-edit-simulate.py --self-test
# Cần:          Python ≥ 3.8, chỉ thư viện chuẩn · không bí mật · mạng chỉ khi dùng --ref
# Ca thử:       --self-test (không cần mạng) → "SELF-TEST PASS: 2/2" · exit 0
#               (ca 1: sửa hợp lệ ra đúng byte; ca 2: old_str xuất hiện 2 lần phải bị bắt)
# Nguồn gốc:    dựng lại từ hàm apply() + bước mô phỏng của gen_c11.py / c10_ops.py phiên Cowork 26/09 (C09–C11): giữ luật
#               "mỗi old_str đúng một lần, áp theo thứ tự"; đổi thành công cụ nhận tham số, không đường dẫn cứng.
# Luật:         theo TEMPLATE-DOT-SCRIPT: không đường dẫn cứng, exit 0/1. Không gọi cổng ghi — chỉ mô phỏng.
# Chép lên VPS: chỉ khi phải chạy ở đó · theo lệnh · ghi sha256 + nguồn@commit vào sổ công cụ · không sửa bản chép.
import hashlib, json, os, sys, tempfile, urllib.error, urllib.parse, urllib.request

REPO = 'Huyen1974/incomex-workspace'


def sha(b):
    return hashlib.sha256(b).hexdigest()


def read_base(path, base, ref, repo):
    if base is not None:
        p = os.path.join(base, path)
        if not os.path.exists(p):
            return None
        with open(p, 'rb') as f:
            return f.read()
    url = 'https://raw.githubusercontent.com/%s/%s/%s' % (repo, ref, urllib.parse.quote(path))
    try:
        with urllib.request.urlopen(url, timeout=60) as r:
            return r.read()
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise


def simulate(ops, base=None, ref='main', out=None, repo=REPO, quiet=False):
    """Trả về (ok, báo cáo). Áp theo thứ tự như cổng ghi: op sau thấy kết quả của op trước trên cùng tệp."""
    cur, orig, report, ok = {}, {}, [], True
    for i, op in enumerate(ops, 1):
        kind, path = op.get('op'), op.get('path')
        if kind not in ('edit', 'write') or not path:
            report.append('op %d: chỉ mô phỏng edit/write có path — bỏ qua %r' % (i, kind))
            ok = False
            continue
        if path not in cur:
            b = read_base(path, base, ref, repo)
            orig[path] = b
            cur[path] = b
        before = cur[path]
        ev = op.get('expected_version')
        if ev and orig[path] is not None and not sha(orig[path]).startswith(ev):
            report.append('op %d %s: LỆCH VERSION — mong %s, bản gốc %s' % (i, path, ev, sha(orig[path])[:16]))
            ok = False
        if kind == 'write':
            if before is not None and not ev:
                report.append('op %d %s: ghi đè tệp đã có mà thiếu expected_version (cổng sẽ từ chối)' % (i, path))
                ok = False
            cur[path] = op.get('content', '').encode('utf-8')
            continue
        if before is None:
            report.append('op %d %s: tệp chưa có, không sửa được' % (i, path))
            ok = False
            continue
        text = before.decode('utf-8')
        for j, e in enumerate(op.get('edits', []), 1):
            n = text.count(e['old_str'])
            if n != 1:
                report.append('op %d %s edit %d: old_str xuất hiện %d lần (phải đúng 1) · đầu chuỗi: %r'
                              % (i, path, j, n, e['old_str'][:70]))
                ok = False
                continue
            text = text.replace(e['old_str'], e['new_str'], 1)
        cur[path] = text.encode('utf-8')
    for path, b in cur.items():
        o = orig.get(path)
        report.append('%s · %s → %s · %s → %d byte' % (path, sha(o)[:16] if o is not None else 'mới', sha(b)[:16],
                                                      len(o) if o is not None else 0, len(b)))
        if out:
            p = os.path.join(out, path)
            os.makedirs(os.path.dirname(p) or '.', exist_ok=True)
            with open(p, 'wb') as f:
                f.write(b)
    if not quiet:
        print('\n'.join(report))
    return ok, report, cur


def self_test():
    d = tempfile.mkdtemp()
    os.makedirs(os.path.join(d, 'a'))
    src = 'Dòng 1\nMã: CAT-001\nMã: CAT-002\n'.encode('utf-8')
    with open(os.path.join(d, 'a', 'x.md'), 'wb') as f:
        f.write(src)
    v = sha(src)[:16]
    ok1, _, cur = simulate([{'op': 'edit', 'path': 'a/x.md', 'expected_version': v,
                             'edits': [{'old_str': 'Dòng 1', 'new_str': 'Dòng một'}]}], base=d, quiet=True)
    pass1 = ok1 and cur['a/x.md'] == 'Dòng một\nMã: CAT-001\nMã: CAT-002\n'.encode('utf-8')
    ok2, rep2, _ = simulate([{'op': 'edit', 'path': 'a/x.md', 'edits': [{'old_str': 'Mã: ', 'new_str': 'Code: '}]}],
                            base=d, quiet=True)
    pass2 = (not ok2) and any('xuất hiện 2 lần' in r for r in rep2)
    n = int(pass1) + int(pass2)
    print('SELF-TEST %s: %d/2' % ('PASS' if n == 2 else 'FAIL', n))
    return 0 if n == 2 else 1


def main(argv):
    if '--self-test' in argv:
        return self_test()
    opt = {}
    pos = []
    it = iter(argv)
    for a in it:
        if a in ('--base', '--ref', '--out', '--repo'):
            opt[a[2:]] = next(it, None)
        else:
            pos.append(a)
    if not pos:
        print('cách chạy: python3 dot-edit-simulate.py OPS.json (--base DIR | --ref REF) [--out DIR] · hoặc --self-test')
        return 2
    try:
        with open(pos[0], encoding='utf-8') as f:
            ops = json.load(f)
        if isinstance(ops, dict):
            ops = ops.get('ops', [])
        ok, _, _ = simulate(ops, base=opt.get('base'), ref=opt.get('ref') or 'main', out=opt.get('out'),
                            repo=opt.get('repo') or REPO)
    except Exception as e:  # noqa: BLE001
        print('KHÔNG ĐỌC ĐƯỢC ĐẦU VÀO:', e)
        return 2
    print('KẾT QUẢ:', 'ÁP ĐƯỢC HẾT' if ok else 'CÓ LỖI — chưa gửi cổng ghi')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
