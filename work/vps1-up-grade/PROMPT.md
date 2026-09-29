# PROMPT — VPSUP SEC-CRED-ROTATE · retire 2 credential production bị lộ trong KB

RUN_ID: VPSUP-SEC-CRED-ROTATE-20260929-01
STATUS: Chỉ thực thi sau khi COLLAB có READY đúng SHA commit cuối chạm file này và Owner/GPT Host phát RUN.
Host: GPT Chat · GPT-VPSUP-20260926-A
Executor_Surface: Claude Code CLI trên Mac Owner.
Report_Write_Path: **fs_* / Incomex VPS MCP · root gh → incomex-workspace/main**.
Runtime_Write_Path: VPS1 production theo DOT/GSM/config path đã duyệt; VPS2 clone chỉ đọc/checkpoint, không dựng TARGET.
Runtime VPS là SSOT.
Mọi Directus/PG mutation = **DOT-only**; không direct SQL fallback.

## 0. Mục tiêu duy nhất

G2 CURRENT parity đã PASS. Trước G3, retire an toàn đúng **2 credential production đang còn hiệu lực** đã được chứng minh từng nằm trong KB/Qdrant production:

1. `AGENT_DATA_API_KEY`.
2. Mật khẩu PostgreSQL của role `incomex`.

Mục tiêu cuối:
- credential cũ không còn xác thực được;
- credential mới nằm ở canonical secret store và mọi live consumer cần thiết dùng được;
- live/searchable KB + history/revision + Qdrant/derived store không còn exact old credential;
- không phá business text ngoài đúng chuỗi credential;
- có backup sạch mới sau rotation/redaction;
- backup lịch sử mã hóa không rewrite/xóa: chỉ được coi là chứa **retired credential** đã vô hiệu;
- production health PASS;
- sau đó mới sang G3 TARGET STACK.

## 1. Read/collision gate

1. Đọc `AGENTS.md` → task COLLAB §0 + KQ G2 + P39–P42 → PROMPT này.
2. READY phải khớp commit cuối chạm PROMPT.
3. Xác minh KQ G2 commit `fdab670752647bc072ab2dcfebe1be5b24aaab25` vẫn là CURRENT result và clone VPS2 đang stopped.
4. Xác minh không có executor/RUN khác đang mutation các bề mặt:
   - `agent-data` auth/config;
   - PostgreSQL role `incomex`;
   - KB/knowledge tables;
   - Qdrant collections;
   - GSM versions tương ứng.
   Có conflict thật ⇒ DỪNG.
5. Đọc machine state AD1 bằng verify script hiện hữu trên VPS1:
   - `AD1_24H=PASS` hoặc terminal `FAIL` ⇒ watcher 24h đã kết thúc, rotation được phép theo scope;
   - vẫn `GEN=2 RUNNING` ⇒ DỪNG trước mọi mutation/restart `agent-data`; không phá cửa sổ AD1.
6. Không gọi Guard/ruleset chỉ để PRE.
7. PRE chụp StartedAt/image/health của các service sẽ có thể reload/restart; chụp config/hash reference nhưng không secret value.

## 2. Luật secret handling

- Tuyệt đối không in/log/repo/chat plaintext secret.
- Giá trị secret chỉ được tồn tại:
  - trong GSM;
  - process memory;
  - tmpfs/root-only ephemeral file 0600 trong thời gian rotation nếu thực sự cần rollback/test.
- Mọi report dùng tên secret + version + SHA-256 prefix/fingerprint, không value.
- Không copy secret vào workspace/Git/VPS2.
- Không dùng shell tracing `set -x`.
- Tmpfs chứa old/new value phải shred/unlink ngay sau terminal PASS/DỪNG.
- Không tạo thêm plaintext backup chứa secret.

## 3. PRE — inventory chính xác consumer/source-of-truth

### A. AGENT_DATA_API_KEY
Đã biết canonical GSM secret `AGENT_DATA_API_KEY` tồn tại. PRE phải:
- xác minh current GSM enabled version + fingerprint nội bộ, không in value;
- inventory mọi live consumer/reference bằng tên/path/unit/env-name, tối thiểu:
  - server-side auth của `incomex-agent-data`;
  - Hermes key fetch/runtime nếu đang dùng;
  - tools/scripts hiện hành có `AGENT_DATA_API_KEY`;
  - gateway/consumer khác nếu runtime/config chứng minh có.
- phân loại consumer: MUST_SWITCH / STALE_NOT_RUNNING / NOT_USING.
- xác định service nào thực sự cần restart/reload để nhận key mới.

### B. PostgreSQL role incomex
- xác minh role `incomex` tồn tại, login/connection count và DB consumer hiện tại, không đọc password.
- inventory mọi live reference dùng role này bằng config/env-name/path/service; không suy từ tên.
- GSM có secret `PG_PASSWORD` lịch sử; **không mặc định nó đang đúng**. PRE phải xác định source-of-truth đang dùng hiện tại và sau RUN canonical phải là GSM version mới.
- xác định backup/DOT/cron/app nào cần credential mới để không gãy sau rotation.

Nếu không xác định được consumer/source-of-truth cho một credential ⇒ DỪNG trước mutation.

## 4. Rotation A — AGENT_DATA_API_KEY

Thực hiện một credential một lần; không xoay hai cái song song.

1. Tạo **new GSM version** cho `AGENT_DATA_API_KEY` bằng random mạnh; không in value.
2. Không disable old version ngay.
3. Stage new key vào đúng secret-loading mechanism hiện hữu của các MUST_SWITCH consumer.
4. Nếu server hỗ trợ dual-key native đã chứng minh ⇒ dùng dual-key tạm.
5. Nếu không hỗ trợ dual-key:
   - chuẩn bị toàn bộ consumer config trước;
   - thực hiện một coordinated reload/restart tối thiểu đúng service cần thiết;
   - không restart `claude-mcp`/Hermes/khác nếu không thực sự tham chiếu key.
6. Verify bằng new key:
   - agent-data health;
   - ít nhất auth endpoint/tool read đại diện;
   - Hermes/tools MUST_SWITCH nếu có.
7. Chỉ sau positive new-key PASS:
   - disable old GSM version;
   - reload/restart consumer còn cache old key nếu cần;
   - negative test old key phải 401/deny **mà không log value**.
8. Nếu new key fail:
   - rollback consumer về old enabled version khi old còn valid;
   - DỪNG;
   - không disable old.

Acceptance A: NEW works everywhere MUST_SWITCH; OLD fails; old GSM version disabled, chưa destroy trong RUN này.

## 5. Rotation B — PostgreSQL role incomex

PG write chỉ qua một DOT narrow production-safe.

### DOT
- ưu tiên DOT hiện hữu phù hợp; thiếu thì tạo `dot-vpsup-pg-role-rotate` theo DROOT27:
  - `--help` đủ purpose/when/not/input/dry-run/execute/rollback/secret-handling/examples/exit codes;
  - dry-run mặc định;
  - allowlist đúng role `incomex` + production PG target;
  - refusal nếu role/host/db/system_identifier ngoài PRE;
  - không nhận password qua argv/log.
- new password sinh mạnh và ghi **new GSM version `PG_PASSWORD`**; GSM trở thành canonical source sau RUN.
- old plaintext nếu cần rollback chỉ giữ tmpfs 0600, không persistent.

### Thứ tự
1. Stage consumer config/reference để sẵn sàng dùng new `PG_PASSWORD`.
2. Dry-run DOT: role + dependency + active sessions.
3. Execute rotate password role `incomex`.
4. Reload/restart tối thiểu đúng consumer cần reconnect.
5. Verify:
   - new credential connect PASS đúng DB/role/privilege expected;
   - các MUST_SWITCH consumer health/read/write test phù hợp PASS;
   - old credential connect FAIL.
6. Nếu fail trong cửa sổ kiểm:
   - rollback password qua DOT bằng old value từ tmpfs;
   - rollback consumer reference;
   - DỪNG.
7. Khi PASS: disable old GSM `PG_PASSWORD` version nếu nó chính là old canonical version; không destroy trong RUN này.

Không đổi role grants/ownership/RLS/superuser flags trong RUN này.

## 6. Redact live/searchable production stores — exact match only

Chỉ làm **sau khi cả hai old credential đã bị invalidate**.

### Fresh dry-run
- dùng đúng 2 old credential fingerprint/hash đã biết từ G2 evidence;
- quét live DB `directus` + `incomex_metadata` và tất cả Qdrant BUSINESS collection/searchable payload có thể chứa KB;
- không in value;
- báo:
  `credential_id | store | table/column-or-collection | rows/points | occurrences`.
- khác số G2 **không tự coi là lỗi** vì production đã tiếp tục ghi; dùng số fresh dry-run làm expected.
- nếu phát hiện **credential thứ ba** hoặc match mơ hồ ngoài đúng 2 fingerprint ⇒ DỪNG hỏi Owner.

### Execute
- mutation DB/Directus content phải qua DOT narrow; Qdrant qua DOT/native wrapped action có same exact-match guard.
- chỉ thay **đúng exact old credential values** bằng `REDACTED_RETIRED_CREDENTIAL`.
- không regex rộng; không sửa business text khác.
- transaction/count guard:
  - DB: actual row/occurrence phải khớp fresh dry-run, lệch ⇒ rollback transaction + DỪNG;
  - Qdrant: lập exact point-id plan trước; partial mismatch/failure ⇒ rollback bằng ephemeral old value trong cùng RUN rồi DỪNG.
- bao phủ history/revision/KB tables và Qdrant derived payload đã inventory.
- rebuild/invalidate derived searchable cache/index nếu consumer hiện hành có; không tự xóa business data.

### Post-scan
- exact old fingerprints trong live/searchable DB/Qdrant/cache = 0.
- không đòi byte-level vacuum/rewrite toàn PG/Qdrant production chỉ để xóa forensic dead tuples/WAL; credential đã invalidated. Ghi residual physical-retention risk theo lifecycle/backup, không làm disruptive rewrite trong RUN này.

## 7. Historical backups / Drive

**Không rewrite, không xóa backup lịch sử mã hóa.**
Lý do: credential cũ sau rotation đã vô hiệu; phá backup làm giảm khả năng phục hồi.

Làm:
1. Xác định cutoff timestamp: backup trước thời điểm redaction có thể chứa retired credential.
2. Ghi metadata/report: `PRE_ROTATION_BACKUP_MAY_CONTAIN_RETIRED_SECRET`; không sửa payload backup.
3. Sau redaction + service health PASS, chạy **một backup sạch mới** bằng pipeline hiện hữu:
   - DB/directus;
   - incomex_metadata;
   - Qdrant;
   - business files nếu pipeline hiện hành có.
4. Read-back/hash verify như BK1/backup policy hiện hữu.
5. Không đổi retention trong RUN này; backup cũ tự hết theo retention bình thường.

## 8. Production verification

Sau cả hai rotation + redact:
- Directus/vps/giaoduc/ops routes đại diện 200/expected;
- agent-data health + auth path PASS;
- PG consumer dùng role `incomex` PASS;
- Hermes/tool consumer AGENT_DATA_API_KEY PASS nếu MUST_SWITCH;
- backup job clean-run PASS;
- Qdrant reads PASS;
- no unexpected failed service;
- e-learning FREEZE/static 200 giữ nguyên;
- không thay VPS2 CURRENT checkpoint;
- StartedAt/restart delta chỉ đúng service được PRE xác định cần reload/restart.

## 9. GATE SEC-CRED PASS

PASS khi:
1. AGENT_DATA old key bị disable và auth FAIL; new key PASS mọi MUST_SWITCH.
2. PG old password FAIL; new password PASS; GSM `PG_PASSWORD` là canonical new version.
3. Live/searchable production stores exact old credential count = 0.
4. Không có credential thứ ba.
5. Historical encrypted backups giữ nguyên, đã đánh dấu cutoff; có một **backup sạch mới + read-back verify**.
6. Production health PASS, không unrelated mutation.
7. Tmpfs/ephemeral old/new secret material đã xóa.
8. G2 CURRENT checkpoint vẫn stopped/safe.

Nếu PASS ⇒ **NEXT G3 TARGET STACK**.

## 10. Report

Không tạo repo file mới.

### COLLAB.md
- Dòng hiện hành;
- `KQ@VPSUP-SEC-CRED-ROTATE-20260929-01 XONG|DỪNG`;
- chỉ report secret name/version/fingerprint prefix + consumer counts + redact counts; không value.
- nếu PASS: `SEC-CRED PASS · G2 HOST ACCEPTED · NEXT G3 TARGET STACK`.

### view.html
Cập nhật ngắn:
- G2 Host ACCEPTED;
- SEC-CRED rotate 2/2 PASS|STOP;
- old credential invalid;
- live searchable copy = 0;
- clean backup mới PASS;
- NEXT G3.

Commit:
`[Claude Code] VPSUP-SEC-CRED-ROTATE · retire credential lộ trong KB`

## 11. Sau RUN — không làm

- Không destroy old GSM versions; chỉ disable.
- Không rewrite/delete historical backup.
- Không nâng PostgreSQL/Directus/Nuxt/Qdrant.
- Không dựng TARGET.
- Không sửa schema/RLS/permission ngoài credential scope.
- Không xử lý unrelated security cleanup.

Sau SEC-CRED PASS, Host mới phát G3.
