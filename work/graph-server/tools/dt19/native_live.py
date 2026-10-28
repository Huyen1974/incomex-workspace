import json,subprocess,os,re,hashlib,datetime
def sh(c): return subprocess.run(c,shell=True,capture_output=True,text=True,timeout=60).stdout
out={"at":datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")}
# docker
names=[l.strip() for l in sh("docker ps -a --format '{{.Names}}'").splitlines() if l.strip()]
out["docker_all"]=sorted(names)
out["docker"]=sorted("docker:container:"+n for n in names if not n.startswith("workspace-job-") and not n.startswith("incomex-graph-v1-rc-"))
# listeners
ls=set()
for l in sh("ss -ltnH").splitlines():
    p=l.split()
    if len(p)>=4: ls.add("net:listen:"+p[3])
out["listen"]=sorted(ls)
# systemd unit files /etc/systemd/system regular files
u=[]
for f in os.listdir("/etc/systemd/system"):
    pth="/etc/systemd/system/"+f
    if os.path.isfile(pth) and not os.path.islink(pth) and re.search(r"\.(service|timer|socket|path|mount)$",f): u.append(f)
out["unit_files"]=sorted(u)
# git repos depth<=3
g=sh("find /opt/incomex -maxdepth 4 -name .git 2>/dev/null").split()
out["git"]=sorted("git:repo:"+os.path.dirname(x) for x in g)
# opt entries
out["opt"]=sorted(["/opt/"+x for x in os.listdir("/opt")]+["/opt/incomex/"+x for x in os.listdir("/opt/incomex")])
# cron lines
n=0
for f in sh("ls /var/spool/cron/crontabs/* /etc/cron.d/* /etc/crontab 2>/dev/null").split():
    try:
        for l in open(f,errors="ignore"):
            s=l.strip()
            if s and not s.startswith("#") and not re.match(r"^[A-Z_]+=",s): n+=1
    except Exception: pass
out["cron_lines"]=n
out["sha"]={k:hashlib.sha256("\n".join(v).encode()).hexdigest()[:16] for k,v in out.items() if isinstance(v,list)}
print(json.dumps(out))
