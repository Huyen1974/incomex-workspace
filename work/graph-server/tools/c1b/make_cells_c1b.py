#!/usr/bin/env python3
# GS-C1B-LAYERED-IMPACT-20261022-08 · sinh cert-cells.json v3 (c1b-1) = bản C1-A (c1a-1) + đúng các dòng C1-B; thêm nguồn = thêm dòng.
# Dùng: make_cells_c1b.py <cert-cells.json C1-A> <sample.json (c1b_sample)> <out.json>
# Thêm: khối l1_pilot (11 bảng khoá theo hạt giống + biên nhận mẫu + sổ kiểu có nghĩa native) · 11 ô l1:<db>.<schema>.<bảng> (neo Graph) ·
# ô l1:pilot11:scope (bắt nút/cạnh lạc) · ô directus:permission (toàn cục, MỘT PHẦN) · bản đồ nhãn/cạnh mới trỏ về ô TOÀN CỤC (MỘT PHẦN)
# để bộ nhãn cũ vẫn bảo thủ; chỉ phân loại L1_SCOPED_LOOKUP (n4-qc-2) mới thu hẹp về ô của một bảng mẫu.
import json, sys

src, sample, out = sys.argv[1:4]
c = json.load(open(src, encoding="utf-8"))
s = json.load(open(sample, encoding="utf-8"))
RUN = "GS-C1B-LAYERED-IMPACT-20261022-08"
CLASSES = ["table", "view", "trigger", "l1_fk", "view_dep_kind", "directus_collection", "directus_relation", "directus_permission"]
AUTH = ("PG catalog pg_constraint · pg_rewrite+pg_depend · pg_trigger+pg_proc · pg_class + Directus directus_collections/relations/permissions "
        "(db directus, vai context_pack_readonly, REPEATABLE READ READ ONLY, đọc trọn rồi lọc)")
TYPES = ["HAS_FK", "REFERENCES", "DEPENDS_ON", "ON_TABLE", "EXECUTES", "MAPS_TO_TABLE", "RELATION_MANY", "RELATION_ONE", "PERMISSION_ON"]
OWNER = "Graph Host · work/graph-server"
assert c["catalog_version"] == "c1a-1" and s["anchor"]["native_identity_ok"] and len(s["pilot11"]) == 11 == len(set(s["pilot11"]))
c["catalog_version"] = "c1b-1"
c["written_by"] = RUN
c["l1_pilot"] = {
    "tables": s["pilot11"], "anchor": s["anchor"]["table"], "seed": s["seed"], "formula": s["formula"], "frozen_by": RUN,
    "sample_receipt": {"snapshot": s["snapshot"], "universe": s["universe"], "strata": s["strata"]},
    "graph_layer": "pgl1",
    "model": {
        "labels": {
            "PgTable": "pg_class relkind r/p/f; id = schema.bảng. Bảng chưa có trong lane pgdot (không trigger) được tạo ở gs_layer pgl1",
            "PgView": "pg_class relkind v/m (view/matview); id = schema.tên; kind = relkind",
            "PgForeignKey": "pg_constraint contype='f'; id = schema.bảng_mang_ràng_buộc.tên_ràng_buộc; columns/ref_columns (thứ tự conkey/confkey); "
                            "on_update/on_delete = confupdtype/confdeltype (a no action · r restrict · c cascade · n set null · d set default)",
            "DirectusCollection": "directus_collections.collection; registry = 'referenced_only' khi collection không có dòng directus_collections nhưng "
                                  "được directus_relations/permissions nhắc (collection hệ thống, khai báo trong mã Directus)",
            "DirectusRelation": "directus_relations; id = many_collection.many_field; one_collection (null với quan hệ M2A)",
            "DirectusPermission": "directus_permissions; id = khoá dòng; action; policy. KHÔNG đọc cột permissions/validation/presets/fields",
        },
        "types": {
            "HAS_FK": "PgTable → PgForeignKey · pg_constraint.conrelid (bảng mang ràng buộc)",
            "REFERENCES": "PgForeignKey → PgTable · pg_constraint.confrelid (bảng được tham chiếu)",
            "DEPENDS_ON": "PgView → PgTable · pg_depend classid=pg_rewrite, refclassid=pg_class (view/matview dùng trực tiếp bảng)",
            "ON_TABLE": "PgTrigger → PgTable · pg_trigger.tgrelid (đã có, lane pgdot)",
            "EXECUTES": "PgTrigger → PgFunction · pg_trigger.tgfoid (đã có, lane pgdot)",
            "MAPS_TO_TABLE": "DirectusCollection → PgTable|PgView · lõi Directus: collection = quan hệ cùng tên schema public",
            "RELATION_MANY": "DirectusRelation → DirectusCollection · directus_relations.many_collection",
            "RELATION_ONE": "DirectusRelation → DirectusCollection · directus_relations.one_collection",
            "PERMISSION_ON": "DirectusPermission → DirectusCollection · directus_permissions.collection",
        },
        "edge_provenance": ["trust", "snapshot_utc", "source"],
        "not_l1": "đọc/ghi trong thân hàm, EXECUTE động, flow/operation Directus, DOT, mã = L2 (state/refresh/cert/l2-candidates.json, MỘT PHẦN); "
                  "hành vi chạy thật = L3 MỞ",
    },
}
for t in s["pilot11"]:
    c["cells"].append({
        "key": "l1:" + t, "gate": "G1", "parent": "pg:directus", "layer": "L1", "trust": "EXACT_AT_SNAPSHOT", "owner": OWNER, "authority": AUTH,
        "gap": None, "scope": "L1 catalog khai báo của %s%s: khoá ngoại vào/ra · view phụ thuộc trực tiếp · trigger→hàm · Directus collection/"
                              "relation/permission" % (t, " (neo C1-B)" if t == s["anchor"]["table"] else ""),
        "source": {"adapter": "pg_l1", "db": "directus", "classes": CLASSES, "table": t},
        "graph": {"l1_anchor": t.split(".", 1)[1]}, "source_relations": TYPES})
P = ["trust", "snapshot_utc", "source"]
c["cells"].append({
    "key": "l1:pilot11:scope", "gate": "G1", "parent": "pg:directus", "layer": "L1", "trust": "EXACT_AT_SNAPSHOT", "owner": OWNER, "authority": AUTH,
    "gap": None, "scope": "phạm vi mẫu C1-B: MỌI nút PgView/PgForeignKey/Directus* và MỌI cạnh L1 mới trong Graph = hợp 11 ô bảng (không nút/cạnh lạc)",
    "source": {"adapter": "pg_l1_scope", "db": "directus", "classes": CLASSES, "tables": s["pilot11"]},
    "graph": {"nodes": [{"label": "PgView", "prefix": "pg:view:", "attrs": ["kind"]},
                        {"label": "PgForeignKey", "prefix": "pg:fk:", "attrs": ["columns", "ref_columns", "on_update", "on_delete"]},
                        {"label": "DirectusCollection", "prefix": "directus:collection:", "attrs": ["registry"]},
                        {"label": "DirectusRelation", "prefix": "directus:relation:", "attrs": ["one_collection"]},
                        {"label": "DirectusPermission", "prefix": "directus:permission:", "attrs": ["action", "policy"]}],
              "edges": [{"type": "HAS_FK", "from": "PgTable", "to": "PgForeignKey", "prov": P},
                        {"type": "REFERENCES", "from": "PgForeignKey", "to": "PgTable", "prov": P},
                        {"type": "DEPENDS_ON", "from": "PgView", "to": "PgTable", "prov": P},
                        {"type": "MAPS_TO_TABLE", "from": "DirectusCollection", "to": "PgTable", "prov": P},
                        {"type": "RELATION_MANY", "from": "DirectusRelation", "to": "DirectusCollection", "prov": P},
                        {"type": "RELATION_ONE", "from": "DirectusRelation", "to": "DirectusCollection", "prov": P},
                        {"type": "PERMISSION_ON", "from": "DirectusPermission", "to": "DirectusCollection", "prov": P}]}})
c["cells"].append({
    "key": "directus:permission", "gate": "G1", "parent": "pg:directus", "authority": "Directus metadata directus_* (PG directus, vai chỉ-đọc)",
    "gap": "C1-B: Graph chỉ có quyền của 11 bảng mẫu (ô l1:*); toàn cục chưa nạp", "graph": None,
    "scope": "Directus permission (dòng directus_permissions: id, collection, action, policy)",
    "source": {"adapter": "pg", "db": "directus", "classes": ["directus_permission"]}})
for x in c["cells"]:
    if x["key"] in ("pg:directus:fk", "pg:directus:view", "pg:directus:view_dep", "directus:collection", "directus:relation"):
        x["gap"] = (x.get("gap") or "") + " · C1-B: Graph chỉ có phần của 11 bảng mẫu (ô l1:*), toàn cục vẫn MỘT PHẦN"
c["graph_label_map"].update({"PgView": ["pg:directus:view"], "PgForeignKey": ["pg:directus:fk"], "DirectusCollection": ["directus:collection"],
                             "DirectusRelation": ["directus:relation"], "DirectusPermission": ["directus:permission"]})
c["graph_rel_map"].update({"HAS_FK": ["pg:directus:fk"], "REFERENCES": ["pg:directus:fk"], "DEPENDS_ON": ["pg:directus:view_dep"],
                           "MAPS_TO_TABLE": ["directus:collection"], "RELATION_MANY": ["directus:relation"], "RELATION_ONE": ["directus:relation"],
                           "PERMISSION_ON": ["directus:permission"]})
c["certified_props"].update({"PgView": ["id", "gs_key", "kind"], "PgForeignKey": ["id", "gs_key", "columns", "ref_columns", "on_update", "on_delete"],
                             "DirectusCollection": ["id", "gs_key", "registry"], "DirectusRelation": ["id", "gs_key", "one_collection"],
                             "DirectusPermission": ["id", "gs_key", "action", "policy"]})
c["query_classes"]["L1_SCOPED_LOOKUP"] = ("C1-B n4-qc-2: mọi đường đi từ MỘT bảng mẫu (PgTable {id}) theo hình L1 khai báo (ON_TABLE←/EXECUTES→ · "
                                          "HAS_FK→REFERENCES→ · ←REFERENCES←HAS_FK · ←DEPENDS_ON · ←MAPS_TO_TABLE←PERMISSION_ON · ←MAPS_TO_TABLE←RELATION_*→"
                                          "RELATION_*→MAPS_TO_TABLE) ⇒ chỉ ô l1:<bảng>; answer_scope = L1_DECLARED_CATALOG_ONLY; câu hỏi tác động toàn phần "
                                          "vẫn impact_question_actionability = NOT_ACTION_SAFE")
json.dump(c, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1, sort_keys=True)
print("CELLS", c["catalog_version"], len(c["cells"]))
