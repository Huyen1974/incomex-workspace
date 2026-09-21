# BÁO CÁO — vps-clean-20-9-26

Tài liệu báo cáo duy nhất của việc này (D04). Lượt mới chèn lên đầu, giữ nguyên mục cũ. Chỉ chứa bản đã làm sạch; bằng chứng thô nằm trên VPS ngoài Git.

---

## R2 — Dọn đợt 1 · 21/09/2026 · executor=Claude Code CLI · write_path=workspace_*

RUN_ID `VPSC-R2-20260921-01` · PROMPT@f701fc5ca09041d47752cc7c5bca46ab290e8043 — đã kiểm: commit cuối chạm `PROMPT.md` đúng mã này; `GPT REVIEWED@` + `OWNER_APPROVED@` + Host `READY@` cùng mã. Chạy 2 phiên: phiên 1 làm đợt A + B1; phiên 2 (phiên mới sạch) làm B4 + K1 + K2, ghi phần này, rồi B1 (kiểm lại) → B2 → B3. **Trạng thái: MACHINE_DONE — đợt A + đợt B (B1–B4) + K1 + K2 xong · KQ@VPSC-R2-20260921-01 XONG.** Phần 1 ghi ~10:27Z (`35e51b2`), cập nhật cuối ~10:40Z. Đơn vị GiB (1024³), giờ UTC.

### 1. CHO OWNER

- Đĩa trống: **9,398 → 43,452GiB** (91% → 55%).
- Thu hồi: đợt A **6,846GiB** + B3 **27,361GiB** = **34,207GiB** (ròng 34,054 — chênh ~0,15GiB là tăng nền giữa hai phiên).
- Khoá vòi **4/4**: Qdrant (B4), bản sao Nuxt (K2), log Directus + context-pack.tmp + cache (K1, cron mỗi giờ; lượt cron thật đầu 10:23Z: không có gì để làm, không lỗi).
- Bản Qdrant mới nhất đã nằm ngoài VPS (mã hoá, md5 khớp); server-side còn đúng 1 bản (0,22GiB).
- Mục tiêu 45GiB trống: còn thiếu **1,548GiB** → đợt 2 (N9/N11 cứu rồi xoá).
- Health không đổi: 12 container (10 có healthcheck đều healthy), Qdrant green, `points_count` không đổi trong B3, web 200, Directus ok.
- Host cần biết 2 việc (§6): HVU-B3 chạy song song 10:20–10:25Z rồi tự dừng/rollback; B2 phải thử lại 1 lần do Drive giới hạn tốc độ.

### 2. Bảng thu hồi

| Nhóm | Dự kiến | Thực | Số mục | Kiểm chỉ-đọc phiên 2 · health |
|---|---:|---:|---|---|
| A1 · N2 log pm2 Directus (cắt về 0 tại chỗ) | ~1,32 | trong tổng A | 1 file | log còn ~0,36MiB, pm2 vẫn ghi tiếp (mtime mới) |
| A2 · N4 context-pack.tmp ≤ `20260918-070009-403a50` | ~1,44 | trong tổng A | 979 | 0 build ≤ mốc; còn 22 build, 43MiB |
| A3 · N5 cache (6 thư mục) | ~1,42 | trong tổng A | 6 | 5/6 vắng; `/root/.cache/pip` đã tái sinh 15MiB (dưới trần 300MiB của K1) |
| A4 · N3 bản sao Nuxt | ~2,6 | trong tổng A | 63 | còn đúng 10 tên = tập GIỮ của PROMPT, 0 tên lạ |
| **Tổng đợt A** | ~6,8 | **6,846** | | trống 9,398→16,244; 12 container; Qdrant 20181 green |
| B1 · chọn bản cứu | — | PASS (phiên 1) · kiểm lại PASS | 1 bản | sha256 bản host = `.checksum` Qdrant |
| B2 · đưa ra ngoài VPS | — | PASS (lần thử 2) | 1 + meta | md5 luồng mã hoá = md5 Drive; byte khớp |
| B3 · xoá snapshot server-side | ~27,3 | **27,360** (df +27,361) | 159/160 | còn 1 bản; `points_count` 20183 trước = sau, green |
| B4 · K1 · K2 (khoá vòi) | 0 | 0 | K1 chạy thử: 0 | health không đổi (đo 10:25Z) |
| **Tổng R2** | ~34,1 | **34,207** | | trống 9,398→43,452; 12 container; web 200; Directus ok (đo 10:38Z) |

Phiên 1 chỉ để lại số tổng của đợt A, không tách từng nhóm; phiên 2 không đo lại bằng cách tạo lại dữ liệu. K1 chạy thử: **"không có gì để làm"**, rc=0 — Host dự kiến 1–2 build quá hạn, nhưng lúc chạy chỉ có đúng 22 build nên luật "luôn giữ 22 build mới nhất" che hết; đó là luật chạy đúng, không phải lệch.

### 3. Script đã sửa/tạo (git cục bộ `/opt/incomex`, không remote)

| File | Commit | Nội dung |
|---|---|---|
| `scripts/qdrant-backup.sh` (B4) | `b97e5d3` | Bản cũ = HEAD trước đó (file đã được theo dõi, sạch). Sau `docker cp`: tên snapshot phải đúng dạng Qdrant sinh; file host >0 byte; sha256 khớp file `.checksum` Qdrant tạo cho ĐÚNG snapshot đó → mới `DELETE …/snapshots/<tên>?wait=true`; bước nào lỗi → ghi FAILED vào `backup.log`, GIỮ snapshot server-side, thoát 1. Không có xoá hàng loạt theo tuổi (V1-01). Sửa kèm lỗi cũ: `if [ $? -eq 0 ]` sau lệnh dưới `set -e` làm nhánh FAILED không bao giờ chạy. Khoá Qdrant cho lệnh DELETE truyền bằng biến môi trường, không nằm trên dòng lệnh. |
| `scripts/phai-cu/dung-va-trien-khai.sh` (K2) | `3180326` | Thêm bước 8, chỉ chạy khi deploy đã qua mọi kiểm: giữ 3 `nuxt-output.truoc-*` mới nhất theo tên (gồm bản vừa sao), xoá `truoc-*` cũ hơn; tên phải khớp `nuxt-output.truoc-YYYYMMDD-HHMMSS`; không đụng tên khác; xoá lỗi chỉ cảnh báo. Không chạy deploy để thử; `bash -n` PASS; nếu chạy lúc này sẽ xoá 0 (đang có đúng 3). |
| `scripts/vps-retention.sh` (K1, mới) | `0dc9379` | Đúng 3 luật: (a) log pm2 trong container Directus >200MiB → cắt về 0 tại chỗ; (b) `context-pack.tmp`: xoá build không còn file nào mới hơn 3 ngày, luôn giữ 22 build mới nhất theo tên, bỏ qua thư mục có tiến trình mở file/cwd, bỏ cả lượt nếu builder đang chạy; (c) 6 thư mục cache của A3: chỉ lượt 04:xx giờ máy và khi không có npm/pip/uv chạy; thư mục >300MiB thì xoá. `flock` chống chạy chồng. Mỗi hành động 1 dòng vào `/var/log/incomex/vps-retention.log`; không có gì thì không ghi. |

`/etc/cron.d/vps-retention` (ngoài git, root 644):

```
# VPSC-R2 K1 2026-09-21 (Claude Code) · nguoi gac kho: /opt/incomex/scripts/vps-retention.sh — dung 3 quy tac a/b/c, xem dau script.
# Gio = gio may (CEST; cron Ubuntu bo qua CRON_TZ). Quy tac (c) chi chay o luot 04:23. Tat nguoi gac kho: xoa file nay.
SHELL=/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
23 * * * * root /opt/incomex/scripts/vps-retention.sh >/dev/null 2>>/var/log/incomex/vps-retention.log
```

`/etc/logrotate.d/incomex` (ngoài git; không có bản nguồn trong `/opt/incomex`): thêm đúng 1 dòng `/var/log/incomex/vps-retention.log` vào khối sẵn có `weekly · rotate 4 · compress` (cùng khối `backup.log` Qdrant/MySQL) = giữ 4 tuần. `logrotate -d` nhận file. Hoàn tác: xoá đúng dòng đó.

### 4. Bản cứu Qdrant

- **Bản rõ:** snapshot `production_documents-7363544529537161-2026-09-21-01-00-04.snapshot` (collection `production_documents`, 2026-09-21 01:00:04Z theo tên), bản host `qdrant_2026-09-21_0300.snapshot`, **236.036.608 byte**, sha256 `b6328a739b46810438963dcb01d0e9b892f75691ec3e428d62392181e6303049` = `.checksum` Qdrant tạo cho đúng snapshot đó (B1 kiểm ở cả hai phiên; `backup.log` xác nhận ánh xạ tên).
- **Bản mã hoá:** OpenPGP bằng đúng khoá công khai người nhận của `backup-to-gdrive.sh` (vân tay khoá khớp trước khi mã hoá; gói đầu của đối tượng trên Drive đúng keyid người nhận), truyền thẳng `gpg | tee | rclone rcat` — không file lớn trên VPS. Đích: thư mục con `rescue/vpsc-r2/` của đích backup mã hoá, cùng remote rclone. Đối tượng `<tên snapshot>.gpg` **175.333.216 byte**; md5 luồng lúc gửi = md5 phía Drive (`rclone md5sum`) = **`b8180c2e93be512b7a14f624f45443be`** — khớp; byte gửi = byte Drive.
- **Meta** `<tên snapshot>.gpg.meta.json` (901 byte): collection, tên snapshot, thời điểm, byte + sha256 bản rõ, byte + md5 bản mã hoá, người nhận, `payload: REDACTED`.
- **Khôi phục** (chưa diễn tập ở R2): tải về máy giữ khoá bí mật → `gpg --decrypt` → kiểm sha256 = giá trị trên → nạp lại qua API recover/upload snapshot của Qdrant.
- **Hạn giữ trên Drive:** `backup-to-gdrive.sh` chỉ đếm tệp cấp đầu của tiền tố; `code-backup-to-gdrive.sh` chỉ xoá tệp khớp mẫu `<repo>_…_ICT.tar.gz` trong thư mục riêng ⇒ không job nào tự xoá bản cứu. Bản cứu CHƯA có hạn giữ — Host chốt (D02).
- Server-side sau B3: còn đúng bản này; từ 22/09 B4 sẽ xoá bản mỗi ngày sau khi kiểm, nên server-side dự kiến chỉ còn bản cũ này (0,22GiB) + 0 bản mới.

### 5. Việc để lượt sau

- Đợt 2: N9/N11 cứu ra ngoài VPS rồi xoá; N6–N8 sau R03 CLOSED; Hermes G22/G23 (chủ Hermes); `backup-to-gdrive.sh` còn nhánh xoá snapshot khi tải lỗi (V1-01).
- Hậu kiểm B4 ở lượt cron thật đầu tiên (03:00 giờ máy 22/09): `backup.log` phải có dòng `sha256 verified … deleted server-side`; số snapshot server-side không tăng.
- Phần POST cũ của `qdrant-backup.sh` vẫn đặt khoá Qdrant trong đối số lệnh (thấy qua bảng tiến trình) — ngoài phạm vi R2, đề xuất sửa cùng lúc vá `backup-to-gdrive.sh`.
- Bản sao `scripts/phai-cu/` trên máy Mac giờ cũ hơn VPS (thêm bước 8 của K2) — đồng bộ khi chạm.
- Chốt hạn giữ bản cứu `rescue/vpsc-r2/` trên Drive (đề xuất: xoá khi B4 đã chạy đúng ≥7 lượt và đợt 2 xong). Bản server-side còn lại (21/09) cũng có thể xoá sau đó.
- Remote rclone của backup đang dùng OAuth client dùng chung nên dễ bị Drive giới hạn tốc độ (xem B2) — đề xuất client riêng, ngoài phạm vi R2.

### 6. Sự cố và bẫy đã gặp

- Phiên 1: bộ an toàn chặn cả phiên vì transcript của phiên đó đã chứa bí mật; không bí mật nào vào repo; đã có SEC-01 ở COLLAB.
- Phiên 2 · HVU-B3 chạy song song, trái điều kiện vận hành của READY: 10:20:37Z container agent-data được tạo lại bằng image `agent-data-hvu:b3-20260921` (build 10:18:49Z), 10:21:34Z tạo lại lần nữa, ~10:23Z quay về `agent-data-r03:20260920-finalclose`, healthy lại 10:24:55Z. R2 không gây ra (R2 chỉ `docker exec` python đọc API Qdrant). Đo lại 10:25Z: health = mốc. Repo ghi HVU.B3 DỪNG + rollback đã kiểm (`c38bced`, `64cd576`). Agent để agent-data ổn định ~13 phút, kiểm healthy + không sự kiện mới rồi mới làm B2/B3; B3 kiểm healthy ngay trước khi xoá. R2 xong ~10:38Z — HVU-B3 có thể tiếp tục theo Host.
- B2 lần 1 (10:30–10:32Z): `rclone rcat` bị Google Drive trả 403 `rateLimitExceeded` (hạn mức truy vấn/phút của OAuth client dùng chung); gpg/tee OK; đã kiểm không có đối tượng dở trên Drive. Thử lại đúng MỘT lần cùng thao tác, chỉ thêm `--drive-chunk-size 64M --tpslimit 4 --low-level-retries 30` (ít request hơn, kiên nhẫn hơn) → PASS sau 19s. Không đổi đích, khoá hay kiểm tra nào.
- B3: `points_count` 20181 (10:25Z) → 20183 lúc bắt đầu B3 = dữ liệu nghiệp vụ ghi thêm bình thường; trong B3 không đổi (20183 trước = sau).
- K1: lượt cron thật đầu tiên 12:23 giờ máy (10:23Z) đã chạy (syslog có CMD); log 0 byte = không có gì để làm, không lỗi.
- Bẫy của chính agent: một lệnh gộp có liệt kê tham số tiến trình bị bộ phân quyền từ chối — đúng, vì dòng lệnh của `qdrant-backup.sh` mang khoá Qdrant; đã đổi sang chỉ đếm theo tên tiến trình.

---

## V1b — Codex hoàn tất thẩm tra · 21/09/2026 · executor=Codex Desktop qua SSH · write_path=workspace_*

RUN_ID `VPSC-V1B-20260921-01` · PROMPT@7ad18cf486bc6e77c07c7235dd6599b099a8ec3a, đã kiểm đúng commit cuối chạm file và OWNER_APPROVED/READY. Đầu vào repo @a15cfff1fdc441b9a630b79335c1ee75e9513905; kiểm R03 lại khi kết thúc, vẫn chưa CLOSED. **MACHINE_DONE — hoàn tất phần thẩm tra bổ sung; chưa triển khai dọn.** Số đo 21/09 khoảng 08:22–08:37Z. Đơn vị GiB; chỗ kế thừa V1/R1 được ghi rõ, không coi là đo mới.

### 1. CHO OWNER

- Đã quét đầy đủ theo D07. Đĩa lúc vào: **91%, trống 9,401GiB**; cần thu hồi ròng **35,599GiB** để đạt 45GiB trống.
- Tổng đo `du` **86,340GiB**, `df` dùng **86,406GiB**; lệch **0,066GiB**, không còn khoản lệch nhiều GB chưa đối soát.
- Nguồn tăng +2,94GiB sáng nay chủ yếu là **cập nhật/cứu hộ Hermes**: backup mới 2,210GiB, thư mục Hermes tăng ròng khoảng 0,501GiB, pack Git tạm mới 0,104GiB; hai bản sao deploy web thêm 0,084GiB.
- Các khoản trên giải thích khoảng **2,90GiB**; khoảng **0,04GiB** còn lại là sai số thời điểm/làm tròn và ghi/xoá nền chưa tách chính xác. Không lấy toàn bộ file vừa sửa làm “dung lượng tăng”.
- Nhóm đủ bằng chứng để đưa vào duyệt dọn: **N2 log + N4 context-pack cũ + N5 cache xác định = khoảng 4,185GiB**. Đây là ước lượng trước thao tác, chưa phải dung lượng đã thu hồi.
- **N1 Qdrant vẫn BLOCK** theo đề bài: cần hoàn tất bằng chứng cứu hộ ngoài VPS trước. Không cộng 27,58GiB vào số đã PASS.
- N3 có 71 thư mục sao Nuxt (~2,999GiB) và 1 file chỉ đường; có bản vẫn được script rollback gọi. N11 có Git worktree còn đăng ký và đường logrotate: không xoá trọn danh sách R1.
- **PASS 6 / REVISE 3 / BLOCK 6**; trong 6 PASS, N12/N13/N14 là PASS cho **giữ nguyên**, thu hồi 0.
- Chỉ ghi mục V1b và dòng VPSC.3; không ghi file bằng chứng lên VPS, không xoá/sửa/restart runtime. Host có thể dùng kết quả để chốt đề bài dọn ngay.

### 2. Chấm lại N1–N15

PASS trong bảng là phạm vi cụ thể đã kiểm để trình duyệt, không phải lệnh triển khai và không xác nhận các cơ chế retention đã được cài. V1-01…V1-06 đã được Host nhận tại D07 vẫn là yêu cầu cho lượt dọn.

| Nhóm | GB V1b / nguồn số | Kết luận | Lý do và phạm vi |
|---|---:|---|---|
| N1 Qdrant | 27,581 snapshot (V1); lớp ghi đo mới 27,581 | BLOCK | Giữ kết luận V1 theo §2E của PROMPT: chưa có bằng chứng snapshot cần giữ nằm ngoài VPS. Không tải/giải mã hay tạo bằng chứng mới ở lượt này. |
| N2 Log Directus | ≥1,316 (stat V1; lớp ghi mới 1,317) | PASS | Kiểm thêm thấy đúng log đang được mở bởi 1 FD. Đưa vào duyệt **cắt nội dung file tại chỗ**, không unlink/rm; lấy 1,316GiB làm ước lượng bảo thủ. Điều kiện vá xoay log/trần tại V1-04 phải đi cùng lượt dọn. |
| N3 Nuxt | 2,999 toàn bộ 71 thư mục; thêm 1 file chỉ đường | REVISE | Đã grep riêng đủ 72 tên. Chỉ live `nuxt-output` đang bind vào Nuxt. Nhưng `nuxt-output.bak.20260531-rp-final` được script rollback đọc; `.prev` và `.bak.pre-phab1c-20260627T165940Z` còn được mã QA/workflow nhắc. Cần chốt KEEP cụ thể gồm 3 bản gần nhất + mốc và các phụ thuộc được giữ; chưa cộng toàn nhóm vào PASS. |
| N4 context-pack.tmp | tổng 1,486; **1,444 ứng viên** | PASS | Kiểm nội dung từng cây: 979/1.001 thư mục có mọi mtime cũ hơn 3 ngày, không symlink, không thấy FD/map/process tham chiếu vào cây tạm. Giữ 22 thư mục gần đây + thư mục gốc. Dọn đúng tập cũ, kiểm lại không có job dùng trước mutation; không đụng staging/current. |
| N5 Cache | tổng phạm vi rộng 1,515; **1,424 phạm vi chốt** | PASS | Chỉ 6 vùng cụ thể dưới đây; kiểm không có hardlink file, FD hoặc map đang dùng. **Giữ `_npx`, browser runtime, uv/pnpm và phần ngoài danh sách**. Không coi toàn bộ `.npm` là sẽ được lệnh cache-clean xoá. |
| N6 Build cache | không đo lặp, R1 ~0,4 | BLOCK | R03 vẫn CLIENT-ONLY, chưa CLOSED; không mở cổng prune. Không dùng số R1 như số thu hồi mới. |
| N7 7 image trung gian | chưa xác nhận GB thu hồi riêng | BLOCK | Kế thừa kiểm từng ID/RootFS ở V1, không làm lặp. Vẫn giữ rollback tới R03 CLOSED. |
| N8 9 image local-only | chưa xác nhận GB thu hồi riêng | BLOCK | Quan hệ RootFS đã kiểm ở V1; chưa có rescue off-VPS kiểm được cho đúng tập image. Không coi dung lượng logic image là block sẽ thu hồi. |
| N9 Postgres /tmp cũ | **4,202** (1.952 target); cả /tmp 4,230 | BLOCK | Đã grep từng tên qua đủ scope. 38 dump chiếm 2,764GiB; có file SQL backup ~0,859GiB. Các tên ngắn có thể trùng script/host; không suy kết quả grep host thành quan hệ trong container. Dữ liệu cũ vẫn phải cứu trước xoá, không duyệt `/tmp/*` chung. |
| N10 SQL sau 24/07 | **0,001377**; 127 file | REVISE | R1 ghi 0,14GiB/~140 file là lệch lớn: tập `*.sql` sau mốc 24/07 chỉ ~1,41MiB. Cần sửa manifest và bỏ phần cộng nhầm; không coi mọi mục khác trong /tmp là SQL tạm. |
| N11 Tồn dư mission | **5,146**, 38 target cụ thể | BLOCK | Đã định danh và grep đủ từng target, có bảng dưới. `/root/agent-runs` còn 3 worktree đăng ký; `backups/mysql/backup.log` còn trong logrotate. Giữ phần phụ thuộc, không xoá thư mục cha theo wildcard; phần backup còn lại phải rescue trước. |
| N12 Giữ theo nhãn | không đo lặp, R1 ~1,0 | PASS (giữ) | Duy trì UNKNOWN_HOLD theo nhãn/mission, không đưa vào purge/thu hồi. |
| N13 DB thử | 1,174 (V1, không đo lặp size) | PASS (giữ) | Xác nhận lại đúng catalog comment dùng chung: **có nhãn CẤM XOÁ và DEL-1**. Giữ UNKNOWN_HOLD, không thử DROP và không đo activity theo thời gian. Đính chính lỗi kiểm comment của V1 ở dưới. |
| N14 Hermes bản cũ | không đo lặp, R1 ~3,0 | PASS (giữ) | Kế thừa launcher đã kiểm ở V1; bản cài/cứu hộ Hermes đang liên quan công việc cập nhật sáng nay. Giữ nguyên, không gộp việc hợp nhất/xoá vào nhóm cache. |
| N15 Alpine/kernel | không đo lặp, R1 ~0,3 | REVISE | Tiếp tục HOLD, không có số thu hồi mới; không cần đưa nhóm nhỏ này vào bước dọn đầu. |

**Số cộng để duyệt:** N2 1.413.027.126 byte + N4 1.550.823.424 byte + N5 1.529.266.176 byte = **4.493.116.726 byte ≈ 4,185GiB**. N12/N13/N14 PASS giữ không cộng dung lượng. Nếu chỉ làm ba nhóm này và không có ghi nền mới, available 9,401 → khoảng **13,585GiB**, chưa đạt mục tiêu 45GiB. Phần còn thiếu để đạt mục tiêu sau ba nhóm là khoảng **31,415GiB**; ưu tiên gỡ gate N1 trong đề bài dọn thay vì ép các nhóm đang HOLD thành an toàn.

**N4 — tập giữ:** 22 build từ `20260918-100007-0944f0` trở đi tại thời điểm đo; ứng viên cũ nhất/ mới nhất lấy theo mọi file bên trong, không theo mtime thư mục cha. Build cũ mới nhất thuộc tập ứng viên là `20260918-070009-403a50`. Tổng ứng viên 1,444GiB gần số R1 1,45GiB; **số lượng 979 khác ~990 của R1**, đã sửa cách lọc.

**N5 — danh sách chốt đo, không wildcard:**

| Vùng | Byte cấp phát | MiB |
|---|---:|---:|
| `/root/.npm/_cacache` | 695.414.784 | 663,20 |
| `/var/lib/hermes/.npm/_cacache` | 459.755.520 | 438,46 |
| `/root/.cache/pip` | 76.234.752 | 72,70 |
| `/root/.cache/node-gyp` | 67.747.840 | 64,61 |
| `/root/.cache/electron` | 115.056.640 | 109,73 |
| `/var/lib/hermes/.cache/electron` | 115.056.640 | 109,73 |

**Đính chính V1 về N13:** V1 đã dùng `obj_description` để đọc nhãn của database. Database là shared object nên phải dùng `shobj_description`. Lần kiểm đúng trả về có nhãn CẤM XOÁ/DEL-1; **không có bằng chứng nhãn bị gỡ**. Đây là lỗi phép kiểm của Codex ở V1, không phải vấn đề cần Owner/Host giải quyết. V1 vẫn giữ nguyên như lịch sử theo yêu cầu; kết luận hiện hành là giữ DB.

### 3. Đối soát đĩa và nguồn +2,94GiB

#### 3.1 Tổng đã đo độc lập

| Phần | GiB |
|---|---:|
| /var | 52,282 |
| /opt | 17,544 |
| /usr | 8,754 |
| /root | 5,612 |
| Swap, /tmp, /etc và phần còn lại | 2,148 |
| **Tổng du -x /** | **86,340** |
| **df Used** | **86,406** |
| **Chênh df–du** | **0,066** |

df byte lúc vào: Used **92.777.492.480**, Available **10.093.826.048**, tổng filesystem **102.888.095.744**. `lsof +L1` ghi nhận khoảng **8,46MiB** file đã unlink nhưng còn mở (khử lặp FD theo inode; có vài đối tượng memfd rất nhỏ, không dùng chúng để suy dung lượng đĩa). Chênh còn lại phù hợp metadata filesystem và thời điểm đo; không có khoảng lệch >3GiB.

Trong **42,884GiB containerd**:

| Thành phần | GiB |
|---|---:|
| Lớp ghi Qdrant | 27,581 |
| Lớp ghi postgres | 4,230 |
| Lớp ghi Directus | 1,317 |
| Lớp ghi 8 container khác đo được | 0,072 |
| Snapshot ảnh + init/các lớp còn lại | 7,511 |
| Blob nén | 2,164 |
| Metadata/chỉ mục snapshotter | 0,009 |

Tổng snapshotter **40,711GiB**, blob **2,164GiB**. Phần 7,511GiB được xác định bằng phần còn lại sau khi trừ các lớp ghi đo được; không gọi toàn bộ là “image có thể xoá”. Cowork runner không đọc được mountinfo qua exec; metadata containerd trả SnapshotKey/Snapshotter rỗng, nên không tự gán cho nó một lớp overlay hay số thu hồi. Giới hạn phân loại nhỏ này không ảnh hưởng tổng du/df và các nhóm PASS.

#### 3.2 Nguồn phát sinh buổi sáng

Đã chạy tìm theo **mtime OR ctime** sau 04:10:37Z, cộng block theo thư mục. Kết quả chỉ dùng để khoanh vùng. Ví dụ file DB sống vừa được ghi lại ~2GiB và log pm2 ~1,3GiB là **kích thước hiện có**, không phải tăng thêm từng ấy GB.

Sau đó đối chiếu **birth time thực qua stat %W**, trong cửa sổ 04:10:37Z–07:49:45Z, trên các cây nghi vấn; không có file mất birth time trong tập kiểm. `find -newerBt` không được bản find này hỗ trợ, nên dùng stat thay thế, không suy ctime thành thời điểm tạo.

| Nguồn | Phần đóng góp/đối chứng | Kết luận |
|---|---|---|
| `/var/backups/hermes` | Tổng mới **2,210GiB**, gồm `snapshot-truoc-update` ~2,203GiB và `20260921T072653-truoc-sua-updater` ~0,007GiB; 2,185GiB file có birth time trong cửa sổ, phần còn lại chủ yếu thư mục | Nguồn mới lớn nhất; R1 chưa có trong sổ nguồn sinh. |
| `/var/lib/hermes` | Đo mới **4.185.202.688 byte = 3,898GiB**; baseline R1 `du -m` 3.478MiB ≈3,396GiB ⇒ **tăng ròng ~0,501GiB** | Do cập nhật Hermes/dependency + các bản backup ZIP/state. Không cộng lại từng component vào tổng này. |
| Bản cài Hermes cũ, pack tạm Git | `tmp_pack_hEkqWK` **112.181.248 byte = 0,104GiB**, birth time trong cửa sổ | Phát sinh từ thao tác Git/update; chưa cấp quyền xoá file đang có thể được công việc khác dùng. |
| Hai bản sao deploy Nuxt sáng nay | `nuxt-output.truoc-20260921-093200` + `…093648`: file mới cấp phát **89.870.336 byte = 0,084GiB** (chưa tính block thư mục) | Do hai lượt deploy web; giữ trong tập rollback gần nhất. |
| Owner View/các file giao diện | Hai bản `hvu-b2-before-view-20260921.html`, `hvu-ui03-before-20260921.html` cộng dưới 1MiB; phần docs/data nhỏ | Không phải nguồn chính gây tăng gần 3GiB. |
| Apt, log, DB và thay file trong lúc update | Có file tạo/sửa trong cửa sổ, đồng thời có file cũ được thay/xoá | Không cộng thô kích thước mới thành tăng ròng. Phần residual khoảng 0,04GiB chưa bóc chính xác từng byte. |

Cộng phần chính **~2,899GiB**, giải thích phần lớn **+2,941GiB** của V1. Đây là đối soát có sai số theo mốc đo và baseline làm tròn MiB, **không phải chứng minh từng byte lịch sử**. Đầu V1b so cuối R1 tăng 2,952GiB, thêm ~0,011GiB so mốc V1; không dùng để ngoại suy tốc độ theo tháng.

Nguồn công việc đã đối chứng: `/opt/incomex/evidence/hermes-safe-update-20260921/README.md` mô tả việc cập nhật/cứu hộ và rollback; mã thật `/usr/local/sbin/hermes-safe-update:38,397–402` đặt một đường snapshot cố định và rsync thay bản trước. Không chạy updater hay health/restart của việc này.

#### 3.3 Bổ sung sổ nguồn sinh cho Host

| ID | Nguồn / loại | Hiện tại | Trigger | Cơ chế giữ đã thấy / việc phải chốt |
|---|---|---:|---|---|
| V1B-G21 | Backup trước cập nhật Hermes — NONBUSINESS_KEEP | 2,210GiB | Updater/diễn tập rollback | Snapshot chính dùng **một đường cố định**, không kết luận nó tự tăng theo số lượt. Giữ working set rollback này tới khi chủ việc chốt; bản phụ trước sửa updater cần hạn giữ/offload riêng. Tính thêm peak lúc backup + update vào ngân sách đĩa. |
| V1B-G22 | Backup ZIP/config của Hermes — NONBUSINESS_KEEP | 0,179GiB tại `.hermes/backups` | Updater Hermes | Chưa thấy hạn giữ được chứng minh trong vòng này; cần chủ cập nhật chốt số bản/TTL và liên hệ snapshot chính. Không xoá lẫn với cache N5. |
| V1B-G23 | Pack Git tạm ở bản cài cũ — DISPOSABLE khi chứng minh job đã kết thúc | 0,104GiB | Git/update | Phải kiểm job/lock trước dọn; không tự coi tên tmp là quyền xoá, không đưa lên Drive như backup dài hạn. |

### 4. Kiểm tham chiếu và bằng chứng

**Đã kiểm từng tên/path:** N3 **72**, N9 **1.952**, N11 **38**; tổng **2.062 target**. N11 có **19 dump iucore, 1 gói VPS, 4 vùng/file backup còn lại dưới backups, 10 vùng dưới /root, 3 vùng dưới docker và directus-dump.sql**, bảng cụ thể ở phần mở rộng. Không còn wildcard trong danh sách kiểm.

Phạm vi grep: `/opt/incomex` (hidden + bỏ qua gitignore, loại `context-pack*` và bỏ kết quả nằm ngay trong chính target), `/etc`, spool crontab **2 user**, `/run/systemd/system`, `/usr/lib/systemd/system` (đường `/lib` tương đương trên máy). Chỉ tìm văn bản, không giải nén dump/archive; không đọc nội dung khớp ra báo cáo. Lần hoàn chỉnh trả **exit 0, không lỗi đọc**. Một lượt chuẩn bị trước đó có WAL biến mất do runtime và cần sửa xử lý offset UTF-8; bảng sau dùng lượt hoàn chỉnh, không dùng zero của lượt lỗi.

Kết quả tổng của lượt hoàn chỉnh: N3 **49 tên không khớp, 23 có khớp**; N9 **1.899 không khớp, 53 có khớp**; N11 **24 không khớp trong 37 target ban đầu**, directus-dump bổ sung có 8 dòng tham chiếu. Các khớp tài liệu/báo cáo của chính đợt audit **không phải phụ thuộc runtime**. Tên ngắn như `mysql`, `backups`, `o5` có thể trùng với target khác; đã đọc ngữ cảnh các điểm trọng yếu trước khi kết luận:

- **N3:** `deploys/ROLLBACK-registries-pivot-20260531.sh:6,9` đọc bản `nuxt-output.bak.20260531-rp-final`; phải bảo vệ nếu giữ khả năng rollback đó. `audit/t2-suare-readme/qa-headless.cjs:6–7` và workflow cũ tham chiếu `.prev`/`.bak.pre-phab1c`; đây là mã kiểm/tham khảo, không chứng minh đang phục vụ. Docker bind hiện chỉ dùng `deploys/nuxt-output`. Ba backup mới nhất theo tên mốc deploy cần giữ: `…093648`, `…093200`, `…053858` ngày 21/09; không chọn “mới nhất” bằng mtime bị `cp -a` bảo toàn.
- **N9:** không thấy direct target trong lịch cron/unit của scope quét; có script thử nhắc các tên như `roles.sql`, `state_probe.sql`, `preflight.sql`, `s179_out`. Path `/tmp` ở host và trong postgres là hai namespace khác nhau; giữ phân biệt này. Dù zero tham chiếu, dump nghiệp vụ vẫn cần cứu hộ. Tập đã đếm rộng cả thư mục cũ để không bỏ sót, không biến cả tập thành danh sách xoá.
- **N11:** `/root/agent-runs` còn được 3 file `.git/worktrees/*/gitdir:1` đăng ký; **giữ** tới khi chủ worktree kết luận. `/etc/logrotate.d/incomex:22` dùng `backups/mysql/backup.log` nhưng có `missingok`; không phải chứng minh MySQL DB đang chạy, chỉ chứng minh R1 “không có tham chiếu” là quá rộng. `backups/mcp-writes-perms/.../rollback.sh:4–5` dùng **docs/mcp-writes/dieu45-phase1**, không phải **backups/dieu45-phase1** — không BLOCK nhầm chỉ vì trùng basename. `docker/directus-dump.sql` 0,031GiB chỉ thấy tài liệu/ignore/history, vẫn cần rescue vì là dump.
- **N4/N5:** đã kiểm FD/map và đường dẫn process, không thấy target đang mở; đây là kiểm tại một thời điểm, lượt dọn vẫn phải kiểm lại ngay trước mutation.
- **N7/N8:** kế thừa kết quả từng ID của V1, không chạy lại phép đã xong.
- **N13:** dùng truy vấn metadata read-only đúng catalog để sửa lỗi V1, không kết nối vào DB thử để đo hoạt động.

Không ghi raw/evidence/script vào VPS. Output được giữ ở phiên; chỉ mục dưới đây đã chuyển thành bảng kiểm theo tên, **không chứa nội dung dump/config, secret, địa chỉ mạng hay ID Drive**. Số giữ/bỏ cuối cùng của N3/N9/N11 phải lấy đúng bảng này và phản hồi Host, không quay về lệnh wildcard của R1.

<details>
<summary>Chỉ mục kiểm từng tên N3/N9/N11 (mở khi cần truy nguồn)</summary>

Mỗi dòng ghi target cụ thể; 0 = không khớp tên/path trong phạm vi grep, không tự chứng minh quyền xoá. Số khớp gồm tài liệu, log, lịch sử và mã. Tên ngắn như mysql/backups có thể trùng; cột đường dẫn đầy đủ và phần nhận định bên trên mới dùng để xác định phụ thuộc. Chỉ giữ một vị trí đối chứng mỗi target, không đưa nội dung nguồn vào repo.

#### N3 — kết quả theo từng tên

| Target | Khớp tên/path | Khớp full path | Vị trí đối chứng |
|---|---:|---:|---|
| `/opt/incomex/deploys/nuxt-output-balo-20260716T234206Z` | 12 | 9 | `/opt/incomex/evidence/lenh3d3-exact-nginx-balo-route-20260717T022923Z/pre-route-drift.txt:6` |
| `/opt/incomex/deploys/nuxt-output-balo-current-path` | 0 | 0 | — |
| `/opt/incomex/deploys/nuxt-output-balo-fresh-20260717T033701Z` | 5 | 2 | `/opt/incomex/evidence/claude-balo-oneclick-20260717T033701Z/artifact-inventory.txt:23` |
| `/opt/incomex/deploys/nuxt-output-pre-dulieuthat-20260820T040741Z` | 0 | 0 | — |
| `/opt/incomex/deploys/nuxt-output-pre-nen-diemdanh-20260820T074533Z` | 0 | 0 | — |
| `/opt/incomex/deploys/nuxt-output-prev-gddh-20260807` | 0 | 0 | — |
| `/opt/incomex/deploys/nuxt-output.backup-elearning-gon-20260820T093040Z` | 0 | 0 | — |
| `/opt/incomex/deploys/nuxt-output.backup-gddh-fast-20260820T1607` | 0 | 0 | — |
| `/opt/incomex/deploys/nuxt-output.backup-gddh-lark-20260820T1533` | 0 | 0 | — |
| `/opt/incomex/deploys/nuxt-output.backup-gddh-remove-points-20260820` | 0 | 0 | — |
| `/opt/incomex/deploys/nuxt-output.backup-pre-tiengnhat-20260822T031955` | 0 | 0 | — |
| `/opt/incomex/deploys/nuxt-output.bak-truoc-T54-20260911` | 0 | 0 | — |
| `/opt/incomex/deploys/nuxt-output.bak-truoc-chang2a4` | 0 | 0 | — |
| `/opt/incomex/deploys/nuxt-output.bak.20260531-rp-final` | 6 | 1 | `/opt/incomex/evidence/lenh3d3-exact-nginx-balo-route-20260717T022923Z/pre-route-drift.txt:7` |
| `/opt/incomex/deploys/nuxt-output.bak.p10d-20260430124407` | 6 | 4 | `/opt/incomex/evidence/lenh3d3-exact-nginx-balo-route-20260717T022923Z/pre-route-drift.txt:8` |
| `/opt/incomex/deploys/nuxt-output.bak.p10d-20260430131514` | 3 | 1 | `/opt/incomex/evidence/lenh3d3-exact-nginx-balo-route-20260717T022923Z/pre-route-drift.txt:9` |
| `/opt/incomex/deploys/nuxt-output.bak.p10d-fix-20260430232716` | 3 | 1 | `/opt/incomex/evidence/lenh3d3-exact-nginx-balo-route-20260717T022923Z/pre-route-drift.txt:10` |
| `/opt/incomex/deploys/nuxt-output.bak.p10d-layout-20260501024725` | 3 | 1 | `/opt/incomex/evidence/lenh3d3-exact-nginx-balo-route-20260717T022923Z/pre-route-drift.txt:11` |
| `/opt/incomex/deploys/nuxt-output.bak.p10d-sidebar-20260501034329` | 3 | 1 | `/opt/incomex/evidence/lenh3d3-exact-nginx-balo-route-20260717T022923Z/pre-route-drift.txt:12` |
| `/opt/incomex/deploys/nuxt-output.bak.p10d-sidebar-labels-20260501034914` | 4 | 2 | `/opt/incomex/evidence/lenh3d3-exact-nginx-balo-route-20260717T022923Z/pre-route-drift.txt:13` |
| `/opt/incomex/deploys/nuxt-output.bak.pre-balo-20260717T033701Z` | 3 | 0 | `/opt/incomex/deploys/00-NHAN-THU-MUC.md:47` |
| `/opt/incomex/deploys/nuxt-output.bak.pre-balo-countfix-20260627T100942Z` | 3 | 1 | `/opt/incomex/evidence/lenh3d3-exact-nginx-balo-route-20260717T022923Z/pre-route-drift.txt:14` |
| `/opt/incomex/deploys/nuxt-output.bak.pre-balo-phaseB-20260627T070949Z` | 3 | 1 | `/opt/incomex/evidence/lenh3d3-exact-nginx-balo-route-20260717T022923Z/pre-route-drift.txt:15` |
| `/opt/incomex/deploys/nuxt-output.bak.pre-doiten-20260813_103456` | 0 | 0 | — |
| `/opt/incomex/deploys/nuxt-output.bak.pre-elearning-embed-20260820T084254Z` | 0 | 0 | — |
| `/opt/incomex/deploys/nuxt-output.bak.pre-exam-20260813T063733Z` | 0 | 0 | — |
| `/opt/incomex/deploys/nuxt-output.bak.pre-exambank-20260813_105142` | 0 | 0 | — |
| `/opt/incomex/deploys/nuxt-output.bak.pre-gddh-20260806T042940Z` | 0 | 0 | — |
| `/opt/incomex/deploys/nuxt-output.bak.pre-gddh-4format-20260807T044330Z` | 0 | 0 | — |
| `/opt/incomex/deploys/nuxt-output.bak.pre-gddh-attendance-20260816_065918` | 0 | 0 | — |
| `/opt/incomex/deploys/nuxt-output.bak.pre-gddh-bode-20260813_114447` | 0 | 0 | — |
| `/opt/incomex/deploys/nuxt-output.bak.pre-gddh-exam-20260813_094241` | 0 | 0 | — |
| `/opt/incomex/deploys/nuxt-output.bak.pre-gddh-khung-20260806T102414Z` | 0 | 0 | — |
| `/opt/incomex/deploys/nuxt-output.bak.pre-gddh-menu3-20260813T043621Z` | 1 | 1 | `/opt/incomex/docker/nuxt-repo/web/pages/giao-duc-dinh-huong/00-NHAN-THU-MUC.md:290` |
| `/opt/incomex/deploys/nuxt-output.bak.pre-gddh-url-20260813_100322` | 0 | 0 | — |
| `/opt/incomex/deploys/nuxt-output.bak.pre-gddh-url2-20260813_101120` | 0 | 0 | — |
| `/opt/incomex/deploys/nuxt-output.bak.pre-hienhet-20260813_110234` | 0 | 0 | — |
| `/opt/incomex/deploys/nuxt-output.bak.pre-lark-qd-lop-20260819_103157` | 0 | 0 | — |
| `/opt/incomex/deploys/nuxt-output.bak.pre-mo-cong-nguoi-ngoai-20260821T175418Z` | 0 | 0 | — |
| `/opt/incomex/deploys/nuxt-output.bak.pre-mobile-20260814T045213Z` | 0 | 0 | — |
| `/opt/incomex/deploys/nuxt-output.bak.pre-mobileux-20260814T060132Z` | 0 | 0 | — |
| `/opt/incomex/deploys/nuxt-output.bak.pre-parserfix-20260813_105703` | 0 | 0 | — |
| `/opt/incomex/deploys/nuxt-output.bak.pre-phab1-20260627T121855Z` | 3 | 1 | `/opt/incomex/evidence/lenh3d3-exact-nginx-balo-route-20260717T022923Z/pre-route-drift.txt:16` |
| `/opt/incomex/deploys/nuxt-output.bak.pre-phab1c-20260627T165940Z` | 4 | 2 | `/opt/incomex/audit/t2-suare-readme/qa-headless.cjs:7` |
| `/opt/incomex/deploys/nuxt-output.bak.pre-reports-live-20260707T155857Z` | 3 | 1 | `/opt/incomex/evidence/lenh3d3-exact-nginx-balo-route-20260717T022923Z/pre-route-drift.txt:18` |
| `/opt/incomex/deploys/nuxt-output.bak.pre-reports-mvp-2a-20260625T135429Z` | 6 | 4 | `/opt/incomex/evidence/lenh3d3-exact-nginx-balo-route-20260717T022923Z/pre-route-drift.txt:19` |
| `/opt/incomex/deploys/nuxt-output.bak.pre-results-20260813_102344` | 0 | 0 | — |
| `/opt/incomex/deploys/nuxt-output.bak.pre-results2-20260813_102853` | 0 | 0 | — |
| `/opt/incomex/deploys/nuxt-output.bak.pre-rp-20260807T061646Z` | 0 | 0 | — |
| `/opt/incomex/deploys/nuxt-output.bak.pre-source-readonly-20260820T060923Z` | 0 | 0 | — |
| `/opt/incomex/deploys/nuxt-output.bak.pre-stars-20260628T134812Z` | 3 | 1 | `/opt/incomex/evidence/lenh3d3-exact-nginx-balo-route-20260717T022923Z/pre-route-drift.txt:20` |
| `/opt/incomex/deploys/nuxt-output.prev` | 17 | 12 | `/opt/incomex/audit/t2-suare-readme/qa-headless.cjs:6` |
| `/opt/incomex/deploys/nuxt-output.prev-d28-gmr-1778407748` | 3 | 1 | `/opt/incomex/evidence/lenh3d3-exact-nginx-balo-route-20260717T022923Z/pre-route-drift.txt:22` |
| `/opt/incomex/deploys/nuxt-output.prev-d28-gmr-1778407785` | 4 | 2 | `/opt/incomex/evidence/lenh3d3-exact-nginx-balo-route-20260717T022923Z/pre-route-drift.txt:23` |
| `/opt/incomex/deploys/nuxt-output.prev-gddh-20260806T051012Z` | 0 | 0 | — |
| `/opt/incomex/deploys/nuxt-output.prev2` | 2 | 1 | `/opt/incomex/evidence/lenh3d3-exact-nginx-balo-route-20260717T022923Z/pre-route-drift.txt:24` |
| `/opt/incomex/deploys/nuxt-output.truoc-20260913-170540` | 0 | 0 | — |
| `/opt/incomex/deploys/nuxt-output.truoc-20260913-233845` | 0 | 0 | — |
| `/opt/incomex/deploys/nuxt-output.truoc-20260913-235600` | 0 | 0 | — |
| `/opt/incomex/deploys/nuxt-output.truoc-20260914-000056` | 0 | 0 | — |
| `/opt/incomex/deploys/nuxt-output.truoc-20260914-115815` | 0 | 0 | — |
| `/opt/incomex/deploys/nuxt-output.truoc-20260914-130502` | 0 | 0 | — |
| `/opt/incomex/deploys/nuxt-output.truoc-20260914-134228` | 0 | 0 | — |
| `/opt/incomex/deploys/nuxt-output.truoc-20260915-022835` | 0 | 0 | — |
| `/opt/incomex/deploys/nuxt-output.truoc-20260915-030847` | 0 | 0 | — |
| `/opt/incomex/deploys/nuxt-output.truoc-20260915-093759` | 0 | 0 | — |
| `/opt/incomex/deploys/nuxt-output.truoc-20260915-104717` | 0 | 0 | — |
| `/opt/incomex/deploys/nuxt-output.truoc-20260915-130354` | 0 | 0 | — |
| `/opt/incomex/deploys/nuxt-output.truoc-20260921-053026` | 5 | 0 | `/opt/incomex/mcp-roots/gh/work/vps-clean-20-9-26/BAO-CAO.md:273` |
| `/opt/incomex/deploys/nuxt-output.truoc-20260921-053858` | 0 | 0 | — |
| `/opt/incomex/deploys/nuxt-output.truoc-20260921-093200` | 0 | 0 | — |
| `/opt/incomex/deploys/nuxt-output.truoc-20260921-093648` | 0 | 0 | — |

#### N9 — kết quả theo từng tên

| Target | Khớp tên/path | Khớp full path | Vị trí đối chứng |
|---|---:|---:|---|
| `postgres:/tmp/canon-adapter-tests.xa0eishn` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-vucr7_7c` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-jqgg0bcb` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-o931fnj8` | 0 | 0 | — |
| `postgres:/tmp/refresh_all_counts_inline.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-nlvvt83y` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-3wucmp6z` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.5uvia622` | 0 | 0 | — |
| `postgres:/tmp/p10b-1b` | 11 | 5 | `/opt/incomex/backups/dieu44_v0_3_readobs_dryrun_rerun_20260516T230306Z/prod-directus-20260516T230306Z.sql:1238113` |
| `postgres:/tmp/canon-adapter-tests.lryzk5t8` | 0 | 0 | — |
| `postgres:/tmp/get_fn2.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-g88bcvd8` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-l_w8xwjq` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-o6od5ewb` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-4h438di5` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-7gbumkhc` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-uud685ve` | 0 | 0 | — |
| `postgres:/tmp/sb200.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-m5d1ehi6` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.0eo0k21u` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-3dcj8nl6` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-gdmml3gt` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-zyphg8az` | 0 | 0 | — |
| `postgres:/tmp/prod_cg2.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-yxx39c6f` | 0 | 0 | — |
| `postgres:/tmp/q8.sql` | 0 | 0 | — |
| `postgres:/tmp/bulk.sql` | 0 | 0 | — |
| `postgres:/tmp/perms_final.sql` | 0 | 0 | — |
| `postgres:/tmp/phase4.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-fumdflcr` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-p8w49x0q` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-hu9uk9gg` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-t117zbtz` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-gq1e7cvh` | 0 | 0 | — |
| `postgres:/tmp/p10b-2b-fix` | 16 | 12 | `/opt/incomex/backups/dieu44_v0_3_readobs_dryrun_rerun_20260516T230306Z/prod-directus-20260516T230306Z.sql:1238141` |
| `postgres:/tmp/iu-cutter-cut-f20c79c-20260520T031054Z` | 0 | 0 | — |
| `postgres:/tmp/p3d4c1u_step45.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-w2bwgpm2` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-ywdb2d75` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-stwg8exl` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-6a2gzk2z` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-afb4u1bo` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-wcxg8h6a` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-w0as8lzp` | 0 | 0 | — |
| `postgres:/tmp/quorum.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-fh4xujm2` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-gna970xx` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-mh7g_e3y` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-omn7_6w0` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-s29bhi8i` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.6gbfm2lu` | 0 | 0 | — |
| `postgres:/tmp/probe3.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-palhrjfk` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-h89uftlx` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-boklsvmf` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-0_zg6fm7` | 0 | 0 | — |
| `postgres:/tmp/d43-fixtures-test` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-dmusnihh` | 0 | 0 | — |
| `postgres:/tmp/dieu45_phase2_post.dump` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-pau2cfp1` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-sii53u0q` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-ipbdwk38` | 0 | 0 | — |
| `postgres:/tmp/post_verify_approve_cut_gate_fix.dump` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-nf40v47h` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-a9bb4jpb` | 0 | 0 | — |
| `postgres:/tmp/getfn.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-uux86fq3` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-6czz4b19` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-y95huwyn` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-6p8z3lb0` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-xnpjbe7d` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-3kejzczx` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-zg1ihacz` | 0 | 0 | — |
| `postgres:/tmp/p10b1b_vocab.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-9i7dpjs_` | 0 | 0 | — |
| `postgres:/tmp/ins_section.sql` | 0 | 0 | — |
| `postgres:/tmp/036.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-5d3643uj` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-4ujjjpz8` | 0 | 0 | — |
| `postgres:/tmp/pa_verify.sql` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.9j75irhw` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-e_kg8re3` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-9ju1u6tb` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-j2t9vveu` | 0 | 0 | — |
| `postgres:/tmp/b3f0a_insert.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-ubg2abs1` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-p1zmmiwi` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-sew6wxhp` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.zzewfg4t` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-udv_f5b2` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-f7pmt427` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-nvm19g1s` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-i_1dy2gu` | 0 | 0 | — |
| `postgres:/tmp/p10a2a-phase0.sql` | 1 | 1 | `/opt/incomex/backups/dieu44_v0_3_readobs_dryrun_rerun_20260516T230306Z/prod-directus-20260516T230306Z.sql:1238075` |
| `postgres:/tmp/iucut-cutwrite-neg-tbtv4ppw` | 0 | 0 | — |
| `postgres:/tmp/p10b1b_trig.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-sbd10his` | 0 | 0 | — |
| `postgres:/tmp/register_scanners.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-gabx37e1` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-tzyloume` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-nooshcp1` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.n0ym0f2c` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-abnb495y` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-wahnveea` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-138al_jo` | 0 | 0 | — |
| `postgres:/tmp/s160_update_d39.sql` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.4tqawhrn` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-tnzqtjf_` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-4mk4rkfu` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-gnh5c1ol` | 0 | 0 | — |
| `postgres:/tmp/25k_phaseE.sql` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.pf_t_c6o` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-80wull50` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-0lx6bbkl` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-ddeocg0x` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-_pnle2pi` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-ze418b6h` | 0 | 0 | — |
| `postgres:/tmp/d1_index.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-m1761ygh` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.0vsc71de` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-cv0fnzc1` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-p375lnpn` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-8hovqctf` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-y24g9f0n` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-7t8kwff5` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-qzsd5hdl` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-uhkvmz9p` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-h2i42qzi` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-pkvpza9w` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-tse695pb` | 0 | 0 | — |
| `postgres:/tmp/b3a2b_txn.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-l00al8y0` | 0 | 0 | — |
| `postgres:/tmp/024.sql` | 0 | 0 | — |
| `postgres:/tmp/preflight_rehearsal.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-9fihp8fa` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-v0utd0lh` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-njmay13a` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-3n9yo76j` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-mic5tvak` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-4f3vnrhy` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-icp64h7n` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-wonbncfs` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-28jsapnu` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-qmh_dpy0` | 0 | 0 | — |
| `postgres:/tmp/g6_run4_20260428_041121` | 9 | 9 | `/opt/incomex/data/tac/gate-a/prechecks-output.txt:4` |
| `postgres:/tmp/iucut-legA-orjs2om7` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-lndc5po7` | 0 | 0 | — |
| `postgres:/tmp/b3f1c_b_execute.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-d888rfoi` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-k8uvih0c` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-n85mov03` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-1qp1vfyz` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-nxia8qd0` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-i4fyxo34` | 0 | 0 | — |
| `postgres:/tmp/25k_phaseC.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-igg1pcqf` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-ola2dsa0` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-lww8_5se` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.wb_xa91o` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-ztt_qt4n` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-pwq3lvdb` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-d5caa3_y` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-ich63ovv` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-tg7vozjo` | 0 | 0 | — |
| `postgres:/tmp/phase_alpha_baseline_20260516T014818Z.dump` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-ucm21spp` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-e6k9ql68` | 0 | 0 | — |
| `postgres:/tmp/b3a2b_preflight.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-wtyhkdho` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-6btb6w3j` | 0 | 0 | — |
| `postgres:/tmp/iu_core_post_50000x.dump` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-3mjac41v` | 0 | 0 | — |
| `postgres:/tmp/o6` | 561 | 0 | `/opt/incomex/deploys/nuxt-output-pre-dulieuthat-20260820T040741Z/public/_nuxt/DEZ2aKzG.js:35` |
| `postgres:/tmp/iucut-prod-ror9d_q0` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-cluqhmby` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-d1tkxj7z` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-toesunvv` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-ony7r3hy` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-v3p8h9o6` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-v2frv2b6` | 0 | 0 | — |
| `postgres:/tmp/iucore_ret3.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-q6zfxfku` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-gkqr_8r2` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-zzbfb2cr` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-5teu3i9o` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-q9u4ungx` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-7332ynrk` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-7pmajwmx` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-9qz25bby` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-1flerc49` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.6igyjii9` | 0 | 0 | — |
| `postgres:/tmp/m1_ddl.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-uwo9ranz` | 0 | 0 | — |
| `postgres:/tmp/110_d9.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-y1z3slre` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-cn4ms58g` | 0 | 0 | — |
| `postgres:/tmp/029.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-ci2ctngz` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-78zd9o63` | 0 | 0 | — |
| `postgres:/tmp/dieu45_phase3b_pre_apply.dump` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-k1nrcps1` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-jicwney7` | 0 | 0 | — |
| `postgres:/tmp/dieu39_unit_kind_fix.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-41qhiwg1` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-6uhwgljq` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-2sn_hhpe` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-_l_f033i` | 0 | 0 | — |
| `postgres:/tmp/pre-iucore-15000x-baseline.dump` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-5qs39aqb` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-_0jhysyg` | 0 | 0 | — |
| `postgres:/tmp/step5.sql` | 0 | 0 | — |
| `postgres:/tmp/036.rollback.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-8r18meiu` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-cpp76ez8` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-f6i5t7eb` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-ue6g25ry` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-xddt6d0w` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-pxxljo8q` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-nofeaxku` | 0 | 0 | — |
| `postgres:/tmp/run_refresh.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-eytnake3` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-abmixp96` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-juzgbkqa` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-jpfq0dkg` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-2o1lqssd` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.zg6the2y` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-6z98fqh2` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-fimm2wav` | 0 | 0 | — |
| `postgres:/tmp/post_iu_cut_runtime_harden_20260526T171912Z.dump` | 0 | 0 | — |
| `postgres:/tmp/obs_check.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-9zt1y8iz` | 0 | 0 | — |
| `postgres:/tmp/lark-gpg-home-2595274` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-60n9u22s` | 0 | 0 | — |
| `postgres:/tmp/d1_verify.sql` | 0 | 0 | — |
| `postgres:/tmp/s161_p1_kg_schema.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-1jtsol9f` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-22ruebua` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-1c1c5sa_` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-8molj0ah` | 0 | 0 | — |
| `postgres:/tmp/053_proofs.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-4ognrwzs` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-3m2_wkqg` | 0 | 0 | — |
| `postgres:/tmp/d1_verify2.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-rl5flgu3` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-xumgpwdu` | 0 | 0 | — |
| `postgres:/tmp/iu020.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-xu75povn` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-c7v8uvwu` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-ssm0dagc` | 0 | 0 | — |
| `postgres:/tmp/fix_meta_counts.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-i79i6gzt` | 0 | 0 | — |
| `postgres:/tmp/d30_d31_probes.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-taf46u62` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-tv2d2g_d` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-iszdboan` | 0 | 0 | — |
| `postgres:/tmp/afl-insert.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-dxx2orqb` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-odr_5sbe` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-9fhq2840` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-l0bcveb5` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-40yqn42m` | 0 | 0 | — |
| `postgres:/tmp/dieu45_phase2_proof.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-1l51hys4` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.qbwgmfmb` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-5mz3u5fn` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-kxvh18nq` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-mdc0o540` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-sxxq8wbf` | 0 | 0 | — |
| `postgres:/tmp/baseline4.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-x35t5k1g` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-oua0d_pj` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-83j7qh2w` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-81flr3kw` | 0 | 0 | — |
| `postgres:/tmp/update_trigger_fn.sql` | 0 | 0 | — |
| `postgres:/tmp/inv.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-igekgk70` | 0 | 0 | — |
| `postgres:/tmp/step1.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-jy3zk_pb` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-ncnvo6m0` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-bvojvc5i` | 0 | 0 | — |
| `postgres:/tmp/d1_force.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-l1q0i71_` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-fpn4z84w` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-5f0qhqgi` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-f6nt5dj4` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-m0klxaxg` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.u0wndkpu` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-8cofuyka` | 0 | 0 | — |
| `postgres:/tmp/s179_out` | 2 | 2 | `/opt/incomex/lark-client/scripts/s179_probe.py:21` |
| `postgres:/tmp/iucut-legA-qqixvmoj` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-1nroevd7` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-anuhyyax` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-icxgknh5` | 0 | 0 | — |
| `postgres:/tmp/pre-91000x-20260526T010854Z.dump` | 0 | 0 | — |
| `postgres:/tmp/035_auto_instantiate_log_retention_policy.rollback.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-lay0dfvt` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-s0i01hmu` | 0 | 0 | — |
| `postgres:/tmp/01-piece-event-type-seed.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-gy_tunye` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-m2nb7q83` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-w1hbm34w` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-9ne_31vc` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-18phwhbr` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-cis3v7xx` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-ru7k2qnm` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-oc_wv7_8` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-esh1pi65` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-v_5szhhl` | 0 | 0 | — |
| `postgres:/tmp/directus-pre-iucore-4000x-20260523T084654Z.dump` | 0 | 0 | — |
| `postgres:/tmp/s170c_fix.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-_wxhrd6p` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-jqua0ejs` | 0 | 0 | — |
| `postgres:/tmp/053_dryrun.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-j10dug0h` | 0 | 0 | — |
| `postgres:/tmp/view_final.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-i9gzjj_0` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-zir7h1u5` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-iwbj3zf8` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-8eecqq8c` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-l_uas2x6` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-7u3s6ovj` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-0z3uzxpi` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-cumea66z` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-niukamkh` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-4i4_17oj` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-1uhkqes6` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-48yk5tty` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-tipavnua` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-0r0lq8v5` | 0 | 0 | — |
| `postgres:/tmp/dieu45_phase3b_post_apply.dump` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-pa7yl82r` | 0 | 0 | — |
| `postgres:/tmp/directus-pre-iucore-8000x-execute-20260524T081848Z.dump` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-6vq4fxy1` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-lphbfna7` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-1vzo2spj` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-er0ayz5z` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-4uh4spjy` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-n70x17a2` | 0 | 0 | — |
| `postgres:/tmp/nuxt-output-p10d-fix` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-0v0tecm9` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-hov8mdsc` | 0 | 0 | — |
| `postgres:/tmp/pre-iucore-18000x-baseline.dump` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-bf8v8zpb` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-yxvxb4xs` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.3pbte24q` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-5aj8vzlw` | 0 | 0 | — |
| `postgres:/tmp/table_to_view.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-dxtvndkw` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-u7q6_y5t` | 0 | 0 | — |
| `postgres:/tmp/pg_dump_pre_mig055_20260527T043033Z.dump` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.nylvj8ok` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-63py0x9o` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-3sag69xx` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-ifo9bywk` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-6pqqalit` | 0 | 0 | — |
| `postgres:/tmp/patch_payload_and_resume.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-5_yoej5z` | 0 | 0 | — |
| `postgres:/tmp/053_phaseE_regression.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-yvjsczaa` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-s26g8tgu` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-gb2muf21` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-ld5jiw_i` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-33r1rm3z` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-mjd6g70i` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-habsdwur` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-5tw0jotj` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-dr8v9v1v` | 0 | 0 | — |
| `postgres:/tmp/053_iu_cut_runtime_hardening.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-zkcdhu7b` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-fwar7xg_` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-7nwcc7zu` | 0 | 0 | — |
| `postgres:/tmp/s161_p2_dot_kg.sql` | 0 | 0 | — |
| `postgres:/tmp/s178fix16_e2e` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.80vtpvuf` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-1cg9gtzi` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-6_wnt6ox` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-wc0ga6lk` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-icfwlyr4` | 0 | 0 | — |
| `postgres:/tmp/nuxt-output-p10d-sidebar` | 0 | 0 | — |
| `postgres:/tmp/p10b-2b` | 16 | 10 | `/opt/incomex/backups/dieu44_v0_3_readobs_dryrun_rerun_20260516T230306Z/prod-directus-20260516T230306Z.sql:1238130` |
| `postgres:/tmp/iucut-cli-hbqo8ay4` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-4cfechuz` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-x3wb_e52` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-ztaxe_5p` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-kjppj_1f` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-mc99n4gl` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-9qz6wdih` | 0 | 0 | — |
| `postgres:/tmp/mig_055.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-_15j5mx_` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-2401jl28` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-t18muvuy` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-ccm9udwq` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.upsd6xxo` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-63lpg06u` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-s3oqmca4` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-9be3swr4` | 0 | 0 | — |
| `postgres:/tmp/nuxt-output-p10d-sidebar-704ff74` | 0 | 0 | — |
| `postgres:/tmp/pre_dieu39_verify_mark_fix_20260527_094407.dump` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-f99mrezn` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-9sdbr8gt` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-8kuonevu` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-zb4sz3hy` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-x4o21c8b` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-eafgahwf` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-ctzi3mro` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-cpt5l6av` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-5lo228f7` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-chlgt303` | 0 | 0 | — |
| `postgres:/tmp/create_auto_functions.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-jm2kjz_4` | 0 | 0 | — |
| `postgres:/tmp/05_discovery_views_v3.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-bcc6eujq` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-wuferqvc` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-xko0dek0` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-95mm64m6` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-bilnryyg` | 0 | 0 | — |
| `postgres:/tmp/lark-summary-2026-04-11` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-kxd3glg9` | 0 | 0 | — |
| `postgres:/tmp/25k_phaseB.sql` | 0 | 0 | — |
| `postgres:/tmp/042R_iu_core_operator_aliases.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-wf12pvz8` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-83u9w8yv` | 0 | 0 | — |
| `postgres:/tmp/280-seed.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-kvpvs49r` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-spfa73za` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-45qdvowv` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-3gbcsz4o` | 0 | 0 | — |
| `postgres:/tmp/set_perms_pr.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-u2ixr0j_` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-40xeigih` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-ovj2_lk2` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-hgkx2o4i` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-gr_s0hpl` | 0 | 0 | — |
| `postgres:/tmp/g6_run_20260427_114640` | 8 | 8 | `/opt/incomex/backups/dieu44_v0_3_readobs_dryrun_rerun_20260516T230306Z/prod-directus-20260516T230306Z.sql:1237871` |
| `postgres:/tmp/dieu38_patch_pieces_content.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-1xa1nj91` | 0 | 0 | — |
| `postgres:/tmp/o5` | 434 | 0 | `/opt/incomex/deploys/nuxt-output-pre-dulieuthat-20260820T040741Z/public/_nuxt/DEZ2aKzG.js:31` |
| `postgres:/tmp/iucut-cutplan-neg-j8xxq9jk` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-508ywii6` | 0 | 0 | — |
| `postgres:/tmp/postdmp_iu_cut_op_pipeline_20260526_164434.dump` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-scqjdhkk` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-3lffl4b5` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-g4s8q2hg` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-fh8agjaz` | 0 | 0 | — |
| `postgres:/tmp/lark-test-audit-b4-confirm` | 1 | 1 | `/opt/incomex/lark-client/tests/test_cli_records.py:273` |
| `postgres:/tmp/b3a4_health.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-5c6wvsru` | 0 | 0 | — |
| `postgres:/tmp/dieu43-p0-v12` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-ed6kj29t` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-dmja8oyr` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-zwkqax2_` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-7drbpks0` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-nu4zujdn` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-zi5rro5o` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-qm7le1xi` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-ti2oe6la` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-rneqgobj` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.09mz5lpg` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-34ehp0aw` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-swtx678_` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-98cgpkay` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-26df07kj` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-_mn1wtil` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-xpkqs45_` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-74ze4pjr` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.mwg4t3_3` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-g0_95jwh` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-yys3iqwt` | 0 | 0 | — |
| `postgres:/tmp/m3a_log.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-o5rdza8b` | 0 | 0 | — |
| `postgres:/tmp/pa_fix_rollback.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-xs3z5b0u` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-apw60j6f` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-htmbskw2` | 0 | 0 | — |
| `postgres:/tmp/sp.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-jqs757ma` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-nbdxmmcm` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-rxty1ojh` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-d733d74y` | 0 | 0 | — |
| `postgres:/tmp/02-prereq-dot-config.sql` | 6 | 0 | `/opt/incomex/backups/dieu44_v0_3_readobs_dryrun_rerun_20260516T230306Z/prod-directus-20260516T230306Z.sql:1237573` |
| `postgres:/tmp/scan.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-4tnl6_bw` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-8743tp8w` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-umnctsgf` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-rs9dzr35` | 0 | 0 | — |
| `postgres:/tmp/fix25_a2_a7.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-rqkfnv2l` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-0pynmuyd` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.vdq99xtv` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-jqvtrh1f` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-_i_irxug` | 0 | 0 | — |
| `postgres:/tmp/12000x_DEF_only.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-snn19ghk` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-eqb3dwkq` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-1va9e28q` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-p2t3s8xy` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-9du4865n` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-21l036ex` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-1j4w_xkq` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-ip4o2_7e` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-630gf8ip` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-1dmth8bb` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-5xqc9q99` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-0d66s_xp` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-5xbidzir` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-3d08wyi5` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-99y19c7f` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.r18wqexf` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-a6dd5q7n` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-a7ht6gk9` | 0 | 0 | — |
| `postgres:/tmp/view_perms2.sql` | 0 | 0 | — |
| `postgres:/tmp/s162_p3_quality.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-rw5izhf3` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-bqsv6x4m` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-pto2qnft` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-g8sam7fs` | 0 | 0 | — |
| `postgres:/tmp/step2.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-e2i3bsjy` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-m8i63hp8` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-qe2s88z6` | 0 | 0 | — |
| `postgres:/tmp/g6_run_20260428_022517` | 5 | 5 | `/opt/incomex/backups/dieu44_v0_3_readobs_dryrun_rerun_20260516T230306Z/prod-directus-20260516T230306Z.sql:1237964` |
| `postgres:/tmp/iucut-legA-krtysy_3` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-njp79_xa` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-2iok2g_q` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-4h7rr7z9` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-hlv_yho0` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-i_lzhlmi` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-bnajsxj5` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-x30vf9g1` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-g1b8ati3` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-vg585_9d` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-m0300uy3` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-lvhezg4t` | 0 | 0 | — |
| `postgres:/tmp/110_iu_core_dot_conformance_scan.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-pvjzgpas` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-6l14g7yv` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-tfxi33xg` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-8yhpd12b` | 0 | 0 | — |
| `postgres:/tmp/b3a3_verify.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-2ik2p025` | 0 | 0 | — |
| `postgres:/tmp/iu_core_18000x_apply_v2_template.sql` | 0 | 0 | — |
| `postgres:/tmp/pre_iu_cut_runtime_harden_20260526T170620Z.dump` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-8r872_uq` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-k4pwj7zx` | 0 | 0 | — |
| `postgres:/tmp/q9.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-xv75myrq` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-eh13jvk0` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-boxj3w9v` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-xetw7uct` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-i0atbfe0` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-tp1hh5v9` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-2ckzmdw4` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-t4dpfgec` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-xx2sn7vf` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-c3m_b2yn` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-rzi8nxev` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-309llz15` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-x_vjgw3s` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-tlftsg8z` | 0 | 0 | — |
| `postgres:/tmp/mig08.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-742jnlx_` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-149jdabj` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-6h2w5__e` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-u76cwn_l` | 0 | 0 | — |
| `postgres:/tmp/iu_core_18000x_bulk_instances.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-r4960z2x` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-72rort4v` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-u7b4ayd7` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-er7f9qjx` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-dxz_rft7` | 0 | 0 | — |
| `postgres:/tmp/snap_before.sql` | 1 | 1 | `/opt/incomex/data/workspace-tools/results/0d9563bf78354e0d8d20e0d19adbc0f1:1` |
| `postgres:/tmp/iucut-legA-r3msz9d6` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-_0g_3ley` | 0 | 0 | — |
| `postgres:/tmp/view_perms.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-_en44l8e` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-p3vol5kz` | 0 | 0 | — |
| `postgres:/tmp/scaleout.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-vnfusgvp` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-aoryup65` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-pp5cznyj` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-hthivtf7` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-ulqw2dra` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-nn68s7az` | 0 | 0 | — |
| `postgres:/tmp/s163_fill.sql` | 0 | 0 | — |
| `postgres:/tmp/fix_refresh_fn.sql` | 0 | 0 | — |
| `postgres:/tmp/v3-create-apr.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-men08vo6` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-jm0faapu` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-2k0yuoh5` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-m32dnmie` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-lnsl3wyg` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-984iol5d` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-95ow9f74` | 0 | 0 | — |
| `postgres:/tmp/mark_dot_applied.sql` | 0 | 0 | — |
| `postgres:/tmp/systemd-private-c2f7e1f5fd3246dd926825ec5f8e2eea-polkit.service-PNY5oH` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-ai4z8yhm` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-u1_n_lq_` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-lbdvx_1w` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-or6xni64` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-fn_d6860` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-k8igabhr` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-a_x_v8ku` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-fn2n6xtr` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-q9b4aodm` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-2gq83jir` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-24pywlnp` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-xwbvbg5_` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-2tak48x2` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-i5wgpudz` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-01s712e8` | 0 | 0 | — |
| `postgres:/tmp/create_pivot_results.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-y30b19_7` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-48bf76dg` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-qny7qr98` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-423ysueu` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-q8ohjqis` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-1zxff0u0` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.ycb0frkd` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-v_47dj3p` | 0 | 0 | — |
| `postgres:/tmp/boundary.sql` | 0 | 0 | — |
| `postgres:/tmp/species_pivot2.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-x50oaken` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-co4j4ldk` | 0 | 0 | — |
| `postgres:/tmp/330_three_axis_envelope_auto_refresh_smoke.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-vj1k_7vu` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests._eaftkt0` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-n0po5s22` | 0 | 0 | — |
| `postgres:/tmp/desc-autogen-tests.sql` | 0 | 0 | — |
| `postgres:/tmp/directus-pre-iucore-25000x-20260525T043922Z.dump` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.o3xemdfd` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-4v51ujmi` | 0 | 0 | — |
| `postgres:/tmp/mark_applied.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-96ojdnc1` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-lqnsk2ka` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-qjutz1on` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-nj4830u6` | 0 | 0 | — |
| `postgres:/tmp/021.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-jkvo7h6h` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-yifznlyc` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-zo61p8ki` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-3hjq8h55` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-s854pntm` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-lzp02j3h` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-xxlhwk9x` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-sv8opejq` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-85i636u0` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-u1vjp_ox` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-925fbv5u` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-bwiq5wfj` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-4j103plk` | 0 | 0 | — |
| `postgres:/tmp/c2b-seed` | 1 | 1 | `/opt/incomex/backups/dieu44_v0_3_readobs_dryrun_rerun_20260516T230306Z/prod-directus-20260516T230306Z.sql:1237857` |
| `postgres:/tmp/iucut-prod-a-dlbgmvat` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-nvxbwldx` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-8oqwm14m` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-tgdyoiem` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-5dajm9xj` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-168rjh6d` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-ghz7lzg7` | 0 | 0 | — |
| `postgres:/tmp/dieu39_regression_tests.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-sqonrq5x` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-gvazixjb` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-j9bqtcal` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-qnpq7tyq` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-imzvxv36` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-30jwabuf` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-xh2414e4` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-5fpwrtih` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-loxzwovb` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-lzzzwcw0` | 0 | 0 | — |
| `postgres:/tmp/iu-cutter-v05-stage` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-pfrvc3li` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-5gd3umco` | 0 | 0 | — |
| `postgres:/tmp/d43r2` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-9gamtr01` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-6chvmz6m` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-nqdpz1aq` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-usourtw7` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-v7yusddr` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-ycbw6ws2` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-gu3aw0z3` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-e69hfvz7` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-stwizmui` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-fb73pm6j` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-yab915xr` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-ffmazlhg` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-s21pcibt` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-0qrjedqc` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-6wulcek3` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-w0r8q7gi` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-lrv3_ti5` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-v_sginui` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-3wq0ssqm` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-tcfjzhzb` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-s4_s4g77` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-m60eblqd` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-mnq0w6r1` | 0 | 0 | — |
| `postgres:/tmp/create_approval.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-w30czudo` | 0 | 0 | — |
| `postgres:/tmp/baseline3.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-1ib4emvi` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-8i488hjf` | 0 | 0 | — |
| `postgres:/tmp/preflight2.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-d0ax7ufl` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-tw1u64ln` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-b8t8q7ya` | 0 | 0 | — |
| `postgres:/tmp/__pycache__` | 2629 | 0 | `/opt/incomex/scripts/code-backup-to-gdrive.sh:247` |
| `postgres:/tmp/iucut-cutplan-gh_deqqc` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-21n3zghs` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-trrd0h5e` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-0jxjxxoj` | 0 | 0 | — |
| `postgres:/tmp/030.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-ajqpn1g8` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-4x6xh0nm` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-3q2djujg` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-tgkr8h5d` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-9m15khst` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-_74oc65w` | 0 | 0 | — |
| `postgres:/tmp/hc_update.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-vmi5tgge` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-u4ejw_wd` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-w1ptoo_d` | 0 | 0 | — |
| `postgres:/tmp/pre_verify_approve_cut_gate_fix.dump` | 0 | 0 | — |
| `postgres:/tmp/r110.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-ak83jiho` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-5ikoicnz` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-g47fd3e9` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-gphxlown` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-n3tl3sm4` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-8de082oy` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-55cbm_25` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-5o__qkyf` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.ysj_v0c1` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-o460u6s4` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-imvtjg9f` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-8idu_lpl` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-c95njao_` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-0x3j02q0` | 0 | 0 | — |
| `postgres:/tmp/pre-110500x.dump` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-_j1hzexh` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-lp9481uv` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-kqdcldmw` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-vjeebvb0` | 0 | 0 | — |
| `postgres:/tmp/d1_explain_force.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-h07in71o` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-m_j1qb8t` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-qz7kdvbz` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-uxfz3zui` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-w911ml37` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-34xbci08` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-3yrui31l` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-i1biisa8` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-j20anwvx` | 0 | 0 | — |
| `postgres:/tmp/iucore_baseline2.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-71vgvcxa` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-wzybi5a1` | 0 | 0 | — |
| `postgres:/tmp/directus-pre-iucore-6000x-20260523T140636Z.dump` | 1 | 0 | `/opt/incomex/data/workspace-tools/results/0d9563bf78354e0d8d20e0d19adbc0f1:1` |
| `postgres:/tmp/iucut-cli-sjix97vk` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-z_sfulou` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-5lp_wbe_` | 0 | 0 | — |
| `postgres:/tmp/pa_step14.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-uzr9cv4i` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-6j0bkiry` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-e1f89iio` | 0 | 0 | — |
| `postgres:/tmp/dieu45_phase2_pre.dump` | 0 | 0 | — |
| `postgres:/tmp/r310.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-9mjrewrt` | 0 | 0 | — |
| `postgres:/tmp/d.dump` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-yfn2kzwo` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-ipeg_388` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-wx90wled` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-q5l68enk` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-6piy367h` | 0 | 0 | — |
| `postgres:/tmp/iucore_retention.sql` | 0 | 0 | — |
| `postgres:/tmp/sb180.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-hmaf1r25` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-vy61tfa6` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-20bna29b` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-wgh5wjgh` | 0 | 0 | — |
| `postgres:/tmp/preflight_workflow.sql` | 0 | 0 | — |
| `postgres:/tmp/mig033.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-fz2lskxo` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-rp60aydf` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-p0d2yonz` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-7ifsu_x6` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-6510_f7k` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-rtg2v308` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-10b8it6x` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-w2emwe65` | 0 | 0 | — |
| `postgres:/tmp/110_scan.sql` | 0 | 0 | — |
| `postgres:/tmp/iu_core_18000x_piece_event_live_proof.sql` | 0 | 0 | — |
| `postgres:/tmp/register_view_fields.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-b3ga6xwo` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-d5oju76e` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-mo9b8ovw` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-xm_bj1kp` | 0 | 0 | — |
| `postgres:/tmp/evt.sql` | 0 | 0 | — |
| `postgres:/tmp/nuxt-output-p10d-layout` | 0 | 0 | — |
| `postgres:/tmp/s1.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-kd2ohi2g` | 0 | 0 | — |
| `postgres:/tmp/nvsz_probe.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-i04cfj06` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-ahq2dwtr` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-dj508mpx` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-jd1ysre3` | 0 | 0 | — |
| `postgres:/tmp/p3d4c1u_ddl.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-ni9tko3f` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-2m8apvz5` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-5og4ui1y` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-02su4k7i` | 0 | 0 | — |
| `postgres:/tmp/node-compile-cache` | 1 | 0 | `/opt/incomex/docker/nuxt-repo/web/node_modules/.pnpm/@types+node@25.0.1/node_modules/@types/node/module.d.ts:69` |
| `postgres:/tmp/h.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-ztvqpxor` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-k9w2syt3` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-rqx7u9jr` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-1zx1b9kl` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-1zjly267` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-kewmvd_1` | 0 | 0 | — |
| `postgres:/tmp/b3a_readiness.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-twxmxu2v` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-po7e5z39` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-qv_pl8ep` | 0 | 0 | — |
| `postgres:/tmp/034_auto_instantiate_dot_registration.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-t95_5e1e` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-1pij_14r` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-ad3_ik08` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-_g3dlyev` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-xit6upyj` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.2bc33uir` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-7ybkomq6` | 0 | 0 | — |
| `postgres:/tmp/050.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-jpg_angf` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-40_5ik24` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-1vln_2iz` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-xkyzdajr` | 0 | 0 | — |
| `postgres:/tmp/fn_log_issue.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-_b3c73p2` | 0 | 0 | — |
| `postgres:/tmp/034_auto_instantiate_dot_registration.rollback.sql` | 0 | 0 | — |
| `postgres:/tmp/d1_index2.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-he_4t7kw` | 0 | 0 | — |
| `postgres:/tmp/d28-stage2-kb` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-xgcmgp5p` | 0 | 0 | — |
| `postgres:/tmp/step3.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-3ky8xtn9` | 0 | 0 | — |
| `postgres:/tmp/check_pcs.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-j8nvfygz` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-vpdxm5ak` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-rqrnpf0_` | 0 | 0 | — |
| `postgres:/tmp/056.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-_cerz_gr` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-_iat4zfd` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-a_3oz_ry` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-g_26rpzv` | 0 | 0 | — |
| `postgres:/tmp/mig_052_dryrun.sql` | 0 | 0 | — |
| `postgres:/tmp/fix_meta_counts_v2.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-45rm66xa` | 0 | 0 | — |
| `postgres:/tmp/iucore_baseline.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-vpe_ejuh` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-bon4r2fl` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-ru5yho4r` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-15c2fxuo` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-kve6g3jm` | 0 | 0 | — |
| `postgres:/tmp/031.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-hji71fdx` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-xbjt041h` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-78t8pp_b` | 0 | 0 | — |
| `postgres:/tmp/hotfix_a_trigger.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-z_uwbzmn` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-x_a0kz0r` | 0 | 0 | — |
| `postgres:/tmp/directus-pre-iucore-20260521T103010Z.dump` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-v19seey7` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-7bc6b21u` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-m14w0rgl` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-n5uaur34` | 0 | 0 | — |
| `postgres:/tmp/hotfix_b_retro.sql` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.vo3ye_dv` | 0 | 0 | — |
| `postgres:/tmp/iu_core_pre_50000x.dump` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-kje007fe` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-ozg29jrh` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-t5a3h40x` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-w4zxxa0k` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-owrd1gh1` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-e6o6kory` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-qgv1hei0` | 0 | 0 | — |
| `postgres:/tmp/baseline2.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-7pygsddg` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-ehifio51` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-l8nk_bmo` | 0 | 0 | — |
| `postgres:/tmp/b3a3_phase3.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-itwiml4g` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-3of1yh1r` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-ssevxc_q` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-ogc_k_nd` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-8cyzijx0` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-kt5kfxys` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-elq5kp56` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-qipxg4fo` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-nvaq8udk` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-z4dsx7je` | 0 | 0 | — |
| `postgres:/tmp/p10a-2a-render.sql` | 4 | 2 | `/opt/incomex/backups/dieu44_v0_3_readobs_dryrun_rerun_20260516T230306Z/prod-directus-20260516T230306Z.sql:1238075` |
| `postgres:/tmp/iucut-cli-nokbxavn` | 0 | 0 | — |
| `postgres:/tmp/280.sql` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.b79qwpzd` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-rjf__jey` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-77u4kr_l` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.i2wsh42a` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-_emsuhtm` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-3i4u9_vs` | 0 | 0 | — |
| `postgres:/tmp/predmp_iu_cut_op_pipeline_20260526_162516.dump` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-2kqckp2b` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-d0jxspfz` | 0 | 0 | — |
| `postgres:/tmp/pa_pb_gate_verify.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-m0p9cyw8` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-n7avk9sl` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-1dswismv` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-ksei5v0n` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-cixu5f7a` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-076riua_` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-_6d8xwuv` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-jk6bezkb` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-_cp2inoq` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-zxl483x3` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-o_13__8f` | 0 | 0 | — |
| `postgres:/tmp/iu25k.dump` | 0 | 0 | — |
| `postgres:/tmp/patch_and_resume.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-ok1fy0sc` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-ky84h3iw` | 0 | 0 | — |
| `postgres:/tmp/iu_core_18000x_auto_instantiate_proof.sql` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.rvwtdd75` | 0 | 0 | — |
| `postgres:/tmp/log-investigation` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-rzow98cm` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-yfomjn6t` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-ogk9o6fv` | 0 | 0 | — |
| `postgres:/tmp/proof-100000x.sql` | 0 | 0 | — |
| `postgres:/tmp/12000x_proofs.sql` | 0 | 0 | — |
| `postgres:/tmp/v1pieces.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-s5ar5nf7` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-alzzh9z1` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-2lpvfle7` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-37tjby3e` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-wqvv_dlg` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.mwg0jovj` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-temq1c09` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-3k1qcfsu` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-o8tlfhg_` | 0 | 0 | — |
| `postgres:/tmp/pivot_setup.sql` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.7_yejm5i` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-wunjjdjx` | 0 | 0 | — |
| `postgres:/tmp/280_seed.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-wj87pozi` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-wa5_djz7` | 0 | 0 | — |
| `postgres:/tmp/dieu38_mark_pieces.sql` | 0 | 0 | — |
| `postgres:/tmp/m2.sql` | 1 | 1 | `/opt/incomex/backups/dieu44_v0_3_readobs_dryrun_rerun_20260516T230306Z/prod-directus-20260516T230306Z.sql:20356` |
| `postgres:/tmp/iucut-cutplan-neg-u024zgao` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-cy6pxksd` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-ai5ixw0n` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-ba9cuv61` | 0 | 0 | — |
| `postgres:/tmp/post_dieu39_verify_mark_fix_20260527_095238.dump` | 0 | 0 | — |
| `postgres:/tmp/runtime_110.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-bshozj3y` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-4fajkl2h` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-e1z2qlgb` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-qf6qr5o3` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-1j68pgb7` | 0 | 0 | — |
| `postgres:/tmp/roles.sql` | 6 | 3 | `/opt/incomex/dot/iu-cutter/.dryrun-v0.4-2026-05-17/run_dryrun_v0_4.sh:144` |
| `postgres:/tmp/iucut-cutplan-neg-m0__9f5e` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-xjwhqvkq` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-ic1t5wfm` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-e_fn7xhp` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-as24y7uy` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-zxpkmvla` | 0 | 0 | — |
| `postgres:/tmp/iu-cutter-canon-f20c79c-20260520T040918Z` | 0 | 0 | — |
| `postgres:/tmp/pa_fix_remaining.sql` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.z3qxcpey` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-iqzcofc2` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-v_oaja5w` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-5q3zmatf` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-lhj7n483` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-wisvn_t3` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-3u1vyd7c` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-wvaavp0i` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-nyppqpyz` | 0 | 0 | — |
| `postgres:/tmp/create_approval_trigger.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-hyt5sa3w` | 0 | 0 | — |
| `postgres:/tmp/050-proof.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-7ws0ctfe` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-4q2cm5m2` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-lvsmm9ss` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.h__obrid` | 0 | 0 | — |
| `postgres:/tmp/o9-reports` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-h3lc5ghd` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-7shm1ht0` | 0 | 0 | — |
| `postgres:/tmp/p3d4c1u_step23.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-zuhs3eao` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-mb95jy1c` | 0 | 0 | — |
| `postgres:/tmp/state_probe.sql` | 7 | 4 | `/opt/incomex/backups/_phase_alpha_prod_exec_kit/run_phase_alpha_prod.sh:98` |
| `postgres:/tmp/035_auto_instantiate_log_retention_policy.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-t_xew3st` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-ctjl1yxz` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-pc47tug2` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-a5k4pjfd` | 0 | 0 | — |
| `postgres:/tmp/healthcheck_only.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-1w1wr39v` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-idklbfjb` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-sb033519` | 0 | 0 | — |
| `postgres:/tmp/claude-0` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-9yqbwkkk` | 0 | 0 | — |
| `postgres:/tmp/p3d4c1u_tests.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-3v0pb6a0` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-_bko1qej` | 0 | 0 | — |
| `postgres:/tmp/p10a-2c-render-json.sql` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.ysyc7md7` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-7hkf8mmn` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.z98gii47` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-onpoem92` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-qll4m0pf` | 0 | 0 | — |
| `postgres:/tmp/register_view_fields2.sql` | 0 | 0 | — |
| `postgres:/tmp/dot110b.sql` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.x303edzj` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-f30bcug9` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.ebds_iwc` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-gy2d_ilq` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-x_jndz8o` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-613qbm8c` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-52utoequ` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-v64serta` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-k1awfcbn` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-5a3f_tto` | 0 | 0 | — |
| `postgres:/tmp/q5.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-ev8wrmfp` | 0 | 0 | — |
| `postgres:/tmp/032_template_versioning_and_observability.sql` | 0 | 0 | — |
| `postgres:/tmp/phase_f_d30_d31.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-muksmcg5` | 0 | 0 | — |
| `postgres:/tmp/02.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-bqutck6u` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-fechcqp8` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-n_x6oavo` | 0 | 0 | — |
| `postgres:/tmp/preflight.sql` | 3 | 2 | `/opt/incomex/backups/_phase_alpha_prod_exec_kit/run_phase_alpha_prod.sh:127` |
| `postgres:/tmp/post-91000x-20260526T012335Z.dump` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-6ob7fbx2` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-6504rodp` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-b7a0purw` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a9eaacwu` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-udfijnhu` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-kvslxm3d` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-wcpc3n6h` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-fbu0thnd` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-4_36jp7v` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-gql67vif` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-em7ijerv` | 0 | 0 | — |
| `postgres:/tmp/04-author-mode-verification.sql` | 0 | 0 | — |
| `postgres:/tmp/iu-core-sandbox` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-smks4cuv` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-23qmzdgi` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-4ks4quks` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-2lqz5_5c` | 0 | 0 | — |
| `postgres:/tmp/rollback_dryrun.sql` | 0 | 0 | — |
| `postgres:/tmp/post-110500x.dump` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-x1i2iysv` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-3_yzl_lx` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-6l82rvhh` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-109vgzax` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-w1k3mx3k` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-1z4x7_vq` | 0 | 0 | — |
| `postgres:/tmp/cut_zone` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-jt_l22l6` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-fzn09fnq` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-t0xxqfmj` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-gv1s4zzo` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-3yvrrpca` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-kri38sdg` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-2528ax7f` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-ckz5tnb4` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-sxit6huy` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-wssqsqrh` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-l_82n3kj` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.0v9t2qn3` | 0 | 0 | — |
| `postgres:/tmp/v2.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-_q9azamg` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-z_kqqnax` | 0 | 0 | — |
| `postgres:/tmp/lark-gpg-home-2591244` | 0 | 0 | — |
| `postgres:/tmp/dot_scan_6000x.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-6fgvn_ty` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-6q3pozqi` | 0 | 0 | — |
| `postgres:/tmp/sync_actual.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-mycosqts` | 0 | 0 | — |
| `postgres:/tmp/systemd-private-c2f7e1f5fd3246dd926825ec5f8e2eea-systemd-resolved.service-S7cAZz` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-kituxyyc` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-o3nihodc` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-2b8bu0kn` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-24_qojz4` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-xd5u9rbz` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-1vdffedl` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-bvlqq2fe` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-zuj1h77a` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-ymo4a7ti` | 0 | 0 | — |
| `postgres:/tmp/p10b-1c` | 13 | 7 | `/opt/incomex/backups/dieu44_v0_3_readobs_dryrun_rerun_20260516T230306Z/prod-directus-20260516T230306Z.sql:1238115` |
| `postgres:/tmp/r280.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-l_auu3u0` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-h3y2xtam` | 0 | 0 | — |
| `postgres:/tmp/iucore_schema.sql` | 0 | 0 | — |
| `postgres:/tmp/species_pivot3.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-0cl10nxx` | 0 | 0 | — |
| `postgres:/tmp/032_apply.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-l9mus37q` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-vil0h3hy` | 0 | 0 | — |
| `postgres:/tmp/baseline.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-jd37fsvc` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-2dkz348z` | 0 | 0 | — |
| `postgres:/tmp/110.sql` | 0 | 0 | — |
| `postgres:/tmp/q4.sql` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.i2uu_w47` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-mkyv6yug` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-qu3jig7q` | 0 | 0 | — |
| `postgres:/tmp/b3a1b_seed.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-o7i6onec` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-vww8ul4g` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-6ot1ixip` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-bluk3kv1` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-rgqceqf6` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-l60sdok7` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-43dl510h` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-dhu8474y` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-h5ezugnv` | 0 | 0 | — |
| `postgres:/tmp/hc-trigger-new.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-u6x21nk8` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-_w47k633` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-_5ufzzmx` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-wdds14dt` | 0 | 0 | — |
| `postgres:/tmp/preflight3.sql` | 0 | 0 | — |
| `postgres:/tmp/p10d-output` | 7 | 7 | `/opt/incomex/backups/dieu44_v0_3_readobs_dryrun_rerun_20260516T230306Z/prod-directus-20260516T230306Z.sql:1238243` |
| `postgres:/tmp/iucut-cutwrite-neg-z1p9bywh` | 0 | 0 | — |
| `postgres:/tmp/dump_op_fns.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-l2bo3_qj` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-02_dboxw` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-u5cigeyg` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-pupod_ks` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-xm_bdlk2` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-7rawusl1` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-8g3ndtri` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-p0auw9ld` | 0 | 0 | — |
| `postgres:/tmp/027_piece_split_primitive.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-054_c615` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-p37bvws2` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-wumbrrvy` | 0 | 0 | — |
| `postgres:/tmp/fix21-refs` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-pngq21dm` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-ux1o2ozr` | 0 | 0 | — |
| `postgres:/tmp/mig_052.sql` | 0 | 0 | — |
| `postgres:/tmp/m3b_fields.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-c33l7_kf` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-d4swjzkv` | 0 | 0 | — |
| `postgres:/tmp/03-dieu43-v1-2-extensions.sql` | 8 | 0 | `/opt/incomex/backups/dieu44_v0_3_readobs_dryrun_rerun_20260516T230306Z/prod-directus-20260516T230306Z.sql:1237574` |
| `postgres:/tmp/iucut-prod-rljqfodr` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-7uwiskcc` | 0 | 0 | — |
| `postgres:/tmp/01-dieu43-block1-schema.sql` | 11 | 0 | `/opt/incomex/data/workspace-tools/results/7626b8f084ad402b9a1dce6fb3a38005:1` |
| `postgres:/tmp/iucut-cli-jeaqo6u8` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-29akalv6` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-7almi7vq` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-forrj3pz` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-d0kleuv0` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-pq2vivyf` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-q1u7ezdg` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-wjic2bop` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-o0_5b0rg` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-83u6jjp5` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-ptoanq00` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-snyloi5y` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-ddvamqxr` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-jrrthvyo` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-y6h0vwch` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-2mt94f96` | 0 | 0 | — |
| `postgres:/tmp/post-iucore-18000x.dump` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-xmz8etok` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-0iexw40n` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-ugn46cal` | 0 | 0 | — |
| `postgres:/tmp/etr_cols.sql` | 0 | 0 | — |
| `postgres:/tmp/preflight_d1.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-emlqmltn` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-foqwb6ku` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-iv6ctufg` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-ksb12vte` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-isnf4qjt` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-jquoqq3v` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-8g2xqumj` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-t_ns8zdn` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-lz6drc35` | 0 | 0 | — |
| `postgres:/tmp/dieu45_phase2_mig_051.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-twp2_kuh` | 0 | 0 | — |
| `postgres:/tmp/f.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-oar5k10e` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.z1y9yvlf` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-b301tfla` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-v6f7p6k9` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-evsu8qk0` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-ofjog0sp` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests._54xi2av` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-40yvq3gy` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-4i8tt8ao` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-bxn72bfp` | 0 | 0 | — |
| `postgres:/tmp/systemd-private-c2f7e1f5fd3246dd926825ec5f8e2eea-systemd-timesyncd.service-eP9nlu` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-cq8_54o2` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-_f9mxzt9` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-jxdnx5kb` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-krwocm5m` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-i_o63_e9` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-er_80h3l` | 0 | 0 | — |
| `postgres:/tmp/fix_refresh_fn2.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-kd1h800m` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-8ngxn032` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-6abldyue` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-bhsoymz2` | 0 | 0 | — |
| `postgres:/tmp/verify_alpha.sql` | 7 | 3 | `/opt/incomex/backups/_phase_alpha_prod_exec_kit/run_phase_alpha_prod.sh:170` |
| `postgres:/tmp/kilo` | 7 | 0 | `/opt/incomex/data/workspace-tools/results/b9ed162f85fb46cfb75572ae7aa9bb1c:1` |
| `postgres:/tmp/iucut-legA-ezhzmzbh` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-3rmra9yn` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-3rdnk6be` | 0 | 0 | — |
| `postgres:/tmp/reg056.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-38omz8_7` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-6tii1nlc` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-qp35kj7c` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-9sd9w2xa` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-suro_rx0` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-2n1lvcg0` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-9b7ezc_a` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-9w4vy06f` | 0 | 0 | — |
| `postgres:/tmp/regression.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-ps1n3n8w` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-gysahdv8` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-epn73wex` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-anpq7h76` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-b6dzcus7` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-5630w7io` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-95s9t6tr` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-p3k10yph` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.v9mouydm` | 0 | 0 | — |
| `postgres:/tmp/runtime_340.sql` | 0 | 0 | — |
| `postgres:/tmp/g6_artifacts_run2` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-8ftbamnx` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-cqubmyyp` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-w252u0_6` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-usmg38kw` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-mkszgcb3` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-m8_7mbl2` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-1kf0qpv2` | 0 | 0 | — |
| `postgres:/tmp/ro_test.sql` | 0 | 0 | — |
| `postgres:/tmp/p1_inspect.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-6a2khyop` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-nz_da9zl` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-anh6jp0x` | 0 | 0 | — |
| `postgres:/tmp/sb150.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-hwapeayr` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-1lk98vf5` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-4ol2qkf4` | 0 | 0 | — |
| `postgres:/tmp/s170c_pivot_query.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-0wf9qv9p` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-5z1rmlyx` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-39fg6fru` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-2oxcjlj8` | 0 | 0 | — |
| `postgres:/tmp/dieu43-phase15` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-v8hgyi5s` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-1hhtd4fl` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-kb0hpzb5` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-rg3k4r6z` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-8hcf_5gt` | 0 | 0 | — |
| `postgres:/tmp/m3a_lifecycle_retry_preddl_20260520T080709Z.dump` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-dfwdrpvv` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-9kz2fr6d` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-kwglxm9r` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-h14mi1qw` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-95a93677` | 0 | 0 | — |
| `postgres:/tmp/029_piece_event_runtime_substrate.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-d6mftg5k` | 0 | 0 | — |
| `postgres:/tmp/dot110.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-3z65kv8w` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-xtufac37` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.rh54hctn` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-0fvwdj1k` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests._tqjd1m7` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-kuvhhjwu` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-e220lduc` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-uaedbpb1` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-2ey72gcb` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-8k1obsxn` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-o85avvy8` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-km4dtue3` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-sjkjeb8r` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-ku_vrfq2` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-f08f71k0` | 0 | 0 | — |
| `postgres:/tmp/discover.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-el8diiml` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-49ry2iib` | 0 | 0 | — |
| `postgres:/tmp/retro.sql` | 0 | 0 | — |
| `postgres:/tmp/v6-delta.sql` | 1 | 1 | `/opt/incomex/backups/dieu44_v0_3_readobs_dryrun_rerun_20260516T230306Z/prod-directus-20260516T230306Z.sql:1238946` |
| `postgres:/tmp/iucut-cli-2fwpybym` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-hi_wr0ju` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-4gmjt_5x` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-4b27n8er` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-idioj13f` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-qvp3si0h` | 0 | 0 | — |
| `postgres:/tmp/systemd-private-c2f7e1f5fd3246dd926825ec5f8e2eea-lark-mcp-remote.service-1YzHbb` | 0 | 0 | — |
| `postgres:/tmp/o8e` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-38_7vfw2` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-e5fe437w` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-bu6d4479` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-_dg0kkdp` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-8533y8i2` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-z98hlcro` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-gius5g48` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-ddjiaqwi` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-04_dl0qh` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-e99i8b75` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-i0pfewq3` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-9a7hyai_` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-q6yqrt1d` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-l4riwuqv` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-smghc_i_` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-bdycie8d` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-k4e5t_jt` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-02u6oql3` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-q4eeh_98` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-ql_y4g6h` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-11lo04dy` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-qcr9sle7` | 0 | 0 | — |
| `postgres:/tmp/g6_run_20260427_104428` | 3 | 3 | `/opt/incomex/backups/dieu44_v0_3_readobs_dryrun_rerun_20260516T230306Z/prod-directus-20260516T230306Z.sql:1237900` |
| `postgres:/tmp/iucut-cutwrite-neg-s4j23ooi` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-ecddhxq7` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-kg42n9fr` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-9ic7po35` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-szbay0bz` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-yydmku_c` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-o4bvv4l4` | 0 | 0 | — |
| `postgres:/tmp/probe_dump_1779812405.dump` | 0 | 0 | — |
| `postgres:/tmp/d36_macroA_migration.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-w_c7emkr` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-afwjkbd7` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.u0j0ohsy` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-bbvjyglg` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-tcen_uel` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-pbkt4dso` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-g0f5q01s` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-n9j4tp96` | 0 | 0 | — |
| `postgres:/tmp/fns.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-5eg5a6cv` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-03qlmqz3` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-3n_lnx53` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-8kof_skv` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-0h6fvg5g` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-5_tycez2` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.8qfhp_pq` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-z_pryd0n` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-h9o94ofz` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-arnfd5xg` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-i4wwfqsx` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-kxfbw332` | 0 | 0 | — |
| `postgres:/tmp/phase_f_regression.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-xxx4lt91` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-zpuqdyzz` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.xk8_bebt` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-wuzwugcx` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-1vaf6kg7` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-fxhwj9fo` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-ywiixtg2` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-eszcmzgj` | 0 | 0 | — |
| `postgres:/tmp/d9.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-a5ua6ulf` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-i7q77xox` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-lzxj1je4` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-hhoct78y` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-d1hrkxfk` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-8ma27phy` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-h39idjff` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-41z0ura3` | 0 | 0 | — |
| `postgres:/tmp/260_piece_split_primitive_probe.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-orgvpfau` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-w6e7oowc` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-avxfv95u` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-0rnxzc8v` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-zzyh7ibe` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-3qtrw1h8` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-ukjsbtf4` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-ez75nkh3` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-2h_fmeq_` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-xr9j_5xx` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-rwzbgm7u` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-pbhg3qew` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-g0nqpdfo` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-mdjwmv8o` | 0 | 0 | — |
| `postgres:/tmp/d1_analyze.sql` | 0 | 0 | — |
| `postgres:/tmp/g6_artifacts` | 23 | 0 | `/opt/incomex/backups/dieu44_v0_3_readobs_dryrun_rerun_20260516T230306Z/prod-directus-20260516T230306Z.sql:1237917` |
| `postgres:/tmp/iucut-cutplan-6b7tejzq` | 0 | 0 | — |
| `postgres:/tmp/lark-gpg-home-3369664` | 0 | 0 | — |
| `postgres:/tmp/iucore_ret2.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-8hzrvh5v` | 0 | 0 | — |
| `postgres:/tmp/p3d-vector-hardening-backup-20260511-050538` | 4 | 4 | `/opt/incomex/backups/dieu44_v0_3_readobs_dryrun_rerun_20260516T230306Z/prod-directus-20260516T230306Z.sql:1238912` |
| `postgres:/tmp/iucut-legA-u4ythg41` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-z5_wra0v` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-6yw57r29` | 0 | 0 | — |
| `postgres:/tmp/role_chk.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-5tb006f1` | 0 | 0 | — |
| `postgres:/tmp/register_task_tools.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-e6tix4yw` | 0 | 0 | — |
| `postgres:/tmp/dieu45_phase3` | 7 | 0 | `/opt/incomex/mcp-roots/gh/work/vps-clean-20-9-26/BAO-CAO.md:224` |
| `postgres:/tmp/iucut-cutwrite-6gfp98x_` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-bxd1e0l6` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-wqc4gmgr` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-3gtx1g2t` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-cup_ueff` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-vfooj6p3` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-rfr_rx3v` | 0 | 0 | — |
| `postgres:/tmp/systemd-private-c2f7e1f5fd3246dd926825ec5f8e2eea-ModemManager.service-E0FAGf` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-jww59vrv` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-5zxqp03d` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-rivxst63` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-y2mqlgc6` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-2a9q73ll` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-rau8fgb7` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-t9x7b_pm` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-3vin1lel` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.cn6rwljd` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-r5wdyy1q` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-wc_fehzu` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-gancmxjb` | 0 | 0 | — |
| `postgres:/tmp/d28-gmr-output-1778407785` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-z009s5d0` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-yc0xz07j` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-e0pzbj0_` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-7d1pti_c` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-xwdml8rc` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-h9iy1tyh` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-kwlqta2u` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-_avuuadc` | 0 | 0 | — |
| `postgres:/tmp/04-dieu43-v1-2-role-fdw-trigger.sql` | 6 | 0 | `/opt/incomex/backups/dieu44_v0_3_readobs_dryrun_rerun_20260516T230306Z/prod-directus-20260516T230306Z.sql:1237575` |
| `postgres:/tmp/028_piece_merge_primitive.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-44gdrdno` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-akr4vg29` | 0 | 0 | — |
| `postgres:/tmp/s178_fix17.sql` | 0 | 0 | — |
| `postgres:/tmp/clone_finalized_2026-06-03.dump` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-6g29kqn7` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-_4b0ph43` | 0 | 0 | — |
| `postgres:/tmp/12000x_phase_G_proof.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-pzrqnv_g` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-q9kepvna` | 0 | 0 | — |
| `postgres:/tmp/lark-test-audit` | 2 | 2 | `/opt/incomex/lark-client/tests/test_cli_records.py:103` |
| `postgres:/tmp/pb_fix_verify.sql` | 0 | 0 | — |
| `postgres:/tmp/b3f1b_exec.sql` | 5 | 5 | `/opt/incomex/logs/b3f1b-soft-gate-exec-20260513T030315Z.log:5` |
| `postgres:/tmp/iucut-legA-nydqsk6s` | 0 | 0 | — |
| `postgres:/tmp/pa_step9_13.sql` | 0 | 0 | — |
| `postgres:/tmp/d43-artifacts` | 1 | 1 | `/opt/incomex/backups/dieu44_v0_3_readobs_dryrun_rerun_20260516T230306Z/prod-directus-20260516T230306Z.sql:1237604` |
| `postgres:/tmp/iucut-legA-_1m5l997` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-ai538hk3` | 0 | 0 | — |
| `postgres:/tmp/06-dieu43-v1-2-schema-migrate.sql` | 5 | 0 | `/opt/incomex/backups/dieu44_v0_3_readobs_dryrun_rerun_20260516T230306Z/prod-directus-20260516T230306Z.sql:1237578` |
| `postgres:/tmp/iucut-cutwrite-neg-783g2m64` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-r7dclcj6` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-_chj0mkl` | 0 | 0 | — |
| `postgres:/tmp/iucore_directus_verify.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-akhtiacd` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-wjxcjmzm` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-d6r3pl4t` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-0pjob4am` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-juxxsdj0` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-cz82cpyc` | 0 | 0 | — |
| `postgres:/tmp/meta_5.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-yfsdbqb4` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.1dripl15` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.b5wx40xp` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-2dzsuiov` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-dmaz910l` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-v2zm3ps7` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-gc2he0gh` | 0 | 0 | — |
| `postgres:/tmp/pytest-of-root` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-lxagad5k` | 0 | 0 | — |
| `postgres:/tmp/run_pilot.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-b36knp8r` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-9glxhze1` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-b7e5u37w` | 0 | 0 | — |
| `postgres:/tmp/dump_cut_chain.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-v30i9pjm` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-devqvpdg` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.j996yqh_` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-ck6iy_8z` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-wedtvtvo` | 0 | 0 | — |
| `postgres:/tmp/etr_sample.sql` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.1b80vy07` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-e079tzzz` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-lmg3krk1` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-qmms17mq` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-88nl68tv` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-ump50hdc` | 0 | 0 | — |
| `postgres:/tmp/290_template_versioning_probe.sql` | 0 | 0 | — |
| `postgres:/tmp/auto_refresh_pilot_6000x.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-hpyzuk2k` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-sd713jbn` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a5r_17hf` | 0 | 0 | — |
| `postgres:/tmp/systemd-private-c2f7e1f5fd3246dd926825ec5f8e2eea-systemd-logind.service-eWC9Pt` | 0 | 0 | — |
| `postgres:/tmp/create_fresh_tables.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-82ugcxui` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-j5zwbolg` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-502uio0q` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-hb1j9nx7` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-y8tpjzgn` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-sly1d9hk` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-usc3pxq6` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.k0ju32wn` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-wfzv8umx` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-9_zy5qxf` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-vf35ypfc` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-ydmsjwen` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-h8rwyrsh` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-feuh5xyi` | 0 | 0 | — |
| `postgres:/tmp/t1.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-w3hbbtkh` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-w90ym7k6` | 0 | 0 | — |
| `postgres:/tmp/c1_snapshot.sql` | 1 | 1 | `/opt/incomex/data/workspace-tools/results/0d9563bf78354e0d8d20e0d19adbc0f1:1` |
| `postgres:/tmp/iucut-legA-14mmd0t7` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-faflbe3s` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-sxvyvqdn` | 0 | 0 | — |
| `postgres:/tmp/healthcheck.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-7f39lu8h` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-543q9yb2` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-4_v1x70l` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-cined0_3` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-w4vxjn6p` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-u9fk2yf1` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-sg95x4tj` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-tv_ydlib` | 0 | 0 | — |
| `postgres:/tmp/pre_dieu39_unit_kind_fix_20260527.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-n2005f7h` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-z7__j1pa` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-5f2apc12` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-8o0zamh0` | 0 | 0 | — |
| `postgres:/tmp/220_three_axis_envelope_auto_refresh_probe.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-dfwj2hr6` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-t17jy5zy` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-97ua_3e6` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-s3_mo_xg` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-l90pnc_f` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-jsxbjmt6` | 0 | 0 | — |
| `postgres:/tmp/meta_pivot_results.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-fssktu1k` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-1yn_w_nh` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-p190yijg` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-1xv0ziya` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-jxf2482u` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-h8okj6ji` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-8avkp99i` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-ipc9drop` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-wk_h2hv1` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-3vntzfnl` | 0 | 0 | — |
| `postgres:/tmp/07-dieu43-v1-2-fdw-optimize.sql` | 9 | 0 | `/opt/incomex/backups/dieu44_v0_3_readobs_dryrun_rerun_20260516T230306Z/prod-directus-20260516T230306Z.sql:1237579` |
| `postgres:/tmp/iucut-cli-fc8s34vq` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-n777qmd9` | 0 | 0 | — |
| `postgres:/tmp/prod_cg.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-7ta04ome` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-717ojee1` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-ic_igmwv` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-45mi2q15` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-iv1vfrje` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-gjiviijp` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-yihjmaz_` | 0 | 0 | — |
| `postgres:/tmp/032_template_versioning_and_observability.rollback.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-7ou8kb1z` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-iu3ie65z` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-3bt5ll4p` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-_vc8b_z9` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-h75eb_ft` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-emnr5pff` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-ik5bhqr1` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-k8ewagkc` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-96pr_565` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-86i4rlnp` | 0 | 0 | — |
| `postgres:/tmp/directus-pre-10000x-20260524T125703Z.dump` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-cdcm4b5s` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-pg2d1zti` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-h4j9l4np` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-ec_s3a5o` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-2wdxfrj9` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-647214u1` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-xejen_8s` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-4k7g2fb1` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-_7m_d9zo` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-nef67p5i` | 0 | 0 | — |
| `postgres:/tmp/iu_core_18000x_mutation_invariant_proof.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-5v6tsxqq` | 0 | 0 | — |
| `postgres:/tmp/phase123.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-90lgw5il` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-tvgc7euy` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-nq3ilrfy` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-w5g474yy` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-j_dlqmqx` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-xih6s0fj` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-vlpylnmc` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-w0lmwq2y` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-ser910_m` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-x0gq1lei` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-0odo018q` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.z3ydqqn4` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-fruwcntj` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-gt9xh7a3` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-b0_8fvl0` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-v8gm02vp` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-62fhlbkt` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-670melkm` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-g7106d6n` | 0 | 0 | — |
| `postgres:/tmp/p10b-2c` | 16 | 12 | `/opt/incomex/backups/dieu44_v0_3_readobs_dryrun_rerun_20260516T230306Z/prod-directus-20260516T230306Z.sql:1238137` |
| `postgres:/tmp/fix21-docs` | 5 | 4 | `/opt/incomex/exports/laws-new-mirror/reports/rs3c/01-source-access-recovery-proof-2026-06-21.md:35` |
| `postgres:/tmp/iucut-cli-t1s823w_` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.b39wshoq` | 0 | 0 | — |
| `postgres:/tmp/02b_observation_rollback.sql` | 0 | 0 | — |
| `postgres:/tmp/project_map.sql` | 4 | 0 | `/opt/incomex/data/workspace-tools/results/6ab21fbfccfc4c1b9c1800df5110af02:1` |
| `postgres:/tmp/iucut-prod-54k77mvq` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-gqr669bp` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-nvgg27z9` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-sunlxta1` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-9la8xy8d` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-uwm868ay` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-yzqdudo6` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-tn_ggq1g` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-wj4xfkwo` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.21somt3k` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-33i7b0w3` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-r8h8v_hp` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-5rh039sa` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-zzpa4hdc` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-o9gtlbfz` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-9t14fbee` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-esn2k6fl` | 0 | 0 | — |
| `postgres:/tmp/register_view_fields3.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-d61yo7eu` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-w4c123xb` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-5hk5o9bb` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-3fzi8ypk` | 0 | 0 | — |
| `postgres:/tmp/sb170.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-rl7txr6t` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-8psi1xol` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-1bmz9m4n` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-2eh387ce` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-9p7_szid` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.j958ivok` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-4ovlo5np` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-z84pxert` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-p1j_hooz` | 0 | 0 | — |
| `postgres:/tmp/iu25k_post.dump` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-nhcus5yy` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-kzuxegnu` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.kn242h0z` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-15burv3i` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-ynq_4a5k` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-ayk06fi1` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-mct_6yg6` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-2zy9r759` | 0 | 0 | — |
| `postgres:/tmp/batch_meta_catalog_v2.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-39eb4z_z` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-ct2wpkbg` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-v7ssjvlc` | 0 | 0 | — |
| `postgres:/tmp/prod_counts.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-z7vxj4op` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-llhljyc5` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-iz5reik5` | 0 | 0 | — |
| `postgres:/tmp/step4.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-aa8ed3b1` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-csw2ys78` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-baitlbvj` | 0 | 0 | — |
| `postgres:/tmp/backfill_dot_desc.sql` | 0 | 0 | — |
| `postgres:/tmp/fix_consistency.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-7ci2cpf1` | 0 | 0 | — |
| `postgres:/tmp/set_perms.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-eexchm6z` | 0 | 0 | — |
| `postgres:/tmp/test-validate-wrap.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-2uigdngc` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-7lji0fx9` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-9nd5prqf` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-4xozyi70` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-_3qpvd85` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-dj963hbm` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-16ju_jgd` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-9qt3hu2q` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-_no8ckxv` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-762g2nbl` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-3c9pq4i8` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-k5h0z80y` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-8d3o7a1y` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-a4mqy4qs` | 0 | 0 | — |
| `postgres:/tmp/cp-sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-nznehe0o` | 0 | 0 | — |
| `postgres:/tmp/pa_migration.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-b2cc9rvd` | 0 | 0 | — |
| `postgres:/tmp/p3d-vector-search-boost-backup-20260511-093334` | 2 | 2 | `/opt/incomex/backups/dieu44_v0_3_readobs_dryrun_rerun_20260516T230306Z/prod-directus-20260516T230306Z.sql:1238902` |
| `postgres:/tmp/iucut-prod-a-usldfp07` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-sbe4k527` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-q6z3d9vv` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-gk4n27bz` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-7wj48so4` | 0 | 0 | — |
| `postgres:/tmp/retention_dryrun.sql` | 0 | 0 | — |
| `postgres:/tmp/b3a3_list.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-uu5uc2pw` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-m4qqmljp` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-9_excom8` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-jegsfulh` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-_pom8nsa` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-qe9s3t_7` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-hw2vxzfl` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-y9i8dqmw` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.08_p9xg6` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-jvxny7_j` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-84bb5oq8` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.5w2o_3jn` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-z1_1djaz` | 0 | 0 | — |
| `postgres:/tmp/c1_introspect.sql` | 1 | 1 | `/opt/incomex/data/workspace-tools/results/0d9563bf78354e0d8d20e0d19adbc0f1:1` |
| `postgres:/tmp/batch_meta_catalog.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-k74r89ap` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-n62x_21q` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-3ieic8v1` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-rycainll` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-gjnqdlmw` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-5nhle1do` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.vvn2zue_` | 0 | 0 | — |
| `postgres:/tmp/dieu43-phase1` | 3 | 3 | `/opt/incomex/backups/dieu44_v0_3_readobs_dryrun_rerun_20260516T230306Z/prod-directus-20260516T230306Z.sql:1237559` |
| `postgres:/tmp/iucut-cli-jeyqncv3` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-lzqbkec6` | 0 | 0 | — |
| `postgres:/tmp/pre-ogv-p0.dump` | 0 | 0 | — |
| `postgres:/tmp/iucore_dot.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-3vszxxvz` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.b6rdnpqu` | 0 | 0 | — |
| `postgres:/tmp/s164_register.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-tklzuejj` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-0cca7pu7` | 0 | 0 | — |
| `postgres:/tmp/health-h11-description-coverage.sql` | 4 | 0 | `/opt/incomex/data/workspace-tools/results/6ab21fbfccfc4c1b9c1800df5110af02:1` |
| `postgres:/tmp/iucut-prod-oqbx3vu4` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-0l38i3fw` | 0 | 0 | — |
| `postgres:/tmp/lineage_cols.sql` | 0 | 0 | — |
| `postgres:/tmp/d30_d31_suite.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-815necnl` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-35dlnxmd` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-nkhcgifj` | 0 | 0 | — |
| `postgres:/tmp/iu_onboard_9000x` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-4kfd4d1e` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-4lzikz0r` | 0 | 0 | — |
| `postgres:/tmp/probe.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-2p_7rraw` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-ytqgmacj` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-ikcvhemx` | 0 | 0 | — |
| `postgres:/tmp/05-dieu43-v1-2-rev3-alter-check.sql` | 5 | 0 | `/opt/incomex/backups/dieu44_v0_3_readobs_dryrun_rerun_20260516T230306Z/prod-directus-20260516T230306Z.sql:1237577` |
| `postgres:/tmp/iucut-legA-xot1xx00` | 0 | 0 | — |
| `postgres:/tmp/b3a3_install.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-xix6tw90` | 0 | 0 | — |
| `postgres:/tmp/qt.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-oxp2bo_n` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-3mvicwf4` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-yqp7fty6` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-thgoh32_` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-kanrmro2` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-g4l9yqhp` | 0 | 0 | — |
| `postgres:/tmp/pg_dump_post_mig055_20260527T044228Z.dump` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-hf78j5cu` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-k6ztf92x` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-r14xbk0r` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-oxvm2t7i` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-e6ro42nj` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.qx0n1igu` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-ps4e09en` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-fflcl275` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-g2zbttg8` | 0 | 0 | — |
| `postgres:/tmp/m3b_fields_cleanup.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-fok75ivx` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-non93yet` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests._9afre4d` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-qby96bmn` | 0 | 0 | — |
| `postgres:/tmp/register_dot_batch.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-54xvdckt` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-ddzvhlus` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-0nvzhkoc` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-kfw04wx9` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-_1jtelf5` | 0 | 0 | — |
| `postgres:/tmp/real_corpus_pilot_6000x.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-k2ismnuh` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-3k_brwj2` | 0 | 0 | — |
| `postgres:/tmp/270_piece_merge_primitive_probe.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-yq70fubn` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-kui8fgqv` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-e9zch0fa` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-w_dxtlj_` | 0 | 0 | — |
| `postgres:/tmp/q6.sql` | 0 | 0 | — |
| `postgres:/tmp/lark-test-audit-b4` | 1 | 1 | `/opt/incomex/lark-client/tests/test_cli_records.py:233` |
| `postgres:/tmp/iucut-cutwrite-neg-jxa1gfmg` | 0 | 0 | — |
| `postgres:/tmp/iucore_reverify.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-nt3p9ko2` | 0 | 0 | — |
| `postgres:/tmp/desc-autogen-engine.sql` | 1 | 0 | `/opt/incomex/backups/dieu44_v0_3_readobs_dryrun_rerun_20260516T230306Z/prod-directus-20260516T230306Z.sql:1237592` |
| `postgres:/tmp/iucut-cutplan-neg-3mqfyoeg` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-jppz29w9` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-5xzhs2ew` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-b1iwv3su` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.m2ueve7k` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-2pa4b2wz` | 0 | 0 | — |
| `postgres:/tmp/PD_RUNTIME_OBS_FULL_ROLLBACK.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-e1jjjd6a` | 0 | 0 | — |
| `postgres:/tmp/00-prereq-dot-operations.sql` | 8 | 0 | `/opt/incomex/data/workspace-tools/results/7626b8f084ad402b9a1dce6fb3a38005:1` |
| `postgres:/tmp/neg.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-k48zz1tp` | 0 | 0 | — |
| `postgres:/tmp/codex-v6-kb` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-zqyilyia` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-4eauci4g` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.nbb57c_a` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-en291nle` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-54s2wox_` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-cmvcegyl` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-f1bshybw` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-q7wrnn9z` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-udcgb8ka` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-tx3cb23u` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-c1m6zgm3` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-72hflxa8` | 0 | 0 | — |
| `postgres:/tmp/tmux-0` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-fy0y_pxj` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-2nyqqkq4` | 0 | 0 | — |
| `postgres:/tmp/final_snapshot.sql` | 0 | 0 | — |
| `postgres:/tmp/event_boundary_probe.sql` | 0 | 0 | — |
| `postgres:/tmp/sandbox_230.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-icp6ugpy` | 0 | 0 | — |
| `postgres:/tmp/01.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-vr7vd886` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-_svr6nfg` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-bcv28bx7` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-warp7c_4` | 0 | 0 | — |
| `postgres:/tmp/baseline5.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-1k_33tkc` | 0 | 0 | — |
| `postgres:/tmp/reg_dot152.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-27ysbr78` | 0 | 0 | — |
| `postgres:/tmp/proof.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-wtw_r1dr` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-vjxb3nvl` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-3s24geej` | 0 | 0 | — |
| `postgres:/tmp/species_pivot.sql` | 0 | 0 | — |
| `postgres:/tmp/p1_install.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-2mffqfus` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-5f6wanb8` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-p85v5ro9` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-1bz4xbvw` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-00ccqd41` | 0 | 0 | — |
| `postgres:/tmp/cf.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-s8mux2ao` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-xog0_zzh` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-yh2j0bix` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-5jvhz6av` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-bu5g6ppn` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-n8graiwd` | 0 | 0 | — |
| `postgres:/tmp/mark_5_applied.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-szc35q1c` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-4zhoq5aa` | 0 | 0 | — |
| `postgres:/tmp/023_three_axis_envelope_auto_refresh_hook.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-a4aepqpf` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-pi3g694o` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-9iiavr8j` | 0 | 0 | — |
| `postgres:/tmp/schema.sql` | 1 | 1 | `/opt/incomex/backups/dieu44_v0_3_readobs_dryrun_rerun_20260516T230306Z/prod-directus-20260516T230306Z.sql:1239582` |
| `postgres:/tmp/iucut-prod-x6vsz3zc` | 0 | 0 | — |
| `postgres:/tmp/280_operator_runtime_catalog_seed.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-d7b9vr6i` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-xad9i906` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-n6cbj76b` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-5r3dljo4` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-gbafr1py` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-rkt5t52k` | 0 | 0 | — |
| `postgres:/tmp/proof_dieu37.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-rv43wdo0` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-2ake1jui` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-_h42clk0` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-og0x2nhv` | 0 | 0 | — |
| `postgres:/tmp/q7.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-cnq6enkw` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-pp5gldkw` | 0 | 0 | — |
| `postgres:/tmp/12000x_phase_D_workflow_proof.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-rnm6dmee` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-soimxl6m` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-s3kcf_o0` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-ak35yiaf` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-j0mkaq__` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-sq3gu_q_` | 0 | 0 | — |
| `postgres:/tmp/mig_054_dieu39_verify_mark_root_cause_fix.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-88k1l8pr` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-kf_sbbiz` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-u5cuayen` | 0 | 0 | — |
| `postgres:/tmp/systemd-private-c2f7e1f5fd3246dd926825ec5f8e2eea-fwupd.service-mk9chp` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-18dszhnc` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-p2y4mbx5` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-ywlqme8m` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-x08wwh8e` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-it9zx3nb` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-e7es_9xj` | 0 | 0 | — |
| `postgres:/tmp/tmp.NEAEgbEdbO` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-clyf90dr` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-3dvu8tlb` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-30bs205j` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-_gyrhg07` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-dakeaoup` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-8_ilo8qh` | 0 | 0 | — |
| `postgres:/tmp/fn_kb_notify_vector_sync.new.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-yjxjky1a` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-9q2m9g2g` | 0 | 0 | — |
| `postgres:/tmp/scaleout_verify.sql` | 0 | 0 | — |
| `postgres:/tmp/log.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-m2pnl3ey` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-cyqft_0h` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-_2b2uayn` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-8xxo4ei7` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-1kt8kcq_` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-jpr8zyem` | 0 | 0 | — |
| `postgres:/tmp/25k_phaseC2.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-xu4bonzd` | 0 | 0 | — |
| `postgres:/tmp/insert_cat.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-yay48ook` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.00v5fq01` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-_lq87ji5` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-fxypgkfx` | 0 | 0 | — |
| `postgres:/tmp/m3a_lifecycle_preddl_20260520T074811Z.dump` | 0 | 0 | — |
| `postgres:/tmp/auto.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-itevp7a8` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-hbv_mc93` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-48c7ovlh` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-m8_3nrmt` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-zbeh34nt` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-egb6lrg5` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-deuacbb6` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-5hs8qj5f` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-69vpepf5` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-wrv0ngm0` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-uso1o_ro` | 0 | 0 | — |
| `postgres:/tmp/02b_observation_substrate_v2.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-papld6zb` | 0 | 0 | — |
| `postgres:/tmp/canon-adapter-tests.w3cr4_2r` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-uzsfvtje` | 0 | 0 | — |
| `postgres:/tmp/290.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-arm69bjz` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-2grasjnq` | 0 | 0 | — |
| `postgres:/tmp/g6_artifacts_run3` | 0 | 0 | — |
| `postgres:/tmp/d36_macroA_proofs.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-c8iznree` | 0 | 0 | — |
| `postgres:/tmp/d28-gmr-output-1778407748` | 1 | 1 | `/opt/incomex/backups/dieu44_v0_3_readobs_dryrun_rerun_20260516T230306Z/prod-directus-20260516T230306Z.sql:1238855` |
| `postgres:/tmp/sb190.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-5qpvl0kj` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-gqw0a5u9` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-up7ot023` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-ptswtfui` | 0 | 0 | — |
| `postgres:/tmp/iucut-prod-a-f0h1gaj2` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-ryyzf07g` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-o5_edt3f` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutplan-neg-lvxx0p8r` | 0 | 0 | — |
| `postgres:/tmp/iucut-cli-0hg0dr86` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-gqg49vem` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-hj0vy7jl` | 0 | 0 | — |
| `postgres:/tmp/iucut-legA-mms3shsi` | 0 | 0 | — |
| `postgres:/tmp/v.sql` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-3oacuu10` | 0 | 0 | — |
| `postgres:/tmp/iucut-cutwrite-neg-0t9im_qf` | 0 | 0 | — |

#### N11 — kết quả theo từng tên

| Target | Khớp tên/path | Khớp full path | Vị trí đối chứng |
|---|---:|---:|---|
| `/opt/incomex/backups/directus-pre-iucore-120x-20260522T065235Z.dump` | 0 | 0 | — |
| `/opt/incomex/backups/directus-pre-iucore-1500x-20260523T025705Z.dump` | 0 | 0 | — |
| `/opt/incomex/backups/directus-pre-iucore-1500x-20260523T025723Z.dump` | 0 | 0 | — |
| `/opt/incomex/backups/directus-pre-iucore-1k-20260522T142308Z.dump` | 0 | 0 | — |
| `/opt/incomex/backups/directus-pre-iucore-1kplus-20260523T021535Z.dump` | 0 | 0 | — |
| `/opt/incomex/backups/directus-pre-iucore-2000x-20260523T033615Z.dump` | 0 | 0 | — |
| `/opt/incomex/backups/directus-pre-iucore-2400x-20260523T061016Z.dump` | 0 | 0 | — |
| `/opt/incomex/backups/directus-pre-iucore-240x-20260522T072323Z.dump` | 0 | 0 | — |
| `/opt/incomex/backups/directus-pre-iucore-3000x-20260523T071027Z.dump` | 0 | 0 | — |
| `/opt/incomex/backups/directus-pre-iucore-30x-20260522T023541Z.dump` | 0 | 0 | — |
| `/opt/incomex/backups/directus-pre-iucore-4000x-20260523T084654Z.dump` | 0 | 0 | — |
| `/opt/incomex/backups/directus-pre-iucore-5000x-20260523T093747Z.dump` | 0 | 0 | — |
| `/opt/incomex/backups/directus-pre-iucore-500x-20260522T083543Z.dump` | 0 | 0 | — |
| `/opt/incomex/backups/directus-pre-iucore-500x-durable-20260522T112557Z.dump` | 0 | 0 | — |
| `/opt/incomex/backups/directus-pre-iucore-540x-20260522T091458Z.dump` | 0 | 0 | — |
| `/opt/incomex/backups/directus-pre-iucore-60x-20260522T032338Z.dump` | 0 | 0 | — |
| `/opt/incomex/backups/directus-pre-iucore-960x-20260522T135027Z.dump` | 0 | 0 | — |
| `/opt/incomex/backups/directus-pre-iucore-structevent-20260522T015648Z.dump` | 0 | 0 | — |
| `/opt/incomex/backups/directus-pre-iucore-structop-20260521T151127Z.dump` | 0 | 0 | — |
| `/opt/incomex/backups/vps-backup-20260718_203701.tar.gz` | 37 | 0 | `/opt/incomex/logs/backup-gdrive.log:157448` |
| `/opt/incomex/backups/mysql` | 1939 | 43 | `/opt/incomex/scripts/mysql-backup.sh.retired:8` |
| `/opt/incomex/backups/mysql-pre-pg-migration.sql` | 21 | 6 | `/opt/incomex/docker/agent-data-repo/knowledge/current-state/reports/directus-dual-superadmin-owner-ready-2026-07-24.md:204` |
| `/opt/incomex/backups/iu-core-70000x` | 14 | 0 | `/opt/incomex/mcp-roots/gh/work/vps-clean-20-9-26/BAO-CAO.md:166` |
| `/opt/incomex/backups/dieu45-phase1` | 23 | 0 | `/opt/incomex/backups/mcp-writes-perms/20260604T033154Z/rollback.sh:4` |
| `/root/backups` | 4851 | 15 | `/opt/incomex/mcp-roots/gh/work/vps-clean-20-9-26/BAO-CAO.md:166` |
| `/root/p0-2-dryrun` | 3 | 3 | `/opt/incomex/backups/dieu44_v0_3_readobs_dryrun_rerun_20260516T230306Z/prod-directus-20260516T230306Z.sql:1239651` |
| `/root/p0-2-prod-exec` | 4 | 4 | `/opt/incomex/backups/dieu44_v0_3_readobs_dryrun_rerun_20260516T230306Z/prod-directus-20260516T230306Z.sql:1239655` |
| `/root/wsq5_apply` | 0 | 0 | — |
| `/root/wsq5_apply_backup_20260518T054609Z` | 0 | 0 | — |
| `/root/wsq5_reauth_backup_20260518T065011Z` | 0 | 0 | — |
| `/root/wsq5_seed_priv_backup_20260518T072520Z` | 0 | 0 | — |
| `/root/phase7-rerun-backups` | 11 | 0 | `/opt/incomex/mcp-roots/gh/work/vps-clean-20-9-26/BAO-CAO.md:226` |
| `/root/agent-runs` | 47 | 25 | `/opt/incomex/.git/worktrees/codex-gemini/gitdir:1` |
| `/root/mcp-nolimit-stage` | 94 | 78 | `/opt/incomex/data/workspace-tools/results/e601389b1e694358bb2e89e6dcef6956:1` |
| `/opt/incomex/docker/mysql` | 1898 | 4 | `/opt/incomex/mcp-roots/gh/work/vps-clean-20-9-26/BAO-CAO.md:166` |
| `/opt/incomex/docker/dieu44_v0_4_connenv_prod_20260517T030513Z` | 0 | 0 | — |
| `/opt/incomex/docker/dieu44_v0_5_constmarker_amend_prod_20260518T081501Z` | 2 | 0 | `/opt/incomex/evidence/del1j-20260803/out/git-moi.txt:10` |
| `/opt/incomex/docker/directus-dump.sql` | 8 dòng | xem ghi chú | `/opt/incomex/docker/agent-data-repo/knowledge/current-state/reports/directus-dual-superadmin-owner-ready-2026-07-24.md:205` |

</details>

---

## V1 — Codex thẩm tra · 21/09/2026 · executor=Codex Desktop qua SSH (shell VPS) · write_path=workspace_*

RUN_ID `VPSC-V1-20260921-01` · PROMPT@3131bdee21a080a6fdfb5138ca72c2b7b3d30a38 (đã kiểm commit cuối chạm PROMPT, khớp OWNER_APPROVED + READY). Based_on repo `76c5490fe8088a9cb18af7722da8235fb0840220`. **Kết quả: DỪNG / V1_LIMITED — chưa hoàn tất thẩm tra để duyệt dọn.** Đo nhẹ trực tiếp 21/09/2026 khoảng 07:48–07:53Z, không lấy số R1 làm số V1. Đơn vị GB dưới đây = GiB.

### 1. CHO OWNER

- **Chưa nên duyệt triển khai toàn bộ phương án R1.** Đĩa hiện 91%, dùng 86,39GiB, trống **9,41GiB**; vượt ngưỡng chỉ đo nhẹ của PROMPT.
- Xác nhận độc lập Qdrant giữ **160 snapshot, 27,58GiB** và script hằng ngày không xoá snapshot server-side.
- Xác nhận script deploy sao Nuxt không tỉa; builder context-pack chép sang staging nhưng không dọn nguồn tạm. Log Directus hiện **1,316GiB**; chưa đo được tốc độ tăng độc lập.
- **N1 chưa qua cổng cứu hộ:** bản host mới nhất ngày 21/09; gói Drive được phản ánh trong meta/log ngày 20/09. Meta không có danh mục/checksum từng snapshot.
- Phát hiện script Drive vẫn xoá snapshot tạm sau khi tải thất bại; trạng thái PASS/COMPLETE không chứng minh đầy đủ thành phần Qdrant. Cần sửa điều kiện thành công trước khi dùng làm bằng chứng xoá.
- Ngay cả giả sử thu hồi đủ 34,4GiB của R1, hiện chỉ đạt **43,81GiB trống**, chưa đạt mục tiêu 45GiB.
- Đã kiểm RootFS của từng image N7/N8: không là tiền tố image đang chạy, không container nào dùng trực tiếp; vẫn phải giữ cổng R03/cứu hộ.
- **PASS 1 / REVISE 6 / BLOCK 8. PASS duy nhất là giữ N14, không phải cho xoá. Thu hồi được xác nhận đủ điều kiện xoá: 0GiB.**
- Không xoá/sửa dữ liệu, không restart, không chạy dọn, không tải/giải mã backup. Chỉ ghi báo cáo này và dòng VPSC.3.

### 2. Kết quả N1–N15

PASS = khuyến nghị của nhóm đã được xác minh trong phạm vi nêu; PASS cho HOLD không được cộng vào thu hồi. REVISE = cần sửa phương án/bổ sung bằng chứng; BLOCK = chưa được mở cổng xoá. Dấu “—” là **chưa đo**, không phải 0 và không sao chép số R1.

| Nhóm | GB R1 | GB V1 | Kết luận | Lý do |
|---|---:|---:|---|---|
| N1 Qdrant | 27,6 | 27,581 (allocated) | BLOCK | 160 snapshot được đếm trực tiếp; host có 8 bản 14–21/09, bản 21/09 là 236.036.608 byte. Chưa chứng minh snapshot mới nhất có trong gói Drive; meta chỉ cấp gói, script có nhánh bỏ qua lỗi tải. Không duyệt xoá toàn bộ theo bằng chứng hiện có. |
| N2 Log Directus | 1,3 | 1,316 | REVISE | stat file xác nhận kích thước; container tạo 23/07. Chưa kiểm độc lập cấu hình xoay log/file descriptor và chưa có tốc độ đo độc lập. “Hằng ngày, nếu >100MB thì truncate” không tạo trần 100MB giữa hai lượt; cần quy tắc xoay/cắt có trần và kiểm sau thao tác. |
| N3 Bản sao Nuxt | 2,7 | — | BLOCK | Đếm 66 thư mục khớp `nuxt-output.*`; còn tên dạng `nuxt-output-*`. R1 dùng tổng nhiều dạng tên nên không được so số lượng như cùng một tập. Chưa grep từng target qua mã, /etc, crontab mọi user và systemd; chưa chốt danh sách 3 bản gần nhất + bản mốc. Không quét sâu ở 91%. |
| N4 context-pack.tmp | 1,45 | — | REVISE | 1.001 thư mục, 979 có mtime thư mục >3 ngày; **không đồng nghĩa 979 thư mục an toàn để xoá**. R1 ghi ~990 ứng viên. Phải kiểm nội dung mới nhất/trạng thái job và loại lượt đang chạy; builder xác nhận thiếu dọn nguồn tạm. Chưa đo GB độc lập. |
| N5 Cache | ~1,4 | — | REVISE | Chưa đo lại block có thể thu hồi/working set. Dọn theo tháng chưa chứng minh trần 1GB; cần chỉ rõ công cụ/chủ cache, giữ browser runtime và loại hardlink trước khi tính dung lượng. |
| N6 Build cache | 0,4 | — | BLOCK | R03 hiện CLIENT-ONLY FINAL ACCEPTANCE, chưa CLOSED. Chưa xác minh lại GC/thu hồi thực tế của backend build. |
| N7 7 image trung gian | ≤0,5 | — | BLOCK | Kiểm riêng đủ 7 ID: không container dùng, RootFS không là tiền tố của image đang chạy. R03 chưa CLOSED; quan hệ lớp đúng không thay thế quyền bỏ rollback hoặc chứng minh số GB thu hồi. |
| N8 9 image local-only | ~2–3 | — | BLOCK | Kiểm riêng đủ 9 ID: không container dùng, RootFS không là tiền tố của image đang chạy. Chưa có bằng chứng rescue off-VPS và load/khôi phục cho đúng tập image, không cộng GB ước lượng vào số an toàn. |
| N9 Dump cũ postgres | 4,1 | — | BLOCK | Chưa grep từng tên qua đầy đủ các nguồn tham chiếu bắt buộc; chưa có cứu hộ kiểm được. Cần manifest chính xác và tách khỏi N10 để không trùng file .sql. |
| N10 SQL tạm | 0,14 | — | REVISE | Chưa kiểm từng file/job đang dùng và ranh giới N9; tuổi >7 ngày không tự chứng minh file dùng một lần. Quy tắc phải loại job đang chạy và giữ/quarantine đúng manifest. |
| N11 Tồn dư mission | ~5,5 | — | BLOCK | Chưa grep từng tên/đường dẫn; danh sách hiện còn wildcard và “…” nên chưa phải manifest xoá. Cần loại chính xác N12 và mọi file/dữ liệu còn phụ thuộc, rồi cứu hộ. |
| N12 Giữ theo nhãn | ~1,0 | — | BLOCK | Giữ nguyên UNKNOWN_HOLD; chưa kiểm độc lập từng nhãn/checkpoint. Không đưa các mục này vào purge chung theo tuổi hay toàn thư mục cha. |
| N13 DB thử | 1,2 | 1,174 | REVISE | DB còn tồn tại: 1.260.534.807 byte. Giữ UNKNOWN_HOLD, không đo chuỗi theo thời gian. Kiểm chuỗi chính xác “CẤM XOÁ” trong comment trả false; chưa chứng minh nhãn bị gỡ (có thể khác cách viết). Cần đối chiếu nhãn DEL-1; chưa có bằng chứng đủ gate backup/dependency để xoá. |
| N14 Hermes cũ | 3,0 | — | PASS (giữ) | Đọc launcher thực tế: lệnh hermes vẫn exec venv dưới `/usr/local/lib/hermes-agent`. Xác nhận phải giữ; chưa duyệt chuyển launcher/hợp nhất/xoá. Không tính dung lượng thu hồi. |
| N15 Alpine/kernel | ~0,3 | — | REVISE | Chưa kiểm tham chiếu Alpine, kernel dự phòng và cơ chế tự dọn; tiếp tục HOLD, chưa được tính vào thu hồi. |

**Phạm vi chưa hoàn tất:** không chạy du tầng 1, quét lớp ghi containerd, tổng file mở đã xoá, grep toàn bộ tham chiếu N3/N9/N11 hoặc rà toàn đĩa tìm nguồn ≥0,5GiB, vì cổng 91% chỉ cho đo nhẹ. Không xác nhận lại đối soát du–df hoặc tổng BUSINESS/operational của R1. Phiên thực tế là Codex Desktop điều khiển shell VPS qua SSH, **không phải Codex CLI chạy trực tiếp trên VPS như nhãn yêu cầu**; ghi rõ sai khác, không giả lập executor. Trước lượt tiếp cần Host phản ánh đúng bề mặt thực thi vào đề bài.

### 3. Các hiệu chỉnh bắt buộc trước đề bài dọn

**V1-01 · Backup Qdrant phải chứng minh đủ thành phần và thất bại thì dừng.** Mã VPS `scripts/backup-to-gdrive.sh:258–274` cho phép list/create lỗi qua `|| true`; tải snapshot lỗi chỉ ghi WARN rồi vẫn gọi DELETE. Lượt mới nhất đọc được có thông báo snapshot + upload hoàn tất, không thấy WARN tải lỗi; điều đó **không phải bằng chứng đã kiểm payload**. Meta config không có inventory từng snapshot, payload đã che. Không suy “backup hằng ngày PASS” thành “snapshot cần giữ đã có ngoài VPS”. Cần manifest gồm collection, tên/thời điểm/size/checksum snapshot, liên kết với gói off-VPS và xác minh khôi phục phù hợp trên máy ngoài VPS; không tải về ổ đang đầy. Bản host ngày 21/09 và gói ngày 20/09 là hai mốc khác nhau, không diễn đạt là cùng bản mới nhất.

Chỉnh đề xuất vá `qdrant-backup.sh`: chỉ DELETE đúng snapshot sau khi sao chép thành công và kiểm tính toàn vẹn; nếu một bước lỗi thì giữ bản nguồn + báo lỗi. Không thêm xoá mọi snapshot >1 ngày vô điều kiện, vì có thể xoá bản duy nhất của lượt backup thất bại. Chốt retention theo tập đã được chứng minh có bản cứu, loại snapshot đang tạo/tải. Qdrant có API riêng [xoá snapshot collection](https://api.qdrant.tech/v-1-18-x/api-reference/snapshots/delete-snapshot?explorer=true); đó là thao tác API, không phải lệnh restart. V1 không gọi DELETE và chưa kiểm thời gian thu hồi block thực tế.

**V1-02 · Tính lại dung lượng mục tiêu từ số hiện tại và tránh cộng trùng.** df chính xác: tổng 102.888.095.744 byte, dùng 92.765.503.488, available 10.105.815.040. Dùng tăng **2,94GiB** so với số cuối R1 04:10Z; nguyên nhân chưa được đối soát, không quy thành tốc độ tăng ổn định. Muốn đạt 45GiB từ mốc này cần thu hồi ròng ít nhất **35,59GiB**, chưa tính phát sinh/tạm trong khi thao tác. Theo giả thiết R1 34,4GiB cũng chỉ đạt 43,81GiB. Phải dùng available thực tế, không lấy tổng trừ used bỏ qua reserved space. N9/N10 phải tách tập .sql; N11/N12 phải tách vùng có nhãn; image chia sẻ layer chỉ tính phần vật lý thực sự có thể giải phóng.

**V1-03 · Chốt manifest và bảo vệ rollback/job đang chạy.** N3 phải liệt kê chính xác cả dạng tên chấm và gạch ngang, chỉ rõ bản mốc; R1 vừa nói “1 bản mốc” vừa cho tối đa 2 nên trần 4×45MB chưa nhất quán. N3/N9/N11 bắt buộc kiểm từng tên qua đủ nguồn tham chiếu của PROMPT; grep thư mục cha không thay thế được. N4/N10 kiểm job/lock và thời điểm ghi nội dung, không chỉ tuổi thư mục. Đặt kiểm tra lại target ngay trước mutation để tránh deploy/backup chen ngang. R03 chưa CLOSED nên giữ nguyên cổng rollback/build cache.

**V1-04 · Phân biệt lịch dọn với trần bảo đảm.** Cron cắt log khi >100MB một lần/ngày cho phép tăng thêm cả ngày; dọn cache hằng tháng không chứng minh ≤1GB. Snapshot còn giữ ≤1 ngày không có steady-state 0 tuyệt đối và còn peak lúc tạo/sao chép. TTL 30 ngày cho mission không đồng nghĩa local 0 khi vẫn có mission mới. Bổ sung budget, kiểm tần suất/overshoot, xử lý khi job dọn hoặc offload lỗi và đỉnh dung lượng tạm; tính lại tổng mức ổn định thay vì giữ nguyên con số 34,5GiB của R1.

**V1-05 · Không xoá mù dữ liệu phục hồi công cụ hoặc lịch sử.** TTL `transactions/jobs/results` cần chủ workspace xác nhận riêng từng loại, giữ job đang chạy và journal/idempotency còn cần khôi phục. Không áp purge chung cho toàn cây workspace-tools. `git gc` không tự hạn chế dung lượng lịch sử còn được tham chiếu; `--prune=now` cũng không nên trở thành quy tắc mặc định khi còn tiến trình ghi. Các đề xuất này cần được cụ thể hoá trong đề bài sau, chưa triển khai.

**V1-06 · Cứu hộ ngoài VPS theo bộ có thể khôi phục.** N8/N9/N11 cần kiểm thành công mọi chặng nén/mã hoá/upload, checksum và đối tượng hoàn chỉnh trước xoá nguồn; có kế hoạch khôi phục kiểm được, không tạo gói cứu lớn trên VPS. Retention Drive giữ theo bộ artifact + meta và tính riêng lưu lượng nạp hằng tháng với tổng dung lượng lưu ổn định; “tăng ròng ~0” không có nghĩa “không tải thêm dữ liệu”. Tôn trọng nhãn giữ/mission còn mở trước mọi TTL chung.

**Bốn nguyên nhân R1:** (1) xác nhận cơ chế rò Qdrant và GB; (2) xác nhận mã deploy thiếu tỉa, chưa xác nhận GB; (3) xác nhận file pm2 lớn, chưa xác nhận độc lập tốc độ hay toàn bộ cấu hình rotation; (4) xác nhận builder không dọn nguồn và số thư mục, chưa xác nhận GB/tốc độ. Chưa đủ căn cứ nói R1 không bỏ sót nguồn ≥0,5GiB; chênh df 2,94GiB là phần còn mở.

### 4. Bằng chứng và giới hạn

Bằng chứng mới lấy trực tiếp qua shell VPS, giữ trong output công cụ của phiên; **không tạo kho raw hoặc file tạm mới trên VPS**, không đọc lại số raw R1 để thay phép đo. Repo chỉ có tóm tắt đã làm sạch:

- E01: df, thời gian UTC, danh sách container/trạng thái; phép đo đầu đã báo 91%. Có thêm một df byte trong bước định danh để tính chính xác; đây là lặp ngoài yêu cầu “mỗi phép đo một lần”, không dùng làm chuỗi đo tốc độ và không có sleep.
- E02: liệt kê metadata một tầng snapshot Qdrant: 160 file snapshot; tổng snapshot/checksum 29.613.664.768 byte logic, **29.615.128.576 byte cấp phát**; danh sách 8 bản host.
- E03: stat duy nhất log pm2: 1.413.027.126 byte logic, 2.759.832 block ×512; ngày tạo container 23/07. Không đọc nội dung log truy cập.
- E04: liệt kê một tầng deploy/context-pack và đọc mã trực tiếp `qdrant-backup.sh`, `backup-to-gdrive.sh`, `dung-va-trien-khai.sh`, `dot-context-pack-build.sh`; chỉ xuất nhánh liên quan đã che thông tin nhạy cảm.
- E05: Docker inspect container + image metadata, đối chiếu đủ từng ID N7/N8 với RootFS image đang chạy và tham chiếu của cả container dừng.
- E06: meta staging config ngày 20/09, status PASS/COMPLETE, chỉ báo điều kiện từ đoạn log lượt mới nhất; **không truy cập/list Drive trực tiếp, không checksum payload hoặc giải mã**.
- E07: đọc launcher Hermes; truy vấn metadata DB thử bằng phiên read-only. Lần kết nối đầu bằng role mặc định không thành công; lần dùng role cấu hình của container thành công, không đo activity theo thời gian.
- E08: trạng thái R03 đọc từ `work/mcp-workspace/COLLAB.md` ở cùng Based_on; vẫn chưa CLOSED.

**NEXT cho Host:** xử lý V1-01–V1-06 và điều kiện nguồn đĩa tăng, chốt đúng executor/phạm vi phép đo nhẹ để hoàn tất những mục còn thiếu; chưa dùng báo cáo giới hạn này làm giấy duyệt dọn. Không ghi MACHINE_DONE vì phép thẩm tra tổng và grep bắt buộc chưa hoàn tất.

---

## R1 — 09/2026 · UNVERIFIED_R1 · executor=Claude Code CLI · write_path=workspace_*

RUN_ID `VPSC-R1-20260920-01` · PROMPT@`7ce1cbd389a9ca54e12d74cf2f8aeb6306334c65` (khớp READY) · đo 2026-09-21 03:26Z → 04:11Z · chế độ AUDIT / NO PRODUCTION MUTATION.
Đơn vị: **GB = GiB** như `df -h`/`du`. "Từ 24/07" = từ lúc dọn xong 24/07 ~07:30Z tới lúc bắt đầu đo (57,8 ngày). "GB/tháng" = quy về 30 ngày.
Mọi số dưới đây là **UNVERIFIED_R1** cho tới khi Host đo lại và Codex thẩm tra (VPSC.3).

### 1. CHO OWNER

**Kết luận một câu:** đĩa đầy lại không phải vì dữ liệu nghiệp vụ (chỉ 2,5GB, gần như đứng yên) mà vì **một script backup Qdrant quên xoá bản chụp bên trong Qdrant** — riêng nó chiếm 27,6GB và ăn **~6,6GB mỗi tháng**, tức một nửa mức đầy lại từ 24/07. Cộng thêm bản sao web trước mỗi deploy, log truy cập của Directus và bản dựng tạm context-pack không ai xoá.

**Anh cần quyết (3 câu):**

1. **Xoá 27,6GB bản chụp Qdrant cũ + sửa script để không kẹt nữa?** Bản mới nhất luôn có bản sao ở ổ ngoài container (7 ngày) và trên Drive (hằng ngày từ 20/07); các bản cũ hơn chỉ là trạng thái quá khứ của chỉ mục vector, tái tạo được. → **PM đề xuất: ĐỒNG Ý** sau khi Codex PASS. Xoá qua API của Qdrant, không restart, không phụ thuộc R03. Chỉ riêng việc này đã đưa đĩa từ 12GB lên ~40GB trống.
2. **~9,6GB dump và bản chụp cũ từ các mission tháng 5–7** (trong container postgres 4,1GB, `/opt/incomex/backups` + `/root` + MySQL cũ 5,5GB) — đưa lên Drive rồi xoá khỏi VPS? → **PM đề xuất: ĐỒNG Ý đưa lên Drive** (mã hoá, giữ 12 tháng) rồi xoá tại VPS; riêng các mục DEL-1 dán nhãn "giữ lâu/cấm xoá" để nguyên.
3. **DB thử `directus_gov_test_20260602` (1,2GB, nhãn DEL-1 "CẤM XOÁ", chưa có bản ngoài VPS) và bản cài Hermes cũ (3,0GB, lệnh `hermes` vẫn trỏ vào)** — giữ trên VPS hay chuyển đi? → **PM đề xuất:** DB thử: dump ra Drive trước, **giữ nguyên trên VPS** tới khi DEL-1 kết luận. Hermes: gom về một bản cài (dịch vụ đang chạy bản trong `/var/lib/hermes`), bỏ bản cũ sau khi chuyển lệnh `hermes`.

**Ma trận nguồn sinh** (đối soát với df ở dòng cuối)

| # | Nguồn sinh | LOẠI | Hiện tại GB | Tăng từ 24/07 | GB/tháng | Bounded? | Ổn định dự kiến GB | Thu hồi an toàn GB | Màu |
|---|---|---|---:|---:|---:|---|---:|---:|---|
| 1 | Bản chụp Qdrant kẹt trong container (`qdrant-backup.sh`) | DISPOSABLE | 27,6 | +12,7 | 6,6 | `FAIL_UNBOUNDED` | 0 | 27,6 | 🔴 |
| 2 | Bản sao web Nuxt trước mỗi deploy (`deploys/nuxt-output.*`, 70 bản sao) | DISPOSABLE | 2,9 | +2,0 | 1,1 (14 ngày gần: 1,5) | `FAIL_UNBOUNDED` | 0,2 | 2,7 | 🔴 |
| 3 | Log truy cập pm2 bên trong container Directus | DISPOSABLE | 1,3 | +1,3 | 0,7 | `FAIL_UNBOUNDED` | 0,1 | 1,3 | 🔴 |
| 4 | Bản dựng tạm `context-pack.tmp` (999 bản, 3 giờ/lần) | DISPOSABLE | 1,5 | +0,75 | 0,4 | `FAIL_UNBOUNDED` | 0,05 | 1,45 | 🔴 |
| 5 | Hermes: 2 bản cài + cache | RUNTIME (+cache DISPOSABLE) | 6,6 | +4,3 | 0,4 (+3,7 cài một lần) | `FAIL_UNBOUNDED` | 3,2 (+3,0 nếu giữ bản cũ) | 0,5 | 🔴 |
| 6 | Image Docker: đang chạy + cha + rollback + trung gian | RUNTIME / rollback | 9,7 | +1,0 | 0,5 | `FAIL_UNBOUNDED` (không luật giữ N tag) | ~8 | 0 lúc này (chờ R03; cứu trước ~2–3) | 🔴 |
| 7 | Build cache | DISPOSABLE | 0,2 (+phần trong kho image) | +0,2 | ~0,1 | trần GC mặc định, chưa khai | ≤1 | 0,4 sau R03 | 🟡 |
| 8 | Cache công cụ ở `/root` (npm, pip, uv, electron, node-gyp, playwright) | DISPOSABLE | 1,9 | +0,4 | 0,2 | `FAIL_UNBOUNDED` | 1,0 | 0,9 | 🔴 |
| 9 | `/tmp` bên trong container postgres (dump tháng 5 + file SQL tạm của agent) | NONBUSINESS_KEEP | 4,2 | +0,14 | 0,07 | `FAIL_UNBOUNDED` | 0 | 0 lúc này (câu 2) | 🔴 |
| 10 | Tồn dư mission: dump / bản chụp / checkpoint / thư mục stage không hạn xoá | NONBUSINESS_KEEP | 6,5 | +0,3 | 0,15 | `FAIL_UNBOUNDED` | 0 | 0 lúc này (câu 2) | 🔴 |
| 11 | DB thử `directus_gov_test_20260602` | NONBUSINESS_KEEP | 1,2 | 0 | 0 | tĩnh | 1,2 (0 nếu chuyển đi) | 0 (HOLD) | 🟡 |
| 12 | Backup vòng quay tại chỗ (PG 7 ngày, Qdrant 7 ngày, gói Drive 1 bộ) | NONBUSINESS_KEEP | 3,0 | ~0 | ~0 | trần local 7 ngày | 3,0 | 0 | 🟢 |
| 13 | Backup Lark tại chỗ (JSONL giải nén + tar.gz) | NONBUSINESS_KEEP | 1,2 (cuối phiên 1,1: lượt 21/09 đã thay lượt 14/09) | +1,2 | 0 | có trần: `prune-local` xoá lượt cũ sau offsite-ok | 1,1 (nay) / 0,1 (sau vá) | 0 | 🟡 |
| 14 | Log: journald, Docker json, `/var/log`, `/opt/incomex/logs` | DISPOSABLE | 1,8 | +0,2 | ~0,05 phần không trần | phần lớn có trần | 2,5 | 0 | 🟡 |
| 15 | Trạng thái công cụ workspace + cowork runner | RUNTIME | 0,45 | +0,45 | chưa rõ | chưa thấy TTL | 0,5 | 0 | 🟡 |
| 16 | Thư mục làm việc mission (`evidence/ staging/ tmp/ work/ artifacts/ exports/`) | DISPOSABLE (có phần bằng chứng) | 0,16 | ~+0,1 | ~0,05 | `FAIL_UNBOUNDED` (không TTL) | 0,05 | 0 | 🔴 |
| 17 | Công cụ AI + git (Claude Code, Codex, `.git`, clone, mcp-roots) | RUNTIME | 1,1 | +0,1 | ~0 | tự giữ 3 bản / gc tuần | 1,1 | 0 | 🟢 |
| 18 | PostgreSQL sống (`directus`, `incomex_metadata`, WAL) | BUSINESS_LIVE | 2,2 | +0,05 | 0,03 | nghiệp vụ | 2,2 + tăng tự nhiên | — | 🟢 |
| 19 | Qdrant storage (vector thật) | BUSINESS_LIVE | 0,2 | ~0 | ~0 | nghiệp vụ | 0,2 | — | 🟢 |
| 20 | Hệ điều hành, mã, swap 2GB, node_modules/venv, lặt vặt | RUNTIME | 9,6 | +0,5 | ~0,1 | ổn | 9,6 | 0 | 🟢 |
| | **Cộng BUSINESS_LIVE** | | **2,5** | +0,05 | | | 2,5 | | |
| | **Cộng RUNTIME_WORKING_SET** | | **26,7** | +5,6 | | | ~22,3 (+3,0 nếu giữ Hermes cũ) | | |
| | **Cộng NONBUSINESS_KEEP** | | **16,1** | +1,7 | | | ~4,4 | | |
| | **Cộng DISPOSABLE_REBUILDABLE** | | **38,0** | +18,4 | | | ~5,2 | | |
| | **TỔNG (du)** | | **83,3** | **+25,7** | **~11,5 đang chạy** | | **~34,5** | **34,4 ngay + 0,4 sau R03** | |
| | **df lúc bắt đầu đo** | | **83,4** | **+25,7** (58G→84G) | 13,3 TB (gồm cài Hermes) | | | | |

Đối soát: tổng `du` 83,3GB so với `df` 83,4GB (lệch 0,07GB = metadata + file đã xoá còn mở 0,02GB + ghi trong lúc đo). Tổng mức tăng theo dòng 25,7GB so với `df` tăng 25,7GB; khoảng ~1GB trong đó là ước lượng (dòng 14, 17, 20). Không có khoản lệch >3GB chưa giải thích.

**Hai con số tách bạch**
- **Nghiệp vụ:** hôm nay **2,5GB** (3% phần đã dùng). Tăng ~0,05GB từ 24/07.
- **Vận hành:** hôm nay **80,9GB** (97%). Sau khi áp đủ trần/TTL/đưa-ra-ngoài ở §7: **~32GB** (~35GB nếu giữ bản cài Hermes cũ). Toàn đĩa khi đó ~34,5GB dùng / 95,8GB → **trống ~61GB**.
- Mức tăng ngoài nghiệp vụ đang chạy **~11,5GB/tháng** = gần **4 lần ngưỡng đỏ 3GB/tháng**. 14 ngày gần nhất riêng nguồn 1–4 đã ~4GB.
- Dọn ngay lớp `DELETE_PROVEN_SAFE` (nhóm 1–5 ở §6): trống **12,4 → ~46,8GB** (đạt T1 ≥45GB). Cộng lớp cứu-rồi-xoá: ~57GB.

---

### 2. CHO PM

#### §3 Đo tổng + đối soát (tóm tắt)

- `df /` lúc bắt đầu (03:26Z): 89.549.037.568 B dùng · 13.322.280.960 B trống · 88%. Inode 9%. `df` lúc cuối: 04:10:37Z 89.607.528.448 B dùng · 13.263.790.080 B trống · 88% — chênh ròng +0,06GB, khớp với 2 bản sao do 2 lần deploy Nuxt trong lúc đo (+~0,08GB) và lượt backup Lark thay lượt cũ (−~0,05GB); R1 chỉ ghi 0,2MB bằng chứng.
- `du -x` tầng 1: `/var` 49,5GB (trong đó `/var/lib/containerd` **42,9GB**, `/var/lib/hermes` 3,4GB, `/var/log` ~1,3GB) · `/opt` 17,4GB (`/opt/incomex` 14,0GB, `/opt/workflow/postgres` 3,4GB) · `/usr` 8,7GB (có `/usr/local/lib/hermes-agent` 3,0GB) · `/root` 5,6GB · `/swapfile` 2,0GB · `/tmp` 0,14GB.
- Docker 29.2.1 dùng **kho image containerd** (snapshotter overlayfs) nên `/var/lib/docker` chỉ 0,7GB; image + lớp ghi container nằm hết trong `/var/lib/containerd`. Trong 42,9GB đó: lớp ghi `incomex-qdrant` **27,6GB**, lớp ghi `postgres` 4,2GB, lớp ghi `incomex-directus` 1,3GB, snapshot image 7,6GB, kho blob nén 2,2GB.
- `docker system df` báo Images 46GB / "reclaimable 37GB" — **con số này sai lệch** với kho containerd: đo thật, toàn bộ snapshot image chỉ 7,6GB và image tạo từ 24/07 chỉ chiếm 0,9GB. Không dùng số "reclaimable" của Docker để ước lượng thu hồi.
- Log: `daemon.json` đã có `max-size 50m × 3` (nghi vấn f ở PROMPT **không đúng** với log Docker); journald `SystemMaxUse=1G` (đang 1,0GB); `/var/log` ~0,24GB ngoài journal.
- File đã xoá còn bị giữ (`lsof +L1`): 70 file, 0,02GB — không đáng kể.
- Hardlink: `deploys/` 0 file nlink>1 (mỗi bản sao Nuxt chiếm chỗ thật); cache uv/pnpm có hardlink vào venv/node_modules nên xoá cache uv/pnpm thu hồi thấp (đã loại khỏi lớp an toàn).
- Swap: `/swapfile` 2GB, đang dùng 0,35GB. Không có snap. Kernel: 6.8.0-139 (đang dùng) + 6.8.0-90 (cũ, ~0,3GB).

#### §4 Sổ nguồn sinh (Generator Registry)

| Nguồn sinh | Path | LOẠI | Trigger | Tần suất | GB | Tăng từ 24/07 | GB/tháng | Cần ở VPS? | Trần local đề xuất | Ổn định tính ra | Giữ dài: đích · ngân sách · hạn | Tái tạo được: quy tắc xoá | Quy tắc giữ hiện có | Tự dọn? | Nguyên nhân rò | Chủ |
|---|---|---|---|---|---:|---:|---:|---|---|---|---|---|---|---|---|---|
| Bản chụp Qdrant server-side | `/qdrant/snapshots/production_documents/` trong lớp ghi container `incomex-qdrant` (không có bind) | DISPOSABLE | cron root `qdrant-backup.sh` | 1 lần/ngày 03:00 giờ máy | 27,6 (160 bản, 67→225MB/bản) | +12,7 (60 bản) | 6,6 và tăng theo cỡ collection | Không — bản ở host 7 ngày + gói Drive hằng ngày đã đủ | 0 bản trong container | 0 × 1 ngày = 0 | Đã có trên Drive trong gói cấu hình hằng ngày | Xoá bằng API Qdrant ngay sau `docker cp` | Script xoá bản ở host >7 ngày; **không xoá bản trong Qdrant** | Không | Script POST tạo snapshot → `docker cp` ra host → không gọi DELETE (script Drive `backup-to-gdrive.sh` thì có DELETE) | hạ tầng backup (cron root) |
| Bản sao web trước deploy | `/opt/incomex/deploys/nuxt-output.truoc-*`, `.bak*`, `-pre-*`, `.backup-*` | DISPOSABLE (rollback ngắn hạn) | `scripts/phai-cu/dung-va-trien-khai.sh` (`cp -a` trước rsync) + sao lưu tay | mỗi deploy; 16 bản/14 ngày | 2,9 (70 bản sao × ~43MB) | +2,0 (47 bản) | 1,1 TB / 1,5 gần | Có, nhưng chỉ vài bản gần nhất để hoàn tác | 3 bản mới nhất + 1 bản mốc | 4 × 0,045 = 0,2 | — | Giữ 3 mới nhất + mốc, xoá phần còn lại sau mỗi deploy | Không có | Không | Script chỉ sao, không tỉa | quy trình deploy Nuxt |
| Log pm2 Directus | `/home/node/.pm2/logs/directus-out-0.log` trong lớp ghi `incomex-directus` | DISPOSABLE | tiến trình Directus (pm2-runtime), ghi mỗi request | liên tục ~23MB/ngày | 1,3 (1 file) | +1,3 (container tạo 23/07) | 0,7 | Không cần giữ lịch sử | 100MB | 23MB/ngày × ≤4 ngày ≈ 0,1 | — | Cắt về 0 khi >100MB (truncate, file đang mở) hoặc hạ mức log | `max-size` của Docker **không áp** cho file pm2 trong container | Không | Log nằm trong container, không có xoay vòng | Directus (image chính hãng) |
| Bản dựng tạm context-pack | `/opt/incomex/context-pack.tmp/<BUILD_ID>` | DISPOSABLE | cron user incomex `dot-context-pack-build.sh` | 3 giờ/lần | 1,5 (999 thư mục) | +0,75 (399) | 0,4 | Không, sau khi đã chép sang staging | 3 ngày | ~8 bản/ngày × 3 ngày × 1,5MB ≈ 0,04 | — | Xoá `.tmp/<BUILD_ID>` ngay khi chép xong + dọn >3 ngày | `dot-context-pack-retention-cleanup` chỉ dọn `context-pack-staging` (7 ngày, tối thiểu 3) | Không (staging thì có) | Builder ghi `.tmp/<BUILD_ID>` rồi chép, không xoá nguồn | DOT context-pack |
| Hermes — bản đang chạy | `/var/lib/hermes/hermes-agent` (+ `.agent-browser`, `.hermes`, `work` 8G thưa) | RUNTIME | systemd `hermes-serve`, `hermes-gateway`, relay | chạy thường trực; cập nhật tay (28/07, 11/09) | 2,7 + ảnh `work` 0,2 (trần cứng 8G) | +2,9 (cài 28/07) | ~0,2/lần cập nhật (pack git mới) | Có — dịch vụ đang chạy | 1 bản cài + `git gc` sau cập nhật | ~2,9 | — | — | Không | Không | Mỗi lần cập nhật để lại pack git + dependency cũ | Hermes (systemd hermes-*) |
| Hermes — bản cài cũ | `/usr/local/lib/hermes-agent` | RUNTIME? → `UNKNOWN_HOLD` | lệnh `/usr/local/bin/hermes` vẫn trỏ vào; phiên tmux demo từ 05/2026 | cập nhật 28/07, 11/09 | 3,0 | +0,7 (2 pack git 0,34 + 0,35) | ~0,3 | Chưa rõ — trùng chức năng bản đang chạy | 0 sau khi hợp nhất | 0 | — | — | Không | Không | Hai bản cài song song | Hermes |
| Hermes — cache | `/var/lib/hermes/.npm`, `.cache` (uv, electron) | DISPOSABLE | cài/cập nhật | theo cập nhật | 0,75 | +0,75 | ~0,1 | Không | 0,3 | 0,3 | — | `npm cache clean`, `uv cache prune` sau cập nhật | Không | Không | Cache không trần | Hermes |
| Image Docker cục bộ | kho containerd | RUNTIME (đang chạy + cha) / rollback | build tay theo mission (R03, hardening, continuation, workspace…) | 20 image mới 17–20/09 | 7,6 snapshot + 2,2 blob | +1,0 | 0,5 (dồn theo đợt build) | Có cho image đang chạy + cha; rollback chỉ vài bản | chạy + cha + 2 rollback/dịch vụ | ~8 | Rollback cũ: bản cứu trên Drive (`docker save`) ~2–3GB, giữ 12 tháng | Image dựng lại được từ Dockerfile trên VPS thì xoá sau R03 | Không có luật giữ N tag | Không | Mỗi lần build thêm tag mới, không tỉa | các mission build image |
| Build cache BuildKit | `/var/lib/docker/buildkit` + snapshot trong containerd | DISPOSABLE | `docker build` | theo đợt build | Docker báo 0,86 (0,41 riêng) | +0,86 (24/07 là 0) | ~0,45 | Không | `keepStorage` 1–2GB | ≤1–2 | — | `builder prune --keep-storage` sau R03 | GC mặc định của BuildKit, chưa khai trần | Có (mặc định) | — | build |
| Lớp ghi container postgres `/tmp` | `/tmp` trong `postgres` (2.866 mục) | NONBUSINESS_KEEP (dump cũ) + DISPOSABLE (SQL tạm) | agent `docker cp` file .sql/.dump vào để chạy | theo mission | 4,2 (4,1 là dump 05/2026) | +0,14 | 0,07 | Không — dump cũ là bản chụp DB tháng 5, SQL tạm là rác | 0 (TTL 7 ngày cho SQL tạm) | ~0 | Dump cũ: Drive mã hoá, ≤5GB một lần, giữ 12 tháng | SQL tạm: xoá >7 ngày | Không | Không | Agent chép file vào container, không dọn; nằm trong lớp ghi nên còn mãi tới khi recreate | agent/mission |
| Tồn dư mission | `/opt/incomex/backups/*` ngoài vòng quay (19 dump iucore, `dieu44_*` giữ, `vps-backup-20260718`, mysql, `iu-core-70000x`, `dieu45-phase1`, `pg-ngoai-vong-luan-chuyen`…), `/root/backups`, `/root/*checkpoint*`, `/root/p0-2-*`, `wsq5_*`, `phase7-*`, `agent-runs`, `mcp-nolimit-stage`, `/opt/incomex/docker/mysql`, `docker/dieu44_*` | NONBUSINESS_KEEP | mission thủ công | theo mission | 6,5 | +0,3 | 0,15 | Không cần nằm trên VPS | 0 (mọi dump mission TTL 30 ngày tại chỗ) | 0 | Drive mã hoá, ~6GB một lần + ≤1GB/tháng, giữ 12 tháng | — | Không | Không | Không có quy ước hạn xoá cho bản chụp mission | agent/mission |
| DB thử governance | `directus_gov_test_20260602` trong PG (1,2GB) | NONBUSINESS_KEEP | — (tĩnh từ 01/08) | — | 1,2 | 0 | 0 | Không cần chạy; nhãn DEL-1 "CẤM XOÁ" vì giữ 202 dòng duy nhất | giữ tới DEL-1 kết luận | 1,2 | Dump ra Drive (≤0,2GB nén), giữ vô hạn tới DEL-1 | — | nhãn COMMENT ON DATABASE: CẤM XOÁ | — | — | DEL-1 |
| Backup PG vòng quay | `/opt/incomex/backups/pg/directus_*.sql.gz` | NONBUSINESS_KEEP | cron root `pg-backup.sh` 02:27 | ngày | 1,0 (9 bản × 115MB) | ~0 | ~0 | Có — khôi phục nhanh tại chỗ | 7 ngày | 0,12 × 8 ≈ 1,0 | Drive (gói mã hoá hằng ngày) | — | `RETENTION_DAYS=7` | Có | — | hạ tầng backup |
| Backup Qdrant vòng quay | `/opt/incomex/backups/qdrant/*.snapshot` | NONBUSINESS_KEEP | `qdrant-backup.sh` | ngày | 1,7 (8 bản) | ~0 | ~0 | Có | 7 ngày | 0,22 × 8 ≈ 1,8 | Drive | — | `RETENTION_DAYS=7` | Có | — | hạ tầng backup |
| Gói Drive tại chỗ | `/var/lib/incomex/backup-staging` | NONBUSINESS_KEEP | cron `backup-to-gdrive.sh` 20:37 | ngày | 0,3 | ~0 | 0 | Có (bộ mới nhất) | 1 bộ | 0,3 | Drive: xem dòng "Drive" dưới | — | `LOCAL_KEEP=1` | Có | — | hạ tầng backup |
| Backup Lark | `/opt/incomex/lark-backups/daily/<ngày>`, `archives/` | NONBUSINESS_KEEP | systemd `s177-lark-backup.timer` T2+T5 03:15Z | 2 lần/tuần | 1,2 (cuối phiên 1,1) | +1,2 | 0 (vòng) | Chỉ cần bản nén mới nhất | giữ tar.gz 1–2 bản; JSONL xoá ngay khi offsite-ok | 0,07 × 2 ≈ 0,1 | Drive (đã có offsite-ok) | — | `prune-local` sau offsite-ok (script ghi 14 ngày; đo thật 21/09: lượt mới thay lượt 14/09, còn 1 thư mục JSONL + 1 tar.gz) | Có | Giữ JSONL giải nén 1,1GB trong khi bản nén 70MB đã lên Drive | Lark ops |
| Drive (đích ngoài VPS) | thư mục backup mã hoá trên Drive | NONBUSINESS_KEEP | `backup-to-gdrive.sh` | ngày | 18,4 trên Drive (280 đối tượng từ 20/07) | +18,4 trên Drive | ~8,6 trên Drive | — | — | — | **Chưa có hạn giữ ở đích** — đề xuất 30 bản ngày + 12 bản tháng ≈ 12GB | — | `MAX_REMOTE_BACKUPS=14` chỉ áp cho file cũ ở gốc, không áp thư mục mã hoá | Không | Thiếu bước tỉa ở đích | hạ tầng backup |
| Log Docker json | `/var/lib/docker/containers/*/*-json.log` | DISPOSABLE | Docker | liên tục | 0,5 | ~+0,2 | 0 (có trần) | Không | 50MB × 3 / container (đang có) | ≤1,8 | — | — | `max-size 50m, max-file 3` | Có | — | Docker |
| journald | `/var/log/journal` | DISPOSABLE | systemd | liên tục | 1,0 | ~0 | 0 | Không | 1G (đang có) | 1,0 | — | — | `SystemMaxUse=1G` | Có | — | OS |
| Log ứng dụng theo ngày | `/var/log/incomex/hc-executor*-<ngày>.log` (306 file), `/opt/incomex/logs/disk-snapshots/` | DISPOSABLE | cron `dot-hc-executor*` (3 giờ), `disk-monitor.sh` (giờ, khi >85%) | 3 giờ / giờ | ~0,1 | +0,01 | ~0,01 | Không | 30 ngày | nhỏ | — | xoá >30 ngày | logrotate không bắt tên file theo ngày; `disk-snapshots` đang giữ 30 file (~1MB) | Một phần | Tên file theo ngày | DOT / hạ tầng |
| Cache `/root` | `.npm` 0,67 · `.cache` 1,2 (playwright 0,63, uv 0,26, electron 0,11, pip 0,07, node-gyp 0,06) | DISPOSABLE (playwright headless = RUNTIME, agent-data gắn vào) | npm/pip/uv/playwright | theo cài đặt | 1,9 | +0,4 | 0,2 | Không (trừ playwright headless) | 1GB | ≤1 | — | dọn cache hằng tháng bằng lệnh của chính công cụ | Không | Không | Cache không trần | agent/tooling |
| Trạng thái công cụ workspace | `/opt/incomex/data/workspace-tools` (transactions, jobs, results, `.before/.json`) | RUNTIME | agent-data `workspace_*` | liên tục từ 17/09 | 0,11 | +0,11 (4,6 ngày) | ~0,7 nếu giữ nhịp | Có (idempotency, khôi phục) | TTL 14 ngày (cần chủ công cụ xác nhận) | ~0,3 | — | — | Chưa thấy TTL | Chưa rõ | — | agent-data workspace |
| Cowork runner | `/var/lib/incomex-cowork` (jobs 53, ảnh 1G thưa) | RUNTIME | cowork runner | theo job | 0,3 | +0,3 (từ 26/07) | ~0,1 | Có | theo `incomex-cowork-audit-retention` | ~0,3 | — | — | timer retention có sẵn (chưa kiểm phạm vi) | Có? | — | Cowork |
| Thư mục làm việc mission | `/opt/incomex/{evidence,staging,tmp,work,artifacts,exports}` | NONBUSINESS / DISPOSABLE | agent/mission | theo mission | 0,16 | ~+0,1 | ~0,05 | Chỉ khi mission đang mở | TTL 30 ngày rồi đưa ra ngoài hoặc xoá | ~0,05 | Drive nếu là bằng chứng | xoá >30 ngày | Không | Không | Không có quy ước | agent/mission |
| Công cụ AI | `~/.claude` + 3 bản Claude Code 0,67 · `~/.codex` 0,05 · `~/.hermes` 0,02 · `~/.gemini`: không có | RUNTIME | tự cập nhật | — | 0,75 | ~0 | ~0 | Có | tự giữ 3 bản | 0,75 | — | — | Claude Code tự giữ 3 bản | Có | — | tooling |
| Git | `/opt/incomex/.git` 0,27 (74 commit từ 24/07, không remote) · sổ git 5 phút `docs/mcp-writes/.git` 1MB · clone `data/workspace-tools/github-workspace` 0,03 · `mcp-roots` 0,03 · `nuxt-repo/.git` 0,02 | RUNTIME | commit tay / timer 5 phút / connector | — | 0,35 | ~+0,1 | ~0,05 | Có (lịch sử mã SSOT) | — | chậm | — | — | `mcp-writes-git-gc.timer` hằng tuần | Có | — | hạ tầng |
| node_modules / venv | `nuxt-repo/web` 0,7 · `venv-xlsx` 0,07 · `lark-client/.venv` 0,08 · `agent-data-repo` 0,05 | RUNTIME | build/cài | — | 0,9 | +0,07 | ~0 | Có | — | 0,9 | — | — | — | — | — | các dịch vụ |
| PostgreSQL sống | `/opt/workflow/postgres/data` (`directus` 1,72 · `incomex_metadata` 0,41 · WAL ~0,08) | BUSINESS_LIVE | Directus/DOT | liên tục | 2,2 | +0,05 | 0,03 | Có | `max_wal_size 1GB`, không slot, archive off | — | Drive hằng ngày | — | — | — | — | Directus |
| Qdrant storage | `/opt/incomex/docker/qdrant/data` (bind) | BUSINESS_LIVE | agent-data/KB | liên tục | 0,22 | ~0 | ~0 | Có | — | — | Drive hằng ngày | — | — | — | — | KB |
| Volume Docker có tên | — | — | — | — | 0 | 0 | 0 | — | — | — | — | — | — | — | Không có volume nào (mọi dữ liệu là bind) | ✖ |
| Hệ thống | swapfile 2,0 · `/tmp` 0,14 · `/var/tmp` 0 · snap: không · apt cache 0,11 + lists 0,2 · kernel cũ 6.8.0-90 ~0,3 | RUNTIME / DISPOSABLE | OS | — | ~2,8 | ~+0,3 | ~0,1 | Có | 2 kernel | ~2,8 | — | `apt clean` định kỳ | unattended-upgrades | Có | — | OS |

**File >64MB trong `/opt/incomex` ngoài vòng quay:** `backups/dieu44_v0_3_readobs_dryrun_rerun_…/prod-directus-….sql` 0,62GB (giữ lại từ 24/07 vì REF=1) · `.git/objects/pack/pack-69d1….pack` 0,26GB (git, bình thường) · `backups/vps-backup-20260718_203701.tar.gz` 0,25GB · `docker/mysql/data/directus/directus_revisions.ibd` 0,13GB (MySQL cũ trước khi chuyển PG) · `backups/mysql-pre-pg-migration.sql` 0,11GB · `backups/pg-ngoai-vong-luan-chuyen/…` 0,11GB (DEL-1 "giữ lâu"). Các file >64MB còn lại là backup vòng quay (PG, Qdrant) và JSONL của backup Lark.

**Các chỗ cách ly do mission 24/07 tạo — vẫn còn đủ:** 5 image agent-data (`5a7eb4e4e2a2`, `b6154accb6d8`, `bfe092449032`, `d53a11072c00`, `9421cd9c4303`) · 2 image claude-mcp rollback (`73f953f71632`, `37098dc6ef6e`) · 7 thư mục `/root/*-checkpoint-*` (thêm 2 thư mục cùng loại tạo sau: `integrity-sm-fallback-r0-checkpoint-20260724T144500Z`, `c2b-f1-safety`) · thư mục `dieu44_…_rerun_20260516T230306Z` · 19 dump `directus-pre-iucore-*` · `/root/vps-clean-minimum-delete-manifest.tsv`.

**Vì sao `incomex-nuxt` chạy image "không tag":** compose khai image Nuxt **theo digest** (qua một biến môi trường; đã đối chiếu biến đó trỏ cùng image `72715a92885c`, không chép giá trị cấu hình vào đây). Container được tạo theo digest nên `docker ps` hiện ID. Image vẫn mang tag `…/web-test/nuxt-ssr:latest` của registry đã chết. Mã web không nằm trong image mà ở bind `/opt/incomex/deploys/nuxt-output → /app/.output`. Nếu compose recreate thì vẫn lên đúng image `72715a92885c` (miễn là image còn tại chỗ). Có bản cứu image trên Drive từ 21/07. ⇒ Hard-KEEP. Đề xuất ở lượt dọn: gắn thêm một tag cục bộ ghim digest để không ai dọn nhầm.

**Chuỗi cha–con image** (kiểm bằng tiền tố RootFS, khớp với các dòng `FROM` trong Dockerfile trên VPS):
- claude-mcp đang chạy `r03-finalclose` (`6b48248fa29f`) ← `r03-nametwin` (`7e25b17974bd`) ← `r03-20260920` (`e33bf3c0efe3`) ← `harden-20260919` (`70f04144fb42`) ← `phase0.9` (`d34e31acc759`) ← `phase0.5a` (`7034f4425d93`) ← `phase1a` (`7c0096602a1c`). Không phải cha: `phase0.6-fs` (`1176031f7b72`), `phase0.7-nolimit` (`11cbf7d2dbd2`), `phase0.8-1e` (`1fa4430a2d0c`), `rollback` (`37098dc6ef6e`), `rollback-pre-p2b` (`73f953f71632`).
- agent-data đang chạy `agent-data-r03:20260920-finalclose` (`cb20894c3bf8`) ← `r03 nametwin` (`519b2965db4a`) ← `r03 lifecycle` (`d3f5a6f54744`) ← `hardening:20260919-harden` (`bf38e829f501`) ← `hardening:20260918-opid` (`0ba7fd24528e`) ← `hardening:20260918-final` (`e1befd50f96f`) ← `workspace:20260917-git` (`c59c891af08c`) ← `agent-data-local:latest` = `workspace-base:20260917` (`9acd60503290`). Không phải cha: `continuation:20260918` (`2bd8638edac0`), `continuation:20260918-final` (`6b391ca38bef`), `hardening:20260918` (`eefb7bbe6c98`), `workspace:20260917` (`18a85d9ad4b3`), 4 bản `agent-data-local:*` cũ, `agent-data-test` (`9421cd9c4303`).
- claude-kb đang chạy `c5-20260918` (`87787b08bf3a`) ← `v1` (`0de33745213e`) ← `v1-pre-p05a-t3` (`3cf3065bf66e`). cowork chạy `phase1b`/`phase1a`; `pre-r2a` (`9095606afe72`, `ecf31f124168`) không phải cha.

#### §5 Backup

1. **Cơ chế đang chạy:** `pg-backup.sh` (cron 02:27, DB `directus`, giữ 7 ngày) · `qdrant-backup.sh` (cron 03:00, collection `production_documents`, giữ 7 ngày ở host) · `backup-to-gdrive.sh` (cron 20:37: `pg_dump | gzip | gpg` + gói cấu hình có snapshot Qdrant mọi collection, compose, nginx/TLS, scripts; staging giữ 1 bộ) · `code-backup-to-gdrive.sh` (cron 4 lần/ngày, giữ 1 tại chỗ, 56 trên Drive) · `s177-lark-backup` (timer T2+T5) · `mcp-writes-git-snapshot` (5 phút, git cục bộ) · context-pack (3 giờ).
2. **Các lượt gần nhất:** gói Drive **25/25 lượt "Upload complete" 27/08–20/09**; status file lượt 20/09: `PASS · COMPLETE`. `pg-backup` 21/09 OK (kept=9). `qdrant-backup` 17–21/09 OK mỗi ngày. Lark: `Finished` 03/09, 07/09, 10/09, 14/09, 17/09 (lượt 17/09 không để lại thư mục ngày — cần xem). `code-backup`: ⚪ log có (cập nhật 20/09 20:02) nhưng R1 chưa bóc được kết quả từng lượt.
3. **Bản mới nhất trên Drive (liệt kê chỉ đọc):** 20/09 — dump DB 119MB + gói cấu hình 169MB + 2 `meta.json`. Thư mục mã hoá có 280 đối tượng / 18,4GB, cũ nhất 20/07.
4. **Hạn giữ thực tế so với cấu hình:** PG tại chỗ 9 bản (7 ngày ✓) · Qdrant tại chỗ 8 bản (✓) · staging 1 bộ (✓) · **Drive thư mục mã hoá: không tỉa** — 63 ngày liên tục, ~8,6GB/tháng; `MAX_REMOTE_BACKUPS=14` chỉ áp cho file cũ ở gốc. Drive còn trống ~4,96TiB nên chưa nguy, nhưng theo D02 đích phải có hạn giữ. **Bản chụp Qdrant trong container: không có hạn giữ** (nguồn số 1).
5. **Tồn dư `.tmp/.partial`:** staging sạch (trap dọn `.partial`); `lark-backups/tmp` ~0.
6. **Lồng nhau:** gói cấu hình chứa snapshot Qdrant (có chủ ý), không chứa deploy/node_modules. `code-backup` loại `.git`, `node_modules`, `.nuxt`, `.output`, cache, `dist`, `.venv` ✓. Backup Lark giữ cả JSONL giải nén lẫn tar.gz (lặp ×16 dung lượng).
7. **Khôi phục (không diễn tập, không tốn đĩa):** sha256 của 2 gói staging **khớp** `meta.json`. `gpg --list-packets` đọc được gói khoá công khai; VPS không có khoá bí mật (đúng thiết kế), không giải mã ra đĩa. Bằng chứng khôi phục gần nhất: `OFF_VPS_DECRYPTION_RECOVERY = PASS` (vps-recovery-prep 24/07) và pg-restore-test 20/05 → **đã 58 ngày, quá 30 ngày ⇒ rủi ro**. Đề xuất diễn tập khôi phục sau khi dọn xong (khi đĩa có chỗ).
⇒ Mọi file liên quan backup ngoài vòng quay đang để `UNKNOWN_HOLD` hoặc `RESCUE_BEFORE_DELETE`; không mục backup nào được xếp `DELETE_PROVEN_SAFE`.

#### §6 Manifest ứng viên dọn

Hard-KEEP (không vào lớp xoá): 12 container đang chạy + image của chúng + mọi image cha ở §4 · `72715a92885c` (Nuxt) · tag rollback R03 (`claude-mcp-local:r03-*`, `*:rollback-pre-*-20260920`, `agent-data-r03:*`) tới khi R03 CLOSED · `postgres:16` · mọi bind mount dữ liệu · `deploys/nuxt-output` (bản đang chạy) · `deploys/web-test` (cron integrity chạy script ở đây) · `context-pack/`, `context-pack-staging/` · `/root/.cache/ms-playwright/chromium_headless_shell-1223` (agent-data gắn vào).

| Nhóm | Đường dẫn / ID | GB | Lớp | Bằng chứng | Tham chiếu / phụ thuộc | Cách lùi |
|---|---|---:|---|---|---|---|
| N1 Qdrant | 160 bản chụp `production_documents-…snapshot` (+`.checksum`) trong container `incomex-qdrant` | 27,6 | `DELETE_PROVEN_SAFE` | 05, 06, 08, s19 | Không script nào đọc lại theo tên (script chỉ `docker cp` bản vừa tạo); không container khác gắn; không phải cha/rollback | Bản host 8 ngày gần nhất + gói Drive hằng ngày (có snapshot mọi collection). Xoá bằng `DELETE /collections/production_documents/snapshots/<tên>`, không `rm`, không restart |
| N2 Log Directus | `/home/node/.pm2/logs/directus-out-0.log` trong `incomex-directus` | 1,3 | `DELETE_PROVEN_SAFE` (cắt về 0) | 04, 05, 14 | File đang mở bởi pm2 ⇒ chỉ `truncate`, không `rm` | Log truy cập, không cần lùi |
| N3 Bản sao Nuxt | 66 thư mục `deploys/nuxt-output.*` cũ (70 bản sao lúc 04:11Z), giữ 3 bản mới nhất + 1 bản mốc | 2,7 | `DELETE_PROVEN_SAFE`* | 09, s19 | Script deploy chỉ dùng bản vừa tạo để hoàn tác; không cron/systemd trỏ vào; nlink=1. *Codex cần grep từng tên trước khi PASS | 3 bản mới nhất còn tại chỗ; mã nguồn web thật ở máy Mac |
| N4 context-pack | `context-pack.tmp/<BUILD_ID>` cũ hơn 3 ngày (~990 thư mục) | 1,45 | `DELETE_PROVEN_SAFE` | 09, s19 | Builder chỉ ghi `.tmp/<BUILD_ID>` của lượt mình rồi chép sang staging; `dot-dieu43-fs-verify` chỉ kiểm thư mục `.tmp` tồn tại ⇒ giữ thư mục gốc | Tái tạo bằng lượt build kế tiếp |
| N5 Cache | `/root/.npm`, `/var/lib/hermes/.npm`, `/root/.cache/{pip,node-gyp,electron}`, `/var/lib/hermes/.cache/electron` | ~1,4 | `DELETE_PROVEN_SAFE` (bằng lệnh dọn của chính công cụ) | 13, 07 | Không gồm uv/pnpm (hardlink vào venv/node_modules) và playwright headless (agent-data gắn) | Tự tải lại khi cần |
| N6 Build cache | BuildKit (0,41 riêng) | 0,4 | `DELETE_PROVEN_SAFE` — **chờ R03 CLOSED** | 02 | build lại image rollback R03 có thể cần cache | `docker builder prune --keep-storage` |
| N7 Image trung gian R03-era | `2bd8638edac0`, `6b391ca38bef`, `eefb7bbe6c98`, `18a85d9ad4b3`, `1176031f7b72`, `11cbf7d2dbd2`, `1fa4430a2d0c` | ≤0,5 (đo thật) | `KEEP_ROLLBACK_UNTIL_R03_CLOSED` → sau đó `QUARANTINE_FIRST` | 02, 16, 15 | Không container dùng; không là cha của image đang chạy; mang tag `rollback-pre-*` của chuỗi 17–19/09 | Dockerfile còn trên VPS (không bit-exact) ⇒ muốn chắc thì `docker save` trước |
| N8 Image cũ local-only | `5a7eb4e4e2a2`, `b6154accb6d8`, `bfe092449032`, `d53a11072c00`, `9421cd9c4303`, `37098dc6ef6e`, `73f953f71632`, `9095606afe72`, `ecf31f124168` | ~2–3 (Docker báo cao hơn; đo df trước/sau) | `RESCUE_BEFORE_DELETE` | 02, 16, KB 24/07 | Không container dùng, không là cha; registry đã chết ⇒ không kéo lại được | `docker save \| gzip` → Drive, ~2–3GB, kiểm sha256, khôi phục `docker load` |
| N9 Dump cũ trong container postgres | `/tmp/*.dump`, `*.sql`, thư mục `dieu45_phase3`, `nuxt-output-*`, `d28-*`… (05–06/2026) | 4,1 | `RESCUE_BEFORE_DELETE` | 05, 14 | Không cron/script trỏ vào (cần Codex grep); là bản chụp DB thật ⇒ dữ liệu nhạy cảm | Nén + gpg → Drive (~2–3GB), sha256, khôi phục `pg_restore --table` chọn lọc |
| N10 SQL tạm của agent trong container postgres | `/tmp/*.sql` sau 24/07 (~140 file) | 0,14 | `QUARANTINE_FIRST` | 14 | Agent có thể còn đang dùng file gần đây | Giữ 7 ngày gần nhất |
| N11 Tồn dư mission | 19 dump `directus-pre-iucore-*`, `vps-backup-20260718…tar.gz`, `mysql/` + `mysql-pre-pg-migration.sql`, `iu-core-70000x/`, `dieu45-phase1/`, `/root/backups/`, `/root/{p0-2-*,wsq5_*,phase7-rerun-backups,agent-runs,mcp-nolimit-stage}`, `/opt/incomex/docker/{mysql,dieu44_*}`, `directus-dump.sql` | ~5,5 | `RESCUE_BEFORE_DELETE` | 01, 10, 13, 15 | Không cron/systemd trỏ vào theo grep tên thư mục cha (cần Codex grep từng tên) | Nén + gpg → Drive, sha256, giữ 12 tháng |
| N12 Giữ theo nhãn | `pg-ngoai-vong-luan-chuyen/` (DEL-1 "giữ lâu"), `dieu44_…_rerun_20260516T230306Z` (REF=1), 9 thư mục `/root/*checkpoint*` (có thể chứa bí mật) | ~1,0 | `UNKNOWN_HOLD` | 10, 13, KB 24/07 | nhãn DEL-1 / mission bảo mật | Chờ DEL-1 và chủ mission |
| N13 DB thử | `directus_gov_test_20260602` | 1,2 | `UNKNOWN_HOLD` | 13, 17 | `DB_DELETE_GATE`: (a) ✓ đúng target, owner là role quản trị của cụm PG, tạo 02/06 · (b) ✗ 0 kết nối đang mở ở cả 3 lần đọc, nhưng trong 30 phút `xact_commit` +68, `tup_returned` +159.566 — R1 chỉ tự mở 1 phiên (~3 truy vấn) ⇒ có tiến trình khác kết nối ngắn định kỳ, chưa xác định (xem dưới) · (c) ⚠ không cron/script chạy trỏ vào, nhưng ~3.277 file tài liệu/context-pack nhắc tên · (d) ⚠ DB có `postgres_fdw` trỏ ra `incomex_metadata` (chiều ra; không DB nào trỏ vào nó), không pub/sub · (e) ✗ **không có bản ngoài VPS** · nhãn DB: DEL-1 "CẤM XOÁ" | Dump ra Drive trước; DROP chỉ sau DEL-1 + Owner |
| N14 Hermes bản cũ | `/usr/local/lib/hermes-agent` | 3,0 | `UNKNOWN_HOLD` | 13 | `/usr/local/bin/hermes` còn gọi venv của bản này; dịch vụ systemd dùng bản `/var/lib/hermes` | Hợp nhất lệnh CLI trước |
| N15 Nhỏ | `alpine:latest` (`28bd5fe8b56d`); kernel cũ 6.8.0-90 | ~0,3 | `UNKNOWN_HOLD` (chưa grep script dùng `alpine`) / để apt tự lo | 02, 07 | — | kéo lại từ Docker Hub |

`DB_DELETE_GATE` (b) — chỉ số `pg_stat_database` của DB thử: 03:40:20Z `xact_commit=146.462 · tup_returned=389.726.111` → 03:44:34Z `146.470 · 389.747.351` → 04:10:37Z `146.530 · 389.885.677`, `sessions`=87 (DEL-1 ghi 49 phiên hôm 01/08). Lưu ý: lúc 03:44:35Z R1 tự mở **1 phiên** vào DB này để đọc `pg_foreign_server` (mục d), nên số lần 3 có phần do R1. Phần tăng giữa lần 1 và 2 (trước khi R1 kết nối) và phần lớn mức tăng tới lần 3 không phải của R1; số phiên tăng 49 → 87 từ 01/08 ⇒ có thứ vẫn chạm vào DB này. Chưa xác định nguồn ⇒ gate (b) FAIL. (D05 cho phép không chờ lần đọc 3; lần 3 đã chạy xong trước khi thấy D05, giữ lại để tham khảo — kết luận `UNKNOWN_HOLD` không đổi vì (e) đã FAIL.)

**Cộng:**
- Duyệt toàn bộ `DELETE_PROVEN_SAFE` (N1–N5): **~34,4GB** (N1 27,6 · N2 1,3 · N3 2,7 · N4 1,45 · N5 1,4). Thêm N6 sau R03 CLOSED: +0,4.
- Duyệt thêm `QUARANTINE_FIRST` (N7 sau R03, N10): +≤0,6.
- Cứu rồi xoá `RESCUE_BEFORE_DELETE` (N8, N9, N11): +~12GB tại VPS; cần **~10–12GB chỗ trên Drive**, không cất lên chính ổ VPS (dump nén trực tiếp thành luồng `gzip | gpg | rclone`, như script Drive đang làm).
- `UNKNOWN_HOLD` (N12–N15): ~5,5GB, không tính vào thu hồi.

#### §7 Khoá vòi (chỉ đề xuất, chưa làm)

| Nguồn | Sửa ở đâu | Quy tắc bằng số | Lý do |
|---|---|---|---|
| Bản chụp Qdrant | `scripts/qdrant-backup.sh` | Sau `docker cp` gọi `DELETE` đúng snapshot vừa tạo (như `backup-to-gdrive.sh` đã làm); thêm bước dọn mọi snapshot server-side cũ hơn 1 ngày. Host giữ 7 ngày như cũ | Ổn định: 0 trong container thay vì +6,6GB/tháng |
| Bản sao Nuxt | `scripts/phai-cu/dung-va-trien-khai.sh` | Sau khi deploy xong: giữ 3 bản `nuxt-output.truoc-*` mới nhất + 1 bản mốc (đặt tên `*.moc-*`, tối đa 2), xoá phần còn lại | 4 × 45MB = 0,2GB; đủ hoàn tác 3 lần gần nhất |
| Log pm2 Directus | cron root hằng ngày | `truncate -s 0` log pm2 trong container khi >100MB; hoặc hạ mức log request (đổi config → cần Owner) | Trần 100MB |
| context-pack.tmp | `dot/bin/dot-context-pack-build.sh` + `dot-context-pack-retention-cleanup` | Builder xoá `.tmp/<BUILD_ID>` ngay khi chép xong; retention dọn thêm `.tmp/*` >3 ngày | ~0,04GB |
| Image Docker | quy trình build/deploy (luật cho agent) | Mỗi dịch vụ: image đang chạy + mọi cha + tối đa 2 tag rollback; bản thứ 3 trở đi: `docker save` → Drive rồi xoá. Khai `builder gc keepStorage=2GB` trong `daemon.json` (đổi config → Owner) | ~8GB image, ≤2GB build cache |
| Hermes | quy trình cập nhật Hermes | Sau mỗi lần cập nhật: `git gc --prune=now`, `npm cache clean --force`, `uv cache prune`; chỉ một bản cài | Cài ~2,9GB + cache ≤0,3GB |
| `/tmp` container postgres | luật cho agent + cron tuần | Chạy SQL qua stdin (`docker exec -i … psql < file`) thay vì chép vào container; cron tuần xoá `/tmp/*.sql` >7 ngày trong container | ~0 |
| Tồn dư mission | luật cho agent | Bằng chứng/dump mission để ở `/var/lib/incomex-audit/<mission>/`, TTL 30 ngày, hết hạn thì đưa ra Drive hoặc xoá; `/root` không phải chỗ để dump | 0 tại chỗ |
| Backup Lark | `lark-backups/bin/s177-lark-backup-prune-local` | Có `.offsite-ok` là xoá ngay thư mục JSONL giải nén; giữ 1–2 tar.gz gần nhất | ~0,1GB thay vì ~1,1GB |
| Drive | `backup-to-gdrive.sh` | Tỉa thư mục mã hoá: giữ 30 bản ngày + 12 bản cuối tháng | Đích ~12GB, ngân sách tăng ~0 |
| Cache `/root` | cron tháng | `npm cache clean --force`, `pip cache purge`; trần 1GB | ≤1GB |
| Trạng thái workspace-tools | chủ agent-data | Xác nhận/khai TTL cho `transactions/jobs/results` (đề xuất 14 ngày) | ~0,3GB |
| Log theo ngày | `/etc/logrotate.d/incomex` | Bắt `hc-executor*-*.log` với `maxage 30` | nhỏ |
| Chuông | `scripts/disk-monitor.sh` (cron giờ) + monitor push "Disk Usage" có sẵn trong uptime-kuma | Ngưỡng 80% vàng / 90% đỏ (hiện 85%, chỉ ghi log). Đẩy trạng thái lên monitor Kuma đang có (cần xác minh ai đang đẩy). Thêm đo tuần tổng các nguồn §4, cửa sổ trượt 14 ngày, báo đỏ khi ngoài nghiệp vụ >3GB/tháng | T4 |

**Cộng lại sau khi áp đủ:**
- Mức ổn định tại chỗ: nghiệp vụ ~2,5GB + vận hành ~32GB = **~34,5GB / 95,8GB (36%)** (~37,5GB nếu giữ Hermes cũ; +1GB nếu chưa vá Lark).
- Biên: trống ~61GB. Graph (AGE) cần ≤1GB (§8). 12 tháng nghiệp vụ: PG `directus` tăng ~0,03GB/tháng, dự phòng 2GB. Còn lại **~58GB**.
- Đổ thêm ra ngoài VPS: một lần ~10–12GB (cứu N8, N9, N11) + dump DB thử ≤0,2GB. Định kỳ: ~0 thêm so với hiện tại. Gói Drive hiện ~8,6GB/tháng sẽ về trạng thái ổn định ~12GB tổng nếu áp tỉa đích. Drive còn trống ~4,96TiB. Mỗi lượt đẩy hằng ngày ~1–2 phút (có một lượt 17/09 mất 36 phút).

#### §8 Chỗ cho Graph (ước lượng)

- Apache AGE là extension trong PG16 hiện có. Image postgres có AGE: +0,3–0,7GB (build thêm extension hoặc dùng image AGE cho PG16). Đổi image = restart postgres ⇒ việc riêng, sau khi dọn.
- Dữ liệu: `universal_edges` hiện **2,5MB** (bảng 0,8MB + index 1,7MB, ~2.269 dòng). Dù graph gấp 10–50 lần vẫn <0,2GB. Nạp graph cần WAL/temp tạm ≤1GB (`max_wal_size` 1GB).
- Kết luận: **sau dọn thừa chỗ** (cần ~1–2GB, sẽ có ≥45GB trống). Ngay cả bây giờ 12GB trống vẫn chứa được về dung lượng. Rủi ro thật là vòi rò ~11,5GB/tháng: không khoá vòi thì chỗ trống sẽ lại hết sau vài tháng, Graph hay không cũng vậy.

#### Ghi chú phụ (ngoài phạm vi, không xử lý)

- Crontab root có các dòng `CRON_TZ=…`, nhưng cron của Ubuntu **bỏ qua `CRON_TZ`**: log cho thấy `qdrant-backup.sh` chạy 03:00 giờ máy (CEST), không phải 03:00 UTC như nhãn trong script ghi.
- Trong lúc đo có việc khác ghi đĩa, **không phải R1**: backup Lark lượt 21/09 chạy 03:27:55Z → 03:55:37Z (thêm lượt 21/09 ~1,1GB rồi `prune-local` bỏ lượt 14/09) và **2 lần deploy Nuxt** lúc 03:30Z và 03:38Z (tạo `nuxt-output.truoc-20260921-053026` và `-053858`, mỗi bản ~43MB).
- `disk-monitor.sh` hiện chỉ ghi log (ngưỡng 85%) và mỗi giờ ghi một bản chụp vào `/opt/incomex/logs/disk-snapshots/` khi vượt ngưỡng (hiện 30 file ~1MB, có vẻ đã có giới hạn).

---

### 3. KHO BẰNG CHỨNG

- Đường dẫn: `/var/lib/incomex-audit/VPSC-R1-20260920/` trên VPS (quyền 700, ngoài mọi cây Git — `git rev-parse` báo không nằm trong work tree trước khi ghi). Chỉ mục: `INDEX.md`. Tổng: 204KB, 22 file (≤200MB). Không commit/push ở đâu.
- Nội dung: bảng tổng hợp, không có danh sách file thô toàn cây; secret đã che (`***MASKED***`), không in nội dung `.env`/dump/backup mã hoá.
- Lệnh đã chạy (tất cả chỉ đọc; `du`/`find` dưới `nice -n 19 ionice -c3 timeout`, luôn `-x`, không quét `/proc` `/sys`): `df -B1 / -h / -i` · `du --max-depth` theo tầng · `docker version/info/system df -v/buildx du/ps -a -s/images/inspect/image inspect/volume ls` · `find -newerct 2026-07-24` (chỉ khoanh vùng) + `stat %W` (btime) · `lsof +L1` · `journalctl --disk-usage` · `crontab -l` mọi user, `/etc/cron.d`, `systemctl list-timers/list-units/cat` · `grep` script (che secret) · `psql` chỉ đọc (`pg_database_size`, `pg_stat_database`, `pg_stat_activity`, `pg_foreign_server`, `pg_extension`, `pg_publication/subscription`, `pg_total_relation_size`) · `rclone lsl/lsf/size/about/lsd` (chỉ đọc) · `sha256sum` · `gpg --list-packets` (không giải mã) · `sqlite3` đọc tên monitor Kuma · `git count-objects/log`.
- Ghi duy nhất của R1 trên VPS: thư mục bằng chứng trên. Không xoá, không restart, không sửa cron/systemd/config, không docker save/tag/prune, không VACUUM/DROP.
