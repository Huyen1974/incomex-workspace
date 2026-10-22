#!/usr/bin/env python3
# GS-C1A-CERT-QUALITYGATE-20261022-07 · cài C1-A trong MỘT cửa sổ VPS-GHI (Điều 30/31, apply-v0, Config Guard, sổ mã) + đường lùi.
#   install : (1) kiểm: Config Guard CLEAN · 3 đích sửa đúng mốc · 3 tệp mới chưa có
#             (2) 3 tệp mới (graph_cert.py · cert-cells.json · cert-baseline.json) + baseline Config Guard + apply-v0 sổ mã + registry
#             (3) apply-v0 graph-v1-mcp-wrapper (bọc nhãn N4) · graph-refresh-cli (giấy + đèn mỗi lượt)
#             (4) đèn Kuma push «Graph Certificate (C1-A)» qua socket chính thức (khuôn ensure-jev-gw-kuma-monitor.sh như đèn #23),
#                 interval 90000 s, maxretries 0, resendInterval 1, kênh #2; token kuma.db (chỉ-đọc) → /etc/incomex/kuma-push/graph-cert.token 0600
#             (5) nhịp THỬ (down, nhãn TIN THỬ) · apply-v0 mcpw-protection-guard (KUMA_MONITORS_EXPECTED +24 · TIN_BAO A24)
#             (6) kuma-push.sh cron (lượt thường của job — làm mới bảng đèn để total = fleet) · drift-check CLEAN · selftest/doctor
#   rollback: lùi theo thứ tự ngược (Guard → đèn deleteMonitor + token → wrapper/refresh → registry/sổ mã → baseline → tệp mới)
# Hỏng bất kỳ bước install ⇒ tự lùi. Exit 0 PASS · 1 FAIL đã lùi · 3 dừng trước ghi · 30 lùi chưa sạch
import hashlib, json, os, re, shutil, subprocess, sys, time

RUN = "GS-C1A-CERT-QUALITYGATE-20261022-07"
E = "/opt/incomex/work/graph-server/evidence/" + RUN
S, ST, M = E + "/scripts", E + "/stage", E + "/m"
P = "/opt/incomex/graph-server/prod-v1"
CG = "/var/lib/incomex-config-guard-v0"
REG = CG + "/registry.tsv"
LEDGER = "/opt/incomex/scripts/code-ledger.tsv"
MID = RUN + ".M"
CH = "/root/incomex-config-changes/" + MID
KDB = "/opt/incomex/uptime-kuma/kuma.db"
NAME = "Graph Certificate (C1-A)"
TOKF = "/etc/incomex/kuma-push/graph-cert.token"
TEMPLATE = "/opt/incomex/scripts/ensure-jev-gw-kuma-monitor.sh"
NEW = [("graph-refresh-lib-cert", P + "/bin/refresh/graph_cert.py", S + "/graph_cert.py", "HOST_SCRIPT", "PYTHON_SYNTAX", "644"),
       ("graph-cert-cells", P + "/manifest/cert-cells.json", S + "/cert-cells.json", "HOST_CONFIG", "JSON", "644"),
       ("graph-cert-baseline", P + "/manifest/cert-baseline.json", S + "/cert-baseline.json", "HOST_CONFIG", "JSON", "644")]
MOD = [("graph-v1-mcp-wrapper", "/opt/incomex/graph-server/mcp-readonly-v1/bin/graph-v1", ST + "/graph-v1-mcp.new",
        "d13f83b5b91c0a9f238c6940f1685899b7997e8fa681d7a414a2e65d71095228"),
       ("graph-refresh-cli", P + "/bin/graph-refresh", ST + "/graph-refresh.new", "97b4e4a8ac46933454713d1f8cabc1c16db77cddad3696814aa1473b927a1ed6"),
       ("mcpw-protection-guard", "/opt/incomex/scripts/mcpw-protection-guard", ST + "/guard.new",
        "125cfec2acfbc5ae711eb61ab34f5c84fb6333196653daea7b1339804ae2e9bb")]
now = lambda: time.strftime("%FT%TZ", time.gmtime())
LOG = M + "/install.log"


def say(*a):
    line = now() + " " + " ".join(str(x) for x in a)
    print(line, flush=True)
    with open(LOG, "a") as f:
        f.write(line + "\n")


def sh(cmd, timeout=300, inp=None, env=None):
    p = subprocess.run(cmd, capture_output=True, timeout=timeout, input=inp, env=env)
    return p.returncode, p.stdout.decode(errors="replace"), p.stderr.decode(errors="replace")


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def ro(q):
    return sh(["sqlite3", "-separator", "|", "file:%s?mode=ro" % KDB, q])[1].strip()


def apply_v0(target, live, cand):
    rc, o, e = sh(["incomex-config-apply-v0", "--mutation-id", MID, "--agent", "claude-code-cli", "--target-id", target, "--candidate", cand,
                   "--expected-baseline", sha(live)], timeout=180)
    out = " ".join(l for l in (o + e).splitlines() if l.startswith(("RESULT=", "REASON=")))
    return rc == 0 and "RESULT=APPLIED" in out and sha(live) == sha(cand), out


def kuma_node(js, extra_env):
    """Chạy đoạn node trong container uptime-kuma với khoá ký phiên lấy từ kuma.db (chỉ-đọc), env-file tmpfs, không in."""
    row = ro("select (select value from setting where key='jwtSecret' limit 1),(select username from user where active=1 order by id limit 1),"
             "(select password from user where active=1 order by id limit 1);")
    js_, au, ph = (row.split("|") + ["", "", ""])[:3]
    if not (js_ and au and ph):
        return 8, "", "no auth material"
    f = "/dev/shm/gs-c1a-kuma.%d" % os.getpid()
    fd = os.open(f, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, "w") as h:
        h.write("KUMA_JWT_SECRET=%s\nKUMA_AUTH_USER=%s\nKUMA_PASSWORD_HASH=%s\n" % (js_, au, ph))
    try:
        cmd = ["docker", "exec", "-i", "--env-file", f]
        for k, v in extra_env.items():
            cmd += ["-e", "%s=%s" % (k, v)]
        return sh(cmd + ["uptime-kuma", "node", "-"], inp=js.encode(), timeout=60)
    finally:
        sh(["shred", "-u", f])


DELETE_JS = r'''
const { io } = require("socket.io-client"); const jwt = require("jsonwebtoken");
const { localWebSocketURL } = require("/app/server/config"); const { shake256, SHAKE256_LENGTH } = require("/app/server/util-server");
const emit = (s, e, p) => new Promise(r => s.emit(e, p, x => r(x)));
const tok = jwt.sign({ username: process.env.KUMA_AUTH_USER, h: shake256(process.env.KUMA_PASSWORD_HASH, SHAKE256_LENGTH) }, process.env.KUMA_JWT_SECRET);
const s = io(localWebSocketURL, { reconnection: false, timeout: 5000 }); const t = setTimeout(() => process.exit(8), 20000);
s.once("connect", async () => { const l = await emit(s, "loginByToken", tok); if (!l || !l.ok) process.exit(8);
  const p = await emit(s, "deleteMonitor", Number(process.env.MID)); console.log(JSON.stringify(p)); clearTimeout(t); s.close(); process.exit(p && p.ok ? 0 : 8); });
s.once("connect_error", () => process.exit(8));
'''


def push(status, msg):
    import urllib.parse, urllib.request
    tok = open(TOKF).read().strip()
    q = urllib.parse.urlencode({"status": status, "msg": msg, "ping": ""})
    with urllib.request.urlopen("http://127.0.0.1:3001/api/push/" + tok + "?" + q, timeout=15) as r:
        return json.loads(r.read().decode() or "{}").get("ok")


def state():
    return json.load(open(M + "/done.json")) if os.path.exists(M + "/done.json") else {}


def save(d):
    json.dump(d, open(M + "/done.json", "w"), indent=1)


def install():
    os.makedirs(M + "/backup", mode=0o700, exist_ok=True)
    os.makedirs(CH, mode=0o700, exist_ok=True)
    rc, o, _ = sh(["incomex-config-status-v0"])
    if "STATUS=CLEAN" not in o:
        say("STOP Config Guard không CLEAN"); return 3
    reg, led = open(REG).read(), open(LEDGER).read()
    for t, live, src, *_ in NEW:
        if os.path.exists(live) or ("\n%s\t" % t) in reg or os.path.exists(CG + "/baseline/%s.sha256" % t) or ("\n%s\t" % live) in led or not os.path.isfile(src):
            say("STOP tệp mới đã có/thiếu nguồn", t); return 3
    for t, live, cand, want in MOD:
        if sha(live) != want or open(CG + "/baseline/%s.sha256" % t).read().split()[0] != want or not os.path.isfile(cand):
            say("STOP đích lệch mốc", t, sha(live)[:16]); return 3
    if ro("select count(*) from monitor where name='%s';" % NAME) != "0" or os.path.exists(TOKF):
        say("STOP đèn/token đã có"); return 3
    shutil.copy2(REG, M + "/backup/registry.tsv.truoc")
    shutil.copy2(LEDGER, M + "/backup/code-ledger.tsv.truoc")
    for t, live, cand, want in MOD:
        shutil.copy2(live, M + "/backup/%s.truoc" % t)
    d = {"files": [], "baselines": [], "ledger": False, "registry": False, "mod": [], "monitor": None, "token": False, "steps": []}
    save(d)
    try:
        for t, live, src, fc, val, mode in NEW:                                   # (2) tệp mới
            shutil.copyfile(src, live)
            os.chown(live, 0, 0)
            os.chmod(live, int(mode, 8))
            d["files"].append(live)
            bd = CG + "/baseline/"
            shutil.copy2(live, bd + t + ".content"); os.chmod(bd + t + ".content", 0o600)
            open(bd + t + ".sha256", "w").write(sha(live) + "\n"); os.chmod(bd + t + ".sha256", 0o600)
            open(bd + t + ".meta", "w").write("root:root %s\n" % mode); os.chmod(bd + t + ".meta", 0o600)
            d["baselines"].append(t)
        save(d)
        lines = led.splitlines(True)
        head = [l for l in lines if l.startswith("#")]
        body = sorted([l for l in lines if not l.startswith("#")] + ["%s\tLOCKED\t%s\tGS-C1A:graph-cert\n" % (live, t) for t, live, *_ in NEW],
                      key=lambda x: x.split("\t", 1)[0].encode())
        open(CH + "/code-ledger.tsv", "w").write("".join(head + body)); os.chmod(CH + "/code-ledger.tsv", 0o600)
        ok, out = apply_v0("r7-code-ledger-tsv", LEDGER, CH + "/code-ledger.tsv")
        say("apply-v0 r7-code-ledger-tsv", out)
        if not ok:
            raise RuntimeError("code-ledger")
        d["ledger"] = True; save(d)
        rows = ["# %s (graph-server C1-A, Điều 30/31): máy cấp giấy ĐỦ/MỘT PHẦN (graph_cert) + danh mục ô + mốc đèn #24. Đổi chỉ qua apply-v0.\n" % RUN,
                "#   Rollback: c1a_install.py rollback trong thư mục bằng chứng RUN (bản trước ở rollback/ của guard-registry).\n"]
        rows += ["%s\t%s\t%s\tNO\tPRIVATE_COPY\t%s\tNONE\troot:root\t%s\n" % (t, live, fc, val, mode) for t, live, src, fc, val, mode in NEW]
        open(CH + "/registry.tsv", "w").write(reg + ("" if reg.endswith("\n") else "\n") + "".join(rows)); os.chmod(CH + "/registry.tsv", 0o600)
        ok, out = apply_v0("guard-registry", REG, CH + "/registry.tsv")
        say("apply-v0 guard-registry", out)
        if not ok:
            raise RuntimeError("guard-registry")
        d["registry"] = True; save(d)
        for t, live, cand, want in MOD[:2]:                                     # (3) wrapper + refresh
            c = CH + "/" + t
            shutil.copyfile(cand, c); os.chmod(c, 0o600)
            ok, out = apply_v0(t, live, c)
            say("apply-v0", t, out)
            if not ok:
                raise RuntimeError(t)
            d["mod"].append(t); save(d)
        # (4) đèn Kuma theo khuôn #23
        tpl = open(TEMPLATE).read()
        for old, new in (('MONITOR_NAME="JEV Gateway"', 'MONITOR_NAME="%s"' % NAME), ("resendInterval: 0,", "resendInterval: 1,")):
            assert tpl.count(old) == 1, old
            tpl = tpl.replace(old, new)
        tpl, k = re.subn(r"PUSH_INTERVAL_SECONDS=\d+", "PUSH_INTERVAL_SECONDS=90000", tpl, count=1); assert k == 1
        tpl, k = re.subn(r"maxretries: 0,", "maxretries: 0,", tpl, count=1); assert k == 1
        tpl, k = re.subn(r'description: "[^"]*"', 'description: "GS C1-A (%s): graph-refresh moi luot (timer 22:40 UTC, ca luot bo qua) day up/down. '
                         'DOWN = luot bo qua, may cap giay loi, bo doc nguon hong, o thuoc san DU tut, nguon moi/mat o 9 cua. Im >90000s = timer/may chet. '
                         'Xu ly: Graph Host doc prod-v1/state/refresh/cert/current.json + incidents.jsonl."' % RUN, tpl, count=1); assert k == 1
        tf = "/dev/shm/gs-c1a-ensure.%d" % os.getpid()
        fd = os.open(tf, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o700)
        with os.fdopen(fd, "w") as h:
            h.write(tpl)
        rc, o, e = sh(["bash", tf], timeout=120)
        sh(["shred", "-u", tf])
        mid = ro("select id from monitor where name='%s' limit 1;" % NAME)
        say("ensure monitor rc=%s id=%s" % (rc, mid), (o + e).strip().splitlines()[-1][:160] if (o + e).strip() else "")
        if rc != 0 or not mid.isdigit():
            raise RuntimeError("ensure monitor")
        d["monitor"] = int(mid); save(d)
        tok = ro("select push_token from monitor where id=%s;" % mid)
        if not re.fullmatch(r"[A-Za-z0-9_-]+", tok or ""):
            raise RuntimeError("push token")
        os.makedirs(os.path.dirname(TOKF), mode=0o700, exist_ok=True)
        fd = os.open(TOKF, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
        with os.fdopen(fd, "w") as h:
            h.write(tok + "\n")
        tok = None
        d["token"] = True; save(d)
        cfg = ro("select id,name,type,active,interval,maxretries,resend_interval,(select group_concat(notification_id) from monitor_notification n "
                 "where n.monitor_id=m.id) from monitor m where id=%s;" % mid)
        say("monitor", cfg)
        if not cfg.endswith("|2") or "|push|1|90000|0|1|" not in cfg:
            raise RuntimeError("cấu hình đèn lệch " + cfg)
        ok = push("down", "TIN THỬ C1-A (không phải sự cố): kiểm đường đèn #%s → Telegram; lượt cấp giấy thật đẩy trạng thái thật ngay sau" % mid)
        time.sleep(3)
        hb = ro("select time||'|'||status||'|'||important||'|'||coalesce(msg,'') from heartbeat where monitor_id=%s order by id desc limit 1;" % mid)
        say("nhịp THỬ ok=%s" % ok, hb[:200])
        d["test_beat"] = hb; save(d)
        if not ok or "|0|1|" not in hb:
            raise RuntimeError("nhịp thử không lưu/không important")
        c = CH + "/mcpw-protection-guard"                                       # (5) Guard
        shutil.copyfile(MOD[2][2], c); os.chmod(c, 0o600)
        ok, out = apply_v0("mcpw-protection-guard", MOD[2][1], c)
        say("apply-v0 mcpw-protection-guard", out)
        if not ok:
            raise RuntimeError("guard")
        d["mod"].append("mcpw-protection-guard"); save(d)
        rc, o, e = sh(["/opt/incomex/scripts/kuma-push.sh", "cron"], timeout=120)   # (6) lượt thường của job: bảng đèn total = fleet
        bd_ = json.load(open("/opt/incomex/logs/bang-den.json"))
        say("kuma-push.sh cron rc=%s · bảng đèn total=%s up=%s at=%s" % (rc, bd_.get("total"), bd_.get("up"), bd_.get("generated_at")))
        rc, o, e = sh(["incomex-config-drift-check", "--quiet"], timeout=300)
        rc2, o2, _ = sh(["incomex-config-status-v0"])
        say("drift-check rc=%s" % rc, " ".join(l for l in o2.splitlines() if l.startswith(("STATUS", "TRACKED_FILE_COUNT"))))
        if "STATUS=CLEAN" not in o2:
            raise RuntimeError("Config Guard không CLEAN")
        rc, o, e = sh([P + "/bin/graph-refresh", "selftest"], timeout=120)
        say("graph-refresh selftest rc=%s" % rc, (o + e).strip().splitlines()[-1] if (o + e).strip() else "")
        rc2, o2, e2 = sh(["/opt/incomex/graph-server/mcp-readonly-v1/bin/graph-v1", "doctor"], timeout=180)
        say("graph-v1 doctor rc=%s" % rc2, (json.loads(o2).get("verdict") if o2.strip().startswith("{") else o2[-120:]))
        if rc != 0 or rc2 != 0:
            raise RuntimeError("selftest/doctor")
        d["result"] = "INSTALL_PASS"; save(d)
        json.dump({"result": "INSTALL_PASS", "at": now(), "files": {l: sha(l) for _, l, *_ in NEW} | {l: sha(l) for _, l, *_ in MOD},
                   "monitor": cfg}, open(M + "/install-result.json", "w"), ensure_ascii=False, indent=1)
        return 0
    except Exception as e:  # noqa: BLE001
        say("FAIL", type(e).__name__, str(e)[:300], "⇒ lùi")
        return rollback()


def rollback():
    d = state()
    bad = []
    for t, live, cand, want in reversed(MOD):
        if t in d.get("mod", []) and sha(live) != want:
            c = CH + "/%s.rollback" % t
            shutil.copy2(M + "/backup/%s.truoc" % t, c); os.chmod(c, 0o600)
            ok, out = apply_v0(t, live, c); say("lùi", t, out); bad += [] if ok else [t]
    if d.get("monitor"):
        rc, o, e = kuma_node(DELETE_JS, {"MID": str(d["monitor"])})
        say("lùi đèn deleteMonitor #%s rc=%s" % (d["monitor"], rc), o.strip()[:120])
        bad += [] if rc == 0 else ["monitor"]
    if d.get("token") or os.path.exists(TOKF):
        sh(["shred", "-u", TOKF])
    if d.get("registry") and sha(REG) != sha(M + "/backup/registry.tsv.truoc"):
        c = CH + "/registry.rollback.tsv"
        shutil.copy2(M + "/backup/registry.tsv.truoc", c); os.chmod(c, 0o600)
        ok, out = apply_v0("guard-registry", REG, c); say("lùi guard-registry", out); bad += [] if ok else ["registry"]
    if d.get("ledger") and sha(LEDGER) != sha(M + "/backup/code-ledger.tsv.truoc"):
        c = CH + "/code-ledger.rollback.tsv"
        shutil.copy2(M + "/backup/code-ledger.tsv.truoc", c); os.chmod(c, 0o600)
        ok, out = apply_v0("r7-code-ledger-tsv", LEDGER, c); say("lùi code-ledger", out); bad += [] if ok else ["ledger"]
    for t in d.get("baselines", []):
        for ext in (".content", ".sha256", ".meta"):
            try:
                os.remove(CG + "/baseline/" + t + ext)
            except OSError:
                pass
    for live in d.get("files", []):
        try:
            os.remove(live)
        except OSError:
            pass
    sh(["/opt/incomex/scripts/kuma-push.sh", "cron"], timeout=120)
    rc, o, _ = sh(["incomex-config-drift-check", "--quiet"], timeout=300)
    rc, o, _ = sh(["incomex-config-status-v0"])
    clean = "STATUS=CLEAN" in o and not bad
    d["rollback"] = {"at": now(), "clean": clean, "bad": bad}
    save(d)
    say("rollback xong clean=%s bad=%s" % (clean, bad))
    return 1 if clean else 30


if __name__ == "__main__":
    os.makedirs(M, mode=0o700, exist_ok=True)
    sys.exit(install() if sys.argv[1:] == ["install"] else rollback() if sys.argv[1:] == ["rollback"] else 2)
