# PROMPT — VPSC · R3 Bịt nốt vòi + đợt 2 lấy chỗ (CÓ MUTATION — chỉ đúng danh sách trong file này)

RUN_ID: VPSC-R3-20260921-01
Soạn: Claude Chat (Host), 21/09/2026, từ P14 + P15 (GPT) + V2 (Codex: V2-01, V2-02, D, F) + Host (hai khoá cho mỗi vòi, hạn giữ Drive chính, vòi nhỏ). Trạng thái chỉ tin `work/vps-clean-20-9-26/COLLAB.md`. Chỉ chạy khi COLLAB có đủ `GPT REVIEWED@` + `OWNER_APPROVED@` + Host `READY@` đúng full SHA commit cuối chạm file này, và lệnh RUN.
**Executor_Surface = Claude Code CLI trên máy Mac, điều khiển shell root VPS qua SSH** (đúng bề mặt R2). **Write_Path = `workspace_*`**; dự phòng `fs_*`. Cấm git/GitHub native để ghi repo workspace; không clone.
**Nguyên tắc:** chỉ làm đúng mục có tên. Không tự quyết thêm. Ghi báo cáo TRƯỚC khi sang phần có rủi ro (§3). Mỗi vòi có HAI khoá: khoá ở nơi sinh (script) + người gác ở nơi chứa (`vps-retention.sh`).

## 0. Cổng
1. `df -B1 /`; Available <3GiB → DỪNG.
2. Read-gate COLLAB qua Write_Path; giấy phép khớp full SHA commit cuối chạm PROMPT.md (không so HEAD); lệch → DỪNG.
3. **NO_CONCURRENT_VPS_MUTATION:** không có tiến trình `docker build/compose/pull`; container `incomex-agent-data` đã tạo ≥10 phút và healthy; COLLAB gốc và COLLAB các việc khác không có RUN đang chạy đụng VPS. Không đạt → chờ tối đa 15 phút rồi DỪNG. Trước mỗi phần (Phase) kiểm lại agent-data không bị tạo lại; bị tạo lại → không làm phần kế, ghi lý do. KHÔNG tự rollback/xoá image của việc khác.
4. Đọc `BAO-CAO.md` mục V2 (V2-01, V2-02, D, F), R2, V1b (bảng N9/N11 theo tên).
5. Chụp trạng thái trước: df; 12 container + health; `production_documents` status + `points_count` + số snapshot server-side; web 200; Directus health.
6. Không có tiến trình backup/deploy/builder đang chạy (đếm theo tên).

## 1. Luật cứng
- Không restart/recreate container; không docker rm/rmi/prune/build/save/pull; không DROP/VACUUM. Không đụng N6–N8 (image/build cache — chờ R03 CLOSED), N12–N15, DB thử, `/var/backups/hermes/snapshot-truoc-update` (G21), `/root/agent-runs`, `backups/mysql/backup.log`.
- **Luật bí mật:** không in bất kỳ token/khoá nào ra màn hình hay vào file ngoài đúng file cấu hình đích; bí mật chỉ đi qua pipe hoặc biến trong shell con. Không cat/grep/head/less/sed-in `rclone.conf`, `.env`, `secrets/` (ngoại lệ duy nhất: `grep -c` chỉ in số đếm); không `rclone config show`, `env`, `set -x`; không liệt kê tham số tiến trình.
- Sửa script: commit git cục bộ `/opt/incomex` trước/sau, `bash -n`, kiểm nhánh lỗi bằng mô phỏng (thay lệnh bằng stub trả lỗi). KHÔNG chạy backup/deploy thật, không tạo/xoá snapshot thật để thử.
- Xoá theo danh sách tên; in số dự kiến và số thực trước mỗi nhóm; lệch → DỪNG nhóm đó.
- Sau mỗi Phase: đo lại §0.5; health xấu đi → DỪNG.

## Phase 0 — SEC-01: xoay token Drive (Owner ngồi máy ~5 phút)
0.1 Xác định remote rclone Drive mà `backup-to-gdrive.sh`, `code-backup-to-gdrive.sh`, backup Lark dùng: chỉ in TÊN remote và TÊN file cấu hình. Kiểm remote có client riêng không bằng `grep -c` dòng `client_id` có giá trị (chỉ in số): >0 → DỪNG Phase 0 (cần hướng dẫn riêng).
0.2 Nạp token cũ vào biến shell con (không in). Trên Mac chạy `rclone authorize "drive"` (thiếu rclone thì cài qua Homebrew) và nhắn Owner đúng một câu: **"Trình duyệt vừa mở: anh đăng nhập đúng tài khoản Google chứa thư mục backup rồi bấm Cho phép (Allow)."** Token mới đi thẳng qua pipe/SSH vào `rclone config update <remote> token …` trên VPS, không in.
0.3 Kiểm token mới: liệt kê đích backup mã hoá (chỉ in số đối tượng).
0.4 Thu hồi token cũ bằng endpoint thu hồi OAuth của Google (giá trị từ biến ở 0.2). Kiểm lại 0.3. Nếu token mới cũng mất hiệu lực → làm lại 0.2 đúng MỘT lần (Owner bấm Cho phép lần nữa) → kiểm lại. KHÔNG thu hồi bằng cách gỡ toàn bộ quyền ứng dụng trong tài khoản Google (có thể cắt cả máy khác dùng rclone).
0.5 File cấu hình rclone khác trên VPS còn giữ đúng token cũ (so bằng băm, không in) → cập nhật token mới.
0.6 Chỉ sau khi 0.4 xác nhận token cũ đã bị thu hồi: trên Mac tìm file dữ liệu/transcript/scratchpad của Claude Code có chứa token cũ (`grep -rlF` với giá trị từ biến, chỉ in tên file) → xoá các file đó; báo số file đã xoá (không ghi đường dẫn có tên tài khoản vào repo).
0.7 Phase 0 lỗi hoặc bị chặn → KHÔNG làm Phase 2 và 3 (dùng Drive); vẫn làm Phase 1; ghi `STOPPED · Phase 0`.

## Phase 1 — Bịt vòi trên VPS (không cần Drive)
1.1 **V2-01 · `scripts/qdrant-backup.sh` fail-closed:** mọi lỗi từ POST tạo snapshot tới DELETE đều ghi `FAILED` vào `backup.log`, thoát ≠0 và không DELETE (bọc từng bước hoặc trap). Khoá Qdrant không nằm trên dòng lệnh (truyền qua stdin/biến môi trường). Mô phỏng đủ nhánh lỗi POST / copy / checksum / DELETE.
1.2 **V2-02 · `scripts/phai-cu/dung-va-trien-khai.sh`:** lọc regex `nuxt-output.truoc-YYYYMMDD-HHMMSS` TRƯỚC → sort → giữ 3. Thêm: mỗi lần deploy ghi sha256 của chính script vào log deploy (để biết đường deploy thật).
1.3 **Mở rộng người gác `scripts/vps-retention.sh`** (giữ a/b/c, thêm đúng các luật sau; mỗi luật bỏ lượt nếu tiến trình liên quan đang chạy):
  (d) bản sao Nuxt ở nơi chứa: trong `deploys/`, chỉ tên khớp `nuxt-output.truoc-YYYYMMDD-HHMMSS`: giữ 3 mới nhất theo tên, xoá phần còn lại; không đụng tên khác.
  (e) Hermes: `/var/lib/hermes/.hermes/backups` giữ 5 file mới nhất (G22); `tmp_pack_*` trong `.git/objects/pack` của hai bản cài Hermes, cũ hơn 1 ngày và không có tiến trình git → xoá (G23).
  (f) Lark: thư mục JSONL giải nén của một lượt → xoá khi lượt đó đã có tar.gz + dấu `.offsite-ok` (đọc đúng cấu trúc từ `s177-lark-backup-prune-local`; không sửa script Lark).
  (g) `/var/log/incomex/hc-executor*-*.log` cũ hơn 30 ngày → xoá.
  (h) `/var/lib/incomex-audit/*` cũ hơn 30 ngày → xoá.
  (i) `/tmp/*.sql` trong container postgres cũ hơn 7 ngày → xoá — **viết sẵn nhưng TẮT**, chỉ bật ở 3.4 sau khi N9 đã cứu.
  Chạy thử 1 lần (chưa có (i)): ghi tên từng mục bị xoá — lượt đầu có thể xoá pack tạm Hermes và JSONL Lark cũ: đó là luật chạy đúng.
1.4 **Cảnh báo đĩa (T4) — chỉ đọc:** `disk-monitor.sh` và uptime-kuma hiện có gửi được báo đến Owner không (không cấu hình mới, không đọc mật khẩu); ghi kết quả.
1.5 **Ghi ngay** mục R3 phần 1 lên đầu `BAO-CAO.md` + dòng `VPSC.5b` = `IN_PROGRESS · Phase 0/1 xong`.

## Phase 2 — Drive: fail-closed + hạn giữ (chỉ khi Phase 0 PASS)
2.1 **`scripts/backup-to-gdrive.sh` fail-closed:** nhánh snapshot Qdrant — list/create/tải lỗi thì KHÔNG DELETE snapshot nguồn và trạng thái lượt không được là PASS; chỉ DELETE sau khi tải xong và kích thước >0. Khoá Qdrant khỏi dòng lệnh. Mô phỏng nhánh lỗi; không chạy backup thật.
2.2 **Hạn giữ ở đích Drive** (thêm vào `backup-to-gdrive.sh`, chạy SAU khi lượt upload mới đã kiểm xong; lỗi tỉa chỉ cảnh báo): thư mục backup mã hoá chính giữ **30 bộ ngày gần nhất + bộ cuối mỗi tháng trong 12 tháng** (một bộ = artifact + meta cùng lượt; không bao giờ xoá bộ mới nhất); `rescue/vpsc-r2/` xoá sau 2026-10-21; `rescue/vpsc-r3/` giữ 12 tháng. Tính trước trần dự kiến ở đích (GB) và so với dung lượng Drive còn trống.
2.3 **Tỉa Drive lần đầu:** chạy thử không xoá (in tên + số bộ sẽ xoá; dự kiến ~30 bộ từ 20/07 tới ~20/08, giữ bộ cuối 31/07); lệch nhiều → DỪNG. Khớp → chạy thật, kiểm số bộ còn lại.

## Phase 3 — Đợt 2: cứu N9/N11 ra ngoài rồi xoá (chỉ khi Phase 0 PASS)
3.1 Danh sách đúng tên từ V1b: **N9** = các target trong bảng "N9 — kết quả theo từng tên" (trong `/tmp` của container postgres); **N11** = 38 target của V1b TRỪ `/root/agent-runs`, `backups/mysql/backup.log` và mọi mục N12. In số lượng + tổng byte trước; lệch với V1b/V2 → DỪNG nhóm.
3.2 Cứu từng nhóm: luồng `tar` → nén → mã hoá bằng đúng khoá công khai của backup → `rclone rcat` vào `rescue/vpsc-r3/<nhóm>.tar.gz.gpg`; md5 luồng = md5 phía Drive; kèm manifest nhỏ (tên + byte từng mục). Dùng `--tpslimit` để tránh giới hạn tốc độ. Không tạo file lớn trên VPS.
3.3 Chỉ xoá nhóm sau khi md5 khớp; xoá đúng danh sách; kiểm lại.
3.4 N9 xong → bật luật (i) trong người gác; commit.
3.5 df: mục tiêu trống >45GiB.

## 4. Báo cáo
- Cập nhật mục "R3 — Bịt nốt vòi + đợt 2 · <ngày> · executor=Claude Code CLI · write_path=<…>" ở đầu `BAO-CAO.md`: (1) CHO OWNER ≤8 dòng: SEC-01 xong chưa; df trước/sau; vòi nào đã có hai khoá; Drive đã có hạn giữ chưa. (2) Bảng vòi: tên · khoá nơi sinh · khoá nơi chứa · trần · trạng thái. (3) Script/commit/cron. (4) Bản cứu N9/N11: tên, byte, md5 (không ID Drive). (5) Việc còn lại: N6–N8 sau R03 (chủ R03); TTL `workspace-tools` (chủ agent-data); kết quả T4.
- Repo công khai: không secret/token, IP/tên miền nội bộ, ID Google Drive, tên tài khoản, output lệnh thô.
- Sửa dòng `VPSC.5b` thành `MACHINE_DONE · R3 · xem BAO-CAO.md` hoặc `STOPPED · <Phase/bước> · <lý do>`.
- Trả đúng một dòng: `XONG · VPSC-R3 · SEC-01 <xong|chưa> · trống <trước>→<sau>GiB · vòi hai khoá <n>/<tổng> · Drive hạn giữ <có|chưa> · xem BAO-CAO.md` hoặc `DỪNG · VPSC-R3 · <Phase/bước> · <lý do>`.

## 5. Sau R3 (không phải việc của agent)
Codex V3 chỉ đọc, sau ít nhất một lượt cron Qdrant thật + một vòng người gác: kiểm trigger thật, hai khoá, hạn giữ Drive, df. PASS → VPSC.6 theo dõi 2 tuần.
