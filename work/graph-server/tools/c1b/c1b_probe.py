#!/usr/bin/env python3
# GS-C1B-LAYERED-IMPACT-20261022-08 · (khuôn mcp_probe C1-A) thử cổng đọc graph-v1 từ tiến trình MCP MỚI: nhãn N4 + khối layers L1/L2/L3 C1-B.
# Dùng: mcp_probe.py <out.json> <ssh-remote-command...>
import json, subprocess, sys, time

out, cmd = sys.argv[1], sys.argv[2:]
Q = [
    ("l1_iu_triggers", "read-cypher", "MATCH (g:PgTrigger)-[:ON_TABLE]->(t:PgTable {id: 'public.information_unit'}) RETURN g.id AS x ORDER BY x"),
    ("l1_iu_trigger_handlers", "read-cypher", "MATCH (t:PgTable {id: 'public.information_unit'})<-[:ON_TABLE]-(g:PgTrigger)-[:EXECUTES]->(f:PgFunction) RETURN g.id AS trg, f.id AS fn ORDER BY trg"),
    ("l1_iu_fk_in", "read-cypher", "MATCH (t:PgTable {id: 'public.information_unit'})<-[:REFERENCES]-(f:PgForeignKey)<-[:HAS_FK]-(s:PgTable) RETURN s.id AS src, f.id AS fk, f.on_delete AS on_delete ORDER BY fk"),
    ("l1_iu_fk_out", "read-cypher", "MATCH (t:PgTable {id: 'public.information_unit'})-[:HAS_FK]->(f:PgForeignKey)-[:REFERENCES]->(d:PgTable) RETURN f.id AS fk, d.id AS dst"),
    ("l1_iu_views", "read-cypher", "MATCH (t:PgTable {id: 'public.information_unit'})<-[:DEPENDS_ON]-(v:PgView) RETURN v.id AS view_id ORDER BY view_id"),
    ("l1_iu_permissions", "read-cypher", "MATCH (t:PgTable {id: 'public.information_unit'})<-[:MAPS_TO_TABLE]-(c:DirectusCollection)<-[:PERMISSION_ON]-(p:DirectusPermission) RETURN p.action AS action, count(p) AS n ORDER BY action"),
    ("l1_pages_translations_relations", "read-cypher", "MATCH (t:PgTable {id: 'public.pages_translations'})<-[:MAPS_TO_TABLE]-(c:DirectusCollection)<-[:RELATION_MANY]-(r:DirectusRelation)-[:RELATION_ONE]->(o:DirectusCollection)-[:MAPS_TO_TABLE]->(x:PgTable) RETURN r.id AS rel, x.id AS other ORDER BY rel"),
    ("l1_empty_tac_vocab_views", "read-cypher", "MATCH (t:PgTable {id: 'public.tac_review_state_vocab'})<-[:DEPENDS_ON]-(v:PgView) RETURN v.id AS v"),
    ("l1_param_anchor", "read-cypher", "MATCH (t:PgTable {id: $t})<-[:DEPENDS_ON]-(v:PgView) RETURN v.id AS view_id ORDER BY view_id", {"t": "public.agents"}),
    ("impact_iu_full", "read-cypher", "MATCH (t:PgTable {id: 'public.information_unit'})-[*1..3]-(x) RETURN count(DISTINCT x) AS c"),
    ("escape_shape_3hop", "read-cypher", "MATCH (t:PgTable {id: 'public.information_unit'})<-[:REFERENCES]-(f:PgForeignKey)<-[:HAS_FK]-(s:PgTable)<-[:ON_TABLE]-(g:PgTrigger) RETURN g.id AS g LIMIT 5"),
    ("nonpilot_dot_tools_triggers", "read-cypher", "MATCH (g:PgTrigger)-[:ON_TABLE]->(t:PgTable {id: 'public.dot_tools'}) RETURN g.id AS trigger ORDER BY trigger"),
    ("global_fk_unanchored", "read-cypher", "MATCH (f:PgForeignKey)-[:REFERENCES]->(t:PgTable) RETURN count(f) AS c"),
    ("adversarial_call_db_labels", "read-cypher", "CALL db.labels() YIELD label RETURN label"),
    ("adversarial_unlabeled_scan", "read-cypher", "MATCH (n) RETURN count(n) AS c"),
    ("adversarial_return_node", "read-cypher", "MATCH (t:PgTable {id: 'public.information_unit'})<-[:DEPENDS_ON]-(v:PgView) RETURN v LIMIT 1"),
    ("syntax_error", "read-cypher", "MATCH (g:PgTrigger RETURN g"),
]
p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
msgs = [{"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2025-06-18", "capabilities": {},
                                                                       "clientInfo": {"name": "gs-c1b-probe", "version": "1"}}},
        {"jsonrpc": "2.0", "method": "notifications/initialized"}, {"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}},
        {"jsonrpc": "2.0", "id": 3, "method": "resources/list", "params": {}}, {"jsonrpc": "2.0", "id": 4, "method": "prompts/list", "params": {}},
        {"jsonrpc": "2.0", "id": 10, "method": "tools/call", "params": {"name": "get-schema", "arguments": {}}}]
for i, (name, tool, q, *pp) in enumerate(Q):
    msgs.append({"jsonrpc": "2.0", "id": 100 + i, "method": "tools/call", "params": {"name": tool, "arguments": dict({"query": q}, **({"params": pp[0]} if pp else {}))}})
t0 = time.time()
o, e = p.communicate("".join(json.dumps(m) + "\n" for m in msgs).encode(), timeout=600)
res = {"seconds": round(time.time() - t0, 1), "rc": p.returncode, "stderr_tail": e.decode(errors="replace")[-300:], "replies": {}}
for line in o.decode(errors="replace").splitlines():
    try:
        m = json.loads(line)
    except ValueError:
        continue
    res["replies"][str(m.get("id"))] = m
summary = []
for mid, name in [("10", "get_schema")] + [(str(100 + i), x[0]) for i, x in enumerate(Q)]:
    m = res["replies"].get(mid) or {}
    r = m.get("result") or {}
    lab = (r.get("_meta") or {}).get("incomex.graph/completeness_v1") or (((m.get("error") or {}).get("data") or {}) if isinstance((m.get("error") or {}).get("data"), dict) else {}).get("incomex.graph/completeness_v1")
    first = ((r.get("content") or [{}])[0].get("text") or "")[:24]
    rows = None
    for c in (r.get("content") or [])[1:]:
        try:
            rows = len(json.loads(c.get("text") or ""))
        except (ValueError, TypeError):
            pass
    summary.append({"q": name, "label": (lab or {}).get("completeness_label"), "class": (lab or {}).get("query_class"),
                    "act": (lab or {}).get("query_actionability"), "missing": len((lab or {}).get("missing_or_unknown_cell_ids") or []),
                    "first_block": first, "rows": rows, "isError": r.get("isError") or ("error" in m), "reason": ((lab or {}).get("reason") or "")[:90],
                    "scope": (lab or {}).get("answer_scope"), "impact": (lab or {}).get("impact_question_actionability"),
                    "layers": {k: v.get("label") for k, v in ((lab or {}).get("layers") or {}).items()},
                    "l2_cand": (((lab or {}).get("layers") or {}).get("L2") or {}).get("candidates_count"),
                    "proof": [(lab or {}).get("proof_issued_at"), (lab or {}).get("expires_at")], "cells": ((lab or {}).get("relevant_cell_ids") or [])[:2]})
tl = (res["replies"].get("2") or {}).get("result", {}).get("tools") or []
res["tools"] = [t.get("name") for t in tl]
res["tools_desc_has_n4"] = all("[graph-v1 N4]" in (t.get("description") or "") for t in tl)
res["resources_list"] = res["replies"].get("3")
res["prompts_list"] = res["replies"].get("4")
res["summary"] = summary
json.dump(res, open(out, "w"), ensure_ascii=False, indent=1)
print(json.dumps({"rc": res["rc"], "seconds": res["seconds"], "tools": res["tools"], "desc_n4": res["tools_desc_has_n4"],
                  "resources": (res["resources_list"] or {}).get("error", (res["resources_list"] or {}).get("result")),
                  "prompts": (res["prompts_list"] or {}).get("error", (res["prompts_list"] or {}).get("result"))}, ensure_ascii=False))
for s in summary:
    print(json.dumps(s, ensure_ascii=False))
