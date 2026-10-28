"""Dung DUNG MOT tep GEXF tong (private, Mac) tu ban xuat logic graph-v1 = diem khoi phuc D23 hien hanh — GS-RAM-GATE-C1E-20261027-15 (E3).
Khuon build_view_r11.py (VIEW0/R11): khong tu che nhan/quan he; nhan nut = ma dang luu. Them so voi R11: 4 khoi lop (Base88 · PG/DOT gom
pg+dot+pgl1 · Ha tang infra · Code gom code+code-meta), canh cheo lop giu nguyen (khong dung cho bo cuc), moi nut/canh mang O giay N4 +
nhan N4 tai T (theo giay current.json) + gio cap giay + trang thai retired + quyen xem PRIVATE.
  prep   <src_dir> <work_dir>             : kiem sha256 nguon (SHA256SUMS + meta.json = RECMAN), ghi layout-input.json
  write  <src_dir> <work_dir> <out_dir>   : doc positions.json, ghi graph-merged.gexf + manifest.json
  verify <src_dir> <out_dir>              : parse XML doc lap, dem nut/canh, so gs_keys_sha256/edges_sha256 voi graph-invariants.json
"""
import collections, datetime, hashlib, json, math, os, sys
from xml.sax.saxutils import quoteattr

RUN_ID = "GS-RAM-GATE-C1E-20261027-15"
META_SHA = "6e7ec6e7200585c0c025f65b26d3f39527e61d08258984e12c498b624b52f34c"   # recovery-manifest current.meta_sha256 (S0 + POST)
SOURCE_PATH = "/opt/incomex/graph-server/prod-v1/backups/recovery/current/ (D23 2026-10-26T10:52:58Z, = Graph sống 27/10 05:09Z)"
PY_REPOS = {"claude-mcp", "claude-kb", "lark-client", "agent-data-repo"}
RULE = "luật v0.6/R11"
GROUP = {"b88": "base88", "pg": "pgdot", "dot": "pgdot", "pgl1": "pgdot", "infra": "infra", "code": "code", "code-meta": "code"}
ORDER = ["base88", "pgdot", "infra", "code"]
GROUP_TITLE = {"base88": "Base88", "pgdot": "PG/DOT (+L1 catalog)", "infra": "Hạ tầng (container/unit/cổng/git)", "code": "Code"}
NO_TRUST = "Graph không lưu"
ACL = "PRIVATE · chỉ Owner trên Mac này (không công khai, không Git/Drive)"
LABEL_FIELDS = ("company_code", "order_code", "union_code", "name", "key", "path", "id", "gs_key")
NODE_COLOR = {"B88Company": (214, 39, 40), "B88Order": (255, 127, 14), "B88Trainee": (242, 177, 52), "B88Union": (140, 86, 75),
              "PgTable": (31, 119, 180), "PgFunction": (23, 190, 207), "PgTrigger": (107, 174, 214), "PgView": (70, 130, 200),
              "PgForeignKey": (90, 150, 220), "DotCommand": (57, 73, 171), "DotRegistryEntry": (121, 134, 203),
              "CodeSymbol": (44, 160, 44), "CodeModule": (0, 112, 60), "CodeFileReference": (127, 201, 127), "CodeTestReference": (184, 225, 134),
              "CodeInsight": (102, 194, 164), "ExternalDependency": (166, 166, 60), "CodeRepository": (0, 77, 38), "GraphMetadata": (127, 127, 127),
              "ApiEndpoint": (0, 150, 120)}
GROUP_COLOR = {"pgdot": (75, 120, 200), "infra": (148, 103, 189)}
EDGE_COLOR = {"base88": (214, 120, 60, 0.35), "pgdot": (60, 110, 190, 0.35), "infra": (148, 103, 189, 0.45), "code": (60, 150, 80, 0.30)}


def code_edge_trust(rtype, repo):
    if rtype in ("part_of", "evidences"):
        return "DERIVED_WITH_RULE"
    if repo in PY_REPOS:
        return {"declares": "EXACT_POSITIVE", "has_method": "EXACT_POSITIVE", "implements": "EXACT_POSITIVE", "imports": "EXACT_POSITIVE",
                "calls": "HIGH_CANDIDATE", "instantiates": "ADVISORY"}.get(rtype, "UNKNOWN_FROM_GRAPH")
    return "UNKNOWN_FROM_GRAPH"


def code_node_trust(p, ntype):
    repo, kind, name = p.get("repo"), p.get("kind"), str(p.get("name") or "")
    if ntype in ("CodeRepository", "GraphMetadata"):
        return "DERIVED_WITH_RULE"
    if kind == "dependency":
        if name.startswith("module-edge:"):
            return "DERIVED_WITH_RULE"
        if repo in PY_REPOS:
            return "EXACT_POSITIVE"
        return "UNKNOWN_ALIAS_TO_PACKAGE" if "node_modules/" in name else "EXACT_POSITIVE (thư mục→đích)"
    if kind == "symbol":
        return "EXACT_POSITIVE" if repo in PY_REPOS else "UNKNOWN_FROM_GRAPH"
    return "ADVISORY"


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def sval(v):
    if v is None:
        return ""
    if isinstance(v, (dict, list, tuple)):
        return json.dumps(v, ensure_ascii=False, sort_keys=True, default=str)
    return str(v)


def load(src):
    if sha256(os.path.join(src, "meta.json")) != META_SHA:
        sys.exit("META_NE_RECMAN")
    want = dict(reversed(l.split()) for l in open(os.path.join(src, "SHA256SUMS")) if l.strip())
    meta = json.load(open(os.path.join(src, "meta.json")))
    for f in ("nodes.jsonl", "rels.jsonl"):
        got = sha256(os.path.join(src, f))
        if got != want.get(f) or got != meta["files"][f]:
            sys.exit("SOURCE_SHA_MISMATCH %s" % f)
    nodes = {}
    for line in open(os.path.join(src, "nodes.jsonl"), encoding="utf-8"):
        d = json.loads(line)
        labs = sorted(x for x in d["l"] if x not in ("GS", "__Node__"))
        p = d["p"]
        nodes[d["k"]] = {"type": labs[0] if len(labs) == 1 else "+".join(labs), "labels": labs, "props": p,
                         "group": GROUP.get(p.get("gs_layer"), "code")}
    rels = []
    for i, line in enumerate(open(os.path.join(src, "rels.jsonl"), encoding="utf-8")):
        r = json.loads(line)
        if r["s"] not in nodes or r["d"] not in nodes:
            sys.exit("DANGLING %s" % r["t"])
        rels.append({"id": "e%d" % i, "type": r["t"], "src": r["s"], "dst": r["d"], "props": r["p"], "group": nodes[r["s"]]["group"],
                     "cross": nodes[r["s"]]["group"] != nodes[r["d"]]["group"]})
    return meta, nodes, rels


def prep(src, work):
    meta, nodes, rels = load(src)
    out = {"order": ORDER, "groups": {}}
    for g in ORDER:
        ks = sorted(k for k, n in nodes.items() if n["group"] == g)
        es = [[r["src"], r["dst"]] for r in rels if r["group"] == g and not r["cross"]]
        out["groups"][g] = {"nodes": ks, "edges": es}
    os.makedirs(work, mode=0o700, exist_ok=True)
    json.dump(out, open(os.path.join(work, "layout-input.json"), "w"))
    print(json.dumps({g: (len(v["nodes"]), len(v["edges"])) for g, v in out["groups"].items()}),
          "cross", sum(r["cross"] for r in rels), "state", meta["state"]["nodes"], meta["state"]["edges"])


def n4(cells, du):
    if not cells:
        return "KHÔNG CÓ Ô (MỘT PHẦN)"
    return "ĐỦ tại T" if all(c in du for c in cells) else "MỘT PHẦN"


def write(src, work, outdir):
    meta, nodes, rels = load(src)
    pos = json.load(open(os.path.join(work, "positions.json")))
    cat = json.load(open(os.path.join(src, "cert-cells.json")))
    cert = json.load(open(os.path.join(src, "cert-summary.json")))
    du, at = set(cert["du_cells"]), cert["generated_at"]
    lm, rm = cat.get("graph_label_map") or {}, cat.get("graph_rel_map") or {}
    deg = collections.Counter()
    for r in rels:
        deg[r["src"]] += 1
        deg[r["dst"]] += 1
    first = ("gs_key", "name", "id", "company_code", "order_code", "union_code", "key", "path", "value", "source", "trust", "snapshot_utc", "gs_layer",
             "retired_at", "retired_by", "retired_reason", "schema", "file_path", "line", "kind", "symbol_kind", "repo", "description",
             "source_file", "source_fields", "catalog", "rule")
    rank = lambda k: (first.index(k), "") if k in first else (len(first), k)
    node_keys = sorted({k for n in nodes.values() for k in n["props"]}, key=rank)
    edge_keys = sorted({k for r in rels for k in r["props"]}, key=rank)
    n_attrs = [("lop", "Lớp"), ("lop_graph", "Lớp Graph (gs_layer)"), ("loai", "Loại nút"), ("muc_tin", "Mức tin (trust)"), ("nguon_tin", "Nguồn mức tin"),
               ("bac", "Số cạnh"), ("o_giay", "Ô giấy N4"), ("nhan_n4", "Nhãn N4 tại T"), ("giay_t", "Giấy cấp lúc (T)"), ("trang_thai", "Trạng thái"),
               ("acl", "Quyền xem")] + [("p_" + k, k) for k in node_keys]
    e_attrs = [("lop", "Lớp"), ("loai", "Loại cạnh"), ("muc_tin", "Mức tin (trust)"), ("nguon_tin", "Nguồn mức tin"), ("o_giay", "Ô giấy N4"),
               ("nhan_n4", "Nhãn N4 tại T"), ("cheo", "Cạnh chéo lớp"), ("acl", "Quyền xem")] + [("p_" + k, k) for k in edge_keys]
    nid = {k: str(i) for i, (k, t) in enumerate(n_attrs)}
    eid = {k: str(i) for i, (k, t) in enumerate(e_attrs)}
    gen = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    desc = ("Graph Incomex · TOÀN BỘ 4 khối lớp · bản xuất D23 %s (= Graph sống, %d nút/%d cạnh) · nodes sha256 %s · rels sha256 %s · giấy N4 %s · "
            "PRIVATE Mac · ảnh chụp tĩnh, KHÔNG tự cập nhật" % (meta["created_at"], meta["state"]["nodes"], meta["state"]["edges"], meta["files"]["nodes.jsonl"],
                                                              meta["files"]["rels.jsonl"], at))
    L = ['<?xml version="1.0" encoding="UTF-8"?>', '<gexf xmlns="http://gexf.net/1.3" xmlns:viz="http://gexf.net/1.3/viz" version="1.3">',
         '  <meta lastmodifieddate="%s"><creator>Incomex Graph C1-E (Claude Code CLI · %s)</creator><description>%s</description></meta>' % (gen[:10], RUN_ID, quoteattr(desc)[1:-1]),
         '  <graph defaultedgetype="directed" mode="static">', '    <attributes class="node" mode="static">']
    L += ['      <attribute id="%s" title=%s type="%s"/>' % (nid[i], quoteattr(t), "integer" if i == "bac" else "string") for i, t in n_attrs]
    L += ['    </attributes>', '    <attributes class="edge" mode="static">']
    L += ['      <attribute id="%s" title=%s type="string"/>' % (eid[i], quoteattr(t)) for i, t in e_attrs]
    L += ['    </attributes>', '    <nodes>']
    for k in sorted(nodes):
        n = nodes[k]
        p = n["props"]
        label = next((sval(p[f]) for f in LABEL_FIELDS if p.get(f) not in (None, "")), k)
        if p.get("trust"):
            mt, nt = sval(p["trust"]), "Graph"
        elif n["group"] == "code":
            mt, nt = code_node_trust(p, n["type"]), RULE
        else:
            mt, nt = NO_TRUST, ""
        cells = sorted({c for l in n["labels"] for c in lm.get(l, [])})
        vals = {"lop": GROUP_TITLE[n["group"]], "lop_graph": sval(p.get("gs_layer")), "loai": n["type"], "muc_tin": mt, "nguon_tin": nt, "bac": str(deg[k]),
                "o_giay": ",".join(cells), "nhan_n4": n4(cells, du), "giay_t": at, "trang_thai": "RETIRED %s" % p["retired_at"] if p.get("retired_at") else "đang có",
                "acl": ACL}
        vals.update({"p_" + a: sval(p[a]) for a in p})
        x, y = pos[k]
        r, g, b = NODE_COLOR.get(n["type"], GROUP_COLOR.get(n["group"], (110, 110, 110)))
        size = min(30.0, 3 + 2.2 * math.sqrt(deg[k]))
        L.append('      <node id=%s label=%s><attvalues>' % (quoteattr(k), quoteattr(label)) +
                 "".join('<attvalue for="%s" value=%s/>' % (nid[a], quoteattr(v)) for a, v in vals.items() if v != "") +
                 '</attvalues><viz:size value="%.2f"/><viz:position x="%.3f" y="%.3f" z="0.0"/><viz:color r="%d" g="%d" b="%d"/></node>' % (size, x, y, r, g, b))
    L += ['    </nodes>', '    <edges>']
    trust_ct = collections.Counter()
    for e in rels:
        p = e["props"]
        if p.get("trust"):
            mt, nt = sval(p["trust"]), "Graph"
        elif e["group"] == "code":
            mt, nt = code_edge_trust(e["type"], nodes[e["src"]]["props"].get("repo") or nodes[e["dst"]]["props"].get("repo")), RULE
        else:
            mt, nt = NO_TRUST, ""
        trust_ct[mt + ("" if nt != RULE else " (" + RULE + ")")] += 1
        cells = sorted(rm.get(e["type"], []))
        vals = {"lop": GROUP_TITLE[e["group"]], "loai": e["type"], "muc_tin": mt, "nguon_tin": nt, "o_giay": ",".join(cells), "nhan_n4": n4(cells, du),
                "cheo": "có (%s→%s)" % (GROUP_TITLE[nodes[e["src"]]["group"]], GROUP_TITLE[nodes[e["dst"]]["group"]]) if e["cross"] else "", "acl": ACL}
        vals.update({"p_" + a: sval(p[a]) for a in p})
        r, g, b, a = EDGE_COLOR[e["group"]]
        L.append('      <edge id="%s" source=%s target=%s label=%s><attvalues>' % (e["id"], quoteattr(e["src"]), quoteattr(e["dst"]), quoteattr(e["type"])) +
                 "".join('<attvalue for="%s" value=%s/>' % (eid[k2], quoteattr(v)) for k2, v in vals.items() if v != "") +
                 '</attvalues><viz:color r="%d" g="%d" b="%d" a="%s"/></edge>' % (r, g, b, a))
    L += ['    </edges>', '  </graph>', '</gexf>', '']
    os.makedirs(outdir, mode=0o700, exist_ok=True)
    path = os.path.join(outdir, "graph-merged.gexf")
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write("\n".join(L))
    man = {"run_id": RUN_ID, "based_on": "VIEW0/R11 (cùng bố cục/màu/nhãn) + khối Hạ tầng + ô giấy N4", "generated_utc": gen, "source_path_vps": SOURCE_PATH,
           "source_meta": {"created_at": meta["created_at"], "label": meta.get("label"), "state": meta["state"], "meta_sha256": META_SHA, "files": meta["files"]},
           "cert": {"generated_at": at, "self_sha256": cert.get("self_sha256"), "du": cert["du"], "cells": cert["cells"]},
           "acl": ACL, "n4_note": "Nhãn N4 trong tệp = theo giấy tại T; tệp là ẢNH CHỤP TĨNH — câu trả lời hành động phải qua graph-v1 (nhãn máy).",
           "proposed_separated": "86 nhóm / 12 gợi ý D17-b (R10) + 5 ứng viên JEV SHADOW C1-E KHÔNG nằm trong tệp (PROPOSED, không canonical)",
           "layout": "graphology-layout-forceatlas2@0.10.1 (graphology@0.25.4), seed cố định 20261027, mỗi khối lớp một vùng; cạnh chéo lớp không dùng cho bố cục",
           "files": {"graph-merged.gexf": {"nodes": len(nodes), "edges": len(rels), "cross_layer_edges": sum(r["cross"] for r in rels), "sha256": sha256(path),
                                            "bytes": os.path.getsize(path), "edge_trust": dict(trust_ct),
                                            "groups": dict(collections.Counter(GROUP_TITLE[n["group"]] for n in nodes.values())),
                                            "node_types": dict(collections.Counter(n["type"] for n in nodes.values())),
                                            "retired_nodes": sum(1 for n in nodes.values() if n["props"].get("retired_at"))}}}
    fd = os.open(os.path.join(outdir, "manifest.json"), os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        json.dump(man, f, ensure_ascii=False, indent=1)
    print(json.dumps(man["files"]["graph-merged.gexf"], ensure_ascii=False)[:600])


def verify(src, outdir):
    import xml.etree.ElementTree as ET
    NS = {"g": "http://gexf.net/1.3", "viz": "http://gexf.net/1.3/viz"}
    inv = json.load(open(os.path.join(src, "graph-invariants.json")))
    man = json.load(open(os.path.join(outdir, "manifest.json")))
    root = ET.parse(os.path.join(outdir, "graph-merged.gexf")).getroot()
    nodes = root.findall(".//g:nodes/g:node", NS)
    edges = root.findall(".//g:edges/g:edge", NS)
    ids = [n.get("id") for n in nodes]
    sid = set(ids)
    keys_sha = hashlib.sha256("\n".join(sorted(ids)).encode()).hexdigest()
    es = sorted("%s|%s|%s" % (e.get("label"), e.get("source"), e.get("target")) for e in edges)
    edges_sha = hashlib.sha256("\n".join(es).encode()).hexdigest()
    titles = {a.get("id"): a.get("title") for a in root.findall('.//g:attributes[@class="node"]/g:attribute', NS)}
    need = {"Ô giấy N4", "Nhãn N4 tại T", "Giấy cấp lúc (T)", "Trạng thái", "Quyền xem", "Mức tin (trust)", "source"}
    res = {"version": root.get("version"), "nodes": len(ids), "nodes_unique": len(sid), "edges": len(edges), "edges_unique_id": len({e.get("id") for e in edges}),
           "dangling": sum(1 for e in edges if e.get("source") not in sid or e.get("target") not in sid),
           "viz_all_nodes": all(n.find("viz:position", NS) is not None and n.find("viz:color", NS) is not None for n in nodes),
           "gs_keys_sha256": keys_sha, "gs_keys_sha256_eq_inv": keys_sha == inv["gs_keys_sha256"],
           "edges_sha256": edges_sha, "edges_sha256_eq_inv": edges_sha == inv["edges_sha256"],
           "counts_eq_inv": (len(sid), len(edges)) == (inv["gs_keys_count"], inv["edges_count"]),
           "manifest_eq": (len(ids), len(edges)) == (man["files"]["graph-merged.gexf"]["nodes"], man["files"]["graph-merged.gexf"]["edges"])
           and sha256(os.path.join(outdir, "graph-merged.gexf")) == man["files"]["graph-merged.gexf"]["sha256"],
           "attrs_present": sorted(need - set(titles.values())) == []}
    res["PASS"] = all(v for k, v in res.items() if isinstance(v, bool)) and res["dangling"] == 0
    json.dump(res, open(os.path.join(outdir, "gexf-verify.json"), "w"), ensure_ascii=False, indent=1)
    print(json.dumps(res, ensure_ascii=False))


if __name__ == "__main__":
    c = sys.argv[1]
    if c == "prep":
        prep(sys.argv[2], sys.argv[3])
    elif c == "write":
        write(sys.argv[2], sys.argv[3], sys.argv[4])
    elif c == "verify":
        verify(sys.argv[2], sys.argv[3])
    else:
        sys.exit("dùng: build_view_c1e.py prep|write|verify ...")
