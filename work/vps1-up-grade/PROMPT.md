# PROMPT — VPSUP G5 ROLLBACK REHEARSAL · stepwise rollback on VPS2

RUN_ID: VPSUP-G5-ROLLBACK-REHEARSAL-20261001-01
STATUS: **DRAFT — CHƯA READY/RUN. Chỉ READY khi Host đã ghi dòng `G4 PASS` trong COLLAB (PASS có disposition được tính — P84) và activation lab đã release sạch.**
Host: GPT Chat · GPT-VPSUP-20260926-A
Executor_Surface: Claude Code CLI trên Mac Owner.
Report_Write_Path: **workspace_* / Incomex VPS MCP → incomex-workspace/main** (sau MCPW identity cutover; dùng actor `claude-code`).
Runtime_Write_Path: **VPS2 LAB ONLY. VPS1 production = READ-ONLY.** Không DNS/GSM mutation.
Đầu vào: G4C KQ `85b188d8…` CORE_PASS + `soak/FINAL` (08:08Z, VERDICT=FAIL 2/8 đã có disposition P82/P84) + dòng Host `G4 PASS`; checkpoint A; DOT candidate UUID normalize; lane-C Nuxt4 patch; exact image digests.

## G5.0 · Mục tiêu
Chứng minh **rollback thật** trước khi mở G6 cutover rehearsal, theo mô hình 2 tầng để giảm downtime:

- **S1 · SAFE MINORS baseline:** PostgreSQL16.15 + nginx1.30.5 + Qdrant/Kuma exact digest, nhưng Directus11.5.1/schema11.14 + Nuxt3 hiện hành vẫn phục vụ được. S1 sau khi PASS trở thành rollback baseline; không cần quay PG/nginx về minor cũ nếu S2 major lỗi.
- **S2 · MAJOR:** targeted UUID normalize → official Directus12.3.1 migrate → OIG POST `/license` → Nuxt4 patch/runtime.

Nếu S2 fail **trước khi unfreeze write**, rollback = trả activation nếu đã dùng → stop S2 → restore checkpoint pre-S2 → boot Directus11/Nuxt3 trên S1 → SAME SLICE CURRENT PASS. Không có business write mới sau freeze nên không mất dữ liệu.

## G5.1 · Gate/PRE
READY chỉ hợp lệ khi COLLAB có dòng Host `G4 PASS` (PASS có disposition được tính). Soak G4C đã kết thúc: `soak/FINAL` = `VERDICT=FAIL` chỉ ở 2 tiêu chí đã có disposition (P82/P84) — (1) thời lượng tính 5,99994h là lỗi công thức, vòng thật 21649s; (2) 1/12 lượt kiểm license trả `503 Under pressure`, lượt trước/sau và lúc trả đều active. **Executor không dừng vì chữ `VERDICT=FAIL` này và không chạy lại soak.** Chỉ dừng khi:
- `soak/FINAL` khác mô tả trên (thêm tiêu chí trượt, hoặc 6 tiêu chí còn lại không còn đạt: 5xx+neterr ≤0.5% · 0 restart/OOM · Nuxt heap slope ≤5 MB/h);
- `LICENSE_RELEASE_FAILED`, activation slot chưa trả, TARGET còn chạy, egress còn mở, hoặc working DB chứa secret chưa cleanup theo P71/P72;
- checkpoint A + G2 artifacts không còn bất biến.
Gặp một trong các điều trên ⇒ không chạy G5; Host xử lý đúng blocker, không tự repair.

Đọc AGENTS → COLLAB §0 (Đường ray) + KQ G4C/P75–P84 + dòng Host `G4 PASS` → PROMPT này → G4C `INDEX.md` + `soak/FINAL`. Ghi STARTED theo DROOT31; DROOT30 trước first VPS2 mutation.

Snapshot VPS1 read-only: exact CURRENT images/config/source + latest MCP/agent-data state sau B2A; G5 không chạm VPS1.

Chạy **tuần tự từng stack** trên VPS2, kiểm RAM trước mỗi bước (G4C từng OOM PG lab khi chạy song song).

## G5.2 · Quyết định Host về licensing grace
**Không sửa `directus_migrations.timestamp` chỉ để tạo 30-day grace.** Directus12.3.1 lấy Core grace từ timestamp migration `20260507A`; legacy DB thiếu default nên migration row mới NULL. G7 sẽ không dựa grace:
1. trước downtime kiểm OIG secret metadata + licensing endpoint reachability;
2. sau `migrate:latest` phải `POST /license` thành công **trước unfreeze write**;
3. activate fail ⇒ rollback S2 ngay khi write vẫn freeze.
G5 phải diễn tập đúng failure path này.

## G5.3 · Chuẩn hoá target trước rollback test
Reuse, không thiết kế lại:
- `dot-directus-uuid-normalize` + ABC map sha từ G4C; dry-run phải khớp prod-size checkpoint A và plan sha;
- candidate NULL cho đúng 1 `directus_flows.operation` orphan/rỗng;
- extension host patch `^11 || ^12`;
- lane-C Nuxt4 patch hiện hành.

**/login:** G4C phát hiện CURRENT Nuxt3 đã trắng 200, TARGET Nuxt4 thành 500 `$t`. Đây là gap cần đóng trước G6. Dùng patch-candidate nhỏ đã có; tối đa 3 file sửa tay ngoài lane-C patch. Trên lab phải đạt `/login` HTTP 200 + hydrate + không console/server error. Fail ⇒ G5 KQ có blocker `LOGIN_PATCH_FAIL`; rollback rehearsal phần DB có thể vẫn chạy, nhưng Host không G5 PASS/G6.

**Directus admin UI:** không dùng tunnel Mac chậm. Dùng browser/headless sẵn có **ngay trên VPS2/lab network** (reuse Playwright đã có; không install browser mới nếu chưa có) để tải admin HTML/assets và login flow. Nếu không có browser usable thì API login + asset integrity vẫn ghi evidence, nhưng Host quyết blocker sau; không ngồi chờ tunnel.

**Lab key bị lộ transcript G4C:** không reuse/promote giá trị đó; tạo credential lab mới nếu cần. Không rotation production vì fingerprint chứng minh 0 trùng prod.

## G5.4 · Rehearsal S1 baseline
Từ fresh clone checkpoint A:
- boot PG16.15 + Directus11.5.1 + CURRENT Nuxt3 trên S1; nginx1.30.5 exact config; Qdrant/Kuma pin như target;
- SAME SLICE CURRENT expected + agent-data/MCP read consumers sau B2A;
- ghi `S1_BASELINE_PASS` + hash checkpoint pre-S2.
Không chạy lại soak dài.

## G5.5 · Rehearsal activation-failure rollback
Trên copy S1:
1. freeze writes / bắt đầu downtime timer;
2. run UUID DOT + official migrate 12.3.1;
3. **chặn licensing egress có chủ đích**, thử `POST /license` ⇒ phải fail/không active;
4. vì chưa unfreeze, rollback ngay: stop target; discard migrated DB; restore pre-S2 checkpoint; boot Directus11/Nuxt3 on S1;
5. SAME SLICE CURRENT phải PASS; row/value hashes = pre-S2.
Ghi `ACTIVATION_FAIL_ROLLBACK_PASS` + rollback duration. Không được tiêu activation slot.

## G5.6 · Rehearsal full S2 → rollback
Fresh copy S1 khác:
1. freeze write + timer;
2. UUID DOT + migrate official + extension patch;
3. mở licensing tối thiểu → `POST /license` 204, active;
4. Nuxt4 final patch gồm login fix; Directus12 + nginx/Qdrant/agent-data;
5. quick target acceptance: `/server/ping`, OIG active, `/login`, Directus admin browser/API, 132 routes diff đã chốt, permission negatives, representative Flow/agent-data write; **không unfreeze business writes**;
5b. **thử rollback chỉ frontend:** khi Directus12 còn chạy, đổi sang image Nuxt3 CURRENT (không patch, SDK19) → 132 route + 9 trang + auth + browser; ghi `FRONTEND_ONLY_ROLLBACK=PASS|FAIL` kèm lỗi cụ thể; không đổi DB; xong trả về Nuxt4 rồi mới sang bước 6;
6. rollback: `DELETE /license` khi Directus+egress còn chạy → confirm slot giảm → stop S2 → restore pre-S2 checkpoint → boot S1 Directus11/Nuxt3;
7. SAME SLICE CURRENT + hashes PASS.
Ghi forward duration và rollback duration theo từng bước; mục tiêu là runbook G6/G7, không đặt ngưỡng giờ tùy ý.

Nếu deactivation fail: theo P72 giữ DB/PUBLIC_URL đủ retry; không shred và KQ `LICENSE_RELEASE_FAILED`.

## G5.7 · Outputs/KQ
Hồ sơ: thêm `G5/` dưới `/opt/incomex/work/vps1-up-grade/G4-TARGET-20260930/` hoặc thư mục kế cận rõ ràng; không tạo framework mới.

KQ executor hợp lệ:
- `KQ@VPSUP-G5-ROLLBACK-REHEARSAL-20261001-01 MACHINE_DONE · ROLLBACK_PASS · LOGIN_PASS · ADMIN_UI_PASS`
- hoặc cùng `ADMIN_UI_UNVERIFIED` nếu chỉ browser local không khả thi nhưng API/assets PASS;
- hoặc `DỪNG · <exact blocker>`.

Báo: S1 baseline; forward timings (UUID/migrate/license/Nuxt); rollback timings; activation-failure path; final CURRENT hash/SAME SLICE; activation slot before/after; login/admin result; latest agent-data/MCP consumer snapshot; `FRONTEND_ONLY_ROLLBACK`; pressure/503 (P82): cấu hình bộ giới hạn tải Directus 12 (`PRESSURE_LIMITER_*`) so với CURRENT + RAM/CPU/event-loop lab trong lúc chạy — chỉ ghi số, không thêm cổng; dữ liệu cho chính sách sau unfreeze (bảng nào nhận ghi nghiệp vụ trong vận hành thường, cách xuất phần ghi mới nếu phải restore) — Host chốt chính sách, executor không tự quyết.

Executor không tự ghi G5 PASS, không chạy G6/G7/DNS.

## HISTORY — G4C/G4B/G4/G3
**Từ marker HISTORY trở xuống chỉ là lịch sử/evidence, KHÔNG phải lệnh G5.**

## G4C.0 · Quyết định Host và mục tiêu
Host **không chọn F2** (không tự viết DDL thay 2 migration, không tự ghi `directus_migrations`). Chọn **F1 có mục tiêu / upstream-aligned**:
- không đổi cả 324/325 cột `char(36)`;
- chuẩn hoá sang PostgreSQL `uuid` **chỉ** các cột mà Directus 12.3.1 canonical schema yêu cầu là UUID và các cột relation thực sự trỏ tới PK UUID đó;
- business ID `char(36)` không liên quan Directus system UUID giữ nguyên.

Mục tiêu RUN này: trên **working copy của checkpoint A**, tự sinh canonical map từ Directus12.3.1 sạch → phân loại 32 non-UUID → nếu tập candidate sạch/repair được theo luật dưới đây thì normalize trong lab → chạy official `migrate:latest` → nếu PASS tiếp tục Directus runtime + SAME SLICE và arm soak. Không chạm production.

## G4C.1 · Read/PRE
Đọc AGENTS → COLLAB §0 + KQ G4/G4B + P68–P75 → PROMPT này → hồ sơ G4B. READY phải = commit cuối chạm PROMPT. Ghi STARTED theo DROOT31; DROOT30 ngay trước first VPS2 mutation.

PRE:
- checkpoint A content/meta hash = KQ G4/G4B; G2 checkpoint + lane C patch/.output/image digests khớp; TARGET 0 container; e-learning 200;
- OIG key chỉ metadata EXISTS, **không materialize/activate trước khi `migrate:latest` PASS**;
- VPS1 chỉ-read snapshot schema để chứng minh blocker vẫn tương đồng; không query giá trị secret.

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
