#!/usr/bin/env python3
# GS-C1D-NATIVE-AUTOCOVER-20261023-10 · (khuôn c1c_probe) khách MCP stdio LẠNH chính thức qua graph-v1 (tiến trình mới): nhãn N4 có hàng rào
#   Graph (K1) + hàng rào danh mục (K3, catalog_revision), ô L1 bảng mẫu cũ + bảng lô mới, ô infra (cổng nghe→chủ · unit→đích · worktree),
#   phân trang L2, câu đối kháng. Dùng: c1d_probe.py <out.json> <lệnh ssh từ xa...>
import json, subprocess, sys, time

out, cmd = sys.argv[1], sys.argv[2:]
p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
NID = [100]


def send(m):
    p.stdin.write((json.dumps(m) + "\n").encode())
    p.stdin.flush()


def call(method, params, timeout=180):
    NID[0] += 1
    mid = NID[0]
    send({"jsonrpc": "2.0", "id": mid, "method": method, "params": params})
    t = time.time()
    while time.time() - t < timeout:
        line = p.stdout.readline()
        if not line:
            break
        try:
            m = json.loads(line)
        except ValueError:
            continue
        if m.get("id") == mid:
            return m
    return {"error": {"message": "timeout"}}


def label(m):
    r = m.get("result") or {}
    lab = (r.get("_meta") or {}).get("incomex.graph/completeness_v1")
    if lab is None and isinstance((m.get("error") or {}).get("data"), dict):
        lab = m["error"]["data"].get("incomex.graph/completeness_v1")
    first = ((r.get("content") or [{}])[0].get("text") or "")[:24]
    rows = None
    for c in (r.get("content") or [])[1:]:
        try:
            rows = len(json.loads(c.get("text") or ""))
        except (ValueError, TypeError):
            pass
    return lab or {}, first, rows, bool(r.get("isError") or "error" in m)


t0 = time.time()
init = call("initialize", {"protocolVersion": "2025-06-18", "capabilities": {}, "clientInfo": {"name": "gs-c1d-probe", "version": "1"}})
send({"jsonrpc": "2.0", "method": "notifications/initialized"})
tl = call("tools/list", {})
res = {"init_ok": "result" in init, "tools": [t.get("name") for t in (tl.get("result") or {}).get("tools") or []], "queries": [], "paging": {}}
IU = "MATCH (g:PgTrigger)-[:ON_TABLE]->(:PgTable {id: 'public.information_unit'}) RETURN g.id AS x ORDER BY x"
Q = [("l1_iu_triggers", "read-cypher", {"query": IU}),
     ("l1_new_law_catalog_fk", "read-cypher", {"query": "MATCH (t:PgTable {id: 'public.law_catalog'})-[:HAS_FK]->(f:PgForeignKey)-[:REFERENCES]->(d:PgTable) RETURN f.id AS fk, d.id AS d ORDER BY fk"}),
     ("l1_new_process_run_observation_in", "read-cypher", {"query": "MATCH (s:PgTable)-[:HAS_FK]->(f:PgForeignKey)-[:REFERENCES]->(t:PgTable {id: 'public.process_run_observation'}) RETURN f.id AS fk ORDER BY fk"}),
     ("cell_trigger_count", "read-cypher", {"query": "MATCH (g:PgTrigger)-[:ON_TABLE]->(t:PgTable) RETURN count(g) AS c"}),
     ("infra_listener_unit", "read-cypher", {"query": "MATCH (l:NetListener)-[:BOUND_BY_PROCESS_OF]->(u:SystemdUnit) RETURN l.id AS l, u.id AS u ORDER BY l, u"}),
     ("infra_listener_container", "read-cypher", {"query": "MATCH (l:NetListener)-[:PUBLISHED_BY]->(c:DockerContainer) RETURN l.id AS l, c.id AS c ORDER BY l"}),
     ("infra_socket_triggers", "read-cypher", {"query": "MATCH (s:SystemdUnit)-[:TRIGGERS]->(t:SystemdUnit) RETURN s.id AS s, t.id AS t ORDER BY s"}),
     ("infra_git_worktree", "read-cypher", {"query": "MATCH (a:GitRepository)-[:WORKTREE_OF]->(b:GitRepository) RETURN a.id AS a, b.id AS b"}),
     ("infra_container_count", "read-cypher", {"query": "MATCH (c:DockerContainer) RETURN count(c) AS c"}),
     ("empty_certified", "read-cypher", {"query": "MATCH (g:PgTrigger {id: 'public.no_such_table.no_such_trigger'}) RETURN g.id AS x"}),
     ("impact_iu", "read-cypher", {"query": "MATCH (t:PgTable {id: 'public.information_unit'})-[*1..3]-(x) RETURN count(DISTINCT x) AS c"}),
     ("adversarial_call", "read-cypher", {"query": "CALL db.labels() YIELD label RETURN label"}),
     ("adversarial_unlabeled", "read-cypher", {"query": "MATCH (n) RETURN count(n) AS c"}),
     ("syntax_error", "read-cypher", {"query": "MATCH (g:PgTrigger RETURN g"}),
     ("get_schema", "get-schema", {})]
for name, tool, args in Q:
    m = call("tools/call", {"name": tool, "arguments": args})
    lab, first, rows, err = label(m)
    gr = lab.get("graph_revision") or {}
    res["queries"].append({"q": name, "label": lab.get("completeness_label"), "act": lab.get("query_actionability"), "class": lab.get("query_class"),
                           "fence": gr.get("status"), "fence_why": gr.get("why"), "engine": lab.get("engine_version"), "first_block": first, "rows": rows,
                           "isError": err, "list_meta_keys": sorted((lab.get("list_meta") or {}).keys()),
                           "missing": len(lab.get("missing_or_unknown_cell_ids") or []), "source_freshness": (lab.get("source_freshness") or {}).get("mode"),
                           "l2_fresh": ((lab.get("layers") or {}).get("L2") or {}).get("freshness"), "reason": (lab.get("reason") or "")[:120],
                           "catalog": (lab.get("catalog_revision") or {}).get("status"), "l1": ((lab.get("layers") or {}).get("L1") or {}).get("label")})
# K2: đọc trọn danh sách L2 qua chính read-cypher theo next_cursor
got, cur, pages, metas = [], None, [], []
for _ in range(10):
    args = {"query": IU, "params": {"n4_page": cur}} if cur else {"query": IU}
    m = call("tools/call", {"name": "read-cypher", "arguments": args})
    lab, first, rows, err = label(m)
    meta = (lab.get("list_meta") or {}).get("layers.L2.candidates") or {}
    metas.append(meta)
    got += [json.dumps(c, sort_keys=True, ensure_ascii=False) for c in ((lab.get("layers") or {}).get("L2") or {}).get("candidates") or []]
    pages.append({"shown": meta.get("shown"), "offset": meta.get("offset"), "rows": rows, "isError": err, "label": lab.get("completeness_label"),
                  "paging": ((lab.get("layers") or {}).get("L2") or {}).get("paging")})
    cur = meta.get("next_cursor")
    if not cur:
        break
res["paging"] = {"total": (metas[0] if metas else {}).get("total"), "collected": len(got), "unique": len(set(got)), "pages": pages}
c1 = (metas[0] if metas else {}).get("next_cursor")
m = call("tools/call", {"name": "read-cypher", "arguments": {"query": "MATCH (g:PgTrigger)-[:ON_TABLE]->(:PgTable {id: 'public.agents'}) RETURN g.id AS x",
                                                                "params": {"n4_page": c1}}})
lab, first, rows, err = label(m)
res["paging"]["scope_mismatch"] = ((lab.get("layers") or {}).get("L2") or {}).get("paging")
m = call("tools/call", {"name": "read-cypher", "arguments": {"query": IU, "params": {"n4_page": "n4p1:bogus"}}})
lab, first, rows, err = label(m)
res["paging"]["malformed"] = ((lab.get("layers") or {}).get("L2") or {}).get("paging")
res["paging"]["malformed_rows_ok"] = rows
res["seconds"] = round(time.time() - t0, 1)
p.stdin.close()
try:
    p.wait(timeout=30)
except subprocess.TimeoutExpired:
    p.kill()
res["rc"] = p.returncode
res["stderr_tail"] = p.stderr.read().decode(errors="replace")[-300:]
json.dump(res, open(out, "w"), ensure_ascii=False, indent=1)
print(json.dumps({k: res[k] for k in ("init_ok", "tools", "seconds", "rc")}, ensure_ascii=False))
for q in res["queries"]:
    print(json.dumps({k: q[k] for k in ("q", "label", "act", "class", "fence", "catalog", "engine", "rows", "isError", "missing", "reason")}, ensure_ascii=False))
print(json.dumps({k: v for k, v in res["paging"].items() if k != "pages"}, ensure_ascii=False))
print(json.dumps([(x["shown"], x["offset"], x["rows"], x["label"]) for x in res["paging"]["pages"]], ensure_ascii=False))
