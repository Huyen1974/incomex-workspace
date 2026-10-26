#!/usr/bin/env python3
# GS-C1D2-SCOPED-AUTOCOVER-20261026-13 · LỖI GIẢ CÔ LẬP cho ứng viên C1-D2 (graph-refresh + graph_autocover + graph_cert):
#   R3 retire có chứng minh + nghịch đảo đúng byte (bộ thực thi Cypher giả cho đúng các câu graph_autocover sinh) · bộ đọc ô loại bản retire
#   · nhãn N4 MỘT PHẦN khi phạm vi có bản retire · R2 chuông theo lý do (vàng có chủ / đỏ nội bộ) · P255(a) cờ VPS-GHI phải chứng minh tươi
#   (kể cả đổi chủ giữa kiểm và ghi) · H1 W2/W3 · T6 áp lực ⇒ SKIP · R1 lượt NO_CHANGE vẫn cấp giấy đối soát đủ.
#   Không chạm Neo4j/PG/Directus/Qdrant/Lark production: trạng thái ở thư mục tạm, Graph giả; module production chỉ ĐỌC (graph_recovery,
#   r7_g1lib, graph-v1, cert-cells, giấy current.json để mượn khuôn). Fixture KHÔNG phải lượt timer tự nhiên.
# Dùng: python3 -I c1d2_fixtures.py <graph-refresh> <graph_cert.py> <graph_autocover.py> [--out F]
import copy, hashlib, importlib.machinery, importlib.util, json, os, re, shutil, subprocess, sys, tempfile, time, types

GRF_P, GC_P, GA_P = sys.argv[1:4]
OUT = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else None
PROD = "/opt/incomex/graph-server/prod-v1"
TMP = tempfile.mkdtemp(prefix="gs-c1d2-fx-", dir="/dev/shm")
os.makedirs(TMP + "/cert")
os.environ.update(GS_CERT_CELLS=PROD + "/manifest/cert-cells.json", GS_CERT_DIR=TMP + "/cert", GS_CERT_BASELINE=TMP + "/baseline.json")
json.dump({"certified_floor": [], "accepted_partial": {}, "yellow_repeat_hours": 168}, open(TMP + "/baseline.json", "w"))
RES = []


def load(path, name):
    ldr = importlib.machinery.SourceFileLoader(name, path)
    m = importlib.util.module_from_spec(importlib.util.spec_from_loader(name, ldr))
    ldr.exec_module(m)
    return m


def case(group, cid, name, ok, detail=""):
    RES.append({"group": group, "id": cid, "case": name, "pass": bool(ok), "detail": str(detail)[:400]})
    print("%-5s %-5s %-86s %s %s" % (group, cid, name[:86], "PASS" if ok else "FAIL", str(detail)[:150]), flush=True)


sys.path.insert(0, PROD + "/bin/refresh")
GC = load(GC_P, "graph_cert")
GA = load(GA_P, "graph_autocover")
sys.modules["graph_cert"], sys.modules["graph_autocover"] = GC, GA
RF = load(GRF_P, "graph_refresh_c1d2_fx")
assert RF.GC is GC and RF.GA is GA


# =========================================================================== bộ thực thi Cypher giả (đúng các câu graph_autocover sinh)
class MiniGraph:
    """nodes {gs_key: (labels, props)} · edges [(s, t, d, props)]. Mỗi http_cypher = một giao dịch (lỗi ⇒ lùi trọn)."""

    def __init__(self, nodes, edges):
        self.n = {k: (list(l), dict(p)) for k, (l, p) in nodes.items()}
        self.e = [(s, t, d, dict(p)) for s, t, d, p in edges]

    def state(self):
        return hashlib.sha256(json.dumps({"n": sorted([k, sorted(l), p] for k, (l, p) in self.n.items()),
                                          "e": sorted([s, t, d, p] for s, t, d, p in self.e)}, sort_keys=True).encode()).hexdigest()

    def rows(self, d):
        r = d["results"][0]
        return [dict(zip(r["columns"], x["row"])) for x in r["data"]]

    def _one(self, q, p, n, e):
        res = lambda cols, rows: {"columns": cols, "data": [{"row": r} for r in rows]}
        if q.startswith("MATCH (n:GS) WHERE n.gs_layer = $l"):
            return res(["k", "l", "p"], [[k, v[0], v[1]] for k, v in n.items() if v[1].get("gs_layer") == p["l"]])
        if q.startswith("MATCH (a:GS)-[x]->(b:GS) WHERE a.gs_layer = $l"):
            lay = lambda k: (n.get(k) or ([], {}))[1].get("gs_layer")
            return res(["s", "t", "d", "p"], [[s, t, d_, pp] for s, t, d_, pp in e if lay(s) == p["l"] or lay(d_) == p["l"]])
        if q.startswith("MATCH (n:GS) WHERE n.gs_key IN $k RETURN"):
            return res(["k", "l", "layer"], [[k, n[k][0], n[k][1].get("gs_layer")] for k in p["k"] if k in n])
        m = re.fullmatch(r"UNWIND \$rows AS p CREATE \(n:(.+)\) SET n = p", q)
        if m:
            labs = [x.strip("`") for x in m.group(1).split(":")]
            for r in p["rows"]:
                if r["gs_key"] in n:
                    raise ValueError("trùng khoá")
                n[r["gs_key"]] = (labs, dict(r))
            return res([], [])
        if q == "UNWIND $rows AS r MATCH (n:GS {gs_key: r.k}) SET n = r.p":
            for r in p["rows"]:
                n[r["k"]] = (n[r["k"]][0], dict(r["p"]))
            return res([], [])
        if q == "UNWIND $rows AS r MATCH (n:GS {gs_key: r.k}) SET n += r.ret":
            for r in p["rows"]:
                n[r["k"]][1].update(r["ret"])
            return res([], [])
        m = re.fullmatch(r"UNWIND \$rows AS r MATCH \(a:GS \{gs_key: r\.s\}\) MATCH \(b:GS \{gs_key: r\.d\}\) CREATE \(a\)-\[x:`(\w+)`\]->\(b\) SET x = r\.p", q)
        if m:
            for r in p["rows"]:
                if r["s"] in n and r["d"] in n:
                    e.append((r["s"], m.group(1), r["d"], dict(r["p"])))
            return res([], [])
        m = re.fullmatch(r"UNWIND \$rows AS r MATCH \(a:GS \{gs_key: r\.s\}\)-\[x:`(\w+)`\]->\(b:GS \{gs_key: r\.d\}\) SET x (\+?=) r\.(ret|p)", q)
        if m:
            for r in p["rows"]:
                hit = [i for i, x in enumerate(e) if (x[0], x[1], x[2]) == (r["s"], m.group(1), r["d"])]
                for i in hit:
                    s, t, d_, pp = e[i]
                    e[i] = (s, t, d_, dict(pp, **r["ret"]) if m.group(2) == "+=" else dict(r["p"]))
            return res([], [])
        m = re.fullmatch(r"MATCH \(a:GS \{gs_key: \$s\}\)-\[x:`(\w+)`\]->\(b:GS \{gs_key: \$d\}\) SET x = \$p", q)
        if m:
            for i, x in enumerate(e):
                if (x[0], x[1], x[2]) == (p["s"], m.group(1), p["d"]):
                    e[i] = (x[0], x[1], x[2], dict(p["p"]))
            return res([], [])
        if q == "MATCH (:GS)-[x]->(:GS) WHERE x.gs_edge_key IN $k DELETE x":
            e[:] = [x for x in e if x[3].get("gs_edge_key") not in set(p["k"])]
            return res([], [])
        if q == "MATCH (n:GS) WHERE n.gs_key IN $k DETACH DELETE n":
            ks = set(p["k"])
            e[:] = [x for x in e if x[0] not in ks and x[2] not in ks]
            for k in ks:
                n.pop(k, None)
            return res([], [])
        # bộ đọc ô graph_cert (graph_nodes/graph_edges) — đúng các câu đã sửa ở C1-D2
        act = lambda pp: (pp or {}).get("gs_status") != "retired"
        m = re.fullmatch(r"MATCH \(n:`(\w+)`\) WHERE (NOT \()?coalesce\(n\.gs_status, ''\) <> 'retired'\)? RETURN count\(n\) AS c", q)
        if m:
            want = not m.group(2)
            return res(["c"], [[sum(1 for l, pp in n.values() if m.group(1) in l and act(pp) == want)]])
        m = re.fullmatch(r"MATCH \(n:`(\w+)`\) WHERE n\.gs_key > \$after AND coalesce\(n\.gs_status, ''\) <> 'retired' RETURN .*LIMIT \$page", q)
        if m:
            got = sorted((k, v) for k, v in n.items() if m.group(1) in v[0] and act(v[1]) and k > p["after"])[:p["page"]]
            return res(["k", "id", "av", "gs"], [[k, v[1].get("id"), [v[1].get(a) for a in p["attrs"]], "GS" in v[0]] for k, v in got])
        ACT_E = r"coalesce\(r\.gs_status, ''\) <> 'retired' AND coalesce\(x\.gs_status, ''\) <> 'retired' AND coalesce\(y\.gs_status, ''\) <> 'retired'"
        live_e = lambda s, d_, pp: act(pp) and act(n[s][1]) and act(n[d_][1])
        m = re.fullmatch(r"MATCH \(x\)-\[r:`(\w+)`\]->\(y\) WHERE %s RETURN count\(r\) AS c" % ACT_E, q)
        if m:
            return res(["c"], [[sum(1 for s, t, d_, pp in e if t == m.group(1) and live_e(s, d_, pp))]])
        m = re.fullmatch(r"MATCH \(x:`(\w+)`\)-\[r:`(\w+)`\]->\(y:`(\w+)`\) WHERE (NOT \()?%s\)? RETURN count\(r\) AS c" % ACT_E, q)
        if m:
            a, t, b, neg = m.groups()
            return res(["c"], [[sum(1 for s, tt, d_, pp in e if tt == t and a in n[s][0] and b in n[d_][0] and live_e(s, d_, pp) == (not neg))]])
        m = re.fullmatch(r"MATCH \(x:`(\w+)`\)-\[r:`(\w+)`\]->\(y:`(\w+)`\) WHERE %s WITH .* LIMIT \$page" % ACT_E, q)
        if m:
            a, t, b = m.groups()
            got = sorted(("%s|%s|%d" % (s, d_, i), s, d_, pp) for i, (s, tt, d_, pp) in enumerate(e)
                         if tt == t and a in n[s][0] and b in n[d_][0] and live_e(s, d_, pp))
            got = [x for x in got if x[0] > p["after"]][:p["page"]]
            return res(["k", "s", "d", "prov"], [[k, n[s][1].get("id"), n[d_][1].get("id"), True] for k, s, d_, _ in got])
        raise AssertionError("MiniGraph câu lạ: " + q[:120])

    def http_cypher(self, stmts, pw, timeout=0):
        n, e = copy.deepcopy(self.n), copy.deepcopy(self.e)
        out = []
        for q, p in stmts:
            out.append(self._one(q, p or {}, n, e))
        self.n, self.e = n, e
        return {"results": out, "errors": []}


def N(k, label, layer="infra", **pp):
    return {"l": ["GS", label], "p": dict({"gs_key": k, "id": k.split(":", 2)[-1], "gs_layer": layer, "trust": "EXACT_AT_SNAPSHOT", "snapshot_utc": "t", "run": "r"}, **pp)}


def E(s, t, d_):
    return {"t": t, "s": s, "d": d_, "p": {"trust": "EXACT_AT_SNAPSHOT", "snapshot_utc": "t", "source": "x", "run": "r", "gs_edge_key": GA.sha16("%s|%s|%s" % (s, t, d_))}}


def graph_of(nodes, edges, **over):
    """MiniGraph từ tập mong muốn (dấu giờ cũ) + ghi đè thuộc tính."""
    gn = {k: (v["l"], dict(v["p"], snapshot_utc="old", run="old", **over.get(k, {}))) for k, v in nodes.items()}
    return MiniGraph(gn, [(e["s"], e["t"], e["d"], dict(e["p"], snapshot_utc="old")) for e in edges.values()])


NATIVE = lambda ctr_all=(), amb=(): {"retire_proof": {"containers_all": list(ctr_all), "readers": {}}, "ambiguous_listeners": list(amb)}
CAPS, USED = {"nodes": 600, "edges": 1200}, {"nodes": 0, "edges": 0}
L = "c1d:infra"
try:
    # ======================================================================= R3 — retire có chứng minh + nghịch đảo
    A, B, C = "net:listen:127.0.0.1:45551", "systemd:unit:hermes-gateway.service", "systemd:unit:other.service"
    A2 = "net:listen:127.0.0.1:57501"
    base_n = {A: N(A, "NetListener"), B: N(B, "SystemdUnit", kind="service"), C: N(C, "SystemdUnit", kind="service")}
    base_e = {(A, "BOUND_BY_PROCESS_OF", B): E(A, "BOUND_BY_PROCESS_OF", B)}
    # R3a — cổng 45551 biến mất, 57501 mới cùng chủ (ca sống 25/10: hermes-gateway đổi cổng ngẫu nhiên)
    g1 = graph_of(base_n, base_e)
    pre = g1.state()
    want_n = {A2: N(A2, "NetListener"), B: base_n[B], C: base_n[C]}
    want_e = {(A2, "BOUND_BY_PROCESS_OF", B): E(A2, "BOUND_BY_PROCESS_OF", B)}
    pl = GA.plan(g1, "", L, want_n, want_e, CAPS, USED, native=NATIVE())
    case("R3", "R3a", "cổng nghe mất ở `ss` (đọc trọn) ⇒ retire nút + cạnh chạm nó; cổng mới được tạo; 0 xoá, F không có DELETE",
         [x["k"] for x in pl["retire_nodes"]] == [A] and [x["key"] for x in pl["retire_edges"]] == [(A, "BOUND_BY_PROCESS_OF", B)]
         and pl["counts"]["nodes_add"] == 1 and pl["counts"]["nodes_delete"] == 0 and not any("DELETE" in q for q, _ in pl["F"]) and not pl["stale_nodes"],
         pl["counts"])
    g1.http_cypher(pl["F"], "")
    mid = g1.state()
    ret_ok = g1.n[A][1].get("gs_status") == "retired" and "SOURCE_ABSENT_FULL_READ" in g1.n[A][1].get("retired_reason", "") and A in g1.n \
        and any(x[:3] == (A, "BOUND_BY_PROCESS_OF", B) and x[3].get("gs_status") == "retired" for x in g1.e)
    g1.http_cypher(pl["I"], "")
    case("R3", "R3b", "F đánh dấu thuộc tính (nút còn nguyên, nhãn/loại cạnh không đổi) · I đưa Graph về ĐÚNG trạng thái PRE",
         ret_ok and mid != pre and g1.state() == pre, (ret_ok, mid[:8], g1.state()[:8], pre[:8]))
    # R3c — A→B thành A→C (cùng cổng, đổi chủ; B vẫn còn trong Graph và không còn chủ cổng)
    g2 = graph_of(base_n, base_e)
    pl = GA.plan(g2, "", L, {A: base_n[A], C: base_n[C]}, {(A, "BOUND_BY_PROCESS_OF", C): E(A, "BOUND_BY_PROCESS_OF", C)}, CAPS, USED, native=NATIVE())
    case("R3", "R3c", "cùng số lượng, đổi đích A→B thành A→C ⇒ tạo A→C + retire A→B (đầu chủ thể A đọc trọn); unit B không retire (giữ stale)",
         [x["key"] for x in pl["retire_edges"]] == [(A, "BOUND_BY_PROCESS_OF", B)] and pl["counts"]["edges_add"] == 1 and not pl["retire_nodes"]
         and pl["stale_nodes"] == [B], (pl["counts"], pl["stale_nodes"]))
    # R3d — cổng mơ hồ (không xác định được chủ trong lượt) ⇒ KHÔNG retire cạnh
    pl = GA.plan(graph_of(base_n, base_e), "", L, {A: base_n[A], B: base_n[B]}, {}, CAPS, USED, native=NATIVE(amb=["127.0.0.1:45551"]))
    case("R3", "R3d", "cổng mơ hồ (AMBIGUOUS) ⇒ cạnh vắng KHÔNG retire, giữ stale (ô MỘT PHẦN)",
         not pl["retire_edges"] and pl["stale_edges"] == ["|".join((A, "BOUND_BY_PROCESS_OF", B))], (pl["retire_edges"], pl["stale_edges"]))
    # R3e — nguồn từ chối / bộ đọc không chứng minh (không có retire_proof) ⇒ 0 retire
    pl = GA.plan(graph_of(base_n, base_e), "", L, {B: base_n[B], C: base_n[C]}, {}, CAPS, USED, native={"ambiguous_listeners": []})
    pl2 = GA.plan(graph_of(base_n, base_e), "", L, {B: base_n[B], C: base_n[C]}, {}, CAPS, USED, native=None)
    case("R3", "R3e", "báo cáo bộ đọc thiếu chứng minh vắng mặt / không có ⇒ 0 retire, đối tượng giữ stale",
         not pl["retire_nodes"] and not pl2["retire_nodes"] and pl["stale_nodes"] == [A] and pl["retire_hold_why"], (pl["counts"], pl["retire_hold_why"]))
    case("R3", "R3e2", "bộ đọc gốc hỏng ⇒ decide BLOCKED (không ghi, không retire, đèn đỏ)",
         RF.decide({"b88": {"csv_sha256": {}}, "pgdot": {"expected_sha256": "e", "q_dot_identical": True}, "code": {}, "c1d": {L: {"error": "ss rc=1"}}},
                   {"b88": {"csv_sha256": {}}, "pgdot": {"expected_sha256": "e"}, "code": {"repos": {}}})[L]["decision"] == "BLOCKED", "")
    # R3f — container: vắng docker ps -a ⇒ retire; còn trong docker ps -a nhưng bị lọc mẫu tạm ⇒ KHÔNG retire
    K1, K2, LP = "docker:container:gone", "docker:container:gs-tmp-x", "net:listen:0.0.0.0:8080"
    cn = {K1: N(K1, "DockerContainer"), K2: N(K2, "DockerContainer"), LP: N(LP, "NetListener")}
    ce = {(LP, "PUBLISHED_BY", K1): E(LP, "PUBLISHED_BY", K1)}
    pl = GA.plan(graph_of(cn, ce), "", L, {LP: cn[LP]}, {}, CAPS, USED, native=NATIVE(ctr_all=["gs-tmp-x", "incomex-nuxt"]))
    case("R3", "R3f", "container vắng `docker ps -a` ⇒ retire (+ cạnh PUBLISHED_BY chạm nó) · container còn sống nhưng bị lọc mẫu tạm ⇒ KHÔNG retire",
         [x["k"] for x in pl["retire_nodes"]] == [K1] and [x["key"] for x in pl["retire_edges"]] == [(LP, "PUBLISHED_BY", K1)] and pl["stale_nodes"] == [K2],
         (pl["counts"], pl["stale_nodes"]))
    # R3g — trộn sống/retire: bản retire quay lại nguồn ⇒ hồi sinh (SET bỏ gs_status) · bản retire vẫn vắng ⇒ không làm gì
    rp = {"gs_status": "retired", "retired_at": "2026-10-01T00:00:00Z", "retired_reason": "SOURCE_ABSENT_FULL_READ ss -ltne", "retired_by": "x"}
    g3 = graph_of(base_n, base_e, **{A: rp})
    g3.e = [(s, t, d_, dict(pp, **rp)) for s, t, d_, pp in g3.e]
    pl = GA.plan(g3, "", L, base_n, base_e, CAPS, USED, native=NATIVE())
    g3.http_cypher(pl["F"], "")
    revived = "gs_status" not in g3.n[A][1] and all("gs_status" not in x[3] for x in g3.e)
    pl_b = GA.plan(graph_of(base_n, base_e, **{A: rp}), "", L, {B: base_n[B], C: base_n[C]}, {}, CAPS, USED, native=NATIVE())
    case("R3", "R3g", "bản retire có lại ở nguồn ⇒ hồi sinh (nút + cạnh hết gs_status) · bản retire vẫn vắng ⇒ 0 thao tác, đếm already_retired",
         revived and pl["counts"]["nodes_set"] == 1 and pl["counts"]["edges_set"] == 1 and not pl_b["retire_nodes"]
         and pl_b["counts"]["already_retired_nodes"] == 1, (pl["counts"], pl_b["counts"]))
    # R3h — lane pgl1 / SystemdUnit: vắng nguồn không chứng minh mất ⇒ không retire
    pn = {"pg:table:a": N("pg:table:a", "PgTable", layer="pgl1")}
    pl = GA.plan(graph_of(pn, {}), "", "c1d:pgl1", {}, {}, CAPS, USED, native=NATIVE())
    pl_u = GA.plan(graph_of(base_n, {}), "", L, {A: base_n[A]}, {}, CAPS, USED, native=NATIVE())
    case("R3", "R3h", "lane pgl1 và SystemdUnit: vắng ở nguồn KHÔNG phải chứng minh mất ⇒ giữ stale, 0 retire",
         not pl["retire_nodes"] and pl["stale_nodes"] == ["pg:table:a"] and not pl_u["retire_nodes"] and sorted(pl_u["stale_nodes"]) == sorted([B, C]),
         (pl["counts"], pl_u["counts"]))
    # R3i — vân tay danh tính có retire (kiểm «nguồn đổi giữa lượt»)
    p_a = GA.plan(graph_of(base_n, base_e), "", L, want_n, want_e, CAPS, USED, native=NATIVE())
    p_b = GA.plan(graph_of(base_n, base_e), "", L, dict(want_n, **{A: base_n[A]}), want_e, CAPS, USED, native=NATIVE())
    case("R3", "R3i", "vân tay danh tính đổi khi tập retire đổi (nguồn đổi giữa lượt ⇒ dừng trước ghi)", p_a["ident_sha256"] != p_b["ident_sha256"]
         and not p_a["empty"], (p_a["ident_sha256"][:8], p_b["ident_sha256"][:8]))

    # ======================================================================= bộ đọc ô graph_cert loại bản retire
    gR = graph_of({A: base_n[A], A2: N(A2, "NetListener"), B: base_n[B]}, {(A, "BOUND_BY_PROCESS_OF", B): E(A, "BOUND_BY_PROCESS_OF", B),
                                                                            (A2, "BOUND_BY_PROCESS_OF", B): E(A2, "BOUND_BY_PROCESS_OF", B)}, **{A: rp})
    rn = GC.graph_nodes(gR, "", "NetListener", [], "net:listen:")
    re_ = GC.graph_edges(gR, "", "BOUND_BY_PROCESS_OF", "NetListener", "SystemdUnit", ["source"])
    case("CERT", "C1", "graph_nodes: chỉ đối tượng hiện hành vào phần băm; bản retire đếm riêng (retired_excluded)",
         [r[1] for r in rn["rows"]] == ["127.0.0.1:57501"] and rn["total"] == 1 and rn["retired_excluded"] == 1 and rn["complete"], rn)
    case("CERT", "C2", "graph_edges: cạnh chạm nút retire không còn hiện hành (loại khỏi phần băm, đếm retired_excluded)",
         [r[0] for r in re_["rows"]] == ["127.0.0.1:57501"] and re_["retired_excluded"] == 1 and re_["other_endpoints"] == 0 and re_["complete"], re_)
    gZ = graph_of({A2: N(A2, "NetListener"), B: base_n[B]}, {(A2, "BOUND_BY_PROCESS_OF", B): E(A2, "BOUND_BY_PROCESS_OF", B)})
    rz = GC.graph_nodes(gZ, "", "NetListener", [], "net:listen:")
    case("CERT", "C3", "không có bản retire ⇒ bộ đọc mới trả đúng như cũ (retired_excluded 0)", rz["total"] == 1 and rz["retired_excluded"] == 0, rz)

    # ======================================================================= nhãn N4: MỘT PHẦN khi phạm vi có bản retire
    doc = json.load(open(PROD + "/state/refresh/cert/current.json"))
    cat = GC.catalog_read()[1]
    lm = cat.get("graph_label_map") or {}
    du_cells = {k for k, c in doc["cells"].items() if c.get("status") == GC.DU}
    lab_pick = next((l for l in sorted(lm) if lm[l] and set(lm[l]) <= du_cells), None)
    if lab_pick is None:
        case("N4", "N1", "có nhãn danh mục mà mọi ô cần đang ĐỦ trong giấy sống để thử", False, "không tìm thấy")
    else:
        d0 = copy.deepcopy(doc)
        d0["engine_sha256"] = GC._SELF_SHA
        d0["engine_version"] = GC.ENGINE_VERSION
        now0 = GC.parse_iso(d0["generated_at"]) + 60
        for k in d0["cells"]:
            d0["cells"][k]["retired_in_scope"] = 0
        d0["self_sha256"] = GC.self_sha(d0)
        ep = d0.get("graph_epoch")
        live = lambda: ep                          # K1: Graph sống = mốc trong giấy (giả); khoá graph-refresh nhả (False)
        q = "MATCH (x:%s) RETURN count(x)" % lab_pick
        l0 = GC._label_impl("read-cypher", {"query": q}, result_rows=1, now=now0, doc=d0, live=live, lock_state=False)
        d1 = copy.deepcopy(d0)
        d1["cells"][lm[lab_pick][0]]["retired_in_scope"] = 2
        d1["self_sha256"] = GC.self_sha(d1)
        l1 = GC._label_impl("read-cypher", {"query": q}, result_rows=1, now=now0, doc=d1, live=live, lock_state=False)
        case("N4", "N1", "truy vấn ô %s: không có bản retire ⇒ ĐỦ (đối chứng, cùng giấy)" % lab_pick, l0["completeness_label"] == GC.DU,
             (l0["completeness_label"], l0.get("reason")))
        case("N4", "N2", "cùng truy vấn, ô có bản retire trong phạm vi ⇒ MỘT PHẦN RETIRED_IN_SCOPE, không hành động được",
             l1["completeness_label"] == GC.MP and str(l1.get("reason", "")).startswith("RETIRED_IN_SCOPE") and l1["query_actionability"] != l0["query_actionability"]
             and l1["retired_in_scope_cell_ids"] == [lm[lab_pick][0]], (l1["completeness_label"], str(l1.get("reason"))[:90]))

    # ======================================================================= A — thư mục G1–G9: cha mới nhận theo tiền tố của ô đã đối chiếu
    CAND_CELLS = os.path.join(os.path.dirname(os.path.abspath(GC_P)), "cert-cells.json")
    par = copy.deepcopy((doc.get("directory") or {}).get("parents") or {})
    par["G2"] = sorted(set(par.get("G2") or []) | {"docker:incomex-graph-v1-rc-fx"})          # bản Neo4j tạm (ô tự loại trừ) ⇒ không được nhận
    par["G9"] = sorted(set(par.get("G9") or []) | {"git:work/viec-moi-fx"})

    class FS:
        def get(self, k):
            G = lambda g: par.get(g) or []
            return {"pg": {"postgres": {"classes": {"databases": {"ok": True, "rows": [[x[3:]] for x in G("G1")]}}}},
                    "docker": {"names_after": [x[7:] for x in G("G2")]}, "systemd": {"after": [x[8:] for x in G("G3")]},
                    "systemd_inv": {"units": [x[8:] for x in G("G3")]}, "cron": {"entries": [[x[5:]] for x in G("G4")]},
                    "nginx": {"servers": [[x[6:]] for x in G("G5") if not x.startswith("nginx:listen:")]},
                    "listeners": {"listen": [x[13:] for x in G("G5") if x.startswith("nginx:listen:")]},
                    "opt": {"entries": [[x[4:], "d"] for x in G("G6")]}, "qdrant": {"collections": {x[7:]: {} for x in G("G7")}},
                    "lark_bases": {"bases": [x[5:] for x in G("G8")]},
                    "git": {"dirs": [x[4:] for x in G("G9") if not x.startswith("git:repo:")]},
                    "git_repos": {"repos": {x[9:]: {} for x in G("G9") if x.startswith("git:repo:")}}}[k]
    base_live = json.load(open(PROD + "/manifest/cert-baseline.json"))
    d_old = GC.directory(json.load(open(PROD + "/manifest/cert-cells.json"))["cells"], FS(), base_live)
    d_new = GC.directory(json.load(open(CAND_CELLS))["cells"], FS(), base_live) if os.path.exists(CAND_CELLS) else {"new_source_unhandled": ["THIẾU cert-cells ứng viên"]}
    gone = sorted(set(d_old["new_source_unhandled"]) - set(d_new["new_source_unhandled"]))
    case("A", "A1", "G2: container mới (2 runner ghm-ci-*) được ô infra:container (đối chiếu nguồn↔Graph mọi container) nhận theo tiền tố docker:",
         {"docker:ghm-ci-agent-data-test", "docker:ghm-ci-web-test"} <= set(gone), gone)
    case("A", "A2", "G9: work/* là MỘT loại nguồn — thư mục việc mới (kể cả việc giả mới) do ô git:workspace:work nhận, ô đó vẫn MỘT PHẦN (ACK GAP-C0-13)",
         {"git:work/github-management", "git:work/nhap-directus-for-workflow", "git:work/viec-moi-fx"} <= set(gone)
         and "git:workspace:work" in (base_live.get("accepted_partial") or {}), gone)
    case("A", "A3", "bản Neo4j tạm (mẫu loại trừ của chính ô) + unit HJW chờ chủ + /opt/incomex/ci-runner VẪN chưa được nhận (không nhận rộng)",
         {"docker:incomex-graph-v1-rc-fx", "systemd:incomex-hjwcap.path", "systemd:incomex-hjwcap.service", "opt:/opt/incomex/ci-runner"}
         <= set(d_new["new_source_unhandled"]), d_new["new_source_unhandled"])

    # ======================================================================= R2 — chuông theo lý do
    owned = [{"cell": "code:claude-mcp", "owner": "PROOT12 · MCPW", "reason": "RUNTIME_NE_HEAD claude-mcp 1 tệp (app/server.py) · lane không ghi"}]
    st1, msg1, inc1 = GC.alarm(None, None, now=time.time(), baseline={"accepted_partial": {}}, prev_open={}, owned=owned)
    po = {i["id"]: dict(i, first_seen=GC.now_iso(time.time()), last_paged_at=GC.now_iso(time.time())) for i in inc1}
    st2, msg2, inc2 = GC.alarm(None, None, now=time.time() + 3600, baseline={"accepted_partial": {}}, prev_open=po, owned=owned)
    st3, msg3, inc3 = GC.alarm(None, None, now=time.time() + 169 * 3600, baseline={"accepted_partial": {}}, prev_open=po, owned=owned)
    case("R2", "A1", "nguồn ngoài BLOCKED có chủ ⇒ VÀNG (warning) gọi trang MỘT lần, không đỏ", st1 == "down" and msg1.startswith("VÀNG MỚI")
         and inc1[0]["kind"] == "SOURCE_BLOCKED_OWNED" and inc1[0]["severity"] == "warning" and inc1[0]["owner"] == "PROOT12 · MCPW", (st1, msg1[:80]))
    case("R2", "A2", "lượt sau cùng lý do ⇒ không gọi trang lại (UP kèm danh sách vàng) · quá 168h ⇒ nhắc lại", st2 == "up" and not inc2[0]["page"]
         and "VÀNG mở 1" in msg2 and st3 == "down" and inc3[0]["page_reason"] == "REPEAT_DUE", (st2, msg2[:80], st3))
    st4, msg4, inc4 = GC.alarm(None, "máy cấp giấy lỗi RuntimeError", now=time.time(), baseline={"accepted_partial": {}}, prev_open=po, owned=owned)
    case("R2", "A3", "lỗi NỘI BỘ Graph cùng lúc ⇒ vẫn ĐỎ critical (vàng không che đỏ)", st4 == "down" and msg4.startswith("ĐỎ OPERATIONAL"), msg4[:80])
    red, own = RF.code_blocked_split({"code": {"repos": {"claude-mcp": {"decision": "BLOCKED", "why": "bản chạy ≠ nguồn cho vào", "runtime": {"diff_vs_head": ["app/server.py"]}},
                                                         "claude-kb": {"decision": "BLOCKED", "why": "RuntimeError đọc byte container", "runtime": None},
                                                         "nuxt-web": {"decision": "SKIP_NEEDS_IDENTITY"}, "lark-client": {"decision": "NO_CHANGE"}}}})
    case("R2", "A4", "tách: claude-mcp (chủ khai báo, đọc trọn) ⇒ vàng · claude-kb lỗi chụp + nuxt cần danh tính ⇒ đỏ", [i["cell"] for i in own] == ["code:claude-mcp"]
         and red == ["claude-kb BLOCKED", "nuxt-web SKIP_NEEDS_IDENTITY"], (red, own))
    doc_f = copy.deepcopy(doc)
    doc_f["self_sha256"] = GC.self_sha(doc_f)
    base_floor = {"certified_floor": sorted(du_cells)[:1], "accepted_partial": {}}
    dff = copy.deepcopy(doc_f)
    dff["engine_sha256"] = GC._SELF_SHA
    dff["cells"][sorted(du_cells)[0]]["status"] = GC.MP
    dff["self_sha256"] = GC.self_sha(dff)
    st5, msg5, _ = GC.alarm(dff, None, now=GC.parse_iso(doc["generated_at"]) + 60, baseline=base_floor, prev_open={}, owned=owned)
    case("R2", "A5", "ngoài sàn (ô sàn tụt) ⇒ ĐỎ COVERAGE_REGRESSION dù nguồn ngoài chỉ vàng", st5 == "down" and "COVERAGE_REGRESSION" in msg5, msg5[:90])

    # ======================================================================= P255(a) — cờ VPS-GHI chứng minh tươi
    GWD = TMP + "/gw"
    os.makedirs(GWD)
    subprocess.run(["git", "init", "-q", "-b", "main", GWD], check=True)
    open(GWD + "/COLLAB.md", "w").write("# x\n- **VPS-GHI: trống** · fx\n")
    subprocess.run(["git", "-C", GWD, "-c", "user.email=fx@x", "-c", "user.name=fx", "add", "COLLAB.md"], check=True)
    subprocess.run(["git", "-C", GWD, "-c", "user.email=fx@x", "-c", "user.name=fx", "commit", "-q", "-m", "fx"], check=True)
    open(GWD + "/.git/FETCH_HEAD", "w").write("x\n")
    head = subprocess.run(["git", "-C", GWD, "rev-parse", "HEAD"], capture_output=True).stdout.decode().strip()
    RF.GW_CLONE, RF.GW_SYNC = GWD, TMP + "/gw.sync"
    open(RF.GW_SYNC, "w").write("1")
    real_lr = RF.ls_remote_head

    def flag_with(remote, sync_age, line=None):
        RF.ls_remote_head = lambda timeout=20: remote
        t = time.time() - sync_age if sync_age is not None else None
        if t is not None:
            os.utime(RF.GW_SYNC, (t, t))
        if line:
            open(GWD + "/COLLAB.md", "w").write("# x\n%s\n" % line)
        return RF.vps_ghi_state()
    f1 = flag_with(head, 10000)
    f2 = flag_with("f" * 40, 5)
    f3 = flag_with(None, 299)
    f4 = flag_with(None, 301)
    f5 = flag_with(head, 1, line="- **VPS-GHI: GIỮ — RUN-KHAC** · x")
    case("FLAG", "F1", "clone = HEAD remote đọc ngay ⇒ tươi (dù FETCH_HEAD/mốc gateway cũ hàng giờ)", f1["ok"] and f1["fresh"] == "REMOTE_HEAD_EQ_CLONE", f1)
    case("FLAG", "F2", "remote đã tiến (clone tụt) ⇒ KHÔNG tươi dù gateway vừa đối chiếu 5s ⇒ chặn ghi", not f2["ok"] and f2["fresh"] == "CLONE_BEHIND_REMOTE", f2)
    case("FLAG", "F3", "ls-remote lỗi + gateway đối chiếu 299s ⇒ tươi (ca PASS ≤300s)", f3["ok"] and f3["fresh"].startswith("GATEWAY_SYNC"), f3)
    case("FLAG", "F4", "ls-remote lỗi + gateway đối chiếu 301s ⇒ KHÔNG tươi (ca âm 301s chặn ghi)", not f4["ok"] and f4["fresh"].startswith("LS_REMOTE_FAIL"), f4)
    case("FLAG", "F5", "cờ do RUN khác giữ (tươi) ⇒ KHÔNG ok", not f5["ok"] and f5["why"] == "VPS-GHI đang giữ", f5)
    lr = real_lr(timeout=20)
    case("FLAG", "F6", "ls-remote ẩn danh thật tới repo workspace trả HEAD 40 hex (chỉ đọc, không khoá)", bool(lr and re.fullmatch(r"[0-9a-f]{40}", lr)), (lr or "")[:12])
    RF.ls_remote_head = real_lr

    # ======================================================================= cmd_run có hàm ghi giả: đổi chủ giữa kiểm và ghi · T6 · H1 · R1
    T2 = TMP + "/run"
    os.makedirs(T2 + "/state/runs")
    for nm in ("graph-invariants.json", "pins.json", "refresh-sources.json", "recovery-manifest.json"):
        shutil.copyfile(PROD + "/manifest/" + nm, T2 + "/" + nm)
    RF.INV, RF.PINS, RF.SOURCES, RF.RECMAN = (T2 + "/" + x for x in ("graph-invariants.json", "pins.json", "refresh-sources.json", "recovery-manifest.json"))
    RF.STATE, RF.LOG, RF.PGL1_CROSS, RF.STOPF = T2 + "/state", T2 + "/log.jsonl", T2 + "/cross.json", T2 + "/state/STOP"
    INV0 = json.load(open(RF.INV))
    st0 = json.load(open(RF.RECMAN))["current"]["state"]
    calls = []

    class FakeGr:
        def password(self):
            return ""

        def invariants(self, pw):
            return dict(INV0)

        def inv_equal(self, a, b):
            keys = ("labels", "rels", "nodes", "gs_nodes", "gs_keys_count", "gs_keys_sha256", "edges_count", "edges_sha256", "gs_keys_distinct")
            return [k for k in keys if a.get(k) != b.get(k)]
    real_load = RF.r7_g1lib.load
    RF.r7_g1lib.load = lambda path=None: FakeGr()
    RF.take_lock = lambda trig: open(os.devnull, "w")
    RF.term_to_fail = lambda: None
    srcs0 = json.load(open(RF.SOURCES))
    RF.cap_b88 = lambda w: {"csv_sha256": srcs0["b88"]["csv_sha256"], "snapshot_utc": "x", "input_dir": w}
    RF.cap_pgdot = lambda w: {"expected_sha256": srcs0["pgdot"]["expected_sha256"], "q_dot_identical": True, "snapshot_utc": {}, "input_dir": w}
    RF.cap_code = lambda w, s_: {}
    fpl = {"empty": False, "problems": [], "counts": {"nodes_add": 1, "edges_add": 0, "nodes_set": 0, "edges_set": 0, "nodes_retire": 1, "edges_retire": 1,
                                                    "stale_nodes": 0, "stale_edges": 0}, "cap_bound_partial": False, "sha256": "s", "ident_sha256": "i", "F": [], "I": []}
    RF.cap_c1d = lambda g, pw, s_, c_, lanes=RF.C1D_LANES: {l: dict(fpl, empty=(l != L)) for l in lanes}
    GST = {"h": st0}                         # trạng thái Graph giả: apply_plan ⇒ NEW, undo ⇒ PRE
    RF.full_hash = lambda g, pw: GST["h"]
    RF.build_c1d_lane = lambda lane, pl, work, report, expect=None: {"lane": lane, "F": [], "I": [], "pre_hash": st0, "new_hash": st0, "new_inv": {},
                                                                     "stage_new": None, "stage_old": None, "plan_sha256": "s", "counts": pl["counts"]}
    RF.other_writers = lambda: []
    RF.apply_plan = lambda target, plan, report: calls.append("apply_plan") or GST.update(h="NEW") or True
    RF.undo = lambda target, plan, report: calls.append("undo") or GST.update(h=st0) or report.update(undo_eq_pre=True) or True

    def fake_v0(target, live, cand_obj, mid, raw_bytes=None):
        calls.append("apply_v0:" + target)
        if raw_bytes is not None:
            open(live, "wb").write(raw_bytes)
        else:
            json.dump(cand_obj, open(live, "w"), indent=1, sort_keys=True, ensure_ascii=False)
        return True, "RESULT=APPLIED"
    RF.apply_v0 = fake_v0
    RF.new_recovery_point = lambda g, pw, label, drive, report: calls.append("recovery_point") or ({"name": "fx", "state": st0, "meta_sha256": "m"}, T2 + "/stg")
    RF.commit_recovery_point = lambda stg, rp: calls.append("commit") or None
    RF.recovery_ok = lambda g=None: {"ok": True}
    ticks = []
    RF.cert_tick = lambda rec, *a, **k: ticks.append(dict(k, op_failure=k.get("op_failure"))) or {}
    RF.l2_tick = lambda rec: None
    RF.preconditions = lambda g, pw, need_vps=True: ({}, [])
    snap = lambda: {p: open(p, "rb").read() for p in (RF.INV, RF.PINS, RF.SOURCES, RF.RECMAN)}
    reset_files = lambda s: [open(p, "wb").write(b) for p, b in s.items()]
    S0 = snap()

    def run_with(flags):
        it = iter(flags)
        RF.vps_ghi_state = lambda: next(it, {"ok": False, "why": "hết"})
        calls.clear(); ticks.clear()
        GST["h"] = st0
        reset_files(S0)
        rc = RF.cmd_run(types.SimpleNamespace(execute=True, trigger="timer", only=L))
        return rc, json.load(open(RF.STATE + "/last.json"))
    ok_f = {"ok": True, "fresh": "REMOTE_HEAD_EQ_CLONE"}
    rc, last = run_with([{"ok": False, "why": "cờ VPS-GHI không chứng minh tươi: CLONE_BEHIND_REMOTE"}])
    case("FLAG", "F7", "cmd_run: cờ không tươi ngay trước ghi ⇒ DELTA_SKIPPED_SAFE, 0 apply_plan, 0 apply-v0, sổ byte PRE",
         last["result"] == "DELTA_SKIPPED_SAFE" and "apply_plan" not in calls and not any(c.startswith("apply_v0") for c in calls) and snap() == S0,
         (last["result"], calls))
    rc, last = run_with([ok_f, {"ok": False, "why": "VPS-GHI đang giữ"}])
    case("FLAG", "F8", "cmd_run: ĐỔI CHỦ giữa kiểm và ghi (sau giao dịch Graph) ⇒ FAIL + I (lùi Graph), 0 apply-v0 sổ, sổ byte PRE, đèn đỏ",
         last["result"] == "FAIL" and "undo" in calls and not any(c.startswith("apply_v0") for c in calls) and snap() == S0
         and "cờ VPS-GHI" in (last.get("why") or "") and ticks and ticks[-1]["op_failure"], (last["result"], last.get("why"), calls))
    rc, last = run_with([ok_f, ok_f])
    case("FLAG", "F9", "cmd_run: cờ tươi cả hai lần kiểm ⇒ DELTA_APPLIED; sổ c1d cộng dồn retired_nodes/edges; t6 có pha + tổng",
         last["result"] == "DELTA_APPLIED" and "commit" in calls and json.load(open(RF.SOURCES))["c1d"][L]["retired_nodes"] ==
         (srcs0.get("c1d", {}).get(L, {}).get("retired_nodes", 0) + 1) and len(last["t6"]["phases"]) >= 5 and "cpu_s" in last["t6"]["total"],
         (last["result"], [p["phase"] for p in last.get("t6", {}).get("phases", [])]))
    # T6 — áp lực thật ⇒ SKIP trước bản tạm
    real_psi = RF._psi
    RF._psi = lambda kind: 55.0 if kind == "memory" else 0.0
    rc, last = run_with([ok_f, ok_f])
    RF._psi = real_psi
    case("T6", "T1", "PSI memory 55% (áp lực thật) ⇒ DELTA_SKIPPED_SAFE trước dựng bản tạm, 0 ghi", last["result"] == "DELTA_SKIPPED_SAFE"
         and "T6" in last["report"][L].get("skip", "") and "apply_plan" not in calls, last["report"][L].get("skip"))
    real_sw = RF._vmswap
    cnt = iter(range(0, 10 ** 9, 5000))
    RF._vmswap = lambda: next(cnt)
    rc, last = run_with([ok_f, ok_f])
    RF._vmswap = real_sw
    case("T6", "T2", "swap vào/ra 5000 trang/s (thrash) ⇒ SKIP trước ghi; swap ĐẦY nhưng si/so=0 không chặn (F9 đã PASS với máy thật)",
         last["result"] == "DELTA_SKIPPED_SAFE" and "swap" in last["report"][L].get("skip", ""), last["report"][L].get("skip"))
    # R1 — lượt NO_CHANGE vẫn cấp giấy (đối soát độc lập trọn ô), không bỏ vì tem rẻ không đổi
    RF.cap_c1d = lambda g, pw, s_, c_, lanes=RF.C1D_LANES: {l: dict(fpl, empty=True) for l in lanes}
    rc, last = run_with([ok_f, ok_f])
    case("R1", "R1", "mọi lane NO_CHANGE (băm/HEAD không đổi) ⇒ vẫn gọi cert_tick cấp giấy (issue mặc định True) — đối soát không bị bỏ",
         last["result"] == "NO_CHANGE" and ticks and ticks[-1].get("issue", True) is True, (last["result"], ticks[-1:] and list(ticks[-1].keys())))
    GRF_SRC = open(GRF_P).read()
    case("R1", "R2", "giấy (GC.run) đọc trọn MỌI ô mỗi lượt: không có nhánh bỏ ô theo tín hiệu rẻ (signals_now chỉ báo, không lọc ô)",
         "for c in cells:" in open(GC_P).read() and "signals_now(S" in open(GC_P).read() and "issue=set(bad) <= CERT_RUN_ON_SKIP" in GRF_SRC, "mẫu mã")
    # R2 đầu-cuối: lượt có code BLOCKED claude-mcp (chủ khai báo) ⇒ cert_tick nhận owned, op_failure không chứa «code BLOCKED»
    RF.cap_c1d = lambda g, pw, s_, c_, lanes=RF.C1D_LANES: {l: dict(fpl, empty=True) for l in lanes}
    RF.cap_code = lambda w, s_: {"claude-mcp": {"rule": "git-head", "runtime_ok": False, "runtime": {"container": "incomex-claude-mcp", "diff_vs_head": ["app/server.py"]}}}
    real_decide = RF.decide
    srcs_c = json.load(open(RF.SOURCES))

    def dec_patch(caps, sources):
        d = real_decide(dict(caps, code={}), sources)
        d["code"] = {"decision": "BLOCKED", "repos": {"claude-mcp": {"decision": "BLOCKED", "why": "bản chạy ≠ nguồn cho vào",
                                                                     "runtime": caps["code"]["claude-mcp"]["runtime"]}}}
        return d
    RF.decide = dec_patch
    rc, last = run_with([ok_f, ok_f])
    RF.decide = real_decide
    RF.cap_code = lambda w, s_: {}
    case("R2", "A6", "cmd_run: code BLOCKED chỉ vì claude-mcp ≠ HEAD ⇒ cert_tick(owned=[code:claude-mcp]) + KHÔNG có «code BLOCKED» trong lỗi đỏ",
         ticks and [i["cell"] for i in ticks[-1].get("owned") or []] == ["code:claude-mcp"] and "code BLOCKED" not in (ticks[-1]["op_failure"] or ""),
         (ticks[-1:] and (ticks[-1].get("owned"), ticks[-1]["op_failure"])))

    # ======================================================================= H1 — W2 / W3 / P (recovery_ok thật, verify_files thay)
    RC = TMP + "/rec"
    os.makedirs(RC + "/current")
    RF.REC_CUR, RF.REC_ROOT = RC + "/current", RC
    H = load(GRF_P, "graph_refresh_c1d2_h1")
    H.REC_CUR, H.REC_ROOT, H.INV, H.RECMAN = RC + "/current", RC, T2 + "/inv-h1.json", T2 + "/recman-h1.json"
    H.GR.verify_files = lambda d: (json.load(open(d + "/meta.json")), [])
    pre_inv = {k: INV0[k] for k in INV0 if k not in ("run", "computed_at")}

    def h1(meta_inv, inv, recman_meta_ok=True):
        json.dump({"invariants": meta_inv, "state": {}}, open(RC + "/current/meta.json", "w"))
        json.dump(dict(inv, run="X", computed_at="T"), open(H.INV, "w"))
        json.dump({"current": {"meta_sha256": H.sha_file(RC + "/current/meta.json") if recman_meta_ok else "0" * 64}}, open(H.RECMAN, "w"))
        return H.recovery_ok(FakeGr())
    adv = dict(pre_inv, gs_keys_count=pre_inv["gs_keys_count"] + 3, gs_keys_sha256="9" * 64)
    hp, hw2, hw3 = h1(pre_inv, pre_inv), h1(pre_inv, adv), h1(pre_inv, pre_inv, recman_meta_ok=False)
    case("H1", "H1", "điểm = RECMAN và meta.invariants = INV (chỉ khác run/computed_at) ⇒ recovery_ok", hp["ok"], hp.get("why"))
    case("H1", "W2", "W2: Graph+INV đã tiến, điểm/RECMAN còn PRE ⇒ recovery_ok FALSE (lý do H1) ⇒ tiền điều kiện recovery ⇒ SKIP đỏ, 0 ghi",
         not hw2["ok"] and str(hw2.get("why")).startswith("H1") and "gs_keys_count" in hw2["why"], hw2.get("why"))
    case("H1", "W3", "W3: điểm hiện hành ≠ recovery-manifest ⇒ vẫn FALSE như trước (lệch manifest)", not hw3["ok"] and "lệch manifest" in hw3.get("why", ""), hw3.get("why"))
    # W2 qua cmd_run: tiền điều kiện thật (các cổng khác thay) ⇒ SKIP_PRECONDITION recovery, cert không cấp (issue False) + op_failure ⇒ đỏ, 0 ghi
    class FakeGrAdv(FakeGr):
        def invariants(self, pw):
            return dict(adv)
    H.r7_g1lib.load = lambda path=None: FakeGrAdv()
    H.take_lock = lambda trig: open(os.devnull, "w")
    H.vps_ghi_state = lambda: {"ok": True}
    H.guard_state = lambda: {"ok": True}
    H.config_guard_clean = lambda: True
    real_sh = H.sh
    H.sh = lambda cmd, inp=None, timeout=900, env=None: (0, '{"bad_fast": []}', "") if cmd[:2] == [H.G1, "status"] else real_sh(cmd, inp, timeout, env)
    H.other_writers = lambda: []
    H.STATE, H.LOG = T2 + "/state-h1", T2 + "/log-h1.jsonl"
    hcalls, hticks = [], []
    H.apply_v0 = lambda *a, **k: hcalls.append("apply_v0") or (True, "")
    H.apply_plan = lambda *a, **k: hcalls.append("apply_plan")
    H.cert_tick = lambda rec, *a, **k: hticks.append(k) or {}
    H.l2_tick = lambda rec: None
    h1(pre_inv, adv)
    H.mem_avail = lambda: 8 * 1024 ** 3
    rcw = H.cmd_run(types.SimpleNamespace(execute=True, trigger="timer", only=None))
    lw = json.load(open(H.STATE + "/last.json"))
    case("H1", "W2r", "cmd_run W2 ⇒ SKIP_PRECONDITION [recovery] · 0 apply_plan/apply-v0 · cert_tick issue=False + op_failure (đèn #24 ĐỎ)",
         lw["result"] == "SKIP_PRECONDITION" and "recovery" in lw["failed"] and not hcalls and hticks and hticks[-1].get("issue") is False
         and "recovery" in (hticks[-1].get("op_failure") or ""), (lw["result"], lw.get("failed"), hcalls, hticks[-1:]))
finally:
    shutil.rmtree(TMP, ignore_errors=True)

summ = {"total": len(RES), "pass": sum(r["pass"] for r in RES), "fail": [r["group"] + ":" + r["id"] for r in RES if not r["pass"]],
        "by_group": {g: "%d/%d" % (sum(r["pass"] for r in RES if r["group"] == g), sum(1 for r in RES if r["group"] == g)) for g in sorted({r["group"] for r in RES})},
        "sha256": {os.path.basename(p): hashlib.sha256(open(p, "rb").read()).hexdigest() for p in (GRF_P, GC_P, GA_P)}}
print("C1D2 FIXTURES %s" % json.dumps(summ, ensure_ascii=False))
if OUT:
    json.dump({"summary": summ, "cases": RES}, open(OUT, "w"), ensure_ascii=False, indent=1)
sys.exit(0 if not summ["fail"] else 1)
