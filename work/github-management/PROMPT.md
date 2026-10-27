# PROMPT — C1B FINALIZE · AGENT DATA + WEB HEALTH (DRAFT)

RUN_ID: GHM-C1B-FINALIZE-20261027-03
STATUS: DRAFT_NOT_READY · GPT Host P67 → Claude P68 review → GPT Host ký READY cùng SHA → Owner RUN. Lệnh P64 đã KQ P66, không dùng READY cũ. Đây là nguồn lệnh duy nhất trên repo, không có phiên bản song song ở chat.
EXECUTOR: Codex CLI/Desktop trên Mac; Claude Chat Reviewer; GPT Host quyết và ký; Owner chuyển. KST Claude Code CLI giữ vai từ C3.

## I. Mục tiêu và phạm vi
Khép đúng hai nợ C1B: Agent Data canary/deploy–rollback thật và Web Health Check 13 CHECK trên VPS với chức năng đầy đủ. Kế thừa Web Nuxt4 parity 166/166, CI 16/16, deploy–rollback P66 PASS; Lifecycle/ops-smoke VPS GREEN; C1A runner/4 repo archive P61; không làm lại.
Chỉ 2 repo PRIVATE `Huyen1974/agent-data-test` và `Huyen1974/web-test`, plus script deploy/known-good P61/P66 trong cổng Đ30/31; `incomex-workspace` chỉ sổ điều hành. Không đổi PG/Qdrant/Directus, schema, data, nginx/compose, Guard; không tạo key/token/gateway/repo mới, không force-push hoặc bật auto-CD, không tự C3/C2/C4. Quyền Mac `gh` Owner, SSH/GSM sẵn có dùng theo P57–P64; CI PR không nhận secrets/root/docker.sock.
Khi tác động host phải kiểm VPS-GHI CAS/Guard/STOP/Đ30–31; đọc mã/build/CI và nhánh GitHub không giữ cờ; cờ bận thì thực hiện phần độc lập, không mở RUN chờ.

## II. S0 — PRE & chứng cứ kế thừa
Đọc AGENTS.md → COLLAB §0/P61–P67 → C1B-REPORT/C1B-CLOSE-REPORT, PROMPT DRAFT đã được ký READY mới và evidence private P66; đọc HEAD repo, action status, runner 2 repo. Đối chiếu AD main P66 `251739422a997c9741e487fb4252f3c3d92e1be1`, Web main `728fa1deaee45b36c07714ede1da4c0633683e89`, old runtime healthy, Data Lifecycle run 40359232468 và ops run 40359238669; HEAD mới nếu có thì reconcile, không reset.
Kế thừa AD effective config 17/17 và 40 image files; old AD image `46e0ba15…` và candidate `0419152b…` (phải đọc digest đầy đủ từ P66), old Web giữ nguyên. Không dùng token Directus cũ 401, không kiểm lại C1A/S7/Web/2 audit đã PASS.

## III. S1 — AD canary PG read-only, không DDL production
Nguyên nhân có bằng chứng: `agent_data/main.py` gọi `pg_store.ensure_tables()` khi startup; `pg_store.py` dùng autocommit và CREATE TABLE/INDEX IF NOT EXISTS, PG read-only từ chối ⇒ db=None, /kb/list 500. Sáu đối tượng PG có sẵn theo P66 chưa đồng nghĩa schema definition đã đủ.
**Ưu tiên code change nhỏ trên nhánh AD:** bằng SELECT pg_catalog kiểm đủ bảng/index/column/definition của startup; nếu đã tồn tại đúng cấu trúc thì `ensure_tables()` KHÔNG gọi bất cứ CREATE/ALTER/INDEX nào (fast-path read-only); trường hợp thiếu/mismatch canary phải fail-closed, không tự tạo. Kiểm trong test/DB fixture cô lập (không credential production) và canary bằng PG read-only: log chỉ tên đối tượng/trạng thái, không secret. Không đổi schema/credential/quyền hay config production.
Canary cần /info, /health, /kb/list?limit=1 (HTTP200 + JSON items array) và contract/readonly diagnostics thực; không coi /health 200 là PASS đủ. Giữ Qdrant mutation/listener/workspace supervisor tắt như P66. Nếu hướng fast-path không khả thi, test bootstrap trên DB thử cô lập; không được dùng production schema writer để lách auto-review. Nếu mọi đường an toàn không khả thi, ghi DỪNG đúng AD với exact SQL/đối tượng/backup/backout cần Owner duyệt riêng; làm tiếp Web Health.
Sau canary đủ bằng chứng: CI đúng source SHA/branch trên runner VPS, non-force main fast-forward, kiểm config parity/rollback old digest trước deploy. Không trộn main GitHub cũ vào cây baseline.

## IV. S2 — Web Health CHECK2/5/7/8/12
Giữ toàn bộ 13 CHECK, lịch 6 giờ, logic main-only trusted và key GitHub sẵn có; job hosted cũ ACTIVE tới khi thay thế PASS tương đương. Không đưa secret vào PR.
- CHECK2: sync_status=warning là tín hiệu thực (2 orphan/1 ghost ở Lifecycle); tra quy định blocking/advisory hiện hữu rồi gắn đúng severity, không tự auto-heal hay đổi ngưỡng để được GREEN. Nếu còn true blocking thì FAIL thật và ghi nợ dữ liệu.
- CHECK5: ghi mã HTTP, content-type, response schema /chat ở dạng sanitized; phân biệt auth/route/parser với zero context thật. Probe hạn chế số lượt, không in dữ liệu hoặc gọi AI lặp tốn phí. Giữ tiêu chí kết quả tìm kiếm thật.
- CHECK7: GET /kb/list trả HTTP200, JSON `items` array theo mã Agent Data; xác thực GitHub secret hiện có bằng status mà không in key; lỗi HTTP/shape phải FAIL rõ, không parse/null thành empty.
- CHECK8: không tính AD=0 khi CHECK7 lỗi. API list có `limit,offset,next_offset`, mặc định 50; chỉ so hai tập đồng nghĩa (filter knowledge và non-folder) bằng pagination có giới hạn hoặc read-only aggregate chứng minh tương đương. Trả UNKNOWN/FAIL khi không đủ bằng chứng, không gọi gap9613 là mất dữ liệu.
- CHECK12: trang registries timeout 15s, P66 riêng 60s đạt; áp timeout riêng đủ chuẩn, phân biệt HTTP000/timeout, vẫn kiểm số/contract các registry. Không kéo dài toàn job vô hạn.
Test candidate workflow_dispatch ở nhánh ghim SHA bằng P64 pattern, trên runner VPS đã nghiệm thu, không PR secret; đủ 13/13 TRUE PASS mới promote non-force lên main và run main GREEN; giữ schedule, không disable cùng tên workflow vừa chuyển. Không tạo thêm audit song song.

## V. S3 — AD deploy/rollback thật nếu canary PASS
Chỉ khi read-only canary /kb/list+contract, source CI/main, effective config 17/17, image Config parity, schema present và known-good/old digest/rollback proof đều đạt. Dùng NGUYÊN script deploy P61, 1 restart candidate AD + 1 restart về old; tổng ≤2 restart AD, ngoại lệ 1 known-good emergency restore nếu rollback thật chưa khỏe. Không restart Web, DB, nginx config hay VPS; nginx reload chỉ nếu công cụ P61 đã duyệt. Kiểm contract sau deploy và hash/config/old health sau lùi; không làm DDL/migration/data writes.
Nếu auto-review vẫn chặn vì đường còn DDL khả dụng hoặc chỉ còn permission production có khả năng ghi schema, KHÔNG bypass; DỪNG riêng AD với một blocker có chứng cứ, không buộc Owner canh. Không xin lại quyền Mac/GSM đã có.

## VI. S4 — KQ và bàn giao
C1B_SCOPED=PASS chỉ khi Web P66 vẫn PASS, AD canary+deploy–rollback thật PASS, Web Health main 13/13 GREEN trên VPS, 3/3 audit giữ schedule/semantics, Guard/receipt/VPS-GHI sạch. Nếu không đạt thì XONG CÓ GIỚI HẠN có ma trận PASS/FAIL theo hai nhánh và NEXT_TRIGGER chính xác; không tô xanh CHECK thực lỗi.
Ghi SHA từng repo, CI runs/runner, Web Health từng CHECK, data warnings, AD /kb/list/no-DDL proof, release/rollback, chi phí đo, trạng thái production, POST scoped và nợ GLOBAL_GUARD riêng. Trả VPS-GHI, đóng lease/cleanup build tạm, giữ known-good. Ghi KQ+Bảng/ROADMAP/README cùng commit, không tự chạy C3/C2/C4.
