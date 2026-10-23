# chỉ đọc: chạy bộ đọc cửa G2–G6/G9 của graph_cert sống + so với accepted_directory_parents; liệt kê loại unit systemd khác .service/.timer
import sys, os, json, re, glob
sys.path.insert(0, "/opt/incomex/graph-server/prod-v1/bin/refresh")
import graph_cert as GC
b = json.load(open(GC.BASELINE)); acc = set(b["accepted_directory_parents"])
d = GC.docker_read(); s = GC.systemd_read(); c = GC.cron_read(); n = GC.nginx_read(); o = GC.opt_read(); g = GC.git_read()
par = {"G2": ["docker:" + x for x in d["names_after"]], "G3": ["systemd:" + x for x in s["after"]],
       "G4": sorted({"cron:" + e[0].split("|")[0] for e in c["entries"]}), "G5": ["nginx:" + x[0] for x in n["servers"]],
       "G6": ["opt:" + e[0] for e in o["entries"] if e[1] == "d"], "G9": ["git:" + x for x in g["dirs"]]}
for k, xs in par.items():
    new = sorted(set(xs) - acc); gone = sorted(x for x in acc if x.split(":")[0] == xs[0].split(":")[0] and x not in xs) if xs else []
    print(k, len(xs), "NEW", new[:12], "GONE", gone[:12])
base = "/etc/systemd/system"
other = sorted(f for f in os.listdir(base) if os.path.isfile(os.path.join(base, f)) and not os.path.islink(os.path.join(base, f)) and not f.endswith((".service", ".timer")))
print("systemd other unit files:", other)
dropins = sorted(p for p in glob.glob(base + "/*.d/*.conf"))
print("drop-ins:", len(dropins), [p.replace(base + "/", "") for p in dropins][:40])
print("docker images", len(d["images"]), "containers", len(d["containers"]), "ok", d["ok"])
print("cron entries", len(c["entries"]), "errors", c["errors"])
print("nginx servers", len(n["servers"]), "edges", len(n["edges"]))
print("opt entries", len(o["entries"]), "ledger", len(o["ledger"] or []))
print("git head", g["head"][:12], "dirs", len(g["dirs"]))
repos = sorted(os.path.dirname(p) for p in glob.glob("/opt/incomex/*/.git") + glob.glob("/opt/incomex/*/*/.git") + glob.glob("/opt/*/.git"))
print("git repos depth<=2:", repos)
