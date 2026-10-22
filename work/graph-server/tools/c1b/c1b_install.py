#!/usr/bin/env python3
# GS-C1B-LAYERED-IMPACT-20261022-08 · cài C1-B trong MỘT cửa sổ VPS-GHI (Điều 30/31, apply-v0, Config Guard) + đường lùi.
#   pre-write : kiểm Config Guard CLEAN + 4 đích đúng mốc PRE · sao lưu .truoc (4 đích + giấy) · THU HỒI giấy ô ĐỦ có thể bị ảnh hưởng
#               (pg:directus:trigger — cùng nhãn PgTable/PgFunction) TRƯỚC giao dịch Graph · apply-v0 graph-refresh-lib-scoresets (lọc lane) ·
#               graph-refresh-lib-cert (v3) · graph-cert-cells (c1b-1)
#   baseline  : cert-baseline = mốc cũ + certified_floor thêm 12 ô L1 (11 bảng + phạm vi) — CHỈ ô đã ĐỦ ở diễn tập (rehearse.json) — apply-v0
#   l2        : đặt ứng viên L2 (w/l2-candidates.json) vào state/refresh/cert/ (dữ liệu, 0640)
#   rollback  : đặt lại NGUYÊN byte .truoc (baseline → cells → cert → scorer) qua apply-v0; giấy sẽ cấp lại ở lượt cert kế
# Exit 0 PASS · 1 FAIL · 3 dừng trước ghi
import hashlib, importlib.machinery, importlib.util, json, os, shutil, subprocess, sys, time

RUN = "GS-C1B-LAYERED-IMPACT-20261022-08"
E = "/opt/incomex/work/graph-server/evidence/" + RUN
S, M = E + "/scripts", E + "/m"
P = "/opt/incomex/graph-server/prod-v1"
MID = RUN + ".M"
CH = "/root/incomex-config-changes/" + MID
CERT = P + "/state/refresh/cert"
T = [("graph-refresh-lib-scoresets", P + "/bin/refresh/r7_score_sets.py", S + "/v3/r7_score_sets.py", "0c46fcd13f2c21a4637126ee16f73c498eb3999b495e12ee988c5d9eb1ae7361"),
     ("graph-refresh-lib-cert", P + "/bin/refresh/graph_cert.py", S + "/v3/graph_cert.py", "581c83a00665b903fe5892aeb7ad5eaac795a449cd7ec363bc237d6a23decc55"),
     ("graph-cert-cells", P + "/manifest/cert-cells.json", S + "/v3/cert-cells.json", "bf4ae7899cd6af27bb3f34145ced01640e6684a2fe2928eab179a03382b9287a")]
BASE = ("graph-cert-baseline", P + "/manifest/cert-baseline.json", "f2dbb6d18fb145bb86c36fbfde94d34956a5c5f3397064b096ae8b708a881341")
REVOKE = ["pg:directus:trigger"]
now = lambda: time.strftime("%FT%TZ", time.gmtime())
LOG = M + "/install.log"


def say(*a):
    line = now() + " " + " ".join(str(x) for x in a)
    print(line, flush=True)
    with open(LOG, "a") as f:
        f.write(line + "\n")


def sh(cmd, timeout=300):
    p = subprocess.run(cmd, capture_output=True, timeout=timeout)
    return p.returncode, p.stdout.decode(errors="replace"), p.stderr.decode(errors="replace")


sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()


def apply_v0(target, live, cand):
    rc, o, e = sh(["incomex-config-apply-v0", "--mutation-id", MID, "--agent", "claude-code-cli", "--target-id", target, "--candidate", cand,
                   "--expected-baseline", sha(live)], timeout=180)
    out = " ".join(l for l in (o + e).splitlines() if l.startswith(("RESULT=", "REASON=")))
    return rc == 0 and "RESULT=APPLIED" in out and sha(live) == sha(cand), out


def gc_lib():
    ldr = importlib.machinery.SourceFileLoader("graph_cert_v3", S + "/v3/graph_cert.py")
    m = importlib.util.module_from_spec(importlib.util.spec_from_loader("graph_cert_v3", ldr))
    ldr.exec_module(m)
    return m


def revoke():
    G = gc_lib()
    doc = json.load(open(CERT + "/current.json"))
    ok, why = G.verify_manifest(doc)
    if not ok:
        return False, "giấy hiện hành không hợp lệ: " + why
    for k in REVOKE:
        c = doc["cells"].get(k)
        if c:
            c.update(status=G.MP, reasons=["REVOKED_BEFORE_GRAPH_WRITE %s %s (cấp lại sau khi đối chiếu độc lập)" % (RUN, now())])
            c.pop("issued_at", None)
            c.pop("expires_at", None)
    doc["revoked"] = {"by": RUN, "at": now(), "cells": REVOKE}
    doc["summary"] = G.summarize(doc)
    doc.pop("self_sha256", None)
    doc["self_sha256"] = G.self_sha(doc)
    tmp = CERT + "/current.json.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=1, sort_keys=True)
    os.chmod(tmp, 0o640)
    os.replace(tmp, CERT + "/current.json")
    eff, _ = G.effective(doc)
    return all(eff[k][0] == G.MP for k in REVOKE if k in eff), doc["self_sha256"]


def pre_write():
    os.makedirs(M + "/backup", mode=0o700, exist_ok=True)
    os.makedirs(CH, mode=0o700, exist_ok=True)
    rc, o, _ = sh(["incomex-config-status-v0"])
    if "STATUS=CLEAN" not in o:
        say("STOP Config Guard không CLEAN"); return 3
    for t, live, cand, want in T + [(BASE[0], BASE[1], None, BASE[2])]:
        if sha(live) != want or open("/var/lib/incomex-config-guard-v0/baseline/%s.sha256" % t).read().split()[0] != want or (cand and not os.path.isfile(cand)):
            say("STOP đích lệch mốc PRE", t, sha(live)[:16]); return 3
    for t, live, cand, want in T + [(BASE[0], BASE[1], None, BASE[2])]:
        shutil.copy2(live, M + "/backup/%s.truoc" % t)
    shutil.copy2(CERT + "/current.json", M + "/backup/cert-current.json.truoc")
    ok, info = revoke()
    say("revoke", REVOKE, "OK" if ok else "FAIL", info)
    if not ok:
        return 1
    for t, live, cand, want in T:
        c = CH + "/" + os.path.basename(live)
        shutil.copyfile(cand, c)
        os.chmod(c, 0o600)
        ok, out = apply_v0(t, live, c)
        say("apply-v0", t, out, sha(live)[:16])
        if not ok:
            say("FAIL ⇒ rollback")
            rollback()
            return 1
    return 0


def baseline():
    reh = json.load(open(E + "/w/rehearse.json"))
    du = sorted(k for k, v in reh["cert_on_temp"].items() if k.startswith("l1:") and v["status"] == "ĐỦ tại T")
    b = json.load(open(BASE[1]))
    if sha(BASE[1]) != BASE[2]:
        say("STOP baseline lệch mốc"); return 3
    b["certified_floor"] = sorted(set(b["certified_floor"]) | set(du))
    b.setdefault("notes", {})["C1B"] = ("%s: thêm %d ô L1 (11 bảng mẫu + phạm vi) vào sàn — đã ĐỦ khi diễn tập Neo4j tạm (rehearse.json) và phải ĐỦ ở lượt cấp giấy "
                                        "thật sau ghi; tụt ⇒ đèn #24 DOWN COVERAGE_REGRESSION (PROMPT C1-B §5, Host P211 READY). Không đổi ô MỘT PHẦN nào." % (RUN, len(du)))
    b["written_by"], b["written_at"] = RUN, now()
    c = CH + "/cert-baseline.json"
    json.dump(b, open(c, "w"), ensure_ascii=False, indent=1, sort_keys=True)
    os.chmod(c, 0o600)
    ok, out = apply_v0(BASE[0], BASE[1], c)
    say("apply-v0", BASE[0], out, "floor+%d" % len(du), sha(BASE[1])[:16])
    return 0 if ok else 1


def l2():
    src = E + "/w/l2-candidates.json"
    d = json.load(open(src))
    assert d.get("format") == "graph-l2-candidates-v1" and d.get("self_sha256")
    tmp = CERT + "/l2-candidates.json.tmp"
    shutil.copyfile(src, tmp)
    os.chmod(tmp, 0o640)
    os.replace(tmp, CERT + "/l2-candidates.json")
    say("l2 đặt", d["self_sha256"][:16], sha(CERT + "/l2-candidates.json")[:16])
    return 0


def rollback():
    bad = 0
    for t, live, *_ in [BASE] + list(reversed(T)):
        b = M + "/backup/%s.truoc" % t
        if os.path.exists(b) and sha(live) != sha(b):
            c = CH + "/rb-" + os.path.basename(live)
            shutil.copyfile(b, c)
            os.chmod(c, 0o600)
            ok, out = apply_v0(t, live, c)
            say("rollback", t, out)
            bad += 0 if ok else 1
    return 0 if not bad else 1


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    fn = {"pre-write": pre_write, "baseline": baseline, "l2": l2, "rollback": rollback}.get(cmd)
    if not fn:
        print("dùng: c1b_install.py pre-write|baseline|l2|rollback"); sys.exit(2)
    sys.exit(fn())
