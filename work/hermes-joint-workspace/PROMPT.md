# HJW RUN24 — Codex khép bốn đường quản trị KB, chỉ tạo nguồn mã ứng viên
RUN_ID: HJW-G8-AD-KB-ADMIN-20261030-24
STATUS: FINAL_PROMPT, NO_AUTO_RUN. Chỉ chạy sau Host READY@full last-touch PROMPT SHA ở COLLAB HJW và Owner chuyển lệnh.
Executor: Codex Desktop MacBook (developer); Host GPT Chat. Không thêm vòng KST cho sửa nhỏ.
Write_Path: nhánh dev đang có của DRAFT PR #358 tại Huyen1974/agent-data-test; KQ/Bảng và evidence qua workspace_* Gateway D12 vào work/hermes-joint-workspace. Không ghi production/VPS/PG/Qdrant.

Đọc AGENTS A0/A2/A5/A6, DROOT30/31/56/58/60, GHM_CODE_CHANNEL; root COLLAB; HJW COLLAB §0/§1–3/Bảng/P458/P486–P487; PROMPT này; PR #358/#357; evidence RUN23; agent_data/server.py, kb_declaration.py, declaration_contract.py và tests/unit/test_hjw_four_facts.py.

## Phạm vi đã chốt
- RUN23 P486 đạt G8_AD_KB_PRIMARY_SOURCE_CI_PASS cho MCP/stdio/hybrid/REST; PR358 OPEN/DRAFT HEAD 2d966640a0ccdf22fec50ee45a725fdfb41bfe48, base main 6160f9ad6e5d16012dfe20bb59949abf5ffadad2, GH run41075696274 SUCCESS với 271 Unit PASS. HTTP fixture30 PASS không phải live E2E. PR357 OPEN/DRAFT HEAD 36c682914c9f412078113b6d85319f11356d1130, không sửa. Verified product/origin profile mapping mới có hỗ trợ trong code và fixture, chưa có cấu hình live.
- Còn bốn admin KB REST cần phân loại và khai danh bằng CÙNG kb_declaration/declaration_contract: POST /kb/reindex và /kb/reindex-missing luôn là logical write; POST /kb/cleanup-orphans khi dry_run=false là write, dry_run=true mặc định chỉ đọc; POST /kb/audit-sync khi auto_heal=true là write, auto_heal=false mặc định chỉ đọc. Các read-mode vẫn yêu cầu auth hiện hữu nhưng KHÔNG đòi thêm 4 facts. Với write-mode, check bốn facts trước bất kỳ PG/Qdrant/event mutation nào kể cả khi không có dữ liệu cần sửa. Không cho gọi Python handler trực tiếp lách lớp admission. Không suy actor/môi trường từ VPS, UA, IP hoặc shared API key.
- Reuse FastAPI auth hiện hữu, kb_declaration.writer hoặc helper nhỏ cùng contract; không mở gateway mới, secret mới, quyền mới, bảng mới hoặc dịch vụ mới. Hợp lệ trả receipt với raw/canonical/provenance/auth; thiếu/sai trả chỉ dẫn, 0 mutation; ghi Qdrant thất bại chỉ báo kết quả partial/unconfirmed, không giả atomic. Giữ API/legacy advertise, dry-run, audit read-only, limits và lỗi cũ.

## Host DROOT60 INPUT READY
H1 Source/refs: GH PR358/head/main và PR357 pin phía trên, 14 paths, Codex push branch đã chứng minh thực. 
H2 Code: Host đã đọc server.py bốn routes, _run_reindex/_run_cleanup và audit-sync auto_heal; kb_declaration có sẵn PRIMARY, ADMIN_UNCOVERED, writer, parse, profile_facts. 
H3 CI: GitHub run41075696274 preflight/scan/policy/unit SUCCESS 271 đúng head; test file HJW đã bắt buộc trong Unit tests; thêm ca vào file đó, không sửa workflow. 
H4 Safety: chỉ dev PR, 0 VPS write; no GH main merge/PR357 edits; rollback nhánh nháp chưa merge. 
H5 Runtime: Host không yêu cầu Docker/live DB; Mac/CI fixture, credentials/head freshness và tests lúc chạy là EXECUTOR_FRESHNESS. HOST_UNVERIFIED=0 cho scope source-only.

## STEP_WALK
S0 — Kiểm READY/STOP, repo/head/branch/main PR357 fresh, 0 RUN active; ghi STARTED. Main drift thì so diff để không mất mã và KQ PARTIAL nếu conflict.
S1 — Sửa nhỏ tối đa ba tệp agent_data/server.py, agent_data/kb_declaration.py, tests/unit/test_hjw_four_facts.py. Bọc admission trước write; phân biệt read-only vs mutating theo payload; auth trước declaration; cleanup context mỗi request; không đổi primary writers/CI/queue.
S2 — Test các route ở enforce: missing/mismatch/forged server metadata/wrong credential => zero PG/Qdrant/business event; valid => 4 facts receipt; advertise legacy không đổi; cleanup dry_run true và audit auto_heal false đọc được không khai; false/true mutating phải khai; store-error phải báo partial. Dùng real contract và handler với fake storage; chạy Mac tests 271+ và GitHub gate trên exact new head; HTTP fixture riêng khi deps có, không gọi live KB.
S3 — Push non-force đúng nhánh PR358, giữ PR357 và main không đổi. Kiểm CI head/base Unit tests thật SUCCESS; queued/RED => PARTIAL có log, không chờ vô hạn. Ghi P488/KQ/Bảng và evidence/run24-kb-admin-20261030; đóng sạch, 0 VPS mutation. PASS chỉ G8_AD_KB_ADMIN_SOURCE_CI_PASS, KHÔNG G8_SYSTEM/KST_ACCEPT/deploy.

Còn sau RUN24: inventory writer KB đầy đủ; PR357 fresh queue.sqlite bootstrap race và xung đột workspace_tasks.py/workspace_execution.py; tích hợp 4worker+4facts, Linux image build/rollback; advertise-only, C1/C2 AI thật, guarded enforce. KST review tổng hợp trước release, không giữa các sửa nhỏ.
