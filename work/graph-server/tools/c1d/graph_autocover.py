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
RETIRE (GS-C1D2-SCOPED-AUTOCOVER-20261026-13, R3/T4): chỉ lane c1d:infra, chỉ khi bộ đọc gốc đọc TRỌN chứng minh đối tượng đã mất — nút
  DockerContainer vắng trong `docker ps -a` (kể cả mẫu tạm) · NetListener vắng trong `ss -ltne` · GitRepository vắng trong lượt quét .git;
  cạnh G5/G9 (BOUND_BY_PROCESS_OF/PUBLISHED_BY/LISTENS_ON/WORKTREE_OF/RESOLVES_TO_TOPLEVEL) khi hai đầu còn sống, cổng nghe không mơ hồ
  mà nguồn không còn cạnh đó (A→B thành A→C), hoặc khi một đầu bị retire. Đánh dấu bằng THUỘC TÍNH trên chính nút/cạnh (gs_status=retired
  + retired_at/retired_reason/retired_by) — không xoá cứng, không đổi nhãn/loại cạnh. Đối tượng quay lại nguồn ⇒ SET thuộc tính nguồn (hồi
  sinh). SystemdUnit/TRIGGERS/REQUIRES_MOUNT/lane pgl1: vắng nguồn KHÔNG chứng minh mất ⇒ giữ `stale` (ô MỘT PHẦN). Nghịch đảo I = đặt lại
  nguyên thuộc tính cũ của phần đã retire.
SYNC-CORE (GS-COV2-SYNC-CORE-20261031-02, ỨNG VIÊN, chưa triển khai): lane `sync:native` hoà giải theo trạng thái — vũ trụ lấy từ catalog nguồn
  (không danh sách vật), khoá có hệ/DB/loại, quota theo LƯỢT (phần dư lượt sau tự bắt kịp, không trần cộng dồn), THÊM/SỬA/gỡ mềm cả nút lẫn cạnh.
  Chỉ gỡ khi bộ đọc đọc TRỌN + oracle K0 độc lập xác nhận; giảm >75% một ô ⇒ chặn và báo. Không có lịch, dịch vụ hay quyền mới.
"""
import hashlib, importlib.machinery, importlib.util, json, os, re, subprocess, time

ROOT = "/opt/incomex/graph-server/prod-v1"
RB = ROOT + "/bin/refresh"
NATIVE_LANE = "sync:native"
NS = "native:"                                       # khoá hệ/DB/loại riêng: lane cũ giữ nguyên tới khi có bằng chứng migration, không đụng nhau
LAYER = {"c1d:infra": "infra", "c1d:pgl1": "pgl1", NATIVE_LANE: "native"}
PREFIX = {"NetListener": "net:listen:", "SystemdUnit": "systemd:unit:", "DockerContainer": "docker:container:", "GitRepository": "git:repo:"}
LABELS = {"c1d:infra": {"GS", "NetListener", "SystemdUnit", "DockerContainer", "GitRepository"},
          "c1d:pgl1": {"GS", "PgTable", "PgView", "PgForeignKey", "DirectusCollection", "DirectusRelation", "DirectusPermission"}}
TYPES = {"c1d:infra": {"BOUND_BY_PROCESS_OF", "PUBLISHED_BY", "LISTENS_ON", "TRIGGERS", "REQUIRES_MOUNT", "WORKTREE_OF", "RESOLVES_TO_TOPLEVEL"},
         "c1d:pgl1": {"HAS_FK", "REFERENCES", "DEPENDS_ON", "MAPS_TO_TABLE", "RELATION_MANY", "RELATION_ONE", "PERMISSION_ON"},
         NATIVE_LANE: {"ON_TABLE", "EXECUTES", "HAS_FK", "REFERENCES", "DEPENDS_ON", "CALLS", "USES_SERVER", "REFERS_IN_BODY", "OPERATION_OF", "PERMISSION_ON",
                       "BRANCH_OF", "AT_COMMIT", "IN_COMMIT", "REFERS_IN_FILE"}}
VOLATILE = {"snapshot_utc", "run", "loaded_at", "gs_edge_key", "head_at_load", "source_file"}   # không thuộc danh tính khi so khác
RETIRED = "retired"                                  # C1-D2 R3: gs_status của nút/cạnh đã mất ở nguồn (chứng minh bằng bộ đọc trọn)
RETIRE = {"c1d:infra": {"labels": {"DockerContainer": "docker ps -a", "NetListener": "ss -ltne", "GitRepository": "quét .git"},
                        # loại cạnh ⇒ vị trí đầu CHỦ THỂ (bộ đọc trọn của đầu này quyết toàn bộ cạnh loại đó của nó): cổng nghe / kho git
                        "subject": {"BOUND_BY_PROCESS_OF": 0, "PUBLISHED_BY": 0, "LISTENS_ON": 2, "WORKTREE_OF": 0, "RESOLVES_TO_TOPLEVEL": 0},
                        "listener_types": {"BOUND_BY_PROCESS_OF", "PUBLISHED_BY", "LISTENS_ON"}}}
now_iso = lambda: time.strftime("%FT%TZ", time.gmtime())


def is_retired(p):
    return (p or {}).get("gs_status") == RETIRED


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


def read_containers(ephemeral, seen=None):
    rc, o, _ = sh(["docker", "ps", "-a", "--format", "{{.Names}}"], 60)
    if rc != 0:
        raise RuntimeError("docker ps rc=%s" % rc)
    if seen is not None:                              # C1-D2 R3: MỌI tên (kể cả mẫu tạm) — chỉ vắng ở đây mới chứng minh container đã mất
        seen.extend(o.split())
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
    seen = []
    ctr = read_containers(eph, seen)
    rep["retire_proof"] = {"containers_all": sorted(set(seen)), "readers": dict(RETIRE["c1d:infra"]["labels"])}
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


# =========================================================================== lane sync:native (1) khai báo nguồn: LOẠI, không danh sách vật
RELKIND = {"r": ("table", "PgTable"), "p": ("table", "PgTable"), "f": ("foreign_table", "PgTable"), "v": ("view", "PgView"), "m": ("matview", "PgView"),
           "S": ("sequence", "PgSequence")}
REL_NOT_LOADED = {"i", "I", "c"}                     # chỉ mục, kiểu composite: nằm trong catalog nhưng chưa có lớp ⇒ ghi GAP, không bỏ im
PG_COL = {"schema": "name", "rel": "kind schema name owner ext hash tup ncol rls", "func": "schema name args lang vol kind hash ext owner secdef argtypes",
          "trigger": "schema tab name enabled fschema fname fargs", "evttrigger": "name event enabled fn", "fk": "schema tab name fschema ftab validated",
          "viewdep": "schema name kind dschema dname dkind", "viewfunc": "schema name fschema fname", "extension": "name ver nsp owner",
          "fdwserver": "name fdw", "ftable": "schema tab server", "rule": "schema tab name", "rlspolicy": "schema tab name"}
PG_NO_NODE = {"meta", "constraint", "publication", "subscription_count", "depcount", "shdepcount"}
DT_COL = {"dcol": "id group singleton hidden", "dfield": "coll field interface", "drel": "coll field one_coll one_field",
          "dflow": "id name status trigger acc created hash", "dop": "id flow type key hash resolve reject", "dpolicy": "id name admin app", "drole": "id name",
          "daccess": "id role user policy", "dperm": "id coll action policy hash"}
DT_NO_NODE = {"dcount", "dwindow", "dflowact"}
RUNTIME_ERR = (("list-units", "systemd"), ("unit-files", "systemd"), ("timers", "systemd"), ("docker", "docker"), ("inspect", "docker"), ("ss", "net"), ("nginx", "nginx"))
TRANSIENT_UNIT = re.compile(r"^(session-\d+\.scope|run-.*)$")   # phiên ssh/lệnh tạm: sinh rồi mất giữa hai lượt, không phải vật của hệ thống
SECRET_RE = re.compile(r"(gh[pousr]_[A-Za-z0-9]{16,}|github_pat_\w{16,}|\bsk-[\w-]{16,}|xox[baprs]-[\w-]{10,}|eyJ[\w-]{10,}\.[\w-]{10,}|AKIA[0-9A-Z]{16}|"
                       r"://[^/\s:]+:[^@/\s]+@|(?i:password|passwd|secret|token|api[_-]?key)\s*[=:]\s*\S{6,})")
FULL, PARTIAL, STALE = "FULL", "PARTIAL", "STALE"
DROP_PROOF, DROP_BLOCK = 0.30, 0.75                  # ≥30%: ghi bằng chứng; >75% một ô: chặn và báo (không phải giấy phép gỡ dưới mức này)


def family_of(i):
    """Họ nguồn theo khoá: pg:<db> · directus · cron · systemd · docker · net · nginx · github."""
    p = (i[len(NS):] if i.startswith(NS) else i).split(":")
    return "pg:" + p[1] if p[0] == "pg" else p[0]


def _clean(v):
    return ("sha16:" + sha16(v)) if isinstance(v, str) and SECRET_RE.search(v) else v


def _rows(path, col, seen):
    out = {}
    for ln in open(path, encoding="utf-8", errors="replace"):
        f = ln.rstrip("\n").split("\t")
        seen.add(f[0])
        if f[0] in col:
            out.setdefault(f[0], []).append(dict(zip(col[f[0]].split(), f[1:])))
    return out


def _file_ok(path, err=None, must=None):
    """Bằng chứng đọc trọn của một tệp nguồn: có, không rỗng, stderr rỗng, dòng cuối của bộ đọc có mặt. Lý do lỗi hoặc None."""
    if not os.path.isfile(path) or not os.path.getsize(path):
        return "MISSING_OR_EMPTY " + os.path.basename(path)
    if err and os.path.isfile(err) and os.path.getsize(err):
        return "READER_STDERR " + open(err, errors="replace").read(120).strip()
    if must and must not in open(path, errors="replace").read():
        return "TRUNCATED no " + must.strip()
    return None


def read_universe(T, tag, gh=None):
    """Đọc ảnh catalog gốc (cat-/dt-/runtime-/derived- của K0, gh tuỳ chọn) ⇒ nodes, edges, sources {họ: {status, why}}, gaps. Họ không đọc trọn ⇒ 0 hàng."""
    import glob
    nodes, edges, src, gaps = {}, {}, {}, []
    snap = open(T + "/at.txt").read().strip().split("=")[-1] if os.path.isfile(T + "/at.txt") else tag

    def node(fam, cls, label, i, **a):
        nodes[NS + i] = {"l": ["GS", label], "p": dict({k: _clean(v) for k, v in a.items() if v is not None}, id=i, gs_key=NS + i, gs_layer="native", family=fam, cls=cls,
                                                  evidence="NATIVE", trust="EXACT_AT_SNAPSHOT", snapshot_utc=snap, run=NATIVE_LANE)}

    def edge(s, t, d, ev="NATIVE"):
        s, d = NS + s, NS + d
        edges[(s, t, d)] = {"t": t, "s": s, "d": d, "p": {"family": family_of(s), "evidence": ev, "trust": "EXACT_AT_SNAPSHOT", "snapshot_utc": snap, "run": NATIVE_LANE,
                                                         "gs_edge_key": sha16("%s|%s|%s" % (s, t, d))}}

    for path in sorted(glob.glob("%s/cat-%s-*.tsv" % (T, tag))):
        db = os.path.basename(path)[len("cat-%s-" % tag):-4]
        fam = "pg:" + db
        why = _file_ok(path, "%s/cat-%s.err" % (T, db), "depcount\t")
        src[fam] = {"status": PARTIAL if why else FULL, "why": why}
        if why:
            continue
        seen = set()
        c = _rows(path, PG_COL, seen)
        for k in sorted(seen - set(PG_COL) - PG_NO_NODE):
            src[fam].update(status=PARTIAL, why="NEW_CLASS_UNHANDLED " + k)
            gaps.append("%s NEW_CLASS_UNHANDLED %s" % (fam, k))
        key = lambda cls, sch, nm: "pg:%s:%s:%s.%s" % (db, cls, sch, nm)
        kind = {}
        for r in c.get("rel", []):
            if r["ext"] != "false":
                continue
            if r["kind"] in REL_NOT_LOADED:
                continue
            if r["kind"] not in RELKIND:
                src[fam].update(status=PARTIAL, why="NEW_CLASS_UNHANDLED relkind " + r["kind"])
                gaps.append("%s NEW_RELKIND %s" % (fam, r["kind"]))
                continue
            cls, label = RELKIND[r["kind"]]
            kind[(r["schema"], r["name"])] = cls
            node(fam, cls, label, key(cls, r["schema"], r["name"]), hash=r["hash"], owner=r["owner"], ncol=r["ncol"], relkind=r["kind"])
        fsig = {}
        for r in c.get("func", []):
            if r["ext"] == "false":
                node(fam, "function", "PgFunction", key("function", r["schema"], "%s(%s)" % (r["name"], r["args"])), hash=r["hash"], lang=r["lang"], vol=r["vol"],
                     kind=r["kind"], secdef=r["secdef"])
                fsig.setdefault((r["schema"], r["name"]), []).append(r["args"])
        for r in c.get("trigger", []):
            i = "pg:%s:trigger:%s.%s.%s" % (db, r["schema"], r["tab"], r["name"])
            node(fam, "trigger", "PgTrigger", i, enabled=r["enabled"])
            edge(i, "ON_TABLE", key(kind.get((r["schema"], r["tab"]), "table"), r["schema"], r["tab"]))
            edge(i, "EXECUTES", key("function", r["fschema"], "%s(%s)" % (r["fname"], r["fargs"])))
        for r in c.get("fk", []):
            i = "pg:%s:fk:%s.%s.%s" % (db, r["schema"], r["tab"], r["name"])
            node(fam, "fk", "PgForeignKey", i, validated=r["validated"])
            edge(key("table", r["schema"], r["tab"]), "HAS_FK", i)
            edge(i, "REFERENCES", key("table", r["fschema"], r["ftab"]))
        dep = {"r": "table", "p": "table", "f": "foreign_table", "v": "view", "m": "matview", "S": "sequence", "i": "index", "I": "index", "c": "type"}
        for r in c.get("viewdep", []):
            edge(key(dep[r["kind"]], r["schema"], r["name"]), "DEPENDS_ON", key(dep.get(r["dkind"], "?"), r["dschema"], r["dname"]))
        for r in c.get("viewfunc", []):
            for a in fsig.get((r["fschema"], r["fname"]), []):
                edge(key("view", r["schema"], r["name"]), "CALLS", key("function", r["fschema"], "%s(%s)" % (r["fname"], a)))
        for r in c.get("evttrigger", []):
            node(fam, "event_trigger", "PgEventTrigger", "pg:%s:event_trigger:%s" % (db, r["name"]), enabled=r["enabled"])
        for r in c.get("schema", []):
            node(fam, "schema", "PgSchema", "pg:%s:schema:%s" % (db, r["name"]))
        for r in c.get("extension", []):
            node(fam, "extension", "PgExtension", "pg:%s:extension:%s" % (db, r["name"]), ver=r["ver"], owner=r["owner"])
        for r in c.get("rlspolicy", []):
            node(fam, "rls_policy", "PgRlsPolicy", "pg:%s:rls:%s.%s.%s" % (db, r["schema"], r["tab"], r["name"]))
        for r in c.get("rule", []):
            node(fam, "rule", "PgRule", "pg:%s:rule:%s.%s.%s" % (db, r["schema"], r["tab"], r["name"]))
        for r in c.get("fdwserver", []):
            node(fam, "fdw_server", "PgFdwServer", "pg:%s:server:%s" % (db, r["name"]))
        for r in c.get("ftable", []):
            edge(key("foreign_table", r["schema"], r["tab"]), "USES_SERVER", "pg:%s:server:%s" % (db, r["server"]))
    if not any(k.startswith("pg:") for k in src):
        src["pg"] = {"status": PARTIAL, "why": "NO_CATALOG"}
    der = "%s/derived-%s.jsonl" % (T, tag)
    if os.path.isfile(der):
        for ln in open(der):
            x = json.loads(ln)
            if src.get("pg:" + x["db"], {}).get("status") == FULL:
                edge("pg:%s:function:%s" % (x["db"], x["f"]), x.get("t", "REFERS_IN_BODY"), "pg:%s:table:%s" % (x["db"], x["r"]), "DERIVED")
    else:
        gaps.append("pg DERIVED_NOT_READ")
    dtp = "%s/dt-%s.tsv" % (T, tag)
    why = _file_ok(dtp, T + "/dt.err", "dperm\t")
    src["directus"] = {"status": PARTIAL if why else FULL, "why": why}
    if not why:
        seen = set()
        d = _rows(dtp, DT_COL, seen)
        for k in sorted(seen - set(DT_COL) - DT_NO_NODE):
            src["directus"].update(status=PARTIAL, why="NEW_CLASS_UNHANDLED " + k)
            gaps.append("directus NEW_CLASS_UNHANDLED " + k)
        for r in d.get("dcol", []):
            node("directus", "directus_collection", "DirectusCollection", "directus:collection:" + r["id"])
        for r in d.get("dfield", []):
            node("directus", "directus_field", "DirectusField", "directus:field:%s.%s" % (r["coll"], r["field"]))
        for r in d.get("drel", []):
            node("directus", "directus_relation", "DirectusRelation", "directus:relation:%s.%s" % (r["coll"], r["field"]))
        for r in d.get("dflow", []):
            node("directus", "directus_flow", "DirectusFlow", "directus:flow:" + r["id"], name=r["name"], status=r["status"], trigger=r["trigger"], hash=r["hash"])
        for r in d.get("dop", []):
            node("directus", "directus_operation", "DirectusOperation", "directus:operation:" + r["id"], type=r["type"], hash=r["hash"])
            edge("directus:operation:" + r["id"], "OPERATION_OF", "directus:flow:" + r["flow"])
        for r in d.get("dpolicy", []):
            node("directus", "directus_policy", "DirectusPolicy", "directus:policy:" + r["id"], admin=r["admin"])
        for r in d.get("drole", []):
            node("directus", "directus_role", "DirectusRole", "directus:role:" + r["id"])
        for r in d.get("daccess", []):
            node("directus", "directus_access", "DirectusAccess", "directus:access:" + r["id"])
        for r in d.get("dperm", []):
            node("directus", "directus_permission", "DirectusPermission", "directus:permission:" + r["id"], coll=r["coll"], action=r["action"], hash=r["hash"])
            edge("directus:permission:" + r["id"], "PERMISSION_ON", "directus:collection:" + r["coll"])
    rtp = "%s/runtime-%s.json" % (T, tag)
    why = _file_ok(rtp, None, None)
    rt = None
    if not why:
        try:
            rt = json.load(open(rtp))
        except ValueError as e:
            why = "JSON " + str(e)[:80]
    for f in ("cron", "systemd", "docker", "net", "nginx"):
        src[f] = {"status": PARTIAL if why else FULL, "why": why}
    if rt:
        for e in rt.get("errors") or []:
            fam = next((f for pre, f in RUNTIME_ERR if str(e.get("where")).startswith(pre)), "cron")
            src[fam].update(status=PARTIAL, why="%s rc=%s" % (e.get("where"), e.get("rc")))
        ok = lambda f: src[f]["status"] == FULL
        for c in rt.get("cron", []) if ok("cron") else []:
            node("cron", "cron_entry", "CronEntry", "cron:%s:%s:%s" % (c["src"], c["user"], c["line"]), state="DISABLED" if c["disabled"] else "ENABLED", hash=c["sha"], head=c.get("cmd_head"))
        if ok("systemd"):
            for u in rt.get("units", []):
                if not TRANSIENT_UNIT.match(u["unit"]):
                    node("systemd", "systemd_unit", "SystemdUnit", "systemd:unit:" + u["unit"], active=u["active"], sub=u["sub"], load=u["load"])
            for u in rt.get("unit_files", []):
                if NS + "systemd:unit:" + u["unit"] not in nodes and not TRANSIENT_UNIT.match(u["unit"]):
                    node("systemd", "systemd_unit", "SystemdUnit", "systemd:unit:" + u["unit"], active="not-loaded", ufs=u.get("state"))
            for d in rt.get("dropins", []):
                node("systemd", "systemd_dropin", "SystemdDropin", "systemd:dropin:" + d)
        for c in rt.get("containers", []) if ok("docker") else []:
            node("docker", "docker_container", "DockerContainer", "docker:container:" + c["name"], state=c["state"], image=c["image_id"])
        for x in rt.get("listeners", []) if ok("net") else []:
            node("net", "net_listener", "NetListener", "net:%s:%s" % (x["proto"], x["listen"]), procs=",".join(x["procs"]))
        if ok("nginx") and rt.get("nginx"):
            for s in rt["nginx"]["server_names"]:
                node("nginx", "nginx_server_name", "NginxServerName", "nginx:server_name:" + s)
            for u in rt["nginx"]["upstream_targets"]:
                node("nginx", "nginx_upstream", "NginxUpstream", "nginx:upstream:" + u)
    if gh is not None:
        read_github_into(gh, node, edge, src, gaps)
    return {"nodes": nodes, "edges": edges, "sources": src, "gaps": gaps, "snapshot_utc": snap}


def read_github_into(gh, node, edge, src, gaps):
    """GitHub mức 1: repo/nhánh/commit/tệp (đường + băm blob, không nội dung), kể cả kho lưu trữ. Commit→container KHÔNG suy: cần digest/biên nhận deploy."""
    bad = gh.get("errors") or [r["name"] for r in gh.get("repos", []) if r.get("truncated")]
    src["github"] = {"status": PARTIAL if bad else FULL, "why": str(bad)[:120] if bad else None}
    gaps.append("github COMMIT_TO_CONTAINER SOURCE_IDENTITY_UNVERIFIED")
    if bad:
        return
    for r in gh.get("repos", []):
        rk = "github:repo:" + r["name"]
        node("github", "github_repo", "GitHubRepo", rk, archived=str(r["archived"]))
        if not r.get("branch") or not r.get("head"):
            continue
        bk, ck = "github:branch:%s:%s" % (r["name"], r["branch"]), "github:commit:%s:%s" % (r["name"], r["head"])
        node("github", "github_branch", "GitHubBranch", bk)
        node("github", "github_commit", "GitHubCommit", ck)
        edge(bk, "BRANCH_OF", rk)
        edge(bk, "AT_COMMIT", ck)
        for f in r["files"]:
            fk = "github:file:%s:%s" % (r["name"], f["p"])
            node("github", "github_file", "GitHubFile", fk, blob=f["h"])
            edge(fk, "IN_COMMIT", bk)


def derive_file_refs(path_key, text, native_names):
    """Tên lấy từ catalog nguồn, không gõ sẵn ⇒ cạnh REFERS_IN_FILE nhãn DERIVED: có nhắc tên, KHÔNG chứng minh mã chạy gọi tới."""
    words = set(re.findall(r"[A-Za-z_][A-Za-z0-9_]{3,}", text))
    return sorted((path_key, "REFERS_IN_FILE", k) for n, k in native_names.items() if n in words)


# =========================================================================== lane sync:native (2) cổng gỡ theo ô nguồn×loại
def _gate_cell(cell, gone, active, srcs, oracle):
    """Lý do KHÔNG được gỡ ô này, hoặc None. Giảm >75% luôn chặn, dù đọc đủ."""
    fam = cell[0]
    if (srcs.get(fam) or {}).get("status") != FULL:
        return "SOURCE_NOT_FULL %s" % ((srcs.get(fam) or {}).get("why"),)
    if len(gone) / max(len(active), 1) > DROP_BLOCK:
        return "MASS_DROP_BLOCKED %d/%d" % (len(gone), len(active))
    o = (oracle or {}).get(fam) or {}
    if not o.get("ok"):
        return "ORACLE_NOT_CONFIRMED %s" % (o.get("why"),)
    if cell[1] in (o.get("disagree") or ()):
        return "ORACLE_ANGLE_DISAGREE " + cell[1]
    seen = set(gone) & {NS + i for i in o.get("ids") or ()}
    if seen:
        return "ORACLE_STILL_SEES %d" % len(seen)
    return None


def retire_native(gn, ge, nodes, edges, native):
    srcs, oracle = native.get("sources") or {}, native.get("oracle") or {}
    gate = native.setdefault("retire_gate", {"held": {}, "alerts": [], "large_drop_proof": {}, "human_hold": []})
    by = {}
    for k, v in gn.items():
        if not is_retired(v[1]):
            by.setdefault((v[1].get("family") or family_of(k), v[1].get("cls") or "?"), []).append(k)
    rn = []
    for cell, active in sorted(by.items()):
        gone = sorted(k for k in active if k not in nodes)
        if not gone:
            continue
        why = _gate_cell(cell, gone, active, srcs, oracle)
        name = "%s|%s" % cell
        if why:
            gate["held"][name] = why
            if why.startswith("MASS_DROP"):
                gate["alerts"].append(name + " " + why)
            continue
        if len(gone) / len(active) >= DROP_PROOF:
            gate["large_drop_proof"][name] = {"gone": len(gone), "active": len(active), "proof": "FULL_READ+K0_ORACLE"}
        rn += [{"k": k, "old": gn[k][1], "reader": name} for k in gone]
    dead = {x["k"] for x in rn} | {k for k, v in gn.items() if is_retired(v[1])}
    held_keys = {k for cell, a in by.items() if "%s|%s" % cell in gate["held"] for k in a if k not in nodes}
    by_e = {}
    for key, have in ge.items():
        if key[1] in TYPES[NATIVE_LANE] and len(have) == 1 and not is_retired(have[0]):
            by_e.setdefault((have[0].get("family") or family_of(key[0]), key[1]), []).append(key)
    re_ = []
    for cell, active in sorted(by_e.items()):
        gone = [k for k in active if k not in edges]
        if not gone:
            continue
        why = _gate_cell(cell, gone, active, srcs, {cell[0]: dict((oracle.get(cell[0]) or {}), ids=())})
        name = "%s|%s" % cell
        for key in sorted(gone):
            p = ge[key][0]
            if p.get("evidence") == "HUMAN" or p.get("human_approved"):          # quan hệ người duyệt: không tự gỡ, báo để người xử lý
                gate["human_hold"].append("|".join(key))
            elif key[0] in held_keys or key[2] in held_keys:                     # đầu nút đang bị giữ ⇒ cạnh giữ theo
                gate["held"].setdefault(name, "ENDPOINT_HELD")
            elif key[0] in dead or key[2] in dead:
                re_.append({"key": key, "old": p, "why": "ENDPOINT_RETIRED"})
            elif why:
                gate["held"][name] = why
            elif "|".join((key[0][len(NS):], key[1], key[2][len(NS):])) in ((oracle.get(cell[0]) or {}).get("edges") or ()):
                gate["held"][name] = "ORACLE_STILL_SEES_EDGE"
            else:
                re_.append({"key": key, "old": p, "why": "SOURCE_EDGE_ABSENT_FULL_READ " + name})
    return rn, re_, ("; ".join(sorted(gate["held"])) or None)


# =========================================================================== lane sync:native (3) oracle hai chiều + giấy theo ô
def oracle_diff(k_nodes, k_edges, gn, ge, families):
    """So tập khoá oracle (K0, parser riêng) ↔ Graph đang sống theo họ: id, loại, cạnh+loại+chiều, hai chiều. Cạnh treo ở nguồn ⇒ đếm riêng."""
    bare = lambda k: k[len(NS):] if k.startswith(NS) else k
    live_n = {bare(k): v[1].get("cls") for k, v in gn.items() if not is_retired(v[1])}
    live_e = {(bare(k[0]), k[1], bare(k[2])) for k, v in ge.items() if v and not all(is_retired(p) for p in v)}
    src_n = {n["id"]: n["cls"] for n in k_nodes if not TRANSIENT_UNIT.match(n["id"].rsplit(":", 1)[-1])}
    src_e, dangling = set(), 0
    for e in k_edges:
        if e["s"] in src_n and e["d"] in src_n:
            src_e.add((e["s"], e["t"], e["d"]))
        else:
            dangling += 1
    out = {}
    for f in families:
        fn = lambda d: {k for k in d if family_of(k) == f}
        fe = lambda d: {k for k in d if family_of(k[0]) == f}
        a, b, c, d = fn(src_n), fn(live_n), fe(src_e), fe(live_e)
        out[f] = {"only_source": sorted(a - b), "only_graph": sorted(b - a), "type_mismatch": sorted(k for k in a & b if src_n[k] != live_n[k]),
                  "edge_only_source": sorted("|".join(k) for k in c - d), "edge_only_graph": sorted("|".join(k) for k in d - c), "nodes": len(b), "edges": len(d)}
        out[f]["ok"] = not (out[f]["only_source"] or out[f]["only_graph"] or out[f]["type_mismatch"] or out[f]["edge_only_source"] or out[f]["edge_only_graph"])
    return {"families": out, "source_dangling_edges": dangling}


def source_cert(uni, diff, pl, state, now_ts, ttl_h=26, oracle=None):
    """Giấy theo nguồn×loại, dùng state sẵn có (refresh-sources) cho thế hệ/lần đạt cuối. Thế hệ chỉ tăng khi đọc trọn + kế hoạch ghi hết + oracle khớp."""
    gate = pl.get("retire_gate") or {}
    cells, fam_cls = {}, {}
    for n in uni["nodes"].values():
        fam_cls.setdefault(n["p"]["family"], set()).add(n["p"]["cls"])
    for f, s in sorted(uni["sources"].items()):
        o = (diff.get("families") or {}).get(f) or {}
        held = sorted(k for k in gate.get("held", {}) if k.split("|")[0] == f)
        if s["status"] != FULL:
            st, why = PARTIAL, s.get("why")
        elif pl.get("problems"):
            st, why = PARTIAL, "PLAN_PROBLEM %s" % pl["problems"][0]
        elif held:
            st, why = PARTIAL, gate["held"][held[0]]
        elif pl.get("quota_left"):
            st, why = PARTIAL, "QUOTA_RESUME %d" % pl["quota_left"]
        elif f != "github" and not o.get("ok"):
            st, why = PARTIAL, "ORACLE_MISMATCH"
        elif (oracle or {}).get(f) and not oracle[f].get("ok"):
            st, why = PARTIAL, "ORACLE_NOT_CONFIRMED %s" % (oracle[f].get("why"),)
        else:
            st, why = FULL, None
        rec = state.setdefault(f, {"generation": 0, "last_success": None})
        if st == FULL:
            rec.update(generation=rec["generation"] + 1, last_success=now_ts)
        elif rec["last_success"] is not None and now_ts - rec["last_success"] > ttl_h * 3600:
            st, why = STALE, "LAST_SUCCESS_OLDER_THAN_%dH" % ttl_h
        cells[f] = {"status": st, "why": why, "classes": sorted(fam_cls.get(f, ())), "generation": rec["generation"], "last_success": rec["last_success"]}
    ev = {}
    for e in uni["edges"].values():
        ev[e["p"]["evidence"]] = ev.get(e["p"]["evidence"], 0) + 1
    return {"cells": cells, "gaps": uni["gaps"], "edge_evidence": ev, "alerts": gate.get("alerts", []),
            "actionability": "ACTION_SAFE_IN_SCOPE" if all(c["status"] == FULL for c in cells.values()) and not uni["gaps"] else "NOT_ACTION_SAFE"}


# R7 CHỈ THIẾT KẾ, tắt mặc định, chưa nối vào graph-refresh: Graph là chỉ mục suy từ nguồn nên chỉ các cổng thuộc chính nó mới được bỏ lượt. Owner quyết.
GATE_SCOPED = {"khoa_rieng", "vps_ghi", "ram", "dia", "neo4j", "tien_trinh_ghi", "stop", "guard_graph"}


def gate_decision(bad, r7=False):
    relevant = set(bad) & GATE_SCOPED if r7 else set(bad)
    return {"decision": "SKIP" if relevant else "GO", "blocking": sorted(relevant), "ignored": sorted(set(bad) - relevant)}


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


def retire_plan(lane, gn, ge, nodes, edges, other, native):
    """C1-D2 R3: phần stale CHỨNG MINH được là đã mất ⇒ (nút retire [{k, old}], cạnh retire [{key, old}], lý do giữ stale). native = báo cáo
    bộ đọc gốc của lượt (desired_*); thiếu ⇒ không retire gì."""
    if lane == NATIVE_LANE:
        return retire_native(gn, ge, nodes, edges, native or {})
    rule = RETIRE.get(lane)
    if not rule or not isinstance(native, dict) or "retire_proof" not in native:
        return [], [], "lane/bộ đọc không chứng minh được vắng mặt"
    all_ctr = set((native.get("retire_proof") or {}).get("containers_all") or [])
    amb = {"net:listen:" + a for a in native.get("ambiguous_listeners") or []}
    lab = lambda k: next((x for x in gn[k][0] if x != "GS"), None)
    rn = []
    for k in sorted(k for k in gn if k not in nodes and not is_retired(gn[k][1])):
        lb = lab(k)
        if lb not in rule["labels"]:
            continue
        if lb == "DockerContainer" and str(gn[k][1].get("id")) in all_ctr:   # còn trong docker ps -a (mẫu tạm bị lọc) ⇒ chưa chứng minh mất
            continue
        rn.append({"k": k, "old": gn[k][1], "reader": rule["labels"][lb]})
    gone = {x["k"] for x in rn}
    re_ = []
    for key in sorted(ge):
        have = ge[key]
        if key in edges or len(have) != 1 or is_retired(have[0]) or key[1] not in TYPES[lane] or not (key[0] in gn or key[2] in gn):
            continue
        if key[0] in gone or key[2] in gone:
            re_.append({"key": key, "old": have[0], "why": "ENDPOINT_RETIRED"})
            continue
        pos = rule["subject"].get(key[1])
        subj = key[pos] if pos is not None else None
        # đầu chủ thể còn sống trong lượt đọc trọn này (có trong tập nguồn) và không mơ hồ ⇒ nguồn đã nói đủ cạnh của nó ⇒ cạnh vắng = đã mất
        if subj and subj in nodes and not (key[1] in rule["listener_types"] and subj in amb):
            re_.append({"key": key, "old": have[0], "why": "SOURCE_EDGE_ABSENT_SUBJECT_FULLY_READ " + subj})
    return rn, re_, None


def plan(g, pw, lane, nodes, edges, caps, used=None, extra_check=None, native=None):
    """Kế hoạch ⇒ dict (create/set/retire/stale/problems/F/I). caps = quota MỖI LƯỢT {nodes, edges}: phần dư để lượt sau (cap_bound_partial), không
    trần cộng dồn; used giữ chữ ký cũ, không còn dùng. native = báo cáo bộ đọc gốc (desired_*) — C1-D2 R3 chỉ retire khi báo cáo chứng minh vắng mặt."""
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
    if missing_end and lane != NATIVE_LANE:     # lane native: nguồn có cạnh treo (194 quyền trỏ collection vắng) ⇒ GAP, không chặn cả lượt
        problems.append("EDGE_ENDPOINT_MISSING %d (vd %s)" % (len(missing_end), missing_end[0]))
    mine = set(gn) | {n["p"]["gs_key"] for n in create_n}
    outside = [e for e in create_e + [x["new"] for x in set_e] if isinstance(e, dict) and "s" in e and e["s"] not in mine and e["d"] not in mine]
    if outside:                                  # cạnh lane phải chạm ít nhất một nút của lane (không tạo quan hệ giữa hai lớp khác)
        problems.append("EDGE_OUTSIDE_LANE %d" % len(outside))
    lane_t = TYPES[lane]
    retire_n, retire_e, retire_why = retire_plan(lane, gn, ge, nodes, edges, other, native) if not problems else ([], [], "kế hoạch có vấn đề")
    rk, rek = {x["k"] for x in retire_n}, {x["key"] for x in retire_e}
    old_ret_n = sorted(k for k in gn if k not in nodes and is_retired(gn[k][1]))
    old_ret_e = sorted("|".join(k) for k in ge if k not in edges and k[1] in lane_t and ge[k] and all(is_retired(p) for p in ge[k]))
    stale_n = sorted(k for k in gn if k not in nodes and k not in rk and not is_retired(gn[k][1]))
    stale_e = sorted("|".join(k) for k in ge if k not in edges and k[1] in lane_t and (k[0] in gn or k[2] in gn) and k not in rek
                     and not (ge[k] and all(is_retired(p) for p in ge[k])))
    room_n, room_e = int(caps.get("nodes", 0)), int(caps.get("edges", 0))
    n_before = len(create_n) + len(set_n) + len(retire_n) + len(create_e) + len(set_e) + len(retire_e)
    create_n = sorted(create_n, key=lambda n: sha16(n["p"]["gs_key"]))[:room_n]     # thứ tự tất định; phần dư KHÔNG ghi, lượt sau tự bắt kịp
    set_n = set_n[:max(room_n - len(create_n), 0)]
    retire_n = retire_n[:max(room_n - len(create_n) - len(set_n), 0)]
    ok_keys = set(gn) | set(other) | {n["p"]["gs_key"] for n in create_n}
    create_e = [e for e in sorted(create_e, key=lambda e: e["p"]["gs_edge_key"]) if e["s"] in ok_keys and e["d"] in ok_keys][:room_e]
    set_e = set_e[:max(room_e - len(create_e), 0)]
    retire_e = retire_e[:max(room_e - len(create_e) - len(set_e), 0)]
    quota_left = n_before - (len(create_n) + len(set_n) + len(retire_n) + len(create_e) + len(set_e) + len(retire_e))
    cap_partial = quota_left > 0
    if extra_check:
        problems += extra_check(gn, other)
    ck = sorted(n["p"]["gs_key"] for n in create_n)
    ek = sorted(e["p"]["gs_edge_key"] for e in create_e)
    ret = {"gs_status": RETIRED, "retired_at": now_iso(), "retired_by": "graph-refresh " + lane}
    for x in retire_n:
        x["ret"] = dict(ret, retired_reason="SOURCE_ABSENT_FULL_READ " + x["reader"])
    for x in retire_e:
        x["ret"] = dict(ret, retired_reason=x["why"])
    F, I = statements(create_n, set_n, create_e, set_e, ck, ek, retire_n, retire_e)
    out = {"lane": lane, "layer": layer, "at": now_iso(), "create_nodes": create_n, "set_nodes": set_n, "create_edges": create_e, "set_edges": set_e,
           "retire_nodes": retire_n, "retire_edges": retire_e, "retire_hold_why": retire_why,
           "reuse_nodes": reuse, "stale_nodes": stale_n, "stale_edges": stale_e, "created_keys": ck, "created_edge_keys": ek, "problems": problems,
           "cap_bound_partial": cap_partial, "caps": caps, "quota_left": quota_left, "edges_missing_end": len(missing_end),
           "retire_gate": ((native or {}).get("retire_gate") or {"held": {"*": "PLAN_PROBLEM"}, "alerts": [], "large_drop_proof": {}, "human_hold": []}) if lane == NATIVE_LANE else None,
           "counts": {"nodes_add": len(create_n), "edges_add": len(create_e), "nodes_set": len(set_n), "edges_set": len(set_e), "nodes_delete": 0,
                      "edges_delete": 0, "nodes_retire": len(retire_n), "edges_retire": len(retire_e), "already_retired_nodes": len(old_ret_n),
                      "already_retired_edges": len(old_ret_e), "stale_nodes": len(stale_n), "stale_edges": len(stale_e), "reused": len(reuse)},
           "F": F, "I": I}
    out["sha256"] = hashlib.sha256(json.dumps({k: out[k] for k in ("create_nodes", "set_nodes", "create_edges", "set_edges", "retire_nodes", "retire_edges")},
                                              sort_keys=True, ensure_ascii=False, default=str).encode()).hexdigest()
    # vân tay DANH TÍNH của kế hoạch (bỏ thuộc tính dễ đổi: snapshot_utc/run/…) — dùng kiểm «nguồn đổi giữa lượt»: đọc lại nguồn chỉ khác dấu
    # giờ chụp ⇒ cùng vân tay; đối tượng/cạnh/thuộc tính danh tính đổi ⇒ khác ⇒ dừng trước ghi
    out["ident_sha256"] = hashlib.sha256(json.dumps({"n": sorted([n["p"]["gs_key"], _ident(n["p"])] for n in create_n),
                                                     "sn": sorted([x["k"], _ident(x["new"])] for x in set_n),
                                                     "e": sorted([e["s"], e["t"], e["d"], _ident(e["p"])] for e in create_e),
                                                     "se": sorted([list(x["key"]), _ident(x["new"])] for x in set_e),
                                                     "rn": sorted(x["k"] for x in retire_n), "re": sorted(list(x["key"]) for x in retire_e)},
                                                    sort_keys=True, ensure_ascii=False, default=str).encode()).hexdigest()
    out["empty"] = not (create_n or set_n or create_e or set_e or retire_n or retire_e)
    return out


def statements(create_n, set_n, create_e, set_e, ck, ek, retire_n=(), retire_e=()):
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
    if retire_n:                                   # C1-D2 R3: đánh dấu thuộc tính, KHÔNG xoá/đổi nhãn; I đặt lại nguyên thuộc tính cũ
        F.append(("UNWIND $rows AS r MATCH (n:GS {gs_key: r.k}) SET n += r.ret", {"rows": [{"k": x["k"], "ret": x["ret"]} for x in retire_n]}))
    rt = {}
    for x in retire_e:
        rt.setdefault(x["key"][1], []).append(x)
    for t, xs in sorted(rt.items()):
        cy = "UNWIND $rows AS r MATCH (a:GS {gs_key: r.s})-[x:`%s`]->(b:GS {gs_key: r.d}) SET x %s r.%s" % (t.replace("`", ""), "%s", "%s")
        F.append((cy % ("+=", "ret"), {"rows": [{"s": x["key"][0], "d": x["key"][2], "ret": x["ret"]} for x in xs]}))
        I.append((cy % ("=", "p"), {"rows": [{"s": x["key"][0], "d": x["key"][2], "p": x["old"]} for x in xs]}))
    if retire_n:
        I.append(("UNWIND $rows AS r MATCH (n:GS {gs_key: r.k}) SET n = r.p", {"rows": [{"k": x["k"], "p": x["old"]} for x in retire_n]}))
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
