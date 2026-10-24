#!/usr/bin/env python3
# GS-C1D-NATIVE-AUTOCOVER-20261023-10 · ghi Graph production cho MỘT lane C1-D bằng CHÍNH đường graph-refresh đã cài (cmd_run --execute
# --only <lane>): mọi tiền điều kiện giữ nguyên (Guard periodic ≤15′, Config Guard CLEAN, graph-v1 status, invariants = manifest, điểm khôi
# phục = manifest, RAM/đĩa, không writer khác, không STOP) TRỪ cổng «VPS-GHI trống»: cờ đang do CHÍNH RUN này giữ ⇒ thay cổng đó bằng kiểm
# «cờ thuộc RUN này» (chỉ trong tiến trình này). Bản tạm → máy cấp giấy chấm ô lane → I/F → khô → MỘT giao dịch → apply-v0 invariants/pins
# → điểm khôi phục tạm + Drive D23 → apply-v0 sources/recovery-manifest → chốt điểm khôi phục → giấy + đèn #24.
# Gia cố GS-C1D-FIX-RECOVERY-20261024-11: RUN_ID là tham số (không ghim RUN cũ) · chủ cờ = ĐÚNG tên trong `- **VPS-GHI: GIỮ — <RUN_ID>**`
# (không khớp nhầm phần lịch sử «trước đó») · clone cổng tươi ≤ 5′ (FETCH_HEAD; cổng fetch mỗi lần commit) · MỖI lần graph-refresh hỏi cờ
# (tiền điều kiện + ngay trước ghi) đọc LẠI dòng cờ. Thiếu/cũ/đổi chủ ⇒ DỪNG trước ghi (rc 3), người chạy nhả cờ.
# Dùng: c1d_apply.py <RUN_ID> <lane> <out.json>
import importlib.machinery, importlib.util, json, os, re, sys, time, types

GRF_PATH = "/opt/incomex/graph-server/prod-v1/bin/graph-refresh"
MAX_AGE_S = 300
HELD = re.compile(r"- \*\*VPS-GHI: GIỮ — ([^*]+?)\*\*")


def flag(clone, run, max_age=MAX_AGE_S):
    """Cờ VPS-GHI trong clone cổng ⇒ {"ok", "free", "holder", "fetch_age_s", "why"}; ok chỉ khi chủ cờ == run và clone tươi ≤ max_age."""
    try:
        age = time.time() - os.stat(clone + "/.git/FETCH_HEAD").st_mtime
        line = next((l for l in open(clone + "/COLLAB.md", encoding="utf-8") if l.startswith("- **VPS-GHI:")), "")
    except OSError as e:
        return {"ok": False, "free": None, "holder": None, "fetch_age_s": None, "why": "không đọc được clone cổng: %s" % type(e).__name__}
    m = HELD.match(line)
    holder = m.group(1).strip() if m else None
    free = line.startswith("- **VPS-GHI: trống**")
    why = ("không thấy dòng VPS-GHI" if not line else "cờ VPS-GHI đang trống" if free else
           "chủ cờ %r ≠ %s" % (holder, run) if holder != run else
           "clone cổng cũ %ds > %ds" % (age, max_age) if age > max_age else None)
    return {"ok": why is None, "free": free, "holder": holder, "fetch_age_s": int(age), "why": why}


def main(argv):
    run, lane, out = argv[1:4]
    ldr = importlib.machinery.SourceFileLoader("graph_refresh_c1d_apply", GRF_PATH)
    GRF = importlib.util.module_from_spec(importlib.util.spec_from_loader("graph_refresh_c1d_apply", ldr))
    ldr.exec_module(GRF)
    f0 = flag(GRF.GW_CLONE, run)
    if not f0["ok"]:
        print("C1D_APPLY STOP %s" % f0["why"]); return 3

    def held_by_run():                      # graph-refresh gọi ở tiền điều kiện VÀ ngay trước ghi ⇒ mỗi lần đọc lại
        st = flag(GRF.GW_CLONE, run)
        return dict(st, held_by=run if st["ok"] else None)
    GRF.vps_ghi_state = held_by_run
    rc = GRF.cmd_run(types.SimpleNamespace(execute=True, trigger="manual", only=lane))
    last = json.load(open(GRF.STATE + "/last.json"))
    json.dump(last, open(out, "w"), ensure_ascii=False, indent=1, sort_keys=True, default=str)
    print("C1D_APPLY rc=%s result=%s applied=%s cert=%s l2=%s" % (rc, last.get("result"), last.get("applied"),
          json.dumps(((last.get("cert") or {}).get("alarm") or {}), ensure_ascii=False)[:300], json.dumps(last.get("l2"), ensure_ascii=False)[:200]))
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv))
