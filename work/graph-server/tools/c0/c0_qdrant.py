# GS-C0-COVERAGE-INVENTORY-20261022-05 · F3 · METADATA QDRANT CHỈ-ĐỌC (GET) — dùng lại được
# Chạy BÊN TRONG container incomex-agent-data qua stdin (dùng QDRANT_URL/QDRANT_API_KEY sẵn có của dịch vụ, không in):
#   ssh contabo 'timeout 120 docker exec -i incomex-agent-data python -I -B -' < c0_qdrant.py > qdrant.json
# Chỉ GET /collections, /collections/{c}, /aliases: số point, cấu hình vector (chiều/khoảng cách), TÊN khoá payload
# đã đánh chỉ mục. Không đọc vector, không đọc payload/văn bản, không scroll/search.
import json, os, urllib.request

base = (os.environ.get("QDRANT_URL") or "").rstrip("/")
hdr = {"api-key": os.environ["QDRANT_API_KEY"]} if os.environ.get("QDRANT_API_KEY") else {}
out = {"qdrant_url_configured": bool(base), "api_key_configured": bool(hdr)}


def get(path):
    req = urllib.request.Request(base + path, headers=hdr, method="GET")
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.loads(r.read().decode())


try:
    cols = [c["name"] for c in get("/collections")["result"]["collections"]]
    out["collections"] = {}
    for c in cols:
        r = get(f"/collections/{c}")["result"]
        vec = r.get("config", {}).get("params", {}).get("vectors", {})
        if "size" in vec:
            vec = {"": vec}
        out["collections"][c] = {
            "status": r.get("status"), "points_count": r.get("points_count"),
            "points_count_kind": "COLLECTION_INFO (approximate per Qdrant docs)",
            "indexed_vectors_count": r.get("indexed_vectors_count"), "segments_count": r.get("segments_count"),
            "vectors": {k: {"size": v.get("size"), "distance": v.get("distance")} for k, v in vec.items()},
            "payload_index_keys": sorted((r.get("payload_schema") or {}).keys())}
    try:
        out["aliases"] = [a["alias_name"] + "->" + a["collection_name"] for a in get("/aliases")["result"]["aliases"]]
    except Exception as e:
        out["aliases"] = f"ERR:{type(e).__name__}"
except Exception as e:
    out["error"] = type(e).__name__
print(json.dumps(out, ensure_ascii=False))
