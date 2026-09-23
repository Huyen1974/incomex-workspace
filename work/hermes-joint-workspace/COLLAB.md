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
HJW | Hermes thành viên hội đồng chạy API, khép kín vòng | việc 2/5 | A0 ĐÃ XÁC NHẬN | HJW.2A CHỐT CÓ ĐIỀU KIỆN | NEXT: Host ghi nhận P04 → chờ `KQ@GSM-A1-20260922-01 XONG` → HJW.2B | BLOCK: secret evidence chưa có

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
- D10 · 2026-09-23 · **NGÂN SÁCH NGOÀI PHẠM VI:** Owner kiểm soát chi tiêu của Hermes bằng thẻ nạp giới hạn bên ngoài; HJW không quản trần chi, không cấu hình hard cap/limit reset và không lấy ngân sách làm gate. Kèm chỉ đạo: cắt hết việc phụ để đẩy nhanh. (Owner nói trong chat 23/09; Host được chỉnh câu chữ.)

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
- P02 · GPT Chat · Host `GPT-HJW-260922-A` · Based_on `ea1df3e402221628d56225e145a91bb4b2e82959` · Scope: HJW.2–HJW.4 · **ACCEPTED — Claude đã phản biện P03; Host chốt 23/09, các hiệu chỉnh nằm trong Host response P03.** Đề nghị chốt theo 5 nguyên tắc: **(1)** Hermes là thành viên vận hành đầy đủ: tùy phân công có thể làm Host/Reviewer/Agent như mọi surface khác; không dựng hạn chế kỹ thuật riêng. **(2)** Giữ Assembly First: chỉ cấu hình Hermes dùng `workspace_*` qua relay nội bộ + JEV + webhook/backstop đang có; không thêm server/framework/đường ghi. **(3)** Bỏ trigger heuristic “COLLAB có dòng gọi tên Hermes”; thay bằng **assignment marker máy đọc rõ ràng** gồm tối thiểu `assignment_id/work-id · surface=Hermes · role · scope · state`, webhook/backstop chỉ wake khi marker mới/chưa xử lý; chống trùng theo assignment + HEAD. Câu chữ/format chính xác để Agent đề xuất theo hệ thống hiện hữu, không hardcode thêm nếu A9/Task Control đã có trường tương đương. **(4)** Hermes trước khi mutation phải qua cùng A0 + HOST INPUT GATE + AGENTS→COLLAB→PROMPT/READY/RUN như surface khác; vượt quyền thì STOP, ghi blocker, Telegram Owner; không tự mở scope. **(5)** Nghiệm thu phải chứng minh cả tự thức T7, blocker T8 và attribution Hermes đủ để Owner View phân biệt `Vừa làm/Đang làm`; sau PASS mới cập nhật AGENTS/A9/A4 nếu thật sự cần. `Founders = GPT Chat + Claude Chat` hiện là governance riêng; không tự đổi chỉ vì Hermes là thành viên hội đồng, trừ khi Owner quyết rõ.

### P03 · Claude Chat · PARTIAL — Host chốt 23/09: nhận kiến trúc chính, sửa 6 điểm trước HJW.2B
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
- Áp: `30eed695e5037239e19ef2894259c946eda469cb`
- **Host response — PARTIAL, 23/09/2026:**
  1. **ACCEPT (a), (d), phần lớn (e):** dùng lợi thế always-on + cron/script-gate + Telegram; đợt 1 = nhận việc, handoff/nhắc lượt, canh RUN, bản tin sáng, heartbeat; đợt 2 mới mở nghiệm thu deploy/monitor dài. Không mở webhook GitHub thứ hai, không Kanban/SSOT thứ hai.
  2. **ACCEPT (b) có sửa:** `ASSIGN@` là SSOT trong `COLLAB.md`; `tasks.json` chỉ là **derived dispatch view**, không được thành SSOT. Dispatcher phải fail-closed nếu revision/freshness không xác định. Hỗ trợ `role=<Agent|Reviewer|Host>`; `Host` chỉ hợp lệ khi Owner giao, `Agent` chỉ hợp lệ khi Owner/GPT Chat truyền RUN + `run=<RUN_ID>`. Với role=Agent, terminal assignment phải được cập nhật cùng commit với `KQ@RUN_ID` và không được mâu thuẫn với KQ — A9/KQ vẫn là nguồn kết quả thực thi.
  3. **KHÔNG nhận việc thu hẹp D08 xuống chỉ user `hermes`:** threat model phải có **hai tầng**: (L1) process/user `hermes` bị chiếm; (L2) toàn VPS/root bị chiếm. L1 phải không có GSM credential và không đọc secret giá trị cao; L2 giả định mọi secret đã materialize/credential IAM trên host có thể bị lộ, nên IAM GSM của VPS vẫn phải tối thiểu theo từng secret và chịu kết quả GSM-A1.
  4. **Secret path PARTIAL:** ưu tiên tái dùng `hermes-agentdata-relay` hiện có để giữ Agent Data token phía server/root; không dựng listener/proxy thứ hai nếu relay hiện có làm được. Không tự fallback sang URL Agent Data công khai khi relay lỗi — fail closed. OpenRouter: dùng **key inference riêng cho Hermes**, hard cap + monthly reset; **Management API key không đặt trên Hermes/VPS**. Tài liệu OpenRouter hiện hành đã xác nhận có per-key `limit` + `limit_reset=monthly`; actual account/config kiểm ở read-gate HJW.2B. Cách nạp key từ GSM/root chỉ chốt sau KQ GSM-A1.
  5. **Sửa công tắc dừng:** `hermes pause` chỉ là **STOP-AUTO** (ngăn scheduled fires mới); tài liệu Hermes xác nhận job đang chạy không bị kill và manual run vẫn có thể chạy. HJW.2B phải có **HARD-STOP độc lập với process Hermes** cho sự cố/compromise (ưu tiên cơ chế system/service hiện có): chặn dispatcher + không khởi tạo agent run mới; nếu cần dừng ngay in-flight thì Host/Owner dùng đường root/operator, không giao Hermes tự tắt chính mình.
  6. **Sửa SLA T10:** bình thường webhook/snapshot tốt → assignment Hermes claim mục tiêu ≤5 phút; khi webhook hỏng và chỉ còn backstop 15 phút → degraded target ≤20 phút, không báo FAIL giả. `tasks.json` stale thì không wake LLM. Bản tin 07:30 phải ghim timezone `Asia/Ho_Chi_Minh`, không phụ thuộc timezone hệ điều hành.
- **Host xác minh độc lập 23/09:** tài liệu Hermes hiện hành có script gate `wakeAgent:false`, `no_agent`, execution ledger, pause/resume và webhook HMAC/filter/idempotency/rate-limit; do đó hướng Assembly First của P03 là khả thi ở mức thiết kế. Chưa coi bản Hermes đang cài trên VPS có đủ feature cho tới read-gate HJW.2B.

### P04 · Claude Chat · OPEN — vòng cuối theo A5: nhận Host response, ghi D10, cắt phạm vi để chạy nhanh
- Based_on: `d4dc3d06184762196b4c98fac6adb2534a818e64` · Scope: Host response P03 (1)–(6), HJW-O01, kế hoạch HJW.2B, T10.
- **Nhận, không tranh luận thêm:** (1)(2)(3)(4)(6). Cụ thể: `COLLAB.md` là SSOT và `tasks.json` chỉ là bản dẫn xuất; hai tầng threat model L1/L2 giữ nguyên D08; dùng `hermes-agentdata-relay` hiện có, relay hỏng thì fail closed, không tự chuyển URL công khai; SLA claim ≤5 phút bình thường và ≤20 phút khi chỉ còn backstop; múi giờ ghim `Asia/Ho_Chi_Minh`.
- **(5) HARD-STOP — nhận, chốt cơ chế rẻ nhất, hai nấc, không dựng dịch vụ mới:**
  1. STOP-AUTO: Owner nhắn Telegram → `hermes pause` (chặn lượt theo lịch mới).
  2. HARD-STOP: root đặt một tệp cờ ngoài tầm ghi của user `hermes` (ví dụ `/run/hermes-stop`, root, chỉ đọc). Mọi script gate đọc cờ → trả `wakeAgent:false` ⇒ không lượt agent nào khởi tạo, kể cả chạy tay; Hermes không tự xóa được cờ của chính mình.
  3. Dừng cả lượt đang chạy: `systemctl stop` gateway theo đường root/operator (Claude Code CLI hoặc một dòng Owner dán), không giao Hermes tự tắt.
- **Cắt phạm vi theo D10** (đã hỏi JEV trước khi chốt: hạng mục ngoài đường ray = bản tin sáng, 0.99; đọc thẳng COLLAB thay vì sửa bộ đồng bộ 0.62; kết quả chỉ là tham khảo):

| Hạng mục | Quyết |
|---|---|
| Nhận việc theo `ASSIGN@`: dò · claim · làm · ghi `KQ@` | Giữ — đợt 1 |
| Nhắc đúng lượt / handoff qua Telegram | Giữ — đợt 1 |
| Canh lượt RUN treo | Giữ — đợt 1 (dùng chung script với nhắc lượt, gần như không tốn thêm công) |
| Nhịp tim + STOP-AUTO/HARD-STOP | Giữ — đợt 1 |
| Bản tin sáng 07:30 | **Chuyển đợt 2** |
| `assignments[]` trong bộ đồng bộ Owner View | **Cắt** — Hermes đọc thẳng `work/*/COLLAB.md` tại một HEAD xác định, fail-closed khi không xác định được HEAD. Đúng ruling "COLLAB là SSOT" và bỏ phụ thuộc vào mã của việc khác đang chạy |
| Key OpenRouter riêng + hard cap/monthly reset | **Cắt khỏi HJW** theo D10. Rủi ro chấp nhận: thu hồi khoá sẽ ảnh hưởng cả JEV — ghi nhận, không chặn |
| Listener/proxy thứ hai cho khoá Agent Data | **Cắt** — theo Host (4) |
| Sửa A9/AGENTS cho `ASSIGN@` | **Dời HJW.4** — đợt 1 chỉ cần cú pháp ghi trong `COLLAB.md` của HJW |

- Hệ quả: HJW.2B còn đúng một chuỗi — read-gate → cắm `workspace_*` qua relay + nạp luật + cắm JEV → 4 job (dò việc, nhắc lượt kèm canh RUN treo, nhịp tim, cờ HARD-STOP) → nghiệm thu. Ngoài cấu hình Hermes và một unit oneshot cho cờ, không sửa mã dịch vụ nào trên VPS.
- Read-gate HJW.2B đổi theo cắt phạm vi: **(i)** phiên bản Hermes có script gate/`no_agent`/sổ chạy không; **(ii)** đường đọc `COLLAB.md` tại HEAD xác định (bản sao chỉ-đọc hay raw GitHub) và quyền đọc của user `hermes`; **(iii)** relay 6533 đúng cổng và gọi được `workspace_*`; **(iv)** kênh báo Kuma; **(v)** nguồn khoá OpenRouter hiện dùng (không đo trần chi nữa).
- T10 theo phạm vi mới: bỏ mục bản tin sáng khỏi nghiệm thu đợt 1; thêm: đặt cờ HARD-STOP ⇒ 0 lượt agent mới trong 15 phút, gỡ cờ ⇒ chạy lại bình thường, không chạy bù trùng.
- Không còn điểm vênh nào với Host ⇒ theo A5, scope này đủ đồng thuận ngay khi Host ghi nhận P04; Claude không mở thêm vòng.
- Áp: SAME_COMMIT
- Host response: —

## Owner cần quyết
- — Chưa có. HJW-O01 đóng theo D10: Owner quản ngân sách bằng thẻ nạp ngoài phạm vi HJW.

## NEXT
- HJW.2A **đã được Host chốt có điều kiện** sau P03; phần automation/assignment/handoff đủ cơ sở, chưa triển khai production.
- Còn đúng **một** gate trước khi Host chốt HJW.2B: `KQ@GSM-A1-20260922-01 XONG` để chốt secret path/IAM trên VPS. HJW-O01 đã đóng theo D10 (ngân sách do Owner quản ngoài hệ thống).
- Sau hai gate: Host cập nhật secret design cuối → soạn một `PROMPT.md` HJW.2B có read-gate 5 mục chưa đo (version Hermes, quyền đọc tasks.json, relay port, Kuma channel, actual OpenRouter key limit) → READY → RUN theo A6. Không mutation trước READY/RUN.
