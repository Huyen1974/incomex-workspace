set -u; umask 077
R=GS-COV2-P-SCHEMA-READONLY-USAGE-METERS-20261030-01; W=/root/incomex-config-changes/$R-ev
D=/opt/workflow/postgres18/18/docker; F=$D/postgresql.auto.conf; B=$W/postgresql.auto.conf.truoc; OLD=0874e665ecf5c0a6135a73158ea1b71a959dafb809574810da5c9cc28c0c63ed
q(){ docker exec -i postgres psql -XAtq -v ON_ERROR_STOP=1 -F'|' -U workflow_admin -d postgres -c "$1" </dev/null; }
facts(){ q "select setting,source,coalesce(sourcefile,'-'),pending_restart from pg_settings where name='track_functions'"; q "select count(*) from pg_file_settings where error is not null"; }
state(){ echo "$1 :: $(facts | tr '\n' ' ') :: file=$(sha256sum $F | cut -c1-16) $(stat -c '%u:%g %a %s' $F)"; }
expect_old(){ [ "$(sha256sum $F | cut -d' ' -f1)" = "$OLD" ] && [ "$(q "select setting||'|'||source from pg_settings where name='track_functions'")" = "none|default" ] && [ "$(q "select count(*) from pg_file_settings where error is not null")" = 0 ]; }
expect_new(){ [ "$(q "select setting||'|'||source||'|'||sourcefile||'|'||pending_restart from pg_settings where name='track_functions'")" = "pl|configuration file|/var/lib/postgresql/18/docker/postgresql.auto.conf|false" ] && [ "$(q "select count(*) from pg_file_settings where error is not null")" = 0 ]; }
restore(){ cp -a $B $F.gsp2tmp && mv -f $F.gsp2tmp $F && q "select pg_reload_conf()" >/dev/null; sleep 2; }
apply(){ q "alter system set track_functions = 'pl'" >/dev/null && q "select pg_reload_conf()" >/dev/null; sleep 2; }
load(){ echo "$1 load=$(cut -d' ' -f1-3 /proc/loadavg) mem_avail_mb=$(awk '/MemAvailable/{print int($2/1024)}' /proc/meminfo) xact=$(q "select sum(xact_commit) from pg_stat_database") pgcpu=$(docker stats --no-stream --format '{{.CPUPerc}} {{.MemUsage}}' postgres </dev/null)"; }
# 0 chạy thử mọi bộ kiểm trên trạng thái hiện tại TRƯỚC khi đổi
state PRE; expect_old || { echo "P2_NOT_APPLIED: expect_old sai trên trạng thái gốc"; exit 31; }
[ "$(docker exec postgres sha256sum /var/lib/postgresql/18/docker/postgresql.auto.conf </dev/null | cut -d' ' -f1)" = "$(sha256sum $F | cut -d' ' -f1)" ] || { echo "P2_NOT_APPLIED: đường host ≠ tệp PG"; exit 32; }
cp -a $F $B; [ "$(sha256sum $B | cut -d' ' -f1)" = "$OLD" ] || { echo "P2_NOT_APPLIED: sao lưu sai"; exit 33; }
expect_new && { echo "bộ kiểm expect_new sai dương"; exit 34; }; echo "checker_negative_ok"
load LOAD_PRE
# 1 áp
apply; state APPLY1; if ! expect_new; then restore; state ROLLBACK_AUTO; echo P2_FAIL_APPLY1; exit 35; fi; S1=$(sha256sum $F | cut -d' ' -f1)
# 2 diễn tập lùi thật: ghi lại đúng byte + reload (không ALTER SYSTEM RESET)
restore; state DRILL_BACK; expect_old || { echo "P2_FAIL_DRILL: lùi không về đúng"; exit 36; }; echo "drill_exact_ok sha=$(sha256sum $F | cut -c1-16) mtime_giu=$(stat -c %Y $F)=$(stat -c %Y $B)"
# 3 áp lại
apply; state APPLY2; if ! expect_new || [ "$(sha256sum $F | cut -d' ' -f1)" != "$S1" ]; then restore; state ROLLBACK_AUTO; echo P2_FAIL_APPLY2; exit 37; fi
cp -a $F $W/postgresql.auto.conf.sau; echo "bytes_after:"; sed -n '3,$p' $F
load LOAD_POST
ls $D | grep -c gsp2tmp
docker logs --since 5m postgres </dev/null 2>&1 | grep -E 'track_functions|FATAL|PANIC|ERROR.*conf|reload' | tail -6 | cut -c1-160
