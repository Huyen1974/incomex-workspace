#!/usr/bin/env python3
"""Version-scoped CT-000.4 flow probes; no PG, Flow, network or remote writes.

Runs short event traces through the unchanged published interpreter. Expected
properties are independent of B1-B11: an expired deadline must not authorize a
new effect; a compensation attempt ceiling must hold before a new send.
This is not exhaustive model checking or a PostgreSQL integration test.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

SUPPORTED_SOURCES = {
    # Read-only CT source extract and the full remote file at SOURCE_HEAD.
    "4d2a73a183c2ded90de6164a0e33eaf2ce47efef740edeb5157e67648fd69e83",
    "b94a70383f2e44ffadd9fa6c3e60868152eb0027c53cbb82e9ea8e1184625999",
}
EXPECTED_CHECKER = "9e9436cdc058cb480e08ed6dc7062e0d74b18aae43ccbd1e632342939e4ecbd2"
SOURCE_HEAD = "250792dce8380e94aa5fe85ce22477925150e6b8"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--html", type=Path, default=Path(__file__).with_name("ban-duyet.html"))
    ap.add_argument("--checker", type=Path, default=Path(__file__).with_name("kiem-ct000-4.py"))
    ap.add_argument("--out", type=Path, default=Path(__file__).with_name("flow_results.json"))
    args = ap.parse_args()
    report = {
        "audit": "CT000-v6-short-flow-probes", "source_head": SOURCE_HEAD,
        "method": "Published interpreter, unmodified tables, independently chosen raw inputs/event ordering and independent effect/bound oracles.",
        "scope": {"postgresql_executed": False, "directus_executed": False,
                  "remote_modified": False, "exhaustive_search_executed": False},
        "positive_controls": [], "findings": [],
    }

    def finish(code, verdict):
        report.update(exit_code=code, verdict=verdict)
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps({"verdict": verdict, "exit_code": code, "report": str(args.out),
                          "positive_controls": [{"id": p["id"], "status": p["status"]} for p in report["positive_controls"]],
                          "findings": [{"id": p["id"], "status": p["status"]} for p in report["findings"]]},
                         ensure_ascii=False, indent=2))
        return code

    try:
        hashes = {"html": digest(args.html), "checker": digest(args.checker)}
        report["inputs"] = {"html": str(args.html.resolve()), "checker": str(args.checker.resolve()), "sha256": hashes}
        if hashes["html"] not in SUPPORTED_SOURCES or hashes["checker"] != EXPECTED_CHECKER:
            report["reason"] = "The pinned specification/interpreter changed. Review predicates and update fixtures before rerunning; do not merely replace hashes."
            return finish(2, "NOT_EVALUATED_REVIEW_REQUIRED")
        spec = importlib.util.spec_from_file_location("ct000_published_interpreter", args.checker)
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        tables = m.cat_bang(args.html.read_text(encoding="utf-8"))
        model = m.nap(tables)
        report["static_errors"] = m.kiem_tinh(model)
        if report["static_errors"]:
            return finish(1, "SOURCE_STATIC_ERRORS")

        watch = ["st", "quá_hạn_gốc", "có_hạn_PH", "quá_hạn_PH", "hết_hạn_giữ", "thế_hệ", "gen_giữ",
                 "ý_định", "kết_luận", "đang_bay", "đã_làm", "tổng_làm", "bù_bay", "đã_bù", "lần_bù", "MB", "cờ_huỷ"]

        def trace(inputs, events):
            state = dict(m.MAC_DINH)
            state.update(m.AN)
            state.update(inputs)
            state["st"] = "Mới"
            steps = []
            for event, supplied in events:
                before = dict(state)
                world = [change for name, _, change in m.the_gioi(state) if name == event]
                if world:
                    state = dict(state)
                    state.update(world[0])
                    tid, value, chosen = "WORLD", None, world[0]
                else:
                    chosen = dict(supplied)
                    if event == "làm thao tác":
                        chosen.update(tác_nhân=state["gen_giữ"], _ai="chính")
                    formula = model["FORM"].get((state["st"], event))
                    if formula is None:
                        raise RuntimeError(f"No formula for {state['st']} / {event}")
                    context = dict(state)
                    context.update(chosen)
                    if not m.ev_(formula[1], context):
                        raise RuntimeError(f"Event not enabled: {state['st']} / {event}")
                    value = next((label for label, code, _ in formula[2] if m.ev_(code, context)), None)
                    state, tid = m.ap_dung(model, state, event, chosen)
                    if state is None:
                        raise RuntimeError(f"Trace failed: {tid!r}")
                steps.append({
                    "event": event, "input": chosen, "computed_value": value, "transition": tid,
                    "before": {k: before[k] for k in watch}, "after": {k: state[k] for k in watch},
                    "published_B_invariant_errors": m.vi_pham(model, state),
                })
            return {"initial_overrides": inputs, "steps": steps, "final": {k: state[k] for k in watch}}

        entering = [("khai xong", {}), ("chấm", {}), ("chấm", {}), ("xin nhận", {})]
        send = ("làm thao tác", {})
        completed = entering + [send, ("bên nhận làm", {}), ("kết quả", {"mã": "OK"})]
        compensation = completed + [("chấm", {}), ("yêu cầu huỷ", {}), ("xét", {})]
        retry_compensation = [("bù mất", {}), ("qua hạn giữ", {}), ("hết hạn giữ", {})]

        normal = trace({}, completed + [("chấm", {}), ("chấm", {})])
        normal_ok = normal["final"]["st"] == "Kết thúc·Đạt" and all(not s["published_B_invariant_errors"] for s in normal["steps"])
        report["positive_controls"].append({"id": "PC-NORMAL", "status": "PASS" if normal_ok else "FAIL", "trace": normal})

        before_deadline = trace({}, entering + [send])
        allowed_ok = before_deadline["final"]["đang_bay"] == 1 and not before_deadline["final"]["quá_hạn_gốc"]
        report["positive_controls"].append({"id": "PC-BEFORE-DEADLINE", "status": "PASS" if allowed_ok else "FAIL", "trace": before_deadline})

        cancellation = trace({}, entering + [("yêu cầu huỷ", {}), send])
        cancelled_ok = cancellation["final"]["đang_bay"] == 0 and cancellation["steps"][-1]["transition"] == "T16"
        report["positive_controls"].append({"id": "PC-CANCEL-FENCE", "status": "PASS" if cancelled_ok else "FAIL", "trace": cancellation})

        budget_available = trace({"MB": 2, "chờ_duyệt": True}, compensation + retry_compensation)
        spare_ok = budget_available["final"]["lần_bù"] == 2 and budget_available["final"]["bù_bay"] == 1 and not budget_available["final"]["quá_hạn_PH"]
        report["positive_controls"].append({"id": "PC-COMPENSATION-BUDGET-AVAILABLE", "status": "PASS" if spare_ok else "FAIL", "trace": budget_available})

        deadline = trace({}, entering + [("qua hạn gốc", {}), send])
        last = deadline["steps"][-1]
        violates = last["before"]["quá_hạn_gốc"] and last["after"]["đang_bay"] > last["before"]["đang_bay"]
        report["findings"].append({
            "id": "F-DEADLINE", "status": "REPRODUCED_MODEL_COUNTEREXAMPLE" if violates else "NOT_REPRODUCED",
            "title": "T15 sends a new business effect after the root deadline expires while the lease is still valid",
            "locations": ["Bảng Giá trị / làm thao tác", "T15", "Bảng Bất biến"],
            "oracle": "Once the root deadline expires, a newly initiated business effect requires an explicit extension; an existing in-flight effect may still be reconciled.",
            "trace": deadline,
            "fix": "Check root deadline at the send/intent authorization boundary, not only at claim. Route expiry to the existing deadline/reconciliation path; add an invariant for new sends after expiry.",
        })

        budget = trace({"MB": 1, "chờ_duyệt": True}, compensation + retry_compensation)
        violates = budget["final"]["lần_bù"] > budget["final"]["MB"] and budget["steps"][-1]["after"]["bù_bay"] > budget["steps"][-1]["before"]["bù_bay"]
        report["findings"].append({
            "id": "F-COMPENSATION-BUDGET", "status": "REPRODUCED_MODEL_COUNTEREXAMPLE" if violates else "NOT_REPRODUCED",
            "title": "MB=1 nevertheless permits compensation send number 2 on lease expiry",
            "locations": ["Bảng Giá trị / hết hạn giữ at Bù", "T88", "Bảng Biến / MB", "Bảng Bất biến"],
            "oracle": "MB is declared as the compensation attempt ceiling; a new attempt may start only while the pre-increment count is below MB.",
            "trace": budget,
            "fix": "Authorize a new compensation attempt only when lần_bù < MB, then increment and enqueue atomically. Do not suppress reconciliation or completion of an already authorized attempt. Check every send edge, including T66/T81/T88/T90/T94.",
        })

        recovery = trace({"MB": 2, "chờ_duyệt": True}, compensation + [("bù mất", {}), ("qua hạn PH", {}), ("qua hạn giữ", {}), ("hết hạn giữ", {})])
        last = recovery["steps"][-1]
        violates = last["before"]["quá_hạn_PH"] and last["after"]["bù_bay"] > last["before"]["bù_bay"]
        report["findings"].append({
            "id": "F-RECOVERY-DEADLINE", "status": "REPRODUCED_MODEL_COUNTEREXAMPLE" if violates else "NOT_REPRODUCED",
            "title": "T88 starts a new compensation after the recovery deadline has expired",
            "locations": ["Bảng Giá trị / hết hạn giữ at Bù", "T88", "T76/T92 expiry branches", "Bảng Bất biến B9"],
            "oracle": "PH is the recovery time budget. Expiry may permit recording/reconciling already initiated effects, but must not silently authorize a new compensation without Owner extension.",
            "trace": recovery,
            "fix": "Check PH before each new recovery effect. Route to the specified Owner escalation, preserve pending evidence, and require the existing explicit extension before a new attempt. B9 must test the relevant deadline behavior, not just that a deadline flag exists.",
        })

        report["unchanged_inputs"] = hashes == {"html": digest(args.html), "checker": digest(args.checker)}
        if not report["unchanged_inputs"] or any(c["status"] != "PASS" for c in report["positive_controls"]):
            return finish(2, "NOT_EVALUATED_REVIEW_REQUIRED")
        if any(f["status"] == "REPRODUCED_MODEL_COUNTEREXAMPLE" for f in report["findings"]):
            return finish(1, "MODEL_WORKFLOW_FINDINGS_REMAIN")
        return finish(0, "NO_COUNTEREXAMPLE_IN_THESE_SHORT_TRACES_ONLY")
    except Exception as exc:
        report["error"] = {"type": type(exc).__name__, "message": str(exc)}
        return finish(2, "NOT_EVALUATED_REVIEW_REQUIRED")


if __name__ == "__main__":
    raise SystemExit(main())
