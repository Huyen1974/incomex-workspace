#!/usr/bin/env python3
"""Independent, stdlib-only audit of the displayed CT-000.4 tables.

This does not import, execute, or copy the host's H7 checker.  It parses the
HTML tables, checks their declared alphabet, and examines the larger boundary
between the prose value classifier and the transition table.  Graph results
are structural, not a proof of the prose actions or a running PostgreSQL system.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import re
from collections import defaultdict, deque
from html.parser import HTMLParser
from pathlib import Path


# Some semantic probes below interpret Vietnamese prose, rather than a formal
# predicate language.  They are valid only for the reviewed snapshot.  Pin the
# entire HTML (conservative: even a cosmetic edit requires review), so an edited
# classifier cannot silently inherit old findings or a false PASS.
SUPPORTED_SOURCE_SHA256 = "b1fb2d7694ccd3493a4da7f1b72598285982556bfcbbb5414657bc30bd33fad3"


def clean(s):
    return " ".join(s.split())


class TableReader(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.tables = []
        self.table = None
        self.depth = 0
        self.in_caption = False
        self.cell = None
        self.row = None

    def handle_starttag(self, tag, attrs):
        if tag == "table":
            self.depth += 1
            if self.depth == 1:
                self.table = {"caption": [], "rows": []}
        if self.depth != 1:
            return
        if tag == "caption":
            self.in_caption = True
        elif tag == "tr":
            self.row = []
        elif tag == "td":
            self.cell = []

    def handle_endtag(self, tag):
        if self.depth == 1:
            if tag == "caption":
                self.in_caption = False
            elif tag == "td" and self.cell is not None:
                self.row.append(clean("".join(self.cell)))
                self.cell = None
            elif tag == "tr" and self.row is not None:
                if self.row:
                    self.table["rows"].append(self.row)
                self.row = None
            elif tag == "table":
                self.table["caption"] = clean("".join(self.table["caption"]))
                self.tables.append(self.table)
                self.table = None
        if tag == "table":
            self.depth -= 1

    def handle_data(self, data):
        if self.depth == 1:
            if self.in_caption:
                self.table["caption"].append(data)
            if self.cell is not None:
                self.cell.append(data)


def expand_names(expr):
    """Expand the published + / {variable} notation, retaining substitutions."""
    names = []
    for part in expr.split(" + "):
        match = re.fullmatch(r"(.+?)\s*\[([^:\]]+):\s*([^\]]+)\]", part)
        if match:
            template, variable, raw_values = match.groups()
            for value in raw_values.split(","):
                value = value.strip()
                names.append((template.replace("{" + variable + "}", value),
                              {variable: value}))
        else:
            names.append((part, {}))
    return names


def components(vertices, edges):
    """Kosaraju traversal; independent implementation from the host checker."""
    forward = {v: set() for v in vertices}
    reverse = {v: set() for v in vertices}
    for edge in edges:
        a, b = edge["source"], edge["target"]
        if a in forward and b in forward:
            forward[a].add(b)
            reverse[b].add(a)
    visited, finish = set(), []

    def first(v):
        visited.add(v)
        for n in sorted(forward[v]):
            if n not in visited:
                first(n)
        finish.append(v)

    for vertex in sorted(vertices):
        if vertex not in visited:
            first(vertex)
    visited, answer = set(), []
    for vertex in reversed(finish):
        if vertex in visited:
            continue
        pending, component = [vertex], set()
        while pending:
            node = pending.pop()
            if node in visited:
                continue
            visited.add(node)
            component.add(node)
            pending.extend(reverse[node] - visited)
        answer.append(sorted(component))
    return answer


def reachable(starts, edges, reverse=False):
    adj = defaultdict(set)
    for edge in edges:
        a, b = edge["source"], edge["target"]
        adj[b if reverse else a].add(a if reverse else b)
    found, todo = set(starts), deque(starts)
    while todo:
        for target in adj[todo.popleft()]:
            if target not in found:
                found.add(target)
                todo.append(target)
    return found


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--html", "--source", dest="source", type=Path,
                    default=Path(__file__).with_name("ban-duyet.html"))
    ap.add_argument("--out", "--output", dest="output", type=Path,
                    default=Path(__file__).with_name("independent_results.json"))
    args = ap.parse_args()
    raw = args.source.read_bytes()
    source_hash = hashlib.sha256(raw).hexdigest()
    if source_hash != SUPPORTED_SOURCE_SHA256:
        output = dict(
            audit="independent-ct0004-v5", checker_version=2,
            overall_status="NOT_EVALUATED_REVIEW_REQUIRED",
            source=str(args.source), sha256=source_hash,
            applicability=dict(scope="exact reviewed HTML snapshot",
                               supported_sha256=SUPPORTED_SOURCE_SHA256,
                               actual_sha256=source_hash,
                               supported=False),
            reason="Source changed. Review the prose predicates and the associated probes before evaluating this version. No old findings or PASS have been reused.",
            findings=[],
        )
        args.output.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(output, ensure_ascii=False, indent=2))
        return 2
    parser = TableReader()
    parser.feed(raw.decode("utf-8"))

    def table(name):
        matches = [t for t in parser.tables if t["caption"].startswith(name)]
        if len(matches) != 1:
            raise ValueError(("table must be unique", name, len(matches)))
        return matches[0]["rows"]

    state_rows = table("Bảng Trạng thái")
    transition_rows = table("Bảng Chuyển trạng thái")
    value_rows = table("Bảng Giá trị")
    action_rows = table("Bảng Bước xử lý lỗi (X1–X9)")
    states, duplicate_state_names = {}, []
    for name_expr, kind, holder, check, raw_domain in state_rows:
        domain = {}
        if raw_domain != "—":
            for segment in raw_domain.split(" ; "):
                event, values = segment.split(": ", 1)
                domain[event] = values.split(" / ")
        for name, bindings in expand_names(name_expr):
            if name in states:
                duplicate_state_names.append(name)
            states[name] = dict(kind=kind, holder=holder, check=check,
                                events=dict(domain), bindings=bindings)
    terminal = {s for s, d in states.items() if d["kind"] == "kết thúc"}
    for name, definition in states.items():
        if name not in terminal:
            # This additional event is explicitly stated in the state caption.
            definition["events"]["yêu cầu huỷ"] = ["ok"]
    expanded = []
    dynamic_returns = [s for s in states if s.startswith("Chấm G")]
    for tid, source_expr, event, raw_values, action, target_expr in transition_rows:
        if source_expr.startswith("*"):
            excluded = set(source_expr.split("trừ", 1)[1].strip().split(", ")) if "trừ" in source_expr else set()
            sources = [(s, {}) for s in states if s not in terminal and s not in excluded]
        else:
            sources = expand_names(source_expr)
        for source, bindings in sources:
            target = target_expr
            for variable, value in bindings.items():
                target = target.replace("{" + variable + "}", value)
            targets = ([source] if target == "(giữ nguyên)" else
                       dynamic_returns if "[bước trở lại]" in target else [target])
            for value in raw_values.split(" / "):
                expanded.append(dict(id=tid, source=source, event=event, value=value,
                                     action=action, targets=targets,
                                     target_expression=target_expr))

    index = defaultdict(list)
    for row in expanded:
        index[(row["source"], row["event"], row["value"])].append(row)
    declared = {(s, e, v) for s, d in states.items() for e, vals in d["events"].items() for v in vals}
    missing = sorted(declared - set(index))
    excess = sorted(set(index) - declared)
    duplicate = [{"key": key, "transitions": [r["id"] for r in rows]}
                 for key, rows in index.items() if len(rows) != 1]
    edges = [dict(source=r["source"], target=t, id=r["id"], event=r["event"],
                  value=r["value"], action=r["action"])
             for r in expanded for t in r["targets"]]
    bad_targets = [e for e in edges if e["target"] not in states]
    reach = reachable(["Mới"], edges)
    finish = reachable(terminal, edges, reverse=True)
    human_events = {"yêu cầu huỷ", "trả lời", "quyết định"}
    automatic_edges = [e for e in edges if e["event"] not in human_events]
    auto_components = components(states, automatic_edges)
    cycles = []
    for comp in auto_components:
        internal = [e for e in automatic_edges if e["source"] in comp and e["target"] in comp]
        if len(comp) > 1 or any(e["source"] == e["target"] for e in internal):
            cycles.append(dict(states=comp, transitions=sorted({e["id"] for e in internal})))

    # Unknown/missing inputs are outside the declared closed alphabet.  Their
    # rejection is intentional in PG requirement 16.  Count them, do not label
    # every rejection as a workflow defect.
    boundary_probes = []
    for state, data in states.items():
        for event in data["events"]:
            for value in (None, "", "<unknown>"):
                boundary_probes.append(dict(state=state, event=event, value=value,
                                            matches=len(index.get((state, event, value), []))))
    for state in states:
        for event in (None, "", "<unknown>"):
            boundary_probes.append(dict(state=state, event=event, value="ok",
                                        matches=len(index.get((state, event, "ok"), []))))
    for bad_state in (None, "", "<unknown>"):
        boundary_probes.append(dict(state=bad_state, event="yêu cầu huỷ", value="ok",
                                    matches=len(index.get((bad_state, "yêu cầu huỷ", "ok"), []))))

    def step(state, event, value):
        rows = index.get((state, event, value), [])
        return rows[0] if len(rows) == 1 else None

    def trace(start, event_values):
        current, result = start, []
        for event, value in event_values:
            row = step(current, event, value)
            if row is None:
                result.append(dict(state=current, event=event, value=value, outcome="NO_TABLE_ROW"))
                return dict(final=current, outcome="NO_TABLE_ROW", steps=result)
            if len(row["targets"]) != 1:
                result.append(dict(state=current, event=event, value=value, transition=row["id"],
                                   outcome="DYNAMIC_RETURN_REQUIRES_CONTEXT"))
                return dict(final=current, outcome="DYNAMIC_RETURN_REQUIRES_CONTEXT", steps=result)
            next_state = row["targets"][0]
            result.append(dict(state=current, event=event, value=value,
                               transition=row["id"], target=next_state))
            current = next_state
        return dict(final=current, outcome="ROUTED", steps=result)

    # Static producer/consumer comparison.  Unlike the state domain, the
    # value table uses a single row for every context of each event.  This
    # conservative comparison shows where a context restriction is necessary;
    # it does not assert that every mismatch is reachable with valid data.
    common_producer_labels = {
        "kiểm lại": ["đóng", "quá hạn gốc", "không thể thoả", "thoả", "còn chờ"],
        "đến lúc kiểm": ["quá hạn gốc", "quá hạn khai", "quá hạn PH", "quá lần 2", "quá lần 1", "chờ quá T", "chưa quá"],
    }
    producer_mismatch = []
    for state, definition in states.items():
        for event, producer_values in common_producer_labels.items():
            if event in definition["events"]:
                accepted = set(definition["events"][event])
                for value in producer_values:
                    if value not in accepted:
                        producer_mismatch.append(dict(state=state, event=event,
                                                      produced_value=value, matches=0))
    lexical_mismatch = []
    for row in expanded:
        if row["event"] in common_producer_labels and row["value"] not in common_producer_labels[row["event"]]:
            lexical_mismatch.append(dict(transition=row["id"], state=row["source"],
                                         event=row["event"], transition_value=row["value"],
                                         producer_values=common_producer_labels[row["event"]]))

    # The host explicitly specifies First semantics.  Implement only the
    # unambiguous first two written clauses, not a guessed corrected classifier.
    result_value_text = dict(value_rows)["kết quả"]
    result_clauses = [part.split(": ", 1) for part in result_value_text.split(" · ") if ": " in part]

    def literal_result_class(code, safe):
        for label, predicate in result_clauses:
            if predicate.startswith("còn lại"):
                return label
            if label == "Lỗi tạm an toàn":
                if code in {"UNAVAILABLE", "RESOURCE_EXHAUSTED"} and safe:
                    return label
            elif code in re.findall(r"\b[A-Z][A-Z_]+\b", predicate):
                return label
        return None

    shadow_cases = []
    later_expected = {"ABORTED": "Xung đột", "FAILED_PRECONDITION": "Lỗi điều kiện",
                      "PERMISSION_DENIED": "Lỗi điều kiện", "INVALID_ARGUMENT": "Lỗi điều kiện",
                      "UNKNOWN": "Chưa biết", "DEADLINE_EXCEEDED": "Chưa biết"}
    for code, expected in later_expected.items():
        actual = literal_result_class(code, False)
        actual_row, expected_row = step("Đang chạy", "kết quả", actual), step("Đang chạy", "kết quả", expected)
        shadow_cases.append(dict(input=dict(code=code, retry_safe=False), actual=actual,
                                 stated_later_rule=expected,
                                 actual_transition=actual_row["id"] if actual_row else None,
                                 intended_transition=expected_row["id"] if expected_row else None,
                                 actual_target=actual_row["targets"][0] if actual_row else None,
                                 intended_target=expected_row["targets"][0] if expected_row else None))

    # Exhaustive, small raw-field enumeration for G2.  No author code used.
    # null/blank or false without a reason are malformed inputs, included to
    # show the closed labels do not establish validation coverage.
    raw_g2_results = []
    for status, reason, waived in itertools.product(("Đúng", "Sai", "Chưa biết", None, ""),
                                                   (None, "lỗi", "chờ"), (False, True)):
        if status != "Đúng" and reason == "lỗi":
            value = "lỗi"
        elif status == "Chưa biết" and reason is None:
            value = "chưa biết"
        elif reason == "chờ":
            value = "chờ"
        elif status == "Đúng" or waived:
            value = "đủ"
        else:
            value = None
        raw_g2_results.append(dict(status=status, reason=reason, owner_waiver_valid=waived,
                                   classified=value, missing_value_rule=value is None,
                                   waiver_preempted=waived and value != "đủ"))

    recovery_waits = []
    for state in states:
        if state.startswith("Chờ ĐK·ĐS·") or state == "Chờ ĐK·Bù":
            loop = step(state, "kiểm lại", "còn chờ")
            recovery_waits.append(dict(state=state, loop_transition=loop["id"],
                                       accepted_values=states[state]["events"]["kiểm lại"],
                                       action=loop["action"],
                                       expiry_transition_present=any("hạn" in r["value"] for r in expanded if r["source"] == state),
                                       source_failure_transition_present=step(state, "kiểm lại", "không thể thoả") is not None,
                                       trace=trace(state, [("kiểm lại", "còn chờ")] * 4)))

    # Candidate concurrent-event boundaries.  These are obligations, not
    # automatically bugs: DB serialization or a stale-event rule may settle
    # them.  The model checker alone cannot prove those external mechanisms.
    race_specs = [
        ("result_vs_cancel", "Đang chạy", ("kết quả", "Đạt"), ("yêu cầu huỷ", "ok")),
        ("result_vs_reclaim", "Đang chạy", ("kết quả", "Đạt"), ("hết hạn giữ", "có dở")),
        ("answer_vs_timeout", "Chờ người·G4", ("trả lời", "có"), ("đến lúc kiểm", "quá lần 2")),
    ]
    races = [dict(name=name, start=start, a_then_b=trace(start, [a, b]),
                  b_then_a=trace(start, [b, a])) for name, start, a, b in race_specs]
    action_references = []
    for tid, source_expr, event, raw_values, action, target_expr in transition_rows:
        references = sorted(set(re.findall(r"\bX[1-9]\b", action)))
        if references:
            action_references.append(dict(transition=tid, referenced_steps=references,
                                          unconditional_target=target_expr, action=action))
    undefined_value_events = sorted({r["event"] for r in expanded} -
                                    {"chấm", "xin nhận", "hết hạn giữ", "kết quả", "đối soát", "xét", "kiểm lại", "đến lúc kiểm"})

    findings = [
        dict(id="IA-01", status="FAIL" if any(c["actual"] != c["stated_later_rule"] for c in shadow_cases) else "PASS",
             severity="validated_literal", kind="literal_first_rule_shadowing",
             locations=["Bảng Giá trị/kết quả", "T24", "T25", "T26", "T27"],
             claim="The second classifier clause 'còn lại' shadows later result clauses under the stated First semantics.",
             witnesses=shadow_cases,
             fix="Move the unsafe-transient default inside the transient-error group; explicitly define Đạt and Một phần; put a final unknown/invalid-input fallback last."),
        dict(id="IA-02", status="FAIL" if lexical_mismatch else "PASS",
             severity="validated_literal", kind="producer_consumer_exact_label_mismatch",
             locations=["Bảng Giá trị/đến lúc kiểm", "T16"],
             claim="The value table ends the timer classifier with 'chưa quá', but state Chờ and T16 require 'chưa'.",
             witness=trace("Chờ", [("đến lúc kiểm", "chưa quá")]),
             fix="Use one canonical value in producer, state domain, and transition row."),
        dict(id="IA-03", status="NOT_PROVEN", severity="requires_implementation",
             kind="classifier_context_scope_not_formalized",
             locations=["Bảng Giá trị/kiểm lại", "Bảng Giá trị/đến lúc kiểm"],
             mismatch_count=len(producer_mismatch),
             claim="The single prose classifier row can name values absent from particular state domains; context-specific predicates are not encoded.",
             witness={"state":"Chờ người·ĐS·Huỷ", "context":"root deadline expired and recovery deadline still future", "literal_first_output":"quá hạn gốc", "accepted":states["Chờ người·ĐS·Huỷ"]["events"]["đến lúc kiểm"]},
             fix="Key each classifier by state/event, or specify state applicability in every predicate before asserting totality."),
        dict(id="IA-04", status="COUNTEREXAMPLE_IN_TABLE_ABSTRACTION", severity="validated_literal",
             kind="automatic_wait_cycles_not_bounded_in_table",
             locations=["T75", "T83"],
             claim="Four recovery wait states admit arbitrary repeated automatic checks; their table domains contain neither recovery-expiry nor impossible-source outcomes. H7 excludes all wait states from its cycle check.",
             witnesses=recovery_waits,
             fix="Define expiry/source-failure handling for these waiting states, or formally model the linked incident process and prove its escalation discharges the wait."),
        dict(id="IA-05", status="NOT_PROVEN", severity="requires_implementation",
             kind="raw_input_guard_totality",
             locations=["Bảng Giá trị/chấm G2", "T06–T09"],
             claim="Enumerating declared labels does not validate the raw answers that produce them. Some missing/invalid raw values have no classifier result; valid waivers can be preempted by earlier error/wait clauses unless effective conditions are normalized first.",
             witnesses=[r for r in raw_g2_results if r["missing_value_rule"] or r["waiver_preempted"]],
             fix="Validate raw enum/reason/waiver fields before classification; specify effective waived condition and an explicit failure path for malformed input."),
        dict(id="IA-06", status="NOT_PROVEN", severity="requires_implementation",
             kind="action_outcome_coverage",
             locations=["X4", "T10–T13", "X3", "T85"],
             claim="The table indexes event labels and destination names; X4 UPDATE-zero and X3 failure after T85 are written in prose but have no separate corresponding outcome in these transition rows.",
             witnesses=[dict(action="X4 UPDATE returns 0 rows", declared=states["Chờ"]["events"]["xin nhận"], prose="X2"),
                        dict(action="T85 invokes X3; no valid MOW", prose="X3 failure ⇒ X7", table_target="Chấm [bước trở lại]")],
             fix="Specify whether these are explicit no-op/reclassification API outcomes or table transitions; execute and assert both branches."),
    ]
    output = dict(
        audit="independent-ct0004-v5", checker_version=2, source=str(args.source),
        sha256=source_hash,
        applicability=dict(scope="exact reviewed HTML snapshot",
                           supported_sha256=SUPPORTED_SOURCE_SHA256,
                           actual_sha256=source_hash,
                           supported=True),
        scope={"independent_of_author_code": True, "stdlib_only": True,
               "not_executed": ["PostgreSQL functions", "Directus Flow", "external side effects", "host H7 checker"],
               "limitations": ["Prose action effects are not machine-executable in the source.",
                               "Dynamic Owner return targets are structurally over-approximated to the declared gate states.",
                               "Candidate event races are not assumed jointly feasible without guards.",
                               "Structural reachability is existential, not eventual completion under all schedules."]},
        counts=dict(state_table_rows=len(state_rows), states=len(states), terminal_states=len(terminal),
                    transition_table_rows=len(transition_rows), expanded_event_value_pairs=len(index),
                    declared_event_value_pairs=len(declared), edges_with_dynamic_returns=len(edges),
                    value_table_rows=len(value_rows)),
        declared_alphabet=dict(status="PASS" if not (missing or excess or duplicate or bad_targets or duplicate_state_names) else "FAIL",
                               missing=missing, excess=excess, duplicate=duplicate,
                               invalid_targets=bad_targets, duplicate_state_names=duplicate_state_names),
        graph=dict(unreachable_from_new=sorted(set(states)-reach),
                   no_existential_path_to_terminal=sorted(set(states)-finish),
                   automatic_sccs_including_wait_states=cycles,
                   wait_self_loops=[e for e in automatic_edges if e["source"]==e["target"] and states[e["source"]]["kind"]=="chờ"]),
        boundary=dict(policy="PG requirement 16 intentionally rejects missing tuples; these are outside the 160-pair claim.",
                      probes=len(boundary_probes), matched=sum(p["matches"]>0 for p in boundary_probes),
                      examples=boundary_probes[:9],
                      durable_rejection_recovery="Not specified by the transition table itself; orphan scan covers some bad-record cases."),
        producer_consumer=dict(common_classifier_mismatches=producer_mismatch,
                               lexical_mismatches=lexical_mismatch,
                               events_without_a_dedicated_value_table_definition=undefined_value_events),
        raw_guard_enumeration=dict(g2_combinations=len(raw_g2_results),
                                   missing_rule_cases=sum(r["missing_value_rule"] for r in raw_g2_results),
                                   waiver_preempted_cases=sum(r["waiver_preempted"] for r in raw_g2_results)),
        event_races=races, action_references=action_references,
        findings=findings,
    )
    args.output.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output), "counts": output["counts"],
                      "declared_alphabet": output["declared_alphabet"]["status"],
                      "graph_unreachable": output["graph"]["unreachable_from_new"],
                      "automatic_scc_count": len(cycles),
                      "boundary_rejections": len(boundary_probes),
                      "producer_consumer_mismatch_count": len(producer_mismatch),
                      "findings": [{"id": f["id"], "status": f["status"], "severity":f["severity"], "kind": f["kind"]} for f in findings]},
                     ensure_ascii=False, indent=2))
    structural_failure = output["declared_alphabet"]["status"] == "FAIL" or bool(
        output["graph"]["unreachable_from_new"] or output["graph"]["no_existential_path_to_terminal"])
    validated_failure = any(f["status"] == "FAIL" and f["severity"] == "validated_literal" for f in findings)
    return 1 if structural_failure or validated_failure else 0


if __name__ == "__main__":
    raise SystemExit(main())
