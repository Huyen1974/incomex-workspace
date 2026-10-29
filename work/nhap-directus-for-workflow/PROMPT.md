# NDW · TS4 CỔNG GHI LUẬT S4 HẸP · P98/P99 · CHỈ TẠO VÀ TEST CỔNG (0 LUẬT)
RUN_ID: NDW-TS4-S4-LUAT-GATE-20261029-01
TASK: work/nhap-directus-for-workflow
EXECUTOR_SURFACE: Claude Code CLI
STATUS: **DRAFT · OWNER G2 TS4 GATE CHƯA CÓ · CHƯA GPT HOST READY · CHƯA OWNER DISPATCH. CẤM STARTED/MUTATION.** Sau khi Owner trực tiếp duyệt một lệnh DOT mới/validator/manifest+3 Guard targets+smoke UPDATE 0 theo P98/P99, Host mới ký `READY@<full last-touch PROMPT commit SHA>` ở COLLAB (DROOT58, REVIEW_REUSED=P98), Owner chuyển chuẩn DROOT38 AUTO0; S0 PASS mới chạy. Owner P94 chỉ duyệt CREATE S4 rỗng, không cấp G2 sửa code/Guard/ghi luật. Không dùng READY P95 đã CONSUMED.

READ_PATH: AGENTS.md (A0/A6/R1a/R1b/R3/R4/DROOT30/31/48/58) → root COLLAB lease → task COLLAB §0/P96–P99/§3.TQ/§3.KH → P98 R2/R3 → PROMPT này. VPS runtime code SSOT (không tự lấy Git cũ ghi đè). Host đã đọc nguồn Web Reports main: P0 là RUN khác, không đụng trong TS4 này.
WRITE_PATH: theo đường DOT hiện hữu trên VPS1, chỉ tạo mới (không overwrite): `/opt/incomex/dot/bin/dot-pg-s4-luat-apply`, `/opt/incomex/dot/lib/dot-pg-s4-luat-validate.py`, `/opt/incomex/dot/sql/s4-luat/approved-s4-luat-manifest.tsv`, file smoke 0-row nằm cùng thư mục và được SHA-pin bởi manifest; `guard-registry` thêm đúng 3 target/baseline qua `incomex-config-apply-v0`, biên nhận Guard và COLLAB STARTED/KQ qua workspace gateway. Không sửa `dot-pg-atomic-apply`, `dot-pg-label-apply`/validator gốc, `dot-sql-approved-manifest`, PG schema/roles, registry cũ, Web/Graph/Directus, không tạo service/timer/worker/bảng mới, không git add/reset/checkout/commit `/opt/incomex/dot`.

## Đích nghiệm thu (một DOT thật, KHÔNG nạp luật)
- `dot-pg-s4-luat-apply` chỉ nhận tệp SQL thuộc thư mục `sql/s4-luat/` **đã đúng path/hash trong manifest riêng**, không nhận path ngoài, link giả/symlink, tham số bypass/SQL trực tiếp. Mỗi lần chạy xác minh SHA, đúng bytes được validator đọc và trình psql; reject nếu file thay giữa check và execute (TOCTOU).
- Bộ kiểm import và sử dụng lại `tach_cau_lenh` từ `dot-pg-label-validate.py` (đọc interface/khả năng import thật ở S1). **Từ chối mặc định** mọi SQL không thuộc đúng hai AST/grammar sau: (1) `INSERT INTO public.tai_san_luat (các cột hợp lệ trong 14 cột, không lặp) VALUES (...)` chỉ literal chuỗi SQL chuẩn, số nguyên, `NULL`, boolean; `VALUES` nhiều tuple hợp lệ; (2) `UPDATE public.tai_san_luat SET con_hieu_luc = false WHERE ma = '<mã literal>'`. Cho phép chuỗi literal chứa `;`, `--`, `/*`, dấu nháy nhân đôi nhưng không coi chúng là SQL bên ngoài. Parser phải tiêu thụ toàn bộ token từng statement; chỉ một chuỗi câu thuộc hai class, giới hạn hợp lý số câu/tệp và bytes theo mẫu DOT hiện hữu, thực thi một transaction.
- **CẤM** INSERT/UPDATE bảng khác, `DELETE/TRUNCATE/DROP/ALTER/CREATE`, UPDATE cột khác, LIKE/WHERE khác, function/subquery/cast/CTE/`SELECT`, `RETURNING`/`ON CONFLICT`/`DO`/`SET`/`COPY`, identifier quoted, E/U&/dollar strings, psql meta (`\copy`, `\!`), nested comment/statement hidden, transaction control; không lách bằng comment/Unicode/tên alias/encoding. PG CHECK của S4 được giữ, không cho cổng mới bỏ rào nghiệp vụ của PG.
- **PG-safe:** đúng DB `directus`; dùng vai hiện có `workflow_admin`, `psql -1 -v ON_ERROR_STOP=1`; kiểm trong cùng transaction **sau khi giữ khóa phù hợp trên `public.tai_san_luat`** rằng không có noninternal trigger/rule có thể chuyển hướng ghi; nếu có ⇒ DỪNG trước SQL; không sửa PG role/trigger/rule. `--check` chỉ validation + RO, không có `UPDATE`/PG DDL ngoài chế độ execute thật.
- Đường lùi: từ chối cho chạy mới bằng **vô hiệu hóa command theo cơ chế DEL-1J** + Config Guard registry/manifest reconcile có receipt, bảo toàn baseline `.pre`. **Không** chỉ đổi tên command rồi để Config Guard MISSING/RED vĩnh viễn. S1 phải xác minh đường disable+Guard MATCH/APPROVED_CHANGE thật; không chứng minh được ⇒ STOP ngay trước production ghi, báo Host một blocker, không tự nới Guard/xóa lịch sử.
- **Smoke duy nhất được Owner G2 xét:** file `UPDATE public.tai_san_luat SET con_hieu_luc = false WHERE ma = 'kiem-thu-khong-ton-tai';` nằm trong new manifest với SHA; execute đúng một lần sau PRE, kết quả `UPDATE 0` và `COMMIT rc=0`, S4 row count trước/sau **0**, OID/catalog/relacl/role/triggers/no collections/no table_registry unchanged, chỉ +3 Config Guard targets; không có luật mới hay V3.

## S0 — Gates, STARTED riêng, không tranh cờ
(1) Owner `G2·TS4 cổng P99` trên task COLLAB (đúng phạm vi mới), (2) Host READY@PROMPT last-touch SHA đầy đủ ở commit riêng (Reviewer P98 reused), (3) Owner chuyển câu chuẩn, (4) không STOP/HOLD/COUNCIL_ALERT OPEN/STARTED trùng, root VPS-GHI trống, đủ RAM/PSI, (5) command gateway read/write đã chứng minh. PASS ⇒ `STARTED@NDW-TS4-S4-LUAT-GATE-20261029-01 <UTC> · executor=Claude Code CLI` commit riêng, đọc lại xác nhận. Nếu không ⇒ DỪNG không ghi VPS.

## S1 — PRE (Mac candidate / VPS read-only, chưa lấy quyền ghi)
- So thật source live `dot-pg-label-apply` + `dot-pg-label-validate.py` (`tach_cau_lenh`, cách kiểm CTE/comment/quoted), cổng DDL `dot-pg-atomic-apply` chỉ đọc, validator hiện có, Guard registry format, `incomex-config-apply-v0` và `dot-dot-register`. Không tự đổi đoạn code cũ.
- Đo `/opt/incomex/dot` dirty hiện hành (P98 thấy ≈226 modified +34 untracked; manifest live lệch HEAD 8 dòng), snapshot owner/mode/ACL và các tệp cùng mẫu; verify Config Guard drift-check MATCH, `tai_san_luat` OID 296646/14 cột/rowcount0/ACL P96 chưa đổi; exact 3 path mới chưa có (nếu có collision: DỪNG, không overwrite).
- Viết candidate local không phải production, chạy **toàn bộ R3 âm/dương của P98** và kiểm lại strict parser/full consumption; ít nhất 17 âm (CTE DML, 2nd statement, quoted/copy/casts/DO/ON CONFLICT/function/UPDATE khác) + dương gồm INSERT với `qt001_`/`birth_registry`/`meta_catalog` bên trong literal, nhiều VALUES, quote chứa `;`/`--`/`/*`/`''`, UPDATE false. Không chạy dữ liệu dương vào DB thật. Thuần `--check` không tạo DB changes.
- Chứng minh **kế hoạch rollback phù hợp Guard** từ cấu trúc hiện hữu + backup/baseline đã có (không thêm sidecar/service); thiếu hoặc không bảo toàn dirty Git hiện hành ⇒ STOP. Pass mới lấy VPS-GHI CAS và Guard PRE.

## S2 — One bounded production install; Config Guard bảo vệ ngay
- Install wrapper/validator/manifest mới và một smoke SQL có SHA (mode/owner theo mẫu, purpose header); không overwrite đối tượng cũ. Wrapper từ chối ngay khi chưa pin sha hoặc sai path, không có đường debug bypass.
- Đăng ký đúng 3 đích vào Config Guard (wrapper, validator, manifest) qua apply-v0; trước/sau `guard-registry` phải preserve toàn bộ dòng cũ, drift-check sau MATCH. Kiểm code ledger/Điều 30/31 cho script mới qua cơ chế hiện hữu, không mở cảnh báo nền hay auto-register legacy.
- Sau install, tự kiểm `--check` âm/dương **trên bản code vừa áp**; nếu khác candidate đã duyệt STOP, không chạy smoke.

## S3 — Một smoke 0 row trong cùng transaction
- Đọc lần cuối task COLLAB/PROMPT READY/STOP, root lease, SHA candidate và manifest. Dùng wrapper đúng một lần chạy fixture UPDATE 0 qua psql -1; preflight trigger/rule trong cùng transaction dưới lock. Kiểm output UPDATE 0/COMMIT, 0 bảng S4 rows trước/sau, same owner/role/ACL/OID/constraints/index/PG trigger alerts/Directus registry.
- Gặp thay đổi dữ liệu thật hoặc write ngoài scope ⇒ STOP, áp đường disable có Guard MATCH theo S1, ghi KQ MỘT PHẦN, không tự chạy lệnh sửa/DELETE.

## S4–S5 — Guard POST, KQ/lease trả
- Config Guard MATCH đúng 3 target mới + registry; Guard POST `same_or_better` theo footprint thực, Đ30/31, event change/receipt; đèn #24 cũ PREEXISTING_SAME không biến thành rollback giả. Nếu sau COMMIT có regression do scope mới, vô hiệu hóa command + reconcile Guard theo đường chứng minh ở S1; không đổi PG hay rollback S4 table (vốn chưa đổi dữ liệu).
- COLLAB KQ: SHA/bytes ba file, manifest smoke, source label parser được dùng lại, số test âm/dương, command install path/role, smoke UPDATE 0/PG row count0, registry baseline→after, Guard PRE/POST, rollback proof, dirty Git preserved, VPS-GHI returned. `NEXT_TRIGGER=GPT_HOST_NGHIEM_THU_TS4_GATE_THEN_OWNER_APPROVE_FIRST_RULE_BATCH_AND_V3`. Không mở lô luật/V3/Web/RAG hoặc tự tạo RUN khác.

## DROOT48 · STEP_WALK
| Bước | Surface | Trigger/deadline | Evidence | Hỏng |
|---|---|---|---|---|
| S0 | Claude Code CLI | Owner dispatch sau G2/READY; ≤5′ | G2 + PROMPT SHA/STOP/lease + STARTED commit riêng | DỪNG |
| S1 | Claude Code CLI | S0; ≤12′ RO/offline | source parser, dirty Git/baseline, 17+ âm/dương, rollback-Guard proof | DỪNG 0 production |
| S2 | Claude Code CLI | S1 PASS + VPS-GHI/Guard PRE; ≤15′ | 3 new targets + fixture SHA/registry Guard MATCH, installed tests PASS | DỪNG/MỘT PHẦN |
| S3 | Claude Code CLI | S2; ≤5′ | one UPDATE 0/COMMIT, row 0→0, no trigger/rule/DDL/role | disable/Guard match nếu regression |
| S4–S5 | Claude Code CLI | S3; ≤10′ | Guard POST/receipt, KQ, cờ trả | Host nghiệm thu |
Hard stop 55′, không giữ terminal chờ hay chạy nền. Nếu có input/rollback chưa sẵn thì DỪNG **trước** thay đổi production; không sửa thêm quyền/Guard/code ngoài scope.
