#!/usr/bin/env python3
"""graph_autocover — BỘ NẠP CỘNG-THÊM CÓ GIỚI HẠN của graph-refresh cho lane C1-D · GS-C1D-NATIVE-AUTOCOVER-20261023-10

Thư viện của graph-refresh (lane `c1d:infra`, `c1d:pgl1`), KHÔNG có lịch riêng, KHÔNG dịch vụ mới. Chỉ đọc nguồn bằng công cụ gốc;
ghi Graph CHỈ qua đường guarded của graph-refresh (bản tạm từ điểm khôi phục → diễn tập F/I → tập khô → MỘT giao dịch → invariants/
pins/điểm khôi phục + Drive D23 qua apply-v0). Bộ đọc ở đây viết ĐỘC LẬP với bộ đọc ô của graph_cert (máy cấp giấy chấm lại).

  c1d:infra  (gs_layer infra)  — quan hệ kỹ thuật có chứng cứ gốc:
     G5 NetListener (ss -ltne ino ⇒ tiến trình giữ fd qua /proc/*/fd) -[BOUND_BY_PROCESS_OF]-> SystemdUnit (cgroup /system.slice/*.service)
        · -[PUBLISHED_BY]-> DockerContainer (docker-proxy giữ fd + PortBindings khai báo) · SystemdUnit(.socket) -[LISTENS_ON]-> NetListener
        (systemd pid 1 giữ fd + `systemctl list-sockets`). Cổng không có chủ chắc chắn ⇒ KHÔNG cạnh, ghi ambiguous (ô MỘT PHẦN).
     G3 SystemdUnit khai báo (danh sách trong cert-cells c1d.units_declared, 7 unit cũ): .socket/.path -[TRIGGERS]-> dịch vụ
        (`systemctl list-sockets/list-paths`) · dịch vụ -[REQUIRES_MOUNT]-> .mount (RequiredBy= khai báo). Unit HJW chờ chủ HJW ⇒ loại.
     G2 DockerContainer (mọi container trừ mẫu tạm) · G9 GitRepository + -[WORKTREE_OF]-> / -[RESOLVES_TO_TOPLEVEL]-> (đọc .git/commondir).
        Kho→cây mã: CHỈ thuộc tính bằng chứng `code_roots_evidence` (cạnh vào lớp code sẽ phá cổng đóng kín của lane code).
  c1d:pgl1   (gs_layer pgl1)   — lớp L1 catalog khai báo của các bảng mẫu (cert-cells l1_pilot.tables), dựng bằng bộ nạp C1-B (c1b_l1.build
     + c1b_l1_native, bản chép byte trong bin/refresh) — biến lớp C1-B tĩnh thành lane hằng đêm.
LUẬT GHI: chỉ CỘNG nút/cạnh mới + SET thuộc tính đổi của nút/cạnh THUỘC lane; 0 xoá; nút lane khác chỉ được dùng làm điểm cuối (không sửa);
  nguồn mất đối tượng ⇒ giữ trong Graph, báo `stale` (ô MỘT PHẦN, không tỉa). Trần toàn pilot C1-D (cert-cells c1d.caps) tính cộng dồn
  theo refresh-sources c1d.*.created_* — vượt ⇒ lấy mẫu tất định theo sha256(khoá ổn định), CAP_BOUND_PARTIAL, phần dư không ghi.
  Nghịch đảo I = xoá đúng cạnh/nút đã tạo (gs_edge_key/gs_key) + đặt lại thuộc tính cũ của phần đã SET.
"""
import hashlib, importlib.machinery, importlib.util, json, os, re, subprocess, time

ROOT = "/opt/incomex/graph-server/prod-v1"
RB = ROOT + "/bin/refresh"
LAYER = {"c1d:infra": "infra", "c1d:pgl1": "pgl1"}
PREFIX = {"NetListener": "net:listen:", "SystemdUnit": "systemd:unit:", "DockerContainer": "docker:container:", "GitRepository": "git:repo:"}
LABELS = {"c1d:infra": {"GS", "NetListener", "SystemdUnit", "DockerContainer", "GitRepository"},
          "c1d:pgl1": {"GS", "PgTable", "PgView", "PgForeignKey", "DirectusCollection", "DirectusRelation", "DirectusPermission"}}
TYPES = {"c1d:infra": {"BOUND_BY_PROCESS_OF", "PUBLISHED_BY", "LISTENS_ON", "TRIGGERS", "REQUIRES_MOUNT", "WORKTREE_OF", "RESOLVES_TO_TOPLEVEL"},
         "c1d:pgl1": {"HAS_FK", "REFERENCES", "DEPENDS_ON", "MAPS_TO_TABLE", "RELATION_MANY", "RELATION_ONE", "PERMISSION_ON"}}
VOLATILE = {"snapshot_utc", "run", "loaded_at", "gs_edge_key", "head_at_load", "source_file"}   # không thuộc danh tính khi so khác
now_iso = lambda: time.strftime("%FT%TZ", time.gmtime())


def sh(cmd, timeout=120, inp=None):
    try:
        p = subprocess.run(cmd, capture_output=True, timeout=timeout, input=inp)
        return p.returncode, p.stdout.decode(errors="replace"), p.stderr.decode(errors="replace")
    except (OSError, subprocess.TimeoutExpired) as e:
        return 124, "", type(e).__name__


def sha16(s):
    return hashlib.sha256(s.encode()).hexdigest()[:16]


# =========================================================================== bộ đọc gốc (lane infra)
def _fd_holders():
    """inode socket ⇒ {pid…} bằng cách đọc /proc/*/fd (không dùng ss -p)."""
    out = {}
    for pid in os.listdir("/proc"):
        if not pid.isdigit():
            continue
        d = "/proc/%s/fd" % pid
        try:
            for fd in os.listdir(d):
                try:
                    t = os.readlink(d + "/" + fd)
                except OSError:
                    continue
                if t.startswith("socket:["):
                    out.setdefault(t[8:-1], set()).add(int(pid))
        except OSError:
            continue
    return out


def _proc(pid):
    try:
        comm = open("/proc/%d/comm" % pid).read().strip()
        cg = open("/proc/%d/cgroup" % pid).read().strip().splitlines()[0].split(":", 2)[-1]
        return comm, cg
    except OSError:
        return None, None


def read_listeners():
    rc, o, _ = sh(["ss", "-H", "-ltne"], 30)
    if rc != 0:
        raise RuntimeError("ss -ltne rc=%s" % rc)
    ino = {}
    for ln in o.splitlines():
        p = ln.split()
        m = re.search(r"\bino:(\d+)", ln)
        if len(p) >= 4 and m:
            ino.setdefault(p[3], set()).add(m.group(1))
    return ino


def read_socket_units():
    rc, o, _ = sh(["systemctl", "list-sockets", "--all", "--full", "--no-legend", "--no-pager"], 60)
    if rc != 0:
        raise RuntimeError("list-sockets rc=%s" % rc)
    lst, act = {}, {}
    for ln in o.splitlines():
        p = ln.split()
        if len(p) >= 3 and p[-2].endswith(".socket"):
            listen, unit, acts = " ".join(p[:-2]), p[-2], p[-1]
            lst.setdefault(unit, set()).add(listen)
            if acts != "-":
                act.setdefault(unit, set()).update(acts.split(","))
    return lst, act


def read_path_units():
    rc, o, _ = sh(["systemctl", "list-paths", "--all", "--full", "--no-legend", "--no-pager"], 60)
    act = {}
    for ln in o.splitlines() if rc == 0 else []:
        p = ln.split()
        if len(p) >= 4 and p[-2].endswith(".path"):
            act.setdefault(p[-2], set()).add(p[-1])
    return act


def read_unit_props(units):
    if not units:
        return {}
    rc, o, _ = sh(["systemctl", "show", "--no-pager", "-p", "Id,FragmentPath,What,Where,RequiredBy,LoadState"] + sorted(units), 60)
    if rc != 0:
        raise RuntimeError("systemctl show rc=%s" % rc)
    out = {}
    for blk in o.strip().split("\n\n"):
        d = {}
        for ln in blk.splitlines():
            k, _, v = ln.partition("=")
            d[k] = v
        if d.get("Id"):
            out[d["Id"]] = d
    return out


def read_containers(ephemeral):
    rc, o, _ = sh(["docker", "ps", "-a", "--format", "{{.Names}}"], 60)
    if rc != 0:
        raise RuntimeError("docker ps rc=%s" % rc)
    names = sorted(n for n in o.split() if not any(re.search(e, "docker:" + n) for e in ephemeral))
    out = {}
    for n in names:
        rc, j, _ = sh(["docker", "inspect", "--type", "container", n], 60)
        if rc != 0:
            raise RuntimeError("docker inspect %s rc=%s" % (n, rc))
        d = json.loads(j)[0]
        binds = []
        for port, bs in ((d.get("HostConfig") or {}).get("PortBindings") or {}).items():
            for b in bs or []:
                hp, hi = b.get("HostPort"), b.get("HostIp") or ""
                if hi == "":                                  # HostIp rỗng ⇒ docker mở cả IPv4 lẫn IPv6
                    binds += ["0.0.0.0:%s" % hp, "[::]:%s" % hp]
                else:
                    binds.append(("[%s]:%s" if ":" in hi else "%s:%s") % (hi, hp))
        out[n] = {"id12": d["Id"][:12], "image": (d.get("Config") or {}).get("Image"), "binds": sorted(set(binds))}
    return out


def read_git():
    import glob
    roots = sorted({os.path.dirname(p) for pat in ("/opt/incomex/.git", "/opt/incomex/*/.git", "/opt/incomex/*/*/.git", "/opt/incomex/*/*/*/.git")
                    for p in glob.glob(pat)})
    out = {}
    for r in roots:
        g = os.path.join(r, ".git")
        if os.path.isdir(g):
            gitdir = g
        else:
            try:
                gitdir = open(g).read().split("gitdir:", 1)[1].strip()
            except (OSError, IndexError):
                raise RuntimeError("đọc .git %s" % r)
            gitdir = os.path.normpath(os.path.join(r, gitdir))
        cd = os.path.join(gitdir, "commondir")
        common = os.path.normpath(os.path.join(gitdir, open(cd).read().strip())) if os.path.isfile(cd) else gitdir
        rc, top, _ = sh(["git", "-c", "safe.directory=*", "--no-optional-locks", "-C", r, "rev-parse", "--show-toplevel"], 30)
        rc2, head, _ = sh(["git", "-c", "safe.directory=*", "--no-optional-locks", "-C", r, "rev-parse", "HEAD"], 30)
        if rc != 0:
            raise RuntimeError("git toplevel %s" % r)
        out[r] = {"top": top.strip(), "gitdir": gitdir.rstrip("/"), "common": common.rstrip("/"), "head": head.strip()[:12] if rc2 == 0 else None}
    return out


def code_roots_for(repo_path, loaded, code_caps, tops):
    """Bằng chứng kho→cây mã: CHỈ khi cây mã luật git-head có toplevel = kho này VÀ bản chạy = HEAD (runtime_ok) VÀ vân tay tệp HEAD = bộ đang
    nạp trong Graph. HEAD một mình KHÔNG chứng minh mã chạy (commit mới chưa triển khai ⇒ runtime_ok sai / vân tay khác ⇒ không ghi)."""
    ev = []
    for repo, spec in sorted((loaded or {}).items()):
        if spec.get("rule") != "git-head":
            continue
        c = (code_caps or {}).get(repo) or {}
        if tops.get(repo) == repo_path and c.get("runtime_ok") and c.get("files_tsv_sha256") and \
                c.get("files_tsv_sha256") == (spec.get("loaded") or {}).get("files_tsv_sha256"):
            ev.append("%s@%s" % (repo, c["files_tsv_sha256"][:16]))
    return ev


def desired_infra(cat, code_caps=None, sources=None, run="c1d:infra"):
    """⇒ (nodes {gs_key: {l, p}}, edges {(s,t,d): {t,s,d,p}}, report). code_caps/sources (graph-refresh cap_code + refresh-sources) chỉ để
    ghi thuộc tính bằng chứng kho→cây mã; không có ⇒ thuộc tính vắng (không suy)."""
    c1d = cat.get("c1d") or {}
    declared = list(c1d.get("units_declared") or [])
    exclude = set(c1d.get("units_excluded_pending_owner") or [])
    eph = list(c1d.get("ephemeral_parent_patterns") or []) + [x for c in cat.get("cells") or [] if (c.get("source") or {}).get("adapter") == "c1d"
                                                           for x in (c["source"].get("exclude_patterns") or [])]
    snap = now_iso()
    nodes, edges, rep = {}, {}, {"ambiguous_listeners": [], "excluded_units": sorted(exclude), "snapshot_utc": snap}

    def node(label, nid, props, fam, src):
        k = PREFIX[label] + nid
        p = {"id": nid, "gs_key": k, "gs_layer": "infra", "family": fam, "source": src, "trust": "EXACT_AT_SNAPSHOT", "snapshot_utc": snap, "run": run}
        p.update({a: b for a, b in props.items() if b is not None})
        if k in nodes and nodes[k]["l"] != ["GS", label]:
            raise RuntimeError("nhãn trùng khoá %s" % k)
        nodes.setdefault(k, {"l": ["GS", label], "p": p})["p"].update({a: b for a, b in props.items() if b is not None})
        return k

    def edge(s, t, d, src):
        edges[(s, t, d)] = {"t": t, "s": s, "d": d, "p": {"trust": "EXACT_AT_SNAPSHOT", "snapshot_utc": snap, "source": src, "run": run,
                                                          "gs_edge_key": sha16("%s|%s|%s" % (s, t, d))}}

    # --- G2 container
    ctr = read_containers(eph)
    for n, x in ctr.items():
        node("DockerContainer", n, {"container_id": x["id12"], "image": x["image"]}, "G2", "docker inspect")
    # --- G5 listener → chủ
    lis, holders = read_listeners(), _fd_holders()
    sock_listen, sock_act = read_socket_units()
    listen_unit = {}
    for u, ls in sock_listen.items():
        for l_ in ls:
            listen_unit.setdefault(l_, set()).add(u)
    owner_units = set()
    for addr in sorted(lis):
        node("NetListener", addr, {}, "G5", "ss -ltne + /proc/*/fd")
        pids = set().union(*(holders.get(i, set()) for i in lis[addr]))
        got = 0
        for pid in sorted(pids):
            if pid == 1:
                for u in sorted(listen_unit.get(addr, ())):
                    if u in exclude:
                        continue
                    owner_units.add(u)
                    edge(PREFIX["SystemdUnit"] + u, "LISTENS_ON", PREFIX["NetListener"] + addr, "systemd pid1 fd + list-sockets")
                    got += 1
                continue
            comm, cg = _proc(pid)
            if comm is None:
                continue
            if comm == "docker-proxy":
                for n, x in ctr.items():
                    if addr in x["binds"]:
                        edge(PREFIX["NetListener"] + addr, "PUBLISHED_BY", PREFIX["DockerContainer"] + n, "docker-proxy fd + PortBindings")
                        got += 1
                continue
            u = cg.rstrip("/").split("/")[-1]
            if cg.startswith("/system.slice/") and u.endswith(".service") and u not in exclude:
                owner_units.add(u)
                edge(PREFIX["NetListener"] + addr, "BOUND_BY_PROCESS_OF", PREFIX["SystemdUnit"] + u, "/proc/<pid>/fd + cgroup")
                got += 1
        if not got:
            rep["ambiguous_listeners"].append(addr)
    # --- G3 unit khai báo → đích
    path_act = read_path_units()
    names = set(owner_units) | set(declared)
    for u in declared:
        if u in exclude:
            continue
        for t in sorted(sock_act.get(u, set()) | path_act.get(u, set())):
            if t not in exclude:
                edge(PREFIX["SystemdUnit"] + u, "TRIGGERS", PREFIX["SystemdUnit"] + t, "list-sockets/list-paths ACTIVATES")
                names.add(t)
    props = read_unit_props(names)
    for u in declared:
        if u.endswith(".mount"):
            for s in (props.get(u) or {}).get("RequiredBy", "").split():
                if s not in exclude:
                    edge(PREFIX["SystemdUnit"] + s, "REQUIRES_MOUNT", PREFIX["SystemdUnit"] + u, "systemctl show RequiredBy")
                    names.add(s)
    props.update(read_unit_props(names - set(props)))
    for u in sorted(names):
        x = props.get(u) or {}
        if x.get("LoadState") != "loaded":
            raise RuntimeError("unit không nạp %s" % u)
        node("SystemdUnit", u, {"kind": u.rsplit(".", 1)[-1], "fragment_dir": os.path.dirname(x.get("FragmentPath") or "") or None,
                                "listen": ",".join(sorted(sock_listen.get(u, ()))) or None,
                                "mount_what": (x.get("What") or None) if u.endswith(".mount") else None,
                                "mount_where": (x.get("Where") or None) if u.endswith(".mount") else None}, "G3", "systemctl show + list-sockets")
    # --- G9 kho git
    gits = read_git()
    loaded = ((sources or {}).get("code") or {}).get("repos") or {}
    tops = {}
    for repo, spec in sorted(loaded.items()):
        if spec.get("rule") == "git-head":
            rc, top, _ = sh(["git", "-c", "safe.directory=*", "--no-optional-locks", "-C", spec["root"], "rev-parse", "--show-toplevel"], 30)
            tops[repo] = top.strip() if rc == 0 else None
    for r, x in gits.items():
        ev = code_roots_for(r, loaded, code_caps, tops)
        node("GitRepository", r, {"toplevel": x["top"], "head_at_load": x["head"], "code_roots_evidence": ",".join(ev) or None}, "G9", "git .git/commondir + rev-parse")
    for r, x in gits.items():
        if x["top"] != r and x["top"] in gits:
            edge(PREFIX["GitRepository"] + r, "RESOLVES_TO_TOPLEVEL", PREFIX["GitRepository"] + x["top"], "git rev-parse --show-toplevel")
        if x["gitdir"] != x["common"] and os.path.basename(x["common"]) == ".git":
            own = os.path.dirname(x["common"])
            if own in gits and own != r:
                edge(PREFIX["GitRepository"] + r, "WORKTREE_OF", PREFIX["GitRepository"] + own, "git commondir")
    return nodes, edges, rep


# =========================================================================== lane pgl1 (bộ nạp C1-B, bản chép byte trong bin/refresh)
def _load(name, path):
    ldr = importlib.machinery.SourceFileLoader(name, path)
    m = importlib.util.module_from_spec(importlib.util.spec_from_loader(name, ldr))
    ldr.exec_module(m)
    return m


def desired_pgl1(cat, run="c1d:pgl1"):
    L1 = _load("c1b_l1_lane", RB + "/c1b_l1.py")
    tables = list((cat.get("l1_pilot") or {}).get("tables") or [])
    nat = L1.native(tables)
    nodes, edges, need = L1.build(nat, tables)
    for n in nodes.values():
        n["p"]["run"] = run
    out_e = {}
    for k, e in edges.items():
        e["p"]["run"] = run
        e["p"]["gs_edge_key"] = sha16("%s|%s|%s" % k)
        out_e[k] = e
    return nodes, out_e, {"need_existing": {("|".join(k) if isinstance(k, tuple) else k): v for k, v in need.items()},
                          "snapshot_utc": nat["reader"]["snapshot_utc"], "tables": tables}


# =========================================================================== so khác với Graph (chỉ đọc)
def _ident(p):
    return {k: v for k, v in (p or {}).items() if k not in VOLATILE}


def graph_layer(g, pw, layer):
    rows = g.rows(g.http_cypher([("MATCH (n:GS) WHERE n.gs_layer = $l RETURN n.gs_key AS k, labels(n) AS l, properties(n) AS p", {"l": layer})], pw, timeout=600))
    nodes = {r["k"]: (sorted(r["l"]), r["p"]) for r in rows}
    rel = g.rows(g.http_cypher([("MATCH (a:GS)-[x]->(b:GS) WHERE a.gs_layer = $l OR b.gs_layer = $l RETURN a.gs_key AS s, type(x) AS t, b.gs_key AS d, "
                                 "properties(x) AS p", {"l": layer})], pw, timeout=600))
    edges = {}
    for r in rel:
        edges.setdefault((r["s"], r["t"], r["d"]), []).append(r["p"])
    return nodes, edges


def graph_keys(g, pw, keys):
    out = {}
    keys = sorted(keys)
    for i in range(0, len(keys), 500):
        for r in g.rows(g.http_cypher([("MATCH (n:GS) WHERE n.gs_key IN $k RETURN n.gs_key AS k, labels(n) AS l, n.gs_layer AS layer", {"k": keys[i:i + 500]})],
                                      pw, timeout=300)):
            out[r["k"]] = (sorted(r["l"]), r["layer"])
    return out


def plan(g, pw, lane, nodes, edges, caps, used, extra_check=None):
    """Kế hoạch cộng-thêm ⇒ dict (create/set/stale/problems/F/I). used = {nodes, edges} đã tạo cộng dồn của pilot (trần toàn C1-D)."""
    layer = LAYER[lane]
    gn, ge = graph_layer(g, pw, layer)
    other = graph_keys(g, pw, {k for k in nodes if k not in gn} | {x for e in edges for x in (e[0], e[2]) if x not in gn and x not in nodes})
    problems, create_n, set_n, reuse = [], [], [], []
    for k, n in sorted(nodes.items()):
        if k in gn:
            if gn[k][0] != sorted(n["l"]):
                problems.append("LABEL_CONFLICT %s" % k)
            elif _ident(gn[k][1]) != _ident(n["p"]):
                set_n.append({"k": k, "new": n["p"], "old": gn[k][1]})
        elif k in other:
            if other[k][0] != sorted(n["l"]):
                problems.append("LABEL_CONFLICT_OTHER_LAYER %s %s" % (k, other[k][1]))
            reuse.append(k)                         # nút lane khác: chỉ dùng làm điểm cuối, KHÔNG sửa
        else:
            create_n.append(n)
    exist = set(gn) | set(other) | {n["p"]["gs_key"] for n in create_n}
    create_e, set_e, missing_end = [], [], []
    for key, e in sorted(edges.items()):
        if key[0] not in exist or key[2] not in exist:
            missing_end.append("|".join(key))
            continue
        have = ge.get(key) or []
        if len(have) > 1:
            problems.append("EDGE_ALREADY_MULTI %s" % "|".join(key))
        elif not have:
            create_e.append(e)
        elif _ident(have[0]) != _ident(e["p"]):
            set_e.append({"key": key, "new": e["p"], "old": have[0]})
    if missing_end:
        problems.append("EDGE_ENDPOINT_MISSING %d (vd %s)" % (len(missing_end), missing_end[0]))
    mine = set(gn) | {n["p"]["gs_key"] for n in create_n}
    outside = [e for e in create_e + [x["new"] for x in set_e] if isinstance(e, dict) and "s" in e and e["s"] not in mine and e["d"] not in mine]
    if outside:                                  # cạnh lane phải chạm ít nhất một nút của lane (không tạo quan hệ giữa hai lớp khác)
        problems.append("EDGE_OUTSIDE_LANE %d" % len(outside))
    stale_n = sorted(k for k in gn if k not in nodes)
    lane_t = TYPES[lane]
    stale_e = sorted("|".join(k) for k in ge if k not in edges and k[1] in lane_t and (k[0] in gn or k[2] in gn))
    cap_partial = False
    room_n = max(int(caps.get("nodes", 0)) - int(used.get("nodes", 0)), 0)
    room_e = max(int(caps.get("edges", 0)) - int(used.get("edges", 0)), 0)
    if len(create_n) > room_n or len(create_e) > room_e:      # lấy mẫu tất định theo băm khoá ổn định; phần dư KHÔNG ghi
        cap_partial = True
        create_n = sorted(create_n, key=lambda n: sha16(n["p"]["gs_key"]))[:room_n]
        ok_keys = set(gn) | set(other) | {n["p"]["gs_key"] for n in create_n}
        create_e = [e for e in sorted(create_e, key=lambda e: e["p"]["gs_edge_key"]) if e["s"] in ok_keys and e["d"] in ok_keys][:room_e]
    if extra_check:
        problems += extra_check(gn, other)
    ck = sorted(n["p"]["gs_key"] for n in create_n)
    ek = sorted(e["p"]["gs_edge_key"] for e in create_e)
    F, I = statements(create_n, set_n, create_e, set_e, ck, ek)
    out = {"lane": lane, "layer": layer, "at": now_iso(), "create_nodes": create_n, "set_nodes": set_n, "create_edges": create_e, "set_edges": set_e,
           "reuse_nodes": reuse, "stale_nodes": stale_n, "stale_edges": stale_e, "created_keys": ck, "created_edge_keys": ek, "problems": problems,
           "cap_bound_partial": cap_partial, "caps": caps, "used_before": used,
           "counts": {"nodes_add": len(create_n), "edges_add": len(create_e), "nodes_set": len(set_n), "edges_set": len(set_e), "nodes_delete": 0,
                      "edges_delete": 0, "stale_nodes": len(stale_n), "stale_edges": len(stale_e), "reused": len(reuse)},
           "F": F, "I": I}
    out["sha256"] = hashlib.sha256(json.dumps({k: out[k] for k in ("create_nodes", "set_nodes", "create_edges", "set_edges")}, sort_keys=True,
                                              ensure_ascii=False, default=str).encode()).hexdigest()
    # vân tay DANH TÍNH của kế hoạch (bỏ thuộc tính dễ đổi: snapshot_utc/run/…) — dùng kiểm «nguồn đổi giữa lượt»: đọc lại nguồn chỉ khác dấu
    # giờ chụp ⇒ cùng vân tay; đối tượng/cạnh/thuộc tính danh tính đổi ⇒ khác ⇒ dừng trước ghi
    out["ident_sha256"] = hashlib.sha256(json.dumps({"n": sorted([n["p"]["gs_key"], _ident(n["p"])] for n in create_n),
                                                     "sn": sorted([x["k"], _ident(x["new"])] for x in set_n),
                                                     "e": sorted([e["s"], e["t"], e["d"], _ident(e["p"])] for e in create_e),
                                                     "se": sorted([list(x["key"]), _ident(x["new"])] for x in set_e)},
                                                    sort_keys=True, ensure_ascii=False, default=str).encode()).hexdigest()
    out["empty"] = not (create_n or set_n or create_e or set_e)
    return out


def statements(create_n, set_n, create_e, set_e, ck, ek):
    F, I = [], []
    by = {}
    for n in create_n:
        by.setdefault(tuple(n["l"]), []).append(n["p"])
    for labs, ps in sorted(by.items()):
        lab = ":".join("`%s`" % x.replace("`", "") for x in labs)
        for i in range(0, len(ps), 500):
            F.append(("UNWIND $rows AS p CREATE (n:%s) SET n = p" % lab, {"rows": ps[i:i + 500]}))
    if set_n:
        F.append(("UNWIND $rows AS r MATCH (n:GS {gs_key: r.k}) SET n = r.p", {"rows": [{"k": x["k"], "p": x["new"]} for x in set_n]}))
    bt = {}
    for e in create_e:
        bt.setdefault(e["t"], []).append({"s": e["s"], "d": e["d"], "p": e["p"]})
    for t, rs in sorted(bt.items()):
        for i in range(0, len(rs), 500):
            F.append(("UNWIND $rows AS r MATCH (a:GS {gs_key: r.s}) MATCH (b:GS {gs_key: r.d}) CREATE (a)-[x:`%s`]->(b) SET x = r.p" % t.replace("`", ""),
                      {"rows": rs[i:i + 500]}))
    for x in set_e:
        s, t, d = x["key"]
        F.append(("MATCH (a:GS {gs_key: $s})-[x:`%s`]->(b:GS {gs_key: $d}) SET x = $p" % t.replace("`", ""), {"s": s, "d": d, "p": x["new"]}))
        I.append(("MATCH (a:GS {gs_key: $s})-[x:`%s`]->(b:GS {gs_key: $d}) SET x = $p" % t.replace("`", ""), {"s": s, "d": d, "p": x["old"]}))
    if ek:
        I.insert(0, ("MATCH (:GS)-[x]->(:GS) WHERE x.gs_edge_key IN $k DELETE x", {"k": ek}))
    if set_n:
        I.append(("UNWIND $rows AS r MATCH (n:GS {gs_key: r.k}) SET n = r.p", {"rows": [{"k": x["k"], "p": x["old"]} for x in set_n]}))
    if ck:
        I.append(("MATCH (n:GS) WHERE n.gs_key IN $k DETACH DELETE n", {"k": ck}))
    return F, I


# =========================================================================== chấm độc lập trên một Graph bất kỳ (bản tạm/production)
def score(GC, gmod, pw, cells, only_keys):
    """Máy cấp giấy (graph_cert) chấm các ô lane trên Graph gmod: nguồn đọc lại bằng bộ đọc ô (độc lập với bộ nạp) ⇒ {ô: (trạng thái, lý do)}."""
    S = GC.Sources(cells)
    out = {}
    for c in cells:
        if c["key"] not in only_keys:
            continue
        src = GC.source_for(c, S)
        src.pop("_rowsets", None)
        try:
            if (c.get("graph") or {}).get("l1_anchor"):
                go, ge, gm = GC.graph_l1_read(gmod, pw, c["graph"]["l1_anchor"])
            else:
                go, ge, gm = GC.graph_read(gmod, pw, c["graph"])
            gr = {"objects": go, "edges": ge, "meta": gm}
        except Exception as e:  # noqa: BLE001
            gr = {"error": "%s %s" % (type(e).__name__, str(e)[:120])}
        r = GC.evaluate(c, src, gr, time.time(), 26)
        out[c["key"]] = (r["status"], r.get("reasons"), r.get("diff"))
    return out
