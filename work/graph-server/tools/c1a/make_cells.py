#!/usr/bin/env python3
# GS-C1A-CERT-QUALITYGATE-20261022-07 · sinh manifest/cert-cells.json (danh mục ô CT1 — thêm nguồn = thêm dòng, không thêm code)
import json, sys

RUN = "GS-C1A-CERT-QUALITYGATE-20261022-07"
P = ["trust", "snapshot_utc", "source_file", "source_row"]
PB = ["catalog", "trust", "snapshot_utc", "source_file", "source_fields"]
DBS = ["directus", "incomex_metadata", "postgres", "workflow"]
BASES = ["55-yeu-cau-thanh-toan-hs", "55-yeu-cau-thanh-toan-hs-copy", "65-yeu-cau-thanh-toan", "65-yeu-cau-thanh-toan-kt",
         "66-phe-duyet-yeu-cau-thanh-toan", "07-quan-ly-cong-viec", "88-phai-cu", "88-phai-cu-base-dem", "base-giao-viec-khong-tieu-chuan",
         "du-lieu-phai-cu-1", "dn-mien-nam", "doi-ngoai-nl", "ho-so", "ho-so-cong-ty-thanh-tra", "ke-toan-nl", "kiem-soat-nl", "thanh-tra",
         "tt-nguon-nl", "data-dao-tao-incomex"]
REPOS = ["agent-data-repo", "claude-kb", "claude-mcp", "lark-client", "nuxt-web"]
CODE_LABELS = ["ApiEndpoint", "CodeFileReference", "CodeInsight", "CodeModule", "CodeRepository", "CodeSymbol", "CodeTestReference",
               "ExternalDependency", "__Node__"]
CODE_RELS = ["calls", "declares", "evidences", "has_method", "implements", "imports", "instantiates", "part_of"]
GAP = {"table": "GAP-C0-01/02", "view": "GAP-C0-03", "trigger": "C0 F1 trigger ngoài directus (ADAPTER_MISSING)", "function": "GAP-C0-05",
       "fk": "GAP-C0-04", "view_dep": "GAP-C0-03"}
cells = []


def cell(key, gate, parent, source, scope, graph=None, gap=None, authority=None, **kw):
    c = {"key": key, "gate": gate, "parent": parent, "source": source, "scope": scope, "graph": graph, "gap": gap,
         "authority": authority or source.get("adapter")}
    c.update(kw)
    cells.append(c)


for db in DBS:
    auth = "PG catalog (pg_class/pg_trigger/pg_proc/pg_constraint/pg_depend) db %s, vai context_pack_readonly" % db
    for cls, scope in (("table", "bảng thường/phân vùng/ngoại (relkind r,p,f) ngoài schema hệ thống"),
                       ("view", "view + matview (relkind v,m)"),
                       ("trigger", "trigger không nội bộ + cạnh ON_TABLE (trigger→bảng) + EXECUTES (trigger→hàm) + enabled_code"),
                       ("function", "hàm người dùng (không thuộc extension)"),
                       ("fk", "khoá ngoại (đối tượng ràng buộc + cạnh bảng→bảng)"),
                       ("view_dep", "cạnh view→bảng (pg_depend/pg_rewrite)")):
        g = None
        if db == "directus" and cls == "table":
            g = {"nodes": [{"label": "PgTable", "prefix": "pg:table:"}]}
        if db == "directus" and cls == "trigger":
            g = {"nodes": [{"label": "PgTrigger", "prefix": "pg:trigger:", "attrs": ["enabled_code"]}],
                 "edges": [{"type": "ON_TABLE", "from": "PgTrigger", "to": "PgTable", "prov": P},
                           {"type": "EXECUTES", "from": "PgTrigger", "to": "PgFunction", "prov": P}]}
        if db == "directus" and cls == "function":
            g = {"nodes": [{"label": "PgFunction", "prefix": "pg:function:"}]}
        cell("pg:%s:%s" % (db, cls), "G1", "pg:" + db, {"adapter": "pg", "db": db, "classes": [cls]}, "%s · %s" % (db, scope), g, GAP[cls], auth)
for cls, extra, scope in (("directus_collection", [], "Directus collection"), ("directus_relation", [], "Directus relation (cạnh many→one)"),
                          ("directus_flow", ["directus_operation"], "Directus flow + operation (cạnh operation→flow)")):
    cell("directus:" + cls.split("_", 1)[1], "G1", "pg:directus", {"adapter": "pg", "db": "directus", "classes": [cls] + extra}, scope, None,
         "GAP-C0-06", "Directus metadata directus_* (PG directus, vai chỉ-đọc)")
cell("dot:registry", "G1", "pg:directus", {"adapter": "pg", "db": "directus", "classes": ["dot_tools"]},
     "PG dot_tools (mọi dòng) + cạnh REGISTERS (dòng→lệnh dot/bin) + PAIRED_WITH (cặp dot)",
     {"nodes": [{"label": "DotRegistryEntry", "prefix": "dot:registry:"}],
      "edges": [{"type": "REGISTERS", "from": "DotRegistryEntry", "to": "DotCommand", "prov": P},
                {"type": "PAIRED_WITH", "from": "DotRegistryEntry", "to": "DotRegistryEntry", "prov": P}]},
     "F10 (C0 chỉ đếm — C1-A đối chiếu theo mã)", "PG dot_tools + /opt/incomex/dot/bin")
cell("dot:cham", "G1", "pg:directus", {"adapter": "none"}, "DOT chạm bảng PG (khai CHAM 239 tệp) — chưa có cạnh máy đọc",
     None, "C0 F10 CHAM (OPEN)", "DOT script khai báo", open_classes=["DOT→PG CHAM"])
cell("pg:directus:function_body", "G1", "pg:directus", {"adapter": "none"}, "thân hàm đọc/ghi bảng nào (48 hàm EXECUTE động)",
     None, "GAP-C0-05 (OPEN, v0.5 UNKNOWN)", "PG pg_proc.prosrc", open_classes=["hàm→bảng", "SQL động"])
cell("dot:command", "G6", "opt:/opt/incomex", {"adapter": "dot_bin"}, "lệnh DOT trong /opt/incomex/dot/bin theo luật nhãn LBL-2",
     {"nodes": [{"label": "DotCommand", "prefix": "dot:command:"}]}, "F10", "/opt/incomex/dot/bin + 00-SO-DOT.tsv")
cell("docker:container", "G2", "docker", {"adapter": "docker"}, "container (mọi trạng thái) + cạnh USES_IMAGE/MOUNTS/PUBLISHES", None, "GAP-C0-10",
     "docker ps -a + docker inspect")
cell("docker:image", "G2", "docker", {"adapter": "docker", "part": "image"}, "image (ID)", None, "GAP-C0-10", "docker images")
cell("systemd:unit", "G3", "systemd", {"adapter": "systemd"}, "unit .service/.timer tệp thường trong /etc/systemd/system + cạnh TRIGGERS/EXECS "
     "(unit của gói trong /lib = UNSCOPED)", None, "GAP-C0-10", "/etc/systemd/system")
cell("cron:entry", "G4", "cron", {"adapter": "cron"}, "dòng lịch crontab spool + /etc/cron.d + /etc/crontab + cron.{hourly,daily,weekly,monthly} + cạnh RUNS",
     None, "GAP-C0-10", "cron spool/cron.d")
cell("nginx:route", "G5", "nginx", {"adapter": "nginx"}, "server (server_name|listen) + cạnh PROXIES (location băm, đích host:port)",
     None, "GAP-C0-10", "docker exec incomex-nginx nginx -T")
cell("opt:entries", "G6", "opt", {"adapter": "opt"}, "mục cấp 1 trong /opt và /opt/incomex", None, "GAP-C0-09", "listdir")
cell("opt:code-ledger", "G6", "opt", {"adapter": "opt", "part": "ledger"}, "đường + trạng thái trong sổ mã code-ledger.tsv", None,
     "GAP-C0-09/12", "/opt/incomex/scripts/code-ledger.tsv")
for c in ("production_documents", "iu_core_iu_chunks"):
    cell("qdrant:%s:meta" % c, "G7", "qdrant:" + c, {"adapter": "qdrant_meta", "collection": c}, "collection %s: cấu hình vector + chỉ mục payload + alias" % c,
         None, "GAP-C0-07", "Qdrant GET /collections, /aliases")
cell("kb:production_documents", "G7", "qdrant:production_documents", {"adapter": "mb"},
     "M-b: ID tài liệu PG incomex_metadata.kb_documents ↔ ID payload document_id Qdrant production_documents (không vector/văn bản)",
     None, "GAP-C0-07 / P191 M-b", "PG kb_documents + Qdrant scroll payload document_id", private_ids=True)
for b in BASES:
    cell("lark:%s:schema" % b, "G8", "lark:" + b, {"adapter": "lark_schema", "base": b}, "base %s: bảng + trường liên kết (type 18/21)" % b,
         None, "GAP-C0-14", "LarkReader list_tables/list_fields (bases.yaml)")
cell("lark:88-phai-cu:b88", "G8", "lark:88-phai-cu", {"adapter": "b88"},
     "base 88-phai-cu: bản ghi 4 bảng (11 field id) + 4 loại cạnh CANDIDATE/SELECTED_FOR_ORDER, ORDER_MANAGED_BY_UNION, ORDER_FOR_COMPANY",
     {"nodes": [{"label": "B88Order", "prefix": "b88:order:", "attrs": ["order_code"]}, {"label": "B88Trainee", "prefix": "b88:trainee:"},
                {"label": "B88Union", "prefix": "b88:union:", "attrs": ["union_code"]}, {"label": "B88Company", "prefix": "b88:company:", "attrs": ["company_code"]}],
      "edges": [{"type": "CANDIDATE_FOR_ORDER", "from": "B88Trainee", "to": "B88Order", "prov": PB},
                {"type": "SELECTED_FOR_ORDER", "from": "B88Trainee", "to": "B88Order", "prov": PB},
                {"type": "ORDER_MANAGED_BY_UNION", "from": "B88Order", "to": "B88Union", "prov": PB},
                {"type": "ORDER_FOR_COMPANY", "from": "B88Order", "to": "B88Company", "prov": PB}]},
     "F9 (lane b88 R7)", "Lark 88-phai-cu (r7_b6.py, 11 field id)", private_ids=True)
cell("git:workspace:work", "G9", "git", {"adapter": "git"}, "thư mục việc work/* + work/done-tasks/* tại HEAD bản clone cổng", None, "GAP-C0-13",
     "git ls-tree (clone cổng workspace)")
for r in REPOS:
    cell("code:%s:files" % r, "G9", "code:" + r, {"adapter": "code_identity", "repo": r},
         "cây mã %s đang chạy: tệp ↔ nút mã Graph (Enola/Cognee ngữ nghĩa, chưa có phép so ID tất định)" % r, None,
         "GAP-C0-09 (code↔Graph không so ID ở C1-A)", "refresh-sources code identity")

code_cells = ["code:%s:files" % r for r in REPOS]
doc = {
    "format": "graph-cert-cells-v1", "catalog_version": "c1a-1", "written_by": RUN, "ttl_hours": 26,
    "canon": "CANON-V1: hàng JSON gọn sort_keys UTF-8, sắp theo byte, tiền tố độ dài 8 byte big-endian, SHA256; đối tượng và cạnh băm riêng",
    "cells": cells,
    "graph_label_map": {"PgTable": ["pg:directus:table"], "PgTrigger": ["pg:directus:trigger"], "PgFunction": ["pg:directus:function"],
                        "DotCommand": ["dot:command"], "DotRegistryEntry": ["dot:registry"],
                        "B88Order": ["lark:88-phai-cu:b88"], "B88Trainee": ["lark:88-phai-cu:b88"], "B88Union": ["lark:88-phai-cu:b88"],
                        "B88Company": ["lark:88-phai-cu:b88"], "GS": [], "GraphMetadata": ["directory:g1-g9"],
                        **{l: code_cells for l in CODE_LABELS}},
    "graph_rel_map": {"ON_TABLE": ["pg:directus:trigger"], "EXECUTES": ["pg:directus:trigger"], "REGISTERS": ["dot:registry"],
                      "PAIRED_WITH": ["dot:registry"], **{r: ["lark:88-phai-cu:b88"] for r in ("CANDIDATE_FOR_ORDER", "SELECTED_FOR_ORDER",
                                                                                              "ORDER_MANAGED_BY_UNION", "ORDER_FOR_COMPANY")},
                      **{r: code_cells for r in CODE_RELS}},
    "certified_props": {"PgTable": ["id", "gs_key"], "PgTrigger": ["id", "gs_key", "enabled_code"], "PgFunction": ["id", "gs_key"],
                        "DotCommand": ["id", "gs_key"], "DotRegistryEntry": ["id", "gs_key"], "B88Order": ["id", "gs_key", "order_code"],
                        "B88Trainee": ["id", "gs_key"], "B88Union": ["id", "gs_key", "union_code"], "B88Company": ["id", "gs_key", "company_code"]},
    "endpoint_cover": {"PgTable": ["ON_TABLE"], "PgFunction": ["EXECUTES"], "DotCommand": ["REGISTERS"]},
    "query_classes": {"CELL_SCOPED_LOOKUP": "mọi nhãn/cạnh trong danh mục, không đường *, không thủ tục, chỉ thuộc tính đã băm ⇒ nhãn = ô kém nhất",
                      "IMPACT_OR_PATH": "đường độ dài thay đổi ⇒ cần mọi ô (luôn MỘT PHẦN tới khi mọi ô ĐỦ)",
                      "UNCERTIFIED_PROPERTY": "lọc/đọc thuộc tính ngoài phần băm ⇒ MỘT PHẦN",
                      "UNSUPPORTED": "nút không nhãn, nhãn/cạnh lạ, CALL/APOC/subquery ⇒ MỘT PHẦN, cần mọi ô",
                      "GRAPH_SCHEMA": "get-schema ⇒ MỘT PHẦN (lược đồ Graph không phải khẳng định đủ)"},
}
json.dump(doc, open(sys.argv[1], "w"), ensure_ascii=False, indent=1, sort_keys=True)
print(len(cells), "cells")
