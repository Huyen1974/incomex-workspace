#!/usr/bin/env python3
"""c1b_l2 — ỨNG VIÊN L2 (đọc văn bản, MỘT PHẦN) cho 11 bảng mẫu C1-B · GS-C1B-LAYERED-IMPACT-20261022-08

Chỉ đọc. Không chứng nhận gì: tham chiếu tĩnh KHÔNG chứng minh thực thi; đích động (EXECUTE/format) = UNKNOWN; hai đường cùng GHI một đích
= POTENTIAL_COLLISION (không phải đồng thời thật — L3 MỞ). Nguồn (bộ đọc sẵn có, cửa sổ có giới hạn):
  PG directus  pg_proc.prosrc (plpgsql/sql, ngoài extension) + pg_trigger (cả database) — trong container incomex-claude-mcp, vai
               context_pack_readonly, REPEATABLE READ READ ONLY; chỉ xuất ứng viên + sha256 thân hàm, KHÔNG xuất thân hàm
  Directus     directus_flows (trigger, options.scope/collections) + directus_operations (type, options.collection) — chỉ tên collection,
               không xuất giá trị khác của options (có thể chứa URL/khoá)
  văn bản      /opt/incomex/dot/bin · /opt/incomex/scripts · cây mã claude-mcp/claude-kb/lark-client · agent-data (container, /app) ·
               Nuxt bản build đang chạy (deploys/nuxt-output-n4/server) — grep -w tên bảng, ≤ 200 dòng/bảng/cây
Dùng: c1b_l2.py <cells.json> <out.json>   (root trên VPS). In tóm tắt.
"""
import hashlib, json, os, re, subprocess, sys, time

RUN = "GS-C1B-LAYERED-IMPACT-20261022-08"
CAP = 200
TREES = [("dot", "/opt/incomex/dot/bin", None), ("scripts", "/opt/incomex/scripts", None), ("claude-mcp", "/opt/incomex/claude-mcp", None),
         ("claude-kb", "/opt/incomex/claude-kb", None), ("lark-client", "/opt/incomex/lark-client", None),
         ("agent-data", "/app", "incomex-agent-data"), ("nuxt-web", "/opt/incomex/deploys/nuxt-output-n4/server", None)]
EXCL = ["--exclude-dir=" + d for d in (".git", ".venv", "venv", "site-packages", "node_modules", "__pycache__", "credentials", ".cache", "backups")]
W_RE = re.compile(r"\b(INSERT\s+INTO|UPDATE|DELETE\s+FROM|TRUNCATE|MERGE\s+INTO|UPSERT|ON\s+CONFLICT)\b|createItems?\b|updateItems?\b|deleteItems?\b|"
                  r"\.(insert|update|delete|upsert)\s*\(|method\s*[:=]\s*['\"](POST|PATCH|PUT|DELETE)", re.I)
R_RE = re.compile(r"\b(SELECT|FROM|JOIN)\b|readItems?\b|\.select\s*\(", re.I)

PG = r'''
import hashlib, json, os, re
import psycopg
T = json.loads(os.environ["C1B_TABLES"])
OPT = "-c default_transaction_read_only=on -c statement_timeout=60000 -c lock_timeout=2000"
NS = "n.nspname NOT IN ('pg_catalog','information_schema','pg_toast') AND n.nspname NOT LIKE 'pg_temp%'"
c = psycopg.connect(host=os.environ.get("PG_HOST", "postgres"), user=os.environ["PG_USER_RO"], password=os.environ["PG_PASSWORD_RO"], dbname="directus",
                    options=OPT, autocommit=True)
cur = c.cursor()
cur.execute("BEGIN ISOLATION LEVEL REPEATABLE READ READ ONLY")
cur.execute("SELECT pg_current_snapshot()::text, to_char(clock_timestamp() AT TIME ZONE 'UTC','YYYY-MM-DD\"T\"HH24:MI:SS\"Z\"')")
snap, ts = cur.fetchone()
cur.execute("SELECT n.nspname||'.'||p.proname||'('||pg_get_function_identity_arguments(p.oid)||')', l.lanname, p.prosrc FROM pg_proc p "
            "JOIN pg_namespace n ON n.oid=p.pronamespace JOIN pg_language l ON l.oid=p.prolang WHERE " + NS + " AND l.lanname IN ('plpgsql','sql') "
            "AND NOT EXISTS (SELECT 1 FROM pg_depend d WHERE d.classid='pg_proc'::regclass AND d.objid=p.oid AND d.deptype='e')")
funcs = cur.fetchall()
cur.execute("SELECT n.nspname||'.'||c.relname, t.tgname, pn.nspname||'.'||p.proname||'('||pg_get_function_identity_arguments(p.oid)||')' "
            "FROM pg_trigger t JOIN pg_class c ON c.oid=t.tgrelid JOIN pg_namespace n ON n.oid=c.relnamespace JOIN pg_proc p ON p.oid=t.tgfoid "
            "JOIN pg_namespace pn ON pn.oid=p.pronamespace WHERE NOT t.tgisinternal")
trg = cur.fetchall()
cur.execute("SELECT f.id::text, f.name, f.status, f.trigger, f.options::text FROM directus_flows f")
flows = cur.fetchall()
cur.execute("SELECT o.id::text, o.flow::text, o.type, o.options::text FROM directus_operations o")
ops = cur.fetchall()
cur.execute("ROLLBACK")
c.close()
ident = r'(?:"?[A-Za-z_][\w]*"?\s*\.\s*)?"?([A-Za-z_][\w]*)"?'
W = re.compile(r"\b(INSERT\s+INTO|UPDATE|DELETE\s+FROM|TRUNCATE(?:\s+TABLE)?|MERGE\s+INTO)\s+(?:ONLY\s+)?" + ident, re.I)
R = re.compile(r"\b(FROM|JOIN)\s+(?:ONLY\s+)?" + ident, re.I)
CALL = re.compile(r"\b(PERFORM|SELECT)\s+(?:[A-Za-z_]\w*\.)?([A-Za-z_]\w*)\s*\(", re.I)
NOTIFY = re.compile(r"pg_notify\s*\(\s*'([^']+)'|\bNOTIFY\s+([A-Za-z_]\w*)", re.I)
F = {}
for fid, lang, src in funcs:
    s = re.sub(r"--[^\n]*", "", src or "")
    lines = s.split("\n")
    rec = {"lang": lang, "sha256": hashlib.sha256((src or "").encode()).hexdigest(), "writes": {}, "reads": {}, "calls": [], "notify": [],
           "dynamic": bool(re.search(r"\bEXECUTE\b(?!\s+(FUNCTION|PROCEDURE))", s, re.I)), "mentions": {}}
    for i, ln in enumerate(lines, 1):
        for m in W.finditer(ln):
            rec["writes"].setdefault(m.group(2).lower(), []).append(i)
        for m in R.finditer(ln):
            rec["reads"].setdefault(m.group(2).lower(), []).append(i)
        for m in CALL.finditer(ln):
            rec["calls"].append(m.group(2).lower())
        for m in NOTIFY.finditer(ln):
            rec["notify"].append(m.group(1) or m.group(2))
        for t in T:
            nm = t.split(".")[-1]
            if re.search(r"\b%s\b" % re.escape(nm), ln) and not W.search(ln) and not R.search(ln):
                rec["mentions"].setdefault(nm, []).append(i)
    rec["calls"] = sorted(set(rec["calls"]))[:40]
    rec["notify"] = sorted(set(rec["notify"]))
    F[fid] = rec
def names(o, keys=("collection", "collections", "scope")):
    try:
        d = json.loads(o or "null") or {}
    except ValueError:
        return {}
    return {k: d.get(k) for k in keys if isinstance(d, dict) and d.get(k) is not None}
print(json.dumps({"snapshot": {"pg_snapshot": snap, "snapshot_utc": ts}, "functions": F, "triggers": trg,
                  "flows": [[i, n, s, t, names(o)] for i, n, s, t, o in flows], "operations": [[i, f, t, names(o, ("collection",))] for i, f, t, o in ops]},
                 ensure_ascii=False))
'''


def sh(cmd, inp=None, timeout=300):
    p = subprocess.run(cmd, input=inp, capture_output=True, timeout=timeout)
    return p.returncode, p.stdout.decode(errors="replace"), p.stderr.decode(errors="replace")


def grep_tree(label, root, container, name):
    cmd = ["grep", "-rnIw", "--max-count=50"] + EXCL + ["-e", name, root]
    if container:
        cmd = ["docker", "exec", container] + cmd
    rc, o, _ = sh(cmd, timeout=180)
    hits = []
    for ln in o.splitlines():
        m = re.match(r"^(.*?):(\d+):(.*)$", ln)
        if not m:
            continue
        path, line, text = m.group(1), int(m.group(2)), m.group(3)
        if re.search(r"\.(bak|pre|orig|old)\b|\.bak-|\.pre-|\d{8}T\d{6}Z", path):
            continue
        op = "WRITE" if W_RE.search(text) else ("READ" if R_RE.search(text) else "REFERENCE")
        hits.append({"kind": "TEXT_" + label.upper().replace("-", "_"), "via": ("%s:%s" % (container, path)) if container else path, "line": line,
                     "op": op, "target": name, "trust": "STATIC_TEXT_CANDIDATE", "source": label,
                     "line_sha256": hashlib.sha256(text.encode()).hexdigest()[:16]})
    return hits[:CAP], len(hits), rc


def main(cells, out):
    cat = json.load(open(cells, encoding="utf-8"))
    tables = cat["l1_pilot"]["tables"]
    rc, o, e = sh(["docker", "exec", "-i", "-e", "C1B_TABLES=" + json.dumps(tables), "incomex-claude-mcp", "python", "-I", "-B", "-"], PG.encode(), 600)
    if rc:
        raise SystemExit("PG rc=%s %s" % (rc, e[-300:]))
    pg = json.loads(o)
    F, trg = pg["functions"], pg["triggers"]
    handler_of = {}
    for tbl, tg, fn in trg:
        handler_of.setdefault(fn, []).append("%s.%s" % (tbl, tg))
    res = {"format": "graph-l2-candidates-v1", "run": RUN, "generated_at": time.strftime("%FT%TZ", time.gmtime()), "pg_snapshot": pg["snapshot"],
           "contract": "L2 SOURCE_TEXT_DERIVED_PARTIAL: ứng viên đọc văn bản, luôn MỘT PHẦN; tham chiếu tĩnh không chứng minh thực thi; đích động = UNKNOWN; "
                       "POTENTIAL_COLLISION ≠ RUNTIME_CONFIRMED (L3 MỞ)",
           "functions_read": len(F), "functions_dynamic": sum(1 for v in F.values() if v["dynamic"]), "tables": {}, "text_trees": [t[0] for t in TREES]}
    for full in tables:
        T = full.split(".", 1)[1]
        nm = T.split(".")[-1]
        cand, unk = [], []
        # (1) trigger trên T → hàm xử lý → bảng hàm ghi/đọc (L1 cho hai bước đầu, L2 cho bước ghi)
        for tbl, tg, fn in trg:
            if tbl != T:
                continue
            f = F.get(fn) or {}
            for x, ls in sorted((f.get("writes") or {}).items()):
                cand.append({"kind": "TRIGGER_HANDLER_WRITES", "via": "%s.%s → %s" % (tbl, tg, fn), "target": x, "op": "WRITE", "trust": "STATIC_TEXT_CANDIDATE",
                             "source": "pg_proc.prosrc sha256 " + f["sha256"][:16], "line": ls[0]})
            for ch in f.get("notify") or []:
                cand.append({"kind": "TRIGGER_HANDLER_NOTIFY", "via": "%s.%s → %s" % (tbl, tg, fn), "target": "channel:" + ch, "op": "EMIT",
                             "trust": "STATIC_TEXT_CANDIDATE", "source": "pg_proc.prosrc sha256 " + f["sha256"][:16], "line": None})
            if f.get("dynamic"):
                unk.append({"via": "%s.%s → %s" % (tbl, tg, fn), "why": "EXECUTE động trong hàm xử lý ⇒ đích UNKNOWN", "source": "pg_proc.prosrc sha256 " + f["sha256"][:16]})
            shared = sorted(set(handler_of.get(fn, [])) - {"%s.%s" % (tbl, tg)})
            if shared:
                cand.append({"kind": "SHARED_HANDLER_L1", "via": fn, "target": "%d trigger khác dùng chung hàm" % len(shared), "op": "SHARES_HANDLER",
                             "trust": "EXACT_AT_SNAPSHOT (pg_trigger.tgfoid, cả database)", "source": "pg_trigger", "line": None, "others": shared[:12]})
        # (2) hàm bất kỳ ghi/đọc/nhắc T
        for fid, f in sorted(F.items()):
            if nm in (f.get("writes") or {}):
                cand.append({"kind": "FUNCTION_WRITES_TABLE", "via": fid, "target": nm, "op": "WRITE", "trust": "STATIC_TEXT_CANDIDATE",
                             "source": "pg_proc.prosrc sha256 " + f["sha256"][:16], "line": f["writes"][nm][0], "called_by_triggers": handler_of.get(fid, [])[:8]})
            elif nm in (f.get("reads") or {}):
                cand.append({"kind": "FUNCTION_READS_TABLE", "via": fid, "target": nm, "op": "READ", "trust": "STATIC_TEXT_CANDIDATE",
                             "source": "pg_proc.prosrc sha256 " + f["sha256"][:16], "line": f["reads"][nm][0]})
            if f.get("dynamic") and nm in (f.get("mentions") or {}):
                unk.append({"via": fid, "why": "EXECUTE động + tên bảng trong chuỗi ⇒ đọc/ghi UNKNOWN", "source": "pg_proc.prosrc sha256 " + f["sha256"][:16],
                            "line": f["mentions"][nm][0]})
        # (3) Directus flow/operation nhắc collection
        if T.startswith("public."):
            for fid, fname, st, trig, o in pg["flows"]:
                cols = o.get("collections") or []
                if nm in (cols if isinstance(cols, list) else [cols]):
                    cand.append({"kind": "DIRECTUS_FLOW_TRIGGER", "via": "flow %s «%s» (%s, %s)" % (fid[:8], fname, trig, st), "target": nm,
                                 "op": "TRIGGERED_BY " + ",".join(o.get("scope") or []) if isinstance(o.get("scope"), list) else "TRIGGERED_BY",
                                 "trust": "DECLARED_FLOW_CONFIG", "source": "directus_flows.options", "line": None})
            for oid, flow, typ, o in pg["operations"]:
                if o.get("collection") == nm:
                    op = {"item-create": "WRITE", "item-update": "WRITE", "item-delete": "WRITE", "item-read": "READ"}.get(typ, "REFERENCE")
                    cand.append({"kind": "DIRECTUS_OPERATION", "via": "operation %s (%s) in flow %s" % (oid[:8], typ, (flow or "")[:8]), "target": nm, "op": op,
                                 "trust": "DECLARED_FLOW_CONFIG", "source": "directus_operations.options", "line": None})
        # (4) văn bản: DOT · scripts · mã
        counts = {}
        for label, root, cont in TREES:
            hits, n, rc_ = grep_tree(label, root, cont, nm)
            counts[label] = {"hits": n, "kept": len(hits), "rc": rc_}
            cand += hits
        writes = {}
        for c in cand:
            if c["op"] == "WRITE":
                w = c["via"].split(":")[0] if c["kind"].startswith("TEXT_") else c["via"]
                if c["kind"] == "DIRECTUS_OPERATION":          # nhiều operation trong MỘT flow = một đường ghi
                    w = "flow " + c["via"].rsplit(" ", 1)[-1]
                writes.setdefault(c["target"], set()).add(w)
        coll = [{"target": t, "writers": sorted(w)[:12], "writers_count": len(w), "status": "POTENTIAL_COLLISION",
                 "not": "không có dấu vết chạy đồng thời — L3 MỞ"} for t, w in sorted(writes.items()) if len(w) >= 2]
        res["tables"][full] = {"candidates": cand, "candidates_count": len(cand), "unknown_dynamic": unk, "potential_collisions": coll, "text_hits": counts,
                               "by_kind": {k: sum(1 for c in cand if c["kind"] == k) for k in sorted({c["kind"] for c in cand})}}
    body = json.dumps(res, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    res["self_sha256"] = hashlib.sha256(body.encode()).hexdigest()
    json.dump(res, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1, sort_keys=True)
    for full, v in res["tables"].items():
        print("L2 %-48s cand=%-4d unknown=%-3d collisions=%-3d %s" % (full, v["candidates_count"], len(v["unknown_dynamic"]), len(v["potential_collisions"]), v["by_kind"]))
    print("L2 functions_read=%d dynamic=%d self_sha256=%s" % (res["functions_read"], res["functions_dynamic"], res["self_sha256"][:16]))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(2)
    main(*sys.argv[1:])
