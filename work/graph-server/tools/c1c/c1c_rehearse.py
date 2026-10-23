#!/usr/bin/env python3
# GS-C1C · DIỄN TẬP lượt cấp giấy v4 trên nguồn THẬT + Graph production (chỉ đọc), trạng thái ghi vào thư mục tạm (không đụng state production).
# Dùng: c1c_rehearse.py <graph_cert.py ứng viên> <thư mục giấy tạm> <out.json> [--alarm]
import importlib.machinery, importlib.util, json, os, shutil, sys, time
cand, cdir, out = sys.argv[1:4]
os.makedirs(cdir, mode=0o700, exist_ok=True)
P = "/opt/incomex/graph-server/prod-v1/state/refresh/cert"
for f in ("l2-candidates.json", "canary.json", "alarm.json"):
    if not os.path.exists(os.path.join(cdir, f)):
        shutil.copyfile(os.path.join(P, f), os.path.join(cdir, f))
os.environ["GS_CERT_DIR"] = cdir
ldr = importlib.machinery.SourceFileLoader("graph_cert_rh", cand)
G = importlib.util.module_from_spec(importlib.util.spec_from_loader("graph_cert_rh", ldr))
ldr.exec_module(G)
t = time.time()
doc = G.run(run_label="GS-C1C rehearse (thư mục tạm)")
rep = {"seconds": round(time.time() - t, 1), "summary": doc["summary"], "graph_epoch": {k: v for k, v in doc["graph_epoch"].items() if k != "bookmark_sha256"},
       "bookmark_sha16": (doc["graph_epoch"].get("bookmark_sha256") or "")[:16], "graph_snapshot": doc["graph_snapshot"],
       "directory": {k: doc["directory"].get(k) for k in ("status", "new_source_unhandled", "vanished", "errors", "per_gate")},
       "families": {g: {k: m.get(k) for k in ("status", "native_counts", "parents", "change_since_last_good", "reader_errors", "consistency", "source_version")}
                    for g, m in doc["coverage_matrix"].items()}, "reader_errors": doc["reader_errors"]}
if "--alarm" in sys.argv:
    st, msg, inc = G.alarm(doc)
    rep["alarm"] = {"status": st, "msg": msg, "incidents": [{k: i.get(k) for k in ("kind", "severity", "cell", "reason", "page", "page_reason", "id")} for i in inc]}
    if "--record" in sys.argv:                       # biên nhận vào thư mục TẠM (dập trùng lượt sau); không đẩy Kuma
        new, gone = G.record_incidents(inc)
        rep["alarm"]["new"], rep["alarm"]["resolved"] = [i["id"] for i in new], [i["id"] for i in gone]
json.dump(rep, open(out, "w"), ensure_ascii=False, indent=1, default=str)
print(json.dumps({"seconds": rep["seconds"], "summary": {k: v for k, v in doc["summary"].items() if k != "du_cells"}, "dir": rep["directory"]["status"],
                  "new": rep["directory"]["new_source_unhandled"], "vanished": rep["directory"]["vanished"], "alarm": (rep.get("alarm") or {}).get("msg")},
                 ensure_ascii=False))
