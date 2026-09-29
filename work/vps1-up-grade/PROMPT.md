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

1. Đọc `AGENTS.md` → task COLLAB §0 + KQ G2 + P39–P45 → PROMPT này.
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

### A. AGENT_DATA_API_KEY — R2 consumer checklist bắt buộc
Đã biết canonical GSM secret `AGENT_DATA_API_KEY` tồn tại. PRE phải xác minh current GSM enabled version + fingerprint nội bộ, không in value, rồi kiểm **từng mục** dưới đây; không được kết thúc inventory nếu còn mục `UNKNOWN`:

**ON_VPS:**
- server-side auth của `incomex-agent-data`;
- Directus: `FLOWS_ENV_ALLOW_LIST`/env/reference đưa `AGENT_DATA_API_KEY` vào Flow; nếu image/container nhận env lúc create thì phân loại `MUST_SWITCH_RECREATE`;
- Nuxt: `NUXT_AGENT_DATA_API_KEY`/env/reference; nếu nhận env lúc create thì `MUST_SWITCH_RECREATE`;
- `claude-kb` `.env`/runtime nếu đang chạy hoặc là caller hiện hành;
- Hermes key-fetch + `/run/hermes`/runtime nếu thực sự dùng;
- cron/script/gateway/tool hiện hành có `AGENT_DATA_API_KEY`.

**OFF_VPS:**
- GitHub Actions secret `AGENT_DATA_API_KEY` của workflow `data-lifecycle` nếu workflow tồn tại/đang dùng;
- cấu hình MCP/Codex/Cursor/launcher trên Mac Owner có reference tới key này.

**LITERAL/FALLBACK trong source:**
- `scripts/reconcile-knowledge.py`;
- `scripts/reconcile-tasks.py`;
- và literal khác nếu exact old-key fingerprint/hash khớp.
Literal source chỉ ghi `FOLLOWUP_CODE_SECRET_GUARD`; không coi là credential thứ ba và **không sửa code trong RUN này**.

Phân loại mỗi dòng: `MUST_SWITCH_RECREATE | MUST_SWITCH_RELOAD | OFF_VPS | STALE_NOT_RUNNING | NOT_USING | LITERAL_FOLLOWUP` + bằng chứng path/unit/workflow/config. Xác định service nào cần recreate/reload và thứ tự cutover.

OFF_VPS: nếu có đường an toàn để cập nhật từ GSM **không in value** (ví dụ GitHub secret qua stdin) thì cập nhật trong RUN trước khi disable old key. Nếu không thể tự cập nhật, ghi đúng **một bước Owner** phải làm sau cutover (ví dụ restart/reload app Mac sau khi launcher/config đã lấy key mới); không mở rộng scope và không coi OFF_VPS là lý do DỪNG nếu production on-VPS đã PASS.

### B. PostgreSQL role incomex — R1 gồm consumer ẩn trong PG
- xác minh role `incomex` tồn tại, login/connection count và DB consumer hiện tại, không đọc password.
- inventory mọi live reference dùng role này bằng config/env-name/path/service; không suy từ tên.
- **Bắt buộc kiểm FDW trong chính PostgreSQL:** DB `directus` có server `incomex_meta_srv` và user mapping cho roles `workflow_admin` + `directus`. Đọc metadata/options qua DOT/superuser-safe path nhưng không in secret; xác định remote user của từng mapping.
- Nếu một mapping dùng remote user `incomex`, phân loại nó là `MUST_SWITCH_FDW` và phải cập nhật password option trong **cùng cửa sổ rotation B** với role `incomex`; không được để mapping dùng old password sau ALTER ROLE.
- PRE ghi foreign table(s)/query đại diện dùng `incomex_meta_srv` để §5 verify sau rotation.
- GSM có secret `PG_PASSWORD` lịch sử; **không mặc định nó đang đúng**. PRE phải xác định source-of-truth đang dùng hiện tại và sau RUN canonical phải là GSM version mới.
- xác định backup/DOT/cron/app/FDW nào cần credential mới để không gãy sau rotation.

Nếu không xác định được consumer/source-of-truth cho một credential ⇒ DỪNG trước mutation.

## 4. Rotation A — AGENT_DATA_API_KEY · R3 coordinated cutover, **DUAL-KEY = KHÔNG**

Đã đo source `agent-data`: chỉ có **một master `API_KEY` duy nhất**. Không thăm dò dual-key nữa và không thiết kế dựa trên hai key song song.

Thực hiện một credential một lần; không xoay hai credential song song.

1. Tạo **new GSM version** cho `AGENT_DATA_API_KEY` bằng random mạnh; không in value. **Old GSM version vẫn enabled** để rollback trong cửa sổ cutover.
2. Hoàn thành checklist R2; mọi `MUST_SWITCH_*` phải có candidate config/reference mới sẵn sàng nhưng chưa để production caller dùng lệch pha.
3. OFF_VPS có đường tự động an toàn thì stage/update trước cutover; literal source chỉ FOLLOWUP.
4. Chụp PRE health + StartedAt + config hash của Directus, Nuxt, agent-data, claude-kb nếu MUST_SWITCH, Hermes nếu MUST_SWITCH.
5. **Coordinated cutover ngắn:** đổi server-side `agent-data` sang new key và recreate/reload **trong cùng cửa sổ** các consumer on-VPS đã phân loại `MUST_SWITCH`, đặc biệt Directus + Nuxt + agent-data (+ claude-kb nếu dùng). Hermes chỉ restart/reload nếu inventory chứng minh runtime cache key và cần switch.
6. Health/auth ngay sau cutover:
   - agent-data health PASS;
   - Directus Flow/caller đại diện dùng new key PASS;
   - Nuxt/KB caller đại diện PASS;
   - claude-kb/Hermes/tool MUST_SWITCH PASS;
   - GitHub Actions/OFF_VPS nếu đã auto-update: verify reference/update state không lộ value.
7. Khi NEW PASS mọi **on-VPS MUST_SWITCH**:
   - disable old GSM version;
   - negative test old key phải 401/deny mà không log value;
   - consumer nào còn cache old key phải được recreate/reload ngay.
8. Nếu bất kỳ on-VPS MUST_SWITCH fail trong cửa sổ:
   - re-enable/giữ enabled old GSM version;
   - rollback server + consumer references về old;
   - recreate lại đúng services;
   - verify health;
   - DỪNG. Không để trạng thái nửa mới/nửa cũ.
9. Nếu chỉ còn OFF_VPS cần thao tác thủ công, production on-VPS vẫn được PASS; report đúng **một bước Owner** cần làm và consumer đó có thể tạm fail sau khi old key bị disable cho tới khi Owner refresh/restart.

Acceptance A: NEW works mọi on-VPS MUST_SWITCH; OLD fails; old GSM version disabled chưa destroy; OFF_VPS được auto-update hoặc có đúng một Owner action rõ ràng; không consumer on-VPS UNKNOWN.

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
1. Stage consumer config/reference để sẵn sàng dùng new `PG_PASSWORD`; PRE phải có danh sách `MUST_SWITCH_FDW` từ R1.
2. Dry-run DOT: role + dependency + active sessions + FDW server/user-mapping targets.
3. Trong **một coordinated transaction/window**:
   - rotate password role `incomex`;
   - với mỗi `MUST_SWITCH_FDW`, cập nhật password option của user mapping `incomex_meta_srv` cho roles `workflow_admin`/`directus` dùng đúng new password; không đổi remote user/server/grants khác.
4. Reload/restart tối thiểu đúng consumer cần reconnect.
5. Verify:
   - new credential connect PASS đúng DB/role/privilege expected;
   - các MUST_SWITCH consumer health/read/write test phù hợp PASS;
   - **foreign-table read qua DB `directus`/`incomex_meta_srv` PASS** bằng query đại diện đã chụp PRE;
   - 13 live connections/consumer set sau reconnect hợp lý, không auth failure tăng bất thường;
   - old credential connect FAIL.
6. Nếu fail trong cửa sổ kiểm:
   - rollback role password qua DOT bằng old value từ tmpfs;
   - rollback FDW user-mapping password option cùng old value;
   - rollback consumer reference;
   - verify foreign-table read + health;
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

## 8A. Lớp bảo vệ Điều 30/31 — bắt buộc trong cùng RUN

Áp DROOT29 + KB `Điều 30 v1.2` và `Điều 31 v1.2` cho mọi **mã/config production bền** được tạo mới hoặc sửa chức năng trong RUN này. Không mở service/DB/guard mới nếu lớp hiện hữu ghép được.

1. **Inventory protection target trước KQ:** liệt kê mọi DOT/script/config/unit/runtime file production được tạo/sửa bởi SEC-CRED; tách file tạm/evidence không chạy production.
2. **Điều 30 — regression proof:** chức năng cũ bị bề mặt thay đổi phải có bằng chứng không hồi quy. Nếu thay đổi/recreate Directus/Nuxt ảnh hưởng UI/web thì API/SSR 200 **không đủ**: chạy browser thật trên các luồng đại diện đã sống trước RUN (ít nhất Owner View/Knowledge hoặc trang nghiệp vụ liên quan auth/data path) và lưu bằng chứng PASS; nếu không chạm UI/web code thì ghi `D30_UI_NOT_TOUCHED` nhưng vẫn chạy regression smoke của consumer cũ bị rotate.
3. **Điều 31 — integrity/protection:** mọi target bền mới/sửa phải được đăng ký vào **Protection Guard/Config Guard/contract/watchdog hiện hữu** phù hợp, gồm path + hash/invariant + owner/scope + expected state. Không để code production mới ở trạng thái `UNMONITORED`.
4. **Inverse/self-protection:** checker phải phát hiện target bị thiếu/đổi ngoài dự kiến; chính file checker/baseline nếu bị sửa phải nằm trong phạm vi tự bảo vệ hiện hữu. Không tự học baseline từ live drift.
5. **Negative/mutant:** trên fixture/bản sao, làm ít nhất một sai hash/config/missing-target cho mỗi lớp mới và chứng minh Guard FAIL; không phá production để test.
6. **Watchdog:** chứng minh runner/checker còn sống bằng cơ chế watchdog hiện hữu của Điều 31 (không tạo service mới); silence/runner-dead không được tính PASS.
7. **Controlled rebaseline:** restart/recreate có chủ đích chỉ rebaseline sau POST chứng minh đúng RUN_ID, expected image/hash/StartedAt, health PASS, outside-scope=0; lưu old→new + reason. Lệch ngoài dự kiến ⇒ không rebaseline, DỪNG/rollback.
8. **Rollback/known-good:** mỗi target mới/sửa phải có đường rollback hoặc known-good hash/version đã ghi trong evidence.

KQ SEC-CRED không được XONG nếu lớp bảo vệ của durable production delta còn thiếu hoặc Guard/Config Guard/Điều 31 watchdog không PASS.

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
9. Durable production code/config delta đã có **Điều 30/31 protection coverage PASS**: regression proof phù hợp, Protection/Config Guard registered, mutant FAIL như kỳ vọng, watchdog sống, controlled rebaseline/rollback đầy đủ.

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
- **FOLLOWUP sau SEC-CRED, không chặn G3:** thêm chốt ở DOT/endpoint ghi KB để từ chối payload khớp hash credential đang dùng hoặc mẫu secret phổ biến; đồng thời dọn literal fallback secret trong source nếu R2 phát hiện. Không mở RUN này sang preventive guard.

Sau SEC-CRED PASS, Host mới phát G3.
