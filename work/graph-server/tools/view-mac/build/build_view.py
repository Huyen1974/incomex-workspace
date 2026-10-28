"""Dung tep do thi cho man hinh VIEW0 tu ban xuat graph-v1 R9 (chi doc nguon).

RUN: GS-VIEW0-MAC-LOCAL-20261011-17 · task work/graph-server
  prep  <src_dir> <work_dir>            : kiem sha256 nguon, tach 3 lop, ghi layout-input.json
  write <src_dir> <work_dir> <out_dir>  : doc positions.json (Graphology ForceAtlas2), ghi 4 tep GEXF 1.3 + manifest.json
Khong tu che nhan/quan he: nhan nut = ma dang luu (company_code|order_code|union_code|name|key|id|gs_key);
canh ma khong co trust => "Graph không lưu".
"""
import ast, collections, datetime, hashlib, json, math, os, sys
from xml.sax.saxutils import quoteattr

PIN = {
    "graph-v1-nodes.jsonl": "a50322d5fa9d016f1d80fbed6a957175903714a8697e10c485dadd53a492d1c4",
    "graph-v1-rels.jsonl": "01247b5c568c918eaa3916e8fc188dcfbf26ebff950e8e8408b13b0537cd2e71",
}
SOURCE_PATH = "/opt/incomex/work/graph-server/evidence/GS-R9-BUSINESS-LIVE-REFRESH-20261009-15/s3/export-post/"
SOURCE_EXPORTED_UTC = "2026-10-11T01:14Z"
GROUP = {"b88": "base88", "pg": "pgdot", "dot": "pgdot", "code": "code", "code-meta": "code"}
GROUP_TITLE = {"base88": "Base88", "pgdot": "PG/DOT", "code": "Code"}
EXPECT = {"base88": (1009, 1504), "pgdot": (1276, 1201), "code": (1311, 4118)}
NO_TRUST = "Graph không lưu"
LABEL_FIELDS = ("company_code", "order_code", "union_code", "name", "key", "id", "gs_key")
NODE_COLOR = {  # mot ho mau cho moi lop
    "B88Company": (214, 39, 40), "B88Order": (255, 127, 14), "B88Trainee": (242, 177, 52), "B88Union": (140, 86, 75),
    "PgTable": (31, 119, 180), "PgFunction": (23, 190, 207), "PgTrigger": (107, 174, 214),
    "DotCommand": (57, 73, 171), "DotRegistryEntry": (121, 134, 203),
    "CodeSymbol": (44, 160, 44), "CodeModule": (0, 112, 60), "CodeFileReference": (127, 201, 127),
    "CodeTestReference": (184, 225, 134), "CodeInsight": (102, 194, 164), "ExternalDependency": (166, 166, 60),
    "CodeRepository": (0, 77, 38), "GraphMetadata": (127, 127, 127),
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
    n_attrs = [("lop", "Lớp"), ("loai", "Loại nút"), ("muc_tin", "Mức tin (trust)"), ("bac", "Số cạnh")] + \
              [(f"p_{k}", k) for k in node_keys]
    e_attrs = [("lop", "Lớp"), ("loai", "Loại cạnh"), ("muc_tin", "Mức tin (trust)")] + \
              [(f"p_{k}", k) for k in edge_keys]
    nid = {k: str(i) for i, (k, t) in enumerate(n_attrs)}
    eid = {k: str(i) for i, (k, t) in enumerate(e_attrs)}
    generated = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    src_sha = {k: v for k, v in PIN.items()}
    files = {"graph-merged.gexf": None, "graph-base88.gexf": "base88", "graph-pgdot.gexf": "pgdot", "graph-code.gexf": "code"}
    manifest = {"run_id": "GS-VIEW0-MAC-LOCAL-20261011-17", "generated_utc": generated, "source_path_vps": SOURCE_PATH,
                "source_exported_utc": SOURCE_EXPORTED_UTC, "source_sha256": src_sha,
                "layout": "graphology-layout-forceatlas2@0.10.1 (graphology@0.25.4), seed co dinh, moi lop mot khoi, 3 khoi xep tam giac",
                "color": "theo lop (ho mau) va loai nut; canh theo lop", "size": "3 + 2.2*sqrt(so canh), toi da 30",
                "label": "ma dang luu: " + "|".join(LABEL_FIELDS), "edge_trust_missing": NO_TRUST, "exclusions": 0,
                "files": {}}
    for fname, grp in files.items():
        ns = [k for k in sorted(nodes) if grp is None or nodes[k]["group"] == grp]
        es = [r for r in rels if grp is None or r["group"] == grp]
        title = "Toàn bộ 3 lớp" if grp is None else GROUP_TITLE[grp]
        lines = ['<?xml version="1.0" encoding="UTF-8"?>',
                 '<gexf xmlns="http://gexf.net/1.3" xmlns:viz="http://gexf.net/1.3/viz" version="1.3">',
                 f'  <meta lastmodifieddate="{generated[:10]}"><creator>Incomex Graph VIEW0 (Claude Code CLI)</creator>'
                 f'<description>{quoteattr("Graph Incomex · " + title + " · nguồn graph-v1 export R9 " + SOURCE_EXPORTED_UTC + " · nodes sha256 " + PIN["graph-v1-nodes.jsonl"] + " · rels sha256 " + PIN["graph-v1-rels.jsonl"])[1:-1]}</description></meta>',
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
            vals = {"lop": GROUP_TITLE[n["group"]], "loai": n["type"], "muc_tin": sval(p.get("trust")) or NO_TRUST,
                    "bac": str(deg[k])}
            vals.update({f"p_{a}": sval(p[a]) for a in p})
            x, y = pos[k]
            r, g, b = NODE_COLOR[n["type"]]
            size = min(30.0, 3 + 2.2 * math.sqrt(deg[k]))
            lines.append(f'      <node id={quoteattr(k)} label={quoteattr(label)}><attvalues>' +
                         "".join(f'<attvalue for="{nid[a]}" value={quoteattr(v)}/>' for a, v in vals.items() if v != "") +
                         f'</attvalues><viz:size value="{size:.2f}"/><viz:position x="{x:.3f}" y="{y:.3f}" z="0.0"/>'
                         f'<viz:color r="{r}" g="{g}" b="{b}"/></node>')
        lines += ['    </nodes>', '    <edges>']
        for e in es:
            p = e["props"]
            vals = {"lop": GROUP_TITLE[e["group"]], "loai": e["type"], "muc_tin": sval(p.get("trust")) or NO_TRUST}
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
        trust = collections.Counter(sval(e["props"].get("trust")) or NO_TRUST for e in es)
        manifest["files"][fname] = {"layer": title, "nodes": len(ns), "edges": len(es), "sha256": sha256(path),
                                    "bytes": os.path.getsize(path), "edge_trust": dict(trust),
                                    "node_types": dict(collections.Counter(nodes[k]["type"] for k in ns))}
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
