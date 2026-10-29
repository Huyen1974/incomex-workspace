# NDW TS3/S4 · SỔ LUẬT 1 BẢNG P91 (4 Ô NULL/KẾ THỪA; MẪU HỌ NEO DB; V3 SAU TS4)
RUN_ID: NDW-TS3-S4-ONE-RULE-TABLE-20261029-02
TASK: work/nhap-directus-for-workflow
EXECUTOR_SURFACE: Claude Code CLI
STATUS: OWNER_APPROVED_G1G2@P94 · CONDITIONAL_READY. Executable ONLY when task COLLAB contains Host READY@the exact full last-touch commit SHA of this PROMPT, Owner manually dispatches, and S0 PASS; otherwise BLOCKED. This authorizes one empty S4 rules table only, not rule insertion, report publication, role changes or DROP. REVIEW_REUSED=P91/P93.

READ_PATH: AGENTS.md A0/A6/R1a/R1b/R3/R4/DROOT30/31/48/58 → root COLLAB VPS-GHI → task COLLAB §0/Bảng/§3.TQ/§3.KH, P73/P75/P81/P85/P86/P88/P89/P90/**P91/P92** (SQL P91 và giới hạn triển khai TS4/V3) → PROMPT này. PG qua `query_pg` READ ONLY; VPS S1 chỉ SSH đọc. Không lôi P0 Nuxt, Graph, TS4 data writer/V3 vào RUN CREATE S4 này.
WRITE_PATH: hai SQL file mới `/opt/incomex/dot/sql/directus/`, baseline+2 registry IDs, 2 approved SQL manifest lines qua `incomex-config-apply-v0`, đúng một `dot-pg-atomic-apply`, STARTED/KQ task COLLAB qua `workspace_edit`. KHÔNG psql/docker exec/Directus REST/Studio tay, không thay role/ACL của bảng cũ, không `git add/commit` trong `/opt/incomex/dot`, không tạo collection/report/Flow/job/index ngoài SQL đã duyệt, không viết một luật nào.

## Đích & SQL P91 bất biến · P92 Host ACCEPT C1/C2/C3
- Tạo đúng **một bảng** `directus.public.tai_san_luat`, **14 cột**, PK `ma`, partial UNIQUE index `tai_san_luat_mot_mau`. C1: 4 ô `he/workflow/vung/quyet_dinh` **NULL được phép**, nghĩa là không phát biểu, sẽ kế thừa khi V3 đọc; CHECK `num_nonnulls(he, workflow, vung, quyet_dinh) >= 1` và các CHECK P91 `ho_neo, ho_regex, ho_chi_giu, oid, vat_khoa`. C2 mẫu họ neo `^pg:<db>:` / `^ext:<db>:` / `^dot:` nhưng prefix CHECK không kiểm mọi nhánh regex; dữ liệu luật chỉ nhập khi TS4 DOT writer kiểm full pattern/âm tính DB khác. **0 DÒNG** lúc tạo, không nạp 158 ứng viên. Không thêm `tai_san_he`/`tai_san_quyet_dinh`, không tạo V3/Graph/Nuxt/report trong RUN này. `pg_catalog` giữ vật, bảng S4 chỉ giữ luật Owner, nhãn COMMENT cũ là evidence.
- Tệp ÁP `directus/ndw-s4-luat.sql` = **nguyên SQL P91** 45 dòng LF cuối, **4.782 B SHA256 `90424a188eaa28d25339e47489656c6dfa9ff5712fa728599eeabf5f6e157f86`**. Host đã băm lại nguyên khối P91 độc lập khớp. Tệp LÙI `directus/ndw-s4-luat-lui.sql` = nguyên SQL lùi P89 **412 B SHA256 `fc88ca914fc1a6145f04cd7d86dba20e53c7e459d204b36bbe59e1632c9dbf2b`**; soft rollback REVOKE+COMMENT, **KHÔNG DROP**. Sai byte/SHA ⇒ DỪNG 0 PG mutation, không sửa ad hoc; cấm dùng SQL áp cũ P89 4.309 B SHA `fb5d30fc`.
- Chủ `workflow_admin`, SELECT `context_pack_readonly`; vai `directus` kế thừa SELECT như PG-A2b, nhưng DML phải false. Các quyền đọc HTTP không được mở vì không đăng ký collection/permission/`table_registry`. S4 là khung luật 0 dòng, **không tự gán Giữ/Bỏ hoặc bật bất kỳ thay đổi runtime**.
- Evidence P91: 22 ca PG16 mô phỏng prod + cổng guardrail PASS, PG18 chỉ đo RO trên CTE 4,8s/0 xung đột ở snapshot; prod PG18 chưa CREATE DDL P91. P92 Host nhận hai rào TS4: prefix neo DB không ngăn nhánh `|` vượt DB; hiệu lực `tat/bo` kế thừa xuống con chỉ là HIỂN THỊ, không là ủy quyền thao tác con. RUN này chỉ DDL bảng rỗng nên không cần nạp/bộ resolver V3, S1 vẫn kiểm runtime/guardrail/selftest trước S2.

## S0 · Gate đọc trước và STARTED commit RIÊNG
Xác minh Owner G1/G2 trực tiếp **P91/P92**, Host READY@full last-touch SHA đúng PROMPT (DROOT58), Owner chuyển câu chuẩn DROOT38, 0 STOP_REQUESTED/HOLD/COUNCIL_ALERT OPEN/STARTED trùng RUN, VPS-GHI trống và RAM/PSI đủ. PASS ⇒ ghi `STARTED@NDW-TS3-S4-ONE-RULE-TABLE-20261029-02 <UTC> · executor=Claude Code CLI` vào COLLAB task **một commit riêng** trước S1; không ghi được ⇒ DỪNG.

## S1 · Kiểm PRE chỉ đọc + DOT selftest 0 dấu vết
1. PG18.6 qua `query_pg`: `tai_san_luat` chưa có trong `pg_class`/`pg_type`, tên `tai_san_luat_mot_mau` và CHECK `tai_san_luat_ho_neo`/`tai_san_luat_co_noi_dung` chưa xung đột; V1/V2 P85 còn sống; membership `directus→context_pack_readonly`, default ACL và `workflow_admin CREATE ON public` đúng P91; `trigger_guard_alerts` baseline sống (mốc 129 chỉ là lịch sử), `evt_trigger_guard_ddl` không đổi hành vi; 0 Directus collection/permission/`table_registry` nhắc S4.
2. Dựng trên Mac **SQL P91 4.782 B SHA `90424a18…7f86`** + rollback P89 412 B SHA `fc88ca91…dbf2b`, so đủ SHA byte chính xác; VPS 2 SQL path chưa tồn tại; registry `dot-sql-ndw-s4-luat`/`dot-sql-ndw-s4-luat-lui` chưa có. Cổng `dot-pg-atomic-apply` live SHA `e1307be7ab06b1c4c705294ff03fdd8678410621d856c9b383a1496c278e962e`, guardrail 2 SQL PASS; DOT selftest `_selftest/atomic_happy.sql` TEMP ON COMMIT DROP, rc=0/COMMIT; không thử CREATE TABLE thủ công trên production.
3. Config Guard `guard-registry` + `dot-sql-approved-manifest` MATCH; live manifest baseline P85 18 dòng SHA bắt đầu `18ae52f1` chỉ là mốc, nếu đã thay hợp lệ đọc cả baseline sống/giữ nguyên mọi dòng cũ; mẫu registry 9 cột; apply-v0 --help có `--mutation-id --agent --target-id --candidate --expected-baseline`; F1 ACL cũ/F2 6 Git lines dirty giữ nguyên, không tự `setfacl`/git stage/commit/reset.
4. Không có blocker footprint ⇒ mới lấy VPS-GHI CAS và Guard PRE. Bất kỳ quyền thực tế/guardrail/trigger/SHA/rollback nào lệch => KQ DỪNG 0 PG DDL, không sửa ngoài scope hay tự retry. Không kiểm vòng lặp 3 DB/Graph vô ích.

## S2 · Ghi đúng footprint chỉ sau S1 PASS
2.1 Install đúng hai tệp SQL vào `/opt/incomex/dot/sql/directus/` cùng owner/mode như P85; sha256 trên VPS phải đúng.
2.2 Theo mẫu baseline triplet `{content,sha256,meta}`, đăng ký 2 id trong Config Guard + thêm 2 hàng registry qua `incomex-config-apply-v0 --target-id guard-registry`, APPLIED/MATCH.
2.3 Thêm vào manifest sống đúng 2 dòng `<sha256><TAB>directus/ndw-s4-luat.sql` và `<sha256><TAB>directus/ndw-s4-luat-lui.sql`, LF cuối và giữ byte nguyên các dòng cũ; qua `incomex-config-apply-v0 --target-id dot-sql-approved-manifest`, APPLIED/MATCH. Ghi ACL trước/sau, không khôi phục tay hoặc commit Git DOT.
2.4 Chạy **đúng một lần** `dot-pg-atomic-apply directus/ndw-s4-luat.sql`. Fail: PG rollback giao dịch; KQ DỪNG/MỘT PHẦN theo footprint files/Guard đã ghi (không tô 0 ghi giả), không retry/DROP.

## S3 · Đọc nghiệm thu qua `query_pg` RO
- Có đúng một bảng `public.tai_san_luat` **14 cột và 0 dòng**, owner workflow_admin, PK ma + partial unique index `tai_san_luat_mot_mau`, đầy đủ CHECK P91 `tai_san_luat_vat_khoa`, `tai_san_luat_ho_neo`, `tai_san_luat_ho_regex`, `tai_san_luat_oid`, `tai_san_luat_ho_chi_giu`, `tai_san_luat_co_noi_dung`; `he/workflow/vung/quyet_dinh` phải **nullable**, CHECK `num_nonnulls>=1` tồn tại; comment/relacl P91 chính xác. `context_pack_readonly` SELECT true/DML false, `directus` SELECT kế thừa true/DML false, role ngoài nhóm SELECT false. Không tạo role/trigger/collection/permission/`table_registry`; `trigger_guard_alerts` delta=0.
- V1 đối chiếu Census cùng snapshot: dự kiến +1 bảng/+14 cột/+2 index, V2 ~+2 index→table edges; vì nguồn sống có thể thay đổi chỉ báo chính xác chênh theo loại, không dùng tổng P85 cố định để giả fail/pass. Chụp OID, relacl, catalog columns/constraints/index/comments hash làm mốc Điều 30/31 (PG core không có `pg_get_tabledef`).
- **Không thực thi** 158 luật ứng viên, không test INSERT/UPDATE production khi Owner chỉ duyệt tạo bảng 0 dòng, không tạo V3/báo cáo. CHECK `ho_neo` chỉ rào prefix textual, không chứng minh cách ly toàn biểu thức regex; UNIQUE chỉ chặn mẫu giống nhau, không chứng minh 0 overlap. Gate TS4 data writer/VIEW V3 nằm lượt sau, kiểm đầy đủ trước lô luật đầu.

## S4–S5 · POST/lùi/KQ và trả cờ
Config Guard 2 SQL targets + registry + manifest = MATCH, Guard POST đúng footprint thật, Điều 30/31, biên nhận Telegram message_id. Nếu regression thật sau COMMIT đúng footprint S4 thì qua DOT chạy SQL lùi 1 lần (REVOKE+COMMENT, schema vẫn còn), KQ MỘT PHẦN/Host; PREEXISTING RED khác chủ không rollback. KQ ghi STARTED riêng, 2 mutation receipts/sha trước-sau, SQL SHA, OID/schema/ACL/0 rows/trigger delta, Guard PRE/POST, VPS-GHI trả, không tệp tạm/process. NEXT_TRIGGER=GPT_HOST_NGHIEM_THU_S4_THEN_DOT_TS4_WRITER_GATE. Không mở Graph/V3/TS4/Web hoặc lô luật trong RUN này.

## DROOT48
| Bước | Ai | Trigger/hạn | Evidence | Hỏng |
|---|---|---|---|---|
| S0 | Claude Code CLI | Owner chuyển sau Host READY, ≤5′ | Owner G1G2 P91/P92 + READY SHA + STARTED riêng | DỪNG |
| S1 | Claude Code CLI | S0, ≤10′ | PG18 role/trigger + SQL bytes/guardrail/selftest + Guard MATCH | DỪNG 0 PG DDL |
| S2 | Claude Code CLI | S1+VPS-GHI/Guard PRE, ≤15′ | 2 SQL files +2 registry +2 manifest, 1 DOT atomic commit | DỪNG/MỘT PHẦN đúng footprint |
| S3 | Claude Code CLI | S2, ≤10′ | 1 bảng 14 cột/0 dòng/ACL/check/index/trigger | lùi mềm nếu regression |
| S4–S5 | Claude Code CLI | S3, ≤10′ | Guard POST/receipt, KQ, cờ trả | Host nghiệm thu |
Hard stop 55 phút; không chạy nền/không chờ Owner tại terminal.
