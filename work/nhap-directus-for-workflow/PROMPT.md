# PG-A2b · TẠO ĐÚNG 2 VIEW V1/V2 (SQL P75 GIỮ NGUYÊN, KHÔNG ĐỔI VAI) + BẢO VỆ CONFIG GUARD
RUN_ID: NDW-PGA2B-TWO-VIEWS-20261028-03
TASK: work/nhap-directus-for-workflow
EXECUTOR_SURFACE: Claude Code CLI
READ_PATH: AGENTS (R1a, R1b, R3) → root COLLAB lease → task COLLAB §0/Bảng/P73/P75/P79/P80/P81/P82/**P83 ủy quyền Owner và Host G1/G2** → PROMPT này; `query_pg` RO; SSH chỉ đọc cho S1.
WRITE_PATH (chỉ ở S2, đúng thứ tự): 2 tệp SQL mới trong `/opt/incomex/dot/sql/directus/`; baseline + hàng registry cho 2 đích mới; `incomex-config-apply-v0` cho `guard-registry` và `dot-sql-approved-manifest`; `dot-pg-atomic-apply directus/ndw-pga2-v1v2.sql` một lần; `workspace_edit` cho STARTED/KQ. KHÔNG psql/docker exec tay, KHÔNG git add/commit trong `/opt/incomex/dot`, KHÔNG GRANT/REVOKE vai hay membership.
STATUS: CLOSED_AFTER_KQ_P85 · `NDW-PGA2B-TWO-VIEWS-20261028-03` đã KQ XONG tại P85 (`c65d094c`), Host ACCEPT P86; READY P84 đã tiêu thụ. **KHÔNG chạy lại PROMPT này.** Đây là bản lưu vận hành P85; RUN tiếp S4/V3 cần PROMPT mới, phản biện và G1/G2 riêng. Các bước S0–S5 bên dưới là lịch sử của RUN đã đóng.

## Đích và chứng cứ đã đo (P81 — không đo lại toàn bộ)
- Tạo đúng 2 VIEW `directus.public.v_pg_asset_catalog` (V1), `directus.public.v_pg_dependency_edges` (V2). SQL **giữ nguyên P75**: tệp áp `directus/ndw-pga2-v1v2.sql` 9.980 B sha256 `b59103401ef4e1666b1a5671c37d914b6029bf3d5c315d0f197882d251e7d31d`; tệp lùi `directus/ndw-pga2-v1v2-lui.sql` 902 B sha256 `bd19885f96b5020bc833e04747f31b191f5532db2d655a6d5e06eb92796830e3`. Dựng theo công thức P75 (khối SQL đầu của P73 + thay đúng 5 dòng; tệp lùi nguyên văn P75). Sha khác ⇒ DỪNG, không tự sửa.
- Quyền (phương án D, P81): `directus` là thành viên `context_pack_readonly` (inherit/set true) nên đọc 2 VIEW gián tiếp — **đã chấp nhận**, vì VIEW `security_invoker` chỉ đọc 14 catalog vốn mở cho PUBLIC, không thêm dữ liệu. KHÔNG đổi/thu membership (12 quan hệ ở `incomex_metadata` + FDW đang dựa vào nó). Cổng chặn lộ = không đăng ký collection/permission Directus, không thêm dòng `table_registry`.
- Không tạo S4/V3/bảng/cột/index/role/extension; không sửa Nuxt/nginx/Kuma/Graph/cấu hình PG. `public.v_report_pg` là TABLE, không đụng. Bốn dòng manifest chưa commit git (c2b1xv×2, directus-system-defaults×2) là nợ cũ của việc khác: giữ nguyên, không git.

## S0 · Gate + STARTED riêng (≤5′)
Đọc theo READ_PATH; READY đúng last-touch; **Owner delegation và Host quyết G1/G2 P83** trong COLLAB; 0 STOP_REQUESTED/COUNCIL_ALERT OPEN/STARTED trùng RUN; PSI/RAM ổn. PASS ⇒ ghi `STARTED@NDW-PGA2B-TWO-VIEWS-20261028-03 <UTC> · executor=Claude Code CLI` thành commit riêng, đọc lại thấy rồi mới sang S1. Không ghi được ⇒ DỪNG.

## S1 · Kiểm trước khi ghi — chỉ đọc + selftest 0 dấu vết (≤10′). Một mục lệch ⇒ KQ DỪNG, 0 ghi, nêu đúng mục lệch
1.1 PG (`query_pg`): 18.6; hai tên trống trong `pg_class` và `pg_type`; `v_report_pg` relkind `r`; `pg_auth_members` (bỏ vai `pg_*`) đúng **1 cạnh** directus→context_pack_readonly như P81 (thêm cạnh/vai mới ⇒ DỪNG); default ACL `workflow_admin/public/r` chỉ có grantee `context_pack_readonly`, `directus`; 0 dòng `directus_collections`/`directus_permissions`/`table_registry` nhắc 2 tên VIEW.
1.2 Tệp: dựng 2 tệp trên Mac ⇒ đúng byte/sha; trên VPS 2 đường đích chưa tồn tại.
1.3 Cổng ghi: sha `/opt/incomex/dot/bin/dot-pg-atomic-apply` = `e1307be7ab06b1c4c705294ff03fdd8678410621d856c9b383a1496c278e962e`; chạy **selftest của chính cổng** `dot-pg-atomic-apply _selftest/atomic_happy.sql` (bảng TEMP ON COMMIT DROP, 0 dấu vết; sha tệp `79cce6fb…` đã khớp manifest ở P81) ⇒ phải `COMMIT thành công`, rc=0.
1.4 Config Guard: `incomex-config-apply-v0 --help` có `--mutation-id --agent --target-id --candidate --expected-baseline`; `incomex-config-drift-check` cho `guard-registry` và `dot-sql-approved-manifest` = MATCH; manifest sống dự kiến sha `d4caa0d05350cad7b7af165edc5de960bdc6b5a6e04d9c62da0cafc971547d3c` (16 dòng) — khác thì chỉ đi tiếp nếu drift-check MATCH và ghi sha mới; registry có hàng mẫu `dot-sql-directus-defaults-1241` đủ 9 cột; 2 id mới `dot-sql-ndw-pga2-v1v2`, `dot-sql-ndw-pga2-v1v2-lui` chưa có.

## S2 · Ghi đúng thứ tự (≤15′) — chỉ sau S1 PASS, lấy VPS-GHI (CAS) + Guard PRE như B0b P27
2.1 Đặt 2 tệp vào `/opt/incomex/dot/sql/directus/` (tệp thường, cùng chủ/quyền với `directus-system-defaults-12.4.1.sql`) ⇒ sha trên VPS đúng.
2.2 Đăng ký 2 đích mới theo trình tự đã chạy thật (vps-clean BAO-CAO §4 L2A): baseline `{content,sha256,meta}` cho 2 id theo đúng định dạng triplet có sẵn → `incomex-config-apply-v0 --mutation-id <M> --agent claude-code-cli --target-id guard-registry --candidate /root/incomex-config-changes/<M>/registry.tsv --expected-baseline <sha sống>`, ứng viên = registry sống + đúng 2 hàng chép hàng mẫu (đổi id/đường) ⇒ APPLIED; drift-check 2 id mới = MATCH.
2.3 `incomex-config-apply-v0 --target-id dot-sql-approved-manifest`, ứng viên = manifest sống **giữ nguyên 16 dòng** + đúng 2 dòng dạng `<sha256><TAB>directus/ndw-pga2-v1v2.sql` và `<sha256><TAB>directus/ndw-pga2-v1v2-lui.sql` (đúng một ký tự TAB, không dấu cách; LF cuối dòng) ⇒ APPLIED.
2.4 `dot-pg-atomic-apply directus/ndw-pga2-v1v2.sql` **một lần**, không retry.
Hỏng ở 2.1–2.3 ⇒ DỪNG (tệp/hàng đã thêm vô hại, giữ nguyên; gỡ chỉ khi Host quyết, qua `.pre` của apply-v0). Hỏng ở 2.4 ⇒ PG tự huỷ giao dịch ⇒ KQ DỪNG.

## S3 · Kiểm sau áp (`query_pg` RO, ≤10′)
(a) V1 `kind,count,count(DISTINCT canonical_key)`, V2 `relation_type,completeness,count`; so Census sống cùng mốc — chênh hợp lệ so với P73 = **+2 view, +20 column, V2 ≈ +0**; khác ⇒ liệt kê tên đổi, không tô đỏ giả. (b) Cha mồ côi bằng câu CTE MATERIALIZED ở P75 (constraint DOMAIN = UNKNOWN; quá 5 s = CHƯA KIỂM, không lùi). (c) `relacl` = chủ + `context_pack_readonly=r`; câu âm tính P75 sửa thành `rolname NOT IN ('workflow_admin','context_pack_readonly','directus')` ⇒ 0 dòng; `reloptions` có `security_invoker=true`; `context_pack_readonly` đọc được.

## S4 · Guard POST + bảo vệ Điều 30/31 (≤5′)
drift-check: `guard-registry`, `dot-sql-approved-manifest`, 2 id mới = MATCH. KQ ghi OID + sha256(`pg_get_viewdef`) + `relacl` của 2 VIEW làm mốc. Xác nhận 0 collection/permission/`table_registry` mới. Hỏng sau COMMIT ⇒ `dot-pg-atomic-apply directus/ndw-pga2-v1v2-lui.sql` một lần ⇒ KQ MỘT PHẦN + Host.

## S5 · KQ + trả cờ
KQ trong COLLAB: mutation-id + sha trước/sau của từng đích apply-v0, OID/viewdef-sha/relacl, số V1/V2 sau áp, Guard, cờ VPS-GHI đã trả, 0 tệp tạm/tiến trình. Cập nhật Bảng điều khiển + `NEXT_TRIGGER=GPT_HOST_NGHIEM_THU_PGA2B`. Không mở S4/V3/E1, không git commit dot, không đăng ký collection/report.

## DROOT48
| Bước | Ai | Trigger/hạn | Chứng cứ | Hỏng thì |
|---|---|---|---|---|
| S0 | Claude Code | Owner dispatch sau Host READY, ≤5′ | READY@SHA + Owner ủy quyền/Host G1G2@P83 + PSI · STARTED commit riêng | DỪNG |
| S1 | Claude Code | S0, ≤10′ | 4 nhóm kiểm + selftest cổng | DỪNG 0 ghi |
| S2 | Claude Code | S1 + VPS-GHI + Guard PRE, ≤15′ | 2 tệp sha · registry/manifest APPLIED · apply 1 lần | DỪNG / PG tự huỷ |
| S3 | Claude Code | S2, ≤10′ | +2 view/+20 column, mồ côi, ACL | tệp lùi ⇒ MỘT PHẦN |
| S4–S5 | Claude Code | S3, ≤8′ | Guard POST, KQ, trả cờ | Host nghiệm thu |
Hard stop 55′; không chạy nền, không giữ terminal chờ.
