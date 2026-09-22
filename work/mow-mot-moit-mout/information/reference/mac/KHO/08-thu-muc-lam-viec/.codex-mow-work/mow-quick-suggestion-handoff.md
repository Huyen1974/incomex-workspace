# MOW — GÓP Ý CẢI TIẾN MỘT DÒNG

Ngày: 2026-07-21  
Trang: `mow-unified-canvas-v2.html`

## Kết quả

Luồng Đề xuất/Cải tiến đã được hạ về đúng bản chất:

1. Người dùng bấm **Góp ý** hoặc biểu tượng trên một ô.
2. Chỉ một textarea xuất hiện.
3. Hệ tự gắn người, thời gian, vị trí MOW và task/run/bản ghi nếu trang gọi truyền sang.
4. Mỗi lần gửi tạo một row có event `IMPROVEMENT_SUGGESTION_QUEUED`.
5. Admin sẽ xem row trong sổ nháp; không có bước bắt buộc phân tầng, tạo phiếu hay sửa cấu trúc.

## Ranh giới an toàn

- Mã form đề xuất cấu trúc cũ vẫn còn trong file để không phá phụ thuộc cũ, nhưng nút chèn và “Đề xuất nâng cao” không còn truy cập được từ luồng thường.
- Bản này chưa ghi PostgreSQL. Row demo nằm trong `window.MOW_IMPROVEMENT_SUGGESTIONS`.
- Khi nối thật, server phải lấy `actor_id` từ phiên đăng nhập; không tin actor do trình duyệt gửi.
- Context từ MOT có thể truyền qua `window.MOW_SUGGESTION_CONTEXT` hoặc query: `task_id`, `run_id`, `step_run_id`, `business_record_type`, `business_record_id`.

## Nghiệm thu runtime

- Vào Góp ý từ T4 vẫn ở T4, không bị nhảy về T2.
- Form thật chỉ có một ô người dùng nhập.
- Context test tự nhận `TSK-42`, `RUN-7`, `BR-99`.
- Bấm biểu tượng trên ô `PB01` tự gắn `PB01 · Nhân sự`.
- Một lần gửi sinh đúng một row `QUEUED`.
- Quay về Thường đóng modal và khôi phục lưới ba thẻ.
- Không có runtime exception.

## Data-region delta

Thêm 11 mã: 10 mã `mow.propose.quick.*` và `mow.propose.advanced.open`; tổng 2 DỮ LIỆU, 5 HÀNH VI, 4 GIAO DIỆN. Danh sách chi tiết nằm trong `mow-quick-suggestion-data-region-manifest.csv`.

## Git

- Trước: `mow-before-simple-suggestion`.
- Sau: `mow-after-simple-suggestion`.

Vòng sửa cache bản nâng cao:

- Snapshot giao diện sống trước sửa: `mow-ui-current-protected-20260721`.
- Sau sửa: `mow-after-advanced-cache-fix-20260721`.

SHA-256 hiện tại sau vòng sửa cache:

- `mow-unified-canvas-v2.html`: `09ef2753b0a8643332f0e0ed638eea2a6024d45f4bfa76e9bc8deee788c96fdf`
- `mow-canvas-url-v1.js`: `3e381e96ce60fd6e87cea417eb3147010168a53af211403add5f927a9c155110`
- `mvx-v3.js`: `24351e04297e02064ee4408b2e745913693425882aaeee200bd654dc5ad5357c`
