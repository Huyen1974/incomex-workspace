"""Kiem doc lap 4 tep GEXF: parse XML, dem nut/canh duy nhat, tinh lai gs_keys_sha256 / edges_sha256
(cung cong thuc graph-v1 invariants) va so voi nguon; kiem moi nut co viz:position/color/size."""
import hashlib, json, sys, xml.etree.ElementTree as ET
NS = {"g": "http://gexf.net/1.3", "viz": "http://gexf.net/1.3/viz"}
data = sys.argv[1]
man = json.load(open(f"{data}/manifest.json"))
res = {}
allk, alle = None, None
for fname, info in man["files"].items():
    root = ET.parse(f"{data}/{fname}").getroot()
    assert root.get("version") == "1.3", fname
    nodes = root.findall(".//g:nodes/g:node", NS); edges = root.findall(".//g:edges/g:edge", NS)
    ids = [n.get("id") for n in nodes]; eids = [e.get("id") for e in edges]
    viz_ok = all(n.find("viz:position", NS) is not None and n.find("viz:color", NS) is not None and n.find("viz:size", NS) is not None for n in nodes)
    keys = sorted(ids); es = sorted(f'{e.get("label")}|{e.get("source")}|{e.get("target")}' for e in edges)
    attr_title = {a.get("id"): a.get("title") for a in root.findall('.//g:attributes[@class="edge"]/g:attribute', NS)}
    mt = next(k for k, t in attr_title.items() if t == "Mức tin (trust)")
    no_trust = sum(1 for e in edges if not any(v.get("for") == mt and v.get("value") for v in e.findall(".//g:attvalue", NS)))
    res[fname] = {"nodes": len(ids), "nodes_unique": len(set(ids)), "edges": len(eids), "edges_unique_id": len(set(eids)),
                  "dangling": sum(1 for e in edges if e.get("source") not in set(ids) or e.get("target") not in set(ids)),
                  "viz_all_nodes": viz_ok, "edges_trust_missing_label": no_trust,
                  "gs_keys_sha256": hashlib.sha256("\n".join(keys).encode()).hexdigest(),
                  "edges_sha256": hashlib.sha256("\n".join(es).encode()).hexdigest(),
                  "manifest_counts_match": (len(ids), len(eids)) == (info["nodes"], info["edges"])}
print(json.dumps(res, indent=1, ensure_ascii=False))
