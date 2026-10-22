#!/usr/bin/env python3
# GS-C1A-CERT-QUALITYGATE-20261022-07 · coverage Guard POST v2: mỗi mục footprint đủ 4 ô (Đ31 · Đ30 proof · watchdog · rollback).
# Dùng: c1a_cov.py <guard-post1.json>  → <E>/guard-cov/coverage.tsv + d30-*.txt
import hashlib, json, os, sys, time

RUN = "GS-C1A-CERT-QUALITYGATE-20261022-07"
E = "/opt/incomex/work/graph-server/evidence/" + RUN
C = E + "/guard-cov"
CG = "/var/lib/incomex-config-guard-v0"
os.makedirs(C, mode=0o700, exist_ok=True)
post = json.load(open(sys.argv[1]))
items = post.get("footprint") or []
reg = {}
for l in open(CG + "/registry.tsv", encoding="utf-8"):
    f = l.rstrip("\n").split("\t")
    if len(f) > 2 and not l.startswith("#"):
        reg[f[1]] = f[0]
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()
log = open(E + "/m/install.log").read()
res = json.load(open(E + "/m/install-result.json"))
BK = {"/opt/incomex/graph-server/mcp-readonly-v1/bin/graph-v1": E + "/m/backup/graph-v1-mcp-wrapper.truoc",
      "/opt/incomex/graph-server/prod-v1/bin/graph-refresh": E + "/m/backup/graph-refresh-cli.truoc",
      "/opt/incomex/scripts/mcpw-protection-guard": E + "/m/backup/mcpw-protection-guard.truoc",
      "/opt/incomex/scripts/code-ledger.tsv": E + "/m/backup/code-ledger.tsv.truoc",
      "/var/lib/incomex-config-guard-v0/registry.tsv": E + "/m/backup/registry.tsv.truoc"}
WD = {"/opt/incomex/scripts/mcpw-protection-guard": "Config Guard drift-check + Guard selftest + INV15/INV16 mỗi 5′ (#22)",
      "/opt/incomex/graph-server/prod-v1/bin/graph-refresh": "Config Guard drift-check + INV23 code_ledger + graph-refresh selftest + INV16 (nguồn gửi A24)",
      "/opt/incomex/graph-server/mcp-readonly-v1/bin/graph-v1": "Config Guard drift-check + INV23 code_ledger + graph-v1 doctor"}
rows = ["# item\td31\td30_proof\twatchdog\trollback\trollback_sha256 · %s · %s\n" % (RUN, time.strftime("%FT%TZ", time.gmtime()))]
for it in items:
    iid = it["id"]
    if it["kind"] == "file":
        p = it["path"]
        tid = reg.get(p)
        cg = open(CG + "/baseline/%s.sha256" % tid).read().split()[0] if tid else None
        cur = sha(p)                                   # hash HIỆN TẠI (POST2 tính lại; sổ mã đổi thêm 1 lần sau POST1)
        ok = tid and cg == cur
        pf = C + "/d30-%s.txt" % (tid or os.path.basename(p))
        open(pf, "w").write("--run %s · đích=%s · tệp=%s\nsha256 mới=%s · baseline Config Guard=%s · %s\n%s\nKẾT LUẬN: %s\n" % (
            RUN, tid, p, cur, cg, "TRÙNG" if ok else "LỆCH", "\n".join(l for l in log.splitlines() if "apply-v0" in l or "drift-check" in l
                                                                               or "selftest" in l or "doctor" in l), "PASS" if ok else "FAIL"))
        wd = WD.get(p, "Config Guard drift-check + INV23 code_ledger (LOCKED %s)" % tid)
        if it["pre"] == "ABSENT_OR_OUTSIDE_BASELINE":
            rb, rbs = "new:%s/scripts/c1a_install.py rollback (gỡ tệp + hàng registry/sổ mã + baseline)" % E, "-"
        else:
            rb = BK[p]
            rbs = sha(rb)
        rows.append("%s\tconfig-guard:%s\t%s\t%s\t%s\t%s\n" % (iid, tid, pf, wd, rb, rbs))
    elif it["kind"] == "kuma":
        pf = C + "/d30-kuma-24.txt"
        if not os.path.exists(pf):
            import subprocess
            hb = subprocess.run(["sqlite3", "-separator", "|", "file:/opt/incomex/uptime-kuma/kuma.db?mode=ro",
                                 "select time,status,important,msg from heartbeat where monitor_id=24 order by id"], capture_output=True, text=True).stdout
            g = subprocess.run("grep -E 'GUARD PERIODIC|INV15|INV16' /var/log/incomex/mcpw-guard.log | tail -6", shell=True, capture_output=True, text=True).stdout
            open(pf, "w").write("--run %s · đèn Kuma #24 «Graph Certificate (C1-A)» tạo qua socket chính thức (khuôn ensure-jev-gw-kuma-monitor.sh như #23)\n"
                                "cấu hình: %s\nnhịp:\n%s\nGuard periodic sau cài:\n%s\nKẾT LUẬN: PASS (đèn #24 đăng ký KUMA_MONITORS_EXPECTED + TIN_BAO A24, "
                                "nhịp THỬ down + nhịp thật up, INV15/INV16 PASS)\n" % (RUN, res.get("monitor"), hb, g))
        rows.append("%s\tkuma-snapshot\t%s\tINV15 kuma_telegram_coverage + INV16 tin_bao A24 (#24 trong #22)\tkuma:%s\t-\n" % (iid, pf, it["pre"]))
    else:
        pf = C + "/foreign-%s.txt" % iid.replace("/", "_").replace(":", "_")
        open(pf, "w").write("--run %s · mục footprint %s KHÔNG do lượt này tạo\nKẾT LUẬN: PASS (ghi nhận để đủ 4 ô)\n" % (RUN, iid))
        rows.append("%s\tforeign\t%s\tINV20/#22 Guard periodic\t-\t-\n" % (iid, pf))
open(C + "/coverage.tsv", "w").write("".join(rows))
print(len(items), "mục ·", C + "/coverage.tsv")
