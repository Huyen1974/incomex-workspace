# COLLAB — Hermes Joint Workspace

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
- Mục tiêu (mở rộng 2026-09-21 và 22/09 theo chỉ đạo Owner): Hermes là thành viên hội đồng cùng GPT và Claude, **chạy API 24/7 trên VPS**. Không chỉ “vào được workspace” như hai thành viên ban đầu, Hermes phải phát huy lợi thế always-on: tự thức đúng lúc, nhận trigger máy-máy, gọi API/webhook/scheduler, theo dõi việc dài hạn, retry có kiểm soát và chủ động nhắn Telegram cho Owner — để các vòng việc có thể khép kín mà Owner không phải trực máy.
- Nhiệm vụ/phạm vi: (1) nối Hermes qua Agent Data đang có, không mở đường ghi Git thứ ba, không đưa tài khoản GitHub Owner lên VPS, không cấp sudo rộng; (2) tái dùng GitHub webhook + backstop đang chạy nhưng chỉ wake theo assignment máy đọc hợp lệ; (3) **thiết kế đầy đủ lớp automation/orchestration của Hermes trước khi triển khai**, xác định trigger → quyết định → hành động → retry/dedup → báo Owner/handoff; (4) **thiết kế secret boundary riêng cho bề mặt VPS**: không mặc định cho Hermes/VPS quyền truy cập trực tiếp rộng vào Google Secret Manager (GSM). Phải đọc kết quả `work/gsm-access-audit/`, xác định threat model và tối thiểu hoá credential/quyền GSM/secret material tồn tại trên VPS; ưu tiên chỉ đưa đúng bí mật tối thiểu cho đúng process/thời điểm thay vì cho agent khả năng duyệt/đọc kho secret. Giải pháp cụ thể do hội đồng review rồi mới chốt.
- Tiêu chí xong: T1–T8 hiện có + **T9 Secret boundary** (Hermes không giữ quyền GSM rộng/không cần thiết; đường cấp secret, rotation, failure/compromise đã được review và test) + **T10 Automation value** (ít nhất các đường webhook/assignment, scheduled/backstop, API action và Telegram notification/handoff được thiết kế, chống trùng, có retry/cost/observability và nghiệm thu thật theo scope đã chốt). Sau đó mới cập nhật luật gốc hội đồng 3 thành viên.
- Xác nhận User: **ĐÃ XÁC NHẬN — Owner 22/09/2026**: ngoài mục tiêu Hermes chạy API khép kín vòng, HJW phải (a) hạn chế rủi ro secret do Hermes sống trên VPS và không mặc định truy cập GSM trực tiếp; (b) khai thác đầy đủ thế mạnh always-on/API/webhook/Telegram của Hermes, thiết kế xong trước rồi mới triển khai.

Hội đồng: GPT · Claude · Hermes (Owner quyết 2026-09-20, ghi ở COLLAB gốc DROOT02). Trước mắt làm việc: GPT + Claude; Hermes vào khi HJW.3 PASS.
Host: GPT Chat · Host_ID: GPT-HJW-260922-A · Owner chuyển Host 2026-09-22
HTML chính: `view.html`

## Dòng hiện hành
HJW | Hermes thành viên hội đồng chạy API, khép kín vòng | việc 2/5 | A0 ĐÃ XÁC NHẬN | NEXT: Claude phản biện P02 → GPT Host chốt PROMPT HJW.2 | BLOCK: —

## Quyết định Owner
- D01 · 2026-09-20 · Mục tiêu: Hermes tham gia workspace đầy đủ như một thành viên. Được làm gì hay không là do lệnh điều hành, như GPT/Claude; không dựng rào kỹ thuật riêng cho Hermes.
- D02 · 2026-09-20 · Hội đồng gồm 3 thành viên: GPT · Claude · Hermes.
- D03 · 2026-09-20 · Kênh: Agent Data (`workspace_*`, cùng cửa Claude Code đang dùng) vì Hermes nằm trên VPS. Không đưa tài khoản GitHub của Owner lên VPS; không mở cửa ghi thứ ba (giữ D12).
- D04 · 2026-09-20 · Cách làm: tham gia · an toàn · tận dụng tối đa cái đang có · hạn chế xây mới · nhanh nhất, không sa đà.
- D05 · 2026-09-21 · Owner xác nhận mục tiêu mở rộng: Hermes chạy API 24/7 để khép kín vòng, nhưng **tự động phải tiết kiệm**. GitHub push/webhook không được mặc định đánh thức LLM Hermes cho mọi thay đổi; phải có bộ lọc deterministic trước, chỉ wake Hermes khi tín hiệu/assignment máy đọc xác định việc tới lượt Hermes. Backstop dùng cùng logic chống trùng.
- D06 · 2026-09-21 · Tách việc dứt điểm: JEV.B1 OpenAI hoàn tất + nghiệm thu trước; sau đó `work/hermes-joint-workspace/` mới RUN riêng. Không một RUN/PROMPT gộp hai task.
- D07 · 2026-09-22 · Owner chuyển Host của HJW sang **GPT Chat**; Host_ID hiện hành `GPT-HJW-260922-A`. Việc chuyển Host không đổi A0, D01–D06 hay phạm vi kỹ thuật đã chốt.
- D08 · 2026-09-22 · **SECRET BOUNDARY:** do Hermes chạy thường trực trên VPS, HJW phải coi VPS là trust zone thấp hơn control plane chứa secret. Không mặc định cấp cho Hermes/VPS quyền GSM trực tiếp/rộng. Hội đồng phải dựa trên `work/gsm-access-audit/` để chọn cơ chế cấp bí mật tối thiểu, rotation/revoke rõ và xác định chính xác rủi ro còn lại trước implementation.
- D09 · 2026-09-22 · **ALWAYS-ON VALUE:** mục tiêu đưa Hermes vào hội đồng là tận dụng khác biệt 24/7 + API/webhook/scheduler + Telegram, không chỉ đạt parity đọc/ghi với GPT/Claude. Phải hoàn tất thiết kế automation/orchestration và ma trận use-case trước khi phát RUN cấu hình production.

## Kế hoạch
- HJW.1 | Mở việc + nhận ý kiến GPT (P01) | ✓ 21/09
- **HJW.2A — DESIGN / NO PRODUCTION MUTATION** | Hội đồng thiết kế đầy đủ trước khi code/config: **(a)** ma trận năng lực Hermes khác GPT/Claude: always-on, inbound webhook, scheduler/backstop, outbound API, long-running watch/retry, Telegram notify/command, handoff; **(b)** assignment lifecycle máy đọc: create/claim/run/block/done + idempotency/dedup/retry/rate-limit/cost/observability; **(c)** secret threat model trên VPS: secret nào Hermes thật sự cần, cái gì không được đưa lên VPS, quyền GSM nào phải loại, rotation/revoke/failure mode; bắt buộc dùng evidence từ `work/gsm-access-audit/`; **(d)** ranh giới tự động hoá: việc nào Hermes tự xử lý, việc nào chỉ báo/đẩy assignment cho GPT/Claude/Owner; không giả định có đường wake GPT/Claude nếu chưa được nghiệm thu; **(e)** xác định phần nào chỉ cần assembly/config hiện hữu và phần nào thật sự cần thay đổi. GPT Host tổng hợp, Claude phản biện ít nhất một vòng. | ▶ hiện hành
- **HJW.2B — IMPLEMENT** | Chỉ sau HJW.2A đồng thuận: một PROMPT mục tiêu mở cho Claude Code CLI để cấu hình Hermes dùng `workspace_*` qua relay nội bộ, nạp luật, cắm JEV, assignment wake + webhook/backstop, Telegram và secret path đã được duyệt. Không mở đường ghi thứ ba; không dựng framework mới nếu capability hiện hữu đủ. | □ sau HJW.2A
- HJW.3 | Nghiệm thu **T1–T10** bằng chạy thật; ngoài R03/stale-write/cross-client còn phải test wake đúng/không wake thừa, blocker vượt quyền, Telegram, retry/dedup và secret boundary/rotation theo thiết kế. | □
- HJW.4 | Sau PASS mới ghi luật gốc/phần hiển thị thật sự cần cho hội đồng 3 thành viên + `[Hermes]`; không tự đổi Founders nếu Owner chưa quyết. | □
- HJW.5 | Đóng: Host đối chiếu T1–T10; xin Owner một chữ trước khi dọn fixture nếu có. | □

## Câu hỏi hội đồng
- Q01 · Hermes gọi Agent Data qua relay nội bộ `127.0.0.1:6533` hay URL công khai? Đề xuất Host: relay nội bộ (không ra internet, có sẵn); relay hỏng mới dùng URL công khai.
- Q02 · Hội đồng 3 thành viên có đổi READY thành 3 chìa không? Đề xuất Host: giữ 2 chìa (thành viên không sửa cuối ghi REVIEWED + Host ghi READY) để không chậm.
- Q03 · Có tách khoá Agent Data riêng cho Hermes không? Đề xuất Host: đưa lại vào HJW.2A dưới threat model mới D08; không mặc định dùng chung chỉ vì trước đây D04 ưu tiên làm nhanh.
- Q04 · **GSM/secret boundary:** Hermes thực sự cần những secret nào? Có thể loại hoàn toàn quyền GSM khỏi process Hermes không? Nếu vẫn phải lấy secret từ GSM, boundary nào chỉ cho phép materialize đúng secret/đúng thời điểm mà không trao quyền duyệt/đọc rộng? Rotation/revoke và sự cố VPS bị chiếm quyền xử lý thế nào? Hội đồng phải đối chiếu kết quả GSM audit trước khi kết luận.
- Q05 · **Automation portfolio:** những việc nào nên mặc định giao Hermes vì lợi thế 24/7 (webhook, scheduled check, condition/watch, API workflow, retry, Telegram), và việc nào vẫn nên để GPT/Claude vì cần tương tác/đánh giá sâu? Cần ma trận use-case → trigger → action → owner → cost/risk.
- Q06 · **Handoff/dispatch:** khi Hermes phát hiện việc cần GPT/Claude nhưng hai bề mặt không always-on, tín hiệu chuẩn là gì? Trước mắt phải dùng SSOT assignment + Telegram/Owner nếu chưa có wake path đã nghiệm thu; không được giả định khả năng gọi trực tiếp ứng dụng thuê bao.

## Ý kiến đang mở
- P01 · GPT Chat (prompt soạn trong chat, Owner chuyển 21/09) · **PARTIAL** — Host nhận: Agent Data trước, không deploy key trực tiếp, T7/T8, skill mỏng, không sudo rộng, không sửa backend khi R03 đóng băng, Q01 = relay nội bộ. Không nhận: soạn ngoài repo; gộp chung một prompt với JEV; T7 đánh thức Hermes mỗi lần push rồi mới tự NO-OP (đốt token vô ích — thay bằng lọc tất định ở HJW.2c). Lý do chi tiết: `work/jev-integration/COLLAB.md` P08.
- P02 · GPT Chat · Host `GPT-HJW-260922-A` · Based_on `ea1df3e402221628d56225e145a91bb4b2e82959` · Scope: HJW.2–HJW.4 · **OPEN — chờ Claude phản biện một vòng**. Đề nghị chốt theo 5 nguyên tắc: **(1)** Hermes là thành viên vận hành đầy đủ: tùy phân công có thể làm Host/Reviewer/Agent như mọi surface khác; không dựng hạn chế kỹ thuật riêng. **(2)** Giữ Assembly First: chỉ cấu hình Hermes dùng `workspace_*` qua relay nội bộ + JEV + webhook/backstop đang có; không thêm server/framework/đường ghi. **(3)** Bỏ trigger heuristic “COLLAB có dòng gọi tên Hermes”; thay bằng **assignment marker máy đọc rõ ràng** gồm tối thiểu `assignment_id/work-id · surface=Hermes · role · scope · state`, webhook/backstop chỉ wake khi marker mới/chưa xử lý; chống trùng theo assignment + HEAD. Câu chữ/format chính xác để Agent đề xuất theo hệ thống hiện hữu, không hardcode thêm nếu A9/Task Control đã có trường tương đương. **(4)** Hermes trước khi mutation phải qua cùng A0 + HOST INPUT GATE + AGENTS→COLLAB→PROMPT/READY/RUN như surface khác; vượt quyền thì STOP, ghi blocker, Telegram Owner; không tự mở scope. **(5)** Nghiệm thu phải chứng minh cả tự thức T7, blocker T8 và attribution Hermes đủ để Owner View phân biệt `Vừa làm/Đang làm`; sau PASS mới cập nhật AGENTS/A9/A4 nếu thật sự cần. `Founders = GPT Chat + Claude Chat` hiện là governance riêng; không tự đổi chỉ vì Hermes là thành viên hội đồng, trừ khi Owner quyết rõ.

## Owner cần quyết
- — Chưa có.

## NEXT
- A0 **đã mở rộng và Owner xác nhận lại 22/09** với D08 Secret Boundary + D09 Always-on Value; JEV DONE; R03 CLOSED.
- **GPT Chat là Host hiện hành. Chưa RUN production.** HJW chuyển sang **HJW.2A DESIGN** trước, chưa soạn prompt implementation.
- Claude Chat phản biện P02 + D08/D09 + Q04–Q06 đúng một vòng theo A5/Planning Guide; đồng thời phải đọc kết quả `work/gsm-access-audit/` khi có để không thiết kế secret path bằng giả định. Sau khi HJW.2A đủ đồng thuận, GPT Host mới chốt `PROMPT.md` HJW.2B, READY rồi mới RUN.
