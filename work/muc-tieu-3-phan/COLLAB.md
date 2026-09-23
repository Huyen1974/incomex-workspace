# COLLAB — muc-tieu-3-phan

Tên việc: Mục tiêu 3 phần
Host: Claude Chat · Host_ID: CLAUDE-MT3-260923-A
HTML chính: (chưa có)

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
Xác nhận User: ĐÃ XÁC NHẬN (nguyên văn lời User, 2026-09-23)

### 1. Mục tiêu
> Ở phần mục tiêu giờ hơi lộn xộn. Có thể các bạn hiểu ban đầu và cập nhật trong quá trình làm. Nhưng kết quả cuối cùng là nội dung vừa dài, vừa lộn xộn và đôi khi lại không thống nhất (không diễn đạt được hết các mong muốn của user.
>
> Tôi muốn việc này (mục tiêu) chia ra thành 3 phần:
>
> 1. Mục tiêu (ngắn gọn, chỉ đạo từ user viết thật ngắn) Cái này User sẽ rà soát thường xuyên.
> 2. Thế nào là hoàn thành? Cái này cũng rất ngắn. User chỉ đạo gõ vào cho khúc triết.
> 3. Các chi tiết cần đạt. Các bạn muốn ghi gì cũng được. AI hay ghi dài, các bạn tư đọc với nhau. Nhưng tôi muốn làm rõ mục 1 và 2 để làm kim chỉ nam. (Tất nhiên là những việc này có thể thay đổi. Tức là nếu 1 việc dài những gì đã xong rồi, thì có thể xóa đi cho ngắn. Chị để lại các mục tiêu sắp tới. Còn chi tiết AI tự ghi, tự đọc với nhau (nhưng Host kiểm soát)
>
> Cái này phải rõ ràng cấu trúc từ Gh chứ không chỉ UI ở phía VPS.

### 2. Thế nào là hoàn thành
- Mọi việc trong repo có §0 đúng ba phần; phần 1 và 2 ngắn và là lời Owner. *(đề xuất — chờ Owner gật)*
- Mở một việc trên web là thấy ngay phần 1 và 2; chi tiết và vòng cũ gập lại. *(đề xuất — chờ Owner gật)*
- AI mở việc mới là tự viết đúng khuôn này, không ai phải nhắc. *(đề xuất — chờ Owner gật)*

### 3. Chi tiết cần đạt (AI ghi, Host kiểm)
- Khuôn §0 chuẩn, tên mục con cố định để máy đọc được: `### 1. Mục tiêu` · `### 2. Thế nào là hoàn thành` · `### 3. Chi tiết cần đạt` · `### Vòng trước`. Dòng `Xác nhận User:` giữ nguyên ở đầu §0 (A9 không đổi).
- Sở hữu: phần 1–2 là lời Owner — AI không tự sửa chữ, chỉ được đề xuất và đánh dấu *(đề xuất — chờ Owner gật)*; phần 3 Host quản, được cắt gọn khi hạng mục đã XONG (giữ một dòng tóm tắt + mã commit); `### Vòng trước` giữ các khối A0 cũ, không xoá.
- Parser + view đọc đúng bốn mục; việc chưa chuẩn thì cảnh báo chứ không vỡ; tìm kiếm vẫn quét toàn bộ §0.
- Di trú toàn bộ việc hiện có (cả `done-tasks`) sang khuôn mới, không sửa chữ Owner, không xoá lịch sử.

## Trạng thái
- 2026-09-23 · Mở việc theo chỉ đạo Owner; Host Claude Chat; Executor dự kiến Codex/GPT Work. PROMPT `MT3-20260923-01` đã soạn.

## Owner cần quyết
- Phần 2 “Thế nào là hoàn thành” đang là đề xuất của Host — Owner gật hoặc gõ lại theo ý mình (không chặn RUN).
