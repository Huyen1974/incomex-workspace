#!/usr/bin/env python3
# GS-C1B-LAYERED-IMPACT-20261022-08 · ma trận lỗi giả C1-B (CÔ LẬP: catalog tiêm + Graph giả + thư mục tạm; 0 ghi production, 0 mạng).
# Mỗi ca hỏng phải ra MỘT PHẦN/NOT_ACTION_SAFE (+ biên nhận khi cần); ca dương thật lấy từ lượt cấp giấy thật (không ở đây).
# Dùng: c1b_fixtures.py <dir chứa graph_cert.py v3> <out.json>
import copy, json, os, re, sys, tempfile, time

S, OUT = sys.argv[1:3]
TMP = tempfile.mkdtemp(prefix="gs-c1b-fx-", dir="/dev/shm" if os.path.isdir("/dev/shm") else None)
CAT = TMP + "/cells.json"
os.environ.update(GS_CERT_CELLS=CAT, GS_CERT_DIR=TMP + "/cert", GS_CERT_BASELINE=TMP + "/baseline.json")
sys.path.insert(0, S)
import graph_cert as G  # noqa: E402

DU, MP = G.DU, G.MP
results = []


def case(cid, name, ok, detail=""):
    results.append({"id": cid, "case": name, "pass": bool(ok), "detail": str(detail)[:300]})
    print("%-4s %-66s %s %s" % (cid, name[:66], "PASS" if ok else "FAIL", str(detail)[:140]), flush=True)


# ---------------------------------------------------------------- thế giới catalog nhỏ (3 bảng, 2 bảng mẫu)
def world(n_perm=3):
    R = {"table": [["public.a"], ["public.b"], ["public.c"], ["public.directus_folders"]], "view": [["public.v_a", "v"], ["public.mv_b", "m"]],
         "trigger": [["public", "a", "trg_a1", "public", "fn_x", "", "O"], ["public", "a", "trg_a2", "public", "fn_x", "", "O"],
                     ["public", "b", "trg_b1", "public", "fn_y", "p integer", "D"]],
         "l1_fk": [["public.b", "b_a_fk", "public.a", "a_id", "id", "a", "c"], ["public.a", "a_c_fk", "public.c", "c_id", "id", "a", "a"],
                   ["public.c", "c_b_fk", "public.b", "b_id", "id", "a", "n"]],
         "view_dep_kind": [["public.v_a", "v", "public.a"], ["public.mv_b", "m", "public.b"], ["public.v_a", "v", "public.c"]],
         "directus_collection": [["a"], ["b"], ["c"]],
         "directus_relation": [["b", "a_id", "a"], ["a", "folder", "directus_folders"], ["c", "x", None]],
         "directus_permission": [[str(i), "a", ["read", "create", "update"][i % 3], "pol-%d" % (i % 2)] for i in range(1, n_perm + 1)] +
                                [["99000001", "b", "read", None]]}
    return R


PILOT = ["directus.public.a", "directus.public.b"]
CLASSES = G.L1_CLASSES
P = ["trust", "snapshot_utc", "source"]


def catalog():
    cells = [{"key": "l1:" + t, "gate": "G1", "parent": "pg:directus", "scope": "fx", "owner": G.OWNER,
              "source": {"adapter": "pg_l1", "db": "directus", "classes": CLASSES, "table": t}, "graph": {"l1_anchor": t.split(".", 1)[1]},
              "source_relations": list(G.L1_ALL_TYPES)} for t in PILOT]
    cells.append({"key": "l1:pilot11:scope", "gate": "G1", "parent": "pg:directus", "scope": "fx",
                  "source": {"adapter": "pg_l1_scope", "db": "directus", "classes": CLASSES, "tables": PILOT},
                  "graph": {"nodes": [{"label": l, "prefix": G.L1_PREFIX[l], "attrs": G.L1_ATTRS[l]} for l in G.L1_LABELS],
                            "edges": [{"type": "HAS_FK", "from": "PgTable", "to": "PgForeignKey", "prov": P},
                                      {"type": "REFERENCES", "from": "PgForeignKey", "to": "PgTable", "prov": P},
                                      {"type": "DEPENDS_ON", "from": "PgView", "to": "PgTable", "prov": P},
                                      {"type": "MAPS_TO_TABLE", "from": "DirectusCollection", "to": "PgTable", "prov": P},
                                      {"type": "RELATION_MANY", "from": "DirectusRelation", "to": "DirectusCollection", "prov": P},
                                      {"type": "RELATION_ONE", "from": "DirectusRelation", "to": "DirectusCollection", "prov": P},
                                      {"type": "PERMISSION_ON", "from": "DirectusPermission", "to": "DirectusCollection", "prov": P}]}})
    real = json.load(open(os.path.join(S, "cert-cells.json"), encoding="utf-8"))
    return {"format": "graph-cert-cells-v1", "catalog_version": "fixture-c1b", "ttl_hours": 26, "cells": cells,
            "graph_label_map": real["graph_label_map"], "graph_rel_map": real["graph_rel_map"], "certified_props": real["certified_props"],
            "endpoint_cover": real["endpoint_cover"], "l1_pilot": {"tables": PILOT}}


# ---------------------------------------------------------------- Graph giả: nút {gs_key: (label, id, props)} · cạnh [(s_key, type, d_key, prov)]
class FakeG:
    def __init__(self, nodes, edges, truncate_at=None, canary_lie=None):
        self.n, self.e, self.cap, self.lie = nodes, edges, truncate_at, canary_lie

    def password(self):
        return ""

    def invariants(self, pw):
        return {"gs_keys_sha256": "fx", "edges_sha256": "fx", "gs_keys_count": len(self.n), "edges_count": len(self.e)}

    def http_cypher(self, stmts, pw, timeout=0):
        (q, p), = stmts
        res = lambda cols, rows: {"results": [{"columns": cols, "data": [{"row": r} for r in rows]}], "errors": []}
        lab = lambda k: self.n[k][0]
        m = re.match(r"MATCH \(t:PgTable \{id: \$t\}\) RETURN properties\(t\) AS p", q)
        if m:
            return res(["p"], [[self.n[k][2]] for k in self.n if self.n[k][0] == "PgTable" and self.n[k][1] == p["t"]])
        m = re.match(r"MATCH \(c:DirectusCollection \{id: \$c\}\) RETURN properties\(c\) AS p", q)
        if m:
            return res(["p"], [[self.n[k][2]] for k in self.n if self.n[k][0] == "DirectusCollection" and self.n[k][1] == p["c"]])
        m = re.match(r"MATCH \(a:GS \{gs_key: \$key\}\)(<?)-\[r:`(\w+)`\]-(>?)\(b\) (RETURN count|WITH)", q)
        if m:
            out, t = bool(m.group(3)), m.group(2)
            hits = [(e, i) for i, e in enumerate(self.e) if e[1] == t and ((e[0] == p["key"]) if out else (e[2] == p["key"]))]
            if m.group(4) == "RETURN count":
                return res(["c"], [[len(hits)]])
            rows = sorted(((e[2] if out else e[0]) + "|%d" % i, e) for e, i in hits)
            rows = [r for r in rows if r[0] > p["after"]][:p["page"]]
            o = lambda e: e[2] if out else e[0]
            return res(["k", "id", "l", "p", "prov"], [[k, self.n[o(e)][1], [self.n[o(e)][0]], self.n[o(e)][2], e[3]] for k, e in rows])
        m = re.match(r"MATCH \(n:`(\w+)`\) RETURN count\(n\)", q)
        if m:
            return res(["c"], [[sum(1 for v in self.n.values() if v[0] == m.group(1))]])
        m = re.match(r"MATCH \(n:`(\w+)`\) WHERE n.gs_key > \$after", q)
        if m:
            rows = sorted((k, v[1], [v[2].get(a) for a in p["attrs"]]) for k, v in self.n.items() if v[0] == m.group(1))
            if self.cap is not None:
                rows = rows[:self.cap]
            rows = [r for r in rows if r[0] > p["after"]][:p["page"]]
            return res(["k", "id", "av", "gs"], [[k, i, a, True] for k, i, a in rows])
        m = re.match(r"MATCH \(\)-\[r:`(\w+)`\]->\(\) RETURN count", q)
        if m:
            return res(["c"], [[sum(1 for e in self.e if e[1] == m.group(1))]])
        m = re.match(r"MATCH \(:`(\w+)`\)-\[r:`(\w+)`\]->\(:`(\w+)`\) RETURN count", q)
        if m:
            return res(["c"], [[sum(1 for e in self.e if e[1] == m.group(2) and lab(e[0]) == m.group(1) and lab(e[2]) == m.group(3))]])
        m = re.match(r"MATCH \(x:`(\w+)`\)-\[r:`(\w+)`\]->\(y:`(\w+)`\)", q)
        if m:
            rows = sorted(("%s|%s|%d" % (e[0], e[2], i), self.n[e[0]][1], self.n[e[2]][1], e[3]) for i, e in enumerate(self.e)
                          if e[1] == m.group(2) and lab(e[0]) == m.group(1) and lab(e[2]) == m.group(3))
            rows = [r for r in rows if r[0] > p["after"]][:p["page"]]
            return res(["k", "s", "d", "prov"], [list(r) for r in rows])
        for name, (tpl, _) in G.L1_TEMPLATES.items():      # mẫu canary: tính từ cạnh giả
            mm = re.fullmatch(re.escape(tpl).replace(re.escape("%s"), "(.+?)"), q)
            if mm:
                T = mm.group(1)
                tk = "pg:table:" + T
                E = self.e
                if name == "trigger":
                    xs = {self.n[e[0]][1] for e in E if e[1] == "ON_TABLE" and e[2] == tk}
                elif name == "fk_in":
                    xs = {self.n[f[0]][1] + " <- " + self.n[h[0]][1] for f in E if f[1] == "REFERENCES" and f[2] == tk for h in E if h[1] == "HAS_FK" and h[2] == f[0]}
                elif name == "fk_out":
                    xs = {self.n[f[2]][1] + " -> " + self.n[r[2]][1] for f in E if f[1] == "HAS_FK" and f[0] == tk for r in E if r[1] == "REFERENCES" and r[0] == f[2]}
                elif name == "view":
                    xs = {self.n[e[0]][1] for e in E if e[1] == "DEPENDS_ON" and e[2] == tk}
                else:
                    cs = {e[0] for e in E if e[1] == "MAPS_TO_TABLE" and e[2] == tk}
                    xs = {self.n[e[0]][1] + ":" + self.n[e[0]][2]["action"] for e in E if e[1] == "PERMISSION_ON" and e[2] in cs}
                if self.lie == name:
                    xs = set(list(xs)[1:]) | {"<lie>"}
                return res(["x"], [[x] for x in sorted(xs)])
        raise RuntimeError("fake: không hiểu " + q[:90])


def graph_from(R, tables):
    """Graph hoàn hảo dựng từ l1_native (đúng hợp đồng) cho các bảng ⇒ FakeG."""
    nodes, edges = {}, {}
    for full in tables:
        o, e, why = G.l1_native(R, full.split(".", 1)[1])
        for x in o:
            lab, nid = x[0], x[1]
            props = {"gs_key": G.L1_PREFIX[lab] + nid, "id": nid}
            props.update({a: v for a, v in zip(G.L1_ATTRS[lab], x[2:]) if v is not None})
            nodes[props["gs_key"]] = (lab, nid, props)
        for s, t, d in e:
            ks = {"HAS_FK": ("PgTable", "PgForeignKey"), "REFERENCES": ("PgForeignKey", "PgTable"), "DEPENDS_ON": ("PgView", "PgTable"),
                  "ON_TABLE": ("PgTrigger", "PgTable"), "EXECUTES": ("PgTrigger", "PgFunction"), "MAPS_TO_TABLE": ("DirectusCollection", None),
                  "RELATION_MANY": ("DirectusRelation", "DirectusCollection"), "RELATION_ONE": ("DirectusRelation", "DirectusCollection"),
                  "PERMISSION_ON": ("DirectusPermission", "DirectusCollection")}[t]
            dl = ks[1] or next(v[0] for v in nodes.values() if v[1] == d and v[0] in ("PgTable", "PgView"))
            edges[(G.L1_PREFIX[ks[0]] + s, t, G.L1_PREFIX[dl] + d)] = True
    return nodes, [(s, t, d, True) for (s, t, d) in edges]


def inj(R):
    return {"pg": {"directus": {"reader": {"role": "fx", "pg_snapshot": "1:1:"}, "classes": {c: {"ok": True, "rows": R[c]} for c in CLASSES}},
                   "postgres": {"reader": {}, "classes": {"databases": {"ok": True, "rows": [["directus"], ["postgres"]]}}}}}


def run(R, g, only=None, write=False, now=None):
    json.dump(catalog(), open(CAT, "w"))
    return G.run(g, "", only=only or {"l1:directus.public.a", "l1:directus.public.b", "l1:pilot11:scope"}, injected=inj(R), write=write, now=now)


st = lambda d, k: d["cells"][k]["status"]
A, B, SC = "l1:directus.public.a", "l1:directus.public.b", "l1:pilot11:scope"
R0 = world()
N0, E0 = graph_from(R0, PILOT)

d = run(R0, FakeG(N0, E0))
case("P1", "Graph khớp catalog ⇒ 2 ô bảng + ô phạm vi ĐỦ, canary 0 lệch", st(d, A) == DU and st(d, B) == DU and st(d, SC) == DU and not d["canary"]["mismatch"],
     {k: (v["status"], v.get("reasons")) for k, v in d["cells"].items()})

# F1 cùng số, đổi đích khoá ngoại
E1 = [((s, t, "pg:table:public.b", pr) if (t == "REFERENCES" and s == "pg:fk:public.a.a_c_fk") else (s, t, x, pr)) for s, t, x, pr in E0]
d = run(R0, FakeG(N0, E1))
case("F1", "FK đổi đích, CÙNG số cạnh ⇒ băm lệch ⇒ MỘT PHẦN", st(d, A) == MP and any("EDGE_DIGEST" in r for r in d["cells"][A]["reasons"]),
     d["cells"][A]["reasons"])

# F2 thiếu view
N2 = {k: v for k, v in N0.items() if k != "pg:view:public.mv_b"}
E2 = [e for e in E0 if e[0] != "pg:view:public.mv_b"]
d = run(R0, FakeG(N2, E2))
case("F2", "view phụ thuộc vắng trong Graph ⇒ ô bảng b + ô phạm vi MỘT PHẦN", st(d, B) == MP and st(d, SC) == MP, d["cells"][B]["reasons"][:3])

# F3 nút lạc ngoài mẫu
N3 = dict(N0, **{"directus:permission:777": ("DirectusPermission", "777", {"gs_key": "directus:permission:777", "id": "777", "action": "read"})})
d = run(R0, FakeG(N3, E0))
case("F3", "nút DirectusPermission lạc (không thuộc 11 bảng) ⇒ ô phạm vi MỘT PHẦN, ô bảng giữ ĐỦ", st(d, SC) == MP and st(d, A) == DU, d["cells"][SC]["reasons"][:2])

# F4 cạnh thiếu provenance
E4 = [(s, t, x, (False if t == "PERMISSION_ON" else pr)) for s, t, x, pr in E0]
d = run(R0, FakeG(N0, E4))
case("F4", "cạnh PERMISSION_ON thiếu provenance ⇒ MỘT PHẦN", st(d, A) == MP and any("PROVENANCE" in r for r in d["cells"][A]["reasons"]), d["cells"][A]["reasons"][:2])

# F5 nguồn có khoá ngoại MỚI (Graph chưa theo kịp)
R5 = copy.deepcopy(R0)
R5["l1_fk"].append(["public.c", "c_a_fk2", "public.a", "a2", "id", "a", "a"])
d = run(R5, FakeG(N0, E0))
case("F5", "catalog có FK mới vào bảng a ⇒ ô a MỘT PHẦN (thiếu trong Graph)", st(d, A) == MP and d["cells"][A]["diff"]["edges_missing_in_graph"] == 2, d["cells"][A]["diff"])

# F6 bộ đọc catalog mất quyền
R6 = inj(R0)
R6["pg"]["directus"]["classes"]["directus_permission"] = {"ok": False, "error": "NO_ACCESS InsufficientPrivilege"}
json.dump(catalog(), open(CAT, "w"))
d = G.run(FakeG(N0, E0), "", only={A, B, SC}, injected=R6, write=False)
case("F6", "mất quyền đọc directus_permissions ⇒ MỘT PHẦN NO_ACCESS (không phải rỗng)", st(d, A) == MP and d["cells"][A]["reasons"][0].startswith("NO_ACCESS"),
     d["cells"][A]["reasons"][:1])

# F7 > 9000 ID: 9.500 quyền trên bảng a, đọc trọn theo trang
R7 = world(9500)
N7, E7 = graph_from(R7, PILOT)
d = run(R7, FakeG(N7, E7))
pg_ = (d["cells"][SC].get("graph") or {}).get("pages") or {}
case("F7", "9.500 DirectusPermission ⇒ đọc trọn qua trang (2000/trang) ⇒ ĐỦ", st(d, SC) == DU and st(d, A) == DU and pg_.get("DirectusPermission", 0) >= 5, [st(d, SC), st(d, A), d["cells"][A]["reasons"][:2], d["cells"][SC]["reasons"][:2]] or
     {"pages": pg_, "objs": d["cells"][SC]["source"]["objects_count"]})
d = run(R7, FakeG(N7, E7, truncate_at=9000))
case("F8", "cùng Graph nhưng bộ đọc cắt 9.000 (LIMIT cũ) ⇒ MỘT PHẦN GRAPH_INCOMPLETE", st(d, SC) == MP and any("INCOMPLETE" in r for r in d["cells"][SC]["reasons"]),
     d["cells"][SC]["reasons"][:2])

# F9 canary: Graph trả lời mẫu truy vấn khác catalog dù băm ô khớp ⇒ thu hồi giấy
d = run(R0, FakeG(N0, E0, canary_lie="permission"))
case("F9", "canary: câu trả lời mẫu lệch catalog ⇒ thu hồi giấy ô a (CANARY_MISMATCH)", st(d, A) == MP and any("CANARY_MISMATCH" in r for r in d["cells"][A]["reasons"]),
     d["canary"]["mismatch"])

# F10 canary xoay vòng + bộ đếm lượt (state chỉ ghi khi write)
os.makedirs(TMP + "/cert", exist_ok=True)
d1 = run(R0, FakeG(N0, E0), write=True)
d2 = run(R0, FakeG(N0, E0), write=True)
cs = json.load(open(TMP + "/cert/canary.json"))
case("F10", "canary ghi bộ đếm lượt thành công (xoay vòng bảng)", cs["ticks_ok"] == 2 and d1["canary"]["tick_index"] == 0 and d2["canary"]["tick_index"] == 1, cs)

# ---------------------------------------------------------------- nhãn N4 theo lớp
cat = catalog()
now = time.time()
good = run(R0, FakeG(N0, E0))
good["self_sha256"] = G.self_sha(good)
lab = lambda q, doc=good, rows=None, params=None: G.label_for("read-cypher", {"query": q, "params": params or {}}, rows, now=now, doc=doc, cat=cat)
l = lab(G.L1_TEMPLATES["fk_in"][0] % "public.a", rows=1)
case("N1", "câu L1 neo bảng mẫu ⇒ ĐỦ tại T · answer_scope L1 · impact NOT_ACTION_SAFE", l["completeness_label"] == DU and l["query_class"] == "L1_SCOPED_LOOKUP"
     and l["answer_scope"] == "L1_DECLARED_CATALOG_ONLY" and l["impact_question_actionability"] == "NOT_ACTION_SAFE" and l["layers"]["L3"]["label"] == "MỞ",
     {k: l[k] for k in ("completeness_label", "query_class", "relevant_cell_ids")})
l = lab("MATCH (t:PgTable {id: 'public.a'})<-[:DEPENDS_ON]-(v:PgView {id: 'public.none'}) RETURN v.id", rows=0)
case("N2", "neo bảng mẫu + lọc thêm id khác ⇒ không thu hẹp ⇒ MỘT PHẦN", l["completeness_label"] == MP, l["reason"][:80])
l = lab("MATCH (t:PgTable {id: 'public.a'})<-[:DEPENDS_ON]-(v:PgView) RETURN v.id", rows=0)
case("N3", "câu L1 rỗng trong ô ĐỦ ⇒ ĐỦ, «rỗng được chứng nhận»", l["completeness_label"] == DU and "rỗng" in l["reason"], l["reason"])
l = lab("MATCH (t:PgTable {id: 'public.a'})<-[:REFERENCES]-(f:PgForeignKey)<-[:HAS_FK]-(s:PgTable)<-[:ON_TABLE]-(g:PgTrigger) RETURN g.id")
case("N4", "đi quá hình L1 (trigger của bảng bên kia) ⇒ MỘT PHẦN", l["completeness_label"] == MP and l["query_class"] != "L1_SCOPED_LOOKUP", l["query_class"])
l = lab("MATCH (t:PgTable {id: 'public.a'})-[*1..3]-(x) RETURN count(x)")
case("N5", "câu tác động toàn phần ⇒ MỘT PHẦN · L1 ĐỦ · L2 MỘT PHẦN · L3 MỞ", l["completeness_label"] == MP and l["layers"]["L1"]["label"] == DU
     and l["layers"]["L2"]["label"] == MP and l["layers"]["L3"]["label"] == "MỞ" and l["query_actionability"] == "NOT_ACTION_SAFE", {k: v["label"] for k, v in l["layers"].items()})
l = lab("MATCH (g:PgTrigger)-[:ON_TABLE]->(t:PgTable {id: 'public.c'}) RETURN g.id")
case("N6", "bảng ngoài mẫu ⇒ không L1_SCOPED (ô toàn cục)", l["query_class"] != "L1_SCOPED_LOOKUP" and l["layers"]["L1"]["label"] == "KHÔNG_ÁP_DỤNG", l["query_class"])
l = lab("CALL db.labels()")
case("N7", "Cypher thô CALL ⇒ MỘT PHẦN", l["completeness_label"] == MP, l["query_class"])
l = lab("MATCH (t:PgTable {id: $x})<-[:DEPENDS_ON]-(v:PgView) RETURN v.id", params={"x": "public.a"})
case("N8", "neo qua tham số $x ⇒ L1_SCOPED ĐỦ", l["completeness_label"] == DU and l["query_class"] == "L1_SCOPED_LOOKUP", l["query_class"])
l = lab(G.L1_TEMPLATES["fk_in"][0] % "public.a", doc=dict(good, generated_at=G.now_iso(now - 30 * 3600)))
case("N9", "giấy sửa tay / quá hạn ⇒ MỘT PHẦN", l["completeness_label"] == MP, l["reason"])
l = lab("MATCH (f:PgForeignKey)-[:REFERENCES]->(t:PgTable) RETURN f.id")
case("N10", "FK toàn cục (không neo) ⇒ ô toàn cục pg:directus:fk ⇒ MỘT PHẦN", l["completeness_label"] == MP and "pg:directus:fk" in l["missing_or_unknown_cell_ids"],
     l["missing_or_unknown_cell_ids"][:3])
l = lab("MATCH (t:PgTable {id: 'public.a'})-[:DEPENDS_ON]-(v:PgView) RETURN v.id")
case("N11", "cạnh vô hướng ⇒ không thu hẹp ⇒ MỘT PHẦN", l["completeness_label"] == MP, l["query_class"])
l = lab("MATCH (t:PgTable {id: 'public.a'})<-[:DEPENDS_ON]-(v:PgView) RETURN v", rows=1)
case("N12", "trả nguyên nút (thuộc tính chưa băm) ⇒ MỘT PHẦN", l["completeness_label"] == MP and l["query_class"] == "UNCERTIFIED_PROPERTY", l["query_class"])

# ---------------------------------------------------------------- L2/L3: hai đường cùng ghi ⇒ POTENTIAL_COLLISION, không phải chạy thật
l2 = {"format": "graph-l2-candidates-v1", "generated_at": G.now_iso(now), "self_sha256": "fx", "tables": {"directus.public.a": {
      "candidates": [{"kind": "TRIGGER_HANDLER_WRITES", "via": "public.a.trg_a1 → public.fn_x()", "target": "log", "op": "WRITE"},
                     {"kind": "TRIGGER_HANDLER_WRITES", "via": "public.a.trg_a2 → public.fn_x()", "target": "log", "op": "WRITE"}],
      "potential_collisions": [{"target": "log", "writers": ["public.a.trg_a1 → public.fn_x()", "public.a.trg_a2 → public.fn_x()"], "status": "POTENTIAL_COLLISION"}]}}}
json.dump(l2, open(G.L2_FILE, "w"))
l = lab("MATCH (t:PgTable {id: 'public.a'})-[*1..2]-(x) RETURN count(x)")
pc = l["layers"]["L2"].get("potential_collisions") or []
case("L1", "hai trigger cùng ghi một bảng ⇒ L2 POTENTIAL_COLLISION, L3 MỞ (không RUNTIME_CONFIRMED), toàn câu NOT_ACTION_SAFE",
     pc and pc[0]["status"] == "POTENTIAL_COLLISION" and "RUNTIME_CONFIRMED" not in json.dumps(l, ensure_ascii=False).replace("không phải RUNTIME_CONFIRMED", "")
     and l["layers"]["L3"]["label"] == "MỞ" and l["impact_question_actionability"] == "NOT_ACTION_SAFE", pc)
os.remove(G.L2_FILE)
l = lab(G.L1_TEMPLATES["fk_in"][0] % "public.a")
case("L2", "không có tệp L2 ⇒ L2 MỘT PHẦN, snapshot None (không bịa ứng viên)", l["layers"]["L2"]["label"] == MP and l["layers"]["L2"]["snapshot"] is None, l["layers"]["L2"])

# ---------------------------------------------------------------- đèn: ô bảng mẫu thuộc sàn tụt ⇒ DOWN + chủ + sự cố mới khi đã DOWN
bl = {"certified_floor": [A, B, SC], "accepted_partial": {}}
bad = run(R0, FakeG(N0, E1))
bad["self_sha256"] = G.self_sha(bad)
s1, m1, inc1 = G.alarm(bad, baseline=bl, now=now)
case("A1", "ô L1 thuộc sàn tụt ⇒ đèn DOWN COVERAGE_REGRESSION, biên nhận có chủ", s1 == "down" and any(i["kind"] == "COVERAGE_REGRESSION" and i["cell"] == A
     and i["owner"] == G.OWNER for i in inc1), m1)
new1, _ = G.record_incidents(inc1, now=now)
bad2 = run(R0, FakeG(N2, E2))
bad2["self_sha256"] = G.self_sha(bad2)
s2, m2, inc2 = G.alarm(bad2, baseline=bl, now=now + 60)
new2, gone2 = G.record_incidents(inc2, now=now + 60)
case("A2", "đèn đã DOWN, lỗi MỚI (thiếu view) ⇒ biên nhận sự cố mới riêng", s2 == "down" and any(i["cell"] == B for i in new2), [i["cell"] for i in new2])
s3, m3, inc3 = G.alarm(None, op_failure="lượt timer bỏ qua: khoá graph-refresh đang bận", baseline=bl, now=now)
case("A3", "lượt lịch bỏ lỡ ⇒ DOWN OPERATIONAL (khác FIRST_NATURAL_TICK_NOT_OBSERVED: chỉ là fixture)", s3 == "down" and inc3[0]["kind"] == "OPERATIONAL", m3)

ok = all(r["pass"] for r in results)
json.dump({"run": "GS-C1B-LAYERED-IMPACT-20261022-08", "at": G.now_iso(), "pass": sum(r["pass"] for r in results), "total": len(results), "results": results,
           "note": "fixture cô lập — KHÔNG thay lượt tự nhiên đầu tiên của timer (FIRST_NATURAL_TICK quan sát riêng ở journal)"},
          open(OUT, "w"), ensure_ascii=False, indent=1)
import shutil  # noqa: E402
shutil.rmtree(TMP, ignore_errors=True)
print("FIXTURES %d/%d %s" % (sum(r["pass"] for r in results), len(results), "PASS" if ok else "FAIL"))
sys.exit(0 if ok else 1)
