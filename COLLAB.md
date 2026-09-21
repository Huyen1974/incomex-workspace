# COLLAB — Incomex Workspace · điều phối gốc

Host: GPT · Owner giao: 2026-09-20
Cấu trúc bắt buộc: root chỉ có `AGENTS.md`, `README.md`, `COLLAB.md`, `work/`.

## Đang làm
- `work/hpml-view-for-user/` · HVU-B3 · B2/B2.1 PASS; P14–P15 ACCEPTED. B3 chốt semantics per-task: `Vừa làm` = Git author gateway bền tới commit kế tiếp cùng task; `Đang làm` = gateway presence TTL 10′. PROMPT B3 đã soạn, chờ READY.
- `work/mcp-workspace/` · R03 · chốt MCP Git + VPS để quay lại công việc nghiệp vụ.
- `work/jev-integration/` · PLAN-V01 · mở việc, đang lấy ý kiến hội đồng; chưa RUN triển khai.
- `work/hermes-joint-workspace/` · HJW · Claude mở việc, chờ GPT review; nối Hermes khi R03 CLOSED.
- `work/vps-clean-20-9-26/` · VPSC · Claude mở việc: đĩa VPS 87% (trống 13GB, ~3 tuần chạm 95%) — PROMPT khảo sát chỉ đọc chờ GPT review; xoá thật chờ R03 CLOSED.
- `work/mow-mot-moit-mout/` · MMIM · file gốc đã import nguyên byte; chuẩn bị giao Codex gom tài liệu liên quan vào `information/`.
- NEXT: R03 backend đã MACHINE_DONE/frozen. Tạo đúng MỘT MCP app GPT mới từ Full All hiện hữu → Scan theo cổng `work/mcp-workspace/COLLAB.md` → Owner Connect tay → reconnect Claude/open phiên mới → bài 9 bước × 4 surface + VPS/CROSS → CLOSED.

## Đã xong
- —

## Quyết định Owner
- DROOT01 · 2026-09-20 · Mọi công việc nằm dưới `work/<work-id>/`; không đặt prompt/test/evidence/archive của công việc ở root.
- DCLIENT01 · 2026-09-20 · Tài khoản ChatGPT Pro hiện tại không có Refresh app. Sau backend/schema cuối, GPT phải tạo MCP app mới từ đúng server hiện hữu, Scan Tools/so schema trước khi Owner connect tay; giữ app cũ làm rollback tới khi app mới PASS.
- DROOT02 · 2026-09-20 · Hội đồng AI gồm 3 thành viên: GPT · Claude · Hermes. Hermes vào qua kênh Agent Data và làm việc khi nối xong; được làm gì do lệnh điều hành. Chi tiết và việc sửa AGENTS A2/A4: `work/hermes-joint-workspace/`.
- DROOT03 · 2026-09-20 · **A0 mục tiêu User là cổng bắt buộc:** mỗi `work/<work-id>/COLLAB.md` phải đặt mục tiêu/nhiệm vụ User ở đầu; AI mở việc/soạn thảo phải xác nhận lại với User trước khi lập/thảo luận kế hoạch hoặc thực thi; mọi AI tham gia phải đọc mục này trước.
- DROOT04 · 2026-09-21 · **HOST INPUT GATE:** Host chịu trách nhiệm đủ đầu vào và phải đưa agent về đúng workspace/ref trước khi làm. Môi trường quen thuộc không cần PRECHECK riêng; có thể gộp gate chỉ đọc ở đầu RUN, nhưng agent chỉ được mutation sau khi đọc đúng AGENTS → COLLAB → PROMPT và kiểm các đầu vào cụ thể của việc. Không tạo thủ tục lặp lại cho năng lực môi trường đã nghiệm thu.
- DROOT05 · 2026-09-21 · **OWNER VIEW V1:** bỏ webhook/event-driven; dùng bản sao workspace chỉ-đọc cập nhật `git pull --ff-only` theo nhu cầu (nút Cập nhật hoặc mở trang khi index cũ >~10 phút). `COLLAB.md` gốc có `Đang làm/Đã xong` làm dấu Now/Done. Owner View được lấy HTML chính + asset cần hiển thị; file điều phối/phụ không public mặc định. MÃ/runtime vẫn tuyệt đối theo §11.
- DROOT06 · 2026-09-21 · **CAPABILITY-FIRST / ROLE-SEPARATE:** hạ tầng và connector đã setup/nghiệm thu là năng lực dùng chung cho mọi bề mặt thực sự bind được; không chia quyền kỹ thuật theo OpenAI/Claude. Vai trò Host/Reviewer/Agent gán riêng theo bề mặt cụ thể (GPT Chat/Work/Codex, Claude Chat/Cowork/Code CLI, Hermes…). Host phải ghi Executor_Surface + Write_Path, và giám sát kết quả qua SSOT/hạ tầng chung.
- DROOT07 · 2026-09-21 · **OWNER VIEW AUTO-DATA, thay DROOT05 về cadence:** UI03 đã có. Dữ liệu/tài liệu tự đồng bộ từ `main` bằng **GitHub webhook `push` (chuông báo) + backstop 15 phút** — cập nhật 21/09 theo 4 nguyên tắc Owner (tự động tối đa, không chạy vô ích, dùng cơ chế GitHub, rủi ro vừa đủ), thay kiểm 60 giây; HEAD không đổi thì thoát, HEAD đổi mới dựng snapshot. Task tự phát hiện từ `work/*/COLLAB.md`; root `Đã xong` chỉ đánh dấu Done. Publish nguyên tử + last-good; lỗi giữ bản tốt cuối và tự retry. Chỉ dữ liệu tự đổ; mã/app `view.html` vẫn triển khai có kiểm soát theo §11.
- DROOT08 · 2026-09-21 · **ACTOR SIGNAL PER TASK:** `Vừa làm` là author/surface của commit gateway thành công gần nhất chạm đúng task, không TTL và chỉ commit sau chạm cùng task mới thay; `Đang làm` là presence gateway theo `surface × task`, TTL 10 phút, không đi qua Git. Commit thành công clear presence của chính surface/task; task khác không ảnh hưởng. UI phải ghi chú nghĩa hai tín hiệu và không suy từ Git author chung/prefix tự do.

## Owner cần quyết
- —
