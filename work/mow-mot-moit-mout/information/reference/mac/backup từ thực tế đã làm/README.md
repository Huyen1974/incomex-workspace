# Từ thực tế đã làm — hướng dẫn thư mục

- Bản làm việc: `từ thực tế đã làm.html`. Mở file này; khi di chuyển, giữ cùng thư mục `assets`.
- Ảnh: `assets/images/` — 16 file nguyên bytes, IMG-001 đến IMG-016; không nén, không gộp.
- Danh mục ảnh: `assets/image-manifest.json` — ID, đường dẫn tính từ HTML, MIME, SHA256, dung lượng, section/tiêu đề, alt, figcaption, URL nguồn và thứ tự.
- URL nguồn được lấy từ figure; nếu không có thì liệt kê các URL trong section dưới dạng ứng viên, không suy đoán nguồn chính xác.
- Bản trước khi tách: `backup/từ thực tế đã làm.before-extract-images.html` — chỉ để khôi phục, không phải bản làm việc.

## Trạng thái ngày 14/09/2026

- PASS: HTML 6.182.749 → 1.023.056 bytes; 16 ảnh base64 → 16 file; 17 thẻ img giữ nguyên (1 thẻ zoom-image vốn không có src, được JS gán khi mở ảnh).
- PASS: mọi src đã khai báo tồn tại; SHA256 từng file khớp bytes giải mã ban đầu; không còn ảnh base64 trong HTML làm việc.
- PASS: 16 ID duy nhất, đủ 16 entry manifest; không có ảnh trùng bytes.
- PASS: đảo ngược riêng src + data-image-id khôi phục chính xác toàn bộ bytes HTML gốc; vì vậy text, alt, figcaption, ID, anchor, URL, CSS/JS, button/dialog, thứ tự đều giữ nguyên.
- CHƯA KIỂM bằng browser: hiển thị ảnh, click phóng to, ma trận/JS và console. Công cụ browser từ chối file:// theo chính sách URL; không thực hiện cách vòng qua.
- Việc còn mở: Owner mở HTML tại chỗ, xem ảnh và bấm phóng to/đóng; thử các bộ lọc và ô ma trận; kiểm console.

## Danh mục ảnh

- `IMG-001` → `assets/images/IMG-001-man-hinh-nhin-cau-truc-he-thong-co-gi-nam-o-dau.png` — Ảnh Owner cung cấp: MOW tại T2, có đường dẫn chuỗi, thanh 7 tầng và sáu ô nhiệm vụ chứa các công việc.
- `IMG-002` → `assets/images/IMG-002-hai-chi-tiet-rieng-o-tang-2-vi-sao-can-ca-hai-anh.png` — Ký hiệu mặt cười và mặt cười cùng robot trên ô quy trình
- `IMG-003` → `assets/images/IMG-003-bieu-tuong-cua-quy-trinh-duoc-suy-tu-cac-task.png` — Ô Phỏng vấn hiện ba công việc và dòng màu xanh … +3 nữa
- `IMG-004` → `assets/images/IMG-004-bon-che-do-o-goc-phai-cung-mot-he-thong-nhung-nhin-theo-muc-dich-khac-nhau.png` — Ảnh Owner cung cấp: nhóm chế độ Thường, Đề xuất, Vận hành, Quản trị ở góc phải; phía dưới còn có công tắc Khuôn mẫu và Vận hành chưa bàn trong lượt này.
- `IMG-005` → `assets/images/IMG-005-de-xuat-them-moi-hoac-bao-cho-can-sua-ngay-tai-noi-dang-nhin.png` — Ảnh Owner cung cấp: ô Phỏng vấn có dấu cộng hai bên, bánh răng đề xuất cải tiến và ô vàng số 2 chỉ các đề xuất đang chờ xem xét.
- `IMG-006` → `assets/images/IMG-006-man-hinh-de-xuat-cai-tien-sua-thu-ngay-tren-ban-dang-nhin-chua-dung-vao-cau-truc-chin.png` — Màn hình đề xuất cải tiến ô Phỏng vấn: có sửa tên, xóa hàng, đổi thứ tự bằng vùng 6 chấm, thêm mục, Gửi đề xuất, Hủy và Đề xuất nâng cao
- `IMG-007` → `assets/images/IMG-007-cot-thu-hai-cua-moi-hang-ai-thuc-hien-task.png` — Vùng 6 chấm và biểu tượng mặt cười của task do con người thực hiện
- `IMG-008` → `assets/images/IMG-008-mat-cuoi-con-nguoi-lam.png` — Vùng 6 chấm và biểu tượng robot màu xanh của task tự động
- `IMG-009` → `assets/images/IMG-009-de-xuat-nang-cao-do-thoi-gian-ghi-lich-su-cai-tien-va-tao-du-lieu-quan-tri.png` — Màn hình Đề xuất nâng cao cho nhiệm vụ Phỏng vấn: có danh sách công việc, cột thời gian phút, thêm thời gian dự phòng phát sinh, cộng dồn thời gian, nhập tay, tổng thời gian, ý kiến khác và Gửi đề xuất
- `IMG-010` → `assets/images/IMG-010-mow-van-hanh-toi-dang-co-nhung-quy-trinh-nao-va-chung-dang-o-trang-thai-nao.png` — MOW chế độ Vận hành tại T2: các quy trình được hiển thị theo thẻ Kanban, có màu trạng thái, tiến độ, người phụ trách và mốc thời gian
- `IMG-011` → `assets/images/IMG-011-mow-quan-tri-admin-quan-ly-toan-bo-quy-trinh-va-biet-ngay-quy-trinh-nao-da-du-de-chay.png` — Ảnh Owner cung cấp: MOW Master Nháp 2, danh sách các quy trình đã đúc với bộ lọc theo cây 7 tầng, tình trạng vai trò và trạng thái.
- `IMG-012` → `assets/images/IMG-012-mot-ban-lam-viec-thoi-gian-thuc-cua-tung-nguoi.png` — MOT Dashboard: danh sách công việc của một người ở bên trái; công việc đang chọn ở giữa với phần việc phải làm, thông tin tham khảo và nút hoàn thành.
- `IMG-013` → `assets/images/IMG-013-7-t1-de-xuat-ban-chuan-hoa-de-mot-task-co-the-chay.png` — Màn hình T1 Đề xuất: bên trái là MOIT và MOUT; bên phải là bảng khai báo chi tiết dữ liệu và field; phía dưới là các nhóm cấu hình như Nguyên tắc giao việc, Ai làm và ai nhận, Chạy và kết thúc.
- `IMG-014` → `assets/images/IMG-014-7-3-phan-duoi-khung-config-chuan-cua-mot-task-so-nhom-khong-co-dinh.png` — Màn hình chi tiết config T1 với ba nhóm: Nguyên tắc giao việc; Ai làm và ai nhận; Chạy và kết thúc. Mỗi dòng có cột test, tình trạng và ghi chú.
- `IMG-015` → `assets/images/IMG-015-duyet-ntgv.png` — Duyệt NTGV — danh sách nguyên tắc giao việc chờ phê duyệt, có tìm kiếm, lọc vai và T7-T1, bảng NẾU/THÌ, trạng thái đề xuất và cột phê duyệt.
- `IMG-016` → `assets/images/IMG-016-7-4-1-mot-studio-chuan-hoa-cach-moit-va-mout-hien-ben-trong-mot-task.png` — MOT Studio: khung sắp xếp L1–L4 và các form nhúng chuẩn E01, E02 dùng để ghép field theo mẫu cố định.
