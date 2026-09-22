# SUPERSEDED — KHÔNG CÒN LÀ TRẠNG THÁI HIỆN HÀNH

Tài liệu này ghi lại phương án tạm thời đã gộp `Đề xuất` vào `Góp ý`.  
Trạng thái hiện hành xem: `mow-proposal-chain-restore-handoff.md`.

# MOW — SỬA LỖI ĐỀ XUẤT NÂNG CAO NẠP BẢN CŨ

Ngày: 2026-07-21  
URL nghiệm thu: `mow-unified-canvas-v2.html?che-do=gop-y`

## Nguyên nhân

1. Trang nạp cùng `mvx-v3.js` ba lần với `?v=1`, `?v=2`, `?v=4`.
2. Trình duyệt có thể lấy lại cache cũ của một trong ba URL.
3. `mow-canvas-url-v1.js` không phải router; nó là lớp khôi phục UI cũ, ghi đè nút và CSS của luồng mới.
4. Tham số `?che-do=gop-y` vì thế không được định tuyến đúng.

## Đã sửa

- Chỉ nạp một file: `./mvx-v3.js?v=5`.
- Gắn build marker: `mvx-v3.2-20260721-v5`.
- Viết lại `mow-canvas-url-v1.js` thành router thuần, không can thiệp UI:
  - `thuong` → `normal`
  - `gop-y` → `proposal`
  - `van-hanh` → `instance`
  - `quan-tri` → `governance`
- Góp ý một dòng vẫn là mặc định.
- Thêm nút **Đề xuất nâng cao** riêng trong khung góp ý; nút này mở đúng node hiện tại.

## Nghiệm thu runtime

- Mở trực tiếp `?che-do=gop-y` đi vào `proposal`.
- Chỉ có một network resource `mvx-v3.js?v=5`.
- `window.MVX_BUILD = mvx-v3.2-20260721-v5`.
- Bản nâng cao T4 mở đúng `PB01 · Nhân sự`.
- Bản nâng cao T2 hiện đủ bảng thời gian, cộng dồn, thêm task, thêm buffer và các tổng.
- Đổi sang Thường cập nhật URL thành `?che-do=thuong`.
- Không có runtime exception.

## Git bảo vệ

- Mốc đã commit trước thay đổi lần này: `mow-after-simple-suggestion`.
- Snapshot đúng giao diện sống ngay trước khi sửa: `mow-ui-current-protected-20260721` — commit `b8272f7`.
- Tag sau sửa: `mow-after-advanced-cache-fix-20260721`.

SHA-256 sau sửa:

- `mow-unified-canvas-v2.html`: `09ef2753b0a8643332f0e0ed638eea2a6024d45f4bfa76e9bc8deee788c96fdf`
- `mow-canvas-url-v1.js`: `3e381e96ce60fd6e87cea417eb3147010168a53af211403add5f927a9c155110`
- `mvx-v3.js`: `24351e04297e02064ee4408b2e745913693425882aaeee200bd654dc5ad5357c`
