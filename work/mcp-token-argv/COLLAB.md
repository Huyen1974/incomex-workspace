# COLLAB — mcp-token-argv

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
Xác nhận User: **ĐÃ XÁC NHẬN** — Owner 22/09/2026 yêu cầu Host Claude xử lý nốt các lỗ còn lại sau HVU và đóng vấn đề.

### 1. Mục tiêu
- Mục tiêu: loại Bearer token ra khỏi command-line argv của wrapper `lark-crud-gateway` / `mcp-remote` trên Mac, đưa secret về env/secret store phù hợp và giữ dịch vụ hoạt động bình thường.
*(đề xuất — chờ Owner gật; giữ nguyên câu chữ §0 cũ)*

### 2. Thế nào là hoàn thành
- Bearer token không còn hiện trong argv; wrapper vẫn hoạt động và credential cũ được xử lý an toàn. *(đề xuất — chờ Owner gật)*

### 3. Chi tiết cần đạt (AI ghi, Host kiểm)
- Giữ nguyên phạm vi, tiêu chí và chỉ đạo chi tiết tại Vòng trước; Host rà soát, cập nhật phần này khi triển khai.

### Vòng trước
- Mục tiêu: loại Bearer token ra khỏi command-line argv của wrapper `lark-crud-gateway` / `mcp-remote` trên Mac, đưa secret về env/secret store phù hợp và giữ dịch vụ hoạt động bình thường.
- Nhiệm vụ/phạm vi: Host Claude khảo sát đúng launch path/config/process đang dùng; tuyệt đối không in token vào repo/chat/log; tạo rollback; chuyển secret khỏi argv; sau khi đường mới hoạt động thì rotate credential cũ nếu quyền hiện có cho phép; restart tối thiểu đúng wrapper/process liên quan; kiểm lại chức năng.
- Tiêu chí xong: `ps`/process argv không còn lộ Bearer token; token không nằm trong file/log/history public; credential cũ đã được rotate/revoke hoặc có lý do + một action Owner tối thiểu nếu bắt buộc; lark-crud-gateway/mcp-remote smoke PASS; rollback được ghi rõ.
- Xác nhận User: **ĐÃ XÁC NHẬN** — Owner 22/09/2026 yêu cầu Host Claude xử lý nốt các lỗ còn lại sau HVU và đóng vấn đề.

Host: Claude Chat
Executor_Surface dự kiến: Claude Code CLI/Cowork
Nguồn phát hiện: RUN `HVU-B3-CLEANUP-20260921-03` — chỉ ghi nhận hiện tượng token xuất hiện trong argv; **không chép giá trị token**.

## Trạng thái
OPEN · security follow-up độc lập; không chặn đóng `work/hpml-view-for-user/`.

## Nguyên tắc bắt buộc
- Không đọc/echo/copy secret vào báo cáo nếu không cần; chỉ xác nhận presence/absence.
- Không đổi rộng MCP schema/version/auth khác ngoài wrapper/token này.
- Không restart ChatGPT/Claude connector khác nếu không cần.
- Nếu rotate cần thao tác Owner trên UI mà Host không làm được, gom thành đúng một action ngắn sau khi đã hoàn tất mọi bước máy có thể làm.

## Owner cần quyết
- —
