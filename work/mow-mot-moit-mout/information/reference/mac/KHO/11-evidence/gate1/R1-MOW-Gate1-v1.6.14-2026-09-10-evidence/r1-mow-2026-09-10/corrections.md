# Lỗi thao tác/giới hạn thu evidence

- Python local chưa có issuer CA phù hợp, HTTPS source capture thất bại. Dùng system curl giữ nguyên certificate verification; không dùng insecure/TLS bypass. Browser HTTPS đã mở bình thường.
- Bản đầu của harness liệt kê 54 script URL nhưng chưa bỏ HTML comment và chưa dùng `<base href>` của New MODT, gây 8 false 404. Đã sửa resolver: danh sách hợp lệ cuối có 47 URL, đều HTTP 200/TLS verify 0. `asset-capture.json` là kết quả đã sửa; các 404 do harness không được dùng làm finding ứng dụng. `/w/wf-0001` là một 404 khác, quan sát trực tiếp trong browser.
- Mở New MODT lần đầu timeout 10 giây ở công cụ nhưng tab đã tạo. Chọn lại chính tab đó đọc được trang bình thường; không coi timeout này là route failure.
- Kiểm bản SSOT tạm phát hiện thao tác thay ô cuối có thể nuốt các cột trước, và bản nháp D03 dùng 6 ô trong bảng gốc 4 ô. Đã sửa ở bản tạm, thêm kiểm số ô và bảo toàn toàn bộ các cột source/Fit của Capability Matrix cùng tên/URL U02–U04. Chưa ghi file SSOT chính khi phát hiện/sửa hai lỗi này; receipt cuối ghi đúng một lần ghi.
- Một số file AX `*-detail.txt` chỉ là phần thay đổi AX do browser cache. Dùng PNG và bản `*-dom.txt` khi có để đọc trạng thái đầy đủ, cùng source đã lưu; không diễn giải AX delta là toàn bộ trang.
