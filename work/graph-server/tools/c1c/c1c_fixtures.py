#!/usr/bin/env python3
# GS-C1C-PRODUCTION-TRUST-GATE-20261023-09 · LỖI GIẢ CÔ LẬP cho graph_cert v4 (c1c-1): K1 hàng rào phiên bản Graph · K2 không cắt im ·
#   G1–G9 phát hiện thêm/sửa/xoá cha + con · báo động ĐỎ/VÀNG/ghi sổ. Không chạm Neo4j/PG/Directus/Qdrant/Lark production: mọi trạng thái
#   ở thư mục tạm (GS_CERT_DIR), nguồn = dữ liệu tiêm, Graph = đối tượng giả. Fixture KHÔNG phải lượt timer tự nhiên.
# Dùng: python3 -I c1c_fixtures.py <graph_cert.py ứng viên> <cert-cells.json> <current.json thật (chỉ đọc)> <l2-candidates.json thật> [--out F]
# Exit 0 = mọi ca PASS · 1 = có ca FAIL
import copy, fcntl, hashlib, importlib.machinery, importlib.util, json, os, shutil, subprocess, sys, tempfile, time

CAND, CELLS_P, CUR_P, L2_P = sys.argv[1:5]
OUT = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else None
TMP = tempfile.mkdtemp(prefix="gs-c1c-fx-")
os.environ["GS_CERT_DIR"] = TMP + "/cert"
os.environ["GS_CERT_CELLS"] = CELLS_P
os.environ["GS_CERT_BASELINE"] = TMP + "/baseline.json"
os.makedirs(TMP + "/cert")
shutil.copyfile(L2_P, TMP + "/cert/l2-candidates.json")


def load(path, name):
    ldr = importlib.machinery.SourceFileLoader(name, path)
    m = importlib.util.module_from_spec(importlib.util.spec_from_loader(name, ldr))
    ldr.exec_module(m)
    return m


G = load(CAND, "graph_cert_c1c")
iso = G.parse_iso
NOW = iso("2026-10-23T05:00:00Z")
CAT = json.load(open(CELLS_P))
RES = []


def case(group, name, ok, detail=""):
    RES.append({"group": group, "case": name, "pass": bool(ok), "detail": str(detail)[:300]})


E0 = {"fence": "neo4j-http-bookmark+container-start", "bookmark_sha256": "a" * 64, "container": "8d69eb118434", "started_at": "2026-10-18T15:28:03Z",
      "restart_count": "0", "read_at": "2026-10-22T23:04:12Z"}


def sign(doc):
    doc.pop("self_sha256", None)
    doc["self_sha256"] = G.self_sha(doc)
    return doc


def cert_doc(epoch=E0, stable=True):
    d = json.load(open(CUR_P))
    d = copy.deepcopy(d)
    if epoch is not None:
        d["graph_epoch"] = dict(epoch, stable_during_run=stable)
    else:
        d.pop("graph_epoch", None)
    return sign(d)


live_ok = lambda: dict(E0)
IUQ = "MATCH (g:PgTrigger)-[:ON_TABLE]->(:PgTable {id: 'public.information_unit'}) RETURN g.id AS x"
TRQ = "MATCH (g:PgTrigger)-[:ON_TABLE]->(t:PgTable) RETURN count(g) AS c"
lab = lambda q, doc, live=live_ok, lock=False, rows=7, params=None, now=NOW: G.label_for("read-cypher", {"query": q, "params": params or {}}, rows, now, doc, CAT, live, lock)

# ============================================================== K1
d0 = cert_doc()
L = lab(IUQ, d0)
case("K1", "K1.0 đối chứng: mốc khớp ⇒ ĐỦ (L1 IU)", L["completeness_label"] == G.DU and L["graph_revision"]["status"] == "MATCH", L.get("reason"))
L = lab(TRQ, d0)
case("K1", "K1.0b đối chứng: ô trigger ĐỦ khi mốc khớp", L["completeness_label"] == G.DU, L.get("reason"))
chg = lambda: dict(E0, bookmark_sha256="b" * 64)
for q, nm in ((IUQ, "L1 IU"), (TRQ, "ô trigger"), ("MATCH (t:PgTable {id: 'public.khong_ton_tai'}) RETURN t.id AS x", "rỗng")):
    L = lab(q, d0, live=chg, rows=0 if nm == "rỗng" else 7)
    case("K1", "K1.1 (i) Graph đổi (bookmark khác), giấy cũ ⇒ MỘT PHẦN · %s" % nm,
         L["completeness_label"] == G.MP and L["query_actionability"] == G.ACT_NO and L["graph_revision"]["status"] == "GRAPH_CHANGED_SINCE_CERT"
         and L["reason"].startswith("GRAPH_CHANGED_SINCE_CERT"), L.get("reason"))
d_pin = cert_doc()
d_pin["graph_snapshot"] = dict(d_pin.get("graph_snapshot") or {})   # tệp ghim/invariants giữ nguyên (chưa cập nhật) — không được tin
sign(d_pin)
L = lab(IUQ, d_pin, live=chg)
case("K1", "K1.2 (ii) Graph đổi, tệp ghim chưa cập nhật (graph_snapshot = ghim cũ) ⇒ vẫn MỘT PHẦN (không tin ghim)",
     L["completeness_label"] == G.MP and L["graph_revision"]["status"] == "GRAPH_CHANGED_SINCE_CERT", L.get("reason"))


class FakeGraph:
    """Đồ giả Graph cho run(): DotCommand nodes; bookmark theo lịch (đổi giữa lượt ⇒ mô phỏng commit/crash giữa ghi và cấp giấy)."""

    def __init__(self, names, bookmarks):
        self.names, self.bms, self.calls = sorted(names), list(bookmarks), 0

    def http_cypher(self, stmts, pw, timeout=300):
        q, p = stmts[0]
        if q.startswith("RETURN 1"):
            b = self.bms[min(self.calls, len(self.bms) - 1)]
            self.calls += 1
            return {"results": [{"columns": ["x"], "data": [{"row": [1]}]}], "errors": [], "lastBookmarks": [b]}
        if "count(n)" in q:
            return {"results": [{"columns": ["c"], "data": [{"row": [len(self.names)]}]}], "errors": []}
        if "n.gs_key > $after" in q:
            rows = [["dot:command:" + n, n, [], True] for n in self.names if "dot:command:" + n > p["after"]][:p["page"]]
            return {"results": [{"columns": ["k", "id", "av", "gs"], "data": [{"row": r} for r in rows]}], "errors": []}
        return {"results": [{"columns": ["c"], "data": [{"row": [0]}]}], "errors": []}

    def invariants(self, pw):
        return {"gs_keys_sha256": "g" * 64, "edges_sha256": "e" * 64, "gs_keys_count": len(self.names), "edges_count": 0}


_orig_inspect = G.sh


def fake_sh(cmd, inp=None, timeout=300, env=None):
    if cmd[:2] == ["docker", "inspect"] and G.GRAPH_CTR in cmd:
        return 0, "8d69eb118434ffff|2026-10-18T15:28:03Z|true|0\n", ""
    return _orig_inspect(cmd, inp, timeout, env)


G.sh = fake_sh
inj = {"dot_bin": {"commands": ["dot-a", "dot-b"], "commands_after": ["dot-a", "dot-b"]}}
json.dump({"certified_floor": ["dot:command"]}, open(os.environ["GS_CERT_BASELINE"], "w"))
doc = G.run(FakeGraph(["dot-a", "dot-b"], ["FB:x1"]), "pw", only={"dot:command"}, injected=inj, write=False, now=NOW)
case("K1", "K1.3a đối chứng run(): bookmark đứng yên cả lượt ⇒ ô ĐỦ + mốc ổn định",
     doc["cells"]["dot:command"]["status"] == G.DU and doc["graph_epoch"]["stable_during_run"] is True, doc["cells"]["dot:command"].get("reasons"))
doc = G.run(FakeGraph(["dot-a", "dot-b"], ["FB:x1", "FB:x2"]), "pw", only={"dot:command"}, injected=inj, write=False, now=NOW)
case("K1", "K1.3 (iii) commit/crash giữa lượt cấp giấy (bookmark đầu ≠ cuối) ⇒ ô MỘT PHẦN GRAPH_CHANGED_DURING_CERT",
     doc["cells"]["dot:command"]["status"] == G.MP and "GRAPH_CHANGED_DURING_CERT" in doc["cells"]["dot:command"]["reasons"]
     and doc["graph_epoch"]["stable_during_run"] is False, doc["cells"]["dot:command"].get("reasons"))
L = lab(IUQ, sign(dict(d0, graph_epoch=dict(doc["graph_epoch"]))))
case("K1", "K1.3b giấy cấp khi Graph đổi giữa lượt ⇒ nhãn MỘT PHẦN UNVERIFIED", L["completeness_label"] == G.MP and
     L["graph_revision"]["status"] == "GRAPH_REVISION_UNVERIFIED", L.get("reason"))
cell = {"key": "x:trg", "gate": "G1", "graph": {"edges": [{"type": "ON_TABLE"}]}}
src = {"ok": True, "objects": [["PgTrigger", "public.a.t1", "O"]], "edges": [["public.a.t1", "ON_TABLE", "public.b"]], "consistency": "PG_REPEATABLE_READ_READ_ONLY"}
gr = {"objects": [["PgTrigger", "public.a.t1", "O"]], "edges": [["public.a.t1", "ON_TABLE", "public.a"]], "meta": {"complete": True, "problems": []}}
r = G.evaluate(cell, src, gr, NOW, 26)
case("K1", "K1.4 (iv) quan hệ nguồn đổi đích trong cùng cha (cùng số cạnh) ⇒ MỘT PHẦN EDGE_DIGEST_MISMATCH",
     r["status"] == G.MP and any(x.startswith("EDGE_DIGEST_MISMATCH") for x in r["reasons"]), r["reasons"])
L = lab(IUQ, d0, now=iso("2026-10-24T02:00:00Z"))
case("K1", "K1.5a (v) giấy hết hạn ⇒ MỘT PHẦN", L["completeness_label"] == G.MP, L.get("reason"))
bad = cert_doc()
bad["cells"]["l1:directus.public.information_unit"]["status"] = G.DU
bad["generated_at"] = "2026-10-22T23:04:13Z"                       # sửa sau khi ký
L = lab(IUQ, bad)
case("K1", "K1.5b (v) giấy hỏng (sửa sau ký) ⇒ MỘT PHẦN MANIFEST_CORRUPT", L["completeness_label"] == G.MP and "CORRUPT" in str(L["reason"]), L.get("reason"))
L = lab(IUQ, cert_doc(epoch=None))
case("K1", "K1.5c (v) giấy không có mốc phiên bản (cấp trước C1-C) ⇒ MỘT PHẦN GRAPH_REVISION_UNVERIFIED",
     L["completeness_label"] == G.MP and L["graph_revision"]["status"] == "GRAPH_REVISION_UNVERIFIED", L.get("reason"))
L = lab(IUQ, cert_doc(stable=False))
case("K1", "K1.5d (v) mốc không ổn định trong lượt ⇒ MỘT PHẦN", L["completeness_label"] == G.MP, L.get("reason"))
L = lab(IUQ, d0, live=lambda: {"error": "GRAPH_READ_FAIL URLError"})
case("K1", "K1.6a (vi) đường đọc mất phiên bản sống (Graph không đọc được) ⇒ MỘT PHẦN UNVERIFIED",
     L["completeness_label"] == G.MP and L["graph_revision"]["status"] == "GRAPH_REVISION_UNVERIFIED", L.get("reason"))
L = lab(IUQ, d0, live=lambda: dict(E0, started_at="2026-10-23T05:00:00Z"))
case("K1", "K1.6b Graph restart (StartedAt khác, bookmark như cũ) ⇒ MỘT PHẦN", L["completeness_label"] == G.MP and "started_at" in L["graph_revision"]["why"], L.get("reason"))
L = lab(IUQ, d0, lock=True)
case("K1", "K1.6c đang ghi (khoá graph-refresh giữ) ⇒ MỘT PHẦN GRAPH_MUTATION_IN_PROGRESS", L["completeness_label"] == G.MP and
     L["graph_revision"]["status"] == "GRAPH_MUTATION_IN_PROGRESS", L.get("reason"))
L = lab(IUQ, d0, lock=None)
case("K1", "K1.6d không đọc được /proc/locks ⇒ MỘT PHẦN", L["completeness_label"] == G.MP, L.get("reason"))
L = G.label_for("get-schema", {}, None, NOW, d0, CAT, chg, False)
case("K1", "K1.6e get-schema khi Graph đổi ⇒ MỘT PHẦN", L["completeness_label"] == G.MP, L.get("reason"))
# bộ nhãn cũ trong tiến trình MCP sống lâu (stale cache)
eng = TMP + "/engine/graph_cert.py"
os.makedirs(os.path.dirname(eng))
shutil.copyfile(CAND, eng)
E = load(eng, "graph_cert_engine_copy")
with open(eng, "a") as f:
    f.write("\n# bản mới cài (đổi băm)\n")
L = E.label_for("read-cypher", {"query": IUQ}, 7, NOW, d0, CAT, live_ok, False)
case("K1", "K1.6f bộ nhãn cũ trong bộ nhớ, tệp đã đổi ⇒ nạp bản trên đĩa (vẫn đúng nhãn)", L["completeness_label"] == G.DU and
     "graph_cert_live_" in str([k for k in E._FRESH.values()][0].__name__), L.get("reason"))
with open(eng, "a") as f:
    f.write("\nthis is not python (\n")
L = E.label_for("read-cypher", {"query": IUQ}, 7, NOW, d0, CAT, live_ok, False)
case("K1", "K1.6g tệp bộ nhãn mới hỏng ⇒ MỘT PHẦN LABEL_ENGINE_STALE (không dùng bộ cũ nói ĐỦ)",
     L["completeness_label"] == G.MP and str(L["reason"]).startswith("LABEL_ENGINE_STALE"), L.get("reason"))
if os.path.exists("/proc/locks"):
    lf = TMP + "/x.lock"
    open(lf, "w").close()
    p = subprocess.Popen([sys.executable, "-I", "-c", "import fcntl,sys,time;f=open(sys.argv[1],'w');fcntl.flock(f,fcntl.LOCK_EX);print('L',flush=True);time.sleep(30)", lf],
                         stdout=subprocess.PIPE)
    p.stdout.readline()
    held = G.refresh_lock_held(lf)
    p.kill(); p.wait()
    case("K1", "K1.7 /proc/locks thấy khoá FLOCK do tiến trình khác giữ (không tự lấy khoá)", held is True and G.refresh_lock_held(lf) is False, held)

# ============================================================== K2
l2 = json.load(open(L2_P))
iu = l2["tables"]["directus.public.information_unit"]["candidates"]
seen, cur, pages, order = [], None, [], []
while True:
    L = lab(IUQ, d0, params={"n4_page": cur} if cur else None)
    m = L["list_meta"]["layers.L2.candidates"]
    pages.append(m["shown"])
    seen += [json.dumps(c, sort_keys=True) for c in L["layers"]["L2"]["candidates"]]
    cur = m["next_cursor"]
    if not cur or len(pages) > 10:
        break
proj = [json.dumps({k: c.get(k) for k in ("kind", "via", "target", "op", "trust", "source", "line")}, sort_keys=True) for c in iu]
case("K2", "K2.1 IU 44 ứng viên, mỗi trang 12: 12/12/12/8, đủ 44, không trùng, đúng thứ tự", pages == [12, 12, 12, 8] and seen == proj and len(set(seen)) == 44,
     pages)
L = lab(IUQ, d0)
m = L["list_meta"]["layers.L2.candidates"]
case("K2", "K2.1b trang đầu: total 44 · shown 12 · truncated · next_cursor có", m["total"] == 44 and m["shown"] == 12 and m["truncated"] and m["next_cursor"], m)
syn = copy.deepcopy(l2)
syn["tables"]["directus.public.information_unit"]["potential_collisions"] = [{"target": "t%d" % i, "writers": ["w%d" % i]} for i in range(20)]
syn["tables"]["directus.public.information_unit"]["unknown_dynamic"] = [{"fn": "f%d" % i} for i in range(15)]
syn.pop("self_sha256", None)
syn["self_sha256"] = hashlib.sha256(json.dumps(syn, sort_keys=True).encode()).hexdigest()
json.dump(syn, open(TMP + "/cert/l2-candidates.json", "w"))
for name, size, total in (("potential_collisions", 8, 20), ("unknown_dynamic", 6, 15)):
    got, cur, n = [], None, 0
    while n < 10:
        L = lab(IUQ, d0, params={"n4_page": cur} if cur else None)
        m = L["list_meta"]["layers.L2." + name]
        if cur is None:
            first = m
        got += [json.dumps(x, sort_keys=True) for x in L["layers"]["L2"][name]]
        cur, n = m["next_cursor"], n + 1
        if not cur:
            break
    case("K2", "K2.2 %s >%d: total %d, trang %d, đủ không trùng" % (name, size, total, size),
         first["total"] == total and first["shown"] == size and first["truncated"] and len(got) == total and len(set(got)) == total, (first, len(got)))
L = lab(IUQ, d0)
cur_iu = L["list_meta"]["layers.L2.candidates"]["next_cursor"]
AGQ = "MATCH (g:PgTrigger)-[:ON_TABLE]->(:PgTable {id: 'public.agents'}) RETURN g.id AS x"
L = lab(AGQ, d0, params={"n4_page": cur_iu})
case("K2", "K2.3a con trỏ của bảng khác ⇒ từ chối CURSOR_SCOPE_MISMATCH, trả trang đầu", L["layers"]["L2"]["paging"]["accepted"] is False and
     "SCOPE" in L["layers"]["L2"]["paging"]["denied"] and L["list_meta"]["layers.L2.candidates"]["offset"] == 0, L["layers"]["L2"]["paging"])
L = lab(IUQ, d0, params={"n4_page": cur_iu.rsplit(":", 1)[0] + ":" + "0" * 12})
case("K2", "K2.3b con trỏ của ảnh L2 cũ ⇒ CURSOR_STALE", "STALE" in str(L["layers"]["L2"]["paging"]["denied"]), L["layers"]["L2"]["paging"])
L = lab(IUQ, d0, params={"n4_page": "../../etc/passwd"})
case("K2", "K2.3c con trỏ hỏng ⇒ CURSOR_INVALID", L["layers"]["L2"]["paging"]["denied"] == "CURSOR_INVALID", L["layers"]["L2"]["paging"])
L = lab(IUQ, d0, params={"n4_page": cur_iu.replace(":12:", ":900:")})
case("K2", "K2.3d con trỏ quá cuối ⇒ CURSOR_OUT_OF_RANGE", "OUT_OF_RANGE" in str(L["layers"]["L2"]["paging"]["denied"]), L["layers"]["L2"]["paging"])
L = lab(TRQ, d0, params={"n4_page": cur_iu})
case("K2", "K2.3e con trỏ trên truy vấn không neo bảng mẫu ⇒ từ chối", L["layers"]["L2"].get("paging", {}).get("accepted") is False, L["layers"]["L2"].get("paging"))
shutil.copyfile(L2_P, TMP + "/cert/l2-candidates.json")
L = lab(IUQ, d0, now=iso("2026-10-24T00:00:00Z"))
f1 = L["layers"]["L2"]["freshness"]
L = lab(IUQ, d0, now=iso("2026-10-24T01:00:00Z"))
f2 = L["layers"]["L2"]["freshness"]
case("K2", "K2.4a L2 25,3h chưa cũ · 26,3h ⇒ STALE + lý do", f1["stale"] is False and f2["stale"] is True and "L2_STALE" in L["layers"]["L2"]["reason"], (f1["age_hours"], f2["age_hours"]))
L = lab(IUQ, d0)
case("K2", "K2.4b catalog (giấy L1) mới hơn ảnh L2 ⇒ catalog_newer_than_l2", L["layers"]["L2"]["freshness"]["catalog_newer_than_l2"] is True, L["layers"]["L2"]["freshness"])
case("K2", "K2.4c L2 luôn MỘT PHẦN kể cả khi L1 ĐỦ + mốc khớp", L["layers"]["L2"]["label"] == G.MP and L["layers"]["L1"]["label"] == G.DU, L["layers"]["L2"]["label"])
L = lab("MATCH (n:PgTable) RETURN count(n) AS c", d0)
L2_ = lab("MATCH (a)-[r]->(b) RETURN count(r) AS c", d0)
okm = all(v["total"] == len(L2_[k]) if k in L2_ and isinstance(L2_[k], list) else True for k, v in L2_["list_meta"].items())
case("K2", "K2.5 mọi danh sách có list_meta, tổng = độ dài; source_scope không còn cắt 12", okm and L2_["list_meta"]["source_scope"]["total"] == len(L2_["source_scope"])
     and len(L2_["source_scope"]) > 12 and not L2_["list_meta"]["missing_or_unknown_cell_ids"]["truncated"], len(L2_["source_scope"]))

# ============================================================== G1–G9
class FS:
    def __init__(self, cache):
        self.cache = copy.deepcopy(cache)

    def get(self, n):
        return self.cache.get(n) or {"_error": "không tiêm " + n}


TRG = ["public", "a", "t1", "public", "f", "", "O"]
BASE = {
    "pg": {"directus": {"reader": {"pg_snapshot": "1:1:", "snapshot_utc": "2026-10-23T00:00:00Z"}, "classes": {
        "table": {"ok": True, "rows": [["public.a"], ["public.b"]]}, "view": {"ok": True, "rows": [["public.v", "v"]]},
        "trigger": {"ok": True, "rows": [TRG]}, "function": {"ok": True, "rows": [["public.f()"]]}, "fk": {"ok": True, "rows": [["public.a", "a_fk", "public.b"]]},
        "view_dep": {"ok": True, "rows": [["public.v", "public.a"]]}, "function_src": {"ok": True, "rows": [["public.f()", "m1"]]}}},
        "postgres": {"reader": {}, "classes": {"databases": {"ok": True, "rows": [["directus"], ["postgres"]]},
                                              "cdc_caps": {"ok": True, "rows": [["wal_level", "replica"], ["replication_slots", "0"], ["logical_slots", "0"]]},
                                              "wal_lsn": {"ok": True, "rows": [["0/1"]]}}}},
    "docker": {"containers": [["c1", "sha256:aaaaaaaaaaaaaaaa"], ["c2", "sha256:bbbbbbbbbbbbbbbb"]], "edges": [["c1", "USES_IMAGE", "sha256:aaaaaaaaaaaaaaaa"]],
               "images": ["sha256:aaaaaaaaaaaaaaaa", "sha256:bbbbbbbbbbbbbbbb"], "ok": True, "names_before": ["c1", "c2"], "names_after": ["c1", "c2"]},
    "systemd": {"units": [["a.service"]], "edges": [["a.service", "EXECS", "/opt/x/a.sh", "ExecStart#0"]], "before": ["a.service"], "after": ["a.service"]},
    "systemd_inv": {"units": {"a.service": "h1", "b.timer": "h2"}, "dropins": {"a.service.d/x.conf": "d1"}, "stable": True},
    "cron": {"entries": [["/etc/cron.d/x|* * * * *|/opt/x/a.sh"]], "edges": [], "errors": []},
    "cron_files": {"files": {"/etc/cron.d/x": "f1", "/etc/crontab": "f2"}, "errors": []},
    "nginx": {"servers": [["a.com|443"]], "edges": [["a.com|443|loc1", "PROXIES", "http://x:1"]], "conf_sha256": "c1"},
    "listeners": {"listen": ["0.0.0.0:443"]},
    "opt": {"entries": [["/opt/incomex", "d"], ["/opt/x", "d"]], "ledger": [["/opt/x/a.sh", "LOCKED"]]},
    "code_files": {"files": {"/opt/x/a.sh": "s1"}, "not_hashable": 0, "size_capped": 0, "ledger_rows": 1},
    "qdrant": {"collections": {"production_documents": {"vectors": {"": [768, "Cosine"]}, "payload_index": []}}, "aliases": [], "counts": {"production_documents": 2}},
    "qdrant_ids": {"doc_ids": ["d1", "d2"], "scroll_complete": True, "count_before": 2, "count_after": 2, "points_without_document_id": 0},
    "lark_bases": {"bases": ["b1"]},
    "lark": {"b1": {"tables": ["t1"], "links": [["t1", "f1", "t1"]], "field_errors": [], "tables_after": ["t1"]}},
    "b88": {"objects": [["B88Order", "r1", "o1"]], "edges": [["r1", "SELECTED_FOR_ORDER", "r2"]], "freeze_sha256": "z"},
    "git": {"dirs": ["work/a"], "head": "h1"},
    "git_repos": {"repos": {"/opt/incomex/dot": "t1"}, "errors": []},
}
FCELLS = [{"key": "pg:directus:table", "gate": "G1", "parent": "pg:directus"}, {"key": "docker:container", "gate": "G2", "parent": "docker"},
          {"key": "systemd:unit", "gate": "G3", "parent": "systemd"}, {"key": "cron:entry", "gate": "G4", "parent": "cron"},
          {"key": "nginx:route", "gate": "G5", "parent": "nginx"}, {"key": "opt:entries", "gate": "G6", "parent": "opt"},
          {"key": "qdrant:production_documents:meta", "gate": "G7", "parent": "qdrant:production_documents"},
          {"key": "lark:b1:schema", "gate": "G8", "parent": "lark:b1"}, {"key": "git:workspace:work", "gate": "G9", "parent": "git"}]
dr0 = G.directory(FCELLS, FS(BASE), {})
ACC = sorted(x for xs in dr0["parents"].values() for x in xs)
BL = {"accepted_directory_parents": ACC, "ephemeral_parent_patterns": ["^docker:workspace-job-[0-9a-f]+$"], "certified_floor": [], "accepted_partial": {
    c["key"]: {"why": "fixture"} for c in FCELLS}}
dr0 = G.directory(FCELLS, FS(BASE), BL)
case("G", "G0 nền: 9 cửa đọc, 0 cha lạ, thư mục ĐỦ", dr0["status"] == G.DU and dr0["gates_compared"] == sorted(G.GATE_PREFIX), dr0["reasons"])
INV0 = G.inventory_now(FS(BASE), dr0)
PREV = {"families": INV0}
RESMIN = {c["key"]: dict(c, status=G.MP, reasons=["GRAPH_CLASS_NOT_LOADED"], reader_pass=True) for c in FCELLS}


def evalmut(mut, gate):
    src = copy.deepcopy(BASE)
    mut(src)
    dr = G.directory(FCELLS, FS(src), BL)
    inv = G.inventory_now(FS(src), dr)
    mx = G.coverage_matrix({}, RESMIN, dr, inv, PREV, NOW)
    doc = sign({"format": G.FORMAT, "generated_at": G.now_iso(NOW), "cells": RESMIN, "directory": dr, "coverage_matrix": mx, "summary": {}})
    st, msg, inc = G.alarm(doc, None, NOW, BL, {})
    return dr, inv, mx[gate], st, msg, inc


def chk(group, name, mut, gate, want_parent=None, want=None, want_status=None):
    dr, inv, m, st, msg, inc = evalmut(mut, gate)
    ch = m["change_since_last_good"] or {}
    ok = True
    if want_parent:
        ok &= want_parent in dr["new_source_unhandled"] and m["status"] == "PENDING_SOURCE_CELL" and dr["status"] == G.MP and \
              any(i["kind"] == "NEW_SOURCE_UNHANDLED" and i["page"] and i["severity"] == "warning" for i in inc) and st == "down"
    if want:
        for t, k, n in want:
            ok &= (ch.get({"+": "added", "-": "removed", "~": "modified"}[t]) or {}).get(k) == n
        ok &= any(i["kind"] == "SOURCE_CHANGE" and not i["page"] for i in inc)
    if want_status:
        ok &= m["status"] == want_status
    case(group, name, ok, {"status": m["status"], "chg": {k: ch.get(k) for k in ("added", "removed", "modified")}, "un": dr["new_source_unhandled"][:3], "st": st})


def add(path, val):
    def f(s):
        cur = s
        for p in path[:-1]:
            cur = cur[p]
        if isinstance(cur[path[-1]], list):
            cur[path[-1]].append(val)
        else:
            cur[path[-1]].update(val)
    return f


def seq(*fs):
    def f(s):
        for x in fs:
            x(s)
    return f


cls = ["pg", "directus", "classes"]
# G1
chk("G1", "G1a database mới ⇒ NEW_SOURCE_UNHANDLED + vàng", add(["pg", "postgres", "classes", "databases", "rows"], ["newdb"]), "G1", want_parent="pg:newdb")
chk("G1", "G1b cha cũ: trigger mới + thân hàm đổi + xoá FK ⇒ + ~ -", seq(add(cls + ["trigger", "rows"], ["public", "b", "t2", "public", "f", "", "O"]),
    lambda s: s["pg"]["directus"]["classes"]["function_src"].update(rows=[["public.f()", "m2"]]), lambda s: s["pg"]["directus"]["classes"]["fk"].update(rows=[])),
    "G1", want=[("+", "directus.trigger", 1), ("~", "directus.function_src", 1), ("-", "directus.fk", 1)])
chk("G1", "G1c cùng số bảng, đổi tên (a→c) ⇒ +1 −1", lambda s: s["pg"]["directus"]["classes"]["table"].update(rows=[["public.c"], ["public.b"]]), "G1",
    want=[("+", "directus.table", 1), ("-", "directus.table", 1)])
# G2
chk("G2", "G2a container mới ⇒ cha mới", seq(add(["docker", "containers"], ["c3", "sha256:cccccccccccccccc"]), add(["docker", "names_after"], "c3"), add(["docker", "names_before"], "c3")),
    "G2", want_parent="docker:c3")
chk("G2", "G2b mã mới dưới container cũ (đổi image ID, cùng tên) ⇒ SỬA", lambda s: s["docker"].update(containers=[["c1", "sha256:dddddddddddddddd"], ["c2", "sha256:bbbbbbbbbbbbbbbb"]]),
    "G2", want=[("~", "container", 1)])
chk("G2", "G2c cùng số image, đổi ID ⇒ +1 −1", lambda s: s["docker"].update(images=["sha256:aaaaaaaaaaaaaaaa", "sha256:eeeeeeeeeeeeeeee"]), "G2",
    want=[("+", "image", 1), ("-", "image", 1)])
# G3
chk("G3", "G3a unit .path mới (loại trước đây không thấy) ⇒ cha mới", add(["systemd_inv", "units"], {"c.path": "h3"}), "G3", want_parent="systemd:c.path")
chk("G3", "G3b sửa drop-in + nội dung unit cũ ⇒ SỬA", lambda s: s["systemd_inv"].update(units={"a.service": "h9", "b.timer": "h2"}, dropins={"a.service.d/x.conf": "d9"}),
    "G3", want=[("~", "unit", 1), ("~", "dropin", 1)])
# G4
chk("G4", "G4a tệp cron mới ⇒ cha mới", seq(add(["cron", "entries"], ["/etc/cron.d/y|@daily|/opt/x/b.sh"]), add(["cron_files", "files"], {"/etc/cron.d/y": "f3"})),
    "G4", want_parent="cron:/etc/cron.d/y")
chk("G4", "G4b dòng mới trong tệp cron cũ ⇒ + entry + ~ file", seq(add(["cron", "entries"], ["/etc/cron.d/x|0 1 * * *|/opt/x/c.sh"]),
    lambda s: s["cron_files"]["files"].update({"/etc/cron.d/x": "f9"})), "G4", want=[("+", "entry", 1), ("~", "file", 1)])
# G5
chk("G5", "G5a server nginx mới ⇒ cha mới", add(["nginx", "servers"], ["b.com|443"]), "G5", want_parent="nginx:b.com|443")
chk("G5", "G5b route mới trong server cũ ⇒ + route", add(["nginx", "edges"], ["a.com|443|loc2", "PROXIES", "http://y:2"]), "G5", want=[("+", "route", 1)])
chk("G5", "G5c cổng nghe mới ⇒ cha mới", add(["listeners", "listen"], "0.0.0.0:8080"), "G5", want_parent="nginx:listen:0.0.0.0:8080")
# G6
chk("G6", "G6a thư mục /opt mới ⇒ cha mới", add(["opt", "entries"], ["/opt/newapp", "d"]), "G6", want_parent="opt:/opt/newapp")
chk("G6", "G6b mã mới triển khai dưới thư mục cũ (đổi nội dung tệp trong sổ) ⇒ SỬA", lambda s: s["code_files"]["files"].update({"/opt/x/a.sh": "s2"}), "G6",
    want=[("~", "code_file", 1)])
# G7
chk("G7", "G7a collection mới ⇒ cha mới", seq(lambda s: s["qdrant"]["collections"].update({"newcol": {"vectors": {"": [1, "Dot"]}, "payload_index": []}})), "G7",
    want_parent="qdrant:newcol")
chk("G7", "G7b cùng số document_id, đổi chỗ ⇒ +1 −1 (mã băm riêng tư)", lambda s: s["qdrant_ids"].update(doc_ids=["d1", "d3"]), "G7",
    want=[("+", "document_id:production_documents", 1), ("-", "document_id:production_documents", 1)])
# G8
chk("G8", "G8a base mới trong bases.yaml ⇒ cha mới", add(["lark_bases", "bases"], "b2"), "G8", want_parent="lark:b2")
chk("G8", "G8b trường liên kết mới + bản ghi b88 đổi chỗ ⇒ + link · ±b88", seq(add(["lark", "b1", "links"], ["t1", "f2", "t1"]),
    lambda s: s["b88"].update(objects=[["B88Order", "r9", "o1"]])), "G8", want=[("+", "link_field", 1), ("+", "b88_record", 1), ("-", "b88_record", 1)])
# G9
chk("G9", "G9a thư mục work/ mới ⇒ cha mới (G9 không còn chỉ ghi sổ)", add(["git", "dirs"], "work/new-task"), "G9", want_parent="git:work/new-task")
chk("G9", "G9b kho git mới dưới /opt/incomex ⇒ cha mới", add(["git_repos", "repos"], {"/opt/incomex/newrepo": "t9"}), "G9", want_parent="git:repo:/opt/incomex/newrepo")
chk("G9", "G9c HEAD/tree kho cũ đổi ⇒ SỬA", lambda s: s["git_repos"]["repos"].update({"/opt/incomex/dot": "t2"}), "G9", want=[("~", "repo", 1)])
# bộ đọc hỏng / mất quyền · đổi giữa hai lần đọc · sinh-rồi-mất · không đổi
for g, key, val in (("G1", "pg", {"_error": "rc=1 connect"}), ("G2", "docker", {"error": "docker ps rc=1"}), ("G3", "systemd_inv", {"error": "PermissionError"}),
                    ("G4", "cron", {"entries": [], "edges": [], "errors": ["/var/spool/cron/crontabs/root"]}), ("G5", "nginx", {"error": "nginx -T rc=1"}),
                    ("G6", "code_files", {"error": "PermissionError"}), ("G7", "qdrant", {"error": "rc=1"}), ("G8", "lark_bases", {"error": "bases.yaml"}),
                    ("G9", "git", {"error": "git rc=128/0"})):
    dr, inv, m, st, msg, inc = evalmut(lambda s, k=key, v=val: s.update({k: v}), g)
    case(g, "%se bộ đọc hỏng/mất quyền ⇒ READER_FAILED + ĐỎ OPERATIONAL, không suy «xoá»" % g, m["status"] == "READER_FAILED" and st == "down" and
         any(i["kind"] == "OPERATIONAL" and i["severity"] == "critical" for i in inc) and not (m["change_since_last_good"] or {}).get("removed"), (m["status"], st, msg[:80]))
dr, inv, m, st, msg, inc = evalmut(lambda s: s["docker"].update(names_after=["c1", "c2", "c3"]), "G2")
case("G2", "G2f nguồn đổi giữa hai lần đọc ⇒ DRIFT, không ghi đè ảnh tốt", m["consistency"] == "DRIFT", m["consistency"])
G.write_inventory(PREV, inv, NOW)
kept = json.load(open(G.INVENTORY))["families"]["G2"] == INV0["G2"]
case("G2", "G2f' ảnh DRIFT không thay last-good", kept, kept)
dr, inv, m, st, msg, inc = evalmut(lambda s: None, "G2")
case("G", "G-eph sinh rồi mất giữa hai lượt chụp ⇒ 0 thay đổi + EPHEMERAL_CHANGE_NOT_OBSERVABLE (không báo «đã phát hiện»)",
     (m["change_since_last_good"] or {}).get("total_changes") == 0 and m["ephemeral_change_observable"] is False and "EPHEMERAL" in m["blind_spot"], m["blind_spot"][:60])
allok = True
for g in sorted(G.GATE_PREFIX):
    dr, inv, m, st, msg, inc = evalmut(lambda s: None, g)
    allok &= m["status"] == "PARTIAL_UNMODELED" and not (m["change_since_last_good"] or {}).get("total_changes") and st == "up"
case("G", "G-same 9/9 họ không đổi ⇒ giữ PARTIAL_UNMODELED, 0 sự cố mới, đèn UP", allok, allok)
dr, inv, m, st, msg, inc = evalmut(lambda s: s["docker"].update(containers=s["docker"]["containers"] + [["workspace-job-1a2b", "sha256:ffffffffffffffff"]],
                                                                 names_after=["c1", "c2", "workspace-job-1a2b"], names_before=["c1", "c2", "workspace-job-1a2b"]), "G2")
case("G2", "G2g container tạm workspace-job-* (mẫu ephemeral) ⇒ không thành cha lạ", "docker:workspace-job-1a2b" not in dr["new_source_unhandled"], dr["new_source_unhandled"])

# ============================================================== báo động (ĐỎ/VÀNG/ghi sổ, dập trùng, nhắc lại)
dr, inv, m, st, msg, inc = evalmut(add(["systemd_inv", "units"], {"c.path": "h3"}), "G3")
doc = sign({"format": G.FORMAT, "generated_at": G.now_iso(NOW), "cells": RESMIN, "directory": dr,
            "coverage_matrix": G.coverage_matrix({}, RESMIN, dr, inv, PREV, NOW), "summary": {"du": 0, "cells": 9}})
os.environ.pop("X", None)
st1, msg1, inc1 = G.alarm(doc, None, NOW, BL, {})
new1, _ = G.record_incidents(inc1, NOW)
open1 = json.load(open(G.ALARM_STATE))["open"]
st2, msg2, inc2 = G.alarm(doc, None, NOW + 86400, BL, open1)
st3, msg3, inc3 = G.alarm(doc, None, NOW + 169 * 3600, BL, open1)
case("A", "A1 vàng mới ⇒ DOWN đúng một lượt «VÀNG MỚI» (Telegram)", st1 == "down" and msg1.startswith("VÀNG MỚI") and any(i["kind"] == "NEW_SOURCE_UNHANDLED" for i in new1), msg1[:90])
case("A", "A2 lượt sau cùng sự cố (đã báo) ⇒ UP, danh sách vàng mở trong tin, không spam", st2 == "up" and "VÀNG mở" in msg2, msg2[:120])
case("A", "A3 quá 168h còn mở ⇒ nhắc lại (REPEAT_DUE)", st3 == "down" and any(i.get("page_reason") == "REPEAT_DUE" for i in inc3), msg3[:80])
doc_c = sign(dict(doc, directory=dict(dr, errors=["G2 docker"])))
st4, msg4, inc4 = G.alarm(doc_c, None, NOW + 86400, BL, open1)
st5, msg5, _ = G.alarm(doc_c, None, NOW + 2 * 86400, BL, {i["id"]: i for i in inc4})
case("A", "A4 ĐỎ (bộ đọc cửa hỏng) ⇒ DOWN mọi lượt, khác vàng", st4 == "down" and msg4.startswith("ĐỎ") and st5 == "down", (msg4[:60], msg5[:60]))
dr2, inv2, m2, _, _, _ = evalmut(seq(add(["systemd_inv", "units"], {"c.path": "h3"}), add(["opt", "entries"], ["/opt/newapp", "d"])), "G6")
doc6 = sign({"format": G.FORMAT, "generated_at": G.now_iso(NOW), "cells": RESMIN, "directory": dict(dr2, errors=["G2 docker"]),
             "coverage_matrix": G.coverage_matrix({}, RESMIN, dr2, inv2, PREV, NOW), "summary": {}})
prev_down = {i["id"]: dict(i, last_paged_at=G.now_iso(NOW)) for i in inc4}
st6, msg6, inc6 = G.alarm(doc6, None, NOW + 86400, BL, prev_down)
newid = [i for i in inc6 if i["id"] not in prev_down and i["kind"] == "NEW_SOURCE_UNHANDLED"]
case("A", "A5 đèn đã DOWN (ĐỎ) + vàng MỚI ⇒ sự cố mới có mã riêng, page ⇒ nhịp DOWN mang «MỚI <mã>» (biên nhận riêng)", st6 == "down" and newid and newid[0]["page"],
     [i["reason"] for i in newid])
dr10, inv10, m10, st10, msg10, inc10 = evalmut(seq(add(["listeners", "listen"], "127.0.0.1:17474"), add(["listeners", "listen"], "127.0.0.1:17687")), "G5")
ids10 = {i["id"] for i in inc10 if i["kind"] == "NEW_SOURCE_UNHANDLED"}
case("A", "A9 hai nguồn mới chỉ khác chữ số (cổng 17474/17687) ⇒ HAI mã sự cố riêng (không gộp, không dập trùng sai)", len(ids10) == 2, ids10)
docacc = sign({"format": G.FORMAT, "generated_at": G.now_iso(NOW), "cells": RESMIN, "directory": dr0, "coverage_matrix": {}, "summary": {}})
st7, msg7, inc7 = G.alarm(docacc, None, NOW, BL, {})
case("A", "A6 ô MỘT PHẦN đã nhận mốc (accepted_partial) ⇒ không sự cố, không spam", st7 == "up" and not inc7, (st7, len(inc7)))
blf = dict(BL, certified_floor=["pg:directus:table"], accepted_partial={})
st8, msg8, inc8 = G.alarm(docacc, None, NOW, blf, {})
case("A", "A7 ô sàn tụt ⇒ ĐỎ COVERAGE_REGRESSION", st8 == "down" and any(i["kind"] == "COVERAGE_REGRESSION" for i in inc8), msg8[:80])
dr9, inv9, m9, st9, msg9, inc9 = evalmut(lambda s: s["docker"].update(images=["sha256:aaaaaaaaaaaaaaaa", "sha256:eeeeeeeeeeeeeeee"]), "G2")
case("A", "A8 thay đổi con trong họ đã nhận MỘT PHẦN ⇒ ghi sổ SOURCE_CHANGE, không gọi trang, nêu trong tin UP", st9 == "up" and "Δnguồn" in msg9 and
     all(not i["page"] for i in inc9 if i["kind"] == "SOURCE_CHANGE"), msg9[:140])

ok = all(r["pass"] for r in RES)
rep = {"run": "GS-C1C-PRODUCTION-TRUST-GATE-20261023-09", "candidate_sha256": hashlib.sha256(open(CAND, "rb").read()).hexdigest(), "total": len(RES),
       "pass": sum(r["pass"] for r in RES), "fail": [r for r in RES if not r["pass"]], "by_group": {}, "cases": RES,
       "note": "fixture cô lập (thư mục tạm, nguồn tiêm, Graph giả) — KHÔNG phải lượt timer tự nhiên"}
for r in RES:
    g = rep["by_group"].setdefault(r["group"], [0, 0])
    g[0] += r["pass"]
    g[1] += 1
if OUT:
    json.dump(rep, open(OUT, "w"), ensure_ascii=False, indent=1)
print("FIXTURES %d/%d PASS · %s" % (rep["pass"], rep["total"], json.dumps(rep["by_group"])))
for r in rep["fail"]:
    print("  FAIL", r["group"], r["case"], r["detail"])
shutil.rmtree(TMP, ignore_errors=True)
sys.exit(0 if ok else 1)
