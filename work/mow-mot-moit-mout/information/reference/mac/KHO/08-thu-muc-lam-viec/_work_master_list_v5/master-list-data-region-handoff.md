# Handoff master-list v5 — 3 cột T3/T2/T1 và đường dẫn 8 đoạn

## Kết quả

- Snapshot nguồn: `7e09569` — `master-list: 3 cot T3-T2-T1 + duong dan 8 doan + cache v5`.
- `master-list.js`: 42.496 byte, SHA-256 `68b6478407428815784ed5c5a3959b2db6b5a925b6f8aec6a3945e65304f105d` trước; SHA-256 `af6f51afbbc15a3374139a87109e4791eba390cf986b3d2db161e0752d6b2df6` sau.
- Số mã `master.*`: **135 trước -> 143 sau**. Giữ nguyên toàn bộ 135 mã cũ; thêm đúng 8 mã trong `master-list-data-region-manifest.csv`.
- Trọng tài runtime liên trang: source 143 = DOM union 143; thiếu 0, thừa 0; 31 state; lỗi JS/runtime 0.

## Thay đổi hiển thị

1. Bảng dùng chung có ba cột: `Chuyên môn (T3)`, `Nhiệm vụ (T2)`, `Công việc (T1)`.
2. Tầng không có dữ liệu hiển thị `·`; không tự bịa node.
3. Đường dẫn cố định 8 đoạn: `T7 / T6 / T5 / T4 / T3 / T2 / T1 / item.name`.
4. Dạng cây hiển thị đường dẫn đủ 8 đoạn cho từng item.
5. Drawer luôn có 7 dòng tầng và dòng thứ 8 là tên cụ thể của bản; không dùng chữ loại chung như `moit` hoặc `mout`.

## Cache và phạm vi file

- Đã bump `master-list.js?v=4` thành `v=5` tại: `master-hub.html`, `mot-master-v1.html`, `mow-master-v1.html`, `mout-home-v1.html`, `moit-master-v1.html`.
- `master-list-quy-trinh-v1.html` vẫn dùng `?ts=` no-cache nên không bump.
- `moit-master-v1.html` trước đó chỉ có ở local, chưa có trên VPS; vòng này đã đưa lên VPS với `v=5`. Tám mã `moitmaster.*` của trang không đổi.
- `eco-nav.js`, `mot-theme-v1.css`, `master-list-quy-trinh-v1.html` không đổi byte.

## Kiểm chức năng

- MOT có T1: `CM Xuất nhập kho / QT Nhập kho / CV Nhập kệ` hiển thị đúng.
- MOT item đang neo T2: T1 hiển thị `·`, đúng dữ liệu hiện có.
- MOUT có T1 và MOUT khuyết T1 đều đúng; ca neo T6 xác nhận T2 và T1 cùng có thể là `·`.
- MOIT neo T2: T1 hiển thị `·`; đuôi là tên form cụ thể.
- Drawer MOUT: 8 giá trị, đuôi `Doanh thu theo khách hàng`.
- Master Hub vẫn hiện cột Mẹ; drawer quy trình vẫn hiện ma trận `master.process.*`.

## Lưu ý dữ liệu

- Engine chỉ suy từ `item.anchor` qua cây hiện có; không sửa hoặc đoán lại anchor của từng item.
- Một số task MOT mẫu hiện đang neo T2 nên T1 là `·`. Nếu nghiệp vụ xác nhận chúng có node T1 cụ thể, cần sửa dữ liệu item/registry sau; không sửa logic engine.
- Danh sách mẫu của các consumer hiện vẫn là `MASTER_CONFIG.items`, chưa chứng minh đọc registry/PG thật.
- Trình duyệt báo cảnh báo CSP chặn Google Fonts từ bên ngoài; đây là cảnh báo có sẵn của trang, không phải lỗi JS và không ảnh hưởng chức năng vòng này.

## File giao CW

- `master-list-data-region-manifest.csv`: chỉ 8 mã mới, UTF-8, mô tả không dùng ký tự mũi tên đặc biệt.
- `master-list-runtime-audit.json`: source/DOM union, 31 state, cache version và các kiểm chức năng.
- `master-list-data-region-handoff.md`: tài liệu này.
