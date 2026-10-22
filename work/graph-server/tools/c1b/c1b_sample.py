#!/usr/bin/env python3
"""c1b_sample — KHOÁ MẪU 11 BẢNG C1-B (chỉ đọc catalog PG) · GS-C1B-LAYERED-IMPACT-20261022-08

Chạy TRONG container incomex-claude-mcp (vai context_pack_readonly, REPEATABLE READ READ ONLY, khuôn C0/C1-A):
  ssh contabo 'docker exec -i incomex-claude-mcp python -I -B -' < c1b_sample.py
Neo: directus.public.information_unit (kiểm danh tính native). 10 bảng đối chứng theo 5 tầng, mỗi tầng 2 bảng có
SHA256(SEED + khoá) nhỏ nhất chưa chọn/không phải neo; khoá = "directus.<schema>.<bảng>"; tầng thiếu ⇒ lấp từ toàn tập + PARTIAL.
Tầng (thứ tự cố định): fk (bảng có khoá ngoại vào/ra) · view_dep (bảng được view/matview phụ thuộc qua pg_rewrite+pg_depend) ·
trigger (bảng có trigger không nội bộ) · directus_relation (collection có trong directus_relations many/one) ·
directus_permission (collection có dòng directus_permissions). In JSON: danh sách 11 + ảnh chụp + đếm/băm từng tập.
Không ghi gì. Exit 0.
"""
import hashlib, json, os
import psycopg

SEED = "GS-C1B-LAYERED-IMPACT-20261022-08"
ANCHOR = "directus.public.information_unit"
OPT = "-c default_transaction_read_only=on -c statement_timeout=30000 -c lock_timeout=2000 -c idle_in_transaction_session_timeout=120000"
NS = "n.nspname NOT IN ('pg_catalog','information_schema','pg_toast') AND n.nspname NOT LIKE 'pg_temp%' AND n.nspname NOT LIKE 'pg_toast%'"
STRATA = ("fk", "view_dep", "trigger", "directus_relation", "directus_permission")
h = lambda k: hashlib.sha256((SEED + k).encode()).hexdigest()
digest = lambda xs: hashlib.sha256("\n".join(sorted(xs)).encode()).hexdigest()

conn = psycopg.connect(host=os.environ.get("PG_HOST", "postgres"), port=os.environ.get("PG_PORT", "5432"), user=os.environ["PG_USER_RO"],
                       password=os.environ["PG_PASSWORD_RO"], dbname="directus", connect_timeout=5, options=OPT, autocommit=True)
cur = conn.cursor()
cur.execute("BEGIN ISOLATION LEVEL REPEATABLE READ READ ONLY")
cur.execute("SELECT current_database(), current_user, current_setting('transaction_read_only'), current_setting('transaction_isolation'), "
            "pg_current_snapshot()::text, to_char(clock_timestamp() AT TIME ZONE 'UTC','YYYY-MM-DD\"T\"HH24:MI:SS\"Z\"'), version()")
db, role, ro, iso, snap, ts, ver = cur.fetchone()
assert ro == "on" and iso == "repeatable read", "NO_READONLY_REPEATABLE_READ"
q = lambda sql: [tuple(r) for r in (cur.execute(sql) or cur.fetchall())]
uni = {"%s.%s.%s" % (db, s, t): k for s, t, k in q("SELECT n.nspname, c.relname, c.relkind::text FROM pg_class c JOIN pg_namespace n "
                                                     "ON n.oid=c.relnamespace WHERE c.relkind IN ('r','p','f') AND " + NS)}
pub = {k.split(".", 2)[2]: k for k in uni if k.split(".")[1] == "public"}
sets = {}
sets["fk"] = {"%s.%s" % (db, x) for r in q("SELECT n1.nspname||'.'||c1.relname, n2.nspname||'.'||c2.relname FROM pg_constraint co "
                                         "JOIN pg_class c1 ON c1.oid=co.conrelid JOIN pg_namespace n1 ON n1.oid=c1.relnamespace "
                                         "JOIN pg_class c2 ON c2.oid=co.confrelid JOIN pg_namespace n2 ON n2.oid=c2.relnamespace "
                                         "WHERE co.contype='f'") for x in r} & set(uni)
sets["view_dep"] = {"%s.%s" % (db, r[0]) for r in q("SELECT DISTINCT tn.nspname||'.'||t.relname FROM pg_depend d JOIN pg_rewrite rw ON rw.oid=d.objid "
                                                    "JOIN pg_class v ON v.oid=rw.ev_class JOIN pg_class t ON t.oid=d.refobjid "
                                                    "JOIN pg_namespace tn ON tn.oid=t.relnamespace WHERE d.classid='pg_rewrite'::regclass "
                                                    "AND d.refclassid='pg_class'::regclass AND v.oid<>t.oid AND v.relkind IN ('v','m')")} & set(uni)
sets["trigger"] = {"%s.%s" % (db, r[0]) for r in q("SELECT DISTINCT n.nspname||'.'||c.relname FROM pg_trigger t JOIN pg_class c ON c.oid=t.tgrelid "
                                                   "JOIN pg_namespace n ON n.oid=c.relnamespace WHERE NOT t.tgisinternal")} & set(uni)
rel = q("SELECT many_collection, one_collection FROM directus_relations")
sets["directus_relation"] = {pub[x] for r in rel for x in r if x in pub}
perm_cols = [r[0] for r in q("SELECT column_name FROM information_schema.columns WHERE table_schema='public' AND table_name='directus_permissions' ORDER BY ordinal_position")]
sets["directus_permission"] = {pub[r[0]] for r in q("SELECT DISTINCT collection FROM directus_permissions") if r[0] in pub}
anchor_ok = uni.get(ANCHOR) == "r"
chosen, out = [], []
for s in STRATA:
    elig = sorted((h(k), k) for k in sets[s] if k not in chosen and k != ANCHOR)
    pick = [k for _, k in elig[:2]]
    status = "FULL"
    if len(pick) < 2:
        status = "PARTIAL_FILLED_FROM_UNIVERSE"
        rest = sorted((h(k), k) for k in uni if k not in chosen and k not in pick and k != ANCHOR)
        pick += [k for _, k in rest[:2 - len(pick)]]
    chosen += pick
    out.append({"stratum": s, "eligible": len(sets[s]), "eligible_sha256": digest(sets[s]), "status": status,
                "picked": [{"table": k, "sha256_seed_key": h(k), "relkind": uni[k]} for k in pick]})
cur.execute("ROLLBACK")
conn.close()
print(json.dumps({"seed": SEED, "formula": "sha256(utf8(SEED + key)), key = '<db>.<schema>.<table>', 2 nhỏ nhất/tầng, tầng theo thứ tự " + ",".join(STRATA),
                  "anchor": {"table": ANCHOR, "native_identity_ok": anchor_ok, "relkind": uni.get(ANCHOR)},
                  "snapshot": {"db": db, "role": role, "isolation": iso, "read_only": ro, "pg_snapshot": snap, "snapshot_utc": ts, "server": ver.split(",")[0]},
                  "universe": {"count": len(uni), "sha256": digest(uni)}, "directus_permissions_columns": perm_cols, "strata": out,
                  "pilot11": [ANCHOR] + chosen}, ensure_ascii=False, indent=1))
