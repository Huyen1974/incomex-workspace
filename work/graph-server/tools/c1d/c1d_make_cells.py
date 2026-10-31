#!/usr/bin/env python3
"""c1d_make_cells — sinh cert-cells c1d-1 từ c1c-1 (giữ nguyên 80 ô cũ, byte định nghĩa ô cũ KHÔNG đổi) · GS-C1D-NATIVE-AUTOCOVER-20261023-10
+ 4 ô lane infra (G5/G3/G2/G9) + khối c1d (trần pilot, unit khai báo, unit chờ chủ HJW) + hợp đồng phạm vi từng họ `families[G].contract`.
+ lô L1 mới tất định (c1d_l1_batch.py, ≤16 bảng) vào l1_pilot.tables + một ô l1:<bảng> mỗi bảng + ô phạm vi l1:pilot11:scope phủ cả lô.
Dùng: c1d_make_cells.py <cert-cells c1c-1.json> <out.json> [l1-batch.json]"""
import json, sys

RUN = "GS-C1D-NATIVE-AUTOCOVER-20261023-10"
UNITS_DECLARED = ["hermes-agentdata-relay.socket", "hermes-qdrant-relay.socket", "hermes-webhook-bridge.socket", "incomex-balo-reconcile.socket",
                  "incomex-hvu-sync.socket", "var-lib-hermes-work.mount", "var-lib-incomex\\x2dcowork-workspace.mount"]
HJW_PENDING = ["incomex-hjwcap.path", "incomex-hjwcap.service"]
PROV = ["trust", "snapshot_utc", "source"]
OWN = "Graph Host · work/graph-server (bao phủ)"
ALERT = "Telegram Owner qua đèn Kuma #24 «Graph Certificate» (ĐỎ mỗi lượt · VÀNG một lượt + nhắc 168h) · biên nhận state/refresh/cert/incidents.jsonl"

NEW_CELLS = [
    {"key": "infra:listener", "gate": "G5", "parent": None, "parent_prefixes": ["nginx:listen:"], "gap": "C1-C 20 cổng nghe chưa nhận",
     "authority": "ss -ltnp (pid giữ fd) + /proc/<pid>/cgroup + docker-proxy -host-ip/-host-port/-container-ip + systemctl show Listen=",
     "scope": "MỌI cổng nghe TCP host ⇒ chủ chắc chắn: BOUND_BY_PROCESS_OF (tiến trình unit .service giữ fd) · PUBLISHED_BY (docker-proxy + container) · "
              "LISTENS_ON (systemd pid 1 giữ fd cho unit .socket). Không chủ chắc chắn ⇒ AMBIGUOUS_OWNER (ô MỘT PHẦN). Không gồm UDP/unix socket (unix ở ô infra:unit thuộc tính listen).",
     "source": {"adapter": "c1d", "part": "listener"},
     "graph": {"nodes": [{"label": "NetListener", "prefix": "net:listen:"}],
               "edges": [{"type": "BOUND_BY_PROCESS_OF", "from": "NetListener", "to": "SystemdUnit", "prov": PROV},
                         {"type": "PUBLISHED_BY", "from": "NetListener", "to": "DockerContainer", "prov": PROV},
                         {"type": "LISTENS_ON", "from": "SystemdUnit", "to": "NetListener", "prov": PROV}]}},
    {"key": "infra:unit", "gate": "G3", "parent": None, "parents": ["systemd:" + u for u in UNITS_DECLARED], "gap": "C1-C 7 unit cũ .socket/.mount chưa nhận",
     "authority": "systemctl show (Triggers/RequiredBy/Listen/What/Where/FragmentPath) — ánh xạ systemd TỰ khai báo",
     "scope": "7 unit cũ khai báo + đích TRIGGERS + dịch vụ REQUIRES_MOUNT + unit sở hữu cổng nghe (ô infra:listener) — thuộc tính kind/fragment_dir/listen/mount_what/"
              "mount_where. KHÔNG gồm 2 unit HJW mới (incomex-hjwcap.*: chờ chủ HJW), unit gói khác, ExecStart (ô systemd:unit).",
     "source": {"adapter": "c1d", "part": "unit", "units": UNITS_DECLARED},
     "graph": {"nodes": [{"label": "SystemdUnit", "prefix": "systemd:unit:", "attrs": ["kind", "fragment_dir", "listen", "mount_what", "mount_where"]}],
               "edges": [{"type": "TRIGGERS", "from": "SystemdUnit", "to": "SystemdUnit", "prov": PROV},
                         {"type": "REQUIRES_MOUNT", "from": "SystemdUnit", "to": "SystemdUnit", "prov": PROV}]}},
    {"key": "infra:container", "gate": "G2", "parent": "docker", "gap": "GAP-C0-10 (một phần: định danh container)",
     "authority": "docker ps -a + docker inspect (Name/Id/Config.Image)",
     "scope": "MỌI container (mọi trạng thái, trừ mẫu tạm: workspace-job-* và Neo4j tạm của chính graph-refresh incomex-graph-v1-rc-*): tên + Id(12) + image khai báo. KHÔNG gồm mount/mạng/biến môi trường (ô docker:container).",
     "source": {"adapter": "c1d", "part": "container", "exclude_patterns": ["^docker:workspace-job-[0-9a-f]+$", "^docker:incomex-graph-v1-rc-"]},
     "graph": {"nodes": [{"label": "DockerContainer", "prefix": "docker:container:", "attrs": ["container_id", "image"]}]}},
    {"key": "infra:git", "gate": "G9", "parent": None, "parent_prefixes": ["git:repo:"], "gap": "C1-C 9 kho git chưa nhận",
     "authority": "git rev-parse --show-toplevel/--git-common-dir/--git-dir (không fetch, không khoá)",
     "scope": "MỌI kho git dưới /opt/incomex (sâu ≤3): đường + toplevel + WORKTREE_OF (git-common-dir thuộc kho khác) + RESOLVES_TO_TOPLEVEL. Kho→cây mã đã nạp: "
              "CHỈ thuộc tính bằng chứng code_roots_evidence (cạnh vào lớp code phá cổng đóng kín lane code) — KHÔNG phải quan hệ được chứng nhận; HEAD không phải bằng chứng mã chạy.",
     "source": {"adapter": "c1d", "part": "git"},
     "graph": {"nodes": [{"label": "GitRepository", "prefix": "git:repo:", "attrs": ["toplevel"]}],
               "edges": [{"type": "WORKTREE_OF", "from": "GitRepository", "to": "GitRepository", "prov": PROV},
                         {"type": "RESOLVES_TO_TOPLEVEL", "from": "GitRepository", "to": "GitRepository", "prov": PROV}]}},
]


def contract(src, objs, rels, excl, acl, epoch, matcher, loader, grade, owner, detector):
    return {"native_authoritative_source": src, "included_object_types": objs, "covered_relation_types": rels,
            "excluded_relation_bearing_classes": excl, "reader_acl": acl, "version_epoch": epoch, "native_vs_graph_matcher": matcher,
            "detector_status": detector, "supported_incremental_loader": loader, "durable_capture_grade": grade, "owner": owner,
            "incident": ALERT, "last_good": "state/refresh/cert/inventory.json families[G] + signals", "last_attempt": "state/refresh/cert/current.json coverage_matrix[G].read_at",
            "id_kinds": "mã định danh MÃ (đường tệp/unit/container/khoá catalog) tách khỏi mã NỘI DUNG/DỮ LIỆU (id dòng/bản ghi: chỉ băm riêng tư, không nạp)",
            "partial_rule": "thiếu bộ liệt kê hoặc quan hệ con chưa biết ⇒ MỘT PHẦN dù mọi nút cha khớp; ĐỦ cả họ chỉ khi MỌI ô của họ ĐỦ và 0 cha chưa nhận"}


CONTRACTS = {
    "G1": contract("PG catalog 4 db (pg_class/pg_constraint/pg_trigger/pg_proc/pg_depend) + directus_* metadata", ["PgTable", "PgView", "PgTrigger", "PgFunction", "PgForeignKey",
                   "DirectusCollection", "DirectusRelation", "DirectusPermission", "DotRegistryEntry"], ["ON_TABLE", "EXECUTES", "HAS_FK", "REFERENCES", "DEPENDS_ON",
                   "MAPS_TO_TABLE", "RELATION_MANY", "RELATION_ONE", "PERMISSION_ON", "REGISTERS", "PAIRED_WITH"],
                   ["giá trị dòng/FK của bản ghi (Graph là bản đồ, không phải bản sao dữ liệu) — ngoài hợp đồng", "394 bảng ngoài 11 bảng mẫu L1: chỉ lớp pg (bảng có trigger) — MỘT PHẦN",
                    "role/grant/RLS/sequence/index", "thân hàm: chỉ L2 ứng viên"], "context_pack_readonly (REPEATABLE READ READ ONLY, không siêu người dùng)",
                   "pg_current_snapshot + snapshot_utc mỗi lượt", "tập (đối tượng, cạnh) CANON-V1 số + sha256 từng ô", "graph-refresh lane pgdot (dựng lại) + c1d:pgl1 (cộng-thêm)",
                   "SIGNAL_COUNTER_ONLY (pg_stat_*) + PATH_LIMITED_AUDIT (directus_activity); CDC_NOT_AVAILABLE", OWN + " · chủ PG/DOT (schema, D20)", "DETECT_AND_CERT_PER_CELL"),
    "G2": contract("docker ps -a + docker inspect", ["DockerContainer"], ["PUBLISHED_BY (từ ô G5)"], ["mount/volume, mạng, image layer, env/secret",
                   "container sinh-xoá giữa hai lượt (workspace-job-*)"], "root host (docker CLI)", "Id/Created/StartedAt/RestartCount mỗi lượt",
                   "tên + Id12 + image", "c1d:infra", "INDEPENDENT_SNAPSHOT_ONLY (+ scanner wf-universal-scanner lần đọc 2)", OWN + " · chủ hạ tầng VPSC", "DETECT_AND_CERT_IDENTITY"),
    "G3": contract("/etc/systemd/system + systemctl show", ["SystemdUnit"], ["TRIGGERS", "REQUIRES_MOUNT", "LISTENS_ON"], ["ExecStart→tệp (ô systemd:unit, chưa nạp)",
                   "unit gói /lib ngoài tập đích", "unit tạm /run", "2 unit HJW mới incomex-hjwcap.* (chờ chủ HJW)"], "root host (systemctl)", "sha256 tệp unit + drop-in mỗi lượt",
                   "tên unit + thuộc tính khai báo + cạnh", "c1d:infra (7 unit cũ + đích)", "INDEPENDENT_SNAPSHOT_ONLY", OWN + " · chủ hạ tầng VPSC · 2 unit HJW: chủ HJW", "DETECT_AND_CERT_DECLARED_SET"),
    "G4": contract("cron spool + cron.d + crontab + run-parts", ["CronEntry (chưa nạp)"], ["RUNS (chưa nạp)"], ["lệnh trong dòng cron ngoài đường đầu tiên",
                   "at/anacron", "crontab người dùng ngoài spool"], "root host", "sha256 tệp cron", "dòng lịch|đích", "KHÔNG (đối chiếu scanner↔gốc only)",
                   "INDEPENDENT_SNAPSHOT_ONLY (+ scanner)", OWN + " · chủ hạ tầng VPSC", "DETECT_ONLY"),
    "G5": contract("ss -ltnp + /proc + docker-proxy + nginx -T", ["NetListener", "NginxServer (chưa nạp)"], ["BOUND_BY_PROCESS_OF", "PUBLISHED_BY", "LISTENS_ON",
                   "PROXIES (chưa nạp)"], ["route nginx location→upstream (ô nginx:route chưa nạp)", "UDP / unix socket ngoài unit .socket", "cổng mở-rồi-đóng giữa hai lượt"],
                   "root host", "ảnh ss mỗi lượt + sha256 nginx -T", "địa chỉ:cổng + chủ", "c1d:infra", "INDEPENDENT_SNAPSHOT_ONLY", OWN + " · chủ hạ tầng VPSC", "DETECT_AND_CERT_LISTENERS"),
    "G6": contract("listdir /opt + code-ledger + sha256 tệp mã trong sổ", ["DotCommand", "OptEntry (chưa nạp)"], [], ["nội dung tệp ngoài sổ mã", "quét toàn đĩa (không làm)"],
                   "root host", "sha256 tệp mỗi lượt", "đường + vân tay", "lane pgdot (DotCommand)", "INDEPENDENT_SNAPSHOT_ONLY", OWN, "DETECT_ONLY"),
    "G7": contract("Qdrant GET collections/aliases + scroll document_id", ["QdrantCollection (chưa nạp)"], [], ["vector/payload văn bản", "điểm không có document_id"],
                   "khoá dịch vụ trong incomex-agent-data", "points_count lúc chụp", "ID tài liệu băm riêng tư", "KHÔNG", "INDEPENDENT_SNAPSHOT_ONLY",
                   OWN + " · chủ Agent Data (KB↔Qdrant 1/0/2/9)", "DETECT_ONLY"),
    "G8": contract("LarkReader (bases.yaml) list_tables/list_fields + b88 r7_b6", ["LarkTable (chưa nạp)", "B88Order", "B88Trainee", "B88Union", "B88Company"],
                   ["CANDIDATE_FOR_ORDER", "SELECTED_FOR_ORDER", "ORDER_MANAGED_BY_UNION", "ORDER_FOR_COMPANY"], ["bản ghi các base ngoài b88", "trường liên kết ngoài 11 field b88",
                   "bản ghi sửa-rồi-xoá giữa hai lượt"], "app Lark chỉ đọc (lark-client)", "FREEZE_SHA256 b88", "record_id + 4 loại cạnh", "lane b88",
                   "INDEPENDENT_SNAPSHOT_ONLY; modified_time (SOURCE_WATERMARK) chưa đọc ⇒ UNKNOWN", OWN + " · chủ Lark base", "DETECT_AND_CERT_B88"),
    "G9": contract("git rev-parse/ls-tree các kho dưới /opt/incomex + clone cổng workspace", ["GitRepository", "WorkDir (chưa nạp)"], ["WORKTREE_OF", "RESOLVES_TO_TOPLEVEL"],
                   ["kho→cây mã đang chạy (thuộc tính bằng chứng, chưa phải cạnh)", "mã chưa commit / bản triển khai khác HEAD", "lịch sử commit"], "root host (git, không fetch)",
                   "HEAD^{tree} mỗi lượt", "đường kho + toplevel + cạnh", "c1d:infra", "SOURCE_COMMIT_LOG (chỉ mã đã commit)", OWN, "DETECT_AND_CERT_REPOS"),
}


def main(src, out, batch=None):
    cat = json.load(open(src, encoding="utf-8"))
    assert cat["catalog_version"] == "c1c-1" and len(cat["cells"]) == 80, "đầu vào phải là c1c-1 80 ô"
    have = {c["key"] for c in cat["cells"]}
    for c in NEW_CELLS:
        assert c["key"] not in have
        c = {k: v for k, v in c.items() if v is not None}
        cat["cells"].append(c)
    for g, ct in CONTRACTS.items():
        cat["families"].setdefault(g, {})["contract"] = ct
    for g, nxt in (("G2", "C1-D: định danh container đã nạp (infra:container); mount/mạng còn mở"),
                   ("G3", "C1-D: 7 unit cũ + đích khai báo đã nạp (infra:unit); 2 unit HJW chờ chủ HJW; ExecStart còn mở"),
                   ("G5", "C1-D: cổng nghe→chủ đã nạp (infra:listener); route nginx còn mở"),
                   ("G9", "C1-D: kho git + worktree/toplevel đã nạp (infra:git); kho→cây mã chỉ thuộc tính")):
        cat["families"][g]["next_action"] = nxt
        cat["families"][g]["supported_ingestion"] = True
    cat["c1d"] = {"run": RUN, "caps": {"nodes": 20000, "edges": 40000, "note": "quota MỖI LƯỢT, không cộng dồn; phần dư ⇒ CAP_BOUND_PARTIAL, lượt sau tự bắt kịp (SYNC-CORE, đo lại ở LIVE)"},
                  "units_declared": UNITS_DECLARED, "units_excluded_pending_owner": HJW_PENDING,
                  "ephemeral_parent_patterns": ["^docker:workspace-job-[0-9a-f]+$", "^docker:incomex-graph-v1-rc-"],
                  "lanes": {"c1d:infra": {"layer": "infra", "cells": [c["key"] for c in NEW_CELLS]},
                            "c1d:pgl1": {"layer": "pgl1", "cells": "l1:* (l1_pilot.tables) + l1:pilot11:scope"}}}
    if batch:                                   # lô L1 tất định: ô mới cùng khuôn ô l1 C1-B (chỉ thay bảng)
        b = json.load(open(batch, encoding="utf-8"))
        tpl = next(c for c in cat["cells"] if c["key"] == "l1:directus.public.agents")
        old = list(cat["l1_pilot"]["tables"])
        for t in b["chosen"]:
            assert t not in old and t.startswith("directus.")
            st = t.split(".", 1)[1]
            c = json.loads(json.dumps(tpl))
            c.update(key="l1:" + t, gap="C1-D lô L1-1 (tất định %s)" % b["seed"], graph={"l1_anchor": st},
                     scope=tpl["scope"].replace("directus.public.agents", t))
            c["source"] = dict(tpl["source"], table=t)
            cat["cells"].append(c)
        cat["l1_pilot"]["tables"] = old + list(b["chosen"])
        cat["l1_pilot"]["c1d_batch_1"] = {"run": RUN, "rule": b["rule"], "seed": b["seed"], "tables": b["chosen"], "estimated_nodes_add": b["batch_nodes_add"],
                                          "estimated_edges_add": b["batch_edges_add"], "fk_tables": b["fk_tables"], "candidates": b["candidates"]}
        sc = next(c for c in cat["cells"] if c["key"] == "l1:pilot11:scope")
        sc["source"]["tables"] = list(cat["l1_pilot"]["tables"])
        sc["scope"] = "phạm vi mẫu C1-B + lô C1-D (%d bảng, khoá ô giữ tên pilot11 để giữ sàn): MỌI nút PgView/PgForeignKey/Directus* và MỌI cạnh L1 mới trong Graph = hợp các ô bảng (không nút/cạnh lạc)" % len(cat["l1_pilot"]["tables"])
    # nhãn/loại cạnh mới vào danh mục phân loại truy vấn N4 (bảo thủ: mỗi nhãn ⇒ ô của nó; không thêm endpoint_cover ⇒ truy vấn chạm hai nhãn cần cả hai ô ĐỦ)
    cat["graph_label_map"].update({"NetListener": ["infra:listener"], "SystemdUnit": ["infra:unit"], "DockerContainer": ["infra:container"], "GitRepository": ["infra:git"]})
    for t in ("BOUND_BY_PROCESS_OF", "PUBLISHED_BY", "LISTENS_ON"):
        cat["graph_rel_map"][t] = ["infra:listener"]
    for t in ("TRIGGERS", "REQUIRES_MOUNT"):
        cat["graph_rel_map"][t] = ["infra:unit"]
    for t in ("WORKTREE_OF", "RESOLVES_TO_TOPLEVEL"):
        cat["graph_rel_map"][t] = ["infra:git"]
    cat["certified_props"].update({"NetListener": ["id", "gs_key"], "SystemdUnit": ["id", "gs_key", "kind", "fragment_dir", "listen", "mount_what", "mount_where"],
                                   "DockerContainer": ["id", "gs_key", "container_id", "image"], "GitRepository": ["id", "gs_key", "toplevel"]})
    cat["catalog_version"] = "c1d-1"
    cat["written_by"] = RUN
    with open(out, "w", encoding="utf-8") as f:
        json.dump(cat, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write("\n")
    print("cells %d (+%d infra, l1 bảng %d) catalog_version %s" % (len(cat["cells"]), len(NEW_CELLS), len(cat["l1_pilot"]["tables"]), cat["catalog_version"]))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
