# PROMPT — HVU-DEEPLINK01 · DRAFT R2 FOR CLAUDE REVIEW · NO RUN

## 0. Trạng thái / gate
Đây là **yêu cầu bổ sung của task hiện có** `work/hpml-view-for-user/`. Không tạo task mới.

**Chưa giao Claude Code CLI.** Chỉ READY/RUN sau khi Claude Chat review lại R2 và GPT Host + Claude Chat đồng thuận, không còn P OPEN/OWNER liên quan.

## 1. Mục tiêu Owner — phạm vi chung
Làm URL của `https://vps.incomexsaigoncorp.vn/knowledge/modules` phản ánh đủ vị trí User đang xem để **chỉ cần gửi URL là người/AI mở được đúng chỗ**, tối thiểu:
- đúng task;
- đúng tab/view của Task html view;
- nếu đang ở nội dung công việc: đúng khu vực/bảng/mục con khi phần đó có định danh ổn định.

Đây là **năng lực chung của Task html view**, không phải chức năng riêng cho MOW/MOT/MMIM. MOW/MOT có thể dùng làm fixture kiểm thử nhưng **không được trở thành dependency, contract hay lý do sửa task khác**.

Giữ tương thích:
`?task=<task-id>`

Contract ưu tiên tối giản để Claude review:
`?task=<task-id>&view=control|content&at=<stable-id>`

Trong đó `at` chỉ là mã/ID ổn định của vị trí bên trong nội dung; không suy từ STT hoặc text hiển thị.

## 2. Hai chiều bắt buộc của mục tiêu
Phải phân biệt và đáp ứng cả hai:
1. **URL → UI:** mở URL đã chia sẻ thì phục hồi đúng task/view/vị trí.
2. **UI → URL:** khi User đổi task/view hoặc đi tới một khu vực/bảng/mục con mà hệ thống có thể nhận biết an toàn, URL phải cập nhật để nút Copy link/địa chỉ hiện tại thật sự chia sẻ được vị trí đó.

Không được coi việc “đã biết sẵn `at` rồi gắn hash để mở” là đủ nếu UI không có cách cập nhật `at` khi User đang điều hướng.

Nếu với HTML con hiện tại không có cơ chế chung để biết vị trí sâu mà không sửa tài liệu con, Claude phải ghi rõ **giới hạn kỹ thuật của V1** và đề xuất cách nhỏ nhất; không được lấy một file MMIM có `revealHash()` làm giả định cho mọi task.

## 3. Nguyên tắc làm nhỏ
- Ưu tiên frontend nhỏ nhất; tận dụng `URLSearchParams`, History API và fragment/hash chuẩn của trình duyệt khi đủ.
- `replaceState` được ưu tiên nếu không cần tạo lịch sử; không thêm `popstate` nếu không dùng `pushState`.
- Query phải được validate/normalize; dựng URL bằng API chuẩn, không nối chuỗi không kiểm soát.
- Không redesign UI.
- Không đổi database, MCP/connector, sync/presence/B2/B3.
- Không thêm message listener/postMessage/handshake nếu production không thật sự cần.
- Không nới sandbox/`allow-same-origin`.
- Deep-link không được tạo presence “Đang làm”.
- Không sửa MOW/MOT/MMIM trong RUN này.
- Không mở task phụ.

## 4. Acceptance
A1. `?task=<id>` cũ vẫn mở đúng task.
A2. `task + view` mở đúng tab/view.
A3. Khi có `at=<stable-id>` hợp lệ, mở đúng vị trí tương ứng; ID không tồn tại thì fallback an toàn.
A4. Đổi task/view trên UI làm URL cập nhật đúng.
A5. Với vị trí sâu mà viewer nhận biết được, UI cập nhật `at`; nếu production chưa có tín hiệu chung để nhận biết thì phải báo giới hạn, không giả PASS nhờ riêng MMIM.
A6. Copy link mở ở cửa sổ mới phục hồi đúng trạng thái mà URL đã mã hóa.
A7. Done task vẫn mở đúng qua deep-link, tự hiện đúng nhóm nếu cần.
A8. `view=content` nhưng không có tài liệu thì fallback về control/trạng thái hợp lệ.
A9. Query được làm sạch; không chèn HTML/script/path traversal.
A10. Không thêm message listener hoặc nới sandbox nếu không cần.
A11. Không làm đổi presence/“Đang làm”.
A12. Không regression Master list, search, Now/Done, detail, B2/B3.
A13. Nếu có nút **Copy link**, nó phải sao chép đúng URL hiện tại sau khi state đã đồng bộ.
A14. MOW/MOT/MMIM chỉ được dùng làm fixture kiểm thử; production solution phải không phụ thuộc chúng.

## 5. Yêu cầu Claude Chat review R2
Claude Chat **chỉ review, không RUN**:
1. Xác nhận R2 đã tách hẳn scope HVU khỏi MOW/MOT/MMIM chưa.
2. Xác nhận contract `task + view + at` có đủ cho năng lực chung không.
3. Kiểm tra riêng điểm **UI → URL**: production hiện có tín hiệu chung nào để xác định `at` khi User đi sâu trong iframe hay không; nếu không, ghi giới hạn và giải pháp tối thiểu thay vì dựa riêng vào MMIM.
4. ACCEPT hoặc CHANGE cụ thể và ghi vào `COLLAB.md`.

Chỉ sau ACCEPT/consensus mới chuyển READY cho Claude Code CLI.

Kết thúc R2: **NO RUN**.
