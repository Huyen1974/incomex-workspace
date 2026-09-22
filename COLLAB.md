# COLLAB — Incomex Workspace · điều phối gốc

Host: GPT · Owner giao: 2026-09-20
Cấu trúc bắt buộc: root chỉ có `AGENTS.md`, `README.md`, `COLLAB.md`, `work/`.

## Đang làm
- `work/hpml-view-for-user/` · HVU-VPSARCHIVE01 DESIGN · A0 Owner nguyên văn + P29 Claude/P30 GPT; web mặc định chỉ Now + kho hồ sơ VPS hai chiều; chờ Claude P31 consensus, chưa RUN.
- `work/gsm-access-audit/` · GSM · Host Claude · audit caller/tần suất + tồn kho version Google Secret Manager; PROMPT GSM-A1 chỉ đọc READY, chờ RUN cho Claude Code CLI.
- `work/mcp-token-argv/` · SECURITY · Host Claude · loại Bearer token khỏi argv của lark-crud-gateway/mcp-remote; migrate secret + rotate + smoke; không chặn HVU.
- `work/hermes-joint-workspace/` · HJW · Host GPT · A0 xác nhận lại 22/09: thêm Secret Boundary cho VPS/GSM + khai thác always-on/API/webhook/Telegram; hiện ở HJW.2A DESIGN, chưa RUN production.
- `work/vps-clean-20-9-26/` · VPSC · Claude mở việc: đĩa VPS 87% (trống 13GB, ~3 tuần chạm 95%) — PROMPT khảo sát chỉ đọc chờ GPT review; xoá thật chờ R03 CLOSED.
- `work/mow-mot-moit-mout/` · MMIM · file gốc đã import nguyên byte; chuẩn bị giao Codex gom tài liệu liên quan vào `information/`.
- NEXT: HJW.2A: GPT Host xử lý P03 (Claude đã phản biện 22/09; READY HJW.2B chờ thêm KQ GSM-A1); chỉ sau khi thiết kế đủ đồng thuận mới sang HJW.2B PROMPT/READY/RUN.

## Đã xong
- Archive: `work/done-tasks/` · vị trí folder là trạng thái Done (DROOT11); tìm/mở lại việc cũ trên Task html view bằng lệnh `Mở lại <id>`.

## Quyết định Owner
- DROOT01 · 2026-09-20 · Mọi công việc nằm dưới `work/<work-id>/`; không đặt prompt/test/evidence/archive của công việc ở root.
- DCLIENT01 · 2026-09-20 · Tài khoản ChatGPT Pro hiện tại không có Refresh app. Sau backend/schema cuối, GPT phải tạo MCP app mới từ đúng server hiện hữu, Scan Tools/so schema trước khi Owner connect tay; giữ app cũ làm rollback tới khi app mới PASS.
- DROOT02 · 2026-09-20 · Hội đồng AI gồm 3 thành viên: GPT · Claude · Hermes. Hermes vào qua kênh Agent Data và làm việc khi nối xong; được làm gì do lệnh điều hành. Chi tiết và việc sửa AGENTS A2/A4: `work/hermes-joint-workspace/`.
- DROOT03 · 2026-09-20 · **A0 mục tiêu User là cổng bắt buộc:** mỗi `work/<work-id>/COLLAB.md` phải đặt mục tiêu/nhiệm vụ User ở đầu; AI mở việc/soạn thảo phải xác nhận lại với User trước khi lập/thảo luận kế hoạch hoặc thực thi; mọi AI tham gia phải đọc mục này trước.
- DROOT04 · 2026-09-21 · **HOST INPUT GATE:** Host chịu trách nhiệm đủ đầu vào và phải đưa agent về đúng workspace/ref trước khi làm. Môi trường quen thuộc không cần PRECHECK riêng; có thể gộp gate chỉ đọc ở đầu RUN, nhưng agent chỉ được mutation sau khi đọc đúng AGENTS → COLLAB → PROMPT và kiểm các đầu vào cụ thể của việc. Không tạo thủ tục lặp lại cho năng lực môi trường đã nghiệm thu.
- DROOT05 · 2026-09-21 · **OWNER VIEW V1:** bỏ webhook/event-driven; dùng bản sao workspace chỉ-đọc cập nhật `git pull --ff-only` theo nhu cầu (nút Cập nhật hoặc mở trang khi index cũ >~10 phút). ~~`COLLAB.md` gốc có `Đang làm/Đã xong` làm dấu Now/Done.~~ (thay bởi DROOT11) Owner View được lấy HTML chính + asset cần hiển thị; file điều phối/phụ không public mặc định. MÃ/runtime vẫn tuyệt đối theo §11.
- DROOT06 · 2026-09-21 · **CAPABILITY-FIRST / ROLE-SEPARATE:** hạ tầng và connector đã setup/nghiệm thu là năng lực dùng chung cho mọi bề mặt thực sự bind được; không chia quyền kỹ thuật theo OpenAI/Claude. Vai trò Host/Reviewer/Agent gán riêng theo bề mặt cụ thể (GPT Chat/Work/Codex, Claude Chat/Cowork/Code CLI, Hermes…). Host phải ghi Executor_Surface + Write_Path, và giám sát kết quả qua SSOT/hạ tầng chung.
- DROOT07 · 2026-09-21 · **OWNER VIEW AUTO-DATA, thay DROOT05 về cadence:** UI03 đã có. Dữ liệu/tài liệu tự đồng bộ từ `main` bằng **GitHub webhook `push` (chuông báo) + backstop 15 phút** — cập nhật 21/09 theo 4 nguyên tắc Owner (tự động tối đa, không chạy vô ích, dùng cơ chế GitHub, rủi ro vừa đủ), thay kiểm 60 giây; HEAD không đổi thì thoát, HEAD đổi mới dựng snapshot. Task tự phát hiện từ `work/*/COLLAB.md`; ~~root `Đã xong` chỉ đánh dấu Done.~~ (thay bởi DROOT11) Publish nguyên tử + last-good; lỗi giữ bản tốt cuối và tự retry. Chỉ dữ liệu tự đổ; mã/app `view.html` vẫn triển khai có kiểm soát theo §11.
- DROOT08 · 2026-09-21 · **ACTOR SIGNAL PER TASK:** `Vừa làm` là surface có commit gateway thành công gần nhất chạm đúng task, không TTL và chỉ commit sau chạm cùng task mới thay; gateway đặt Git author name theo nhãn client server-side và giữ email gateway cố định, B2 đọc author của commit cuối riêng từng task. `Đang làm` là **latest-only presence thật theo task**, TTL 10 phút: tín hiệu mới thay ngay và vô hiệu tín hiệu cũ, mỗi task tối đa một actor đang làm; actor cũ không được sống lại khi actor mới clear/hết TTL. Commit chỉ clear nếu actor commit vẫn là latest; clear xong để trống tới activity mới.
- DROOT09 · 2026-09-21 · **R03 CLOSED + B3 CONTRACT FREEZE:** R03 đã nghiệm thu GPT/Claude/VPS/CROSS và CLOSED. B3 phải giữ nguyên tools/list, schema/hash, serverInfo/version, auth/URL và tool request/response/error semantics. **Ngoại lệ đã chốt:** Git author name là metadata attribution được gateway đặt theo nhãn client server-side, email gateway giữ nguyên; thay author không yêu cầu bump/reconnect vì client không cần rediscover contract.
- DROOT10 · 2026-09-21 · **DEPLOY HEALTH GATE:** service sau deploy có tối đa 5 phút STARTING; trong STARTING cấm MCP smoke/cấm rollback. Chỉ TỐT sau healthy ổn định + contract + live read/write PASS; chỉ HỎNG khi timeout/dead hoặc đã healthy mà acceptance fail. Rollback một lệnh duy nhất, không huỷ/chồng compose.
- DROOT11 · 2026-09-22 · **ARCHIVE FOLDER-STATE** (HVU-ARCHIVE01; A0 Owner xác nhận trực tiếp 22/09, consensus P23–P29): `work/<id>/` = Now, `work/done-tasks/<id>/` = Done; vị trí thư mục là nguồn trạng thái duy nhất, root không giữ danh sách Done. Đóng/Mở lại = Git move nguyên thư mục, giữ id + lịch sử; hai lệnh chuẩn `Đóng <id>` / `Mở lại <id>` theo AGENTS A9. Owner View tìm xuyên Now + Done theo id + tên + toàn bộ A0; URL tài liệu key theo task-id.

## Owner cần quyết
- —
