#!/usr/bin/env python3
# GS-C1D-NATIVE-AUTOCOVER-20261023-10 · LỖI GIẢ CÔ LẬP cho graph_cert v5 (c1d-1) + graph_autocover + graph-refresh lane c1d:
#   K3 hàng rào danh mục ô · tín hiệu thay đổi đúng hạng · kế hoạch cộng-thêm 0 xoá/trần/nghịch đảo · quyết định lane.
#   Không chạm Neo4j/PG/Directus/Qdrant/Lark production: trạng thái ở thư mục tạm, nguồn tiêm, Graph giả. Fixture KHÔNG phải lượt timer tự nhiên.
# C1-D2 (GS-C1D2-SCOPED-AUTOCOVER-20261026-13): L17 kỳ vọng theo sổ đóng băng đầu ca + đối chứng âm L17n (+4 phải FAIL).
# Dùng: python3 -I c1d_fixtures.py <graph_cert.py> <graph_autocover.py> <graph-refresh> <cert-cells c1d.json> <giấy v5 thật (chỉ đọc)> [--out F]
# SYNC-CORE (chạy được trên Mac, không cần /dev/shm hay /opt): c1d_fixtures.py --sync-core … (xem sync_core_main).
import copy, hashlib, importlib.machinery, importlib.util, json, os, re, shutil, sys, tempfile, time


# SYNC-CORE (GS-COV2-SYNC-CORE-20261031-02): 3 nhịp × 7 ca trên catalog K0 thật + đồ thị giả trong bộ nhớ; chạy đúng plan()/statements() ứng viên, oracle = k0_reconcile.py
# (parser riêng, tiến trình riêng). Kết quả tối đa FIXTURE_PASS: Cypher không chạy trên engine, nguồn đổi là đổi trên bản sao, chưa phải nhịp production.
# Dùng: python3 -I c1d_fixtures.py --sync-core <graph_autocover.py> <k0_reconcile.py> <ảnh T1> <ảnh T2> <graph.json> <gh.json> <gh-oracle.json> [--out F]
def sync_core_main(args):
    import math, resource, subprocess
    OUT_ = args[args.index("--out") + 1] if "--out" in args else None
    GA_, K0, T1, T2, GJ, GH, GHO = args[:7]
    ldr = importlib.machinery.SourceFileLoader("ga_sync", GA_)
    GA_M = importlib.util.module_from_spec(importlib.util.spec_from_loader("ga_sync", ldr))
    ldr.exec_module(GA_M)
    W = tempfile.mkdtemp(prefix="gs-sync-fx-")
    STUB = W + "/graph-stub.json"
    json.dump({"at": "stub", "nodes": [], "edges": []}, open(STUB, "w"))
    gh0, gho = json.load(open(GH)), json.load(open(GHO))
    res, t00 = [], time.time()
    LANE, NS = GA_M.NATIVE_LANE, GA_M.NS
    QUOTA = {"nodes": 200000, "edges": 200000}
    CANARY = "gh" + "p_" + "FixtureOnly" + "0123456789abcdefXYZ"

    class Mem:
        """Graph giả: chỉ hiểu đúng các mẫu Cypher ứng viên phát ra; mẫu lạ ⇒ lỗi, không bỏ qua."""
        def __init__(self, n=None, e=None):
            self.n, self.e = dict(n or {}), dict(e or {})

        def clone(self):
            return Mem(self.n, self.e)

        def rows(self, r):
            return r

        def http_cypher(self, stmts, pw, timeout=0):
            cy, p = stmts[0]
            if cy.startswith("MATCH (n:GS) WHERE n.gs_layer = $l"):
                return [{"k": k, "l": v[0], "p": v[1]} for k, v in self.n.items() if v[1].get("gs_layer") == p["l"]]
            if cy.startswith("MATCH (a:GS)-[x]->(b:GS) WHERE a.gs_layer = $l"):
                lay = lambda k: (self.n.get(k) or (0, {}))[1].get("gs_layer")
                return [{"s": k[0], "t": k[1], "d": k[2], "p": v} for k, v in self.e.items() if lay(k[0]) == p["l"] or lay(k[2]) == p["l"]]
            if cy.startswith("MATCH (n:GS) WHERE n.gs_key IN $k"):
                return [{"k": k, "l": self.n[k][0], "layer": self.n[k][1].get("gs_layer")} for k in p["k"] if k in self.n]
            raise RuntimeError("Cypher đọc lạ " + cy[:80])

        def apply(self, F):
            m = 0
            for cy, p in F:
                x = re.match(r"UNWIND \$rows AS p CREATE \(n:(.+?)\) SET n = p$", cy)
                if x:
                    for r in p["rows"]:
                        assert r["gs_key"] not in self.n, "CREATE trùng " + r["gs_key"]
                        self.n[r["gs_key"]] = (sorted(l.strip("`") for l in x.group(1).split(":")), dict(r))
                        m += 1
                    continue
                if cy == "UNWIND $rows AS r MATCH (n:GS {gs_key: r.k}) SET n = r.p":
                    for r in p["rows"]:
                        self.n[r["k"]] = (self.n[r["k"]][0], dict(r["p"]))
                        m += 1
                    continue
                if cy == "UNWIND $rows AS r MATCH (n:GS {gs_key: r.k}) SET n += r.ret":
                    for r in p["rows"]:
                        self.n[r["k"]] = (self.n[r["k"]][0], dict(self.n[r["k"]][1], **r["ret"]))
                        m += 1
                    continue
                x = re.match(r"UNWIND \$rows AS r MATCH \(a:GS \{gs_key: r\.s\}\) MATCH \(b:GS \{gs_key: r\.d\}\) CREATE \(a\)-\[x:`(.+?)`\]->\(b\) SET x = r\.p$", cy)
                if x:
                    for r in p["rows"]:
                        assert r["s"] in self.n and r["d"] in self.n, "cạnh thiếu đầu"
                        self.e[(r["s"], x.group(1), r["d"])] = dict(r["p"])
                        m += 1
                    continue
                x = re.match(r"MATCH \(a:GS \{gs_key: \$s\}\)-\[x:`(.+?)`\]->\(b:GS \{gs_key: \$d\}\) SET x = \$p$", cy)
                if x:
                    self.e[(p["s"], x.group(1), p["d"])] = dict(p["p"])
                    m += 1
                    continue
                x = re.match(r"UNWIND \$rows AS r MATCH \(a:GS \{gs_key: r\.s\}\)-\[x:`(.+?)`\]->\(b:GS \{gs_key: r\.d\}\) SET x \+= r\.ret$", cy)
                if x:
                    for r in p["rows"]:
                        k = (r["s"], x.group(1), r["d"])
                        self.e[k] = dict(self.e[k], **r["ret"])
                        m += 1
                    continue
                raise RuntimeError("Cypher ghi lạ " + cy[:90])
            return m

        def sig(self, layer=None):
            f = lambda p: layer is None or p.get("gs_layer") == layer
            live = sorted(k for k, v in self.n.items() if f(v[1]) and not GA_M.is_retired(v[1]))
            ed = sorted("|".join(k) for k, v in self.e.items() if not GA_M.is_retired(v) and (layer is None or f((self.n.get(k[0]) or (0, {}))[1])))
            return hashlib.sha256(json.dumps([live, ed]).encode()).hexdigest()[:16]

    def oracle(T, tag, gh):
        o = tempfile.mkdtemp(dir=W)
        p = subprocess.run([sys.executable, "-I", "-B", K0, T, tag, STUB, o], capture_output=True, text=True)
        if p.returncode:
            raise RuntimeError("K0 lỗi " + p.stderr[-200:])
        kn = [json.loads(l) for l in open("%s/candidate-nodes-%s.jsonl" % (o, tag))]
        ke = [json.loads(l) for l in open("%s/candidate-edges-%s.jsonl" % (o, tag))]
        s = json.load(open("%s/summary-%s.json" % (o, tag)))
        shutil.rmtree(o)
        out = {}
        fams = {GA_M.family_of(n["id"]) for n in kn} | {"pg:" + d for d in s["dbs"]} | {"directus", "cron", "systemd", "docker", "net", "nginx"}
        for f in fams:
            out[f] = {"ok": True, "why": None, "disagree": [], "ids": [], "edges": set()}
        for k, v in s["reader_errors"].items():
            if k.startswith("pg:"):
                tg = ["pg:" + k.split(":")[-1]]
            elif k.startswith("directus"):
                tg = ["directus"]
            else:
                tg = [next((f for pre, f in GA_M.RUNTIME_ERR if str(v[0]).startswith(pre)), "cron")] if v and "rc=" in str(v[0]) else ["cron", "systemd", "docker", "net", "nginx"]
            for f in tg:
                out[f].update(ok=False, why="%s %s" % (k, str(v)[:80]))
        for t in s["toc_vs_catalog"]:
            if t["n_only_cat"] or t["n_only_toc"]:
                out["pg:" + t["db"]]["disagree"].append(t["cls"])
        for n in kn:
            out[GA_M.family_of(n["id"])]["ids"].append(n["id"])
        for e in ke:
            out[GA_M.family_of(e["s"])]["edges"].add("|".join((e["s"], e["t"], e["d"])))
        bad = sorted(r["name"] for r in gh["repos"] if r.get("head") and gho.get(r["name"]) != r["head"])
        out["github"] = {"ok": not (gh.get("errors") or bad), "why": str(gh.get("errors") or bad)[:100] or None, "disagree": [], "ids": [], "edges": set()}
        return out, kn, ke, s

    def run(gg, T, tag, gh, quota=QUOTA, state=None, now=None):
        uni = GA_M.read_universe(T, tag, gh)
        orc, kn, ke, ks = oracle(T, tag, gh)
        native = {"sources": uni["sources"], "oracle": orc}
        pl = GA_M.plan(gg, "", LANE, uni["nodes"], uni["edges"], quota, native=native)
        m = gg.apply(pl["F"]) if not pl["problems"] else 0
        gn, ge = GA_M.graph_layer(gg, "", "native")
        df = GA_M.oracle_diff(kn, ke, gn, ge, [f for f in uni["sources"] if f != "github"])
        cert = GA_M.source_cert(uni, df, pl, {} if state is None else state, now or time.time(), oracle=orc)
        return {"uni": uni, "pl": pl, "applied": m, "diff": df, "cert": cert, "ks": ks}

    def fams_ok(r, fams):
        return all(r["diff"]["families"][f]["ok"] for f in fams if f in r["diff"]["families"])

    def bad_of(r):
        return {f: {k: (len(v) if isinstance(v, list) else v) for k, v in x.items() if v and k not in ("ok", "nodes", "edges")} for f, x in r["diff"]["families"].items() if not x["ok"]}

    def fresh(base, name):
        d = "%s/%s" % (W, name)
        shutil.rmtree(d, ignore_errors=True)
        shutil.copytree(base, d, ignore=shutil.ignore_patterns("*.dump", "globals*", "stat*", "*.tgz"))
        return d

    def edit(T, f, fn):
        p = T + "/" + f
        b = open(p, encoding="utf-8", errors="replace").read()
        n = fn(b)
        open(p, "w", encoding="utf-8").write(n)

    def toc_drop(T, tag, db, pat):
        def fn(b):
            ls = b.split("\n")
            kept = [l for l in ls if not (l and not l.startswith(";") and re.match(pat, l))]
            gone = len(ls) - len(kept)
            return re.sub(r"(?m)^(;\s+TOC Entries: )(\d+)$", lambda m: m.group(1) + str(int(m.group(2)) - gone), "\n".join(kept))
        edit(T, "toc-%s-%s.txt" % (tag, db), fn)

    def toc_add(T, tag, db, lines):
        edit(T, "toc-%s-%s.txt" % (tag, db), lambda b: re.sub(r"(?m)^(;\s+TOC Entries: )(\d+)$", lambda m: m.group(1) + str(int(m.group(2)) + len(lines)), b) + "\n".join(lines) + "\n")

    def views(T, tag):
        trig = set()
        out, total = [], 0
        for l in open("%s/cat-%s-directus.tsv" % (T, tag), errors="replace"):
            f = l.rstrip("\n").split("\t")
            if f[0] in ("trigger", "rule"):
                trig.add(f[2])
            if f[0] == "rel" and f[1] == "v" and f[5] == "false":
                total += 1                                  # mẫu số = mọi view của ô, không riêng schema public
                if f[2] == "public":
                    out.append(f[3])
        return sorted((v for v in out if v not in trig), key=lambda v: hashlib.sha256(v.encode()).hexdigest()), total

    def rm_views(T, tag, names, toc=True):
        s = set(names)

        def fn(b):
            keep = []
            for l in b.split("\n"):
                f = l.split("\t")
                if (f[0] == "rel" and f[1] == "v" and f[2] == "public" and f[3] in s) or (f[0] == "viewdep" and ((f[1] == "public" and f[2] in s) or (f[4] == "public" and f[5] in s))) or (f[0] == "viewfunc" and f[1] == "public" and f[2] in s):
                    continue
                keep.append(l)
            return "\n".join(keep)
        edit(T, "cat-%s-directus.tsv" % tag, fn)
        if toc:
            toc_drop(T, tag, "directus", r"^\d+;\s+\d+\s+\d+\s+VIEW public (%s) " % "|".join(map(re.escape, s)))

    def mut_add(T, tag, gh, n):
        ta, fk, fl, op = "zz_core_%d" % n, "zz_core_%d_fk" % n, "00000000-0000-4000-8000-%012d" % n, "00000000-0000-4000-9000-%012d" % n
        edit(T, "cat-%s-directus.tsv" % tag, lambda b: b.rstrip("\n") + "\nrel\tr\tpublic\t%s\towner\tfalse\tabc\t0\t1\tfalse\nfk\tpublic\t%s\t%s\tpublic\tbirth_registry\ttrue\n" % (ta, ta, fk))
        toc_add(T, tag, "directus", ["99%d1; 1259 99%d1 TABLE public %s owner" % (n, n, ta), "99%d2; 2606 99%d2 FK CONSTRAINT public %s %s owner" % (n, n, ta, fk)])
        edit(T, "dt-%s.tsv" % tag, lambda b: b.rstrip("\n") + "\ndflow\t%s\tflow %s\tactive\tevent\t\t\tabc\ndop\t%s\t%s\tlog\tk\tabc\t\t\n" % (fl, CANARY, op, fl))
        g2 = copy.deepcopy(gh)
        g2["repos"][0]["files"].append({"p": "zz/core_%d.py" % n, "h": "a" * 40})
        return g2, {NS + "pg:directus:table:public." + ta, NS + "pg:directus:fk:public.%s.%s" % (ta, fk), NS + "directus:flow:" + fl, NS + "directus:operation:" + op}, {(NS + "directus:operation:" + op, "OPERATION_OF", NS + "directus:flow:" + fl), (NS + "pg:directus:fk:public.%s.%s" % (ta, fk), "REFERENCES", NS + "pg:directus:table:public.birth_registry")}

    def mut_retarget(T, tag):
        rows = [l.split("\t") for l in open("%s/cat-%s-directus.tsv" % (T, tag), errors="replace").read().split("\n")]
        tr = next(r for r in rows if r[0] == "trigger" and r[7] == "")
        fns = [r for r in rows if r[0] == "func" and r[3] == "" and r[8] == "false" and r[2] != tr[6] and r[1] == tr[5]]
        c = fns[0]
        fk = next(r for r in rows if r[0] == "fk" and r[4] == "public" and r[5] != "birth_registry")
        edit(T, "cat-%s-directus.tsv" % tag, lambda b: b.replace("\t".join(tr), "\t".join(tr[:6] + [c[2]] + tr[7:])).replace("\t".join(fk), "\t".join(fk[:5] + ["birth_registry"] + fk[6:])))
        ti = NS + "pg:directus:trigger:%s.%s.%s" % (tr[1], tr[2], tr[3])
        fi = NS + "pg:directus:fk:%s.%s.%s" % (fk[1], fk[2], fk[3])
        return {(ti, "EXECUTES", NS + "pg:directus:function:%s.%s()" % (tr[5], tr[6])), (fi, "REFERENCES", NS + "pg:directus:table:%s.%s" % (fk[4], fk[5]))}, {(ti, "EXECUTES", NS + "pg:directus:function:%s.%s()" % (c[1], c[2])), (fi, "REFERENCES", NS + "pg:directus:table:public.birth_registry")}

    def live_e(gg, k):
        return k in gg.e and not GA_M.is_retired(gg.e[k])

    def rec(cy, cid, name, ok, detail):
        res.append({"cycle": cy, "case": cid, "name": name, "pass": bool(ok), "detail": detail})
        print("nhịp%s ca%s %-44s %s %s" % (cy, cid, name[:44], "PASS" if ok else "FAIL", str(detail)[:230]), flush=True)

    # đồ thị khởi đầu: mọi nút/cạnh production 30/10 (đọc K0, chỉ khoá+nhãn) đóng vai lane cũ — ứng viên không được chạm
    G0 = json.load(open(GJ))
    seed = Mem({n["k"]: (sorted(["GS"] + [x for x in n["l"]]), {"gs_key": n["k"], "gs_layer": n.get("layer") or "legacy"}) for n in G0["nodes"] if n.get("k")},
               {(e["s"], e["t"], e["d"]): {"legacy": True} for e in G0["edges"]})
    legacy_sig = hashlib.sha256(json.dumps([sorted((k, str(v)) for k, v in seed.n.items()), sorted("|".join(k) for k in seed.e)]).encode()).hexdigest()[:16]
    legacy_keys, legacy_edges = set(seed.n), set(seed.e)

    def legacy_same(gg):
        return all(gg.n[k][1].get("gs_layer") == seed.n[k][1].get("gs_layer") and not GA_M.is_retired(gg.n[k][1]) for k in legacy_keys) and all(k in gg.e and gg.e[k] == {"legacy": True} for k in legacy_edges)

    gg = seed.clone()
    bases = [("1", T1, "T1", "ảnh K0 T1 30/10"), ("2", T2, "T2", "ảnh K0 T2 30/10 (đổi thật T1→T2)"), ("3", T2, "T2", "T2 + đọc lại 31/10 khớp băm PG/Directus")]
    meta = []
    for cy, base, tag, label in bases:
        t0 = time.time()
        r0 = run(gg, base, tag, gh0)
        r1 = run(gg, base, tag, gh0)
        c = r0["pl"]["counts"]
        meta.append({"cycle": cy, "label": label, "plan": {k: c[k] for k in ("nodes_add", "edges_add", "nodes_set", "edges_set", "nodes_retire", "edges_retire", "edges_delete", "nodes_delete", "reused")},
                     "edges_missing_end": r0["pl"]["edges_missing_end"], "problems": r0["pl"]["problems"][:4], "held": r0["pl"]["retire_gate"]["held"] if r0["pl"]["retire_gate"] else {}, "base_oracle_bad": bad_of(r1),
                     "cert": {f: x["status"] + ("" if not x["why"] else " " + str(x["why"])[:70]) for f, x in r1["cert"]["cells"].items()},
                     "source_dangling": r1["diff"]["source_dangling_edges"], "gaps": r1["uni"]["gaps"], "legacy_untouched": legacy_same(gg), "replay_writes": r1["applied"]})
        print("NỀN nhịp", cy, json.dumps(meta[-1], ensure_ascii=False)[:1400], flush=True)
        base_sig, active = gg.sig("native"), None

        # ca 1 ADD vật/cạnh + bí mật giả trong tên flow
        T = fresh(base, "c1")
        g = gg.clone()
        gh1, add_n, add_e = mut_add(T, tag, gh0, 1)
        r = run(g, T, tag, gh1)
        ok = all(k in g.n and not GA_M.is_retired(g.n[k][1]) for k in add_n) and all(live_e(g, k) for k in add_e) and r["pl"]["counts"]["nodes_retire"] == 0
        leak = sum(CANARY in json.dumps(v[1]) for v in g.n.values())
        rec(cy, 1, "ADD vật+cạnh · bí mật giả bị che", ok and fams_ok(r, ["pg:directus", "cron", "systemd", "docker", "net", "nginx"]) and leak == 0 and legacy_same(g),
            {"add_n": r["pl"]["counts"]["nodes_add"], "add_e": r["pl"]["counts"]["edges_add"], "secret_in_graph": leak, "oracle_bad": bad_of(r)})

        # ca 2 retire 30% khi đọc đủ + oracle; đối chứng âm: chỉ catalog đổi, TOC còn ⇒ 0 gỡ; rồi vật quay lại ⇒ hồi sinh
        T = fresh(base, "c2")
        vs, nv = views(T, tag)
        k30 = math.ceil(0.30 * nv)
        rm_views(T, tag, vs[:k30])
        g = gg.clone()
        r = run(g, T, tag, gh0)
        rn = r["pl"]["counts"]["nodes_retire"]
        proof = r["pl"]["retire_gate"]["large_drop_proof"]
        Tn = fresh(base, "c2n")
        rm_views(Tn, tag, vs[:k30], toc=False)
        gn2 = gg.clone()
        rn2 = run(gn2, Tn, tag, gh0)
        back = run(g, base, tag, gh0)
        ok = rn == k30 and "pg:directus|view" in proof and r["diff"]["families"]["pg:directus"]["ok"] and rn2["pl"]["counts"]["nodes_retire"] == 0 and gg.sig("native") == gn2.sig("native") and g.sig("native") == base_sig and legacy_same(g)
        rec(cy, 2, "retire 30% có chứng minh · TOC trái ⇒ 0 · hồi sinh", ok, {"retired": rn, "of": nv, "edges_retired": r["pl"]["counts"]["edges_retire"], "proof": proof.get("pg:directus|view"), "neg_held": rn2["pl"]["retire_gate"]["held"].get("pg:directus|view"), "revive_set": back["pl"]["counts"]["nodes_set"], "oracle_bad": bad_of(r)})

        # ca 3 giảm >75% ⇒ chặn + báo, 0 gỡ; oracle thấy đúng phần lệch
        T = fresh(base, "c3")
        vs, nv = views(T, tag)
        k80 = min(math.ceil(0.80 * nv), len(vs))
        rm_views(T, tag, vs[:k80])
        g = gg.clone()
        r = run(g, T, tag, gh0)
        f = r["diff"]["families"]["pg:directus"]
        ok = r["pl"]["counts"]["nodes_retire"] == 0 and any("MASS_DROP_BLOCKED" in a for a in r["cert"]["alerts"]) and len(f["only_graph"]) == k80 and r["cert"]["cells"]["pg:directus"]["status"] == "PARTIAL"
        rec(cy, 3, "giảm >75% bị chặn và báo", ok, {"gone_at_source": k80, "of": nv, "retired": r["pl"]["counts"]["nodes_retire"], "alerts": r["cert"]["alerts"][:1], "only_graph": len(f["only_graph"]), "cert": r["cert"]["cells"]["pg:directus"]["status"]})

        # ca 4 A→B thành A→C, số cạnh giữ nguyên
        T = fresh(base, "c4")
        old, new = mut_retarget(T, tag)
        g = gg.clone()
        count0 = sum(1 for k, v in g.e.items() if k[1] in ("EXECUTES", "REFERENCES") and not GA_M.is_retired(v) and (g.n.get(k[0]) or (0, {}))[1].get("gs_layer") == "native")
        r = run(g, T, tag, gh0)
        count1 = sum(1 for k, v in g.e.items() if k[1] in ("EXECUTES", "REFERENCES") and not GA_M.is_retired(v) and (g.n.get(k[0]) or (0, {}))[1].get("gs_layer") == "native")
        ok = count0 == count1 and all(live_e(g, k) for k in new) and not any(live_e(g, k) for k in old) and all(k in g.e for k in old) and r["diff"]["families"]["pg:directus"]["ok"]
        rec(cy, 4, "đổi đích cạnh A→B→A→C, số cạnh không đổi", ok, {"edges_before": count0, "edges_after": count1, "edge_retire": r["pl"]["counts"]["edges_retire"], "edge_add": r["pl"]["counts"]["edges_add"], "oracle_bad": bad_of(r)})

        # ca 5 nguồn 403/503/timeout ⇒ MỘT PHẦN, 0 gỡ, họ khác vẫn chạy
        sub = {}
        for nm, fam, mut, gh_ in (("403 catalog", "pg:directus", lambda t: open(t + "/cat-directus.err", "w").write("ERROR: permission denied for table pg_proc\n"), gh0),
                                  ("503 Directus", "directus", lambda t: open(t + "/dt.err", "w").write("HTTP 503\n"), gh0),
                                  ("timeout cắt cụt", "pg:directus", lambda t: edit(t, "cat-%s-directus.tsv" % tag, lambda b: b[:len(b) // 2]), gh0),
                                  ("timeout docker", "docker", lambda t: edit(t, "runtime-%s.json" % tag, lambda b: json.dumps(dict(json.loads(b), errors=[{"where": "docker-ps", "rc": 124, "stderr": ""}]))), gh0),
                                  ("403 GitHub", "github", lambda t: None, dict(gh0, errors=[{"repo": "x", "where": "tree", "rc": 403}])),
                                  ("loại lạ ⇒ GAP", "pg:directus", lambda t: (edit(t, "cat-%s-directus.tsv" % tag, lambda b: b.rstrip("\n") + "\nloai_moi\tx\n"), rm_views(t, tag, views(t, tag)[0][:1])), gh0)):
            T = fresh(base, "c5")
            mut(T)
            g = gg.clone()
            before = g.sig("native")
            r = run(g, T, tag, gh_)
            cp = r["cert"]["cells"][fam]
            other_full = [f for f, x in r["cert"]["cells"].items() if x["status"] == "FULL" and f != fam]
            sub[nm] = {"retire": r["pl"]["counts"]["nodes_retire"] + r["pl"]["counts"]["edges_retire"], "cert": cp["status"], "sig_same": g.sig("native") == before}
            sub[nm]["ok"] = sub[nm]["retire"] == 0 and cp["status"] == "PARTIAL" and sub[nm]["sig_same"] and bool(other_full)
        rec(cy, 5, "403/503/timeout ⇒ PARTIAL, 0 gỡ, họ khác tiếp tục", all(x["ok"] for x in sub.values()), sub)

        # ca 6 bỏ một nhịp rồi tự bắt kịp; quota nhỏ cũng hội tụ qua nhiều lượt
        Ta = fresh(base, "c6")
        gh6, _, _ = mut_add(Ta, tag, gh0, 2)                       # nhịp bị bỏ: không chạy
        vs, nv = views(Ta, tag)
        rm_views(Ta, tag, vs[:math.ceil(0.10 * nv)])                # nhịp sau: thêm đổi nữa
        old, new = mut_retarget(Ta, tag)
        g = gg.clone()
        r = run(g, Ta, tag, gh6)
        sig_skip = g.sig("native")
        g2 = gg.clone()
        n_runs, rq = 0, None
        while n_runs < 40:
            rq = run(g2, Ta, tag, gh6, quota={"nodes": 60, "edges": 60})
            n_runs += 1
            if rq["pl"]["empty"]:
                break
        ok = r["diff"]["families"]["pg:directus"]["ok"] and all(live_e(g, k) for k in new) and sig_skip == g2.sig("native") and n_runs > 1 and rq["pl"]["quota_left"] == 0
        rec(cy, 6, "bỏ nhịp rồi bắt kịp · quota nhiều lượt cùng đích", ok, {"catch_up": {k: r["pl"]["counts"][k] for k in ("nodes_add", "edges_add", "nodes_retire", "edges_retire")}, "quota_runs": n_runs, "oracle_bad": bad_of(r), "same_sig": sig_skip == g2.sig("native")})

        # ca 7 không đổi ⇒ 0 mutation
        g = gg.clone()
        s0 = (g.sig(), len(g.n), len(g.e))
        r = run(g, fresh(base, "c7"), tag, gh0)
        ok = r["pl"]["empty"] and r["applied"] == 0 and not r["pl"]["F"] and (g.sig(), len(g.n), len(g.e)) == s0
        rec(cy, 7, "NO_CHANGE ⇒ 0 mutation", ok, {"statements": len(r["pl"]["F"]), "applied": r["applied"]})
        meta[-1]["seconds"] = round(time.time() - t0, 1)
    # đối chứng âm của chính bộ thử: oracle thấy Graph sai, bộ quét thấy bí mật giả
    g = gg.clone()
    victim = next(k for k, v in g.n.items() if v[1].get("gs_layer") == "native" and v[1].get("cls") == "table")
    del g.n[victim]
    orc, kn, ke, _ = oracle(T2, "T2", gh0)
    gn, ge = GA_M.graph_layer(g, "", "native")
    neg = GA_M.oracle_diff(kn, ke, gn, ge, [GA_M.family_of(victim)])["families"][GA_M.family_of(victim)]
    gt = {"cycle": "x", "negative_oracle_detects": victim[len(NS):] in neg["only_source"], "secret_scan_detects_canary": bool(GA_M.SECRET_RE.search(CANARY)), "human_edge": None}
    # quan hệ người duyệt không tự gỡ; R7 chỉ là thiết kế tắt mặc định
    g = gg.clone()
    hk = next(k for k in g.e if (g.n.get(k[0]) or (0, {}))[1].get("gs_layer") == "native" and k[1] == "HAS_FK")
    hk2 = (hk[0], "REFERENCES", "human:ref")
    g.n["human:ref"] = (["GS", "PgTable"], {"gs_key": "human:ref", "gs_layer": "legacy"})
    g.e[hk2] = {"family": "pg:directus", "evidence": "HUMAN", "human_approved": True}
    r = run(g, T2, "T2", gh0)
    gt["human_edge"] = {"kept": live_e(g, hk2), "hold": r["pl"]["retire_gate"]["human_hold"][:1]}
    # cổng cạnh giữ (giảm 100%) nhưng đầu nút đã gỡ đúng ⇒ cạnh vẫn gỡ theo, không để cạnh sống trỏ vào vật đã mất
    mk = lambda i: (["GS", "PgView"], {"gs_key": NS + i, "family": "pg:d", "cls": "view"})
    gn_ = {NS + "pg:d:view:%d" % i: mk("pg:d:view:%d" % i) for i in range(10)}
    ge_ = {(NS + "pg:d:view:0", "DEPENDS_ON", NS + "pg:d:view:1"): [{"family": "pg:d", "evidence": "NATIVE"}]}
    rn_, re_, _ = GA_M.retire_native(gn_, ge_, {k: 1 for k in gn_ if not k.endswith(":0")}, {}, {"sources": {"pg:d": {"status": "FULL"}}, "oracle": {"pg:d": {"ok": True}}})
    gt["endpoint_retired"] = [x["why"] for x in re_]
    # thế hệ chỉ tăng khi đạt; nguồn hỏng quá 26h kể từ lần đạt cuối ⇒ STALE, không giữ màu cũ
    uni_ = {"nodes": {}, "edges": {}, "gaps": [], "sources": {"docker": {"status": "FULL"}}}
    ok_d = {"families": {"docker": {"ok": True}}}
    st_ = {}
    a1 = GA_M.source_cert(uni_, ok_d, {}, st_, 1000)["cells"]["docker"]
    uni_["sources"]["docker"] = {"status": "PARTIAL", "why": "503"}
    a2 = GA_M.source_cert(uni_, ok_d, {}, st_, 2000)["cells"]["docker"]
    a3 = GA_M.source_cert(uni_, ok_d, {}, st_, 1000 + 27 * 3600)["cells"]["docker"]
    gt["cert_ttl"] = [(a1["status"], a1["generation"]), (a2["status"], a2["generation"]), (a3["status"], a3["generation"])]
    gt["github_derived"] = GA_M.derive_file_refs("native:github:file:r:a.py", "select * from pivot_results; # pivot_resultsX", {"pivot_results": "native:pg:directus:table:public.pivot_results", "khong_co": "x"})
    gt["r7_design"] = {"current": GA_M.gate_decision(["guard", "config_guard_clean"]), "r7_off_unrelated": GA_M.gate_decision(["guard", "config_guard_clean"], r7=True), "r7_vps_ghi": GA_M.gate_decision(["vps_ghi"], r7=True)}
    ru = resource.getrusage(resource.RUSAGE_SELF)
    rc_ = resource.getrusage(resource.RUSAGE_CHILDREN)
    total = sum(1 for x in res if x["pass"])
    rep_ = {"level": "FIXTURE_PASS" if total == len(res) == 21 and gt["negative_oracle_detects"] and gt["secret_scan_detects_canary"] and gt["human_edge"]["kept"] and len(gt["github_derived"]) == 1 and gt["endpoint_retired"] == ["ENDPOINT_RETIRED"] and gt["cert_ttl"] == [("FULL", 1), ("PARTIAL", 1), ("STALE", 1)] else "FIXTURE_FAIL",
            "pass": total, "total": len(res), "bases": meta, "cases": res, "guards": gt, "legacy_sig": legacy_sig, "seconds": round(time.time() - t00, 1),
            "cpu_user_s": round(ru.ru_utime + rc_.ru_utime, 1), "cpu_sys_s": round(ru.ru_stime + rc_.ru_stime, 1), "maxrss_mb": round(ru.ru_maxrss / 1048576, 1), "maxrss_child_mb": round(rc_.ru_maxrss / 1048576, 1)}
    print(json.dumps({k: rep_[k] for k in ("level", "pass", "total", "guards", "seconds", "cpu_user_s", "cpu_sys_s", "maxrss_mb", "maxrss_child_mb")}, ensure_ascii=False))
    if OUT_:
        json.dump(rep_, open(OUT_, "w"), ensure_ascii=False, indent=1, default=str)
    shutil.rmtree(W, ignore_errors=True)
    return 0 if rep_["level"] == "FIXTURE_PASS" else 1


if len(sys.argv) > 1 and sys.argv[1] == "--sync-core":
    sys.exit(sync_core_main(sys.argv[2:]))

CAND, GA_P, GRF_P, CELLS_P, DOC_P = sys.argv[1:6]
OUT = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else None
TMP = tempfile.mkdtemp(prefix="gs-c1d-fx-", dir="/dev/shm")
CELLS = TMP + "/cells.json"
shutil.copyfile(CELLS_P, CELLS)
os.makedirs(TMP + "/cert")
os.environ.update(GS_CERT_CELLS=CELLS, GS_CERT_DIR=TMP + "/cert", GS_CERT_BASELINE=TMP + "/baseline.json")
json.dump({"certified_floor": ["pg:directus:trigger"], "accepted_partial": {}}, open(TMP + "/baseline.json", "w"))
shutil.copyfile("/opt/incomex/graph-server/prod-v1/state/refresh/cert/l2-candidates.json", TMP + "/cert/l2-candidates.json")


def load(path, name):
    ldr = importlib.machinery.SourceFileLoader(name, path)
    m = importlib.util.module_from_spec(importlib.util.spec_from_loader(name, ldr))
    ldr.exec_module(m)
    return m


G = load(CAND, "graph_cert_c1d_fx")
GA = load(GA_P, "graph_autocover_fx")
DU, MP = G.DU, G.MP
RES = []


def case(group, cid, name, ok, detail=""):
    RES.append({"group": group, "id": cid, "case": name, "pass": bool(ok), "detail": str(detail)[:300]})
    print("%-3s %-6s %-70s %s %s" % (group, cid, name[:70], "PASS" if ok else "FAIL", str(detail)[:140]), flush=True)


def sign(d):
    d.pop("self_sha256", None)
    d["self_sha256"] = G.self_sha(d)
    return d


SHA = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()
BASE = json.load(open(DOC_P))
SHIFT = 0
NOW = G.parse_iso(BASE["generated_at"]) + 600
EP = dict(BASE["graph_epoch"])
live_ok = lambda: dict(EP)
IUQ = "MATCH (g:PgTrigger)-[:ON_TABLE]->(:PgTable {id: 'public.information_unit'}) RETURN g.id AS x"
TRQ = "MATCH (g:PgTrigger)-[:ON_TABLE]->(t:PgTable) RETURN count(g) AS c"


def doc0():
    d = copy.deepcopy(BASE)
    d["catalog_sha256"] = SHA(CELLS)
    d["engine_sha256"], d["engine_version"] = G._SELF_SHA, G.ENGINE_VERSION    # giấy do CHÍNH bộ máy ứng viên cấp (đúng như lượt thật)
    return sign(d)


def lab(q, doc, rows=7, cat=None, live=live_ok):
    return G.label_for("read-cypher", {"query": q, "params": {}}, rows, NOW, doc, cat, live, False)


def write_cells(mut=None, raw=None):
    if raw is not None:
        open(CELLS, "wb").write(raw)
        return
    c = json.load(open(CELLS_P))
    if mut:
        mut(c)
    json.dump(c, open(CELLS, "w", encoding="utf-8"), ensure_ascii=False, indent=1, sort_keys=True)


def reset():
    shutil.copyfile(CELLS_P, CELLS)


try:
    # =========================================================================== K3
    d = doc0()
    a, b = lab(IUQ, d), lab(TRQ, d)
    case("K3", "P1", "danh mục sống = danh mục giấy + định nghĩa ô khớp + K1 MATCH ⇒ L1/ô ĐỦ", a["completeness_label"] == DU and b["completeness_label"] == DU
         and a["catalog_revision"]["status"] == "MATCH", (a["completeness_label"], b["completeness_label"], a["catalog_revision"]))

    def cell(c, k):
        return next(x for x in c["cells"] if x["key"] == k)
    write_cells(lambda c: cell(c, "pg:directus:trigger")["graph"]["edges"].append({"type": "NEW_REL", "from": "PgTrigger", "to": "PgTable", "prov": ["trust"]}))
    b = lab(TRQ, d)
    case("K3", "N1a", "cùng khoá ô + thêm loại quan hệ mới (danh mục đổi, chưa cấp lại) ⇒ MỘT PHẦN CATALOG_CHANGED_SINCE_CERT",
         b["completeness_label"] == MP and "CATALOG_CHANGED_SINCE_CERT" in b["reason"] and b["query_actionability"] == G.ACT_NO, b["reason"][:120])
    d2 = copy.deepcopy(d)
    d2["catalog_sha256"] = SHA(CELLS)                  # giấy mang băm danh mục mới nhưng ô KHÔNG cấp lại (vd lượt --cells cũ) ⇒ định nghĩa ô lệch
    sign(d2)
    b = lab(TRQ, d2)
    case("K3", "N1b", "băm danh mục trùng nhưng định nghĩa ô đổi dưới cùng khoá ⇒ MỘT PHẦN (cell_def_sha256)",
         b["completeness_label"] == MP and "định nghĩa ô đổi" in b["reason"], b["reason"][:120])
    reset()
    write_cells(lambda c: cell(c, "pg:directus:trigger").update(scope=cell(c, "pg:directus:trigger")["scope"] + " · mở rộng"))
    b = lab(TRQ, d)
    case("K3", "N2", "cùng số ô, phạm vi ô khác ⇒ MỘT PHẦN", b["completeness_label"] == MP and "CATALOG_CHANGED" in b["reason"], b["reason"][:100])
    reset()
    write_cells(lambda c: c["l1_pilot"].update(tables=list(c["l1_pilot"]["tables"])[:-1] + ["directus.public.directus_users"]))
    a = lab(IUQ, d)
    case("K3", "N2b", "cùng 11 bảng mẫu nhưng đổi một bảng (cùng số, khác phạm vi) ⇒ MỘT PHẦN", a["completeness_label"] == MP, a["reason"][:100])
    reset()
    write_cells(raw=open(CELLS_P, "rb").read() + b"\n")
    b = lab(TRQ, d)
    case("K3", "N3", "byte danh mục đổi sau khi cấp giấy (chỉ thêm khoảng trắng) ⇒ MỘT PHẦN", b["completeness_label"] == MP and "CATALOG_CHANGED_SINCE_CERT" in b["reason"],
         b["reason"][:100])
    st, msg, inc = G.alarm(d, now=NOW, baseline={"certified_floor": ["pg:directus:trigger"], "accepted_partial": {}})
    case("K3", "N4", "apply danh mục rồi sập trước cấp lại ⇒ ô sàn tụt ⇒ đèn ĐỎ COVERAGE_REGRESSION", st == "down" and "COVERAGE_REGRESSION" in msg, msg[:120])
    reset()
    os.remove(CELLS)
    b = lab(TRQ, d)
    e, why = G.effective(d, NOW)
    case("K3", "N5", "danh mục vắng ⇒ nhãn MỘT PHẦN + mọi ô MỘT PHẦN", b["completeness_label"] == MP and all(v[0] == MP for v in e.values()), b["reason"][:100])
    write_cells(raw=b"{not json")
    b = lab(TRQ, d)
    case("K3", "N5b", "danh mục hỏng (JSON sai) ⇒ MỘT PHẦN CATALOG_VERSION_UNVERIFIED", b["completeness_label"] == MP and "CATALOG" in b["reason"], b["reason"][:100])
    reset()
    d3 = copy.deepcopy(d)
    d3["catalog_sha256"] = "zz"
    sign(d3)
    b = lab(TRQ, d3)
    case("K3", "N6a", "catalog_sha256 trong giấy hỏng (đã ký lại) ⇒ MỘT PHẦN CATALOG_VERSION_UNVERIFIED", b["completeness_label"] == MP and "CATALOG_VERSION_UNVERIFIED" in b["reason"],
         b["reason"][:100])
    d3 = copy.deepcopy(d)
    d3["catalog_sha256"] = "0" * 64                    # sửa không ký lại
    b = lab(TRQ, d3)
    case("K3", "N6b", "sửa catalog_sha256 không ký lại ⇒ MANIFEST_CORRUPT_SELF_SHA256", b["completeness_label"] == MP and "CORRUPT" in b["reason"], b["reason"][:100])
    d4 = copy.deepcopy(d)
    d4["engine_sha256"] = "f9c571f1237e65c163e63c4d246fe313a48a3a9551174cbce3ae06db28d74353"   # bộ máy v4 cũ
    sign(d4)
    b = lab(TRQ, d4)
    case("K3", "N7", "giấy do bộ máy cũ cấp (cache engine cũ) ⇒ MỘT PHẦN ENGINE_CHANGED_SINCE_CERT", b["completeness_label"] == MP and "ENGINE_CHANGED_SINCE_CERT" in b["reason"],
         b["reason"][:120])
    chg = lambda: dict(EP, bookmark_sha256="b" * 64)
    b = lab(TRQ, d, live=chg)
    case("K3", "N8", "Graph đổi so với giấy (K1) vẫn chặn khi danh mục khớp ⇒ MỘT PHẦN GRAPH_CHANGED_SINCE_CERT", b["completeness_label"] == MP and "GRAPH_CHANGED_SINCE_CERT" in b["reason"],
         b["reason"][:100])
    d5 = copy.deepcopy(d)
    for c in d5["cells"].values():
        c.pop("cell_def_sha256", None)
    sign(d5)
    b = lab(TRQ, d5)
    case("K3", "N9", "giấy trước K3 (ô không có cell_def_sha256) ⇒ MỘT PHẦN CATALOG_VERSION_UNVERIFIED", b["completeness_label"] == MP and "trước K3" in b["reason"], b["reason"][:100])
    real_read = G.catalog_read
    calls = {"n": 0}

    def racing(path=None):
        calls["n"] += 1
        r = real_read(path)
        return ("1" * 64, r[1], r[2]) if calls["n"] >= 2 else r
    G.catalog_read = racing
    b = lab(TRQ, d)
    G.catalog_read = real_read
    case("K3", "N10", "danh mục đổi SAU khi tính nhãn (chạy đua đọc→nhãn) ⇒ MỘT PHẦN CATALOG_CHANGED_DURING_LABEL",
         b["completeness_label"] == MP and "CATALOG_CHANGED_DURING_LABEL" in b["reason"], b["reason"][:100])
    write_cells(raw=open(CELLS_P, "rb").read() + b" ")
    b = lab(TRQ, d, rows=0)
    case("K3", "N11", "kết quả rỗng 0/0 khi danh mục lệch ⇒ MỘT PHẦN, không «rỗng được chứng nhận»", b["completeness_label"] == MP and "được chứng nhận" not in (b["reason"] or ""),
         b["reason"][:100])
    s = G.label_for("get-schema", {}, None, NOW, d, None, live_ok, False)
    case("K3", "N12", "get-schema khi danh mục lệch ⇒ MỘT PHẦN + catalog_revision báo lệch", s["completeness_label"] == MP and s["catalog_revision"]["status"] != "MATCH",
         s.get("catalog_revision"))
    reset()
    e, why = G.effective(d, NOW)
    case("K3", "N13", "effective(): danh mục khớp ⇒ 29 ô ĐỦ như giấy, thư mục giữ trạng thái giấy", sum(1 for v in e.values() if v[0] == DU) == BASE["summary"]["du"],
         sum(1 for v in e.values() if v[0] == DU))
    write_cells(raw=open(CELLS_P, "rb").read() + b"\n")
    e, why = G.effective(d, NOW)
    case("K3", "N14", "effective(): danh mục lệch ⇒ 0 ô ĐỦ (đèn/nhãn dùng chung)", not any(v[0] == DU for v in e.values()), sum(1 for v in e.values() if v[0] == DU))
    reset()

    # lượt cấp giấy: danh mục đổi giữa lượt ⇒ CATALOG_CHANGED_DURING_CERT (Graph giả + nguồn tiêm, ô dot:command)
    class FG:
        def __init__(self, ids):
            self.ids = ids

        def password(self):
            return ""

        def invariants(self, pw):
            return {"gs_keys_sha256": "fx", "edges_sha256": "fx", "gs_keys_count": len(self.ids), "edges_count": 0}

        def http_cypher(self, stmts, pw, timeout=0):
            (q, p), = stmts
            res = lambda cols, rows: {"results": [{"columns": cols, "data": [{"row": r} for r in rows]}], "errors": [], "lastBookmarks": ["bm"]}
            if q.startswith("RETURN 1"):
                return res(["x"], [[1]])
            if "RETURN count(n) AS c" in q:
                return res(["c"], [[len(self.ids)]])
            after = (p or {}).get("after", "")
            rows = [["dot:command:" + i, i, [], True] for i in sorted(self.ids) if "dot:command:" + i > after]
            return res(["k", "id", "av", "gs"], rows[:(p or {}).get("page", 2000)])
    G.graph_epoch = lambda g, pw: dict(EP)
    inj = {"dot_bin": {"commands": ["a", "b"], "commands_after": ["a", "b"]}, "pg": {}}
    r1 = G.run(FG(["a", "b"]), "", only={"dot:command"}, injected=inj, write=False, now=NOW)
    case("K3", "R1", "lượt cấp giấy danh mục đứng yên ⇒ ô ĐỦ + cell_def_sha256 + catalog_sha256 = byte đã đọc", r1["cells"]["dot:command"]["status"] == DU
         and r1["catalog_sha256"] == SHA(CELLS) and r1["cells"]["dot:command"].get("cell_def_sha256"), r1["cells"]["dot:command"]["status"])
    calls["n"] = 0

    def flip(path=None):
        calls["n"] += 1
        r = real_read(path)
        return ("2" * 64, r[1], r[2]) if calls["n"] >= 2 else r
    G.catalog_read = flip
    r2 = G.run(FG(["a", "b"]), "", only={"dot:command"}, injected=inj, write=False, now=NOW)
    G.catalog_read = real_read
    case("K3", "R2", "danh mục đổi trong lúc cấp giấy ⇒ MỘT PHẦN CATALOG_CHANGED_DURING_CERT", r2["cells"]["dot:command"]["status"] == MP
         and "CATALOG_CHANGED_DURING_CERT" in r2["cells"]["dot:command"]["reasons"], r2["cells"]["dot:command"]["reasons"])

    # =========================================================================== tín hiệu thay đổi (signals_now, nguồn tiêm)
    class FS:
        def __init__(self, cache):
            self.cache = cache

        def get(self, n):
            return self.cache.get(n, {"_error": "không tiêm"})

    def pgc(rows):
        return {"ok": True, "rows": rows}

    def pgsrc(tables, sys_=None, reset=None, audit=None, window=(), scan=None):
        dd = {"classes": {"stat_tables": pgc([[k] + [str(x) for x in v] for k, v in tables.items()]),
                          "stat_sys": pgc([[k] + [str(x) for x in v] for k, v in (sys_ or {"pg_class": [1, 1, 1]}).items()]),
                          "stat_db": pgc([[reset or "", "1"]])}}
        if audit is not None:
            dd["classes"]["directus_audit"] = pgc(audit)
            dd["classes"]["directus_audit_window"] = pgc(list(window))
        for k, v in (scan or {}).items():
            dd["classes"][k] = pgc(v)
        return {"directus": dd}
    nowt = time.time()
    fin = time.strftime("%Y-%m-%d %H:%M:%S+00", time.gmtime(nowt - 3600))
    old_fin = time.strftime("%Y-%m-%d %H:%M:%S+00", time.gmtime(nowt - 40 * 3600))
    AUD = lambda cnt, mn, mx, rv=10: [["activity", str(cnt), str(mn), str(mx), "2025-12-07 09:13:49", "2026-10-23 09:00:00"], ["revisions", str(rv), "1", str(rv), "", ""]]
    SC = lambda fin_, docker, cron, timer: {"scanner_log": [["docker_containers", fin_, "1"], ["host_crontab", fin_, "1"], ["systemd_timers", fin_, "1"]],
                                           "scanner_docker": [[x, "img"] for x in docker], "scanner_cron": [["/x", s_] for s_ in cron], "scanner_timer": [[x, "s"] for x in timer]}
    nat = {"docker": {"names_after": ["a", "b"]}, "cron": {"entries": [["/etc/crontab|0 * * * *|/x"], ["/etc/crontab|5 * * * *|/y"]], "edges": [], "errors": []},
           "containers_meta": {"meta": {"a": {"id12": "1", "started_at": "s", "restart_count": "0"}}}, "git_repos": {"repos": {"/r": "t1"}}}
    prev = {"pg_counters": {"directus": {"tables": {"public.t": [10, 0, 0]}, "catalog": {"pg_class": [1, 1, 1]}, "stats_reset": None}},
            "directus_audit": {"activity_min_id": 1, "activity_max_id": 100, "revisions_max_id": 10},
            "docker_meta": {"a": {"id12": "1", "started_at": "s", "restart_count": "0"}}, "git_trees": {"/r": "t1"}}
    base_scan = SC(fin, ["a", "b"], ["0 * * * *", "5 * * * *"], [])
    G.sh = (lambda real: (lambda cmd, *a_, **k: (0, "", "") if cmd[:2] == ["systemctl", "list-units"] else real(cmd, *a_, **k)))(G.sh)

    def sig(pg, extra=None, prev_=prev):
        cache = dict(nat, pg=pg)
        cache.update(extra or {})
        return G.signals_now(FS(cache), prev_, nowt)
    f, st_ = sig(pgsrc({"public.t": [11, 0, 1]}, audit=AUD(100, 1, 100), scan=base_scan))
    g1 = {x["kind"]: x for x in f["G1"]}
    case("SIG", "S1", "chèn+xoá giữa hai lượt: số dòng như cũ nhưng bộ đếm đổi ⇒ CHANGED (SIGNAL_COUNTER_ONLY, không phải CDC)",
         g1["pg_stat_counters:directus"]["status"] == "CHANGED" and g1["pg_stat_counters:directus"]["grade"] == "SIGNAL_COUNTER_ONLY"
         and g1["pg_stat_counters:directus"]["delta"]["tables_with_activity"] == 1, g1["pg_stat_counters:directus"].get("delta"))
    case("SIG", "S3", "ghi thẳng SQL (bộ đếm đổi) KHÔNG có trong nhật ký Directus ⇒ audit NO_NEW_EVENTS, hạng PATH_LIMITED_AUDIT",
         g1["directus_activity+revisions"]["status"] == "NO_NEW_EVENTS" and g1["directus_activity+revisions"]["grade"] == "PATH_LIMITED_AUDIT",
         g1["directus_activity+revisions"]["status"])
    f, _ = sig(pgsrc({"public.t": [5, 0, 0]}, audit=AUD(100, 1, 100), scan=base_scan))
    case("SIG", "S2a", "bộ đếm PG giảm (đặt lại/khởi động bẩn) ⇒ UNKNOWN_COUNTER_RESET", f["G1"][0]["status"] == "UNKNOWN_COUNTER_RESET", f["G1"][0].get("why"))
    f, _ = sig(pgsrc({"public.t": [10, 0, 0]}, reset="2026-10-23 01:00:00", audit=AUD(100, 1, 100), scan=base_scan))
    case("SIG", "S2b", "stats_reset đổi dù bộ đếm không giảm ⇒ UNKNOWN_COUNTER_RESET", f["G1"][0]["status"] == "UNKNOWN_COUNTER_RESET", f["G1"][0].get("why"))
    f, _ = sig(pgsrc({"public.t": [10, 0, 0]}, audit=AUD(50, 150, 200), scan=base_scan))
    case("SIG", "S4", "nhật ký Directus bị cắt vượt mốc đã đọc ⇒ UNKNOWN_RETENTION_GAP", f["G1"][-1]["status"] == "UNKNOWN_RETENTION_GAP", f["G1"][-1].get("why"))
    f, _ = sig(pgsrc({"public.t": [10, 0, 0]}, audit=AUD(90, 1, 90), scan=base_scan))
    case("SIG", "S5a", "mốc id Directus lùi (con trỏ trùng/đọc lại) ⇒ UNKNOWN_CURSOR_REGRESSION", f["G1"][-1]["status"] == "UNKNOWN_CURSOR_REGRESSION", f["G1"][-1].get("why"))
    f, st2 = sig(pgsrc({"public.t": [10, 0, 0]}, audit=AUD(100, 1, 100), scan=base_scan))
    case("SIG", "S5b", "đọc lại cùng mốc ⇒ NO_NEW_EVENTS (không đếm đôi), mốc lưu không đổi", f["G1"][-1]["status"] == "NO_NEW_EVENTS"
         and st2["directus_audit"]["activity_max_id"] == 100, f["G1"][-1].get("delta"))
    f, _ = sig(pgsrc({"public.t": [10, 0, 0]}, audit=AUD(105, 1, 105), window=[["directus_relations", "create", "1", "105"]], scan=base_scan))
    case("SIG", "S5c", "sự kiện schema Directus trong cửa sổ 26h ⇒ SCHEMA_EVENTS_IN_WINDOW (phải đọc lại catalog)", f["G1"][-1]["status"] == "SCHEMA_EVENTS_IN_WINDOW",
         f["G1"][-1]["measured"]["window_26h"]["schema_events"])
    f, _ = sig(pgsrc({"public.t": [10, 0, 0]}, audit=AUD(100, 1, 100), scan=SC(old_fin, ["a", "b"], ["0 * * * *", "5 * * * *"], [])))
    case("SIG", "S6a", "scanner cũ > 26h ⇒ SCANNER_STALE (không phải sự thật)", f["G2"][0]["status"] == "SCANNER_STALE", f["G2"][0]["measured"]["scanner_age_h"])
    f, _ = sig(pgsrc({"public.t": [10, 0, 0]}, audit=AUD(100, 1, 100), scan=SC(fin, ["a"] * 1, ["0 * * * *"], [])),
               {"docker": {"names_after": ["a", "b"]}})
    case("SIG", "S6b", "scanner docker 14/gốc 16 (thiếu) ⇒ SCANNER_INCOMPLETE", f["G2"][0]["status"] == "SCANNER_INCOMPLETE", f["G2"][0]["measured"])
    case("SIG", "S6c", "scanner cron 37/gốc 50 (thiếu dòng lịch) ⇒ SCANNER_INCOMPLETE", next(x for x in f["G4"] if x["kind"].startswith("wf"))["status"] == "SCANNER_INCOMPLETE",
         next(x for x in f["G4"] if x["kind"].startswith("wf"))["measured"])
    f, _ = sig(pgsrc({"public.t": [10, 0, 0]}, audit=AUD(100, 1, 100), scan=SC(fin, ["a", "c"], ["0 * * * *", "5 * * * *"], [])))
    case("SIG", "S7", "cùng số nhưng đổi tên đích (a,c vs a,b) ⇒ không xanh vì bằng số: thiếu 1 + thừa 1", f["G2"][0]["status"] == "SCANNER_INCOMPLETE"
         and f["G2"][0]["measured"]["missing_count"] == 1 and f["G2"][0]["measured"]["extra_count"] == 1, f["G2"][0]["measured"])
    g8 = f["G8"][0]
    case("SIG", "S8", "Lark sửa-rồi-xoá trước lượt đêm: không có watermark/lịch sử xoá ⇒ G8 NO_ACCESS/UNKNOWN (không tự nhận SOURCE_WATERMARK)",
         g8["grade"] == "NO_ACCESS/UNKNOWN" and g8["status"] == "UNKNOWN", g8)
    f, _ = sig(pgsrc({"public.t": [10, 0, 0]}, audit=AUD(100, 1, 100), scan=base_scan), {"git_repos": {"repos": {"/r": "t2"}}})
    g9 = f["G9"][0]
    ev = GA.code_roots_for("/opt/incomex", {"k": {"rule": "git-head", "root": "/opt/incomex/k", "loaded": {"files_tsv_sha256": "A"}}},
                           {"k": {"runtime_ok": False, "files_tsv_sha256": "B"}}, {"k": "/opt/incomex"})
    case("SIG", "S9", "commit mới chưa triển khai: git CHANGED (SOURCE_COMMIT_LOG) nhưng KHÔNG có bằng chứng kho→mã chạy", g9["status"] == "CHANGED"
         and g9["grade"] == "SOURCE_COMMIT_LOG" and ev == [], (g9["status"], ev))
    ev2 = GA.code_roots_for("/opt/incomex", {"k": {"rule": "git-head", "root": "/opt/incomex/k", "loaded": {"files_tsv_sha256": "A"}}},
                            {"k": {"runtime_ok": True, "files_tsv_sha256": "A"}}, {"k": "/opt/incomex"})
    case("SIG", "S9b", "bản chạy = HEAD = bộ đang nạp ⇒ có bằng chứng kho→cây mã", ev2 == ["k@A"], ev2)
    f, _ = sig(pgsrc({"public.t": [10, 0, 0]}, audit=AUD(100, 1, 100), scan=base_scan))
    g2 = next(x for x in f["G2"] if x["kind"] == "docker_container_start_meta")
    case("SIG", "S10a", "container sinh-rồi-xoá giữa hai lượt ⇒ KHÔNG thấy (NO_CHANGE_OBSERVED), giới hạn nêu rõ", g2["status"] == "NO_CHANGE_OBSERVED"
         and "sinh-rồi-xoá" in g2["limits"], g2["status"])
    f, _ = sig(pgsrc({"public.t": [10, 0, 0]}, audit=AUD(100, 1, 100), scan=base_scan),
               {"containers_meta": {"meta": {"a": {"id12": "2", "started_at": "s2", "restart_count": "0"}}}})
    g2 = next(x for x in f["G2"] if x["kind"] == "docker_container_start_meta")
    case("SIG", "S10b", "container còn sống bị tái tạo ⇒ CHANGED recreated", g2["status"] == "CHANGED" and g2["delta"]["recreated"] == ["a"], g2["delta"])
    allg = [x.get("grade") for v in f.values() for x in v]
    case("SIG", "S11", "không họ nào tự nhận DURABLE_EVENT_CURSOR_VERIFIED; mọi tín hiệu có hạng trong bảng hạng", "DURABLE_EVENT_CURSOR_VERIFIED" not in allg
         and all(gd in G.GRADES for gd in allg if gd), sorted(set(allg)))
    dd = copy.deepcopy(d)
    dd["coverage_matrix"]["G1"]["change_signals"] = [{"kind": "pg_stat_counters:directus", "status": "UNKNOWN_COUNTER_RESET", "why": "x"}]
    sign(dd)
    st, msg, inc = G.alarm(dd, now=NOW, baseline={"accepted_partial": {}})
    case("SIG", "S12", "tín hiệu mất/đặt lại ⇒ sự cố VÀNG SIGNAL_DEGRADED (gọi trang một lần)", any(i["kind"] == "SIGNAL_DEGRADED" and i["severity"] == "warning" for i in inc),
         [i["reason"] for i in inc if i["kind"] == "SIGNAL_DEGRADED"])

    # =========================================================================== lane: kế hoạch cộng-thêm (Graph giả)
    class GG:
        def __init__(self, nodes, edges):
            self.n, self.e = nodes, edges          # nodes {k: (labels, props)} · edges [(s, t, d, props)]

        def rows(self, d):
            r = d["results"][0]
            return [dict(zip(r["columns"], x["row"])) for x in r["data"]]

        def http_cypher(self, stmts, pw, timeout=0):
            (q, p), = stmts
            res = lambda cols, rows: {"results": [{"columns": cols, "data": [{"row": r} for r in rows]}], "errors": []}
            if q.startswith("MATCH (n:GS) WHERE n.gs_layer = $l"):
                return res(["k", "l", "p"], [[k, v[0], v[1]] for k, v in self.n.items() if v[1].get("gs_layer") == p["l"]])
            if q.startswith("MATCH (a:GS)-[x]->(b:GS) WHERE a.gs_layer = $l"):
                lay = lambda k: (self.n.get(k) or ([], {}))[1].get("gs_layer")
                return res(["s", "t", "d", "p"], [[s, t, d_, pp] for s, t, d_, pp in self.e if lay(s) == p["l"] or lay(d_) == p["l"]])
            if q.startswith("MATCH (n:GS) WHERE n.gs_key IN $k"):
                return res(["k", "l", "layer"], [[k, self.n[k][0], self.n[k][1].get("gs_layer")] for k in p["k"] if k in self.n])
            raise AssertionError(q)

    def N(k, label, layer="infra", **pp):
        return {"l": ["GS", label], "p": dict({"gs_key": k, "id": k.split(":", 2)[-1], "gs_layer": layer, "trust": "EXACT_AT_SNAPSHOT", "snapshot_utc": "t", "run": "r"}, **pp)}

    def E(s, t, d_):
        return {"t": t, "s": s, "d": d_, "p": {"trust": "EXACT_AT_SNAPSHOT", "snapshot_utc": "t", "source": "x", "run": "r", "gs_edge_key": GA.sha16("%s|%s|%s" % (s, t, d_))}}
    want_n = {"net:listen:a": N("net:listen:a", "NetListener"), "systemd:unit:x.service": N("systemd:unit:x.service", "SystemdUnit", kind="service")}
    want_e = {("net:listen:a", "BOUND_BY_PROCESS_OF", "systemd:unit:x.service"): E("net:listen:a", "BOUND_BY_PROCESS_OF", "systemd:unit:x.service")}
    caps, used = {"nodes": 600, "edges": 1200}, {"nodes": 0, "edges": 0}
    gg_full = GG({k: (v["l"], dict(v["p"], snapshot_utc="old", run="old")) for k, v in want_n.items()},
                 [(s, t, d_, dict(e["p"], snapshot_utc="old")) for (s, t, d_), e in want_e.items()])
    pl = GA.plan(gg_full, "", "c1d:infra", want_n, want_e, caps, used)
    case("LANE", "L1", "Graph = nguồn (chỉ khác dấu giờ/lượt) ⇒ kế hoạch rỗng (NO_CHANGE, không SET vô ích)", pl["empty"] and not pl["problems"], pl["counts"])
    pl = GA.plan(GG({}, []), "", "c1d:infra", want_n, want_e, caps, used)
    fq = " ".join(q for q, _ in pl["F"])
    case("LANE", "L2", "Graph rỗng ⇒ +2 nút +1 cạnh; F không có DELETE; I xoá đúng khoá đã tạo", pl["counts"]["nodes_add"] == 2 and pl["counts"]["edges_add"] == 1
         and "DELETE" not in fq and pl["created_keys"] == sorted(want_n) and any("gs_edge_key IN" in q for q, _ in pl["I"]), pl["counts"])
    gg_stale = GG(dict(gg_full.n, **{"net:listen:gone": (["GS", "NetListener"], N("net:listen:gone", "NetListener")["p"])}), gg_full.e)
    pl = GA.plan(gg_stale, "", "c1d:infra", want_n, want_e, caps, used)
    case("LANE", "L3", "nguồn mất đối tượng ⇒ giữ trong Graph, báo stale (0 xoá, không tỉa)", pl["stale_nodes"] == ["net:listen:gone"] and pl["empty"]
         and pl["counts"]["nodes_delete"] == 0, pl["stale_nodes"])
    w2 = copy.deepcopy(want_n)
    w2["systemd:unit:x.service"]["p"]["kind"] = "socket"
    pl = GA.plan(gg_full, "", "c1d:infra", w2, want_e, caps, used)
    case("LANE", "L4", "thuộc tính danh tính đổi ⇒ SET; nghịch đảo đặt lại thuộc tính cũ", pl["counts"]["nodes_set"] == 1
         and any(r["p"]["kind"] == "service" for q, p in pl["I"] if "rows" in p for r in p["rows"]), pl["counts"])
    gg_other = GG({"systemd:unit:x.service": (["GS", "SystemdUnit"], dict(want_n["systemd:unit:x.service"]["p"], gs_layer="other", kind="zzz"))}, [])
    pl = GA.plan(gg_other, "", "c1d:infra", want_n, want_e, caps, used)
    case("LANE", "L5", "nút thuộc lane khác ⇒ chỉ dùng làm điểm cuối, KHÔNG SET", pl["reuse_nodes"] == ["systemd:unit:x.service"] and pl["counts"]["nodes_set"] == 0, pl["counts"])
    many = {"net:listen:%03d" % i: N("net:listen:%03d" % i, "NetListener") for i in range(20)}
    p1 = GA.plan(GG({}, []), "", "c1d:infra", many, {}, {"nodes": 7, "edges": 10}, used)
    p2 = GA.plan(GG({}, []), "", "c1d:infra", dict(reversed(list(many.items()))), {}, {"nodes": 7, "edges": 10}, used)
    case("LANE", "L6", "vượt trần ⇒ CAP_BOUND_PARTIAL, lấy mẫu tất định (hai thứ tự đầu vào ⇒ cùng tập)", p1["cap_bound_partial"] and p1["created_keys"] == p2["created_keys"]
         and len(p1["created_keys"]) == 7, p1["created_keys"][:3])
    p3 = GA.plan(GG({}, []), "", "c1d:infra", many, {}, {"nodes": 5, "edges": 10}, {"nodes": 25, "edges": 0})
    case("LANE", "L6b", "quota MỖI LƯỢT, sổ cộng dồn không còn trừ: thêm đúng 5, còn 15 cho lượt sau", p3["cap_bound_partial"] and len(p3["created_keys"]) == 5 and p3["quota_left"] == 15, len(p3["created_keys"]))
    pl = GA.plan(GG({}, []), "", "c1d:infra", {"net:listen:a": want_n["net:listen:a"]}, want_e, caps, used)
    case("LANE", "L7", "cạnh tới điểm cuối không tồn tại ⇒ vấn đề EDGE_ENDPOINT_MISSING (BLOCKED)", any(x.startswith("EDGE_ENDPOINT_MISSING") for x in pl["problems"]), pl["problems"])
    gg_conf = GG({"net:listen:a": (["GS", "SystemdUnit"], N("net:listen:a", "SystemdUnit")["p"])}, [])
    pl = GA.plan(gg_conf, "", "c1d:infra", want_n, want_e, caps, used)
    case("LANE", "L8", "trùng khoá khác nhãn ⇒ LABEL_CONFLICT", any("LABEL_CONFLICT" in x for x in pl["problems"]), pl["problems"])
    gg_out = GG({"pg:table:a": (["GS", "PgTable"], {"gs_key": "pg:table:a", "gs_layer": "pg"}), "pg:table:b": (["GS", "PgTable"], {"gs_key": "pg:table:b", "gs_layer": "pg"})}, [])
    pl = GA.plan(gg_out, "", "c1d:pgl1", {}, {("pg:table:a", "HAS_FK", "pg:table:b"): E("pg:table:a", "HAS_FK", "pg:table:b")}, caps, used)
    case("LANE", "L9", "cạnh giữa HAI nút lớp khác (không chạm lane) ⇒ EDGE_OUTSIDE_LANE", any("EDGE_OUTSIDE_LANE" in x for x in pl["problems"]), pl["problems"])
    GRF_SRC = open(GRF_P).read()
    # quyết định lane trong graph-refresh (hàm thuần decide) — nạp không chạy main
    sys.path.insert(0, os.path.dirname(CAND))
    sys.modules["graph_cert"], sys.modules["graph_autocover"] = G, GA
    RF = load(GRF_P, "graph_refresh_fx")
    clean = {"b88": {"csv_sha256": {f_: "a" for f_ in RF.LANE_FILES["b88"]}}, "pgdot": {"expected_sha256": "e", "q_dot_identical": True}, "code": {}}
    srcs = {"b88": {"csv_sha256": {f_: "a" for f_ in RF.LANE_FILES["b88"]}}, "pgdot": {"expected_sha256": "e"}, "code": {"repos": {}}}
    mk = lambda c1d: dict(copy.deepcopy(clean), c1d=c1d)
    ok_pl = {"empty": True, "problems": [], "counts": {"stale_nodes": 0, "stale_edges": 0}, "cap_bound_partial": False}
    dl = RF.decide(mk({"c1d:infra": ok_pl, "c1d:pgl1": dict(ok_pl, empty=False)}), srcs)
    case("LANE", "L10a", "decide: kế hoạch rỗng ⇒ NO_CHANGE · có thay đổi ⇒ DELTA", dl["c1d:infra"]["decision"] == "NO_CHANGE" and dl["c1d:pgl1"]["decision"] == "DELTA",
         (dl["c1d:infra"]["decision"], dl["c1d:pgl1"]["decision"]))
    dl = RF.decide(mk({"c1d:infra": {"error": "ss rc=1"}, "c1d:pgl1": dict(ok_pl, problems=["LABEL_CONFLICT x"])}), srcs)
    case("LANE", "L10b", "decide: bộ đọc hỏng / vấn đề kế hoạch ⇒ BLOCKED (đèn ĐỎ, không ghi)", dl["c1d:infra"]["decision"] == "BLOCKED" and dl["c1d:pgl1"]["decision"] == "BLOCKED",
         (dl["c1d:infra"], dl["c1d:pgl1"]))
    case("LANE", "L11", "lý do được phép khi nạp phần đã chứng minh chỉ gồm AMBIGUOUS_OWNER/GIT_UNREADABLE (ô vẫn MỘT PHẦN)",
         RF.C1D_GATE_ALLOWED == ("AMBIGUOUS_OWNER", "GIT_UNREADABLE"), RF.C1D_GATE_ALLOWED)
    cellL = next(c for c in json.load(open(CELLS_P))["cells"] if c["key"] == "infra:listener")
    r = G.evaluate(cellL, {"ok": True, "objects": [["NetListener", "a"]], "edges": [], "consistency": "BEFORE_AFTER_EQUAL", "unresolved": ["AMBIGUOUS_OWNER a"]},
                   {"objects": [["NetListener", "a"]], "edges": [], "meta": {"complete": True, "problems": []}}, NOW, 26)
    case("LANE", "L12", "cổng nghe không chủ chắc chắn ⇒ ô infra:listener MỘT PHẦN AMBIGUOUS_OWNER dù Graph = nguồn", r["status"] == MP and "AMBIGUOUS_OWNER a" in r["reasons"],
         r["reasons"])
    case("LANE", "L13", "graph-refresh: lane c1d dùng cùng khuôn bảo vệ (temp_from_recovery · score · I/F · apply_plan · apply_v0 · new_recovery_point)",
         all(x in GRF_SRC for x in ("def build_c1d_lane", "temp_from_recovery(\"rf-\" + lane", "GA.score(GC, gt", "rehearse_I_eq_pre", "apply_plan(target, plan",
                                    "new_recovery_point(g, pw", "_pilot_total")), "mẫu mã")
    w3 = {k: {"l": v["l"], "p": dict(v["p"], snapshot_utc="t2", run="r2")} for k, v in want_n.items()}
    e3 = {k: {"t": e["t"], "s": e["s"], "d": e["d"], "p": dict(e["p"], snapshot_utc="t2")} for k, e in want_e.items()}
    pa = GA.plan(GG({}, []), "", "c1d:infra", want_n, want_e, caps, used)
    pb = GA.plan(GG({}, []), "", "c1d:infra", w3, e3, caps, used)
    w4 = copy.deepcopy(want_n)
    w4["systemd:unit:x.service"]["p"]["kind"] = "socket"
    pc = GA.plan(GG({}, []), "", "c1d:infra", w4, want_e, caps, used)
    case("LANE", "L15", "kiểm «nguồn đổi giữa lượt»: đọc lại chỉ khác dấu giờ chụp ⇒ CÙNG vân tay danh tính; thuộc tính danh tính đổi ⇒ KHÁC",
         pa["ident_sha256"] == pb["ident_sha256"] and pa["sha256"] != pb["sha256"] and pc["ident_sha256"] != pa["ident_sha256"],
         (pa["ident_sha256"][:8], pb["ident_sha256"][:8], pc["ident_sha256"][:8]))
    case("LANE", "L16", "graph-refresh kiểm lại giữa lượt dùng ident_sha256 (không dùng sha256 gồm dấu giờ)",
         'c2.get("ident_sha256") != caps["c1d"][item]["ident_sha256"]' in GRF_SRC, "mẫu mã")
    # cmd_run trọn đường DELTA của lane c1d với hàm ghi thay bằng bản giả (0 production): sổ nguồn c1d + trần cộng dồn được ghi, kết quả DELTA_APPLIED
    import types as _t
    T2 = TMP + "/run"
    os.makedirs(T2 + "/state/runs")
    for nm in ("graph-invariants.json", "pins.json", "refresh-sources.json", "recovery-manifest.json"):
        shutil.copyfile("/opt/incomex/graph-server/prod-v1/manifest/" + nm, T2 + "/" + nm)
    RF.INV, RF.PINS, RF.SOURCES, RF.RECMAN = (T2 + "/" + x for x in ("graph-invariants.json", "pins.json", "refresh-sources.json", "recovery-manifest.json"))
    RF.STATE, RF.LOG, RF.PGL1_CROSS = T2 + "/state", T2 + "/log.jsonl", T2 + "/cross.json"
    srcs0 = json.load(open(RF.SOURCES))
    st0 = json.load(open(RF.RECMAN))["current"]["state"]
    fake_pl = {"empty": False, "problems": [], "counts": {"nodes_add": 3, "edges_add": 2, "nodes_set": 0, "edges_set": 0, "stale_nodes": 0, "stale_edges": 0},
               "cap_bound_partial": False, "sha256": "s1", "ident_sha256": "i1", "F": [], "I": []}
    rf_calls = []

    class FakeGr:
        def password(self):
            return ""

        def invariants(self, pw):
            return {"labels": {}, "rels": {}}

        def inv_equal(self, a, b):
            return []
    RF.r7_g1lib.load = lambda path=None: FakeGr()
    RF.take_lock = lambda trig: open(os.devnull, "w")
    RF.term_to_fail = lambda: None
    RF.preconditions = lambda g, pw, need_vps=True: ({}, [])
    RF.cap_b88 = lambda w: {"csv_sha256": srcs0["b88"]["csv_sha256"], "snapshot_utc": "x", "input_dir": w}
    RF.cap_pgdot = lambda w: {"expected_sha256": srcs0["pgdot"]["expected_sha256"], "q_dot_identical": True, "snapshot_utc": {}, "input_dir": w}
    RF.cap_code = lambda w, s_: {}
    RF.cap_c1d = lambda g, pw, s_, c_, lanes=RF.C1D_LANES: {l: dict(fake_pl) for l in lanes}
    RF.full_hash = lambda g, pw: st0
    RF.build_c1d_lane = lambda lane, pl, work, report, expect=None: {"lane": lane, "F": [], "I": [], "pre_hash": st0, "new_hash": st0, "new_inv": {},
                                                                     "stage_new": None, "stage_old": None, "plan_sha256": "s1", "counts": pl["counts"]}
    RF.vps_ghi_state = lambda: {"ok": True}
    RF.other_writers = lambda: []
    RF.apply_plan = lambda target, plan, report: rf_calls.append("apply_plan") or True

    def fake_v0(target, live, cand_obj, mid, raw_bytes=None):
        rf_calls.append("apply_v0:" + target)
        if raw_bytes is not None:
            open(live, "wb").write(raw_bytes)
        else:
            json.dump(cand_obj, open(live, "w"), indent=1, sort_keys=True, ensure_ascii=False)
        return True, "RESULT=APPLIED"
    RF.apply_v0 = fake_v0
    # L17 (GS-C1D2-SCOPED-AUTOCOVER-20261026-13): kỳ vọng theo sổ nguồn ĐÓNG BĂNG đầu ca (srcs0) + 3 nút/+2 cạnh, không ghim số tuyệt đối
    #   (183/154 sống làm ca cũ hỏng sẵn); giả new_recovery_point theo chữ ký D23 (điểm, đường tạm) và ghi nhận bước chốt commit_recovery_point.
    p17 = (srcs0.get("c1d") or {}).get("_pilot_total") or {"nodes": 0, "edges": 0}
    cn17 = ((srcs0.get("c1d") or {}).get("c1d:pgl1") or {}).get("created_nodes", 0)
    stg17 = T2 + "/rp-staged"

    def fake_rp17(g, pw, label, drive, report):
        rf_calls.append("recovery_point")
        os.makedirs(stg17, exist_ok=True)
        return {"name": "fx", "state": st0, "meta_sha256": "m"}, stg17
    RF.new_recovery_point = fake_rp17
    RF.commit_recovery_point = lambda stg, rp: rf_calls.append("commit:" + os.path.basename(stg)) or None
    RF.pgl1_cross_from = lambda g, pw: {"edges": [1, 2]}
    RF.cert_tick = lambda rec, *a, **k: rf_calls.append("cert_tick") or {}
    RF.l2_tick = lambda rec: None
    rcx = RF.cmd_run(_t.SimpleNamespace(execute=True, trigger="manual", only="c1d:pgl1"))
    lastx = json.load(open(RF.STATE + "/last.json"))
    nsx = json.load(open(RF.SOURCES))
    l17 = lambda dn: (rcx == 0 and lastx.get("result") == "DELTA_APPLIED"
                      and nsx.get("c1d", {}).get("_pilot_total") == {"nodes": p17["nodes"] + 3 + dn, "edges": p17["edges"] + 2}
                      and nsx["c1d"]["c1d:pgl1"]["created_nodes"] == cn17 + 3 + dn and os.path.exists(RF.PGL1_CROSS)
                      and "recovery_point" in rf_calls and "commit:rp-staged" in rf_calls)
    case("LANE", "L17", "cmd_run lane c1d trọn đường (hàm ghi giả): DELTA_APPLIED, _pilot_total = sổ đầu ca +3/+2, created_nodes đầu ca +3, chốt điểm tạm, cross-edges pgl1",
         l17(0), (rcx, lastx.get("result"), lastx.get("why"), p17, nsx.get("c1d", {}).get("_pilot_total"), rf_calls))
    case("LANE", "L17n", "đối chứng âm L17: cùng lượt, kỳ vọng giả cộng +4 nút ⇒ phép kiểm phải KHÔNG khớp (không phải phép luôn đúng)", not l17(1),
         nsx.get("c1d", {}).get("_pilot_total"))
    case("LANE", "L14", "unit HJW chờ chủ nằm trong danh sách loại trừ của danh mục (không tự nhận)",
         set(json.load(open(CELLS_P))["c1d"]["units_excluded_pending_owner"]) == {"incomex-hjwcap.path", "incomex-hjwcap.service"}, "")
finally:
    shutil.rmtree(TMP, ignore_errors=True)

summ = {"total": len(RES), "pass": sum(r["pass"] for r in RES), "fail": [r["group"] + ":" + r["id"] for r in RES if not r["pass"]],
        "by_group": {g: "%d/%d" % (sum(r["pass"] for r in RES if r["group"] == g), sum(1 for r in RES if r["group"] == g)) for g in sorted({r["group"] for r in RES})},
        "candidate_sha256": hashlib.sha256(open(CAND, "rb").read()).hexdigest(), "autocover_sha256": hashlib.sha256(open(GA_P, "rb").read()).hexdigest()}
print("C1D FIXTURES %s" % json.dumps(summ, ensure_ascii=False))
if OUT:
    json.dump({"summary": summ, "cases": RES}, open(OUT, "w"), ensure_ascii=False, indent=1)
sys.exit(0 if not summ["fail"] else 1)
