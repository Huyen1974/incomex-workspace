# RUN12 — Candidate xưng danh, chưa triển khai

Nguồn: runtime đọc ngày 29/10/2026; READY@4df2412a41bd977d13f89eb860e4f32fae5c8049. Xem P452/KQ tại COLLAB của task.

## Sản phẩm
- [candidate.patch.md](candidate.patch.md): diff đúng baseline; 8 file cũ được sửa, 1 adapter mới và 1 contract chung đóng gói byte-identical cho 3 nơi chạy (13 đường dẫn kể cả nguồn canonical). Không lấy số file làm mục tiêu.
- [tests.md](tests.md): toàn bộ fixture và kết quả 98 PASS, 0 FAIL, 0 SKIP; 1 cảnh báo Pydantic lifespan, không phải lỗi testcase.
- [manifest.json](manifest.json): SHA baseline/candidate/patch/từng file; image production và cách lùi. Candidate image chưa build; không phải bản release đã kiểm trên Linux.

Candidate snapshot Git cục bộ: `0ca9577fe7cf115f4501ffbcdb199fa211cb6c6d`; không phải commit upstream Agent Data/Claude đã push. Snapshot ở `/Users/nmhuyen/Documents/Codex/2026-10-25/x-l-cho-t-i/run12/upstream`. Baseline byte giữ tại `run12/baseline`. Diff/tests/manifest được lưu cùng task qua Gateway để không phụ thuộc chat.

## Hành vi và giới hạn bằng chứng
`declared_actor` tự khai; `authenticated_actor` lấy từ credential context server. Không cấp thêm quyền. Chặn trước staging/enqueue/idempotency; carry qua upload/job/helper; hash thao tác gắn cặp danh tính. Advertise là mặc định, chưa bật enforce. Không có parser `message` dự phòng.

Fixture chạy dispatcher và file/SQLite/journal thật trong thư mục tạm. Import chỉ thay mạng tải file bằng dữ liệu cố định; helper thay phần thực thi đặc quyền; fs_move/UI ghi file thật nhưng giả kết quả ghi sổ Git; restore kiểm gate và dispatch, không thay thế hồi phục Git production. Đã kiểm thiếu/null/rỗng/sai kiểu; không đổi file/state khi từ chối; cùng ID retry; đổi actor/credential; journal/job/upload legacy; đọc không đổi; unknown writer; helper UI/Git; reverse patch khôi phục mọi byte baseline. Chưa có HTTP end-to-end Linux, candidate image hoặc real-client C1. Không gọi fixture là FULL_PASS.

## Client/schema — C2 PARTIAL
| Bề mặt | Quan sát thực tế | Đường cập nhật / trạng thái |
|---|---|---|
| Codex local `agent-data` | Native `codex mcp list --json`: enabled, Streamable HTTP; config có env_http_headers; chưa có declared_actor trong schema phiên này | Cấu hình MCP host; Restart MCP/new session theo hãng, chưa chạy vì server chưa đổi |
| Hosted Incomex MCP full all 2 | Namespace tool đang có, schema cũ; tìm plugin không trả manifest; không có entry Incomex trong plugin config local | Chưa xác định direct custom hay published/managed; KHÔNG suy từ tên; CLIENT_REFRESH_PATH_UNVERIFIED |
| ChatGPT/Dot/Work/Live | Trang Plugins IAB hiển thị Log in; không có phiên quản lý đã xác thực | UI_SESSION_UNAVAILABLE; LIVE_NOT_TESTED; không tuyên bố toàn bộ client đã sẵn sàng |
| Claude Chat/CLI | Runtime FS pinned; chưa thử tools/list mới từ client thật | LIVE_NOT_TESTED; chưa gắn PASS cache/schema |

Tài liệu chính thức đã đọc: [custom MCP refresh](https://developers.openai.com/plugins/deploy/connect-chatgpt#refresh-metadata): deploy/restart server trước, Refresh rồi chat mới. Published plugin dùng continuous review, không mặc định cùng nút Refresh. [MCP local](https://learn.chatgpt.com/docs/extend/mcp): config trên Codex host, Restart và `/mcp`; không thay quản lý plugin cloud.

## Điểm dừng và tiếp tục
Blocker chuyển sang enforcement: chưa chứng minh đường cập nhật schema của các client đang ghi; runtime baseline không có canary enforcement actor/task để cô lập một client. Không tự thêm canary selector. Theo B2/B3, giữ production nguyên trạng và candidate đã làm; không advertise/enforce khi chưa chốt đường client-safe. Đây là dừng sau S1 có sản phẩm, không phải dừng S0 vì thiếu Refresh.

VPS-GHI chưa nhận vì chỉ đọc VPS và sửa snapshot Mac; cờ cuối vẫn trống. Không job/container/dịch vụ mới. Hai container/image và helper hash cuối khớp đầu lượt. Guard script tồn tại; Guard PRE/POST deployment không chạy và không mượn PASS cũ.

NEXT_TRIGGER: xác minh metadata của kết nối hosted đang dùng (direct custom hay published/managed) và đường nhận schema của các client ghi; tiếp tục từ candidate này. Nếu đủ điều kiện advertise, build trên đúng image baseline, hoàn thiện footprint apply, lấy VPS-GHI CAS + Guard PRE, deploy advertise-only, kiểm client cũ, refresh/new session đúng loại rồi C1 thực và C2 trước enforce. Không đề nghị Owner Refresh lúc này vì chưa có schema mới trên server. Không yêu cầu duyệt lại quyền đã cấp.
