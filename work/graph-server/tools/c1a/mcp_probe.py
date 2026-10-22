#!/usr/bin/env python3
# GS-C1A-CERT-QUALITYGATE-20261022-07 · R: thử cổng đọc graph-v1 (MCP stdio qua ssh) — mọi phản hồi tools/call phải có nhãn N4.
# Dùng: mcp_probe.py <out.json> <ssh-remote-command...>
import json, subprocess, sys, time

out, cmd = sys.argv[1], sys.argv[2:]
Q = [
    ("known_trigger_on_table", "read-cypher", "MATCH (g:PgTrigger)-[:ON_TABLE]->(t:PgTable {id: 'public.dot_tools'}) RETURN g.id AS trigger ORDER BY trigger"),
    ("information_unit_triggers", "read-cypher", "MATCH (g:PgTrigger)-[:ON_TABLE]->(t:PgTable) WHERE t.id ENDS WITH '.information_unit' RETURN g.id AS trigger, t.id AS tbl ORDER BY trigger"),
    ("information_unit_impact_q1", "read-cypher", "MATCH (t:PgTable)<-[*1..3]-(x) WHERE t.id ENDS WITH '.information_unit' RETURN DISTINCT labels(x) AS l, count(*) AS c"),
    ("empty_in_certified_cell", "read-cypher", "MATCH (g:PgTrigger {id: 'public.no_such_table.no_such_trigger'}) RETURN g.id"),
    ("empty_in_partial_cell", "read-cypher", "MATCH (t:PgTable {id: 'public.no_such_table'}) RETURN t.id"),
    ("dot_registers", "read-cypher", "MATCH (r:DotRegistryEntry)-[:REGISTERS]->(c:DotCommand) RETURN r.id AS code, c.id AS cmd ORDER BY code LIMIT 5"),
    ("b88_order_union", "read-cypher", "MATCH (o:B88Order)-[:ORDER_MANAGED_BY_UNION]->(u:B88Union) RETURN o.order_code AS o, u.union_code AS u ORDER BY o LIMIT 3"),
    ("adversarial_call_db_labels", "read-cypher", "CALL db.labels() YIELD label RETURN label"),
    ("adversarial_unlabeled_scan", "read-cypher", "MATCH (n) RETURN count(n) AS c"),
    ("adversarial_uncertified_property", "read-cypher", "MATCH (g:PgTrigger) RETURN g.source_file AS f LIMIT 1"),
    ("adversarial_rel_property", "read-cypher", "MATCH (g:PgTrigger)-[r:ON_TABLE]->(t:PgTable) RETURN r.trust LIMIT 1"),
    ("adversarial_comment_hide", "read-cypher", "MATCH (g:PgTrigger) RETURN g.id LIMIT 1 // CALL db.labels()"),
    ("code_layer", "read-cypher", "MATCH (m:CodeModule) RETURN m.gs_key LIMIT 2"),
    ("syntax_error", "read-cypher", "MATCH (g:PgTrigger RETURN g"),
]
p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
msgs = [{"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2025-06-18", "capabilities": {},
                                                                       "clientInfo": {"name": "gs-c1a-probe", "version": "1"}}},
        {"jsonrpc": "2.0", "method": "notifications/initialized"}, {"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}},
        {"jsonrpc": "2.0", "id": 3, "method": "resources/list", "params": {}}, {"jsonrpc": "2.0", "id": 4, "method": "prompts/list", "params": {}},
        {"jsonrpc": "2.0", "id": 10, "method": "tools/call", "params": {"name": "get-schema", "arguments": {}}}]
for i, (name, tool, q) in enumerate(Q):
    msgs.append({"jsonrpc": "2.0", "id": 100 + i, "method": "tools/call", "params": {"name": tool, "arguments": {"query": q}}})
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
for mid, name in [("10", "get_schema")] + [(str(100 + i), n) for i, (n, _, _) in enumerate(Q)]:
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
                    "first_block": first, "rows": rows, "isError": r.get("isError") or ("error" in m), "reason": ((lab or {}).get("reason") or "")[:90]})
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
