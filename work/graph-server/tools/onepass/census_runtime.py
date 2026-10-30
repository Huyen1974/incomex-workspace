#!/usr/bin/env python3
# GS-ALL-SOURCE-ONEPASS-DISCOVERY-AUDIT-20261030-01 · CP1 census — chỉ đọc metadata, không in argv/env/nội dung tệp.
import json, os, subprocess, glob, hashlib, re, stat, time

def sh(cmd, timeout=60):
    try:
        p = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=timeout)
        return p.returncode, p.stdout, p.stderr[-300:]
    except Exception as e:
        return 99, "", repr(e)[:300]

out = {"at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "errors": []}
def err(where, rc, e):
    out["errors"].append({"where": where, "rc": rc, "stderr": e})

# ---- cron: mọi user + dòng comment kiểu lịch (đã tắt)
SCHED = re.compile(r'^\s*(?:#[A-Za-z0-9_\-]*\s*)?(@(reboot|hourly|daily|weekly|monthly|yearly|annually)|([\d\*/,\-]+\s+){4}[\d\*/,\-A-Za-z]+)\s+\S')
def cron_file(path, has_user_field):
    rows = []
    try:
        with open(path, errors="replace") as f:
            for i, line in enumerate(f, 1):
                s = line.rstrip("\n")
                if not s.strip():
                    continue
                if SCHED.match(s):
                    disabled = s.lstrip().startswith("#")
                    body = re.sub(r'^\s*#[A-Za-z0-9_\-]*\s*', '', s).strip()
                    tag = None
                    m = re.match(r'^#([A-Z0-9][A-Z0-9_\-]{6,})\s', s.strip())
                    if disabled and m:
                        tag = m.group(1)[:60]
                    rows.append({"line": i, "disabled": disabled, "disable_tag": tag,
                                 "sha12": hashlib.sha256(body.encode()).hexdigest()[:12]})
    except Exception as e:
        err("cron:" + path, 1, repr(e)[:200])
    return rows
cron = {}
for p in sorted(glob.glob("/var/spool/cron/crontabs/*")):
    cron["spool:" + os.path.basename(p)] = cron_file(p, False)
for p in ["/etc/crontab"] + sorted(glob.glob("/etc/cron.d/*")):
    if os.path.isfile(p):
        cron[p] = cron_file(p, True)
periodic = {}
for d in ["hourly", "daily", "weekly", "monthly"]:
    periodic[d] = sorted(os.path.basename(x) for x in glob.glob(f"/etc/cron.{d}/*"))
out["cron"] = {"files": {k: {"active": sum(not r["disabled"] for r in v), "disabled": sum(r["disabled"] for r in v),
                             "disable_tags": sorted({r["disable_tag"] for r in v if r["disable_tag"]})} for k, v in cron.items()},
               "periodic": periodic,
               "anacron": os.path.exists("/etc/anacrontab"),
               "at_jobs": len(glob.glob("/var/spool/cron/atjobs/*"))}
# user list with login shell (để biết user nào CÓ THỂ có crontab/systemd user)
users = []
for line in open("/etc/passwd"):
    u = line.split(":")
    if len(u) > 6 and not u[6].strip().endswith(("nologin", "false")):
        users.append(u[0])
out["login_users"] = users

# ---- systemd
rc, o, e = sh("systemctl list-unit-files --no-legend --no-pager --type=service,timer,socket,path,mount,automount 2>/dev/null")
uf = [l.split()[:2] for l in o.splitlines() if l.strip()]
out["systemd_unit_files"] = {"count": len(uf), "by_state": {}}
for n, s in uf:
    out["systemd_unit_files"]["by_state"][s] = out["systemd_unit_files"]["by_state"].get(s, 0) + 1
etc_units = sorted(os.path.basename(p) for p in glob.glob("/etc/systemd/system/*") if os.path.isfile(p) and not os.path.islink(p) and re.search(r'\.(service|timer|socket|path|mount)$', p))
out["systemd_etc_regular"] = etc_units
rc, o, e = sh("systemctl list-units --all --no-legend --no-pager --plain --type=service,timer,socket,path,scope 2>/dev/null")
active_units = [l.split()[0] for l in o.splitlines() if l.strip()]
out["systemd_loaded_units"] = len(active_units)
transient = sorted(os.path.basename(p) for p in glob.glob("/run/systemd/transient/*"))
out["systemd_transient"] = transient
rc, o, e = sh("systemctl list-timers --all --no-legend --no-pager 2>/dev/null")
out["systemd_timers"] = sorted({w for l in o.splitlines() for w in l.split() if w.endswith(".timer")})
# user systemd
rc, o, e = sh("loginctl list-users --no-legend 2>/dev/null")
out["linger_users"] = sorted(os.listdir("/var/lib/systemd/linger")) if os.path.isdir("/var/lib/systemd/linger") else []
uu = {}
for h in glob.glob("/home/*/.config/systemd/user") + glob.glob("/root/.config/systemd/user"):
    uu[h] = sorted(os.path.basename(x) for x in glob.glob(h + "/*") if re.search(r'\.(service|timer|socket|path)$', x))
out["user_systemd_dirs"] = uu
# systemd unit regular files outside /etc/systemd/system scanned scope (e.g. /lib local additions with incomex/hjw names)
out["systemd_lib_incomex_like"] = sorted(os.path.basename(p) for p in glob.glob("/lib/systemd/system/*") if re.search(r'(incomex|hjw|graph|hermes|dot|agent|kuma|guard|claude|codex|wf-)', os.path.basename(p)))

# ---- processes → owner class via cgroup (không in argv)
procs = {"docker": 0, "system_service": {}, "user_slice": {}, "other": {}, "kernel": 0}
for pid in os.listdir("/proc"):
    if not pid.isdigit():
        continue
    try:
        cg = open(f"/proc/{pid}/cgroup").read().strip()
        comm = open(f"/proc/{pid}/comm").read().strip()
    except Exception:
        continue
    path = cg.split("::")[-1] if "::" in cg else cg.split(":")[-1]
    if not path or path == "/":
        procs["kernel"] += 1; continue
    if "docker-" in path or "/docker/" in path or "containerd" in path and ".scope" in path:
        procs["docker"] += 1; continue
    m = re.search(r'system\.slice/([^/]+)', path)
    if m:
        procs["system_service"].setdefault(m.group(1), set()).add(comm); continue
    m = re.search(r'user\.slice/(.+)', path)
    if m:
        key = re.sub(r'session-\d+\.scope', 'session-N.scope', m.group(1))
        procs["user_slice"].setdefault(key, set()).add(comm); continue
    procs["other"].setdefault(path, set()).add(comm)
for k in ["system_service", "user_slice", "other"]:
    procs[k] = {a: sorted(b) for a, b in sorted(procs[k].items())}
out["processes"] = procs

# ---- listeners (TCP+UDP) — chỉ cổng + tên tiến trình
rc, o, e = sh("ss -H -lntup 2>/dev/null")
ls = []
for l in o.splitlines():
    f = l.split()
    if len(f) < 5:
        continue
    proto, local = f[0], f[4]
    pm = re.findall(r'\("([^"]+)"', l)
    ls.append({"proto": proto, "local": local, "proc": sorted(set(pm))})
out["listeners"] = ls

# ---- docker
def dj(cmd):
    rc, o, e = sh(cmd, 90)
    if rc != 0:
        err(cmd[:40], rc, e)
    return [json.loads(x) for x in o.splitlines() if x.strip().startswith("{")]
cont = dj("docker ps -a --no-trunc --format '{{json .}}'")
out["docker_containers"] = [{"name": c.get("Names"), "image": c.get("Image"), "state": c.get("State"),
                             "compose_project": (re.search(r'com\.docker\.compose\.project=([^,]+)', c.get("Labels", "")) or [None, None])[1]}
                            for c in cont]
out["docker_images"] = len(dj("docker images -a --format '{{json .}}'"))
vols = dj("docker volume ls --format '{{json .}}'")
out["docker_volumes"] = sorted(v.get("Name")[:64] for v in vols)
nets = dj("docker network ls --format '{{json .}}'")
out["docker_networks"] = sorted(n.get("Name") for n in nets)
# cron/process inside containers (chỉ tên tiến trình)
inner = {}
for c in cont:
    if c.get("State") != "running":
        continue
    rc, o, e = sh(f"docker top {c['Names']} -eo comm 2>/dev/null", 20)
    comms = sorted(set(x.strip() for x in o.splitlines()[1:] if x.strip()))
    flag = [x for x in comms if re.search(r'(cron|crond|supercronic|celery|rq|worker|beat|scheduler|pm2)', x)]
    inner[c["Names"]] = {"n_proc_names": len(comms), "scheduler_like": flag}
out["docker_inner"] = inner

# ---- git repos under /opt (depth ≤4) + deploy dirs without git
repos = []
rc, o, e = sh("timeout 50 find /opt -maxdepth 5 \\( -name node_modules -o -name .venv -o -name venv -o -name __pycache__ \\) -prune -o -name .git -print 2>/dev/null", 60)
for g in sorted(o.split()):
    top = os.path.dirname(g)
    rc2, h, _ = sh(f"git -C '{top}' rev-parse --short=8 HEAD 2>/dev/null", 10)
    rc3, st, _ = sh(f"git --no-optional-locks -C '{top}' status --porcelain=v1 --untracked-files=no 2>/dev/null | wc -l", 20)
    repos.append({"path": top, "head": h.strip() or None, "dirty_tracked": int(st.strip() or 0) if rc3 == 0 else None})
out["git_repos"] = repos
# NB: git status có thể ghi .git/index (bẫy CONN-REPAIR) — dùng --no-optional-locks
out["git_note"] = "git --no-optional-locks (không ghi .git/index)"
# top-level of /opt and /opt/incomex
out["opt_l1"] = sorted(os.listdir("/opt"))
out["opt_incomex_l1"] = sorted(os.listdir("/opt/incomex"))
out["deploys"] = sorted(os.listdir("/opt/incomex/deploys")) if os.path.isdir("/opt/incomex/deploys") else []

# ---- executable scripts outside DOT/ledger: /usr/local/{bin,sbin}, /root/*.sh, /opt/incomex/scripts/**
def execs(globpat):
    r = []
    for p in glob.glob(globpat, recursive=True):
        try:
            st_ = os.stat(p)
        except Exception:
            continue
        if os.path.isfile(p) and st_.st_mode & 0o111:
            r.append(p)
    return sorted(r)
out["exec_usr_local"] = execs("/usr/local/bin/*") + execs("/usr/local/sbin/*")
out["exec_root_home"] = execs("/root/*")
out["exec_opt_incomex_scripts_count"] = len(execs("/opt/incomex/scripts/**/*"))
out["exec_opt_incomex_scripts_dirs"] = sorted({os.path.dirname(p) for p in execs("/opt/incomex/scripts/**/*")})[:200]
ledger = "/opt/incomex/code-ledger.tsv"
led_paths = set()
for cand in [ledger] + glob.glob("/opt/incomex/**/code-ledger.tsv", recursive=False):
    if os.path.isfile(cand):
        for l in open(cand, errors="replace"):
            p = l.split("\t")[0].strip()
            if p.startswith("/"):
                led_paths.add(p)
        out["code_ledger_file"] = cand
out["code_ledger_paths"] = len(led_paths)
def in_ledger(p):
    return any(p == x or p.startswith(x.rstrip("/") + "/") for x in led_paths)
out["usr_local_not_in_ledger"] = [p for p in out["exec_usr_local"] if not in_ledger(p)]
out["root_home_not_in_ledger"] = [p for p in out["exec_root_home"] if not in_ledger(p)]

# ---- nginx (không in đường/location — chỉ đếm + băm)
rc, o, e = sh("docker exec incomex-nginx sh -c 'ls /etc/nginx/conf.d/ 2>/dev/null; nginx -T 2>/dev/null | grep -cE \"^\\s*location\"; nginx -T 2>/dev/null | grep -cE \"^\\s*server_name\"; nginx -T 2>/dev/null | grep -cE \"proxy_pass\"'", 30)
out["nginx_probe"] = {"rc": rc, "lines": o.splitlines()[-40:]}

# ---- queues / outbox / local DB files (metadata only)
q = []
for pat in ["/opt/incomex/**/*.sqlite", "/opt/incomex/**/*.sqlite3", "/opt/incomex/**/*.db", "/var/lib/hjw-control/*", "/opt/incomex/**/queue*"]:
    for p in glob.glob(pat, recursive=True):
        if "/node_modules/" in p or "/.git/" in p:
            continue
        try:
            s = os.stat(p)
        except Exception:
            continue
        if os.path.isfile(p):
            q.append({"path": p, "bytes": s.st_size, "mtime": time.strftime("%Y-%m-%dT%H:%MZ", time.gmtime(s.st_mtime))})
out["local_stores"] = sorted(q, key=lambda x: x["path"])[:300]

# ---- rclone remotes (tên) + gh/gcloud presence (dấu vết phụ thuộc ngoài)
rc, o, e = sh("rclone listremotes 2>/dev/null", 20)
out["rclone_remotes"] = o.split()
out["ext_tools"] = {t: bool(sh(f"command -v {t}")[1].strip()) for t in ["gh", "gcloud", "rclone", "lark-cli", "psql"]}
print(json.dumps(out, ensure_ascii=False, default=list))
