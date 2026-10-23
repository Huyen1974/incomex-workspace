# chỉ đọc: mốc phiên bản Graph production = sha256(bookmark HTTP sau một đọc) + container Id/StartedAt (không in bookmark thô)
import sys, json, hashlib, subprocess, time
sys.path.insert(0, "/opt/incomex/graph-server/prod-v1/bin/refresh")
import r7_g1lib
g = r7_g1lib.load("/opt/incomex/graph-server/prod-v1/bin/graph-v1")
pw = g.password()
bs = [ (g.http_cypher([("RETURN 1 AS x", {})], pw).get("lastBookmarks") or [None])[0] for _ in range(3)]
ins = json.loads(subprocess.run(["docker", "inspect", "incomex-graph-neo4j"], capture_output=True).stdout)[0]
inv = g.invariants(pw)
print(json.dumps({"at": time.strftime("%FT%TZ", time.gmtime()), "bookmark_sha256": [hashlib.sha256(b.encode()).hexdigest()[:16] for b in bs],
                  "container_id12": ins["Id"][:12], "started_at": ins["State"]["StartedAt"], "restarts": ins["RestartCount"],
                  "gs_keys": inv["gs_keys_count"], "gs_sha16": inv["gs_keys_sha256"][:16], "edges": inv["edges_count"], "edges_sha16": inv["edges_sha256"][:16]}))
