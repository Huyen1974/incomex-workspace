# PROMPT — VPSUP G7 · CHUYỂN PRODUCTION MỘT LẦN + NGHIỆM THU + BÀN GIAO

STATUS: **DRAFT RETRY-04 — P121 + P122 + P123 + P124 Reviewer DELTA (so owner extension theo quy tắc, không theo danh tính từng member); chờ Host READY.** §0.3: đã đối chiếu.
RUN_ID: `VPSUP-G7-PROD-CUTOVER-20261003-04` · Executor: phiên Claude Code mới · **Owner dán RUN = Owner duyệt cửa sổ** (45′; G7-03 thực đo gián đoạn 9′53″ rồi rollback trước unfreeze).
Đầu ra duy nhất: VPS1 chạy **PG 18.6 + Directus 12.4.1/OIG + Nuxt 4.5.2/Node 24.21.0 + nginx 1.30.5**, đủ dữ liệu/quyền, sao lưu PG18 đọc lại được, có canh licensing. Không làm gì ngoài đầu ra này (không e-learning/VPS2, không @nuxt/ui v4, không DNS).

## G7.0 · Đọc
AGENTS → BẢNG ĐIỀU KHIỂN → **§0.3 (bảng phiên bản chốt cứng)** → P105–P124 → PROMPT này → hồ sơ G7-03 `INDEX.md` + package cuối SHA `53fb7908f9c6a557e5b5e486057c004faf8affef868c6859f96db6d495a9704e` + G6 `G7-RUNBOOK.md`. G7-04 là cùng gói production, chỉ đóng các blocker đã đo; không thiết kế lại.

## G7.1 · PRE — chỉ đọc, trước đóng băng; một mục trượt ⇒ DỪNG, VPS1 nguyên
1. READY khớp last-touch PROMPT; không RUN khác đang STARTED chưa KQ đụng PG/Directus/Nuxt/nginx/compose/Guard VPS1. Recheck `HJW-FINAL-D30-D31-20261002-04`; nếu STARTED chưa KQ ⇒ DỪNG ở PRE, không mutation/freeze. Ghi PRE trạng thái Kuma #22/INV15; đây là lỗi nền đã có, G7 không sửa, POST phải same-or-better và không được tuyên bố fleet all-green nếu vẫn đỏ.
2. **Baseline package đầu vào = package cuối G7-03, 44 tệp, SHA256SUMS `53fb7908f9c6a557e5b5e486057c004faf8affef868c6859f96db6d495a9704e`.** Nó đã chứa `dot-directus-admin-token-sync`, `dot-directus-license` 1.1.0 và `dot-stack-cutover` 1.0.3. Nếu G7-04 sửa bất kỳ byte nào (verify-data/owner/quarantine/DOT/manifest) ⇒ regenerate `install-prod.manifest` + `SHA256SUMS`, ghi full final hash và chỉ chain package cuối. Không dùng lại SHA cũ sau khi byte đổi.
3. Phiên bản đúng §0.3: PG `postgres:18.6-trixie` index `5a5a84b1…`/amd64 `0377e72c…` · Directus `12.4.1` · Nuxt `4.5.2`/Node `24.21.0` đúng bytes TF · nginx `1.30.5`. Lệch ⇒ DỪNG; **không tra/chọn bản khác**.
4. Compose/.env (`NUXT_SSR_IMAGE`)/mạng/extension live = bản gói đã render (compose `97c534da…`). Khác (việc khác đã sửa từ 09:08Z) ⇒ render lại patch qua DOT trên bản live; diff chỉ được chạm hunk VPSUP; đụng thay đổi của việc khác ⇒ DỪNG.
5. Đĩa VPS1 trống ≥ 20 GB; bản sao lưu đêm gần nhất đọc được. Fresh sample sau G7-03 ~48,7 GB trống.
6. Restore-verify dùng `dot-pg-restore-verify-db` **v1.1.0** từ gói, không dùng v1.0.0 cũ.
7. **Machine identity đã terminal PASS từ G7-03:** admin active `dea4e64c…` có token máy; GSM `DIRECTUS_ADMIN_TOKEN` v2 cùng fingerprint; `/users/me` + `whoami` PASS; `DIRECTUS_OIG_LICENSE_KEY` readable; admin suspended không đổi. G7-04 chỉ verify lại qua DOT/loader, **không tạo/rotate token, không đổi email/password**. Bất kỳ lệch identity/fingerprint ⇒ DỪNG PRE.
8. **Quarantine target PG18 failed trước `pg18-init`:** nếu `/opt/workflow/postgres18` còn non-empty từ G7-03, chỉ qua DOT/wrapper: chứng minh PG16 live healthy · path không mounted · không được live compose/env/reference dùng · marker/owner/mode phù hợp failed target G7-03. PASS ⇒ rename nguyên tử sang `/opt/workflow/postgres18.failed-g7-03` (hoặc tên collision-safe cùng nghĩa) và tạo `/opt/workflow/postgres18` sạch với owner/mode đúng image PG18. Không `rm -rf`; thư mục quarantine giữ tới sau XONG. Preconditions không chắc ⇒ DỪNG PRE.
9. **Patch/test comparator TRƯỚC freeze:** replay `verify-data` mới trên cặp schema artifacts đã lưu của G7-03. Bắt buộc tái hiện raw diff 1.402 dòng của DB `directus`, phân loại 100% vào đúng 2 rule view-deparse ở G7.1B, residual 0. Thêm negative fixture một diff ngoài allowlist ⇒ comparator phải FAIL. Không đạt hai phép này ⇒ DỪNG PRE, không downtime.
10. **Thử cách giữ ownership extension TRƯỚC freeze (P122+P123):** trên một PG18.6 nháp (ngoài production, xoá sau khi thử), DOT tạo DB + role `directus` (NOLOGIN, có CREATE trên DB) rồi chạy đúng bước G7.1C. Không chỉ kiểm `pg_extension.extowner`: trước thử, DOT chụp từ PG16 production nguồn **ownership vector đầy đủ của mọi member object** thuộc `btree_gist` và `pgcrypto` (extension object + các function/operator/type/opclass/opfamily/cast/schema object hoặc loại member thực tế khác), chỉ metadata/owner, không secret. Sau pre-create ở PG18 nháp, chụp cùng vector bằng cùng DOT/cùng quy tắc định danh và so theo **quy tắc sở hữu** (P124), không đòi trùng từng member: **đo thật nguồn (P124, chỉ đọc):** `btree_gist` 1.7 = 258 member (188 function · 26 opclass · 26 opfamily · 12 operator · 6 type), `pgcrypto` 1.3 = 36 function; **100% member owner `workflow_admin` = bootstrap superuser (oid 10)**; extension object owner `directus`. PASS khi đồng thời: (a) extension object owner trên nháp = `directus`; (b) **mọi** member trên nháp có owner = bootstrap superuser của nháp và bản thân bootstrap đó là `workflow_admin` như nguồn; (c) member có mặt ở cả hai bên cùng owner. Số member khác nhau **chỉ được chấp nhận khi `extversion` hai bên khác nhau** (bản extension mặc định của PG18 có thể mới hơn) — ghi số thêm/bớt theo loại, không phải FAIL. Cùng `extversion` mà member lệch, hoặc bất kỳ member nào owner khác bootstrap, hoặc extension owner khác `directus` ⇒ `DỪNG · PRE_BLOCKER_EXTENSION_MEMBER_OWNER`, không freeze, không sửa catalog, không ALTER owner hàng loạt, báo exact object/type/source_owner/target_owner cho Host.

### G7.1A · Machine identity — chỉ verify, không sửa lại
G7-03 đã tạo machine token đúng admin active và GSM v2, rollback production stack không rollback credential vì credential đã verify PASS và là đích lâu dài. G7-04 chỉ:
1. DOT đọc GSM `DIRECTUS_ADMIN_TOKEN` latest bên trong loader, gọi `/users/me`; phải đúng `dea4e64c…`, active, effective admin access.
2. `dot-directus-license whoami` PASS; `status` trên Directus 11 có thể 404 như G7-03 và không phải blocker trước cutover; sau Directus12 phải kiểm route/status thật theo runbook.
3. Đọc đúng `DIRECTUS_OIG_LICENSE_KEY` qua loader vào tmpfs/non-logging path; không enumerate/đọc secret khác.
4. Admin suspended `173a0ab6…` phải vẫn suspended và không bị chạm; không tạo admin/email/password/token mới.

### G7.1B · Schema equivalence PG16→PG18 — không nới cổng, chỉ canonicalize deparse view có kiểm soát
Nguồn chuẩn vẫn là **PG16 production gốc**, không thay bằng một PG16 dựng lại từ dump. PostgreSQL `pg_get_viewdef`/catalog output là decompiled reconstruction, nên khác textual giữa major có thể không phải khác ngữ nghĩa. Comparator giữ 4 normalization hiện hữu và thêm **đúng 2** rule đã đo ở G7-03, **chỉ trong definition của VIEW/MATERIALIZED VIEW**:
- R5: `= ANY ((ARRAY['x'::character varying,…])::text[])` ↔ `= ANY (ARRAY[('x'::character varying)::text,…])` (cast array↔element tương đương).
- R6: hằng trong nhánh UNION được PG18 deparse thêm alias ngầm `AS text` hoặc `AS "varchar"`.

PASS chỉ khi đồng thời:
- data rows/content 5 DB = 0 diff; sequences = 0 diff;
- 4 DB schema còn lại = 0 raw residual như G7-03;
- mọi raw diff của DB `directus` sau 4 rule cũ nằm trong VIEW/MATERIALIZED VIEW và match **chính xác R5 hoặc R6**; ghi count từng rule + danh sách object bị chạm;
- sau R5/R6, normalized residual = **0**;
- bất kỳ diff ngoài view, pattern thứ ba, object mất/thêm, hoặc residual >0 ⇒ FAIL và auto rollback trước unfreeze.
Không dùng wildcard/whitespace blanket normalization; không “ignore view”. Negative fixture ở PRE phải chứng minh comparator vẫn bắt một diff ngoài allowlist.

### G7.1C · Extension ownership — bảo toàn nguồn
Tại freeze, DOT chụp **extension object + full member ownership vector** của source cho các extension trong 5 DB. **P122 đo thật (chỉ đọc, prod PG16):** DB `directus` có `btree_gist` 1.7 + `pgcrypto` 1.3 extension owner `directus` (DB owner `workflow_admin`); hai extension này **trusted**, role `directus` có quyền CREATE trên DB; `pg_db_role_setting` = 0. PostgreSQL docs: với trusted extension do non-superuser cài, **extension object** thuộc caller nhưng **contained objects mặc định thuộc bootstrap superuser** trừ khi script gán khác; target PG18 bootstrap là `workflow_admin`. Vì vậy pre-create dưới `directus` chỉ được dùng sau khi PRE 10 PASS theo **quy tắc sở hữu P124** (extension owner `directus` + mọi member owner = bootstrap `workflow_admin`; số member chỉ được khác khi `extversion` khác). **Cách candidate:** trước `pg_restore` vào PG18, DOT tạo sẵn hai extension dưới role `directus` (`SET ROLE directus; CREATE EXTENSION IF NOT EXISTS … SCHEMA public`); **cấm** `ALTER EXTENSION … OWNER TO` (không có syntax này), cấm sửa `pg_extension`/`pg_shdepend`, và cấm tự ALTER owner hàng loạt member objects nếu PRE 10 thấy lệch. Sau restore, trước verify cuối: áp **cùng quy tắc sở hữu P124** như PRE 10; extension owner khác `directus`, hoặc member nào owner khác bootstrap `workflow_admin` ⇒ FAIL trước unfreeze.

## G7.2 · Chạy — một lệnh, liền một mạch
- Trước freeze, package final phải chứa comparator đã replay PASS/negative PASS, extension-owner restore và quarantine helper; regenerate SHA nếu byte đổi. Sau đó `run/g7-chain.sh` đúng `G7-RUNBOOK.md`. Mọi thao tác PG/Directus qua DOT/script-wrapper (DROOT26/35/39); cấm psql/SQL/REST/CLI tay. Không dừng xin ý kiến giữa các bước.
- Nghiệm thu trước mở ghi trượt ⇒ chuỗi **tự quay lui** về PG16 + Directus 11 + Nuxt3 (đã tập: 4–4,5′), trả slot OIG, ghi `KQ … DỪNG · ROLLED_BACK_PRE_UNFREEZE`.

## G7.3 · Sau mở ghi — không kéo dài gián đoạn
- Theo runbook: Kuma `/server/health` → `/server/ping` · **sao lưu thật bằng công cụ bản 18 + restore-verify v1.1.0 đọc lại được** · Config Guard + sổ DOT + mô tả `dot_tools`.
- **P109 theo §0.3 (thiếu ⇒ Directus 12 có thể khoá âm thầm sau 7 ngày mất licensing):** bật canh licensing trên Kuma → Telegram theo spec đã chốt (kết nối tới licensing từ mạng Directus + trạng thái license; probe không gọi activate/refresh; 2 lần lỗi liên tiếp ~10′ mới báo), dùng cùng `DIRECTUS_ADMIN_TOKEN` loader; bắn **1 tin thử** về Telegram; ghi 5 dòng “mất licensing thì làm gì” vào `G7-RUNBOOK.md` bản VPS1.
- **P114 — KHÔNG đổi email/mật khẩu admin trong G7.** Không cần cho đích nâng cấp; Owner đã nói không vào Studio (D15); nhiều DOT/cron/MCP đang đăng nhập bằng email + mật khẩu (agent-data `directus_stdio_server`, `reconcile-*.py`, Nuxt automation, DOT `environment.sh`) — đổi là có thể hỏng âm thầm. Không tạo/ghi `DIRECTUS_ADMIN_PASSWORD`. Machine automation của G7 dùng `DIRECTUS_ADMIN_TOKEN` như G7.1A.
- Sự cố sau mở ghi ⇒ P88: sửa tiến hoặc quay lui riêng frontend/service; **cấm tự khôi phục DB**; giữ DB lỗi, dừng và báo.

## G7.4 · Giữ đường lùi
Không xoá volume PG16, checkpoint post-S2, image cũ, gói G7; dọn chỉ khi Owner cho phép (việc phụ sau XONG).

## G7.5 · KQ
- Đạt: `KQ@VPSUP-G7-PROD-CUTOVER-20261003-04 XONG · G7_PASS · PG18.6 · DIRECTUS12.4.1 · NUXT4.5.2 · SCHEMA_CANONICAL_PASS · EXT_OWNER_PASS · ADMIN_IDENTITY_PASS · BACKUP_PG18_PASS · LICENSE_MONITOR_PASS` + gián đoạn thật + nơi đặt hồ sơ.
- Không đạt: `… DỪNG · ROLLED_BACK_PRE_UNFREEZE · <lý do>` hoặc `… DỪNG · <blocker>` kèm trạng thái VPS1 hiện tại.
- Sửa ■/➡/cập nhật của Bảng cùng commit KQ; dừng và báo GPT Host.

## HISTORY — G6 đã terminal (KQ `4bfb1df`), KHÔNG CHẠY LẠI CÁC LỆNH BÊN DƯỚI

# PROMPT — VPSUP G6 · HOÀN THIỆN BỘ CUỐI + DIỄN TẬP + GÓI G7 SẴN DÙNG

RUN_ID: VPSUP-G6-INTEGRATED-REHEARSAL-20261002-01
STATUS: **DRAFT — Reviewer P102 đã ACCEPT (cắt 2 phần thừa); chờ Host READY.**
Host: GPT Chat · GPT-VPSUP-20260926-A
Executor_Surface: Claude Code CLI, phiên mới có hook đã nghiệm thu.
Report_Write_Path: Incomex VPS MCP `workspace_*` → `Huyen1974/incomex-workspace/main`, actor xác thực `claude-code`.
Runtime_Write_Path: **VPS2 LAB ONLY** qua DOT/wrapper lab đã nghiệm thu; VPS1 **chỉ đọc/lấy bản sao nhất quán**, không restart, sửa source/config/DB, freeze ghi hay deploy. Secret chỉ theo đường GSM/credential sẵn có, không lộ giá trị.

## G6.0 · Giao đầu ra trọn gói, không xé bước
Một RUN làm liên tục đến khi có: **PG18.x + Directus12.4.1/OIG + Nuxt4.5.2/Node24.21.0 + nginx1.30.5 chạy đạt trên dữ liệu VPS1 mới**, rollback đã thử, **gói lệnh G7 sẵn dùng** kèm số đo/giờ đề xuất. Qdrant/Kuma và UI2/SDK19 giữ như manifest TF.
Các mục dưới là checklist nội bộ trong một RUN, KHÔNG phải các lần xin phép. Agent tự sửa lỗi trong scope lab (wrapper, migration runner, cấu hình, DEFAULT có căn cứ, pipeline backup) và kiểm lại phần bị ảnh hưởng; reuse mọi proof/artifact còn khớp. Không tự đổi đích/thiết kế nghiệp vụ, không nâng UI4, không tự hạ PG18, không mở task/service/framework mới, không chạy G7.
Tác vụ dài có state/log/checkpoint bền trên VPS và cơ chế phục hồi khi Mac mất; không biến thời lượng thành cổng chờ hay bắt Owner canh. Chỉ dừng vì vượt quyền/phạm vi, nguy cơ dữ liệu/secret, thiếu đầu vào thiết yếu hoặc blocker thật không thể xử trong phạm vi.

## G6.1 · Đọc nguồn chuẩn và chốt đầu vào
Đọc `AGENTS.md` → root DROOT22/25–33 → Bảng điều khiển/P99–P101 và Reviewer mới hơn → PROMPT này → TF/S1/G5 INDEX + manifest. READY phải trỏ đúng last-touch PROMPT; xác nhận chưa có G6 STARTED mở, ghi STARTED + ■/➡/cập nhật trước PRE; DROOT30 trước mutation lab đầu tiên. Không sửa PROMPT khi RUN đang sống.
- TARGET-FINAL terminal `65ba02af2d8cf149713e7d755ba9d95bfe0b486e`; S1 `10db62fc63dad80dd241220e704bc94ab6968f4a`; G5 `817c45e4fba2f40b1059eae3994687dbb29e06b4`.
- Dossier TF trên VPS2: `/opt/incomex/work/vps1-up-grade/G4-TARGET-20260930/TF/`. Đọc `INDEX.md`, `TARGET-FINAL-MANIFEST.md`, `SHA256SUMS` và đúng artifact cần dùng; giữ full hashes. Prefix định vị: manifest `41b0e33d…`, Nuxt output `cdbee64a…`, runtime image `5cfe1dda…`, compose patch `8258bc31…`. Không dùng prefix như checksum đầy đủ.
- Chốt PG18 stable patch mới nhất qua release notes/official registry ở PRE, ghi exact version + index/amd64 digest và giữ suốt G6/G7. Không chọn beta/PG19. Directus12.4.1 + Nuxt4.5.2 dùng đúng artifact TF, không build lại/đổi dependency theo thói quen.
- Kiểm lab capacity trước khi dựng, chạy stack nặng lần lượt tránh OOM. Checkpoint G2/G5/TF bất biến; chưa có slot OIG lab đang giữ. Mã licensing/telemetry đã chứng minh không đổi: reuse G4C soak, **không arm lại 6h**.
- Lấy inventory read-only mới của VPS1: image/digest, nguồn cấu hình thực + `.env NUXT_SSR_IMAGE`, extension host, network/mount/alias, mọi DB cần giữ/globals/roles/ACL/extensions/FDW, source/delta đang sống và coverage backup. Đọc KQ liên quan MCPW/MMIM chỉ để carry-forward, không chờ task độc lập.

## G6.2 · Fresh data → PG18 trên volume mới → bộ ứng dụng đã chốt
- Dùng đường dump/backup native sẵn có và DOT/wrapper để lấy bản sao mới, ghi thời điểm/snapshot từng DB; không dừng ghi production trong G6. Mang đủ các DB phải bảo toàn + globals/roles/ownership/ACL/tablespace/sequence/large objects, không chỉ DB Directus. Không bỏ dữ liệu vì tên có chữ test. Tính nhất quán xuyên DB khi cutover phải được bảo đảm bằng freeze toàn bộ writers trong runbook G7.
- Sanitize lab theo manifest G2/TF: không mang token/credential sống vào runtime lab; vô hiệu outbound side effect/cron/Flow có lịch/webhook/retention, map FDW về lab, egress chỉ whitelist đúng khi cần. Backup/SQL dump chỉ giữ private/mã hoá theo pipeline sẵn có, không đưa lên repo public.
- Tạo bản lab PG16 từ bản sao mới làm nguồn và điểm quay lui; tạo **volume PG18 khác hẳn**, dump/restore bằng toolchain18. Tuyệt đối không mở volume PG16 bằng binary18, không link/chia sẻ data files, không xoá/sửa volume gốc. Kiểm PGDATA/mount thực của image18, checksum/initdb, locale/collation, extension versions (gồm các extension thực có), FDW/view/function/trigger/cron. `ANALYZE` sau restore trước đo hiệu năng. PG18 mới có system_identifier mới là bình thường; kiểm đúng volume mới và bảo toàn sysid/data của nguồn PG16, không tái dùng gate S1 “sysid bằng nhau”.
- Restore globals và dependencies đúng thứ tự; lỗi restore không được bỏ qua hoặc xoá constraint/quyền để đạt. Hash/count/sequence/owner/ACL so với nguồn theo từng DB, phân biệt metadata/volatile đã disposition và biến đổi UUID hợp lệ.
- Áp UUID DOT + orphan candidate + official Directus migrations + extension patch đúng công thức TF trên **PG18 mới**. Đọc canonical/manifest và kiểm kết quả thay vì tự đánh dấu migration. Activate OIG bằng POST/đường settings đã proof, kiểm quyền/cách ly trước mọi mô phỏng mở ghi.
- Dùng nguyên bytes Nuxt TF + đúng Node image. Render effective compose gồm `.env NUXT_SSR_IMAGE`; không để env cũ ghi đè image đã chọn. Network `claude_mcp_net` là external **bổ sung**, giữ networks/default/aliases cũ. Áp candidate trên lab, không sửa compose production.
- Wrapper xác minh host/sysid/volume/network của lab theo allowlist mới, kể cả PG18 hai mạng; sửa kiểm tra sai có negative test, không bỏ fail-closed. Lỗi có thể sửa hẹp trên lab thì sửa và tiếp tục trong RUN.

## G6.3 · Đóng các phát sinh TF trong chính bộ cuối
**A. 33 cột DEFAULT thiếu:** lập danh sách chính xác từ fresh clone, so với canonical sạch đúng Directus12.4.1. Chỉ thêm DEFAULT đang thiếu khi có biểu thức upstream rõ, đúng kiểu và không phải tuỳ biến nghiệp vụ; giữ nguyên giá trị hiện có, PK/sequence/tenant/ACL và các default đã cấu hình. Reuse/extend DOT có dry-run/precondition/transaction/verify + SQL rollback khôi phục old default; không suy giá trị secret/provider/tenant. Test tạo field, user, collection bằng API/DOT với payload hợp lệ thông thường (fixture lab), verify và cleanup. **Không lấp đủ trường vào fixture chỉ để che lỗi server.** Default không có nguồn rõ hoặc cần đổi dữ liệu/quyền ngoài scope ⇒ ghi exact blocker. Không mở dự án chuẩn hoá toàn schema.

**B. 503/pressure (P102 gọn):** đo trên bộ PG18 cuối với dữ liệu mới, cùng ngân sách CPU/RAM như production: (1) tải thực lấy từ log production và (2) đỉnh thực ×3. **Đạt khi:** 0 lỗi 503 do Directus quá tải, 0 restart/OOM, p95 không tệ hơn CURRENT đo cùng cách. Tách 503 của nginx auth_limit và lỗi auth mong đợi. Chạy lại replay ~10× của TF **một lần để ghi số**, không điều tra tiếp nếu (1)(2) đạt.
- (1)/(2) trượt ⇒ được sửa hẹp có căn cứ (pool/concurrency/resource trong capacity thật), kiểm lại phần bị ảnh hưởng, lưu exact delta/rollback. Không tắt pressure/rate-limit/security hay nới ngân sách vô căn cứ để lấy PASS. Vẫn không đạt ⇒ PARTIAL, không G7_READY.
- Timeout hữu hạn; không soak N giờ. G4C đã có long-soak, TF license unchanged.

**C. Sao lưu PG18 (P100):** kiểm từng entrypoint backup/cron và binary thật bằng `--version`; dùng `pg_dump`, `pg_dumpall`, `pg_restore` major18 (ưu tiên trong image18 đã pin). Bản sao pipeline backup ở lab phải dump đủ dữ liệu/globals theo policy, báo lỗi fail-closed, đọc lại checksum/nội dung và **khôi phục thử** trên đích lab riêng; không chỉ dùng file tồn tại hay pg_restore --list làm restore proof. Giữ mã hoá/retention cũ; vô hiệu side effect upload/xoá production trong thử lab. Không nâng pipeline kiến trúc mới. Gói G7 chứa đúng thay đổi tối thiểu và một lần chạy pipeline thật/read-back trước XONG, không chờ đêm.

## G6.4 · Diễn tập chuyển + rollback trên đúng bộ cuối
Dùng runner/công thức TF/G5 đã sửa, không thiết kế framework mới. Diễn tập trọn chuỗi tại lab sau khi phần sửa đạt; chỉ lặp phần bị lỗi/input đổi khi cần.
1. PRE ngoài gián đoạn: pin/pull artifact; validate effective compose/env/extension/mạng; backup available; OIG reachability; hash patches và current delta; chuẩn bị rollback. Đo tách PRE khỏi downtime.
2. Freeze mọi writer lab tương ứng với production: không chỉ REST mà cả SQL trực tiếp từ agent/DOT/cron/Flow/queue; drain transaction và ghi mốc. Runbook G7 phải có map writer cụ thể, không giả “chặn web = hết ghi”. Dump cuối/globals trong trạng thái freeze → restore PG18 volume mới → UUID/DEFAULT/migrate → OIG → Nuxt frozen → acceptance. Không dùng DB của G6 làm nguồn data production G7.
3. SAME SLICE/data/rights/Flow/FDW/SQL consumers, 132 routes, browser/login/admin/16 trang TF và thử tạo schema metadata trên fixture. Expected khác chỉ theo TF/migration có căn cứ; không xoá test quyền để PASS. Kiểm reconnect và network từ consumer có thật, artifact vẫn đúng hashes.
4. Trước mở ghi: tạo checkpoint **post-S2 nhất quán** bằng native backup/snapshot có consistency proof (không `cp` volume PostgreSQL đang ghi). Ghi hash/schema/LSN/thời điểm và bảo vệ key trong checkpoint; giữ nguồn PG16/pre-S2. Tính thời gian checkpoint vào cửa sổ nếu thật sự chặn ghi.
5. Chạy thật rollback **trước mở ghi** trên bộ PG18 mới: stop writers/target, trả activation nếu đã dùng, chuyển đúng PG16 volume + Directus11/Nuxt3 và mọi env/network cũ; verify data/consumer/SAME SLICE. Không chỉ sửa image18 về16 trên volume18. G5 proof dùng lại nhưng không thay được rollback volume PG18 mới này.
6. Chính sách **sau mở ghi**: giữ P88 — ưu tiên sửa tiến/rollback frontend-service; cấm tự khôi phục DB PG16 cũ. Cần khôi phục DB thì dừng, giữ DB lỗi, đối soát bằng checkpoint post-S2 + cách hash/PK **đã chứng minh ở G5** (không mô phỏng lại — P102), trình Owner quyết. Không tuyên bố pg_dump18→PG16 là downgrade an toàn.

## G6.5 · Đóng gói luôn G7, không tạo vòng soạn lại
G6 phải giao chung trong hồ sơ việc trên VPS2:
- Manifest full hashes/digests cho PG18 exact, Directus12.4.1, Nuxt/Node frozen, nginx1.30.5; nguồn dữ liệu/snapshot, topology, effective env/extension, globals/DB map; các delta được phép và kết quả test/DEFAULT/load/backup.
- Runner/runbook G7 sẵn dùng: PRE → freeze writers → dump/restore trên **dữ liệu cuối của VPS1** → chuyển → acceptance → checkpoint trước mở ghi → unfreeze → backup thật/read-back → verify monitor/bàn giao. Runner lab/production có kiểm đúng host+sysid+volume/mode, checkpoint/resume khi Mac mất, timeout/stop/rollback rõ; G6 không execute mode production.
- Patch chỉ phần VPSUP trên compose/env/extension/backup và DEFAULT DOT; không reset/stash/commit whole dirty tree của việc khác. Guard/protection Điều30/31 dùng cơ chế hiện hữu, đăng ký đúng delta production trong G7; không rebaseline hộ task khác.
- Rollback plan giữ artifact/volume PG16 và env cũ, vị trí key/cleanup an toàn; danh sách điều kiện trước/sau unfreeze; lỗi DNS phải kiểm bypass DNS giữ đúng Host/SNI, không quay lui DB chỉ vì tên miền lỗi.
- Số đo thực từng đoạn, tổng gián đoạn, thời gian rollback; đề xuất một cửa sổ G7 ít sử dụng theo log và đủ dư quay lui. Không đoán “vài phút” và không bắt chờ đêm nếu số đo/rủi ro không đòi hỏi; Owner duyệt cửa sổ trước production.
Không build lại Nuxt; G6/G7 copy đúng bytes đã kiểm. Nếu phát hiện bắt buộc sửa artifact đã đóng băng hoặc đổi phiên bản ngoài scope, báo exact blocker, không tự rewrite UI. Không xuất DB/secret/compose chứa secret lên GitHub public; repo chỉ tóm tắt + con trỏ/hash an toàn. Mọi lệnh G7 trong hồ sơ chỉ là gói bàn giao, **chưa phải READY/RUN G7**.

## G6.6 · KQ, cleanup và điều kiện kết thúc
Trước KQ: trả slot OIG khi Directus+egress còn hoạt động, xác nhận trả; stop lab target, đóng egress và làm sạch secret theo P71/P72; giữ nguồn/artifact/evidence cần thiết. Deactivate lỗi ⇒ giữ DB/PUBLIC_URL đủ retry, không shred đường cứu rồi báo sạch. Không làm thay đổi e-learning hay xoá hồ sơ/volume gốc.
- Đạt đủ: `KQ@VPSUP-G6-INTEGRATED-REHEARSAL-20261002-01 XONG · G6_PASS · PG18=<exact> · DIRECTUS12.4.1 · NUXT4.5.2 · G7_PACKAGE_COMPLETE`.
- Chưa đạt: `KQ@VPSUP-G6-INTEGRATED-REHEARSAL-20261002-01 DỪNG · PARTIAL · <exact blocker>`, kèm phần đã đạt và điểm tiếp tục, không yêu cầu chạy lại cả gói.
Sửa ■/➡/cập nhật trong cùng commit KQ. Không tự nghiệm thu G7, không phát READY, không nâng production. Host nghiệm thu KQ và Reviewer rà **gói G7 đã có**; sau Owner duyệt cửa sổ mới thực thi G7. Không thêm các RUN “vá DEFAULT”, “đo tải”, “sửa backup” riêng.

Nguồn kỹ thuật hẹp cho đúng implementation: https://www.postgresql.org/docs/18/upgrading.html ; https://www.postgresql.org/docs/18/app-pgdump.html ; https://www.postgresql.org/docs/18/app-pg-dumpall.html ; https://hub.docker.com/_/postgres . Tag list cache không là pin; phải resolve official digest ở PRE.

## HISTORY — TARGET-FINAL đã terminal, KHÔNG CHẠY LẠI CÁC LỆNH BÊN DƯỚI
KQ TF `65ba02a`; PROMPT đã chạy `40df4ec`. Giữ nguyên văn để tái dùng công thức/bằng chứng; chỉ khối G6 phía trên là lệnh hiện hành. Không lấy RUN_ID/STATUS/READY trong lịch sử để thực thi.

# PROMPT — VPSUP CHỐT TARGET CUỐI · Directus 12.4.1 + Nuxt4 artifact

RUN_ID: VPSUP-TARGET-FINAL-20261002-01
STATUS: **DRAFT — CHƯA READY/RUN. Chờ Claude Reviewer rà P92 + prompt này; chỉ Host ghi READY.**
Host: GPT Chat · GPT-VPSUP-20260926-A
Executor_Surface: Claude Code CLI trên Mac Owner.
Report_Write_Path: **workspace_* / Incomex VPS MCP → incomex-workspace/main** (actor `claude-code`).
Runtime_Write_Path: **VPS2 LAB ONLY. VPS1 production = READ-ONLY snapshot/topology evidence.** Không production mutation; không DNS/MCPW/PG18/@nuxt-ui-v4.

## T0 · Mục tiêu duy nhất
Chốt **TARGET cuối sẽ dùng cho G6/G7** bằng một RUN trên VPS2:
- PostgreSQL baseline = **16.15** đã lên production ở S1;
- nginx baseline = **1.30.5** đã lên production ở S1;
- Directus candidate bắt buộc = **12.4.x mới nhất lúc chạy (≥ 12.4.1) + OIG** vì 12.4 sửa GHSA-2xcm-7h22-3m66;
- Nuxt = **4.5.2 / Node24.21.0 / SDK19 / @nuxt/ui2.22.3**; vá nốt đúng 5 file `$t` cùng gốc với `login.vue`;
- Qdrant/Kuma giữ exact digest hiện hành.

PASS ⇒ tạo manifest/artifact/runbook final cho G6. Không cutover VPS1 trong RUN này.

## T1 · Gate/PRE
Đọc: `AGENTS.md` → root DROOT22/25/28–33 → BẢNG ĐIỀU KHIỂN → P88–P92 (+ Reviewer mới hơn nếu có) → PROMPT này → KQ G5 `817c45e`/G5 INDEX → KQ S1 `10db62f`.

READY phải = commit cuối chạm PROMPT. Ghi STARTED theo DROOT31; DROOT30 trước first VPS2 mutation.

PRE:
1. G5 lab clean: 0 target container chạy; OIG slot lab đã trả; egress rule lab đã gỡ; checkpoint `vpsup-g5-ckpt-pre-s2` còn đúng hash/evidence.
2. VPS1 read-only snapshot: PG16.15 + nginx1.30.5; exact live compose sha/bytes; `postgres` network membership, đặc biệt `claude_mcp_net`; A09R1 + agent-data/MCP/Hermes current refs. **Không chờ MCPW/MMIM terminal nếu không chạm VPS2**; chỉ ghi moving-target để G6 recheck fresh.
   **P93:** so `docker inspect` thật với compose cho **mọi container G6/G7 sẽ tạo lại** (directus, nuxt và mọi service trong manifest): Networks · Mounts · Env keys (không value) · ExtraHosts · RestartPolicy · Labels. Mọi thứ gắn tay ngoài compose (như `claude_mcp_net` của postgres) ⇒ ghi vào manifest; chỉ đọc.
3. Config Guard `hvu-sync-py` và Kuma #21/#22 nếu còn đỏ: ghi owner task/status, **không repair/rebaseline trong VPSUP** và không gate TARGET.
4. OIG key chỉ metadata EXISTS; materialize qua đường lab đã proof, không log/value.
5. Resolve Directus **bản vá 12.4.x mới nhất lúc chạy (≥ 12.4.1; có bản mới hơn thì dùng và ghi lý do)** exact **index + amd64 digest** bằng registry read-only; pin digest, không dùng floating tag.

## T2 · Fresh working copy
- Clone checkpoint pre-S2 G5 → working TARGET-FINAL; checkpoint gốc immutable.
- Reuse `dot-directus-uuid-normalize`, ABC map, orphan repair candidate, extension patch và lane-C Nuxt4 patch đã proof; hash phải khớp evidence G4/G5.
- Không dùng dữ liệu production mới trong bước này; **G6 mới là fresh-data rehearsal**.

## T3 · Directus 12.4.1 security/breaking probe
Trên working copy:
1. UUID DOT dry-run/execute/verify như G5.
2. Chạy official Directus12.4.1 `migrate:latest`; cấm manual mark/bypass migration.
3. Boot 12.4.1, activate OIG qua POST `/license`; exact slot before/after.
4. Kiểm tối thiểu các delta 12.4:
   - **GHSA-2xcm-7h22-3m66:** bằng fixture lab non-admin chứng minh update/delete-by-query không thể resolve/mutate item mà actor không có READ;
   - inactive collection API behavior + consumer scan;
   - directus#28318: inventory PK `0`/`''` liên quan update/delete-filter; nếu có thì test fixture và ghi blocker/expected;
   - non-admin folders behavior 12.4.1;
   - Map interface/WebGL2: đếm field dùng interface map trước; 0 ⇒ N/A, > 0 ⇒ thử bằng browser thật;
   - theme/extension compatibility (`@unhead/vue` delta) + extension host;
   - SDK19 + Nuxt consumer, agent-data/MCP/DOT/Flow representative paths.
   - **P93:** liệt kê **đủ** (không chỉ đại diện) mọi đường update/delete theo query/filter: operation Flow `item-update`/`item-delete` có query, DOT và agent-data gọi update/delete theo filter. Đường nào chạy bằng token/accountability không phải admin ⇒ chứng minh kết quả 12.3.1 vs 12.4.x như nhau hoặc ghi khác biệt cụ thể (12.4 bắt buộc quyền READ).
5. 167/actual collections, 128 Flow, permission count = lab/prod source; permission negatives + tenant-sensitive query tests PASS.

**Nếu 12.4.1 có blocker thật không sửa hẹp được:** KQ `DỪNG · DIRECTUS1241_BLOCKER · <exact>`; không tự chọn 12.3.1 làm production target.

## T4 · Vá 5 sibling `$t` + build Nuxt final
Áp cùng cách máy thay đã proof ở `login.vue` cho đúng 5 file:
`register` · `forgot-password` · `logout` · `admin/users` · `error.vue`.
- Không mở rộng rewrite ngoài cùng root-cause.
- Build Nuxt4.5.2/Node24.21.0 trên VPS2 bằng builder/lane đã proof; giữ @nuxt/ui2.22.3 và SDK19 trừ khi Directus12.4.1 test chứng minh bắt buộc đổi.
- Browser thật: login/register/forgot/logout/admin users/error path + 9 trang chính; SSR 200/expected status, hydrate, 0 page error mới, console diff disposition.

## T5 · SAME SLICE + fixed workload
Chạy SAME SLICE G5 A–D + SEC trên Directus12.4.1/Nuxt final:
- 132 routes với baseline timeout đã disposition (`/knowledge/registries` cold có thể ~34s);
- Directus admin browser login;
- representative Flow → agent-data, permission negatives, auth/refresh;
- Qdrant/client path giữ nguyên;
- topology manifest cho G6/G7: ghi VPS1 live `postgres` networks và **bắt buộc giữ `claude_mcp_net`**. **P93 chốt cách:** khai `claude_mcp_net` là mạng ngoài (`external: true`) trong compose cho service `postgres` — tạo lại container bao nhiêu lần cũng tự có, không dựa người nhớ. Chứng minh trên VPS2 (tạo mạng cùng tên trong lab → recreate PG → kiểm membership + kết nối). Gắn tay sau khi tạo chỉ là dự phòng nếu khai báo hỏng. Không mutation VPS1.

**Không thêm soak N giờ.** Thay bằng fixed-workload/replay đủ lớn (ví dụ cùng route/slice lặp tới ≥5.000 HTTP/API request hoặc workload tương đương), ghi error/restart/RSS/heap/CPU. G4 đã có long-soak; G6 sẽ fresh-data rehearsal. Nếu Reviewer chỉ ra failure mode cần thời gian mới lộ thì giao machine-owned timer, không giữ Mac/Claude chờ.

**P93 — failure mode cần thời gian duy nhất đáng xét: license** (telemetry 6 giờ/lần + làm mới license). So mã licensing/telemetry 12.3.1 ↔ 12.4.x (package `@directus/license` + nơi gọi). Không đổi ⇒ dùng lại bằng chứng soak 6 h của G4, không chờ. Có đổi ⇒ máy giữ lab chạy hết 1 chu kỳ telemetry (≥ 6 h) bằng đúng cơ chế soak máy giữ của G4C (tự trả slot cuối); executor ghi KQ phần còn lại rồi thoát, kết quả timer do máy ghi. Rò bộ nhớ chậm để G6 + 7 ngày theo dõi bắt.

## T6 · Đóng gói TARGET cuối
PASS 12.4.1 + Nuxt final ⇒ evidence phải có:
- exact digests: PG16.15 · Directus12.4.1 · nginx1.30.5 · Qdrant/Kuma keep · Node/Nuxt package lock;
- UUID DOT + ABC sha + exact migration count/schema diff;
- Nuxt final patch/hash + 6 file i18n fix (login + 5 sibling);
- **P93:** artifact Nuxt cuối = bản build đã kiểm (`.output`/image) + sha256; G6/G7 **copy đúng bytes này, cấm build lại**;
- patch compose chỉ gồm hunk VPSUP (pin image + mạng `claude_mcp_net`) để G7 áp và commit đúng hunk đó vào git `/opt/incomex`, không đụng thay đổi của việc khác;
- OIG activation/deactivation result; trả slot 204 trước cleanup;
- SAME SLICE/security/browser/fixed-workload results;
- `TARGET-FINAL-MANIFEST` cho G6: artifacts + compose/runtime deltas + **topology PG↔claude_mcp_net** + carry-forward list pointer.

Không sửa/commit live compose VPS1 trong RUN này. Vì `/opt/incomex` đang dirty từ task khác, G6 PRE phải lấy exact live bytes + 3-way diff; cấm reset/clean/stash thay người khác.

## T7 · Cleanup/KQ
Trả OIG activation khi Directus+egress còn chạy → confirm slot giảm → stop TARGET → đóng egress → shred key/runtime-secret-bearing working copy theo runbook đã proof. Giữ checkpoint/evidence không chứa key cần cho G6.

PASS:
`KQ@VPSUP-TARGET-FINAL-20261002-01 XONG · TARGET_FINAL_PASS · DIRECTUS<bản 12.4.x thật> · NUXT4.5.2`

FAIL:
`KQ@VPSUP-TARGET-FINAL-20261002-01 DỪNG · <exact blocker>`

Executor dừng sau KQ. Không tự chạy G6/G7/PG18/Nuxt UI v4.

Runbook lịch sử dùng lại, không thiết kế lại:
- G5: `git show 1ee1137:work/vps1-up-grade/PROMPT.md`
- S1: `git show bbab83d:work/vps1-up-grade/PROMPT.md`

## HISTORY — G4C/G4B/G4/G3
**Từ marker HISTORY trở xuống chỉ là lịch sử/evidence, KHÔNG phải lệnh TARGET-FINAL.**
## G4C.2 · Canonical schema — không đoán bằng tên cột
Tạo một **scratch PostgreSQL DB/volume riêng trên VPS2** và dùng exact Directus12.3.1 image để dựng schema PostgreSQL sạch/canonical. Không dùng OIG key; credential/admin scratch sinh local, không log và huỷ cùng scratch.

Từ canonical DB lấy machine-readable map:
`table.column | data_type | udt_name | nullable | default | PK/unique/index | FK target` cho mọi `directus_*` table.

So với checkpoint A để tạo 3 tập:
A. `SYSTEM_UUID_REQUIRED`: cột `directus_*` mà canonical12.3.1 = uuid nhưng checkpoint A = char(36)/text tương đương.
B. `RELATION_UUID_REQUIRED`: cột ngoài/ trong system tables mà metadata `directus_relations` thật sự trỏ tới PK sẽ đổi ở A; recurse nếu cần để không để relation hai đầu lệch type.
C. `KEEP_CHAR36`: mọi char36 còn lại — business PK/group key/string không nằm A/B. **Không đổi C**, dù giá trị trông giống UUID.

Evidence phải có số lượng + danh sách A/B/C; không dùng heuristic “tên *_id ⇒ uuid”.

**D. Phụ thuộc của A/B — kiểm trước convert và chạy lại sau convert:**
- view/rule dùng cột A/B (ALTER TYPE sẽ bị chặn) — ghi drop/recreate đúng định nghĩa cũ;
- hàm plpgsql/SQL, trigger, event trigger (`evt_trigger_guard_ddl/drop`), job cron SQL (9 hàm `refresh_*`, `fn_backfill_universal_edges`, `fn_refresh_orphan_col`, `birth_trigger_directus_fields`) có nhắc cột A/B — plpgsql chỉ lỗi lúc chạy, nên sau convert phải **chạy thật từng hàm/job trong transaction ROLLBACK**;
- foreign table FDW ở `incomex_metadata` (server `directus_srv`) có cột trỏ sang cột A/B: đọc có điều kiện WHERE trên cột đó (bắt lỗi đẩy điều kiện `uuid = character` sang phía kia);
- consumer SQL trực tiếp ngoài PG: agent-data (`DIRECTUS_DB_*`) + 17 DOT SQL thẳng `directus_*` — phân tích tĩnh câu SQL chạm A/B + chạy đường đọc DB của agent-data trên lab; gãy thì ghi patch candidate.
Phụ thuộc gãy mà không xử lý được trong phạm vi lab ⇒ DỪNG exact blocker.

## G4C.3 · Phân loại 32 non-UUID
Chỉ quan tâm non-UUID nằm trong A/B.
- Với mỗi giá trị lạ trong A/B: ghi `table.column`, row PK, Directus relation target, target tồn tại hay orphan, nullable, và trạng thái record liên quan; redact nội dung nghiệp vụ nếu không cần.
- Non-UUID chỉ nằm C ⇒ **không blocker**, giữ nguyên.
- Cho phép **lab-only auto-repair duy nhất**: system metadata pointer nullable (vd `directus_flows.operation`) mà giá trị không parse UUID **và không có target row tương ứng** ⇒ lưu original vào evidence + set NULL trên working copy để thử migration. Không áp production; ghi thành candidate repair cho G7.
- Nếu non-UUID nằm B ở **custom/business field relation tới Directus UUID target** ⇒ DỪNG trước normalize và báo chính xác các row/field cần Host xử lý; không tự NULL/rewrite business data.
- Nếu non-UUID nằm A nhưng không thuộc auto-repair trên ⇒ DỪNG exact blocker.

## G4C.4 · Normalize trên working copy, không checkpoint A
Clone checkpoint A → working volume G4C; checkpoint A immutable.
Trước DDL capture schema/default/index/constraint/count/value-hash cho A/B.
- Conversion chạy bằng **một DOT candidate** (DROOT27: `--help`, dry-run mặc định in kế hoạch A/B, execute trong 1 transaction, verify; từ chối nếu host/sysid không phải lab) — đây là công cụ G7 sẽ dùng trên production. Đặt trong hồ sơ G4C trên VPS2; đưa lên VPS1 + Config Guard ở G7 (DROOT29). Lưu map A/B/C + sha để G7 so lại với prod trước khi chạy.
- Đo thời gian convert từng bảng + tổng (bảng lớn bị ghi lại toàn bộ, giữ khoá) — số liệu downtime cho G5/G7.

Nếu §G4C.3 không blocker:
- thực hiện conversion A/B trong **một transaction riêng**; ưu tiên `USING NULLIF(btrim(col::text),'')::uuid` khi nullable, hoặc cast tương đương đã proof;
- preserve NOT NULL/default/PK/unique/index; constraint nào cần drop/recreate phải ghi exact before→after;
- không thêm PG FK mới chỉ vì relation metadata nếu canonical/current Directus không có FK đó;
- post-conversion: 0 non-UUID trong A/B, type map A/B khớp canonical/target, row counts unchanged, semantic value hash `uuid::text` khớp pre-cast expectation; mục D (view/hàm/trigger/cron/FDW/consumer SQL) chạy lại PASS.
Rollback proof: discard working copy → checkpoint A.

## G4C.5 · Official Directus migration — không bypass
Sau normalization PASS, chạy **official Directus12.3.1 `database migrate:latest`** trên working copy.
- Cấm sửa migration upstream, cấm manual mark applied, cấm F2.
- Phải PASS qua `20260204A-add-deployment` và `20260512B-add-mcp-oauth`.
- Ghi migration before/after + schema diff; nếu migration khác gãy ⇒ DỪNG exact blocker và reset working copy.

## G4C.6 · Nếu migrate PASS thì tiếp tục G4B ngay
Không mở vòng mới nếu migrate PASS:
1. boot Directus12.3.1;
2. activate OIG bằng **POST `/license` / settings source**, không env-source, để cuối soak có thể `DELETE /license`; activation tối đa 1;
3. LC1–LC6 + 167 collections/128 flows/1.241 permissions + extension + `/server/ping` + telemetry/license;
4. apply đúng lane C patch đã PASS; Nuxt4 runtime + @nuxt/ui2 + SDK19 + SSR/auth/9 UI pages;
5. nginx/Qdrant exact artifacts + SAME SLICE/132 routes/API/Flow/permission negatives;
6. B1 nếu moving-target: chỉ recheck đúng agent-data/MCP/Hermes consumer bị đổi, không chặn phần độc lập.

License cleanup theo P71/P72: cuối soak deactivate khi Directus+egress còn chạy → xác nhận slot giảm → mới stop/cleanup. Deactivate fail ⇒ giữ DB/PUBLIC_URL state đủ retry.

## G4C.7 · Machine soak và KQ
CORE PASS ⇒ arm ≥6h synthetic load machine-owned, đo HTTP errors/restart/RSS/heap+slope; Claude Code ghi KQ rồi thoát.

KQ hợp lệ:
- `KQ@VPSUP-G4C-UUID-NORMALIZE-20261001-01 MACHINE_DONE · UUID_NORMALIZE_PASS · CORE_PASS · SOAK_ARMED`
- `... DỪNG · UUID_DATA_BLOCKER · <exact A/B field+rows>`
- `... DỪNG · <other exact blocker>`.
Không G4 PASS/G5/G6/G7/DNS.

## HISTORY — G4B/G4/G3
**Từ marker HISTORY trở xuống chỉ là lịch sử/evidence, KHÔNG phải lệnh G4C.**

## G4B.0 · Mục tiêu duy nhất
**Không chạy lại G4 từ đầu.** Reuse kết quả đã PASS của Lane A/C/D; chỉ tiếp tục từ checkpoint A để hoàn thành Directus 12.3.1 → runtime Nuxt4/nginx/Qdrant → SAME SLICE + SEC → arm soak machine-owned.

Đã PASS, chỉ regression-check/reuse, **không rerun migration/build đầy đủ nếu hash/checkpoint khớp**:
- Lane A PostgreSQL16.15 physical-PGDATA PASS;
- Lane C Nuxt4.5.2/Node24 build patch `laneC/nuxt4-lab.patch` sha `47c5c4eb…` PASS build-only;
- Lane D nginx1.30.5/Qdrant1.16.3/Kuma artifact PASS;
- e-learning VPS2 200 + G2 checkpoint immutable.

## G4B.1 · Gate trước STARTED
Host READY khi GSM metadata có secret đúng tên `DIRECTUS_OIG_LICENSE_KEY`; không đọc/in value trong Host/repo/chat.

`MCPW-B1-IDENTITY-20260930-01` **không còn là hard gate**. Nếu B1 chưa terminal, G4B chụp snapshot hiện hành của agent-data/MCP/Hermes (source_head/image/StartedAt/config liên quan) và tiếp tục. Nếu B1 đổi các consumer này trong lúc G4B chạy thì **không dừng Directus/Nuxt/SAME SLICE/soak độc lập**; chỉ đánh dấu đúng consumer test bị ảnh hưởng và chạy lại đúng nhóm đó trên snapshot mới trước khi Host ghi G4 PASS. Không rerun Lane A/C/D hay toàn G4B chỉ vì moving target.

Executor read-gate: AGENTS → COLLAB §0 + G4 KQ/P66–P68 → PROMPT này → hồ sơ G4. READY phải = commit cuối chạm PROMPT. Sau read-gate PASS ghi `STARTED@VPSUP-G4B-DIRECTUS-CONTINUE-20260930-01 <UTC> · executor=Claude Code CLI` theo DROOT31. Sau PRE, ngay trước mutation VPS2 đầu tiên áp DROOT30.

PRE fail-closed:
- checkpoint A + G2 hashes + lane C patch + image digests khớp KQ `349b1eb`; TARGET 0 container chạy;
- e-learning static 200;
- `DIRECTUS_OIG_LICENSE_KEY` EXISTS metadata;
- snapshot hiện hành agent-data/MCP/Hermes đã ghi; nếu B1 còn active thì ghi rõ `B1_MOVING_TARGET=YES`, không coi là blocker;
- nếu bất kỳ input/hash/digest không khớp ⇒ DỪNG, không tự rebuild lane A/C/D.

## G4B.2 · Directus 12.3.1 từ checkpoint A
- Clone/copy checkpoint A sang working TARGET B; checkpoint A immutable.
- Mở egress lab tối thiểu tới licensing/telemetry **trước** boot có `LICENSE_KEY`, hoặc dùng đường activate API đã chứng minh; mọi egress khác DROP.
- Materialize key từ GSM theo secret-boundary hiện hữu, không log/stdout/repo/evidence value. NODE_ENV production + PUBLIC_URL hợp lệ.
- Boot exact Directus12.3.1 digest; migrate schema 11.14 →12.3.1; ghi exact migration/duration.
- Activation count trước/sau; activation lab tối đa 1. Key OIG hiện perpetual; không renewal test.
- LC1–LC6 + 167 collections ·128 flows ·1.241 permissions · custom access rules · extension `l2-checkpoint-guard` · IP_TRUST_PROXY · `/server/ping` · WS · PUBLIC_URL · telemetry/license failure behavior.
- Consumer matrix dùng snapshot **mới nhất tại thời điểm test**: Nuxt, agent-data, MCP `directus_*`, Mac MCP nếu relevant, DOT/script/cron, PG function/trigger; Hermes nếu evidence = không gọi thì ghi no-call. Nếu B1 đổi agent-data/MCP/Hermes sau snapshot, ghi `CONSUMER_RECHECK_PENDING` cho đúng nhóm bị ảnh hưởng và recheck đúng nhóm đó trên snapshot mới; không chặn các phần độc lập. DOT chỉ qua wrapper fail-closed lab; production DOT/script chỉ static-analysis/patch candidate.
- Không sửa VPS1 production consumer trong G4B.

## G4B.3 · Integrated runtime
- Apply lại đúng lane C patch đã chứng minh; **không build lại từ source trôi**. Nếu source hash đổi so G4 ⇒ DỪNG/review, không tự merge.
- Boot Nuxt4.5.2/Node24 runtime với Directus12.3.1; `@nuxt/ui2` + SDK19 + SSR/auth/9 UI pages phải PASS.
- nginx1.30.5 + Qdrant1.16.3 exact digest; SAME SLICE G2 A/B/C/D + SEC, expected chỉ đổi đúng breaking đã chốt trong G3/P66.
- Recheck 132 routes; browser thật; Flow/API/agent-data/ops/lab-admin/permission negative cases.
- Outside-scope VPS1 diff phải quy được về MCPW-B1 KQ hoặc =0; G4B tự tạo 0 VPS1 mutation.

## G4B.4 · OIG activation lifecycle
- **Không `DELETE /license` trước soak** vì integrated stack cần license trong toàn bộ soak.
- Lab DB/checkpoint sau activation = secret-bearing, chỉ ở VPS2; không đưa sang repo/Drive/VPS1.
- Khi soak kết thúc (PASS hoặc FAIL), machine cleanup phải stop TARGET, gọi đường trả activation đã chứng minh (`DELETE /license` nếu API/version xác nhận), xóa materialized key/runtime secret và shred checkpoint secret-bearing theo runbook. Nếu return activation fail ⇒ state `LICENSE_RELEASE_FAILED`, báo Host; không âm thầm xoá bằng chứng.

## G4B.5 · Machine-owned soak
Sau CORE integrated PASS:
- arm synthetic load theo nhịp gần production trong **≥6 giờ**, ghi timestamp/request-rate/HTTP error/restart/RSS/heap + slope; watchdog bền;
- machine tự kết luận `PASS|FAIL`, chạy cleanup G4B.4 và tự dừng TARGET;
- Claude Code ghi KQ `MACHINE_DONE · CORE_PASS · SOAK_ARMED` rồi thoát, không chờ 6h.
- Host nghiệm thu state sau; không cần chạy lại Claude Code chỉ để đọc timer.

## G4B.6 · KQ
Hồ sơ tiếp tục dùng `/opt/incomex/work/vps1-up-grade/G4-TARGET-20260930/`, thêm mục G4B; không tạo dossier mới nếu không cần.
KQ executor:
- `KQ@VPSUP-G4B-DIRECTUS-CONTINUE-20260930-01 MACHINE_DONE · CORE_PASS · SOAK_ARMED`
- hoặc `... MACHINE_DONE · CORE_PASS · SOAK_ARMED · CONSUMER_RECHECK_PENDING` nếu duy nhất B1 moving-target còn cần recheck consumer sau;
- hoặc `DỪNG · <exact blocker>`.
Không tự ghi G4 PASS/G5/G6/G7/DNS.

## HISTORY — G4 PARTIAL + G3 đã hoàn tất
**Mọi nội dung từ marker HISTORY này trở xuống chỉ là lịch sử/evidence, KHÔNG phải lệnh G4B.**

## G4.0 · Mục tiêu duy nhất
Dựng **TARGET riêng trên VPS2** từ checkpoint sanitized CURRENT của G2, theo đúng target G3 đã PASS; chạy SAME SLICE + route/API/UI/runtime/security matrix và chuẩn bị rollback evidence. **Không chạm checkpoint CURRENT G2**, không cutover VPS1, không G5 rollback rehearsal đầy đủ.

**TARGET cố định:**
- PostgreSQL `16.15-trixie` theo full digest trong `G3-TARGET-20260930/upstream/digests-*.txt`;
- Directus `12.3.1` index digest `sha256:8978edf633ae28aa31464bb71c55300c94d8bc771ff3727b5fac485173283869` + amd64 digest khớp G3 evidence;
- Nuxt `4.5.2`, Node `24.21.0-alpine3.23` exact digest theo G3 evidence;
- nginx `1.30.5-alpine` exact digest;
- Qdrant KEEP `1.16.3` exact digest; Kuma KEEP `2.2.1` exact digest/manifest (không cần boot Kuma nếu SAME SLICE G2 không dùng nó).

**Không tự đổi target.** Directus 12.4.1 không được migrate thử trong RUN này. Nuxt 3.21.11 chỉ được dùng trong scratch diagnostic nếu cần cô lập lỗi Nuxt4, **không phải production fallback/target** vì Nuxt 3 đã EOL.

## G4.1 · Read/collision gate
Đọc AGENTS → task COLLAB §0 + G2 KQ + G3 KQ/P63–P66 → PROMPT này. READY phải = commit cuối chạm PROMPT. Áp DROOT31: sau read-gate PASS ghi `STARTED@VPSUP-G4-TARGET-PARITY-20260930-01 <UTC> · executor=Claude Code CLI` trước PRE/mutation. STARTED sống ⇒ Host/Reviewer không ghi vào `work/vps1-up-grade/` tới KQ. Áp DROOT30: sau PRE, ngay trước mutation đầu tiên trên VPS2 đọc lại COLLAB + PROMPT; READY/HOLD/STOP_REQUESTED đổi ⇒ DỪNG.

Collision:
- MCPW Pha B/C được chạy song song nếu không chạm VPS2 TARGET/Directus/PG/Nuxt/Qdrant/DNS của G4.
- Nếu MCPW đổi agent-data/MCP/Hermes trong lúc G4 kiểm consumer Directus ⇒ ghi snapshot/time; tiếp tục lane độc lập, nhưng consumer acceptance cuối phải recheck sau MCPW terminal. Không rollback task kia, không gộp task.

PRE bắt buộc:
- VPS2 e-learning vẫn FREEZE + static page 200; CURRENT checkpoint G2 còn nguyên/stopped + hashes khớp;
- đủ disk/RAM/swap; không active TARGET cũ;
- xác nhận target digest full + prefix khớp G3 evidence; nếu tag/digest/advisory target đổi ngoài freeze ⇒ DỪNG trước pull/load;
- kiểm metadata GSM **chỉ để biết OIG key có tồn tại hay không**, không in/đọc value vào log/chat. Tên secret cố định: `DIRECTUS_OIG_LICENSE_KEY`; không dò tên khác trong GSM. Điều kiện OIG của Owner đã xác nhận ở §0, **không hỏi lại doanh thu/nhân sự**.

## G4.2 · Artifact + isolation
- Bảo toàn CURRENT checkpoint G2 immutable; tạo TARGET volumes/network/source-copy riêng.
- Reuse isolation G2: internal lab network + host firewall/DOCKER-USER, production secrets không mang sang TARGET.
- Image Docker lấy theo exact digest. Ưu tiên pull/save/load ngoài lab runtime như G2; builder Nuxt có thể dùng egress riêng tối thiểu cho registry/package fetch rồi đóng lại, không mở egress TARGET runtime.
- Không dùng floating tag `latest`/major tag trong TARGET manifest.

## G4.3 · Lane A — PostgreSQL 16.15
1. Dừng PG CURRENT lab, **copy vật lý** volume dữ liệu PG CURRENT (bản đã dựng từ dump sanitize ở G2) sang volume TARGET riêng, rồi boot 16.15 trên bản copy — đúng đường cutover production (đổi image trên cùng PGDATA). Không initdb mới + restore dump (đó là đường khác). So sha/số dòng trước boot; không mutate CURRENT volume.
2. Boot exact `16.15-trixie` digest; cùng base/glibc như CURRENT.
3. Trước/ sau: extensions, `datcollversion`, checksum, object/table/row counts, owners/ACL/FDW.
4. Chạy lại query G3: `btree_gist`/`ltree` + index dạng bị ảnh hưởng release 16.15. Nếu bằng chứng đổi ⇒ DỪNG và disposition REINDEX trước khi tiếp; không suy từ version.
5. `pg_hba` localhost trust giữ nguyên theo P64; regression-test 6 FDW/foreign reads + cron/DOT read paths trên lab, không tạo bản sao secret mới.
6. PASS lane A phải có rollback = stop TARGET + quay lại CURRENT checkpoint, không downgrade dữ liệu.

## G4.4 · Lane B — Directus 12.3.1 + license
**Eligibility đã được Owner xác nhận; chính sách Directus cập nhật 10/09/2026: OIG hiện perpetual/no-expiration, không có annual renewal gate.** G4 không tạo nhắc gia hạn hằng năm. Vẫn phải chứng minh key thật, activation, telemetry/license connectivity và LC1–LC6.

- Nếu **OIG key chưa tồn tại trong canonical secret store**: ghi `BLOCKED_OIG_KEY_ONLY`, **không ngồi chờ**; bỏ qua lane Directus + integrated tests phụ thuộc Directus, tiếp tục Lane A, Lane C build-only, Lane D artifact/pinning. KQ cuối = PARTIAL với checkpoint tái dùng được.
- Nếu key có: materialize tối thiểu theo secret-boundary hiện hữu, không log value; dùng 1 activation cho lab theo đúng PUBLIC_URL/DB binding; không đưa key vào repo/evidence.
- Tránh bẫy đã đọc trong mã 12.x (`license/manager.ts`): `LICENSE_KEY` qua env + DB chưa có key + không tới được license server ⇒ `process.exit(1)`. Mở egress licensing tối thiểu **trước** lần boot 12.3.1 đầu tiên có key, hoặc boot không key rồi kích hoạt qua API; ghi rõ đường đã dùng để làm runbook G7.
- Activation: ghi số activation trước/sau; LC xong ⇒ `DELETE /license` trả lượt lab (trừ khi Host muốn giữ). DB/checkpoint lab sau kích hoạt chứa `license_key` ⇒ coi là có secret: không mang khỏi VPS2, shred khi dọn lab.
- Trước boot 12.3.1: snapshot/checkpoint TARGET PG sau lane A. Rollback Directus = restore checkpoint + image cũ, không migrate down.
- Chạy migrations 11.14-schema → 12.3.1; ghi exact migration list/duration.
- Gate bắt buộc: 167 collections · 128 flows · 1.241 permissions; custom policy/permission semantics; extension `l2-checkpoint-guard`; IP_TRUST_PROXY; `/server/ping`; WS; PUBLIC_URL; LC1–LC6; telemetry/license failure behavior.
- Consumer matrix: Nuxt, agent-data, MCP `directus_*`, Hermes (nếu thực sự không gọi thì evidence), DOT/script/cron, 17 health/DOT path, 2 PG function/trigger. **Không sửa production consumer ở VPS1**; dùng lab copy/fixture/endpoint override và ghi patch candidate. Production patch thuộc G7/DROOT29. DOT/script chỉ chạy trên lab qua wrapper fail-closed hoặc override URL/DB lab tường minh (như `dot-vpsup-lab-pg` ở G2); DOT không có cơ chế override ⇒ chỉ phân tích tĩnh, không chạy (host VPS2 không bị chặn egress).
- Chỉ egress Directus lab tối thiểu tới endpoint licensing/telemetry cần thiết, theo source/docs; mọi egress khác vẫn DROP; test xong khôi phục policy lab mặc định.
- **Không migrate thử 12.4.1 trong RUN này.** Chỉ ghi release-note delta; nếu có advisory mới chạm 12.3.1 thì DỪNG, Host mở target review mới.

## G4.5 · Lane C — Nuxt 4.5.2 / Node 24.21.0
- Copy source-lock fork Agency OS từ VPS1 read-only sang VPS2 TARGET workspace; production source không sửa.
- Build trong exact Node 24.21.0-alpine3.23; khóa Nuxt 4.5.2 và dependency tree/lock result.
- Gate: `@nuxt/ui v2`, Directus SDK19, custom modules/plugins, Vite/Nitro/server routes, 9 UI pages, route matrix, SSR, auth, iframe GDDH/e-learning.
- Sửa mã cho Nuxt 4 được phép: nâng deps/config + codemod chính thức của Nuxt + tối đa 10 file sửa tay; vượt ngưỡng = “rewrite hàng loạt” ⇒ DỪNG như dưới. Mọi sửa đổi giữ thành patch (git diff trên bản copy lab) cho G7/DROOT29.
- Nếu `@nuxt/ui v2`/source gãy trên Nuxt4: **DỪNG lane target trước rewrite hàng loạt**; ghi exact files/modules/error. Có thể build Nuxt 3.21.11 + Node24 trong scratch riêng chỉ để chẩn đoán/rollback comparison; **không được đổi TARGET/cutover sang Nuxt3** và không tự mở rewrite ~90 files.
- Baseline memory = CURRENT 512m, heap ~249 MB, OOM lịch sử. TARGET core PASS phải ghi memory/heap/restart metrics.

## G4.6 · Lane D — nginx / Qdrant / Kuma + integrated SAME SLICE
- nginx exact 1.30.5-alpine; `nginx -t`, 132 route matrix.
- Qdrant KEEP 1.16.3 exact digest + data checkpoint; agent-data client 1.15 + legacy `search()` phải PASS. Không nâng Qdrant.
- Kuma KEEP 2.2.1: verify/pin digest; không cần dựng thêm monitor nếu G2 SAME SLICE không yêu cầu.
- Khi A+B+C đủ: chạy **cùng SAME SLICE G2** A/B/C/D + SEC, không đổi expected để che regression; browser thật cho UI, API/Flow/agent-data, ops auth, lab-admin, permission negative cases. Expected G2 chỉ được đổi đúng các breaking đã liệt kê ở G3 (vd `/server/health` 403 → `/server/ping`, `IP_TRUST_PROXY`), mỗi thay đổi ghi nguồn; lệch khác = regression.
- Outside-scope diff = 0 trên VPS1. VPS1 service StartedAt/config/source không đổi. Cuối RUN: e-learning tĩnh VPS2 vẫn 200, CURRENT checkpoint G2 hash không đổi.

## G4.7 · No-AI-Wait / soak memory
Không giữ Mac/Claude Code chờ soak. Nếu integrated TARGET core PASS:
- giao phép quan sát memory/restart Nuxt **≥6 giờ** cho timer/Guard/Kuma/state-file deterministic hiện hữu trên VPS2 (mốc > OOM lịch sử ~5,2h), có watchdog và kết quả bền. Soak phải có **tải tổng hợp do máy chạy** (lặp route matrix/trang theo nhịp ≈ lưu lượng prod đo từ log nginx VPS1), ghi độ dốc heap/RSS + số OOM — soak không tải không có giá trị; hết soak máy tự dừng TARGET (restart=no) và ghi kết quả bền;
- Claude Code ghi `CORE_PASS · SOAK_ARMED` và kết thúc. Host sau đọc state để ACCEPT/FAIL soak; không cần agent sống 6 giờ.
- Không tạo service/DB/token bền mới nếu timer/cron/Guard hiện hữu đủ; transient one-shot được phép nếu có cleanup rõ.
Mọi chờ khác >15 phút: machine-owned hoặc `UNKNOWN`, không ngồi chờ.

## G4.8 · KQ / output
Hồ sơ: `/opt/incomex/work/vps1-up-grade/G4-TARGET-20260930/` trên VPS2; task COLLAB chỉ KQ + bảng lane; view 1 dòng. Không tạo repo file mới.

KQ hợp lệ:
- `KQ@VPSUP-G4-TARGET-PARITY-20260930-01 MACHINE_DONE · CORE_PASS · SOAK_ARMED` nếu integrated target PASS và soak đã bàn giao;
- `... PARTIAL · BLOCKED_OIG_KEY_ONLY` nếu chỉ thiếu key sau khi hoàn tất mọi lane độc lập;
- `... DỪNG · <exact blocker>` nếu target incompatibility/data/security gate fail.
Executor **không tự ghi G4 PASS**, không chạy G5/G6/G7/DNS.

## HISTORY — G3 TARGET STACK đã PASS
**Mọi nội dung từ marker HISTORY này trở xuống chỉ là lịch sử/evidence của G3/SEC-CRED, KHÔNG phải lệnh G4.**

## G3.0 · Mục tiêu duy nhất
Chốt **TARGET STACK exact version + immutable digest + migration order + compatibility/license gates** đủ để GPT + Claude quyết định G3 PASS. Không dựng TARGET, không pull/restart/recreate container, không migrate DB, không đổi compose/DNS/GSM.

CURRENT đã chứng minh ở G2: PostgreSQL 16.13 · Directus 11.5.1 (migration 95/20251103A) · Nuxt 3.20.2 / Node 20.20.x · Qdrant 1.16.3 · nginx 1.29.5 · Agency OS fork · agent-data hiện hành. §8A đã XONG `8681322…`; SEC-CRED PASS.

## G3.1 · Read gate + phạm vi đọc
Đọc AGENTS → task COLLAB §0 + G2 KQ + §8A KQ + P60 → PROMPT này. Xác nhận không có STARTED G3 khác; READY phải = commit cuối chạm file này. Áp **DROOT31** (không miễn cho RUN read-only): ngay sau read-gate PASS ghi `STARTED@VPSUP-G3-TARGET-20260930-01 <UTC> · executor=Claude Code CLI` vào task COLLAB; không ghi được ⇒ DỪNG. STARTED chưa có KQ ⇒ Host/Reviewer không sửa PROMPT/READY và không ghi vào `work/vps1-up-grade/`. Nếu bất kỳ mutation nào trở nên cần thiết ⇒ DỪNG, Host mở RUN khác.

Được đọc:
- VPS1/VPS2 current manifests, compose, package.json/lockfiles, Directus migration/extension metadata, PG extensions/config/FDW/hba/checksum, Qdrant client/API usage, Docker image IDs/digests;
- host VPS1: OS/kernel/Docker Engine/compose version;
- official release notes/docs/registries/licensing;
- G2 sanitized artifacts/checkpoint.

Cấm:
- `docker pull`, restart/recreate/start TARGET, install/upgrade package (digest lấy bằng truy vấn registry chỉ đọc, vd `docker buildx imagetools inspect`/`skopeo inspect`/`crane digest`);
- write DB/Directus/Qdrant/GSM/DNS/config;
- thay image/tag/digest;
- sửa source/runtime;
- test tạo side effect.

## G3.2 · Candidate snapshot phải refresh tại lúc chạy
Không coi số dưới đây là target final; executor phải refresh nguồn chính thức:
- PostgreSQL: so `16.15` (minor an toàn của dòng hiện tại) với `18.6` (major hiện hành); PG19 beta loại.
- Directus: đánh giá tối thiểu **bản 11.x cuối cùng** (đường ít đổi nhất, nếu còn được hỗ trợ bảo mật) + `12.1.1`, `12.3.1`, `12.4.1`. Không mặc định latest: 12.4.0 có potential breaking change; 12.4.1 còn mới. License/OIG + LC1–LC6 là gate.
- Nuxt: candidate `4.5.2`; Nuxt 3 đã EOL. Kiểm toàn bộ source-lock/module/custom Vite config trước khi chọn.
- Node cho Nuxt: candidate `24.x LTS` exact patch hiện hành; Nuxt 4 cần Node >=22 và khuyên active LTS.
- Qdrant: mặc định candidate `KEEP 1.16.3`; chỉ nâng nếu có lợi ích/compatibility/security cụ thể. Nếu lên 1.19.x phải tuần tự 1.17.x → 1.18.x → 1.19.x và chứng minh không còn legacy `/search|/recommend|/discover`.
- nginx/Docker/Kuma/JEV/MCP/Hermes: mặc định KEEP trừ khi có blocker support/security/compatibility được chứng minh.

**Tiêu chí chọn TARGET (theo thứ tự ưu tiên, áp cho kết luận A):**
1. Không thành phần nào EOL/hết hỗ trợ bảo mật lúc cutover; mỗi dòng còn hỗ trợ ≥12 tháng sau cutover.
2. Ít thay đổi nhất mà vẫn đạt (1): ưu tiên minor cùng dòng; mỗi lớp tối đa một major; không thêm major không bắt buộc vào cùng đợt cutover (vd PG 16 còn hỗ trợ tới 11/2028 ⇒ PG 18 chỉ chọn khi có lý do cụ thể; không có thì để thành việc riêng sau 7 ngày theo dõi — ghi ở kết luận B).
3. Độ chín: mặc định GA ≥8 tuần và đã có bản vá sau .0; ngoại lệ phải ghi lý do + bằng chứng + lab gate (P60).
4. Rollback khả thi và đo được (G3.3 mục 7).
5. License LC1–LC6 PASS.

## G3.3 · Inventory bắt buộc trước khi chọn
1. **PostgreSQL**: extensions + versions; checksum hiện tại; data size; collation/locale; `pg_hba` localhost `trust`; 4 FDW mappings `incomex_meta_srv`; auth path; feature/deprecation/breaking 16→18; `pg_upgrade` vs dump/restore; rollback checkpoint. **Base OS/libc của image CURRENT** (bookworm/trixie/alpine): TARGET phải cùng base; khác base ⇒ thêm collation gate (REINDEX index text + `ALTER DATABASE … REFRESH COLLATION VERSION`) vào migration order. Nếu xét 18: kiểm thay đổi layout PGDATA/VOLUME của image 18 + checksum mặc định bật khi initdb.
2. **Directus**: exact schema migration; extension/hook `l2-checkpoint-guard`; custom endpoints/extensions; 128 flows/policies/roles; env flags; WebSocket; health endpoint; breaking 12.0→candidate; OIG key state/activation count/telemetry/PUBLIC_URL; LC1–LC6. **Mọi consumer API Directus** ngoài Nuxt: agent-data, tool `directus_*` của các cổng MCP, Hermes, các DOT `dot-directus-*`, script/cron — ghi endpoint/cách xác thực đang dùng và breaking ảnh hưởng từng cái.
3. **Agency OS / Nuxt**: current fork source-lock, package/lockfile, `@nuxt/ui`, Directus SDK, custom modules/plugins, Vite config, Nitro/server routes, Node-native assumptions; upstream Agency OS không có release để kéo về ⇒ đây là migration của fork — ước lượng khối lượng sửa mã (file/module phải đổi) và nơi giữ mã (mã trên VPS là SSOT). **Baseline bộ nhớ:** lịch sử OOM/restart từ 14/09 + NODE_OPTIONS/heap/mem limit hiện hành ⇒ chuẩn so sánh cho G4 (TARGET không được tệ hơn).
4. **Qdrant**: server/client SDK versions + exact endpoints đang gọi; collection/storage compatibility; nếu KEEP phải chứng minh Directus/Nuxt/agent-data target vẫn tương thích.
5. **Images/digests**: target nào chọn phải có exact immutable digest từ official registry; không dùng `latest`/floating tag; ghi cả index digest (multi-arch) và digest `linux/amd64`.
6. **Host VPS1**: OS/kernel/Docker Engine/compose version + hạn hỗ trợ; EOL ⇒ ghi blocker, không nâng trong G3.
7. **Rollback**: thay đổi có migration schema (Directus, PG major) ⇒ rollback = khôi phục checkpoint trước nâng + image cũ, không dựa vào downgrade; ghi thời gian khôi phục ước tính từ số đo G2/BK1.

## G3.4 · Output bắt buộc
Một bảng duy nhất:
`Component | CURRENT | Candidates | TARGET proposed | Exact digest | Why | Breaking/compat gates | Migration order | Rollback | Evidence/source`.

Thêm 4 kết luận:
A. TARGET tối thiểu ít thay đổi nhưng còn support/security;
B. TARGET đề xuất để dùng dài hạn;
C. thứ tự nâng trên VPS2 G4;
D. blocker/UNKNOWN cần Owner hoặc lab chứng minh.

Nơi ghi: bảng đầy đủ + nguồn trong `/opt/incomex/work/vps1-up-grade/G3-TARGET-20260930/INDEX.md`; task COLLAB chỉ ghi KQ + bảng tóm tắt 1 dòng/thành phần (`Component | CURRENT | TARGET proposed | digest ngắn | gate chính`); `view.html` 1 dòng. Không tạo repo file mới. Commit: `[Claude Code] VPSUP-G3-TARGET-20260930-01 · KQ MACHINE_DONE · …`.

G3 chỉ `PASS` sau khi GPT + Claude đồng thuận exact target/digest. Executor chỉ ghi:
`KQ@VPSUP-G3-TARGET-20260930-01 MACHINE_DONE · TARGET PROPOSAL READY FOR REVIEW`
Không tự ghi G3 PASS.

## G3.5 · Không ngồi chờ đồng hồ
Áp DROOT25/DROOT28 nghiêm: G3 không có lý do soak. Nếu một nguồn/check cần chờ >15 phút, ghi `UNKNOWN/RETRY_BY_MACHINE`; không giữ Mac/Claude Code chờ. Từ G4 trở đi, mọi wait/soak >15 phút phải giao timer/Guard/Kuma hiện hữu hoặc one-shot deterministic trên VPS rồi tiếp tục việc độc lập.

## HISTORY — SEC-CRED / §8A đã hoàn tất
**Mọi nội dung từ marker HISTORY này trở xuống chỉ là lịch sử/evidence của RUN cũ, KHÔNG phải lệnh thực thi G3.**

## 0A. SUPERSEDE — phần rotation cũ đã hoàn tất, CẤM chạy lại

KQ `VPSUP-SEC-CRED-ROTATE-20260929-01` commit `0d9c991…` đã hoàn thành phần kỹ thuật: 2/2 old credential retired, live/searchable old copy = 0, backup sạch mới PASS, production health PASS. KQ vẫn `DỪNG` vì executor dùng READY cũ/HOLD và gate §8A chưa làm.

**RUN hiện hành chỉ làm §8A Điều 30/31.** Lệnh thực thi = khối đầu file này (tới hết mục `Báo cáo §8A`) + checklist kỹ thuật `## 8A` (áp cho mọi target ở “Phạm vi” mục 1, không chỉ delta SEC-CRED). Các mục `## 0`–`## 8`, `## 9`, `## 10`, `## 11` là lịch sử/evidence, **KHÔNG CÒN LÀ LỆNH THỰC THI** (các điều cấm ở `## 11` vẫn giữ). CẤM rotate lại credential, tạo GSM version, redact lại KB/Qdrant, hoặc chạy backup sạch lần nữa.

Cổng §8A hiện hành:
- read-gate: `fs_stat` root gh → đọc `AGENTS.md` → task `COLLAB.md` (Dòng hiện hành, KQ SEC-CRED `0d9c991…`, P50–P55) → file này; READY phải = commit cuối chạm file này;
- dependency = KQ terminal sạch của `MCPW-HERMES-TG-RECOVER-20260929-01`: có `KQ@… XONG` hoặc `DỪNG` sạch/rollback, **và** mọi lệch P02/Guard do chính RUN MCPW gây ra (vd restart Hermes) đã được MCPW tự rebaseline, hoặc được KQ MCPW ghi đích danh là residual của MCPW ⇒ §8A để nguyên, **không rebaseline hộ**, không tính là drift của §8A. READY/STARTED của MCPW chưa phải KQ. Lệch không rõ chủ ⇒ DỪNG;
- collision: root/task COLLAB khác không có `STARTED@` nào chưa có KQ đang chạm Protection/Config Guard, P02 baseline hoặc git `/opt/incomex/dot`; có ⇒ DỪNG;
- áp **DROOT31**: ngay sau read-gate PASS và trước PRE, executor phải ghi `STARTED@VPSUP-SEC-CRED-PROTECT-20260929-01 <UTC> · executor=Claude Code CLI` vào chính task COLLAB; không ghi được ⇒ DỪNG trước PRE/mutation;
- áp **DROOT30**: sau PRE và ngay trước first runtime mutation, đọc lại `COLLAB.md` + `PROMPT.md`, xác nhận READY/HOLD/STOP_REQUESTED không đổi; lệch ⇒ DỪNG.
- Host/Reviewer không sửa PROMPT/READY/HOLD khi STARTED còn sống chưa có KQ.

Phạm vi §8A hiện hành:
1. inventory durable delta **của việc VPSUP trên VPS1**: 4 DOT (`dot-vpsup-pg-role-rotate`, `dot-vpsup-cred-redact` — SEC-CRED; `dot-directus-permission-revoke` — SEC1A; `dot-pg-restore-verify-db` — BK1) + 2 script backup BK1 đã mở rộng (`/opt/incomex/scripts/pg-backup.sh`, `/opt/incomex/scripts/backup-to-gdrive.sh`); config/env/nginx/Kuma đã đổi thì kiểm coverage hiện hữu. Target nào đã có guard hiện hữu ⇒ chỉ chứng minh, không đăng ký trùng;
2. Điều 30: dùng evidence SEC-CRED + smoke/browser hiện tại để chứng minh không hồi quy, không tái rotation;
3. Điều 31: đăng ký các target mục 1 chưa có bảo vệ vào Protection/Config Guard hiện hữu với path/hash/invariant/owner/scope/known-good, **chỉ qua lệnh/đường rebaseline chính thức của Guard (ghi reason + RUN_ID), không sửa tay file baseline**. CẤM chạy `dot-dot-register` chế độ thật (bẫy F1/P16: quét cả file `.bak`, in “Registered” kể cả khi 403). Bằng chứng đăng ký = mục guard đúng path + sha hiện hành + mutant FAIL; DOT chưa vào sổ `dot_tools` = gap ghi 1 dòng, không chặn XONG. Commit git chỉ đúng file đã đổi, không `git add -A`;
4. mutant/negative trên fixture cho từng target phải làm Guard FAIL; không phá production, không bắn tin cảnh báo thật tới Owner;
5. self-protection + watchdog hiện hữu PASS;
6. controlled rebaseline P02 chỉ cho StartedAt/hash/config delta đã được KQ SEC-CRED chứng minh; drift ngoài manifest ⇒ DỪNG, không rebaseline (residual đích danh trong KQ MCPW: để nguyên, ghi lại, không tính là drift);
7. không credential/GSM/business-data mutation;
8. **PRE-only handoff checks, không mở scope sửa:**
   - candidate `Antigravity` (MCPW P50): so vân tay (cùng cách tính của KQ SEC-CRED, không in value) giá trị client đang giữ với vân tay cũ/mới trong KQ SEC-CRED:
     - trùng bản mới hoặc không có ⇒ đóng;
     - trùng bản cũ, client nằm trên Mac Owner ⇒ `OFF_VPS_STALE_CLIENT`, **không chặn**: dùng chính giá trị đó (không in) gọi 1 lần endpoint auth, phải bị từ chối 401/403; rồi cập nhật config client từ GSM không in value như SEC-CRED đã làm với `~/.claude.json`/Claude Desktop; không làm được ⇒ ghi đúng 1 bước Owner;
     - trùng bản cũ, consumer chạy trên VPS1 ⇒ `DỪNG · MISSED_ON_VPS_CONSUMER` (hồi quy của SEC-CRED, không tự sửa trong §8A);
     - server còn nhận credential cũ ở bất kỳ đường nào ⇒ `DỪNG · OLD_CREDENTIAL_STILL_VALID`;
   - failed systemd units: bộ nền = `cloud-init.service` + `systemd-networkd-wait-online.service` (lỗi từ 12/02; Reviewer đo 29/09 ~14:50Z vẫn đúng 2 unit này, `jev-gw-health` không còn lỗi). Trùng bộ nền ⇒ `FOLLOWUP_NOT_BLOCKING` (chuyển sang hạng mục DNS/host-resilience). Unit lỗi mới ⇒ truy nguyên: dính credential đã xoay ⇒ `DỪNG` (hồi quy D30 của SEC-CRED, không phải “unrelated”); dính Protection/Config Guard/watchdog ⇒ `DỪNG`; còn lại (vd mạng/DNS bên ngoài) ⇒ `FOLLOWUP_NOT_BLOCKING`. Không sửa unit trong RUN;
   - sự cố DNS 29/09 là follow-up ổn định hạ tầng sau §8A, **không** được lén sửa DNS/resolver trong RUN protection này.

Acceptance: §8A PASS ⇒ ghi `KQ@VPSUP-SEC-CRED-PROTECT-20260929-01 XONG · SEC-CRED PASS · NEXT G3 TARGET STACK`. Ngoài các gate protection, phải có `STARTED` đúng DROOT31, candidate Antigravity đã disposition, failed units đã disposition và không có blocker protection chưa xử lý. Nếu fail ⇒ `DỪNG` với gap chính xác. Không dùng KQ/RUN_ID cũ cho lượt §8A.

Báo cáo §8A (thay `## 10` cũ): không tạo repo file mới; task `COLLAB.md` = Dòng hiện hành + `KQ@VPSUP-SEC-CRED-PROTECT-20260929-01 XONG|DỪNG` (chỉ tên/path/sha/vân tay, không value); `view.html` 1 dòng; hồ sơ VPS1 ghi tiếp vào `/opt/incomex/work/vps1-up-grade/SEC-CRED-ROTATE-20260929/` (thêm mục §8A trong `INDEX.md` sẵn có, không mở thư mục mới). Commit repo: `[Claude Code] VPSUP-SEC-CRED-PROTECT-20260929-01 · KQ XONG|DỪNG · …`.

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
