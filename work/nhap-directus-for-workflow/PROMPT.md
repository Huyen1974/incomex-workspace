# TS3-S4 · HAI BẢNG PG NATIVE · CHỈ 1 MÃ HỆ + 0 QUYẾT ĐỊNH
RUN_ID: NDW-TS3-S4-TWO-TABLES-20261029-01
TASK: work/nhap-directus-for-workflow
EXECUTOR_SURFACE: Claude Code CLI
STATUS: **DRAFT — KHÔNG READY/RUN.** Chỉ chạy khi (1) Owner trực tiếp duyệt G1/G2 S4 theo P88: 2 bảng (vượt trần 1), một seed và SHA áp mới; (2) Host ký READY@full last-touch PROMPT SHA sau duyệt (REVIEW_REUSED=P87); (3) Owner chuyển lệnh chuẩn DROOT38; (4) S0 PASS. Thiếu ⇒ DỪNG 0 PG mutation. Owner P83/READY P84 chỉ dành 2 VIEW cũ, KHÔNG kế thừa.
READ_PATH: AGENTS.md (A0/A6/R1a/R1b/R3/R4/DROOT30/31/48/58) → root COLLAB VPS-GHI → task COLLAB §0/Bảng, §3.TQ/§3.KH và P85–P88 (SQL P87 nguyên văn, fix P88) → PROMPT này; `query_pg` RO; SSH VPS chỉ đọc trong S1.
WRITE_PATH: chỉ 2 SQL mới dưới `/opt/incomex/dot/sql/directus/`; 2 baseline + 2 registry rows và 2 manifest rows qua `incomex-config-apply-v0`; một `dot-pg-atomic-apply`; `workspace_edit` ghi STARTED/KQ. KHÔNG psql/docker exec/REST/Directus Studio tay, không đổi role, không tạo collection/report/Nuxt/Graph/V3/trigger, không git add/commit tại `/opt/incomex/dot`.

## Đích & SQL đúng byte
- Đúng 2 TABLE trong DB `directus.public`: `tai_san_he` từ điển mã hệ riêng cho S4 và `tai_san_quyet_dinh` sổ phân loại/quyết định FK `he`→`tai_san_he.ma`. Seed đúng **1 dòng `tai_san_he.ma='chua_ro'`**, **0 dòng quyết định**. Không nạp 23 hệ hay 16.536 tài sản. Quyền chủ `workflow_admin`, `context_pack_readonly` SELECT, `directus` kế thừa SELECT nhưng **không DML**. `chua_quyet` nghĩa chưa có quyết định giữ/bỏ dù hàng phân loại đã được duyệt.
- Tệp áp `directus/ndw-s4-tai-san.sql` lấy **nguyên SQL P87** (54 dòng + LF cuối; **4.866 B SHA256 `87d01b5fa4e1b4727adc331165c78a9dad527d88abd5420df95cef7a3430f84c`**) và chỉ thay đúng một dòng:
  CŨ `CHECK (can_cu IS NOT NULL OR (he = 'chua_ro' AND workflow = 'chua_ro' AND vung = 'xam' AND quyet_dinh = 'chua_quyet'))`
  MỚI `CHECK (NULLIF(btrim(can_cu), '') IS NOT NULL OR (he = 'chua_ro' AND workflow = 'chua_ro' AND vung = 'xam' AND quyet_dinh = 'chua_quyet'))`
  ⇒ tệp áp phải **4.885 B**, SHA256 `52b9a820a8b3bba3de883328c902df434544f6902671b61cb0b9b918a51884a3`. Chỉ thay một chỗ, SHA lệch ⇒ DỪNG, không tự sửa SQL.
- Tệp lùi `directus/ndw-s4-tai-san-lui.sql` = nguyên P87 **833 B** SHA256 `eb72e62559a871de4ce83bd6adec8864fde6260f719805818b7fad405cca50d3`, REVOKE + COMMENT, KHÔNG DROP. Sau COMMIT hỏng thì lùi CHỨC NĂNG, schema vẫn có. Chưa tạo business rows, từng lô tương lai phải có Owner duyệt, DOT kiểm `canonical_key` V1 + DB + OID/subid và căn cứ nonblank theo snapshot, không tự gán quyết định.
- Evidence từ P87: 17 ca PG16 mô phỏng PASS & guardrail cổng; PG18 production chưa thử DDL mới. P85 đã chứng minh đường DOT/Config Guard. S1 dưới đây kiểm PG18 thật và selftest an toàn, S2 dùng transaction atomic; không cho phép test CREATE TABLE tay.

## S0 · Kiểm READY rồi STARTED commit RIÊNG
Owner G1/G2 P88, Host READY đúng last-touch SHA, Owner dispatch DROOT38, không STOP_REQUESTED/COUNCIL_ALERT OPEN/STARTED trùng, VPS-GHI trống và PSI/RAM đủ. PASS ⇒ ghi `STARTED@NDW-TS3-S4-TWO-TABLES-20261029-01 <UTC> · executor=Claude Code CLI` thành commit riêng và đọc lại xác nhận trước S1. Không ghi được ⇒ DỪNG.

## S1 · PRE trước mutation: chỉ đọc + DOT selftest
1. **PG18.6 thật:** `query_pg` xác nhận hai bảng/tên composite type chưa tồn tại (`pg_class` + `pg_type`), V1/V2 P85 vẫn đọc được, `trigger_guard_alerts` tồn tại và có baseline count, event trigger `evt_trigger_guard_ddl` không đổi hành vi gây ghi khi CREATE TABLE như P87; membership `directus→context_pack_readonly`, default ACL và quyền hiệu dụng đúng hiện hành; 0 `directus_collections`/`directus_permissions`/`table_registry` nhắc 2 bảng. Bất ngờ gây thay đổi quyền/trigger ⇒ DỪNG.
2. **Tệp/cổng:** dựng Mac 2 SQL như trên, byte/SHA đúng; VPS 2 đường tệp chưa có; hai registry ID `dot-sql-ndw-s4-tai-san`/`dot-sql-ndw-s4-tai-san-lui` chưa tồn tại. `dot-pg-atomic-apply` sống SHA `e1307be7ab06b1c4c705294ff03fdd8678410621d856c9b383a1496c278e962e`; 2 SQL qua guardrail PASS, chạy selftest có manifest `_selftest/atomic_happy.sql` (TEMP ON COMMIT DROP) rc=0/COMMIT, không tạo bảng thật ở S1.
3. **Config Guard:** `guard-registry` + `dot-sql-approved-manifest` drift-check MATCH. Manifest P85 dự kiến 18 dòng SHA `18ae52f1…faedf`; nếu live hợp lệ đã thay thì phải đọc baseline sống và bảo toàn TOÀN BỘ dòng (không áp 18 cứng), ghi trước/sau. Registry hàng mẫu 9 cột; `incomex-config-apply-v0 --help` đủ `--mutation-id --agent --target-id --candidate --expected-baseline`. F1: chụp ACL/mode hiện tại, không setfacl tay; F2: không stage hoặc commit 6 dòng lệch Git DOT đang có.
4. Đủ tất cả mới lấy cờ VPS-GHI CAS + Guard PRE; nếu thiếu khả năng ghi/lùi, SHA sai hoặc quyền sai ⇒ DỪNG 0 PG mutation, đúng một blocker. Không tự tạo kế hoạch khác.

## S2 · Chỉ sau S1 PASS + VPS-GHI/Guard PRE
2.1 Đặt đúng 2 SQL trong `/opt/incomex/dot/sql/directus/` theo owner/mode mẫu P85 và hash trên VPS phải khớp.
2.2 Thêm đúng 2 baseline triplet `{content,sha256,meta}` + hai hàng registry giống cấu trúc 9 cột hiện có qua `incomex-config-apply-v0 --target-id guard-registry`; APPLIED và MATCH.
2.3 Manifest ứng viên = manifest sống + đúng 2 dòng `<sha256><TAB>directus/ndw-s4-tai-san.sql` và `<sha256><TAB>directus/ndw-s4-tai-san-lui.sql`, LF cuối; qua `incomex-config-apply-v0 --target-id dot-sql-approved-manifest`; APPLIED/MATCH, giữ mọi byte/dòng cũ. Đo ACL before/after, không sửa tay, không git commit DOT.
2.4 `dot-pg-atomic-apply directus/ndw-s4-tai-san.sql` **một lần**; nếu lỗi thì PG tự rollback giao dịch, không retry. KQ DỪNG/MỘT PHẦN phản ánh đúng SQL/manifest/registry đã chạm, không DROP.

## S3 · Kiểm sau áp qua `query_pg` RO
Hai bảng tồn tại, owner `workflow_admin`, đúng 5+12 cột, PK/FK/CHECK/COMMENT, `pg_get_constraintdef` căn cứ chứa `NULLIF(btrim(can_cu), '')`; `tai_san_he` đúng 1 mã chua_ro, `tai_san_quyet_dinh` **0 dòng**. `relacl` chủ+context_pack_readonly=r; directus SELECT hiệu dụng (đã biết, không phải quyền public qua Web) và DML false; reader group DML false, login lạ SELECT false; `trigger_guard_alerts` delta 0. 0 collection/permission/`table_registry` hoặc role mới. Đối chiếu Census/V1 cùng mốc: dự kiến +2 table/+17 column/+2 index, V2 ~+3 cạnh FK/index; khác vì dữ liệu sống biến động thì liệt kê, không đỏ giả. Chụp OID/ACL và catalog columns/constraints/index/comments (PG core không có `pg_get_tabledef`) làm mốc Điều 30/31.

## S4–S5 · Guard, lùi, KQ
Config Guard 2 SQL ID/manifest/registry MATCH, Guard POST đúng footprint 4 mục, so PRE_RED_SET và giữ Điều 30/31, receipt Owner có message_id. Regression thật sau COMMIT thuộc S4 ⇒ chạy qua DOT tệp lùi 1 lần (REVOKE+COMMENT, 2 bảng còn), KQ MỘT PHẦN/Host; đỏ cũ ngoài scope không rollback. Ghi KQ mutation-id/hash before/after, SQL SHA, 2 OID/ACL/schema fingerprint, 1 hệ/0 quyết định, trigger alerts, Guard receipt, cờ VPS-GHI đã trả/0 process-tmp và `NEXT_TRIGGER=GPT_HOST_NGHIEM_THU_S4`. Không tự khởi động V3/Graph/Nuxt hay viết quyết định. Hard stop 55 phút, không chạy nền.

## DROOT48
| Bước | Ai | Trigger/hạn | Evidence | Hỏng |
|---|---|---|---|---|
| S0 | Claude Code CLI | Owner chuyển sau READY, ≤5′ | G1G2 P88/READY SHA + STARTED commit riêng | DỪNG |
| S1 | Claude Code CLI | S0, ≤10′ | PG18 role/trigger + SQL SHA/selftest + Config Guard MATCH | DỪNG 0 PG |
| S2 | Claude Code CLI | S1 + VPS-GHI/PRE, ≤15′ | 2 SQL + 2 registry + 2 manifest, 1 atomic apply | DỪNG/MỘT PHẦN |
| S3 | Claude Code CLI | S2, ≤10′ | 2 TABLE + 1 hệ/0 quyết định, schema/ACL/trigger | lùi mềm nếu lỗi thật |
| S4–S5 | Claude Code CLI | S3, ≤10′ | Guard POST/receipt, KQ, cờ trả | Host nghiệm thu |
