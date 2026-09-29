# PROMPT — MCPW GEN2 CLOSEOUT + HERMES MANUAL SIGNAL + ĐIỀU 30/31 PROTECTION

RUN_ID: MCPW-GEN2-HERMES-PROTECT-20260929-01
Host: GPT Chat · GPT-MCPW-250925-A
Executor_Surface: Claude Code CLI trên Mac Owner; phần quan sát dài không phụ thuộc Mac.
Report_Write_Path: KQ chính chỉ `work/mcp-workspace/COLLAB.md`; riêng smoke Hermes được ghi đúng `ASSIGN@` + câu trả lời/done trong `work/hermes-joint-workspace/COLLAB.md` theo contract known-good P52/P61. Không file repo mới.
Runtime: VPS1 production; evidence dùng hồ sơ AD1/HJW hiện hữu, không tạo task mới.

## 0. Mục tiêu
Làm đúng ba việc, theo thứ tự:
1. đọc machine-state GEN2 đã kết thúc và full-accept lớp GitHub nếu PASS;
2. khôi phục/chứng minh đường **giao việc MANUAL cho Hermes** theo CONTROL-B/P61 đã nghiệm thu, không bật AUTO và không mở rộng write scope;
3. đưa durable code/config mới của AD1/Hermes vào lớp bảo vệ DROOT29 / Điều 30 / Điều 31 bằng Guard/Config Guard/contract/watchdog hiện hữu.

Không làm Pha B/C lifecycle trong RUN này. Không đụng VPSUP credential rotation.

## 1. Read/collision gate
Đọc AGENTS → root COLLAB DROOT22/25/28/29 → MCPW COLLAB P35–P44 → HJW COLLAB S1–S10 + P52/P61–P64 → PROMPT này.
Đọc machine-state trực tiếp từ VPS, ưu tiên file state/log, không gọi mạng chỉ để xác minh:
- `/var/lib/incomex-mcpw-guard/ad1-watch.json`;
- `/opt/incomex/work/mcp-workspace/MCPW-AD1-20260927/AD1_24H.txt`;
- `ad1-watch.log` tương ứng.
GEN=2 phải terminal PASS. Nếu RUNNING/FAIL/mơ hồ ⇒ DỪNG, chỉ report state; không mutation Hermes/Guard.
Kiểm `work/vps1-up-grade`: nếu SEC-CRED hoặc RUN khác đang mutation agent-data/Hermes/Guard/GSM/credential liên quan ⇒ DỪNG trước mutation. Repo conflict thuần túy thì re-read/version-guard; không vượt active runtime mutation.
Chụp PRE: Agent Data/Claude MCP StartedAt/image/hash/health; HJW gate/plugin/root hashes, jobs/ws-dispatch, STOP, AUTO_ALLOWLIST, Kuma #21/#22; Protection/Config Guard target list/baseline.

## 2. Scope / hard stops
Được:
- đọc state/counter/journal AD1/HJW;
- sửa tối thiểu HJW manual assignment runtime **chỉ nếu live state lệch known-good P52/P61**;
- sửa/đăng ký Protection Guard/Config Guard/contract/watchdog để bao phủ durable targets AD1/HJW;
- restart `hermes-gateway` chỉ khi exact HJW delta bắt buộc và rollback sẵn.

Cấm:
- restart/recreate `agent-data` hoặc `claude-mcp`;
- sửa/rotate AGENT_DATA_API_KEY/PG credential/GSM;
- bật AUTO hoặc thêm AUTO_ALLOWLIST;
- mở rộng Hermes write scope/path/toolset;
- Pha B/C execution ledger/lease;
- ruleset mutation;
- service/DB/port/token mới;
- update Hermes version;
- nới GitHub budget.

## 3. GEN2 full closeout — machine evidence
Nếu GEN2 PASS:
1. lưu exact terminal line + 24 window results; xác minh 24/24 green, root/gate local 0 GitHub theo contract, REST/budget/ruleset/P02 criteria PASS;
2. từ counter hiện hữu tính **write amplification** trong chính 24h:
   - event_calls_peak_per_hour;
   - số push/commit theo cửa sổ tương ứng;
   - event_calls_per_push p50/p95/max nếu đủ mẫu;
   - channel git/raw/REST;
   - 403/429/5xx/timeout/backoff counts.
Không mặc định 3/push nếu dữ liệu không chứng minh.
3. ghi kết luận giới hạn: GEN2 PASS chứng minh tải nền; burst write chỉ được coi bounded nếu event/push ổn định. Writes vẫn fail-closed/revalidate GitHub theo K8/P02.
4. xác minh watcher sau terminal đã chuyển alert-only và watchdog còn sống; không re-arm 24h.

Không sửa counter chỉ để làm đẹp số.

## 4. Hermes MANUAL — xác định lỗi thật trước sửa
Nguồn known-good: HJW CONTROL-B/P52 + FINAL P61/P62 + evidence dưới `/opt/incomex/work/hermes-joint-workspace/HJW-CONTROL-20260926-01/final/`.
Expected:
- mode = **DUYỆT TỪNG VIỆC**;
- `AUTO_ALLOWLIST=()`;
- STOP OFF;
- plugin `hjw-control` + gate/root control hashes/semantics đúng known-good;
- assignment hợp lệ ⇒ Telegram card; chỉ Owner click hợp lệ ⇒ BẮT ĐẦU receipt ⇒ exactly one one-shot `repeat 1`; không click/từ chối/STOP ⇒ 0 model;
- commit/result attribution + Kuma drift monitor giữ nguyên.

Đọc live code/config/jobs/log trước. **Không suy chỉ từ lịch sử P45 `ONE_SHOT_ENABLED=False/no_agent=true`** vì CONTROL-B dùng base job no-agent nhưng sau Owner click mới tạo one-shot. Đồng thời đọc code `in_scope()`/assignment parser hiện hành: contract known-good chỉ nhận dòng `ASSIGN@` nằm trong `work/hermes-joint-workspace/COLLAB.md` với scope HJW; việc cần đọc có thể nằm ở task khác.
Phân loại:
A. runtime known-good + cách giao trước đây sai vị trí ⇒ **không sửa runtime**; dùng đúng ASSIGN ở HJW như P52/P61;
B. runtime drift khỏi P52/P61 ⇒ restore exact known-good bytes/config từ evidence/rollback, không tự viết lại kiến trúc;
C. ASSIGN đúng HJW tạo card nhưng one-shot bị chặn **read-only** khi đọc tài liệu task khác ⇒ mới được xem §5 read-only patch; không tự mở write scope/tool/profile khác;
D. lỗi khác ⇒ DỪNG với root-cause evidence; không bật fail-open/AUTO.

## 5. Live Hermes acceptance — MANUAL, không AUTO
Sau fixture/known-good PASS, tạo **một** smoke đúng contract P52/P61:
1. Một identity **không phải Hermes** ghi vào `work/hermes-joint-workspace/COLLAB.md` đúng một dòng theo format hiện hữu: `ASSIGN@HJW-MANUAL-SMOKE-20260929-01 · to=Hermes · role=Reviewer · scope=work/hermes-joint-workspace · state=open`. Không đặt ASSIGN ở MCPW.
2. Payload/lời giao one-shot phải ghi rõ `MCP root=workspace`, cấm dò/đoán root, và yêu cầu **chỉ đọc** `work/mcp-workspace/COLLAB.md` các P39/P44/P45 hiện hành; không ghi MCPW.
3. Hermes trả đúng 3 dòng **trong HJW COLLAB**: `HERMES_MANUAL_SMOKE=PASS|BLOCKED`; `assignment=<id> actor=<server-auth identity>`; `limitation=<none|mô tả ngắn>`, đồng thời đổi chính ASSIGN `open→done` trong **cùng một commit `[Hermes] ASSIGN@HJW-MANUAL-SMOKE-20260929-01`**. Đây là repo mutation duy nhất được yêu cầu từ Hermes trong smoke và nằm trong write scope HJW đã nghiệm thu.

Acceptance:
1. dòng ASSIGN do non-Hermes identity trong HJW được gate nhận;
2. Telegram card CHỜ DUYỆT xuất hiện ≤5′;
3. trước Owner click = 0 model;
4. Owner click `Cho chạy` ⇒ callback ack + BẮT ĐẦU receipt;
5. đúng 1 one-shot model, profile/toolset không rộng hơn known-good P52/P61;
6. Hermes đọc được các đoạn MCPW được giao, tạo đúng 1 commit trong HJW, ASSIGN→done; Telegram RESULT = XONG suy từ Git/sổ, không từ lời model;
7. commit ngoài HJW = 0; runtime mutation = 0;
8. duplicate/replay/sai người/STOP fixture ⇒ 0 model; AUTO vẫn rỗng.

**Read-only exception, chỉ khi có bằng chứng:** nếu ASSIGN/card/click/one-shot đều đúng nhưng WAKE contract/server read-scope từ chối đọc `work/mcp-workspace/COLLAB.md`, trước hết lưu exact deny evidence. Chỉ trong trường hợp đó được vá nhỏ nhất để mở **read-only** tới exact path cần đọc hoặc generic `work/<task>/...` read nếu cơ chế hiện hữu bắt buộc; write scope vẫn chỉ HJW, toolset/credential/AUTO không đổi. Vết vá phải có fixture allow-read/deny-write + §6 Điều 30/31 protection. Nếu cần mở write chéo task, tool mới, credential mới hoặc route mới ⇒ DỪNG và báo Host.

Nếu ASSIGN đúng HJW mà card không xuất hiện hoặc Owner click không tạo one-shot, DỪNG sau root-cause evidence; không bật đường fail-open cũ.

## 6. DROOT29 · Điều 30/31 protection coverage
Inventory durable production targets do AD1/AD1-FIX/Hermes manual control đang chạy, tối thiểu:
- `/opt/incomex/scripts/mcpw-protection-guard`;
- `/opt/incomex/scripts/hjw-control-root.py`;
- HVU `scripts/hvu-b2/sync.py` + timer/config liên quan;
- `/etc/hermes/hjw-ad1.conf`;
- HJW `hjw_gate.py`, plugin `hjw-control`, root control/watch scripts và jobs/config keys dùng cho MANUAL;
- durable file khác mà PRE chứng minh thuộc exact control path.

Áp:
### Điều 30
- xác định hành vi cũ bị chạm; chạy regression suite/fixture hiện hữu;
- nếu không chạm web UI thì ghi `D30_UI_NOT_TOUCHED`;
- nếu Owner View/web UI bị sửa ngoài dự kiến ⇒ browser thật bắt buộc, API/SSR không thay proof;
- Telegram control nếu bị sửa phải chạy callback/UX regression thật hoặc fixture + một live smoke phù hợp.

### Điều 31
- mọi durable target phải có path + expected hash/invariant + owner/scope trong Protection/Config Guard/contract hiện hữu phù hợp;
- inverse check: target production bị thiếu/unregistered ⇒ FAIL/alert;
- self-protection: guard/baseline/checker file cũng được bảo vệ, không tự học drift;
- negative/mutant trên copy/fixture: sai hash/missing target/config key ⇒ guard FAIL;
- watchdog hiện hữu phải chứng minh runner còn sống; silence không PASS;
- controlled rebaseline chỉ trong RUN được cấp phép với old→new + reason + outside-scope PASS;
- rollback/known-good cho từng delta.

Không tạo service/DB/guard framework mới nếu guard hiện hữu đủ ghép.

## 7. PRE/POST / regression
PRE/POST Protection + Config Guard PASS.
P02/Agent Data/Claude MCP identity không đổi trong RUN này.
HJW STOP/AUTO/profile/toolset không mở rộng.
Kuma #21/#22 health PASS.
Outside-scope runtime diff = 0.
Điều 30/31 target coverage không còn `UNMONITORED`.
Mutant/negative bắt được lỗi; watchdog sống.

## 8. KQ
PASS khi đồng thời:
- GEN2 terminal PASS + write-amplification report;
- Hermes MANUAL signal end-to-end PASS hoặc, nếu capability cross-task bị server scope chặn, cơ chế self-scope known-good PASS + blocker được chứng minh mà không mở quyền;
- DROOT29 / Điều 30/31 protection coverage PASS;
- no AUTO, no agent-data/claude-mcp restart, no credential mutation, no unrelated delta.

Ghi:
`KQ@MCPW-GEN2-HERMES-PROTECT-20260929-01 XONG|DỪNG`
vào MCPW COLLAB; nêu machine state, Hermes root cause/live acceptance, protection targets, guard tests, rollback.

Nếu XONG: dừng phiên. NEXT = VPSUP SEC-CRED theo READY hiện hành; Pha B chỉ sau SEC-CRED PASS để tránh chồng agent-data/credential.

## 9. MacBook
Không có soak dài trong RUN này. Nếu cần theo dõi >15′, bàn giao cho timer/Guard/Kuma VPS theo DROOT28 rồi Agent dừng.