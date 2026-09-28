# PROMPT — VPSUP CLONE CURRENT · dựng parity clone CURRENT cô lập trên VPS2

RUN_ID: VPSUP-CLONE-CURRENT-20260928-01
STATUS: Chỉ thực thi sau khi COLLAB có READY đúng SHA commit cuối chạm file này và Owner/GPT Host phát RUN.
Host: GPT Chat · GPT-VPSUP-20260926-A
Host_Revision: VPSUP-P38-CLONE-CURRENT
Executor_Surface: Claude Code CLI trên Mac Owner.
Report_Write_Path: **fs_* / Incomex VPS MCP · root gh → incomex-workspace/main**.
Runtime_Write_Path: Mac Owner điều phối SSH read từ VPS1 + mutation chỉ trên VPS2; VPS1 chỉ tạo/stream snapshot read-only cần thiết, không restart/recreate/config mutation.
Runtime VPS1/VPS2 là SSOT trạng thái thực.
Directus/PG mutation trên clone vẫn = **DOT-only**.

## 0. Mục tiêu duy nhất

Dựng **CURRENT parity clone** đủ thật trên VPS2 để làm baseline cho nâng cấp, nhưng không biến VPS2 thành production thứ hai.

Clone phải giữ:
1. **Dữ liệu/business semantics thật:** DB `directus`, DB `incomex_metadata`, Qdrant business collections, Directus files/uploads và `/opt/incomex/data` business files.
2. **CURRENT runtime thật:** exact image ID/digest + version của PostgreSQL, Directus, Nuxt/Node image, nginx, Qdrant và agent-data cần cho lát cắt parity.
3. **Config/permission/Flow/extension/source-lock thật** ở mức cần chứng minh migration.
4. Một **SAME SLICE cố định** được chạy trên CURRENT và giữ nguyên expected cho TARGET sau.

Clone **không được mang**:
- credential production có thể dùng lại với VPS1/Drive/GitHub/Telegram/OpenAI/GSM/rclone/cloud;
- static token Directus production;
- Directus `KEY/SECRET` production;
- session/login credential production;
- Hermes/Kuma/backup production/git-push/singleton side effect;
- `directus_gov_test_20260602` (TEST-DERIVED);
- DB `workflow` (DEFAULT/rỗng) và `postgres` ngoài DB mặc định container, trừ khi PRE chứng minh runtime hiện hành thực sự tham chiếu;
- `workspace-tools/queue.sqlite` live ledger — clone tạo ledger lab mới, không copy trạng thái execution production.

Đích cuối RUN: **G2 CURRENT parity PASS** hoặc DỪNG với gap chính xác; chưa nâng bất kỳ version nào.

## 1. Read gate / collision gate

1. `fs_stat work/vps1-up-grade/COLLAB.md`.
2. Đọc: `AGENTS.md` → task COLLAB §0 + P01–P07 phần parity/test + G0 KQ + BK1 KQ + FREEZE/TRUST-CLOSE KQ + P30–P38 → PROMPT này → view.html §7–§9.
3. READY phải khớp commit cuối chạm PROMPT.
4. Xác minh `G1 PASS` tại KQ TRUST-CLOSE; VPS2 vẫn:
   - e-learning app/PHP/MySQL/queue stopped/no-autostart;
   - static `elearning.*` 200;
   - 3307/8080 không listener;
   - swap 4 GiB;
   - ≥ khoảng 70 GiB free;
   - outbound trust candidate = 0.
5. Xác minh không có executor/RUN khác đang mutation VPS2 hoặc cùng Docker storage. Có ⇒ DỪNG.
6. AD1-FIX gen2 trên VPS1:
   - không gọi Guard/ruleset;
   - không restart/mutate `agent-data`/`claude-mcp`;
   - không sửa Kuma/watcher.
7. Repo/version conflict tạm thời ⇒ re-read/diff; task path không đổi thì retry. Runtime conflict tuyệt đối không tự vượt.
8. Nếu PRE phát hiện disk free <45 GiB hoặc swap <4 GiB trước khi clone ⇒ DỪNG, không tự cleanup thêm.

## 2. Luật cô lập trước mọi dữ liệu production

**Không boot bất kỳ container clone nào trước khi S1–S4 PASS.**

### S1 · Namespace riêng
- Dùng compose/project/volume/network tên riêng có prefix rõ, ví dụ `vpsup-current-*`; tuyệt đối không dùng tên/volume e-learning.
- Không overwrite source/config/volume e-learning.
- Không bind public `0.0.0.0`/`[::]`.
- Chỉ một cổng HTTP clone được publish nếu cần test UI, bind **127.0.0.1** (ví dụ `127.0.0.1:<lab-port>`); mọi DB/API backend chỉ Docker internal.
- Truy cập từ Mac qua SSH tunnel hoặc SSH local forwarding.

### S2 · Egress fail-closed
- Tạo network/subnet riêng cho clone và chặn egress của clone **trước first boot** bằng cơ chế Docker/firewall hiện hữu.
- Cho phép traffic nội bộ giữa container clone.
- Không allow internet chỉ vì tiện test.
- Nếu cần load image/package, làm ở **staging trước boot** bằng image tar/source đã duyệt; không mở egress cho runtime clone.
- Negative control trước boot: một container probe cùng network không được đi tới internet/GitHub/Telegram/Google.
- Không làm thay đổi rule phục vụ e-learning static/SSH.

### S3 · Không mang secret production
- Không copy `.env` production nguyên xi.
- Không dump/in env value production.
- Clone chỉ dùng **lab-only random secrets** không hợp lệ trên VPS1, root-owned 0600, không commit/log.
- Directus lab `KEY/SECRET`, DB password, API token phải khác production.
- Telegram/GitHub/OpenAI/Agent-data/rclone/GSM/cloud credential = absent/blank/dummy non-routable.
- Nếu một service không thể khởi động nếu thiếu external secret, không được lấy secret prod; ghi GAP và chỉ chạy phần local-safe.

### S4 · Sanitize DB trước first boot — DOT-only
Trước khi Directus/agent-data clone boot:
- Restore DB clone vào PostgreSQL lab đang cô lập.
- Tìm DOT hiện hữu phù hợp; nếu thiếu capability, tạo **một DOT hẹp tự mô tả** theo DROOT27, dry-run mặc định, allowlist đúng container/DB lab.
- DOT sanitize clone tối thiểu:
  - `directus_users.token`: vô hiệu toàn bộ token production;
  - session/refresh/login state có thể dùng lại: xoá/vô hiệu trong clone;
  - không mang credential máy production;
  - nếu cần một API identity để test agent-data/REST, tạo **lab-only token mới** chỉ trong clone, không trùng prod;
  - nếu cần UI Directus ở G2, dùng credential lab-only; không đưa Owner password production vào VPS2.
- Sanitize phải có BEFORE/AFTER count/hash metadata, không in secret.
- Nếu không chứng minh token/session production đã vô hiệu **trước first boot** ⇒ DỪNG.

## 3. Nguồn clone — FULL BUSINESS DATA, không copy rác test

### A · PostgreSQL
Clone:
- `directus` — full schema + business/config/policy/Flow state.
- `incomex_metadata` — full BUSINESS.
Không clone:
- `directus_gov_test_20260602` — TEST-DERIVED.
- `workflow` — DEFAULT/rỗng 0 bảng, trừ khi PRE tìm thấy runtime reference thật.
- `postgres` — dùng DB mặc định mới của container.

Cách lấy:
- Fresh consistent `pg_dump` read-only từ VPS1; stream qua Mac sang VPS2 hoặc staging ngắn trên Mac/VPS2.
- Không đưa password/role hash production vào clone.
- Giữ owner/ACL semantics bằng **lab roles cùng tên cần thiết nhưng lab password khác**, tạo qua DOT; không copy role password hash prod.
- Ghi source snapshot timestamp + row/schema manifest.

### B · Qdrant
- Dùng snapshot business mới nhất hiện hữu ≤24h nếu đủ collection; ưu tiên snapshot job sẵn có.
- Nếu không có snapshot đủ mới/đủ collection, được tạo snapshot bằng cơ chế Qdrant native đã dùng trong backup; không đổi collection data.
- Clone tất cả collection runtime BUSINESS, không chỉ `production_documents` nếu G0/runtime chứng minh collection khác đang được caller dùng.
- Ghi collection list + vector/point count trước/sau.

### C · Files
- Directus files/uploads đúng mount live.
- `/opt/incomex/data` business files.
- **Exclude `workspace-tools/queue.sqlite` và WAL/SHM của nó**; đây là lifecycle ledger runtime, clone khởi tạo mới.
- Exclude temp/cache/log/backup/mission evidence.
- Manifest path/type/size/checksum trước/sau; không in nội dung business.

### D · Config/runtime assets
Mang cấu trúc cần chạy CURRENT:
- compose/config **không secret**;
- nginx config;
- Directus extension/hook `l2-checkpoint-guard`;
- exact Nuxt/current build image + build/source-lock/commit reference cần cho target sau;
- config Qdrant/agent-data ở mức không secret.
Không mang:
- production `.env`;
- Telegram/Kuma/Hermes/GitHub/backup credential/config;
- unrelated service runtime.

## 4. Exact CURRENT images — ưu tiên reuse/stream, không pull tag trôi

CURRENT phải khớp production tại snapshot:
- PostgreSQL 16.13;
- Directus 11.5.1 (DB migration level hiện tại phải được ghi riêng);
- Qdrant 1.16.3;
- Nuxt 3.20.2 / Node 20.20 exact current image;
- nginx 1.29.5 exact current image;
- agent-data exact image digest/StartedAt generation hiện hành nếu đưa vào chain.

Luật:
- Nếu VPS2 đã có image đúng digest ⇒ reuse.
- Nếu thiếu ⇒ ưu tiên `docker save` exact image từ VPS1 → stream qua Mac → `docker load` VPS2.
- Không cho VPS2 giữ SSH key tới VPS1.
- Không `docker pull <floating-tag>` để dựng CURRENT.
- Ghi table `component | VPS1 image_id/digest | VPS2 image_id/digest | MATCH`.

Nếu không thể có exact image cho core `postgres/directus/nuxt/nginx/qdrant` ⇒ DỪNG G2.

## 5. Compose CURRENT tối thiểu

Dựng tuần tự, không chạy CURRENT/TARGET song song:
- postgres;
- directus;
- qdrant;
- nuxt;
- nginx;
- agent-data nếu có thể chạy local-safe với lab-only identity.

Không dựng:
- Hermes;
- claude-mcp/claude-kb;
- cowork-*;
- JEV;
- Kuma;
- backup cron;
- production mail/bot/webhook consumers;
- production GitHub writer.

Nginx clone:
- dùng config parity nhưng publish localhost only;
- các route tới service cố ý không dựng phải có disposition cố định (ví dụ EXPECTED_NOT_IN_CLONE), không “sửa config cho xanh”.

Directus Flow:
- giữ Flow rows/status để parity schema/config;
- egress đã block cứng nên request/webhook ra ngoài không thoát;
- không sửa hàng loạt Flow chỉ để lab yên.
- Nếu schedule local làm thay đổi business table trước khi baseline xong, DỪNG và dùng native supported suppression nếu đã được chứng minh; không direct SQL tắt Flow hàng loạt.

## 6. Agent-data / local consumer

Mục tiêu là chứng minh caller chính vẫn nói chuyện được với CURRENT clone mà không mang secret production.

- Reuse exact agent-data image nếu khả thi.
- Mọi Directus/API credential = lab-only token tạo trong clone.
- DB/Directus URL trỏ clone internal.
- External GitHub/model/Telegram/Drive/GSM = disabled/blank; egress bị chặn.
- `queue.sqlite` lab = file mới/ledger mới, không copy production.
- Chạy tối thiểu:
  - health/read local;
  - 1 read Directus clone;
  - 1 read `incomex_metadata` qua đường được phép;
  - 1 write vào **record test cô lập** qua DOT/API path được duyệt, rồi cleanup qua cùng đường.
- Nếu image hiện tại không thể start local-safe mà không có external prod secret ⇒ ghi `GAP-AD`, không lấy secret prod. G2 chỉ PASS nếu Host/test matrix chứng minh GAP này không làm sai kết luận migration CURRENT; nếu không ⇒ DỪNG.

## 7. SAME SLICE CURRENT — cố định expected cho TARGET

Ưu tiên reuse Playwright/curl/test asset hiện hữu. Chỉ viết script mỏng trong runtime dossier nếu không có cái sẵn; không mở framework test mới.

Lưu runtime dossier:
`/opt/incomex/work/vps1-up-grade/CLONE-CURRENT-20260928/`

### A · Route
Từ nginx live/source config sinh danh sách host/location cần parity.
Trên clone localhost + Host header:
- status;
- redirect;
- cookie/header quan trọng;
- content marker.
Bao gồm ít nhất:
- `vps.*`;
- `directus.*`;
- `ops.*`;
- `giaoduc.*`;
- Knowledge/Reports/Registries;
- `/ui-preview/`;
- route API/Directus chính.
Route tới service cố ý không dựng: ghi expected disposition, không coi 502 là PASS ngầm.

### B · Data
So source snapshot ↔ clone:
- `directus`: schema/object counts + row counts business tables; loại riêng volatile/audit/session và sanitization delta đã biết.
- `incomex_metadata`: schema + row counts/checksum metadata.
- Qdrant: collection + point/vector count.
- files: manifest checksum.
Không yêu cầu clone = live VPS1 tại thời điểm POST; so với **snapshot timestamp**.

### C · UI
Qua SSH tunnel/localhost:
- Nuxt shell;
- Knowledge;
- Reports;
- Registries;
- GDĐH `giaoduc` + iframe e-learning static;
- `/ui-preview/`.
Chụp screenshot/HTTP evidence trong runtime dossier.
Directus admin:
- ít nhất login page/render;
- nếu lab-only admin credential được tạo an toàn qua DOT/native wrapped path thì test login; nếu không, ghi disposition chứ không dùng prod credential.

### D · Consumer/local runtime
- Directus REST local read + write test record;
- DOT/PG local read;
- agent-data local smoke nếu §6 PASS;
- backup/Kuma/Hermes/GitHub/Telegram **không chạy**; chỉ xác minh chúng không được đưa vào clone.

### SEC · Isolation negative controls
Sau khi clone chạy:
- từ clone container: GitHub/Telegram/Google/public internet = FAIL;
- public internet/Mac trực tiếp tới lab published port = FAIL nếu không qua SSH tunnel;
- Mac qua SSH tunnel → clone nginx = PASS;
- không có production secret file/reference trong compose/env allowlist;
- static token prod count in clone = 0;
- e-learning static public vẫn 200;
- VPS1 health không đổi.

## 8. G2 PASS

G2 `CURRENT parity` PASS khi:
1. Exact CURRENT core image digests MATCH.
2. Source snapshot → clone data/config/files match theo §7-B sau known sanitization.
3. Clone boot local-only; 0 public exposure; egress negative controls PASS.
4. 0 credential production trên clone; Directus tokens/sessions sanitized trước first boot.
5. Route/UI/current slice A–D/SEC không còn diff migration-critical chưa disposition.
6. E-learning FREEZE/static invariants vẫn nguyên.
7. VPS1: 0 restart/recreate/config mutation; business data chỉ read/snapshot.
8. Disk VPS2 sau clone còn ≥25 GiB free; swap 4 GiB.
9. CURRENT baseline dossier + exact manifests đủ để TARGET chạy **cùng expected**.
10. Sau baseline: stop CURRENT containers để tiết kiệm RAM; giữ volumes/checkpoint/manifests. Không xoá clone.

DỪNG nếu:
- first boot xảy ra trước S1–S4 PASS;
- phát hiện prod token/secret đã sang VPS2;
- clone có public ingress hoặc egress;
- exact core image không khớp;
- restore/data manifest lệch không giải thích được;
- service gây side effect thật;
- VPS1 bị mutation ngoài snapshot/read-only;
- disk <25 GiB sau clone;
- có active executor conflict.

## 9. Checkpoint để TARGET dùng tiếp

Trước khi kết thúc XONG:
- lưu exact current image/digest table;
- config/source-lock hashes;
- DB snapshot timestamp + manifests;
- Qdrant snapshot/count;
- file manifest;
- sanitization manifest;
- isolation/firewall manifest;
- SAME SLICE expected/results CURRENT;
- rollback/remove instructions cho clone namespace;
- list delta `VPS1_AFTER_CLONE` = các thay đổi production phát sinh sau snapshot (ban đầu có thể rỗng; không giả định sẽ luôn rỗng).

Không tạo production secret copy.

## 10. Report

Không tạo repo file mới.

### `COLLAB.md`
- Dòng hiện hành;
- `KQ@VPSUP-CLONE-CURRENT-20260928-01 XONG|DỪNG`;
- nếu XONG: `G2 CURRENT PARITY PASS · NEXT G3 TARGET STACK`;
- tóm tắt snapshot, exact images, sanitization, isolation, A–D/SEC, disk.

### `view.html`
Thêm/cập nhật khối CURRENT parity:
- source snapshot → clone;
- components/images MATCH;
- data/config/files;
- isolation;
- SAME SLICE A–D/SEC;
- G2 PASS/DỪNG;
- NEXT = G3 chốt exact target versions/digests.

Commit:
`[Claude Code] VPSUP-CLONE-CURRENT · dựng CURRENT parity cô lập`

Kết thúc Owner đúng một dòng:
`XONG` hoặc `DỪNG — <lý do>`.

## 11. Sau RUN — không làm

Không nâng PostgreSQL/Directus/Nuxt/Node/Qdrant trong RUN này.
Không lấy OIG key/activate Directus 12.
Không dựng TARGET.
Không cutover VPS1.
Không bật lại e-learning app.

Nếu G2 PASS: Host mới phát G3 chốt target stack từ nguồn hiện hành rồi mới nâng lab.
