#!/usr/bin/env python3
# GS-C1D · chuẩn bị HỒI QUY lỗi giả C1-A/C1-B/C1-C trên graph_cert v5 (c1d-1):
#  (1) shim3/graph_cert.py: nạp ứng viên v5 dưới tên graph_cert, ép K1 = khớp (lỗi giả cũ không có Graph/bookmark thật) — K3 GIỮ NGUYÊN
#      (lỗi giả cũ tự sinh danh mục + giấy bằng run() của chính v5 ⇒ hàng rào danh mục tự khớp; nếu lệch ⇒ ca FAIL là thay đổi hành vi thật).
#  (2) giấy v5 cấp lại cho bộ lỗi giả C1-C (đồng hồ cố định 23/10 05:00Z): lấy giấy v5 thật (dry-run, chỉ đọc), dời mốc giờ về trước 05:00Z,
#      đóng dấu engine_sha256 = ứng viên, ký lại. Đây là dữ liệu vào của lỗi giả, KHÔNG phải giấy production.
# Dùng: c1d_regress_prep.py <ứng viên graph_cert.py> <giấy v5 dry-run> <thư mục ra>
import hashlib, json, os, sys, calendar, time
cand, doc_p, out = sys.argv[1:4]
os.makedirs(out + "/shim3", exist_ok=True)
open(out + "/shim3/graph_cert.py", "w").write('''# GS-C1D · shim HỒI QUY v5: K1 = khớp, K3 giữ nguyên (xem c1d_regress_prep.py)
import importlib.machinery, importlib.util, sys
_l = importlib.machinery.SourceFileLoader("graph_cert_v5_regress", %r)
_m = importlib.util.module_from_spec(importlib.util.spec_from_loader("graph_cert_v5_regress", _l))
_l.exec_module(_m)
_EP = {"fence": "fixture-shim", "bookmark_sha256": "f" * 64, "container": "c", "started_at": "s", "restart_count": "0", "read_at": "x"}
_m.graph_epoch = lambda g, pw: dict(_EP)
_m.graph_fence = lambda doc, live=None, lock_state="auto": {"status": "MATCH", "why": None, "fence": "fixture-shim"}
_orig_run = _m.run
def _run(*a, **k):
    d = _orig_run(*a, **k)
    d["coverage_matrix"] = None
    d["self_sha256"] = _m.self_sha(d)
    return d
_m.run = _run
sys.modules["graph_cert"] = _m
''' % cand)
d = json.load(open(doc_p))
tgt = calendar.timegm(time.strptime("2026-10-22T23:30:00", "%Y-%m-%dT%H:%M:%S"))   # như giấy C1-B mà bộ lỗi giả C1-C dựa vào (hết hạn trước 24/10 02:00Z)
g0 = calendar.timegm(time.strptime(d["generated_at"][:19], "%Y-%m-%dT%H:%M:%S"))
sh = lambda s: time.strftime("%FT%TZ", time.gmtime(calendar.timegm(time.strptime(s[:19], "%Y-%m-%dT%H:%M:%S")) - (g0 - tgt))) if s else s
d["generated_at"] = sh(d["generated_at"])
for c in d["cells"].values():
    for k in ("issued_at", "expires_at"):
        if c.get(k):
            c[k] = sh(c[k])
d["engine_sha256"] = hashlib.sha256(open(cand, "rb").read()).hexdigest()
d.pop("self_sha256", None)
d["self_sha256"] = hashlib.sha256(json.dumps(d, ensure_ascii=False, separators=(",", ":"), sort_keys=True, default=str).encode()).hexdigest()
json.dump(d, open(out + "/current.v5-reissued-fixture.json", "w"), ensure_ascii=False, indent=1, sort_keys=True)
print("shim3 + giấy dời giờ %+.1fh, engine %s" % (-(g0 - tgt) / 3600.0, d["engine_sha256"][:12]))
