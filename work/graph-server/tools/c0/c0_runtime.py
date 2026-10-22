#!/usr/bin/env python3
# GS-C0-COVERAGE-INVENTORY-20261022-05 · F5/F6/F7/F10 · KIỂM KÊ HẠ TẦNG + BẢO VỆ + DOT CHỈ-ĐỌC — dùng lại được
# Chạy trên host VPS qua stdin, không ghi tệp:  ssh contabo 'timeout 300 python3 -I -B -' < c0_runtime.py > rt.json
# Chỉ lệnh đọc: docker ps/images/volume/network/inspect(.Mounts,.Config.Image), systemctl list/show(ExecStart path),
# crontab -l + /etc/cron.d (lịch + đường script đầu tiên), nginx -T (server_name/upstream host:port, KHÔNG in path
# location — có route path-secret), ss -ltn, đọc sổ Config Guard/Guard/Kuma/storage/code-ledger/DOT.
# Lọc bí mật tại nguồn: không Environment, không giá trị header, không dòng lệnh đầy đủ.
# Đầu ra JSON {"summary": số đếm, "detail": danh sách tên (chỉ lưu Mac riêng)}.
import json, os, re, subprocess

SUM, DET = {}, {}
SECRETISH = re.compile(r"[A-Za-z0-9_\-]{24,}")


def sh(cmd, timeout=60):
    try:
        p = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=timeout)
        return p.returncode, p.stdout
    except subprocess.TimeoutExpired:
        return 124, ""


def lines(cmd, timeout=60):
    rc, out = sh(cmd, timeout)
    return rc, [l for l in out.splitlines() if l.strip()]


def mask(s):
    return SECRETISH.sub("<long>", s)


# ---------- F6 docker ----------
rc, ps = lines("docker ps -a --format '{{.Names}}|{{.Image}}|{{.State}}|{{.Ports}}'")
cont = [dict(zip(("name", "image", "state", "ports"), l.split("|", 3))) for l in ps]
SUM["docker_containers"] = {"total": len(cont), "running": sum(c["state"] == "running" for c in cont)}
for c in cont:
    _, m = sh(f"docker inspect --format '{{{{range .Mounts}}}}{{{{.Type}}}}:{{{{.Source}}}}->{{{{.Destination}}}}\n{{{{end}}}}' {c['name']}")
    c["mounts"] = [mask(x) for x in m.splitlines() if x.strip()]
    _, nets = sh(f"docker inspect --format '{{{{range $k,$v := .NetworkSettings.Networks}}}}{{{{$k}}}} {{{{end}}}}' {c['name']}")
    c["networks"] = nets.split()
DET["containers"] = cont
_, imgs = lines("docker images --format '{{.Repository}}:{{.Tag}}|{{.ID}}'")
SUM["docker_images"] = len(imgs)
DET["images"] = imgs
_, vols = lines("docker volume ls -q")
used = {m.split(":", 1)[1].split("->")[0] for c in cont for m in c["mounts"] if m.startswith("volume:")}
SUM["docker_volumes"] = {"total": len(vols), "anonymous_64hex": sum(bool(re.fullmatch(r"[0-9a-f]{64}", v)) for v in vols)}
DET["volumes"] = vols
_, nets = lines("docker network ls --format '{{.Name}}|{{.Driver}}'")
SUM["docker_networks"] = len(nets)
DET["networks"] = nets
pub = sorted({p for c in cont for p in re.findall(r"(?:[\d.]+|\[::\]):(\d+)->", c["ports"])}, key=int)
SUM["docker_published_ports"] = len(pub)

# ---------- F6 systemd ----------
_, units = lines("systemctl list-unit-files --type=service,timer --no-legend --plain")
uf = [l.split()[:2] for l in units]
SUM["systemd_unit_files"] = {"service": sum(u[0].endswith(".service") for u in uf), "timer": sum(u[0].endswith(".timer") for u in uf)}
_, timers = lines("systemctl list-timers --all --no-legend --plain")
tlist = []
for l in timers:
    parts = l.split()
    t = [p for p in parts if p.endswith(".timer")]
    s = [p for p in parts if p.endswith(".service")]
    if t:
        tlist.append({"timer": t[0], "activates": s[0] if s else None})
custom_svc = sorted({u[0] for u in uf if u[0].endswith(".service") and os.path.exists(f"/etc/systemd/system/{u[0]}")})
svc_exec = {}
for s in custom_svc + [t["activates"] for t in tlist if t["activates"]]:
    if s in svc_exec:
        continue
    _, ex = sh(f"systemctl show {s} -p ExecStart --value")
    paths = re.findall(r"path=([^ ;]+)", ex)
    argv0 = re.findall(r"argv\[\]=([^ ;]+)(?: ([^ ;]+))?", ex)
    script = None
    for a, b in argv0:
        script = b if b and b.startswith("/") and re.search(r"(python|bash|sh)\d*$", a) else a
    svc_exec[s] = {"exec": paths[0] if paths else None, "script": script}
_, active = lines("systemctl list-units --type=service --state=running --no-legend --plain")
SUM["systemd_custom_services_etc"] = len(custom_svc)
SUM["systemd_running_services"] = len(active)
SUM["systemd_timers"] = len(tlist)
DET["timers"] = tlist
DET["custom_services"] = {s: svc_exec.get(s) for s in custom_svc}
DET["timer_service_exec"] = {t["activates"]: svc_exec.get(t["activates"]) for t in tlist if t["activates"]}

# ---------- F6 cron (lịch + đường script đầu, không in tham số) ----------
cron = []
for src, cmd in [("root", "crontab -l"), ("etc_crontab", "cat /etc/crontab")] + \
        [(f"cron.d/{f}", f"cat /etc/cron.d/{f}") for f in sorted(os.listdir("/etc/cron.d")) if not f.startswith(".")]:
    _, ls_ = lines(cmd)
    for l in ls_:
        if l.lstrip().startswith("#") or re.match(r"^\s*[A-Z_]+=", l):
            continue
        f = l.split()
        if len(f) < 6:
            continue
        sched = " ".join(f[:5]) if not f[0].startswith("@") else f[0]
        rest = f[5:] if not f[0].startswith("@") else f[1:]
        if src != "root" and rest and re.fullmatch(r"[a-z_][a-z0-9_-]*", rest[0]):
            rest = rest[1:]  # cột user
        paths = [x for x in rest if x.startswith("/")]
        cron.append({"src": src, "schedule": sched, "first_path": mask(paths[0]) if paths else (rest[0] if rest else None)})
for d in ("/etc/cron.hourly", "/etc/cron.daily", "/etc/cron.weekly", "/etc/cron.monthly"):
    if os.path.isdir(d):
        for f in sorted(os.listdir(d)):
            if not f.startswith("."):
                cron.append({"src": d, "schedule": d.rsplit(".", 1)[1], "first_path": f"{d}/{f}"})
SUM["cron_entries"] = len(cron)
SUM["cron_entries_by_src"] = {}
for c in cron:
    k = c["src"].split("/")[0]
    SUM["cron_entries_by_src"][k] = SUM["cron_entries_by_src"].get(k, 0) + 1
DET["cron"] = cron

# ---------- F6 nginx (server_name + upstream host:port; KHÔNG in path location) ----------
ngc = [c["name"] for c in cont if c["name"] == "incomex-nginx" or c["image"].startswith("nginx")]
rc, ng = sh(f"timeout 25 docker exec {ngc[0]} nginx -T 2>/dev/null", 30) if ngc else (127, "")
servers, locs, ups, pps = [], 0, set(), set()
for l in ng.splitlines():
    s = l.strip()
    if s.startswith("server_name "):
        servers.append(s[len("server_name "):].rstrip(";"))
    elif s.startswith("location "):
        locs += 1
    elif s.startswith("upstream "):
        ups.add(s.split()[1])
    elif s.startswith("proxy_pass "):
        m = re.match(r"proxy_pass\s+https?://([^/;\s]+)", s)
        if m:
            pps.add(m.group(1))
SUM["nginx"] = {"server_name_directives": len(servers), "distinct_server_names": len({x for s in servers for x in s.split()}),
                "location_blocks": locs, "upstream_blocks": len(ups), "distinct_proxy_targets": len(pps), "nginx_T_rc": rc}
DET["nginx"] = {"server_names": sorted({x for s in servers for x in s.split()}), "upstreams": sorted(ups),
                "proxy_targets": sorted(pps)}

# ---------- F6 listening ports ----------
_, ss = lines("ss -ltnH")
ports = sorted({l.split()[3] for l in ss})
SUM["listening_tcp_sockets"] = len(ports)
DET["listening"] = ports

# ---------- F6 queue / pub-sub / worker hiện có (chỉ metadata) ----------
qk = re.compile(r"redis|rabbit|kafka|nats|mosquitto|celery|rq-|bull|pubsub|queue", re.I)
SUM["queue_like_containers"] = [c["name"] + "|" + c["image"] for c in cont if qk.search(c["name"] + c["image"])]
SUM["queue_like_units"] = sorted(u[0] for u in uf if qk.search(u[0]))
_, procs = lines("ps -eo comm,args --no-headers")
SUM["queue_like_processes"] = sorted({p.split()[0] for p in procs if qk.search(p.split()[0])})
# bộ nghe PG NOTIFY trong mã đang chạy (tĩnh, chỉ tên tệp + số dòng)
_, lst = lines(r"grep -rlE --include='*.py' --include='*.ts' --include='*.js' 'LISTEN [a-z_]+|add_notify_handler|\.notifies\(|pg_notify' "
               "/opt/incomex/docker/agent-data-repo /opt/incomex/claude-mcp /opt/incomex/claude-kb /opt/incomex/lark-client "
               "/opt/incomex/scripts /opt/incomex/dot/bin 2>/dev/null | grep -v node_modules | grep -v '/\\.git/'", 60)
DET["pg_listen_notify_code_files"] = lst
SUM["pg_listen_notify_code_files"] = len(lst)

# ---------- F5 code trees (theo mount container + repo đã biết) ----------
known = ["/opt/incomex/docker/agent-data-repo", "/opt/incomex/claude-kb", "/opt/incomex/claude-mcp",
         "/opt/incomex/lark-client", "/opt/incomex/deploys/nuxt-output-n4", "/opt/incomex/docker/nuxt-repo/web"]
cand = set(known)
for c in cont:
    for m in c["mounts"]:
        if m.startswith("bind:"):
            srcp = m.split(":", 1)[1].split("->")[0]
            if srcp.startswith("/opt/incomex/") and os.path.isdir(srcp):
                cand.add(srcp)
for s in svc_exec.values():
    if s and s.get("script") and s["script"].startswith("/opt/incomex"):
        cand.add(os.path.dirname(s["script"]))
EXT = {".py": "python", ".ts": "ts", ".vue": "vue", ".js": "js", ".mjs": "js", ".sh": "shell", ".sql": "sql", ".go": "go"}
trees = {}
for root in sorted(cand):
    if not os.path.isdir(root):
        continue
    cnt, n = {}, 0
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if d not in ("node_modules", ".git", "__pycache__", ".nuxt", "venv", ".venv", "site-packages")]
        for f in fn:
            e = os.path.splitext(f)[1]
            if e in EXT:
                cnt[EXT[e]] = cnt.get(EXT[e], 0) + 1
            n += 1
            if n > 200000:
                break
    if sum(cnt.values()):
        trees[root] = cnt
DET["code_trees"] = trees
SUM["code_trees_with_source"] = len(trees)

# ---------- F7 Config Guard / Guard / Kuma / storage / code-ledger ----------
def rd(p):
    try:
        return open(p, encoding="utf-8", errors="replace").read()
    except Exception as e:
        return None
cfg = rd("/var/lib/incomex-config-guard-v0/registry.tsv")
if cfg is None:
    SUM["config_guard_targets"] = "NO_ACCESS_OR_MISSING"
else:
    rows = [l.split("\t") for l in cfg.splitlines() if not l.startswith("#") and len(l.split("\t")) >= 3 and l.split("\t")[1].startswith("/")]
    SUM["config_guard_targets"] = len(rows)
    DET["config_guard_targets"] = [r[:3] for r in rows]
    SUM["config_guard_by_class"] = {}
    for r in rows:
        SUM["config_guard_by_class"][r[2]] = SUM["config_guard_by_class"].get(r[2], 0) + 1
bd = rd("/opt/incomex/logs/bang-den.json")
try:
    bdj = json.loads(bd)
    SUM["bang_den_top_keys"] = sorted(bdj.keys()) if isinstance(bdj, dict) else type(bdj).__name__
    DET["bang_den_shape"] = {k: (type(v).__name__, len(v) if hasattr(v, "__len__") else None) for k, v in bdj.items()} if isinstance(bdj, dict) else None
except Exception:
    SUM["bang_den_top_keys"] = "UNPARSEABLE"
st = rd("/opt/incomex/scripts/storage-registry.tsv")
SUM["storage_registry_rows"] = len([l for l in (st or "").splitlines() if l.strip() and not l.startswith("#")])
cl = rd("/opt/incomex/scripts/code-ledger.tsv")
clr = [l.split("\t") for l in (cl or "").splitlines() if l.strip() and not l.startswith("#")]
SUM["code_ledger_rows"] = len(clr)
SUM["code_ledger_by_status"] = {}
for r in clr:
    k = r[1] if len(r) > 1 else "?"
    SUM["code_ledger_by_status"][k] = SUM["code_ledger_by_status"].get(k, 0) + 1
# Guard: danh sách invariant khai trong mã (tên INVn) + trạng thái lượt periodic gần nhất
gsrc = rd("/opt/incomex/scripts/mcpw-protection-guard") or ""
SUM["guard_invariant_ids_in_code"] = sorted({m for m in re.findall(r"\bINV\d+[A-Z_0-9]*\b", gsrc)}, key=lambda x: int(re.match(r"INV(\d+)", x).group(1)))
_, gst = lines("ls -1 /var/lib/incomex-mcpw-guard 2>/dev/null")
DET["guard_state_files"] = gst
# Kuma: số monitor (sqlite mode=ro)
_, km = sh("ls -1 /opt/incomex/uptime-kuma 2>/dev/null")
DET["kuma_dir"] = km.split()
_, kq = sh("python3 -c \"import sqlite3;c=sqlite3.connect('file:/opt/incomex/uptime-kuma/kuma.db?mode=ro',uri=True);"
           "print(c.execute('select count(*), sum(active) from monitor').fetchone());"
           "print([r for r in c.execute('select type,count(*) from monitor group by 1')])\" 2>&1")
SUM["kuma_monitors"] = kq.strip()

# ---------- F10 DOT: sổ tsv ↔ bin ↔ (PG dot_tools ở c0_pg_catalog) ----------
tsv = rd("/opt/incomex/dot/00-SO-DOT.tsv") or ""
trows = [l.split("\t") for l in tsv.splitlines() if l.strip() and not l.startswith("#")]
SUM["dot_tsv_rows"] = len(trows)
DET["dot_tsv_first_cols"] = [r[:3] for r in trows]
bins = sorted(f for f in os.listdir("/opt/incomex/dot/bin") if not f.startswith(".")) if os.path.isdir("/opt/incomex/dot/bin") else []
SUM["dot_bin_files"] = len(bins)
DET["dot_bin"] = bins
hdr = {"CHAM": 0, "AI GOI": 0}
for b in bins:
    p = os.path.join("/opt/incomex/dot/bin", b)
    try:
        head = open(p, encoding="utf-8", errors="replace").read(4000)
    except Exception:
        continue
    for k in hdr:
        if re.search(rf"^#\s*{k}\s*:", head, re.M | re.I):
            hdr[k] += 1
SUM["dot_bin_headers"] = hdr

print(json.dumps({"summary": SUM, "detail": DET}, ensure_ascii=False, default=str))
