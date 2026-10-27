# PG-A1 — CATALOG/DEPENDENCY NATIVE TRÊN 3 DB · SQL CONTRACT CHO V1/V2
RUN_ID: NDW-PGA1-CATALOG-DEPENDENCY-20261027-01
TASK: work/nhap-directus-for-workflow
EXECUTOR_SURFACE: Claude Code CLI
READ_PATH: claude-mcp `query_pg` hiện tại, đúng `context_pack_readonly`, READ ONLY, `statement_timeout=5000`; **P69 đã chứng minh cổng chỉ nhận SELECT và CHẶN SHOW**. Chỉ dùng SELECT catalog trong đúng mẫu validator cho phép, không đổi allowlist/parser hay dùng lối admin; đọc repo qua workspace/Git, vps_status RO.
WRITE_PATH: chỉ `workspace_edit` ghi STARTED/KQ và bảng điều khiển của task `COLLAB.md`; **không có PG/Directus/Docker/Graph/Nuxt runtime mutations**.
STATUS: DRAFT_FOR_ONE_CLAUDE_CHAT_REVIEW — chưa có Host READY/STARTED cho RUN mới. P69 G0-L0 đã KQ DỪNG·MỘT PHẦN và P70 Host đã nghiệm thu; READY P68 áp cho RUN cũ không dùng. Claude Chat phản biện prompt PG-A1 một lượt, Host ký READY đúng last-touch mới, Owner dispatch một câu DROOT38 khi tới lượt (ưu tiên GitHub). Không cần G1/G2 vì đây là READ-ONLY.

## 0. MỤC TIÊU CỤ THỂ: ĐEM PG18 VÀO SỬ DỤNG, KHÔNG LẶP L0
- Đích lâu dài = Sổ PG Tự quản: PG-native catalog/vật/quan hệ; sau PG-A1 chuẩn bị **01 SQL View V1 vật + 01 SQL View V2 quan hệ** (DDL DRAFT thôi, **không CREATE trong RUN này**), làm nền PG-A2 S4+V3 đối soát; mỗi dữ liệu một nguồn, không nhân Ba Lô/registry. Không đợi Graph/PG file mount/nginx/Kuma để kiểm kê PG đã đọc được.
- P69 evidence đã chốt: `query_pg` PASS role `context_pack_readonly` (READ ONLY, statement_timeout 5s), cho phép DB `directus`, `incomex_metadata`, `workflow`, CHẶN `postgres`; PG18.6, Directus12.4.1, postgres_fdw đang cài, pg_cron/pgvector không có; DOT filesystem privileged live-reading BLOCKED_FOR_L1; E1 Kuma SQL-result monitor không PASS; Nginx REPORTS public P0. **KHÔNG khảo sát lại P69, không thêm quyền query_pg, không gợi ý đổi validator**. SQL chỉ metadata/schema.
- PG-first (AGENTS R1a, Tiêu chí 0): ưu tiên `pg_catalog`, `pg_depend`, `pg_rewrite`, `pg_constraint`, `pg_trigger`, `pg_identify_object`, `pg_shdepend` (khi scope cluster cần), native VIEW/CTE. Directus Flows 111 active và Qdrant/RAG/Graph là bổ sung không ảnh hưởng số đếm/hợp đồng V1/V2.

## S0 — Read-gate đơn giản
Đọc AGENTS.md→task COLLAB §0/board/P52/P55/P65/P67/P68/P69/P70/§3.TQ/§3.KH→PROMPT; chỉ thi hành nếu đúng run, có Reviewer đã Host chốt + READY last-touch, Owner dispatch, 0 STOP/COUNCIL_ALERT/trùng STARTED/KQ. Recheck VPS load/PSI, role+allowlist/READ ONLY/timeout trong `query_pg`. G0 READ không lấy VPS-GHI; nếu CPU/memory cạnh tranh với GitHub hoặc query path không hợp lệ thì KQ DỪNG trước truy vấn. Cấm `psql`/Docker exec/direct REST/admin token làm đường vòng.

## S1 — Bộ kiểm đếm tài sản PG ở 3 DB được phép, cùng mốc
- Đọc đúng script/SQL Census TS1 (P52) đang có, tái dùng bộ loại 12 + loại ngoài nếu đã được chứng minh; 3 DB directus, incomex_metadata, workflow từng DB riêng; database postgres = `UNKNOWN/ACCESS_DENIED`, **không** mở allowlist. Chỉ SELECT catalog metadata, không SELECT dữ liệu nghiệp vụ, thân hàm, source code hay file/secret; không SELECT COUNT(*) bảng lớn.
- Đầu ra mỗi DB, mỗi loại: `total · distinct identity · duplicate identity · no_parent/invalid_parent` khi loại có quan hệ cha; cluster objects phân riêng. Identity chuẩn phải chứa tên DB + object class/type + namespace + native signature/name (`pg_identify_object` khi phù hợp), không dùng OID đơn lẻ như khóa vĩnh viễn; dấu OID/time chỉ là evidence để phát hiện DROP+CREATE trùng tên.
- Với `directus` so đếm Census từng loại **cùng phép lọc schema/mốc**, ghi chênh nếu có và lý do snapshot khác; với metadata/workflow nêu số thật và scope, không suy từ P69 (10 tables/1 view/15 funcs chỉ là snapshot cũ). SQL output chỉ aggregate + vài mẫu không nhạy cảm (không dump danh sách nội bộ/định nghĩa/function body lên GitHub).

## S2 — Quan hệ PG-native và giới hạn thực tế
- Đọc `pg_depend` + `pg_rewrite` (đúng cách map rule `ON SELECT` thành VIEW sở hữu) + `pg_constraint` cho FK + `pg_trigger` cho trigger, `pg_shdepend` cho object dùng chung khi quyền đọc đạt. Phân loại `PG_DECLARED_DEP | FK | VIEW_REWRITE | TRIGGER_OWNER | UNKNOWN_DYNAMIC_CODE`, phân biệt quan hệ sở hữu/tham chiếu/phụ thuộc DROP, không suy 'sử dụng lúc chạy' từ `pg_depend`.
- Viết **SELECT bắt đầu bằng từ khóa SELECT** với subquery/aggregate cho quan hệ; chỉ dùng WITH/recursive CTE nếu chính `query_pg` validator đã xác minh CHẤP NHẬN ở vai RO (P69 đã chặn SHOW, không giả parser nhận mọi cú pháp SELECT). Nếu WITH bị từ chối, dùng SELECT lồng/giới hạn một tầng hoặc báo `CTE_UNKNOWN`, **không sửa validator/lách cổng**. Đo số cạnh unique, nguồn/đích chưa map, deptype và dependency qua pg_rewrite/FK; không crawl body/dynamic SQL, không EXPLAIN ANALYZE hay đệ quy vô hạn. Thiếu cạnh không chứng minh vật bỏ được.

## S3 — Chuẩn bị hợp đồng SQL View native có thể áp ngay ở PG-A2
- Đề xuất **V1 asset_catalog**: `db_scope, kind, namespace, canonical_key, native_identity, parent_key, oid_observed, observed_at, source/status` với dữ liệu đọc catalog; V2 `dependency_edges`: `source_key, target_key, relation_type, dependency_type, source_catalog, observed_at, completeness`, không Graph làm oracle. Giữ ≤3 VIEW toàn bộ chương trình khi sau này thêm V3; ở RUN này 0 CREATE/ALTER/INSERT.
- Nêu **SQL SELECT có thể thực thi** (ngắn, tổng hợp/parameter scope), hướng SQL VIEW áp qua DOT hiện có `dot-pg-atomic-apply` sau G1/G2, vấn đề DB cross-namespace: PG VIEW thuộc một DB; **không giả có VIEW tự đọc 3 DB**. Muốn PG tập trung nhiều DB cần `postgres_fdw` + user mapping/USAGE/FDW table design **có phép riêng**, hoặc phục vụ nhiều DB bằng SELECT RO riêng. Ghi rõ đường nào hiện đã có, đường nào chưa, 0 tự CREATE FDW/SERVER.
- Khả năng hiển thị: SQL View không là UI/không tự bảo vệ REST; P69 nginx unauth P0 giữ nguyên, **chưa công bố metadata**. S4 quyết định Owner chưa tạo; role người xem, người duyệt và Graph bridge thuộc giai đoạn sau.

## S4 — KQ và điều phối đúng chủ, không sa đà giám sát
- P69 `BLOCKED_FOR_L1` giữ nguyên: quyền `pg_read_server_files` có thể đọc `/proc/1/environ`/PGDATA, không cấp role, không mount DOT, không tái chạy P64 L1. `file_fdw` available chưa cài, baseline hash 12 hex chưa được Owner chốt, không báo file_changed về lịch sử. 24 SECURITY DEFINER executable rộng là **RISK_NEEDS_PG_SEC_REVIEW**, không gọi hàm/đọc thân hay sửa PUBLIC. Nginx P0 unauth 3 route/domain chuyển Host Web/SEC hiện hữu, không sửa task khác trong lượt; E1 Kuma2.2.1 Postgres monitor không đánh giá SQL result, không chặn catalog. `job_queue` 7 queued từ tháng 5: **một** nợ worker ownership, không tạo 7 ticket/khởi chạy worker.
- Có thể viết **đề xuất không-code** cho E1 về hai đường reuse cần kiểm: Directus Flows 12.4.1 Schedule→Read Data (sau có VIEW registered)→Condition→Request URL tới Kuma Push, hoặc Guard push hiện hành; quyền/flow chạy thật/chống spam/biên nhận còn UNKNOWN, không thêm flow/kuma monitor trong PG-A1. Nguồn Directus Docs: https://docs.directus.io/app/flows/operations ; Kuma Push docs: https://github.com/louislam/uptime-kuma/wiki/Internal-API .
- Ghi tại P kế tiếp trong COLLAB: bảng 3 DB/12 loại (aggregate), identity/parent/edge class, ca đọc dependency mẫu, hợp đồng V1/V2 và Gate G1/G2 nếu muốn triển khai, **trạng thái PG-A1 KQ XONG_CÓ_GIỚI_HẠN** nếu cả 3 DB RO đo được, DB postgres UNKNOWN vẫn nêu; nếu thiếu read-path/timeout thì DỪNG có blocker. Guard/lease/0 temp/mutation, NEXT_TRIGGER=GPT_HOST_NGHIEM_THU_PG_A1. Không tự mở PG-A2/S4, không tự sửa nginx/security/queue.

## Bước ngắn DROOT48
| Bước | Ai | Trigger/giới hạn | Bằng chứng | Khi hỏng/bước kế |
| S0 | Claude Code | Dispatch; ≤3 phút | query_pg role/RO/timeout, STOP, VPS nhẹ | Gate fail KQ DỪNG |
| S1 | Claude Code | S0; ≤8 phút | 3 DB × loại, distinct/parent/scope | Catalog unsupported -> UNKNOWN, S2 |
| S2 | Claude Code | S1; ≤7 phút | pg_depend/pg_rewrite/FK/trigger & bounded CTE | Query timeout → giảm phạm vi, ghi PARTIAL |
| S3 | Claude Code | S2; ≤7 phút | SELECT native V1/V2 DRAFT, crossDB constraint | Missing grant → Owner gate sau |
| S4 | Claude Code | S3; ≤5 phút | KQ/Guard/0 temp/next | Host nhận, không tự RUN tiếp |
Hard stop 35 phút, tuần tự từng SELECT, không chạy nhiều query song song/scan doanh nghiệp, không giữ terminal chờ, không gửi Telegram.

## Review của Claude Chat — 01 vòng rồi Host ký READY
Kiểm P69/P70 và PROMPT mới: scope 3 DB `postgres` deny, PG18 native identity/dependency qua pg_rewrite đúng, SQL có thể chạy bởi query_pg validator/timeout, không chạy lại TS1/P69 và không ghi dữ liệu; không đợi E1/nginx/Graph, có DDL V1/V2 hợp đồng thực thi sau G1/G2. Nếu đồng ý, ghi P tiếp theo REVIEW ACCEPTED/PARTIAL vào COLLAB; chỉ sửa PROMPT khi có lỗi kỹ thuật thật, Host ký READY trên last-touch, Owner dispatch DROOT38. Không cần vòng thảo luận kiến trúc khác.