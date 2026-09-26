#!/usr/bin/env python3
# ==== CÔNG CỤ QUY TRÌNH · nguồn chuẩn: GitHub incomex-workspace · work/mow-mot-moit-mout/cong-cu/ ====
# Mã:           dot-push-verify   (dòng trong 🛠 của ban-duyet.html · sổ công cụ = dòng 35 CAT-006 · chưa đăng ký dot_tools)
# Thuộc:        🏗 Nhà máy — xác nhận tài liệu đã ghi lên GitHub đúng từng byte
# Phạm vi kiểm: K04 · workspace.doc · verify (sau khi ghi) · loại A (chỉ đọc)
# Việc:         Sau khi cổng ghi báo xong: tải bản thật trên GitHub theo commit, so từng byte với bản dự kiến
#               (đầu ra của dot-edit-simulate) hoặc với sha256 mong đợi. Lệch → in vị trí byte đầu tiên khác.
#               Nên dùng mã commit thay cho "main": bản "main" qua CDN có thể trễ vài phút.
# Đầu vào:      --path đường dẫn trong repo · --ref COMMIT|main · một trong hai: --local TỆP hoặc --sha256 HEX
# Đầu ra:       "KHỚP" / "LỆCH" + sha256 hai bên · exit 0 = khớp · 1 = lệch · 2 = không tải/đọc được
# Cách chạy:    python3 dot-push-verify.py --path work/mow-mot-moit-mout/ban-duyet.html --ref <commit> --local out/…/ban-duyet.html
# Cần:          Python ≥ 3.8, chỉ thư viện chuẩn · cần mạng tới raw.githubusercontent.com · không bí mật
# Ca thử:       python3 dot-push-verify.py --path AGENTS.md --ref dd67cc89fa912df4ae75460f8b9662719deb8213 \
#                 --sha256 d8e0e55b053275257b6c85f6794c71b6f6b78459bbf41316dd577f6dba55cd66
# Kết quả mong đợi: KHỚP · exit 0   (đổi 1 ký tự của --sha256 → LỆCH · exit 1)
# Nguồn gốc:    dựng lại từ bước "curl raw GitHub | sha256sum + cmp với bản mô phỏng" phiên Cowork 26/09 (C09–C11).
# Luật:         theo TEMPLATE-DOT-SCRIPT: không đường dẫn cứng, exit 0/1.
# Chép lên VPS: chỉ khi phải chạy ở đó · theo lệnh · ghi sha256 + nguồn@commit vào sổ công cụ · không sửa bản chép.
import hashlib, sys, urllib.error, urllib.parse, urllib.request

REPO = 'Huyen1974/incomex-workspace'


def main(argv):
    opt, it = {}, iter(argv)
    for a in it:
        if a.startswith('--'):
            opt[a[2:]] = next(it, None)
    path, ref, repo = opt.get('path'), opt.get('ref') or 'main', opt.get('repo') or REPO
    if not path or not (opt.get('local') or opt.get('sha256')):
        print('cách chạy: --path P --ref R (--local TỆP | --sha256 HEX) [--repo OWNER/REPO]')
        return 2
    url = 'https://raw.githubusercontent.com/%s/%s/%s' % (repo, ref, urllib.parse.quote(path))
    try:
        with urllib.request.urlopen(url, timeout=60) as r:
            remote = r.read()
        local = None
        if opt.get('local'):
            with open(opt['local'], 'rb') as f:
                local = f.read()
    except (urllib.error.URLError, OSError) as e:
        print('KHÔNG TẢI/ĐỌC ĐƯỢC:', e)
        return 2
    rs = hashlib.sha256(remote).hexdigest()
    want = hashlib.sha256(local).hexdigest() if local is not None else opt['sha256'].lower()
    print('nguồn:', url)
    print('GitHub  sha256:', rs, '·', len(remote), 'byte')
    print('mong đợi sha256:', want, '·', ('%d byte' % len(local)) if local is not None else 'theo --sha256')
    if rs == want:
        print('KHỚP')
        return 0
    if local is not None:
        k = next((i for i, (a, b) in enumerate(zip(remote, local)) if a != b), min(len(remote), len(local)))
        print('LỆCH tại byte %d · GitHub: %r · bản dự kiến: %r' % (k, remote[max(0, k - 40):k + 40], local[max(0, k - 40):k + 40]))
    else:
        print('LỆCH')
    return 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
