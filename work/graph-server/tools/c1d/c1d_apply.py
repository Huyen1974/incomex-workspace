#!/usr/bin/env python3
# GS-C1D-NATIVE-AUTOCOVER-20261023-10 · ghi Graph production cho MỘT lane C1-D bằng CHÍNH đường graph-refresh đã cài (cmd_run --execute
# --only <lane>): mọi tiền điều kiện giữ nguyên (Guard periodic ≤15′, Config Guard CLEAN, graph-v1 status, invariants = manifest, điểm khôi
# phục = manifest, RAM/đĩa, không writer khác, không STOP) TRỪ cổng «VPS-GHI trống»: cờ đang do CHÍNH RUN này giữ (đọc dòng VPS-GHI của clone
# cổng: phải chứa RUN_ID) ⇒ thay cổng đó bằng kiểm «cờ thuộc RUN này» (chỉ trong tiến trình này). Bản tạm → máy cấp giấy chấm ô lane →
# I/F → khô → MỘT giao dịch → apply-v0 invariants/pins → điểm khôi phục + Drive D23 → apply-v0 sources/recovery-manifest → giấy + đèn #24.
# Dùng: c1d_apply.py <lane> <out.json>
import importlib.machinery, importlib.util, json, sys, types

RUN = "GS-C1D-NATIVE-AUTOCOVER-20261023-10"
lane, out = sys.argv[1:3]
GRF_PATH = "/opt/incomex/graph-server/prod-v1/bin/graph-refresh"
ldr = importlib.machinery.SourceFileLoader("graph_refresh_c1d_apply", GRF_PATH)
GRF = importlib.util.module_from_spec(importlib.util.spec_from_loader("graph_refresh_c1d_apply", ldr))
ldr.exec_module(GRF)
line = next((l for l in open(GRF.GW_CLONE + "/COLLAB.md", encoding="utf-8") if l.startswith("- **VPS-GHI:")), "")
if RUN not in line or line.startswith("- **VPS-GHI: trống**"):
    print("C1D_APPLY STOP cờ VPS-GHI không thuộc RUN này: %s" % line[:160]); sys.exit(3)
orig = GRF.vps_ghi_state


def held_by_run():
    st = orig()
    ok = (not st.get("free")) and (st.get("fetch_age_s") or 10 ** 9) <= 86400
    return {"ok": ok, "free": st.get("free"), "fetch_age_s": st.get("fetch_age_s"), "held_by": RUN if ok else None,
            "why": None if ok else "cờ không còn do RUN giữ / clone cũ"}
GRF.vps_ghi_state = held_by_run
a = types.SimpleNamespace(execute=True, trigger="manual", only=lane)
rc = GRF.cmd_run(a)
last = json.load(open(GRF.STATE + "/last.json"))
json.dump(last, open(out, "w"), ensure_ascii=False, indent=1, sort_keys=True, default=str)
print("C1D_APPLY rc=%s result=%s applied=%s cert=%s l2=%s" % (rc, last.get("result"), last.get("applied"),
      json.dumps(((last.get("cert") or {}).get("alarm") or {}), ensure_ascii=False)[:300], json.dumps(last.get("l2"), ensure_ascii=False)[:200]))
sys.exit(rc)
