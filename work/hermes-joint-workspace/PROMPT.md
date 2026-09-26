# PROMPT — HJW CONTROL A · Fail-closed dispatcher + lifecycle proof

RUN_ID: HJW-CONTROL-A-20260926-02
STATUS: Chỉ thực thi sau READY/RUN mới của Host.
Host: GPT Chat · GPT-HJW-260922-A
Executor_Surface: Claude Code CLI phiên mới trên Mac Owner.
Report_Write_Path: gateway `workspace_*` root `workspace` hoặc `fs_*` root `gh`; chỉ file hiện hữu HJW.
Runtime_Write_Path: SSH/operator VPS hiện hữu; mã/runtime VPS là SSOT.
Căn cứ: P41 G0 NO-GO + hồ sơ root-only `/opt/incomex/work/hermes-joint-workspace/HJW-CONTROL-20260926-01/G0.md`; P37–P40; MCPW N1–N7; Điều 30/31; DROOT22.
Quyết định Host: nhận hướng D1–D5 nhưng chia hai pha. Pha A này chỉ D1–D3 + kiểm cách ly. D4–D5, plugin live/restart và thẻ Telegram thật thuộc RUN sau nếu Pha A PASS.
JEV tham khảo: `gen-dec-1790385908-Rsodv75goyjydXGCNiUO` — ưu tiên tách pha B 0,71; D2/D3/D4/D5 riêng lẻ vẫn nghiêng phù hợp.

## 0. Đích / nguyên tắc

Pha A phải chứng minh ba thứ trước khi chạm activation:
1. `ws-dispatch` không còn đường fail-open gọi LLM trước approval;
2. có thể dùng đúng MỘT lifecycle store hiện hữu mà không mất cập nhật/chạy đôi;
3. official Hermes plugin API đủ để làm nút/callback Owner trên bot hiện hữu mà không vá lõi.

Giữ production MANUAL, AUTO allowlist rỗng. Không phát ASSIGN Hermes open trong RUN này. Không gọi model Hermes. Không gửi thẻ approval production. Không update Hermes dù safe-update báo có bản mới; không chạy `hermes-safe-update apply --reviewed`.

Không làm lại audit G0: đọc `G0.md` + checkpoint và chỉ revalidate hash/version/path có liên quan. Nếu source/config liên quan đổi từ P41 thì đọc đúng delta; không quét lại toàn hệ.

## 1. PRE / protection

Trước mutation:
- đọc AGENTS → root COLLAB → HJW §0 + P41 → PROMPT này;
- kiểm READY exact, source_head/freshness;
- xác nhận không có Hermes assignment `state=open`/claimed đang chạy;
- xác nhận MCPW Guard UP, Agent Data healthy, Hermes 7 tool/auth/scope/attribution, STOP/Kuma/Telegram hiện hữu;
- ghi baseline source/config/StartedAt + tập mã test lỗi baseline, không chỉ số đếm;
- append checkpoint PRE vào hồ sơ HJW hiện hữu. Không ghi secret.

PRE fail hoặc có mutation HJW khác chen ngang => DỪNG trước thay đổi.

## 2. D1 — ws-dispatch fail-closed bằng no_agent

Mục tiêu: workspace trigger/webhook/backstop chỉ chạy logic tất định; không có assignment APPROVED hợp lệ thì 0 model call ngay cả khi script lỗi.

- Reuse đúng job `ws-dispatch`, giữ identity/schedule/route/backstop; chuyển sang cơ chế `no_agent` hiện hữu.
- Không tạo scheduler/job nền thứ hai.
- Lưu đủ cấu hình cũ trong hồ sơ/rollback hiện hữu; không in secret.
- Logic no_agent chỉ được tạo một one-shot agent job sau khi đọc lifecycle record APPROVED hợp lệ. Trong Pha A không có APPROVED production nên không được tạo one-shot thật.
- Fault-injection cách ly: timeout, exception, non-zero, malformed output, missing STOP/read error/network error => 0 model call, không tạo one-shot.
- Chứng minh webhook/tick/manual `hermes cron run` đều hội tụ vào cùng no_agent gate và không còn pre-script fail-open dẫn tới model.

Nếu D1 làm mất handoff-watch/run-watch/Kuma/Telegram deterministic jobs khác => rollback D1 và DỪNG.

## 3. D3 — một lifecycle store; notepad chỉ dùng nếu chứng minh không race

Ứng viên ưu tiên là notepad hiện hữu của `ws-dispatch`, nhưng P41 đã xác nhận không có CAS. Vì vậy KHÔNG mặc định chấp nhận.

Phải inventory primitive thật: read/write/delete/append/lock/serialization, process nào ghi, giới hạn 64 KB, crash semantics. Sau đó chọn đúng một trong hai kết luận:

### A. NOTEPAD_SAFE
Chỉ nếu chứng minh bằng test cách ly rằng không mất update/duplicate với callback decision + dispatcher tick chen nhau. Ưu tiên single-writer:
- callback/ingress chỉ ghi event/decision tối thiểu bằng primitive an toàn;
- `ws-dispatch` no_agent là writer duy nhất chuyển lifecycle state;
- generation + ticket id + content/scope hash + expiry chống replay;
- duplicate/out-of-order không chạy hai lần;
- crash/restart đọc lại được;
- không store thứ hai.

### B. NOTEPAD_UNSAFE
Nếu primitive không đủ để chứng minh, DỪNG trước cài plugin/live trial và báo đúng lỗ. Đề xuất lựa chọn nhỏ nhất từ store HIỆN HỮU đã audit (executions/task store) nhưng không triển khai trong RUN này. Không tự tạo DB/file ledger/daemon mới.

Test tối thiểu: 2 callback đồng thời, callback chen tick, tick chen expiry, duplicate/replay, restart giữa write; phải đối soát 0 lost update và tối đa một transition APPROVED→CLAIMABLE.

## 4. D2 — prove official plugin path, KHÔNG activate

- Reuse official plugin extension `~/.hermes/plugins/` + `register_telegram_handler` đã thấy ở P41.
- Không sửa core/upstream Hermes.
- Pha A KHÔNG cài/bật plugin production, KHÔNG restart gateway.
- Chứng minh bằng fixture/in-memory harness hoặc cơ chế cách ly hiện hữu rằng plugin tối thiểu có thể:
  - đăng ký prefix callback riêng `hjw:`;
  - ghim đúng Owner user_id/chat_id từ config hiện hữu;
  - callback_data chỉ mang ticket id ngắn <=64 byte, chi tiết tra lifecycle store;
  - gửi card approval + START + RESULT qua chính bot/consumer hiện hữu;
  - không gọi model khi nhận callback;
  - duplicate/sai người/hết hạn/hash-generation sai => từ chối;
  - không chiếm clarify/exec approval callback hiện hữu.
- Không in token, secret, raw callback payload nhạy cảm.
- Source thử chi tiết/gate/repro chỉ ở hồ sơ VPS root-only; repo chỉ tóm tắt mức cao.

Nếu official extension không đủ và cần patch core => `PLUGIN_CORE_PATCH_REQUIRED`, DỪNG. Không viết/apply patch core.

## 5. P40 hậu click — chỉ thiết kế interface ở Pha A

Pha A chưa chạy trial. Chỉ phải chốt interface để Pha B dùng:
- runner/root hook sẽ đọc lifecycle + execution result và ghi checkpoint TRIAL đã redact vào hồ sơ HJW;
- fields: ticket/execution id, model-call count before/after, Telegram message_id + receipt status, provider usage/cost hoặc UNKNOWN, report commit/status;
- repo public chỉ ghi summary, không repro exploit/gate detail.

D4 implementation + Kuma #21 và D5 enable/restart để Pha B.

## 6. Acceptance A1–A8

A1. PRE PASS, diff ngoài scope = 0.
A2. `ws-dispatch` production ở no_agent; 0 model call trong idle và toàn bộ fault fixture.
A3. Không approved ticket production, không one-shot agent job thật được tạo.
A4. Lifecycle store có bằng chứng chống lost-update/duplicate; nếu không thì KQ DỪNG rõ NOTEPAD_UNSAFE.
A5. Plugin official path đủ cho button/callback/start/result ở fixture; không core patch, không production activation.
A6. Existing Telegram normal chat/clarify/exec approval, STOP, webhook, handoff/run-watch, Kuma và Hermes 7-tool contract không regression.
A7. MCP/P02 Guard + config-guard giữ PASS; test regression so theo tập mã lỗi.
A8. Rollback D1 đã thử/có thể phục hồi chính xác; không đổi model/key/scope/nginx/Agent Data/P02; không restart Hermes trong Pha A.

## 7. KQ / next

Ghi CHÍNH HJW COLLAB + view.html hiện hữu, qua gateway:
- capability table D1/D2/D3;
- exact status `NOTEPAD_SAFE|NOTEPAD_UNSAFE`;
- A1–A8;
- runtime delta thật;
- rollback;
- phần chi tiết nhạy cảm chỉ trỏ hồ sơ VPS.

PASS => `KQ@HJW-CONTROL-A-20260926-02 XONG`, Host mới soạn Pha B D4–D5 + activation + một thẻ thật.
FAIL/blocker => `KQ@HJW-CONTROL-A-20260926-02 DỪNG`, không tự mở Pha B.

Không tạo task/project/repo file mới. Không update Hermes. Không phát assignment Hermes. Không gửi approval card production. Không restart Hermes/nginx/Agent Data.
