#!/usr/bin/env python3
"""c1b_l1 — BỘ NẠP L1 CÓ GIỚI HẠN cho 11 bảng mẫu C1-B vào Graph production v1 · GS-C1B-LAYERED-IMPACT-20261022-08

Chỉ CỘNG nút/cạnh kỹ thuật catalog khai báo (khoá ngoại · view phụ thuộc · Directus collection/relation/permission) của đúng 11 bảng trong
cert-cells.json `l1_pilot` (gs_layer = pgl1). Không sửa/xoá nút có sẵn; trigger/hàm (lane pgdot) chỉ được KIỂM là đã có. Trần: ≤1000 nút,
≤3000 cạnh, 0 xoá. Nguồn = c1b_l1_native.py (catalog lọc trong SQL, container incomex-claude-mcp, vai chỉ-đọc). Dùng lại nguyên các hàm
graph-refresh (create_statements · delete_keys · temp_from_recovery · apply_plan/undo · apply_v0 · new_recovery_point D23 Drive).
Lệnh (root trên VPS, thư mục làm việc <W> = bằng chứng RUN):
  c1b_l1.py preview  <W> <cells.json>   native + Graph ⇒ <W>/plan.json (+ trần, nghịch đảo, PRE)
  c1b_l1.py rehearse <W> <cells.json>   Neo4j TẠM từ điểm khôi phục: F ⇒ chấm giấy v3 (11 ô + phạm vi) ⇒ I ⇒ =PRE ⇒ F ⇒ =NEW
  c1b_l1.py apply    <W>                production (giữ khoá graph-refresh): tập khô RETURN 1/0 ⇒ F một giao dịch ⇒ =NEW ⇒ apply-v0 invariants
                                        + pins ⇒ điểm khôi phục mới + Drive D23 ⇒ apply-v0 recovery-manifest; hỏng ⇒ I + đặt lại 3 tệp
  c1b_l1.py inverse  <W>                production: I (DETACH DELETE đúng gs_key đã tạo) + đặt lại invariants/pins/recovery-manifest PRE
Exit 0 PASS · 1 FAIL (đã lùi) · 2 tham số · 3 cổng/trần không đạt (0 ghi) · 30 lùi chưa sạch
"""
import hashlib, importlib.machinery, importlib.util, json, os, subprocess, sys, time

RUN = "GS-C1B-LAYERED-IMPACT-20261022-08"
HERE = os.path.dirname(os.path.abspath(__file__))
GRF_PATH = "/opt/incomex/graph-server/prod-v1/bin/graph-refresh"
CAP_NODES, CAP_EDGES = 1000, 3000
LAYER = "pgl1"
PREFIX = {"PgTable": "pg:table:", "PgView": "pg:view:", "PgForeignKey": "pg:fk:", "PgTrigger": "pg:trigger:", "PgFunction": "pg:function:",
          "DirectusCollection": "directus:collection:", "DirectusRelation": "directus:relation:", "DirectusPermission": "directus:permission:"}
now = lambda: time.strftime("%FT%TZ", time.gmtime())


def load_grf():
    ldr = importlib.machinery.SourceFileLoader("graph_refresh", GRF_PATH)
    m = importlib.util.module_from_spec(importlib.util.spec_from_loader("graph_refresh", ldr))
    ldr.exec_module(m)
    return m


def native(tables):
    p = subprocess.run(["docker", "exec", "-i", "-e", "C1B_TABLES=" + json.dumps(tables), "incomex-claude-mcp", "python", "-I", "-B", "-"],
                       input=open(os.path.join(HERE, "c1b_l1_native.py"), "rb").read(), capture_output=True, timeout=300)
    if p.returncode:
        raise SystemExit("NATIVE FAIL rc=%s %s" % (p.returncode, p.stderr.decode()[-300:]))
    return json.loads(p.stdout)


def build(nat, tables):
    """Tập mong muốn (nút, cạnh) theo hợp đồng mô hình l1_pilot.model — viết độc lập với graph_cert.l1_native."""
    snap = nat["reader"]["snapshot_utc"]
    rows, ends, ex, rc = nat["rows"], nat["endpoints"], nat["exists"], nat["relation_collections"]
    nodes, edges, need_existing = {}, {}, {}
    cat_ = lambda d: {"source": "pg_catalog", "trust": "EXACT_AT_SNAPSHOT", "snapshot_utc": snap, "run": RUN}
    dmeta = lambda d: {"source": "directus_meta", "trust": "DECLARED", "snapshot_utc": snap, "run": RUN}

    def node(label, nid, props, prov):
        k = PREFIX[label] + nid
        p = dict(prov(None), id=nid, gs_key=k, gs_layer=LAYER, **{a: b for a, b in props.items() if b is not None})
        nodes[k] = {"l": ["GS", label], "p": p}
        return k

    def rel_(label, x):
        kind = ex.get(x) or ends.get(x)
        sch, nm = x.split(".", 1)
        if kind in ("r", "p", "f"):
            return node("PgTable", x, {"schema": sch, "name": nm}, cat_)
        if kind in ("v", "m"):
            return node("PgView", x, {"kind": kind, "schema": sch, "name": nm}, cat_)
        raise SystemExit("ENDPOINT_UNKNOWN %s" % x)

    def edge(s, t, d, prov):
        edges[(s, t, d)] = {"t": t, "s": s, "d": d, "p": dict(prov(None), source_file="c1b_l1_native")}

    for full in tables:
        rel_("PgTable", full.split(".", 1)[1])
    for src, con, dst, cols, rcols, upd, dele in rows["fk"]:
        fid = src + "." + con
        sch, tb = src.split(".", 1)
        fk = node("PgForeignKey", fid, {"columns": cols, "ref_columns": rcols, "on_update": upd, "on_delete": dele, "schema": sch, "table": tb,
                                       "name": con}, cat_)
        edge(rel_("PgTable", src), "HAS_FK", fk, cat_)
        edge(fk, "REFERENCES", rel_("PgTable", dst), cat_)
    for v, kind, t in rows["view_dep"]:
        sch, nm = v.split(".", 1)
        edge(node("PgView", v, {"kind": kind, "schema": sch, "name": nm}, cat_), "DEPENDS_ON", PREFIX["PgTable"] + t, cat_)
    for t, tg, fn, en in rows["trigger"]:                  # lane pgdot sở hữu — chỉ kiểm có sẵn, không tạo
        g = PREFIX["PgTrigger"] + "%s.%s" % (t, tg)
        need_existing[g] = "PgTrigger"
        need_existing[PREFIX["PgFunction"] + fn] = "PgFunction"
        need_existing[(g, "ON_TABLE", PREFIX["PgTable"] + t)] = "edge"
        need_existing[(g, "EXECUTES", PREFIX["PgFunction"] + fn)] = "edge"
    decl = {r[0] for r in rows["directus_collection"]}
    pub = [x.split(".", 2)[2] for x in tables if x.split(".")[1] == "public"]
    colls = {c for c in pub if c in decl or any(c in (r[1], r[3]) for r in rows["directus_relation"]) or any(r[1] == c for r in rows["directus_permission"])}
    for rid, m, f, o in rows["directus_relation"]:
        k = node("DirectusRelation", "%s.%s" % (m, f), {"one_collection": o}, dmeta)
        edge(k, "RELATION_MANY", PREFIX["DirectusCollection"] + m, dmeta)
        colls.add(m)
        if o:
            edge(k, "RELATION_ONE", PREFIX["DirectusCollection"] + o, dmeta)
            colls.add(o)
    for pid, c, act, pol in rows["directus_permission"]:
        edge(node("DirectusPermission", pid, {"action": act, "policy": pol}, dmeta), "PERMISSION_ON", PREFIX["DirectusCollection"] + c, dmeta)
    for c in sorted(colls):
        reg = "directus_collections" if (c in decl or (rc.get(c) or {}).get("in_directus_collections")) else "referenced_only"
        k = node("DirectusCollection", c, {"registry": reg}, dmeta)
        kind = ex.get("public." + c) or (rc.get(c) or {}).get("public_relkind")
        if kind:
            ends.setdefault("public." + c, kind)
            edge(k, "MAPS_TO_TABLE", rel_("PgTable", "public." + c), dmeta)
    return nodes, edges, need_existing


def graph_existing(g, pw, keys):
    out = {}
    for i in range(0, len(keys), 500):
        d = g.http_cypher([("MATCH (n:GS) WHERE n.gs_key IN $k RETURN n.gs_key AS k, [x IN labels(n) WHERE x <> 'GS'] AS l, properties(n) AS p",
                            {"k": keys[i:i + 500]})], pw, timeout=300)
        for r in g.rows(d):
            out[r["k"]] = r
    return out


def graph_edges_exist(g, pw, triples):
    rows = [{"s": s, "t": t, "d": d} for s, t, d in triples]
    d = g.http_cypher([("UNWIND $rows AS r OPTIONAL MATCH (a:GS {gs_key: r.s})-[x]->(b:GS {gs_key: r.d}) WHERE type(x) = r.t "
                        "RETURN r.s AS s, r.t AS t, r.d AS d, count(x) AS n", {"rows": rows})], pw, timeout=300)
    return {(r["s"], r["t"], r["d"]): r["n"] for r in g.rows(d)}


def cmd_preview(W, cells):
    GRF = load_grf()
    cat = json.load(open(cells, encoding="utf-8"))
    tables = cat["l1_pilot"]["tables"]
    g = GRF.r7_g1lib.load(GRF.G1)
    pw = g.password()
    pre_hash = GRF.full_hash(g, pw)
    nat = native(tables)
    json.dump(nat, open(W + "/native-loader.json", "w"), ensure_ascii=False, indent=1, sort_keys=True)
    nodes, edges, need = build(nat, tables)
    have = graph_existing(g, pw, sorted(set(nodes) | {k for k in need if isinstance(k, str)}))
    problems, create_n, reuse = [], [], []
    for k, n in sorted(nodes.items()):
        if k in have:
            if have[k]["l"] != n["l"][1:]:
                problems.append("LABEL_CONFLICT %s %s≠%s" % (k, have[k]["l"], n["l"][1:]))
            reuse.append(k)
        else:
            create_n.append(n)
    for k, lab in need.items():
        if isinstance(k, str) and (k not in have or have[k]["l"] != [lab]):
            problems.append("PGDOT_LANE_MISSING %s" % k)
    trip = sorted(edges) + sorted(k for k in need if isinstance(k, tuple))
    ex = graph_edges_exist(g, pw, trip)
    for t in sorted(k for k in need if isinstance(k, tuple)):
        if ex.get(t) != 1:
            problems.append("PGDOT_EDGE_MISSING %s" % "|".join(t))
    create_e = [e for k, e in sorted(edges.items()) if ex.get(k, 0) == 0]
    dup = [k for k in edges if ex.get(k, 0) > 1]
    if dup:
        problems.append("EDGE_ALREADY_MULTI %d" % len(dup))
    if len(create_n) > CAP_NODES or len(create_e) > CAP_EDGES:
        problems.append("CAP_EXCEEDED nodes=%d edges=%d" % (len(create_n), len(create_e)))
    by_l = {}
    for n in create_n:
        by_l[n["l"][1]] = by_l.get(n["l"][1], 0) + 1
    by_t = {}
    for e in create_e:
        by_t[e["t"]] = by_t.get(e["t"], 0) + 1
    created_keys = sorted(n["p"]["gs_key"] for n in create_n)
    plan = {"run": RUN, "at": now(), "pre_hash": pre_hash, "native_snapshot": nat["reader"], "tables": tables,
            "create_nodes": create_n, "create_edges": create_e, "reuse_nodes": reuse, "created_keys": created_keys,
            "counts": {"nodes_add": len(create_n), "edges_add": len(create_e), "nodes_delete": 0, "edges_delete": 0, "by_label": by_l, "by_type": by_t,
                       "nodes_reused": len(reuse), "pgdot_checked": len(need)},
            "caps": {"nodes": CAP_NODES, "edges": CAP_EDGES}, "problems": problems,
            "inverse": "DETACH DELETE đúng %d gs_key đã tạo (mọi cạnh mới đều chạm ít nhất một nút mới)" % len(created_keys)}
    # mọi cạnh mới phải chạm nút mới ⇒ nghịch đảo = xoá đúng các nút đã tạo
    ck = set(created_keys)
    orphan = [e for e in create_e if e["s"] not in ck and e["d"] not in ck]
    if orphan:
        problems.append("EDGE_BETWEEN_EXISTING_NODES %d (nghịch đảo không đủ)" % len(orphan))
    plan["sha256"] = hashlib.sha256(json.dumps({k: plan[k] for k in ("create_nodes", "create_edges", "created_keys", "pre_hash")}, sort_keys=True,
                                               ensure_ascii=False).encode()).hexdigest()
    json.dump(plan, open(W + "/plan.json", "w"), ensure_ascii=False, indent=1, sort_keys=True)
    print("PREVIEW nodes+%d edges+%d reuse=%d pgdot_checked=%d problems=%s by_label=%s by_type=%s plan=%s" % (
        len(create_n), len(create_e), len(reuse), len(need), problems, by_l, by_t, plan["sha256"][:16]))
    return 3 if problems else 0


def stmts(GRF, plan):
    return GRF.create_statements(plan["create_nodes"], plan["create_edges"]), GRF.delete_keys(plan["created_keys"])


def load_cert_v3(cells, cert_dir):
    os.environ.update(GS_CERT_CELLS=cells, GS_CERT_DIR=cert_dir)
    ldr = importlib.machinery.SourceFileLoader("graph_cert_v3", os.path.join(HERE, "v3", "graph_cert.py"))
    m = importlib.util.module_from_spec(importlib.util.spec_from_loader("graph_cert_v3", ldr))
    ldr.exec_module(m)
    return m


def cmd_rehearse(W, cells):
    GRF = load_grf()
    plan = json.load(open(W + "/plan.json"))
    if plan["problems"]:
        print("REHEARSE STOP problems"); return 3
    F, I = stmts(GRF, plan)
    rep = {"at": now()}
    t, gt, pre = GRF.temp_from_recovery("c1b-l1", expect=plan["pre_hash"])
    try:
        GRF.tx_ok(t.tx, F, "F tạm")
        rep["new_hash"] = GRF.full_hash(gt, "")
        rep["new_inv"] = gt.invariants("")
        cd = W + "/rehearse-cert"
        os.makedirs(cd, mode=0o700, exist_ok=True)
        GC3 = load_cert_v3(cells, cd)
        cat = json.load(open(cells, encoding="utf-8"))
        only = {c["key"] for c in cat["cells"] if c["key"].startswith("l1:")} | {"pg:directus:trigger"}
        doc = GC3.run(gt, "", only=only, write=False)
        rep["cert_on_temp"] = {k: {"status": v["status"], "reasons": v.get("reasons"), "src": [v["source"].get("objects_count"), v["source"].get("edges_count")],
                                   "graph": [(v.get("graph") or {}).get("objects_count"), (v.get("graph") or {}).get("edges_count")]}
                               for k, v in doc["cells"].items() if k in only}
        rep["canary_on_temp"] = doc.get("canary")
        GRF.tx_ok(t.tx, I, "I tạm")
        rep["I_eq_pre"] = GRF.full_hash(gt, "") == pre
        GRF.tx_ok(t.tx, F, "F tạm lần 2")
        rep["F_eq_new"] = GRF.full_hash(gt, "") == rep["new_hash"]
    finally:
        rep["temp_cleanup"] = t.cleanup()
    rep["cert_all_du"] = all(v["status"] == "ĐỦ tại T" for v in rep["cert_on_temp"].values())
    json.dump(rep, open(W + "/rehearse.json", "w"), ensure_ascii=False, indent=1, sort_keys=True, default=str)
    ok = rep["I_eq_pre"] and rep["F_eq_new"]
    print("REHEARSE %s I_eq_pre=%s F_eq_new=%s cert_all_du=%s cells=%s canary_mismatch=%s" % (
        "PASS" if ok else "FAIL", rep["I_eq_pre"], rep["F_eq_new"], rep["cert_all_du"],
        {k: v["status"][:4] for k, v in rep["cert_on_temp"].items()}, (rep.get("canary_on_temp") or {}).get("mismatch")))
    return 0 if ok else 1


def cmd_apply(W):
    GRF = load_grf()
    plan = json.load(open(W + "/plan.json"))
    reh = json.load(open(W + "/rehearse.json"))
    if plan["problems"] or not (reh["I_eq_pre"] and reh["F_eq_new"]):
        print("APPLY STOP plan/rehearse"); return 3
    lf = GRF.take_lock("manual")
    if not lf:
        print("APPLY STOP khoá graph-refresh bận"); return 3
    g = GRF.r7_g1lib.load(GRF.G1)
    pw = g.password()
    ow = GRF.other_writers()
    gs = GRF.guard_state()
    if ow or not gs["ok"] or not GRF.config_guard_clean() or os.path.exists(GRF.STOPF):
        print("APPLY STOP writers=%s guard=%s" % (ow, gs)); return 3
    F, I = stmts(GRF, plan)
    full = {"F": F, "I": I, "pre_hash": plan["pre_hash"], "new_hash": reh["new_hash"], "new_inv": reh["new_inv"], "stage_new": None, "stage_old": None}
    pre_bytes = {p: open(p, "rb").read() for p in (GRF.INV, GRF.PINS, GRF.RECMAN)}
    for p, b in pre_bytes.items():
        open(W + "/pre-" + os.path.basename(p), "wb").write(b)
    rep, applied, mid = {"at": now()}, False, RUN + ".G"
    GRF.term_to_fail()
    try:
        GRF.apply_plan({"g": g, "pw": pw}, full, rep)
        applied = True
        live_inv = g.invariants(pw)
        ok, out = GRF.apply_v0("graph-v1-invariants", GRF.INV, {"run": RUN, **live_inv, "computed_at": now()}, mid)
        if not ok:
            raise GRF.Fail("apply-v0 invariants %s" % out)
        pins = json.loads(pre_bytes[GRF.PINS])
        pins["files"][GRF.INV] = GRF.sha_file(GRF.INV)
        pins["pinned_at"], pins["run"] = now(), RUN
        ok, out = GRF.apply_v0("graph-v1-pins", GRF.PINS, pins, mid)
        if not ok:
            raise GRF.Fail("apply-v0 pins %s" % out)
        rp = GRF.new_recovery_point(g, pw, "c1b-l1-" + time.strftime("%Y%m%dT%H%M%SZ", time.gmtime()), True, rep.setdefault("recovery", {}))
        rm = json.loads(pre_bytes[GRF.RECMAN])
        rm["previous"], rm["current"], rm["updated_at"] = rm.get("current"), rp, now()
        ok, out = GRF.apply_v0("graph-recovery-manifest", GRF.RECMAN, rm, mid)
        if not ok:
            raise GRF.Fail("apply-v0 recovery-manifest %s" % out)
        rep["result"] = "APPLIED"
        rep["recovery_point"] = rp
        rc = 0
    except Exception as e:  # noqa: BLE001
        rep["result"], rep["why"], rc = "FAIL", "%s %s" % (type(e).__name__, str(e)[:300]), 1
        if applied and GRF.full_hash(g, pw) != plan["pre_hash"]:
            rb = {}
            GRF.undo({"g": g, "pw": pw}, full, rb)
            for t, live in (("graph-recovery-manifest", GRF.RECMAN), ("graph-v1-pins", GRF.PINS), ("graph-v1-invariants", GRF.INV)):
                if open(live, "rb").read() != pre_bytes[live]:
                    rb[t] = GRF.apply_v0(t, live, None, RUN + ".RB", raw_bytes=pre_bytes[live])[1]
            rep["rollback"] = rb
            rc = 1 if rb.get("undo_eq_pre") else 30
    json.dump(rep, open(W + "/apply.json", "w"), ensure_ascii=False, indent=1, sort_keys=True, default=str)
    print("APPLY %s %s" % (rep["result"], json.dumps({k: rep.get(k) for k in ("dry_ok", "forward", "why")}, ensure_ascii=False)))
    return rc


def cmd_inverse(W):
    GRF = load_grf()
    plan = json.load(open(W + "/plan.json"))
    reh = json.load(open(W + "/rehearse.json"))
    lf = GRF.take_lock("manual")
    if not lf:
        print("INVERSE STOP khoá bận"); return 3
    g = GRF.r7_g1lib.load(GRF.G1)
    pw = g.password()
    F, I = stmts(GRF, plan)
    rb = {}
    GRF.undo({"g": g, "pw": pw}, {"I": I, "pre_hash": plan["pre_hash"], "stage_old": None}, rb)
    for t, live in (("graph-recovery-manifest", GRF.RECMAN), ("graph-v1-pins", GRF.PINS), ("graph-v1-invariants", GRF.INV)):
        pre = open(W + "/pre-" + os.path.basename(live), "rb").read()
        if open(live, "rb").read() != pre:
            rb[t] = GRF.apply_v0(t, live, None, RUN + ".INV", raw_bytes=pre)[1]
    json.dump(rb, open(W + "/inverse.json", "w"), ensure_ascii=False, indent=1, sort_keys=True, default=str)
    print("INVERSE undo_eq_pre=%s %s" % (rb.get("undo_eq_pre"), {k: v for k, v in rb.items() if k != "undo_eq_pre"}))
    return 0 if rb.get("undo_eq_pre") else 30


if __name__ == "__main__":
    a = sys.argv[1:]
    if len(a) >= 2 and a[0] == "preview" and len(a) == 3:
        sys.exit(cmd_preview(a[1], a[2]))
    if len(a) == 3 and a[0] == "rehearse":
        sys.exit(cmd_rehearse(a[1], a[2]))
    if len(a) == 2 and a[0] == "apply":
        sys.exit(cmd_apply(a[1]))
    if len(a) == 2 and a[0] == "inverse":
        sys.exit(cmd_inverse(a[1]))
    print(__doc__)
    sys.exit(2)
