#!/usr/bin/env python3
"""graph_cert — MÁY CẤP GIẤY «ĐỦ tại T» + NHÃN N4 cho Graph production v1 · GS-C1A-CERT-QUALITYGATE-20261022-07 (CT1–CT6)

Thư viện của graph-refresh (gọi trong mọi lượt timer, kể cả lượt SKIP) và của cổng đọc MCP graph-v1 (nhãn mỗi câu trả lời).
Không ghi Neo4j/PG/Directus/Qdrant/Lark: mọi nguồn đọc bằng công cụ gốc (catalog PG qua vai chỉ-đọc context_pack_readonly trong
container incomex-claude-mcp, docker/systemd/cron/nginx -T, GET/scroll Qdrant trong incomex-agent-data, LarkReader, git), Graph đọc
độc lập bằng Cypher phân trang theo gs_key (không LIMIT cắt cụt, có tổng đếm riêng). Không dùng đầu ra bộ nạp.

CT1  ô = (nguồn × loại) trong manifest/cert-cells.json (Config Guard); ô thư mục `directory` kiểm kê 9 cửa G1–G9 độc lập.
CT2  mỗi ô hai đầu: số + SHA256 (CANON-V1) của đối tượng và cạnh; bằng nhau về số chưa bao giờ là đạt.
CT3  ĐỦ chỉ khi: đọc nguồn trọn + quyền + nhất quán (PG REPEATABLE READ; nguồn khác dấu vân tay trước = sau), đọc Graph trọn
     (tổng đếm = số trang), số + băm đối tượng VÀ mọi loại cạnh khai cho ô khớp, cạnh có provenance; 0/0 chỉ khi bộ đọc gốc
     đọc trọn chứng minh lớp rỗng. Hạn ≤ 26 h. Mọi thứ khác ⇒ MỘT PHẦN (không cần biết lý do).
CT4  label_for(): nhãn = ô kém nhất câu hỏi cần (danh mục loại truy vấn có phiên bản); mặc định MỘT PHẦN/NOT_ACTION_SAFE.
CT5  alarm(): DOWN khi máy không chạy được/đọc nguồn hỏng/lượt bỏ qua (OPERATIONAL) hoặc tụt so với mốc đã nhận
     (manifest/cert-baseline.json, chỉ để dập tin trùng — không bao giờ làm ô xanh) hoặc nguồn mới ở cửa (NEW_SOURCE_UNHANDLED).
Giấy này là bằng chứng kiểm định Graph khớp nguồn tại T trong phạm vi ô — KHÔNG phải chứng thư mật mã, KHÔNG chứng minh nguồn
phản ánh hết thực tế (SQL động, quyết định nói miệng, lệnh gõ tay một lần ⇒ ô MỞ/UNKNOWN).

CLI (chỉ đọc nguồn + Graph; ghi duy nhất tệp trạng thái state/refresh/cert/*):
  graph_cert.py run [--cells k1,k2] [--b88-input DIR] [--no-write] [--out F] [--mb-ids-out F]
  graph_cert.py status                       nhãn hiệu lực từng ô tại giờ hiện tại
  graph_cert.py label --query CYPHER [--rows N] [--tool read-cypher|get-schema]
Exit: 0 ok · 1 lỗi chạy · 2 tham số
"""
import calendar, hashlib, json, os, re, struct, subprocess, sys, time

ROOT = "/opt/incomex/graph-server/prod-v1"
MAN = ROOT + "/manifest"
CELLS = os.environ.get("GS_CERT_CELLS") or MAN + "/cert-cells.json"          # biến môi trường chỉ cho fixture/diễn tập
BASELINE = os.environ.get("GS_CERT_BASELINE") or MAN + "/cert-baseline.json"
CERT_DIR = os.environ.get("GS_CERT_DIR") or ROOT + "/state/refresh/cert"
CURRENT = CERT_DIR + "/current.json"
LAST_GOOD = CERT_DIR + "/last-good.json"
INCIDENTS = CERT_DIR + "/incidents.jsonl"
ALARM_STATE = CERT_DIR + "/alarm.json"
FORMAT = "graph-cert-manifest-v1"
LABEL_FORMAT = "graph-completeness-label-v1"
DU, MP = "ĐỦ tại T", "MỘT PHẦN"
ACT_OK, ACT_NO = "ACTIONABLE_ONLY_WITH_FRESH_PROOF", "NOT_ACTION_SAFE"
MAX_TTL_H = 26
CONSISTENT = ("PG_REPEATABLE_READ_READ_ONLY", "BEFORE_AFTER_EQUAL", "FREEZE_SHA256", "GIT_COMMIT")
CLOCK_SKEW = 300
GRAPH_PAGE = 2000
SAMPLE = 5
LARK_PY = "/opt/incomex/lark-client/.venv/bin/python"
RB = ROOT + "/bin/refresh"
G1 = ROOT + "/bin/graph-v1"
GW_CLONE = "/opt/incomex/data/workspace-tools/github-workspace"
DOT = "/opt/incomex/dot"
LEDGER = "/opt/incomex/scripts/code-ledger.tsv"
BASES = "/opt/incomex/lark-client/config/bases.yaml"
BAK = r"\.(bak|pre)[-.]|\.stage0-frozen|\.[0-9]{8}T[0-9]{6}Z$"   # luật nhãn dot/bin LBL-2 (cùng đặc tả R6D/R7, viết lại độc lập)
now_iso = lambda t=None: time.strftime("%FT%TZ", time.gmtime(t if t is not None else time.time()))


def parse_iso(s):
    try:
        return calendar.timegm(time.strptime(str(s)[:19], "%Y-%m-%dT%H:%M:%S"))
    except (TypeError, ValueError):
        return None


def jload(p, d=None):
    try:
        with open(p, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return d


def sh(cmd, inp=None, timeout=300, env=None):
    try:
        p = subprocess.run(cmd, input=inp, capture_output=True, timeout=timeout, env=env)
        return p.returncode, p.stdout.decode(errors="replace"), p.stderr.decode(errors="replace")
    except (OSError, subprocess.TimeoutExpired) as e:
        return 124, "", type(e).__name__


# =========================================================================== CANON-V1
def canon(rows):
    """(số hàng, sha256, số hàng trùng). Hàng = JSON gọn (sort_keys, UTF-8), sắp theo byte, tiền tố độ dài 8 byte big-endian."""
    enc = sorted(json.dumps(r, ensure_ascii=False, separators=(",", ":"), sort_keys=True).encode() for r in rows)
    h = hashlib.sha256()
    for b in enc:
        h.update(struct.pack(">Q", len(b)))
        h.update(b)
    return len(enc), h.hexdigest(), len(enc) - len(set(enc))


def jkey(r):
    return json.dumps(r, ensure_ascii=False, separators=(",", ":"), sort_keys=True)


def self_sha(doc):
    d = dict(doc)
    d.pop("self_sha256", None)
    return hashlib.sha256(json.dumps(d, ensure_ascii=False, separators=(",", ":"), sort_keys=True, default=str).encode()).hexdigest()


# =========================================================================== nguồn: PG (một giao dịch REPEATABLE READ / database)
PG_SCRIPT = r'''
import json, os, sys
import psycopg
SPEC = json.loads(os.environ["CERT_SPEC"])
OPT = "-c default_transaction_read_only=on -c statement_timeout=30000 -c lock_timeout=2000 -c idle_in_transaction_session_timeout=120000"
NS = "n.nspname NOT IN ('pg_catalog','information_schema','pg_toast') AND n.nspname NOT LIKE 'pg_temp%%' AND n.nspname NOT LIKE 'pg_toast%%'"
Q = {
 "table": "SELECT n.nspname||'.'||c.relname FROM pg_class c JOIN pg_namespace n ON n.oid=c.relnamespace WHERE c.relkind IN ('r','p','f') AND " + NS,
 "view": "SELECT n.nspname||'.'||c.relname, c.relkind::text FROM pg_class c JOIN pg_namespace n ON n.oid=c.relnamespace WHERE c.relkind IN ('v','m') AND " + NS,
 "trigger": "SELECT n.nspname, c.relname, t.tgname, pn.nspname, p.proname, pg_get_function_identity_arguments(p.oid), t.tgenabled::text "
            "FROM pg_trigger t JOIN pg_class c ON c.oid=t.tgrelid JOIN pg_namespace n ON n.oid=c.relnamespace "
            "JOIN pg_proc p ON p.oid=t.tgfoid JOIN pg_namespace pn ON pn.oid=p.pronamespace WHERE NOT t.tgisinternal AND " + NS,
 "function": "SELECT n.nspname||'.'||p.proname||'('||pg_get_function_identity_arguments(p.oid)||')' FROM pg_proc p "
             "JOIN pg_namespace n ON n.oid=p.pronamespace WHERE " + NS + " AND NOT EXISTS (SELECT 1 FROM pg_depend d WHERE d.classid='pg_proc'::regclass "
             "AND d.objid=p.oid AND d.deptype='e')",
 "fk": "SELECT n1.nspname||'.'||c1.relname, co.conname, n2.nspname||'.'||c2.relname FROM pg_constraint co "
       "JOIN pg_class c1 ON c1.oid=co.conrelid JOIN pg_namespace n1 ON n1.oid=c1.relnamespace "
       "JOIN pg_class c2 ON c2.oid=co.confrelid JOIN pg_namespace n2 ON n2.oid=c2.relnamespace "
       "JOIN pg_namespace n ON n.oid=co.connamespace WHERE co.contype='f' AND " + NS,
 "view_dep": "SELECT DISTINCT vn.nspname||'.'||v.relname, tn.nspname||'.'||t.relname FROM pg_depend d JOIN pg_rewrite r ON r.oid=d.objid "
             "JOIN pg_class v ON v.oid=r.ev_class JOIN pg_class t ON t.oid=d.refobjid JOIN pg_namespace vn ON vn.oid=v.relnamespace "
             "JOIN pg_namespace tn ON tn.oid=t.relnamespace JOIN pg_namespace n ON n.oid=vn.oid WHERE d.classid='pg_rewrite'::regclass "
             "AND d.refclassid='pg_class'::regclass AND v.oid<>t.oid AND " + NS,
 "directus_collection": "SELECT collection FROM directus_collections",
 "directus_relation": "SELECT many_collection, many_field, one_collection FROM directus_relations",
 "directus_flow": "SELECT f.id::text, f.trigger, f.status FROM directus_flows f",
 "directus_operation": "SELECT o.id::text, o.flow::text FROM directus_operations o",
 "dot_tools": "SELECT code, name, file_path, paired_dot FROM dot_tools",
 "kb": "SELECT key, data->>'document_id', data->>'deleted_at' IS NOT NULL, data->>'vector_status' FROM kb_documents",
 "databases": "SELECT datname FROM pg_database WHERE NOT datistemplate",
}
out = {}
for db, classes in SPEC.items():
    r = {"classes": {}}
    try:
        conn = psycopg.connect(host=os.environ.get("PG_HOST", "postgres"), port=os.environ.get("PG_PORT", "5432"), user=os.environ["PG_USER_RO"],
                               password=os.environ["PG_PASSWORD_RO"], dbname=db, connect_timeout=5, options=OPT, autocommit=True)
    except Exception as e:
        r["error"] = "connect " + type(e).__name__
        out[db] = r
        continue
    try:
        cur = conn.cursor()
        cur.execute("BEGIN ISOLATION LEVEL REPEATABLE READ READ ONLY")
        cur.execute("SELECT current_user, (SELECT rolsuper FROM pg_roles WHERE rolname=current_user), current_setting('transaction_read_only'), "
                    "current_setting('transaction_isolation'), pg_current_snapshot()::text, txid_current_if_assigned(), "
                    "to_char(clock_timestamp() AT TIME ZONE 'UTC','YYYY-MM-DD\"T\"HH24:MI:SS\"Z\"')")
        u, sup, ro, iso, snap, xid, ts = cur.fetchone()
        r["reader"] = {"role": u, "rolsuper": sup, "transaction_read_only": ro, "isolation": iso, "pg_snapshot": snap, "snapshot_utc": ts}
        if sup or ro != "on" or iso != "repeatable read":
            r["error"] = "NO_READONLY_REPEATABLE_READ"
        else:
            for c in classes:
                cur.execute("SAVEPOINT s")
                try:
                    cur.execute(Q[c])
                    r["classes"][c] = {"ok": True, "rows": [[None if v is None else (v if isinstance(v, (bool, int)) else str(v)) for v in row] for row in cur.fetchall()]}
                    cur.execute("RELEASE SAVEPOINT s")
                except Exception as e:
                    cur.execute("ROLLBACK TO SAVEPOINT s")
                    msg = type(e).__name__
                    r["classes"][c] = {"ok": False, "error": ("NO_ACCESS " if "Privilege" in msg or "permission" in str(e).lower() else "") + msg}
            cur.execute("SELECT txid_current_if_assigned()")
            r["reader"]["xid_after"] = cur.fetchone()[0]
        cur.execute("ROLLBACK")
    except Exception as e:
        r["error"] = "query " + type(e).__name__
    finally:
        conn.close()
    out[db] = r
print(json.dumps(out, ensure_ascii=False))
'''


def pg_read(spec, timeout=600):
    rc, o, e = sh(["docker", "exec", "-i", "-e", "CERT_SPEC=" + json.dumps(spec), "incomex-claude-mcp", "python", "-I", "-B", "-"],
                  inp=PG_SCRIPT.encode(), timeout=timeout)
    try:
        return json.loads(o) if rc == 0 else {"_error": "rc=%s %s" % (rc, e[-200:])}
    except ValueError:
        return {"_error": "json"}


# =========================================================================== nguồn: Qdrant (trong incomex-agent-data, khoá sẵn của dịch vụ)
QD_SCRIPT = r'''
import json, os, sys, urllib.request
base = (os.environ.get("QDRANT_URL") or "").rstrip("/")
hdr = {"Content-Type": "application/json"}
if os.environ.get("QDRANT_API_KEY"):
    hdr["api-key"] = os.environ["QDRANT_API_KEY"]
mode = os.environ.get("CERT_QD", "meta")
def call(path, body=None):
    req = urllib.request.Request(base + path, headers=hdr, method="POST" if body is not None else "GET",
                                 data=json.dumps(body).encode() if body is not None else None)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())["result"]
out = {}
try:
    cols = sorted(c["name"] for c in call("/collections")["collections"])
    out["collections"] = {}
    for c in cols:
        r = call("/collections/" + c)
        vec = (r.get("config") or {}).get("params", {}).get("vectors", {})
        if "size" in vec:
            vec = {"": vec}
        out["collections"][c] = {"vectors": {k: [v.get("size"), v.get("distance")] for k, v in vec.items()},
                                 "payload_index": sorted((r.get("payload_schema") or {}).keys())}
    out["aliases"] = sorted([a["alias_name"], a["collection_name"]] for a in call("/aliases")["aliases"])
    if mode == "ids":
        c = os.environ["CERT_QD_COLLECTION"]
        out["count_before"] = call("/collections/%s/points/count" % c, {"exact": True})["count"]
        ids, n, off, pages, nodoc = set(), 0, None, 0, 0
        while True:
            body = {"limit": 1000, "with_payload": {"include": ["document_id"]}, "with_vector": False}
            if off is not None:
                body["offset"] = off
            r = call("/collections/%s/points/scroll" % c, body)
            pages += 1
            for p in r.get("points") or []:
                n += 1
                d = (p.get("payload") or {}).get("document_id")
                if isinstance(d, str) and d:
                    ids.add(d)
                else:
                    nodoc += 1
            off = r.get("next_page_offset")
            if off is None or pages > 500:
                break
        out["points_scrolled"] = n
        out["points_without_document_id"] = nodoc
        out["pages"] = pages
        out["scroll_complete"] = off is None
        out["count_after"] = call("/collections/%s/points/count" % c, {"exact": True})["count"]
        out["doc_ids"] = sorted(ids)
except Exception as e:
    out["error"] = type(e).__name__
print(json.dumps(out, ensure_ascii=False))
'''


def qd_read(mode="meta", collection=None, timeout=300):
    env = ["-e", "CERT_QD=" + mode] + (["-e", "CERT_QD_COLLECTION=" + collection] if collection else [])
    rc, o, e = sh(["docker", "exec", "-i"] + env + ["incomex-agent-data", "python", "-I", "-B", "-"], inp=QD_SCRIPT.encode(), timeout=timeout)
    try:
        return json.loads(o) if rc == 0 else {"error": "rc=%s" % rc}
    except ValueError:
        return {"error": "json"}


# =========================================================================== nguồn: Lark (LarkReader chỉ-đọc, metadata bảng/trường)
LARK_SCRIPT = r'''
import json, sys, time
sys.path.insert(0, "/opt/incomex/lark-client")
import yaml
from lark_client import LarkCore, LarkReader
reg = yaml.safe_load(open("/opt/incomex/lark-client/config/bases.yaml"))["bases"]
rd = LarkReader(LarkCore())
out = {}
for b in reg:
    key, tok = b["key"], b["app_token"]
    e = {}
    try:
        t1 = sorted(t.get("table_id") for t in rd.list_tables(tok))
        e["tables"] = t1
        links, ferr = [], []
        for tid in t1:
            try:
                for f in rd.list_fields(tok, tid):
                    if f.get("type") in (18, 21):
                        links.append([tid, f.get("field_id"), (f.get("property") or {}).get("table_id")])
            except Exception as x:
                ferr.append(tid)
            time.sleep(0.12)
        e["links"] = links
        e["field_errors"] = ferr
        e["tables_after"] = sorted(t.get("table_id") for t in rd.list_tables(tok))
    except Exception as x:
        e["error"] = ("NO_ACCESS " if "403" in str(x) or "ermission" in str(x) else "") + type(x).__name__
    out[key] = e
print(json.dumps(out, ensure_ascii=False))
'''


def lark_read(timeout=900):
    rc, o, e = sh([LARK_PY, "-I", "-B", "-"], inp=LARK_SCRIPT.encode(), timeout=timeout)
    try:
        return json.loads(o) if rc == 0 else {"_error": "rc=%s" % rc}
    except ValueError:
        return {"_error": "json"}


def lark_bases():
    """Danh mục base từ sổ bases.yaml (đọc dòng key: — không cần thư viện yaml, không đọc app_token)."""
    try:
        return sorted(set(re.findall(r"^\s*-?\s*key:\s*['\"]?([\w.-]+)", open(BASES, encoding="utf-8").read(), re.M)))
    except OSError:
        return None


# =========================================================================== nguồn: host (docker/systemd/cron/nginx//opt/git/DOT)
def docker_read():
    rc, o, _ = sh(["docker", "ps", "-a", "--no-trunc", "--format", "{{.Names}}\t{{.ID}}"], timeout=60)
    if rc != 0:
        return {"error": "docker ps rc=%s" % rc}
    names = sorted(l.split("\t")[0] for l in o.splitlines() if l.strip())
    rc2, o2, _ = sh(["docker", "inspect", "--format", "{{json .}}"] + names, timeout=120) if names else (0, "", "")
    cont, edges = [], []
    for l in o2.splitlines():
        try:
            d = json.loads(l)
        except ValueError:
            continue
        n = d["Name"].lstrip("/")
        cont.append([n, d.get("Image")])
        edges.append([n, "USES_IMAGE", d.get("Image")])
        for m in d.get("Mounts") or []:
            edges.append([n, "MOUNTS", (m.get("Type") or "") + ":" + (m.get("Name") or m.get("Source") or "") + "->" + (m.get("Destination") or "")])
        for port, bs in ((d.get("HostConfig") or {}).get("PortBindings") or {}).items():
            for b in bs or []:
                edges.append([n, "PUBLISHES", "%s:%s->%s" % (b.get("HostIp"), b.get("HostPort"), port)])
    rc3, o3, _ = sh(["docker", "images", "--no-trunc", "--format", "{{.ID}}\t{{.Repository}}:{{.Tag}}"], timeout=60)
    imgs = sorted({l.split("\t")[0] for l in o3.splitlines() if l.strip()})
    rc4, o4, _ = sh(["docker", "ps", "-a", "--no-trunc", "--format", "{{.Names}}\t{{.ID}}"], timeout=60)
    after = sorted(l.split("\t")[0] for l in o4.splitlines() if l.strip())
    return {"containers": cont, "edges": edges, "images": imgs, "ok": rc2 == 0 and rc3 == 0, "names_before": names, "names_after": after}


def systemd_read():
    base = "/etc/systemd/system"
    units, edges = [], []
    try:
        files = sorted(f for f in os.listdir(base) if f.endswith((".service", ".timer")) and os.path.isfile(os.path.join(base, f))
                       and not os.path.islink(os.path.join(base, f)))
    except OSError as e:
        return {"error": type(e).__name__}
    for f in files:
        txt = open(os.path.join(base, f), encoding="utf-8", errors="replace").read()
        units.append([f])
        if f.endswith(".timer"):
            m = re.search(r"^\s*Unit\s*=\s*(\S+)", txt, re.M)
            edges.append([f, "TRIGGERS", m.group(1) if m else f[:-6] + ".service"])
        for i, m in enumerate(re.finditer(r"^\s*(Exec(?:Start|StartPre|StartPost))\s*=\s*[-@:+!]*(\S+)", txt, re.M)):
            edges.append([f, "EXECS", m.group(2), "%s#%d" % (m.group(1), i)])
    after = sorted(f for f in os.listdir(base) if f.endswith((".service", ".timer")) and os.path.isfile(os.path.join(base, f))
                   and not os.path.islink(os.path.join(base, f)))
    return {"units": units, "edges": edges, "before": files, "after": after}


def cron_read():
    files = []
    for b in ("/var/spool/cron/crontabs", "/etc/cron.d"):
        if os.path.isdir(b):
            files += sorted(os.path.join(b, x) for x in os.listdir(b) if not x.startswith("."))
    files.append("/etc/crontab")
    ents, edges, errs = [], [], []
    for p in files:
        try:
            txt = open(p, encoding="utf-8", errors="replace").read()
        except OSError:
            errs.append(p)
            continue
        for ln in txt.splitlines():
            s = ln.strip()
            if not s or s.startswith("#") or re.match(r"^[A-Za-z_]+=", s):
                continue
            parts = s.split()
            sched = " ".join(parts[:1] if s.startswith("@") else parts[:5])
            m = re.search(r"(/[\w./@+-]+)", " ".join(parts[1 if s.startswith("@") else 5:]))
            tgt = m.group(1) if m else "?"
            eid = "%s|%s|%s" % (p, sched, tgt)
            ents.append([eid])
            edges.append([eid, "RUNS", tgt])
    for d in ("/etc/cron.hourly", "/etc/cron.daily", "/etc/cron.weekly", "/etc/cron.monthly"):
        for x in sorted(os.listdir(d)) if os.path.isdir(d) else []:
            if not x.startswith("."):
                eid = "%s|run-parts|%s" % (d, x)
                ents.append([eid])
                edges.append([eid, "RUNS", os.path.join(d, x)])
    return {"entries": ents, "edges": edges, "errors": errs}


def nginx_read():
    rc, o, e = sh(["docker", "exec", "incomex-nginx", "nginx", "-T"], timeout=60)
    if rc != 0:
        return {"error": "nginx -T rc=%s" % rc}
    servers, edges, cur, loc = [], [], None, None
    depth = 0
    for raw in o.splitlines():
        ln = raw.split("#", 1)[0].strip()
        if not ln:
            continue
        if re.match(r"^server\s*\{", ln):
            cur, depth = {"names": [], "listen": []}, 1
            servers.append(cur)
            continue
        if cur is not None:
            m = re.match(r"^server_name\s+([^;]+);", ln)
            if m:
                cur["names"] += m.group(1).split()
            m = re.match(r"^listen\s+([^;]+);", ln)
            if m:
                cur["listen"].append(m.group(1).split()[0])
            m = re.match(r"^location\s+(.+?)\s*\{", ln)
            if m:   # đường location có route path-secret ⇒ chỉ băm, không in
                loc = hashlib.sha256(m.group(1).encode()).hexdigest()[:16]
            m = re.match(r"^proxy_pass\s+([^;]+);", ln)
            if m:
                t = re.sub(r"^(\w+://[^/]+).*$", r"\1", m.group(1))
                sid = ",".join(sorted(cur["names"])) + "|" + ",".join(sorted(cur["listen"]))
                edges.append([sid + "|" + (loc or "-"), "PROXIES", t])
            depth += ln.count("{") - ln.count("}")
            if depth <= 0:
                cur, loc = None, None
    objs = sorted({",".join(sorted(s["names"])) + "|" + ",".join(sorted(s["listen"])) for s in servers})
    return {"servers": [[x] for x in objs], "edges": edges}


def opt_read():
    ents = []
    for b in ("/opt", "/opt/incomex"):
        try:
            for x in sorted(os.listdir(b)):
                ents.append([os.path.join(b, x), "d" if os.path.isdir(os.path.join(b, x)) else "f"])
        except OSError as e:
            return {"error": type(e).__name__}
    led = []
    try:
        for ln in open(LEDGER, encoding="utf-8"):
            if ln.startswith("#") or not ln.strip():
                continue
            c = ln.rstrip("\n").split("\t")
            led.append([c[0], c[1] if len(c) > 1 else "?"])
    except OSError:
        led = None
    return {"entries": ents, "ledger": led}


def dot_bin_read():
    try:
        names = {}
        for e in os.scandir(os.path.join(DOT, "bin")):
            names[e.name] = "d" if e.is_dir(follow_symlinks=False) else ("l" if e.is_symlink() else ("f" if e.is_file(follow_symlinks=False) else "o"))
        cat = set(re.findall(r"^([^\t\n]+)\t", open(os.path.join(DOT, "00-SO-DOT.tsv"), encoding="utf-8").read(), re.M)) - {"name"}
    except OSError as e:
        return {"error": type(e).__name__}
    cmds = []
    for n, t in names.items():
        lab = "dir" if t == "d" else ("backup" if re.search(BAK, n) else ("label_md" if n.endswith(".md") else "live"))
        if t == "f" and (n in cat or lab == "live"):
            cmds.append(n)
    return {"commands": sorted(cmds)}


def git_read():
    rc, o, _ = sh(["git", "-c", "safe.directory=*", "--no-optional-locks", "-C", GW_CLONE, "ls-tree", "-d", "--name-only", "HEAD", "work/", "work/done-tasks/"], timeout=60)
    rc2, h, _ = sh(["git", "-c", "safe.directory=*", "--no-optional-locks", "-C", GW_CLONE, "rev-parse", "HEAD"], timeout=30)
    if rc != 0 or rc2 != 0:
        return {"error": "git rc=%s/%s" % (rc, rc2)}
    return {"dirs": sorted({l.strip() for l in o.splitlines() if l.strip() and l.strip() not in ("work/done-tasks",)}), "head": h.strip()}


# =========================================================================== Graph (Cypher phân trang theo gs_key + tổng đếm riêng)
def g_rows(g, pw, q, p=None, timeout=600):
    d = g.http_cypher([(q, p or {})], pw, timeout=timeout)
    if d.get("errors"):
        raise RuntimeError("cypher " + str(d["errors"][0].get("code")))
    (r,) = d["results"]
    return [dict(zip(r["columns"], x["row"])) for x in r["data"]]


def graph_nodes(g, pw, label, attrs, prefix, page=GRAPH_PAGE):
    lab = label.replace("`", "")
    total = g_rows(g, pw, "MATCH (n:`%s`) RETURN count(n) AS c" % lab)[0]["c"]
    rows, after, pages, bad_key = [], "", 0, 0
    while True:
        rs = g_rows(g, pw, "MATCH (n:`%s`) WHERE n.gs_key > $after RETURN n.gs_key AS k, n.id AS id, [a IN $attrs | n[a]] AS av, "
                           "'GS' IN labels(n) AS gs ORDER BY n.gs_key LIMIT $page" % lab, {"after": after, "attrs": attrs, "page": page})
        pages += 1
        for r in rs:
            rows.append([label, r["id"]] + [None if v is None else str(v) for v in r["av"]])
            if not r["gs"] or r["k"] != (prefix or "") + str(r["id"]):
                bad_key += 1
        if len(rs) < page:
            break
        after = rs[-1]["k"]
    return {"rows": rows, "total": total, "pages": pages, "complete": total == len(rows), "gs_key_bad": bad_key}


def graph_edges(g, pw, rtype, a, b, prov, page=GRAPH_PAGE):
    t = rtype.replace("`", "")
    total_all = g_rows(g, pw, "MATCH ()-[r:`%s`]->() RETURN count(r) AS c" % t)[0]["c"]
    total = g_rows(g, pw, "MATCH (:`%s`)-[r:`%s`]->(:`%s`) RETURN count(r) AS c" % (a, t, b))[0]["c"]
    cond = " AND ".join("r[%s] IS NOT NULL" % json.dumps(k) for k in prov) or "true"
    rows, after, pages, noprov = [], "", 0, 0
    while True:
        rs = g_rows(g, pw, "MATCH (x:`%s`)-[r:`%s`]->(y:`%s`) WITH x, r, y, x.gs_key + '|' + y.gs_key + '|' + elementId(r) AS k WHERE k > $after "
                           "RETURN k, x.id AS s, y.id AS d, %s AS prov ORDER BY k LIMIT $page" % (a, t, b, cond), {"after": after, "page": page})
        pages += 1
        for r in rs:
            rows.append([r["s"], rtype, r["d"]])
            noprov += 0 if r["prov"] else 1
        if len(rs) < page:
            break
        after = rs[-1]["k"]
    return {"rows": rows, "total": total, "total_all_endpoints": total_all, "pages": pages,
            "complete": total == len(rows), "other_endpoints": total_all - total, "provenance_missing": noprov}


def graph_read(g, pw, spec):
    """spec = {"nodes": [{label, prefix, attrs}], "edges": [{type, from, to, prov}]} ⇒ (objects, edges, meta)."""
    objs, edges, meta = [], [], {"complete": True, "problems": []}
    for n in spec.get("nodes") or []:
        r = graph_nodes(g, pw, n["label"], n.get("attrs") or [], n.get("prefix"))
        objs += r.pop("rows")
        meta[n["label"]] = r
        if not r["complete"]:
            meta["complete"] = False
            meta["problems"].append("GRAPH_INCOMPLETE %s %d/%d" % (n["label"], r["pages"], r["total"]))
        if r["gs_key_bad"]:
            meta["problems"].append("GS_KEY_BAD %s %d" % (n["label"], r["gs_key_bad"]))
    for e in spec.get("edges") or []:
        r = graph_edges(g, pw, e["type"], e["from"], e["to"], e.get("prov") or [])
        edges += r.pop("rows")
        meta[e["type"]] = r
        if not r["complete"]:
            meta["complete"] = False
            meta["problems"].append("GRAPH_INCOMPLETE %s" % e["type"])
        if r["other_endpoints"]:
            meta["problems"].append("EDGE_OTHER_ENDPOINTS %s %d" % (e["type"], r["other_endpoints"]))
        if r["provenance_missing"]:
            meta["problems"].append("PROVENANCE_MISSING %s %d" % (e["type"], r["provenance_missing"]))
    return objs, edges, meta


# =========================================================================== thu thập nguồn theo bộ đọc
class Sources:
    """Đọc mỗi bộ đọc gốc MỘT lần cho cả lượt (lười), giữ lỗi để ô biết UNKNOWN."""

    def __init__(self, cells, b88_input=None, injected=None):
        self.cells, self.b88_input, self.cache = cells, b88_input, dict(injected or {})

    def get(self, name):
        if name not in self.cache:
            t0 = time.time()
            try:
                self.cache[name] = getattr(self, "_" + name)()
            except Exception as e:  # noqa: BLE001
                self.cache[name] = {"_error": "%s %s" % (type(e).__name__, str(e)[:160])}
            if isinstance(self.cache[name], dict):
                self.cache[name].setdefault("_seconds", round(time.time() - t0, 1))
        return self.cache[name]

    def _pg(self):
        spec = {}
        for c in self.cells:
            s = c.get("source") or {}
            if s.get("adapter") == "pg":
                spec.setdefault(s["db"], set()).update(s["classes"])
        spec.setdefault("postgres", set()).add("databases")
        return pg_read({k: sorted(v) for k, v in spec.items()})

    def _pg_kb(self):
        return pg_read({"incomex_metadata": ["kb"]})

    def _docker(self):
        return docker_read()

    def _systemd(self):
        return systemd_read()

    def _cron(self):
        return cron_read()

    def _nginx(self):
        return nginx_read()

    def _opt(self):
        return opt_read()

    def _dot_bin(self):
        return dot_bin_read()

    def _git(self):
        return git_read()

    def _qdrant(self):
        return qd_read("meta")

    def _qdrant_ids(self):
        return qd_read("ids", "production_documents")

    def _lark(self):
        return lark_read()

    def _b88(self):
        import csv
        d = self.b88_input
        if not d:
            import tempfile
            work = tempfile.mkdtemp(prefix="gs-cert-b88-", dir="/dev/shm")
            os.makedirs(work + "/input", mode=0o700)
            rc, o, e = sh([LARK_PY, "-I", RB + "/r7_b6.py", work + "/input", work], timeout=900)
            if rc != 0 or not os.path.exists(work + "/input/FREEZE.sha256"):
                sh(["rm", "-rf", work])
                return {"_error": "r7_b6 rc=%s" % rc}
            d = work + "/input"
            self._b88_tmp = work
        rd = lambda f: list(csv.DictReader(open(os.path.join(d, f), encoding="utf-8")))
        out = {"objects": [], "edges": [], "snapshot_utc": (jload(os.path.join(os.path.dirname(d), "b6", "b6-result.json"), {}) or {}).get("snapshot_utc"),
               "freeze_sha256": hashlib.sha256(open(os.path.join(d, "FREEZE.sha256"), "rb").read()).hexdigest()}
        for lab, f, col in (("B88Order", "b88_order.csv", "order_code"), ("B88Trainee", "b88_tts.csv", None),
                            ("B88Union", "b88_union.csv", "union_code"), ("B88Company", "b88_company.csv", "company_code")):
            for r in rd(f):
                out["objects"].append([lab, r["record_id"]] + ([r[col]] if col else []))
        for rel in ("CANDIDATE_FOR_ORDER", "SELECTED_FOR_ORDER", "ORDER_MANAGED_BY_UNION", "ORDER_FOR_COMPANY"):
            for r in rd("b88_rel_%s.csv" % rel.lower()):
                out["edges"].append([r["src_record_id"], rel, r["dst_record_id"]])
        if getattr(self, "_b88_tmp", None):
            sh(["rm", "-rf", self._b88_tmp])
        return out


def src_pg_class(S, db, cls):
    """(ok, rows, reader, why) cho một lớp PG."""
    p = S.get("pg")
    if p.get("_error"):
        return False, None, None, "READER_FAIL " + p["_error"]
    d = p.get(db) or {}
    if d.get("error"):
        return False, None, d.get("reader"), "READER_FAIL " + d["error"]
    c = (d.get("classes") or {}).get(cls)
    if not c:
        return False, None, d.get("reader"), "READER_FAIL lớp %s không đọc" % cls
    if not c["ok"]:
        return False, None, d.get("reader"), ("NO_ACCESS " if c["error"].startswith("NO_ACCESS") else "READER_FAIL ") + c["error"]
    return True, c["rows"], d.get("reader"), None


def source_for(cell, S):
    """⇒ {ok, why, objects, edges, reader, snapshot, consistency, access}"""
    s = cell.get("source") or {}
    a = s.get("adapter")
    res = {"ok": False, "objects": [], "edges": [], "reader": a, "consistency": "NONE", "access": "OK"}
    if a == "pg":
        db = s["db"]
        rowsets = {}
        for c in s["classes"]:
            ok, rows, rdr, why = src_pg_class(S, db, c)
            res["snapshot"] = rdr
            if not ok:
                res["why"] = why
                res["access"] = "NO_ACCESS" if why.startswith("NO_ACCESS") else "FAIL"
                return res
            rowsets[c] = rows
        res["consistency"] = "PG_REPEATABLE_READ_READ_ONLY"
        res["reader"] = "pg:%s:context_pack_readonly" % db
        k = s["classes"][0]
        if k == "table":
            res["objects"] = [["PgTable", r[0]] for r in rowsets[k]]
        elif k == "view":
            res["objects"] = [["PgView", r[0], r[1]] for r in rowsets[k]]
        elif k == "trigger":
            for r in rowsets[k]:
                gid, tid, fid = "%s.%s.%s" % (r[0], r[1], r[2]), "%s.%s" % (r[0], r[1]), "%s.%s(%s)" % (r[3], r[4], r[5] or "")
                res["objects"].append(["PgTrigger", gid, r[6]])
                res["edges"] += [[gid, "ON_TABLE", tid], [gid, "EXECUTES", fid]]
        elif k == "function":
            res["objects"] = [["PgFunction", r[0]] for r in rowsets[k]]
        elif k == "fk":
            for r in rowsets[k]:
                res["objects"].append(["PgForeignKey", r[0] + "." + r[1]])
                res["edges"].append([r[0], "FK", r[2], r[1]])
        elif k == "view_dep":
            res["edges"] = [[r[0], "DEPENDS_ON", r[1]] for r in rowsets[k]]
        elif k == "directus_collection":
            res["objects"] = [["DirectusCollection", r[0]] for r in rowsets[k]]
        elif k == "directus_relation":
            res["edges"] = [[r[0] + "." + str(r[1]), "RELATES", r[2]] for r in rowsets[k]]
        elif k == "directus_flow":
            res["objects"] = [["DirectusFlow", r[0], r[1], r[2]] for r in rowsets[k]] + \
                             [["DirectusOperation", r[0]] for r in rowsets.get("directus_operation", [])]
            res["edges"] = [[r[0], "IN_FLOW", r[1]] for r in rowsets.get("directus_operation", [])]
        elif k == "dot_tools":
            db_ = S.get("dot_bin")
            if db_.get("error") or db_.get("_error"):
                res["why"] = "READER_FAIL dot/bin " + str(db_.get("error") or db_.get("_error"))
                res["access"] = "FAIL"
                return res
            cmdset, codes = set(db_["commands"]), {r[0] for r in rowsets[k]}
            for code, name, fpth, paired in rowsets[k]:
                res["objects"].append(["DotRegistryEntry", code])
                key = (fpth or "").split("/")[-1] if fpth else (name or "")
                if key and key in cmdset:
                    res["edges"].append([code, "REGISTERS", key])
                if paired and paired in codes:
                    res["edges"].append([code, "PAIRED_WITH", paired])
            res["reader"] += "+dot/bin"
            again = db_["commands_after"] if "commands_after" in db_ else dot_bin_read().get("commands")
            if again != db_["commands"]:
                res["consistency"] = "DRIFT"
        res["ok"] = True
        return res
    if a == "dot_bin":
        d = S.get("dot_bin")
        if d.get("error") or d.get("_error"):
            res["why"] = "READER_FAIL " + str(d.get("error") or d.get("_error"))
            return res
        again = d["commands_after"] if "commands_after" in d else dot_bin_read().get("commands")
        res.update(ok=True, objects=[["DotCommand", n] for n in d["commands"]], reader="dot/bin+00-SO-DOT.tsv (luật LBL-2)",
                   consistency="BEFORE_AFTER_EQUAL" if again == d["commands"] else "DRIFT")
        return res
    if a in ("docker", "systemd", "cron", "nginx", "opt", "git"):
        d = S.get(a)
        if d.get("error") or d.get("_error"):
            res["why"] = "READER_FAIL " + str(d.get("error") or d.get("_error"))
            return res
        res["ok"], res["reader"] = True, a
        res["consistency"] = "SINGLE_READ"
        if a in ("cron", "nginx", "opt"):          # đọc lại ngay sau (rẻ): trước = sau ⇒ nhất quán; fixture tiêm "<a>_after"
            again = S.cache.get(a + "_after") or {"cron": cron_read, "nginx": nginx_read, "opt": opt_read}[a]()
            strip = lambda x: {k: v for k, v in x.items() if not k.startswith("_")}
            res["consistency"] = "BEFORE_AFTER_EQUAL" if strip(again) == strip(d) else "DRIFT"
        if a == "docker":
            if s.get("part") == "image":
                res["objects"] = [["DockerImage", x] for x in d["images"]]
            else:
                res["objects"] = [["DockerContainer"] + c for c in d["containers"]]
                res["edges"] = d["edges"]
            res["consistency"] = "BEFORE_AFTER_EQUAL" if d["names_before"] == d["names_after"] else "DRIFT"
        elif a == "systemd":
            res["objects"], res["edges"] = [["SystemdUnit"] + u for u in d["units"]], d["edges"]
            res["consistency"] = "BEFORE_AFTER_EQUAL" if d["before"] == d["after"] else "DRIFT"
        elif a == "cron":
            res["objects"], res["edges"] = [["CronEntry"] + e for e in d["entries"]], d["edges"]
            if d["errors"]:
                res["ok"], res["why"], res["access"] = False, "NO_ACCESS " + ",".join(d["errors"]), "NO_ACCESS"
        elif a == "nginx":
            res["objects"], res["edges"] = [["NginxServer"] + x for x in d["servers"]], d["edges"]
        elif a == "opt":
            if s.get("part") == "ledger":
                if d["ledger"] is None:
                    res["ok"], res["why"] = False, "READER_FAIL code-ledger"
                res["objects"] = [["LedgerPath"] + x for x in d["ledger"] or []]
            else:
                res["objects"] = [["OptEntry"] + x for x in d["entries"]]
        elif a == "git":
            res["objects"] = [["WorkDir", x] for x in d["dirs"]]
            res["snapshot"] = {"git_head": d["head"]}
            res["consistency"] = "GIT_COMMIT"
        return res
    if a == "qdrant_meta":
        d = S.get("qdrant")
        if d.get("error") or d.get("_error"):
            res["why"] = "READER_FAIL " + str(d.get("error") or d.get("_error"))
            return res
        c = (d.get("collections") or {}).get(s["collection"])
        if c is None:
            res["why"] = "READER_FAIL collection vắng"
            return res
        again = S.cache.get("qdrant_after") or qd_read("meta")
        res.update(ok=True, reader="qdrant GET", consistency="BEFORE_AFTER_EQUAL" if (again.get("collections"), again.get("aliases")) ==
                   (d.get("collections"), d.get("aliases")) else "DRIFT",
                   objects=[["QdrantCollection", s["collection"], jkey(c["vectors"]), ",".join(c["payload_index"])]] +
                           [["QdrantAlias", x[0]] for x in d.get("aliases") or [] if x[1] == s["collection"]])
        return res
    if a == "lark_schema":
        d = S.get("lark")
        if d.get("_error"):
            res["why"] = "READER_FAIL " + d["_error"]
            return res
        e = d.get(s["base"])
        if not e or e.get("error"):
            res["why"] = (e or {}).get("error") or "READER_FAIL base vắng"
            res["access"] = "NO_ACCESS" if "NO_ACCESS" in res["why"] else "FAIL"
            if not res["why"].startswith(("NO_ACCESS", "READER_FAIL")):
                res["why"] = "READER_FAIL " + res["why"]
            return res
        if e.get("field_errors"):
            res["why"] = "READER_FAIL trường %d bảng" % len(e["field_errors"])
            return res
        res.update(ok=True, reader="LarkReader list_tables/list_fields",
                   consistency="BEFORE_AFTER_EQUAL" if e["tables"] == e["tables_after"] else "DRIFT",
                   objects=[["LarkTable", t] for t in e["tables"]], edges=[[l[0] + "." + str(l[1]), "LINKS_TO", l[2]] for l in e["links"]])
        return res
    if a == "b88":
        d = S.get("b88")
        if d.get("_error"):
            res["why"] = "READER_FAIL " + d["_error"]
            return res
        res.update(ok=True, reader="lark 88-phai-cu r7_b6 (11 field id)", consistency="FREEZE_SHA256", objects=d["objects"], edges=d["edges"],
                   snapshot={"B88_SNAP": d.get("snapshot_utc"), "freeze_sha256": d.get("freeze_sha256")})
        return res
    if a == "code_identity":
        res["why"] = "READER_NOT_ID_COMPARABLE_C1A"
        return res
    res["why"] = "NO_READER"
    return res


# =========================================================================== M-b (ô KB ↔ Qdrant, không chuyển vector)
def mb_cell(S, ids_out=None):
    p = S.get("pg_kb")
    q = S.get("qdrant_ids")
    r = {"reader": "pg incomex_metadata.kb_documents (key,data.document_id,deleted_at,vector_status) ↔ qdrant production_documents payload.document_id",
         "normalizer": "agent-data server.py: id = data.document_id (khoá PG = id thay '/'→'__', đã đo 0 lệch); sống = deleted_at null; "
                       "ready = vector_status 'ready'", "ok": False}
    kb = ((p.get("incomex_metadata") or {}).get("classes") or {}).get("kb") or {}
    if p.get("_error") or not kb.get("ok"):
        r["why"] = "READER_FAIL pg " + str(p.get("_error") or kb.get("error") or (p.get("incomex_metadata") or {}).get("error"))
        return r
    if q.get("error") or not q.get("scroll_complete") or q.get("count_before") != q.get("count_after") or q.get("points_scrolled") != q.get("count_after"):
        r["why"] = "READER_FAIL qdrant %s complete=%s before=%s after=%s scrolled=%s" % (q.get("error"), q.get("scroll_complete"), q.get("count_before"),
                                                                                    q.get("count_after"), q.get("points_scrolled"))
        return r
    live, deleted, ready = set(), set(), set()
    for key, did, isdel, vs in kb["rows"]:
        i = did or key
        (deleted if isdel else live).add(i)
        if not isdel and vs == "ready":
            ready.add(i)
    qids = set(q["doc_ids"])
    b = {"pg_ready_missing_in_qdrant": sorted(ready - qids), "qdrant_not_in_pg": sorted(qids - live - deleted),
         "qdrant_but_soft_deleted": sorted(qids & (deleted - live)), "qdrant_points_without_document_id": int(q.get("points_without_document_id") or 0),
         "pg_live_not_ready_in_qdrant": sorted((qids & live) - ready)}
    r.update(ok=True, buckets={k: (len(v) if isinstance(v, list) else v) for k, v in b.items()},
             bucket_sha256={k: hashlib.sha256("\n".join(v).encode()).hexdigest() for k, v in b.items() if isinstance(v, list)},
             pg={"rows": len(kb["rows"]), "live": len(live), "soft_deleted": len(deleted - live), "ready": len(ready),
                 "snapshot": (p.get("incomex_metadata") or {}).get("reader")},
             qdrant={"points": q["count_after"], "distinct_document_ids": len(qids), "pages": q["pages"]})
    if ids_out:
        fd = os.open(ids_out, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
        with os.fdopen(fd, "w") as f:
            json.dump({k: v for k, v in b.items() if isinstance(v, list)}, f, ensure_ascii=False, indent=1)
    return r


# =========================================================================== đánh giá ô
def evaluate(cell, src, gread, now, ttl_h):
    out = {"key": cell["key"], "gate": cell["gate"], "parent": cell.get("parent"), "scope": cell.get("scope"),
           "source_authority": cell.get("authority"), "relations_declared": [e["type"] for e in (cell.get("graph") or {}).get("edges") or []] +
           list(cell.get("source_relations") or []), "gap": cell.get("gap"), "status": MP, "reasons": []}
    sc = {"reader": src.get("reader"), "consistency": src.get("consistency"), "snapshot": src.get("snapshot"), "access": src.get("access")}
    if src.get("ok"):
        n, h, dup = canon(src["objects"])
        en, eh, edup = canon(src["edges"])
        sc.update(objects_count=n, objects_sha256=h, edges_count=en, edges_sha256=eh, duplicates=dup + edup)
    out["source"] = sc
    if not src.get("ok"):
        out["reasons"].append(src.get("why") or "SOURCE_UNKNOWN")
        out["reader_pass"] = False
        return out
    out["reader_pass"] = True
    if sc["consistency"] == "DRIFT":
        out["reasons"].append("SOURCE_DRIFT_DURING_READ")
    elif sc["consistency"] not in CONSISTENT:      # ĐỦ cần ranh giới nhất quán (PG RR · trước = sau · FREEZE · commit git)
        out["reasons"].append("NO_CONSISTENCY_PROOF " + str(sc["consistency"]))
    if sc["duplicates"]:
        out["reasons"].append("SOURCE_DUPLICATE_ROWS %d" % sc["duplicates"])
    spec = cell.get("graph")
    if not spec:
        if sc["objects_count"] == 0 and sc["edges_count"] == 0 and not out["reasons"]:
            out["status"], out["proof"] = DU, "NATIVE_EMPTY_CLASS (bộ đọc gốc đọc trọn, lớp rỗng; Graph không cần nút)"
        else:
            out["reasons"].append("GRAPH_CLASS_NOT_LOADED")
        out["graph"] = None
    else:
        if gread.get("error"):
            out["reasons"].append("GRAPH_READ_FAIL " + gread["error"])
            out["graph"] = {"error": gread["error"]}
        else:
            go, ge, gm = gread["objects"], gread["edges"], gread["meta"]
            n, h, dup = canon(go)
            en, eh, edup = canon(ge)
            out["graph"] = {"objects_count": n, "objects_sha256": h, "edges_count": en, "edges_sha256": eh, "duplicates": dup + edup,
                            "complete": gm["complete"], "problems": gm["problems"],
                            "totals": {k: v.get("total") for k, v in gm.items() if isinstance(v, dict) and "total" in v},
                            "pages": {k: v.get("pages") for k, v in gm.items() if isinstance(v, dict) and "pages" in v}}
            out["reasons"] += gm["problems"]
            if dup + edup:
                out["reasons"].append("GRAPH_DUPLICATES %d" % (dup + edup))
            so, se = {jkey(x) for x in src["objects"]}, {jkey(x) for x in src["edges"]}
            go_, ge_ = {jkey(x) for x in go}, {jkey(x) for x in ge}
            diff = {"objects_missing_in_graph": len(so - go_), "objects_extra_in_graph": len(go_ - so),
                    "edges_missing_in_graph": len(se - ge_), "edges_extra_in_graph": len(ge_ - se)}
            if not cell.get("private_ids"):
                diff["sample"] = {"objects_missing": sorted(so - go_)[:SAMPLE], "objects_extra": sorted(go_ - so)[:SAMPLE],
                                  "edges_missing": sorted(se - ge_)[:SAMPLE], "edges_extra": sorted(ge_ - se)[:SAMPLE]}
            out["diff"] = diff
            if h != sc["objects_sha256"] or n != sc["objects_count"]:
                out["reasons"].append("OBJECT_DIGEST_MISMATCH src=%d graph=%d" % (sc["objects_count"], n))
            if eh != sc["edges_sha256"] or en != sc["edges_count"]:
                out["reasons"].append("EDGE_DIGEST_MISMATCH src=%d graph=%d" % (sc["edges_count"], en))
            if not out["reasons"]:
                out["status"] = DU
                out["proof"] = "SOURCE_GRAPH_COUNT_AND_SHA256_EQUAL (đối tượng + %d loại cạnh)" % len(out["relations_declared"])
    for o in cell.get("open_classes") or []:   # lớp khai nhưng không có dấu vết máy ⇒ ô không thể ĐỦ
        out["reasons"].append("OPEN_CLASS " + o)
        out["status"] = MP
    if out["status"] == DU:
        out["issued_at"] = now_iso(now)
        out["expires_at"] = now_iso(now + min(ttl_h, MAX_TTL_H) * 3600)
    return out


# =========================================================================== thư mục G1–G9
def directory(cells, S):
    parents, errors = {}, []
    p = S.get("pg")
    dbs = None if p.get("_error") else (((p.get("postgres") or {}).get("classes") or {}).get("databases") or {})
    if not dbs or not dbs.get("ok"):
        errors.append("G1 pg_database")
    else:
        parents["G1"] = sorted("pg:" + r[0] for r in dbs["rows"])
    d = S.get("docker")
    if d.get("error") or d.get("_error"):
        errors.append("G2 docker")
    else:
        parents["G2"] = sorted("docker:" + n for n in d["names_after"])
    s = S.get("systemd")
    if s.get("error") or s.get("_error"):
        errors.append("G3 systemd")
    else:
        parents["G3"] = sorted("systemd:" + u for u in s["after"])
    c = S.get("cron")
    if c.get("_error") or c.get("errors"):
        errors.append("G4 cron")
    else:
        parents["G4"] = sorted({"cron:" + e[0].split("|")[0] for e in c["entries"]})
    n = S.get("nginx")
    if n.get("error") or n.get("_error"):
        errors.append("G5 nginx")
    else:
        parents["G5"] = sorted("nginx:" + x[0] for x in n["servers"])
    o = S.get("opt")
    if o.get("error") or o.get("_error"):
        errors.append("G6 /opt")
    else:
        parents["G6"] = sorted("opt:" + e[0] for e in o["entries"] if e[1] == "d")
    q = S.get("qdrant")
    if q.get("error") or q.get("_error"):
        errors.append("G7 qdrant")
    else:
        parents["G7"] = sorted("qdrant:" + x for x in q.get("collections") or {})
    lb = lark_bases()
    if lb is None:
        errors.append("G8 bases.yaml")
    else:
        parents["G8"] = sorted("lark:" + x for x in lb)
    gi = S.get("git")
    if gi.get("error") or gi.get("_error"):
        errors.append("G9 git")
    else:
        parents["G9"] = sorted("git:" + x for x in gi["dirs"])
    have = {c.get("parent") for c in cells}
    per_parent = {"G1", "G7", "G8"}
    unhandled = sorted(x for g, xs in parents.items() if g in per_parent for x in xs if x not in have)
    vanished = sorted(x for x in have if x and x.split(":", 1)[0] in ("pg", "qdrant", "lark") and
                      x not in {y for g in per_parent for y in parents.get(g, [])})
    rows = [[g, x] for g, xs in parents.items() for x in xs]
    nn, hh, _ = canon(rows)
    return {"parents": parents, "errors": errors, "new_source_unhandled": unhandled, "vanished": vanished, "count": nn, "sha256": hh,
            "status": DU if not errors and not unhandled and not vanished else MP,
            "reasons": [("GATE_READ_FAIL " + e) for e in errors] + [("NEW_SOURCE_UNHANDLED " + x) for x in unhandled] +
                       [("SOURCE_VANISHED " + x) for x in vanished]}


# =========================================================================== lượt cấp giấy
def load_graph():
    sys.path.insert(0, RB)
    import r7_g1lib
    g = r7_g1lib.load(G1)
    return g, g.password()


def run(g=None, pw=None, only=None, b88_input=None, injected=None, write=True, now=None, ids_out=None, run_label="manual"):
    t0 = time.time()
    now = time.time() if now is None else now
    cat = jload(CELLS)
    if not cat or cat.get("format") != "graph-cert-cells-v1":
        raise RuntimeError("cert-cells.json thiếu/sai định dạng")
    cells = cat["cells"]
    if only:
        cells = [c for c in cells if c["key"] in only]
    if g is None:
        g, pw = load_graph()
    S = Sources(cat["cells"], b88_input=b88_input, injected=injected)
    try:
        ginv = g.invariants(pw)
        gsnap = {"gs_keys_sha256": ginv.get("gs_keys_sha256"), "edges_sha256": ginv.get("edges_sha256"), "gs_keys_count": ginv.get("gs_keys_count"),
                 "edges_count": ginv.get("edges_count"), "read_at": now_iso()}
    except Exception as e:  # noqa: BLE001
        gsnap = {"error": type(e).__name__}
    res = {}
    for c in cells:
        ct = time.time()
        if c["source"].get("adapter") == "mb":
            m = mb_cell(S, ids_out)
            r = {"key": c["key"], "gate": c["gate"], "parent": c.get("parent"), "scope": c.get("scope"), "gap": c.get("gap"),
                 "source_authority": c.get("authority"), "mb": m, "reader_pass": m["ok"], "status": MP, "reasons": []}
            if not m["ok"]:
                r["reasons"].append(m.get("why"))
            elif any(v for k, v in m["buckets"].items() if k != "pg_live_not_ready_in_qdrant"):
                r["reasons"].append("KB_QDRANT_ID_MISMATCH " + ",".join("%s=%s" % (k, v) for k, v in m["buckets"].items() if v))
            else:
                r["status"], r["issued_at"], r["expires_at"] = DU, now_iso(now), now_iso(now + MAX_TTL_H * 3600)
            res[c["key"]] = r
            continue
        src = source_for(c, S)
        gr = {}
        if c.get("graph") and src.get("ok"):
            try:
                go, ge, gm = graph_read(g, pw, c["graph"])
                gr = {"objects": go, "edges": ge, "meta": gm}
            except Exception as e:  # noqa: BLE001
                gr = {"error": "%s %s" % (type(e).__name__, str(e)[:120])}
        r = evaluate(c, src, gr, now, cat.get("ttl_hours", MAX_TTL_H))
        r["graph_snapshot"] = gsnap
        r["seconds"] = round(time.time() - ct, 1)
        res[c["key"]] = r
    dr = directory(cat["cells"], S) if not only else None
    prev = jload(CURRENT)
    if only and prev and verify_manifest(prev, now)[0]:
        merged = dict(prev["cells"])
        merged.update(res)
        res, dr = merged, prev.get("directory")
    readers = {k: (v.get("_error") or v.get("error")) for k, v in S.cache.items() if isinstance(v, dict) and (v.get("_error") or v.get("error"))}
    doc = {"format": FORMAT, "catalog_version": cat.get("catalog_version"), "catalog_sha256": hashlib.sha256(open(CELLS, "rb").read()).hexdigest(),
           "run": {"label": run_label, "only": sorted(only) if only else None, "seconds": round(time.time() - t0, 1)},
           "generated_at": now_iso(now), "graph_snapshot": gsnap, "cells": res, "directory": dr, "reader_errors": readers,
           "contract": "verification evidence/quality contract, NOT a cryptographic certificate, NOT proof of semantic truth of the source"}
    doc["summary"] = summarize(doc)
    doc["self_sha256"] = self_sha(doc)
    if write:
        write_manifest(doc)
    return doc


def summarize(doc):
    cs = doc["cells"].values()
    du = sorted(c["key"] for c in cs if c["status"] == DU)
    return {"cells": len(doc["cells"]), "du": len(du), "mot_phan": len(doc["cells"]) - len(du), "du_cells": du,
            "directory": (doc.get("directory") or {}).get("status"), "reader_fail": sorted(c["key"] for c in cs if not c.get("reader_pass"))}


def write_manifest(doc):
    os.makedirs(CERT_DIR, mode=0o750, exist_ok=True)
    old = jload(CURRENT)
    if old and verify_manifest(old)[0]:
        tmp = LAST_GOOD + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(old, f, ensure_ascii=False, indent=1, sort_keys=True)
        os.replace(tmp, LAST_GOOD)
    tmp = CURRENT + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.flush()
        os.fsync(f.fileno())
    os.chmod(tmp, 0o640)
    os.replace(tmp, CURRENT)


# =========================================================================== kiểm giấy tại giờ hỏi (dùng bởi nhãn N4)
def verify_manifest(doc, now=None):
    now = time.time() if now is None else now
    if not isinstance(doc, dict) or doc.get("format") != FORMAT:
        return False, "MANIFEST_MISSING_OR_BAD_FORMAT"
    if doc.get("self_sha256") != self_sha(doc):
        return False, "MANIFEST_CORRUPT_SELF_SHA256"
    g = parse_iso(doc.get("generated_at"))
    if g is None or g > now + CLOCK_SKEW:
        return False, "CLOCK_OR_GENERATED_AT_INVALID"
    return True, None


def effective(doc, now=None):
    """{cell: (status, reason, issued_at, expires_at)} tại giờ now; giấy hỏng/vắng ⇒ mọi ô MỘT PHẦN."""
    now = time.time() if now is None else now
    ok, why = verify_manifest(doc, now)
    if not ok:
        return {}, why
    out = {}
    for k, c in doc["cells"].items():
        exp = parse_iso(c.get("expires_at"))
        if c.get("status") != DU:
            out[k] = (MP, "; ".join(c.get("reasons") or [])[:200] or "NOT_CERTIFIED", None, None)
        elif exp is None or now >= exp:
            out[k] = (MP, "EXPIRED", c.get("issued_at"), c.get("expires_at"))
        elif exp - parse_iso(c.get("issued_at") or "1970-01-01T00:00:00") > MAX_TTL_H * 3600 + 60:
            out[k] = (MP, "TTL_OVER_26H", c.get("issued_at"), c.get("expires_at"))
        else:
            out[k] = (DU, None, c.get("issued_at"), c.get("expires_at"))
    d = doc.get("directory")
    out["directory:g1-g9"] = (DU if d and d.get("status") == DU and now - parse_iso(doc["generated_at"]) < MAX_TTL_H * 3600 else MP,
                              None if d and d.get("status") == DU else "; ".join((d or {}).get("reasons") or ["NO_DIRECTORY"])[:200],
                              doc.get("generated_at"), None)
    return out, None


# =========================================================================== N4 — nhãn câu trả lời graph-v1
QUERY_CATALOG_VERSION = "n4-qc-1"
RE_NODE = re.compile(r"\(\s*([A-Za-z_]\w*)?\s*((?::\s*`?[A-Za-z_]\w*`?\s*)+)?(?:\{[^{}]*\})?\s*\)")
RE_REL = re.compile(r"\[\s*([A-Za-z_]\w*)?\s*(?::\s*([^\]\s{*]+))?\s*(\*[^\]{]*)?\s*(?:\{[^{}]*\})?\s*\]")
RE_PROP = re.compile(r"\b([A-Za-z_]\w*)\.([A-Za-z_]\w*)\b")
RE_STR = re.compile(r"'(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\"")
UNSUPPORTED = re.compile(r"\b(CALL|apoc|db\.|dbms\.|gds\.|LOAD\s+CSV|shortestPath|allShortestPaths|EXISTS\s*\{|COUNT\s*\{|COLLECT\s*\{)\b", re.I)


def _is_call(body, pos):
    """'(' dính liền sau tên hàm (count(n), labels(n)…) ⇒ không phải mẫu nút; 'MATCH (' có khoảng trắng ⇒ là mẫu nút."""
    return pos > 0 and (body[pos - 1].isalnum() or body[pos - 1] == "_")


def classify_query(q, cat):
    """⇒ (query_class, required_cells, reason). Bảo thủ: không hiểu ⇒ UNSUPPORTED (mọi ô)."""
    lm, rm = cat.get("graph_label_map") or {}, cat.get("graph_rel_map") or {}
    props_ok, cover = cat.get("certified_props") or {}, cat.get("endpoint_cover") or {}
    body = RE_STR.sub("''", q or "")
    if not body.strip():
        return "UNSUPPORTED", ["*"], "truy vấn rỗng"
    if UNSUPPORTED.search(body):
        return "UNSUPPORTED", ["*"], "thủ tục/APOC/subquery/đường ngắn nhất ngoài danh mục"
    nodes, rels, var_label, rel_vars = [], [], {}, set()
    for m in RE_NODE.finditer(body):
        if _is_call(body, m.start()):
            continue
        ls = [x.strip(" :`") for x in (m.group(2) or "").split(":") if x.strip(" :`")]
        if m.group(1) and ls:
            var_label.setdefault(m.group(1), set()).update(ls)
        before, after = body[max(0, m.start() - 3):m.start()], body[m.end():m.end() + 3]
        adj = bool(re.search(r"-\s*$|>\s*$", before) or re.match(r"^\s*(-|<)", after))
        keys = re.findall(r"([A-Za-z_]\w*)\s*:", (re.search(r"\{([^{}]*)\}", m.group(0)) or [None, ""])[1] or "")
        nodes.append((m.group(1), ls, adj, keys))
    for m in RE_REL.finditer(body):
        if m.group(1):
            rel_vars.add(m.group(1))
        if m.group(3):
            return "IMPACT_OR_PATH", ["*"], "đường độ dài thay đổi (*) = câu hỏi tác động/đường đi, cần mọi lớp quan hệ"
        if not m.group(2):
            return "UNSUPPORTED", ["*"], "cạnh không ghi loại"
        for t in m.group(2).split("|"):
            t = t.strip(" `:")
            if t not in rm:
                return "UNSUPPORTED", ["*"], "loại cạnh ngoài danh mục: " + t
            rels.append(t)
        if re.search(r"\{[^{}]*\}", m.group(0)):
            return "UNCERTIFIED_PROPERTY", ["*"], "lọc theo thuộc tính cạnh (không nằm trong phần băm)"
    need = {c for t in rels for c in rm[t]}
    standalone = set()
    for v, ls, adj, keys in nodes:
        if not ls and not (v and v in var_label):
            return "UNSUPPORTED", ["*"], "nút không nhãn (quét toàn Graph)"
        labs = ls or sorted(var_label.get(v, ()))
        for l in labs:
            if l not in lm:
                return "UNSUPPORTED", ["*"], "nhãn ngoài danh mục: " + l
            for k in keys:
                if k not in props_ok.get(l, []):
                    return "UNCERTIFIED_PROPERTY", ["*"], "thuộc tính %s.%s không nằm trong phần băm của ô" % (l, k)
            if not adj:
                standalone.add(l)
    for v, ls, adj, keys in nodes:
        for l in ls or sorted(var_label.get(v, ())):
            covered = l not in standalone and set(cover.get(l, [])) & set(rels)
            if not covered:
                need.update(lm[l])
    for v, p in RE_PROP.findall(body):
        if v in rel_vars:
            return "UNCERTIFIED_PROPERTY", ["*"], "thuộc tính cạnh %s.%s không nằm trong phần băm" % (v, p)
        if v in var_label:
            allowed = set().union(*(set(props_ok.get(l, [])) for l in var_label[v]))
            if p not in allowed:
                return "UNCERTIFIED_PROPERTY", ["*"], "thuộc tính %s.%s không nằm trong phần băm của ô" % (v, p)
    ret = re.split(r"\bRETURN\b", body, flags=re.I)
    if len(ret) > 1:   # trả nguyên nút/cạnh/đường ⇒ gồm thuộc tính chưa băm (chỉ cho phép trong count(...))
        tail = re.sub(r"\bcount\s*\(\s*(DISTINCT\s+)?[A-Za-z_]\w*\s*\)", " ", ret[-1], flags=re.I)
        tail = re.sub(r"\bAS\s+[A-Za-z_]\w*", " ", tail, flags=re.I)              # bí danh cột không phải biến
        bare = set(var_label) | rel_vars | set(re.findall(r"\b([A-Za-z_]\w*)\s*=\s*\(", body))
        for v in sorted(bare):
            if re.search(r"(?<![\w.])%s\b(?!\s*\.)" % re.escape(v), tail):
                return "UNCERTIFIED_PROPERTY", ["*"], "trả nguyên %s (gồm thuộc tính chưa nằm trong phần băm)" % v
    if not need:
        return "UNSUPPORTED", ["*"], "không xác định được ô"
    return "CELL_SCOPED_LOOKUP", sorted(need), None


def label_for(tool, arguments=None, result_rows=None, now=None, doc=None, cat=None):
    """Nhãn máy đọc được cho MỘT câu trả lời graph-v1. Không bao giờ ném lỗi: lỗi ⇒ MỘT PHẦN."""
    now = time.time() if now is None else now
    lab = {"format": LABEL_FORMAT, "completeness_label": MP, "proof_issued_at": None, "expires_at": None, "relevant_cell_ids": [],
           "missing_or_unknown_cell_ids": [], "source_scope": None, "trust": None, "query_actionability": ACT_NO,
           "evidence": {"manifest": CURRENT}, "query_class": None, "query_catalog_version": QUERY_CATALOG_VERSION,
           "reason": None, "computed_at": now_iso(now),
           "note": "Nhãn = ô kém nhất câu hỏi cần (CT4). Vắng cạnh ≠ không có quan hệ trừ khi mọi ô cần ĐỦ. Giấy là bằng chứng kiểm định, "
                   "không phải chứng thư mật mã."}
    try:
        cat = cat if cat is not None else jload(CELLS)
        doc = doc if doc is not None else jload(CURRENT)
        if not cat:
            lab["reason"] = "CATALOG_MISSING"
            return lab
        eff, why = effective(doc, now)
        if doc and isinstance(doc, dict):
            lab["evidence"].update(manifest_self_sha256=doc.get("self_sha256"), generated_at=doc.get("generated_at"),
                                   graph_snapshot=(doc.get("graph_snapshot") or {}).get("gs_keys_sha256"))
        if why:
            lab["reason"] = why
            lab["missing_or_unknown_cell_ids"] = ["*"]
            return lab
        if tool == "get-schema":
            lab.update(query_class="GRAPH_SCHEMA", reason="lược đồ Graph không phải khẳng định đủ về nguồn", relevant_cell_ids=["directory:g1-g9"],
                       missing_or_unknown_cell_ids=sorted(k for k, v in eff.items() if v[0] != DU))
            return lab
        q = (arguments or {}).get("query") or (arguments or {}).get("cypher") or ""
        qc, need, reason = classify_query(q, cat)
        lab["query_class"] = qc
        if "*" in need:
            need = sorted(eff)
        miss = sorted(k for k in need if eff.get(k, (MP,))[0] != DU)
        lab["relevant_cell_ids"] = need
        lab["missing_or_unknown_cell_ids"] = miss
        lab["source_scope"] = sorted({(c.get("scope") or c["key"]) for c in cat["cells"] if c["key"] in need})[:12]
        lab["trust"] = sorted({c.get("trust", "EXACT_AT_SNAPSHOT") for c in cat["cells"] if c["key"] in need})
        if qc == "CELL_SCOPED_LOOKUP" and not miss:
            iss = [eff[k][2] for k in need]
            exp = [eff[k][3] for k in need]
            lab.update(completeness_label=DU, proof_issued_at=min(iss), expires_at=min(exp), query_actionability=ACT_OK,
                       reason="mọi ô cần có giấy còn hạn" + ("; kết quả rỗng được chứng nhận trong phạm vi ô" if result_rows == 0 else ""))
            lab["evidence"]["cells"] = {k: doc["cells"][k].get("proof") for k in need if k in doc["cells"]}
        else:
            lab["reason"] = reason or ("ô chưa ĐỦ: " + ", ".join(miss[:8]) + ("…" if len(miss) > 8 else ""))
            if result_rows == 0:
                lab["reason"] += "; kết quả rỗng KHÔNG chứng minh vắng quan hệ"
        return lab
    except Exception as e:  # noqa: BLE001
        lab["reason"] = "LABEL_ENGINE_ERROR %s" % type(e).__name__
        lab["missing_or_unknown_cell_ids"] = ["*"]
        return lab


# =========================================================================== CT5 — đèn + biên nhận sự cố
def alarm(doc, op_failure=None, now=None, baseline=None):
    """⇒ (status 'up'|'down', msg ≤ 200, incidents[]). CT5 (Owner): đèn xuống khi máy không chạy được hoặc ô TỤT KHỎI ĐỦ so với mốc.
    Gọi trang (DOWN): OPERATIONAL (lượt bỏ qua, máy/giấy lỗi, bộ đọc từng đọc được nay hỏng, cửa không đọc được) · COVERAGE_REGRESSION
    (ô thuộc sàn certified_floor không còn ĐỦ — gồm hết hạn) · NEW_SOURCE_UNHANDLED / SOURCE_VANISHED ở cửa G1–G9.
    Không gọi trang, chỉ biên nhận + nêu tên trong tin: ô MỘT PHẦN chưa được Host nhận mốc (PENDING_HOST_ACK). Mốc chỉ dập tin trùng —
    không bao giờ làm ô xanh."""
    now = time.time() if now is None else now
    baseline = baseline if baseline is not None else (jload(BASELINE) or {})
    acc = {k: v for k, v in (baseline.get("accepted_partial") or {}).items()
           if not v.get("accepted_until") or (parse_iso(v["accepted_until"]) or 0) > now}   # ACK có hạn: hết hạn ⇒ lại chờ Host
    floor = set(baseline.get("certified_floor") or [])
    acc_parents = set(baseline.get("accepted_directory_parents") or [])
    record_only = set(baseline.get("record_only_gates") or [])
    ephemeral = [re.compile(x) for x in baseline.get("ephemeral_parent_patterns") or []]
    inc = []
    if op_failure:
        inc.append({"kind": "OPERATIONAL", "cell": "graph-refresh", "reason": op_failure, "page": True})
    if doc is not None:
        ok, why = verify_manifest(doc, now)
        if not ok:
            inc.append({"kind": "OPERATIONAL", "cell": "manifest", "reason": why, "page": True})
        else:
            eff = effective(doc, now)[0]
            for k, c in doc["cells"].items():
                st_ = eff.get(k, (MP,))[0]
                reasons = "; ".join(c.get("reasons") or [])[:120] or (eff.get(k, (MP, ""))[1] or "")
                failed = not c.get("reader_pass") and str((c.get("reasons") or [""])[0]).startswith("READER_FAIL")
                if failed and (k in floor or (acc.get(k) or {}).get("reader_pass") or (k not in acc and k not in floor)):
                    inc.append({"kind": "OPERATIONAL", "cell": k, "reason": "bộ đọc hỏng: " + reasons, "page": True})
                elif k in floor and st_ != DU:
                    inc.append({"kind": "COVERAGE_REGRESSION", "cell": k, "reason": reasons or "không còn ĐỦ", "page": True})
                elif st_ != DU and k not in acc and k not in floor:
                    inc.append({"kind": "PENDING_HOST_ACK", "cell": k, "reason": reasons, "page": False})
            for k in sorted(floor - set(doc["cells"])):
                inc.append({"kind": "COVERAGE_REGRESSION", "cell": k, "reason": "ô sàn vắng trong giấy", "page": True})
            d = doc.get("directory") or {}
            for e in d.get("errors") or []:
                inc.append({"kind": "OPERATIONAL", "cell": "directory", "reason": "GATE_READ_FAIL " + e, "page": True})
            for x in d.get("new_source_unhandled") or []:
                inc.append({"kind": "NEW_SOURCE_UNHANDLED", "cell": "directory", "reason": x, "page": True})
            for x in d.get("vanished") or []:
                inc.append({"kind": "SOURCE_VANISHED", "cell": "directory", "reason": x, "page": True})
            for g, xs in (d.get("parents") or {}).items():
                if g in record_only or not acc_parents:
                    continue
                for x in xs:
                    if x not in acc_parents and not any(e.search(x) for e in ephemeral):
                        inc.append({"kind": "NEW_SOURCE_UNHANDLED", "cell": "directory:" + g, "reason": x, "page": True})
                for x in sorted({y for y in acc_parents if y.startswith(_gate_prefix(g))} - set(xs)):
                    inc.append({"kind": "SOURCE_VANISHED", "cell": "directory:" + g, "reason": x, "page": True})
    for i in inc:
        i["id"] = hashlib.sha256(("%s|%s|%s" % (i["kind"], i["cell"], re.sub(r"\d+", "#", i["reason"]))).encode()).hexdigest()[:10]
    pages = [i for i in inc if i["page"]]
    pend = [i["cell"] for i in inc if i["kind"] == "PENDING_HOST_ACK"]
    tail = (" · chờ Host nhận mốc: " + ", ".join(pend[:4]) + ("…" if len(pend) > 4 else "")) if pend else ""
    if not pages:
        s = (doc or {}).get("summary") or {}
        return "up", ("OK ĐỦ %s/%s ô · sàn %d giữ ĐỦ · MỘT PHẦN đã nhận mốc %d%s" % (s.get("du"), s.get("cells"), len(floor), len(acc), tail))[:200], inc
    kinds = sorted({i["kind"] for i in pages})
    msg = "%s: %s" % ("+".join(kinds), "; ".join("%s %s" % (i["cell"], i["reason"][:40]) for i in pages[:4]))
    return "down", (msg + tail)[:200], inc


def _gate_prefix(g):
    return {"G1": "pg:", "G2": "docker:", "G3": "systemd:", "G4": "cron:", "G5": "nginx:", "G6": "opt:", "G7": "qdrant:", "G8": "lark:", "G9": "git:"}[g]


def record_incidents(inc, now=None):
    """Biên nhận sự cố máy đọc được (sổ tin báo của ô): mỗi mã mới ⇒ một dòng OPEN; mã biến mất ⇒ RESOLVED. ⇒ (mới, đã hồi)."""
    now = time.time() if now is None else now
    os.makedirs(CERT_DIR, mode=0o750, exist_ok=True)
    st = jload(ALARM_STATE, {}) or {}
    open_ = st.get("open") or {}
    cur = {i["id"]: i for i in inc}
    new = [i for k, i in cur.items() if k not in open_]
    gone = [open_[k] for k in open_ if k not in cur]
    with open(INCIDENTS, "a", encoding="utf-8") as f:
        for i in new:
            f.write(json.dumps(dict(i, event="OPEN", at=now_iso(now)), ensure_ascii=False) + "\n")
        for i in gone:
            f.write(json.dumps(dict(i, event="RESOLVED", at=now_iso(now)), ensure_ascii=False) + "\n")
    st = {"open": {k: dict(v, first_seen=(open_.get(k) or {}).get("first_seen") or now_iso(now)) for k, v in cur.items()}, "updated_at": now_iso(now)}
    tmp = ALARM_STATE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(st, f, ensure_ascii=False, indent=1)
    os.replace(tmp, ALARM_STATE)
    return new, gone


# =========================================================================== CLI
def main(argv):
    import argparse
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("run")
    s.add_argument("--cells")
    s.add_argument("--b88-input")
    s.add_argument("--no-write", action="store_true")
    s.add_argument("--out")
    s.add_argument("--mb-ids-out")
    sub.add_parser("status")
    s = sub.add_parser("label")
    s.add_argument("--query", default="")
    s.add_argument("--rows", type=int)
    s.add_argument("--tool", default="read-cypher")
    a = ap.parse_args(argv)
    if a.cmd == "run":
        doc = run(only=set(a.cells.split(",")) if a.cells else None, b88_input=a.b88_input, write=not a.no_write, ids_out=a.mb_ids_out)
        if a.out:
            with open(a.out, "w", encoding="utf-8") as f:
                json.dump(doc, f, ensure_ascii=False, indent=1, sort_keys=True)
        print("CERT %s" % json.dumps(doc["summary"], ensure_ascii=False))
        return 0
    if a.cmd == "status":
        eff, why = effective(jload(CURRENT))
        print(json.dumps({"why": why, "cells": {k: v[0] + ((" · " + v[1]) if v[1] else "") for k, v in sorted(eff.items())}}, ensure_ascii=False, indent=1))
        return 0
    if a.cmd == "label":
        print(json.dumps(label_for(a.tool, {"query": a.query}, a.rows), ensure_ascii=False, indent=1))
        return 0
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
