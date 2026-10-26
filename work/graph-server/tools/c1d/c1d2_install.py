#!/usr/bin/env python3
# GS-C1D2-SCOPED-AUTOCOVER-20261026-13 · cài C1-D2 trong MỘT cửa sổ VPS-GHI qua apply-v0 (Điều 30/31, Config Guard) + đường lùi nguyên byte.
#   check  : (mặc định, chỉ đọc) Config Guard CLEAN · 4 đích = mốc PRE (tệp sống + baseline Config Guard) hoặc đã = ứng viên · ứng viên đúng sha
#   apply  : sao lưu .truoc → apply-v0 4 đích (lib-autocover → lib-cert → cert-cells → cli) → kiểm sau cài bằng MÃ PRODUCTION mới (selftest ·
#            recovery_ok/H1 · nhãn N4 không lỗi máy · thư viện nạp được) → Config Guard CLEAN; lỗi ⇒ lùi trọn
#   drill  : diễn tập LÙI THẬT: rollback 4 đích (nguyên byte .truoc) → kiểm PRE + CLEAN → apply lại
#   rollback : apply-v0 nguyên byte .truoc ngược thứ tự (KHÔNG đụng Graph; lùi dữ liệu Graph của lane là c1d2_lane_rollback.py)
# Exit 0 PASS · 1 FAIL · 3 dừng trước ghi
import hashlib, importlib.machinery, importlib.util, json, os, shutil, subprocess, sys, time

RUN = "GS-C1D2-SCOPED-AUTOCOVER-20261026-13"
E = "/opt/incomex/work/graph-server/evidence/" + RUN
M = E + "/m"
P = "/opt/incomex/graph-server/prod-v1"
CG = "/var/lib/incomex-config-guard-v0"
MID = RUN + ".M"
CH = "/root/incomex-config-changes/" + MID
# khoá: (đích Config Guard, tệp sống, sha PRE, ứng viên, sha ứng viên) — thứ tự cài: thư viện trước, cli sau cùng
T = {"autocover": ("graph-refresh-lib-autocover", P + "/bin/refresh/graph_autocover.py", "b606d20aa471529b32b553da1dc9968dd8670e1c87fa70a85f1aa5dfb886972b",
                   E + "/scripts/graph_autocover.py", "8ee252fdcbd96a8b849d614ca5a19a2a20b12858aa8b9bf9a92333c434884dbc"),
     "cert": ("graph-refresh-lib-cert", P + "/bin/refresh/graph_cert.py", "75bbb951ffdf2277fe30bafe3c802095246336c43ab42eda09c9c3f5dd6d7eb0",
              E + "/scripts/graph_cert.py", "66c4060b44b5d6469bddb3962126bb7473084712d1cec59426142433c4db8b52"),
     "cells": ("graph-cert-cells", P + "/manifest/cert-cells.json", "afeef5691d60bd44e38a70c2d06dcbb34adebc3e47a2acea676334ee12c9c620",
               E + "/scripts/cert-cells.json", "cfed5148ad60eef73b226fd617458f284e22d45b7678a391eaf3a4b0162a44b4"),
     "cli": ("graph-refresh-cli", P + "/bin/graph-refresh", "cb3561089448860b91dfd0ac163cff72f4ec57efd926f3199065811c3bba2937",
             E + "/scripts/graph-refresh", "e5e0af2f58adf95ea5a3898756bb709c4715d6022dbbeab56a6630ecc23f98ae")}
ORDER = ["autocover", "cert", "cells", "cli"]
LOG = M + "/install.log"
now = lambda: time.strftime("%FT%TZ", time.gmtime())
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()


def say(*a):
    line = now() + " " + " ".join(str(x) for x in a)
    print(line, flush=True)
    with open(LOG, "a") as f:
        f.write(line + "\n")


def sh(cmd, timeout=300):
    p = subprocess.run(cmd, capture_output=True, timeout=timeout)
    return p.returncode, p.stdout.decode(errors="replace"), p.stderr.decode(errors="replace")


def clean():
    return "STATUS=CLEAN" in sh(["incomex-config-status-v0"])[1]


def cg_sha(tid):
    return open(CG + "/baseline/%s.sha256" % tid).read().split()[0]


def apply_v0(tid, live, src, tag):
    os.makedirs(CH, mode=0o700, exist_ok=True)
    c = CH + "/%s-%s" % (tag, os.path.basename(live))
    shutil.copyfile(src, c)
    os.chmod(c, 0o600)
    rc, o, e = sh(["incomex-config-apply-v0", "--mutation-id", MID, "--agent", "claude-code-cli", "--target-id", tid, "--candidate", c,
                   "--expected-baseline", sha(live)], timeout=180)
    out = " ".join(l for l in (o + e).splitlines() if l.startswith(("RESULT=", "REASON=")))
    ok = rc == 0 and "RESULT=APPLIED" in out and sha(live) == sha(src) and cg_sha(tid) == sha(src)
    say("apply-v0", tid, tag, out, sha(live)[:16], "OK" if ok else "FAIL")
    return ok


def check():
    ok = clean()
    say("check Config Guard", "CLEAN" if ok else "KHÔNG CLEAN")
    for k in ORDER:
        tid, live, pre, cand, csha = T[k]
        bk = M + "/backup/%s.truoc" % tid
        at_pre = sha(live) == pre and cg_sha(tid) == pre
        at_new = sha(live) == csha and cg_sha(tid) == csha
        good = os.path.isfile(cand) and sha(cand) == csha and (at_pre or (at_new and os.path.isfile(bk) and sha(bk) == pre))
        say("check", tid, "live", sha(live)[:16], "PRE" if at_pre else ("NEW" if at_new else "LỆCH"), "cand", sha(cand)[:16] if os.path.isfile(cand) else None,
            "OK" if good else "FAIL")
        ok &= good
    return ok


def backup(k):
    tid, live, pre, _, _ = T[k]
    os.makedirs(M + "/backup", mode=0o700, exist_ok=True)
    bk = M + "/backup/%s.truoc" % tid
    if not os.path.exists(bk):
        if sha(live) != pre:
            raise RuntimeError("đích lệch PRE khi sao lưu " + tid)
        shutil.copy2(live, bk)
    return bk


def load(path, name):
    ldr = importlib.machinery.SourceFileLoader(name, path)
    m = importlib.util.module_from_spec(importlib.util.spec_from_loader(name, ldr))
    ldr.exec_module(m)
    return m


def post_check():
    """Kiểm sau cài bằng MÃ MỚI ở đường production (chỉ đọc): selftest · recovery_ok + H1 · nhãn N4 (graph_cert production) không lỗi máy ·
    thư viện autocover có retire_plan · danh mục mới đọc được."""
    rc, o, e = sh([P + "/bin/graph-refresh", "selftest"], timeout=300)
    st = rc == 0 and "SELFTEST: PASS" in o
    sys.path.insert(0, P + "/bin/refresh")
    m = load(P + "/bin/graph-refresh", "grf_c1d2_post_%d" % int(time.time()))
    ro = m.recovery_ok()
    GC = sys.modules["graph_cert"]
    GA = sys.modules["graph_autocover"]
    lab = GC.label_for("read-cypher", {"query": "MATCH (x:GitRepository) RETURN count(x)"})
    lab_ok = isinstance(lab, dict) and not str(lab.get("reason") or "").startswith("LABEL_ENGINE_ERROR")
    cat_ok = (GC.catalog_read()[1] or {}).get("catalog_version") == "c1d2-1"
    fns = all(hasattr(m, f) for f in ("flag_fresh", "code_blocked_split", "t6_probe", "ls_remote_head")) and hasattr(GA, "retire_plan") \
        and GC.ENGINE_VERSION == "c1d2-1" and GC._SELF_FILE == P + "/bin/refresh/graph_cert.py"
    say("post-check", "selftest", "PASS" if st else "FAIL", "· recovery_ok(H1) production", ro.get("ok"), ro.get("why"), "· nhãn N4", lab.get("completeness_label"),
        str(lab.get("reason"))[:90], "· danh mục c1d2-1", cat_ok, "· hàm/phiên bản", fns)
    return st and ro.get("ok") is True and lab_ok and cat_ok and fns


def cmd_apply():
    if not check():
        say("STOP check"); return 3
    todo = [k for k in ORDER if sha(T[k][1]) != T[k][4]]
    for k in todo:
        backup(k)
    for k in todo:
        tid, live, pre, cand, csha = T[k]
        if not apply_v0(tid, live, cand, "c1d2"):
            say("FAIL apply", tid, "⇒ lùi"); cmd_rollback(); return 1
    ok = post_check() and clean()
    if not ok:
        say("FAIL kiểm sau cài ⇒ lùi"); cmd_rollback(); return 1
    say("apply PASS · 4 đích = ứng viên · Config Guard CLEAN")
    return 0


def cmd_rollback():
    bad = []
    for k in reversed(ORDER):
        tid, live, pre, _, _ = T[k]
        bk = M + "/backup/%s.truoc" % tid
        if os.path.exists(bk) and sha(live) != sha(bk):
            if not apply_v0(tid, live, bk, "rb"):
                bad.append(tid)
        pre_ok = sha(live) == pre and cg_sha(tid) == pre
        say("lùi", tid, "nguyên byte PRE", pre_ok)
        if not pre_ok:
            bad.append(tid)
    ok = not bad and clean()
    say("lùi xong · Config Guard", "CLEAN" if clean() else "KHÔNG CLEAN", "· lỗi", bad)
    return 0 if ok else 1


def cmd_drill():
    say("DIỄN TẬP LÙI THẬT 4 đích: rollback → kiểm PRE + CLEAN + selftest bản cũ → cài lại")
    if cmd_rollback() != 0:
        say("DIỄN TẬP LÙI FAIL"); return 1
    rc, o, e = sh([P + "/bin/graph-refresh", "selftest"], timeout=300)
    say("bản PRE selftest", "PASS" if rc == 0 and "SELFTEST: PASS" in o else "FAIL", "· có flag_fresh?", "flag" in o)
    return cmd_apply()


if __name__ == "__main__":
    os.makedirs(M, exist_ok=True)
    c = sys.argv[1] if len(sys.argv) > 1 else "check"
    if c == "check":
        sys.exit(0 if check() else 1)
    fn = {"apply": cmd_apply, "drill": cmd_drill, "rollback": cmd_rollback, "postcheck": lambda: 0 if post_check() else 1}.get(c)
    if not fn:
        print("dùng: c1d2_install.py check|apply|drill|rollback|postcheck"); sys.exit(2)
    sys.exit(fn())
