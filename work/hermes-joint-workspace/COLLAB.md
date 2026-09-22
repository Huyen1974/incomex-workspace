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
HJW | Hermes thành viên hội đồng chạy API, khép kín vòng | việc 2/5 | A0 ĐÃ XÁC NHẬN | NEXT: GPT Host xử lý P03 (Claude phản biện xong 22/09) → chốt HJW.2A | BLOCK: —

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

### P03 · Claude Chat · OPEN — phản biện một vòng: P02 + D08/D09 + Q01–Q06 · thiết kế HJW.2A (a)–(e)
- Based_on: `9be25c6df618bff15d3bfd8b47940d9e9889e004` · Scope: A0, D05–D09, HJW.2A (a)–(e), Q01–Q06, P02, T9–T10.
- Đã kiểm thật 22/09: (1) tài liệu Hermes hiện hành — cron có `script` + `{"wakeAgent": false}` (lọc bằng script, 0 LLM), `no_agent`, sổ chạy `executions.db` (claimed → running → completed/failed/unknown), incident chỉ báo một lần, thang thử lại 5/15/30 phút khi chưa gọi model, `hermes pause`, ghim model/reasoning/toolset theo từng job; webhook route có HMAC, `filters`, idempotency, rate-limit, `cron_job`. (2) Mã agent-data `hvu_signals.py`: nhãn Git author lấy từ MCP `clientInfo.name` ⇒ Hermes có attribution/presence mà không sửa gateway. (3) Bộ đồng bộ Owner View đã xuất `docker/nginx/static/ui-preview/hpml-view-for-user/data/tasks.json` + `revisions/<HEAD>/` = nguồn tín hiệu máy đọc sẵn trên VPS. (4) GSM-A1 chưa chạy (README §8 "CHƯA CHẠY").
- Chưa kiểm (Agent đo ở cổng chỉ-đọc HJW.2B): phiên bản Hermes đang cài có đủ các tính năng trên không; user `hermes` đọc được `tasks.json` không; relay 6533 trỏ 8000 hay 8080; Kuma có kênh báo Owner không; OpenRouter đặt hạn mức theo từng key được không.

**Trả lời P02:** ACCEPT (1)(2)(4)(5). (3) ACCEPT và chốt cụ thể ở (b). Attribution ở (5) chỉ cần thêm 1 dòng bảng phiên dịch A9 cho nhãn client của Hermes.

**(a) Hermes khác GPT/Claude ở đâu** — cột Hermes đều là tính năng có sẵn:

| Năng lực | GPT/Claude Chat | Claude Code CLI | Hermes |
|---|---|---|---|
| Tự thức theo lịch/sự kiện | không | không | cron + script-gate |
| Lọc 0-token trước khi gọi LLM | — | — | `wakeAgent:false`, `no_agent` |
| Chạy 24/7, cả khi Mac gập | không | không | có |
| Chủ động nhắn Owner | không | không | Telegram |
| Canh việc dài tới khi đạt điều kiện | không | trong 1 phiên | job tự huỷ khi xong |
| Quyền root/sudo | không | có (qua SSH) | không — việc cần root chuyển Claude Code |

**(b) Vòng đời giao việc**
- Dấu máy đọc (mở rộng A9, một dòng, không phụ thuộc vị trí): `ASSIGN@<WORK>-<NN> · to=<surface> · role=<Agent|Reviewer> · scope=<path> · state=<open|claimed|blocked|done>`, thêm `· run=<RUN_ID>` khi role=Agent.
- `open`: Host ghi. role=Agent chỉ hợp lệ khi dòng do Owner/GPT Chat ghi và có `run=` — đó chính là lệnh RUN cho Hermes theo A6; Hermes vẫn kiểm READY đúng SHA.
- `claimed`: Hermes đổi `open→claimed` bằng `workspace_edit` có expected_version. Hai lượt chen nhau thì lượt sau bị từ chối ⇒ dùng khoá lạc quan sẵn có, không dựng lock.
- `done`/`blocked`: ghi cùng commit kết quả (A4). `blocked` thêm một dòng "Owner cần quyết" + Telegram.
- Dò việc: bộ đồng bộ hiện có thêm `assignments[]` vào `tasks.json` (một bộ đọc duy nhất; Owner View thấy luôn việc đang giao cho ai). Job `ws-dispatch` mỗi 2 phút chạy script đọc `tasks.json`: revision không đổi hoặc không có dấu mới cho Hermes ⇒ `wakeAgent:false`. Chuông GitHub webhook + backstop 15 phút của bộ đồng bộ chính là trigger — không cần webhook thứ hai, không mở cổng mới.
- Chống trùng 3 lớp: revision SHA · khoá lạc quan khi claim · sổ chạy at-most-once. Chỉ tự thử lại khi chưa gọi model/chưa claim; việc đã có tác dụng phụ thì không tự chạy lại mà chuyển `blocked`.
- Chi phí: `cron.max_parallel_jobs=1`; ghim model + reasoning + toolset theo từng job; key OpenRouter riêng cho Hermes có hạn mức (xem c).
- Quan sát: sổ chạy + `hermes cron doctor` + incident; Kuma push nhịp tim 5 phút (Hermes chết thì Kuma báo — không để Hermes tự báo cái chết của mình); Git + `lastActors`.
- Công tắc: Owner nhắn "dừng tự động" → Hermes chạy `hermes pause`; "chạy lại" → `hermes resume`.

**(c) Secret — trả lời Q04, Q03**

| Thứ | Hermes cần? | Cách cấp | Nếu Hermes bị chiếm | Thu hồi |
|---|---|---|---|---|
| Quyền GSM | Không | giữ hiện trạng: user `hermes` không có credential Google | không đọc được kho | — |
| Deploy key / tài khoản GitHub Owner | Không | agent-data giữ | — | — |
| Khoá Agent Data | Không cầm | listener proxy loopback riêng cho Hermes, khoá gắn ở phía root; không sửa mã agent-data (giữ DROOT09) | dùng được trong lúc bị chiếm nhưng không mang khoá ra ngoài; mọi lần ghi có version guard + lịch sử Git | gỡ listener: chỉ Hermes mất quyền, GPT/Claude Code không ảnh hưởng |
| Key OpenRouter | Có | key riêng cho Hermes (khác key JEV), có hạn mức; root oneshot GSM → `/run/hermes` lúc start như hiện có | mất tối đa bằng hạn mức | xoá key trên OpenRouter, thêm version GSM, restart |
| Token bot Telegram | Có | như hiện có | kẻ gian nhắn Owner dưới tên Hermes | BotFather thu hồi |

- Proxy không làm được bằng cấu hình sẵn có thì lùi về mẫu tmpfs hiện có cho khoá Agent Data và ghi rõ rủi ro còn lại.
- Chỉnh chữ D08: vùng tin cậy thấp là **user `hermes`** (sandbox); root VPS chính là nơi nạp secret. Rủi ro còn lại — root VPS bị chiếm thì lộ mọi secret mà service account của VPS đọc được — chuyển GSM.3: cấp IAM theo từng secret thay vì cả project.
- Cổng READY HJW.2B: có `KQ@GSM-A1-20260922-01 XONG` xác nhận dòng "Hermes — nạp khoá" chỉ gọi lúc start và user `hermes` không có credential Google.

**(d) Danh mục tự động hoá — trả lời Q05**

| # | Việc | Trigger | LLM | Owner nhận gì | Đợt |
|---|---|---|---|---|---|
| 1 | Nhận và làm việc được giao | dấu `to=Hermes · state=open` | có | Telegram 3 dòng STATUS · COMMIT · NEXT | 1 |
| 2 | Chuông "đến lượt ai" | dấu/NEXT cho GPT, Claude, Owner chưa ai nhận sau 2 giờ; ngoài giờ gộp vào bản tin sáng | không | đúng 1 dòng lệnh để dán vào app | 1 |
| 3 | Canh RUN treo | READY + RUN mà chưa có `KQ@` sau 6 giờ, hoặc `KQ@ DỪNG` | không | cảnh báo 1 lần | 1 |
| 4 | Bản tin sáng 07:30 | lịch | không | ≤10 dòng: việc đổi hôm qua, việc tắc, "Anh cần quyết", tiền OpenRouter hôm qua | 1 |
| 5 | Nhịp tim | 5 phút | không | chỉ báo khi Hermes chết (qua Kuma) | 1 |
| 6 | Nghiệm thu độc lập sau deploy | `KQ@… XONG` có deploy | tuỳ việc | PASS/FAIL do Hermes tự gọi lại, không tin báo cáo agent | 2 |
| 7 | Canh ổ đĩa, backup, việc chờ bên ngoài | lịch, tự huỷ khi xong | không | báo khi vượt ngưỡng hoặc khi xong | 2 |
| 8 | Khảo sát/review nền dài (như review JEV) | dấu giao việc | có | báo cáo vào repo | 2 |

- Đợt 1 dựng đường ray và chứng minh T10. Đợt 2 là từng việc giao cho Hermes qua chính đường ray đó (một script + một job mỗi việc), không cần PROMPT lớn mới.
- Không giao Hermes: diễn giải luật nền (Founders), chốt trực tiếp với Owner (GPT Chat), việc cần root (Claude Code CLI), phá huỷ hoặc production khi chưa có RUN.

**(e) Có sẵn / thêm mới** — phần thêm mới toàn là cấu hình hoặc script nhỏ, không server mới:
- Có sẵn: cron/script-gate/`no_agent`/webhook/sổ chạy/pause/Telegram của Hermes; relay 6533; `tasks.json` + revisions; attribution theo `clientInfo`; mẫu Kuma push; mẫu root oneshot GSM → tmpfs; `workspace_*` có expected_version.
- Thêm mới: cú pháp `ASSIGN@` trong A9; `assignments[]` trong bộ đồng bộ; 1 dòng bảng phiên dịch A9; 1 listener proxy; key OpenRouter riêng + hạn mức; ~5 script trong `~/.hermes/scripts/`; 5 job đợt 1; nâng cấp Hermes nếu bản đang cài thiếu tính năng (giữ bản cũ để quay lại).
- Không làm: webhook GitHub thứ hai trỏ vào Hermes hay mở cổng 8644 ra internet (trễ ≤2 phút là đủ); Kanban của Hermes (thành SSOT thứ hai); đưa thuê bao Claude/ChatGPT lên VPS.

**Q06 — handoff:** tín hiệu chuẩn là dấu `to=` GPT Chat / Claude Chat / Owner trong COLLAB + Telegram đúng 1 dòng dán (`WS … · đọc AGENTS.md → …`); phần việc của Owner chỉ còn copy-paste. Hermes gọi model Claude/GPT qua OpenRouter cho việc của mình thì kết quả vẫn là của Hermes, không tính là review của thành viên kia. Chạy CLI headless trên VPS bằng thuê bao của Owner = đưa secret giá trị cao lên VPS ⇒ chỉ xét khi Owner quyết riêng.
**Q01:** giữ relay nội bộ, đo lại cổng. **Q02:** giữ 2 chìa; Hermes được làm một chìa khi được giao Reviewer.

**T9/T10 đo được** (thay câu chữ chung):
- T9: user `hermes` gọi GSM bị từ chối · không đọc được khoá Agent Data · key OpenRouter của Hermes có hạn mức, khác key JEV · xoay key xong Hermes lành sau 1 restart, GSM ≤ 1 lượt/restart.
- T10: 24 giờ không có việc ⇒ 0 lượt LLM do tự động (đối chiếu sổ chạy + usage OpenRouter) · dấu mới ⇒ claimed ≤ 5 phút, hai lượt chen nhau chỉ 1 claim · blocked ⇒ Telegram + dòng Owner cần quyết ≤ 5 phút · tắt gateway ⇒ Kuma báo ≤ 10 phút · "dừng tự động" có hiệu lực ngay, bật lại không chạy trùng.

- Owner cần quyết (Host đưa lên khi chốt): hạn mức key OpenRouter của Hermes — đề xuất **10 USD/tháng**, chỉnh sau khi đo T6.
- Đề nghị Host: nhận thì đưa (a)–(e) vào `view.html` rồi chốt HJW.2A. PROMPT HJW.2B làm một lần: cổng chỉ-đọc (5 mục "chưa kiểm") → cấu hình đợt 1 → nghiệm thu T1–T10. Không có hành động phá huỷ; nâng cấp Hermes phải giữ đường quay lại.
- Áp: SAME_COMMIT
- Host response: —

## Owner cần quyết
- — Chưa có.

## NEXT
- A0 **đã mở rộng và Owner xác nhận lại 22/09** với D08 Secret Boundary + D09 Always-on Value; JEV DONE; R03 CLOSED.
- **GPT Chat là Host hiện hành. Chưa RUN production.** HJW chuyển sang **HJW.2A DESIGN** trước, chưa soạn prompt implementation.
- Claude Chat phản biện P02 + D08/D09 + Q04–Q06 đúng một vòng theo A5/Planning Guide; đồng thời phải đọc kết quả `work/gsm-access-audit/` khi có để không thiết kế secret path bằng giả định. Sau khi HJW.2A đủ đồng thuận, GPT Host mới chốt `PROMPT.md` HJW.2B, READY rồi mới RUN.
