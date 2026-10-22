#!/usr/bin/env python3
# GS-C1A-CERT-QUALITYGATE-20261022-07 · ma trận lỗi giả §6 (fixture CÔ LẬP: nguồn tiêm + Graph giả + thư mục tạm; không ghi production,
# không mạng Kuma/Telegram). Mỗi ca hỏng phải ra MỘT PHẦN/NOT_ACTION_SAFE + biên nhận; ca dương thật lấy từ lượt cấp giấy thật.
# Dùng: c1a_fixtures.py <scripts_dir> <guard_candidate> <graph_refresh_candidate> <real_run.json> <out.json>
import copy, importlib.machinery, importlib.util, json, os, shutil, sys, tempfile, time

S, GUARD, REFRESH, REAL, OUT = sys.argv[1:6]
TMP = tempfile.mkdtemp(prefix="gs-c1a-fx-", dir="/dev/shm")
CAT = TMP + "/cells.json"
os.environ.update(GS_CERT_CELLS=CAT, GS_CERT_DIR=TMP + "/cert", GS_CERT_BASELINE=TMP + "/baseline.json")
sys.path.insert(0, S)
import graph_cert as G  # noqa: E402

DU, MP = G.DU, G.MP
results = []


def case(cid, name, ok, detail=""):
    results.append({"id": cid, "case": name, "pass": bool(ok), "detail": str(detail)[:300]})
    print("%-4s %-62s %s %s" % (cid, name[:62], "PASS" if ok else "FAIL", str(detail)[:150]), flush=True)


# ---------------------------------------------------------------- Graph giả hiểu đúng các mẫu Cypher của graph_cert
class FakeG:
    def __init__(self, nodes, edges, truncate_at=None):
        self.nodes, self.edges, self.cap = nodes, edges, truncate_at   # nodes {label: [(id, [attrs])]} · edges {type: [(s, d, A, B)]}

    def password(self):
        return ""

    def invariants(self, pw):
        return {"gs_keys_sha256": "fixture", "edges_sha256": "fixture", "gs_keys_count": sum(len(v) for v in self.nodes.values()), "edges_count": 0}

    def http_cypher(self, stmts, pw, timeout=0):
        (q, p), = stmts
        import re
        def res(cols, rows):
            return {"results": [{"columns": cols, "data": [{"row": r} for r in rows]}], "errors": []}
        m = re.match(r"MATCH \(n:`(\w+)`\) RETURN count\(n\)", q)
        if m:
            return res(["c"], [[len(self.nodes.get(m.group(1), []))]])
        m = re.match(r"MATCH \(n:`(\w+)`\) WHERE n.gs_key > \$after", q)
        if m:
            lab = m.group(1)
            pref = {"PgTrigger": "pg:trigger:"}.get(lab, "x:")
            rows = sorted((pref + i, i, a) for i, a in self.nodes.get(lab, []))
            if self.cap is not None:
                rows = rows[:self.cap]                      # mô phỏng bộ đọc cũ LIMIT 9000
            rows = [r for r in rows if r[0] > p["after"]][:p["page"]]
            return res(["k", "id", "av", "gs"], [[k, i, a, True] for k, i, a in rows])
        m = re.match(r"MATCH \(\)-\[r:`(\w+)`\]->\(\) RETURN count", q)
        if m:
            return res(["c"], [[len(self.edges.get(m.group(1), []))]])
        m = re.match(r"MATCH \(:`(\w+)`\)-\[r:`(\w+)`\]->\(:`(\w+)`\) RETURN count", q)
        if m:
            return res(["c"], [[sum(1 for e in self.edges.get(m.group(2), []) if e[2] == m.group(1) and e[3] == m.group(3))]])
        m = re.match(r"MATCH \(x:`(\w+)`\)-\[r:`(\w+)`\]->\(y:`(\w+)`\)", q)
        if m:
            rows = sorted(("%s|%s|%d" % (s, d, n), s, d) for n, (s, d, a, b) in enumerate(self.edges.get(m.group(2), []))
                          if a == m.group(1) and b == m.group(3))
            rows = [r for r in rows if r[0] > p["after"]][:p["page"]]
            return res(["k", "s", "d", "prov"], [[k, s, d, True] for k, s, d in rows])
        raise RuntimeError("fake: không hiểu " + q[:60])


TRG_CELL = {"key": "pg:directus:trigger", "gate": "G1", "parent": "pg:directus", "source": {"adapter": "pg", "db": "directus", "classes": ["trigger"]},
            "scope": "fixture trigger", "graph": {"nodes": [{"label": "PgTrigger", "prefix": "pg:trigger:", "attrs": ["enabled_code"]}],
                                                  "edges": [{"type": "ON_TABLE", "from": "PgTrigger", "to": "PgTable", "prov": ["trust"]},
                                                            {"type": "EXECUTES", "from": "PgTrigger", "to": "PgFunction", "prov": ["trust"]}]}}
FK_CELL = {"key": "pg:directus:fk", "gate": "G1", "parent": "pg:directus", "source": {"adapter": "pg", "db": "directus", "classes": ["fk"]}, "scope": "fk", "graph": None}
FLOW_CELL = {"key": "directus:flow", "gate": "G1", "parent": "pg:directus", "source": {"adapter": "pg", "db": "directus", "classes": ["directus_flow", "directus_operation"]},
             "scope": "flow", "graph": None}
EMPTY_CELL = {"key": "pg:workflow:trigger", "gate": "G1", "parent": "pg:workflow", "source": {"adapter": "pg", "db": "workflow", "classes": ["trigger"]},
              "scope": "empty", "graph": None}
DOT_CELL = {"key": "dot:command", "gate": "G6", "parent": "opt", "source": {"adapter": "dot_bin"}, "scope": "dot", "graph": {"nodes": [{"label": "DotCommand", "prefix": "x:"}]}}
LARK_CELL = {"key": "lark:b1:schema", "gate": "G8", "parent": "lark:b1", "source": {"adapter": "lark_schema", "base": "b1"}, "scope": "lark", "graph": None}
DOCK_CELL = {"key": "docker:container", "gate": "G2", "parent": "docker", "source": {"adapter": "docker"}, "scope": "docker", "graph": None}
MB_CELL = {"key": "kb:production_documents", "gate": "G7", "parent": "qdrant:production_documents", "source": {"adapter": "mb"}, "scope": "mb", "graph": None}
CAT_BASE = {"format": "graph-cert-cells-v1", "catalog_version": "fixture", "ttl_hours": 26,
            "graph_label_map": {"PgTrigger": ["pg:directus:trigger"], "PgTable": ["pg:directus:table"], "PgFunction": ["pg:directus:function"]},
            "graph_rel_map": {"ON_TABLE": ["pg:directus:trigger"], "EXECUTES": ["pg:directus:trigger"]},
            "certified_props": {"PgTrigger": ["id", "gs_key", "enabled_code"], "PgTable": ["id", "gs_key"]}, "endpoint_cover": {"PgTable": ["ON_TABLE"]}}


def trig_rows(n):
    return [["public", "t%d" % (i % 7), "trg%05d" % i, "public", "fn%d" % (i % 3), "", "O"] for i in range(n)]


def pg_inject(rows, extra=None, db_ok=True, cls_ok=True, dbs=("directus", "postgres")):
    d = {"directus": {"reader": {"role": "fx"}, "classes": {"trigger": {"ok": cls_ok, "rows": rows} if cls_ok else {"ok": False, "error": "NO_ACCESS InsufficientPrivilege"}}},
         "postgres": {"reader": {}, "classes": {"databases": {"ok": True, "rows": [[x] for x in dbs]}}},
         "workflow": {"reader": {}, "classes": {"trigger": {"ok": True, "rows": []}}}}
    if not db_ok:
        d["directus"] = {"error": "connect OperationalError"}
    for k, v in (extra or {}).items():
        d["directus"]["classes"][k] = v
    return d


def graph_for(rows, drop_edge=False, extra_node=False, swap=False):
    nodes = {"PgTrigger": [("%s.%s.%s" % (r[0], r[1], r[2]), [r[6]]) for r in rows]}
    edges = {"ON_TABLE": [("%s.%s.%s" % (r[0], r[1], r[2]), "%s.%s" % (r[0], r[1]), "PgTrigger", "PgTable") for r in rows],
             "EXECUTES": [("%s.%s.%s" % (r[0], r[1], r[2]), "%s.%s()" % (r[3], r[4]), "PgTrigger", "PgFunction") for r in rows]}
    if drop_edge:
        edges["ON_TABLE"] = edges["ON_TABLE"][1:]
    if extra_node:
        nodes["PgTrigger"].append(("public.t0.extra_trigger", ["O"]))
    if swap:
        nodes["PgTrigger"][0] = ("public.t0.swapped_id", nodes["PgTrigger"][0][1])
    return nodes, edges


def run_cells(cells, inj, g, now=None):
    json.dump(dict(CAT_BASE, cells=cells), open(CAT, "w"))
    return G.run(g, "", injected=inj, write=False, now=now)


def other_inj():
    return {"docker": {"error": "fx"}, "systemd": {"error": "fx"}, "cron": {"_error": "fx"}, "nginx": {"error": "fx"}, "opt": {"error": "fx"},
            "qdrant": {"error": "fx"}, "git": {"error": "fx"}}


R = trig_rows(5)
base_inj = lambda **k: dict(other_inj(), pg=pg_inject(R, **k))
try:
    # ---- dương trên fixture (đối chứng) + các ca hỏng đối tượng/cạnh
    d = run_cells([TRG_CELL], base_inj(), FakeG(*graph_for(R)))
    c = d["cells"]["pg:directus:trigger"]
    case("F00", "đối chứng fixture: nguồn = Graph ⇒ ĐỦ", c["status"] == DU, c.get("proof"))
    for cid, name, kw in (("F01", "thừa 1 nút trong Graph", {"extra_node": True}), ("F02", "thiếu 1 cạnh, số nút bằng nhau", {"drop_edge": True}),
                          ("F03", "cùng tổng nhưng tráo 1 ID", {"swap": True})):
        c = run_cells([TRG_CELL], base_inj(), FakeG(*graph_for(R, **kw)))["cells"]["pg:directus:trigger"]
        case(cid, name + " ⇒ MỘT PHẦN", c["status"] == MP, c["reasons"])
    c = run_cells([TRG_CELL], dict(other_inj(), pg=pg_inject(trig_rows(6))), FakeG(*graph_for(R)))["cells"]["pg:directus:trigger"]
    case("F04", "trigger con mới trong DB PG cũ ⇒ MỘT PHẦN", c["status"] == MP, c["reasons"])
    a = run_cells([FK_CELL, FLOW_CELL], dict(other_inj(), pg=pg_inject(R, extra={"fk": {"ok": True, "rows": [["public.a", "fk1", "public.b"]]},
                                                                               "directus_flow": {"ok": True, "rows": [["f1", "event", "active"]]},
                                                                               "directus_operation": {"ok": True, "rows": [["o1", "f1"]]}})), FakeG({}, {}))
    b = run_cells([FK_CELL, FLOW_CELL], dict(other_inj(), pg=pg_inject(R, extra={"fk": {"ok": True, "rows": [["public.a", "fk1", "public.b"], ["public.a", "fk2", "public.c"]]},
                                                                               "directus_flow": {"ok": True, "rows": [["f1", "event", "active"], ["f2", "webhook", "active"]]},
                                                                               "directus_operation": {"ok": True, "rows": [["o1", "f1"]]}})), FakeG({}, {}))
    case("F04b", "FK mới cùng DB ⇒ băm nguồn đổi + ô MỘT PHẦN",
         a["cells"]["pg:directus:fk"]["source"]["edges_sha256"] != b["cells"]["pg:directus:fk"]["source"]["edges_sha256"] and b["cells"]["pg:directus:fk"]["status"] == MP, "")
    case("F04c", "flow Directus mới ⇒ băm nguồn đổi + ô MỘT PHẦN",
         a["cells"]["directus:flow"]["source"]["objects_sha256"] != b["cells"]["directus:flow"]["source"]["objects_sha256"] and b["cells"]["directus:flow"]["status"] == MP, "")
    la = {"b1": {"tables": ["t1", "t2"], "tables_after": ["t1", "t2"], "links": [["t1", "f1", "t2"]], "field_errors": []}}
    lb = copy.deepcopy(la)
    lb["b1"]["links"].append(["t2", "f9", "t1"])
    x = run_cells([LARK_CELL], dict(other_inj(), pg=pg_inject(R), lark=la), FakeG({}, {}))["cells"]["lark:b1:schema"]
    y = run_cells([LARK_CELL], dict(other_inj(), pg=pg_inject(R), lark=lb), FakeG({}, {}))["cells"]["lark:b1:schema"]
    case("F05", "link Lark mới trong base cũ ⇒ băm cạnh đổi, MỘT PHẦN", x["source"]["edges_sha256"] != y["source"]["edges_sha256"] and y["status"] == MP, "")
    dk = {"containers": [["c1", "sha256:aaa"]], "edges": [["c1", "USES_IMAGE", "sha256:aaa"]], "images": ["sha256:aaa"], "ok": True, "names_before": ["c1"], "names_after": ["c1"]}
    dk2 = copy.deepcopy(dk)
    dk2["containers"] = [["c1", "sha256:bbb"]]
    dk2["edges"] = [["c1", "USES_IMAGE", "sha256:bbb"]]
    i1 = dict(other_inj(), pg=pg_inject(R), docker=dk)
    i2 = dict(other_inj(), pg=pg_inject(R), docker=dk2)
    x = run_cells([DOCK_CELL], i1, FakeG({}, {}))["cells"]["docker:container"]
    y = run_cells([DOCK_CELL], i2, FakeG({}, {}))["cells"]["docker:container"]
    case("F06", "mã triển khai đổi trong container cũ ⇒ băm đổi, MỘT PHẦN", x["source"]["objects_sha256"] != y["source"]["objects_sha256"] and y["status"] == MP, "")
    CRON_CELL = {"key": "cron:entry", "gate": "G4", "parent": "cron", "source": {"adapter": "cron"}, "scope": "cron",
                 "graph": {"nodes": [{"label": "CronEntry", "prefix": "x:"}]}}
    cr = {"entries": [["f|* * * * *|/a"]], "edges": [], "errors": []}
    c = run_cells([CRON_CELL], dict(other_inj(), pg=pg_inject(R), cron=cr), FakeG({"CronEntry": [("f|* * * * *|/a", [])]}, {}))["cells"]["cron:entry"]
    case("F08b", "bộ đọc chỉ đọc một lần ⇒ không có ranh giới nhất quán ⇒ không ĐỦ", c["status"] == MP and any("NO_CONSISTENCY_PROOF" in r or "DRIFT" in r for r in c["reasons"]), c["reasons"])
    c = run_cells([CRON_CELL], dict(other_inj(), pg=pg_inject(R), cron=cr, cron_after=copy.deepcopy(cr)), FakeG({"CronEntry": [("f|* * * * *|/a", [])]}, {}))["cells"]["cron:entry"]
    case("F08c", "đọc lại trước = sau ⇒ BEFORE_AFTER_EQUAL ⇒ ĐỦ (đối chứng)", c["status"] == DU and c["source"]["consistency"] == "BEFORE_AFTER_EQUAL", c.get("proof"))
    c = run_cells([TRG_CELL], base_inj(cls_ok=False), FakeG(*graph_for(R)))["cells"]["pg:directus:trigger"]
    case("F07", "bộ đọc nguồn bị từ chối quyền ⇒ MỘT PHẦN NO_ACCESS", c["status"] == MP and "NO_ACCESS" in c["reasons"][0], c["reasons"])
    dd = {"format": G.FORMAT, "generated_at": G.now_iso(), "cells": {"pg:directus:trigger": c}, "directory": None}
    dd["self_sha256"] = G.self_sha(dd)
    st, msg, inc = G.alarm(dd, baseline={"certified_floor": ["pg:directus:trigger"]})
    case("F07b", "mất quyền ở ô thuộc sàn ĐỦ ⇒ đèn DOWN + biên nhận có tên ô", st == "down" and any(i["cell"] == "pg:directus:trigger" for i in inc), msg)
    c = run_cells([DOT_CELL], dict(other_inj(), pg=pg_inject(R), dot_bin={"commands": ["a", "b"], "commands_after": ["a", "b", "c"]}),
                  FakeG({"DotCommand": [("a", []), ("b", [])]}, {}))["cells"]["dot:command"]
    case("F08", "nguồn đổi giữa lúc liệt kê và cấp ⇒ DRIFT ⇒ MỘT PHẦN", c["status"] == MP and "SOURCE_DRIFT_DURING_READ" in c["reasons"], c["reasons"])
    d = run_cells([TRG_CELL], dict(other_inj(), pg=pg_inject(R, dbs=("directus", "postgres", "newdb"))), FakeG(*graph_for(R)))
    dr = d["directory"]
    st, msg, inc = G.alarm(d, baseline={})
    case("F09", "nguồn mới ở cửa (DB PG mới) ⇒ thư mục MỘT PHẦN + NEW_SOURCE_UNHANDLED", dr["status"] == MP and "pg:newdb" in dr["new_source_unhandled"]
         and any(i["kind"] == "NEW_SOURCE_UNHANDLED" for i in inc), dr["reasons"][:3])
    c = run_cells([TRG_CELL], base_inj(db_ok=False), FakeG(*graph_for(R)))["cells"]["pg:directus:trigger"]
    case("F10", "nguồn chưa kiểm chứng (bộ đọc hỏng) ⇒ không ĐỦ", c["status"] == MP and c["reasons"][0].startswith("READER_FAIL"), c["reasons"])
    c = run_cells([TRG_CELL], dict(other_inj(), pg=pg_inject([])), FakeG(*graph_for(R)))["cells"]["pg:directus:trigger"]
    case("F10b", "nguồn trả 0 hàng nhưng Graph có ⇒ MỘT PHẦN (0 ≠ rỗng đã chứng minh)", c["status"] == MP, c["reasons"])
    c = run_cells([EMPTY_CELL], base_inj(), FakeG({}, {}))["cells"]["pg:workflow:trigger"]
    case("F10c", "lớp rỗng có bằng chứng bộ đọc gốc đọc trọn ⇒ ĐỦ (NATIVE_EMPTY)", c["status"] == DU and "NATIVE_EMPTY" in c["proof"], c.get("proof"))
    R9 = trig_rows(9500)
    c = run_cells([TRG_CELL], dict(other_inj(), pg=pg_inject(R9)), FakeG(*graph_for(R9)))["cells"]["pg:directus:trigger"]
    case("F11", "Graph 9.500 ID phân trang trọn ⇒ ĐỦ (đối chứng)", c["status"] == DU and c["graph"]["pages"]["PgTrigger"] >= 5, c["graph"]["pages"])
    c = run_cells([TRG_CELL], dict(other_inj(), pg=pg_inject(R9)), FakeG(*graph_for(R9), truncate_at=9000))["cells"]["pg:directus:trigger"]
    case("F11b", "Graph bị cắt ở 9.000 (kiểu LIMIT 9000 cũ) ⇒ GRAPH_INCOMPLETE ⇒ MỘT PHẦN", c["status"] == MP and any("GRAPH_INCOMPLETE" in r for r in c["reasons"]), c["reasons"][:2])
    # ---- hạn, lượt bỏ qua, giấy hỏng, nhãn
    good = run_cells([TRG_CELL], base_inj(), FakeG(*graph_for(R)))
    good["directory"] = None                                 # chỉ ô trigger (thư mục fixture không có cửa đọc được)
    good["self_sha256"] = G.self_sha(good)
    cat = dict(CAT_BASE, cells=[TRG_CELL])
    q = "MATCH (g:PgTrigger)-[:ON_TABLE]->(t:PgTable {id: 'public.t0'}) RETURN g.id"
    lab = G.label_for("read-cypher", {"query": q}, 3, doc=good, cat=cat)
    case("F12a", "giấy còn hạn ⇒ nhãn ĐỦ + ACTIONABLE_ONLY_WITH_FRESH_PROOF", lab["completeness_label"] == DU and lab["query_actionability"] == G.ACT_OK, lab["reason"])
    t26 = G.parse_iso(good["cells"]["pg:directus:trigger"]["expires_at"]) + 1
    lab = G.label_for("read-cypher", {"query": q}, 3, doc=good, cat=cat, now=t26)
    case("F12b", "quá 26 h ⇒ EXPIRED ⇒ MỘT PHẦN", lab["completeness_label"] == MP and "pg:directus:trigger" in lab["missing_or_unknown_cell_ids"], lab["reason"])
    st, msg, inc = G.alarm(None, "lượt làm mới bỏ qua: tiền điều kiện guard", baseline={})
    case("F12c", "lượt bị bỏ qua ⇒ đèn DOWN OPERATIONAL (không bao giờ xanh)", st == "down" and inc[0]["kind"] == "OPERATIONAL", msg)
    lab = G.label_for("read-cypher", {"query": q}, 3, doc=None, cat=cat)
    case("F13a", "giấy bị xoá ⇒ MỘT PHẦN", lab["completeness_label"] == MP and lab["reason"] == "MANIFEST_MISSING_OR_BAD_FORMAT", lab["reason"])
    bad = copy.deepcopy(good)
    bad["cells"]["pg:directus:trigger"]["expires_at"] = "2099-01-01T00:00:00Z"
    lab = G.label_for("read-cypher", {"query": q}, 3, doc=bad, cat=cat)
    case("F13b", "giấy bị sửa tay (kéo dài hạn) ⇒ self_sha256 lệch ⇒ MỘT PHẦN", lab["completeness_label"] == MP and "CORRUPT" in lab["reason"], lab["reason"])
    fut = copy.deepcopy(good)
    fut["generated_at"] = "2099-01-01T00:00:00Z"
    fut["self_sha256"] = G.self_sha(fut)
    lab = G.label_for("read-cypher", {"query": q}, 3, doc=fut, cat=cat)
    case("F13c", "đồng hồ/giờ cấp ở tương lai ⇒ MỘT PHẦN", lab["completeness_label"] == MP and "CLOCK" in lab["reason"], lab["reason"])
    lab = G.label_for("read-cypher", {"query": "MATCH (g:PgTrigger {id: 'none'}) RETURN g.id"}, 0, doc=good, cat=cat)
    case("F15a", "kết quả rỗng trong ô ĐỦ ⇒ ĐỦ (vắng được chứng nhận)", lab["completeness_label"] == DU and "rỗng" in lab["reason"], lab["reason"])
    lab = G.label_for("read-cypher", {"query": "MATCH (t:PgTable {id: 'none'}) RETURN t.id"}, 0, doc=good, cat=cat)
    case("F15b", "kết quả rỗng trong ô chưa ĐỦ ⇒ MỘT PHẦN, không suy vắng", lab["completeness_label"] == MP and "KHÔNG" in lab["reason"], lab["reason"])
    for cid, qq in (("F16a", "CALL db.labels() YIELD label RETURN label"), ("F16b", "MATCH (n) RETURN count(n)"),
                    ("F16c", "MATCH (g:PgTrigger) RETURN g"), ("F16d", "MATCH (g:PgTrigger)-[*1..3]-(x) RETURN count(x)"),
                    ("F16e", "MATCH (g:PgTrigger) RETURN g.source_file")):
        lab = G.label_for("read-cypher", {"query": qq}, 1, doc=good, cat=cat)
        case(cid, "Cypher thô/đối kháng ⇒ MỘT PHẦN: " + qq[:40], lab["completeness_label"] == MP and lab["query_actionability"] == G.ACT_NO, lab["query_class"])
    lab = G.label_for("get-schema", {}, None, doc=good, cat=cat)
    case("F16f", "get-schema ⇒ MỘT PHẦN", lab["completeness_label"] == MP, lab["reason"])
    # ---- M-b
    kb = {"incomex_metadata": {"reader": {}, "classes": {"kb": {"ok": True, "rows": [["a", "a", False, "ready"], ["b", "b", False, "ready"], ["c", "c", True, "deleted"]]}}}}
    qd_ok = {"count_before": 2, "count_after": 2, "points_scrolled": 2, "scroll_complete": True, "pages": 1, "doc_ids": ["a", "b"], "points_without_document_id": 0}
    qd_bad = dict(qd_ok, doc_ids=["a", "c"])
    c = run_cells([MB_CELL], dict(other_inj(), pg=pg_inject(R), pg_kb=kb, qdrant_ids=qd_ok), FakeG({}, {}))["cells"]["kb:production_documents"]
    case("F14a", "KB↔Qdrant khớp ID ⇒ ĐỦ (đối chứng)", c["status"] == DU, c["mb"]["buckets"])
    c = run_cells([MB_CELL], dict(other_inj(), pg=pg_inject(R), pg_kb=kb, qdrant_ids=qd_bad), FakeG({}, {}))["cells"]["kb:production_documents"]
    case("F14b", "KB↔Qdrant lệch ID (thiếu b, thừa c đã xoá mềm) ⇒ MỘT PHẦN + nhóm", c["status"] == MP and c["mb"]["buckets"]["qdrant_but_soft_deleted"] == 1
         and c["mb"]["buckets"]["pg_ready_missing_in_qdrant"] == 1, c["mb"]["buckets"])
    c = run_cells([MB_CELL], dict(other_inj(), pg=pg_inject(R), pg_kb=kb, qdrant_ids=dict(qd_ok, count_after=3)), FakeG({}, {}))["cells"]["kb:production_documents"]
    case("F14c", "Qdrant đổi trong lúc cuộn ⇒ không ĐỦ (READER_FAIL)", c["status"] == MP and "READER_FAIL" in c["reasons"][0], c["reasons"])
    # ---- biên nhận sự cố mới khi đèn đã DOWN + ACK không làm xanh
    i1 = [{"kind": "COVERAGE_MOT_PHAN", "cell": "a", "reason": "x", "id": "aaaa"}]
    n1, _ = G.record_incidents(i1)
    n2, g2 = G.record_incidents(i1 + [{"kind": "OPERATIONAL", "cell": "b", "reason": "y", "id": "bbbb"}])
    n3, g3 = G.record_incidents([{"kind": "OPERATIONAL", "cell": "b", "reason": "y", "id": "bbbb"}])
    case("F21", "lỗi mới khi đèn đã DOWN ⇒ biên nhận riêng (MỚI) + đóng sự cố đã hồi", [i["id"] for i in n2] == ["bbbb"] and not n3 and [i["id"] for i in g3] == ["aaaa"],
         {"new2": [i["id"] for i in n2], "resolved3": [i["id"] for i in g3]})
    acc = {"accepted_partial": {"pg:directus:trigger": {"gap": "fx", "reader_pass": True}}}
    partial = run_cells([TRG_CELL], base_inj(), FakeG(*graph_for(R, extra_node=True)))
    partial["directory"] = None
    partial["self_sha256"] = G.self_sha(partial)
    st, msg, inc = G.alarm(partial, baseline=acc)
    lab = G.label_for("read-cypher", {"query": q}, 3, doc=partial, cat=cat)
    case("F22", "ACK mốc chỉ dập tin (đèn UP) — nhãn vẫn MỘT PHẦN", st == "up" and lab["completeness_label"] == MP, (st, lab["completeness_label"]))
    st, msg, inc = G.alarm(partial, baseline={"certified_floor": ["pg:directus:trigger"], "accepted_partial": {}})
    case("F22b", "ô thuộc sàn ĐỦ tụt (thừa nút) ⇒ DOWN COVERAGE_REGRESSION", st == "down" and "COVERAGE_REGRESSION" in msg, msg)
    st, msg, inc = G.alarm(partial, baseline={"accepted_partial": {}})
    case("F22c", "ô chưa từng ĐỦ, chưa nhận mốc ⇒ không gọi trang, biên nhận PENDING_HOST_ACK + nêu tên", st == "up" and "chờ Host" in msg
         and any(i["kind"] == "PENDING_HOST_ACK" for i in inc), msg)
    exp_doc = copy.deepcopy(good)
    st, msg, inc = G.alarm(exp_doc, now=G.parse_iso(good["cells"]["pg:directus:trigger"]["expires_at"]) + 5, baseline={"certified_floor": ["pg:directus:trigger"]})
    case("F12d", "giấy sàn hết hạn (không cấp lại) ⇒ DOWN COVERAGE_REGRESSION", st == "down" and "COVERAGE_REGRESSION" in msg, msg)

    # ---- Guard thật (bản ứng viên): DOWN còn nhịp không làm #22 đỏ; câm / thiếu đăng ký ⇒ đỏ
    def load(path, name):
        ld = importlib.machinery.SourceFileLoader(name, path)
        sp = importlib.util.spec_from_loader(name, ld)
        m = importlib.util.module_from_spec(sp)
        ld.exec_module(m)
        return m
    gd = load(GUARD, "guard_cand")
    kf = gd.kuma_coverage_facts()
    now = kf["now"]
    ts = lambda age: time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(now - age))
    base_mons = [m for m in kf["monitors"] if m[0] != 24]
    kf["bang_den_total"] = len(base_mons) + 1

    def with24(status, age, active=1, links="2", present=True):
        f = copy.deepcopy(kf)
        f["monitors"] = base_mons + ([(24, "Graph Certificate (C1-A)", "push", active, 90000, ts(age), links, status)] if present else [])
        f["bang_den_total"] = len(f["monitors"])
        return f
    r = gd.c_kuma_coverage(with24(0, 60))
    case("F17a", "#24 DOWN còn nhịp ⇒ INV15 PASS (không làm #22 đỏ), liệt kê đèn dịch vụ đỏ", r[1] and "#24" in r[2], r[2][:150])
    r = gd.c_kuma_coverage(with24(0, 90000 + 301))
    case("F19", "#24 câm > chu kỳ+300 s ⇒ INV15 FAIL (đèn câm)", not r[1] and "câm" in r[2], r[2][:150])
    r = gd.c_kuma_coverage(with24(0, 60, present=False))
    case("F18a", "Guard đã đăng ký #24 nhưng đèn mất ⇒ INV15 FAIL", not r[1] and "#24" in r[2], r[2][:150])
    r = gd.c_kuma_coverage(with24(0, 60, active=0))
    case("F18b", "#24 bị tạm dừng ⇒ INV15 FAIL", not r[1], r[2][:150])
    # INV16: dòng A24 + nguồn gửi graph-refresh
    tbf = gd.tin_bao_facts(["INV15.kuma_telegram_coverage"], with24(0, 60), now)
    tbf["found"]["path:/opt/incomex/graph-server/prod-v1/bin/graph-refresh"] = "incomex-graph-refresh.service"
    row = gd.c_tin_bao(tbf)
    a24 = [x for x in gd.TB_LAST["rows"] if x["ma"] == "A24"]
    case("F17b", "INV16 có A24: đèn DOWN còn nhịp ⇒ 'đang đỏ (vẫn báo được)', không làm sổ đỏ vì A24",
         a24 and a24[0]["trang_thai"] == "chạy" and not any("A24" in x for x in gd.TB_LAST["loi"]), (a24[0]["ly_do"] if a24 else None, gd.TB_LAST["loi"][:2]))
    go = load(GUARD.replace("guard.new", "guard.orig"), "guard_orig") if os.path.exists(GUARD.replace("guard.new", "guard.orig")) else None
    if go:
        tbo = go.tin_bao_facts(["INV15.kuma_telegram_coverage"], with24(0, 60), now)
        tbo["found"]["path:/opt/incomex/graph-server/prod-v1/bin/graph-refresh"] = "incomex-graph-refresh.service"
        go.c_tin_bao(tbo)
        case("F18c", "nguồn gửi graph-refresh KHÔNG có dòng sổ (Guard cũ) ⇒ INV16 'nguồn ngoài sổ' ĐỎ",
             any("graph-refresh" in x and "ngoài sổ" in x for x in go.TB_LAST["loi"]), go.TB_LAST["loi"][:2])
    # ---- tự khoá: Guard đỏ ⇒ graph-refresh SKIP ⇒ nhịp DOWN thật ⇒ #24 còn nhịp ⇒ INV15 vẫn PASS ⇒ lượt sau Guard xanh ⇒ UP hợp lệ
    rf = load(REFRESH, "graph_refresh_cand")
    pushed = []
    rf.cert_push = lambda st, msg: pushed.append((st, msg)) or {"pushed": True, "status": st, "fixture": True}
    rf.preconditions = lambda g, pw, need_vps=True: ({"guard": {"ok": False, "why": "fixture Guard đỏ"}}, ["guard"])
    rf.logline = lambda rec: None
    rf.r7_g1lib.load = lambda path=None: FakeG(*graph_for(R))
    rf.GC.run = lambda *a, **k: copy.deepcopy(good)
    rf.take_lock = lambda trig: open(os.devnull, "w")

    class A:
        execute, trigger = True, "timer"
    rc = rf.cmd_run(A())
    case("F20a", "Guard đỏ ⇒ graph-refresh SKIP (rc 0) ⇒ đẩy nhịp DOWN thật, không ghi Graph", rc == 0 and pushed and pushed[-1][0] == "down"
         and "bỏ qua" in pushed[-1][1], pushed[-1] if pushed else None)
    r = gd.c_kuma_coverage(with24(0, 30))
    case("F20b", "nhịp DOWN đó ⇒ #24 còn nhịp ⇒ INV15 PASS ⇒ #22 không đỏ vì Graph (không tự khoá)", r[1], r[2][:120])
    rec = {"cmd": "run", "trigger": "timer"}
    orig_alarm = G.alarm                                     # rf.GC LÀ module G ⇒ giữ hàm gốc trước khi thay
    rf.GC.alarm = lambda doc, op_failure=None, now=None, baseline=None: orig_alarm(doc, op_failure, now, {"accepted_partial": {}})
    out = rf.cert_tick(rec, None, None, op_failure=None)
    case("F20c", "lượt sau Guard xanh, không tụt mốc ⇒ UP hợp lệ (không giả)", (out.get("alarm") or {}).get("status") == "up" and pushed[-1][0] == "up",
         out.get("alarm") or out.get("alarm_error"))
finally:
    shutil.rmtree(TMP, ignore_errors=True)

summary = {"total": len(results), "pass": sum(r["pass"] for r in results), "fail": [r["id"] for r in results if not r["pass"]]}
real = json.load(open(REAL))
t = real["cells"]["pg:directus:trigger"]
summary["positive_real_cell"] = {"cell": "pg:directus:trigger", "status": t["status"], "source": t["source"], "graph": {k: t["graph"][k] for k in ("objects_count", "objects_sha256", "edges_count", "edges_sha256", "complete", "totals")},
                                 "issued_at": t.get("issued_at"), "expires_at": t.get("expires_at")}
json.dump({"summary": summary, "results": results}, open(OUT, "w"), ensure_ascii=False, indent=1)
print("FIXTURES %d/%d PASS fail=%s · dương thật pg:directus:trigger=%s" % (summary["pass"], summary["total"], summary["fail"], t["status"]))
sys.exit(0 if not summary["fail"] else 1)
