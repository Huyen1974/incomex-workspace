"""Doc ban xuat R9 (chi doc), tinh lai gs_keys_sha256/edges_sha256 nhu graph-v1 invariants,
dem theo lop gs_layer va kiem canh cheo lop, canh song song, vong tu than. In JSON ra stdout."""
import ast, collections, hashlib, json, sys
src = sys.argv[1]
def P(v): return ast.literal_eval(v) if isinstance(v, str) else v
nodes = {}
for l in open(f"{src}/graph-v1-nodes.jsonl"):
    d = json.loads(l); labs = P(d["labels"]); p = P(d["props"])
    nodes[p["gs_key"]] = (labs, p)
rels = [json.loads(l) for l in open(f"{src}/graph-v1-rels.jsonl")]
GROUP = {"b88": "base88", "pg": "pgdot", "dot": "pgdot", "code": "code", "code-meta": "code"}
gs_keys = sorted(k for k, (labs, p) in nodes.items() if "GS" in labs)
edges = sorted(f'{r["type"]}|{r["src"]}|{r["dst"]}' for r in rels)
out = {"nodes": len(nodes), "edges": len(rels),
       "gs_keys_count": len(gs_keys), "gs_keys_sha256": hashlib.sha256("\n".join(gs_keys).encode()).hexdigest(),
       "edges_count": len(edges), "edges_sha256": hashlib.sha256("\n".join(edges).encode()).hexdigest()}
nl = collections.Counter(GROUP[p["gs_layer"]] for labs, p in nodes.values())
el = collections.Counter(); cross = 0; missing = 0
pairs = collections.Counter(); loops = 0; trust = collections.Counter(); trust_by = collections.Counter()
labels = collections.Counter(l for labs, p in nodes.values() for l in labs)
types = collections.Counter(r["type"] for r in rels)
for r in rels:
    a, b = nodes.get(r["src"]), nodes.get(r["dst"])
    if a is None or b is None: missing += 1; continue
    ga, gb = GROUP[a[1]["gs_layer"]], GROUP[b[1]["gs_layer"]]
    if ga != gb: cross += 1
    el[ga] += 1
    pairs[(r["src"], r["dst"])] += 1
    if r["src"] == r["dst"]: loops += 1
    t = P(r["props"]).get("trust"); trust[t or "Graph không lưu"] += 1; trust_by[(ga, t or "Graph không lưu")] += 1
out.update(nodes_by_layer=dict(nl), edges_by_layer=dict(el), cross_layer_edges=cross, edges_missing_endpoint=missing,
           parallel_pairs=sum(1 for c in pairs.values() if c > 1), parallel_extra_edges=sum(c - 1 for c in pairs.values() if c > 1),
           self_loops=loops, edge_trust=dict(trust), edge_trust_by_layer={f"{k[0]}|{k[1]}": v for k, v in trust_by.items()},
           labels=dict(labels), rel_types=dict(types))
print(json.dumps(out, ensure_ascii=False, indent=1, sort_keys=True))
