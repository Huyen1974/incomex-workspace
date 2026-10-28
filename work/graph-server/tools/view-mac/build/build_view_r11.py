"""Dung tep do thi cho man hinh VIEW0 tu ban xuat graph-v1 (chi doc nguon) — ban R11 (GS-R11-R10C-INTEGRATED-20261021-03).

Khac VIEW0: nguon = ban xuat graph-v1 production sau R11 (pin sha qua tham so moi truong GS_PIN_NODES/GS_PIN_RELS, so dem
GS_EXPECT); lop Code gom 5 cay (claude-mcp, claude-kb, lark-client, agent-data-repo, nuxt-web); canh/nut code khong luu trust trong
Graph => cot "Mức tin (trust)" ghi muc SUY THEO LUAT CODE-EDGE-TRUST v0.6 + R11 kem cot "Nguồn mức tin" = "luật v0.6/R11".
(goc) RUN: GS-VIEW0-MAC-LOCAL-20261011-17 · task work/graph-server
  prep  <src_dir> <work_dir>            : kiem sha256 nguon, tach 3 lop, ghi layout-input.json
  write <src_dir> <work_dir> <out_dir>  : doc positions.json (Graphology ForceAtlas2), ghi 4 tep GEXF 1.3 + manifest.json
Khong tu che nhan/quan he: nhan nut = ma dang luu (company_code|order_code|union_code|name|key|id|gs_key);
canh ma khong co trust => "Graph không lưu".
"""
import ast, collections, datetime, hashlib, json, math, os, sys
from xml.sax.saxutils import quoteattr

PIN = {"graph-v1-nodes.jsonl": os.environ["GS_PIN_NODES"], "graph-v1-rels.jsonl": os.environ["GS_PIN_RELS"]}
SOURCE_PATH = os.environ["GS_SOURCE_PATH"]
SOURCE_EXPORTED_UTC = os.environ["GS_SOURCE_EXPORTED_UTC"]
RUN_ID = "GS-R11-R10C-INTEGRATED-20261021-03"
CODE_SRC = json.loads(os.environ.get("GS_CODE_SOURCES", "{}"))     # repo -> mô tả nguồn mã đang chạy (refresh-sources.json)
PY_REPOS = {"claude-mcp", "claude-kb", "lark-client", "agent-data-repo"}
RULE = "luật v0.6/R11"


def code_edge_trust(rtype, repo):
    """CODE-EDGE-TRUST v0.6 (+R11). Python: declares/has_method/implements/imports = EXACT_POSITIVE; calls = HIGH_CANDIDATE;
    instantiates = ADVISORY. TS/Vue: chỉ dependency directory→target đo được (nút), cạnh imports/calls/declares = UNKNOWN_FROM_GRAPH.
    part_of/evidences = cấu trúc Cognee (DERIVED_WITH_RULE)."""
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
GROUP = {"b88": "base88", "pg": "pgdot", "dot": "pgdot", "code": "code", "code-meta": "code"}
GROUP_TITLE = {"base88": "Base88", "pgdot": "PG/DOT", "code": "Code"}
EXPECT = {k: tuple(v) for k, v in json.loads(os.environ["GS_EXPECT"]).items()}
NO_TRUST = "Graph không lưu"
LABEL_FIELDS = ("company_code", "order_code", "union_code", "name", "key", "id", "gs_key")
NODE_COLOR = {  # mot ho mau cho moi lop
    "B88Company": (214, 39, 40), "B88Order": (255, 127, 14), "B88Trainee": (242, 177, 52), "B88Union": (140, 86, 75),
    "PgTable": (31, 119, 180), "PgFunction": (23, 190, 207), "PgTrigger": (107, 174, 214),
    "DotCommand": (57, 73, 171), "DotRegistryEntry": (121, 134, 203),
    "CodeSymbol": (44, 160, 44), "CodeModule": (0, 112, 60), "CodeFileReference": (127, 201, 127),
    "CodeTestReference": (184, 225, 134), "CodeInsight": (102, 194, 164), "ExternalDependency": (166, 166, 60),
    "CodeRepository": (0, 77, 38), "GraphMetadata": (127, 127, 127), "ApiEndpoint": (0, 150, 120),
}
EDGE_COLOR = {"base88": (214, 120, 60, 0.35), "pgdot": (60, 110, 190, 0.35), "code": (60, 150, 80, 0.30)}


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def P(v):
    return ast.literal_eval(v) if isinstance(v, str) else v


def load(src):
    for name, want in PIN.items():
        got = sha256(os.path.join(src, name))
        if got != want:
            sys.exit(f"NO_READONLY_EXPORT_TO_MAC: {name} sha256 {got} != {want}")
    nodes = {}
    for line in open(os.path.join(src, "graph-v1-nodes.jsonl"), encoding="utf-8"):
        d = json.loads(line)
        labs = [x for x in P(d["labels"]) if x not in ("GS", "__Node__")]
        p = P(d["props"])
        nodes[p["gs_key"]] = {"type": labs[0] if len(labs) == 1 else "+".join(labs), "props": p,
                              "group": GROUP[p["gs_layer"]]}
    rels = []
    for i, line in enumerate(open(os.path.join(src, "graph-v1-rels.jsonl"), encoding="utf-8")):
        r = json.loads(line)
        g = nodes[r["src"]]["group"]
        if nodes[r["dst"]]["group"] != g:
            sys.exit(f"CROSS_LAYER_EDGE {r['type']} {r['src']} {r['dst']}")
        rels.append({"id": f"e{i}", "type": r["type"], "src": r["src"], "dst": r["dst"], "props": P(r["props"]), "group": g})
    return nodes, rels


def prep(src, work):
    nodes, rels = load(src)
    deg = collections.Counter()
    for r in rels:
        deg[r["src"]] += 1
        deg[r["dst"]] += 1
    out = {}
    for g in EXPECT:
        ks = sorted(k for k, n in nodes.items() if n["group"] == g)
        es = [[r["src"], r["dst"]] for r in rels if r["group"] == g]
        if (len(ks), len(es)) != EXPECT[g]:
            sys.exit(f"LAYER_COUNT_MISMATCH {g} {(len(ks), len(es))} != {EXPECT[g]}")
        out[g] = {"nodes": ks, "edges": es, "isolated": sum(1 for k in ks if deg[k] == 0)}
    json.dump(out, open(os.path.join(work, "layout-input.json"), "w"))
    print(json.dumps({g: {"nodes": len(v["nodes"]), "edges": len(v["edges"]), "isolated": v["isolated"]} for g, v in out.items()}))


def sval(v):
    if v is None:
        return ""
    if isinstance(v, (dict, list, tuple)):
        return json.dumps(v, ensure_ascii=False, sort_keys=True, default=str)
    return str(v)


def write(src, work, outdir):
    nodes, rels = load(src)
    pos = json.load(open(os.path.join(work, "positions.json")))
    deg = collections.Counter()
    for r in rels:
        deg[r["src"]] += 1
        deg[r["dst"]] += 1
    # thu tu thuoc tinh co dinh: cot dan xuat dat ten Viet, roi cot dinh danh/nguon, con lai giu dung ten Graph (a-z).
    # id thuoc tinh la so: parser GEXF cua Gephi Lite chi dung `title` lam ten cot khi id la so.
    first = ("gs_key", "name", "id", "company_code", "order_code", "union_code", "key", "value", "source", "trust",
             "snapshot_utc", "gs_layer", "schema", "args", "file_path", "line", "kind", "symbol_kind", "repo", "description",
             "source_file", "source_row", "declared_status", "paired_dot", "enabled_code", "catalog", "rule", "source_fields",
             "relationship_name", "edge_text")
    rank = lambda k: (first.index(k), "") if k in first else (len(first), k)
    node_keys = sorted({k for n in nodes.values() for k in n["props"]}, key=rank)
    edge_keys = sorted({k for r in rels for k in r["props"]}, key=rank)
    n_attrs = [("lop", "Lớp"), ("loai", "Loại nút"), ("muc_tin", "Mức tin (trust)"), ("nguon_tin", "Nguồn mức tin"), ("bac", "Số cạnh"),
               ("nguon_ma", "Nguồn mã đang chạy")] + [(f"p_{k}", k) for k in node_keys]
    e_attrs = [("lop", "Lớp"), ("loai", "Loại cạnh"), ("muc_tin", "Mức tin (trust)"), ("nguon_tin", "Nguồn mức tin")] + \
              [(f"p_{k}", k) for k in edge_keys]
    nid = {k: str(i) for i, (k, t) in enumerate(n_attrs)}
    eid = {k: str(i) for i, (k, t) in enumerate(e_attrs)}
    generated = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    src_sha = {k: v for k, v in PIN.items()}
    files = {"graph-merged.gexf": None, "graph-base88.gexf": "base88", "graph-pgdot.gexf": "pgdot", "graph-code.gexf": "code"}
    manifest = {"run_id": RUN_ID, "based_on": "VIEW0 GS-VIEW0-MAC-LOCAL-20261011-17 (cùng bố cục/màu/nhãn)", "generated_utc": generated,
                "source_path_vps": SOURCE_PATH, "code_sources": CODE_SRC,
                "trust_rule": "Base88/PG/DOT: trust lưu trong Graph. Code: suy theo CODE-EDGE-TRUST v0.6 + R11 (cột Nguồn mức tin)",
                "proposed_separated": "86 nhóm / 12 gợi ý D17-b (R10) KHÔNG nằm trong tệp này (PROPOSED, không canonical)",
                "source_exported_utc": SOURCE_EXPORTED_UTC, "source_sha256": src_sha,
                "layout": "graphology-layout-forceatlas2@0.10.1 (graphology@0.25.4), seed co dinh, moi lop mot khoi, 3 khoi xep tam giac",
                "color": "theo lop (ho mau) va loai nut; canh theo lop", "size": "3 + 2.2*sqrt(so canh), toi da 30",
                "label": "ma dang luu: " + "|".join(LABEL_FIELDS), "edge_trust_missing": NO_TRUST, "exclusions": 0,
                "files": {}}
    for fname, grp in files.items():
        ns = [k for k in sorted(nodes) if grp is None or nodes[k]["group"] == grp]
        es = [r for r in rels if grp is None or r["group"] == grp]
        title = "Toàn bộ 3 lớp (Code 5 cây)" if grp is None else GROUP_TITLE[grp]
        lines = ['<?xml version="1.0" encoding="UTF-8"?>',
                 '<gexf xmlns="http://gexf.net/1.3" xmlns:viz="http://gexf.net/1.3/viz" version="1.3">',
                 f'  <meta lastmodifieddate="{generated[:10]}"><creator>Incomex Graph VIEW0 R11 (Claude Code CLI)</creator>'
                 f'<description>{quoteattr("Graph Incomex · " + title + " · nguồn graph-v1 export R11 " + SOURCE_EXPORTED_UTC + " · nodes sha256 " + PIN["graph-v1-nodes.jsonl"] + " · rels sha256 " + PIN["graph-v1-rels.jsonl"])[1:-1]}</description></meta>',
                 '  <graph defaultedgetype="directed" mode="static">',
                 '    <attributes class="node" mode="static">']
        lines += [f'      <attribute id="{nid[i]}" title={quoteattr(t)} type="{"integer" if i == "bac" else "string"}"/>' for i, t in n_attrs]
        lines += ['    </attributes>', '    <attributes class="edge" mode="static">']
        lines += [f'      <attribute id="{eid[i]}" title={quoteattr(t)} type="string"/>' for i, t in e_attrs]
        lines += ['    </attributes>', '    <nodes>']
        for k in ns:
            n = nodes[k]
            p = n["props"]
            label = next(sval(p[f]) for f in LABEL_FIELDS if p.get(f) not in (None, ""))
            if p.get("trust"):
                mt, nt = sval(p["trust"]), "Graph"
            elif n["group"] == "code":
                mt, nt = code_node_trust(p, n["type"]), RULE
            else:
                mt, nt = NO_TRUST, ""
            vals = {"lop": GROUP_TITLE[n["group"]], "loai": n["type"], "muc_tin": mt, "nguon_tin": nt, "bac": str(deg[k]),
                    "nguon_ma": CODE_SRC.get(p.get("repo"), "") if n["group"] == "code" else ""}
            vals.update({f"p_{a}": sval(p[a]) for a in p})
            x, y = pos[k]
            r, g, b = NODE_COLOR.get(n["type"], (110, 110, 110))
            size = min(30.0, 3 + 2.2 * math.sqrt(deg[k]))
            lines.append(f'      <node id={quoteattr(k)} label={quoteattr(label)}><attvalues>' +
                         "".join(f'<attvalue for="{nid[a]}" value={quoteattr(v)}/>' for a, v in vals.items() if v != "") +
                         f'</attvalues><viz:size value="{size:.2f}"/><viz:position x="{x:.3f}" y="{y:.3f}" z="0.0"/>'
                         f'<viz:color r="{r}" g="{g}" b="{b}"/></node>')
        lines += ['    </nodes>', '    <edges>']
        for e in es:
            p = e["props"]
            if p.get("trust"):
                mt, nt = sval(p["trust"]), "Graph"
            elif e["group"] == "code":
                mt, nt = code_edge_trust(e["type"], nodes[e["src"]]["props"].get("repo") or nodes[e["dst"]]["props"].get("repo")), RULE
            else:
                mt, nt = NO_TRUST, ""
            vals = {"lop": GROUP_TITLE[e["group"]], "loai": e["type"], "muc_tin": mt, "nguon_tin": nt}
            vals.update({f"p_{a}": sval(p[a]) for a in p})
            r, g, b, a = EDGE_COLOR[e["group"]]
            lines.append(f'      <edge id="{e["id"]}" source={quoteattr(e["src"])} target={quoteattr(e["dst"])} label={quoteattr(e["type"])}><attvalues>' +
                         "".join(f'<attvalue for="{eid[k]}" value={quoteattr(v)}/>' for k, v in vals.items() if v != "") +
                         f'</attvalues><viz:color r="{r}" g="{g}" b="{b}" a="{a}"/></edge>')
        lines += ['    </edges>', '  </graph>', '</gexf>', '']
        path = os.path.join(outdir, fname)
        fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        trust = collections.Counter(sval(e["props"].get("trust")) or (code_edge_trust(e["type"], nodes[e["src"]]["props"].get("repo") or nodes[e["dst"]]["props"].get("repo")) + " (" + RULE + ")" if e["group"] == "code" else NO_TRUST) for e in es)
        manifest["files"][fname] = {"layer": title, "nodes": len(ns), "edges": len(es), "sha256": sha256(path),
                                    "bytes": os.path.getsize(path), "edge_trust": dict(trust),
                                    "node_types": dict(collections.Counter(nodes[k]["type"] for k in ns)),
                                    "code_repos": dict(collections.Counter(nodes[k]["props"].get("repo") for k in ns if nodes[k]["group"] == "code"))}
    mpath = os.path.join(outdir, "manifest.json")
    fd = os.open(mpath, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=1)
    print(json.dumps({k: (v["nodes"], v["edges"], v["sha256"][:12]) for k, v in manifest["files"].items()}))


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "prep":
        prep(sys.argv[2], sys.argv[3])
    elif cmd == "write":
        write(sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        sys.exit("usage: build_view.py prep|write ...")
