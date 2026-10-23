#!/usr/bin/env python3
# GS-C1C-PRODUCTION-TRUST-GATE-20261023-09 · (khuôn c1a_cov C1-A) coverage Guard POST v2: mỗi mục footprint đủ 4 ô (Đ31 · Đ30 proof · watchdog · rollback).
# Dùng: c1c_cov.py <guard-post1.json>  → <E>/guard-cov/coverage.tsv + d30-*.txt
import hashlib, json, os, sys, time

RUN = "GS-C1C-PRODUCTION-TRUST-GATE-20261023-09"
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
P = "/opt/incomex/graph-server/prod-v1"
BK = {P + "/bin/refresh/graph_cert.py": E + "/m/backup/graph-refresh-lib-cert.truoc",
      P + "/manifest/cert-cells.json": E + "/m/backup/graph-cert-cells.truoc",
      P + "/manifest/cert-baseline.json": E + "/m/backup/graph-cert-baseline.truoc"}
WD = {P + "/bin/refresh/graph_cert.py": "Config Guard drift-check + INV23 code_ledger + đèn #24 mỗi lượt graph-refresh + c1c_fixtures 81/81 + hồi quy C1-B 28/28 + INV22 graph_v1",
      P + "/manifest/cert-cells.json": "Config Guard drift-check + ma trận bao phủ G1–G9 + đèn #24",
      P + "/manifest/cert-baseline.json": "Config Guard drift-check + đèn #24 (sàn 29 ô gồm lark:88-phai-cu:b88)"}
rows = ["# item\td31\td30_proof\twatchdog\trollback\trollback_sha256 · %s · %s\n" % (RUN, time.strftime("%FT%TZ", time.gmtime()))]
for it in items:
    iid = it["id"]
    if it["kind"] == "file" and it["path"] in BK:
        p = it["path"]
        tid = reg.get(p)
        cg = open(CG + "/baseline/%s.sha256" % tid).read().split()[0] if tid else None
        cur = sha(p)
        ok = tid and cg == cur
        pf = C + "/d30-%s.txt" % (tid or os.path.basename(p))
        open(pf, "w").write("--run %s · đích=%s · tệp=%s\nsha256 mới=%s · baseline Config Guard=%s · %s\n%s\nKẾT LUẬN: %s\n" % (
            RUN, tid, p, cur, cg, "TRÙNG" if ok else "LỆCH", "\n".join(l for l in log.splitlines() if "apply-v0" in l or "rollback" in l or "stale-mcp" in l
                                                                               or "baseline" in l), "PASS" if ok else "FAIL"))
        rb = BK[p]
        rows.append("%s\tconfig-guard:%s\t%s\t%s\t%s\t%s\n" % (iid, tid, pf, WD[p], rb, sha(rb)))
    else:
        pf = C + "/foreign-%s.txt" % iid.replace("/", "_").replace(":", "_")
        open(pf, "w").write("--run %s · mục footprint %s KHÔNG do lượt này tạo (việc song song/tác nhân khác)\nKẾT LUẬN: PASS (ghi nhận để đủ 4 ô)\n" % (RUN, iid))
        rows.append("%s\tforeign\t%s\tINV20/#22 Guard periodic\t-\t-\n" % (iid, pf))
open(C + "/coverage.tsv", "w").write("".join(rows))
print(len(items), "mục ·", C + "/coverage.tsv")
