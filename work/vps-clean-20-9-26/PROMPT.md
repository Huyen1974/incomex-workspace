# PROMPT — VPSC R6 · VPS HEALTH + DISK-LEAK CLOSEOUT 05/10/2026

STATUS: **DRAFT — P31 DELTA đã được Host áp tại P32; Claude Reviewer đã xác nhận diff + sửa 2 chỗ tại P33; chờ GPT Host READY trên đúng bản này**
RUN_ID: VPSC-R6-HEALTH-LEAK-CLOSEOUT-20261005-01
Executor_Surface: Claude Code CLI trên Mac → SSH root VPS theo đường hiện hữu
Write_Path: repo SSOT qua `workspace_*` profile Claude Code; runtime/config qua DOT/script-wrapper + Config Guard
Evidence_Dir: `/opt/incomex/work/vps-clean-20-9-26/R6-20261005/`
DOT 100% cho runtime/data/config; không direct SQL/psql/Directus REST.

## 0 · Đích
VPS khỏe và ổ đĩa không tăng bất thường vì dữ liệu vận hành/tạm không bounded. Sửa gốc trước, đặt trần tự động, dọn phần chứng minh an toàn, đo lại. **Không xoá active/rollback/bằng chứng cần thiết chỉ để đạt số.**

Owner D15 (05/10 15:31): dữ liệu/artifact thực sự không còn dùng thì được xoá. Owner bổ sung 15:34: nếu không còn cần ở VPS nhưng chưa đủ tự tin xoá thẳng, **archive một bản lên Google Drive bằng đường backup/rclone hiện hữu, verify checksum/size/readback rồi mới xoá local**. Không mở lại `vps1-up-grade`.

## 1 · PRE + luật cứng
1. Đọc `AGENTS.md` → root `COLLAB.md` → Bảng + D15 + P29–P33 → audit 05/10 trong `BAO-CAO.md` → PROMPT này.
2. Fresh-check CWEB/HJW/PGNB. Nếu có RUN mutation chung nginx/agent-data/PG/Directus thì phần va chạm **DỪNG**, các phần độc lập A/B/C/E được tiếp tục theo bảng phụ thuộc §7.
3. Baseline: `df -B1 /` + `df -i`; một lượt `ionice -c3 nice -n19 du -x` top-down; reconcile df↔du; `lsof +L1`; container/StartedAt/health; HTTP `/`, `/w/`, Agent Data/UI, knowledge sample; failed units; Kuma/Guard; I/O/load/swap bounded sample.
4. Một lượt full-disk `du/find` duy nhất trong PRE; các lượt sau chỉ đo taxonomy đã lập.
5. **CẤM Docker:** `docker buildx`, `docker builder`, `docker system df|prune`, `docker image prune`, `docker volume prune`, mọi `-f/--force`. Chỉ-read bằng `docker ps`, `docker image ls`, `docker volume ls`, `docker inspect`, `docker info`, log/compose config read-only. Không restart dockerd/containerd; không recreate container trong R6, trừ đúng một ngoại lệ nêu ở §3 (rebuild agent-data khi bắt buộc, qua DOT deploy hiện hữu).
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
- Inventory bắt buộc: `directus_gov_test_20260602`; `/opt/incomex/work/**`; `/opt/incomex/logs`; Docker image/container logs/writable layers/volumes; PG WAL/temp; Qdrant; `/tmp`/`/var/tmp`/`/var/cache`; journal/coredump; workspace results/uploads/jobs/transactions; `/var/lib/hermes`; home/cache công cụ AI; kernel cũ; inode hotspots; 2 PG18 quarantine + PG16 cũ.
- Business/live data = `BUSINESS_GROWTH`: không cap/xoá mù nhưng có owner + expected growth.
- Mỗi non-business group phải có: `current_bytes · growth_driver · hard_cap_bytes · TTL/age · protected_set · cleanup_trigger · owner`. Thiếu trường ⇒ STORAGE_BOUND chưa PASS.

### C1 · Log
Mở rộng logrotate hiện hữu cho `/var/log/incomex` và `/opt/incomex/logs` append logs. Chọn reopen/copytruncate theo writer thật; numeric size cap + age + compress. Verify writer vẫn ghi sau rotate.

### C2 · CWEB/deploy
Reference graph từ compose/systemd/nginx/symlink/manifest/deploy/rollback. Bảo vệ current CWEB + exact rollback còn hiệu lực. Build/prepared/repair/retained cũ chỉ candidate khi 0 reference + reproducible.
Không thêm regex từng tên mới làm giải pháp gốc; dùng storage registry §C6.

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
- raw dir/old cluster: stream archive one-by-one qua rclone/đường backup hiện hữu, tránh tạo duplicate lớn trên VPS; manifest + SHA256/size + Drive listing/readback;
- chỉ khi offsite verify PASS + Host approve đúng SHA plan mới xoá local.
- Mọi bản đưa lên Drive đi đúng khuôn đã chạy ở R3 mục 3.2 (xem `BAO-CAO.md`): `tar` hoặc dump → `gzip` → `gpg` bằng khoá công khai của `backup-to-gdrive.sh` (kiểm vân tay trước) → `rclone rcat` vào `rescue/vpsc-r6/` của đích mã hoá. **Không plaintext lên Drive; không tìm/giải mã bằng khoá bí mật trên VPS** (VPS chỉ có khoá công khai) — “readback” = md5 + size của luồng mã hoá khớp đối tượng trên Drive.
- Trước khi tải: `rclone about` chứng minh Drive còn trống ≥ dung lượng bản tải + 10 GiB cho backup đêm; thiếu ⇒ không tải, ghi blocker. Đặt hạn giữ 12 tháng cho `rescue/vpsc-r6/` bằng cơ chế hạn giữ Drive hiện hữu.
- Nếu Drive đã có bản dump mã hoá của đúng dữ liệu đó (backup đêm cuối trước cutover hoặc `rescue/vpsup-bk1/`, md5/size đọc được) ⇒ coi là đã có bản offsite, không tải thêm raw dir.
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
Đèn #11 đỏ khi bất kỳ:
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
