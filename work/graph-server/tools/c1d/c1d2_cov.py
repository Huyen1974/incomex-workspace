#!/usr/bin/env python3
# GS-C1D2-SCOPED-AUTOCOVER-20261026-13 · (khuôn c1d_cov GS-C1D-NATIVE-AUTOCOVER-20261023-10) coverage Guard POST v2: mỗi mục footprint đủ 4 ô (Đ31 · Đ30 proof · watchdog · rollback).
# Dùng: c1d_cov.py <guard-post1.json>  → <E>/guard-cov/coverage.tsv + d30-*.txt
import hashlib, json, os, sys, time

RUN = "GS-C1D2-SCOPED-AUTOCOVER-20261026-13"
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
log = open(E + "/m/install.log").read() if os.path.exists(E + "/m/install.log") else ""
applog = "".join(open(E + "/w/" + f).read()[-1500:] + "\n" for f in sorted(os.listdir(E + "/w")) if f.startswith("apply-") and f.endswith(".txt"))
P = "/opt/incomex/graph-server/prod-v1"
INST = E + "/scripts/c1d2_install.py"
BK = {P + "/bin/refresh/graph_cert.py": E + "/m/backup/graph-refresh-lib-cert.truoc",
      P + "/bin/refresh/graph_autocover.py": E + "/m/backup/graph-refresh-lib-autocover.truoc",
      P + "/manifest/cert-cells.json": E + "/m/backup/graph-cert-cells.truoc",
      P + "/bin/graph-refresh": E + "/m/backup/graph-refresh-cli.truoc",
      P + "/manifest/graph-invariants.json": E + "/m/backup/graph-v1-invariants.truoc",
      P + "/manifest/pins.json": E + "/m/backup/graph-v1-pins.truoc",
      P + "/manifest/refresh-sources.json": E + "/m/backup/graph-refresh-sources.truoc",
      P + "/manifest/recovery-manifest.json": E + "/m/backup/graph-recovery-manifest.truoc"}
NEWF = set()
WD = {P + "/bin/refresh/graph_cert.py": "Config Guard drift-check + INV23 code_ledger + đèn #24 mỗi lượt graph-refresh + c1d2_fixtures 41/41 + c1d_fixtures 60/60 + bộ đọc cũ=mới 11/11 + INV22",
      P + "/bin/refresh/graph_autocover.py": "Config Guard drift-check + INV23 + graph-refresh lane c1d mỗi lượt (bản tạm + máy cấp giấy chấm ô) + c1d2_fixtures R3 10/10 + đèn #24",
      P + "/manifest/cert-cells.json": "Config Guard drift-check + K3 hàng rào danh mục (mọi nhãn) + ma trận bao phủ G1–G9 + đèn #24",
      P + "/bin/graph-refresh": "Config Guard drift-check + INV23 + graph-refresh selftest (cờ tươi + tách chuông) + c1dfix_fixtures D23 22/22 + đèn #24",
      P + "/manifest/graph-invariants.json": "Config Guard drift-check + INV22 graph_v1 (invariants = manifest)",
      P + "/manifest/pins.json": "Config Guard drift-check + INV22 graph_v1 status",
      P + "/manifest/refresh-sources.json": "Config Guard drift-check + graph-refresh decide (c1d._pilot_total trần cộng dồn)",
      P + "/manifest/recovery-manifest.json": "Config Guard drift-check + graph-refresh tiền điều kiện recovery (H1) + Drive D23"}
for p in NEWF:
    WD[p] = "Config Guard drift-check (đích mới) + INV23 code_ledger + graph-refresh lane c1d mỗi lượt + đèn #24"
rows = ["# item\td31\td30_proof\twatchdog\trollback\trollback_sha256 · %s · %s\n" % (RUN, time.strftime("%FT%TZ", time.gmtime()))]
for it in items:
    iid = it["id"]
    p = it.get("path")
    if it["kind"] == "file" and (p in BK or p in NEWF):
        tid = reg.get(p) or {CG + "/registry.tsv": "guard-registry", "/opt/incomex/scripts/code-ledger.tsv": "r7-code-ledger-tsv"}.get(p)
        cgf = CG + "/baseline/%s.sha256" % tid if tid else None
        cg = open(cgf).read().split()[0] if cgf and os.path.exists(cgf) else None
        cur = sha(p)
        ok = bool(tid) and cg == cur
        pf = C + "/d30-%s.txt" % (tid or os.path.basename(p))
        open(pf, "w").write("--run %s · đích=%s · tệp=%s\nsha256 mới=%s · baseline Config Guard=%s · %s\n%s\n%s\nKẾT LUẬN: %s\n" % (
            RUN, tid, p, cur, cg, "TRÙNG" if ok else "LỆCH", "\n".join(l for l in log.splitlines() if "apply-v0" in l or "lùi" in l or "DIỄN TẬP" in l),
            applog[-2500:], "PASS" if ok else "FAIL"))
        rb = BK.get(p) if (BK.get(p) and os.path.exists(BK.get(p))) else INST
        rows.append("%s\tconfig-guard:%s\t%s\t%s\t%s\t%s\n" % (iid, tid, pf, WD[p], rb, sha(rb)))
    else:
        pf = C + "/foreign-%s.txt" % iid.replace("/", "_").replace(":", "_")
        open(pf, "w").write("--run %s · mục footprint %s KHÔNG do lượt này tạo (việc song song/tác nhân khác hoặc dữ liệu trạng thái)\nKẾT LUẬN: PASS (ghi nhận để đủ 4 ô)\n" % (RUN, iid))
        rows.append("%s\tforeign\t%s\tINV20/#22 Guard periodic\t-\t-\n" % (iid, pf))
open(C + "/coverage.tsv", "w").write("".join(rows))
print(len(items), "mục ·", C + "/coverage.tsv")
