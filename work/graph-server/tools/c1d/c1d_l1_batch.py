#!/usr/bin/env python3
# GS-C1D · chọn TẤT ĐỊNH lô bảng L1 mới (≤16, không phải 394) cho lane c1d:pgl1 — CHỈ ĐỌC (catalog qua vai chỉ-đọc, bộ nạp C1-B).
# Ứng viên: bảng directus (relkind r/p) có ≥1 khoá ngoại vào/ra (mang quan hệ), ngoài 11 bảng mẫu; thứ tự sha256(SEED + khoá); nhận lần lượt
# nếu phần cộng thêm của riêng bảng đó ≤ trần/bảng và cộng dồn ≤ ngân sách lô. Dùng: c1d_l1_batch.py <cert-cells> <c1b_l1.py> <out.json>
import hashlib, importlib.machinery, importlib.util, json, subprocess, sys
cells_p, l1_p, out = sys.argv[1:4]
SEED, MAXN, BUDGET_N, BUDGET_E, PER_N, PER_E = "GS-C1D-L1-BATCH-1:", 16, 300, 600, 40, 80
ldr = importlib.machinery.SourceFileLoader("c1b_l1_b", l1_p)
L1 = importlib.util.module_from_spec(importlib.util.spec_from_loader("c1b_l1_b", ldr))
ldr.exec_module(L1)
cat = json.load(open(cells_p))
pilot = list(cat["l1_pilot"]["tables"])
PG = r'''
import json, os, psycopg
c = psycopg.connect(host="postgres", port="5432", user=os.environ["PG_USER_RO"], password=os.environ["PG_PASSWORD_RO"], dbname="directus", connect_timeout=5,
                    options="-c default_transaction_read_only=on -c statement_timeout=30000", autocommit=True)
cur = c.cursor()
cur.execute("SELECT DISTINCT n1.nspname||'.'||c1.relname FROM pg_constraint co JOIN pg_class c1 ON c1.oid=co.conrelid JOIN pg_namespace n1 ON n1.oid=c1.relnamespace "
            "WHERE co.contype='f' AND c1.relkind IN ('r','p') UNION SELECT DISTINCT n2.nspname||'.'||c2.relname FROM pg_constraint co JOIN pg_class c2 ON c2.oid=co.confrelid "
            "JOIN pg_namespace n2 ON n2.oid=c2.relnamespace WHERE co.contype='f' AND c2.relkind IN ('r','p') ORDER BY 1")
print(json.dumps([r[0] for r in cur.fetchall()]))
'''
p = subprocess.run(["docker", "exec", "-i", "incomex-claude-mcp", "python", "-I", "-B", "-"], input=PG.encode(), capture_output=True, timeout=120)
if p.returncode:
    raise SystemExit("PG rc=%s %s" % (p.returncode, p.stderr.decode()[-300:]))
fk_tables = ["directus." + x for x in json.loads(p.stdout)]
cand = sorted((t for t in fk_tables if t not in pilot and not t.split(".")[1] in ("pg_catalog", "information_schema")), key=lambda t: hashlib.sha256((SEED + t).encode()).hexdigest())


def size(tables):
    n, e, _ = L1.build(L1.native(tables), tables)
    return set(n), set(e)
base_n, base_e = size(pilot)
chosen, cur_n, cur_e, log = [], set(base_n), set(base_e), []
for t in cand:
    if len(chosen) >= MAXN:
        break
    n, e = size(pilot + chosen + [t])
    dn, de = len(n - cur_n), len(e - cur_e)
    ok = dn <= PER_N and de <= PER_E and len(n - base_n) <= BUDGET_N and len(e - base_e) <= BUDGET_E
    log.append({"table": t, "rank_sha": hashlib.sha256((SEED + t).encode()).hexdigest()[:12], "add_nodes": dn, "add_edges": de, "accepted": ok})
    if ok:
        chosen.append(t)
        cur_n, cur_e = n, e
res = {"seed": SEED, "rule": "bảng directus có ≥1 FK vào/ra, ngoài 11 mẫu; thứ tự sha256(SEED+khoá); nhận nếu thêm ≤%d nút/≤%d cạnh và lô ≤%d/≤%d" % (PER_N, PER_E, BUDGET_N, BUDGET_E),
       "fk_tables": len(fk_tables), "candidates": len(cand), "chosen": chosen, "batch_nodes_add": len(cur_n - base_n), "batch_edges_add": len(cur_e - base_e),
       "pilot_nodes": len(base_n), "pilot_edges": len(base_e), "log": log}
json.dump(res, open(out, "w"), ensure_ascii=False, indent=1)
print(json.dumps({k: v for k, v in res.items() if k != "log"}, ensure_ascii=False))
