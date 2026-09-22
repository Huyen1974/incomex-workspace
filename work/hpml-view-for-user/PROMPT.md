# PROMPT — HVU.ARCHIVE01 · DRAFT thiết kế work/done-tasks

STATUS: DRAFT · CHỈ THẢO LUẬN/ĐỒNG THUẬN · KHÔNG RUN PRODUCTION
RUN_ID: HVU-ARCHIVE01-DESIGN-20260922-01
Host: GPT Chat
Reviewer: Claude Chat
Executor_Surface: — · chỉ chốt sau đồng thuận

## 0. Mục tiêu Owner đã xác nhận
Tạo một mô hình duy nhất để AI và con người nhìn là hiểu ngay:
- `work/<task-id>/` = **Đang làm**.
- `work/done-tasks/<task-id>/` = **Đã xong**.
- GitHub/workspace là SSOT; VPS clone/mirror phải phản ánh cùng cấu trúc.
- Web phải tìm/xem được **cả việc đang làm và việc đã xong**, để có thể tra cứu, sửa, nâng cấp lại.
- User không phải nhớ bước phụ: “đóng việc” → AI move task vào `done-tasks`; “mở lại” → AI move task ra lại `work/<task-id>`.

B2/B2.1/B3 hiện hành đã PASS; pha này là bổ sung archive, không redesign actor/presence.

## 1. Đề xuất kiến trúc tối giản để Claude phản biện
### 1.1 Một trạng thái duy nhất = vị trí folder
- Active discovery: đúng `work/*/COLLAB.md`, loại reserved `work/done-tasks/`.
- Done discovery: đúng `work/done-tasks/*/COLLAB.md`.
- Không dùng recursive `work/**/COLLAB.md` để tránh bắt nhầm thư mục phụ.
- Sau khi rollout, root `## Đã xong` không còn là nguồn trạng thái task; có thể giữ ghi chú lịch sử/quyết định nhưng không phải maintain danh sách hàng trăm task.

### 1.2 GitHub ↔ VPS
- Bản clone chỉ-đọc/sync source trên VPS theo Git nên tự có đúng path `work/` và `work/done-tasks/` sau webhook/fetch; **không chạy một lệnh move VPS riêng**.
- B2 snapshot đọc cả hai nguồn và xuất cùng một `tasks.json` với `bucket=Now|Done` lấy từ source path.
- Web có hai nhóm/filter `Đang làm` / `Đã xong`, ô search tìm xuyên cả hai.
- Task Done vẫn xem được mục tiêu/lịch sử/HTML/tài liệu. Để giảm break link, public document/cache có thể tiếp tục key theo `task-id` dù source path nằm trong `done-tasks`; Claude kiểm xem đây có phải phương án ít sửa nhất.

### 1.3 Đóng / mở lại
**Đóng việc:** trong thao tác kết thúc bình thường, AI ghi KQ/CLOSED cần thiết rồi Git move nguyên folder:
`work/A/` → `work/done-tasks/A/`.
Webhook tự publish → A chuyển nhóm Done trên web.

**Mở lại:** Git move:
`work/done-tasks/A/` → `work/A/`.
Giữ nguyên `task-id=A` và Git history. Host phải đọc lại A0/trạng thái; READY/RUN lịch sử không được tự dùng làm giấy phép mới. Khi cần RUN mới phải phát READY mới theo prompt hiện hành.

### 1.4 B3 / signal
- `done-tasks` là **reserved container**, không phải task-id.
- Mọi path dưới `work/done-tasks/` không tạo `Đang làm` cho archive và không được parse thành task `done-tasks`.
- Khi task được reopen về `work/<id>/`, signal hoạt động lại bình thường.
- Done task có thể tiếp tục hiển thị `Vừa làm` lịch sử từ commit Git nếu hữu ích; `Đang làm` phải trống.

## 2. Migration dự kiến sau đồng thuận
Không làm trong lượt review này.
Sau khi Claude đồng thuận và Host chốt PROMPT triển khai:
1. tạo `work/done-tasks/`;
2. sửa B2 discovery/mapping + UI bucket/search;
3. thêm guard B3 reserved path;
4. regression webhook/retention/actor/presence;
5. move các task đã CLOSED hiện có (trước mắt `hpml-view-for-user`, `mcp-workspace`) vào archive;
6. kiểm VPS/web vẫn tìm và mở được chúng.

## 3. Những gì KHÔNG làm
- Không database/task manager mới.
- Không scheduler/archive service mới nếu AI có thể move trong commit đóng việc.
- Không duplicate trạng thái Now/Done ở nhiều nơi.
- Không đổi MCP schema/version/auth.
- Không xóa lịch sử Git.
- Không move production trong lượt DESIGN này.

## 4. Claude cần phản biện
Claude Chat đọc thực địa hiện hành và ghi P24 vào COLLAB:
1. ACCEPT/CHANGE kiến trúc trên.
2. Xác nhận B2 hiện chỉ scan một tầng và thay đổi tối thiểu để đọc thêm `done-tasks/*`.
3. Kiểm tác động tới document path/cache/retention/search và đề xuất cách ít sửa nhất mà link ổn định.
4. Kiểm B3 guard reserved `done-tasks`: mọi đường tool/path nào cần tránh parse nhầm.
5. Kiểm quy tắc root `Đã xong` có thể bỏ vai trò state source sau migration mà không phá A9/parser.
6. Chỉ ra blocker thật nếu có. Nếu không có, đề nghị Host soạn PROMPT RUN.

Không mutation runtime ở lượt Claude review.
