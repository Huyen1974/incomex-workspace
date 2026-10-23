# GS-C1C · lỗi giả cô lập: Neo4j TẠM rỗng (cùng image production), kiểm hàng rào phiên bản = bookmark HTTP (chuỗi mờ, so bằng nhau)
# + lastStartTime. Không chạm Neo4j production. Mật khẩu tạm sinh ngẫu nhiên trong bộ nhớ, không in. Dọn container + volume ẩn danh khi xong.
# BẪY ĐÃ GẶP (23/10 04:29Z): `docker rm -f` KHÔNG kèm -v để lại 2 volume ẩn danh (/data 517 MB + /logs) ⇒ đèn #11 DISK EVENT_UNDECLARED đỏ; đã gỡ tay 05:14Z ⇒ nay dùng `rm -f -v`.
import base64, json, secrets, subprocess, sys, time, urllib.request
IMG = "neo4j@sha256:d9cfe82983d27f5a75b3aaae8f316d04f9a698a3b7f6103a508f7caf8362f255"
NAME, PORT = "gs-c1c-fence-probe", 27474
pw = secrets.token_hex(16)
def sh(*a, t=120):
    p = subprocess.run(list(a), capture_output=True, timeout=t); return p.returncode, p.stdout.decode(errors="replace"), p.stderr.decode(errors="replace")
def q(db, stmts):
    body = json.dumps({"statements": [{"statement": s} for s in stmts]}).encode()
    req = urllib.request.Request("http://127.0.0.1:%d/db/%s/tx/commit" % (PORT, db), data=body, method="POST", headers={
        "Content-Type": "application/json", "Accept": "application/json;charset=UTF-8",
        "Authorization": "Basic " + base64.b64encode(("neo4j:" + pw).encode()).decode()})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)
def bm():
    d = q("neo4j", ["RETURN 1 AS x"]); return (d.get("lastBookmarks") or [None])[0]
def start():
    d = q("system", ["SHOW DATABASE neo4j YIELD lastStartTime, databaseID"]); return d["results"][0]["data"][0]["row"]
def wait():
    for _ in range(90):
        try:
            bm(); return True
        except Exception:
            time.sleep(2)
    return False
out = {}
sh("docker", "rm", "-f", "-v", NAME)
rc, o, e = sh("docker", "run", "-d", "--name", NAME, "-p", "127.0.0.1:%d:7474" % PORT, "--memory", "900m",
              "-e", "NEO4J_AUTH=neo4j/" + pw, "-e", "NEO4J_server_memory_heap_max__size=256m", "-e", "NEO4J_server_memory_heap_initial__size=128m",
              "-e", "NEO4J_server_memory_pagecache_size=32m", "-e", "NEO4J_PLUGINS=[]", IMG)
out["run_rc"] = rc
try:
    out["ready"] = wait()
    b0 = bm(); s0 = start()
    reads = [bm() for _ in range(5)]
    out["T1_reads_stable"] = all(x == b0 for x in reads)
    q("neo4j", ["CREATE (:T {id:'a'})"]); b1 = bm()
    out["T2_write_changes_bookmark"] = b1 != b0
    out["T3_reads_after_write_stable"] = all(bm() == b1 for _ in range(3))
    d = q("neo4j", ["CREATE (:T {id:'b'})", "RETURN 1/0"]); b2 = bm()
    out["T4_failed_tx_errors"] = bool(d.get("errors"))
    out["T4_failed_tx_bookmark_unchanged"] = b2 == b1
    out["T4_failed_tx_rolled_back"] = q("neo4j", ["MATCH (t:T {id:'b'}) RETURN count(t) AS c"])["results"][0]["data"][0]["row"][0] == 0
    q("neo4j", ["MATCH (t:T {id:'a'}) SET t.id = 'a2'"]); b3 = bm()
    out["T5_property_only_change_bookmark"] = b3 != b1
    q("neo4j", ["MATCH (t:T) RETURN count(t)"]); out["T6_read_tx_no_change"] = bm() == b3
    rc, _, _ = sh("docker", "restart", NAME, t=180); wait()
    b4 = bm(); s1 = start()
    out["T7_restart_bookmark_equal"] = b4 == b3
    out["T7_restart_laststart_changed"] = s1[0] != s0[0]
    out["T7_databaseID_same"] = s1[1] == s0[1]
    out["bookmark_prefix"] = (b0 or "")[:3]
finally:
    sh("docker", "rm", "-f", "-v", NAME)
    out["cleanup_gone"] = sh("docker", "ps", "-a", "--filter", "name=" + NAME, "--format", "{{.Names}}")[1].strip() == ""
print(json.dumps(out, indent=1))
