#!/usr/bin/env python3
# GS-C1D2-SCOPED-AUTOCOVER-20261026-13 · ghi Graph production cho MỘT lane (c1d:infra) bằng CHÍNH đường graph-refresh đã cài (cmd_run --execute
# --only <lane>) — khuôn c1d_apply (GS-C1D-FIX): mọi tiền điều kiện giữ nguyên TRỪ cổng «VPS-GHI trống»: cờ do CHÍNH RUN này giữ ⇒ thay bằng
# «chủ cờ = ĐÚNG RUN_ID trong `- **VPS-GHI: GIỮ — <RUN_ID>**`» + clone cổng tươi; đọc LẠI ở mọi lần graph-refresh hỏi (tiền điều kiện · ngay
# trước ghi · SAU giao dịch Graph — C1-D2 P255(a)). Tươi = FETCH_HEAD ≤ 300 s HOẶC HEAD clone = HEAD remote đọc ngay (git ls-remote ẩn danh).
# Lưu kế hoạch nghịch đảo (I + băm PRE/NEW) vào bằng chứng TRƯỚC khi ghi ⇒ c1d2_lane_rollback.py lùi được sau lượt nếu Guard POST không đạt.
# Dùng: c1d2_apply.py <RUN_ID> <lane> <out.json>
import importlib.machinery, importlib.util, json, os, re, sys, time, types

GRF_PATH = "/opt/incomex/graph-server/prod-v1/bin/graph-refresh"
E = "/opt/incomex/work/graph-server/evidence/GS-C1D2-SCOPED-AUTOCOVER-20261026-13"
MAX_AGE_S = 300
HELD = re.compile(r"- \*\*VPS-GHI: GIỮ — ([^*]+?)\*\*")


def flag(GRF, run, max_age=MAX_AGE_S):
    clone = GRF.GW_CLONE
    try:
        age = time.time() - os.stat(clone + "/.git/FETCH_HEAD").st_mtime
        line = next((l for l in open(clone + "/COLLAB.md", encoding="utf-8") if l.startswith("- **VPS-GHI:")), "")
    except OSError as e:
        return {"ok": False, "free": None, "holder": None, "fetch_age_s": None, "why": "không đọc được clone cổng: %s" % type(e).__name__}
    m = HELD.match(line)
    holder = m.group(1).strip() if m else None
    free = line.startswith("- **VPS-GHI: trống**")
    fresh = "FETCH_HEAD_LE_%dS" % max_age if age <= max_age else None
    if not fresh:
        head = GRF.git(clone, "rev-parse", "HEAD").stdout.decode().strip()
        remote = GRF.ls_remote_head()
        fresh = "REMOTE_HEAD_EQ_CLONE" if remote and remote == head else None
    why = ("không thấy dòng VPS-GHI" if not line else "cờ VPS-GHI đang trống" if free else
           "chủ cờ %r ≠ %s" % (holder, run) if holder != run else
           "clone cổng cũ %ds > %ds và HEAD clone ≠ remote" % (age, max_age) if not fresh else None)
    return {"ok": why is None, "free": free, "holder": holder, "fetch_age_s": int(age), "fresh": fresh, "why": why}


def main(argv):
    run, lane, out = argv[1:4]
    ldr = importlib.machinery.SourceFileLoader("graph_refresh_c1d2_apply", GRF_PATH)
    GRF = importlib.util.module_from_spec(importlib.util.spec_from_loader("graph_refresh_c1d2_apply", ldr))
    ldr.exec_module(GRF)
    f0 = flag(GRF, run)
    print("C1D2_APPLY flag0 %s" % json.dumps(f0, ensure_ascii=False), flush=True)
    if not f0["ok"]:
        print("C1D2_APPLY STOP %s" % f0["why"]); return 3
    checks = []

    def held_by_run():
        st = flag(GRF, run)
        checks.append(dict(st, at=GRF.now()))
        return dict(st, held_by=run if st["ok"] else None)
    GRF.vps_ghi_state = held_by_run
    real_apply = GRF.apply_plan

    def apply_saving_inverse(target, plan, report):          # chỉ lượt production (đích = Graph sống) mới lưu nghịch đảo
        if target.get("g") is not None and target.get("pw"):
            with open(E + "/m/lane-plan-inverse.json", "w") as f:
                json.dump({"lane": plan.get("lane"), "pre_hash": plan["pre_hash"], "new_hash": plan["new_hash"], "I": plan["I"], "F": plan["F"],
                           "counts": plan.get("counts"), "plan_sha256": plan.get("plan_sha256"), "saved_at": GRF.now()}, f, ensure_ascii=False, default=str)
            os.chmod(E + "/m/lane-plan-inverse.json", 0o600)
        return real_apply(target, plan, report)
    GRF.apply_plan = apply_saving_inverse
    rc = GRF.cmd_run(types.SimpleNamespace(execute=True, trigger="manual", only=lane))
    last = json.load(open(GRF.STATE + "/last.json"))
    last["c1d2_flag_checks"] = checks
    json.dump(last, open(out, "w"), ensure_ascii=False, indent=1, sort_keys=True, default=str)
    print("C1D2_APPLY rc=%s result=%s applied=%s cert=%s flag_checks=%d" % (rc, last.get("result"), last.get("applied"),
          json.dumps(((last.get("cert") or {}).get("alarm") or {}), ensure_ascii=False)[:300], len(checks)))
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv))
