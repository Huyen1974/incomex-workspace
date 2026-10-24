# B0 — KIỂM KÊ DIRECTUS + POSTGRESQL + DOT — CHỈ ĐỌC
RUN_ID: NDW-B0-INVENTORY-20261024-01
Executor_Surface: Claude Code CLI trên Mac Owner (đường DOT tới VPS1 như các RUN trước).
Write_Path: repo `incomex-workspace`, chỉ ghi `work/nhap-directus-for-workflow/COLLAB.md` (commit tiền tố `[Claude Code]`) · VPS1: chỉ DOT ở chế độ đọc / `--check` / `--dry-run`; tệp tạm duy nhất được phép là snapshot JSON của `dot-schema-snapshot` trong `/opt/incomex/dot/snapshots/`. Không ghi Directus/PG.

**Trạng thái:** GPT Host chốt phạm vi B0 theo P21; Owner chuyển thủ công cho Claude Code. Chỉ được đọc dữ liệu và metadata; **KHÔNG** tạo/sửa/xóa collection, table, Field, Flow, quyền, data hay production. G1/G2 vẫn chờ Owner duyệt riêng. Đây là công việc thật, không tạo dữ liệu test hay bản HTML mới.

**Bắt buộc trước khi thao tác:** đọc `AGENTS.md`; đọc `work/nhap-directus-for-workflow/COLLAB.md` từ §0, P20–P21 và §3.KH. Kiểm tra Git/nguồn hiện hành. Dùng DOT hoặc wrapper **đã được phép** theo DROOT26/DROOT35; tuyệt đối không dùng SQL/REST/CLI trực tiếp để thay thế DOT, không đưa secret/token vào kết quả. Nếu công cụ cần thiết không có chế độ chỉ đọc đáng tin cậy, ghi rõ thiếu và bỏ phần đó, không tự tạo DOT mới trong B0.

**Đường đọc đã biết (Reviewer Claude đã xem mã DOT và trang báo cáo ngày 24/10) — dùng trước khi tìm đường khác:**
- Collection + field + quan hệ + ghi chú `?`: `dot-schema-snapshot` (chỉ ghi 1 tệp JSON vào `dot/snapshots/`).
- Tên mọi bảng PG: báo cáo PG Census có sẵn `/reports/report-pg` (24/10: 393 table · 699 view · 10.099 cột) và `/reports/report-balo-table` (danh sách table theo schema) — chỉ đọc trang, không truy vấn PG. Số «~351» trong P21 là số cũ.
- DOT ↔ `dot_tools`: `dot-dot-catalog --check` · `dot-dot-health --dry-run` · `dot-dot-register --dry-run` · `dot-fill-tool-descriptions --dry-run`; danh mục đĩa `/opt/incomex/dot/00-SO-DOT.tsv` (bản 08/10).
- **KHÔNG chạy trong B0:** `dot-collection-health` (ghi `system_issues`), `dot-collection-create` (ghi 6 sổ hệ thống: `meta_catalog`, `schema_birth_registry`, `collection_registry`, `collection_labels`, `collection_species`, `entity_dependencies`), `dot-schema-apply`, `dot-content-create/update/delete`, và mọi DOT chưa chứng minh được chế độ không ghi. Mục (D) nêu rõ DOT nào trong số này dùng được cho B1 và cách tránh ghi nhầm sổ hệ thống.

## Các việc phải thực hiện trong một lượt B0

1. **Directus:** xác định instance/backend DB ở mức cấu hình không lộ secret; liệt kê tên toàn bộ collection qua công cụ đọc metadata (không duyệt từng bản ghi). Với nhóm liên quan cỗ máy — `meta_catalog`, `dot_tools`, Công thức/CT-000.1/CT-008, 43 câu hỏi, Field, MBM, MMOW, MOW, khuôn, Miền CV, hồ sơ — đọc kỹ field, mô tả `?`, quan hệ, quyền, mã sổ, số bản ghi nếu lấy được an toàn. Chỉ ghi **đã có** khi xác nhận tồn tại thực.
2. **PostgreSQL:** lấy **danh mục tên bảng/schema mức metadata** để nhận diện trùng và chọn tái sử dụng; **KHÔNG** vét dữ liệu hoặc kiểm chi tiết tất cả hàng trăm bảng. Chỉ kiểm chi tiết cấu trúc/PK-FK/quyền/phụ thuộc và số dòng bằng cách nhẹ/an toàn cho **bảng liên quan cỗ máy** (nhất là `meta_catalog`, `dot_tools`, `workflows` và bảng mapping với Công thức/Field/MMOW/MOW). Không truy cập dữ liệu nhạy cảm và không chạy count toàn bảng lớn. Phân biệt bản trong Master MOW với bản ghi `workflows` thật.
3. **DOT:** dựa trên danh mục hiện có và các lệnh đọc/--help/dry-run được chứng minh không ghi, đối chiếu `dot_tools` (CAT-006) với file lệnh thực tế; nhận diện DOT đọc/tạo collection, sửa schema/field/relationship và đường ghi B1, nêu cái còn thiếu. Số lượng báo cáo cũ chỉ là mốc lịch sử, không được gọi là hiện trạng chưa đo. **Không tạo `nhap_dot`, không sửa registry trong B0.**
4. **Sổ của các sổ + nguồn cũ:** đối chiếu `meta_catalog`, Master of Master, ML-DEF và HTML Công thức đã chốt chỉ để xác định nguồn/chênh lệch, **không mở lại HTML để sửa nghiệp vụ**. Tìm collection hiện có phù hợp cho Công thức. Ưu tiên dùng lại; collection mới nếu cần phải đề xuất tên kỹ thuật **dùng lâu dài, không `nhap_`/`test_`**, trạng thái ĐANG THIẾT KẾ tại nhà SSOT.
5. **Quyền và chốt B1:** kiểm cơ chế bảo vệ nào hiện còn phụ thuộc tiền tố `nhap_`; xác định danh sách collection/role/DOT mà B1 cần được Owner duyệt. Tuyệt đối **không** thay quyền, tạo bảng hay tự đổi cờ READY cho B1.

## Đầu ra tối thiểu

Ngay sau read-gate ghi `STARTED@NDW-B0-INVENTORY-20261024-01 <UTC> · executor=Claude Code` vào COLLAB; khi xong ghi `KQ@NDW-B0-INVENTORY-20261024-01 XONG|DỪNG` cùng commit báo cáo.
Ghi **một báo cáo ngắn** vào chính `work/nhap-directus-for-workflow/COLLAB.md` (mục kết quả B0) và cập nhật Bảng điều khiển; commit/push rồi đọc kiểm lại. Nội dung gồm: (A) bảng collections Directus: tên / có thật / trường-quan hệ chính / nhà SSOT / trạng thái / dùng lại-thiếu; (B) bảng PG **sẽ dùng**: schema.table / chức năng / dùng lại-sửa-tạo-không đụng / liên hệ Directus / mức xác minh; (C) DOT có sẵn và thiếu đúng 1–3 năng lực liên quan đến B1; (D) đề xuất B1 Công thức với tên, schema tối thiểu, quyền, nguồn/đích, quyết định Owner cần phê duyệt. Mục chưa kiểm được ghi `CHƯA KIỂM`, không tự đánh dấu đạt.

**Thời gian:** cố gắng ≤15 phút/lượt; nếu khối lượng lớn, hoàn thành nhóm liên quan Công thức và bảng nền trước, lưu checkpoint/phần còn lại rõ ràng, **không quét vét cạn**. Không phát RUN B1, không thay đổi production, không tạo HTML/app/collection trong B0.

**Kết thúc:** báo Owner tối đa 6 dòng: số collections đã kê; số PG tables liên quan đã xác minh; bảng nào có thể dùng lại; DOT thiếu; B1 đề nghị; commit + trạng thái B0 ĐẠT/MỘT PHẦN/CHƯA ĐẠT.