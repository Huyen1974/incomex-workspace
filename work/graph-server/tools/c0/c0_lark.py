# GS-C0-COVERAGE-INVENTORY-20261022-05 · F9 · METADATA LARK CHỈ-ĐỌC — dùng lại được
# Chạy trên host VPS bằng venv lark-client (LarkReader chỉ-đọc, sổ base = config/bases.yaml):
#   ssh contabo 'cd /opt/incomex/lark-client && timeout 600 .venv/bin/python -I -B -' < c0_lark.py > lark.json
# Chỉ app/bảng/trường (tên, id, kiểu, đích link). KHÔNG đọc bản ghi. Ghi chú: LarkCore tự ghi nhật ký kiểm toán đọc
# của chính lark-client (hành vi sẵn có của bộ đọc, không phải thay đổi cấu hình).
import json, sys, time
sys.path.insert(0, "/opt/incomex/lark-client")
import yaml
from lark_client import LarkCore, LarkReader

reg = yaml.safe_load(open("/opt/incomex/lark-client/config/bases.yaml"))["bases"]
rd = LarkReader(LarkCore())
S, D = {"bases_in_registry": len(reg), "bases": {}}, {"bases": {}}
for b in reg:
    key, tok = b["key"], b["app_token"]
    ent = {"role": b.get("role"), "note": b.get("note")}
    try:
        tables = rd.list_tables(tok)
    except Exception as e:
        ent["access"] = f"NO_ACCESS:{type(e).__name__}"
        S["bases"][key] = ent
        continue
    ent["access"] = "OK"
    ent["tables"] = len(tables)
    nf = nl = 0
    det = []
    for t in tables:
        tid = t.get("table_id")
        try:
            fields = rd.list_fields(tok, tid)
        except Exception as e:
            det.append({"table_id": tid, "name": t.get("name"), "error": type(e).__name__})
            continue
        links = [{"field_id": f.get("field_id"), "type": f.get("type"),
                  "target_table": (f.get("property") or {}).get("table_id")}
                 for f in fields if f.get("type") in (18, 21)]
        nf += len(fields)
        nl += len(links)
        det.append({"table_id": tid, "name": t.get("name"), "fields": len(fields), "links": links})
        time.sleep(0.12)
    ent["fields"] = nf
    ent["link_fields"] = nl
    S["bases"][key] = ent
    D["bases"][key] = {"app_token": tok, "tables": det}
S["tables_total"] = sum(v.get("tables", 0) for v in S["bases"].values())
S["fields_total"] = sum(v.get("fields", 0) for v in S["bases"].values())
S["link_fields_total"] = sum(v.get("link_fields", 0) for v in S["bases"].values())
print(json.dumps({"summary": S, "detail": D}, ensure_ascii=False))
