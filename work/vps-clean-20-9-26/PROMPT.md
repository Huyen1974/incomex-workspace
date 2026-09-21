# PROMPT — VPSC · V2 Codex hậu kiểm R2 (AUDIT / NO PRODUCTION MUTATION)

RUN_ID: VPSC-V2-20260921-01
Soạn: Claude Chat (Host), 21/09/2026, theo D06 + P14(1). Trạng thái chỉ tin `work/vps-clean-20-9-26/COLLAB.md`. Chỉ chạy khi COLLAB có `OWNER_APPROVED@` + Host `READY@` đúng full SHA commit cuối chạm file này + lệnh RUN.
**Executor_Surface = Codex Desktop điều khiển shell VPS qua SSH** (đã chạy V1/V1b). **Write_Path = `workspace_*`**; dự phòng `fs_*`. Cấm git/GitHub native để ghi repo; không clone.
**Mục đích:** xác nhận R2 làm đúng danh sách và 4 khoá vòi đúng thiết kế, TRƯỚC khi giao lượt sau. Tự đo, không tin số R2.

## 0. Cổng
1. `df -B1 /`; Available <3GiB → DỪNG.
2. Đúng một read-gate: đọc COLLAB qua Write_Path; fail → DỪNG. Giấy phép khớp full SHA commit cuối chạm file này (không so HEAD); lệch → DỪNG.
3. Đọc `BAO-CAO.md` mục R2 (đối tượng hậu kiểm) và mục V1b (manifest gốc).

## 1. Luật cứng
- CHỈ ĐỌC. Cấm: rm/mv/truncate/ghi đè; docker rm/rmi/prune/save/tag/build/restart; API xoá Qdrant; DROP; sửa cron/config/script; chạy deploy; chạy `vps-retention.sh` hay `qdrant-backup.sh`.
- **Luật bí mật:** không cat/grep/head/less/sed-in file `rclone.conf`, `.env`, `secrets/`; không `rclone config show`, `env`, `set -x`; không liệt kê tham số tiến trình (`ps -ef`, `ps -o args`, `/proc/*/cmdline`) — chỉ đếm theo tên. Cần remote/đích Drive thì nạp biến trong shell con từ đúng nguồn `backup-to-gdrive.sh` dùng, không in giá trị.
- Không ghi file lên VPS. Không chờ/sleep. Mục tiêu ≤40 phút.
- Chỉ ghi repo: mục V2 đầu `BAO-CAO.md` + dòng `VPSC.5v` trong COLLAB.

## 2. Kiểm
A. **Tổng:** df; 12 container + health; collection `production_documents` status + `points_count`; web 200; Directus `/server/health`.
B. **Đúng danh sách R2:**
  - A1: log pm2 Directus nhỏ, pm2 vẫn ghi tiếp.
  - A2: không còn build nào ≤ `20260918-070009-403a50`; không build nào mới hơn bị xoá sai quy tắc.
  - A3: 6 thư mục cache vắng hoặc <300MiB.
  - A4: trong `deploys/` còn đúng 10 tên tập GIỮ + `nuxt-output` + các `truoc-*` sinh SAU R2 (nếu có, ghi tên); không mất tên nào ngoài 63 tên đã duyệt.
  - B3: số snapshot server-side của `production_documents` = 1 (nếu lượt cron đã chạy thì ghi rõ).
  - B2: đối tượng `<snapshot>.gpg` + meta có trong `rescue/vpsc-r2/` trên Drive, md5 = `b8180c2e93be512b7a14f624f45443be` (dùng `rclone md5sum` đúng thư mục, không in cấu hình).
C. **Mã khoá vòi** (git cục bộ `/opt/incomex`): đọc `git show b97e5d3`, `3180326`, `0dc9379`; `/etc/cron.d/vps-retention`; dòng logrotate. Chấm so với PROMPT R2 (`f701fc5`): B4 chỉ DELETE sau sha256 khớp, lỗi thì giữ, không xoá hàng loạt theo tuổi; K1 đúng 3 quy tắc + flock + log; K2 chỉ tỉa `nuxt-output.truoc-YYYYMMDD-HHMMSS`, chỉ sau deploy thành công. `bash -n` cả 3.
D. **K2 có thật sự khoá được không:** R2 §5 ghi bản `scripts/phai-cu/` trên máy Mac cũ hơn VPS. Xác định bản `dung-va-trien-khai.sh` nào thực sự tạo `nuxt-output.truoc-*` trên VPS (bản trên VPS hay lệnh đẩy từ máy Mac), dựa vào dấu vết thật: log/journal/auth log, thời điểm tạo 3 bản `truoc-*` gần nhất, nơi gọi `cp -a`. Kết luận: K2 hiệu lực / không hiệu lực / chưa xác định.
E. **Không mutation ngoài phạm vi:** các mục HOLD còn nguyên — N9 (`/tmp` postgres: đếm dump), N11 (các target bảng V1b), N12, N13 (DB còn + nhãn còn), N14 (`/usr/local/lib/hermes-agent`), `/var/backups/hermes`, image N7/N8 (đủ ID), `deploys/nuxt-output` đang chạy.
F. **Ảnh hưởng HVU-B3 chạy chen 10:20–10:25Z:** container agent-data đang chạy image nào; image `agent-data-hvu:b3-20260921` còn không, chiếm bao nhiêu.

## 3. Báo cáo
- Chèn mục "V2 — Codex hậu kiểm R2 · <ngày> · executor=Codex Desktop qua SSH · write_path=<…>" lên ĐẦU `BAO-CAO.md`; không sửa mục cũ.
- (1) CHO OWNER ≤8 dòng: R2 đúng/sai; 4 khoá vòi đạt/không; df hiện tại. (2) Bảng A–F: mục · kết quả · PASS/REVISE/BLOCK · lý do. (3) Việc Host cần xử lý ở lượt sau.
- Repo công khai: không secret/token, IP/tên miền nội bộ, ID Google Drive, tên tài khoản, output lệnh thô.
- Sửa dòng `VPSC.5v` trong COLLAB thành `MACHINE_DONE · V2 · PASS <n> / REVISE <n> / BLOCK <n>` (có expected_version).
- Trả đúng một dòng: `XONG · VPSC-V2 · PASS <n> / REVISE <n> / BLOCK <n> · K2 <hiệu lực|không|chưa rõ> · trống <GiB> · xem BAO-CAO.md` hoặc `DỪNG · VPSC-V2 · <mục> · <lý do>`.
