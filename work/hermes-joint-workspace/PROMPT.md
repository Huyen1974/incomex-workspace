# PROMPT — HJW · N3 COURIER / WAKE MATRIX · AUTO1 ASSISTED

RUN_ID: HJW-N3-COURIER-WAKE-20261007-01
STATUS: DRAFT · Host P188 soạn sau N2 PASS_WITH_RESIDUAL/P187 · chờ Claude Reviewer vòng 1/5 · CHƯA READY · CHƯA RUN
Host: GPT Chat · GPT-HJW-260922-A · Owner đã chỉ định cho HJW hiện tại
Reviewer: Claude Chat
Executor_Surface: Claude Code CLI phiên MỚI trên Mac cho inventory/orchestration + SSH/trusted-runner checks; các phiên canary được N3 gọi phải là phiên MỚI tách vai theo §5
Write_Path: repo qua workspace_*; runtime/config chỉ qua DOT/wrapper/apply path hiện hữu; không ad-hoc
Node: N3 / 6 · Automation target = AUTO1 ASSISTED
Owner_steps: 0 nếu binding/auth hiện hữu đủ. Nếu canary bắt buộc phải tạo routine/secret chính thức mới, gom **đúng một checkpoint Owner** với 4 ý `tạo gì · vì sao · ở đâu · không làm thì hỏng gì`; Owner không duyệt ⇒ KQ DỪNG sạch. DROOT43: không giữ terminal/model/browser chờ.

## 0. Mục tiêu duy nhất

Biến phần **nhắc lượt/copy-paste giữa các AI** thành máy làm, nhưng vẫn giữ Owner là người chỉ định Host và còn điều hành ở giai đoạn đầu.

N3 phải đo + thử + nếu đủ điều kiện thì bật một lớp **courier/wake AUTO1** có ba tầng:
1. **Đường chính:** Hermes VPS/trusted runner gọi **official direct invocation** của hãng bằng một con trỏ ngắn tới SSOT repo.
2. **Lưới an toàn song song:** self-pull/event/schedule chính thức của chính AI nếu hãng có; không được coi đường chậm/đốt model khi idle là đường chính.
3. **Fallback:** Hermes-Mac/Mac mini dùng official local CLI/app; Owner tay là lối cuối.

**Browser UI automation/scraping = DISABLED_BY_DEFAULT.** Không bot gõ vào chatgpt.com/claude.ai để giả courier.

N3 không xây Council Core N4, không tự chọn Host, không mở AUTO2/AUTO3.

## 1. Acceptance — N3 xong khi

### A. Wake matrix thật
Có bảng cho tối thiểu các surface/seat hiện hành:
- OpenAI-main: GPT Chat/Work/Dot — một ghế, task chọn đúng một bề mặt;
- Codex;
- Claude Chat/Cowork hoặc cloud/routine nếu tài khoản có;
- Claude Code CLI;
- Hermes VPS;
- Hermes-Mac/Mac mini.

Mỗi hàng:
`Seat | Vendor | Official path | Current account sees | Auth boundary | Server identity | Trigger | Claim latency | Idle model cost | Quota/cost | Receipt | Policy source/date | Live result | Class`

Class chỉ một trong:
`PRIMARY_DIRECT | SELF_PULL_SAFETY | LOCAL_FALLBACK | MANUAL_ONLY | POLICY_UNCERTAIN | VENDOR_LIMIT`.

### B. Primary courier canary
Hermes VPS/trusted runner phải live-call bằng đường chính thức được **ít nhất một Anthropic seat** và **ít nhất một OpenAI-family seat** (OpenAI-main hoặc Codex), hoặc chứng minh bằng evidence rằng vendor hiện không cho và ghi residual rõ.

Canary phải:
- 0 Owner copy-paste sau khi bắt đầu; bằng chứng = courier log `t0` + provider/session receipt + commit/P do **chính identity đích** ghi, và giữa `t0`→commit đó không có tin/commit thao tác từ Owner;
- courier chỉ gửi `task · step · round · seat · pointer`, không gửi prompt semantic;
- phiên đích tự đọc đúng đoạn repo rồi ghi đúng một receipt/P ngắn;
- có provider/session/run id hoặc receipt tương đương;
- log start/end/latency/identity/result, không lộ secret;
- max 2 live calls/seat trong RUN này.

### C. Claude dual-role trial
Thử hai phiên Claude **MỚI**:
1. `role=reviewer`: đọc N3 pointer + đúng đoạn cần thiết, ghi đúng một mục P nhận xét/canary receipt.
2. `role=worker`: nhận một sub-assignment N3 đã duyệt sẵn, làm một tác vụ an toàn/bounded và ghi canary result.

Bắt buộc đo identity phía server:
- nếu cả hai cùng `claude-code` ⇒ hai vai dùng được nhưng **không tính hai seat/quorum độc lập**;
- nếu routine/cloud và CLI có identity khác thật ⇒ ghi evidence rồi mới tính khác seat.
Worker không tự nghiệm thu KQ của chính mình.

### D. Self-pull safety net
Đo ít nhất một cơ chế self-pull/event/schedule chính thức nếu tài khoản/hãng có.
- cadence > claim timeout hoặc idle vẫn tốn model ⇒ chỉ `SELF_PULL_SAFETY`, không PRIMARY;
- ghế chỉ có self-check: claim timeout = chu kỳ check + 15 phút;
- không tạo polling model dày để cố đạt SLA.

### E. Safety/policy
- official docs hiện hành của từng hãng được re-check ngay trong RUN;
- **cấm** chép file/key/cookie của phiên đăng nhập sẵn có từ Mac/browser lên VPS;
- credential chính thức dành cho script (API key/OAuth token do Owner tạo qua flow hãng, ví dụ `claude setup-token`) chỉ được đặt vào **loader secret hiện hữu**; model/Hermes không đọc giá trị; tạo mới chỉ sau checkpoint Owner ở §2;
- secret chỉ qua loader/secret boundary hiện hữu;
- không cài browser bot, extension automation, scraping output;
- global STOP hiện hữu phải thắng courier;
- dedup/idempotency: cùng `task+step+round+seat+generation` không wake hai lần;
- chống loop: chỉ courier/dispatcher được wake seat; AI nhận việc không được tự gọi AI khác trong canary;
- không có COUNCIL_ALERT / DIRECTIVE_INTEGRITY_ALERT mở ở scope;
- POST-PROTECT/Config Guard/rollback receipt nếu có mutation runtime.

### F. Owner visibility
Bảng điều khiển phải ghi:
`Bước N3 · vòng k/5 · gọi: <seat...>`.
Mỗi P hội đồng/canary mở đầu:
`Ghế: <seat> · Bước/vòng: N3 · k/5`.
Sổ gọi tối thiểu:
`ai gọi ai · lúc nào · path class · provider session/receipt · server identity · commit/result`.
Ghi vào **sổ tin báo hiện hữu** và bảng trong P KQ; không mở file mới. Không tạo Owner View/DB/service mới.

## 2. Luật khóa

- Đọc: `AGENTS.md` → root COLLAB DROOT40–46 → HJW Bảng → §0.3 HĐ19–HĐ25 → P186 → P187 → file này.
- §0.3: đã đối chiếu. F1–F4 P186 là bắt buộc.
- Owner luôn chỉ định Host. N3 **không** được viết logic tự chọn Host.
- Task bootstrap chỉ ghi phần riêng; defaults lấy từ AGENTS, không copy lại.
- Không tạo task/project/file/service/DB/route public mới.
- **Candidate creation đã review nhưng CHƯA được Owner duyệt:** nếu Pha A chứng minh cần thiết, hỏi Owner đúng một lần để tạo (a) ≤1 Claude Routine chỉ có **API trigger, không schedule**, scope đúng repo/canary của `claude-main`; (b) ≤1 secret item cho mỗi hãng trong loader hiện hữu. Prompt hỏi phải đủ 4 ý A0. Owner gật mới tạo; Owner không gật ⇒ `AUTH_OWNER_ACTION_REQUIRED`. KQ không PASS ⇒ routine/secret N3 vừa tạo phải disable/revoke trong cùng RUN nếu API cho phép an toàn.
- Ngoài danh sách trên hoặc muốn tạo file/service/route ⇒ `KQ DỪNG · DELTA_REVIEW_REQUIRED`, nêu exact delta + rollback.
- Không install package/CLI chỉ để thử. Ưu tiên binary/client/routine đã có. Cần install/login mới ⇒ checkpoint.
- Không dùng raw token/session cookie/auth export từ browser.
- DROOT30/31/35/42/43, Config/Protection Guard và NO-WAIT áp nguyên.
- RUN khác đang STARTED trên shared runtime: inventory read-only được làm; trước mutation phải clear, không chờ.
- Chính sách hãng là gate sống: docs cũ trong P182/P185 chỉ là đầu vào; executor phải re-check official docs hiện hành trước live test.
- Policy wording mơ hồ cho subscription automation ⇒ `POLICY_UNCERTAIN`, **không enable** và không lách bằng web UI.

## 3. PHA A — INVENTORY / POLICY / BINDING · READ-ONLY

1. Fresh-read Bảng + PROMPT + READY; chỉ bắt đầu RUN khi READY đúng last-touch.
2. Kiểm STOP/concurrency/protection hiện hành.
3. Inventory **không cài gì**:
   - Hermes VPS dispatcher/courier/runtime hiện hữu;
   - command/client/routine/Work/Codex/Claude paths đang có trên VPS/Mac;
   - auth: linked account / API key / subscription login / none;
   - server-side author labels đã thấy;
   - current schedules/events/self-pull mechanisms;
   - Mac fallback readiness, nhưng không mở browser automation.
4. Đọc official docs hiện hành của Anthropic/OpenAI cho đúng path sẽ thử; ghi URL/title/date vào P, không chép dài.
5. Chốt wake matrix PRE và danh sách canary **ngay trong P READY**: `seat · bề mặt · official path · max_calls≤2`. Codex là canary seat, không mặc nhiên có phiếu HJW. `openai-main` chỉ gọi **bề mặt đã được Owner chỉ định (hiện GPT Chat)**; Work/Dot chỉ đo capability, không được ghi P vào HJW ở N3.
6. Phiên canary chỉ có gateway tools đọc/ghi đúng HJW COLLAB; **không shell, không tool gọi AI khác**, có trần call/time.

Không live-call model nếu chưa biết path/policy/auth.

## 4. PHA B — PRIMARY DIRECT INVOCATION CANARY

Thứ tự:
1. **Hermes VPS/trusted runner → official direct invocation**.
2. Nếu VPS không thể vì auth/policy nhưng official local path có sẵn: Hermes-Mac/Mac mini fallback.
3. Self-pull chạy song song như safety net, không thay direct path nếu quá chậm.
4. Owner manual = classification cuối, không dùng để giả PASS.

Mỗi call chỉ gửi pointer:
`HJW · N3 · vòng <k> · seat <id> · đọc AGENTS → HJW Bảng → P/section <ref> · làm đúng role`.

Target tự lấy semantic content từ repo.

Đo:
- provider/session/run receipt;
- t0/t_claim/t_result;
- server identity/commit author label;
- model call count nếu thấy được;
- lỗi/policy/auth.

Path cần browser automation để lấy Output ⇒ classify `POLICY_UNCERTAIN|MANUAL_ONLY`, không chạy.

## 5. PHA C — CLAUDE DUAL-ROLE FRESH SESSION

### C1 Reviewer canary
Gọi một phiên Claude mới bằng **official path tốt nhất đã đo**:
- role=reviewer;
- đọc đúng pointer;
- không code/runtime;
- ghi đúng một P canary ngắn vào HJW COLLAB;
- P mở đầu `CANARY · Ghế: ... · Bước/vòng: N3 · <k>/5`; **P canary không tính phiếu hội đồng**;
- đóng phiên.

### C2 Worker canary
Gọi **một phiên mới khác**, role=worker.
Sub-assignment N3 cho phép:
- chỉ đọc một fixture/đoạn hiện hữu được chọn trước;
- làm tác vụ bounded không ảnh hưởng production;
- nếu cần ghi, chỉ ghi một canary result vào HJW COLLAB;
- không tự review kết quả;
- đóng phiên.

Không dùng `--resume` mặc định.

Kết luận identity:
`SAME_IDENTITY_TWO_ROLES` hoặc `SEPARATE_IDENTITIES`.

## 6. PHA D — SELF-PULL SAFETY NET

Với mechanism chính thức có sẵn:
- đo cadence thật;
- xác định model call khi idle;
- không tạo lịch dày hơn chỉ để đạt claim SLA;
- không tạo schedule mới nếu Owner chưa duyệt và existing mechanism không có fixture an toàn.

Kết luận:
`SAFETY_NET_PASS | SAFETY_NET_TOO_SLOW | SAFETY_NET_COSTLY_IDLE | NOT_AVAILABLE`.

## 7. PHA E — MINIMAL ENABLEMENT

Chỉ nếu A–D chứng minh một `PRIMARY_DIRECT` đúng policy và **existing Hermes dispatcher/courier reuse được**. `PRIMARY_DIRECT` phải có `t_claim - t0 ≤ Claim_Timeout_Min` lấy từ AGENTS. `trusted runner` = VPS/wrapper/DOT **đang có**, không thêm runner mới.

**Authority gate:** courier chỉ đưa thư khi có **chuông/lệnh do identity server-side của Host hiện hành hoặc Owner ghi** trong đúng scope (Bảng/ASSIGN_V1/canonical call record). Commit/P của ghế khác **không tạo lượt gọi**. Pha E giữ `Automation_Level=AUTO0`, không đổi chế độ approval, không thêm `AUTO_ALLOWLIST`; việc bật AUTO1 cho HJW là quyết định Owner **sau KQ N3**.
- Đặt trần daily calls per seat trong config hiện hữu trước enable; canary vẫn max 2/seat.

Được phép:
- sửa cấu hình/logic **hiện hữu** của HJW courier/dispatcher;
- thêm mapping seat→official path trong config hiện hữu;
- thêm dedup/receipt/STOP check vào code hiện hữu;
- cập nhật Config/Protection Guard + sổ tin báo nếu path mới tạo loại tin mới;
- apply qua wrapper/DOT hiện hữu, rollback + post-protect cùng RUN.

Không được:
- tạo service/daemon/database/browser bot/file mới;
- mở route public mới;
- cài package/CLI;
- copy credential;
- bật AUTO2/AUTO3.

Cần một việc cấm ⇒ `KQ DỪNG · DELTA_REVIEW_REQUIRED · CONTINUE_SAME_NODE`.

## 8. Negative tests

1. Duplicate pointer cùng generation ⇒ 1 wake.
2. Seat ngoài roster ⇒ không wake.
3. Courier mang semantic/prompt thay vì pointer ⇒ reject.
4. STOP active ⇒ 0 wake.
5. Alert mở trong scope ⇒ không wake mutation role.
6. Reviewer cố worker mutation / worker cố làm reviewer quorum ⇒ block/không tính.
7. Same technical identity ⇒ không đếm hai seat.
8. Browser/UI-only path ⇒ không automate.
9. Policy source stale/không truy cập được ⇒ không enable.
10. Self-pull trễ ⇒ không PRIMARY_DIRECT.
11. Mac ngủ/tắt khi có thư chờ ⇒ thư không mất, không nhân đôi; pending quá hạn mới cảnh báo.
12. Chuông/lệnh do ghế không phải Host/Owner ghi ⇒ **0 lượt gọi**.

## 9. Disposition

### PASS
`KQ@HJW-N3-COURIER-WAKE-20261007-01 XONG · N3_PASS · AUTO1_PRIMARY_COURIER_PASS · MULTI_VENDOR_WAKE_MEASURED · CLAUDE_DUAL_ROLE_MEASURED · SELF_PULL_SAFETY_MEASURED · NO_BROWSER_AUTOMATION · PROTECTION_CLEAN`

PASS yêu cầu:
- ≥1 Anthropic official automated path live-pass;
- ≥1 OpenAI-family official automated path live-pass;
- Owner 0 thao tác/copy-paste trong live canary;
- negative tests §8 **đều PASS trên fixture, 0 tin thử tới Owner**;
- receipt + server identity + dedup/STOP proof.

Đường chỉ chạy từ Hermes-Mac = residual `PRIMARY_MAC_ONLY`, **không tính PASS**. Không bắt mọi seat PRIMARY_DIRECT; residual/class phải rõ.

### PASS_WITH_RESIDUAL
Chỉ được dùng khi **≥1 official automated path chạy thật với 0 thao tác Owner** và toàn bộ negative §8 PASS; vendor family còn lại phải có `VENDOR_LIMIT|POLICY_UNCERTAIN|AUTH_OWNER_ACTION_REQUIRED` kèm evidence.
`KQ@... XONG · N3_PASS_WITH_RESIDUAL · <residuals> · MOVE_TO:N4`
**0 đường automated live-pass ⇒ DỪNG**, không MOVE_TO N4. Host/Reviewer quyết residual trước N4.

### DỪNG
`POLICY_UNCERTAIN:<path>` · `VENDOR_LIMIT:<path>` · `AUTH_OWNER_ACTION_REQUIRED` · `DELTA_REVIEW_REQUIRED` · `CONCURRENCY_GATE` · `EXTERNAL_GREEN_GATE` · `PROTECTION_FAIL`.

DỪNG = checkpoint sạch, 0 waiter, đóng CLI.

## 10. Báo cáo cuối

Một P ngắn:
1. `Ghế · Bước/vòng`;
2. wake matrix PRE→POST;
3. receipts/latency/identity;
4. Claude dual-role result;
5. self-pull result;
6. runtime delta + rollback nếu có;
7. negative tests;
8. exact residual;
9. Owner action = 0 hoặc đúng một human-only;
10. đề nghị Host: `PASS | PASS_WITH_RESIDUAL | DỪNG`.

Không paste secret, session cookie, private URL/token hay raw provider response dài.
