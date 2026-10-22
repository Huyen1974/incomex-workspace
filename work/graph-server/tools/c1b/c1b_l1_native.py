#!/usr/bin/env python3
"""c1b_l1_native — BỘ ĐỌC L1 (catalog khai báo) cho danh sách bảng, phía BỘ NẠP · GS-C1B-LAYERED-IMPACT-20261022-08

Chạy TRONG container incomex-claude-mcp (vai context_pack_readonly, một giao dịch REPEATABLE READ READ ONLY):
  ssh contabo 'docker exec -i -e C1B_TABLES=<json list "db.schema.table"> incomex-claude-mcp python -I -B -' < c1b_l1_native.py
Lọc NGAY trong SQL theo bảng (bộ kiểm graph_cert đọc trọn database rồi lọc bằng Python — hai cách viết độc lập, không dùng
chung đầu ra). Lớp L1: khoá ngoại vào/ra (pg_constraint, cột + hành động ON UPDATE/DELETE) · view/matview phụ thuộc trực tiếp
(pg_rewrite+pg_depend) · trigger không nội bộ + hàm xử lý (pg_trigger.tgfoid→pg_proc) · Directus khai báo: directus_collections,
directus_relations (many/one), directus_permissions (id, action, policy — KHÔNG đọc permissions/validation/presets/fields).
KHÔNG có cạnh đọc/ghi trong thân hàm (L2). In JSON. Không ghi gì.
"""
import json, os
import psycopg

OPT = "-c default_transaction_read_only=on -c statement_timeout=30000 -c lock_timeout=2000 -c idle_in_transaction_session_timeout=120000"
tables = json.loads(os.environ["C1B_TABLES"])
dbs = {t.split(".")[0] for t in tables}
assert dbs == {"directus"}, "chỉ db directus"
qual = [t.split(".", 1)[1] for t in tables]                       # schema.table
pub = [q.split(".", 1)[1] for q in qual if q.startswith("public.")]  # tên collection Directus = bảng schema public
conn = psycopg.connect(host=os.environ.get("PG_HOST", "postgres"), port=os.environ.get("PG_PORT", "5432"), user=os.environ["PG_USER_RO"],
                       password=os.environ["PG_PASSWORD_RO"], dbname="directus", connect_timeout=5, options=OPT, autocommit=True)
cur = conn.cursor()
cur.execute("BEGIN ISOLATION LEVEL REPEATABLE READ READ ONLY")
cur.execute("SELECT current_user, current_setting('transaction_read_only'), current_setting('transaction_isolation'), pg_current_snapshot()::text, "
            "to_char(clock_timestamp() AT TIME ZONE 'UTC','YYYY-MM-DD\"T\"HH24:MI:SS\"Z\"'), txid_current_if_assigned()")
role, ro, iso, snap, ts, xid = cur.fetchone()
assert ro == "on" and iso == "repeatable read" and xid is None
S = lambda v: None if v is None else str(v)


def q(sql, *a):
    cur.execute(sql, a)
    return [[S(x) for x in r] for r in cur.fetchall()]


COLS = ("(SELECT string_agg(a.attname, ',' ORDER BY k.o) FROM unnest(%s) WITH ORDINALITY k(n, o) JOIN pg_attribute a "
        "ON a.attrelid=%s AND a.attnum=k.n)")
out = {"reader": {"role": role, "isolation": iso, "read_only": ro, "pg_snapshot": snap, "snapshot_utc": ts}, "tables": {}}
exists = {r[0]: r[1] for r in q("SELECT n.nspname||'.'||c.relname, c.relkind::text FROM pg_class c JOIN pg_namespace n ON n.oid=c.relnamespace "
                                 "WHERE n.nspname||'.'||c.relname = ANY(%s)", qual)}
fk = q("SELECT n1.nspname||'.'||c1.relname, co.conname, n2.nspname||'.'||c2.relname, " + COLS % ("co.conkey", "co.conrelid") + ", " +
       COLS % ("co.confkey", "co.confrelid") + ", co.confupdtype::text, co.confdeltype::text FROM pg_constraint co "
       "JOIN pg_class c1 ON c1.oid=co.conrelid JOIN pg_namespace n1 ON n1.oid=c1.relnamespace "
       "JOIN pg_class c2 ON c2.oid=co.confrelid JOIN pg_namespace n2 ON n2.oid=c2.relnamespace "
       "WHERE co.contype='f' AND (n1.nspname||'.'||c1.relname = ANY(%s) OR n2.nspname||'.'||c2.relname = ANY(%s))", qual, qual)
vd = q("SELECT DISTINCT vn.nspname||'.'||v.relname, v.relkind::text, tn.nspname||'.'||t.relname FROM pg_depend d "
       "JOIN pg_rewrite r ON r.oid=d.objid JOIN pg_class v ON v.oid=r.ev_class JOIN pg_class t ON t.oid=d.refobjid "
       "JOIN pg_namespace vn ON vn.oid=v.relnamespace JOIN pg_namespace tn ON tn.oid=t.relnamespace "
       "WHERE d.classid='pg_rewrite'::regclass AND d.refclassid='pg_class'::regclass AND v.oid<>t.oid "
       "AND tn.nspname||'.'||t.relname = ANY(%s)", qual)
tg = q("SELECT n.nspname||'.'||c.relname, t.tgname, pn.nspname||'.'||p.proname||'('||pg_get_function_identity_arguments(p.oid)||')', "
       "t.tgenabled::text FROM pg_trigger t JOIN pg_class c ON c.oid=t.tgrelid JOIN pg_namespace n ON n.oid=c.relnamespace "
       "JOIN pg_proc p ON p.oid=t.tgfoid JOIN pg_namespace pn ON pn.oid=p.pronamespace "
       "WHERE NOT t.tgisinternal AND n.nspname||'.'||c.relname = ANY(%s)", qual)
dc = q("SELECT collection FROM directus_collections WHERE collection = ANY(%s)", pub)
dr = q("SELECT id, many_collection, many_field, one_collection FROM directus_relations WHERE many_collection = ANY(%s) OR one_collection = ANY(%s)", pub, pub)
dp = q("SELECT id, collection, action, policy FROM directus_permissions WHERE collection = ANY(%s)", pub)
# điểm cuối phía bên kia: bảng tồn tại? collection khai báo?
others = sorted({r[0] for r in fk} | {r[2] for r in fk} | {r[0] for r in vd})
ends = {r[0]: r[1] for r in q("SELECT n.nspname||'.'||c.relname, c.relkind::text FROM pg_class c JOIN pg_namespace n ON n.oid=c.relnamespace "
                               "WHERE n.nspname||'.'||c.relname = ANY(%s)", others)}
cols = sorted({x for r in dr for x in (r[1], r[3]) if x})
dc_all = {r[0] for r in q("SELECT collection FROM directus_collections WHERE collection = ANY(%s)", cols)}
pub_tables = {r[0]: r[1] for r in q("SELECT c.relname, c.relkind::text FROM pg_class c JOIN pg_namespace n ON n.oid=c.relnamespace WHERE n.nspname='public' "
                                     "AND c.relkind IN ('r','p','f','v','m') AND c.relname = ANY(%s)", cols)}
cur.execute("SELECT txid_current_if_assigned()")
out["reader"]["xid_after"] = cur.fetchone()[0]
cur.execute("ROLLBACK")
conn.close()
out["rows"] = {"fk": fk, "view_dep": vd, "trigger": tg, "directus_collection": dc, "directus_relation": dr, "directus_permission": dp}
out["exists"] = exists
out["endpoints"] = ends
out["relation_collections"] = {c: {"in_directus_collections": c in dc_all, "public_relkind": pub_tables.get(c)} for c in cols}
print(json.dumps(out, ensure_ascii=False))
