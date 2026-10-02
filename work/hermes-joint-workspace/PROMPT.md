# PROMPT — HJW MAINT · client/backend session.create compatibility + Điều 30/31

RUN_ID: HJW-MAINT-COMPAT-20261002-01
Host: GPT Chat · GPT-HJW-260922-A
Executor_Surface: Claude Code CLI phiên mới trên Mac Owner.
Runtime_Write_Path: SSH/operator VPS hiện hữu; không tạo service/task/file mới.
Report_Write_Path: chỉ `work/hermes-joint-workspace/{COLLAB.md,PROMPT.md}` qua gateway; evidence dùng hồ sơ VPS HJW hiện hữu.
Owner_authorization: 02/10/2026 — kiểm lại lỗi Hermes thực tế và đưa phần mới vào bảo vệ Điều 30/31.

## 0. Mục tiêu duy nhất

Sửa và khóa lỗi thực tế:
`invalid params for session.create: cwd_explicit: Extra inputs are not permitted — the client and the Hermes backend are out of sync (different versions)`.

Không thêm capability. Không bật AUTO. Không đổi Agent Data/P02/nginx/Nuxt/model/key/scope/toolset.

PASS chỉ khi **đúng client thật → đúng backend thật** tạo được session; không chấp nhận chỉ service healthy hoặc unit test nội bộ.

## 1. Hard scope / ngân sách

- Trước mutation phải snapshot: binary/path/version/package/schema + unit ExecStart + MainPID/StartedAt của Hermes client/serve/gateway; Config Guard/Protection Guard current state; rollback.
- Không chạy blind `hermes update`.
- Tái dùng `hermes-safe-update` hiện hữu. Chỉ update/restart nếu D1 chứng minh version/schema/load-process lệch.
- Tối đa restart `hermes-serve` và `hermes-gateway` khi thực sự cần; không restart service khác.
- Không tạo service/timer/DB/monitor/file repo mới.
- AUTO_ALLOWLIST cuối RUN vẫn rỗng; manual Telegram gate/STOP giữ nguyên.
- Nếu cần vượt scope trên: DỪNG trước mutation, báo Host.

## 2. D1 — chẩn đoán thật, NO MUTATION

Đo và ghi evidence, không suy từ README:
1. Client thật đang phát `session.create`: executable/path, `--version`, package/source path, schema/request fields; xác nhận nơi sinh `cwd_explicit`.
2. `hermes-serve` + `hermes-gateway`: `systemctl show/cat` cho ExecStart/MainPID/StartedAt/EnvironmentFile (không in secret); cmdline/executable/package/source thực của process đang chạy.
3. Backend schema thật của `session.create`: request model/fields; xác nhận có/không `cwd_explicit`.
4. Phân loại đúng một root cause:
   - A: client package mới / backend package cũ;
   - B: package trên đĩa đã đồng bộ nhưng process backend chưa restart, đang giữ code cũ;
   - C: hai service dùng khác venv/binary/package;
   - D: lỗi khác — có evidence cụ thể.
5. Reproduce lỗi một lần bằng **đúng đường client Owner đang dùng**, rồi dừng; không lặp lỗi.

## 3. D2 — sửa tối thiểu, chỉ khi D1 đủ bằng chứng

- Nếu B: restart tối thiểu service đang giữ code cũ; không update package.
- Nếu A/C: dùng cơ chế `hermes-safe-update`/update hiện hữu để đồng bộ **cả hai đầu về cùng một bản đã xác định**, không cài song song venv/binary thứ hai; backup/rollback trước.
- Sau thay đổi: restart `hermes-serve` → verify, rồi `hermes-gateway` → verify; không dependency-bounce key services.
- Nếu safe-update/health fail: rollback về PRE, báo BLOCKED.
- Không in secret/token/env values.

## 4. Điều 30 — regression protection bắt buộc

Tái dùng test/harness hiện hữu; không tạo framework mới:
1. E2E thật: client Owner → `session.create` → backend PASS, bao gồm request có hành vi `cwd_explicit` đúng với version hiện hành.
2. Regression: gateway/manual Telegram gate, STOP, AUTO rỗng, Agent Gateway 7 tool và HJW control path vẫn PASS.
3. Negative fixture/mutant: mô phỏng client/backend schema lệch (ví dụ client có field mà backend không có) ⇒ test phải FAIL rõ ràng trước khi tuyên bố healthy.
4. Không chỉ test version string; phải test schema/handshake thật.

## 5. Điều 31 — integrity/self-detection bắt buộc

Bổ sung vào **Protection Guard/Config Guard hiện hữu**, không service mới:
1. Invariant `HERMES_CLIENT_BACKEND_COMPAT`: local/no GitHub/no LLM; kiểm executable/package identity + schema/handshake fingerprint của client↔serve/backend. Lệch hoặc backend không parse request chuẩn ⇒ FAIL.
2. Dùng 2-pass như invariant runtime hiện hữu để tránh flap nhưng không PASS giả.
3. Kiểm các unit/config/script/package-path thực dùng bởi serve/gateway đã nằm trong Config Guard; thiếu target nào trực tiếp quyết định version/schema thì đăng ký vào registry hiện hữu trong cùng RUN.
4. Mutant/fixture version-schema mismatch ⇒ invariant đỏ; clean ⇒ xanh.
5. Watchdog phải chứng minh invariant mới được chạy định kỳ; không tạo monitor mới nếu Protection Guard/Kuma hiện hữu đã bao phủ.

## 6. Rà toàn bộ phần mới vừa làm

Không mở task mới. Đối chiếu R6/MCPW đã đóng:
- lifecycle/receiver/workspace_tools/importer/presence/Owner View/Hermes config+gate/Protection Guard đã có protection ⇒ giữ nguyên, không làm lại;
- chỉ bổ sung thiếu hụt mới phát hiện là Hermes core client↔backend compatibility và đúng file/config/package-path liên quan.
Nếu phát hiện một thành phần mới khác **thực sự live nhưng chưa được Điều 30/31 bảo vệ**, liệt kê + đưa vào guard/test hiện hữu trong scope; không dựng cơ chế mới.

## 7. Acceptance

PASS khi đồng thời:
- lỗi `cwd_explicit` không reproduce trên đúng client thật;
- client/serve/gateway cùng identity/version/schema phù hợp;
- real `session.create` PASS;
- `hermes-safe-update health` (nếu dùng) PASS;
- Config Guard CLEAN; Protection Guard PASS có invariant compatibility mới;
- mutant mismatch bị bắt;
- manual gate/STOP/AUTO rỗng/7-tool regression PASS;
- 0 scope creep, rollback có thật.

KQ:
`KQ@HJW-MAINT-COMPAT-20261002-01 XONG · HERMES_COMPAT_PROTECTED`
hoặc
`KQ@HJW-MAINT-COMPAT-20261002-01 BLOCKED · <root cause/evidence>`.

Sau KQ dừng; Host + Claude Reviewer nghiệm thu một lượt. Không tự mở việc tiếp.

---

# VÒNG TRƯỚC — PROMPT HJW FINAL (ĐÃ ĐÓNG, KHÔNG CHẠY LẠI)
# PROMPT — HJW FINAL · Telegram UX + closeout evidence

RUN_ID: HJW-FINAL-20260926-05
STATUS: Chỉ thực thi sau READY/RUN mới của Host.
Host: GPT Chat · GPT-HJW-260922-A
Executor_Surface: Claude Code CLI phiên mới trên Mac Owner.
Report_Write_Path: gateway workspace_*/fs_*; chỉ file HJW hiện hữu + view.html hiện hữu.
Runtime_Write_Path: SSH/operator VPS hiện hữu; runtime VPS là SSOT.

Căn cứ bắt buộc: HJW §0.3 S1–S9; P51 KQ CONTROL-B XONG; P52 + Host response P54; P54; Điều 30/31; DROOT22.
Mục tiêu: UX polish nhỏ nhưng thật → verify → closeout evidence HJW.4/HJW.5. Không mở lại kiến trúc CONTROL-B.

## 0. Ranh giới

Được:
- sửa plugin/config/script HJW CONTROL hiện hữu đúng phần UX Telegram và input-template;
- restart tối đa hermes-gateway nếu plugin không hot-reload, theo block an toàn/rollback;
- cập nhật HJW COLLAB + view.html hiện hữu;
- append evidence trong hồ sơ VPS HJW hiện hữu.

Không:
- không gọi Hermes model;
- không tạo assignment/trial mới;
- không bật AUTO; AUTO_ALLOWLIST cuối RUN vẫn rỗng;
- không update Hermes/safe-update;
- không đổi Agent Data/P02/nginx/Nuxt/model/key/scope/toolset;
- không tạo repo file/task/project mới;
- không sửa AGENTS.md trong RUN này (Claude Code không phải Founder). Chỉ đề xuất exact foundation delta cho Host/Founders ở COLLAB.

Reuse toàn bộ evidence P34/P45/P51; không chạy lại destructive/HARD-STOP/canary nếu không có regression causal.

## 1. PRE

Đọc AGENTS → root COLLAB → HJW §0 S1–S9 + Dòng hiện hành + P51/P52/P54 → PROMPT này.
Xác nhận:
- READY exact;
- 0 assignment Hermes open/claimed, 0 pending approval card có thể wake;
- CONTROL-B manual mode, AUTO rỗng;
- plugin/hjw_gate/root monitor hashes + gateway StartedAt;
- Guard/config-guard/P02/Agent Gateway 7 tool/Kuma healthy;
- Telegram callback current API/client/wrapper capability.

Snapshot plugin/config/scripts cần sửa + rollback trước mutation. Không in token/secret.

## 2. U1 — Header/nhiệm vụ nhất quán

Mọi tin HJW do control plane gửi phải theo cùng một grammar, nhìn vài giây hiểu được:

### Approval card
Header: `HJW · GIAO VIỆC · CHỜ DUYỆT`
- `Từ: <😊 Owner | 🤖 AI/máy giao> → Tới: 🤖 Hermes (<role>)`
- `Việc: <task readable>`
- `Nhiệm vụ: <1–2 dòng hành động cụ thể>`
- `Phạm vi: <read/write scope>`
- `Mã: <ticket> · ASSIGN <id>`
- `Tiếp theo: Owner chọn Cho chạy / Không chạy`
- link Xem việc.

### START
Header: `HJW · HERMES THỰC HIỆN · ĐANG CHẠY`
- `Từ: <😊 Owner | 🤖 AI/máy giao> → Tới: 🤖 Hermes (<role>)`
- ticket/task/scope;
- Owner approved_at;
- `Tiếp theo: Hermes làm → báo KẾT QUẢ`.

### RESULT
Header: `HJW · HERMES REPORT · <XONG|BLOCKED|NO_NEW_VALUE>`
- `Từ: 🤖 Hermes → Tới: <🤖 Host | 😊 Owner>`
- Đã làm;
- Kết quả;
- commit/report;
- duration + provider usage/cost hoặc UNKNOWN;
- `Tiếp theo: <actor/action>`.

### Commit notification
Header: `HJW · HERMES COMMIT · GHI NHẬN`
- `🤖 Hermes → Repo`
- task/ticket nếu map được;
- short SHA + summary;
- trạng thái execution;
- không lặp nếu RESULT đã surfaced cùng commit nhưng ledger phải đánh dấu surfaced.

Tên surface dùng bảng A9, không tự suy hãng/model sâu hơn evidence.

## 3. U2 — Click phải có phản hồi và đổi trạng thái

Ngay khi nhận callback hợp lệ:
1. gọi `answerCallbackQuery` ngay, text ngắn:
   - Cho chạy: `Đã nhận: Cho chạy`
   - Không chạy: `Đã nhận: Không chạy`
   - Dừng tất cả: `Đã nhận: Dừng tất cả`
2. sau khi lifecycle write thành công, edit **chính message** bằng editMessageText/editMessageReplyMarkup:
   - CHỜ DUYỆT → `✅ ĐÃ DUYỆT · <time>`;
   - hoặc `⛔ ĐÃ TỪ CHỐI · <time>`;
   - STOP → `🛑 ĐÃ YÊU CẦU DỪNG · <time>`, sau root receipt update thành `🛑 ĐÃ DỪNG · <time>`.
3. Ưu tiên biến action đã xử lý thành `disabled` nếu đường Bot API hiện hữu hỗ trợ sạch; nếu wrapper/runtime hiện tại không expose `disabled` thì **không coi là blocker**: thay nút vừa bấm bằng dòng trạng thái + giờ và gỡ action đối nghịch để không còn bấm được.
4. `Xem việc` và `Dừng tất cả` còn lại theo state hợp lệ.
5. duplicate/replay callback trả ack “Đã xử lý” và không đổi lifecycle lần hai.

Restart/plugin recovery phải render lại đúng state từ ledger, không quay về CHỜ DUYỆT giả.

## 4. U3 — Màu nút

Telegram Bot API hiện hành hỗ trợ InlineKeyboardButton.style:
- `success` xanh lá;
- `primary` xanh dương;
- `danger` đỏ.
Bot API hiện hành cũng có `disabled`, nhưng wrapper runtime có thể chưa expose trực tiếp; vì vậy `disabled` là tối ưu UX, không phải điều kiện chặn.

Áp:
- `Cho chạy` = success (xanh lá), hành động được khuyến nghị.
- `Xem việc` = primary (xanh dương).
- `Dừng tất cả` = danger (đỏ), chỉ dành cho stop/nguy hiểm.
- `Không chạy` = default/trung tính, không dùng đỏ để khỏi lẫn “Dừng tất cả”.
- cảnh báo = `⚠️` + text/default. Telegram không có style vàng chuẩn: KHÔNG giả vàng bằng hack.

Nếu wrapper hiện tại chưa expose `style` nhưng Bot API endpoint hiện hành có:
- ưu tiên raw Bot API/HTTP helper ĐANG CÓ trong plugin/runtime;
- không patch Hermes core, không bot/token/client thứ hai.
Nếu không làm được **màu style** bằng extension/helper hiện hữu ⇒ ghi limitation và DỪNG trước tuyên bố U3 PASS. Riêng thiếu `disabled` ở wrapper không làm RUN DỪNG; dùng fallback thay nút bằng trạng thái + giờ như §3.

Màu chỉ phụ trợ; text/icon/state phải đủ hiểu trên client không render style.

## 5. UX acceptance — không model call

Fixture + live bot API:
U1. Header 4 loại đúng grammar và from→to/next rõ.
U2. callback ack được gọi trước khi client hết progress; handler idempotent.
U3. click Cho chạy thử trong fixture → message edit thành ĐÃ DUYỆT + giờ; action đối nghịch không còn bấm được; `disabled` dùng nếu đường hiện hữu hỗ trợ, không bắt buộc.
U4. styles được Bot API nhận: success/primary/danger.
U5. STOP state edit đúng và không có Resume qua Hermes.
U6. Không chạy/default không lẫn màu đỏ STOP.
U7. callback duplicate/restart không hồi state.
U8. normal Hermes chat/clarify/exec approval không regression.
U9. 0 model call, AUTO rỗng, 0 assignment mới.
U10. Guard/config-guard/Kuma/7-tool/P02 PASS trước-sau.

Live verification không cần Owner click: được gửi một message UX fixture/private metadata-only rồi edit bằng chính Bot API để chứng minh API/render path; không tạo ticket executable, không model. Không spam quá 1 test message; sau test edit thành `HJW · UX TEST · PASS` hoặc xoá nếu cơ chế hiện hữu hỗ trợ an toàn.

## 6. S9 — Input/context contract

Sửa template one-shot hiện hữu để mọi assignment HJW tương lai tự chứa:
- `MCP root=workspace`;
- exact task path;
- exact read targets: AGENTS + HJW §0 + các P/KQ được giao;
- exact write path;
- cấm dò/đoán root; read root đầu fail ⇒ BLOCKED;
- ưu tiên workspace_search/read window; cấm đọc full HJW COLLAB nếu không cần.

Không tự đặt hard token cap. Ghi provider token/duration thật. AUTO vẫn OFF.
P52 threshold ≤150k chỉ là đề xuất Hermes và hiện **không đạt**; không encode nó thành gate production.

## 7. HJW.4 — foundation delta đề xuất, KHÔNG tự sửa AGENTS

Dựa evidence hiện có, ghi một khối ngắn `FOUNDATION_DELTA` vào HJW COLLAB để GPT/Claude Founders nghiệm thu:
- hội đồng 3 thành viên/attribution/mapping nếu phần nào đã có thì ghi “đã có — không sửa lại”;
- L1 AUTH PLACEHOLDER LAW: placeholder auth/secret không bao giờ được thành credential runtime; source thiếu ⇒ fail closed/unavailable/random unknown + negative test;
- L2 COST SOURCE LAW: số chi phí thật lấy provider ledger/API; agent estimate chỉ informational;
- S8 Telegram operational UX: header from→to, callback ack+edit state, success/primary/danger semantics, warning fallback;
- S9 explicit root/input contract cho unattended workspace job.
- **Capability truth source:** ma trận T1–T10 cuối trong HJW COLLAB là nguồn trạng thái chung về năng lực đã chứng minh. Mọi AI/Agent phải đọc ma trận này trước khi tự đánh giá `đang có gì/còn thiếu gì`; memory/skill chỉ là tham khảo và không được lấn bằng chứng mới hơn.

Không copy lịch sử dài vào AGENTS; đề xuất patch tối thiểu vào đúng mục hiện hữu.

## 8. HJW.5 — final evidence matrix

Lập T1–T10 cuối cùng trong HJW COLLAB từ evidence P34/P45/P51/P58 và spot-check hiện trạng. **Ma trận này sau closeout là nguồn sự thật chung về capability/readiness; mọi AI phải đọc trước khi tự đánh giá.**
- mỗi T: PASS/PARTIAL/NOT_RETESTED + evidence commit/path/time; phân biệt `đã chạy thật`, `đo live lượt này`, `đọc hồ sơ cũ`, `chưa từng thử`;
- không biến “7 tool” thành suy quyền ngoài scope;
- không rerun destructive tests/HARD-STOP/nginx/canary nếu không regression causal;
- **đính chính P58:** không ghi “Internet ingress chưa từng chạy” — P34 đã có public external test 21/21 từ Mac với V2 hợp lệ đi tới ws-dispatch. Không rerun; ghi evidence cũ + trạng thái vận hành thường ngày chưa có traffic webhook gần đây nếu cần;
- **đính chính P58:** không ghi “Telegram chưa có tin thật” — CONTROL-B đã có thẻ/tin thật, Owner click thật và receipt (#42–#49 theo P51). Không yêu cầu Owner gửi mẫu mới;
- **nhịp thật:** đo read-only lịch sử runs hiện tại và ghi interval/lateness thực tế; nếu ~3 phút thì ghi ~3 phút, không ghi thiết kế 2 phút. Không sửa cadence trong RUN này nếu vẫn ≤5 phút contract;
- **cost thật:** với 4 lượt model đã có trong usage audit, ưu tiên đọc provider-authoritative cost/usage từ dữ liệu response/log hiện hữu; nếu đã có generation id và có **đường read-only hiện hữu** tới OpenRouter accounting thì được đọc mà không in/expose key. Không tạo credential/helper mới, không hỏi Owner bảng giá, không tự nhân giá thủ công. Không lấy được ⇒ ghi `UNKNOWN/PARTIAL` theo L2, không bịa số;
- T10 ghi CONTROL-B end-to-end + residual fake-approval + MANUAL/AUTO rỗng + 0-token gate evidence; P52 loại việc review-read là ứng viên, chưa auto; actual token 293k invalid trial / 490k successful trial nên hiệu quả chưa đủ để AUTO;
- các mục P58 **không làm trong FINAL**: kênh trực tiếp GPT/Claude→Hermes (MCPW signal/dispatch), mở thêm toolset cho auto-run, quyền đọc ledger DB. Chỉ ghi NEXT đúng task, không triển khai.

Nuxt V8 heap restart chỉ ghi “OUT-OF-SCOPE OBSERVATION → VPSC”, không sửa.

## 9. KQ

KQ XONG chỉ khi:
- U1–U10 PASS;
- S9 template applied/tested fixture;
- CONTROL-B không regression;
- FOUNDATION_DELTA + T1–T10 matrix ghi xong và matrix có correction/nhịp/cost theo P58;
- AUTO_ALLOWLIST vẫn rỗng;
- rollback UX delta có sẵn;
- no new model call.

Ghi:
`KQ@HJW-FINAL-20260926-05 XONG`

Nếu blocker:
`KQ@HJW-FINAL-20260926-05 DỪNG`

Không move task sang done-tasks; Host sẽ nghiệm thu foundation delta rồi đóng HJW.
