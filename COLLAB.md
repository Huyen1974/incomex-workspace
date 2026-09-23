# COLLAB — Incomex Workspace · điều phối gốc

Host: GPT · Owner giao: 2026-09-20
Cấu trúc bắt buộc: root chỉ có `AGENTS.md`, `README.md`, `COLLAB.md`, `work/`.

## Handoff phiên mới · 2026-09-23
- **Nguồn chuẩn:** đọc `AGENTS.md` → root `COLLAB.md` → `COLLAB.md` của đúng việc. Không dựa vào lịch sử chat cũ nếu Git đã có trạng thái mới hơn. Tài liệu/workspace = GitHub SSOT; runtime = VPS SSOT.
- **Ưu tiên 1 · VPSC** — `work/vps-clean-20-9-26/` · Host Claude. Hiện `R4b` đã `OWNER_APPROVED + READY` với RUN_ID `VPSC-R4B-20260923-01`, PROMPT_SHA `fbb28bb85969ebdedf683e557ce134686fdbbde7`. Mục tiêu khép việc clean: dọn dấu SEC-01 còn lại sau khi xác nhận credential cũ chết; báo image hằng ngày chỉ-read; sửa failed services được nêu; đổi timezone VPS sang `Asia/Ho_Chi_Minh` nhưng giữ nguyên **thời điểm chạy thật** của lịch. NEXT: Owner RUN R4b → Codex V3 sau một đêm trigger thật → VPSC.6 theo dõi/đóng. Không mở lại audit nguyên nhân đĩa.
- **Ưu tiên 2 · GSM** — `work/gsm-access-audit/` · Host Claude. GSM-A1 **XONG** commit `0bdbe6b`: 167 access/30 ngày = 0 USD, 41 version ≈ 2,10 USD/tháng; không rỉ máu. Hai quyết định dọn version/Lark thuộc GSM, không chặn HJW.
- **Ưu tiên 3 · HJW** — `work/hermes-joint-workspace/` · Host GPT. Đang ở HJW.2A DESIGN; tiếp tục theo `COLLAB.md` của việc sau khi hai việc trên không còn chặn. Không tự suy từ chat cũ.
- **Quy ước Google:** không tạo thêm Google Cloud project/service. Project còn giữ là `github-chatgpt-ggcloud`; Google không phải runtime/SSOT. Drive chỉ là offsite backup; GSM là secret store cho tới khi có quyết định khác.
- **Cửa vào phiên mới:** `WS gốc · Host GPT · tiếp quản phiên 2026-09-23 · đọc AGENTS.md → COLLAB.md · làm theo mục Handoff phiên mới; trước khi thao tác một việc phải đọc COLLAB.md của việc đó.`

## Đang làm
- `work/gsm-access-audit/` · GSM · Host Claude · audit caller/tần suất + tồn kho version Google Secret Manager; PROMPT GSM-A1 chỉ đọc READY, chờ RUN cho Claude Code CLI.
- `work/mcp-token-argv/` · SECURITY · Host Claude · loại Bearer token khỏi argv của lark-crud-gateway/mcp-remote; migrate secret + rotate + smoke; không chặn HVU.
- `work/hermes-joint-workspace/` · HJW · Host GPT · HJW.2A + GSM + P07/P08 review đã xong. Host đã áp 7 sửa chặn READY + siết relay boundary; `PROMPT.md` HJW.2B FINAL, chờ READY@SHA → RUN.
- `work/vps-clean-20-9-26/` · VPSC · Claude mở việc: đĩa VPS 87% (trống 13GB, ~3 tuần chạm 95%) — PROMPT khảo sát chỉ đọc chờ GPT review; xoá thật chờ R03 CLOSED.
- `work/mow-mot-moit-mout/` · MMIM · file gốc đã import nguyên byte; chuẩn bị giao Codex gom tài liệu liên quan vào `information/`.
- `work/hpml-view-for-user/` · HVU-DEEPLINK01 · mở lại 23/09 để làm URL deep-link theo tab/section/step/detail; DRAFT/NO RUN, runtime VPS tách khỏi MMIM.
- `work/muc-tieu-3-phan/` · MT3 · Host Claude · chuẩn hoá §0 thành ba phần (Mục tiêu / Thế nào là hoàn thành / Chi tiết) trên GitHub + view; PROMPT `MT3-20260923-01`, Executor Codex.
- NEXT: HJW: GPT Host ghi READY theo commit cuối chạm PROMPT → truyền RUN `HJW-2B-20260923-01` cho Claude Code CLI.

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
- DROOT12 · 2026-09-22 · **VPS EVIDENCE ARCHIVE** (HVU-VPSARCHIVE01; A0 Owner nguyên văn 22/09, consensus P29–P32): hồ sơ VPS không-runtime của việc ở `/opt/incomex/work/<id>/` (Now) / `/opt/incomex/work/done-tasks/<id>/` (Done), sync tự đổi tên theo Git, không xoá; runtime/secret/đường cứu hộ hiện hành ở ngoài kho; `deploys` chỉ chuyển mục `ARCHIVE_SAFE` sau kiểm kê. Web mặc định chỉ Now + `Đã xong (N)` gập; link theo việc `/knowledge/modules?task=<id>`. Không tạo nguồn trạng thái mới (AGENTS A8).
- DROOT13 · 2026-09-23 · **JEV-AS-REFERENCE:** với quyết định hữu hạn (phân loại/chọn phương án/routing/scoring), Host/Reviewer ưu tiên gọi JEV Reference trên evidence thô trước khi chốt nếu JEV phù hợp; lưu result id/confidence. JEV không thay quyết định của Owner/hội đồng và không dùng thay source/runtime cho fact kỹ thuật quyết định được trực tiếp.

## Owner cần quyết
- —
