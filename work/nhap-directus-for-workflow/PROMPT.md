# TS2 — CHUẨN HÓA DOT VÀ TỰ ĐỒNG BỘ dot_tools · KHÔNG ĐỘNG BA LÔ
RUN_ID: NDW-TS2-DOTTOOLS-AUTOSYNC-20261026-01
TASK: work/nhap-directus-for-workflow
STATUS: DRAFT_REVIEW_REQUIRED — KHÔNG RUN. Claude rà phạm vi kỹ thuật 1 vòng, Host ký READY trên last-touch; trước ghi production bắt buộc có G2·TS2 riêng của Owner.
EXECUTOR: Claude Code CLI; mọi PG/Directus/DOT qua cổng có quyền, repo theo A4/DROOT56, VPS-GHI/Điều 30/31 theo hiện trạng.

## MỤC TIÊU VÀ GIỚI HẠN
Đọc AGENTS.md, COLLAB bảng + §3.TQ K0–K10/SYNC-1..7 + P52/P54/P55 + §3.KH, PROMPT này; kiểm source code sống trước khi gọi. Theo P55: A vật PG đọc sống; Census so số; Graph đọc nguồn và canh riêng bởi Graph Host. Ba Lô, bốn báo cáo và socket = LEGACY, GIỮ NGUYÊN, tuyệt đối không sync/tắt/xóa/chạm. Không tạo S4/VIEW/đổi Graph/đăng báo cáo Nuxt. Chỉ khép danh tính DOT hợp lệ trên đĩa ↔ dot_tools để chuẩn bị cơ chế tự đồng bộ an toàn.
P52: dot-dot-catalog --check = 253/253 trong bộ lọc; dot_tools 314 dòng; 190 dòng thiếu script_path; 329 tệp dot-*; 129 chưa ghép theo tên. Các số 190/129 KHÔNG đồng nghĩa thiếu 190/129 tài sản; xác minh code/hash và active/backup/disabled/retired trước khi ghi.

## CỔNG
- S0 phải xác minh đúng RUN/READY, STOP, Guard, VPS-GHI, tải CPU/RAM/swap và không có worker trùng. Không STARTED/KQ trùng; không chạy lệnh có side-effect giả dạng --dry-run. Cấm dot-dot-health --dry-run, cấm dùng dot-report-publish SQL-error để lấy số (P52 bug 1.716 temp/CPU).
- Bất kỳ SQL/DOT runtime/role/scheduler hay thay dot_tools production cần Owner G2·TS2 có danh sách đối tượng/footprint, đường lùi và Guard; thêm cột/schema cần G1 riêng. Không có G2 cụ thể thì chỉ đo RO và KQ DỪNG/CHƯA ĐẠT, không lấy G2 tổng quát làm phép.
- Không sửa mô tả/nhãn/Owner quyết; không xóa/disable hoặc tạo dòng DOT chưa xác minh identity, không thay secret/token/permission; không tạo cron/timer/triggers mới tùy tiện. Mất quyền/không chứng minh read-only ⇒ STOP/UNKNOWN, không lách bằng REST/psql/shell.
- Không public dữ liệu định danh nội bộ: `/api/reports/live` chưa auth (P52) ⇒ TS2 không công bố View/Report. Khóa Graph thiếu DB và reader chưa dùng VIEW là việc Host Graph riêng.

## S0–S4 MỘT RUN CÓ CHECKPOINT
S0 · Kiểm read-gate, S0 VPS/Guard/cờ, so tập filename theo nguồn chuẩn và tính quyền writer; nếu chưa đủ cổng thì DỪNG sạch.
S1 · Đọc mã dot-dot-catalog/dot-dot-register và sổ dot_tools qua DOT RO hợp lệ. Lọc active/backup/disabled/retired, ghép code/hash/path; ghi 5 chỉ số distinct_active, mapped_exact, missing_verified, orphan_verified, ambiguous (số mới cùng mốc), không dump đường nội bộ trong repo.
S2 · Xác minh đường hiện có upsert idempotent + một lịch/trigger/nhịp canh thật, retry 1 lần+backoff; không viết cơ chế mới nếu dùng lại được. Nếu không có writer/cadence tin cậy thì ghi thiếu và đề xuất mở đúng một capability nhỏ cho G2 riêng.
S3 · Chỉ sau G2 cụ thể và đủ trước/sau: backup có hash, apply chỉ trường kỹ thuật của DOT đã match chắc chắn bằng đường đã duyệt; giữ mọi item ambiguous nguyên trạng; verify lại bộ ID/code/hash độc lập, rollback khi lỗi và Guard POST/return VPS-GHI. Không cập nhật S4/Graph/Balo.
S4 · Nghiệm thu tự động end-to-end qua nhịp chạy thật nếu có, dấu last_success/age, test fail-closed bằng fixture RO nếu an toàn, cảnh báo có người nhận/dedup nguồn. Không chứng minh được nhịp hoặc cần lịch mới ⇒ AUTO_SYNC=CHƯA ĐẠT, không tự chạy/treo chờ; chỉ ghi KQ scoped.

## TIÊU CHÍ XONG
Đã biết chính xác DOT nào active/thật, không tự thêm nhầm 129 file hay xoá nhầm registry; có đường được duyệt máy tự verify→sync→verify, báo lỗi nếu không tự cập nhật, có biên nhận lịch/cảnh báo, không nhân dữ liệu/không làm rơi nhãn. Nếu chưa có tick/người nhận/đường G2 thì KQ DỪNG hoặc MỘT PHẦN có blocker; không nhận XONG giả. KQ@NDW-TS2-DOTTOOLS-AUTOSYNC-20261026-01 tại mục P trống kế tiếp kèm số mới và evidence an toàn, Guard/rollback, 0 tệp/process tạm. NEXT_TRIGGER=GPT_HOST_NGHIEM_THU_TS2. Không tự TS3. Mục tiêu 50 phút, dừng 75 phút, không giữ terminal nền.

## CLAUDE REVIEW — MỘT VÒNG DUY NHẤT
Kiểm code/hash matching, đường DOT idempotent/nhịp có thật, G1/G2, rollback/guard, không chạm LEGACY, không public Nuxt hay sửa Graph; nếu thấy lỗi safety, sửa thẳng chính PROMPT và ghi Review trên last-touch. Host sẽ đọc diff và tự chốt READY, không quay lại bàn P48–P55.