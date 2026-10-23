#!/usr/bin/env python3
# GS-C1C-PRODUCTION-TRUST-GATE-20261023-09 · cert-cells c1b-1 → c1c-1: thêm khối "families" (bảng cấu hình 9 họ G1–G9 cho ma trận bao phủ:
#   chủ · bộ liệt kê gốc · có nạp Graph không · khả năng thu thay đổi bền (CDC/audit) đo được · vùng ngoài phạm vi đã biết · người nhận báo · việc kế).
#   Không đổi ô nào (80 ô giữ nguyên byte theo khoá). Dùng: c1c_make_cells.py <cert-cells.json cũ> <out> <pg_cdc_caps.json>
import json, sys

src, out, capf = sys.argv[1:4]
c = json.load(open(src, encoding="utf-8"))
assert c.get("format") == "graph-cert-cells-v1" and c.get("catalog_version") == "c1b-1", c.get("catalog_version")
caps = json.load(open(capf))
H = "Graph Host · work/graph-server"
TG = "Telegram Owner qua đèn Kuma #24 «Graph Certificate» (ĐỎ mỗi lượt · VÀNG một lượt + nhắc 168h) · biên nhận state/refresh/cert/incidents.jsonl"
NIGHT = "chụp mỗi đêm trong graph-refresh 22:40Z + so ảnh tốt trước (NIGHTLY_SNAPSHOT_DIFF) — sinh rồi mất giữa hai lượt KHÔNG thấy"
F = {
    "G1": {"family": "pg", "owner": H + " (bao phủ) · chủ PG/DOT (schema, D20)", "supported_ingestion": True,
           "durable_change_capture": {"available": False, "signal": "NIGHTLY_SNAPSHOT_DIFF + pg_current_wal_lsn làm mốc đọc (không phải con trỏ CDC)",
                                      "measured": caps, "why": "CDC_NOT_AVAILABLE: wal_level=%s, %s slot logic, %s publication, %s event trigger — không có "
                                      "subscriber bền đã xác nhận (outbox/NOTIFY chưa chứng minh); DDL không bắt được bằng logical decoding; C1-C KHÔNG cài "
                                      "Debezium/slot/đổi cấu hình PG" % (caps.get("wal_level"), caps.get("logical_slots"), caps.get("publications"), caps.get("event_triggers"))},
           "out_of_scope_unknown": ["thay đổi dữ liệu dòng (giá trị FK, bản ghi) — TRANSIENT_CHANGE_BLIND_SPOT", "role/grant/RLS policy/extension/sequence/index",
                                    "db mới chưa nhận (chỉ thấy tên ở cửa)", "thân hàm: chỉ vân tay md5(prosrc) — nghĩa ở L2"],
           "next_action": "C1-D: nhận theo lô có bảo vệ 394 bảng/700 view/FK/Directus toàn cục vào lane pgdot; CDC/audit chỉ khi Owner duyệt riêng"},
    "G2": {"family": "docker", "owner": H + " (bao phủ) · chủ hạ tầng VPSC", "supported_ingestion": False,
           "durable_change_capture": {"available": False, "signal": NIGHT, "why": "docker events không có người nhận bền; image ID đổi dưới tên cũ ⇒ SỬA ở lượt kế"},
           "out_of_scope_unknown": ["biến môi trường/secret container", "nội dung lớp image", "container sinh-xoá giữa hai lượt (workspace-job-* là mẫu tạm)"],
           "next_action": "C1-D: lớp DockerContainer/Image/Mount trong Graph + ô đối chiếu ID"},
    "G3": {"family": "systemd", "owner": H + " (bao phủ) · chủ hạ tầng VPSC", "supported_ingestion": False,
           "durable_change_capture": {"available": False, "signal": NIGHT, "why": "journal không phải sổ thay đổi tệp unit có người nhận bền"},
           "out_of_scope_unknown": ["unit gói trong /lib/systemd/system", "unit tạm /run/systemd", "unit người dùng"],
           "next_action": "C1-D: lớp SystemdUnit (mọi loại) + drop-in + cạnh EXECS/TRIGGERS"},
    "G4": {"family": "cron", "owner": H + " (bao phủ) · chủ hạ tầng VPSC", "supported_ingestion": False,
           "durable_change_capture": {"available": False, "signal": NIGHT, "why": "cron không có audit; sửa dòng thấy qua sha256 tệp ở lượt kế"},
           "out_of_scope_unknown": ["crontab người dùng ngoài spool", "at/anacron"], "next_action": "C1-D: lớp CronEntry + cạnh RUNS"},
    "G5": {"family": "nginx", "owner": H + " (bao phủ) · chủ cổng/route (MCPW/VPSC)", "supported_ingestion": False,
           "durable_change_capture": {"available": False, "signal": NIGHT, "why": "nginx -T chỉ là ảnh cấu hình; cổng nghe đọc ss -ltn lúc chụp"},
           "out_of_scope_unknown": ["route bên trong ứng dụng container", "tường lửa", "đường path-secret chỉ lưu băm"],
           "next_action": "C1-D: lớp NginxServer/Route/Listener + đối chiếu"},
    "G6": {"family": "opt", "owner": H + " (bao phủ) · chủ sổ mã (VPSC, INV23)", "supported_ingestion": True,
           "durable_change_capture": {"available": False, "signal": NIGHT + " + vân tay sha256 tệp mã trong code-ledger",
                                      "why": "Config Guard canh băm đích đã đăng ký (drift-check), không phải sổ thay đổi cho mọi tệp"},
           "out_of_scope_unknown": ["cây thư mục sâu hơn cấp 1 ngoài sổ mã", "thư mục dữ liệu chạy"], "next_action": "C1-D: lớp OptEntry/CodeFile + ô ID"},
    "G7": {"family": "qdrant", "owner": H + " (đo) · chủ Agent Data/KB (sửa lệch KB↔Qdrant)", "supported_ingestion": False,
           "durable_change_capture": {"available": False, "signal": NIGHT + " (collection/alias/points_count + tập document_id băm)",
                                      "why": "Qdrant không có luồng thay đổi; vector/payload khác document_id không đọc"},
           "out_of_scope_unknown": ["vector", "payload ngoài document_id", "point thiếu document_id (đếm, không định danh)"],
           "next_action": "C1-D: ô ID document_id ↔ kb_documents (M-b) + lớp QdrantCollection"},
    "G8": {"family": "lark", "owner": H + " (bao phủ) · chủ dữ liệu Lark (nghiệp vụ)", "supported_ingestion": True,
           "durable_change_capture": {"available": False, "signal": NIGHT + " (bases.yaml + bảng/trường liên kết; b88 bản ghi băm)",
                                      "why": "chưa đăng ký sự kiện Lark (event subscription) — bản ghi ngoài b88 không theo dõi"},
           "out_of_scope_unknown": ["bản ghi/giá trị liên kết ngoài base 88 (dữ liệu riêng tư)", "base không có trong bases.yaml"],
           "next_action": "C1-D: lớp LarkTable/LinkField metadata cho 19 base; bản ghi chỉ khi có connector + Owner duyệt"},
    "G9": {"family": "git", "owner": H + " (bao phủ) · chủ kho (TQT sổ công cụ ML-DEF-023 cho công cụ)", "supported_ingestion": True,
           "durable_change_capture": {"available": True, "partial": True, "signal": "GIT_COMMIT_LOG cho nội dung đã commit + HEAD/tree mỗi đêm",
                                      "why": "lịch sử commit bền cho tệp tracked; cây làm việc/tệp chưa commit/bản triển khai không nằm trong log"},
           "out_of_scope_unknown": ["tệp chưa commit / cây làm việc bẩn", "kho sâu hơn 3 cấp dưới /opt/incomex", "bản đang chạy khác HEAD (đo ở lane code)"],
           "next_action": "C1-D: ô ID mã (code:*) so tệp/ký hiệu với bản đang chạy"},
}
for g in F:
    F[g]["alert_recipient"] = TG
c["families"] = F
c["catalog_version"] = "c1c-1"
c["written_by"] = "GS-C1C-PRODUCTION-TRUST-GATE-20261023-09"
json.dump(c, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1, sort_keys=True)
print("cells", len(c["cells"]), "families", sorted(F), "→", out)
