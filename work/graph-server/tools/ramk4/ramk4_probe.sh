#!/usr/bin/env bash
# GS-RAM-K4-PREFLIGHT-READONLY-20261029-22 · bộ đo CHỈ ĐỌC (chạy: ssh contabo 'bash -s' < ramk4_probe.sh > out.txt)
# Chỉ đọc /proc, /sys/fs/cgroup, docker ps/stats/inspect, tệp giấy Graph và registry Config Guard.
# Không ghi tệp, không restart/kill, không drop cache, không in biến môi trường hay argv đầy đủ.
set -u
echo "== T $(date -u +%FT%TZ)"
free -k
grep -E 'MemTotal|MemAvailable|^Cached|Shmem:|SReclaimable|SwapTotal|SwapFree|AnonPages' /proc/meminfo
cat /proc/pressure/memory 2>&1
vmstat 1 3
echo "== cgroup theo container (MiB)"
for d in /sys/fs/cgroup/system.slice/docker-*.scope; do
  id=$(basename "$d" | sed 's/docker-//;s/.scope//'); n=$(docker inspect -f '{{.Name}}' "$id" 2>/dev/null)
  echo "$n cur=$(($(cat $d/memory.current)/1048576)) anon=$(awk '/^anon /{print int($2/1048576)}' $d/memory.stat) swap=$(($(cat $d/memory.swap.current)/1048576)) max=$(cat $d/memory.max) peak=$(($(cat $d/memory.peak 2>/dev/null || echo 0)/1048576))"
done | sort -t= -k2 -rn
for d in /sys/fs/cgroup/system.slice/*.service; do c=$(($(cat $d/memory.current 2>/dev/null || echo 0)/1048576)); [ "$c" -gt 80 ] && echo "$(basename $d) cur=$c"; done
echo "== tiến trình RSS lớn (tên lệnh, không argv)"
ps -eo pid,ppid,rss,etimes,comm --sort=-rss | head -20
echo "== worker agent-data (PSS kB)"
P=$(docker inspect -f '{{.State.Pid}}' incomex-agent-data)
for c in $(ps --ppid "$P" -o pid= ; for q in $(ps --ppid "$P" -o pid=); do ps --ppid "$q" -o pid=; done); do
  awk -v p="$c" '/^Pss:/{s=$2}END{print p, "pss_kB=" s}' /proc/$c/smaps_rollup 2>/dev/null
done
grep -n 'AGENT_DATA_WORKERS' /opt/incomex/docker/docker-compose.yml
echo "== Graph: lượt làm mới gần nhất + giấy"
journalctl -u incomex-graph-refresh.service --since '-26h' --no-pager | grep -E 'RUN ' | tail -3
python3 - <<'PY'
import json
R='/opt/incomex/graph-server/prod-v1/state/refresh'
l=json.load(open(R+'/last.json')); print('last', l['at'], l['result'], l.get('failed'))
c=json.load(open(R+'/cert/current.json')); print('cert generated_at', c['generated_at'], 'catalog', c['catalog_sha256'][:16], 'engine', c['engine_sha256'][:16])
for k in ('infra:container','infra:listener','infra:unit','infra:git'):
    s=c['cells'][k]['source']; print(k, c['cells'][k]['status'], s.get('objects_count'), s.get('objects_sha256','')[:16])
src=json.load(open('/opt/incomex/graph-server/prod-v1/manifest/refresh-sources.json'))
f=src['code']['repos']['nuxt-web']['loaded']['artifact_fingerprint']; print('nuxt loaded nitro_json', f['nitro_json'][:16], 'build_json', f['cweb_owned_build_json'][:16])
PY
D=/opt/incomex/deploys/nuxt-output-n4; echo "nuxt live $(sha256sum < $D/nitro.json | cut -c1-16) $(sha256sum < $D/cweb-owned-build.json | cut -c1-16)"
echo "== wrapper/baseline Config Guard"
G=/var/lib/incomex-config-guard-v0
for t in graph-v1-mcp-wrapper graph-v1-cli graph-refresh-cli graph-refresh-lib-cert vpsup-docker-compose; do
  p=$(awk -F'\t' -v t="$t" '$1==t{print $2}' $G/registry.tsv)
  echo "$t live=$(sha256sum < "$p" | cut -c1-16) baseline=$(cut -c1-16 $G/baseline/$t.sha256 2>/dev/null)"
done
ps -eo rss,comm | awk '$2~/graph-v1|neo4j-mcp/'
