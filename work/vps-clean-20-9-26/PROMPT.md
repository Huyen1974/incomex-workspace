# PROMPT — VPSC R6 · VPS HEALTH + DISK-LEAK CLOSEOUT 05/10/2026

STATUS: **DRAFT — P31 DELTA đang được Host áp; chờ Claude Reviewer xác nhận diff + GPT Host READY**
RUN_ID: VPSC-R6-HEALTH-LEAK-CLOSEOUT-20261005-01
Executor_Surface: Claude Code CLI trên Mac → SSH root VPS theo đường hiện hữu
Write_Path: repo SSOT qua `workspace_*` profile Claude Code; runtime/config qua DOT/script-wrapper + Config Guard
Evidence_Dir: `/opt/incomex/work/vps-clean-20-9-26/R6-20261005/`
DOT 100% cho runtime/data/config; không direct SQL/psql/Directus REST.

## 0 · Đích
VPS khỏe và ổ đĩa không tăng bất thường vì dữ liệu vận hành/tạm không bounded. Sửa gốc trước, đặt trần tự động, dọn phần chứng minh an toàn, đo lại. **Không xoá active/rollback/bằng chứng cần thiết chỉ để đạt số.**

Owner D15 (05/10 15:31): dữ liệu/artifact thực sự không còn dùng thì được xoá. Nếu không còn cần ở VPS nhưng chưa đủ tự tin xoá thẳng, **archive một bản lên Google Drive bằng đường backup/rclone hiện hữu, verify checksum/size/readback rồi mới xoá local**. Không mở lại `vps1-up-grade`.

## 1 · PRE + luật cứng
1. Đọc `AGENTS.md` → root `COLLAB.md` → Bảng + D15 + P29–P32 → audit 05/10 trong `BAO-CAO.md` → PROMPT này.
2. Fresh-check CWEB/HJW/PGNB. Nếu có RUN mutation chung nginx/agent-data/PG/Directus thì phần va chạm **DỪNG**, các phần độc lập A/B/C/E được tiếp tục theo bảng phụ thuộc §7.
3. Baseline: `df -B1 /` + `df -i`; một lượt `ionice -c3 nice -n19 du -x` top-down; reconcile df↔du; `lsof +L1`; container/StartedAt/health; HTTP `/`, `/w/`, Agent Data/UI, knowledge sample; failed units; Kuma/Guard; I/O/load/swap bounded sample.
4. Một lượt full-disk `du/find` duy nhất trong PRE; các lượt sau chỉ đo taxonomy đã lập.
5. **CẤM Docker:** `docker buildx`, `docker builder`, `docker system df|prune`, `docker image prune`, `docker volume prune`, mọi `-f/--force`. Chỉ-read bằng `docker ps`, `docker image ls`, `docker volume ls`, `docker inspect`, `docker info`, log/compose config read-only. Không restart dockerd/containerd, không recreate container trong R6.
6. Không reboot VPS. Không DNS/cert CWEB. Không đổi PG/Directus schema ngoài approved DOT. Không raw dump secret/config.
7. Trước mutation, tạo `MUTATION_MANIFEST`: exact file/config dự kiến sửa + before hash + component + rollback. Chỉ các mục này được rebaseline Config Guard sau verify; file phát sinh ngoài manifest ⇒ DỪNG phần đó.
8. POST-PROTECT bắt buộc: before/after hash, regression, Guard/Config Guard, watchdog/monitor, rollback/known-good, Telegram receipt. Bảng Điều 30/31 còn THIẾU ⇒ KQ PARTIAL.

## 2 · A — Checker truth trước
Phạm vi hẹp: chỉ sửa **cơ chế lỗi thực thi ⇒ ERROR/UNKNOWN, rollup không PASS** và các câu query/checker sai hiện hành; không đổi schema nghiệp vụ.
- Rà 30 check + fresh logs: missing table/column, `enum_range(text)`, `btrim(integer)`, `git_sha`, logger > varchar(50), direct `meta_catalog` write.
- Quét thêm mẫu nuốt lỗi trong DOT/checker: `2>/dev/null || true`, biến rỗng/NULL bị coi 0, default-on-error.
- Caller refresh counts phải dùng approved `refresh_registry_counts`/DOT tương đương; guard direct meta_catalog write giữ nguyên.
- Negative fixtures: lỗi SQL, missing column, wrong type, empty result do execution failure ⇒ FAIL/UNKNOWN.
- Rerun 30 check; từng fail còn lại phân loại `REAL_DATA_ISSUE` hoặc `CHECKER_FIXED/PASS`; 0 SQL execution error ẩn.

## 3 · B — Queue/worker: sửa tối thiểu đúng gốc
Không “thiết kế lại” Queue, không batch metric nếu chưa cần. Chỉ bốn delta:
1. `disk_state()` dùng Queue đã có/reuse và chỉ ghi flag khi giá trị đổi.
2. `migrate_legacy()` đọc flag trước; chỉ `BEGIN IMMEDIATE` khi chưa migrate.
3. Schema/bootstrap chỉ một lần cho mỗi process/path; fast-path constructor/status không migration/write.
4. Worker bắt `database is locked` và retry bounded/backoff, không chết/restart loop.
Giữ nguyên schema, ordering, operation_id idempotency, cancel/critical/recovery semantics.
- Host worker đọc source trực tiếp; container agent-data dùng image. Áp phía host trước; nếu 5s idle đã giảm ≥80% write + 0 lock thì **không rebuild/restart agent-data** chỉ để đồng bộ. Nếu bắt buộc rebuild: dùng DOT deploy hiện hữu + rollback tag + DROOT10.
- Chạy `tests/continuation/` và concurrent status/cancel + 2 job nhỏ + recovery fixture.
- PASS: 0 lock, 0 duplicate job, restart counter không tăng; mẫu 5s idle `syscw` và write_bytes giảm ≥80% từ 840 / 3,33 MB hoặc giải thích chính xác unavoidable writes.

## 4 · C — Inventory top-down + bounded storage

### C0 · Không bỏ sót
- Top-down `du -x /`; tổng taxonomy + `CHƯA_PHÂN_LOẠI` phải giải thích df-used. `CHƯA_PHÂN_LOẠI > 1 GiB` ⇒ tách tiếp đến dưới ngưỡng.
- Giải thích ≥90% phần tăng 43%→66% theo ngày/sự kiện bằng `logs/disk-monitor.log`.
- Inventory bắt buộc thêm: `directus_gov_test_20260602`; `/opt/incomex/work/**`; `/opt/incomex/logs`; Docker image/container logs/writable layers/volumes; PG WAL/temp; Qdrant; `/tmp`/`/var/tmp`/`/var/cache`; journal/coredump; workspace results/uploads/jobs/transactions; `/var/lib/hermes`; home/cache công cụ AI; kernel cũ; inode hotspots; 2 PG18 quarantine + PG16 cũ.
- Business/live data = `BUSINESS_GROWTH`: không cap/xoá mù nhưng có owner + expected growth.
- Mỗi non-business group phải có: `current_bytes · growth_driver · hard_cap_bytes · TTL/age · protected_set · cleanup_trigger · owner`. Thiếu trường ⇒ STORAGE_BOUND chưa PASS.

### C1 · Log
Mở rộng logrotate hiện hữu cho `/var/log/incomex` và `/opt/incomex/logs` append logs. Chọn reopen/copytruncate theo writer thật; numeric size cap + age + compress. Verify writer vẫn ghi sau rotate.

### C2 · CWEB/deploy
Reference graph từ compose/systemd/nginx/symlink/manifest/deploy/rollback. Bảo vệ current CWEB + exact rollback còn hiệu lực. Build/prepared/repair/retained cũ chỉ candidate khi 0 reference + reproducible.
Không thêm regex từng tên mới làm giải pháp gốc; dùng storage registry §C7.

### C3 · Workspace transactions
- `prepared/push_unknown/rollback_conflict` luôn giữ.
- Completed: chỉ compact/GC bulky before-image khi commit tồn tại trên remote + before/after hashes đủ truy vết; giữ manifest/audit metadata.
- Có age + size high-water; dry-run + pending fixture phải chứng minh recovery-needed không bị đụng.

### C4 · Residual VPSUP + DB thử
Nhóm dữ liệu `D`: PG16 cũ, `postgres18.failed-g7-03`, `.failed-g7-05a`, DB `directus_gov_test_20260602`.
Điều kiện:
- 0 live mount/ref/unit/container;
- current PG18 healthy;
- backup PG18 **sau cutover** ở Drive + restore-verify PASS;
- DB test: logical dump qua DOT → Drive → checksum/list/readback verify trước DROP.
Nếu không còn runtime use nhưng vẫn có nghi ngờ phục hồi: **archive cold copy lên Drive trước khi xoá local**:
- raw dir/old cluster: stream archive one-by-one qua rclone/đường backup hiện hữu, tránh tạo duplicate lớn trên VPS; manifest + SHA256/size + Drive object listing/readback;
- chỉ khi offsite verify PASS + Host approve đúng SHA plan mới xoá local.
Hồ sơ `/opt/incomex/work` không xoá trong R6; chỉ report bytes/đề xuất offsite archive cho task Done.

### C5 · Existing bounded groups
Recheck Docker image keeper/build cache, PG backup, Qdrant snapshots, Owner View revisions, context pack, workspace results TTL. Naming mới không được bypass keeper.

### C6 · Storage registry: tên lạ = đỏ
Dùng cơ chế hiện hữu `vps-retention.sh` + `disk-monitor.sh`; registry machine-readable mỗi dòng:
`path_pattern | class | cap_bytes | ttl | protected_set | owner`.
Phủ ít nhất direct children của `/opt/incomex/deploys`, `/opt/workflow`, `/opt/incomex`. Mục không match registry và tồn tại >24h ⇒ đèn #11 đỏ + tên, **không tự xoá**.
`/opt/incomex/work`: cap tổng + per-task, không auto-delete evidence.
Negative fixture: unknown-dir age giả ⇒ đỏ; remove fixture ⇒ xanh.

### C7 · Slope alert + watcher
`disk-monitor.sh` mỗi giờ ghi df bytes; mỗi ngày ghi bytes theo storage registry taxonomy.
Đèn #11 đỏ khi **bất kỳ**:
- used ≥80%;
- free giảm ≥2 GiB/24h;
- free giảm ≥3 GiB/7 ngày;
- unknown path >24h.
Thử âm fixture trước PASS. RUN chỉ smoke ≥30 phút; kết luận “hết rò” cuối cùng lấy từ **một chu kỳ ngày** do máy tự ghi sau R6, không dựa Mac/người quay lại đo. Sau RUN có thể ghi `POST_WATCH_REQUIRED`; Owner không phải làm gì.

## 5 · F0 — Destructive plan + duyệt SHA
Agent **không tự xoá**.

Lập canonical delete plan, mỗi dòng:
`group | path/id | bytes | reason | reference_proof | recovery/offsite | sha256/object`.
Tách:
- **T** = tái tạo được (obsolete build/prepared/repair/retained, rotated logs/cache).
- **D** = từng là data/rollback: PG16 cũ, 2 PG18 failed dirs, `directus_gov_test_20260602`.

Tính `PLAN_T_SHA256`, `PLAN_D_SHA256`, ghi vào COLLAB.
- T: chỉ xoá sau `HOST_APPROVED_DELETE_T@<sha>`.
- D: Owner D15 đã cho phép nguyên tắc; vẫn chỉ xoá sau `HOST_APPROVED_DELETE_D@<sha>` và điều kiện C4 PASS.
- Ngay trước xoá tính lại canonical SHA; lệch ⇒ không xoá.
- Nếu Host chưa duyệt trong cùng phiên: giữ nguyên, ghi `PROTECTED_WAITING_APPROVAL`, các phần khác tiếp tục.
- Nếu artifact D không còn dùng nhưng proof chưa đủ tự tin: archive Drive + verify như C4 trước khi đưa vào D plan.
Sau cleanup chạy dry-run lần 2 ⇒ 0 destructive candidate mới nếu không có dữ liệu hợp lệ mới.

Mục tiêu capacity = **45 GiB free** (= 48,3 GB thập phân), chỉ là target; không xoá protected data để đạt số.

## 6 · D — Knowledge performance: DEFER nếu CWEB chưa cutover
Phần này chạy sau cùng.
- Nếu CWEB chưa `CUTOVER XONG`/chưa ở done-tasks: chỉ đo + chuẩn bị source patch; **không build/deploy Nuxt**, ghi `KNOWLEDGE=DEFERRED_CWEB`; không làm R6 fail.
- Sau CWEB cutover: dùng đúng DOT deploy quản `nuxt-output-n4`, giữ patch CWEB, update rollback known-good, chạy lại regression CWEB.
- Bỏ initial full-tree; minimal index/lazy branch/versioned cache; không đổi ACL.
- Target ≥60% raw bytes reduction và local p95 ≤1,5s; đo raw bytes + TTFB. Không UA-block thô làm giải pháp chính.

## 7 · E — HTTP/Hermes/OS + bảng dừng/tiếp
A, B, C, E độc lập: phần nào trượt thì ghi blocker rồi tiếp tục phần độc lập khác.
F phụ thuộc C + Host approval. D phụ thuộc CWEB gate.
- Correlate presence 502/root 404/503 theo timestamp/backend; chỉ sửa khi có root cause; không tăng timeout/restart/tắt alert để che.
- Hermes chỉ technical maintenance proof được; không chen thiết kế HJW.
- Không đổi PG config.
- failed units: phân biệt boot-old/current. Reboot-required chỉ lập preflight/rollback/time proposal; **không reboot R6**.

## 8 · Cleanup/POST-PROTECT/nghiệm thu
Sau mutation:
- core containers/StartedAt expected; `/`, `/w/`, Agent Data/UI, Directus, PG, Qdrant, critical CWEB; Guard/Config Guard/Kuma same-or-better;
- rebaseline **chỉ** file trong MUTATION_MANIFEST, ghi before→after hash + reason;
- Điều 30/31 coverage THIẾU 0; rollback/known-good; Telegram receipt;
- storage inventory cuối đủ taxonomy; every non-business = BOUNDED hoặc blocker;
- capacity ≥45 GiB nếu đủ candidate safe; nếu không, report exact protected bytes, không xoá mù.

## 9 · Root-policy proposal (không gate R6)
Ghi một đề xuất vào P/KQ để Founders cân nhắc đưa lên root:
POST-PROTECT của mọi task thêm cột `để lại gì trên đĩa | bytes | hạn giữ | owner`, để task mới không tạo hàng tồn vô hạn. Không tự sửa luật root trong R6 nếu chưa có quyết định riêng.

## 10 · KQ
KQ@VPSC-R6-HEALTH-LEAK-CLOSEOUT-20261005-01 XONG|DỪNG · DISK=<used/free> · CHECKER=<...> · QUEUE=<...> · STORAGE_BOUND=<...> · DELETE_T=<...> · DELETE_D=<...> · KNOWLEDGE=<PASS|DEFERRED_CWEB|...> · HEALTH=<...> · WATCH=<PASS|POST_WATCH_REQUIRED>

Cập nhật Bảng + `BAO-CAO.md` cùng commit KQ. Không tự archive; Host nghiệm thu.
## C5 Existing bounded groups
- Recheck Docker image keeper/build-cache 5 GB, PG backup keeper, Qdrant snapshots, Owner View revisions, context pack, workspace results TTL. Nếu keeper đang fail/không còn match naming mới thì sửa cùng cơ chế hiện hữu, không dựng cleaner song song.

## 5 · D — Knowledge payload / bot pressure
- Xác định đúng source đang render `/knowledge/...`; không thay ACL/public-private trong RUN nếu chưa có quyết định.
- Bỏ fetch full-tree `limit:-1` ở initial render: index/menu tối thiểu + lazy branch hoặc cache versioned dùng chung; chỉ fields cần thiết; cache/compression qua đường hiện hữu.
- Crawl: dùng robots/cache/rate controls phù hợp, không block người dùng thật bằng UA heuristic thô.
- Acceptance: cùng trang VPS architecture initial bytes giảm **≥60%** từ ~3,19 MB, 10 request local p95 ≤1,5 s hoặc ghi blocker định lượng; 0 Nginx temp-file buffering cho test target nếu response đã dưới buffer hợp lý; UI/content không mất.

## 6 · E — HTTP/Hermes/OS maintenance
- Correlate `/api/presence/event` 502 và root 404/503 theo timestamp/request/backend. Chỉ sửa khi có root cause; không restart/tăng timeout/tắt alert để che.
- Hermes: chỉ xử lý serve/gateway version/job-lifecycle nếu thuộc technical maintenance đã proof; không chen vào thiết kế HJW hiện hành.
- `cloud-init`/`networkd-wait-online`: xác định boot-old vs current impact. `reboot-required`: lập preflight + rollback + thời điểm đề xuất, **không reboot trong R6**.

## 7 · F — Cleanup execute + nghiệm thu
- Trước destructive cleanup tạo canonical plan: path/id · bytes · reason · reference proof · rollback/recovery replacement · SHA256 plan. Chỉ xóa/move đúng allowlist đã proof ở C; ambiguous ⇒ giữ.
- Sau fix/cleanup: disk target **free ≥45 GB** nếu đủ candidate an toàn; nếu protected artifacts khiến <45 GB thì KQ PARTIAL + exact protected bytes, không xóa mù. **45 GB chỉ là mục tiêu capacity, không thay tiêu chí leak-closed.**
- Core: containers/StartedAt expected, `/`, `/w/`, Agent Data/UI, Directus, PG, Qdrant, CWEB routes critical, Guard/Config Guard/Kuma same-or-better; không secret leak.
- Storage inventory cuối phải có `group · bytes · growth source · hard_cap_bytes · TTL/age · protected_set · next cleanup · owner`; mọi non-business source = BOUNDED hoặc blocker rõ.
- **Slope proof:** chụp bytes theo cùng taxonomy tối thiểu tại PRE, ngay sau cleanup, và ≥2 mốc sau đó trong cửa sổ ≥30 phút khi hệ thống idle/hoạt động bình thường; với nguồn theo job, chạy/quan sát đúng một trigger đại diện nếu an toàn. Tính Δbytes/time theo group. Không được kết luận “đã hết rò” chỉ từ một snapshot. Nếu không thể chờ đủ cửa sổ trong RUN, cài/giữ watcher hiện hữu + ghi `POST_WATCH_REQUIRED`; Host chỉ đóng hoàn toàn sau cửa sổ hậu kiểm.
- Cleaner/keeper đã sửa phải rerun dry-run lần 2 ⇒ 0 candidate mới ngoài dữ liệu phát sinh hợp lệ.
- Performance POST: cùng bounded sample PRE/POST, không tăng iowait/swap churn/load bất thường; nếu load còn cao phải chỉ ra process/container causal.
- Gửi Telegram receipt theo R4 nếu có production mutation.

## 8 · KQ
PASS chỉ khi: checker truth contract PASS · worker lock/write PASS · retention/caps PASS · safe cleanup proof · knowledge performance PASS hoặc blocker được Host chấp nhận · core health same-or-better.
KQ: `KQ@VPSC-R6-HEALTH-LEAK-CLOSEOUT-20261005-01 XONG|DỪNG · DISK=<used/free> · CHECKER=<...> · QUEUE=<...> · STORAGE_BOUND=<...> · KNOWLEDGE=<...> · HEALTH=<...>`.
Cập nhật Bảng + `BAO-CAO.md` cùng commit KQ. Không tự archive; Host nghiệm thu.

## HISTORY — R5b terminal, KHÔNG CHẠY PHẦN DƯỚI

# PROMPT — VPSC · R5b tiếp nối R5: nạp trần build cache (B5) + tập GIỮ image hữu hạn (KEEP_SET v2) — CÓ MUTATION, XOÁ IMAGE CHỈ SAU KHI HOST DUYỆT (PHẦN F)

RUN_ID: VPSC-R5B-20260924-01
Soạn: Claude Chat (Host CLAUDE-VPSC-260920-A), 23/09/2026, sau R5 DỪNG ở B5 (BAO-CAO mục R5, `40c7b73`) và P25 của GPT. **Không chạy lại A, C của R5** (live-restore đã bật; luật (l) đã cài; 3 tag đã xoá hợp lệ). Chỉ làm: (B5) restart dockerd 1 lần có kiểm soát để nạp trần 5GiB; (C') đổi tập GIỮ của luật (l) sang KEEP_SET v2 hữu hạn, cài ở **chế độ thử (không xoá)**, lập kế hoạch xoá cho Host duyệt. Lượt xoá thật chỉ chạy **trong cùng phiên (Phần F)** sau khi Host ghi `HOST_APPROVED_DELETE@<sha256 kế hoạch>` vào COLLAB (nguyên tắc Owner: hành động phá huỷ không để agent tự quyết; JEV host_checkpoint 0,66). Đã áp P26: làm ngay hôm nay, không chờ qua đêm. Đã áp P27: trap bật lại cron, không mất job ngoài nhóm lặp, sha256 trên danh sách xoá chuẩn hoá.
Chỉ chạy khi COLLAB có **`GPT REVIEWED@` + `OWNER_APPROVED@` + Host `READY@` cùng full SHA** commit cuối chạm file này + lệnh RUN.
**Executor_Surface = Claude Code CLI trên Mac → shell root VPS qua SSH, mở bằng `claude --dangerously-skip-permissions`** (Owner cho phép rõ 1 lần `systemctl restart docker` theo B5 — D13). **Write_Path = `fs_*` (gh)**, dự phòng `workspace_*`. Không clone, không ghi repo bằng git.
**Chế độ (D08):** luật cứng dưới đây thay van tự động. Nếu một lệnh vẫn bị bộ phân quyền của phiên chặn → **không lách**, ghi lại và áp nhánh DỪNG tương ứng. Giờ ghi UTC (Z); VPS giữ Europe/Berlin; cron đọc giờ máy và bỏ qua `CRON_TZ`.

## 0. Cổng (chỉ đọc)
1. Read-gate: đọc `AGENTS.md` → `work/vps-clean-20-9-26/COLLAB.md` (A0 vòng 2, D08, D10–D13, P18–P25) → `PROMPT.md` → mục R5 của `BAO-CAO.md`; giấy phép khớp SHA; thiếu `GPT REVIEWED@` → DỪNG.
2. NO_CONCURRENT_VPS_MUTATION — kiểm lại đầu mỗi phần: không `docker build`/`buildx`/`compose … --build`/`buildctl`/`docker pull`/deploy đang chạy; không RUN việc khác đang đụng VPS.
3. Chụp trạng thái trước: `df -B1 /`; `docker ps` (12 container + health + StartedAt); `docker info --format '{{.LiveRestoreEnabled}} {{.ServerVersion}}'` phải `true 29.2.1`; `/etc/docker/daemon.json` sha256 = bản A của R5 (`3ceba3d8…`); web 200; Directus health; Qdrant green + points; `systemctl --failed`; `incomex-kuma-push` active; sha256 cấu hình rclone hiện hành; `ss -ltn`.
4. Hồ sơ: `/var/lib/incomex-audit/VPSC-R5B-20260924/`; dùng lại tệp của R5 ở `/var/lib/incomex-audit/VPSC-R5-20260923/` (`12-daemon.json.B`, `cua-so.py`) sau khi kiểm sha256 khớp BAO-CAO R5.

## 1. Luật cứng
- **CẤM:** `docker buildx …`, `docker builder …`, `docker system df|prune`, `docker image prune`, **`docker image rm` (chỉ trong Phần F, đúng kế hoạch đã duyệt)**, mọi `-f/--force`. Docker chỉ được: `docker ps`, `docker image ls`, `docker inspect` (kể cả `--type=image`), `docker info`, `docker version`, `docker logs`, `docker compose … config --images` (chỉ đọc), `docker start <container>` (chỉ trong nhánh lùi B5, đúng container bị dừng, không recreate).
- dockerd: `systemctl restart docker` **đúng 1 lần ở B5** (+ 1 lần lùi nếu B5 hỏng); tuyệt đối không restart khi `LiveRestoreEnabled` ≠ true. Không stop/restart/recreate container; không restart containerd.
- Bí mật: không in nội dung `.env`/token/cấu hình rclone.
- Script trong `/opt/incomex`: commit git cục bộ trước/sau, `bash -n`, thử khô. File ngoài git (`/etc/docker/daemon.json`): bản cũ + sha256 vào hồ sơ trước khi sửa.
- Người gác `scripts/vps-retention.sh`: luật (a)–(k) giữ nguyên từng byte; chỉ sửa phần luật (l).
- Không đụng Kuma, cấu hình backup Drive, múi giờ; không sửa lịch cron/timer. Ngoại lệ duy nhất: `systemctl stop cron` / `systemctl start cron` trong cửa sổ B5 (P26).
- Sau mỗi phần kiểm health như cổng 3; xấu đi → lùi phần đó → DỪNG.

## Phần C' — KEEP_SET v2 hữu hạn (làm TRƯỚC cửa sổ B5, chế độ thử)
C'1 Sửa luật (l) — **chỉ thay định nghĩa tập GIỮ + thêm công tắc xoá**, giữ nguyên cơ chế resolve (tag / `repo@sha256` / Compose sau nội suy → ImageID bằng `docker inspect --type=image`), fail-closed P22, `CANH_BAO`, gác build/pull/deploy, khoá, lịch Chủ nhật 02Z:
   - **Công tắc xoá** `L_XOA` trong script, mặc định **0**: lượt hằng tuần chỉ lập kế hoạch + ghi log (như `--chi-l-thu`), không xoá. R5c mới đặt 1.
   - **KEEP_SET v2 = (1) ∪ (2) ∪ (3) ∪ (4):**
     (1) ImageID của mọi container (chạy hoặc dừng).
     (2) **ACTIVE_ROLLBACK_SET** = ImageID resolve từ **chuỗi đang hoạt động** thôi: gốc = compose + `.env` của các project có container đang tồn tại; unit incomex trong `/etc/systemd/system` (không phải unit của gói OS) cùng `EnvironmentFile=`, chương trình `Exec*=`, đích symlink, include (`source`/`.`/`--env-file`/`compose -f`) theo đường dẫn cố định; script deploy/rollback của dịch vụ sống và **con trỏ/manifest rollback mà chính script đó đọc khi lùi**. Bản sao `.bak`, `backups/`, ghi chú rollback, tài liệu, bằng chứng, thư mục deploy lịch sử **không phải gốc** (giữ làm lịch sử, không bắt giữ image) — trừ khi nằm trên chuỗi đang hoạt động.
     (3) 2 ImageID khác nhau mới nhất (theo Created), ngoài (1)(2), **trong cùng repository với image đang chạy của mỗi container** (đường lùi theo dịch vụ). Repository không có container nào dùng thì không có (3).
     (4) **Ân hạn:** mọi ImageID tạo trong 30 ngày gần nhất.
     Mọi tag trỏ vào ImageID thuộc KEEP_SET được giữ; `<none>` chỉ vào kế hoạch xoá khi ngoài KEEP_SET.
   - **5 diễn giải phạm vi (D13, theo P25):** (i) bỏ tài liệu/bằng chứng/mã nguồn — **trừ** tệp nằm trên chuỗi đang hoạt động; (ii) tệp gói OS nguyên gốc chỉ được bỏ khi nằm ngoài chuỗi đang hoạt động; nếu unit/wrapper incomex gọi tới nó và nó có thể gọi Docker/Compose hoặc trỏ tham chiếu triển khai thì phải quét; (iii) `EnvironmentFile=-…` tồn tại thì phải quét, chỉ khi thiếu mới không tính unresolved; đường dẫn động trên chuỗi đang hoạt động có thể quyết định image mà không resolve được → unresolved (P22); (iv) tag được tham chiếu nhưng không còn trên máy = `ABSENT`, log riêng, không tính unresolved; (v) thiếu `env_file` mà `image:` là chữ cố định → resolve theo chữ **chỉ khi** chuỗi không có nội suy và tệp/project compose xác định chắc chắn; ngược lại unresolved.
   - **Trần v2 (ghi vào báo cáo bằng số):** |KEEP_SET| ≤ |(1)| + |(2)| + 2×(số repository có container) + (số ImageID tạo trong 30 ngày). Không còn số hạng tăng theo số tệp `.bak`/ghi chú.
C'2 `bash -n`; thử khô với `docker` giả (bản sao script, log/khoá riêng): giữ nguyên các ca P20–P24 của R5 đang đạt; thêm ca: `.bak`/`backups/`/ghi chú tham chiếu image cũ >30 ngày → vào kế hoạch xoá; cùng image đó <30 ngày → giữ; con trỏ rollback do script rollback sống đọc → giữ; repository không container, >30 ngày, ngoài (2) → vào kế hoạch; `EnvironmentFile=-` tồn tại chứa tham chiếu → giữ; đường dẫn động trên chuỗi đang hoạt động → unresolved; thêm 5 tệp `.bak` mới → |KEEP_SET| không đổi; `L_XOA=0` → không có lệnh `rm` nào được gọi. diff chỉ trong phần (l). Commit git cục bộ.
C'3 Chạy thật chế độ thử trên dữ liệu thật → **kế hoạch xoá** (JSON trong hồ sơ + sha256) + đối chiếu chéo độc lập (mã riêng): giao KEEP_SET = 0; không ImageID của 12 container; mỗi repository có container còn ≥ image đang chạy + đường lùi; unresolved làm mất trần = 0 (khác 0 → `IMAGE = PENDING_UNRESOLVED`). **Không xoá gì.** Báo cáo: bảng theo repository (ImageID hiện · giữ theo (1)(2)(3)(4) · sẽ xoá · GiB ước tính giải phóng), danh sách sẽ xoá (repo:tag · ImageID ngắn · Created · vì sao không giữ), trần v2 bằng số, sha256 kế hoạch.

## Phần B5 — Restart dockerd có kiểm soát để nạp trần build cache 5GiB
B5.1 Dùng đúng `12-daemon.json.B` của R5 (live-restore + log-opts + `builder.gc {enabled: true, defaultMaxUsedSpace: "5GB"}`), kiểm sha256 khớp R5 (`f0c9c4a7…`) + `dockerd --validate` OK.
B5.2 **Cửa sổ bảo trì chủ động (P26) — làm ngay, không chờ giờ tự nhiên:** (a) không job nào gọi Docker đang chạy/giữ khoá; (b) không backup/deploy/job giờ cố định nào rơi trong 15 phút tới; (c) không systemd timer incomex nào đến hạn trong 10 phút tới (timer không tạm dừng, không sửa). Chưa đạt → chờ, tối đa 15 phút; vẫn chưa đạt, hoặc có timer `Persistent=true` gọi Docker sẽ rơi vào cửa sổ → `PENDING_RESTART` → DỪNG. Đạt → chạy toàn bộ B5.2–B5.5 bằng **một script duy nhất** trên VPS; dòng đầu tiên ngay sau `systemctl stop cron` là `trap 'systemctl start cron; systemctl is-active cron' EXIT INT TERM` (P27) — lỗi, bị chặn hay dừng giữa chừng thì cron vẫn được bật lại; sau script agent kiểm lại `cron` active. **(d) Không mất job ngoài nhóm lặp (P27):** trước khi dừng, liệt kê mọi dòng cron (mọi user + `/etc/cron.d` + `/etc/crontab`) đến hạn trong 10 phút tới; chỉ được bỏ lỡ một lượt của job lặp chu kỳ ≤10 phút (ghi tên, kiểm lượt kế tiếp chạy tốt); có bất kỳ job nào khác đến hạn → chờ (tính vào 15 phút), không dừng cron. Chờ job cron đang chạy (nếu có) kết thúc rồi mới restart.
B5.3 Ngay trước: cổng NO_CONCURRENT + chụp lại như cổng 3. Cài `12-daemon.json.B` → `systemctl restart docker` đúng 1 lần.
B5.4 Kiểm (≤3 phút): `systemctl is-active docker`; `LiveRestoreEnabled` = true; 12 container running, **StartedAt không đổi**, health như cổng 3; web 200; Directus ok; Qdrant green + đủ points; cổng nghe như trước; Kuma running + `incomex-kuma-push` active (unit `Requires=docker` sẽ khởi động lại theo) + `kuma-push.sh cron|disk` rc=0; `rclone lsf gdrive-backup:` rc=0; journal dockerd không lỗi → `systemctl start cron` → lượt kế tiếp của các job `*/5` và `*/10` gọi `docker exec` chạy bình thường → `BUILD_CACHE = BOUNDED · 5GiB · đã nạp qua restart`. **Cron phải được bật lại trong mọi nhánh** (kể cả lùi/DỪNG).
B5.5 Hỏng bất kỳ điểm nào → cài lại bản A (`3ceba3d8…`) → `systemctl restart docker` (lần lùi) → container nào dừng thì `docker start` đúng container đó → kiểm lại → `systemctl start cron` → `BUILD_CACHE = LUI` → DỪNG. Lệnh restart bị bộ phân quyền chặn → `PENDING_RESTART` → DỪNG (không lách).

## Phần D — Kiểm cuối (hỏng → lùi phần gây ra → DỪNG)
- Kuma → Telegram: container Kuma running/healthy; `/etc/cron.d/kuma-push` nguyên; `kuma-push.sh cron|disk` rc=0; `incomex-kuma-push` active.
- Backup Drive: sha256 cấu hình rclone không do lượt này ghi (token tự làm mới bởi cron phái cử được ghi chú nếu đổi); mọi tệp cron/timer trùng byte bản chụp; `rclone lsf gdrive-backup:` rc=0.
- Health như cổng 3; `systemctl --failed` chỉ còn `cloud-init`, `systemd-networkd-wait-online`; `cron` active; số image chỉ giảm đúng số mục kế hoạch đã duyệt (nếu F chạy).

## Phần F — Xoá theo kế hoạch Host duyệt (cùng phiên)
F1 Sau C'3 + B5 + D: **sha256 kế hoạch = sha256 của danh sách xoá chuẩn hoá (P27)**: mỗi mục một dòng `<repo:tag hoặc <none>>\t<ImageID đầy đủ sha256:…>`, bỏ trùng, sắp xếp `LC_ALL=C sort`, xuống dòng LF, không có thời gian/kích thước/metadata động. Ghi kế hoạch + sha256 vào BAO-CAO + COLLAB (dòng `VPSC.9` = `CHO_HOST_DUYET · sha256=<…>`), trả Owner 1 dòng `CHỜ DUYỆT · VPSC-R5b · sẽ xoá <n> image (~<GiB>) · sha256=<…>`, rồi chờ: đọc COLLAB 2 phút/lần, **tối đa 60 phút**, tìm dòng `HOST_APPROVED_DELETE@<đúng sha256 đó>`.
F2 Có duyệt → cổng NO_CONCURRENT → tính lại danh sách xoá chuẩn hoá theo đúng cách F1: sha256 phải trùng (khác → DỪNG, không xoá) → đặt `L_XOA=1` (commit git cục bộ) → `--chi-l` xoá đúng các mục kế hoạch bằng `docker image rm` không `-f` → `du` kho image trước/sau; 12 container StartedAt không đổi + health như cổng 3; `--chi-l-thu` sau đó = 0 mục.
F3 Hết 60 phút chưa có duyệt → giữ `L_XOA=0`, KQ DỪNG `CHO_DUYET` (Host duyệt sau thì chạy lại riêng F).

## Phần E — Báo cáo + ghi repo
- Chèn mục "R5b — Tiếp nối: B5 + KEEP_SET v2 · <ngày> · executor=… · write_path=… · KQ <XONG|STOPPED · bước>" lên ĐẦU `BAO-CAO.md`: (1) CHO OWNER ≤5 dòng; (2) B5; (3) KEEP_SET v2: 5 diễn giải đã áp, bảng theo repository, danh sách sẽ xoá, trần v2 bằng số, sha256 kế hoạch; (4) trước/sau; (5) đường lùi + hồ sơ.
- Repo công khai: không secret/token, IP/tên miền nội bộ, tên tài khoản, output lệnh thô.
- COLLAB: sửa dòng `VPSC.9` thành `MACHINE_DONE · R5b · … · đã xoá theo kế hoạch sha256=<…>` hoặc `STOPPED · <phần.bước> · <lý do>`; ngay dưới thêm đúng một dòng `KQ@VPSC-R5B-20260924-01 XONG` hoặc `KQ@VPSC-R5B-20260924-01 DỪNG`. **XONG** = B5 `BOUNDED` đã nạp + C' cài + kế hoạch xoá có sha256 + đối chiếu đạt + unresolved làm mất trần = 0 + F xoá xong theo kế hoạch đã duyệt (`L_XOA=1`) + D đạt. `PENDING_RESTART`, `LUI`, `PENDING_UNRESOLVED`, `CHO_DUYET` → DỪNG. Theo dõi dài hạn (GC qua nhiều lần build, luật tuần Chủ nhật) không phải điều kiện XONG (P26).
- Trả Owner đúng một dòng: `XONG · VPSC-R5b · build cache trần 5GiB đã nạp · KEEP_SET v2 <trước>→<sau> ImageID, đã xoá <n> (~<GiB>) · trống <GiB> · xem BAO-CAO.md` hoặc `DỪNG · VPSC-R5b · <phần.bước> · <lý do>`.

## Sau R5b (không phải việc của agent)
Host nghiệm thu → GPT đóng P18/P25/P26 → Đóng việc. Theo dõi dài hạn (luật tuần, GC) qua Kuma + log, không chặn đóng.
