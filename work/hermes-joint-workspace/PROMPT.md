# PROMPT — HJW CONTROL B · Manual dispatch + Telegram visibility + Owner STOP

RUN_ID: HJW-CONTROL-B-20260926-04
STATUS: Chỉ thực thi sau READY/RUN mới của Host.
Host: GPT Chat · GPT-HJW-260922-A
Executor_Surface: Claude Code CLI phiên mới trên Mac Owner.
Report_Write_Path: gateway `workspace_*`/`fs_*`; chỉ file HJW hiện hữu.
Runtime_Write_Path: SSH/operator VPS hiện hữu; mã/runtime VPS là SSOT.

Căn cứ: Owner clarification 26/09 + Claude P48; P45 KQ CONTROL-A XONG; P37–P45; MCPW N1–N7; Điều 30/31; DROOT22.
Host ruling: CONTROL-C/P46 bị supersede — không cắt/sandbox toolset chat Hermes. Công tắc là cơ chế vận hành human-in-the-loop để kiểm soát đường GIAO VIỆC trong giai đoạn thử, không phải hàng rào chống Hermes.
JEV Host `gen-dec-1790398502-Bsc2dxHB7DnLbLdgkL6h`: P48 = 1,00; root STOP + visibility = 0,91; residual fake-click có thể chấp nhận cho bounded trial = 0,67 với các guard dưới đây.

## 0. Đích

Giữ Hermes là thành viên đầy đủ:
- KHÔNG giảm toolset/backend của Telegram/Desktop Owner chat.
- KHÔNG bỏ terminal/file/code/cronjob chỉ để bảo vệ gate.
- KHÔNG thay Agent Gateway 7-tool contract/scope trong RUN này.

Lắp đường điều khiển thử nghiệm:
1. hệ thống tự phát hiện việc nhưng MANUAL mặc định;
2. trước mỗi auto-run cần thẻ Telegram `Cho chạy`;
3. sau click, trước model call phải Telegram `BẮT ĐẦU`;
4. kết thúc phải Telegram `KẾT QUẢ`;
5. mọi commit có trusted actor `agent-gw/hermes` phải được báo Telegram bằng logic tất định;
6. Owner có nút `Dừng tất cả`; STOP thật do root áp và uid `hermes` không tự gỡ;
7. control-plane drift/đường chạy ngoài luồng phải báo ≤5 phút;
8. AUTO production allowlist vẫn RỖNG; không tự nâng tự động.

**Giới hạn được chấp nhận cho giai đoạn thử:** nút `Cho chạy` là operational human gate, CHƯA phải cryptographic/security boundary chống một interactive Hermes session tự giả marker. Bù bằng START-before-model + root STOP + drift/commit visibility. Không được mô tả nó là tamper-proof.

## 1. Reuse, không làm lại

Reuse:
- G0 `/opt/incomex/work/hermes-joint-workspace/HJW-CONTROL-20260926-01/G0.md`;
- Pha A `.../phaseA/EVIDENCE-A.md`;
- production hiện tại: `ws-dispatch.no_agent=true`, `ONE_SHOT_ENABLED=False`, NOTEPAD_SAFE, plugin official fixture 16/16.

Chỉ revalidate:
- Hermes version/source baseline P45; nếu safe-update đã áp bản mới thì rerun fixture A2/A4/A5 + plugin fixture trước mutation;
- Guard/Kuma/P02/Agent Data/Hermes 7 tool healthy;
- 0 ASSIGN Hermes open/claimed;
- no_agent + one-shot hard-disabled còn đúng.

Không chạy `hermes-safe-update apply --reviewed` trong RUN.

## 2. PRE / rollback

PRE:
- snapshot/hash config/script/plugin/job/root-cron liên quan;
- baseline toolsets/chat capabilities; Telegram/clarify/exec approval; STOP/Kuma;
- baseline Git actor/commit cursor để kiểm notifier;
- config-guard + MCPW Guard.

Rollback phải chuẩn bị trước mutation:
- bật root STOP-DISPATCH;
- disable/remove HJW control plugin/config delta;
- trả script/root-cron/job config;
- restart tối thiểu đúng service nếu cần;
- **không** tự resume one-shot/auto dispatch sau rollback; giữ MANUAL+STOP tới Host quyết.
- lifecycle/notepad/evidence giữ nguyên để reconcile, không xóa lịch sử.

## 3. Plugin live — official extension, không core patch

Dùng official `~/.hermes/plugins/` + `register_telegram_handler` đã PASS fixture:
- một plugin HJW control tối thiểu; không patch upstream/core;
- callback prefix riêng `hjw:`, không chiếm `ea:`/clarify/core handlers;
- callback_data chỉ ticket id ngắn ≤64 bytes;
- đúng Owner user/chat mới được ghi APPROVED/DENIED;
- thẻ có `Cho chạy`, `Không chạy`, `Xem việc`, và `Dừng tất cả`;
- dùng chính bot/consumer hiện hữu, không getUpdates/bot/token/route thứ hai.

Plugin không được trực tiếp gọi model. Nó chỉ ghi lifecycle event/outbox/stop-request bằng primitive đã kiểm P45.

Cài/bật qua extension/config chính thức. Restart nếu bắt buộc: **chỉ `hermes-gateway` một lần**, theo block VPS nguyên khối đã dùng ở P02: checkpoint → restart → health → rollback nếu fail. Không restart serve/nginx/Agent Data nếu không causal.

## 4. Lifecycle + manual dispatch

Dùng đúng notepad scheme P45:
- key rời `t:` ticket / `ok:` approved / `no:` denied / `out:` outbox;
- generation + task hash + scope + expiry;
- consume approval bằng `delete_note` rowcount: 1 thắng, 0 thua;
- expiry/replay/duplicate/out-of-order không chạy;
- outbox có sequence; thẻ hết hạn phải bị bỏ trước khi gửi;
- cap/TTL theo P39: 24h, tối đa 10 thẻ mới/ngày giờ VN; gom tin nhưng vé độc lập.

**ONE_SHOT_ENABLED chỉ được bật sau toàn bộ negative test trước-trial PASS.**
One-shot:
- đúng một job `--repeat 1`;
- toolset = `incomex-workspace` 7 tool, không terminal/server-write;
- assignment/scope/READY/generation revalidate ngay trước claim;
- không claim/lease trong lúc pending approval;
- AUTO allowlist rỗng.

Không có ticket approved hợp lệ => `ws-dispatch no_agent` 0 model call.

## 5. Telegram visibility — 3 lớp

### 5.1 Thẻ chờ duyệt
Trước model:
- task/assignment;
- Hermes sẽ làm gì;
- lý do cần AI;
- read/write scope;
- output dự kiến;
- link task;
- nút Cho chạy / Không chạy / Xem việc / Dừng tất cả.

Pending = 0 model call.

### 5.2 START trước model call
Sau khi consume APPROVED nhưng **trước khi tạo/model-run**:
`BẮT ĐẦU · <ticket> · <task> · Owner bấm <timestamp> · scope=<...>`

START gửi thất bại => không model call; giữ ticket trạng thái phù hợp và báo/retry deterministic, không chạy âm thầm.

### 5.3 RESULT
Sau run:
- Hermes đã làm gì;
- kết quả / NO_NEW_VALUE / blocker;
- report/commit thật;
- duration;
- provider usage/cost thật hoặc UNKNOWN;
- NEXT actor.

Không dùng model self-claim làm bằng chứng; lấy ledger/Git/report.

## 6. Báo mọi commit Hermes — deterministic

Tái dùng root cron/monitor hiện hữu, không LLM:
- theo dõi Git commits mới có trusted gateway actor `agent-gw/hermes` trên workspace;
- mỗi commit chưa seen phải gửi Telegram: task/path, short SHA, commit summary, execution/ticket nếu map được;
- cursor bền để restart không bỏ commit và không báo lặp;
- nếu RESULT đã chứa cùng commit, được dedup thành một delivery nhưng ledger phải chứng minh commit đã được surfaced;
- commit Hermes không map được ticket/assignment => cảnh báo `HERMES_COMMIT_OUTSIDE_TRACKED_RUN`.

Không log secret/content; metadata only.

## 7. Dừng tất cả — Owner operational kill switch

Root-owned STOP hiện hữu là chốt thật:
- chứng minh uid `hermes` không write/delete/rename/replace được STOP.
- plugin callback `Dừng tất cả` chỉ ghi **stop-request**; root cron hiện hữu đọc ở tick kế và bật STOP root-owned.
- stop-request giả là fail-safe: chỉ có thể dừng thêm, không chạy thêm.
- khi STOP ON: ws-dispatch, webhook-triggered dispatch và one-shot creation đều 0 run mới.
- Hermes không tự gỡ STOP.

**Không có nút Resume trong Hermes plugin.**
Mở lại chỉ qua một đường Owner/Host không do uid `hermes` quyết định (repo/Host/Claude Code path hiện hữu), có audit. Không dựng service mới.

Test STOP từ Telegram fixture + live một lần trước trial; thời gian click→STOP ghi thật. Mục tiêu ≤5 phút, ưu tiên tick hiện hữu nhanh hơn.

## 8. Drift + ngoài luồng ≤5 phút

Mở rộng đúng root cron/Protection/Kuma path hiện hữu, không service mới. Mỗi ≤5 phút kiểm:
- `ws-dispatch.no_agent`;
- `ONE_SHOT_ENABLED`;
- plugin enabled/hash;
- `platform_toolsets` / one-shot toolset;
- số job agent bất thường;
- STOP state;
- lifecycle approvals không có click receipt tương ứng;
- Hermes source/version drift;
- commit Hermes ngoài tracked run.

Lệch => Telegram một lần/condition + Kuma state phù hợp; không tự gọi LLM.
Không autofix trừ STOP fail-safe đã chốt; còn lại alert + giữ MANUAL/STOP.

## 9. P40 checkpoint sau CLI

Root hook hiện hữu phải ghi redacted checkpoint vào hồ sơ HJW:
- ticket/execution id;
- model calls before/after approval;
- approval/start/result Telegram message_id + delivery/receipt status;
- report commit;
- duration;
- provider usage/cost hoặc UNKNOWN;
- STOP/drift state.

Sau khi Claude Code CLI kết thúc ở WAIT_OWNER_CLICK, VPS vẫn nhận click và tự chạy/ghi TRIAL; Owner không phải mở lại terminal.

Repo public chỉ summary; gate/repro chi tiết ở hồ sơ VPS root-only.

## 10. Acceptance B1–B15

B1. Existing Hermes Owner chat toolset/backend **không giảm**.
B2. Idle/pending/denied/expired/invalid => 0 model calls.
B3. Valid Owner click exactly once => exactly one one-shot/run.
B4. Duplicate/replay/wrong user/wrong chat/stale generation/changed task => 0 run.
B5. START Telegram đã có receipt trước model call; START fail => 0 model.
B6. RESULT maps to real report/commit and usage evidence.
B7. Every new `agent-gw/hermes` commit in fixture/live trial is surfaced/deduped without loss.
B8. STOP button causes root STOP; uid hermes cannot clear; STOP blocks all new dispatch.
B9. Control-plane drift fixture triggers alert ≤5 min; no LLM.
B10. Cron/webhook/manual trigger all converge through MANUAL gate; AUTO allowlist empty.
B11. Plugin callback does not break normal chat/clarify/exec approval.
B12. Restart/recovery does not duplicate ticket/run/commit notification.
B13. Guard/config-guard/P02/Agent Gateway 7-tool/auth/scope/Kuma no regression.
B14. Rollback returns plugin/config/scripts clean and leaves auto dispatch stopped.
B15. One real bounded Hermes trial after Owner click returns useful new result or honest NO_NEW_VALUE, with START/RESULT/commit/checkpoint evidence.

## 11. Trial

Chỉ sau B1–B14 PASS:
- materialize một bounded HJW review question chưa có đáp án;
- send exactly one approval card;
- checkpoint `WAIT_OWNER_CLICK`;
- Owner bấm `Cho chạy`;
- system continues without terminal;
- trial Hermes chỉ dùng 7 workspace tools, không runtime mutation;
- report mức cao, không ghi exploit reproduction vào public repo.

Nếu không có câu hỏi mới đủ giá trị => `TRIAL_NOT_READY`, không đốt token thay bằng tóm tắt cũ.

## 12. KQ

Trước click: không KQ XONG.
Sau B1–B15:
`KQ@HJW-CONTROL-B-20260926-04 XONG`

Blocker/rollback:
`KQ@HJW-CONTROL-B-20260926-04 DỪNG`

Ghi HJW COLLAB + view.html hiện hữu; chi tiết nhạy cảm chỉ hồ sơ VPS.

Sau B XONG:
- Host nghiệm thu;
- HJW.4 promote phần luật còn thiếu;
- HJW.5 đối chiếu T1–T10/closeout;
- sau đó quay lại MCPW identity/lifecycle/scoped lease/NEXT.
