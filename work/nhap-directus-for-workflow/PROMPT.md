# NDW · TS4 CỔNG GHI LUẬT S4 HẸP · P98/P99 · CHỈ TẠO VÀ TEST CỔNG (0 LUẬT)
RUN_ID: NDW-TS4-S4-LUAT-GATE-20261029-01
TASK: work/nhap-directus-for-workflow
EXECUTOR_SURFACE: Claude Code CLI
STATUS: **OWNER_G2_APPROVED@P102 · CONDITIONAL_READY_ONLY_IF_HOST_READY_SIGNATURE_IN_COLLAB · NOT_STARTED.** Owner đã duyệt đúng 1 DOT hẹp/3 Guard targets/manifest chỉ một smoke UPDATE 0 theo P100/P101. Claude P98/P100 phản biện, Host P101/P102 đã rà DROOT60; không mở vòng khác. RUN chỉ hợp lệ khi task COLLAB có một chữ ký Host `READY@full last-touch PROMPT commit SHA` cho RUN hiện hành ở P103, Owner chuyển câu DROOT38 và S0/S1 PASS. Thiếu bất kỳ cổng nào ⇒ không ghi. Cấm luật thật/V3/Web/DDL/PG role, không sử dụng READY P95 cũ.

READ_PATH: AGENTS.md A0/A6/R1a/R1b/R3/R4/**DROOT60**/DROOT30/31/48/58 → root COLLAB VPS-GHI → task COLLAB §0/P96–P102/§3.TQ/§3.KH (HUMAN_DIRECTIVE P102 + Host READY P103) → P98 R2/R3, P100 T1–T5 → PROMPT này, gồm INPUT READY TABLE. Runtime DOT ở VPS1 là SSOT; không checkout Git DOT cũ; P0 Web chạy phạm vi khác.
WRITE_PATH: chỉ tạo mới trên VPS1 `/opt/incomex/dot/bin/dot-pg-s4-luat-apply` (root:root 755), `/opt/incomex/dot/lib/dot-pg-s4-luat-validate.py` (644), `/opt/incomex/dot/sql/s4-luat/approved-s4-luat-manifest.tsv` (644), một smoke SQL UPDATE 0 (644) trong `sql/s4-luat/`. **Manifest production đúng 1 dòng smoke**, không fixture khác. Registry thêm 3 target Config Guard qua `incomex-config-apply-v0`; Guard PRE/POST. Fixture kiểm tra chỉ trong RUN temp **ngoài** thư mục sản xuất. Disable wrapper bằng `apply-v0` cập nhật nội dung + baseline Guard, không đổi tên. Không sửa `dot-pg-atomic-apply`, label-apply, Guard core, PG schema/role, `dot-sql-approved-manifest`, Web/Graph/Directus; không gọi dot-dot-register/không Git add/reset/checkout.

## Đích nghiệm thu (một DOT thật, KHÔNG nạp luật)
- `dot-pg-s4-luat-apply` chỉ đọc đường canonical trong `sql/s4-luat/` và manifest **1 dòng smoke** (SHA/path), từ chối symlink/path ngoài/file chưa được duyệt/SHA lệch/args bypass. Snapshot SQL tạm 0600 đọc 1 lần, SHA/validator/psql dùng cùng bytes; dọn trap, tối đa 2 MiB / 2.000 statements, không TOCTOU.
- Validator dùng lại `tach_cau_lenh` từ `dot-pg-label-validate.py` qua `importlib` do tên file có gạch ngang (P100 đã kiểm import không có side effects). Strict parse hoàn toàn hai statement classes: INSERT INTO public.tai_san_luat (cột thuộc 14, không trùng) VALUES literal chuỗi/số nguyên/NULL/boolean, nhiều tuple; hoặc UPDATE public.tai_san_luat SET con_hieu_luc=false WHERE ma='literal'. Chấp nhận `;`, `--`, `/*`, `''` *trong literal* nhưng cấm SQL ẩn ngoài literal. Limit 2 MiB / 2.000 câu/tệp.
- **CẤM** INSERT/UPDATE bảng khác, `DELETE/TRUNCATE/DROP/ALTER/CREATE`, UPDATE cột khác, LIKE/WHERE khác, function/subquery/cast/CTE/`SELECT`, `RETURNING`/`ON CONFLICT`/`DO`/`SET`/`COPY`, identifier quoted, E/U&/dollar strings, psql meta (`\copy`, `\!`), nested comment/statement hidden, transaction control; không lách bằng comment/Unicode/tên alias/encoding. PG CHECK của S4 được giữ, không cho cổng mới bỏ rào nghiệp vụ của PG.
- **PG-safe cụ thể theo P100:** `docker exec -i postgres psql -X -U workflow_admin -d directus -1 -v ON_ERROR_STOP=1 -c 'LOCK + DO preflight' -f -` trên đúng snapshot đã SHA; DO dưới lock kiểm `pg_trigger` noninternal và `pg_rewrite` của S4, nếu có thì exception trước ghi. `-1` làm chung một transaction, lỗi một dòng rollback toàn batch; không DDL/role/trigger. Lệnh hoàn chỉnh trong hợp đồng P101 bên dưới.
- **Lùi fail-closed:** dùng chính apply-v0 thay **nội dung** wrapper đang được Guard bảo vệ bằng candidate DISABLED `exit 1`, cập nhật approved baseline cùng target ⇒ drift-check MATCH, Guard POST, bản trước ở `.pre`; không `mv`, không xoá target/manifest, không đổi PG. S1 chứng minh bằng --help + mẫu P96 và candidate byte/SHA chứ không chạy lùi production để diễn tập.
- **Smoke duy nhất** tại production manifest 1 dòng: `UPDATE public.tai_san_luat SET con_hieu_luc = false WHERE ma = 'kiem-thu-khong-ton-tai';`, chạy một lần, bảng S4 trước/sau 0 rows; `LOCK TABLE`/`DO`/`UPDATE 0`/COMMIT rc0, OID/ACL/trigger/catalog/registry không đổi. Không INSERT dương test hay luật thật, không V3.

## P101 — ĐẦU VÀO THỰC THI ĐÃ CỤ THỂ HÓA (Claude P100: 5 điểm)
**T1 · KHÔNG BẪY MANIFEST:** Kiểm NGỮ PHÁP dùng trực tiếp `python3 /opt/incomex/dot/lib/dot-pg-s4-luat-validate.py <fixture>` (trên Mac dùng candidate tương ứng); fixture âm/dương ở thư mục tạm RUN **ngoài** `sql/s4-luat/`. Wrapper `--check` chỉ dùng để thử riêng khóa đường dẫn/manifest/hash và chính smoke đã được phê duyệt. Wrapper kiểu label kiểm manifest **trước validator**, nên không dùng lỗi từ manifest làm bằng chứng ngữ pháp bị chặn. Test dương INSERT tuyệt đối không có trong manifest. **Manifest production chỉ có đúng một dòng**, đó là SHA + path đến file smoke UPDATE 0.
**T2 · LÙI ĐÚNG CONFIG GUARD:** Chuẩn bị candidate DISABLED của chính wrapper (in `S4_LUAT_GATE_DISABLED`, `exit 1`, không gọi PostgreSQL) trong hồ sơ RUN. Khi cần lùi: `incomex-config-apply-v0` cập nhật **nội dung target wrapper đã đăng ký**, đồng thời cập nhật approved baseline tương ứng để Config Guard MATCH/POST; không đổi tên, không xóa script/registry/manifest. Wrapper phiên bản chạy được lưu trong bản `.pre` của mutation này, bật lại cũng qua apply-v0 sau quyền riêng. S1 xác minh command `--help`, mẫu triplet/backup đúng P96; không buộc chạy rollback thật khi chưa có regression.
**T3 · TRANSACTION PG KHÔNG ĐỂ AGENT TỰ LẮP:** Wrapper copy file input đã xác thực sang snapshot tạm `0600` **một lần** (trap xoá), kiểm tối đa **2 MiB / 2.000 câu**, hash snapshot so với một dòng manifest, chạy validator trên snapshot, sau đó chạy CHÍNH snapshot, không đọc file input lần hai (TOCTOU). Dùng dạng lệnh cố định dưới đây, trong đó `DO` chỉ do wrapper tin cậy tạo, **không** đọc từ file luật:
```bash
docker exec -i postgres psql -X -U workflow_admin -d directus \
  -1 -v ON_ERROR_STOP=1 \
  -c "LOCK TABLE public.tai_san_luat IN SHARE ROW EXCLUSIVE MODE;
DO \$s4\$ BEGIN
  IF EXISTS (SELECT 1 FROM pg_trigger WHERE tgrelid='public.tai_san_luat'::regclass AND NOT tgisinternal)
     OR EXISTS (SELECT 1 FROM pg_rewrite WHERE ev_class='public.tai_san_luat'::regclass)
  THEN RAISE EXCEPTION 'S4_TRIGGER_OR_RULE_BLOCKED'; END IF;
END \$s4\$;" \
  -f - < "$SNAPSHOT"
```
Theo tài liệu PG18, `-1` gộp `-c` và `-f` vào một giao dịch; `LOCK` xảy ra trước `DO`, rồi mới SQL file. Nếu rule/trigger không nội bộ xuất hiện ⇒ exception, toàn bộ rollback; nếu một dòng lỗi thì ROLLBACK toàn batch. P100 đã diễn tập PG16 3 tình huống, production chỉ chạy **một smoke UPDATE 0**. Smoke chỉ được chạy khi `tai_san_luat` vẫn 0 dòng và target `kiem-thu-khong-ton-tai` vắng mặt, kiểm trước/sau; không dùng lệnh DO lạ viết từ fixture.
**T4 · ĐIỀU 30/31:** Điều 30 = chạy lại âm/dương bằng validator trực tiếp trên code **đã cài**, cộng riêng test wrapper khóa 1–3 trên path/symlink/unapproved/tamper (tamper tại fixture cô lập, không sửa live manifest). Điều 31 = 3 target Guard (wrapper + validator + manifest) MATCH và Guard POST đúng footprint + receipt. **Không có bước tìm `code ledger` riêng.**
**T5 · KHÔNG DÙNG LEGACY:** Không gọi `dot-dot-register` (TS2 P60 đã dừng). Ghi purpose ở đầu wrapper theo mẫu label-apply. S5 chỉ kiểm `dot-dot-catalog --check` nếu đã xác nhận read-only; thiếu tên mới không chặn/không tự sync.
**Các cổng độc lập:** S0 xác minh G2 mới + READY đúng PROMPT + 0 STOP và VPS-GHI TRỐNG; nguồn DOT runtime VPS là chuẩn. Nhận thấy HJW đang giữ VPS-GHI tại lúc P100, **Owner không dispatch vào CLI khi lease còn bận**. Bảo toàn Git DOT dirty (P98 226 modified/34 untracked), manifest S4 trước đó vẫn ở baseline, không checkout/reset/add-A.

## INPUT READY TABLE · DROOT60 · Host P102 (trước READY, không mở precheck RUN)
| Nguồn đầu vào | HOST_VERIFIED và bằng chứng | EXECUTOR_FRESHNESS ở S0/S1 của cùng RUN |
|---|---|---|
| Quyền Owner/G2 và scope | P102 `HUMAN_DIRECTIVE@NDW-TS4-S4-LUAT-GATE-OWNER-G2-20261029`; 1 DOT hẹp + 3 Guard targets + 1 smoke UPDATE 0, không INSERT luật | đọc lại G2, READY full SHA, STOP/HOLD/STARTED |
| Hội đồng/vai | COLLAB `COUNCIL_BOOTSTRAP_V1` có GPT Chat Host, Claude Chat Reviewer P98/P100, Claude Code CLI Worker/AUTO0; P101 đã chốt 5 sửa | kiểm council alert mới/role executor trong RUN |
| Đường ghi & parser nguồn | P96 sử dụng DOT/Config Guard/live manifest+apply-v0 thành công, P100 đọc `dot-pg-label-apply` dòng 139–157 và importlib `tach_cau_lenh`; P101 đã đóng các lỗ. Không dùng Git DOT bẩn để deploy | S1 đọc code live, path/mode/khả năng psql, 3 path chưa tồn tại, --help, import, 17+ fixture; chỉ tạo sau PASS |
| PG & tiêu chí kết quả | P96 S4 OID296646 14 cột/0 dòng, role workflow_admin, P98 PG18 đọc RO xác nhận; PG16 lock + DO + psql -1 đã thử 3 ca P100 | S1 PG18 thực tế đúng container/role/metadata, row 0; S3 UPDATE 0/PG metadata không đổi |
| Config Guard & rollback | P96 Config Guard 556/556, apply-v0 quản registry/manifest + .pre, P100 đường lùi DISABLED trên cùng Guard target, không đổi tên/xóa | S1 drift-check baseline sống/--help và đường lùi, Guard PRE; S5 drift MATCH/POST; nếu lỗi dùng apply-v0 đúng phạm vi |
| VPS-GHI/nguồn lực | Root COLLAB lần Host đọc: VPS-GHI trống sau HJW P468 trả cờ 10:47Z; đây chỉ là mốc | S0/S2 CAS/PSI/RAM/STOP/Guard/HEAD tươi, fail thực ⇒ dừng an toàn; không chờ ở terminal |
| Code mới và âm/dương | N/A trước khi xây: chưa có wrapper/validator TS4 nên không giả test PASS; mục tiêu ≤2MiB/2000 statements, 1 smoke duy nhất được Owner duyệt | S1 candidate test, S2 installed direct validator test + wrapper key tests; S3 đúng 1 UPDATE 0 |

**Chỉ EXECUTOR_FRESHNESS và kiểm thử chính sản phẩm được tạo trong RUN mới được để Agent đo khi chạy; phần nguồn/danh tính/permission/scope đã được Host đối chiếu P96/P98/P100/P101 và G2 P102.**

## S0 — Gates, STARTED riêng, không tranh cờ
(1) Owner `HUMAN_DIRECTIVE@NDW-TS4-S4-LUAT-GATE-OWNER-G2-20261029` P102 đã có, (2) Host P103 `READY@full last-touch PROMPT SHA` trong COLLAB, (3) Owner chuyển đúng câu DROOT38, (4) 0 STOP/HOLD/COUNCIL_ALERT OPEN/STARTED trùng, VPS-GHI trống và resources/PSI tươi, (5) WRITE_PATH workspace+VPS binding và code/runtime/Guard S1 theo INPUT READY TABLE. PASS ⇒ `STARTED@NDW-TS4-S4-LUAT-GATE-20261029-01 <UTC> · executor=Claude Code CLI` ghi task COLLAB commit RIÊNG trước S1; nếu fail chính xác thì STOP 0 mutation, không hỏi lại G2.

## S1 — PRE (Mac candidate / VPS read-only, chưa lấy quyền ghi)
- S1 đọc-only đúng file runtime `dot-pg-label-apply`/`dot-pg-label-validate.py` (`tach_cau_lenh`, `importlib`), `dot-pg-atomic-apply` để đối chiếu (không sửa), registry/config apply-v0 --help + mẫu P96 rollback. **Không gọi `dot-dot-register`**; không khảo sát legacy ngoài footprint.
- Đo `/opt/incomex/dot` dirty hiện hành (P98 thấy ≈226 modified +34 untracked; manifest live lệch HEAD 8 dòng), snapshot owner/mode/ACL và các tệp cùng mẫu; verify Config Guard drift-check MATCH, `tai_san_luat` OID 296646/14 cột/rowcount0/ACL P96 chưa đổi; exact 3 path mới chưa có (nếu có collision: DỪNG, không overwrite). Kiểm **kết nối PG18 production theo chính đường sẽ chạy ở S3**, nhưng READ ONLY: `docker exec -i postgres psql -X -U workflow_admin -d directus -v ON_ERROR_STOP=1 -c 'SELECT current_user, current_database();'` (0 ghi/0 lock), xác minh tên container/role/DB và khả năng `DO` qua danh mục `pg_language`, trước khi tạo wrapper; không suy từ thử PG16 rằng production chắc chắn PASS. Với source PG-S4, so hash cấu trúc cột/ràng buộc/chỉ mục hiện tại với mốc P96 theo cùng truy vấn nếu sẵn, hoặc so metadata canonical cột/CHECK/index/default/role trong một lượt RO; khác footprint thì dừng **trước S2**, không tự sửa.
- S1 candidate Mac/staging: kiểm NGỮ PHÁP bằng **gọi trực tiếp validator** trên ≥17 fixture âm + dương P98 (qt001_/birth_registry/meta_catalog trong literal, nhiều VALUES, chuỗi `;`/`--`/`/*`/`''`), tất cả nằm ngoài `sql/s4-luat/`, không trong manifest. Kiểm khóa path/manifest/SHA riêng trên wrapper candidate và test file giả cô lập, không phá file protected. Không dùng wrapper --check làm bằng chứng validator đúng; không chạy INSERT dương vào PG prod.
- S1 chứng minh đường lùi bằng `incomex-config-apply-v0 --help`, P96 triplet/registry/`.pre`, candidate wrapper DISABLED `exit 1` sẵn sàng và kế hoạch Guard MATCH; không thử đổi tên, không ghi prod để «chứng minh». Nếu tool thật thiếu quyền hoặc không có baseline hợp lệ thì dừng **trước S2** và báo blocker cụ thể.

## S2 — One bounded production install; Config Guard bảo vệ ngay
- S2 install đúng wrapper/validator/manifest và đúng một SQL smoke; **manifest production chỉ 1 line smoke SHA/path**, không cất fixture thử trong `sql/s4-luat/`. Mode chủ theo P100 root:root: wrapper 755, các tệp khác 644. Không overwrite file cũ, không debug bypass.
- S2 qua apply-v0 ghi đúng 3 target Guard mới wrapper/validator/manifest; bảo toàn registry cũ. **Điều 30 = kiểm lại trực tiếp validator các fixture âm/dương và các khóa wrapper 1–3 trên code đã cài**; **Điều 31 = 3 target MATCH + Guard POST/receipt**. Không chạy/tìm `code ledger`, không gọi dot-dot-register.
- Sau cài code thật: (a) direct `python3 /opt/incomex/dot/lib/dot-pg-s4-luat-validate.py <fixture>` âm/dương phải giống candidate; (b) wrapper `--check` CHỈ smoke được manifest duyệt PASS; (c) wrapper khóa 1–3 sai path/symlink/không manifest/hash lệch FAIL, test hash/tamper trên bản staging riêng, không sửa file Guard canh. Manifest luôn 1 dòng, không sinh INSERT fixture được duyệt.

## S3 — Một smoke 0 row trong cùng transaction
- S3 kiểm lại READY/STOP/root lease và snapshot SQL 0600, bảng S4 vẫn 0 rows/OID/ACL đúng. Wrapper dùng `psql -1` một lần theo command mẫu P101: `-c` LOCK+DO kiểm trigger/rule, `-f -` nhận đúng snapshot; `UPDATE 0`, COMMIT rc0, rowcount 0→0, không DDL/role/trigger. Một statement lỗi ⇒ toàn bộ ROLLBACK, không chạy lại tùy tiện.
- Gặp thay đổi dữ liệu thật hoặc write ngoài scope ⇒ STOP, áp đường disable có Guard MATCH theo S1, ghi KQ MỘT PHẦN, không tự chạy lệnh sửa/DELETE.

## S4–S5 — Guard POST, KQ/lease trả
- S4–S5 Guard MATCH 3 targets + registry/POST footprint/receipt; Điều 30 validator+wrapper tests, Điều 31 Guard+POST, không code ledger. Nếu có regression trong scope, apply-v0 thay wrapper bằng DISABLED `exit 1` và cập nhật target approved baseline để Guard xanh, không đổi tên/DELETE/PG schema. #24 đỏ sẵn khác chủ không rollback.
- KQ: bản SHA/bytes wrapper/validator/manifest và **1 smoke**; số 17+ fixture âm/dương chạy validator trực tiếp, khóa wrapper 1–3, test candidate vs installed, psql lock/DO/UPDATE 0/COMMIT, rowcount/metadata/Guard PRE-POST và đường lùi apply-v0 DISABLED, unchanged DOT Git/worktree, không dot-dot-register, receipt/cờ trả; NEXT_TRIGGER=GPT_HOST_NGHIEM_THU_TS4_GATE_THEN_OWNER_APPROVE_FIRST_RULE_BATCH_AND_V3. Cấm viết luật/V3/Web.

## DROOT48 · STEP_WALK
| Bước | Surface | Trigger/deadline | Evidence | Hỏng |
|---|---|---|---|---|
| S0 | Claude Code CLI | Owner dispatch sau G2/READY; ≤5′ | G2 + PROMPT SHA/STOP/lease + STARTED commit riêng | DỪNG |
| S1 | Claude Code CLI | S0, ≤25′ Mac candidate/RO VPS | importlib; direct validator 17+ âm/dương và wrapper keys 1–3 riêng, DISABLED apply-v0 plan | DỪNG trước production nếu thực sự fail |
| S2 | Claude Code CLI | S1 PASS+lease/Guard PRE, ≤20′ | 3 Guard targets, manifest 1 smoke, test direct validator trên bản cài+key checks | DỪNG/MỘT PHẦN đúng footprint |
| S3 | Claude Code CLI | S2 PASS, ≤8′ | một psql -1 -c lock/DO -f -, UPDATE 0/COMMIT, rowcount0→0 | disable qua apply-v0/Guard MATCH nếu regression |
| S4–S5 | Claude Code CLI | S3; ≤10′ | Guard POST/receipt, KQ, cờ trả | Host nghiệm thu |
Hard stop 75′ (đủ thời gian dựng strict validator + 17+ ca kiểm; không bị cắt ở phút 12 chỉ vì đang phát triển), không giữ terminal chờ hay chạy nền. Nếu có input/rollback chưa sẵn thì DỪNG **trước** thay đổi production; không sửa thêm quyền/Guard/code ngoài scope.
