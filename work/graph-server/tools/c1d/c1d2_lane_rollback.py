#!/usr/bin/env python3
# GS-C1D2-SCOPED-AUTOCOVER-20261026-13 · LÙI dữ liệu Graph của lượt lane SAU khi lượt đã chốt (chỉ dùng nếu Guard POST/hard-gate không đạt):
#   cờ do RUN giữ + Graph = NEW đã lưu ⇒ chạy I (MỘT giao dịch) ⇒ Graph = PRE ⇒ apply-v0 nguyên byte PRE invariants/pins/refresh-sources ⇒
#   graph-refresh recovery-point --drive (điểm khôi phục mới từ Graph = PRE, RECMAN trỏ điểm đó) ⇒ recovery_ok (kể cả H1).
# Dùng: c1d2_lane_rollback.py <RUN_ID>   (exit 0 lùi sạch · 1 lỗi · 3 dừng trước ghi)
import importlib.machinery, importlib.util, json, os, sys, time, types
E = "/opt/incomex/work/graph-server/evidence/GS-C1D2-SCOPED-AUTOCOVER-20261026-13"
sys.path.insert(0, E + "/scripts")
import c1d2_apply as CA  # noqa: E402

run = sys.argv[1]
ldr = importlib.machinery.SourceFileLoader("grf_c1d2_rb", CA.GRF_PATH)
GRF = importlib.util.module_from_spec(importlib.util.spec_from_loader("grf_c1d2_rb", ldr))
ldr.exec_module(GRF)
f0 = CA.flag(GRF, run)
if not f0["ok"]:
    print("LANE_ROLLBACK STOP cờ %s" % f0["why"]); sys.exit(3)
inv = json.load(open(E + "/m/lane-plan-inverse.json"))
g = GRF.r7_g1lib.load(GRF.G1)
pw = g.password()
h0 = GRF.full_hash(g, pw)
if h0 != inv["new_hash"]:
    print("LANE_ROLLBACK STOP Graph ≠ NEW đã lưu (đã đổi sau lượt) — không tự lùi"); sys.exit(3)
d = g.http_cypher(inv["I"], pw, timeout=1500)
if d.get("errors") or GRF.full_hash(g, pw) != inv["pre_hash"]:
    print("LANE_ROLLBACK FAIL I lỗi/không về PRE %s" % (d.get("errors") or "")[:200]); sys.exit(1)
out = {"graph_eq_pre": True}
ts = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())
for tid, live, bk in (("graph-v1-invariants", GRF.INV, "graph-v1-invariants"), ("graph-v1-pins", GRF.PINS, "graph-v1-pins"),
                      ("graph-refresh-sources", GRF.SOURCES, "graph-refresh-sources")):
    raw = open(E + "/m/backup/%s.truoc" % bk, "rb").read()
    if open(live, "rb").read() != raw:
        out[tid] = GRF.apply_v0(tid, live, None, "C1D2-LANE-RB-" + ts, raw_bytes=raw)
rc = GRF.cmd_recovery_point(types.SimpleNamespace(label="c1d2-lane-rollback-" + ts, drive=True, out=E + "/m/lane-rollback-recovery.json"))
ro = GRF.recovery_ok(g)
out.update(recovery_point_rc=rc, recovery_ok=ro.get("ok"), why=ro.get("why"), inv_eq=not g.inv_equal(g.invariants(pw), GRF.jload(GRF.INV)))
json.dump(out, open(E + "/m/lane-rollback.json", "w"), ensure_ascii=False, indent=1, default=str)
print("LANE_ROLLBACK %s %s" % ("PASS" if rc == 0 and ro.get("ok") and out["inv_eq"] else "FAIL", json.dumps(out, ensure_ascii=False, default=str)[:400]))
sys.exit(0 if rc == 0 and ro.get("ok") and out["inv_eq"] else 1)
