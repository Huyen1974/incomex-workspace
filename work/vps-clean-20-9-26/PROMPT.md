# PROMPT — VPSC · R2 Dọn đợt 1 + khoá 4 vòi rò (CÓ MUTATION — chỉ đúng danh sách trong file này)

RUN_ID: VPSC-R2-20260921-01
Soạn: Claude Chat (Host), 21/09/2026, từ V1b + P13 (GPT) + V1-01…V1-06 (Codex). Trạng thái chỉ tin `work/vps-clean-20-9-26/COLLAB.md`. Chỉ chạy khi COLLAB có đủ `GPT REVIEWED@` + `OWNER_APPROVED@` + Host `READY@` đúng full SHA commit cuối chạm file này, và lệnh RUN.
**Executor_Surface = Claude Code CLI chạy trên VPS (shell root)** — đúng bề mặt đã chạy R1.
**Write_Path = `workspace_*`** (đã ghi được ở R1); dự phòng `fs_*`. Cấm git/GitHub native để ghi repo workspace; không clone.
**Nguyên tắc:** chỉ làm đúng các mục có tên dưới đây. Thứ gì không có tên trong file này thì KHÔNG đụng, kể cả khi trông giống rác. Không tự quyết thêm.

## 0. Cổng
1. `df -B1 /`; Available <3GiB → DỪNG.
2. Read-gate: đọc COLLAB qua Write_Path; giấy phép khớp full SHA commit cuối chạm PROMPT.md (không so HEAD); lệch → DỪNG.
3. Đọc `BAO-CAO.md` mục V1b (manifest gốc, bảng N3 theo tên) và mục V1 (V1-01…V1-06).
4. Chụp trạng thái trước: df; `docker ps` (12 container + health); `points_count` + status của collection `production_documents`; số snapshot server-side; web trả 200; Directus `/server/health`.
5. Không có tiến trình đang chạy: `qdrant-backup.sh`, `backup-to-gdrive.sh`, `code-backup-to-gdrive.sh`, `dung-va-trien-khai.sh`, `dot-context-pack-build.sh`, npm/pip/uv install. Có → chờ tối đa 15 phút; vẫn chạy → DỪNG.

## 1. Luật cứng
- Không restart/recreate container; không docker rm/rmi/prune/build/save; không DROP/VACUUM. Không đụng N6–N15 (image, build cache, postgres /tmp, tồn dư mission, nhãn giữ, DB thử, Hermes kể cả `/var/backups/hermes`).
- Xoá theo danh sách tên cụ thể. Trước mỗi nhóm: in số lượng dự kiến và số thực; lệch → DỪNG nhóm đó (không tự sửa danh sách).
- Sửa script: chỉ các file nêu ở §3 B4 và §4. Trước khi sửa commit trạng thái cũ vào git cục bộ `/opt/incomex` (nếu file chưa được theo dõi thì thêm vào); sửa; `bash -n`; commit `VPSC-R2 · <file> · <lý do>`. Không tạo bản `.bak` trên đĩa.
- Không ghi bằng chứng thô ra VPS ngoài log hành động của §4 (≤1MB).
- Sau mỗi đợt: đo lại §0.4. Health xấu đi → DỪNG, không làm đợt kế.

## 2. Đợt A — tạo khoảng thở (dự kiến ~6,8GiB)
- **A1 · N2 log Directus (~1,32GiB):** cắt về 0 tại chỗ `/home/node/.pm2/logs/directus-out-0.log` trong container `incomex-directus` (truncate), KHÔNG rm. Kiểm file vẫn được pm2 ghi tiếp sau đó.
- **A2 · N4 context-pack.tmp (~1,44GiB):** xoá các thư mục `/opt/incomex/context-pack.tmp/<BUILD_ID>` có BUILD_ID ≤ `20260918-070009-403a50` (so theo tên). Dự kiến **979**. Giữ thư mục gốc `.tmp`, mọi build mới hơn, `context-pack/`, `context-pack-staging/`. Trước khi xoá kiểm không tiến trình nào mở file trong tập này.
- **A3 · N5 cache (~1,42GiB):** xoá đúng 6 thư mục: `/root/.npm/_cacache`, `/var/lib/hermes/.npm/_cacache`, `/root/.cache/pip`, `/root/.cache/node-gyp`, `/root/.cache/electron`, `/var/lib/hermes/.cache/electron`. Giữ `_npx`, `ms-playwright`, uv, pnpm và mọi thứ khác.
- **A4 · N3 bản sao Nuxt (~2,6GiB):** xoá đúng các tên trong bảng "N3 — kết quả theo từng tên" của V1b, TRỪ tập GIỮ: `nuxt-output` (đang chạy, không có trong bảng), `nuxt-output.truoc-20260921-093648`, `nuxt-output.truoc-20260921-093200`, `nuxt-output.truoc-20260921-053858` (3 bản gần nhất), `nuxt-output.bak.20260531-rp-final` (script rollback đọc), `nuxt-output.prev` và `nuxt-output.bak.pre-phab1c-20260627T165940Z` (mã QA nhắc), `nuxt-output-balo-20260716T234206Z`, `nuxt-output-balo-fresh-20260717T033701Z`, `nuxt-output-balo-current-path` (nhóm balo giữ nguyên). Dự kiến xoá **63** thư mục. Bản sao tạo sau V1b (không có trong bảng) → không đụng.
- Cuối đợt A: đo lại §0.4; thu hồi thực lệch >15% so với tổng dự kiến → DỪNG, không làm đợt B.

## 3. Đợt B — gỡ cổng Qdrant (dự kiến ~27,3GiB)
- **B1 · Chọn bản cứu:** file snapshot `production_documents` mới nhất trong `/opt/incomex/backups/qdrant/`. Tính sha256; đối chiếu với file `.checksum` Qdrant tạo cho đúng snapshot đó trong container. Khớp → đi tiếp; không khớp/không có → thử bản host kế trước; không bản nào khớp → DỪNG đợt B.
- **B2 · Đưa ra ngoài VPS:** mã hoá bằng đúng khoá công khai + cấu hình rclone mà `backup-to-gdrive.sh` đang dùng, truyền thẳng (pipe) lên thư mục con `rescue/vpsc-r2/` của đích backup mã hoá — không tạo file lớn trên VPS. Tính md5 của luồng đã mã hoá trong lúc gửi và đối chiếu với md5 phía Drive (`rclone md5sum`). Tải kèm file meta nhỏ: collection, tên snapshot, thời điểm, byte, sha256 bản rõ, md5 bản mã hoá. Không khớp → DỪNG đợt B.
- **B3 · Xoá snapshot server-side:** bằng API Qdrant `DELETE /collections/production_documents/snapshots/<tên>`, lần lượt từng cái, xoá TẤT CẢ trừ **1 snapshot mới nhất**. In danh sách + số lượng trước khi xoá (dự kiến ~160 tổng, xoá ~159). Mỗi lệnh phải trả thành công; lỗi → DỪNG. Không restart Qdrant. Sau khi xong: `points_count` của `production_documents` KHÔNG đổi, status green. (Cơ sở: các bản bị xoá hoặc đã có bản trên host 7 ngày, hoặc là trạng thái cũ; bản mới nhất đã có ngoài VPS ở B2.)
- **B4 · Khoá vòi Qdrant:** sửa `scripts/qdrant-backup.sh`: sau `docker cp` thành công, kiểm file >0 byte và sha256 khớp `.checksum` của Qdrant → mới gọi DELETE đúng snapshot vừa tạo; bước nào lỗi → giữ snapshot server-side, ghi lỗi, thoát mã ≠0. KHÔNG thêm lệnh xoá hàng loạt theo tuổi (V1-01).
- Cuối đợt B: đo lại §0.4 + số snapshot server-side.

## 4. Khoá 3 vòi còn lại (làm sau đợt A, trước báo cáo)
- **K1 · MỘT người gác kho:** tạo `/opt/incomex/scripts/vps-retention.sh` + `/etc/cron.d/vps-retention` chạy mỗi giờ, chứa đúng 3 quy tắc:
  (a) log pm2 Directus >200MiB → cắt về 0 tại chỗ;
  (b) `context-pack.tmp`: xoá build cũ hơn 3 ngày, luôn giữ 22 build mới nhất theo tên, bỏ qua thư mục có tiến trình đang mở file;
  (c) 6 thư mục cache ở A3: chỉ chạy lúc 04:xx và khi không có npm/pip/uv đang chạy; thư mục nào >300MiB thì xoá thư mục đó.
  Mỗi lần có hành động ghi 1 dòng vào `/var/log/incomex/vps-retention.log`; thêm file log này vào logrotate hiện có (giữ 4 tuần). Chạy thử 1 lần ngay sau khi tạo: kết quả phải là "không có gì để làm".
- **K2 · Bản sao Nuxt:** sửa `scripts/phai-cu/dung-va-trien-khai.sh`: sau deploy thành công, giữ 3 bản `nuxt-output.truoc-*` mới nhất theo tên, xoá các bản `nuxt-output.truoc-*` cũ hơn; không đụng tên khác. Không chạy deploy để thử; chỉ `bash -n`.
- Trần sau khoá: log pm2 ≤~0,2GiB · context-pack.tmp ≤~0,05GiB · cache ≤~1,8GiB · snapshot Qdrant server-side ~0 sau mỗi lượt · bản sao Nuxt ≤~0,5GiB.

## 5. Báo cáo
- Chèn mục "R2 — Dọn đợt 1 · <ngày> · executor=Claude Code CLI · write_path=<…>" lên ĐẦU `BAO-CAO.md`.
- (1) CHO OWNER ≤8 dòng: df trước/sau; thu hồi từng nhóm; 4 vòi đã khoá; còn thiếu bao nhiêu để đạt 45GiB. (2) Bảng: nhóm · dự kiến · thực · số mục xoá · health. (3) Script đã sửa/tạo: tên file + commit git cục bộ + nội dung cron. (4) Bản cứu Qdrant: tên, byte, sha256, md5 khớp (không ghi ID Drive). (5) Việc để lượt sau: N9/N11 cứu rồi xoá; N6–N8 sau R03; Hermes G22/G23 (chủ Hermes); `backup-to-gdrive.sh` còn nhánh xoá snapshot khi tải lỗi (V1-01).
- Repo công khai: không secret/token, IP/tên miền nội bộ, ID Google Drive, tên tài khoản, output lệnh thô.
- Sửa dòng `VPSC.5` trong COLLAB thành `MACHINE_DONE · R2 · xem BAO-CAO.md` hoặc `STOPPED · <đợt/bước> · <lý do>`.
- Trả đúng một dòng: `XONG · VPSC-R2 · trống <trước>→<sau>GiB · thu hồi <GiB> · khoá 4/4 vòi · xem BAO-CAO.md` hoặc `DỪNG · VPSC-R2 · <đợt/bước> · <lý do>`.

## 6. Sau R2 (không phải việc của agent)
Codex hậu kiểm độc lập (df, health, số mục đã xoá đúng danh sách, script khoá vòi). Đợt 2 (N9/N11 cứu rồi xoá) là PROMPT sau.
