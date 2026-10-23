# GS-C1C · shim HỒI QUY: nạp graph_cert v4 ứng viên dưới tên graph_cert cho lỗi giả C1-A/C1-B cũ, ép hàng rào K1 = khớp
# (lỗi giả cũ không có Graph thật/bookmark) ⇒ chỉ đo hành vi cũ có bị phá không. Không dùng ngoài hồi quy.
import importlib.machinery, importlib.util, sys
_l = importlib.machinery.SourceFileLoader("graph_cert_v4_regress", "/opt/incomex/work/graph-server/evidence/GS-C1C-PRODUCTION-TRUST-GATE-20261023-09/scripts/graph_cert.py")
_m = importlib.util.module_from_spec(importlib.util.spec_from_loader("graph_cert_v4_regress", _l))
_l.exec_module(_m)
_EP = {"fence": "fixture-shim", "bookmark_sha256": "f" * 64, "container": "c", "started_at": "s", "restart_count": "0", "read_at": "x"}
_m.graph_epoch = lambda g, pw: dict(_EP)
_m.graph_fence = lambda doc, live=None, lock_state="auto": {"status": "MATCH", "why": None, "fence": "fixture-shim"}
sys.modules["graph_cert"] = _m
