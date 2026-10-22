#!/usr/bin/env python3
# GS-R7 · chấm tập node/cạnh sau nạp (chỉ đọc Neo4j) = tập kỳ vọng đóng băng TRƯỚC nạp: 0 thừa / 0 thiếu + provenance + gs_key.
# Dùng: r7_score_sets.py pgdot <graph-v1> <b5/expected.json> <out.json> | r7_score_sets.py b88 <graph-v1> <b6/input> <out.json>
# Exit 0 PASS · 1 FAIL
# GS-C1B-LAYERED-IMPACT-20261022-08: mode pgdot chỉ chấm nút thuộc lane (gs_layer pg/dot) — nút PgTable lớp pgl1 (L1 catalog 11 bảng mẫu C1-B,
#   bảng chưa có trigger) KHÔNG thuộc tập kỳ vọng lane pgdot; không lọc thì chúng bị tính «extra» ⇒ lane pgdot không làm mới được nữa.
import csv, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import r7_g1lib  # noqa: E402

mode, g1, src, out = sys.argv[1:5]
g = r7_g1lib.load(g1)
pw = g.password()
q = lambda s, p=None: g.rows(g.http_cypher([(s, p or {})], pw, timeout=600))
m = {"mode": mode, "nodes": {}, "edges": {}, "problems": []}
LANE_FILTER = " WHERE n.gs_layer IN ['pg', 'dot']" if mode == "pgdot" else ""


def cmp_nodes(label, exp_ids, prefix, extra_ret=""):
    rs = q("MATCH (n:%s)%s RETURN n.id AS id, n.gs_key AS g, 'GS' IN labels(n) AS gs%s" % (label, LANE_FILTER, extra_ret))
    ids = [r["id"] for r in rs]
    e = set(exp_ids)
    d = {"expected": len(e), "graph": len(ids), "missing": sorted(e - set(ids))[:20], "extra": sorted(set(ids) - e)[:20],
         "dup": len(ids) - len(set(ids)), "gs_key_bad": sum(1 for r in rs if r["g"] != prefix + r["id"] or not r["gs"])}
    m["nodes"][label] = d
    if d["missing"] or d["extra"] or d["dup"] or d["gs_key_bad"]:
        m["problems"].append(label)
    return rs


def cmp_edges(rtype, a, b, exp_pairs, prov_keys):
    rs = q("MATCH (x:%s)-[r:%s]->(y:%s) RETURN x.id AS s, y.id AS d, %s AS prov" % (a, rtype, b, " AND ".join("r.%s IS NOT NULL" % k for k in prov_keys)))
    got = [(r["s"], r["d"]) for r in rs]
    e = {tuple(x) for x in exp_pairs}
    other = q("MATCH ()-[r:%s]->() RETURN count(r) AS n" % rtype)[0]["n"]
    d = {"expected": len(e), "graph": len(got), "missing": sorted(map(list, e - set(got)))[:20], "extra": sorted(map(list, set(got) - e))[:20],
         "dup": len(got) - len(set(got)), "provenance_missing": sum(1 for r in rs if not r["prov"]), "same_type_other_endpoints": other - len(got)}
    m["edges"][rtype] = d
    if d["missing"] or d["extra"] or d["dup"] or d["provenance_missing"] or d["same_type_other_endpoints"]:
        m["problems"].append(rtype)


if mode == "pgdot":
    ex = json.load(open(src))
    for lab, pre in ex["gs_key_prefix"].items():
        rs = cmp_nodes(lab, ex["nodes"][lab], pre, ", n.enabled_code AS en" if lab == "PgTrigger" else "")
        if lab == "PgTrigger":
            bad = sum(1 for r in rs if ex["enabled_code"].get(r["id"]) != r["en"])
            m["nodes"][lab]["enabled_code_mismatch"] = bad
            if bad:
                m["problems"].append("enabled_code")
    P = ("trust", "snapshot_utc", "source_file", "source_row")
    cmp_edges("ON_TABLE", "PgTrigger", "PgTable", ex["edges"]["ON_TABLE"], P)
    cmp_edges("EXECUTES", "PgTrigger", "PgFunction", ex["edges"]["EXECUTES"], P)
    cmp_edges("REGISTERS", "DotRegistryEntry", "DotCommand", ex["edges"]["REGISTERS"], P)
    cmp_edges("PAIRED_WITH", "DotRegistryEntry", "DotRegistryEntry", ex["edges"]["PAIRED_WITH"], P)
elif mode == "b88":
    rd = lambda f: list(csv.DictReader(open(os.path.join(src, f), encoding="utf-8")))
    for lab, f, pre, col in (("B88Order", "b88_order.csv", "b88:order:", "order_code"), ("B88Trainee", "b88_tts.csv", "b88:trainee:", None),
                             ("B88Union", "b88_union.csv", "b88:union:", "union_code"), ("B88Company", "b88_company.csv", "b88:company:", "company_code")):
        rows = rd(f)
        rs = cmp_nodes(lab, [r["record_id"] for r in rows], pre, (", n.%s AS code" % col) if col else "")
        if col:
            want = {r["record_id"]: r[col] for r in rows}
            bad = sum(1 for r in rs if want.get(r["id"]) != r["code"])
            m["nodes"][lab]["code_mismatch"] = bad
            if bad:
                m["problems"].append(lab + ".code")
        props = q("MATCH (n:%s) UNWIND keys(n) AS k RETURN DISTINCT k ORDER BY k" % lab)
        m["nodes"][lab]["property_keys"] = [r["k"] for r in props]
    P = ("catalog", "trust", "snapshot_utc", "source_file", "source_fields")
    for rel, a, b in (("CANDIDATE_FOR_ORDER", "B88Trainee", "B88Order"), ("SELECTED_FOR_ORDER", "B88Trainee", "B88Order"),
                      ("ORDER_MANAGED_BY_UNION", "B88Order", "B88Union"), ("ORDER_FOR_COMPANY", "B88Order", "B88Company")):
        ex = [(r["src_record_id"], r["dst_record_id"]) for r in rd("b88_rel_%s.csv" % rel.lower())]
        cmp_edges(rel, a, b, ex, P)
    allowed = {"id", "gs_key", "gs_layer", "source", "trust", "snapshot_utc", "order_code", "union_code", "company_code"}
    leak = {lab: sorted(set(v["property_keys"]) - allowed) for lab, v in m["nodes"].items()}
    m["property_whitelist_violations"] = {k: v for k, v in leak.items() if v}
    if m["property_whitelist_violations"]:
        m["problems"].append("property_whitelist")
m["verdict"] = "PASS" if not m["problems"] else "FAIL"
json.dump(m, open(out, "w"), ensure_ascii=False, indent=1, sort_keys=True)
print("SCORE %s %s nodes=%s edges=%s problems=%s" % (mode, m["verdict"], {k: (v["expected"], v["graph"]) for k, v in m["nodes"].items()},
                                                   {k: (v["expected"], v["graph"]) for k, v in m["edges"].items()}, m["problems"]))
sys.exit(0 if m["verdict"] == "PASS" else 1)
