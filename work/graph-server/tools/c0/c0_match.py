#!/usr/bin/env python3
# GS-C0-COVERAGE-INVENTORY-20261022-05 · ĐỐI CHIẾU BA CHIỀU công cụ gốc ↔ sổ PG ↔ Graph + BẢNG BAO PHỦ F1–F10 — dùng lại được
# Đầu vào (thư mục riêng Mac, ví dụ ~/Incomex-Graph-View/c0): pg.json (c0_pg_catalog.py) · pg_health.json (c0_pg_health.py) ·
#   runtime.json (c0_runtime.py) · qdrant.json (c0_qdrant.py) · lark.json (c0_lark.py) · docs.json (c0_docs.py) ·
#   graph_nodes.json = khoá Graph lấy bằng công cụ sẵn có (chỉ-đọc):
#   ssh contabo '/opt/incomex/graph-server/prod-v1/bin/graph-v1 cypher --out /dev/stdout --query "MATCH (n:GS) RETURN
#     [l IN labels(n) WHERE NOT l IN [\"GS\",\"__Node__\"]][0] AS l, n.gs_key AS k, n.gs_layer AS layer ORDER BY k LIMIT 9000"'
# Chạy: python3 -I c0_match.py DIR  ⇒ ghi DIR/coverage.json (bảng + GAP + danh sách lệch, chỉ lưu Mac) và in tóm tắt.
import collections, json, os, sys

D = sys.argv[1] if len(sys.argv) > 1 else "."
J = lambda f: json.load(open(os.path.join(D, f)))
pg, ph, rt, qd, lk, dc = J("pg.json"), J("pg_health.json"), J("runtime.json"), J("qdrant.json"), J("lark.json"), J("docs.json")
raw = open(os.path.join(D, "graph_nodes.json")).read()
gn, _ = json.JSONDecoder().raw_decode(raw)
rows = gn if isinstance(gn, list) else [r["row"] for r in gn["statements"][0]["results"][0]["data"]]
G = collections.defaultdict(set)
for l, k, _layer in rows:
    G[l].add(k)
strip = lambda lab, pre: {k[len(pre):] for k in G[lab]}

dbs = pg["summary"]["databases"]
dd, ds = pg["detail"]["directus"], dbs["directus"]
cat = {db: v.get("catalog", {}) for db, v in dbs.items()}
T, F, TR = set(dd["catalog"]["base_tables"]), set(dd["catalog"]["functions"]), set(dd["catalog"]["triggers"])
gT, gF, gTR = strip("PgTable", "pg:table:"), strip("PgFunction", "pg:function:"), strip("PgTrigger", "pg:trigger:")
V = {v.split("|")[0] for v in dd["catalog"]["views"]}
reg = ds["registries"]
other = lambda key: sum((cat[db].get("relkind", {}).get(key, 0) if key in cat[db].get("relkind", {}) else cat[db].get(key, 0))
                        for db in cat if db != "directus")

def row(fam, obj, universe, registry, graph, matched, missing, extra, reader, access, status, note=""):
    return dict(family=fam, object=obj, universe=universe, registry=registry, graph=graph, matched=matched,
                missing_in_graph=missing, extra_in_graph=extra, reader=reader, access=access, status=status, note=note)

M = []
crt = reg["collection_registry"]["vs_base_tables"]
M.append(row("F1", "PG bảng (directus)", len(T), f"collection_registry 168 (khớp {crt['matched']}, sổ thừa {crt['registry_not_table']}, bảng ngoài sổ {crt['table_not_in_registry']})",
             len(gT), len(T & gT), len(T - gT), len(gT - T), "R7 pgdot (chỉ bảng có trigger)", "OK", "PARTIAL",
             f"thừa = {sorted(gT - T)} (nay là VIEW)"))
M.append(row("F1", "PG bảng (incomex_metadata/postgres/workflow)", other("base_tables"), "—", 0, 0, other("base_tables"), 0, "NONE", "OK", "ADAPTER_MISSING",
             "postgres + workflow rỗng (0 bảng)"))
M.append(row("F1", "PG view+matview (mọi db)", sum(cat[d]["relkind"]["views"] + cat[d]["relkind"]["matviews"] for d in cat), "table_registry.view_name (một phần)", 0, 0,
             sum(cat[d]["relkind"]["views"] + cat[d]["relkind"]["matviews"] for d in cat), 0, "NONE", "OK", "ADAPTER_MISSING"))
M.append(row("F1", "PG trigger (directus)", len(TR), f"trigger_registry 107 (live ngoài sổ {reg['trigger_registry']['vs_pg_trigger_names']['live_not_in_registry']})",
             len(gTR), len(TR & gTR), len(TR - gTR), len(gTR - TR), "R7 pgdot", "OK", "COMPLETE"))
M.append(row("F1", "PG trigger (incomex_metadata)", cat["incomex_metadata"]["triggers_non_internal"], "—", 0, 0, cat["incomex_metadata"]["triggers_non_internal"], 0, "NONE", "OK", "ADAPTER_MISSING"))
M.append(row("F1", "PG hàm người dùng (directus, không tính extension)", len(F), "—", len(gF), len(F & gF), len(F - gF), len(gF - F), "R7 pgdot (chỉ hàm của trigger)", "OK", "PARTIAL"))
M.append(row("F1", "PG hàm (incomex_metadata)", sum(cat["incomex_metadata"]["functions_by_kind"].values()), "—", 0, 0, sum(cat["incomex_metadata"]["functions_by_kind"].values()), 0, "NONE", "OK", "ADAPTER_MISSING"))
M.append(row("F1", "PG khoá ngoại (ràng buộc / cặp bảng)", f"{ds['catalog']['constraints'].get('f', 0)} / {ds['catalog']['fk_table_pairs']}", "—", 0, 0, ds["catalog"]["fk_table_pairs"], 0, "NONE", "OK", "ADAPTER_MISSING"))
M.append(row("F1", "PG view→bảng (pg_depend)", ds["catalog"]["view_dep_pairs"], "—", 0, 0, ds["catalog"]["view_dep_pairs"], 0, "NONE", "OK", "ADAPTER_MISSING"))
M.append(row("F1", "PG cột / index / sequence", f"{ds['catalog']['columns']} / {ds['catalog']['relkind']['indexes']} / {ds['catalog']['relkind']['sequences']}", "—", 0, 0, "—", 0, "NONE", "OK", "ADAPTER_MISSING", "giá trị thấp, có thể là thuộc tính nút"))
dx = ds["directus"]
M.append(row("F2", "Directus collection", dx["directus_collections"], "species_collection_map 164 · collection_registry 168", 0, 0, dx["directus_collections"], 0, "NONE", "OK", "ADAPTER_MISSING",
             f"{dx['collections_vs_tables']['collection_no_table_folder_or_alias']} không có bảng (thư mục/view)"))
M.append(row("F2", "Directus field / relation", f"{dx['directus_fields']} / {dx['directus_relations']}", "—", 0, 0, dx["directus_relations"], 0, "NONE", "OK", "ADAPTER_MISSING"))
M.append(row("F2", "Directus flow / operation", f"{dx['directus_flows']} / {dx['directus_operations']}", "—", 0, 0, dx["directus_flows"], 0, "NONE", "OK", "ADAPTER_MISSING",
             f"flow→collection {dx['flow_collection_pairs']} · operation→collection {dx['operation_collection_pairs']}"))
M.append(row("F2", "Directus role/policy/access/permission", f"{dx['directus_roles']}/{dx['directus_policies']}/{dx['directus_access']}/{dx['directus_permissions']}", "—", 0, 0, dx["directus_permissions"], 0, "NONE", "OK", "ADAPTER_MISSING"))
qc = qd.get("collections", {})
M.append(row("F3", "Qdrant collection / point", f"{len(qc)} / {sum(v['points_count'] or 0 for v in qc.values())}", f"iu_qdrant_collection_registry {reg['iu_qdrant_collection_registry']['rows']} (thiếu production_documents)",
             0, 0, len(qc), 0, "NONE", "OK (GET metadata)", "ADAPTER_MISSING"))
M.append(row("F3", "KB tài liệu (incomex_metadata.kb_documents)", dbs["incomex_metadata"]["kb"]["kb_documents_rows_estimated"], "—", 0, 0, "—", 0, "NONE", "OK (reltuples); API KB: NO_ACCESS phiên này", "ADAPTER_MISSING",
             "phân rã vector_status = P191 (không quét toàn bảng)"))
M.append(row("F4", "Sổ tổ chức trong PG", len([k for k, v in reg.items() if v.get("exists")]), "17/17 tồn tại", "dot_tools (DotRegistryEntry)", 1, "16 sổ", 0, "R7 pgdot (dot_tools)", "OK", "PARTIAL",
             "trigger_registry chỉ được R7 đọc để đối chiếu; PgTrigger lấy từ pg_catalog"))
dsum, ddet = rt["summary"], rt["detail"]
M.append(row("F5", "Cây mã có nguồn trên đĩa", dsum["code_trees_with_source"], f"code-ledger {dsum['code_ledger_rows']} (UNKNOWN {dsum['code_ledger_by_status'].get('UNKNOWN', 0)})",
             5, 5, "xem GAP F5", 0, "Enola/Cognee/TS (5 cây)", "OK", "PARTIAL"))
M.append(row("F6", "Container / image / volume / mạng", f"{dsum['docker_containers']['total']}/{dsum['docker_images']}/{dsum['docker_volumes']['total']}/{dsum['docker_networks']}",
             "wf docker_containers 14 (PG) · Config Guard COMPOSE 5", 0, 0, dsum["docker_containers"]["total"], 0, "NONE (Graph)", "OK", "ADAPTER_MISSING"))
M.append(row("F6", "systemd timer / dịch vụ riêng / cron", f"{dsum['systemd_timers']}/{dsum['systemd_custom_services_etc']}/{dsum['cron_entries']}",
             "wf systemd_timers 32 · host_crontab 37 (PG) · Config Guard SYSTEMD 17/CRON 10", 0, 0, dsum["systemd_timers"] + dsum["cron_entries"], 0, "NONE (Graph)", "OK", "ADAPTER_MISSING"))
M.append(row("F6", "nginx host / location / đích proxy · cổng nghe", f"{dsum['nginx']['distinct_server_names']}/{dsum['nginx']['location_blocks']}/{dsum['nginx']['distinct_proxy_targets']} · {dsum['listening_tcp_sockets']}",
             "Config Guard NGINX 14", 0, 0, dsum["nginx"]["location_blocks"], 0, "NONE", "OK (đã che path-secret)", "ADAPTER_MISSING"))
M.append(row("F6", "Hàng đợi / pub-sub", "0 broker · PG outbox/job_queue · NOTIFY 2 kênh", "event_type_registry 52", 0, 0, "—", 0, "NONE", "OK", "ADAPTER_MISSING"))
M.append(row("F7", "Config Guard đích / Guard INV / Kuma / storage / code-ledger",
             f"{dsum['config_guard_targets']} / {len(dsum['guard_invariant_ids_in_code'])} / 22 / {dsum['storage_registry_rows']} / {dsum['code_ledger_rows']}",
             "chính các sổ này", 0, 0, "toàn bộ", 0, "NONE", "OK", "ADAPTER_MISSING"))
dcs = dc["summary"]
M.append(row("F8", "Repo: việc / P / DROOT / commit", f"{dcs['tasks_now'] + dcs['tasks_done']} / {dcs['p_entries_total']} / {dcs['droot_ids_defined_root_collab']} / {dcs['git_commits']}",
             "law_catalog 5 · normative_registry 47", 0, 0, "toàn bộ", 0, "git (có sẵn), chưa nối Graph", "OK", "ADAPTER_MISSING"))
ls_ = lk["summary"]
M.append(row("F9", "Lark base / bảng / trường / trường link", f"{ls_['bases_in_registry']} / {ls_['tables_total']} / {ls_['fields_total']} / {ls_['link_fields_total']}",
             "bases.yaml 19", "4 bảng · 11 trường · 4 loại cạnh", 4, ls_["tables_total"] - 4, 0, "r7_b6.py (88-phai-cu, 11 trường)", "OK (19/19)", "PARTIAL"))
dot_ok = len(G["DotCommand"]) == len(ddet["dot_bin"]) - 80 and len(G["DotRegistryEntry"]) == reg["dot_tools"]["rows"]
M.append(row("F10", "DOT: sổ tsv / bin / PG dot_tools", f"{dsum['dot_tsv_rows'] - 1} / {dsum['dot_bin_files']} (251 lệnh + 80 bản sao/khác) / {reg['dot_tools']['rows']}",
             f"dot_tools {reg['dot_tools']['rows']} (đường tệp {reg['dot_tools'].get('with_file_path')})", f"{len(G['DotCommand'])} lệnh + {len(G['DotRegistryEntry'])} dòng sổ",
             f"{len(G['DotCommand'])} + {len(G['DotRegistryEntry'])}", 0, 0, "R7 pgdot + 00-SO-DOT", "OK", "COMPLETE" if dot_ok else "PARTIAL",
             "DOT→PG khai báo CHAM 239 tệp: chưa thành cạnh (R11-X C)"))
out = {"graph_labels": {k: len(v) for k, v in sorted(G.items())}, "matrix": M}
json.dump(out, open(os.path.join(D, "coverage.json"), "w"), ensure_ascii=False, indent=1, default=str)
for r in M:
    print(f"{r['family']:4} {r['status']:16} {r['object'][:52]:52} U={r['universe']} G={r['graph']} miss={r['missing_in_graph']} extra={r['extra_in_graph']}")
