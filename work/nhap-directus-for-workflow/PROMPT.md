# NDW TS3/S4 · TẠO MỘT BẢNG LUẬT CHO PHÂN LOẠI TÀI SẢN (SSOT RULES)
RUN_ID: NDW-TS3-S4-ONE-RULE-TABLE-20261029-02
TASK: work/nhap-directus-for-workflow
EXECUTOR_SURFACE: Claude Code CLI
STATUS: **DRAFT · OWNER G1/G2 S4 P90 CHƯA CÓ · HOST CHƯA READY · OWNER CHƯA DISPATCH. CẤM RUN/STARTED/MUTATION.** P88 hai bảng `NDW-TS3-S4-TWO-TABLES-20261029-01` SUPERSEDED; P83/P84 chỉ phê duyệt V1/V2 cũ, không được tái dùng. Chỉ khi có (1) Owner trực tiếp duyệt đúng 1 bảng S4 theo P90/P89; (2) Host ký `READY@<full last-touch PROMPT SHA>` ở commit sau, REVIEW_REUSED=P89; (3) Owner chuyển câu DROOT38 (AUTO0); (4) S0 PASS thì mới được thực thi.

READ_PATH: AGENTS.md A0/A6/R1a/R1b/R3/R4/DROOT30/31/48/58 → root COLLAB VPS-GHI → task COLLAB §0/Bảng/§3.TQ/§3.KH, P73/P75/P81/P85/P86/P88/P89/P90 → PROMPT này. PG qua `query_pg` READ ONLY; VPS S1 chỉ SSH đọc. Không lôi P0 Nuxt, Graph, TS4 data writer vào RUN CREATE này.
WRITE_PATH: hai SQL file mới `/opt/incomex/dot/sql/directus/`, baseline+2 registry IDs, 2 approved SQL manifest lines qua `incomex-config-apply-v0`, đúng một `dot-pg-atomic-apply`, STARTED/KQ task COLLAB qua `workspace_edit`. KHÔNG psql/docker exec/Directus REST/Studio tay, không thay role/ACL của bảng cũ, không `git add/commit` trong `/opt/incomex/dot`, không tạo collection/report/Flow/job/index ngoài SQL đã duyệt, không viết một luật nào.

## Đích & SQL P89 bất biến
- Tạo đúng **một bảng** `directus.public.tai_san_luat`, 14 cột/PK `ma`/partial UNIQUE `tai_san_luat_mot_mau`, CHECK P89 (`muc=ho` chỉ `giu/chua_quyet`; `muc=vat` PG có OID; key, can_cu nonblank). **0 DÒNG.** Không tạo `tai_san_he`/`tai_san_quyet_dinh`, không nạp 158 luật ứng viên, không chép 16.536 tài sản, không thêm V3, Graph, Nuxt/report. SSOT vật là PG catalog, SSOT luật duyệt là bảng này; nhãn COMMENT cũ chỉ làm căn cứ, không thay nguồn nghiệp vụ.
- Tệp ÁP `directus/ndw-s4-luat.sql` = **nguyên khối SQL P89** (43 dòng, LF cuối) **4.309 bytes sha256 `fb5d30fc83e97ed236fbe033ccea565ead83a8d07801eced27fad05502ce5193`**. Tệp LÙI `directus/ndw-s4-luat-lui.sql` = SQL lùi P89 **412 bytes sha256 `fc88ca914fc1a6145f04cd7d86dba20e53c7e459d204b36bbe59e1632c9dbf2b`** (chỉ REVOKE+COMMENT, không DROP). Sai byte/SHA ⇒ DỪNG, không chỉnh ad hoc.
- Chủ `workflow_admin`, SELECT `context_pack_readonly`; vai `directus` kế thừa SELECT như PG-A2b, nhưng DML phải false. Các quyền đọc HTTP không được mở vì không đăng ký collection/permission/`table_registry`. S4 là khung luật 0 dòng, **không tự gán Giữ/Bỏ hoặc bật bất kỳ thay đổi runtime**.
- P89 đo `query_pg` RO prod PG18: tên bảng/index/constraint còn trống, vai workflow_admin CREATE có thật, `trigger_guard_alerts` mốc 129 lúc 29/10, code Guard hiện hữu; PG16 giả lập runtime với 15 ca đúng, cổng SQL giả lập PASS. Chưa chứng minh CREATE PG18 live trước S2; S1 kiểm trực tiếp quyền thật và selftest DOT nonpersistent rồi S2 một giao dịch.

## S0 · Gate đọc trước và STARTED commit RIÊNG
Xác minh Owner G1/G2 trực tiếp P90, Host READY@full last-touch SHA đúng PROMPT (DROOT58), Owner chuyển câu chuẩn DROOT38, 0 STOP_REQUESTED/HOLD/COUNCIL_ALERT OPEN/STARTED trùng RUN, VPS-GHI trống và RAM/PSI đủ. PASS ⇒ ghi `STARTED@NDW-TS3-S4-ONE-RULE-TABLE-20261029-02 <UTC> · executor=Claude Code CLI` vào COLLAB task **một commit riêng** trước S1; không ghi được ⇒ DỪNG.

## S1 · Kiểm PRE chỉ đọc + DOT selftest 0 dấu vết
1. PG18.6 qua `query_pg`: `tai_san_luat` chưa tồn tại ở `pg_class`/`pg_type`, tên `tai_san_luat_mot_mau`/constraints chưa xung đột; V1/V2 P85 còn đọc sống; role membership `directus→context_pack_readonly`/default ACL và `workflow_admin CREATE ON public` đúng P89; `trigger_guard_alerts` đọc baseline sống (mốc 129 lịch sử, không ép), `evt_trigger_guard_ddl` không thay đổi logic từ P89; không có Directus collection/permission/`table_registry` nhắc S4.
2. Dựng trên Mac **hai SQL P89 đúng SHA** và kiểm SHA trên tệp chưa có trên VPS; 2 registry IDs `dot-sql-ndw-s4-luat`/`dot-sql-ndw-s4-luat-lui` chưa tồn tại; cổng `dot-pg-atomic-apply` sống SHA `e1307be7ab06b1c4c705294ff03fdd8678410621d856c9b383a1496c278e962e`, guardrail hai SQL PASS; DOT selftest `_selftest/atomic_happy.sql` TEMP ON COMMIT DROP + approved manifest, rc=0/COMMIT. **Không CREATE thử bằng psql hay DOT lên production** tại S1.
3. Config Guard `guard-registry` + `dot-sql-approved-manifest` MATCH; live manifest baseline P85 18 dòng SHA bắt đầu `18ae52f1` chỉ là mốc, nếu đã thay hợp lệ đọc cả baseline sống/giữ nguyên mọi dòng cũ; mẫu registry 9 cột; apply-v0 --help có `--mutation-id --agent --target-id --candidate --expected-baseline`; F1 ACL cũ/F2 6 Git lines dirty giữ nguyên, không tự `setfacl`/git stage/commit/reset.
4. Không có blocker footprint ⇒ mới lấy VPS-GHI CAS và Guard PRE. Bất kỳ quyền thực tế/guardrail/trigger/SHA/rollback nào lệch => KQ DỪNG 0 PG DDL, không sửa ngoài scope hay tự retry. Không kiểm vòng lặp 3 DB/Graph vô ích.

## S2 · Ghi đúng footprint chỉ sau S1 PASS
2.1 Install đúng hai tệp SQL vào `/opt/incomex/dot/sql/directus/` cùng owner/mode như P85; sha256 trên VPS phải đúng.
2.2 Theo mẫu baseline triplet `{content,sha256,meta}`, đăng ký 2 id trong Config Guard + thêm 2 hàng registry qua `incomex-config-apply-v0 --target-id guard-registry`, APPLIED/MATCH.
2.3 Thêm vào manifest sống đúng 2 dòng `<sha256><TAB>directus/ndw-s4-luat.sql` và `<sha256><TAB>directus/ndw-s4-luat-lui.sql`, LF cuối và giữ byte nguyên các dòng cũ; qua `incomex-config-apply-v0 --target-id dot-sql-approved-manifest`, APPLIED/MATCH. Ghi ACL trước/sau, không khôi phục tay hoặc commit Git DOT.
2.4 Chạy **đúng một lần** `dot-pg-atomic-apply directus/ndw-s4-luat.sql`. Fail: PG rollback giao dịch; KQ DỪNG/MỘT PHẦN theo footprint files/Guard đã ghi (không tô 0 ghi giả), không retry/DROP.

## S3 · Đọc nghiệm thu qua `query_pg` RO
- Có đúng một bảng `public.tai_san_luat` với **14 cột, 0 rows**, owner workflow_admin, PRIMARY KEY ma, partial unique index `tai_san_luat_mot_mau`, CHECK P89 `tai_san_luat_vat_khoa/ho_regex/oid/ho_chi_giu`, comments/relacl chính xác. `context_pack_readonly` SELECT OK/DML false, `directus` SELECT kế thừa và DML false, role lạ không đọc. 0 role, không thêm Directus collection/permission/`table_registry`, không có trigger mới, `trigger_guard_alerts` delta 0.
- V1 đối chiếu Census cùng snapshot: dự kiến +1 bảng/+14 cột/+2 index, V2 ~+2 index→table edges; vì nguồn sống có thể thay đổi chỉ báo chính xác chênh theo loại, không dùng tổng P85 cố định để giả fail/pass. Chụp OID, relacl, catalog columns/constraints/index/comments hash làm mốc Điều 30/31 (PG core không có `pg_get_tabledef`).
- **Không thực thi các luật ứng viên hoặc test INSERT/UPDATE thật** khi Owner chỉ duyệt tạo bảng 0 dòng. Luật họ chỉ Giữ/Chưa quyết từ CHECK, nhưng không có kiểm trùng regex khác nhau ở mức DB; đó là gate riêng khi TS4 nạp lô luật, không gọi đã giải quyết.

## S4–S5 · POST/lùi/KQ và trả cờ
Config Guard 2 SQL targets + registry + manifest = MATCH, Guard POST đúng footprint thật, Điều 30/31, biên nhận Telegram message_id. Nếu regression thật sau COMMIT đúng footprint S4 thì qua DOT chạy SQL lùi 1 lần (REVOKE+COMMENT, schema vẫn còn), KQ MỘT PHẦN/Host; PREEXISTING RED khác chủ không rollback. KQ ghi STARTED riêng, 2 mutation receipts/sha trước-sau, SQL SHA, OID/schema/ACL/0 rows/trigger delta, Guard PRE/POST, VPS-GHI trả, không tệp tạm/process. NEXT_TRIGGER=GPT_HOST_NGHIEM_THU_S4_THEN_DOT_TS4_WRITER_GATE. Không mở Graph/V3/TS4/Web hoặc lô luật trong RUN này.

## DROOT48
| Bước | Ai | Trigger/hạn | Evidence | Hỏng |
|---|---|---|---|---|
| S0 | Claude Code CLI | Owner dispatch sau READY; ≤5′ | G1/G2 P90 + READY SHA + STARTED commit riêng | DỪNG |
| S1 | Claude Code CLI | S0, ≤10′ | PG18 role/trigger + SQL bytes/guardrail/selftest + Guard MATCH | DỪNG 0 PG DDL |
| S2 | Claude Code CLI | S1+VPS-GHI/Guard PRE, ≤15′ | 2 SQL files +2 registry +2 manifest, 1 DOT atomic commit | DỪNG/MỘT PHẦN đúng footprint |
| S3 | Claude Code CLI | S2, ≤10′ | 1 bảng 14 cột/0 dòng/ACL/check/index/trigger | lùi mềm nếu regression |
| S4–S5 | Claude Code CLI | S3, ≤10′ | Guard POST/receipt, KQ, cờ trả | Host nghiệm thu |
Hard stop 55 phút; không chạy nền/không chờ Owner tại terminal.
