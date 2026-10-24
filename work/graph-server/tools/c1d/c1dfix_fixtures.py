#!/usr/bin/env python3
# GS-C1D-FIX-RECOVERY-20261024-11 · LỖI GIẢ D23 «ghi tạm rồi chốt» trên Graph GIẢ có trạng thái, CÙNG hàm lõi production:
#   graph-refresh cmd_run · preconditions/recovery_ok · apply_plan (tập khô RETURN 1/0) · undo · new_recovery_point (GR.export/verify_files thật)
#   · commit/uncommit_recovery_point (renameat2 thật, thư mục tạm cùng ext4 với backups/recovery) · cmd_recovery_point; module graph-v1 THẬT
#   (INV_Q/invariants/inv_equal/rows) với http_cypher thay bằng bộ thực thi giả có giao dịch (lỗi ⇒ lùi trọn yêu cầu).
#   Chỉ thay biên ngoài: Neo4j production + Neo4j tạm (restore_check), Drive D23, apply-v0 (ghi tệp tạm), chụp nguồn/dựng kế hoạch lane,
#   Guard/Config Guard/cờ VPS-GHI/graph-v1 status, đèn #24. 0 Neo4j tạm · 0 Drive · 0 ghi production (đường production chỉ ĐỌC: module + sổ nguồn).
#   F1 lỗi sau tạo điểm tạm · F2 lỗi sau apply recovery-manifest trước chốt · F2c lỗi ngay bước chốt · F2d lỗi chép bộ nạp b88 · F3 điểm ≠ manifest
#   · F4 đường tay recovery-point · A c1d_apply gia cố. --negative: chạy F1/F2 trên graph-refresh CŨ — phải bắt được lỗi cũ (điểm ≠ PRE).
# Dùng: python3 -I c1dfix_fixtures.py <graph-refresh> <c1d_apply.py> <thư mục tạm cha ext4> [--negative] [--out F]
import copy, fcntl, hashlib, importlib.machinery, importlib.util, json, os, shutil, subprocess, sys, tempfile, time, types

GRF_P, APPLY_P, PARENT = sys.argv[1:4]
NEG = "--negative" in sys.argv
OUT = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else None
PROD = "/opt/incomex/graph-server/prod-v1"
RES = []
CERTD = tempfile.mkdtemp(prefix="c1dfix-cert-", dir=PARENT)
os.environ.update(GS_CERT_DIR=CERTD, GS_CERT_BASELINE=CERTD + "/baseline.json", GS_CERT_CELLS=PROD + "/manifest/cert-cells.json")


def load(path, name):
    ldr = importlib.machinery.SourceFileLoader(name, path)
    m = importlib.util.module_from_spec(importlib.util.spec_from_loader(name, ldr))
    ldr.exec_module(m)
    return m


def case(cid, name, ok, detail=""):
    RES.append({"id": cid, "case": name, "pass": bool(ok), "detail": str(detail)[:400]})
    print("%-5s %-78s %s %s" % (cid, name[:78], "PASS" if ok else "FAIL", str(detail)[:160]), flush=True)


sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest() if os.path.exists(p) else None


def tree_sha(d):
    if not os.path.isdir(d):
        return None
    h = hashlib.sha256()
    for n in sorted(os.listdir(d)):
        h.update(n.encode() + b"\0" + open(os.path.join(d, n), "rb").read() + b"\0")
    return h.hexdigest()


class FakeDB:
    """Graph giả có trạng thái: nút gs_key → nhãn/thuộc tính; cạnh (type, s, d). Mỗi http_cypher = MỘT giao dịch: lỗi ⇒ lùi trọn."""

    def __init__(self, G, nodes, rels):
        self.G, self.nodes, self.rels, self.writes = G, nodes, rels, 0

    def _res(self, cols, rows):
        return {"columns": cols, "data": [{"row": r} for r in rows]}

    def _q(self, q, p, st):
        n, r = st
        if q == "RETURN 1/0":
            raise ZeroDivisionError
        if q.startswith("FX_ADD "):
            a = json.loads(q[7:])
            for k, lab in a["nodes"]:
                n[k] = {"l": ["GS", lab], "p": {"gs_key": k, "layer": "fx"}}
            r.extend(tuple(x) for x in a["rels"])
            self.writes += 1
            return self._res([], [])
        if q.startswith("FX_DEL "):
            a = json.loads(q[7:])
            for x in a["rels"]:
                r.remove(tuple(x))
            for k, _ in a["nodes"]:
                n.pop(k)
            self.writes += 1
            return self._res([], [])
        GRm = GR_MOD
        if q == GRm.NQ:
            return self._res(["k", "l", "p", "ty"], [[k, v["l"], v["p"], sorted(x + ":STRING" for x in v["p"])] for k, v in n.items()])
        if q == GRm.RQ:
            return self._res(["t", "s", "d", "p", "ty"], [[t, s, d, {}, []] for t, s, d in r])
        if q.startswith("SHOW CONSTRAINTS"):
            return self._res(["name", "type", "entityType", "labelsOrTypes", "properties", "createStatement"],
                             [["gs_key_unique", "UNIQUENESS", "NODE", ["GS"], ["gs_key"], "CREATE CONSTRAINT gs_key_unique"]])
        if q.startswith("SHOW INDEXES"):
            return self._res(["name", "type", "entityType", "labelsOrTypes", "properties", "owningConstraint", "createStatement"], [])
        if q.startswith("CALL dbms.components"):
            return self._res(["name", "versions", "edition"], [["Neo4j Kernel", ["5-fx"], "community"]])
        inv = dict(self.G.INV_Q)
        if q == inv["labels"]:
            c = {}
            for v in n.values():
                for l_ in v["l"]:
                    c[l_] = c.get(l_, 0) + 1
            return self._res(["k", "v"], [[k, c[k]] for k in sorted(c)])
        if q == inv["rels"]:
            c = {}
            for t, _, _ in r:
                c[t] = c.get(t, 0) + 1
            return self._res(["k", "v"], [[k, c[k]] for k in sorted(c)])
        if q == inv["nodes"]:
            return self._res(["k", "v"], [["nodes", len(n)]])
        if q == inv["gs_nodes"]:
            return self._res(["k", "v"], [["gs", sum(1 for v in n.values() if "GS" in v["l"])]])
        if q == inv["gs_keys"]:
            return self._res(["k", "v"], [["gs_keys", sorted(k for k, v in n.items() if "GS" in v["l"])]])
        if q == inv["edges"]:
            return self._res(["k", "v"], [["edges", sorted("%s|%s|%s" % e for e in r)]])
        raise ValueError("FX câu Cypher lạ: " + q[:60])

    def http_cypher(self, stmts, pw, timeout=0):
        st = (copy.deepcopy(self.nodes), list(self.rels))
        results = []
        for q, p in stmts:
            try:
                results.append(self._q(q, p, st))
            except ZeroDivisionError:
                return {"results": results, "errors": [{"code": "Neo.ClientError.Statement.ArithmeticError", "message": "/ by zero"}]}
        self.nodes, self.rels = st
        return {"results": results, "errors": []}


GR_MOD = None


def env(tag, grf=GRF_P):
    """Môi trường cô lập: graph-refresh nạp mới · đường dẫn → thư mục tạm · Graph giả PRE · điểm khôi phục PRE xuất THẬT bằng GR.export."""
    global GR_MOD
    T = tempfile.mkdtemp(prefix="c1dfix-%s-" % tag, dir=PARENT)
    RF = load(grf, "grf_fx_" + tag.replace("-", "_"))
    GR_MOD = RF.GR
    G = RF.r7_g1lib.load(PROD + "/bin/graph-v1")          # module graph-v1 THẬT (chỉ nạp, không gọi đường mạng/container)
    nodes = {"fx:t%02d" % i: {"l": ["GS", "PgTable"], "p": {"gs_key": "fx:t%02d" % i, "layer": "fx"}} for i in range(12)}
    rels = [("HAS_FK", "fx:t%02d" % i, "fx:t%02d" % (i + 1)) for i in range(11)]
    db = FakeDB(G, nodes, rels)
    G.http_cypher = db.http_cypher
    G.password = lambda: ""
    RF.r7_g1lib.load = lambda path=None: G
    os.makedirs(T + "/manifest"); os.makedirs(T + "/state"); os.makedirs(T + "/loaded/pgl1"); os.makedirs(T + "/loaded/b88")
    RF.ROOT = T
    RF.INV, RF.PINS, RF.SOURCES, RF.RECMAN = (T + "/manifest/" + x for x in ("graph-invariants.json", "pins.json", "refresh-sources.json", "recovery-manifest.json"))
    RF.STATE, RF.LOADED, RF.LOG, RF.LOCK, RF.STOPF = T + "/state", T + "/loaded", T + "/log.jsonl", T + "/lock", T + "/state/STOP"
    RF.PGL1_CROSS = T + "/loaded/pgl1/cross-edges.json"
    RF.REC_ROOT, RF.REC_CUR = T + "/recovery", T + "/recovery/current"
    open(T + "/loaded/b88/b88_company.csv", "w").write("PRE\n")
    os.makedirs(RF.REC_ROOT, mode=0o700)
    meta = RF.GR.export(RF.REC_CUR, "fx-pre", G, "")            # điểm khôi phục PRE xuất THẬT từ Graph giả
    json.dump({"run": "FX-PRE", **G.invariants(""), "computed_at": "fx"}, open(RF.INV, "w"), indent=1, sort_keys=True)
    json.dump({"files": {RF.INV: sha(RF.INV)}, "pinned_at": "fx", "run": "FX-PRE"}, open(RF.PINS, "w"), indent=1, sort_keys=True)
    shutil.copyfile(PROD + "/manifest/refresh-sources.json", RF.SOURCES)
    json.dump({"format": "graph-recovery-manifest-v1", "current": {"name": "fx-pre", "meta_sha256": sha(RF.REC_CUR + "/meta.json"),
               "state": meta["state"], "kind": "LOGICAL_RESTORE_PASS"}, "previous": None}, open(RF.RECMAN, "w"), indent=1, sort_keys=True)
    json.dump({"edges": [["fx-pre"]]}, open(RF.PGL1_CROSS, "w"))
    open(T + "/g1-status", "w").write("#!/bin/sh\necho '{}'\n"); os.chmod(T + "/g1-status", 0o755)
    RF.G1 = T + "/g1-status"
    calls, fault = [], {}
    srcs0 = json.load(open(RF.SOURCES))
    RF.vps_ghi_state = lambda: {"ok": True, "free": True, "fetch_age_s": 1, "why": None}
    RF.guard_state = lambda: {"ok": True, "verdict": "UP OK fx"}
    RF.config_guard_clean = lambda: True
    RF.other_writers = lambda: []
    RF.term_to_fail = lambda: None
    RF.cap_b88 = lambda w: {"csv_sha256": ({"b88_company.csv": "fx-new"} if fault.get("lane") == "b88" else srcs0["b88"]["csv_sha256"]),
                            "snapshot_utc": "fx", "input_dir": T + "/b88-new"}
    os.makedirs(T + "/b88-new"); open(T + "/b88-new/b88_company.csv", "w").write("NEW\n")
    RF.cap_pgdot = lambda w: {"expected_sha256": srcs0["pgdot"]["expected_sha256"], "q_dot_identical": True, "snapshot_utc": {}, "input_dir": w}
    RF.cap_code = lambda w, s_: {}
    pl = {"empty": False, "problems": [], "counts": {"nodes_add": 2, "edges_add": 2, "nodes_set": 0, "edges_set": 0, "stale_nodes": 0, "stale_edges": 0},
          "cap_bound_partial": False, "sha256": "fx-s1", "ident_sha256": "fx-i1", "F": [], "I": []}
    RF.cap_c1d = lambda g, pw, s_, c_, lanes=RF.C1D_LANES: {l: dict(pl) for l in lanes if fault.get("lane", "c1d:pgl1") == l}

    def plan(lane, *a, **k):
        add = {"nodes": [["fx:n1", "PgTable"], ["fx:n2", "PgTable"]], "rels": [["HAS_FK", "fx:t00", "fx:n1"], ["HAS_FK", "fx:n1", "fx:n2"]]}
        pre_h = RF.full_hash(G, "")
        sim = FakeDB(G, copy.deepcopy(db.nodes), list(db.rels))
        G.http_cypher = sim.http_cypher
        sim.http_cypher([("FX_ADD " + json.dumps(add), {})], "")
        new_h, new_inv = RF.full_hash(G, ""), G.invariants("")
        G.http_cypher = db.http_cypher
        calls.append("plan:" + lane)
        return {"lane": lane, "F": [("FX_ADD " + json.dumps(add), {})], "I": [("FX_DEL " + json.dumps(add), {})], "pre_hash": pre_h,
                "new_hash": new_h, "new_inv": new_inv, "stage_new": None, "stage_old": None, "plan_sha256": "fx-p1", "counts": pl["counts"]}
    RF.build_c1d_lane = lambda lane, pl_, work, report, expect=None: plan(lane)
    RF.build_csv_lane = lambda lane, *a, **k: plan(lane)

    def restore_check(d, run_label="manual", extra=None):          # biên Neo4j tạm: kiểm tệp + trạng thái = Graph hiện tại
        meta, bad = RF.GR.verify_files(d)
        calls.append("restore_check")
        if fault.get("at") == "restore_check":
            return {"ok": False, "why": "fx nạp lại lệch"}
        ok = not bad and meta["state"] == RF.full_hash(G, "")
        return {"ok": ok, "state_equal": ok, "invariants_diff": [], "schema": {}, "cleanup": {"gone": True}, "why": None if ok else "fx lệch"}
    RF.GR.restore_check = restore_check

    def drive(export_dir, name, report):
        calls.append("drive")
        if fault.get("at") == "drive":
            raise RF.Fail("fx Drive rclone copyto rc=1")
        report.update(drive={"id": "fx-" + name, "remote": "fx:" + name}, ct_sha256="fx", decrypt_verify=True)
        return report
    RF.drive_roundtrip = drive

    def fake_v0(target, live, cand_obj, mid, raw_bytes=None):
        calls.append("apply_v0:" + target + (":raw" if raw_bytes is not None else ""))
        if fault.get("at") == "v0:" + target and raw_bytes is None:
            return False, "RESULT=REJECTED REASON=fx"
        if raw_bytes is not None:
            open(live, "wb").write(raw_bytes)
        else:
            with open(live, "w") as f:
                json.dump(cand_obj, f, indent=1, sort_keys=True, ensure_ascii=False)
        return True, "RESULT=APPLIED"
    RF.apply_v0 = fake_v0

    def cross(g, pw):
        calls.append("cross")
        if fault.get("at") == "cross":
            raise RF.Fail("fx cross-edges lỗi (sau recovery-manifest, trước chốt)")
        return {"edges": sorted([list(e) for e in db.rels])}
    RF.pgl1_cross_from = cross
    shp = types.ModuleType("shutil_fx")                      # bản sao shutil CHỈ cho graph-refresh giả này (tiêm lỗi chép bộ nạp)
    shp.__dict__.update(shutil.__dict__)

    def ct(src, dst, *a, **k):
        if fault.get("at") == "loaded_copy" and dst.startswith(RF.LOADED):
            calls.append("loaded_copy_fail")
            shutil.copytree(src, dst, *a, **k)
            open(dst + "/half", "w").write("x")
            raise OSError(28, "fx ENOSPC khi chép bộ nạp")
        return shutil.copytree(src, dst, *a, **k)
    shp.copytree = ct
    RF.shutil = shp
    RF.l2_tick = lambda rec: None
    ticks = []

    def tick(rec, *a, **k):
        st = RF.GC.alarm(None, k.get("op_failure"), baseline={}, prev_open={})[0]
        ticks.append({"op_failure": k.get("op_failure"), "status": st})
        return {}
    RF.cert_tick = tick
    if "rec_exchange" in vars(RF):
        real_x = RF.rec_exchange

        def xch(a, b):
            calls.append("exchange")
            if fault.get("at") == "exchange" and not fault.get("_fired"):
                fault["_fired"] = True
                raise OSError(5, "fx renameat2 EIO")
            return real_x(a, b)
        RF.rec_exchange = xch
    return types.SimpleNamespace(T=T, RF=RF, G=G, db=db, calls=calls, fault=fault, ticks=ticks)


def snap(e):
    RF = e.RF
    return {"graph": RF.full_hash(e.G, ""), "inv": sha(RF.INV), "pins": sha(RF.PINS), "sources": sha(RF.SOURCES), "recman": sha(RF.RECMAN),
            "cross": sha(RF.PGL1_CROSS), "active": tree_sha(RF.REC_CUR), "loaded_b88": tree_sha(RF.LOADED + "/b88")}


def extras(e):
    RF = e.RF
    stg = sorted(x for x in os.listdir(RF.REC_ROOT) if x != "current")
    lf = open(RF.LOCK, "a+")
    try:
        fcntl.flock(lf, fcntl.LOCK_EX | fcntl.LOCK_NB); fcntl.flock(lf, fcntl.LOCK_UN); free = True
    except OSError:
        free = False
    lf.close()
    return {"staging": stg, "lock_free": free, "recovery_ok": RF.recovery_ok()["ok"], "loaded_old": os.path.exists(RF.LOADED + "/b88.old")}


def run(e, trigger="manual", only="c1d:pgl1"):
    rc = e.RF.cmd_run(types.SimpleNamespace(execute=True, trigger=trigger, only=only))
    return rc, json.load(open(e.RF.STATE + "/last.json"))


def consistent_new(e, pre):
    rm = json.load(open(e.RF.RECMAN))
    return rm["current"]["meta_sha256"] == sha(e.RF.REC_CUR + "/meta.json") and rm["current"]["state"] == e.RF.full_hash(e.G, "") \
        and rm["current"]["state"] != json.loads(json.dumps(pre["graph"])) and (rm.get("previous") or {}).get("name") == "fx-pre"


def fault_case(cid, name, fault, only="c1d:pgl1", grf=GRF_P, neg=False):
    e = env(cid.lower(), grf)
    e.fault.update(fault)
    pre = snap(e)
    rc, last = run(e, only=only)
    post, ex = snap(e), extras(e)
    diff = [k for k in pre if pre[k] != post[k]]
    if neg:                                   # graph-refresh CŨ: phải lộ lỗi cũ (điểm khôi phục ≠ PRE ⇒ ≠ manifest)
        case(cid, name, last.get("result") == "FAIL" and "active" in diff and not ex["recovery_ok"],
             {"rc": rc, "diff": diff, "recovery_ok": ex["recovery_ok"], "why": last.get("why")})
        shutil.rmtree(e.T, ignore_errors=True)
        return
    ok1 = last.get("result") == "FAIL" and rc == 1 and not diff and not ex["staging"] and ex["lock_free"] and ex["recovery_ok"] and not ex["loaded_old"] \
        and (last.get("rollback") or {}).get("recovery_eq_manifest") is True and e.fault.get("at") is not None
    case(cid, name + " ⇒ 7 nhóm (+bộ nạp) byte PRE · 0 bản tạm · khoá nhả", ok1,
         {"rc": rc, "why": (last.get("why") or "")[:90], "diff": diff, "x": ex, "rbp": last.get("recovery_rollback"),
          "rb_keys": sorted((last.get("rollback") or {}).keys())})
    e.fault.clear()
    time.sleep(1.1)                           # runs/<giây> + tên điểm khôi phục theo giây: lượt kế phải khác giây
    if only == "b88":
        e.fault["lane"] = "b88"
    rc2, last2 = run(e, only=only)
    ex2 = extras(e)
    case(cid + "+", "lượt kế tiếp tự chạy KHÔNG cần người: DELTA_APPLIED · điểm = manifest = Graph mới · 0 bản tạm",
         rc2 == 0 and last2.get("result") == "DELTA_APPLIED" and consistent_new(e, pre) and not ex2["staging"] and ex2["lock_free"] and ex2["recovery_ok"]
         and not ex2["loaded_old"] and (only != "b88" or open(e.RF.LOADED + "/b88/b88_company.csv").read() == "NEW\n"),
         {"rc": rc2, "res": last2.get("result"), "why": last2.get("why"), "x": ex2})
    shutil.rmtree(e.T, ignore_errors=True)


try:
    if NEG:
        fault_case("N1", "CŨ · F1 lỗi sau tạo điểm khôi phục (sources từ chối)", {"at": "v0:graph-refresh-sources"}, neg=True)
        fault_case("N2", "CŨ · F2 lỗi sau recovery-manifest trước cross-edges", {"at": "cross"}, neg=True)
    else:
        # P0 đường thường
        e = env("p0")
        pre = snap(e)
        rc, last = run(e)
        ex = extras(e)
        case("P0", "đường thường: DELTA_APPLIED · manifest trỏ điểm mới · điểm = Graph mới · previous = PRE · 0 bản tạm · khoá nhả",
             rc == 0 and last.get("result") == "DELTA_APPLIED" and consistent_new(e, pre) and not ex["staging"] and ex["lock_free"]
             and sha(e.RF.PGL1_CROSS) != pre["cross"] and e.calls.index("exchange") > e.calls.index("apply_v0:graph-recovery-manifest")
             and e.calls.index("exchange") > e.calls.index("cross"),
             {"rc": rc, "res": last.get("result"), "x": ex, "order": [c for c in e.calls if c.startswith(("apply_v0", "exchange", "cross", "drive"))]})
        shutil.rmtree(e.T, ignore_errors=True)
        fault_case("F1", "F1 lỗi sau tạo điểm tạm (apply-v0 sources từ chối)", {"at": "v0:graph-refresh-sources"})
        fault_case("F1b", "F1b lỗi trong tạo điểm tạm (Drive D23 hỏng sau xuất)", {"at": "drive"})
        fault_case("F1c", "F1c lỗi trong tạo điểm tạm (nạp lại lệch)", {"at": "restore_check"})
        fault_case("F2", "F2 lỗi sau apply recovery-manifest, trước chốt (cross-edges)", {"at": "cross"})
        fault_case("F2c", "F2c lỗi NGAY bước chốt (renameat2 EIO)", {"at": "exchange"})
        fault_case("F2d", "F2d lỗi chép bộ nạp b88 (sau recovery-manifest, trước chốt)", {"at": "loaded_copy", "lane": "b88"}, only="b88")
        # F3 điểm khôi phục ≠ manifest từ PRE (đúng trạng thái 11:18Z): ĐỎ + 0 mutation, kể cả lượt timer
        e = env("f3")
        stray = e.T + "/stray"
        e.db.nodes["fx:stray"] = {"l": ["GS", "PgTable"], "p": {"gs_key": "fx:stray", "layer": "fx"}}
        e.RF.GR.export(stray, "fx-stray", e.G, "")
        e.db.nodes.pop("fx:stray")
        shutil.rmtree(e.RF.REC_CUR); os.rename(stray, e.RF.REC_CUR)
        pre = snap(e)
        n0 = len(e.calls)
        rc, last = run(e, trigger="timer")
        post, ex = snap(e), extras(e)
        mut = [c for c in e.calls[n0:] if c.startswith(("apply_v0", "exchange", "plan", "restore_check", "drive"))]
        case("F3", "F3 điểm ≠ manifest từ PRE (lượt timer) ⇒ SKIP_PRECONDITION recovery · đèn ĐỎ · 0 mutation · 0 bản tạm",
             last.get("result") == "SKIP_PRECONDITION" and "recovery" in (last.get("failed") or []) and pre == post and not mut
             and not ex["staging"] and ex["lock_free"] and e.ticks and e.ticks[-1]["status"] == "down" and e.db.writes == 0,
             {"rc": rc, "failed": last.get("failed"), "tick": e.ticks[-1:], "mut": mut, "x": ex})
        shutil.rmtree(e.T, ignore_errors=True)
        # F4 đường tay recovery-point: lỗi ở bước chốt ⇒ manifest + điểm byte PRE; bản thường ⇒ manifest trỏ điểm mới
        e = env("f4")
        e.db.nodes["fx:m"] = {"l": ["GS", "PgTable"], "p": {"gs_key": "fx:m", "layer": "fx"}}
        json.dump({"run": "FX-M", **e.G.invariants(""), "computed_at": "fx"}, open(e.RF.INV, "w"), indent=1, sort_keys=True)
        e.fault["at"] = "exchange"
        pre = snap(e)
        rc = e.RF.cmd_recovery_point(types.SimpleNamespace(label="fx", drive=True, out=None))
        post, ex = snap(e), extras(e)
        case("F4", "F4 recovery-point tay · lỗi ở bước chốt ⇒ manifest + điểm byte PRE · 0 bản tạm",
             rc == 1 and pre["recman"] == post["recman"] and pre["active"] == post["active"] and not ex["staging"],
             {"rc": rc, "x": ex, "diff": [k for k in pre if pre[k] != post[k]]})
        e.fault.clear()
        time.sleep(1.1)
        rc = e.RF.cmd_recovery_point(types.SimpleNamespace(label="fx", drive=True, out=None))
        ex = extras(e)
        rm = json.load(open(e.RF.RECMAN))
        case("F4+", "F4 recovery-point tay thường ⇒ manifest trỏ điểm mới = Graph · previous = PRE · 0 bản tạm",
             rc == 0 and ex["recovery_ok"] and not ex["staging"] and rm["current"]["state"] == e.RF.full_hash(e.G, "")
             and (rm.get("previous") or {}).get("name") == "fx-pre", {"rc": rc, "x": ex})
        shutil.rmtree(e.T, ignore_errors=True)
        # A — c1d_apply gia cố (cờ VPS-GHI): chủ cờ đúng tên · clone ≤ 5′ · đọc lại mỗi lần
        AP = load(APPLY_P, "c1d_apply_fx")
        RUN = "GS-C1D-FIX-RECOVERY-20261024-11"
        C = tempfile.mkdtemp(prefix="c1dfix-clone-", dir=PARENT)
        os.makedirs(C + "/.git")

        def clone(line, age):
            open(C + "/COLLAB.md", "w").write("# COLLAB\n" + line + "\n")
            open(C + "/.git/FETCH_HEAD", "w").write("x\n")
            t = time.time() - age
            os.utime(C + "/.git/FETCH_HEAD", (t, t))
        free_l = "- **VPS-GHI: trống** · %s trả cờ 2026-10-24T05:00Z" % RUN
        other_l = "- **VPS-GHI: GIỮ — HJW-OTHER-20261024-02** (lấy 05:10Z) · trước đó: trống · %s trả cờ 05:00Z" % RUN
        mine_l = "- **VPS-GHI: GIỮ — %s** (graph-server, Claude Code CLI, lấy 05:20Z)" % RUN
        clone(free_l, 10); a1 = AP.flag(C, RUN)
        clone(other_l, 10); a2 = AP.flag(C, RUN)
        old_rule = RUN in other_l and not other_l.startswith("- **VPS-GHI: trống**")     # luật cũ c1d_apply (RUN in line)
        clone(mine_l, 301); a3 = AP.flag(C, RUN)
        clone(mine_l, 10); a4 = AP.flag(C, RUN)
        clone(other_l, 10); a5 = AP.flag(C, RUN)
        case("A1", "cờ trống (dù lịch sử chứa RUN) ⇒ KHÔNG ghi", not a1["ok"] and a1["free"], a1["why"])
        case("A2", "cờ do RUN khác giữ, lịch sử «trước đó» chứa RUN này ⇒ KHÔNG ghi (luật cũ cho qua)", not a2["ok"] and old_rule, (a2["why"], "luật cũ ok=%s" % old_rule))
        case("A3", "cờ của RUN nhưng clone cổng cũ 301 s > 300 s ⇒ KHÔNG ghi", not a3["ok"] and "cũ" in (a3["why"] or ""), a3["why"])
        case("A4", "cờ của RUN + clone tươi ⇒ cho ghi", a4["ok"] and a4["holder"] == RUN, a4)
        case("A5", "đọc LẠI mỗi lần: cờ đổi chủ giữa tiền điều kiện và ngay-trước-ghi ⇒ lần sau KHÔNG ghi", a4["ok"] and not a5["ok"], a5["why"])
        shutil.rmtree(C, ignore_errors=True)
        p = subprocess.run([sys.executable, "-I", APPLY_P, "FX-NOT-THE-HOLDER-20261024-00", "c1d:pgl1", "/dev/null"], capture_output=True, timeout=300)
        o = (p.stdout + p.stderr).decode(errors="replace")
        case("A6", "c1d_apply thật trên VPS với RUN không giữ cờ ⇒ rc 3 DỪNG trước cmd_run (0 ghi)", p.returncode == 3 and "C1D_APPLY STOP" in o, o.strip()[-160:])
finally:
    for d in os.listdir(PARENT):
        if d.startswith("c1dfix-"):
            shutil.rmtree(os.path.join(PARENT, d), ignore_errors=True)

summ = {"total": len(RES), "pass": sum(r["pass"] for r in RES), "fail": [r["id"] for r in RES if not r["pass"]], "negative": NEG,
        "graph_refresh_sha256": hashlib.sha256(open(GRF_P, "rb").read()).hexdigest(), "c1d_apply_sha256": hashlib.sha256(open(APPLY_P, "rb").read()).hexdigest(),
        "leftover": [d for d in os.listdir(PARENT) if d.startswith("c1dfix-")]}
print("C1DFIX FIXTURES %s" % json.dumps(summ, ensure_ascii=False))
if OUT:
    json.dump({"summary": summ, "cases": RES}, open(OUT, "w"), ensure_ascii=False, indent=1)
sys.exit(0 if not summ["fail"] else 1)
