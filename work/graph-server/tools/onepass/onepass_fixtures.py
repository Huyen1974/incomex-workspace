#!/usr/bin/env python3
"""GS-ALL-SOURCE-ONEPASS-DISCOVERY-AUDIT-20261030-01 · CP2 negative fixtures (chạy trên Mac, bản sao graph_cert.py production).

Mỗi ca: dựng nguồn giả có chủ đích → gọi đúng bộ đọc/hàm chấm của graph_cert → so với kỳ vọng ngành
(DISABLED≠ABSENT, lỗi lệnh ≠ rỗng, include nginx không mất, .socket/.path/drop-in có mặt, kho ngoài /opt/incomex có mặt …).
KQ: PASS = graph_cert đã xử lý đúng · GAP = graph_cert cho kết quả sai/thiếu (ghi nguyên nhân).
Cách chạy: python3 -I onepass_fixtures.py <đường graph_cert.py>
"""
import importlib.util, json, os, sys, tempfile, types

spec = importlib.util.spec_from_file_location("graph_cert_copy", sys.argv[1])
G = importlib.util.module_from_spec(spec)
spec.loader.exec_module(G)
REAL_OS, REAL_OPEN = G.os, open
RESULTS = []


def rec(case, verdict, observed, expected, cause=""):
    RESULTS.append({"case": case, "verdict": verdict, "observed": observed, "expected": expected, "cause": cause})


class Remap:
    """Chuyển đường tuyệt đối sang cây tạm (os.listdir/isdir/isfile/islink/path.join/open)."""
    def __init__(self, root):
        self.root = root
        self.path = types.SimpleNamespace(**{k: getattr(REAL_OS.path, k) for k in dir(REAL_OS.path) if not k.startswith("__")})
        for fn in ("isdir", "isfile", "islink", "exists"):
            setattr(self.path, fn, (lambda f: (lambda p: f(self.m(p))))(getattr(REAL_OS.path, fn)))
        self.path.join = REAL_OS.path.join
        self.path.dirname = REAL_OS.path.dirname

    def m(self, p):
        return self.root + p if isinstance(p, str) and p.startswith("/") else p

    def listdir(self, p):
        return REAL_OS.listdir(self.m(p))

    def __getattr__(self, k):
        return getattr(REAL_OS, k)


def with_tree(files):
    root = tempfile.mkdtemp(prefix="gsfx-")
    for p, body in files.items():
        full = root + p
        REAL_OS.makedirs(REAL_OS.path.dirname(full), exist_ok=True)
        with REAL_OPEN(full, "w") as f:
            f.write(body)
    sh = Remap(root)
    G.os = sh
    G.open = lambda p, *a, **k: REAL_OPEN(sh.m(p), *a, **k)
    return root


def reset():
    G.os = REAL_OS
    if hasattr(G, "open"):
        del G.open


# ---------------------------------------------------------------- F1 cron: dòng bị comment-tắt ≠ dòng đã xoá
base = "SHELL=/bin/sh\n3 * * * * /opt/incomex/scripts/a.sh\n*/10 * * * * /opt/incomex/dot/bin/dot-pivot-refresh\n"
off = "SHELL=/bin/sh\n3 * * * * /opt/incomex/scripts/a.sh\n#L1-OFF-VPSC-L1-CRON-OFF-20261013-01 */10 * * * * /opt/incomex/dot/bin/dot-pivot-refresh\n"
gone = "SHELL=/bin/sh\n3 * * * * /opt/incomex/scripts/a.sh\n"
res = {}
for name, body in (("active", base), ("disabled", off), ("deleted", gone)):
    with_tree({"/var/spool/cron/crontabs/root": body, "/etc/crontab": ""})
    res[name] = G.cron_read()
    reset()
same = res["disabled"]["entries"] == res["deleted"]["entries"] and res["disabled"]["edges"] == res["deleted"]["edges"]
rec("F1 cron DISABLED≠ABSENT", "GAP" if same else "PASS",
    {k: len(v["entries"]) for k, v in res.items()}, "disabled giữ dòng với trạng thái DISABLED + thẻ tắt",
    "cron_read bỏ mọi dòng bắt đầu '#' ⇒ tắt có chủ đích và đã xoá cho cùng tập đối tượng; chỉ cron_files_read (băm tệp) thấy đổi" if same else "")

# ---------------------------------------------------------------- F2 cron: crontab của user khác root
with_tree({"/var/spool/cron/crontabs/root": "1 * * * * /x/root.sh\n", "/var/spool/cron/crontabs/incomex": "2 * * * * /x/user.sh\n", "/etc/crontab": ""})
r = G.cron_read(); reset()
users = sorted({e[0].split("|")[0] for e in r["entries"]})
rec("F2 cron mọi user spool", "PASS" if any("incomex" in u for u in users) else "GAP", users, "cả root lẫn incomex")

# ---------------------------------------------------------------- F3 cron: tệp không đọc được ⇒ NO_ACCESS (không phải rỗng)
root = with_tree({"/var/spool/cron/crontabs/root": "1 * * * * /x/a.sh\n", "/etc/crontab": ""})
REAL_OS.chmod(root + "/var/spool/cron/crontabs/root", 0)
r = G.cron_read(); reset()
S = types.SimpleNamespace(get=lambda n: r if n == "cron" else {}, cache={"cron_after": r})
src = G.source_for({"key": "cron:entry", "gate": "G4", "source": {"adapter": "cron"}}, S)
ok = (not src["ok"]) and src.get("access") == "NO_ACCESS"
if REAL_OS.geteuid() == 0:
    rec("F3 cron NO_ACCESS", "SKIP", "chạy bằng root, chmod 0 không chặn", "NO_ACCESS")
else:
    rec("F3 cron NO_ACCESS", "PASS" if ok else "GAP", {"ok": src["ok"], "access": src.get("access")}, "ok=False access=NO_ACCESS")

# ---------------------------------------------------------------- F4 nginx: proxy_pass trong tệp include bị nginx -T in ngoài khối server
NG = """# configuration file /etc/nginx/conf.d/default.conf:
server {
    listen 443 ssl;
    server_name a.example;
    location /app { proxy_pass http://nuxt:3000; }
    location / {
        proxy_pass http://nuxt:3000;
    }
    include /etc/nginx/secrets/route.conf;
}

# configuration file /etc/nginx/secrets/route.conf:
location /SECRET-PATH/mcp {
    proxy_pass http://incomex-claude-mcp:8000;
}
"""
G_sh = G.sh
G.sh = lambda cmd, *a, **k: (0, NG, "")
r = G.nginx_read()
G.sh = G_sh
targets = sorted(e[2] for e in r["edges"])
missing_include = "http://incomex-claude-mcp:8000" not in targets
missing_oneline = targets.count("http://nuxt:3000") < 2
rec("F4 nginx include + location một dòng", "GAP" if (missing_include or missing_oneline) else "PASS", targets,
    "3 cạnh PROXIES (2 nuxt + 1 claude-mcp)",
    ("INCLUDE_CONTEXT_LOST: nginx -T in tệp include sau khối server, bộ đọc chỉ nhận proxy_pass khi đang trong 'server {' ⇒ mất tuyến connector; " if missing_include else "") +
    ("ONE_LINE_LOCATION: 'location … { proxy_pass …; }' một dòng không khớp ^proxy_pass" if missing_oneline else ""))

# ---------------------------------------------------------------- F5 systemd: .socket/.path/drop-in
with_tree({"/etc/systemd/system/a.service": "[Service]\nExecStart=/usr/bin/a\n",
           "/etc/systemd/system/a.socket": "[Socket]\nListenStream=127.0.0.1:1\n",
           "/etc/systemd/system/b.path": "[Path]\nPathChanged=/x\nUnit=b.service\n",
           "/etc/systemd/system/a.service.d/override.conf": "[Service]\nExecStart=\nExecStart=/opt/x/real-a\n"})
r = G.systemd_read(); reset()
units = sorted(u[0] for u in r["units"])
execs = sorted(e[2] for e in r["edges"] if e[1] == "EXECS")
gap = ("a.socket" not in units) or ("b.path" not in units) or ("/opt/x/real-a" not in execs)
rec("F5 systemd socket/path/drop-in", "GAP" if gap else "PASS", {"units": units, "execs": execs},
    "a.service+a.socket+b.path; EXECS theo drop-in /opt/x/real-a",
    "systemd_read chỉ lấy .service/.timer tệp thường; bỏ drop-in *.d/ (ExecStart thật có thể nằm ở override)" if gap else "")

# ---------------------------------------------------------------- F6 docker images lỗi lệnh ⇒ rỗng ⇒ ĐỦ giả?
def fake_sh(cmd, *a, **k):
    if cmd[:2] == ["docker", "ps"]:
        return 0, "c1\tid1\n", ""
    if cmd[:2] == ["docker", "inspect"]:
        return 0, json.dumps({"Name": "/c1", "Image": "sha256:x", "Mounts": [], "HostConfig": {}}) + "\n", ""
    if cmd[:2] == ["docker", "images"]:
        return 1, "", "Cannot connect"
    return 0, "", ""
G.sh = fake_sh
d = G.docker_read()
G.sh = G_sh
S = types.SimpleNamespace(get=lambda n: d if n == "docker" else {}, cache={})
src = G.source_for({"key": "docker:image", "gate": "G2", "source": {"adapter": "docker", "part": "image"}}, S)
ev = G.evaluate({"key": "docker:image", "gate": "G2", "source": {"adapter": "docker", "part": "image"}}, src, {}, 1_800_000_000, 26)
rec("F6 lệnh docker images lỗi ⇒ không được ĐỦ", "GAP" if ev["status"] == G.DU else "PASS",
    {"docker_read.ok": d.get("ok"), "source_ok": src["ok"], "status": ev["status"], "proof": ev.get("proof")}, "MỘT PHẦN READER_FAIL",
    "docker_read trả ok=False nhưng source_for(docker) chỉ kiểm 'error' ⇒ tập rỗng ⇒ NATIVE_EMPTY_CLASS ⇒ ĐỦ GIẢ (FALSE_GREEN)" if ev["status"] == G.DU else "")

# ---------------------------------------------------------------- F7 PG lớp bị từ chối quyền ⇒ NO_ACCESS
S = types.SimpleNamespace(get=lambda n: {"directus": {"reader": {}, "classes": {"table": {"ok": False, "error": "NO_ACCESS InsufficientPrivilege"}}}} if n == "pg" else {}, cache={})
src = G.source_for({"key": "pg:directus:table", "gate": "G1", "source": {"adapter": "pg", "db": "directus", "classes": ["table"]}}, S)
rec("F7 PG NO_ACCESS", "PASS" if (not src["ok"] and src["access"] == "NO_ACCESS") else "GAP", {"ok": src["ok"], "access": src["access"]}, "NO_ACCESS")

# ---------------------------------------------------------------- F8 PG bảng mới trong DB cũ ⇒ kiểm kê thấy ADD
prev = {"kinds": {"directus.table": {"public.a": "h1"}, "directus.directus_flow": {"f1": "h"}}}
cur = {"kinds": {"directus.table": {"public.a": "h1", "public.new_t": "h2"}, "directus.directus_flow": {"f1": "h", "f2": "h"}}}
dif = G.inventory_diff(prev, cur)
rec("F8 bảng mới / flow mới ⇒ ADD", "PASS" if dif["added"].get("directus.table") == 1 and dif["added"].get("directus.directus_flow") == 1 else "GAP",
    dif["added"], "{directus.table:1, directus.directus_flow:1}",
    "phát hiện ở tầng kiểm kê/cảnh báo; KHÔNG có nút Graph cho flow (lớp chưa nạp) ⇒ thấy-mà-không-nạp")

# ---------------------------------------------------------------- F9 Qdrant scroll thiếu trang ⇒ READER_FAIL
S = types.SimpleNamespace(get=lambda n: {"incomex_metadata": {"reader": {}, "classes": {"kb": {"ok": True, "rows": [["k1", "d1", False, "ready"]]}}}} if n == "pg_kb"
                          else {"count_before": 5, "count_after": 5, "points_scrolled": 3, "scroll_complete": False, "doc_ids": ["d1"], "pages": 501}, cache={})
mb = G.mb_cell(S)
rec("F9 Qdrant scroll thiếu trang", "PASS" if (not mb["ok"] and "READER_FAIL" in mb.get("why", "")) else "GAP", mb.get("why"), "READER_FAIL")

# ---------------------------------------------------------------- F10 kho git ngoài /opt/incomex (vd /opt/incomex-cowork)
root = with_tree({"/opt/incomex/.git/HEAD": "x", "/opt/incomex-cowork/.git/HEAD": "x"})
import glob as _g
real_glob = _g.glob
_g.glob = lambda pat: [p[len(root):] for p in real_glob(root + pat)]
G.sh = lambda cmd, *a, **k: (0, "a" * 40 + "\n" + "b" * 40 + "\n", "")
r = G.git_repos_read()
G.sh = G_sh
_g.glob = real_glob
reset()
rec("F10 kho git ngoài /opt/incomex", "GAP" if "/opt/incomex-cowork" not in r["repos"] else "PASS", sorted(r["repos"]),
    "/opt/incomex + /opt/incomex-cowork", "git_repos_read chỉ glob /opt/incomex/** (sâu ≤3) ⇒ mã đang chạy coworkd/cowork-mcp ngoài phạm vi")

# ---------------------------------------------------------------- F11 Directus audit window LIMIT 500 (đếm cắt im)
q = G.PG_SCRIPT
rec("F11 truy vấn có LIMIT cứng", "GAP" if "LIMIT 500" in q else "PASS", "directus_audit_window … LIMIT 500", "phân trang hoặc cờ truncated",
    "chỉ là tín hiệu (SIGNAL_COUNTER_ONLY); >500 cặp collection/action ⇒ cắt im, không cờ truncated")

print(json.dumps(RESULTS, ensure_ascii=False, indent=1))
print("SUMMARY", {v: sum(1 for x in RESULTS if x["verdict"] == v) for v in ("PASS", "GAP", "SKIP")}, file=sys.stderr)
