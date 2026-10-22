#!/usr/bin/env python3
"""Vá graph_cert.py C1-A → v3 C1-B (chỉ thay đúng các đoạn, mỗi đoạn phải khớp đúng 1 lần)."""
import sys

src, dst = sys.argv[1], sys.argv[2]
t = open(src, encoding="utf-8").read()


def rep(old, new, n=1):
    global t
    c = t.count(old)
    if c != n:
        raise SystemExit("PATCH FAIL (%d lần, cần %d): %r" % (c, n, old[:80]))
    t = t.replace(old, new)


# ---------------------------------------------------------------- docstring
rep('''phản ánh hết thực tế (SQL động, quyết định nói miệng, lệnh gõ tay một lần ⇒ ô MỞ/UNKNOWN).
''', '''phản ánh hết thực tế (SQL động, quyết định nói miệng, lệnh gõ tay một lần ⇒ ô MỞ/UNKNOWN).

C1-B (GS-C1B-LAYERED-IMPACT-20261022-08) — câu hỏi tác động Q1 theo BA LỚP, mỗi lớp một nhãn:
  L1 CATALOG_DECLARED_EXACT_AT_SNAPSHOT  ô `l1:<db>.<schema>.<bảng>` cho 11 bảng mẫu (cert-cells.json `l1_pilot`): khoá ngoại vào/ra
     (pg_constraint), view/matview phụ thuộc trực tiếp (pg_rewrite+pg_depend), trigger→hàm (pg_trigger.tgfoid), Directus khai báo
     (directus_collections/relations/permissions). Nguồn: catalog đọc TRỌN database rồi lọc bằng Python (bộ nạp c1b_l1 lọc trong SQL —
     hai cách viết độc lập); Graph: đọc láng giềng từ nút neo theo từng loại cạnh, phân trang + tổng đếm riêng. Ô `l1:pilot11:scope`
     bắt nút/cạnh lạc ngoài 11 bảng. ĐỦ ở L1 KHÔNG chứng minh hàm đọc/ghi bảng nào, hành vi quyền Directus lúc chạy, DROP an toàn.
  L2 SOURCE_TEXT_DERIVED_PARTIAL  ứng viên đọc văn bản (thân hàm PL/pgSQL + EXECUTE động, flow/operation Directus, DOT, mã) trong
     state/refresh/cert/l2-candidates.json — luôn MỘT PHẦN, kèm nguồn/dòng/băm; hai đường cùng GHI một đích = POTENTIAL_COLLISION.
  L3 RUNTIME_OPEN  lịch sử chạy/đồng thời/khoá: MỞ (không dựng bộ theo dõi mới).
  Nhãn câu hỏi = lớp kém nhất cần; truy vấn chỉ đi theo hình L1 từ MỘT bảng mẫu (L1_SCOPED_LOOKUP) được ĐỦ trong phạm vi «chỉ
  metadata catalog khai báo», còn câu hỏi tác động toàn phần luôn impact_question_actionability = NOT_ACTION_SAFE (L2/L3 mở).
  Kiểm mẫu (canary) mỗi lượt: information_unit cố định + 3 bảng xoay vòng (đủ 10 sau 4 lượt) — hỏi Graph bằng mẫu truy vấn chính
  thức so với catalog; lệch ⇒ thu hồi giấy ô đó (MỘT PHẦN) ⇒ đèn #24 (ô thuộc sàn) + biên nhận sự cố có người chịu trách nhiệm.
''')

rep('''  graph_cert.py label --query CYPHER [--rows N] [--tool read-cypher|get-schema]
''', '''  graph_cert.py label --query CYPHER [--rows N] [--tool read-cypher|get-schema] [--params JSON]
''')

rep('''INCIDENTS = CERT_DIR + "/incidents.jsonl"
ALARM_STATE = CERT_DIR + "/alarm.json"
''', '''INCIDENTS = CERT_DIR + "/incidents.jsonl"
ALARM_STATE = CERT_DIR + "/alarm.json"
L2_FILE = CERT_DIR + "/l2-candidates.json"            # C1-B: ứng viên L2 (đọc văn bản, MỘT PHẦN) — dữ liệu, không phải giấy
CANARY_STATE = CERT_DIR + "/canary.json"              # C1-B: bộ đếm lượt kiểm mẫu thành công (xoay vòng 3 bảng/lượt)
OWNER = "Graph Host · work/graph-server"              # người/bộ phận chịu trách nhiệm mọi biên nhận sự cố của giấy
''')

# ---------------------------------------------------------------- PG: lớp mới (đọc trọn database)
rep(''' "directus_operation": "SELECT o.id::text, o.flow::text FROM directus_operations o",
''', ''' "directus_operation": "SELECT o.id::text, o.flow::text FROM directus_operations o",
 "directus_permission": "SELECT p.id::text, p.collection, p.action, p.policy::text FROM directus_permissions p",
 "l1_fk": "SELECT n1.nspname||'.'||c1.relname, co.conname, n2.nspname||'.'||c2.relname, "
          "(SELECT string_agg(a.attname, ',' ORDER BY k.o) FROM unnest(co.conkey) WITH ORDINALITY k(n, o) JOIN pg_attribute a ON a.attrelid=co.conrelid AND a.attnum=k.n), "
          "(SELECT string_agg(a.attname, ',' ORDER BY k.o) FROM unnest(co.confkey) WITH ORDINALITY k(n, o) JOIN pg_attribute a ON a.attrelid=co.confrelid AND a.attnum=k.n), "
          "co.confupdtype::text, co.confdeltype::text FROM pg_constraint co "
          "JOIN pg_class c1 ON c1.oid=co.conrelid JOIN pg_namespace n1 ON n1.oid=c1.relnamespace "
          "JOIN pg_class c2 ON c2.oid=co.confrelid JOIN pg_namespace n2 ON n2.oid=c2.relnamespace WHERE co.contype='f'",
 "view_dep_kind": "SELECT DISTINCT vn.nspname||'.'||v.relname, v.relkind::text, tn.nspname||'.'||t.relname FROM pg_depend d "
                  "JOIN pg_rewrite r ON r.oid=d.objid JOIN pg_class v ON v.oid=r.ev_class JOIN pg_class t ON t.oid=d.refobjid "
                  "JOIN pg_namespace vn ON vn.oid=v.relnamespace JOIN pg_namespace tn ON tn.oid=t.relnamespace "
                  "WHERE d.classid='pg_rewrite'::regclass AND d.refclassid='pg_class'::regclass AND v.oid<>t.oid",
''')

rep('''            if s.get("adapter") == "pg":
                spec.setdefault(s["db"], set()).update(s["classes"])''', '''            if s.get("adapter") in ("pg", "pg_l1", "pg_l1_scope"):
                spec.setdefault(s["db"], set()).update(s["classes"])''')

rep('''            res["edges"] = [[r[0], "IN_FLOW", r[1]] for r in rowsets.get("directus_operation", [])]
''', '''            res["edges"] = [[r[0], "IN_FLOW", r[1]] for r in rowsets.get("directus_operation", [])]
        elif k == "directus_permission":
            res["objects"] = [["DirectusPermission", r[0], r[2], r[3]] for r in rowsets[k]]
''')

# ---------------------------------------------------------------- nguồn L1 (adapter pg_l1 / pg_l1_scope)
rep('''    if a == "code_identity":
        res["why"] = "READER_NOT_ID_COMPARABLE_C1A"
        return res
''', '''    if a in ("pg_l1", "pg_l1_scope"):
        db, R = s["db"], {}
        for c in s["classes"]:
            ok, rows, rdr, why = src_pg_class(S, db, c)
            res["snapshot"] = rdr
            if not ok:
                res["why"], res["access"] = why, ("NO_ACCESS" if why.startswith("NO_ACCESS") else "FAIL")
                return res
            R[c] = rows
        tables = [s["table"]] if a == "pg_l1" else list(s["tables"])
        objs, edges = {}, {}
        for T in tables:
            o, e, why = l1_native(R, T.split(".", 1)[1])
            if why:
                res["why"] = "READER_FAIL %s %s" % (why, T)
                return res
            for x in o:
                if a == "pg_l1" or x[0] in L1_LABELS:
                    objs[jkey(x)] = x
            for x in e:
                if a == "pg_l1" or x[1] in L1_TYPES:
                    edges[jkey(x)] = x
        res.update(ok=True, objects=list(objs.values()), edges=list(edges.values()), consistency="PG_REPEATABLE_READ_READ_ONLY",
                   reader="pg:%s:context_pack_readonly (catalog + directus_* đọc trọn, lọc Python)" % db)
        if a == "pg_l1":
            res["_rowsets"] = R
        return res
    if a == "code_identity":
        res["why"] = "READER_NOT_ID_COMPARABLE_C1A"
        return res
''')

rep('''# =========================================================================== M-b (ô KB ↔ Qdrant, không chuyển vector)
''', '''# =========================================================================== C1-B · L1 catalog khai báo (hợp đồng mô hình = cert-cells l1_pilot.model)
L1_LABELS = ("PgView", "PgForeignKey", "DirectusCollection", "DirectusRelation", "DirectusPermission")
L1_TYPES = ("HAS_FK", "REFERENCES", "DEPENDS_ON", "MAPS_TO_TABLE", "RELATION_MANY", "RELATION_ONE", "PERMISSION_ON")
L1_ALL_TYPES = L1_TYPES + ("ON_TABLE", "EXECUTES")
L1_PREFIX = {"PgTable": "pg:table:", "PgView": "pg:view:", "PgForeignKey": "pg:fk:", "PgTrigger": "pg:trigger:", "PgFunction": "pg:function:",
             "DirectusCollection": "directus:collection:", "DirectusRelation": "directus:relation:", "DirectusPermission": "directus:permission:"}
L1_ATTRS = {"PgTable": [], "PgView": ["kind"], "PgForeignKey": ["columns", "ref_columns", "on_update", "on_delete"], "PgTrigger": ["enabled_code"],
            "PgFunction": [], "DirectusCollection": ["registry"], "DirectusRelation": ["one_collection"], "DirectusPermission": ["action", "policy"]}
L1_PROV = ("trust", "snapshot_utc", "source")
L1_CLASSES = ["table", "view", "trigger", "l1_fk", "view_dep_kind", "directus_collection", "directus_relation", "directus_permission"]


def l1_native(R, T):
    """Ô L1 của bảng T ('schema.bảng') từ các lớp catalog ĐỌC TRỌN database ⇒ (objects, edges, why). Điểm cuối bảng/view theo relkind;
    collection Directus = bảng cùng tên schema public (lõi Directus); collection không có dòng directus_collections nhưng được
    relation/permission nhắc tới ⇒ registry 'referenced_only' (collection hệ thống)."""
    kind = {r[0]: "PgTable" for r in R["table"]}
    vk = {r[0]: r[1] for r in R["view"]}
    kind.update({k: "PgView" for k in vk})
    if kind.get(T) != "PgTable":
        return None, None, "ANCHOR_NOT_NATIVE_TABLE"
    objs, edges = {}, {}

    def obj(o):
        objs[jkey(o)] = o

    def edge(e):
        edges[jkey(e)] = e

    def end(x):
        obj(["PgTable", x] if kind.get(x) == "PgTable" else ["PgView", x, vk[x]] if kind.get(x) == "PgView" else ["UNKNOWN_RELATION", x])

    obj(["PgTable", T])
    for src, con, dst, cols, rcols, upd, dele in R["l1_fk"]:
        if T in (src, dst):
            fid = src + "." + con
            obj(["PgForeignKey", fid, cols, rcols, upd, dele])
            end(src)
            end(dst)
            edge([src, "HAS_FK", fid])
            edge([fid, "REFERENCES", dst])
    for v, vkind, t in R["view_dep_kind"]:
        if t == T:
            obj(["PgView", v, vkind])
            edge([v, "DEPENDS_ON", T])
    for r in R["trigger"]:
        if "%s.%s" % (r[0], r[1]) == T:
            gid, fid = "%s.%s.%s" % (r[0], r[1], r[2]), "%s.%s(%s)" % (r[3], r[4], r[5] or "")
            obj(["PgTrigger", gid, r[6]])
            obj(["PgFunction", fid])
            edge([gid, "ON_TABLE", T])
            edge([gid, "EXECUTES", fid])
    sch, name = T.split(".", 1)
    if sch == "public":
        decl = {r[0] for r in R["directus_collection"]}
        rels = [r for r in R["directus_relation"] if name in (r[0], r[2])]
        perms = [r for r in R["directus_permission"] if r[1] == name]
        colls = {name} if (name in decl or rels or perms) else set()
        for m, f, o in rels:
            rid = "%s.%s" % (m, f)
            obj(["DirectusRelation", rid, o])
            edge([rid, "RELATION_MANY", m])
            colls.add(m)
            if o:
                edge([rid, "RELATION_ONE", o])
                colls.add(o)
        for pid, c, act, pol in perms:
            obj(["DirectusPermission", pid, act, pol])
            edge([pid, "PERMISSION_ON", c])
        for c in sorted(colls):
            obj(["DirectusCollection", c, "directus_collections" if c in decl else "referenced_only"])
            if ("public." + c) in kind:
                end("public." + c)
                edge([c, "MAPS_TO_TABLE", "public." + c])
    return list(objs.values()), list(edges.values()), None


def l1_nbr(g, pw, key, rtype, out, page=GRAPH_PAGE):
    """Láng giềng của nút gs_key=key qua MỘT loại cạnh (out: key→b · in: b→key), đọc trọn theo trang + tổng đếm riêng."""
    pat = ("(a:GS {gs_key: $key})-[r:`%s`]->(b)" if out else "(a:GS {gs_key: $key})<-[r:`%s`]-(b)") % rtype.replace("`", "")
    total = g_rows(g, pw, "MATCH %s RETURN count(r) AS c" % pat, {"key": key})[0]["c"]
    cond = " AND ".join("r[%s] IS NOT NULL" % json.dumps(k) for k in L1_PROV)
    rows, after = [], ""
    while True:
        rs = g_rows(g, pw, "MATCH %s WITH r, b, coalesce(b.gs_key, '') + '|' + elementId(r) AS k WHERE k > $after RETURN k, b.id AS id, "
                           "[x IN labels(b) WHERE x <> 'GS'] AS l, properties(b) AS p, %s AS prov ORDER BY k LIMIT $page" % (pat, cond),
                    {"key": key, "after": after, "page": page})
        rows += rs
        if len(rs) < page:
            break
        after = rs[-1]["k"]
    return rows, total


def graph_l1_read(g, pw, T):
    """Ô L1 phía Graph: từ nút neo PgTable T đi đúng các hình khai báo (không dùng đầu ra bộ nạp) ⇒ (objects, edges, meta)."""
    objs, edges, meta = {}, {}, {"complete": True, "problems": [], "calls": 0}

    def add(lab, nid, p):
        o = [lab, nid] + [None if p.get(x) is None else str(p.get(x)) for x in L1_ATTRS.get(lab, [])]
        objs[jkey(o)] = o
        if p.get("gs_key") != L1_PREFIX.get(lab, "?") + str(nid):
            meta["problems"].append("GS_KEY_BAD %s" % nid)

    def edge(e):
        if jkey(e) in edges:
            meta["problems"].append("GRAPH_DUPLICATE_EDGE %s" % e[1])
        edges[jkey(e)] = e

    def nb(key, rtype, out):
        rs, total = l1_nbr(g, pw, key, rtype, out)
        meta["calls"] += 1
        if total != len(rs):
            meta["complete"] = False
            meta["problems"].append("GRAPH_INCOMPLETE %s %d/%d" % (rtype, len(rs), total))
        if any(not r["prov"] for r in rs):
            meta["problems"].append("PROVENANCE_MISSING %s %d" % (rtype, sum(1 for r in rs if not r["prov"])))
        return [(",".join(sorted(r["l"])), r["id"], r["p"]) for r in rs]

    a = g_rows(g, pw, "MATCH (t:PgTable {id: $t}) RETURN properties(t) AS p", {"t": T})
    if len(a) != 1:
        return [], [], {"complete": True, "problems": ["ANCHOR_MISSING_IN_GRAPH %d" % len(a)], "calls": 1}
    tk = L1_PREFIX["PgTable"] + T
    add("PgTable", T, a[0]["p"])
    fks = {}
    for lab, i, p in nb(tk, "HAS_FK", True) + nb(tk, "REFERENCES", False):
        fks[(lab, i)] = p
    for (lab, fid), p in sorted(fks.items()):
        add(lab, fid, p)
        for l2, s_, ps in nb(p.get("gs_key"), "HAS_FK", False):
            add(l2, s_, ps)
            edge([s_, "HAS_FK", fid])
        for l2, d, pd in nb(p.get("gs_key"), "REFERENCES", True):
            add(l2, d, pd)
            edge([fid, "REFERENCES", d])
    for lab, v, p in nb(tk, "DEPENDS_ON", False):
        add(lab, v, p)
        edge([v, "DEPENDS_ON", T])
    for lab, gid, p in nb(tk, "ON_TABLE", False):
        add(lab, gid, p)
        edge([gid, "ON_TABLE", T])
        for l2, f, pf in nb(p.get("gs_key"), "EXECUTES", True):
            add(l2, f, pf)
            edge([gid, "EXECUTES", f])
    sch, name = T.split(".", 1)
    if sch == "public":
        colls = {}
        c = g_rows(g, pw, "MATCH (c:DirectusCollection {id: $c}) RETURN properties(c) AS p", {"c": name})
        meta["calls"] += 1
        if c:
            colls[("DirectusCollection", name)] = c[0]["p"]
        for lab, cid, p in nb(tk, "MAPS_TO_TABLE", False):
            colls.setdefault((lab, cid), p)
        ck = L1_PREFIX["DirectusCollection"] + name
        for rt in ("RELATION_MANY", "RELATION_ONE"):
            for lab, rid, p in nb(ck, rt, False):
                add(lab, rid, p)
                for rt2 in ("RELATION_MANY", "RELATION_ONE"):
                    for l2, x, px in nb(p.get("gs_key"), rt2, True):
                        colls.setdefault((l2, x), px)
                        edge([rid, rt2, x])
        for lab, pid, p in nb(ck, "PERMISSION_ON", False):
            add(lab, pid, p)
            edge([pid, "PERMISSION_ON", name])
        for (lab, cid), p in sorted(colls.items()):
            add(lab, cid, p)
            for l2, x, px in nb(p.get("gs_key"), "MAPS_TO_TABLE", True):
                add(l2, x, px)
                edge([cid, "MAPS_TO_TABLE", x])
    return list(objs.values()), list(edges.values()), meta


L1_TEMPLATES = {   # mẫu truy vấn chính thức của câu hỏi L1 (canary hỏi Graph đúng như agent hỏi, qua phân loại nhãn)
    "trigger": ("MATCH (g:PgTrigger)-[:ON_TABLE]->(t:PgTable {id: '%s'}) RETURN g.id AS x", lambda T, e: {x[0] for x in e if x[1] == "ON_TABLE" and x[2] == T}),
    "fk_in": ("MATCH (t:PgTable {id: '%s'})<-[:REFERENCES]-(f:PgForeignKey)<-[:HAS_FK]-(s:PgTable) RETURN f.id + ' <- ' + s.id AS x",
              lambda T, e: {x[0] + " <- " + y[0] for x in e if x[1] == "REFERENCES" and x[2] == T for y in e if y[1] == "HAS_FK" and y[2] == x[0]}),
    "fk_out": ("MATCH (t:PgTable {id: '%s'})-[:HAS_FK]->(f:PgForeignKey)-[:REFERENCES]->(d:PgTable) RETURN f.id + ' -> ' + d.id AS x",
               lambda T, e: {y[0] + " -> " + y[2] for x in e if x[1] == "HAS_FK" and x[0] == T for y in e if y[1] == "REFERENCES" and y[0] == x[2]}),
    "view": ("MATCH (t:PgTable {id: '%s'})<-[:DEPENDS_ON]-(v:PgView) RETURN v.id AS x", lambda T, e: {x[0] for x in e if x[1] == "DEPENDS_ON" and x[2] == T}),
    "permission": ("MATCH (t:PgTable {id: '%s'})<-[:MAPS_TO_TABLE]-(c:DirectusCollection)<-[:PERMISSION_ON]-(p:DirectusPermission) RETURN p.id + ':' + p.action AS x",
                   None),
}


def l1_canary(g, pw, cat, res, rowsets, now, state=None, write=True):
    """Kiểm mẫu câu trả lời (M3-3): information_unit cố định + 3 bảng xoay vòng. Hỏi Graph bằng mẫu chính thức, so tập trả lời với catalog
    (đọc trọn database ở lượt này), kiểm nhãn N4 phân loại đúng ô. Lệch ⇒ thu hồi giấy ô đó. ⇒ biên bản canary."""
    pilot = (cat.get("l1_pilot") or {}).get("tables") or []
    if not pilot or rowsets is None:
        return {"ran": False, "why": "không có l1_pilot hoặc bộ đọc catalog hỏng"}
    st = state if state is not None else (jload(CANARY_STATE, {}) or {})
    n = int(st.get("ticks_ok") or 0)
    rest = pilot[1:]
    pick = [pilot[0]] + [rest[(3 * n + j) % len(rest)] for j in range(min(3, len(rest)))]
    out = {"ran": True, "tick_index": n, "tables": pick, "checks": {}, "mismatch": []}
    for full in pick:
        T = full.split(".", 1)[1]
        ck = "l1:" + full
        objs, edges, why = l1_native(rowsets, T)
        perms = {x[1] + ":" + x[2] for x in (objs or []) if x[0] == "DirectusPermission"}
        rec = {}
        for name, (tpl, expf) in L1_TEMPLATES.items():
            q = tpl % T
            try:
                got = {r["x"] for r in g_rows(g, pw, q)}
            except Exception as e:  # noqa: BLE001
                got = {"<lỗi %s>" % type(e).__name__}
            exp = perms if name == "permission" else expf(T, edges or [])
            qc, need, _ = classify_query(q, cat)
            scope = l1_scope_cell(q, {}, cat) if qc == "CELL_SCOPED_LOOKUP" else None
            ok = got == exp and scope == ck
            rec[name] = {"native": len(exp), "graph": len(got), "equal": got == exp, "label_cell": scope, "pass": ok}
            if not ok:
                out["mismatch"].append("%s %s" % (full, name))
        out["checks"][full] = rec
        c = res.get(ck)
        if c is not None and any(not v["pass"] for v in rec.values()):
            c["status"] = MP
            c.pop("issued_at", None)
            c.pop("expires_at", None)
            c["reasons"] = (c.get("reasons") or []) + ["CANARY_MISMATCH " + ",".join(k for k, v in rec.items() if not v["pass"])]
    if write and not out["mismatch"]:
        st = {"ticks_ok": n + 1, "last_ok_at": now_iso(now), "last_tables": pick}
        os.makedirs(CERT_DIR, mode=0o750, exist_ok=True)
        tmp = CANARY_STATE + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(st, f, ensure_ascii=False, indent=1)
        os.replace(tmp, CANARY_STATE)
    return out


# =========================================================================== M-b (ô KB ↔ Qdrant, không chuyển vector)
''')

# ---------------------------------------------------------------- run(): đọc Graph cho ô L1 + canary
rep('''        src = source_for(c, S)
        gr = {}
        if c.get("graph") and src.get("ok"):
            try:
                go, ge, gm = graph_read(g, pw, c["graph"])
                gr = {"objects": go, "edges": ge, "meta": gm}
            except Exception as e:  # noqa: BLE001
                gr = {"error": "%s %s" % (type(e).__name__, str(e)[:120])}
        r = evaluate(c, src, gr, now, cat.get("ttl_hours", MAX_TTL_H))''', '''        src = source_for(c, S)
        if src.get("_rowsets") is not None:
            rowsets = src.pop("_rowsets")
        gr = {}
        if c.get("graph") and src.get("ok"):
            try:
                if c["graph"].get("l1_anchor"):
                    go, ge, gm = graph_l1_read(g, pw, c["graph"]["l1_anchor"])
                else:
                    go, ge, gm = graph_read(g, pw, c["graph"])
                gr = {"objects": go, "edges": ge, "meta": gm}
            except Exception as e:  # noqa: BLE001
                gr = {"error": "%s %s" % (type(e).__name__, str(e)[:120])}
        r = evaluate(c, src, gr, now, cat.get("ttl_hours", MAX_TTL_H))''')

rep('''    res = {}
    for c in cells:
        ct = time.time()''', '''    res, rowsets = {}, None
    for c in cells:
        ct = time.time()''')

rep('''    dr = directory(cat["cells"], S) if not only else None
    prev = jload(CURRENT)''', '''    dr = directory(cat["cells"], S) if not only else None
    canary = None
    if any(k.startswith("l1:") for k in res) and cat.get("l1_pilot"):
        try:
            canary = l1_canary(g, pw, cat, res, rowsets, now, write=write)
        except Exception as e:  # noqa: BLE001
            canary = {"ran": False, "why": "%s %s" % (type(e).__name__, str(e)[:120])}
            for k in res:
                if k.startswith("l1:") and k != "l1:pilot11:scope" and res[k]["status"] == DU:
                    res[k].update(status=MP, reasons=["CANARY_ERROR"])
                    res[k].pop("issued_at", None)
                    res[k].pop("expires_at", None)
    prev = jload(CURRENT)''')

rep('''           "generated_at": now_iso(now), "graph_snapshot": gsnap, "cells": res, "directory": dr, "reader_errors": readers,''',
    '''           "generated_at": now_iso(now), "graph_snapshot": gsnap, "cells": res, "directory": dr, "reader_errors": readers, "canary": canary,''')

# ---------------------------------------------------------------- N4: phạm vi L1 từ MỘT bảng mẫu + nhãn theo lớp
rep('''def label_for(tool, arguments=None, result_rows=None, now=None, doc=None, cat=None):''', '''def _l1_shapes():
    """Hình hợp lệ tính từ bảng neo ra ngoài: (loại cạnh, hướng so với nút đang đứng). Mọi tiền tố đều hợp lệ."""
    base = [(("ON_TABLE", "in"), ("EXECUTES", "out")), (("HAS_FK", "out"), ("REFERENCES", "out")), (("REFERENCES", "in"), ("HAS_FK", "in")),
            (("DEPENDS_ON", "in"),), (("MAPS_TO_TABLE", "in"), ("PERMISSION_ON", "in"))]
    for x in ("RELATION_MANY", "RELATION_ONE"):
        for y in ("RELATION_MANY", "RELATION_ONE"):
            base.append((("MAPS_TO_TABLE", "in"), (x, "in"), (y, "out"), ("MAPS_TO_TABLE", "out")))
    return {p[:i] for p in base for i in range(1, len(p) + 1)}


L1_SHAPES = _l1_shapes()
RE_CLAUSE = re.compile(r"\\b(?:OPTIONAL\\s+)?MATCH\\b(.*?)(?=\\b(?:OPTIONAL\\s+MATCH|MATCH|WHERE|WITH|RETURN|ORDER|LIMIT|SKIP|UNWIND|UNION|CALL)\\b|$)", re.I | re.S)
RE_L1_NODE = re.compile(r"^\\s*([A-Za-z_]\\w*)?\\s*((?::\\s*`?[A-Za-z_]\\w*`?\\s*)*)\\s*(\\{[^{}]*\\})?\\s*$")
RE_L1_STEP = re.compile(r"\\s*(<)?-\\s*\\[([^\\]]*)\\]\\s*-(>)?")
RE_L1_HEAD = re.compile(r"\\s*\\(([^()]*)\\)")


def _split_top(s):
    out, depth, cur = [], 0, ""
    for ch in s:
        depth += ch in "([{"
        depth -= ch in ")]}"
        if ch == "," and depth == 0:
            out.append(cur)
            cur = ""
        else:
            cur += ch
    return [x for x in out + [cur] if x.strip()]


def _l1_parse(q, params, cat):
    """⇒ (bảng neo 'db.schema.bảng' thuộc mẫu | None, hình hợp lệ?). Bảo thủ: không hiểu ⇒ (None, False)."""
    pilot = set((cat.get("l1_pilot") or {}).get("tables") or [])
    if not pilot or not q:
        return None, False
    strs = []

    def keep(m):
        strs.append(m.group(0)[1:-1])
        return "'§%d'" % (len(strs) - 1)
    body = RE_STR.sub(keep, q)
    val = lambda tok: strs[int(tok[2:-1])] if tok.startswith("'§") else (params or {}).get(tok[1:]) if tok.startswith("$") else None
    tvars = set(re.findall(r"\\(\\s*([A-Za-z_]\\w*)\\s*:\\s*`?PgTable\\b", body))
    found = {val(x) for x in re.findall(r"PgTable`?\\s*\\{\\s*id\\s*:\\s*('§\\d+'|\\$\\w+)\\s*\\}", body)}
    found |= {val(tok) for v, tok in re.findall(r"\\b([A-Za-z_]\\w*)\\.id\\s*=\\s*('§\\d+'|\\$\\w+)", body) if v in tvars}
    if len(found) != 1 or ("directus." + str(next(iter(found)))) not in pilot:
        return None, False
    A = "directus." + str(next(iter(found)))
    try:
        a, ok = _l1_walk(body, val, A.split(".", 1)[1])
    except Exception:  # noqa: BLE001
        return A, False
    return A, ok


def _l1_walk(body, val, a):
    """Duyệt mọi mẫu MATCH từ bảng neo a ⇒ (a, mọi bước đều thuộc L1_SHAPES?)."""
    if re.search(r"\\b(UNION|CALL|LOAD|FOREACH|CREATE|MERGE|SET|DELETE|REMOVE|DETACH)\\b", body, re.I) or re.search(r"\\)\\s*<?-{1,2}>?\\s*\\(", body):
        return a, False
    paths = []
    for cm in RE_CLAUSE.finditer(body):
        for part in _split_top(cm.group(1)):
            part, i, seq = re.sub(r"^\\s*[A-Za-z_]\\w*\\s*=\\s*", "", part), 0, []
            while True:
                m = RE_L1_HEAD.match(part, i)
                if not m:
                    return a, False
                nm = RE_L1_NODE.match(m.group(1))
                if not nm:
                    return a, False
                labs = [x.strip(" :`") for x in (nm.group(2) or "").split(":") if x.strip(" :`")]
                props = dict(re.findall(r"([A-Za-z_]\\w*)\\s*:\\s*('§\\d+'|\\$\\w+)", nm.group(3) or ""))
                seq.append({"var": nm.group(1), "labels": labs, "id": val(props["id"]) if "id" in props else None})
                i = m.end()
                if not part[i:].strip():
                    break
                m = RE_L1_STEP.match(part, i)
                if not m or bool(m.group(1)) == bool(m.group(3)):
                    return a, False
                rm = re.match(r"^\\s*([A-Za-z_]\\w*)?\\s*:\\s*`?([A-Za-z_]\\w*)`?\\s*$", m.group(2))
                if not rm:
                    return a, False
                seq.append({"type": rm.group(2), "right": bool(m.group(3))})
                i = m.end()
            paths.append(seq)
    if not paths:
        return a, False
    if {n["id"] for p in paths for n in p[::2] if n["id"] is not None} - {a}:
        return a, False
    avars = {n["var"] for p in paths for n in p[::2] if n["var"] and n["id"] == a}
    avars |= {v for v, tok in re.findall(r"\\b([A-Za-z_]\\w*)\\.id\\s*=\\s*('§\\d+'|\\$\\w+)", body) if val(tok) == a}
    known = {v: () for v in avars}
    is_anchor = lambda n: n["id"] == a or (n["var"] in avars)
    todo = list(paths)
    while todo:
        progress = False
        for p in list(todo):
            ns, rs = p[::2], p[1::2]
            start = 0 if (is_anchor(ns[0]) or ns[0]["var"] in known) else (len(ns) - 1 if (is_anchor(ns[-1]) or ns[-1]["var"] in known) else None)
            if start is None:
                continue
            cur = () if is_anchor(ns[start]) else known[ns[start]["var"]]
            order = range(1, len(ns)) if start == 0 else range(len(ns) - 2, -1, -1)
            for j in order:
                r = rs[j - 1] if start == 0 else rs[j]
                d = ("out" if r["right"] else "in") if start == 0 else ("in" if r["right"] else "out")
                cur = cur + ((r["type"], d),)
                if cur not in L1_SHAPES:
                    return a, False
                v = ns[j]["var"]
                if v and known.get(v, cur) != cur:
                    return a, False
                if v:
                    known[v] = cur
            todo.remove(p)
            progress = True
        if not progress:
            return a, False
    return a, True


def l1_scope_cell(q, params, cat):
    """Ô L1 của bảng mẫu nếu truy vấn chỉ đi theo hình khai báo từ MỘT bảng mẫu; ngược lại None."""
    a, ok = _l1_parse(q, params, cat)
    return ("l1:" + a) if a and ok else None


def layers_for(qc, need, eff, anchor, now=None):
    """Khối nhãn theo lớp (BL1): L1 catalog khai báo · L2 đọc văn bản (luôn MỘT PHẦN) · L3 chạy thật (MỞ)."""
    l1c = ["l1:" + anchor] if anchor else []          # lớp L1 chỉ áp cho câu hỏi neo vào MỘT bảng mẫu
    st = [eff.get(k, (MP, "NOT_CERTIFIED", None, None)) for k in l1c]
    ok = bool(st) and all(s[0] == DU for s in st)
    L1 = {"kind": "CATALOG_DECLARED_EXACT_AT_SNAPSHOT", "cells": l1c, "label": (DU if ok else MP) if l1c else "KHÔNG_ÁP_DỤNG",
          "proof_issued_at": min(s[2] for s in st) if ok else None, "expires_at": min(s[3] for s in st) if ok else None,
          "reasons": [s[1] for s in st if s[0] != DU][:4],
          "scope": "khoá ngoại vào/ra · view phụ thuộc trực tiếp · trigger→hàm xử lý · Directus collection/relation/permission khai báo",
          "not_proven": "bảng nào được hàm đọc/ghi · quyền Directus lúc chạy (chính sách admin bỏ qua dòng quyền) · DROP an toàn · tác động động"}
    L2 = {"kind": "SOURCE_TEXT_DERIVED_PARTIAL", "label": MP,
          "reason": "thân hàm PL/pgSQL/EXECUTE động, flow/operation Directus, DOT, mã: ứng viên đọc văn bản — tham chiếu tĩnh không chứng minh thực thi"}
    l2 = jload(L2_FILE)
    if isinstance(l2, dict):
        L2["snapshot"] = {"file": L2_FILE, "generated_at": l2.get("generated_at"), "self_sha256": l2.get("self_sha256")}
        t = (l2.get("tables") or {}).get(anchor) if anchor else None
        if t:
            L2["candidates_count"] = len(t.get("candidates") or [])
            L2["candidates"] = [{k: c.get(k) for k in ("kind", "via", "target", "op", "trust", "source", "line")} for c in (t.get("candidates") or [])[:12]]
            L2["potential_collisions"] = (t.get("potential_collisions") or [])[:8]
            L2["unknown_dynamic"] = (t.get("unknown_dynamic") or [])[:6]
    else:
        L2["snapshot"] = None
    L3 = {"kind": "RUNTIME_OPEN", "label": "MỞ",
          "reason": "lịch sử chạy, đồng thời, khoá, thứ tự thực thi không có trong catalog/văn bản; C1-B không dựng bộ theo dõi mới. "
                    "Hai đường cùng ghi một đích = POTENTIAL_COLLISION, không phải RUNTIME_CONFIRMED."}
    return {"L1": L1, "L2": L2, "L3": L3}


def label_for(tool, arguments=None, result_rows=None, now=None, doc=None, cat=None):''')

rep('''           "evidence": {"manifest": CURRENT}, "query_class": None, "query_catalog_version": QUERY_CATALOG_VERSION,
           "reason": None, "computed_at": now_iso(now),''', '''           "evidence": {"manifest": CURRENT}, "query_class": None, "query_catalog_version": QUERY_CATALOG_VERSION,
           "reason": None, "computed_at": now_iso(now), "answer_scope": None, "impact_question_actionability": ACT_NO,
           "layers": {"L1": {"label": MP}, "L2": {"label": MP}, "L3": {"label": "MỞ"}},''')

rep('''QUERY_CATALOG_VERSION = "n4-qc-1"''', '''QUERY_CATALOG_VERSION = "n4-qc-2"   # C1-B: + L1_SCOPED_LOOKUP (hình L1 từ một bảng mẫu) + khối layers L1/L2/L3''')

rep('''        q = (arguments or {}).get("query") or (arguments or {}).get("cypher") or ""
        qc, need, reason = classify_query(q, cat)
        lab["query_class"] = qc''', '''        q = (arguments or {}).get("query") or (arguments or {}).get("cypher") or ""
        qc, need, reason = classify_query(q, cat)
        params = (arguments or {}).get("params") if isinstance((arguments or {}).get("params"), dict) else {}
        anchor, shape_ok = _l1_parse(q, params, cat)
        if qc == "CELL_SCOPED_LOOKUP" and anchor and shape_ok:
            qc, need = "L1_SCOPED_LOOKUP", ["l1:" + anchor]
        lab["query_class"] = qc
        lab["answer_scope"] = {"L1_SCOPED_LOOKUP": "L1_DECLARED_CATALOG_ONLY", "IMPACT_OR_PATH": "FULL_IMPACT_ALL_LAYERS"}.get(qc, "CELL_SCOPED" if qc == "CELL_SCOPED_LOOKUP" else "UNSUPPORTED_OR_UNCERTIFIED")''')

rep('''        if qc == "CELL_SCOPED_LOOKUP" and not miss:''', '''        lab["layers"] = layers_for(qc, need, eff, anchor, now)
        if qc in ("CELL_SCOPED_LOOKUP", "L1_SCOPED_LOOKUP") and not miss:''')

rep('''    for i in inc:
        i["id"] = hashlib.sha256(''', '''    for i in inc:
        i.setdefault("owner", OWNER)
        i["id"] = hashlib.sha256(''')

rep('''    s.add_argument("--tool", default="read-cypher")''', '''    s.add_argument("--tool", default="read-cypher")
    s.add_argument("--params", default="{}")''')
rep('''        print(json.dumps(label_for(a.tool, {"query": a.query}, a.rows), ensure_ascii=False, indent=1))''',
    '''        print(json.dumps(label_for(a.tool, {"query": a.query, "params": json.loads(a.params)}, a.rows), ensure_ascii=False, indent=1))''')

open(dst, "w", encoding="utf-8").write(t)
print("PATCH OK", len(t))
