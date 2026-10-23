#!/usr/bin/env python3
# GS-C1C-PRODUCTION-TRUST-GATE-20261023-09 · cài C1-C trong MỘT cửa sổ VPS-GHI (Điều 30/31, apply-v0, Config Guard) + đường lùi.
#   pre-write : Config Guard CLEAN + 3 đích đúng mốc PRE · sao lưu .truoc (3 đích + tệp trạng thái giấy) · apply-v0 graph-refresh-lib-cert (v4 c1c-1)
#               + graph-cert-cells (c1c-1, thêm khối families; 80 ô giữ nguyên)
#   stale-mcp : tiến trình `graph-v1 mcp` khởi động TRƯỚC giờ cài đang giữ bộ nhãn v3 trong bộ nhớ (không có hàng rào K1) ⇒ dừng (SIGTERM) —
#               chỉ tiến trình đọc; khách nối lại sẽ được bộ nhãn v4 (v4 tự nạp lại khi tệp đổi, nên lần cài sau không cần bước này)
#   baseline  : CHỈ khi giấy hiện hành (v4) có ô lark:88-phai-cu:b88 ĐỦ + mốc phiên bản ổn định + invariants sống = manifest + pins trỏ đúng
#               invariants + điểm khôi phục = manifest ⇒ mốc: certified_floor += b88 (rút khỏi pending_host_ack), yellow_repeat_hours 168,
#               record_only_gates [] (G9 so như mọi cửa) — apply-v0
#   rollback  : đặt lại NGUYÊN byte .truoc (baseline → cells → cert) qua apply-v0 + trả tệp trạng thái giấy .truoc; giấy cấp lại ở lượt kế
# Exit 0 PASS · 1 FAIL · 3 dừng trước ghi
import hashlib, importlib.machinery, importlib.util, json, os, shutil, signal, subprocess, sys, time

RUN = "GS-C1C-PRODUCTION-TRUST-GATE-20261023-09"
E = "/opt/incomex/work/graph-server/evidence/" + RUN
S, M = E + "/scripts", E + "/m"
P = "/opt/incomex/graph-server/prod-v1"
MID = RUN + ".M"
CH = "/root/incomex-config-changes/" + MID
CERT = P + "/state/refresh/cert"
T = [("graph-refresh-lib-cert", P + "/bin/refresh/graph_cert.py", S + "/graph_cert.py", "39e4630ed60af748a827dcdb3166260272901af7538d314de3c36b8e810d8a0c"),
     ("graph-cert-cells", P + "/manifest/cert-cells.json", S + "/cert-cells.c1c.json", "74a521d9884aa806b47b44e74b08df7a7f5299a21a340cc27df9d4d8aef6650a")]
BASE = ("graph-cert-baseline", P + "/manifest/cert-baseline.json", "4532b7911149b1dd283ca9a735b0e4a33b065bd8d894cdcaa78d4fa0e66bea2e")
STATE = ["current.json", "alarm.json", "incidents.jsonl", "last-good.json", "canary.json"]
B88 = "lark:88-phai-cu:b88"
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


def pre_write():
    os.makedirs(M + "/backup", mode=0o700, exist_ok=True)
    os.makedirs(CH, mode=0o700, exist_ok=True)
    rc, o, _ = sh(["incomex-config-status-v0"])
    if "STATUS=CLEAN" not in o:
        say("STOP Config Guard không CLEAN"); return 3
    for t, live, cand, want in T + [(BASE[0], BASE[1], None, BASE[2])]:
        cg = open("/var/lib/incomex-config-guard-v0/baseline/%s.sha256" % t).read().split()[0]
        if sha(live) != want or cg != want or (cand and not os.path.isfile(cand)):
            say("STOP đích lệch mốc PRE", t, sha(live)[:16], cg[:16]); return 3
    for t, live, cand, want in T + [(BASE[0], BASE[1], None, BASE[2])]:
        shutil.copy2(live, M + "/backup/%s.truoc" % t)
    for f in STATE:
        if os.path.exists(CERT + "/" + f):
            shutil.copy2(CERT + "/" + f, M + "/backup/cert-%s.truoc" % f)
    say("backup", [os.path.basename(x) for x in sorted(os.listdir(M + "/backup"))])
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


def stale_mcp():
    t_inst = os.stat(T[0][1]).st_mtime
    rc, o, _ = sh(["pgrep", "-f", "mcp-readonly-v1/bin/graph-v1 mcp"])
    hz = os.sysconf("SC_CLK_TCK")
    boot = float(open("/proc/stat").read().split("btime ")[1].split()[0])
    killed, kept = [], []
    for pid in [int(x) for x in o.split()]:
        try:
            st = open("/proc/%d/stat" % pid).read().rsplit(")", 1)[1].split()
            start = boot + int(st[19]) / hz
            kids = [int(x) for x in sh(["pgrep", "-P", str(pid)])[1].split()]
        except (OSError, IndexError, ValueError):
            continue
        if start < t_inst:
            for k in kids:
                try:
                    os.kill(k, signal.SIGTERM)
                except OSError:
                    pass
            os.kill(pid, signal.SIGTERM)
            killed.append({"pid": pid, "started": time.strftime("%FT%TZ", time.gmtime(start)), "children": kids})
        else:
            kept.append(pid)
    time.sleep(2)
    left = [k["pid"] for k in killed if os.path.exists("/proc/%d" % k["pid"])]
    say("stale-mcp dừng", killed, "giữ (mới hơn bản cài)", kept, "còn sống", left)
    return 0 if not left else 1


def gc_lib(path):
    ldr = importlib.machinery.SourceFileLoader("graph_cert_inst", path)
    m = importlib.util.module_from_spec(importlib.util.spec_from_loader("graph_cert_inst", ldr))
    ldr.exec_module(m)
    return m


def baseline():
    G = gc_lib(T[0][1])
    sys.path.insert(0, P + "/bin/refresh")
    import r7_g1lib
    g = r7_g1lib.load(P + "/bin/graph-v1")
    pw = g.password()
    doc = json.load(open(CERT + "/current.json"))
    ok, why = G.verify_manifest(doc)
    eff, _ = G.effective(doc)
    fence = G.graph_fence(doc, lambda: G.graph_epoch(g, pw), "auto")
    inv = g.invariants(pw)
    man = json.load(open(P + "/manifest/graph-invariants.json"))
    pins = json.load(open(P + "/manifest/pins.json"))
    rm = json.load(open(P + "/manifest/recovery-manifest.json"))
    rec_ok = sha(P + "/backups/recovery/current/meta.json") == (rm.get("current") or {}).get("meta_sha256")
    chk = {"manifest_ok": ok, "b88_du": (eff.get(B88) or ("",))[0] == G.DU, "fence": fence["status"], "inv_eq_manifest": not g.inv_equal(inv, man),
           "pins_point_to_invariants": (pins.get("files") or {}).get(P + "/manifest/graph-invariants.json") == sha(P + "/manifest/graph-invariants.json"),
           "recovery_eq_manifest": rec_ok, "b88_proof": (doc["cells"].get(B88) or {}).get("proof"), "b88_source": (doc["cells"].get(B88) or {}).get("source")}
    say("baseline kiểm b88", json.dumps(chk, ensure_ascii=False)[:600])
    if not all(chk[k] for k in ("manifest_ok", "b88_du", "inv_eq_manifest", "pins_point_to_invariants", "recovery_eq_manifest")) or chk["fence"] != "MATCH":
        say("STOP b88 không đủ điều kiện vào sàn ⇒ giữ pending/vàng"); return 3
    b = json.load(open(BASE[1]))
    if sha(BASE[1]) != BASE[2]:
        say("STOP baseline lệch mốc"); return 3
    b["certified_floor"] = sorted(set(b["certified_floor"]) | {B88})
    (b.get("pending_host_ack") or {}).pop(B88, None)
    b["yellow_repeat_hours"] = 168
    b["record_only_gates"] = []
    b.setdefault("notes", {})["C1C"] = (
        "%s: (1) %s vào sàn — giấy v4 ĐỦ (%s; nguồn %s) + hàng rào phiên bản MATCH + invariants sống = manifest + pins trỏ đúng + điểm khôi phục = "
        "manifest (PROMPT C1-C §5, Host P218); tụt ⇒ #24 ĐỎ COVERAGE_REGRESSION. (2) yellow_repeat_hours 168: VÀNG (nguồn mới/biến mất/ô chưa nhận mốc) "
        "gọi trang MỘT lượt khi xuất hiện rồi nhắc mỗi 168h (Alertmanager repeat). (3) record_only_gates []: directory so CẢ 9 cửa (G9 không còn chỉ ghi sổ). "
        "accepted_directory_parents KHÔNG đổi — cha mới do C1-C thấy (loại unit/cổng nghe/kho git) chờ Host nhận." % (
            RUN, B88, (chk["b88_proof"] or "")[:60], json.dumps({k: (chk["b88_source"] or {}).get(k) for k in ("objects_count", "edges_count", "snapshot")},
                                                               ensure_ascii=False)[:160]))
    b["written_by"], b["written_at"] = RUN, now()
    c = CH + "/cert-baseline.json"
    json.dump(b, open(c, "w"), ensure_ascii=False, indent=1, sort_keys=True)
    os.chmod(c, 0o600)
    ok, out = apply_v0(BASE[0], BASE[1], c)
    say("apply-v0", BASE[0], out, "floor+b88 =%d" % len(b["certified_floor"]), sha(BASE[1])[:16])
    return 0 if ok else 1


def rollback():
    bad = 0
    for t, live, *_ in [BASE] + list(reversed(T)):
        bk = M + "/backup/%s.truoc" % t
        if os.path.exists(bk) and sha(live) != sha(bk):
            c = CH + "/rb-" + os.path.basename(live)
            shutil.copyfile(bk, c)
            os.chmod(c, 0o600)
            ok, out = apply_v0(t, live, c)
            say("rollback", t, out, sha(live)[:16])
            bad += 0 if ok else 1
    for f in STATE:
        bk = M + "/backup/cert-%s.truoc" % f
        if os.path.exists(bk):
            tmp = CERT + "/" + f + ".rb"
            shutil.copy2(bk, tmp)
            os.replace(tmp, CERT + "/" + f)
    say("rollback trạng thái giấy (.truoc) đặt lại", STATE, "· inventory.json (v4) giữ — v3 không đọc")
    return 0 if not bad else 1


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    fn = {"pre-write": pre_write, "stale-mcp": stale_mcp, "baseline": baseline, "rollback": rollback}.get(cmd)
    if not fn:
        print("dùng: c1c_install.py pre-write|stale-mcp|baseline|rollback"); sys.exit(2)
    sys.exit(fn())
