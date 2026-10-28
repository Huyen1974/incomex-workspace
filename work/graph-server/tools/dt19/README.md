# dt19 — bộ đọc độc lập nguồn sống cho audit 3 cổng (GS-DATA-TRUST-3GATE-AUDIT-20261028-19, P294)

- **Vai trò:** lần đọc THỨ HAI, độc lập với bộ đọc của `graph-refresh`/`graph_cert` (không dùng chung đầu ra), để so tập khoá nguồn sống ↔ Graph cho Docker container, cổng nghe TCP, kho git, tệp unit `/etc/systemd/system`, mục cấp 1 `/opt`, số dòng cron. CHỈ ĐỌC: `docker ps -a`, `ss -ltnH`, `listdir`, `find`; không ghi gì.
- **Cách chạy (từ Mac, không chép lên VPS):** `ssh contabo 'python3 -I -' < native_live.py > native_live.json`. Phía Graph lấy `gs_key` qua graph-v1 read-cypher rồi so tập (kết quả P294: docker 16=16; cổng nghe 21 sống = 21 nút còn hiệu lực + 1 nút đã retire có `retired_at`; git 8 kho + 1 bí danh symlink = 9 nút).
- **Mã băm:** `native_live.py` sha256 `65c6a23074fb64396c4d13f3cb9d0d8d1d3e24bef2bc8b0a13003e706ad618d0` — BYTE-IDENTICAL với bản đã chạy 28/10 14:53Z (không làm sạch).
- **Giới hạn:** đếm cron ở đây là đếm dòng đơn giản (42), KHÔNG cùng định nghĩa với `graph_cert` (51 mục, có run-parts) ⇒ không dùng để kết luận lệch. Không đọc PG/Directus (PROMPT cấm SQL trực tiếp; chưa có DOT đọc catalog), không đọc Lark/Qdrant.
- **Bằng chứng riêng tư** (tên container/cổng/đường, journal, last.json): chỉ trên Mac Owner `~/Incomex-Graph-View/evidence-private/GS-DATA-TRUST-3GATE-AUDIT-20261028-19/` (8 tệp + `SHA256SUMS`); ghi vào thư mục evidence trên VPS bị bộ phân loại auto-mode của Claude Code từ chối nên không ghi.
- Chưa đăng ký sổ công cụ Master Tool/DOT (nợ chung với `tools/ux16`, `tools/view-mac`, chủ sổ công cụ).
