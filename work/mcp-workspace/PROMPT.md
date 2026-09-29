# PROMPT — MCPW HERMES TELEGRAM RECOVERY · restart-only + manual smoke

RUN_ID: MCPW-HERMES-TG-RECOVER-20260929-01
Host: GPT Chat · GPT-MCPW-250925-A
Executor_Surface: Claude Code CLI trên Mac Owner.
Report_Write_Path: KQ chính ở `work/mcp-workspace/COLLAB.md`; smoke Hermes dùng `work/hermes-joint-workspace/COLLAB.md`.
Runtime: VPS1 production.

## 0. Mục tiêu duy nhất

Kế thừa KQ `645518320c9b59965a0f57b8cf2cf041df6aeeb3`:
- **GEN2 GitHub = PASS**: 24/24 xanh, alert-only tiếp tục;
- **Điều 30/31 = PASS**: gate read-only cross-task + Config Guard 48/48 + mutant/watchdog/rollback đã đạt;
- phần duy nhất chưa đạt = `hermes-gateway` gửi Telegram lỗi `NetworkError`, nên MANUAL smoke chưa hoàn thành.

RUN này chỉ:
1. xác minh lỗi outbound Telegram hiện hành;
2. restart **chỉ `hermes-gateway`** theo thủ tục đã chứng minh ở HJW P61;
3. kiểm health/Config Guard;
4. giao lại một MANUAL smoke đúng contract và kết thúc nếu PASS.

Không chạy lại GEN2. Không sửa lại Điều 30/31. Không mở Pha B/C.

## 1. Read/collision gate

Đọc:
AGENTS → root COLLAB DROOT22/25/28/29/30/31 → MCPW COLLAB P47–P50 + KQ commit `6455183` → HJW COLLAB dòng hướng dẫn đầu file + P52/P61–P64 → PROMPT này.

**Cổng task COLLAB trước READY/RUN:** Host chỉ phát READY khi `work/mcp-workspace/COLLAB.md` ghi được qua gateway đã duyệt; `STARTED` và KQ phải ghi tại chính task COLLAB này, root COLLAB không thay thế.

Ngay sau read-gate PASS và **trước PRE**, executor phải ghi:
`STARTED@MCPW-HERMES-TG-RECOVER-20260929-01 <UTC> · executor=Claude Code CLI`
vào `work/mcp-workspace/COLLAB.md`. Nếu không ghi được ⇒ DỪNG trước PRE/mutation.

Kiểm `work/vps1-up-grade`:
- SEC-CRED đã có KQ terminal; technical rotation đã xong nhưng §8A protection/rebaseline còn HOLD;
- nếu có **active runtime mutation mới** trên Hermes/Guard/agent-data/claude-mcp/GSM/credential ⇒ DỪNG trước restart;
- repo/version conflict thuần túy ⇒ re-read/diff/retry, không overwrite.

PRE:
- `hermes-gateway` MainPID/start time/health;
- HJW gate/plugin/root hashes, STOP, AUTO_ALLOWLIST, jobs relevant;
- Config Guard registry/hash hiện hành;
- sanitized log từ thời điểm Telegram bắt đầu lỗi (~06:04Z 29/09): exception class/chain, không token/chat secret;
- xác minh host vẫn có network/TLS/DNS reachability tới Telegram bằng đường read-only/probe hiện hữu, không in token.

## 2. Scope / hard stops

Được:
- đọc log/state/evidence;
- restart **chỉ `hermes-gateway`**;
- tạo một ASSIGN smoke mới trong HJW COLLAB sau khi outbound Telegram đã phục hồi;
- repo write KQ/ASSIGN theo gateway đã duyệt.

Cấm:
- sửa code/config trước restart;
- restart `hermes-serve`, nginx, agent-data, claude-mcp, Directus, Nuxt;
- sửa/rotate credential/GSM/token;
- rebaseline P02/AD1 trong RUN này;
- bật AUTO / thêm AUTO_ALLOWLIST;
- mở write scope/tool/profile;
- sửa Config Guard registry/baseline nếu không có code/config delta;
- Pha B/C.

Nếu restart-only không chữa lỗi ⇒ DỪNG với evidence, không tự chuyển thành code-fix RUN.

## 3. Xác minh nguyên nhân trước restart

Đối chiếu KQ trước:
- card trước đó đã từng gửi được + callback Owner được ghi nhận;
- từ khoảng 06:04Z outbound send của gateway lỗi `NetworkError`;
- START retry/send sau đó lỗi; 0 model call;
- host/network path không có bằng chứng bị firewall chặn.

Trước restart phải xác minh:
- config/plugin/gate hashes không drift khỏi known-good/P61 hoặc baseline D30/31 hiện hành;
- STOP/AUTO đúng trạng thái;
- lỗi tập trung ở process/gateway outbound path, không phải credential rotation Agent Data.

Nếu thấy config/token Telegram bị đổi/mất/expired hoặc drift ngoài dự kiến ⇒ DỪNG, không restart để che lỗi.

## 4. Restart-only

Trước restart, so MainPID/StartedAt `hermes-gateway` với mốc KQ `6455183`:
- nếu gateway **đã tự khởi động lại sau KQ `6455183`** ⇒ **KHÔNG restart thêm**; ghi `AUTO_RESTART_ALREADY_OCCURRED`, kiểm health/hash/Config Guard rồi chuyển thẳng §5 Telegram TEST;
- chỉ restart nếu vẫn là process cũ và toàn bộ PRE gate PASS.

Ngay trước first runtime mutation/restart, áp DROOT30: re-read `work/mcp-workspace/COLLAB.md` + `PROMPT.md`, xác nhận READY vẫn đúng commit last-touch và không có HOLD/STOP/READY mới; lệch ⇒ DỪNG trước mutation.

Nếu cần restart, dùng đúng thủ tục restart `hermes-gateway` đã chạy thành công ở HJW P61:
1. ghi checkpoint PRE + rollback/reference;
2. restart đúng **một** service/process `hermes-gateway`;
3. chờ health trở lại trong cửa sổ đã chứng minh (xấp xỉ vài chục giây; không tight-loop);
4. xác minh PID/StartedAt mới, health PASS;
5. gate/plugin/root/config bytes/hash không đổi;
6. Config Guard registry/invariants vẫn CLEAN.

Do outbound Telegram đang lỗi, không yêu cầu “gửi Telegram trước restart”. Owner đã trực tiếp yêu cầu tiếp tục và Host đã cấp RUN này. Không dùng việc Telegram hỏng để mở thêm quyền.

Không restart lần hai nếu lần đầu không chữa được; lúc đó chuyển §7 DỪNG.

## 5. Post-restart Telegram check

Trước gọi model:
- dùng deterministic send path hiện hữu của gateway/plugin để gửi một tin TEST rõ nhãn `HJW · TG RECOVERY TEST`;
- xác minh send receipt/message_id;
- nếu send lỗi ⇒ §7 DỪNG;
- xác minh gateway vẫn nhận callback/update path bình thường.

Kuma:
- #21/control-plane phải healthy;
- #22/P02 nếu đang đỏ do **SEC-CRED expected baseline change pending VPSUP §8A** thì ghi `EXPECTED_PENDING_REBASELINE`, **không rebaseline tại đây** và không tính là lỗi Hermes.

## 6. MANUAL smoke mới

Chỉ sau §5 PASS.

Ngay trước tạo ASSIGN, lặp DROOT30 freshness gate sau mọi thời gian chờ/Owner interaction: re-read task COLLAB + PROMPT, READY phải vẫn đúng last-touch và không có HOLD/STOP/READY mới; lệch ⇒ DỪNG trước ASSIGN.

Tạo assignment mới, không reuse vé/card cũ:
`ASSIGN@HJW-MANUAL-SMOKE-20260929-03 · to=Hermes · role=Reviewer · scope=work/hermes-joint-workspace · state=open`

Câu giao phải:
- ghi `MCP root=workspace`;
- chỉ rõ **đường dẫn đầy đủ** `work/mcp-workspace/COLLAB.md`;
- yêu cầu tìm marker duy nhất `MCPW-GEN2-HERMES-PROTECT-20260929-01`;
- cấm dò/đoán root;
- chỉ đọc MCPW, chỉ ghi HJW.

Hermes phải:
- trước Owner click: 0 model;
- Telegram card CHỜ DUYỆT xuất hiện;
- Owner bấm `Cho chạy`;
- callback ack + BẮT ĐẦU receipt gửi thành công;
- đúng 1 one-shot model;
- ghi trong HJW đúng 3 dòng:
  1. `HERMES_MANUAL_SMOKE=PASS|BLOCKED`
  2. `assignment=HJW-MANUAL-SMOKE-20260929-03 actor=<server-auth identity>`
  3. `marker=MCPW-GEN2-HERMES-PROTECT-20260929-01 limitation=<none|...>`
- đổi ASSIGN open→done trong cùng một commit `[Hermes] ASSIGN@HJW-MANUAL-SMOKE-20260929-03`;
- Telegram RESULT = XONG suy từ Git/sổ.

Acceptance:
- đúng 1 model;
- đúng 1 commit Hermes trong HJW;
- 0 commit ngoài HJW;
- AUTO vẫn rỗng;
- no runtime mutation ngoài gateway restart;
- marker bắt buộc đúng, thiếu = BLOCKED.

## 7. Nếu Telegram vẫn lỗi

DỪNG. Không sửa code. Không restart lần 2.

Phân loại đúng đường lỗi:
- deterministic TEST ở §5 **không gửi được** ⇒ ghi `KQ@MCPW-HERMES-TG-RECOVER-20260929-01 DỪNG · TELEGRAM_NETWORKERROR_PERSISTS`;
- deterministic TEST **PASS**, nhưng sau Owner click thì tin `BẮT ĐẦU` lỗi ⇒ ghi `KQ@MCPW-HERMES-TG-RECOVER-20260929-01 DỪNG · TELEGRAM_START_PATH_DEFECT`; giữ fail-closed, không code-fix trong RUN này.

Lưu sanitized evidence:
- exception type + cause chain;
- timestamp;
- PID/start time trước/sau;
- DNS/TLS/network probe;
- send endpoint class/path (không token);
- HTTP client/session state nếu đọc được an toàn;
- gateway health;
- config/hash unchanged;
- riêng `TELEGRAM_START_PATH_DEFECT`: lưu exact evidence của START path và xác nhận TEST path ngay trước đó PASS.

Host sẽ mở RUN code-fix riêng sau khi có root cause.

## 8. Điều 30/31 trong RUN này

Không có code/config delta dự kiến ⇒ **không rebaseline**.
Chỉ verify:
- Config Guard/registry vẫn CLEAN sau restart;
- 13 target AD1/HJW + registry self-protection vẫn được bao phủ;
- watchdog vẫn sống.

Nếu phát sinh nhu cầu sửa code/config ⇒ DỪNG, không mở scope; sửa phải sang RUN mới và áp DROOT29 đầy đủ.

## 9. KQ / NEXT

PASS khi:
- restart-only health PASS;
- outbound Telegram send phục hồi;
- MANUAL smoke end-to-end PASS;
- Config Guard CLEAN, AUTO rỗng, ngoài-scope=0.

Ghi:
`KQ@MCPW-HERMES-TG-RECOVER-20260929-01 XONG`

Sau XONG:
1. dừng phiên;
2. NEXT = VPSUP §8A protection/rebaseline-only để khép SEC-CRED;
3. rồi MCPW Pha B → C.

Không tự chạy NEXT trong cùng phiên.

## 10. Mac/clients

Không có soak dài. Nếu Owner chưa restart Claude Desktop/Claude Code/Codex sau SEC-CRED key rotation, chỉ nhắc trong KQ; không tự sửa config ngoài scope.