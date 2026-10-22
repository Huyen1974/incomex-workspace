# GS-C0-COVERAGE-INVENTORY-20261022-05 · N3 · TÌNH TRẠNG CÁC CƠ CHẾ TỰ PHÁT HIỆN SẴN CÓ TRONG PG (chỉ-đọc) — dùng lại được
# Chạy như c0_pg_catalog.py:  ssh contabo 'timeout 120 docker exec -i incomex-claude-mcp python -I -B -' < c0_pg_health.py
# Chỉ cột trạng thái/thời điểm/mã của sổ quét (workflow_discovery_source_registry, workflow_scanner_registry,
# measurement_registry, trigger_guard_alerts, iu_qdrant_collection_registry) — không đọc nội dung nghiệp vụ.
import json, os, re, psycopg
OPT = "-c default_transaction_read_only=on -c statement_timeout=15000"
c = psycopg.connect(host=os.environ.get("PG_HOST", "postgres"), port=os.environ.get("PG_PORT", "5432"), user=os.environ["PG_USER_RO"],
                    password=os.environ["PG_PASSWORD_RO"], dbname="directus", connect_timeout=5, options=OPT, autocommit=True)
cur = c.cursor(); cur.execute("BEGIN ISOLATION LEVEL REPEATABLE READ READ ONLY")
o = {}
def q(sql):
    try:
        cur.execute(sql); return cur.fetchall()
    except Exception as e:
        cur.execute("ROLLBACK"); cur.execute("BEGIN ISOLATION LEVEL REPEATABLE READ READ ONLY"); return f"ERR:{type(e).__name__}"
o["discovery_sources"] = q("SELECT source_name, source_type, enabled, adapter_status, coverage_status, scannable_from_db, observed_count, "
                           "to_char(last_success_at,'YYYY-MM-DD\"T\"HH24:MI\"Z\"'), error_status IS NOT NULL FROM workflow_discovery_source_registry ORDER BY 1")
o["scanners"] = q("SELECT scanner_code, status, idempotent, to_char(last_run_at,'YYYY-MM-DD\"T\"HH24:MI\"Z\"'), "
                  "to_char(last_success_at,'YYYY-MM-DD\"T\"HH24:MI\"Z\"'), error_message IS NOT NULL FROM workflow_scanner_registry ORDER BY 1")
o["measurement_by_result"] = q("SELECT coalesce(last_result,'<null>'), enabled, count(*), to_char(max(last_run_at),'YYYY-MM-DD\"T\"HH24:MI\"Z\"') "
                               "FROM measurement_registry GROUP BY 1,2 ORDER BY 3 DESC")
o["trigger_guard_alerts"] = q("SELECT count(*), count(*) FILTER (WHERE resolved_at IS NULL), to_char(max(detected_at),'YYYY-MM-DD\"T\"HH24:MI\"Z\"') FROM trigger_guard_alerts")
o["trigger_guard_alerts_cols"] = q("SELECT string_agg(column_name, ',') FROM information_schema.columns WHERE table_name='trigger_guard_alerts'")
o["iu_qdrant_registry"] = q("SELECT collection_name, vector_dim, distance_metric, embedder_model_ref, status FROM iu_qdrant_collection_registry")
o["event_type_lanes"] = q("SELECT delivery_lane, active, count(*) FROM event_type_registry GROUP BY 1,2 ORDER BY 3 DESC")
o["meta_catalog_scan"] = q("SELECT count(*), count(last_scan_date), to_char(max(last_scan_date),'YYYY-MM-DD'), sum(CASE WHEN orphan_count>0 THEN 1 ELSE 0 END) FROM meta_catalog")
# F6 · cơ chế hàng đợi/sự kiện trong PG: chỉ ước lượng hàng + bộ đếm thống kê (chỉ báo hoạt động, không chứng minh giao nhận)
QT = ["event_outbox", "event_pending", "event_read", "event_subscription", "job_queue", "job_dead_letter", "queue_heartbeat",
      "entity_audit_queue", "iu_notification_event", "wf_orphan_remediation_queue", "inbox", "web_incomex_inbox"]
o["queue_tables"] = q("SELECT c.relname, c.reltuples::bigint, s.n_tup_ins, s.n_tup_upd, s.n_tup_del, "
                      "to_char(greatest(s.last_autoanalyze, s.last_analyze),'YYYY-MM-DD') FROM pg_class c "
                      "JOIN pg_namespace n ON n.oid=c.relnamespace AND n.nspname='public' "
                      "LEFT JOIN pg_stat_user_tables s ON s.relid=c.oid WHERE c.relname = ANY(ARRAY%s) ORDER BY 1" % QT)
o["stats_reset"] = q("SELECT to_char(stats_reset,'YYYY-MM-DD') FROM pg_stat_database WHERE datname=current_database()")
cur.execute("ROLLBACK")
# N3 · event trigger DDL làm gì (tĩnh: tạo trigger? ghi bảng nào? NOTIFY?) + kênh NOTIFY khai trong thân hàm — mỗi database
NOTIFY_RE = r"pg_notify\s*\(\s*'([a-z_]+)'"
o["ddl_event_fn"], o["notify_channels"] = {}, {}
for db in ("directus", "incomex_metadata"):
    cc = psycopg.connect(host=os.environ.get("PG_HOST", "postgres"), port=os.environ.get("PG_PORT", "5432"), user=os.environ["PG_USER_RO"],
                         password=os.environ["PG_PASSWORD_RO"], dbname=db, connect_timeout=5, options=OPT, autocommit=True)
    k = cc.cursor()
    k.execute("BEGIN ISOLATION LEVEL REPEATABLE READ READ ONLY")
    k.execute("SELECT p.proname, p.prosrc FROM pg_proc p JOIN pg_event_trigger e ON e.evtfoid = p.oid")
    for n, src in k.fetchall():
        o["ddl_event_fn"][db + ":" + n] = {"creates_trigger": bool(re.search(r"CREATE\s+TRIGGER", src, re.I)),
                                          "inserts": sorted(set(re.findall(r"INSERT\s+INTO\s+([a-z_.]+)", src, re.I))),
                                          "notify": bool(re.search(r"pg_notify|NOTIFY", src, re.I))}
    k.execute("SELECT n.nspname || '.' || p.proname, p.prosrc FROM pg_proc p JOIN pg_namespace n ON n.oid = p.pronamespace "
              "WHERE p.prosrc ~* 'pg_notify'")
    o["notify_channels"][db] = sorted({(fn, ch) for fn, src in k.fetchall() for ch in re.findall(NOTIFY_RE, src, re.I)})
    k.execute("ROLLBACK")
    cc.close()
print(json.dumps(o, ensure_ascii=False, default=str))
