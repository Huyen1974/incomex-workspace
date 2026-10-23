#!/usr/bin/env python3
# GS-C1D-NATIVE-AUTOCOVER-20261023-10 · cài C1-D trong MỘT cửa sổ VPS-GHI (Điều 30/31, apply-v0, Config Guard, sổ mã) + đường lùi.
#   pre-write : Config Guard CLEAN + 3 đích sửa đúng mốc PRE + 4 tệp mới chưa có · sao lưu .truoc (đích + sổ mã + registry + trạng thái giấy +
#               cross-edges pgl1) · (1) 4 tệp mới bin/refresh (graph_autocover · c1b_l1 · c1b_l1_native · c1b_l2 — 3 tệp C1-B chép NGUYÊN byte)
#               + baseline Config Guard + apply-v0 sổ mã (LOCKED) + apply-v0 guard-registry · (2) apply-v0 graph-refresh-lib-cert (v5 c1d-1, K3) ·
#               graph-cert-cells (c1d-1: 80 ô cũ giữ nguyên định nghĩa + 4 ô infra + 16 ô L1 lô 1 + ô phạm vi phủ 27 bảng) · graph-refresh-cli
#               (lane c1d:infra / c1d:pgl1 + L2 mỗi lượt + --only). Thứ tự: tệp mới TRƯỚC graph-refresh (graph-refresh import graph_autocover).
#   rollback  : ngược thứ tự — graph-refresh → cells → cert (NGUYÊN byte .truoc qua apply-v0) → registry → sổ mã → gỡ baseline + 4 tệp mới
#               → trả trạng thái giấy .truoc. KHÔNG đụng Graph (ghi Graph lùi bằng graph-refresh undo trong lượt / graph-inverse dưới đây).
#   drill     : diễn tập LÙI THẬT (rollback → kiểm nguyên byte PRE + Config Guard CLEAN) rồi cài lại (pre-write) — Điều 30
#   graph-inverse <lane> : lùi phần Graph do lane C1-D tạo (xoá đúng nút/cạnh run='graph-refresh <lane>'), đặt lại invariants/pins/sources
#               PRE qua apply-v0 + điểm khôi phục MỚI (graph-refresh recovery-point --drive) — CHỈ khi Host/Owner yêu cầu lùi sau commit (đã diễn
#               tập trên Neo4j tạm: I = PRE). Lưu ý: lane SET thuộc tính nút có sẵn không có ở lượt này (0 SET) nên xoá đúng phần tạo là đủ.
# Exit 0 PASS · 1 FAIL · 3 dừng trước ghi
import hashlib, json, os, shutil, subprocess, sys, time

RUN = "GS-C1D-NATIVE-AUTOCOVER-20261023-10"
E = "/opt/incomex/work/graph-server/evidence/" + RUN
S, M = E + "/scripts", E + "/m"
P = "/opt/incomex/graph-server/prod-v1"
RB = P + "/bin/refresh"
MID = RUN + ".M"
CH = "/root/incomex-config-changes/" + MID
CG = "/var/lib/incomex-config-guard-v0"
REG = CG + "/registry.tsv"
LEDGER = "/opt/incomex/scripts/code-ledger.tsv"
CERT = P + "/state/refresh/cert"
CROSS = P + "/state/refresh/loaded/pgl1/cross-edges.json"
NEW = [("graph-refresh-lib-autocover", RB + "/graph_autocover.py", S + "/graph_autocover.py"),
       ("graph-refresh-lib-c1bl1", RB + "/c1b_l1.py", S + "/c1b_l1.py"),
       ("graph-refresh-lib-c1bl1native", RB + "/c1b_l1_native.py", S + "/c1b_l1_native.py"),
       ("graph-refresh-lib-c1bl2", RB + "/c1b_l2.py", S + "/c1b_l2.py")]
C1B_SHA = {"c1b_l1.py": "9a59f18898a2133fe51158e6765773c937d15cf073fc7fee8495d366de6db2a1",
           "c1b_l1_native.py": "7aa2c83a02380400e68823ae33dfe03f19d0fe2a43dcbd619efb802e4852dfda",
           "c1b_l2.py": "3aa968afcefad2e953d580b79d1384f302364aec43729a269807a70af28ff077"}
MOD = [("graph-refresh-lib-cert", RB + "/graph_cert.py", S + "/graph_cert.py", "f9c571f1237e65c163e63c4d246fe313a48a3a9551174cbce3ae06db28d74353"),
       ("graph-cert-cells", P + "/manifest/cert-cells.json", S + "/cert-cells.c1d.json", "79f870526c0ca36f6da30ceed0a81c7be216fdb11bcc137a00cfdf5a45ec5aba"),
       ("graph-refresh-cli", P + "/bin/graph-refresh", S + "/graph-refresh", "5c5014c1494500dc77c048f86101440147b9ff415ee25c567261d60f635d0134")]
STATE = ["current.json", "alarm.json", "incidents.jsonl", "last-good.json", "canary.json", "inventory.json", "l2-candidates.json"]
GRAPH_T = [("graph-v1-invariants", P + "/manifest/graph-invariants.json"), ("graph-v1-pins", P + "/manifest/pins.json"),
           ("graph-refresh-sources", P + "/manifest/refresh-sources.json"), ("graph-recovery-manifest", P + "/manifest/recovery-manifest.json")]
now = lambda: time.strftime("%FT%TZ", time.gmtime())
LOG = M + "/install.log"
STF = M + "/install-state.json"


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


def st_load():
    try:
        return json.load(open(STF))
    except (OSError, ValueError):
        return {}


def st_save(d):
    json.dump(d, open(STF, "w"), ensure_ascii=False, indent=1)


def backup():
    os.makedirs(M + "/backup", mode=0o700, exist_ok=True)
    for t, live, cand, want in MOD:
        if not os.path.exists(M + "/backup/%s.truoc" % t):
            shutil.copy2(live, M + "/backup/%s.truoc" % t)
    for name, live in (("registry.tsv", REG), ("code-ledger.tsv", LEDGER)):
        if not os.path.exists(M + "/backup/%s.truoc" % name):
            shutil.copy2(live, M + "/backup/%s.truoc" % name)
    for t, live in GRAPH_T:
        if not os.path.exists(M + "/backup/%s.truoc" % t):
            shutil.copy2(live, M + "/backup/%s.truoc" % t)
    for f in STATE:
        if os.path.exists(CERT + "/" + f) and not os.path.exists(M + "/backup/cert-%s.truoc" % f):
            shutil.copy2(CERT + "/" + f, M + "/backup/cert-%s.truoc" % f)
    if os.path.exists(CROSS) and not os.path.exists(M + "/backup/pgl1-cross-edges.json.truoc"):
        shutil.copy2(CROSS, M + "/backup/pgl1-cross-edges.json.truoc")
    say("backup", sorted(os.listdir(M + "/backup")))


def pre_write():
    os.makedirs(CH, mode=0o700, exist_ok=True)
    rc, o, _ = sh(["incomex-config-status-v0"])
    if "STATUS=CLEAN" not in o:
        say("STOP Config Guard không CLEAN"); return 3
    reg, led = open(REG).read(), open(LEDGER).read()
    for t, live, src in NEW:
        b = os.path.basename(src)
        if os.path.exists(live) or ("\n%s\t" % t) in reg or os.path.exists(CG + "/baseline/%s.sha256" % t) or ("\n%s\t" % live) in led \
                or not os.path.isfile(src) or (b in C1B_SHA and sha(src) != C1B_SHA[b]):
            say("STOP tệp mới đã có/thiếu nguồn/lệch byte C1-B", t); return 3
    for t, live, cand, want in MOD:
        cg = open(CG + "/baseline/%s.sha256" % t).read().split()[0]
        if sha(live) != want or cg != want or not os.path.isfile(cand):
            say("STOP đích lệch mốc PRE", t, sha(live)[:16], cg[:16]); return 3
    backup()
    d = {"files": [], "baselines": [], "ledger": False, "registry": False, "mod": []}
    st_save(d)
    try:
        for t, live, src in NEW:                                  # (1) tệp mới + baseline Config Guard
            shutil.copyfile(src, live)
            os.chown(live, 0, 0)
            os.chmod(live, 0o644)
            d["files"].append(live)
            bd = CG + "/baseline/"
            shutil.copy2(live, bd + t + ".content"); os.chmod(bd + t + ".content", 0o600)
            open(bd + t + ".sha256", "w").write(sha(live) + "\n"); os.chmod(bd + t + ".sha256", 0o600)
            open(bd + t + ".meta", "w").write("root:root 644\n"); os.chmod(bd + t + ".meta", 0o600)
            d["baselines"].append(t)
            st_save(d)
        lines = led.splitlines(True)
        head = [l for l in lines if l.startswith("#")]
        body = sorted([l for l in lines if not l.startswith("#")] + ["%s\tLOCKED\t%s\tGS-C1D:graph-refresh-c1d\n" % (live, t) for t, live, _ in NEW],
                      key=lambda x: x.split("\t", 1)[0].encode())
        open(CH + "/code-ledger.tsv", "w").write("".join(head + body)); os.chmod(CH + "/code-ledger.tsv", 0o600)
        ok, out = apply_v0("r7-code-ledger-tsv", LEDGER, CH + "/code-ledger.tsv")
        say("apply-v0 r7-code-ledger-tsv", out)
        if not ok:
            raise RuntimeError("code-ledger")
        d["ledger"] = True; st_save(d)
        rows = ["# %s (graph-server C1-D, Điều 30/31): lane cộng-thêm có giới hạn graph-refresh c1d:infra/c1d:pgl1 (graph_autocover) + bộ nạp/L2 C1-B chép byte. Đổi chỉ qua apply-v0.\n" % RUN,
                "#   Rollback: c1d_install.py rollback trong thư mục bằng chứng RUN (bản trước ở rollback/ của guard-registry).\n"]
        rows += ["%s\t%s\tHOST_SCRIPT\tNO\tPRIVATE_COPY\tPYTHON_SYNTAX\tNONE\troot:root\t644\n" % (t, live) for t, live, _ in NEW]
        open(CH + "/registry.tsv", "w").write(reg + ("" if reg.endswith("\n") else "\n") + "".join(rows)); os.chmod(CH + "/registry.tsv", 0o600)
        ok, out = apply_v0("guard-registry", REG, CH + "/registry.tsv")
        say("apply-v0 guard-registry", out)
        if not ok:
            raise RuntimeError("guard-registry")
        d["registry"] = True; st_save(d)
        for t, live, cand, want in MOD:                           # (2) cert → cells → graph-refresh
            c = CH + "/" + os.path.basename(live)
            shutil.copyfile(cand, c)
            os.chmod(c, 0o600)
            ok, out = apply_v0(t, live, c)
            say("apply-v0", t, out, sha(live)[:16])
            if not ok:
                raise RuntimeError(t)
            d["mod"].append(t); st_save(d)
    except Exception as e:  # noqa: BLE001
        say("FAIL %s ⇒ rollback" % e)
        rollback()
        return 1
    rc, o, _ = sh(["incomex-config-status-v0"])
    say("Config Guard sau cài", "CLEAN" if "STATUS=CLEAN" in o else "KHÔNG CLEAN")
    return 0 if "STATUS=CLEAN" in o else 1


def rollback():
    d, bad = st_load(), []
    for t, live, cand, want in reversed(MOD):
        bk = M + "/backup/%s.truoc" % t
        if os.path.exists(bk) and sha(live) != sha(bk):
            c = CH + "/rb-" + os.path.basename(live)
            shutil.copyfile(bk, c); os.chmod(c, 0o600)
            ok, out = apply_v0(t, live, c)
            say("lùi", t, out, sha(live)[:16])
            bad += [] if ok else [t]
    for name, tid, live in (("registry.tsv", "guard-registry", REG), ("code-ledger.tsv", "r7-code-ledger-tsv", LEDGER)):
        bk = M + "/backup/%s.truoc" % name
        if os.path.exists(bk) and sha(live) != sha(bk):
            c = CH + "/rb-" + name
            shutil.copyfile(bk, c); os.chmod(c, 0o600)
            ok, out = apply_v0(tid, live, c)
            say("lùi", tid, out)
            bad += [] if ok else [tid]
    for t, live, _ in NEW:
        for ext in (".content", ".sha256", ".meta"):
            try:
                os.remove(CG + "/baseline/" + t + ext)
            except OSError:
                pass
        try:
            os.remove(live)
        except OSError:
            pass
    for f in STATE:
        bk = M + "/backup/cert-%s.truoc" % f
        if os.path.exists(bk):
            shutil.copy2(bk, CERT + "/" + f + ".rb")
            os.replace(CERT + "/" + f + ".rb", CERT + "/" + f)
    st_save({"files": [], "baselines": [], "ledger": False, "registry": False, "mod": [], "rolled_back_at": now()})
    rc, o, _ = sh(["incomex-config-status-v0"])
    pre_ok = all(sha(live) == want for t, live, cand, want in MOD) and not any(os.path.exists(l) for _, l, _ in NEW) \
        and sha(REG) == sha(M + "/backup/registry.tsv.truoc") and sha(LEDGER) == sha(M + "/backup/code-ledger.tsv.truoc")
    say("lùi xong · nguyên byte PRE", pre_ok, "· Config Guard", "CLEAN" if "STATUS=CLEAN" in o else "KHÔNG CLEAN", "· lỗi", bad)
    return 0 if pre_ok and not bad and "STATUS=CLEAN" in o else 1


def drill():
    say("DIỄN TẬP LÙI THẬT: rollback → kiểm PRE → cài lại")
    if rollback() != 0:
        say("DIỄN TẬP LÙI FAIL"); return 1
    return pre_write()


def graph_inverse(lane):
    sys.path.insert(0, RB)
    import r7_g1lib
    g = r7_g1lib.load(P + "/bin/graph-v1")
    pw = g.password()
    tag = "graph-refresh " + lane
    d = g.http_cypher([("MATCH (:GS)-[x]->(:GS) WHERE x.run = $r DELETE x", {"r": tag}), ("MATCH (n:GS) WHERE n.run = $r DETACH DELETE n", {"r": tag})], pw, timeout=900)
    say("graph-inverse", lane, "lỗi", [x.get("code") for x in d.get("errors") or []])
    for t, live in GRAPH_T[:3]:          # invariants/pins/sources về PRE; điểm khôi phục: tạo MỚI từ Graph đã lùi (bản cũ cục bộ đã thay)
        bk = M + "/backup/%s.truoc" % t
        if os.path.exists(bk) and sha(live) != sha(bk):
            c = CH + "/inv-" + os.path.basename(live)
            shutil.copyfile(bk, c); os.chmod(c, 0o600)
            say("graph-inverse apply-v0", t, apply_v0(t, live, c)[1])
    bk = M + "/backup/pgl1-cross-edges.json.truoc"
    if lane == "c1d:pgl1" and os.path.exists(bk):
        shutil.copy2(bk, CROSS)
    ok = not g.inv_equal(g.invariants(pw), json.load(open(GRAPH_T[0][1])))
    say("graph-inverse invariants = manifest PRE", ok)
    if ok:
        rc, o, e = sh([P + "/bin/graph-refresh", "recovery-point", "--drive", "--label", "c1d-graph-inverse-" + lane.replace(":", "-")], timeout=3600)
        say("graph-inverse điểm khôi phục mới", rc, (o + e).strip()[-200:])
        ok = rc == 0
    return 0 if ok else 30


FIX1 = [("graph-refresh-lib-autocover", RB + "/graph_autocover.py", S + "/graph_autocover.py", "54e7ce1787079ffb14806d83fe122bbe2452304e54b42ca1d9cf251123fb5775"),
        ("graph-refresh-cli", P + "/bin/graph-refresh", S + "/graph-refresh", "26e47af818c958ac918f4f591d9aeb07454ff20998e191b35153548135213242")]


def fix1():
    """Sửa sau lượt ghi 1 (DELTA_SKIPPED_SAFE «nguồn đổi giữa lượt» giả): kiểm giữa lượt so vân tay DANH TÍNH (ident_sha256) thay vì sha256 gồm
    dấu giờ chụp. apply-v0 2 đích từ bản đã cài C1-D (mốc PRE-FIX1) — rollback toàn RUN vẫn về .truoc trước C1-D."""
    rc, o, _ = sh(["incomex-config-status-v0"])
    if "STATUS=CLEAN" not in o:
        say("STOP fix1 Config Guard không CLEAN"); return 3
    for t, live, cand, want in FIX1:
        if sha(live) != want or not os.path.isfile(cand):
            say("STOP fix1 đích lệch mốc", t, sha(live)[:16]); return 3
    for t, live, cand, want in FIX1:
        shutil.copy2(live, M + "/backup/%s.fix1-truoc" % t)
        c = CH + "/fix1-" + os.path.basename(live)
        shutil.copyfile(cand, c); os.chmod(c, 0o600)
        ok, out = apply_v0(t, live, c)
        say("apply-v0 fix1", t, out, sha(live)[:16])
        if not ok:
            return 1
    rc, o, _ = sh(["incomex-config-status-v0"])
    say("Config Guard sau fix1", "CLEAN" if "STATUS=CLEAN" in o else "KHÔNG CLEAN")
    return 0 if "STATUS=CLEAN" in o else 1


FIX2 = [("graph-refresh-cli", P + "/bin/graph-refresh", S + "/graph-refresh", "d9d1eb5f2974a8b4")]


def fix2():
    """Sửa sau lượt ghi 2 (11:18Z RUN FAIL UnboundLocalError repo ở bước sổ nguồn, graph-refresh đã tự lùi I=PRE): nhánh sổ nguồn của lane c1d
    không rơi xuống nhánh code (if → elif). apply-v0 1 đích từ bản fix1 — lỗi giả L17 (cmd_run trọn đường lane c1d) bắt được lỗi cũ, PASS bản sửa."""
    rc, o, _ = sh(["incomex-config-status-v0"])
    if "STATUS=CLEAN" not in o:
        say("STOP fix2 Config Guard không CLEAN"); return 3
    for t, live, cand, want in FIX2:
        if not sha(live).startswith(want) or not os.path.isfile(cand):
            say("STOP fix2 đích lệch mốc", t, sha(live)[:16]); return 3
        shutil.copy2(live, M + "/backup/%s.fix2-truoc" % t)
        c = CH + "/fix2-" + os.path.basename(live)
        shutil.copyfile(cand, c); os.chmod(c, 0o600)
        ok, out = apply_v0(t, live, c)
        say("apply-v0 fix2", t, out, sha(live)[:16])
        if not ok:
            return 1
    rc, o, _ = sh(["incomex-config-status-v0"])
    say("Config Guard sau fix2", "CLEAN" if "STATUS=CLEAN" in o else "KHÔNG CLEAN")
    return 0 if "STATUS=CLEAN" in o else 1


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "graph-inverse":
        sys.exit(graph_inverse(sys.argv[2]))
    fn = {"pre-write": pre_write, "rollback": rollback, "drill": drill, "fix1": fix1, "fix2": fix2}.get(cmd)
    if not fn:
        print("dùng: c1d_install.py pre-write|rollback|drill|graph-inverse <lane>"); sys.exit(2)
    sys.exit(fn())
