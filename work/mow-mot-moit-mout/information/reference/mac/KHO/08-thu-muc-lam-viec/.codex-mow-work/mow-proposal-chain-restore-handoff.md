# MOW — KHÔI PHỤC CHUỖI ĐỀ XUẤT

Ngày: 2026-07-21  
Phạm vi: chỉ `Đề xuất -> Đề xuất cải tiến -> Đề xuất nâng cao`.

## Nguyên nhân

- Commit `29eeb86` đổi nhãn `Đề xuất` thành `Góp ý` và chèn modal góp một dòng đè luồng đề xuất cũ.
- Router sau đó ghi mode `proposal` thành URL `che-do=gop-y`, làm hai khái niệm tiếp tục bị gộp.
- Mốc Git ngay trước thay đổi là `89f6c0d`.

## Đã khôi phục

- Nút chế độ trở lại `Đề xuất`.
- Banner trở lại `Chế độ Đề xuất — Cải tiến quy trình`.
- Bỏ lớp quick-suggestion đã đè nút thêm ô và nút cải tiến.
- Khôi phục luồng ba tầng:
  1. Vào `Đề xuất`.
  2. Chọn một ô để `Đề xuất cải tiến`.
  3. Từ trình sửa mở `Đề xuất nâng cao`.
- URL của mode này là `?che-do=de-xuat`, không còn là `?che-do=gop-y`.
- Giữ cải tiến an toàn: chỉ nạp một `mvx-v3.js?v=5`, không quay lại ba URL cache cũ.

## Nghiệm thu runtime

- URL `?che-do=de-xuat` vào đúng mode `proposal`, tầng T2.
- Có 6 nút cải tiến và 7 vị trí thêm ô trong dữ liệu mẫu hiện tại.
- Trình cải tiến có tên, thêm mục, gửi đề xuất và lối vào nâng cao.
- Nâng cao có 5 ô thời gian công việc trong case kiểm thử.
- Bật cộng dồn: `TỰ ĐỘNG`, tổng 105, ô tổng bị khóa.
- Tắt cộng dồn: `NHẬP TAY`, nhập 99 và giữ đúng 99.
- Không có runtime exception.

## Git

- Trước khôi phục: tag `mow-before-restore-proposal-chain-20260721` -> `ff0ddc3`.
- Sau khôi phục: commit `e9c0885`, tag `mow-after-restore-proposal-chain-20260721`.
- Commit sau chỉ gồm hai file:
  - `mow-unified-canvas-v2.html`
  - `mow-canvas-url-v1.js`

SHA-256 sau khôi phục:

- `mow-unified-canvas-v2.html`: `4a168e4500899b247fd57087d63071dfc785ea705c5a6a4921f362402a5df4d7`
- `mow-canvas-url-v1.js`: `67028d73b145e5aef79390e45bab8e6906f3d1c5f149afcf796a9a2f490c14a5`
- `mvx-v3.js`: `24351e04297e02064ee4408b2e745913693425882aaeee200bd654dc5ad5357c`
