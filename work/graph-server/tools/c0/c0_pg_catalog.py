# GS-C0-COVERAGE-INVENTORY-20261022-05 · F1/F2/F4/F6(PG)/F10(PG) · KIỂM KÊ CATALOG PG CHỈ-ĐỌC — dùng lại được
# Chạy BÊN TRONG container cổng query_pg qua stdin (cùng đường R6D/R7 r7_b5_pg.py, không ghi file vào container):
#   ssh contabo 'timeout 300 docker exec -i incomex-claude-mcp python -I -B -' < c0_pg_catalog.py > pg.json
# Role PG_USER_RO (context_pack_readonly), mỗi database một giao dịch REPEATABLE READ READ ONLY, statement_timeout.
# Chỉ tên đối tượng/mã/số đếm — không đọc nội dung bản ghi nghiệp vụ, không in credential. Bảng lớn: pg_class.reltuples.
# Đầu ra JSON: {"summary": số đếm (lên repo được), "detail": danh sách tên (chỉ lưu Mac riêng)}.
# Exit: 0 ok · 3 cổng chỉ-đọc không đạt ở database directus · 4 lỗi kết nối directus
import json, os, sys

import psycopg

OPT = ("-c default_transaction_read_only=on -c statement_timeout=20000 "
       "-c lock_timeout=2000 -c idle_in_transaction_session_timeout=60000")
SYS = "('pg_catalog','information_schema','pg_toast')"
USER_NS = f"n.nspname NOT IN {SYS} AND n.nspname NOT LIKE 'pg_temp%' AND n.nspname NOT LIKE 'pg_toast%'"
REGISTRIES = ["collection_registry", "meta_catalog", "table_registry", "trigger_registry", "dot_tools",
              "dot_iu_command_catalog", "entity_species", "species_collection_map", "law_catalog",
              "normative_registry", "measurement_registry", "event_type_registry", "workflow_scanner_registry",
              "workflow_discovery_source_registry", "iu_qdrant_collection_registry", "governance_registry",
              "birth_registry"]
# cột khoá/tên ổn định để đối chiếu (chỉ tên đối tượng hệ thống, không phải dữ liệu nghiệp vụ)
REG_KEYS = {"collection_registry": "collection_name", "table_registry": "collection",
            "species_collection_map": "collection_name", "iu_qdrant_collection_registry": "collection_name",
            "dot_tools": "code", "trigger_registry": "trigger_name", "meta_catalog": "code",
            "entity_species": "species_code", "law_catalog": "law_code", "normative_registry": "code",
            "governance_registry": "code", "event_type_registry": "event_type",
            "workflow_scanner_registry": "scanner_code", "workflow_discovery_source_registry": "source_name",
            "measurement_registry": "measurement_id", "dot_iu_command_catalog": "command_name"}
DIRECTUS = ["directus_collections", "directus_fields", "directus_relations", "directus_flows", "directus_operations",
            "directus_roles", "directus_policies", "directus_permissions", "directus_access", "directus_users",
            "directus_presets", "directus_webhooks", "directus_extensions", "directus_dashboards", "directus_panels"]


def q(cur, sql, args=None):
    cur.execute(sql, args)
    return cur.fetchall()


def one(cur, sql, args=None):
    cur.execute(sql, args)
    return cur.fetchone()[0]


def connect(db):
    return psycopg.connect(host=os.environ.get("PG_HOST", "postgres"), port=os.environ.get("PG_PORT", "5432"),
                           user=os.environ["PG_USER_RO"], password=os.environ["PG_PASSWORD_RO"], dbname=db,
                           connect_timeout=5, options=OPT, autocommit=True)


def begin(cur):
    cur.execute("BEGIN ISOLATION LEVEL REPEATABLE READ READ ONLY")
    cur.execute("SET LOCAL statement_timeout = '20s'")
    r = q(cur, "SELECT current_user, (SELECT rolsuper FROM pg_roles WHERE rolname=current_user), "
               "current_setting('transaction_read_only'), current_setting('server_version'), "
               "to_char(clock_timestamp() AT TIME ZONE 'UTC','YYYY-MM-DD\"T\"HH24:MI:SS\"Z\"')")[0]
    return {"role": r[0], "rolsuper": r[1], "transaction_read_only": r[2], "server_version": r[3], "snapshot_utc": r[4]}


def catalog(cur):
    s, d = {}, {}
    s["schemas"] = one(cur, f"SELECT count(*) FROM pg_namespace n WHERE {USER_NS}")
    rk = dict(q(cur, f"SELECT c.relkind::text, count(*) FROM pg_class c JOIN pg_namespace n ON n.oid=c.relnamespace "
                     f"WHERE {USER_NS} GROUP BY 1"))
    s["relkind"] = {"base_tables": rk.get("r", 0), "partitioned": rk.get("p", 0), "views": rk.get("v", 0),
                    "matviews": rk.get("m", 0), "sequences": rk.get("S", 0), "foreign": rk.get("f", 0),
                    "indexes": rk.get("i", 0) + rk.get("I", 0), "composite_types": rk.get("c", 0)}
    s["columns"] = one(cur, f"SELECT count(*) FROM pg_attribute a JOIN pg_class c ON c.oid=a.attrelid "
                            f"JOIN pg_namespace n ON n.oid=c.relnamespace WHERE {USER_NS} AND a.attnum>0 "
                            f"AND NOT a.attisdropped AND c.relkind IN ('r','p','v','m','f')")
    s["constraints"] = dict(q(cur, f"SELECT co.contype::text, count(*) FROM pg_constraint co "
                                   f"JOIN pg_namespace n ON n.oid=co.connamespace WHERE {USER_NS} GROUP BY 1"))
    fk = q(cur, f"SELECT DISTINCT n1.nspname||'.'||c1.relname, n2.nspname||'.'||c2.relname FROM pg_constraint co "
                f"JOIN pg_class c1 ON c1.oid=co.conrelid JOIN pg_namespace n1 ON n1.oid=c1.relnamespace "
                f"JOIN pg_class c2 ON c2.oid=co.confrelid JOIN pg_namespace n2 ON n2.oid=c2.relnamespace "
                f"JOIN pg_namespace n ON n.oid=co.connamespace WHERE co.contype='f' AND {USER_NS} ORDER BY 1,2")
    s["fk_table_pairs"] = len(fk)
    d["fk_pairs"] = fk
    s["triggers_non_internal"] = one(cur, f"SELECT count(*) FROM pg_trigger t JOIN pg_class c ON c.oid=t.tgrelid "
                                          f"JOIN pg_namespace n ON n.oid=c.relnamespace WHERE NOT t.tgisinternal "
                                          f"AND {USER_NS}")
    evt = q(cur, "SELECT evtname, evtevent, evtfoid::regproc::text, evtenabled::text FROM pg_event_trigger ORDER BY 1")
    s["event_triggers"] = len(evt)
    s["event_trigger_list"] = evt
    fdw = q(cur, "SELECT n.nspname||'.'||c.relname, sv.srvname FROM pg_foreign_table f JOIN pg_class c ON c.oid=f.ftrelid "
                 "JOIN pg_namespace n ON n.oid=c.relnamespace JOIN pg_foreign_server sv ON sv.oid=f.ftserver ORDER BY 1")
    s["foreign_tables"] = fdw
    s["functions_by_kind"] = dict(q(cur, f"SELECT p.prokind::text, count(*) FROM pg_proc p "
                                         f"JOIN pg_namespace n ON n.oid=p.pronamespace "
                                         f"LEFT JOIN pg_depend dep ON dep.objid=p.oid AND dep.deptype='e' "
                                         f"WHERE {USER_NS} AND dep.objid IS NULL GROUP BY 1"))
    s["functions_from_extensions"] = one(cur, f"SELECT count(*) FROM pg_proc p JOIN pg_namespace n ON n.oid=p.pronamespace "
                                              f"JOIN pg_depend dep ON dep.objid=p.oid AND dep.deptype='e' WHERE {USER_NS}")
    vdep = q(cur, f"SELECT DISTINCT nv.nspname||'.'||v.relname, nt.nspname||'.'||t.relname, t.relkind::text "
                  f"FROM pg_rewrite r JOIN pg_class v ON v.oid=r.ev_class JOIN pg_namespace nv ON nv.oid=v.relnamespace "
                  f"JOIN pg_depend dp ON dp.objid=r.oid AND dp.classid='pg_rewrite'::regclass AND dp.refclassid='pg_class'::regclass "
                  f"JOIN pg_class t ON t.oid=dp.refobjid JOIN pg_namespace nt ON nt.oid=t.relnamespace "
                  f"JOIN pg_namespace n ON n.oid=v.relnamespace "
                  f"WHERE v.relkind IN ('v','m') AND t.oid<>v.oid AND {USER_NS} ORDER BY 1,2")
    s["view_dep_pairs"] = len(vdep)
    s["views_with_deps"] = len({a for a, _, _ in vdep})
    d["view_deps"] = vdep
    s["extensions"] = {k: v for k, v in q(cur, "SELECT extname, extversion FROM pg_extension ORDER BY 1")}
    # pub/sub / CDC đã cài (chỉ đếm metadata)
    s["publications"] = one(cur, "SELECT count(*) FROM pg_publication")
    try:
        s["replication_slots"] = one(cur, "SELECT count(*) FROM pg_replication_slots")
    except Exception as e:
        s["replication_slots"] = f"NO_ACCESS:{type(e).__name__}"
        cur.execute("ROLLBACK"); begin(cur)
    try:
        s["subscriptions"] = one(cur, "SELECT count(*) FROM pg_subscription")
    except Exception as e:
        s["subscriptions"] = f"NO_ACCESS:{type(e).__name__}"
        cur.execute("ROLLBACK"); begin(cur)
    # hàm có NOTIFY / EXECUTE động (đếm theo thân hàm — tĩnh, không chạy)
    fn_notify = q(cur, f"SELECT n.nspname||'.'||p.proname FROM pg_proc p JOIN pg_namespace n ON n.oid=p.pronamespace "
                       f"WHERE {USER_NS} AND p.prokind IN ('f','p') AND (p.prosrc ~* 'pg_notify\\s*\\(' OR p.prosrc ~* '\\mNOTIFY\\s+[a-z_]') ORDER BY 1")
    s["functions_with_notify"] = len(fn_notify)
    d["functions_with_notify"] = [r[0] for r in fn_notify]
    s["functions_with_dynamic_execute"] = one(cur, f"SELECT count(*) FROM pg_proc p JOIN pg_namespace n ON n.oid=p.pronamespace "
                                                   f"WHERE {USER_NS} AND p.prokind IN ('f','p') AND p.prosrc ~* '\\mEXECUTE\\M'")
    # danh sách tên để khớp Graph theo khoá ổn định
    d["base_tables"] = [r[0] for r in q(cur, f"SELECT n.nspname||'.'||c.relname FROM pg_class c JOIN pg_namespace n "
                                             f"ON n.oid=c.relnamespace WHERE {USER_NS} AND c.relkind IN ('r','p') ORDER BY 1")]
    d["views"] = [r[0] for r in q(cur, f"SELECT n.nspname||'.'||c.relname||'|'||c.relkind::text FROM pg_class c JOIN pg_namespace n "
                                       f"ON n.oid=c.relnamespace WHERE {USER_NS} AND c.relkind IN ('v','m') ORDER BY 1")]
    d["functions"] = [r[0] for r in q(cur, f"SELECT n.nspname||'.'||p.proname||'('||pg_get_function_identity_arguments(p.oid)||')' "
                                           f"FROM pg_proc p JOIN pg_namespace n ON n.oid=p.pronamespace "
                                           f"LEFT JOIN pg_depend dep ON dep.objid=p.oid AND dep.deptype='e' "
                                           f"WHERE {USER_NS} AND dep.objid IS NULL ORDER BY 1")]
    d["triggers"] = [r[0] for r in q(cur, f"SELECT n.nspname||'.'||c.relname||'.'||t.tgname FROM pg_trigger t "
                                          f"JOIN pg_class c ON c.oid=t.tgrelid JOIN pg_namespace n ON n.oid=c.relnamespace "
                                          f"WHERE NOT t.tgisinternal AND {USER_NS} ORDER BY 1")]
    d["tables_with_trigger"] = sorted({x.rsplit('.', 1)[0] for x in d["triggers"]})
    s["tables_with_trigger"] = len(d["tables_with_trigger"])
    est = q(cur, f"SELECT coalesce(sum(greatest(c.reltuples,0)),0)::bigint, pg_database_size(current_database()) "
                 f"FROM pg_class c JOIN pg_namespace n ON n.oid=c.relnamespace WHERE {USER_NS} AND c.relkind IN ('r','p')")[0]
    s["rows_estimated_reltuples"] = est[0]
    s["db_size_bytes"] = est[1]
    return s, d


def registries(cur, base_tables, triggers):
    s, d = {}, {}
    rows = q(cur, "SELECT c.relname, n.nspname, c.reltuples::bigint FROM pg_class c JOIN pg_namespace n ON n.oid=c.relnamespace "
                  "WHERE c.relkind IN ('r','p','v') AND c.relname = ANY(%s)", (REGISTRIES,))
    found = {r[0]: (r[1], r[2]) for r in rows}
    for name in REGISTRIES:
        if name not in found:
            s[name] = {"exists": False}
            continue
        ns, est = found[name]
        ent = {"exists": True, "schema": ns}
        if est > 100000:
            ent["rows"] = est
            ent["rows_kind"] = "ESTIMATED_reltuples"
        else:
            ent["rows"] = one(cur, f'SELECT count(*) FROM "{ns}"."{name}"')
            ent["rows_kind"] = "EXACT"
        key = REG_KEYS.get(name)
        if key and est <= 100000:
            vals = [r[0] for r in q(cur, f'SELECT DISTINCT "{key}"::text FROM "{ns}"."{name}" WHERE "{key}" IS NOT NULL ORDER BY 1')]
            d[name] = vals
            ent["distinct_keys"] = len(vals)
        if name == "dot_tools":  # F10: đường tệp khai trong sổ PG để đối chiếu với dot/bin + 00-SO-DOT
            d["dot_tools__file_path"] = [r[0] for r in q(cur, f'SELECT DISTINCT coalesce(file_path, script_path)::text FROM "{ns}"."{name}" '
                                                              f'WHERE coalesce(file_path, script_path) IS NOT NULL ORDER BY 1')]
            ent["with_file_path"] = len(d["dot_tools__file_path"])
        s[name] = ent
    # đối chiếu sổ ↔ thực tế (tên bảng không schema: các sổ ghi tên collection = tên bảng public)
    pub = {t.split('.', 1)[1] for t in base_tables if t.startswith('public.')}
    for reg in ("collection_registry", "table_registry", "species_collection_map"):
        if reg in d:
            vals = set(d[reg])
            s[reg]["vs_base_tables"] = {"matched": len(vals & pub), "registry_not_table": len(vals - pub),
                                        "table_not_in_registry": len(pub - vals)}
            d[reg + "__registry_not_table"] = sorted(vals - pub)
            d[reg + "__table_not_in_registry"] = sorted(pub - vals)
    if "trigger_registry" in d:
        live = {t.rsplit('.', 1)[1] for t in triggers}
        vals = set(d["trigger_registry"])
        s["trigger_registry"]["vs_pg_trigger_names"] = {"matched": len(vals & live), "registry_not_live": len(vals - live),
                                                         "live_not_in_registry": len(live - vals)}
        d["trigger_registry__registry_not_live"] = sorted(vals - live)
    return s, d


def directus(cur, base_tables):
    s, d = {}, {}
    have = {r[0] for r in q(cur, "SELECT c.relname FROM pg_class c JOIN pg_namespace n ON n.oid=c.relnamespace "
                                 "WHERE n.nspname='public' AND c.relname = ANY(%s)", (DIRECTUS,))}
    for t in DIRECTUS:
        if t not in have:
            s[t] = None
            continue
        try:
            s[t] = one(cur, f'SELECT count(*) FROM public."{t}"')
        except Exception as e:
            s[t] = f"NO_ACCESS:{type(e).__name__}"
            cur.execute("ROLLBACK"); begin(cur)
    pub = {t.split('.', 1)[1] for t in base_tables if t.startswith('public.')}
    try:
        coll = {r[0] for r in q(cur, "SELECT collection FROM public.directus_collections ORDER BY 1")}
        d["directus_collections"] = sorted(coll)
        d["collection_no_table"] = sorted(coll - pub)
        s["collections_vs_tables"] = {"collections": len(coll),
                                      "matched_table": len(coll & pub), "collection_no_table_folder_or_alias": len(coll - pub),
                                      "public_table_not_collection_excl_directus": len({t for t in pub - coll if not t.startswith('directus_')}),
                                      "directus_system_tables": len({t for t in pub if t.startswith('directus_')})}
        d["public_table_not_collection"] = sorted(t for t in pub - coll if not t.startswith('directus_'))
        rel = q(cur, "SELECT many_collection, many_field, coalesce(one_collection,'') FROM public.directus_relations ORDER BY 1,2")
        d["directus_relations"] = rel
        s["relations_with_one_collection"] = sum(1 for r in rel if r[2])
        fl = q(cur, "SELECT f.id::text, f.trigger, f.status, (SELECT count(*) FROM public.directus_operations o WHERE o.flow=f.id) "
                    "FROM public.directus_flows f ORDER BY 1")
        d["directus_flows"] = fl
        s["flows_by_trigger"] = {}
        for _, trg, st, _n in fl:
            k = f"{trg}|{st}"
            s["flows_by_trigger"][k] = s["flows_by_trigger"].get(k, 0) + 1
        # flow → collection khai trong options (chỉ đếm khoá 'collections' — metadata cấu hình, không nội dung bản ghi)
        fc = q(cur, "SELECT f.id::text, jsonb_array_elements_text(CASE WHEN jsonb_typeof(f.options::jsonb->'collections')='array' "
                    "THEN f.options::jsonb->'collections' ELSE '[]'::jsonb END) FROM public.directus_flows f")
        d["flow_collection_pairs"] = fc
        s["flow_collection_pairs"] = len(fc)
        oc = q(cur, "SELECT o.flow::text, o.type, coalesce(o.options::jsonb->>'collection','') FROM public.directus_operations o")
        s["operations_by_type"] = {}
        for _, typ, _c in oc:
            s["operations_by_type"][typ] = s["operations_by_type"].get(typ, 0) + 1
        d["operation_collection_pairs"] = [(f, c) for f, _t, c in oc if c]
        s["operation_collection_pairs"] = len(d["operation_collection_pairs"])
        s["permission_collections"] = one(cur, "SELECT count(DISTINCT collection) FROM public.directus_permissions")
    except Exception as e:
        s["error"] = type(e).__name__
        cur.execute("ROLLBACK"); begin(cur)
    return s, d


def kb(cur):
    # kb_documents = (key, data jsonb, updated_at): trạng thái vector nằm trong jsonb ⇒ đếm theo trạng thái cần đọc
    # toàn bảng (~400 MB) — PROMPT §1 cấm quét toàn bảng lớn ⇒ chỉ reltuples + kích thước; phân rã trạng thái lấy P191.
    r = q(cur, "SELECT c.reltuples::bigint, pg_total_relation_size(c.oid) FROM pg_class c JOIN pg_namespace n "
               "ON n.oid=c.relnamespace WHERE n.nspname='public' AND c.relname='kb_documents'")[0]
    return {"kb_documents_rows_estimated": r[0], "kb_documents_total_bytes": r[1],
            "vector_status_breakdown": "NOT_MEASURED_FULL_SCAN_FORBIDDEN (see P191)"}


def main():
    out = {"summary": {"databases": {}}, "detail": {}}
    try:
        c0 = connect("directus")
    except Exception as e:
        print(json.dumps({"error": "connect", "type": type(e).__name__}))
        return 4
    cur0 = c0.cursor()
    dbs = q(cur0, "SELECT datname, has_database_privilege(current_user, datname, 'CONNECT') FROM pg_database "
                  "WHERE NOT datistemplate AND datallowconn ORDER BY 1")
    c0.close()
    rc = 0
    for db, can in dbs:
        ent = {"connect_privilege": can}
        out["summary"]["databases"][db] = ent
        if not can:
            ent["access"] = "NO_ACCESS"
            continue
        try:
            conn = connect(db)
        except Exception as e:
            ent["access"] = f"NO_ACCESS:{type(e).__name__}"
            continue
        cur = conn.cursor()
        try:
            ent["session"] = begin(cur)
            if ent["session"]["rolsuper"] or ent["session"]["transaction_read_only"] != "on":
                ent["access"] = "READONLY_GATE_FAIL"
                cur.execute("ROLLBACK")
                rc = 3 if db == "directus" else rc
                continue
            ent["access"] = "OK"
            s, d = catalog(cur)
            ent["catalog"] = s
            out["detail"][db] = {"catalog": d}
            rs, rd = registries(cur, d["base_tables"], d["triggers"])
            if any(v.get("exists") for v in rs.values()):
                ent["registries"] = rs
                out["detail"][db]["registries"] = rd
            if "directus_collections" in {t.split('.', 1)[1] for t in d["base_tables"] if t.startswith('public.')}:
                ds, dd = directus(cur, d["base_tables"])
                ent["directus"] = ds
                out["detail"][db]["directus"] = dd
            if "public.kb_documents" in d["base_tables"]:
                ent["kb"] = kb(cur)
            cur.execute("ROLLBACK")
        except Exception as e:
            ent["error"] = f"{type(e).__name__}"
            try:
                cur.execute("ROLLBACK")
            except Exception:
                pass
        finally:
            conn.close()
    print(json.dumps(out, ensure_ascii=False, default=str))
    return rc


if __name__ == "__main__":
    sys.exit(main())
