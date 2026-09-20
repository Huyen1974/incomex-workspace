# COLLAB — hpml-view-for-user

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC

**Mục tiêu**
- Tạo một lớp mỏng để hiển thị các file HTML của từng công việc từ `incomex-workspace` lên khu vực view trên VPS; GitHub là SSOT của kế hoạch và file thuộc công việc.
- Tạo một nơi quản lý tập trung cho User: mỗi `work/<work-id>/` chỉ có **một view** đại diện, có thể quản lý số lượng hàng trăm hoặc nhiều hơn theo thời gian và tách được công việc đang làm với công việc đã hoàn tất.

**Nhiệm vụ/phạm vi User đã giao**
1. Thiết kế view trên KB tại `https://vps.incomexsaigoncorp.vn/knowledge/modules`.
2. Dùng vị trí hiện tại của nút **Modules** và đổi tên thành **Tasks now**.
3. Loại bỏ các nội dung/chức năng liên quan đến Modules khỏi khu vực này.
4. Dùng bố cục hai cột tương tự Knowledge: cột trái là danh sách công việc/tên file; cột phải là view HTML của công việc đang chọn.
5. Có công cụ tìm kiếm chuẩn cho khu vực quản lý task/view.
6. Kiến trúc phải giữ vai trò **lớp hiển thị mỏng**; không biến VPS/KB thành SSOT mới thay cho GitHub.

**Tiêu chí xong ở mức mục tiêu hiện tại**
- Mỗi công việc có đúng một view HTML có thể truy cập từ khu quản lý tập trung.
- View phản ánh file thuộc workspace/GitHub theo cơ chế được thiết kế, không tạo nguồn kế hoạch song song trên VPS.
- `Tasks now` hỗ trợ danh sách lớn, tìm kiếm và xem nội dung theo bố cục hai cột.
- Có cách quản lý/chuyển các công việc đã hoàn tất ra khỏi nhóm đang làm mà vẫn tra cứu được về sau.
- Phương án đủ rõ để hội đồng GPT · Claude · Hermes review trước khi giao Agent triển khai.

**Xác nhận User:** CHƯA XÁC NHẬN — chờ User xác nhận lại đúng mục tiêu/nhiệm vụ trên theo `AGENTS.md#A0_OBJECTIVE`.

## Trạng thái
- HVU00 · 2026-09-20 · Đã mở công việc và ghi nhận nguyên tắc/mục tiêu User.
- Chưa lập kế hoạch kỹ thuật, chưa tạo `PROMPT.md`, chưa RUN/triển khai production do đang ở cổng A0.

## Owner cần quyết
- Xác nhận hoặc sửa khối `0. MỤC TIÊU/NHIỆM VỤ USER` ở trên.
