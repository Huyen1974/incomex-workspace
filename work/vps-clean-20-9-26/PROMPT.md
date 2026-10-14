# PROMPT — VPSC-N2C-CODE-BACKUP-GPG-20261014-01 · Mã hoá backup mã nguồn lên Drive bằng đúng tuyến GPG khoá công khai của backup PG (D23/D27) · không đổi lịch, không xoá tay, không mở `.env.working`

RUN_ID: VPSC-N2C-CODE-BACKUP-GPG-20261014-01
Task: `work/vps-clean-20-9-26` (VPSC) · D22–D27. Không phải việc mới: lỗ do L2SAFE (`d0af7dd`) tìm ra, bảng backup ghi chủ = VPSC.
Soạn: Claude Chat P102 (B2 sau GPT P101) — thay bản nháp N2a xoá đĩa (lý do ở P102). Rà: GPT Chat Host B3 một lượt: ổn ⇒ READY đúng SHA; sửa nhỏ chỉ thêm kiểm thì sửa thẳng rồi READY (Claude chấp nhận trước).
Executor: Claude Code CLI, phiên MỚI trên Mac, qua `ssh contabo`. Ghi repo: Incomex MCP `workspace_*` root `workspace`.
Status: **DRAFT — Claude Reviewer ACCEPT (P102), chờ GPT Host READY đúng SHA last-touch**.
Bằng chứng: `/opt/incomex/work/vps-clean-20-9-26/VPSC-N2C-CODE-BACKUP-GPG-20261014-01/` (`<EV>`; chỉ receipt đã làm sạch). Báo cáo: mục `N2C-20261014` trong `BAO-CAO.md`. Tiến độ + KQ: dưới P102 trong `COLLAB.md`. Không tạo tệp repo mới.
**Chỉ thực hiện phần trên dòng `LỊCH SỬ` đầu tiên.** Tham chiếu: §1 luật cứng + §2 S0 của bản lịch sử HEAL-01; trong `BAO-CAO.md`: mục `L2-SAFETY-MAP-20261014` (bảng backup) và mục `HEAL-20261013` (cách đã sửa `disk-monitor.sh` + sổ mã — dùng đúng đường đó cho script này).

## 0. Vì sao, và thế nào là XONG
- `scripts/code-backup-to-gdrive.sh` (lịch root 08/12/15/20 giờ VN, giữ 56 bản/repo trên Drive + 1 bản tại chỗ; 2 repo `web-test` = `nuxt-repo`, `agent-data-test` = `agent-data-repo`) đẩy `.tar.gz` **không mã hoá** lên `gdrive-backup:`. Gói có `agent-data-repo/.env.working` (chưa ai mở) và `BACKUP-MANIFEST.txt` ghi `push_token`. Backup PG/cấu hình (`backup-to-gdrive.sh`) đã mã hoá GPG khoá công khai, VPS không giải mã được — tuyến đã chạy thật, dùng lại y nguyên.
- D23 đòi bản trên Drive mã hoá; D27 đòi giữ vững cơ chế backup ⇒ lượt này là **gia cố** backup, không tắt gì.
**XONG khi đủ cả 5:**
1. Bản backup mã nguồn mới là `<repo>_<YYYYMMDD-HHMM>_ICT.tar.gz.gpg`, mã hoá cho ĐÚNG người nhận mà `backup-to-gdrive.sh` đang dùng, gọi `gpg` y hệt cách script đó gọi (cùng cờ, cùng nguồn khoá công khai); luồng `tar | gzip | gpg` không để bản rõ trên đĩa; từ lượt này không còn tệp `.tar.gz` rõ nào mới sinh ra.
2. Retention giữ nguyên chính sách 56 bản/repo trên Drive + 1 bản tại chỗ, đếm CHUNG hai đuôi `.tar.gz` và `.tar.gz.gpg` theo mốc giờ trong tên ⇒ bản rõ cũ trên Drive tự ra hết trong ≤ 14 ngày (4 lượt/ngày); bản rõ tại chỗ được thay ngay ở lượt chạy thử. Không xoá tay thêm bản nào. **Giới hạn kết luận:** «≤14 ngày» chỉ đúng nếu mọi lượt lịch 4 lần/ngày tiếp tục thành công và chính sách retention hoạt động; nếu lượt hỏng thì bản rõ có thể còn lâu hơn. Phải ghi số bản rõ tồn lưu + trách nhiệm xử lý rủi ro đến khi có encrypted restore proof, không tuyên bố đã hết phơi lộ, không tự xóa sớm bản cũ. `gpg --list-packets` chứng minh ciphertext/recipient, KHÔNG thay thế thử giải mã/khôi phục bằng khóa riêng trong môi trường được phép ngoài VPS.
3. Một lượt chạy thử thật cho cả 2 repo: tệp lên Drive, bytes remote = local, `gpg --list-packets` (không cần khoá bí mật) thấy đúng keyid người nhận; 2 monitor Kuma code backup nhận nhịp `up`.
4. D26 đủ 4 ô cho script đã sửa: Đ30 (`bash -n` + lượt chạy thử mục 3) · Đ31 (Config Guard/sổ mã INV23 cập nhật đúng đường HEAL-01) · canh (Kuma 2 monitor code backup → Telegram khi lượt sau hỏng) · lùi (bản sao script trước sửa + cách đặt lại đúng đường).
5. `.env.working`: chỉ đếm số dòng `TÊN=giá_trị` có TÊN chứa KEY/TOKEN/SECRET/PASS và liệt kê TÊN biến (không in giá trị, không in nội dung, không chép, không sửa) → BAO-CAO, để Owner định phạm vi O-R7-KEY.

## 0A. Quyền Owner — khối Owner dán PHẢI có nguyên dòng này
Owner D27 (14/10/2026): «Trong quá trình thực thi, các bạn phải kiểm tra rất kỹ để tránh tắt nhầm các chức năng vẫn đang sử dụng. Lấy ví dụ như điều 30, 31, luật trong KB để bảo vệ những mã đã làm, tránh AI khác vô tình xóa nhầm. Các cơ chế kiểm soát và báo cáo tự động qua Telegram, các cơ chế giám sát, các cơ chế backup tự động xuống Google Drive. Tất cả những việc đó cần phải bóc tách rất kỹ bằng Grab, tránh việc tắt nhầm các chức năng này rồi lại mất công đi lần mò khôi phục lại.»

RUN này chỉ: sửa 1 tệp `scripts/code-backup-to-gdrive.sh` (mã hoá + biểu thức retention/đếm) + chạy thử 1 lượt + đếm tên biến `.env.working`. Không đổi lịch, số bản giữ, remote hay thư mục Drive; không đụng `backup-to-gdrive.sh`/`pg-backup.sh`/`qdrant-backup.sh`; không tạo khoá mới, không đưa khoá bí mật lên VPS; không xoá tay bản backup nào; không mở/sửa `.env.working`; không xoay khoá. Thiếu dòng trên hoặc thiếu Reviewer ACCEPT + Host READY đúng SHA ⇒ DỪNG trước STARTED.

## 1. Luật cứng
- Áp nguyên §1 của bản lịch sử HEAL-01 (VPS-GHI · báo từng bước · danh sách KHÔNG ĐƯỢC · bí mật · nghi ngờ thì giữ).
- Người nhận GPG lấy từ cấu hình đang chạy của `backup-to-gdrive.sh` (đọc mã, không in khoá); không tìm thấy, không khớp hoặc cần khoá bí mật ⇒ DỪNG trước khi sửa.
- Fail-closed: `gpg` lỗi ⇒ không upload, không rơi về bản rõ, Kuma `down` (giữ cơ chế `on_error` hiện có). **Cổng D27 bổ sung của Host:** mọi pipeline `tar … | gpg` phải fail theo lỗi của BẤT KỲ công đoạn nào (`set -o pipefail` hoặc bằng chứng tương đương), ghi ra tệp `.gpg` chưa công bố trước và chỉ upload/signal Kuma UP/tính retention sau khi toàn bộ luồng + checksum thành công. Nếu tar đọc lỗi hoặc gpg nhận dữ liệu thiếu dù tự thoát 0 ⇒ DỪNG, giữ backup known-good và báo SECURITY_HOLD; tuyệt đối không cho script tự fallback tạo/upload `.tar.gz` rõ. Không thêm file backup rõ mới trong preflight/thử nghiệm.
- Chạy thử khi không có lượt lịch trong ± 10 phút (08/12/15/20 giờ VN) và `.code-backup.lock` trống.
- Cấm `find /`, `du /`, quét đệ quy từ gốc (P101 PROCESS_DEVIATION).
- 4 đích lệch cũ (#22) + INV20 giữ nguyên; không sửa Guard/Kuma để lấy PASS.
- Ngân sách ≤ 45 phút.

## 2. S0 — đọc + PRE (chỉ đọc)
1. Đọc `AGENTS.md` → COLLAB gốc (`VPS-GHI`) → VPSC COLLAB §0 (D22–D27) + P101–P102 → PROMPT này → `BAO-CAO.md` mục L2-SAFETY-MAP-20261014 + HEAL-20261013.
2. Kiểm Reviewer ACCEPT + Host READY đúng SHA; khối Owner có dòng D27; Guard PRE + PRE_RED_SET; drift-check PRE.
3. Script: sha hiện tại; có là đích Config Guard / có trong sổ mã INV23 không; đường sửa hợp lệ theo HEAL-01; lượt chạy gần nhất (log) + trạng thái 2 monitor Kuma code backup.
4. Cách `backup-to-gdrive.sh` gọi `gpg` (cờ + nguồn khoá công khai) và keyid người nhận (16 ký tự cuối).
5. Giữ `VPS-GHI` (CAS) + STARTED dưới P102 cùng commit trước mọi thay đổi.

## 3. Thực hiện
1. **Bản sao:** `<EV>/code-backup-to-gdrive.sh.truoc` (sha).
2. **Sửa tối thiểu, không sửa gì khác:** (a) `file_name` thêm đuôi `.gpg`; (b) bước `archive`: `tar … -czf - "${repo_name}" | gpg <cờ y hệt backup-to-gdrive.sh> --output "${archive_path}"`; (c) mọi chỗ khớp đuôi `_ICT.tar.gz` (retention tại chỗ, retention Drive, dòng đếm summary) nhận cả `.tar.gz` và `.tar.gz.gpg`, sắp xếp như cũ; (d) `require_cmd` thêm `gpg`; (e) log thêm `recipient=<keyid>`; (f) 1 dòng nhãn đầu tệp: `# SUA 14/10/2026 VPSC-N2C-CODE-BACKUP-GPG-20261014-01: ma hoa GPG khoa cong khai (cung nguoi nhan backup-to-gdrive.sh); khoi phuc can khoa bi mat giu ngoai VPS`. `bash -n` PASS.
3. **Áp** qua đúng đường S0.3 (Config Guard apply-v0 nếu là đích; sổ mã INV23 theo cách HEAL-01).
4. **Chạy thử 1 lượt** (§1 giờ chạy) và kiểm đủ §0 mục 3 + mục 2 (bản rõ tại chỗ đã được thay; số bản trên Drive mỗi repo vẫn ≤ 56).
5. **`.env.working`:** theo §0 mục 5.
6. **POST:** drift-check (script MATCH baseline mới nếu là đích), Guard `--coverage` 4 ô, 22 đèn = PRE_RED_SET, health 200.
7. **Báo cáo:** mục `N2C-20261014` (cho Owner ≤ 3 dòng · diff · kết quả chạy thử · bảng 4 ô · tên biến `.env.working` + số đếm · số bản rõ cũ còn trên Drive và ngày dự kiến hết) → `KQ@VPSC-N2C-CODE-BACKUP-GPG-20261014-01 XONG|DỪNG · …` dưới P102 → **trả `VPS-GHI: trống` cùng commit**. Guard tổng FAIL chỉ vì #22 cũ ⇒ KQ PARTIAL nợ receipt, KHÔNG lùi.
**Lỗi thì lùi — chỉ khi lỗi MỚI do lượt này** (gpg/upload lỗi · bytes lệch · Kuma code backup `down` · đèn mới đỏ): đặt lại script từ `.truoc` đúng đường S0.3, kiểm sha = PRE; các tệp `.gpg` đã lên Drive giữ (vô hại); KQ DỪNG nêu bước.
**Đồ tạm dự kiến:** `<EV>` (giữ có chủ đích) · thư mục ứng viên apply-v0 nếu dùng (giữ làm đường lùi) · 0 tiến trình nền.

## 4. Bước đi
| Bước | Việc | Bằng chứng | Lỗi thì |
|---|---|---|---|
| 1/5 S0 | đọc, PRE, đường sửa, người nhận GPG, giữ khoá | ảnh PRE, STARTED | DỪNG trước mọi thay đổi |
| 2/5 Sửa + áp | 6 chỗ §3.2, `bash -n`, áp đúng đường | diff, sha | lùi |
| 3/5 Chạy thử | 1 lượt, 2 repo | `.gpg` trên Drive, bytes, keyid, Kuma `up` | lùi |
| 4/5 Kiểm | `.env.working` (tên), drift, coverage 4 ô, 22 đèn | 0 THIẾU | lùi nếu lỗi mới; chỉ #22 cũ ⇒ PARTIAL, giữ |
| 5/5 KQ | BAO-CAO + KQ + trả khoá | 0 tiến trình nền | — |

Sau RUN (không thuộc RUN này, không ai chờ): Reviewer kiểm lượt lịch kế ra `.gpg` và bản rõ cũ giảm dần. Nếu `.env.working` có khoá thật ⇒ gộp vào câu O-R7-KEY cho Owner gật/lắc (xoay khoá + xoá ngay bản rõ cũ trên Drive). Thử khôi phục định kỳ (S-RESTORE) là việc riêng, cần khoá bí mật ngoài VPS.

---

<details><summary>LỊCH SỬ — bản nháp N2a «xoá đĩa Drive-first» (GPT P101, KHÔNG chạy — P102: không có đối tượng ELIGIBLE, #11 đỏ chỉ vì SLOPE7D đang tự hết) — KHÔNG THỰC HIỆN</summary>

# (Lịch sử) PROMPT — VPSC-N2A-DISK-DRIVE-FIRST-20261014-01 · #11 theo số thật, D23/D27, không xóa vật sống
RUN_ID: VPSC-N2A-DISK-DRIVE-FIRST-20261014-01
Task: work/vps-clean-20-9-26. Host GPT Chat P101 B1, Claude Chat Reviewer P102 B2, Claude Code CLI Worker. Owner dán RUN thủ công.
STATUS: DRAFT — CHƯA READY, CẤM RUN. Chỉ thực hiện phần trên LỊCH SỬ khi Claude ACCEPT và GPT Host READY đúng SHA.

## 0. Quyền Owner và đích
D23: «khi xóa chúng ta chuyển xuống Google Drive trước rồi xoá. Nếu có gì đó vẫn có thể lấy được GGD. Hệ thống backup vẫn đang hoạt động».
D27: «Trong quá trình thực thi, các bạn phải kiểm tra rất kỹ để tránh tắt nhầm các chức năng vẫn đang sử dụng. Lấy ví dụ như điều 30, 31, luật trong KB để bảo vệ những mã đã làm, tránh AI khác vô tình xóa nhầm. Các cơ chế kiểm soát và báo cáo tự động qua Telegram, các cơ chế giám sát, các cơ chế backup tự động xuống Google Drive. Tất cả những việc đó cần phải bóc tách rất kỹ bằng Grab, tránh việc tắt nhầm các chức năng này rồi lại mất công đi lần mò khôi phục lại.»
Mục tiêu: đĩa trống >=45GiB, #11 xanh THẬT, các nguồn tăng có van, giữ dịch vụ/backup/Đ30-31. KQ L2SAFE d0af7dd 05:07Z: trống 37,78GiB, còn thiếu ~7,2GiB, storage-watch SLOPE7D -3,06GiB dù 24h gần nhất dung lượng trống tăng 3,6GiB. Không có bằng chứng đang tồn tại 7,2GiB rác được phép dọn. Không ép XONG; nếu không còn đủ ELIGIBLE, KQ PARTIAL và đề xuất Owner nâng dung lượng/cho phép riêng đúng nhóm.

## 1. Cổng D27 PROTECTED — không sửa, không xóa
- GIỮ: Graph production, image Cognee builder ~3,5GiB, 27 old images dùng làm parent/compose/rollback, image D04 còn tham chiếu, Neo4j volumes chưa rõ chủ; PG/Directus/Qdrant data và backups; sổ /var/lib/hjw-control/ledger.jsonl (INV17, 08:00 Telegram), toàn bộ HJW control; sr-mow, Guard/Config Guard, KB laws, sổ mã, Kuma/Telegram, trigger/permission guards, cron root/incomex/cron.d, lịch GDrive PG/code/Qdrant, staging chưa upload/verify, bản rollback còn dùng.
- PROOT04 13/10 là kiểm kê CŨ: H1 đã dọn staging/tmp, 5 image (~0,1GiB thực do shared layer) và một container; H2 đã dọn 2.510 snapshots transactions qua van, gỡ pgvector ~0,65GiB. Không dọn lại hoặc suy Cognee 3,5GiB là image thử. CẤM docker system/image/volume prune, docker buildx prune, docker image rm, blanket rm -rf, find /, du /, dọn journal/backup và xóa mọi thứ ngoài whitelist.
- SECURITY_HOLD: code backup Drive hiện là .tar.gz CHƯA MÃ HÓA, gồm entry .env.working (nội dung chưa mở; không kết luận có secret nhưng không coi an toàn). Không đọc/cat/extract entry này, không in token/credential, không dùng tuyến code-backup plaintext để archive; chỉ đường rescue GPG đã xác minh trong HEAL/H2, khóa ở Secret Manager và không lộ thông tin bí mật. Không thay đổi hoặc tắt backup code đang chạy trong RUN này.
- sr-mow Đ30/31 silent Directus 403 từ 03/10, #22 Guard INV5_6/INV20 cũ của TQT/HJW, receipt Kuma→Telegram UNKNOWN, restore test cuối 05/10 chưa theo định kỳ. Ghi debt cho đúng chủ, không sửa hộ; không coi toàn bộ hệ thống được bảo vệ full PASS.
- Thời lượng tối đa 60 phút, không chờ cron/ngày, không chạy hai mutation VPS cùng lúc. Các hoạt động read-only có thể thực hiện song song với task khác nếu thực sự không xung đột. Không giữ worker/process nền sau KQ.

## 2. S0 đo nhanh bằng số có sẵn, kiểm exact quyền và inventory
Đọc AGENTS, COLLAB gốc VPS-GHI, VPSC D22–D27/P81–P82/P98–P102, BAO-CAO HEAL-20261013/HEAL02-L0/L2SAFE và PROMPT READY hiện hành. Đối chiếu HEAD, khóa, lease, no-concurrent, Guard PRE, 22 lights, tài nguyên, backup/restore sức khỏe và owner của từng vật trước mọi mutation.
Sử dụng storage-watch taxonomy 24h/7d và các nguồn tăng có tên; bounded ls/du tối đa depth 1–2 trên path nguồn đã được đo, tuyệt đối không find / hoặc quét sâu toàn máy. Snapshot df byte, source size và tốc độ, chủ, last ref/open fd, retention valve, archive receipt/restore hash. Không đo lại cả PROOT04, tránh trùng công việc H1/H2.
BẢNG EXACT: path/ID hiện có, owner, valid business ref hoặc rollback, Graph/code/cron/compose references, bytes thực có thể reclaim (không cộng chung Docker layers), approved retention/TTL, encrypted Drive receipt, SHA256/readback/decrypt restore sample, phân loại ELIGIBLE / KEEP / OWNER_REQUIRED. Unknown => KEEP.
Whitelisted ONLY nếu S0 xác minh vẫn cần xử lý, có quyền và existing approved operator: (A) transactions before-images quá 48h và byte ở Git PUSHED/REACHABLE + readback (H2 luật p); (B) completed/unreferenced mcp-helper/mcp-roots đã hết hạn theo retention H1 luật m/n/o có mã hóa+restore proof; (C) VPSC-owned temporary staging/tmp mới hết hạn sau H1, đúng mã/path và không có live refs. Đã ROTATING đúng chính sách thì KEEP, không chạy lại vô nghĩa. Mục thuộc TQT/HJW/HVU/GS => pointer, không thao tác; không chọn thêm bucket mới để cho đủ 45GiB.
Nếu không có ELIGIBLE và approved operator/backup proof => NO_MUTATION, KQ PARTIAL với đúng blocker và phương án tăng ổ hay xin Owner duyệt từng nhóm. Cấm tuỳ ý nâng TTL/cap, bỏ file khỏe hoặc sửa detector.

## 3. Khi và chỉ khi có ELIGIBLE + bốn lớp bảo vệ
Giữ VPS-GHI qua CAS cùng STARTED trước ghi; không tự gỡ khóa người khác. Đọc contract của vps-retention.sh/DOT/apply-v0 hiện hữu và bảo vệ footprint, không tự chế lệnh/công cụ mới.
Lưu exact PRE manifest, sha, refs, proven known-good và rollback. Nếu object chưa có encrypted Drive rescue: stream GPG theo tuyến đã PASS ở HEAL/H2, remote checksum/readback, giải mã kiểm khôi phục mẫu ở vùng cô lập/tạm được phép mà không tạo plaintext archive có secrets; thất bại => KEEP. Nếu đã có receipt hợp lệ không archive lại. Trước delete đối chiếu exact eligible path/id và không có open fd/live refs.
Chỉ gọi existing approved retention operator với selector chính xác, không trực tiếp rm/glob; nếu không có operator hỗ trợ, không xóa và báo thiếu. Sau từng thao tác kiểm df bytes, refs, logic sống, tránh phá audit/Graph/rollback. Lỗi MỚI do RUN => rollback đúng footprint/STOP.
Không sửa scripts/cron/PG/Directus/Graph/Docker, không sửa Guard/Kuma, không thay ngưỡng #11. Không thể đạt 45 bằng item hợp lệ => dừng an toàn và báo thiếu; không tự nâng scope.

## 4. POST & KQ
Đo df free before/after byte thực, 24h source slopes có cùng taxonomy/version, #11 actual reason, restore proof per object; 22 lights PRE/POST, website/API/Directus/PG/Graph/backup/Guard/08:00 ledger still functional. POST-PROTECT footprint Đ30/Đ31/watchdog/rollback, 0 ô thiếu. Guard toàn cục #22 cũ còn FAIL => KQ DỪNG·PARTIAL, không gửi receipt Telegram bypass hoặc tô xanh; lỗi mới => rollback.
Ghi BAO-CAO N2A-DISK-DRIVE-FIRST-20261014, KQ@VPSC-N2A-DISK-DRIVE-FIRST-20261014-01, Sổ P84 cập nhật đúng một nơi; trả VPS-GHI cùng commit nếu đã chiếm; 0 process/tệp tạm ngoài bằng chứng. Ghi rõ bytes thu THỰC, gap đến 45GiB, risk chưa đóng (sr-mow, backup code plaintext .env.working, #22, restore, O-R7-KEY) và MỘT bước kế. Không tự chạy L1b, N2b, Graph-clean hay xóa di sản khác.

</details>

---
## LỊCH SỬ — VPSC-L2D-GRAPH-PROTECT-MAP-20261014-01 · KQ XONG d0af7dd · KHÔNG THỰC HIỆN

# PROMPT — VPSC-L2D-GRAPH-PROTECT-MAP-20261014-01 · Đối chiếu Graph × luật KB × runtime trước khi xét tắt watchdog/di sản; CHỈ ĐỌC

RUN_ID: VPSC-L2D-GRAPH-PROTECT-MAP-20261014-01
Task: work/vps-clean-20-9-26 (VPSC), Owner D22–D27. Host GPT Chat, Reviewer Claude Chat B2, Worker Claude Code CLI; Owner chuyển tay.
Status: DRAFT P98 · Claude Reviewer ACCEPT (P99, đã thu hẹp phạm vi + nạp số đã đo), CHƯA READY, KHÔNG RUN. Chỉ thực hiện phần phía trên dòng LỊCH SỬ sau khi Reviewer ACCEPT và Host READY đúng SHA. Bước điều tra an toàn phục vụ L2(d) và các lượt kế, không mở task mới.
Chỉ được đọc VPS, Graph/PG/KB/log/config qua công cụ đọc được phép; chỉ ghi báo cáo đã ẩn dữ liệu nhạy cảm vào BAO-CAO.md, COLLAB.md bằng workspace_* đúng repo. Không sửa VPS/config/code/DB/cron/timer/flow/triggers/Kuma/Guard/KB/GDrive, không tạo tool, không lấy khóa, không chạy DOT gây ghi hay refresh dữ liệu, không gửi Telegram thử.
Nguyên văn Owner D27: «Trong quá trình thực thi, các bạn phải kiểm tra rất kỹ để tránh tắt nhầm các chức năng vẫn đang sử dụng. Lấy ví dụ như điều 30, 31, luật trong KB để bảo vệ những mã đã làm, tránh AI khác vô tình xóa nhầm. Các cơ chế kiểm soát và báo cáo tự động qua Telegram, các cơ chế giám sát, các cơ chế backup tự động xuống Google Drive. Tất cả những việc đó cần phải bóc tách rất kỹ bằng Grab, tránh việc tắt nhầm các chức năng này rồi lại mất công đi lần mò khôi phục lại.»

## 0. Đích, ranh giới, đánh dấu XONG
L2(a) context-pack OFF đúng một dòng qua apply-v0, crontab user incomex được canh; KQ bf06713 DỪNG·PARTIAL vì Guard #22 cũ làm thiếu Telegram receipt. Giữ kết quả kỹ thuật; không chạy lại L1/L1P/L2(a). L2(a) ở cửa sổ 11,99 giờ L1-only có birth_registry +64 seq_scan (~6,2 GiB) và system_issues (~3,8 GiB); 8 phút sau context-pack OFF birth_registry +0 còn system_issues đọc nhiều — chưa suy ra 24h. 21 cron L1 + context-pack là lịch sử đã OFF, không mặc nhiên chúng không bảo vệ gì.
Đích của RUN CHỈ ĐỌC: lập ma trận cụ thể chức năng ĐANG GIỮ và đường phụ thuộc từ luật KB/AGENTS tới executor, cron/flow, báo lỗi Telegram, snapshot/sao lưu GDrive; xác minh watchdog-monitor.sh, cron-integrity.sh, scanner-counts.sh, dot-context-pack-verify.sh, context-pack-retention và những bước liên quan L1 đã OFF; chọn đúng một ứng viên cải thiện kế tiếp có bằng chứng mà KHÔNG TẮT trong lượt này.
XONG khi có (a) ma trận bảo vệ kiểm được bằng chứng 4 nguồn + owner, (b) bảng KEEP/OFF_CANDIDATE/UNKNOWN từng đối tượng, (c) điểm ảnh hưởng nếu tắt và cách rollback, (d) PG/RAM/disk và mốc sau L2a đúng thời gian; (e) PROMPT DRAFT ứng viên kế tiếp hoặc BLOCKER rõ. 0 mutation VPS. Không giữ terminal chờ 3h/24h.
**Phạm vi (Reviewer P99 thu hẹp — không khảo sát toàn máy):** chỉ 3 nhóm: (1) **hồi tố** 22 dòng lịch đã OFF (21 L1 + 1 L2a) — mỗi dòng có nằm trên chuỗi bảo vệ nào ở A–E không; (2) **sống/chết** các chuỗi bảo vệ sau L1/L1P/L2a, mỗi chuỗi một dòng «last proof» (giờ + nguồn): Telegram cảnh báo + bản tin 08:00 hôm nay, Kuma push #22 (Guard), drift-check Config Guard, sổ mã INV23, backup pg/code/qdrant → GDrive (lần thành công cuối sau 13/10 15:00Z), trigger-guard/permissions-guard; (3) **5 ứng viên** watchdog-monitor · cron-integrity · scanner-counts · dot-context-pack-verify · flow Count Refresh. Ngân sách ≤ 45 phút; vượt thì ghi phần đã có + UNKNOWN, không kéo dài.
**Số Reviewer P99 đã đo 14/10 04:26Z (dùng lại, chỉ xác nhận nếu nghi):** (i) mốc 04:00Z không còn builder: `context_pack_requests` mới nhất vẫn 01:00Z, `birth_registry` seq_scan đứng 9.308 từ 01:01:08Z; (ii) PG đọc đĩa 01:12→04:26Z ≈ 566 khối/phút (L0 12.260 ⇒ ≈ −95%, chưa phải 24h), trong đó `system_issues` ≈ 64% (watchdog mỗi giờ qua REST) ≈ 3% mức L0; (iii) `trg_desc_guard`: 36 bảng governed, 21 có, 15 thiếu; `collection_registry` tạo mới cuối 2026-05-25 ⇒ việc «tự gắn cho bảng mới» của G1 không có dịp nào từ tháng 5; L1 chỉ comment lịch, không gỡ được trigger ⇒ 15 chỗ thiếu có TRƯỚC L1 (không phải hồi quy L1) — RUN chỉ cần đối luật description-guard hiện hành: loại trừ có chủ đích hay GAP cũ; (iv) RAM còn dùng được 6,0/12 GB (13/10: 4,4), swap 2,0/2,0 GB đầy, đĩa trống 38 GB (đích ≥ 45), tải 1,4/2,2/2,4 (13/10: 3,8/3,9/3,3).

## 1. Luật cứng
Đọc AGENTS.md (DROOT26/29/36/39/43/45/48/53), COLLAB gốc (VPS-GHI, NO_CONCURRENT), VPSC §0 D22–D27/Bảng/P95–P99/Sổ P84, BAO-CAO L0/L1/L1P/L2A; Graph task chỉ đọc mục trạng thái/phạm vi, không sửa task Graph.
Các đầu mối sống phải GIỮ: PG Census/ba lô; agent-data RAG và connectors; Graph production; Rule KB/AGENTS Đ30/Đ31; Config Guard+Protection Guard+DROOT29; bất kỳ scheduled checks/trigger guard/permission guard có chức năng thật; mã luật và sổ mã; Kuma/status-watch/Telegram alert + positive heartbeat 08:00; PG/db/code/Qdrant backup-to-GDrive, encryption, Drive-first restore/canary/retention, secret safety. Lark tạm giữ theo D25. Tên thuộc legacy không phải quyền OFF.
Dữ liệu KB có bản luật cũ, ví dụ knowledge/dev/laws/dieu31-system-integrity-law.md v1.2 nói WATCHDOG phải tự kiểm chính máy kiểm. Luật này không chứng minh watchdog-monitor.sh hiện nay là implementation đang có hiệu lực; phải tách tài liệu/phiên bản luật HIỆN HÀNH với cơ chế LIVE, có thể bị thay, và kiểm chứng enforcement thay thế thật. Không tự kết luận “đã có Guard mới nên bỏ được script cũ”.
Graph-v1 chỉ là INDEX bằng chứng: ghi version/timestamp/provenance, cạnh vào/ra, node absent; 0 cạnh KHÔNG có nghĩa 0 phụ thuộc. Phải kiểm thêm mã động, HTTP/Directus, lịch cron/systemd, nhật ký chạy/đèn, kiểm luồng thông báo và backup. Graph thiếu route hoặc snapshot cũ => UNKNOWN/KEEP, không “PASS”. Mọi đọc PG dùng DOT/query_pg chỉ đọc, không SELECT COUNT(*) bảng lớn. Không gọi scripts có side-effect, kể cả --help nếu mã có thể ghi, không dùng SSH ghi qua lối tắt.

## 2. Khảo sát trọng tâm — chứng minh LUỒNG, không quét máy tràn lan
A. Graph: đọc qua đường graph-v1 read-only (nếu lỗi dùng export có mốc tuổi), lấy node/cạnh và refs ID/filename cho từng nhóm Đ30/Đ31, KB law loader/agent prompt, Telegram alert sender + 08:00 heartbeat, Guard/INV, backup GDrive, watchdog/system_issues, context-pack verify; ghi rõ vùng Graph KHÔNG PHỦ (cron, dynamic SQL, Directus HTTP, Nuxt, process). Không sửa graph, không push nhãn LEGACY thủ công.
B. Code/cấu hình hẹp: tìm đúng tên/đường gọi tại scripts, dot/bin, code của agent-data, Nuxt, Graph, cấu hình cron root/incomex, /etc/cron.d, systemd timer, Directus flow thuộc phạm vi, source của backup. Chỉ lưu path:line/ID + digest, không đưa secrets/crontab raw vào Git. Kiểm script nào thực thi, script nào từng OFF, script nào chỉ còn là comment. Đọc sổ Config Guard/Protection Guard/INV15/16/20/23 và trạng thái target MATCH/UNKNOWN.
C. Luật KB: tra nguồn chính danh hiện hành của Điều 30 và 31, luật bảo vệ code trong KB/SSOT, đối chiếu thứ tự ưu tiên/phiên bản với AGENTS/DROOT29 và các luật cũ, chỉ kiểm đọc và xác định nơi runtime thực sự tải/cưỡng chế luật. Nếu chỉ tìm được văn bản luật mà không chứng minh enforcement thì UNKNOWN, không OFF checker. Phân biệt Luật bảo vệ tự giám sát với chức năng nghiệp vụ Registry/Governance đã nghỉ.
D. Telegram/giám sát: vẽ chuỗi sự kiện nguồn → phát hiện → registry 75 loại → Kuma/Guard → Telegram → last-delivered + message_id → lỗi/mất nhịp → fallback/08:00. #22 còn đỏ do INV5_6+INV20, một mismatch mới dễ bị chìm: không gọi full PASS và không gửi bypass. Bất kỳ đường canh/thông báo nào chỉ còn historical thì UNKNOWN, không tắt nguồn khác.
E. Backup Google Drive: đối chiếu các lịch pg-backup, backup-to-gdrive, code-backup-to-gdrive, qdrant-backup, vps-retention và backup staging; đường artifact encrypted → Drive → checksum/last success → restore proof đã có (KHÔNG làm restore mới, không tải secrets/plaintext, không tự thay retention). Kiểm chủ/nhịp/đường cảnh báo khi failed; nếu chưa có bằng chứng live → NEED_REMEDIATION, tuyệt đối không tắt.
F. Hai ứng viên bắt buộc: watchdog-monitor.sh và các script Điều 31 cũ (cron-integrity, scanner-counts); dot-context-pack-verify.sh vẫn chạy và retention context-pack. Rà 21 lịch L1 + 1 context-pack vừa OFF chỉ theo đường phụ thuộc đến A–E, không kiểm nguyên 22 lịch toàn văn nếu không có dấu. Với mỗi ứng viên trình bày chính xác ai gọi, người nhận output, nếu tắt mất gì, có cảnh báo thay thế nào chạy thật, lượng PG disk-read và CPU tiết kiệm đo được, chính xác hay ước, quyền Owner cần khi động đến bảo vệ. **Kiểm hồi tố trọng điểm L1 G1/G2:** dot-hc-executor đã OFF; BAO-CAO L1 ghi HC-TRIGGER không còn tự gắn trg_desc_guard cho bảng governed mới và H11a không tự sửa mô tả. Đối chiếu rõ luật KB knowledge/dev/laws/law-04-birth-process.md/description-guard và bản hiện hành: các bảo vệ đó có thuộc phần Owner D27 đòi GIỮ hay đã có executor thay thế chạy thật? Nếu còn phục vụ bảo vệ mã/dữ liệu mà không có tương đương hoạt động, đánh dấu GAP_CRITICAL → Host/Owner, đề xuất khôi phục đúng riêng chức năng qua apply-v0 với 4 ô Đ30/31; lượt này KHÔNG tự bật lại hay sửa DB.

## 3. Số đo và bảng kết quả
Đọc PG stats Tnew L2(a)=2026-10-14T03:04:43Z → Tcurrent (nêu giờ và stats_reset); mốc cron builder 04:00Z/07:00Z chỉ kiểm nếu thực sự đã qua, không ngồi chờ/khởi động builder; xác minh context_pack_requests không có đợt mới, birth_registry và system_issues seq_scan/disk blocks phân đoạn. Không gán toàn 99% scan 8 phút thành ngày. Đo RAM MemAvailable/swap churn/memory.events claude-kb, Directus, agent-data và đĩa #11 (nguồn tăng 24h lấy từ số storage-watch sẵn có, không `du` toàn đĩa); không tự nâng RAM hoặc đổi monitor.
Bảng đầu ra tối thiểu mỗi hàng: capability; tài liệu luật và trạng thái hiệu lực; runtime source + exact schedule/flow/service; Graph node/edge + freshness; code refs; consumer của nhóm GIỮ; Guard/Telegram/backup last proof; owner; rollback; trạng thái KEEP_CRITICAL / KEEP_UNKNOWN / OFF_CANDIDATE; lý do và evidence còn thiếu. Mục KHÔNG có đủ bằng chứng phải ghi UNKNOWN, không tự suy PASS.
Lập BAO-CAO mục L2-SAFETY-MAP-20261014, thêm bảng quyết định ở Sổ P84, KQ@VPSC-L2D-GRAPH-PROTECT-MAP-20261014-01 XONG|DỪNG dưới P98; nêu KQ chỉ-read, 0 mutation/0 background, không chiếm VPS-GHI nếu không cần write VPS. Không ghi raw secret, code không chứa khóa. Đề xuất duy nhất bước kế tiếp theo thứ tự: có GAP_CRITICAL do L1/L2a gây ⇒ khôi phục đúng riêng chức năng đó qua apply-v0 (4 ô); không có ⇒ chọn theo số giữa đĩa #11 (≥ 45 GiB, Drive-first D23) và L1b RAM/swap. L2(d) watchdog/Điều 31 cũ KHÔNG được đề xuất vì lý do tài nguyên (≈ 3% mức L0 < luật dừng 5%); chỉ đưa Owner gật/lắc nếu bằng chứng cho thấy đường canh mới (Kuma push #22 → Telegram) đã thay thật vai «máy canh máy kiểm» của luật Đ31, có DRAFT/rollback nếu phù hợp, Host+Reviewer quyết SHA sau.
Không tự READY/RUN bước kế, không tự tắt giám sát, backup hay luật trong KB.
---
## LỊCH SỬ — L2(a) VPSC-L2A-CTXPACK-CRON-OFF-20261014-01 KQ PARTIAL bf06713 · KHÔNG RUN LẠI

# PROMPT — VPSC-L2A-CTXPACK-CRON-OFF-20261014-01 · L2(a) đổi đích theo số đo: tắt 1 dòng lịch context-pack hỏng 100% từ 04/05 (nguồn đọc PG lớn nhất còn lại) + khoá crontab user vào Config Guard (D26) · không chạm Directus/flow/PG/mã

RUN_ID: VPSC-L2A-CTXPACK-CRON-OFF-20261014-01
Task: `work/vps-clean-20-9-26` (VPSC) · D22–D26 · bước L2(a) của STEP_WALK_V2. Không phải việc mới.
Soạn: Claude Chat P96 (B2 sau GPT P95). Thay bản nháp «tắt flow Count Refresh» của P95 vì số đo cho thấy flow không phải nguồn chính, và tắt flow cần DOT + ô canh chưa có (lý do đủ ở P96). Rà: GPT Chat Host B3 một lượt: ổn ⇒ READY đúng SHA; sửa nhỏ chỉ thêm kiểm thì sửa thẳng rồi READY (Claude chấp nhận trước).
Executor: Claude Code CLI, phiên MỚI trên Mac, qua `ssh contabo`. Ghi repo: Incomex MCP `workspace_*` root `workspace`.
Status: **DRAFT — Claude Reviewer ACCEPT (P96), chờ GPT Host READY đúng SHA last-touch**.
Bằng chứng: `/opt/incomex/work/vps-clean-20-9-26/VPSC-L2A-CTXPACK-CRON-OFF-20261014-01/` (`<EV>`; chỉ receipt đã làm sạch). Báo cáo: mục `L2A-20261014` trong `BAO-CAO.md` hiện có. Tiến độ + KQ: dưới P96 trong `COLLAB.md`. Không tạo tệp repo mới.
**Chỉ thực hiện phần trên dòng `LỊCH SỬ` đầu tiên.** Tham chiếu được nêu tên: §1 luật cứng + §2 S0 của bản lịch sử HEAL-01; trong `BAO-CAO.md`: mục `L1P-20261013` (§2 đăng ký `guard-registry`, dòng «Sửa lịch đúng đường», bảng coverage) và mục `L1-20261013` (tắt dòng lịch bằng tiền tố + bản sao).

## 0. Vì sao, và thế nào là XONG
Reviewer đo chỉ đọc 14/10 01:00–01:16Z (P96):
- PG giờ đọc theo đợt: 10 phút yên (01:02→01:12Z) cả DB `directus` chỉ +249 khối. Đợt lớn trùng giây với `dot-context-pack-build.sh` — chạy từ lịch của user `incomex` (sổ mã: `cron-cmd:incomex`) mỗi 3 giờ (01, 04, …, 22Z): đọc `context_trigger_sources` → `meta_catalog` → `COUNT(*)` `birth_registry` (1,22 triệu dòng) + `normative_registry` + `system_issues` (cùng giây 01:01:08) → `dot_tools` → rồi hỏng `pipeline exit 126`.
- `context_pack_requests`: lần dựng thành công cuối **2026-05-04 04:00Z**; từ đó **1.150 lượt, 100% hỏng**, `manifest_id` rỗng ⇒ 5 tháng không ra sản phẩm nào; tắt lịch không làm ai mất gì mới (gói cũ, nếu đang được đọc, giữ nguyên).
- `birth_registry` +43 lượt quét ở 15:27–22:33Z (3 lượt builder) và +15 ở 22:33–01:01Z (1 lượt) ⇒ ≈ 14 lượt quét mỗi lượt builder ≈ 40–50% khối PG đọc còn lại (ước; số 24h xác nhận). Flow Count Refresh chỉ đếm `birth_registry` 1 lần/6 giờ (log Directus 18:00:17 · 00:00:15) — không phải nguồn chính.
- Crontab user `incomex` CHƯA là đích Config Guard (L1P chỉ khoá crontab root + 5 tệp `/etc/cron.d`) ⇒ lỗ D26.
**XONG khi đủ cả 5:**
1. Đúng 1 dòng lịch có chuỗi `context-pack-build` bị tắt bằng tiền tố `#L2A-OFF-VPSC-L2A-CTXPACK-CRON-OFF-20261014-01 ` + 1 dòng biển báo; mọi dòng chạy khác (mọi crontab) giữ nguyên nội dung và số lượng.
2. `/var/spool/cron/crontabs/incomex` (và crontab user tự viết khác nếu S0.4 thấy, trừ của việc đang có cờ bận) là đích Config Guard, MATCH sau khi xong.
3. Đường sửa lịch qua `incomex-config-apply-v0` được dùng thật ít nhất 1 lần (lấp nợ L1P «chưa thử thật»); Guard `--coverage` cho footprint lượt này đủ 4 ô Đ30 · Đ31 · canh · lùi, 0 THIẾU.
4. Tpre (đầu RUN) và Tnew (cuối RUN) PG chỉ đọc: `pg_stat_database` (directus) + `pg_stat_user_tables`/`pg_statio_user_tables` của `birth_registry`, `system_issues`, `normative_registry`, `dot_tools`, `meta_catalog`, `context_pack_requests`; ghi cửa sổ L1-only T0 (13/10 14:57:19Z) → Tpre đúng số giờ, không gọi là 24h.
5. 22 đèn = PRE_RED_SET; agent-data `/health`, Directus ping, Nuxt `/knowledge/modules` 200; manifest context pack cuối = như S0.

## 0A. Quyền Owner — khối Owner dán PHẢI có nguyên 2 dòng này
Owner D25 (13/10/2026 20:59): «Xét cho cùng, toàn bộ hệ thống chỉ có mỗi phần nhỏ là: PG đếm PG (ba lo thông tin), agent data (RAG và các connector liên quan) và Graph là cần dùng, tất cả các phần đã triển khi trước đây như: govenance, khai sinh, Miếng thông tin, registries, pivot count, Lark (thì có thể tạm để) Đếu là những thứ có thể off được để tiết kiệm tài nguyên. Nhưng 1 số nội dung như bảo vệ điều 30, 31 thì vẫn cần dùng => vi vậy off theo chủ để rồi xem xét từng phần để tối ưu VPS nhé. Phần thực sự dùng chưa nhiều, nhưng tài nguyên đang bị chiếm dụng nhiều => làm sao bóc tách ra (nhờ graph) để off bớt nhé.»
Owner D26 (13/10/2026 22:25): «Cần nhắc là mọi thứ nên được bảo vệ bởi điều 30 31 tránh các AI làm hỏng mã của nhau nhé»

RUN này chỉ: tắt (đảo được) đúng 1 dòng lịch đã nêu + đăng ký bảo vệ crontab user + đo chỉ đọc. Không xoá tệp/mã/dòng PG, không sửa hay chạy `dot-context-pack-build.sh` hoặc tệp nào của context pack, không Directus/flow/trigger/Nuxt, không sửa Guard/Kuma, không rebaseline đích Config Guard sẵn có, không xoay khoá. Thiếu 1 trong 2 dòng trên hoặc thiếu Reviewer ACCEPT + Host READY đúng SHA PROMPT hiện tại ⇒ DỪNG trước STARTED.

## 1. Luật cứng
- Áp nguyên §1 của bản lịch sử HEAL-01 (VPS-GHI · báo từng bước · danh sách KHÔNG ĐƯỢC · bí mật · nghi ngờ thì giữ).
- **Đích định sẵn, agent không chọn:** chỉ dòng lịch có chuỗi `context-pack-build`. 0 hoặc > 1 dòng như vậy (xét mọi crontab), hoặc builder còn người gọi khác đang có lịch (S0.5) ⇒ DỪNG, ghi tệp + số thứ tự dòng (không in nội dung).
- Dòng nằm trong crontab root (đã canh) ⇒ chỉ sửa qua `incomex-config-apply-v0 --target-id cron-root-crontab` đúng dòng «Sửa lịch đúng đường» của BAO-CAO L1P; không dùng lệnh `crontab`.
- Dòng nằm trong crontab user `incomex` (chưa canh) ⇒ (a) đăng ký baseline hiện tại qua apply-v0 `guard-registry` TRƯỚC, (b) rồi đổi dòng qua apply-v0 với đích vừa đăng ký. apply-v0 không nhận tệp spool user (đọc `--help`/mã ở S0, không tự chế lệnh) ⇒ đổi bằng cách L1 (`crontab -u incomex -l` → tệp `<EV>` → `crontab -u incomex <tệp>`) rồi đăng ký baseline ngay sau trong cùng bước, ghi lý do.
- Giữ nguyên `/etc/cron.d/incomex-context-pack-retention` (đã canh, chỉ dọn gói cũ).
- 4 đích lệch cũ (#22 TQT/HJW) + INV20 giữ nguyên; không sửa Guard/Kuma để lấy PASS.
- Ngân sách ≤ 30 phút; không chờ lượt 3 giờ kế tiếp (Reviewer kiểm sau).

## 2. S0 — đọc + PRE (chỉ đọc)
1. Đọc `AGENTS.md` → COLLAB gốc (`VPS-GHI`) → VPSC COLLAB §0 (D25, D26) + P95–P96 → PROMPT này → `BAO-CAO.md` mục L1P-20261013 + L1-20261013.
2. Kiểm Reviewer ACCEPT + Host READY đúng SHA; khối Owner có 2 dòng §0A; §2 bước 2–3 của bản lịch sử HEAL-01 (sàn tài nguyên, Guard PRE + PRE_RED_SET); drift-check PRE (TOTAL · danh sách MISMATCH).
3. Tpre PG (§0 mục 4) + 3 dòng `context_pack_requests` mới nhất (giờ · trạng thái · lỗi) + manifest cuối (id · giờ).
4. Bảng crontab user: `/var/spool/cron/crontabs/*` → tệp · user · số dòng chạy · đã là đích Config Guard? · việc chủ · cờ bận (chỉ tên, không in nội dung). Dòng `context-pack-build`: tệp · số thứ tự · cột lịch. **Cổng D26 trước STARTED:** đọc mã/`--help` (read-only) và chứng minh `incomex-config-apply-v0` thực sự hỗ trợ đăng ký + thay đúng spool crontab user `incomex` bằng `--target-id` và expected baseline, bảo toàn owner/mode, khiến cron reload. Nếu không chứng minh được đường chuẩn này, **DỪNG trước mutation**, không dùng nhánh fallback `crontab -u` nêu ở §1 hoặc rebaseline sau sửa tay; ghi blocker cho Host xử lý ngoài RUN. Đây là điều kiện làm chặt theo D26, không mở quyền.
5. Người gọi khác của `dot-context-pack-build.sh` (chỉ tên): systemd unit/timer, script, DOT, tiến trình đang chạy. Có lịch khác ⇒ ghi → Host, KHÔNG tắt, DỪNG. Tiến trình đang chạy đúng lúc ⇒ đợi nó tự xong (≤ 2 phút) rồi mới làm §3.
6. Giữ `VPS-GHI` (CAS) + STARTED dưới P96 cùng commit trước mọi thay đổi.

## 3. Thực hiện
1. **Bản sao:** crontab chứa dòng → `<EV>/crontab-<user>.truoc` (sha) + bản spool nguyên quyền.
2. **Đăng ký** (nếu tệp chưa canh): apply-v0 `guard-registry` thêm `/var/spool/cron/crontabs/incomex` (+ tệp đủ điều kiện ở S0.4), baseline = sha hiện tại; `.pre` registry làm đường lùi; drift-check: đích mới MATCH.
3. **Tắt 1 dòng qua apply-v0:** ứng viên = bản hiện tại + tiền tố `#L2A-OFF-VPSC-L2A-CTXPACK-CRON-OFF-20261014-01 ` cho đúng dòng builder + 1 dòng biển báo đầu tệp: `# CONFIG GUARD từ <UTC> (VPSC-L2A-CTXPACK-CRON-OFF-20261014-01 · D25/D26 Owner): tắt lịch context-pack hỏng 100% từ 2026-05-04; bật lại = bỏ tiền tố qua incomex-config-apply-v0; sửa tay ⇒ #22 đỏ.` Kiểm trước nạp: diff đúng −1/+2, dòng chạy giảm đúng 1. Cron tự nạp ≤ 1 phút; đọc lại bằng `crontab -l -u <user>`.
4. **drift-check:** đích này MATCH baseline mới; danh sách MISMATCH cũ không dài thêm.
5. **Thử âm (Đ30):** fixture/selftest của drift-check như L1P (không sửa tay tệp thật); không có ⇒ «chưa thử âm» + lý do.
6. **Guard POST `--coverage`:** footprint lượt này (crontab đã sửa, registry) ⇒ 4 ô, 0 THIẾU.
7. **Biển báo chung:** thêm vào câu «LỊCH MÁY CÓ KHOÁ» ở dòng VPSC của COLLAB gốc: crontab user `incomex` (+ tệp khác nếu có) thuộc Config Guard từ <ngày>.
8. **Tnew + POST:** Tnew PG; 22 đèn = PRE_RED_SET; health 200 (agent-data, Directus ping, Nuxt `/knowledge/modules`); manifest cuối = S0.3; số dòng chạy các crontab khác = PRE.
9. **Báo cáo:** mục `L2A-20261014` trong BAO-CAO (cho Owner ≤ 3 dòng · bảng crontab user · diff · drift trước/sau · coverage 4 ô · Tpre/Tnew · «kiểm sau» ở §4) → `KQ@VPSC-L2A-CTXPACK-CRON-OFF-20261014-01 XONG|DỪNG · …` dưới P96 → **trả `VPS-GHI: trống` cùng commit**. Guard tổng PASS ⇒ gửi Telegram POST-PROTECT, lưu `message_id`; Guard tổng FAIL chỉ vì #22 cũ (INV5_6 4 đích TQT/HJW + INV20) ⇒ ghi «nợ receipt #22», KQ PARTIAL, KHÔNG lùi, không gửi Telegram ngoài đường Guard.
**Lỗi thì lùi — chỉ khi lỗi MỚI do lượt này** (apply-v0 lỗi · đích mới MISMATCH · đèn đỏ mới ngoài PRE_RED_SET · health ≠ 200 · dòng chạy khác đổi): crontab về bản `.truoc` qua apply-v0 (hoặc `crontab -u <user> <EV>/crontab-<user>.truoc` nếu tệp chưa đăng ký) + registry về `.pre` qua apply-v0; kiểm sha = PRE; KQ DỪNG nêu bước. Guard FAIL chỉ vì #22 cũ hoặc câu luân phiên #11 ⇒ PARTIAL, GIỮ thay đổi.
**Đồ tạm dự kiến (DROOT50 c):** `<EV>` (giữ có chủ đích) · thư mục ứng viên apply-v0 `/root/incomex-config-changes/<id>/` + baseline/`.pre` (giữ làm đường lùi) · 0 tiến trình nền · tệp tạm Mac xoá sau KQ.

## 4. Bước đi
| Bước | Việc | Bằng chứng | Lỗi thì |
|---|---|---|---|
| 1/5 S0 | đọc, PRE, Tpre, bảng crontab user, người gọi, giữ khoá | ảnh PRE, STARTED | DỪNG trước mọi thay đổi |
| 2/5 Bản sao + đăng ký | apply-v0 `guard-registry` | sha, registry `.pre` | lùi |
| 3/5 Tắt 1 dòng | apply-v0 đích crontab | diff −1/+2, dòng chạy −1 | lùi |
| 4/5 Kiểm | drift, thử âm, coverage, POST, Tnew | MATCH, 0 THIẾU, 22 đèn = PRE | lùi nếu lỗi mới; chỉ #22 cũ ⇒ PARTIAL, giữ |
| 5/5 KQ | BAO-CAO + KQ + biển báo chung + trả khoá | 0 tiến trình nền | — |

Sau RUN (không thuộc RUN này, không ai chờ): Reviewer ở lượt điều hành kế tiếp kiểm lượt 3 giờ kế (04:00Z/07:00Z…) KHÔNG sinh dòng `context_pack_requests` mới và `birth_registry` không còn đợt quét quanh :00–:01 của giờ đó; đọc L1 24h (T0→Tpre + Tpre→T+24h). Flow Count Refresh GIỮ tạm (ước ≤ 5–6%; muốn tắt cần DOT bật/tắt flow + ô canh flow — Guard ghi vùng U02 «Directus Flows chưa quét») ⇒ xét lại theo luật < 5% sau số 24h.

---

<details><summary>LỊCH SỬ — bản nháp L2(a) «tắt flow Count Refresh» (GPT P95, KHÔNG chạy — Claude P96 đổi đích theo số đo) — KHÔNG THỰC HIỆN</summary>

# (Lịch sử) PROMPT — VPSC-L2A-COUNT-FLOW-OFF-20261014-01 · ngừng một flow Directus di sản có kiểm D26
RUN_ID: VPSC-L2A-COUNT-FLOW-OFF-20261014-01
Task: work/vps-clean-20-9-26. Host GPT Chat; Reviewer Claude Chat; Executor Claude Code CLI, Owner tự dán.
STATUS: DRAFT B1/P95, CHƯA READY. Không tự RUN. Chỉ phần trước mục LỊCH SỬ là hiện hành. Mục này tiếp tục D25/D26, không mở task mới.

## 0. Mục tiêu / giới hạn
D25: ngừng theo chủ đề những Registry/Pivot/Matrix/Governance nghỉ dùng, GIỮ PG đếm PG (ba lô), agent-data RAG/connector, Graph và Điều 30/31 (Lark tạm giữ). L1 đã OFF 21 lịch. L1P đã đăng ký 6 config target; KQ DỪNG·PARTIAL vì Guard #22 đỏ cũ nên thiếu receipt Telegram, KHÔNG coi FULL PASS.
Ứng viên CHỈ MỘT FLOW: [DOT-REG] Count Refresh (6h), nghi POST vào /api/registry/refresh-counts làm đọc birth_registry và viết meta_catalog/v_registry_counts, ~49% PG disk read còn lại trong mẫu 7h (ước, CHƯA đủ chứng minh). Tuyệt đối không xóa các flow khác hoặc ngừng gì thuộc nhóm GIỮ. Chỉ chuyển flow này về trạng thái inactive/disabled có thể bật lại.
Đích: bắt đúng flow ID/triggers/source/consumer; đo PG và nguồn hoạt động trước/sau, dùng DOT và đủ bốn lớp Đ30/Đ31/canh/lùi cho đúng row flow; không đổi code/PG/trigger/cron đã tắt. Nếu không có DOT hoặc lớp Đ31 hợp lệ đang hoạt động thì DỪNG trước mutation, báo rõ blocker.

## 0A. Quyền Owner (khi phát RUN, Owner dán nguyên văn)
D25 (13/10): «Xét cho cùng, toàn bộ hệ thống chỉ có mỗi phần nhỏ là: PG đếm PG (ba lo thông tin), agent data (RAG và các connector liên quan) và Graph là cần dùng, tất cả các phần đã triển khi trước đây như: govenance, khai sinh, Miếng thông tin, registries, pivot count, Lark (thì có thể tạm để) Đếu là những thứ có thể off được để tiết kiệm tài nguyên. Nhưng 1 số nội dung như bảo vệ điều 30, 31 thì vẫn cần dùng => vi vậy off theo chủ để rồi xem xét từng phần để tối ưu VPS nhé. Phần thực sự dùng chưa nhiều, nhưng tài nguyên đang bị chiếm dụng nhiều => làm sao bóc tách ra (nhờ graph) để off bớt nhé.»
D26 (13/10 22:25): «Cần nhắc là mọi thứ nên được bảo vệ bởi điều 30 31 tránh các AI làm hỏng mã của nhau nhé»
Quyền chỉ cho phép tắt DI SẢN, không cho bypass DOT/Đ31 hoặc xoay key.

## 1. S0 chỉ đọc, fail closed
1. AGENTS.md (A4/A5/DROOT26/29/39) → root COLLAB/VPS-GHI → VPSC COLLAB D22–D26/P93–P96 + P95 → PROMPT đúng READY SHA → BAO-CAO L0/L1/L1P. Kiểm shared lock/no concurrent mutation, Guard PRE, các task TQT/HJW/GS. Không đủ gate ⇒ DỪNG trước STARTED.
2. Dùng DOT/query wrapper đã duyệt để tìm flow duy nhất theo tên + lịch sáu giờ, lấy exact ID/status/operations/triggers/schedule và audit; tuyệt đối không đọc/sửa DB bằng SQL/REST/Directus CLI trực tiếp. Nếu flow không duy nhất hoặc quyền owner không rõ thì giữ.
3. Đối chiếu Graph (không phủ hết Directus/Nuxt), mã nguồn endpoints và runtime caller. Nhóm GIỮ gồm PG Census/report-pg, agent-data, Graph, Guard/backup/Kuma/Lark; 0 consumer thực sự phụ thuộc thì flow được nghỉ, trang registry đứng yên là đúng; bất kỳ retained consumer/UNKNOWN thì GIỮ flow, nêu bằng chứng.
4. Tra Master DOT/Tool hiện có. Chứng minh bốn ô Đ30/Đ31/watchdog/rollback cho Directus flow ROW (không chỉ tệp chứng cứ); cần ongoing integrity/diff detector báo đúng flow trạng thái. DOT chưa đủ hoặc không bảo vệ được flow không cho mutation; chỉ lập phương án cải tiến công cụ tại task chủ.
5. Snapshot PG read-only: mốc L1 T0 2026-10-13T14:57:19Z và Tpre của chính RUN (stats_reset/epoch phải khớp), heap_blks_read/seq_scan/pg_stat của birth_registry/system_issues và bảng pivot/meta. Nếu Tpre <24h ghi L1-only window đúng số giờ, CHƯA gọi là 24h; tắt xong ghi Tnew, lập 24h sau Tnew; không trộn attribution. Đo RAM/swap/đĩa, health, PRE_RED_SET.
6. #22 INV5_6 (4 drift cũ TQT/HJW) + INV20 và receipt chưa có: phân biệt inherited vs new. Không khôi phục cảnh báo bằng rebaseline/bypass, không sửa chủ khác.

## 2. Mutation đúng một flow nếu S0 PASS
Giữ VPS-GHI bằng CAS + STARTED cùng commit. Backup flow configuration/ID/previous active status/operations/cron với checksum an toàn, không in secrets. Qua DOT đã có, chỉ đổi đúng state/schedule enabled→disabled của flow unique; không xóa flow, không sửa activity/history/111 flow khác, không direct SQL/REST/CLI, không đổi Nuxt/Graph/PG/docker. Có đường bật lại qua cùng DOT.
Readback bằng DOT: flow inactive, owner/status đúng, các operation không đổi; không cần gọi refresh-counts để thử (tránh tăng tải); smoke nhóm GIỮ (report-pg, agent-data connector, modules, Graph, Kuma, backup) và chú thích trang registry đã nghỉ. Nếu phát hiện retained consumer thất bại, rollback đúng flow ngay và KQ DỪNG.
POST-PROTECT với footprint thật row flow + DOT config liên quan: Đ30 regression, Đ31 integrity lâu dài, watchdog/selfcheck, rollback. Đủ 4 ô và PRE→POST same-or-better, không tạo đèn mới. Lỗi MỚI do RUN => rollback flow. Nếu Guard tổng vẫn FAIL chỉ do #22 cũ làm không gửi receipt, báo DỪNG·PARTIAL và giữ flow OFF khi các kiểm scoped PASS và D25 cho phép, không tô FULL XONG; cần Claude Reviewer xem rủi ro này trước READY. Không sửa Guard/Kuma để lấy PASS, không gửi Telegram ngoài đường đã duyệt.
## 3. KQ
Báo cáo L2A-20261014 (PG Tpre/Tnew, ID/status flow, mapping consumer, DOT/Đ31, rollback, có hay không receipt message_id, lỗi cũ/mới) và KQ@VPSC-L2A-COUNT-FLOW-OFF-20261014-01 XONG|DỪNG trong COLLAB; trả VPS-GHI cùng commit, dọn đồ tạm. Không có RUN mới ngoài L2(a). Sổ P84 giữ L1b RAM, L2(b–f), N2b key/502 Owner-only, #22 TQT/HJW, #11 disk và 08:00/24h.

</details>

---
## LỊCH SỬ — L1P-GUARD-CRON-20261013-01 KQ DỪNG·PARTIAL (9cc3080), KHÔNG THỰC HIỆN

# PROMPT — VPSC-L1P-GUARD-CRON-20261013-01 · Khoá lịch máy vào Config Guard (lấp ô Điều 31 của L1, theo D26) + đo chỉ đọc câu luân phiên Kuma #11 · không đổi dòng lịch nào đang chạy

RUN_ID: VPSC-L1P-GUARD-CRON-20261013-01
Task: `work/vps-clean-20-9-26` (VPSC) · mục tiêu D22–D25 + **D26 (Owner 13/10 22:25: mọi thứ phải được bảo vệ bởi Điều 30/31 để các AI không làm hỏng mã của nhau)**. Không phải việc mới.
Soạn: Claude Chat (P91, B2 sau KQ L1 + GPT B1). Rà: GPT Chat Host một lượt (B3): ổn ⇒ ACCEPT + READY đúng SHA; sửa nhỏ chỉ thêm kiểm thì sửa thẳng rồi READY (Claude chấp nhận trước).
Executor: Claude Code CLI, phiên MỚI trên Mac, qua `ssh contabo`. Ghi repo: Incomex MCP `workspace_*` root `workspace`.
Status: **Host ACCEPT thiết kế (P92) + Reviewer ACCEPT (P93) — chờ GPT Host READY đúng SHA last-touch**.
Bằng chứng: `/opt/incomex/work/vps-clean-20-9-26/VPSC-L1P-GUARD-CRON-20261013-01/` (`<EV>`; chỉ receipt đã làm sạch). Báo cáo: mục `L1P-20261013` trong `BAO-CAO.md` hiện có. Tiến độ + KQ: dưới P91 trong `COLLAB.md`. Không tạo tệp repo mới.
**Chỉ thực hiện phần trên dòng `LỊCH SỬ` đầu tiên.** Tham chiếu được nêu tên: §1 luật cứng + §2 S0 của bản lịch sử HEAL-01; mục L1-20261013 và mục R6 «3. Mutation thật» dòng M11 (đăng ký đích Config Guard qua `guard-registry`) trong `BAO-CAO.md`.

## 0. Mục tiêu và thế nào là XONG
Sau L1, lịch máy (crontab root) vẫn là chỗ bất kỳ AI nào sửa tay được mà không ai hay — đúng lỗ hở D26. Ví dụ: một phiên khác lỡ bỏ dấu `#` ở dòng matrix, máy lại quét 1,2 triệu dòng mỗi 10 phút mà không đèn nào đỏ. Lượt này đưa lịch máy vào Config Guard: sửa tay ⇒ drift-check thấy ⇒ #22 đỏ ⇒ Telegram; sửa đúng đường = `incomex-config-apply-v0` có bản lùi. **Không đổi dòng lịch nào đang chạy.**
**XONG khi đủ cả 5:**
1. Crontab root là đích Config Guard, baseline = sha hiện tại (sau L1 + 1 dòng biển báo §3 mục 2); drift-check một lượt ngay sau: đích mới MATCH.
2. Các tệp `/etc/cron.d/*` tự viết (không thuộc gói `dpkg -S`) chưa có trong Config Guard được đăng ký baseline như mục 1, trừ tệp của việc đang có cờ bận (ghi lại, không đăng ký).
3. Guard POST `--coverage` chạy lại cho footprint L1 (crontab root) và footprint lượt này: đủ 4 ô Điều 30 · Điều 31 · canh · lùi, **0 ô THIẾU**.
4. Kuma #11 (và #21) đọc chỉ đọc `kuma.db` (`mode=ro`) 48 giờ: tách nhịp push (câu do `kuma-push.sh` gửi) với nhịp Kuma tự ghi «No heartbeat in the time window»; khoảng cách lớn nhất giữa hai nhịp push liên tiếp so `interval`. Push đều ≤ interval ⇒ kết luận «hiển thị, không mất nhịp» kèm số; có khoảng > interval ⇒ mất nhịp thật, ghi giờ. **Không sửa Guard, không sửa Kuma.**
5. 22 đèn same-or-better (lý do #11 đánh giá theo mục 4); drift-check không thêm đích lệch mới ngoài các đích mới đăng ký; số dòng lịch đang chạy vẫn 32 và nội dung các dòng chạy không đổi.

## 0A. Quyền Owner — khối Owner dán PHẢI có nguyên dòng này
Owner D26 (13/10/2026 22:25): «Cần nhắc là mọi thứ nên được bảo vệ bởi điều 30 31 tránh các AI làm hỏng mã của nhau nhé»

RUN này chỉ ĐĂNG KÝ bảo vệ (baseline) + thêm 1 dòng chú thích biển báo trong crontab root + đo chỉ đọc. Không tắt/bật lịch, không sửa Guard/Kuma/DOT/mã, không PG/Directus, không rebaseline đích Config Guard sẵn có. Thiếu dòng này hoặc thiếu Reviewer ACCEPT + Host READY đúng SHA PROMPT hiện tại ⇒ DỪNG trước STARTED.

## 1. Luật cứng
- Áp nguyên §1 của bản lịch sử HEAL-01 (VPS-GHI · báo từng bước · danh sách KHÔNG ĐƯỢC · bí mật · nghi ngờ thì giữ).
- Config Guard chỉ qua `incomex-config-apply-v0` đúng cách R6 M11 đã làm (`guard-registry`): đọc cú pháp/`--help` ở S0, không tự chế lệnh, không sửa `registry.tsv` bằng tay; 4 đích đang lệch sẵn (INV5_6 của TQT/HJW) giữ nguyên, không rebaseline.
- Crontab root: chỉ thêm đúng 1 dòng chú thích (§3 mục 2) bằng cách như L1 (`crontab -l` → tệp `<EV>` → `crontab <tệp>`), làm TRƯỚC khi đăng ký baseline. Không đổi dòng nào khác.
- `/etc/cron.d`: chỉ đăng ký baseline, không sửa byte.
- `kuma.db` chỉ đọc; không in cấu hình kênh/token/chat id.
- Ngân sách ≤ 30 phút.

## 2. S0 — đọc + PRE (chỉ đọc)
1. Đọc `AGENTS.md` → COLLAB gốc (`VPS-GHI`) → VPSC COLLAB §0 (D25, D26) + P89–P93 (P92 Host · P93 Reviewer) → PROMPT này → `BAO-CAO.md` mục L1-20261013 + R6 dòng M11.
2. Kiểm Reviewer ACCEPT + Host READY đúng SHA; khối Owner có dòng §0A; §2 bước 2–3 của bản lịch sử HEAL-01 (sàn tài nguyên, Guard PRE + PRE_RED_SET); drift-check PRE (TOTAL · danh sách MISMATCH).
3. Crontab root hiện tại: sha phải = sha sau L1 (`94e90c41…`); khác ⇒ có ai sửa sau L1 ⇒ DỪNG, ghi số thứ tự dòng khác (không in nội dung).
4. Bảng `/etc/cron.d`: tệp · thuộc gói dpkg? · đã là đích Config Guard? · việc chủ · cờ bận của việc chủ.
5. Liệt kê (chỉ tên tệp) chương trình đang chạy theo lịch/systemd có tự ghi crontab (`crontab -`, ghi `/var/spool/cron`, ghi `/etc/cron.d`): có ⇒ ghi tên → Host; vẫn đăng ký (sửa tay bị lộ là đúng mục đích D26).
6. Giữ `VPS-GHI` + dòng STARTED dưới P91 cùng commit trước mọi thay đổi.

## 3. Thực hiện
1. **Bản sao:** `crontab -l > <EV>/crontab.truoc` (sha = mục S0.3) và giữ nguyên `/root/crontab.bak-VPSC-L1-CRON-OFF-20261013-01` của L1.
2. **Biển báo tại chỗ** — thêm đúng 1 dòng ngay dưới dòng nhãn L1: `# CONFIG GUARD từ <UTC> (VPSC-L1P-GUARD-CRON-20261013-01 · D26 Owner): tệp này được canh — sửa qua incomex-config-apply-v0; sửa tay ⇒ đèn #22 đỏ. Bật lại dòng #L1-OFF cũng phải đi đường này.` → nạp → ghi sha mới; dòng chạy vẫn 32.
3. **Đăng ký Config Guard** qua `incomex-config-apply-v0` `guard-registry`: đích crontab root (baseline = sha mục 2) + các tệp `/etc/cron.d` đủ điều kiện ở S0.4; bản `.pre` của registry làm đường lùi.
4. **drift-check một lượt:** các đích mới MATCH; danh sách MISMATCH cũ không dài thêm.
5. **Thử âm (Điều 30 — canh có thật):** chỉ khi drift-check có chế độ thử/fixture trên tệp tạm (không bao giờ sửa tay tệp thật để thử); không có ⇒ ghi «chưa thử âm» kèm lý do.
6. **Guard POST `--coverage`:** footprint L1 (crontab root) + footprint lượt này (crontab root, registry Config Guard) ⇒ 4 ô đủ, 0 THIẾU.
7. **Kuma #11/#21:** đo theo §0 mục 4; bảng: giờ · loại nhịp (push/tự ghi) · trạng thái · câu (cắt 60 ký tự, không token).
8. **Biển báo cho mọi việc khác:** thêm một câu vào dòng VPSC ở COLLAB gốc: «crontab root + `/etc/cron.d/<danh sách>` thuộc Config Guard từ <ngày> — sửa qua apply-v0, sửa tay ⇒ #22 đỏ».
9. **Git cục bộ `/opt/incomex`:** commit dòng nhãn DEL-1 L1 đã thêm vào `docs/KE-HOACH-XOA-20260801.md` (message có RUN_ID L1 + RUN_ID này); chỉ tệp đó. Chỉ commit nếu đối chiếu đúng chủ cây/HEAD và diff chỉ có một dòng nhãn L1; nếu có thay đổi khác hoặc cây đang được phiên khác ghi ⇒ GIỮ, ghi con trỏ về chủ, không commit hộ.
10. **POST:** 22 đèn same-or-better; agent-data `/health`, Directus ping, Nuxt `/knowledge/modules` 200; dòng lịch chạy 32. Nếu Guard vẫn trả `same_or_better=FAIL` hoặc coverage còn THIẾU thì không tự suy PASS từ cùng tập đèn đỏ; báo DỪNG/PARTIAL có bằng chứng, không chạy lại chỉ để canh câu. Phải chứng minh nhịp Kuma thật, không làm xanh giả.
11. **Báo cáo:** mục `L1P-20261013` trong BAO-CAO (cho Owner ≤ 3 dòng · bảng đích Config Guard mới · drift-check trước/sau · bảng coverage 4 ô cho L1 và lượt này · kết luận Kuma có số) → `KQ@VPSC-L1P-GUARD-CRON-20261013-01 XONG|DỪNG · …` dưới P91 → **trả `VPS-GHI: trống` cùng commit**. Báo Owner đúng một dòng. Khi POST-PROTECT phạm vi PASS, gửi Telegram receipt theo DROOT29 và lưu `message_id`; gửi lỗi thì KQ DỪNG/PARTIAL, không nhận full XONG. Guard tổng FAIL từ các đích #22 cũ phải phân biệt riêng, không che.
**Lỗi thì lùi:** registry Config Guard về bản `.pre` qua apply-v0; crontab về `<EV>/crontab.truoc` (chỉ mất dòng biển báo); kiểm sha = PRE; KQ DỪNG nêu bước. **Chỉ lùi khi có lỗi MỚI do chính L1P gây** (apply-v0 báo lỗi · đích mới MISMATCH · đèn đỏ mới ngoài PRE_RED_SET · health ≠ 200 · dòng chạy ≠ 32 hoặc nội dung dòng chạy đổi). Nếu chỉ còn Guard `same_or_better=FAIL` vì #11 luân phiên câu với tập đỏ = PRE_RED_SET, hoặc coverage còn ô THIẾU mà lượt này không làm được ⇒ **GIỮ** đăng ký + biển báo (lùi = mất chính lớp canh D26 cần), KQ PARTIAL nêu ô/câu kèm số Kuma — đúng P92 «Ranh giới».

## 4. Bước đi
| Bước | Việc | Bằng chứng | Lỗi thì |
|---|---|---|---|
| 1/5 S0 | đọc, PRE, drift-check PRE, bảng cron.d, giữ khoá | ảnh PRE, STARTED | DỪNG trước mọi thay đổi |
| 2/5 Biển báo + đăng ký | 1 dòng chú thích, apply-v0 guard-registry | sha, registry `.pre` | lùi |
| 3/5 Kiểm | drift-check, thử âm, Guard coverage 4 ô | 0 THIẾU, đích mới MATCH | lùi nếu lỗi mới do L1P; chỉ FAIL câu #11 / ô THIẾU ngoài tầm ⇒ PARTIAL, giữ |
| 4/5 Kuma + biển báo chung + git | đo #11/#21, dòng COLLAB gốc, commit nhãn DEL-1 | bảng nhịp | ghi UNKNOWN, không đoán |
| 5/5 KQ | BAO-CAO + KQ + trả khoá | 0 tiến trình nền | — |

Sau RUN (không thuộc RUN này): Reviewer đọc `pg_stat` 24h từ T0 của L1 (14:57:19Z 13/10) → Host chọn L1b (trần RAM) hoặc L2 theo chủ đề; mọi lượt sau giữ luật D26: thứ sắp đổi phải có đủ 4 ô Điều 30/31 trong cùng RUN.

---

<details><summary>LỊCH SỬ — L1 VPSC-L1-CRON-OFF-20261013-01 (READY 91334aa8, đã chạy 13/10 14:56–15:17Z, KQ XONG 21/21) — KHÔNG THỰC HIỆN</summary>

# (Lịch sử) PROMPT — VPSC-L1-CRON-OFF-20261013-01 · Tắt theo chủ đề, đợt 1: 21 dòng LỊCH di sản (Pivot/đếm + Governance/APR/heal) · chỉ crontab, không chạm PG/Directus/mã

RUN_ID: VPSC-L1-CRON-OFF-20261013-01
Task: `work/vps-clean-20-9-26` (VPSC) · mục tiêu D22–D24 + **D25 (Owner 13/10 20:59: chỉ giữ PG đếm PG/ba lô, agent-data RAG + connector, Graph và bảo vệ Đ30/31; Lark tạm giữ; governance · khai sinh · miếng thông tin · registries · pivot count off theo chủ đề)**. Không phải việc mới.
Soạn: Claude Chat (P89, B2 theo P88). Rà: GPT Chat Host một lượt (B3): ổn ⇒ ACCEPT + READY đúng SHA; sửa nhỏ thì sửa thẳng rồi READY.
Executor: Claude Code CLI, phiên MỚI trên Mac, qua `ssh contabo`. Ghi repo: Incomex MCP `workspace_*` root `workspace`.
Status: **DRAFT — chờ GPT ACCEPT+READY**.
Bằng chứng: `/opt/incomex/work/vps-clean-20-9-26/VPSC-L1-CRON-OFF-20261013-01/` (gọi tắt `<EV>`; chỉ receipt đã làm sạch). Báo cáo: mục `L1-20261013` trong `BAO-CAO.md` hiện có. Tiến độ + KQ: dưới P89 trong `COLLAB.md`. Không tạo tệp repo mới.
**Chỉ thực hiện phần trên dòng `LỊCH SỬ` đầu tiên.** Tham chiếu được nêu tên: §1 luật cứng + §2 S0 của bản lịch sử HEAL-01; bảng lịch `l0/cron.txt` và Bảng A/B của L0 (`BAO-CAO.md · L0-20261013`).

## 0. Mục tiêu và thế nào là XONG
Ngừng các việc định kỳ của chủ đề di sản đang đốt tài nguyên mà không phục vụ phần đang dùng: theo L0, hai việc quét `birth_registry` (lịch matrix) và `system_issues` (lịch hc-executor) chiếm 98% khối PG phải đọc ngoài bộ đệm; lịch pivot ghi đè 150 dòng mỗi 10 phút. Chỉ tắt LỊCH (đảo được trong 10 giây); trigger, bảng, flow, mã, dữ liệu giữ nguyên.
**XONG khi đủ cả 6:**
1. Đúng các dòng bảng T (§3) đã thành chú thích với tiền tố `#L1-OFF-VPSC-L1-CRON-OFF-20261013-01 ` + đúng 1 dòng nhãn đầu crontab; không dòng nào khác đổi (diff = số dòng T đã tắt + 1).
2. 2 dòng Guard `CRON_EXACT` (`disk-monitor.sh`, `mcpw-protection-guard periodic`) còn nguyên văn, đúng 1 lần; mọi dòng bảng K còn chạy; mọi dòng `CRON_TZ=` giữ nguyên chỗ.
3. Một chu kỳ 10 phút sau khi nạp (≤ 12 phút, ngoài giờ máy 02 và 20 — giờ lịch cũ vốn nghỉ): delta `pivot_results.n_tup_upd` = 0, `meta_catalog.n_tup_upd` = 0, `v_registry_counts.n_tup_ins` = 0, `birth_registry.seq_scan` = 0 (L0: ~150 · ~18 · ~185 · ~6 mỗi 10′). Rơi vào giờ 02/20 ⇒ không chờ: ghi `quan sát rơi giờ nghỉ`, dựa mục 1 + Reviewer đọc 24h.
4. Bản sao `/root/crontab.bak-VPSC-L1-CRON-OFF-20261013-01` có sha256 = crontab lúc PRE; lệnh bật lại ghi sẵn trong BAO-CAO.
5. Guard POST `--coverage` + 22 đèn same-or-better so PRE_RED_SET; agent-data `/health`, Directus ping, Nuxt `/knowledge/modules` 200, Graph đọc được; trang registries/pivot vẫn 200 (số đứng yên là trạng thái đúng của chủ đề đã tắt).
6. Mốc T0 `pg_stat_user_tables` (DB `directus`) ghi vào `<EV>` để Reviewer tự đọc hiệu quả 24h từ bộ đếm cộng dồn — không ai ngồi chờ.

## 0A. Quyền Owner — khối Owner dán PHẢI có nguyên dòng này
Owner D25 (13/10/2026 20:59): «tất cả các phần đã triển khi trước đây như: govenance, khai sinh, Miếng thông tin, registries, pivot count, Lark (thì có thể tạm để) Đếu là những thứ có thể off được để tiết kiệm tài nguyên. Nhưng 1 số nội dung như bảo vệ điều 30, 31 thì vẫn cần dùng => vi vậy off theo chủ để rồi xem xét từng phần để tối ưu VPS nhé.»

RUN này chỉ tắt LỊCH (crontab root) của hai chủ đề Pivot/đếm và Governance/APR/heal. Không tắt trigger/bảng/view/flow, không sửa DOT/script/mã, không xoá dữ liệu. Thiếu dòng này hoặc thiếu Reviewer ACCEPT + Host READY đúng SHA PROMPT hiện tại ⇒ DỪNG trước STARTED.

## 1. Luật cứng
- Áp nguyên §1 của bản lịch sử HEAL-01 (VPS-GHI · báo từng bước · danh sách KHÔNG ĐƯỢC · bí mật · nghi ngờ thì giữ).
- Chỉ đổi crontab root theo đúng §4: `crontab -l` → tệp trong `<EV>` → thêm tiền tố đúng dòng → `crontab <tệp>`. Không sửa `/etc/cron.d/*`, không sửa tệp DOT/script, không PG DDL/DML, không Directus, không restart, không đụng Graph.
- Nhận diện dòng bằng **khoá = cột lịch + chuỗi đặc trưng** ở bảng T; mỗi khoá phải khớp **đúng 1 dòng đang chạy** (không bắt đầu bằng `#`). Khớp 0 hoặc > 1 ⇒ GIỮ dòng đó, ghi lý do, làm tiếp dòng khác. Không tự thêm dòng ngoài bảng T.
- Bí mật: vài dòng crontab chứa lệnh đọc tệp khoá; repo và báo cáo chỉ ghi số thứ tự, khoá, sha256 của dòng — không in nguyên dòng, không in giá trị khoá/biến.
- Ngân sách ≤ 30 phút (cộng tối đa 12 phút quan sát mục 3).

## 2. S0 — đọc + PRE (chỉ đọc)
1. Đọc `AGENTS.md` → COLLAB gốc (`VPS-GHI`) → VPSC COLLAB §0 (D24, D25) + P88 + P89 → PROMPT này → `BAO-CAO.md` mục L0-20261013 (Bảng A/B, mục 5–6) + `l0/cron.txt` của L0.
2. Kiểm Reviewer ACCEPT + Host READY đúng SHA; khối Owner có dòng §0A; làm §2 bước 2–3 của bản lịch sử HEAL-01 (sàn tài nguyên, Guard PRE + PRE_RED_SET).
3. **Bóc tách 3 nguồn cho từng dòng T (chỉ đọc, chỉ in tên tệp/nút):** (i) **Graph** — qua đường đọc graph-v1 (đầu nối lỗi ⇒ bản xuất `/opt/incomex/graph-server/prod-v1/backups/export/graph-v1-{nodes,rels}.jsonl`): với mỗi DOT/hàm ở bảng T, liệt kê cạnh VÀO từ nút thuộc nhóm giữ (mã agent-data, graph-server, claude-mcp, Guard/kuma-push/storage-watch, ba lô) ⇒ kỳ vọng 0; ghi rõ Graph chưa phủ cron/SQL dựng chuỗi/Directus HTTP/Nuxt. (ii) **Mã** — tìm tên DOT/hàm trong đúng các thư mục giữ: `/opt/incomex/docker/agent-data-repo/agent_data`, `/opt/incomex/claude-mcp`, `/opt/incomex/graph-server`, `scripts/mcpw-protection-guard`, `scripts/kuma-push.sh`, `scripts/storage-watch.py`, `/opt/incomex/docker/nuxt-repo/web/server` trừ `api/registry*`/`api/registries*` (`nice -n 19 ionice -c3`, chỉ tên tệp) ⇒ kỳ vọng 0 (Claude P89 đo 0). (iii) **Tin báo** — `logs/bang-den.json` khoá `tin_bao`: 0 loại tin có nguồn là dòng T (P89 đo 0/75). Dòng nào có tham chiếu từ nhóm giữ ⇒ GIỮ dòng đó, ghi `→ Host`.
4. Ảnh PRE vào `<EV>`: `crontab -l` sha256 + bản sao; T0 `pg_stat_user_tables` cho `pivot_results`, `meta_catalog`, `v_registry_counts`, `v_registry_summary`, `birth_registry`, `system_issues`, `approval_requests` (+ `pg_statio_user_tables` hai bảng nóng); danh sách `system_health_checks` đang bật (code · tên · executor_type, không in SQL/ngưỡng) để L2 biết đã ngừng kiểm gì. **Cổng G1/G2 (KHÔNG bỏ qua):** đối chiếu các `system_health_checks` đang bật với executor/verify và chủ đích bảo vệ hiện còn sử dụng (Guard Đ30/31, agent-data/connector, Graph, PG ba lô, backup, cảnh báo). Đọc qua DOT/wrapper chỉ đọc, chỉ lưu tên/mã/trạng thái, không in SQL/literal/secrets. Nếu G1/G2 còn thực thi ít nhất một kiểm tra thiết yếu của nhóm GIỮ hoặc chưa chứng minh hết phụ thuộc thì **GIỮ cả G1/G2** (không tắt cặp này), ghi lý do; các dòng T độc lập vẫn được xét riêng. `0/75` loại tin Telegram không phải bằng chứng đủ để bỏ bộ thực thi kiểm tra sức khỏe.
5. Giữ `VPS-GHI` + dòng STARTED dưới P89 cùng commit trước mọi thay đổi (cú pháp như §2 bước 4 HEAL-01).

## 3. Bảng T — dòng tắt (21) · Bảng K — dòng giữ
| # | Chủ đề · DEL-1 | Cột lịch | Chuỗi đặc trưng | Tốn gì (L0) |
|---|---|---|---|---|
| P1 | Pivot/đếm · Bộ 2–3 | `3-59/10 * * * *` | `refresh_meta_catalog_from_pivot()` | 18 dòng `meta_catalog`/lượt + 10 trigger chuỗi đếm |
| P2 | Pivot · Bộ 3 | `7-59/10 * * * *` | `refresh_pivot_results()` | ghi đè 150 dòng/lượt (~22.000/ngày) |
| P3 | Pivot/orphan · Bộ 3 | `5-59/10 * * * *` | `fn_refresh_orphan_species()` | 1 `docker exec` + 4 hàm/10′ |
| P4 | Matrix · Bộ 3 | `9-59/10 * * * *` | `refresh_matrix_results()` | 6 lần quét `birth_registry`/lượt = 42% khối PG đọc |
| P5 | Pivot · Bộ 3 | `0 4 * * *` | `/dot/bin/dot-pivot-health ` | kiểm sức khoẻ P1–P4 |
| P6 | Matrix · Bộ 3 | `5 4 * * *` | `/dot/bin/dot-matrix-health ` | như P5 |
| P7 | Đếm · Bộ 4 | `30 3 * * *` | `/dot/bin/dot-accuracy-verify ` | sửa `record_count` của `meta_catalog` |
| G1 | Heal · Bộ 1–2 | `0 */3 * * *` | `/dot/bin/dot-hc-executor >>` | phần lớn 56% khối PG đọc (`system_issues`) |
| G2 | Heal | `30 */3 * * *` | `/dot/bin/dot-hc-executor-verify ` | kiểm cặp của G1 |
| G3 | Orphan · Bộ 1,2,4 | `30 2 * * *` | `/dot/bin/dot-orphan-scanner ` | quét `birth_registry` |
| G4 | Phân loại · Bộ 2,4 | `0 3 * * 0` | `/dot/bin/dot-misclass-scanner ` | phân loại loài — Owner đã bỏ cách phân loại này (việc pg-nhan-balo) |
| G5 | APR · Bộ 4 | `0 5 * * *` | `fn_expire_stale_approvals()` | APR ngủ từ 23/07 |
| G6 | APR · Bộ 4 | `30 4 * * *` | `auto_apply_approval()` | như G5; còn 2 yêu cầu `approved` chưa áp — tắt để không tự áp |
| G7 | APR · Bộ 4 | `30 4 * * *` | `/dot/bin/dot-apr-health` | |
| G8 | Sổ DOT · Bộ 4 | `0 3 * * *` | `/dot/bin/dot-dot-health ` | |
| G9 | Registry · Bộ 1–2 | `0 4 * * *` | `/dot/bin/dot-collection-health` | còn lỗi SQL (bảng/cột đã bỏ) |
| G10 | Governance · Bộ 4 | `0 5 * * *` | `/dot/bin/dot-gov-verify ` | |
| G11 | Normative · Bộ 4 | `0 5 * * *` | `/dot/bin/dot-nrm-verify ` | |
| G12 | Normative · Bộ 4 | `30 5 * * *` | `/dot/bin/dot-nrm-sync ` | |
| G13 | Normative · Bộ 4 | `0 6 * * *` | `/dot/bin/dot-nrm-lifecycle ` | |
| G14 | Normative · Bộ 1,4 | `0 4 * * 0` | `/dot/bin/dot-nrm-discover ` | |

**Bảng K — GIỮ, không đụng, kiểm còn chạy sau RUN:** `disk-monitor.sh` + `mcpw-protection-guard periodic` (Guard `CRON_EXACT`) · `db-permissions-guard` · `env-permissions-guard` · bộ «Điều 31» cũ `cron-integrity.sh` · `watchdog-monitor.sh` · `scanner-counts.sh` (LOCKED; Owner giữ Đ30/31 — L2 xét riêng) · `dot-trigger-guard` (bảo vệ trigger Tier A) · `run-sr-mow.sh` (Đ30/31 MOW) · backup (`pg-backup`, `backup-to-gdrive`, `code-backup-to-gdrive`, `qdrant-backup`, dòng 04:17) · `git-push-gh-daily-v2` · `test-mcp-connectivity` · `reconcile-tasks` · `reconcile-knowledge` · `dot-kb-verify.sh` · `dot-api-health.sh` · `dot-vector-audit` · `dot-sync-orphan-scan` · `cdn-cache-warm` · `phai-cu/cron.sh` · `dot-dot-coverage` · `dot-doc-partition` · `dot-script-lint` (nhãn «CHẠM: KHÔNG» — L2) · mọi dòng `CRON_TZ=` · toàn bộ `/etc/cron.d/*`.

## 4. Thực hiện
1. **Bản sao:** `crontab -l > <EV>/crontab.truoc` và `cp` thành `/root/crontab.bak-VPSC-L1-CRON-OFF-20261013-01`; sha256 hai bản = nhau.
2. **Soạn bản sau** `<EV>/crontab.sau` từ `crontab.truoc`: mỗi dòng T khớp đúng 1 ⇒ thêm tiền tố `#L1-OFF-VPSC-L1-CRON-OFF-20261013-01 `; chèn đúng 1 dòng đầu tệp: `# L1-OFF VPSC-L1-CRON-OFF-20261013-01 <UTC> · D25 Owner 13/10 · tắt LỊCH chủ đề Pivot/đếm + Governance/APR/heal (DEL-1 Bộ 1–4) · trigger/bảng/flow/mã CHƯA đổi · bật lại: crontab /root/crontab.bak-VPSC-L1-CRON-OFF-20261013-01 hoặc bỏ tiền tố từng dòng`.
3. **Kiểm trước khi nạp:** `diff` chỉ gồm các dòng T đã khớp + 1 dòng nhãn; 2 dòng `CRON_EXACT` có trong bản sau nguyên văn đúng 1 lần; số dòng không chú thích = trước − số dòng T đã tắt. Sai ⇒ không nạp, KQ DỪNG.
4. **Nạp:** `crontab <EV>/crontab.sau`; `crontab -l | sha256sum` = sha của bản sau.
5. **Quan sát một chu kỳ** (§0 mục 3): T1 ngay sau nạp, T2 sau mốc phút `:x9` kế tiếp; không còn tiến trình `docker exec … refresh_` mới. Bộ đếm còn nhảy ⇒ lùi (§4 mục 9).
6. **Nhãn tại chỗ:** thêm 1 dòng trạng thái vào mục lộ trình của `/opt/incomex/docs/KE-HOACH-XOA-20260801.md`: `<UTC> · VPSC L1 VPSC-L1-CRON-OFF-20261013-01: bước 4, lớp LỊCH, đợt 1 — <n> dòng cron Bộ 1–4 TẮT (đảo được) theo D25; trigger/bảng/flow CHƯA · bật lại: crontab /root/crontab.bak-VPSC-L1-CRON-OFF-20261013-01`. Tệp thuộc Config Guard ⇒ không sửa, ghi lý do vào BAO-CAO.
7. **POST:** Guard POST `--coverage` (footprint thật: crontab root + tệp nhãn) + 22 đèn + health ở §0 mục 5 ⇒ same-or-better so PRE_RED_SET.
8. **Bảng Đ30/31 (R4) cho thành phần «crontab root»:** Hồi quy = diff đúng + 0 dòng T còn chạy + bộ đếm §0 mục 3 · Toàn vẹn = Guard INV15 dòng lịch + `cron.root.sha` PRE→POST trong footprint · Canh = Guard periodic + 22 đèn Kuma · Lùi = `/root/crontab.bak-…` (sha = PRE), lệnh `crontab /root/crontab.bak-VPSC-L1-CRON-OFF-20261013-01`.
9. **Lỗi thì lùi:** mục 3/4/5/7 hỏng hoặc có đèn mới đỏ do RUN ⇒ `crontab /root/crontab.bak-VPSC-L1-CRON-OFF-20261013-01` ngay, kiểm sha = PRE, KQ DỪNG nêu bước.
10. **Báo cáo:** mục `L1-20261013` trong BAO-CAO (cho Owner ≤ 3 dòng · bảng T từng dòng TẮT/GIỮ + lý do · T0/T1/T2 · kết quả bóc tách 3 nguồn · bảng Đ30/31 · danh sách health check đã ngừng) → dòng `KQ@VPSC-L1-CRON-OFF-20261013-01 XONG|DỪNG · …` dưới P89 → **trả `VPS-GHI: trống` cùng commit**. Báo Owner đúng một dòng.

## 5. Bước đi
| Bước | Việc | Bằng chứng | Lỗi thì |
|---|---|---|---|
| 1/5 S0 | đọc, bóc tách 3 nguồn, PRE + T0, giữ khoá | ảnh PRE, STARTED | DỪNG trước mọi thay đổi |
| 2/5 Soạn | bản sao + `crontab.sau` + kiểm diff | diff, sha | không nạp, DỪNG |
| 3/5 Nạp + quan sát | nạp, một chu kỳ 10′ | 4 bộ đếm = 0 | lùi bản sao |
| 4/5 POST | Guard coverage, 22 đèn, health, nhãn DEL-1 | coverage same-or-better | lùi bản sao |
| 5/5 KQ | BAO-CAO + KQ + trả khoá | 0 tiến trình nền | — |

Sau RUN (không thuộc RUN này): Reviewer đọc `pg_stat` 24h từ T0 (bộ đếm cộng dồn, không ai chờ) → Host chọn L1b (trần RAM theo số mới) hoặc L2 theo chủ đề (P89).

</details>

<details><summary>LỊCH SỬ — HEAL02+L0 VPSC-HEAL02-L0-20261013-01 (READY b8ee714e, đã chạy 13/10: Phần 1 DỪNG · Phần 2 XONG) — KHÔNG THỰC HIỆN</summary>

# (Lịch sử) PROMPT — VPSC-HEAL02-L0-20261013-01 · Phần 1: xong việc dở của HEAL (#11 xanh thật) · Phần 2: đo tải + soát di sản theo kế hoạch DEL-1 (CHỈ ĐỌC)

RUN_ID: VPSC-HEAL02-L0-20261013-01
Task: `work/vps-clean-20-9-26` (VPSC) · mục tiêu D22/D23 + **D24 (Owner 13/10: tối ưu VPS, nâng trần RAM, chạy nhanh hơn, tắt dần di sản khai sinh · registry · pivot đếm, dùng Graph)**. Không phải việc mới.
Soạn: Claude Chat theo lệnh Owner 13/10 16:58 +07 (P84). Rà: GPT Chat (Host, khác hãng) **một lượt**: lỗi nhỏ thì sửa thẳng DRAFT rồi ACCEPT + READY đúng SHA cùng commit; vấn đề lớn thì PARTIAL đúng 1 blocker.
Executor: Claude Code CLI, phiên MỚI trên Mac, qua `ssh contabo`. Ghi repo: Incomex MCP `workspace_*` root `workspace`. Cấu hình được bảo vệ: chỉ `incomex-config-apply-v0`.
Status: **DRAFT r2 — GPT Host đã rà 1 lượt (`cf3a67e4`, 5 sửa); Claude P85 giữ 4, sửa lại L0-2 (iii) vì `query_id` luôn NULL + cửa sổ 2 phút không gặp đợt quét; chờ GPT ACCEPT+READY đúng SHA**.
Bằng chứng: `/opt/incomex/work/vps-clean-20-9-26/VPSC-HEAL02-L0-20261013-01/` (chỉ receipt đã làm sạch). Báo cáo: hai mục `HEAL02-20261013` và `L0-20261013` trong `BAO-CAO.md` hiện có. Tiến độ + KQ: dưới P84 trong `COLLAB.md` của việc này. Không tạo tệp repo mới.
**Chỉ thực hiện phần trên dòng `LỊCH SỬ` đầu tiên.** Bản HEAL-01 bên dưới chỉ để tham chiếu đúng các mục được nêu tên (§1 luật cứng, §2 S0, §5 Drive-first, cú pháp registry ở §3).

## 0. Mục tiêu và thế nào là XONG
**Phần 1 (ghi VPS, giữ khoá):** làm nốt điều HEAL-01 dừng (P83): van A1 cho bản chụp trước-sửa của giao dịch + gỡ đồ thử Graph Owner đã gật Q2. **XONG khi đủ cả 5:** (1) Kuma #11 xanh, lý do do storage-watch tính lại sau RUN, không đổi ngưỡng/hạn/kind; (2) đo df trước/sau, đích **≥39,45 GiB hoặc ngưỡng thực cao hơn do storage-watch tính tại S0**, và mốc 7 ngày đang dùng; ngưỡng ≥45 GiB của D24 là mục tiêu sức khoẻ VPS dài hạn, KHÔNG tự đổi điều kiện #11 hay đòi RUN này xóa thêm để đủ 45; (3) van A1 có receipt một lượt chạy thật, dòng transactions sang ROTATING; (4) Guard POST `--coverage`: không đích mới đỏ so PRE_RED_SET, 22 đèn không đèn nào mới đỏ; (5) PG, Qdrant, Directus, Nuxt, agent-data, Neo4j Graph khoẻ, Neo4j production không bị đụng.
**Phần 2 (CHỈ ĐỌC, không giữ khoá):** đo xem VPS đang tiêu tài nguyên vào đâu và ai gây ra, rồi làm lại **bước 2 của KẾ HOẠCH VÔ HIỆU HOÁ DEL-1** bằng số đo mới sau PG18 + Graph. **XONG khi** `BAO-CAO.md · L0-20261013` có đủ Bảng A/B/C ở §4 với số đo thật và **0 thay đổi VPS** trong phần 2.
Phần 1 DỪNG ⇒ vẫn chạy Phần 2 nếu dịch vụ khoẻ và không còn rollback dang dở. **Các mục D24 ≥45 GiB, swap ≤1 GiB/24h, giảm đọc PG ≥50%, di sản TẮT/GIỮ là roadmap nhiều lượt; Phần 2 CHỈ ĐO, chưa được nhận đã đạt các đích đó.** Không ai ngồi chờ; watcher hiện có tự đo 24h.

## 0A. Quyền Owner — khối Owner dán PHẢI có nguyên dòng này
Owner gật Q1–Q5 (Graph P144, 13/10/2026): Q1 bản chụp trước-sửa đã có trong Git giữ 48 giờ rồi xoá, không qua Drive; Q2 dọn D03 D04 D07 D12 D14 D15; Q3 image cũ agent-data và claude-mcp giữ bản đang chạy + 2 bản trước + bản rollback còn trỏ, xoá phần còn lại, không qua Drive; Q4 dừng tmux «agents»/htop 22/05 và 2 Nuxt mồ côi 20/08; Q5 nâng trần RAM claude-mcp 1→1,5 GiB, Postgres 2→3 GiB; mọi xoá khác theo D23 Drive-first.

RUN này chỉ dùng Q1 (A1) và Q2 phần D03 D04 D15. Thiếu dòng này hoặc thiếu GPT ACCEPT+READY đúng SHA PROMPT hiện tại ⇒ DỪNG trước STARTED.

## 1. Luật cứng
- Áp **nguyên §1 của bản lịch sử HEAL-01** (VPS-GHI · báo từng bước · danh sách KHÔNG ĐƯỢC · bí mật · apply-v0 · nghi ngờ thì giữ), với đúng hai điều chỉnh: (a) luật «giữ mọi image Graph» không áp cho **đúng 2 image đồ thử D03 cognee, D04 pgvector và 5 volume treo D15**, và chỉ khi qua 4 điều kiện ở §3 G; image/volume/container `incomex-graph-neo4j` và `/opt/incomex/work/graph-server/**` vẫn cấm; (b) ngân sách: Phần 1 ≤ 45 phút, Phần 2 ≤ 60 phút.
- Báo từng bước dưới P84: `<RUN_ID> · bước k/6 · <xong gì, số> · <UTC> · dự kiến xong <UTC>`.
- **Phần 2 tuyệt đối chỉ đọc:** không DDL, không ALTER/DISABLE/ENABLE, không ghi PG, không đổi flow/cron/timer/cấu hình/container, không chạy DOT hoặc script có ghi (nhãn `LENH GHI DU LIEU THAT` ⇒ không gọi, kể cả `--help`). Truy vấn PG trong phiên `SET default_transaction_read_only = on`, timeout ≤ 10 s, chỉ đọc catalog/thống kê (`pg_stat_*`, `pg_statio_*`, `pg_class`, `pg_trigger`, `pg_proc`, `pg_description`, `directus_flows`); **không `count(*)` trên bảng > 100.000 dòng**. Tìm chữ: `nice -n 19 ionice -c3`, chỉ in tên tệp + số dòng, không quét cả gốc `/`, không tìm toàn gốc `code` qua MCP (P83: làm sập claude-mcp).

## 2. S0 — đọc + PRE
1. Đọc `AGENTS.md` → COLLAB gốc (`VPS-GHI`, PROOT04 ①–⑨) → VPSC COLLAB §0 (D24) + P81–P84 → PROMPT này → `BAO-CAO.md` mục HEAL-20261013. Xác minh GPT ACCEPT+READY đúng SHA và khối Owner có dòng §0A.
2. Làm đúng §2 bước 2–4 của bản lịch sử HEAL-01 (sàn tài nguyên, PRE chỉ đọc, giữ VPS-GHI + STARTED cùng commit trước mọi ghi VPS). Thêm vào ảnh PRE: mốc **T0** của `pg_stat_user_tables` + `pg_statio_user_tables` (DB `directus` và `incomex_metadata`) — dùng lại ở Phần 2.

## 3. Phần 1 — xong việc dở của HEAL
**A1 · bản chụp trước-sửa của giao dịch** (`/opt/incomex/data/workspace-tools/transactions/<tid>/`, Owner Q1, phương án (a) P83):
- Đọc mã **đang chạy trong container** agent-data quanh `workspace_diff(from_version)` (host `agent_data/workspace_tools.py` ~1663–1688): xác nhận có nhánh `VERSION_NOT_RETAINED` trả lỗi sạch khi tệp số không còn, và `from_ref` diff hai commit không cần tệp số. Không có nhánh đó trong mã đang chạy ⇒ KHÔNG làm A1, ghi blocker.
- Ứng viên: chỉ giao dịch root `workspace`; `manifest.json` status `committed` hoặc `rolled_back`; cũ hơn 48 giờ; không lock/lease/job đang chạy. Với từng tệp số `0`, `1`, …: từ manifest xác định path + phiên bản trước; chứng minh `git show <commit reachable từ origin/main đã push>:<path>` cho đúng sha256 của tệp ⇒ xoá đúng tệp đó. Giữ `manifest.json`, `operator-preserved-after.json` và mọi tệp không chứng minh được. `prepared`, `push_unknown`, `rollback_conflict`, không rõ ⇒ không đụng. Root `ui` không đụng.
- Cài thành luật mới trong `/opt/incomex/scripts/vps-retention.sh` cạnh (m)(n)(o) của HEAL-01, qua apply-v0 + rollback; chạy chế độ chỉ in danh sách + sha256 trước, rồi một lượt thật; chạy lại chế độ thử các luật cũ để chứng minh không hồi quy.
- Thử đường đọc thật qua MCP: `workspace_diff` với một `from_version` vừa dọn ⇒ trả `VERSION_NOT_RETAINED` (không lỗi 5xx); `from_ref` hai commit vẫn chạy.
- Registry (`storage-registry.tsv`, qua apply-v0): sau receipt lượt thật, dòng transactions CONTROL_DEBT → ROTATING theo đúng cú pháp và công thức trần ở §3 (Registry) của bản lịch sử HEAL-01.

**G · đồ thử Graph Owner đã gật (Q2: D03 cognee, D04 pgvector, D15 5 volume treo lượt thử 07/10).** Graph Host P145 đã xác nhận đây là **ứng viên cần kiểm tham chiếu**, không phải giấy phép xóa bất kỳ Graph production; log Neo4j đang chạy vẫn bảo vệ tuyệt đối. Gỡ từng mục chỉ khi đủ cả 4: (i) không container nào (kể cả đang dừng) dùng image/volume đó; (ii) tìm tên image/tag/digest/volume (chỉ in tên tệp) trong `/opt/incomex/{docker,scripts,dot,claude-mcp}`, `/opt/incomex/work/graph-server/prod-v1` và `work/graph-server/PROMPT.md` trên repo: không thấy; (iii) không phải image/volume của `incomex-graph-neo4j` hay chuỗi cha của nó; volume có tên/nhãn/ngày tạo khớp lượt thử 07/10 (Graph P145); (iv) image: ghi RepoDigests + đường kéo lại trước khi gỡ; volume: tar Drive-first theo §5 bản lịch sử HEAL-01. Thiếu một điều ⇒ GIỮ mục đó và ghi một dòng `→ việc graph-server` dưới P84. Gỡ image theo ID (không force/prune), volume theo đúng tên. Đo `df` trước/sau.

**POST Phần 1:** chạy đúng một lượt `disk-monitor.sh` (cùng khoá với cron; khoá bận thì đợi lượt cron đó xong, tối đa 10 phút) → Guard POST `--coverage` + 22 đèn + health → mục `HEAL02-20261013` trong BAO-CAO → dòng `KQ@VPSC-HEAL02-L0-20261013-01 · PHẦN 1 XONG|DỪNG · …` dưới P84 và **trả `VPS-GHI: trống` cùng commit**.

## 4. Phần 2 — L0: đo tải + bước 2 DEL-1 (CHỈ ĐỌC, không giữ VPS-GHI)
**Đọc trước (không làm lại):** (a) `docs/KE-HOACH-XOA-20260801.md` từ đầu tới hết «Bốn điều kiện chặn của DEL-1C» (5 bộ: 1 Khai sinh · 2 Registry · 3 Pivot · 4 Governance/Luật · 5 IU đóng băng; bước 1 XONG 01/08; diễn tập tắt/bật 262 trigger khớp 107/107); (b) khối nhãn CUỐI CÙNG (`COMMENT ON` / đầu tệp DOT) của từng ứng viên — câu «vô hiệu hoá thì gì ngừng»; (c) bảng số đo của Claude Chat ở P84; (d) PROOT04 ① ④ ⑦.
**L0-1 · Tải PG:** mốc T1 lúc bắt đầu Phần 2 và T2 lúc kết thúc; delta T0→T2 của `seq_scan`, `seq_tup_read`, `heap_blks_read`, `idx_blks_read`, `n_tup_ins/upd/del` cho 15 bảng đứng đầu; chỉ ngoại suy /ngày khi xác nhận counter không reset và có khoảng đo đủ đại diện; nếu mẫu ít/giờ không điển hình thì ghi DELTA + UNKNOWN, không biến ngoại suy ngắn thành bằng chứng đã tiết kiệm 50%; đối chiếu mức cộng dồn ~9,8 ngày ở P84.
**L0-2 · Ai gây — 4 điểm nóng:** (1) `system_issues` bị quét tuần tự theo đợt; (2) `birth_registry` bị quét tuần tự; (3) `pivot_results` ~20.000 lượt sửa/ngày + chuỗi làm lại `meta_catalog`/`v_registry_*`; (4) `knowledge_documents` bị quét ~8.700 lần/ngày. Mỗi điểm phải có người gọi từ **3 nguồn**: (i) lịch — crontab root, `/etc/cron.d/*`, systemd timer, Directus flow `schedule`, khớp giờ nổ với bước nhảy bộ đếm; (ii) mã — tìm tên bảng/hàm trong `scripts`, `dot/bin`, mã agent-data, Nuxt server/api, operations của Directus flow; (iii) chạy thật — **một** phiên `psql` chỉ đọc (`application_name=vpsc-l0-watch`, tự loại mình khỏi kết quả; một `docker exec` cho cả phiên, không mở `docker exec` mỗi lần lấy mẫu; role thấy được câu lệnh của phiên khác như ảnh PRE HEAL-01, không thấy ⇒ cờ ghi UNKNOWN) chạy `\watch 2` từ đầu Phần 2 tới khi Phần 2 xong, bọc `timeout 3600`; xong việc là dừng ngay, **không ngồi chờ**; trước KQ kiểm còn `0` tiến trình `vpsc-l0-watch`. Mỗi mẫu = một SELECT trên `pg_stat_activity` (bộ nhớ chia sẻ, ~20 dòng, không chạm bảng nghiệp vụ; ~1.800 câu/giờ, tải ≈ 0) + 4 dòng `pg_stat_user_tables` của 4 bảng nóng. **Chỉ in:** giờ · `application_name` · `usename` · `client_addr` · `backend_type` · `state` · `wait_event_type` · tuổi `query_start` · 4 cờ đúng/sai tính ngay trong SQL (`query ~* 'system_issues'` · `'birth_registry'` · `'pivot_results|meta_catalog|v_registry_'` · `'knowledge_documents'`) · loại câu `R|W|FN` lấy từ từ khoá đầu. **KHÔNG in `query`, literal hay đoạn đầu câu lệnh** (giữ đúng ràng buộc GPT `cf3a67e4`). Chỉ lưu dòng có cờ đúng, hoặc mọi phiên đang chạy ở mẫu mà bộ đếm `seq_scan`/`n_tup_upd` của một bảng nóng nhảy so với mẫu trước. **Không dùng `query_id`:** đo 13/10 10:22Z `compute_query_id=auto`, không nạp `pg_stat_statements` ⇒ 0/21 phiên có `query_id` (luôn NULL). Đợt quét `system_issues` không đều (10:00Z +57 trong ~3 phút; 10:03→10:22Z +0): cửa sổ không gặp đợt nào ⇒ nguồn (iii) của điểm đó ghi UNKNOWN, không đoán, không kéo dài để chờ.
**L0-3 · Graph:** với mỗi ứng viên (hàm, trigger, DOT, dòng cron, flow, bảng) hỏi Graph qua đường đọc đã có của việc graph-server (P97, chỉ đọc) các cạnh vào/ra ⇒ «ai còn dùng». Graph mới phủ mã Python production + trigger/DOT tĩnh, chưa phủ SQL dựng chuỗi, gọi HTTP `items/<bảng>` của Directus, Nuxt ⇒ không được kết luận «không ai dùng» chỉ từ Graph; ghi rõ nguồn nào đã xác nhận.
**L0-4 · RAM/swap:** từng container và 15 tiến trình lớn nhất: RSS, VmSwap, `memory.max`, `memory.events` (max, oom), `memory.pressure`; ai đang giữ swap (~1,7/2 GiB lúc 10:00Z).
**L0-5 · Lịch nền:** cron/timer/healthcheck/flow lịch — tần suất × thời lượng × CPU; gồm PROOT04 G4 (healthcheck ~43 exec/phút) và G5 (license-watch 288 container/ngày).
**L0-6 · Directus flow:** 111 flow active (104 event · 5 lịch · 2 webhook): với mỗi flow — collection đích có ghi trong kỳ đo không (delta `n_tup_*`), flow có gọi Agent Data/HTTP không, thuộc bộ DEL-1 nào.
**L0-7 · `system_issues` cũ:** 216.378/227.899 dòng `source=heal_description_basic`, `status=open`, mới nhất 05/06 — còn ai đọc nguồn này không (mã + runtime); ước số khối đọc giảm nếu lưu Drive rồi bỏ.
**L0-8 · Bước 2 DEL-1 cho Bộ 1–4:** mỗi bộ — còn ghi/đọc (delta + cộng dồn); câu nhãn «vô hiệu hoá thì gì ngừng» còn đúng sau PG18 không; 4 điều kiện chặn DEL-1C còn không (đặc biệt `dot-pg-atomic-apply` ghi `table_registry`, `fn_birth_registry_auto` không `EXCEPTION`, FK `RESTRICT` vào `normative_registry`, `governance_object_ownership` CASCADE 29 view). Nhãn `DEL-1I` trên 227 DOT chưa commit (R7 C2): DOT nào còn được gọi (cron/flow/mã).
**Đầu ra — `BAO-CAO.md · L0-20261013`:**
- **Bảng A · Top tiêu tài nguyên:** mục · PG đọc/ghi/ngày · CPU · RAM/swap · exec/ngày · chủ việc.
- **Bảng B · Ứng viên đợt tắt L1 (tối đa 6):** mục · đang tốn (số/ngày) · ai còn dùng (Graph / mã / runtime) · thay bằng gì (vd số ước lượng native của PG, đếm khi mở trang) · lệnh tắt chính xác, đảo được · lệnh bật lại · phép đo trước/sau · lớp D22 · rủi ro. Ứng viên chưa đủ 3 nguồn bằng chứng ⇒ ghi `CHƯA ĐỦ`, không đưa vào L1. Khai sinh (Bộ 1) chỉ được nêu cho đợt sau, không vào L1.
- **Bảng C · RAM:** trần đề xuất từng dịch vụ (có số) + gián đoạn nếu đổi.
- KQ: dòng `KQ@VPSC-HEAL02-L0-20261013-01 · PHẦN 2 XONG|DỪNG · … · 0 thay đổi VPS · 0 tiến trình nền` dưới P84. Báo Owner đúng một dòng cho cả RUN. **Không tắt/xoá gì trong Phần 2** — danh sách L1 do Host + Claude chốt ở lượt sau.

## 5. Bước đi
| Bước | Việc | Bằng chứng | Lỗi thì |
|---|---|---|---|
| 1/6 S0 | đọc, PRE + T0, giữ khoá | ảnh PRE, STARTED | DỪNG trước mọi thay đổi |
| 2/6 A1 | van bản chụp giao dịch | mã đang chạy, dry-run, receipt, `VERSION_NOT_RETAINED` | giữ, làm tiếp G |
| 3/6 G | đồ thử Graph | 4 điều kiện, digest, Drive, df | giữ mục đó |
| 4/6 POST 1 | #11, Guard, đèn, KQ phần 1, trả khoá | storage-watch, coverage | KQ phần 1 DỪNG 1 blocker |
| 5/6 L0 | đo tải + bước 2 DEL-1 | Bảng A/B/C | ghi CHƯA ĐỦ, không đoán |
| 6/6 KQ | KQ phần 2, báo Owner | 0 thay đổi phần 2 | — |

</details>

<details><summary>LỊCH SỬ — HEAL-01 VPSC-HEAL-DISK-MEM-20261013-01 (READY f3fbbd7c, đã chạy 13/10, KQ DỪNG A1) — KHÔNG THỰC HIỆN; chỉ tham chiếu đúng mục PROMPT trên nêu tên</summary>

# (Lịch sử) PROMPT — VPSC-HEAL-DISK-MEM-20261013-01 · Chặn nguồn phình đĩa + dọn đủ để #11 xanh thật + nâng trần RAM đã chứng minh

RUN_ID: VPSC-HEAL-DISK-MEM-20261013-01
Task: `work/vps-clean-20-9-26` (VPSC) — **thay N2a cũ** (READY cũ `dc13606`, chưa bao giờ STARTED). Graph P143/P144, PROOT04 và Codex DIAG-20261013 đã chứng minh N2a chỉ gỡ 3/9 lý do #11. Không phải việc mới.
Soạn: Claude Chat theo lệnh Owner trực tiếp 13/10 14:25 +07 (nguyên văn ở P81). Rà soát: GPT Chat (Host VPSC, khác hãng) **một lượt**: được sửa lỗi nhỏ DRAFT (A6) rồi ghi ACCEPT + READY đúng SHA trong cùng commit; vấn đề lớn thì PARTIAL đúng 1 blocker. Owner: «GPT chỉ có ý kiến nếu ok thì chạy luôn cho nhanh.»
Executor: Claude Code CLI, phiên MỚI trên Mac, qua `ssh contabo`. Ghi repo: Incomex MCP `workspace_*` root `workspace`. Sửa cấu hình được bảo vệ: chỉ `incomex-config-apply-v0`.
Status (lịch sử): READY@f3fbbd7c (P82), chạy 13/10 08:30–09:35Z, **KQ DỪNG A1**; không chạy lại.
Bằng chứng: `/opt/incomex/work/vps-clean-20-9-26/VPSC-HEAL-DISK-MEM-20261013-01/` (chỉ receipt đã làm sạch, không bí mật, không dữ liệu khách). Báo cáo: một mục `HEAL-20261013` trong `BAO-CAO.md` hiện có. Tiến độ + KQ: dưới P81 trong `COLLAB.md` của việc này. Không tạo tệp repo mới. **Chỉ thực hiện phần trên dòng `LỊCH SỬ — N2a cũ`; phần thu gọn bên dưới là bản lưu, KHÔNG thực hiện.**

## 0. Mục tiêu và thế nào là XONG
Owner (D22/D23 + gật Q1–Q5 ngày 13/10): VPS1 sạch, không tái phình, nhanh lại; xoá theo Drive-first trừ ngoại lệ Q1/Q3; không giả xanh.
Ba việc, theo thứ tự ảnh hưởng: (1) **chặn nguồn**: bản chụp trước-sửa (transactions +1,46 GiB/24h, `.before` +0,27), helper queue (+0,25), Git loose objects; (2) **dọn một lần** đủ để SLOPE7D tự hết; (3) **nâng trần RAM đã chứng minh**: claude-mcp chạm 1 GiB 67.256 lần + swap riêng đầy; Postgres chạm 2 GiB 45.123 lần.
**XONG khi đủ cả 8 (đo thật, ghi số):**
1. Kuma #11 xanh, lý do do storage-watch tính lại sau RUN (không đổi ngưỡng/hạn/kind để né).
2. Đĩa trống ≥ max(41 GiB; mốc `df-bytes.tsv` 7 ngày trước − 2 GiB).
3. Van A1–A4 nằm trong `vps-retention.sh`, mỗi van có receipt một lượt chạy thật + bytes trước/sau; 3 dòng CONTROL_DEBT sang ROTATING đúng luật §3.
4. Protection Guard POST `--coverage`: không đích nào mới đỏ so với PRE_RED_SET; mọi tệp đã sửa đều MATCH qua apply-v0.
5. 22 đèn: không đèn nào mới đỏ so với PRE.
6. claude-mcp: memory.current <80% trần mới, swap riêng không đầy; Postgres: bộ đếm `max` trong `memory.events` tăng 0 trong 10 phút sau khi đổi.
7. Độ trễ công cụ thật p50 (10 lần) ≤150 ms, hoặc nhanh hơn PRE ≥50% — ghi cả hai số.
8. PG, Qdrant, Directus, Nuxt, agent-data, Neo4j Graph khoẻ (health 200/healthy hoặc đúng phép đọc native đã xác minh); **không xoá/đụng dữ liệu hay mount của PG/Qdrant/Neo4j**, volume identity giữ nguyên; đối chiếu bản ghi/trạng thái nghiệp vụ, Graph node/edge read-only và backup/restore receipts. Tệp DB đang hoạt động có thể thay kích thước tự nhiên, không đòi equality byte-for-byte của cả thư mục sống.
Thiếu một điều ⇒ KQ DỪNG với đúng một blocker nhỏ nhất; phần đã làm giữ nguyên nếu an toàn; không nới ngưỡng. Sau RUN, watcher hiện có tự đo 24h; không ai ngồi chờ. Mốc 24h (tăng ≤0,5 GiB/ngày, transactions ≤ ~3 GiB, claude-mcp phẳng) do Host đọc ở phiên sau.

## 0A. Quyền Owner — khối Owner dán PHẢI có nguyên dòng này
Owner gật Q1–Q5 (Graph P144, 13/10/2026): Q1 bản chụp trước-sửa đã có trong Git giữ 48 giờ rồi xoá, không qua Drive; Q2 dọn D03 D04 D07 D12 D14 D15; Q3 image cũ agent-data và claude-mcp giữ bản đang chạy + 2 bản trước + bản rollback còn trỏ, xoá phần còn lại, không qua Drive; Q4 dừng tmux «agents»/htop 22/05 và 2 Nuxt mồ côi 20/08; Q5 nâng trần RAM claude-mcp 1→1,5 GiB, Postgres 2→3 GiB; mọi xoá khác theo D23 Drive-first.

Quyền này cấp một lần cho đúng phạm vi trên và cho các lượt định kỳ của van A1–A4. Thiếu dòng này, hoặc thiếu GPT ACCEPT+READY đúng SHA PROMPT hiện tại ⇒ DỪNG trước STARTED. (D13 build cache không dọn vì D10 cấm `docker builder`.)

## 1. Luật cứng (phạm ⇒ dừng bước đó, giữ nguyên, ghi blocker)
- **Một lượt ghi VPS (DROOT54 d):** giữ dòng `VPS-GHI` của COLLAB gốc từ trước thay đổi đầu tiên tới KQ; dòng không trống ⇒ `KQ DỪNG · VPS_BẬN`, không chờ. Cờ STARTED chỉ chạy trên Mac (HJW P313) không chặn.
- **Báo từng bước (DROOT54 a):** hết mỗi bước một dòng `<RUN_ID> · bước k/7 · <xong gì, số> · <UTC> · dự kiến xong <UTC>` dưới P81.
- **KHÔNG ĐƯỢC:** Git gc/prune/reflog expire hay sửa ref; Docker prune hàng loạt (system/image/volume/container) và lệnh builder/buildx (D10); gỡ image cưỡng bức; xoá theo wildcard không có danh sách chính xác; VACUUM/truncate/xoá DB, queue, audit; chạm thư mục dữ liệu PG/Qdrant/Neo4j, transaction log Neo4j, `/var/lib/hermes`, tệp Graph (`/opt/incomex/work/graph-server/**`), mã agent-data (#22 đang chờ TQT P41); sửa `storage-watch.py`; đổi ngưỡng/hạn/kind để lấy xanh; tạo lịch/timer/cron mới; tắt healthcheck/monitor; khởi động lại dịch vụ ngoài bước D.
- **Bí mật:** không in env/.env/token/khoá; tìm chuỗi chỉ in tên tệp; log chỉ đếm; không đưa dữ liệu khách/queue thô vào Git.
- **Cấu hình được bảo vệ** chỉ qua `incomex-config-apply-v0 --target-id <id> --expected-baseline <baseline hiện tại>` + rollback `.pre`; tệp không thuộc registry thì giữ bản `.pre` cạnh tệp + receipt sha256 trước/sau. Đích đang DRIFT ⇒ không đụng, ghi blocker.
- **Nghi ngờ thì giữ:** mọi mục không chứng minh được thì giữ, ghi lý do, làm tiếp phần độc lập.
- Ngân sách ≤2 giờ; quá ⇒ dừng ở ranh giới bước, KQ DỪNG kèm phần đã xong.

## 2. S0 — đọc + chụp PRE (chỉ đọc)
1. Đọc `AGENTS.md` → COLLAB gốc (DROOT54, `VPS-GHI`) → VPSC COLLAB §0 + P81 → PROMPT này → Graph COLLAB P144 → VPSC `BAO-CAO.md` DIAG-20261013 §2–§4 → COLLAB gốc PROOT04 ①–⑨. Xác minh GPT ACCEPT+READY đúng SHA PROMPT hiện tại và khối Owner có dòng §0A.
2. Sàn tài nguyên: MemAvailable ≥3 GiB, đĩa trống ≥20 GiB, không có build/apply/backup/restore đang chạy.
3. PRE chỉ-đọc trước khoá, giữ kết quả trong phiên **không tạo/ghi tệp hay thay VPS**: `df -B1 /`; faults trong `/var/lib/incomex/disk-watch/state.json` + dòng DISKWATCH mới nhất; mốc 7 ngày từ `df-bytes.tsv`; `/opt/incomex/logs/bang-den.json`; Guard PRE `--coverage` + drift-check (PRE_RED_SET theo phép đo thật, không tự giả chỉ có 4 đích); cgroup claude-mcp và postgres: memory.current/max, memory.swap.current/max, memory.events; bằng chứng phiên MCP (đếm log tạo/đóng phiên 24h trong container claude-mcp, số kết nối ESTABLISHED tới cổng dịch vụ); độ trễ p50 10 lần một công cụ đọc nhẹ qua MCP mà phiên có (ưu tiên `fs_list` Incomex VPS, không thì `workspace_stat` Agent Data). **Chỉ ghi ảnh PRE vào thư mục evidence sau khi giữ VPS-GHI và STARTED; nếu khoá thất bại thì không để lại tệp trên VPS.**
4. Giữ khoá trước **mọi** ghi VPS: đọc lại VPS-GHI và shared lease/STARTED mới nhất; chỉ khi thật sự trống, đổi `VPS-GHI: trống` → `VPS-GHI: VPSC-HEAL-DISK-MEM-20261013-01 · VPSC · từ <UTC> · dự kiến <UTC+2h>` và ghi dòng STARTED của RUN_ID dưới P81 bằng expected_version, ưu tiên cùng transaction/commit; nếu một trong hai ghi không thành công thì không mutation và khôi phục đúng trạng thái. Sau đó mới tạo run-scoped evidence, ghi ảnh PRE và bắt đầu bước A. Lease/process thực tế xung đột ⇒ DỪNG, không coi cờ Mac-only là mặc nhiên an toàn nếu có mutation VPS thật.

## 3. Bước A — van chặn nguồn (lâu dài, trong `vps-retention.sh`)
Trước hết đọc mã đang chạy trong container (không chỉ nguồn host): `workspace_operations.py` (ghi bản chụp dòng 353–356, thao tác `restore`, tra `operation_id`), GC trong `workspace_runtime.py`, mã khôi phục lúc khởi động, chỗ ghi `.before`. Nếu đường nào đọc tệp số của giao dịch đã committed/applied ⇒ KHÔNG làm A1, ghi blocker. Ghi kết luận vào bằng chứng.
- **A1 transactions** (`/opt/incomex/data/workspace-tools/transactions/<tid>/`): chỉ xét `manifest.json` status committed, applied hoặc rolled_back, cũ hơn 48 giờ, **đã xác minh job/operation_id/idempotency/audit/rollback/consumer không còn cần bản chụp**, không có khóa/lease/job đang chạy. Với từng tệp số `0`, `1`, …: dựa manifest xác định **root + canonical path + phiên bản trước**, tính SHA256/blob id, chứng minh nội dung chính xác có thể **khôi phục bằng `git show <reachable-commit>:<path>` rồi đối chiếu hash**, commit còn reachable từ ref/bản sao Git còn giữ và có bằng chứng đã push/offsite bền vững. **`git cat-file -e` đơn lẻ hoặc blob dangling trong Git cục bộ KHÔNG đủ quyền xóa**; root ui chỉ có Git local chưa chứng minh offsite ⇒ đi Drive-first §5 nếu hợp lệ, nếu không KEEP. Chỉ xóa đúng tệp bản chụp đã chứng minh phục hồi được; giữ `manifest.json` và mọi tệp sau sửa/độc nhất (`operator-preserved-after.json`), không làm gãy recovery contract; nếu manifest cần cả bộ bản chụp để phục hồi thì KEEP cả giao dịch. Trường hợp không chứng minh Git/offsite, chỉ xét Drive-first §5 sau kiểm references, còn UNKNOWN ⇒ KEEP. Không bao giờ đụng prepared, push_unknown, rollback_conflict hay trạng thái không rõ.
- **A2 `.before`** (tệp chụp đơn ở gốc `/opt/incomex/data/workspace-tools/` và nơi mã chỉ ra): cũ hơn 48 giờ, không còn live references/rollback pin, xác minh **đúng path/version** có thể đọc lại qua commit reachable + hash khớp và có Git offsite/push hoặc recovery bền vững tương đương ⇒ mới xóa đúng tệp (Q1). Blob chỉ tồn tại trong local Git, chưa có commit/ref/nguồn phục hồi độc lập, hoặc không rõ chủ ⇒ KEEP hoặc Drive-first §5 sau khi chứng minh references an toàn; không tự coi `git cat-file -e` là đủ.
- **A3 helper** (`/var/lib/incomex-mcp-helper`): `queue/out/*.json`, `queue/done` đã xong, snapshot P02 đã bị thay (không phải current/previous/pin), cũ hơn 7 ngày, không pending/running/error, hết tham chiếu ⇒ Drive-first §5 rồi bỏ. Giữ `queue/in` và trạng thái hiện hành.
- **A4 Git loose objects:** `/opt/incomex/mcp-roots/gh`, bản clone Git của workspace-tools (`github-workspace`), 2 mirror P02 (agent-data và helper; đường dẫn lấy từ `p02_snapshot.py`/cấu hình). Mỗi repo: không có tiến trình git đang chạy trên repo đó; `git fsck` trước; đếm refs; `git repack -d -q` (không `-a`, không gc/prune); sau đó `git fsck` sạch và refs y nguyên. Lỗi ⇒ dừng repo đó.
- **Cài van:** thêm A1–A4 thành luật mới trong `/opt/incomex/scripts/vps-retention.sh` (chạy theo cron sẵn có, luật hằng ngày như (k)), qua apply-v0 + rollback; chạy chế độ chỉ in danh sách + sha256 trước, rồi một lượt thật ngay. Không sửa `/etc/cron.d/vps-retention`. Chạy lại chế độ thử của các luật cũ để chứng minh không hồi quy.
- **Registry** (`/opt/incomex/scripts/storage-registry.tsv`, qua apply-v0): chỉ sau receipt lượt thật, đổi 3 dòng CONTROL_DEBT (transactions, helper, mcp-roots) sang ROTATING kèm trường van cron trỏ `vps-retention.sh`, trường tệp trỏ mã luật, và trần bằng (thời hạn giữ × dòng vào 24h đo được) × 1,3 — ghi công thức và số (cú pháp theo đúng các dòng ROTATING đang có và `storage-watch.py` dòng 412–417). Nguồn đang tăng chưa có tên thuộc việc khác (PROOT04: `/var/lib` → hjw-control +178 MiB/24h, chủ HJW): thêm một dòng riêng kind CONTROL_DEBT, owner HJW, hạn ngày 16/10/2026 01:00 UTC, lý do một câu — không lập van hộ HJW. Nguồn lạ khác >128 MiB/24h: ghi blocker, không tự phân loại.

## 4. Bước B — dọn một lần (Q2, Q3)
- **B1 image (Q2: D03 D04 D07; Q3: D01 D11):** kê mọi image (ID, tag, RepoDigests, ngày tạo, cỡ riêng). Tập GIỮ = image của mọi container (kể cả đang dừng) + chuỗi cha + 2 bản trước của mỗi repository (luật R03) + image agent-data-hvu tag mcpw-r2-20261001 (đường lùi PROOT03) + mọi tag/ID được nhắc trong compose/rollback/script dưới `/opt/incomex/{docker,claude-mcp,scripts,dot}` và `/opt/incomex/work/graph-server/prod-v1` (tìm bằng grep chỉ in tên tệp) + mọi image Graph/Neo4j/gs-*. Chỉ gỡ image ID thuộc D01, D03, D04, D07, D11 khi **mọi tag/digest cùng ID** đều không nằm trong tập GIỮ, không có container/volume/rollback/compose/Code Ledger ref; kiểm lại từng ID ngay trước gỡ, không thay một image nhiều tag thành nhiều bản độc lập. Gỡ bằng lệnh thường theo đúng ID, không force/prune (Docker từ chối ⇒ giữ). Ghi RepoDigests của D03/D04 và đường pull/restore đã kiểm trước khi gỡ. Đo `df` trước/sau (không tin số reclaimable của docker).
- **B2 staging TQT (D12):** `/opt/incomex/staging/tqt-p32`, `tqt-p33`, `tqt-p36` ⇒ Drive-first §5 ⇒ bỏ đúng 3 thư mục.
- **B3 tạm cũ (D14):** phần thử cũ trong `/var/tmp/jev-gate` và mục trong `/tmp` cũ hơn 7 ngày, không tiến trình nào giữ (`fuser`), không phải socket, không phải `tmux-*`, `systemd-private-*`, hay `lark-gpg-home-*` còn gpg-agent sống ⇒ gom một gói Drive-first §5 ⇒ bỏ đúng danh sách.
- **B4 (D15):** gỡ container Created `workspace-job-0ae7…` (không cưỡng bức). 5 volume treo: volume thuộc project compose của dịch vụ đang chạy ⇒ giữ; còn lại ⇒ tar Drive-first §5 ⇒ gỡ đúng tên volume.
- **Giữ nguyên:** D02 Hermes, D05 Graph, D08 backup-staging, D09 `/root` (chưa rõ chủ), D13 build cache (D10), dữ liệu PG/Qdrant/Neo4j.

## 5. Drive-first (D23) — dùng đúng đường đã duyệt của N2a cũ (P79)
Làm đúng §0B của bản lịch sử bên dưới: đóng gói mã hoá bằng đúng người nhận của `backup-to-gdrive.sh` → đẩy lên thư mục `rescue/vpsc-n2a/` (thư mục `backup-to-gdrive.sh` không tỉa), meta `retain_until` = +12 tháng → readback số mục/cỡ/checksum → thử khôi phục mẫu theo chuỗi đã chứng minh của `dot-pg-restore-verify-db` (giải nén một mẫu, sha256 khớp; gói cắt cụt phải báo lỗi; không để lại gì trên đĩa bền) → kiểm lại tham chiếu ngay trước khi bỏ → bỏ đúng danh sách. Bước nào lỗi ⇒ giữ local, báo. Báo số GB đã đẩy lên Drive.

## 6. Bước C — mồ côi (Q4)
- **C1** tmux `agents` (22/05): kê pane (pid, lệnh, cổng nghe). Không pane nào là dịch vụ systemd/compose, không giữ cổng mà nginx/Kuma dùng, không phải Hermes gateway/serve đang chạy ⇒ đóng phiên tmux `agents` và xác nhận htop đã tắt. Ngược lại ⇒ chỉ dừng tiến trình htop, ghi blocker phần còn lại.
- **C2** 2 tiến trình `node .output/server/index.mjs` (20/08, 127.0.0.1:3101 và :3909): tìm cổng 3101/3909 trong cấu hình nginx và Kuma (chỉ in tên tệp); không ai trỏ ⇒ gửi tín hiệu dừng thường, xác nhận thoát trong 10 giây; còn sống ⇒ để nguyên và báo (không ép dừng).
- gpg-agent cũ: không thuộc Q4, để nguyên.

## 7. Bước E — sửa nhỏ giám sát
`/opt/incomex/scripts/disk-monitor.sh` dòng 85 lấy mã thoát sau lệnh `date` nên luôn ghi `WARN … rc=0`: sửa để lưu mã thoát ngay sau lệnh storage-watch (sửa tối thiểu, qua apply-v0). Thử trên bản sao trong thư mục tạm của lượt với lệnh giả trả lỗi ⇒ log ghi mã khác 0; dọn bản sao sau khi thử.

## 8. Bước D — trần RAM (Q5), làm sau cùng
Ghi một dòng tiến độ trước bước này (D2 có thể khiến agent-data gián đoạn, ghi repo có thể lỗi tạm; bổ sung receipt sau khi khoẻ). **Preflight D1/D2 bắt buộc:** lấy `docker inspect` metadata compose project/service/working directory, image ID/digest, volumes/bind mounts, memory+swap trước thay đổi; kiểm `docker compose config --quiet` tại đúng project trước/sau và diff chỉ đúng giới hạn RAM; backup/recovery PG hiện có phải có receipt kiểm được, cấm đụng dữ liệu PG; dựng lại đúng **một service** với `--no-deps`, **không pull/build/đổi image/tag/volume/mount/network**; giữ bản cấu hình `.pre` và khả năng rollback, làm tuần tự một service và kiểm healthy trước khi sang service kia. Nếu không xác nhận được toàn bộ footprint/backup/recovery thì DỪNG riêng bước D, không mạo hiểm phục hồi bằng giả định.
- **D1 đầu nối Claude (container claude-mcp):** trong tệp compose **được xác minh bằng nhãn service/container đang chạy** (không đoán path theo tên), nâng giới hạn bộ nhớ từ 1 GiB lên 1,5 GiB và giới hạn bộ nhớ cộng swap lên 2,5 GiB (giữ 1 GiB swap như cũ), ghi chú thích Q5 Owner ngày 13/10 (Graph P144); giữ nguyên mọi dòng khác. Qua `incomex-config-apply-v0` nếu Guard quản lý; Guard đang DRIFT ⇒ không sửa. Dựng lại riêng service từ đúng project theo gate chung bước D; xác nhận healthy và một lệnh công cụ thật chạy được.
- **D2 cơ sở dữ liệu (container postgres):** tìm tệp compose thật qua nhãn compose của chính container đó (tệp cấu hình, thư mục làm việc, tên project). Chỉ nâng giới hạn bộ nhớ service này từ 2 GiB lên 3 GiB (nếu có giới hạn bộ nhớ cộng swap thì cùng thêm 1 GiB). **Đọc Guard target hiện hành: nếu target compose đang DRIFT thì KHÔNG đụng; nếu MATCH và được quyền theo Q5 mới apply bằng cổng được bảo vệ. Không mặc định compose đang DRIFT chỉ vì ba tệp Python/Hermes đang đỏ.** Kiểm backup/recovery và volume PG trước bất kỳ recreate; không chạy lệnh nếu volume mapping/image digest sẽ đổi. Dựng lại riêng service này với `--no-deps`, không kéo service khác, từ đúng project; chờ healthy tối đa 180 giây; kiểm Directus, agent-data và Kuma database, xác nhận kết nối PG hiện hữu phục hồi, Graph không bị ảnh hưởng. Dịch vụ phụ thuộc không tự khoẻ trong 180 giây ⇒ ghi blocker, không tự khởi động lại dịch vụ khác.
- Rollback mỗi bước: khôi phục bản `.pre` (apply-v0) rồi dựng lại service đó; làm ngay nếu chính service không khoẻ trong 180 giây.
- **D3 đo sau:** memory.current/max, swap, delta `memory.events` trong 10 phút; p50 10 lần cùng công cụ như PRE.

## 9. POST + KQ
1. Chạy đúng một lượt `/opt/incomex/scripts/disk-monitor.sh` thủ công (cùng khoá với cron; khoá bận thì đợi lượt cron đó xong, tối đa 10 phút) ⇒ storage-watch tính lại và đẩy Kuma #11.
2. Guard POST `--coverage`; bảng 22 đèn; health các dịch vụ ở điều 8 §0; đối chiếu đủ 8 điều XONG.
3. Ghi mục `HEAL-20261013` vào `BAO-CAO.md` (bảng trước/sau: đĩa, từng nguồn, image đã gỡ theo mã D, GB đẩy lên Drive, RAM/swap/events, p50, Guard, đèn, rollback còn sẵn).
4. Dưới P81: dòng KQ của RUN_ID này (XONG hoặc DỪNG, tóm tắt số, thư mục tạm của lượt đã dọn, 0 tiến trình nền, giờ UTC); cùng commit trả `VPS-GHI: trống`.
5. Kế tiếp: XONG ⇒ TQT rà P41 và đăng ký 3 tệp, rồi HJW Hermes, rồi Graph S0 và R10 đúng PROMPT đã ký; DỪNG ⇒ đúng một blocker + chủ.
6. Báo Owner đúng một dòng XONG hoặc DỪNG. Không giữ terminal chờ.

## 10. Bước đi
| Bước | Việc | Bằng chứng | Lỗi thì |
|---|---|---|---|
| 1/7 S0 | đọc, PRE, giữ khoá | ảnh PRE, STARTED | DỪNG trước mọi thay đổi |
| 2/7 A | van A1–A4 + registry | receipt lượt thật, bytes | giữ, làm tiếp phần độc lập |
| 3/7 B | dọn D01 D03 D04 D07 D11 D12 D14 D15 | danh sách + df trước/sau + Drive | giữ mục lỗi |
| 4/7 C | mồ côi | pid/cổng trước/sau | để nguyên mục nghi |
| 5/7 E | mã thoát disk-monitor | thử lỗi | rollback `.pre` |
| 6/7 D | trần RAM | events, p50 trước/sau | rollback `.pre` |
| 7/7 POST | 8 điều XONG, KQ, trả khoá | storage-watch, Guard, đèn | KQ DỪNG 1 blocker |

</details>

<details><summary>LỊCH SỬ — N2a cũ VPSC-N2A-DISK11-CONTROLS-20261011-01 (READY dc13606, chưa chạy, đã thay ngày 13/10) — KHÔNG THỰC HIỆN</summary>

# (Lịch sử) PROMPT — VPSC-N2A-DISK11-CONTROLS-20261011-01 · THREE CONTROL_DEBT #11 HOTFIX (SCOPE N2a)

RUN_ID: VPSC-N2A-DISK11-CONTROLS-20261011-01
Task: `work/vps-clean-20-9-26` (VPSC) · D22/roadmap N2a, **not a new task**.
Executor: Claude Code CLI (new session), Owner manually pastes after **Claude Reviewer exact ACCEPT + GPT Host READY same SHA**.
Repo_Write_Path: existing Incomex MCP `workspace_*`, root=`workspace`; VPS config/runtime via already accepted native paths and `incomex-config-apply-v0` only.
Status: **DRAFT · D23 OWNER DRIVE-FIRST supersedes P76/P77 old PROMPT @d4eeb15 · P79 Claude Reviewer sửa nhỏ §0B (đường thử khôi phục + đích Drive) + ACCEPT đúng SHA bản này · NO READY/RUN**.
Evidence: reuse `/opt/incomex/work/vps-clean-20-9-26/` under a run-scoped subdir; report one section under existing `BAO-CAO.md` and KQ in task `COLLAB.md`. Never create duplicate repo files as progress notes.

## 0. GOAL — CLEAR THE *ACTUAL* BLOCKER, NO SCOPE CREEP
Owner has directed priority to complete Graph R10 promptly; the sole known hard execution gate is **Kuma #11 Disk Usage RED** caused by three VPSC `CONTROL_DEBT` deadlines 2026-10-11T01:00:00Z (not disk fullness: 11/10 physical free ≈42 GB):
1. `/opt/incomex/data/workspace-tools/transactions`: operation backups, baseline historical +62 MB/day.
2. `/var/lib/incomex-mcp-helper`: queue/out, done and P02 backlog, historical +105 MB/day.
3. `/opt/incomex/mcp-roots/gh` (under `/opt/incomex/mcp-roots`): loose Git objects/ref growth.

**Mục tiêu RUN N2a:** sửa đúng ba nguồn CONTROL_DEBT bằng van giới hạn thật, kiểm chứng Kuma #11 GREEN và Guard POST same-or-better. Không lách bằng nới ngưỡng, đổi hạn debt/kind, đặt cap-only hoặc di chuyển dữ liệu sang thư mục khác cùng ổ.

**Ngoài RUN:** C2 312 UNKNOWN+2 excluded, 3 EVIDENCE_DEBT, D22/N2b để VPSC sau; R7 A/B/C1/C3/D/POST giữ nguyên. Không sửa Graph R10, HJW, ứng dụng agent-data/helper hoặc task đã đóng. Cấm Git prune/reflog expiry, queue truncate, xoá wildcard không có danh sách kiểm chứng, broad wipe hay đổi services/PG/Directus.

## 0A. OWNER DIRECTIVE D23 · CHÍNH SÁCH GIỮ HẠN ĐÃ ĐỒNG Ý CÓ ĐIỀU KIỆN, CHƯA READY
Theo chỉ đạo trực tiếp D23, Owner đã đồng ý dọn an toàn và yêu cầu **Drive-before-delete**. Dòng dưới định danh phạm vi được chấp thuận; PROMPT tự nó không phát RUN. Claude Executor vẫn phải thấy đúng câu trong **khối Owner thực sự dán** (một dòng):
Owner cho VPSC N2a trên VPS1 tái dùng vps-retention.sh và kho Google Drive mã hóa hiện hữu để lưu trước-xóa các bản transactions đã hoàn tất, hết tham chiếu, trên 14 ngày và helper queue/out/*.json, queue/done, p02 snapshot đã hết vai trò, hết tham chiếu, trên 7 ngày; chỉ được xoá sau khi tải bản cứu hộ lên Drive, kiểm hash/readback và thử khôi phục PASS, kiểm lại job/idempotency/rollback/consumer cùng danh sách hash ngay trước xoá; giữ nguyên mọi bản chưa rõ, còn dùng hoặc là bản khôi phục duy nhất chưa chứng minh bản Drive dùng được, không xoá khác và không prune/làm mất lịch sử Git.

Thiếu câu này, thiếu một Claude ACCEPT SHA mới, thiếu Host READY exact SHA, thiếu Guard/no concurrent hoặc archive Drive verify/restore PASS thì DỪNG trước STARTED hoặc trước DELETE. Owner cấp quyền một lần cho đúng policy định kỳ trong phạm vi trên; từng lần tự kiểm refs/hash/fresh receipt, lỗi/UNKNOWN thì KEEP và cảnh báo. Không phải xin Owner mỗi ngày. Không đụng dữ liệu độc nhất cần khôi phục khi chưa có proof offsite/restore.

## 0B. OWNER D23 · DRIVE-FIRST VERIFIABLE CLEANUP
- Người dùng đã duyệt nguyên tắc: **archive lên Google Drive rồi mới DELETE local**, tái dùng đúng backup/retention đang có. VPSC các đợt trước từng thực hiện `tar|gzip|gpg→rclone rescue/vpsc-r3`, MD5 readback rồi xoá và backup mã hóa mỗi đêm; **không giả định backup PG/config hiện đã chứa transactions/helper**. Đây là cổng bổ sung an toàn, không xây hệ backup thứ hai. §0A hiện là policy Owner đã cho phép có điều kiện, nhưng Host chưa READY bản sửa và chỉ Owner dán RUN có nguyên văn câu chính sách mới.
- S0 READ-ONLY chứng minh remote rclone/GPG hiện hữu và restore route, bản backup gần nhất, quota/quyền/hạn giữ rescue; không in token/secret, không mở rộng remote hay cloud project. Đích rescue phải có vòng đời đã kiểm, không bị backup-keeper xoá sớm hơn khi cần khôi phục.
- **Đích Drive (P79, theo mã):** thư mục con mới `rescue/vpsc-n2a/` của đích mã hoá hiện hữu, mã hoá bằng đúng khoá công khai người nhận của `backup-to-gdrive.sh` (kiểm vân tay trước). `backup-to-gdrive.sh` chỉ tỉa `rescue/vpsc-r2|r3|r6` ⇒ thư mục mới không bị xoá sớm. N2a **không xoá gì trên Drive và không sửa `backup-to-gdrive.sh`**; meta mỗi gói ghi `retain_until` = +12 tháng (như r3/r6); KQ báo GB/tháng đổ ra Drive + trần dự kiến; luật tỉa `rescue/vpsc-n2a/` theo khuôn r3/r6 = nợ VPSC lượt sau, phải xong trước `retain_until` sớm nhất. Đây là cách đáp ứng gạch «Drive archive cũng phải có retention» dưới đây, không phải cổng XONG của N2a.
- **Đường thử khôi phục (P79, theo mã):** keyring bền của VPS chỉ có khoá công khai (`backup-to-gdrive.sh`: «can never decrypt») ⇒ không giải mã bằng keyring đó, không đưa khoá riêng vào đĩa bền. Tái dùng đúng chuỗi đã chứng minh của DOT `dot-pg-restore-verify-db` (VPSC R6 C4): khoá riêng phục hồi đi thẳng Secret Manager → `gpg --import` vào GNUPGHOME tmpfs riêng của lượt (0700), không vào biến/argv/log/đĩa bền/Git, agent không xem/chép → đọc ngược đối tượng từ Drive → `gpg -d | tar` đủ số mục/byte theo manifest + extract ít nhất một mẫu mỗi gói vào tmpfs, sha256 = manifest → đối chứng âm (gói cắt cụt phải fail) → xoá sạch tmpfs, keyring gốc còn 0 khoá riêng, residue 0. Áp cho **mọi gói trước DELETE, cả lượt RUN lẫn các lượt cron sau**; thiếu gcloud/Secret Manager/chỗ tmpfs hoặc bước nào lỗi ⇒ chỉ upload, KEEP local, cảnh báo, không xanh giả.
- Với từng tập A/B đủ điều kiện: dry-run danh sách exact path+hash+references→gói nhỏ mã hóa bằng khoá đã xác minh→stream lên Drive bằng cổng cũ→xác minh object/count/size/checksum readback và **thử extract/restore một mẫu không ảnh hưởng production**, hash khớp→recheck trạng thái job/refs, symlink, canonical delete-set ngay trước DELETE. Lỗi upload/hash/restore/remote/retention/refs ⇒ **KEEP local; báo blocker, không xanh giả**. Không tải raw customer/queue ra Git, chỉ receipt sanitized và pointer phục hồi private.
- C Git chỉ repack -d nếu fsck, refs/recovery và bản code-backup/offsite hiện hữu đã chứng minh; không cần copy từng loose object lên Drive khi cùng nội dung reachable đã có trong pack và recovery đã đủ, nhưng thiếu recovery proof thì không repack.
- Không đưa bất kỳ archive/log/queue đã dọn trên Drive vào Graph như một node/cạnh hay bằng chứng nguồn nghiệp vụ; **dọn ổ ≠ xoá/thay thế chân lý Graph**. Drive archive cũng phải có retention, không trở thành nguồn rác vô hạn.
- Thời gian giữ N2a khởi động: transactions >14d, helper >7d. Owner muốn xem xét nhanh hơn; executor **đo ứng viên >7d/>3d** và báo Host sau đợt đầu, nhưng không tự áp giảm hạn trong RUN này khi chưa được chứng minh và ký delta.

## 1. S0 HARD AUTH + LIVE RESOURCE / GUARD
1. Đọc `AGENTS.md` → root `COLLAB.md` → VPSC Bảng, §0, P68–P78/BAO-CAO R7, D23 Drive-first §0A/§0B và một Claude reviewer ACCEPT exact SHA mới, last-touch PROMPT và reviewer/Host exact SHA. Kiểm **không có STARTED active/STOP/COUNCIL_ALERT, no HJW/Graph concurrent mutation**. #11 RED là **đối tượng đang chữa**, không giả vờ PRE 22/22: freeze `PRE_RED_SET` và raw reason, yêu cầu các đèn khác cùng Guard Config CLEAN hoặc có reason và owner minh bạch. Active resource floor: MemAvailable ≥3GiB + disk free ≥20GiB, no active PSI/OOM hazard. Nếu khác mà không giải thích được ⇒ KQ DỪNG sạch. **Do not wait/poll/hold terminal.**
2. Preflight full SHA and root gate before writing. If passed, record `STARTED@VPSC-N2A-DISK11-CONTROLS-20261011-01` + root shared busy atomically in one repo commit before first mutation. Preserve all actual scripts/registry/queue state/baseline hashes, support existing coverage Guard C3 and revocable rollback to PRE. No secret or raw customer data in Git/evidence.
3. Read-only inspect each `CONTROL_DEBT` row in `scripts/storage-registry.tsv`: canonical owner, due, path, cap, source classifier, current bytes/rate and what evidence the detector requires before clearing. Inspect existing `storage-watch.py`, retention scripts/timers, `incomex-config-apply-v0 --help`, and Config Guard protected paths. Freeze **allowed exact footprint matrix**, candidate patches and inverse before mutation. If status RED is a real fault (not just deadline) fix it under the same three source boundaries, not by changing the monitor definition.

## 2. N2a — THREE SOURCE CONTROLS (FOUR FIXES P73)
A · Transactions: chỉ backup completed, quá 14 ngày, chứng minh không còn prepared/push_unknown/rollback_conflict/unknown, queued/running, operation_id/idempotency, audit/rollback/recovery refs. Tuổi không đủ để xóa; UNKNOWN/sole recovery => KEEP. Sau OWNER permission §0A, dry-run exact sorted candidate paths + SHA256/state/ref proof; DRIVE-FIRST upload, readback và restore mẫu PASS theo §0B rồi mới kiểm lại references ngay trước xóa. Không có chứng cứ đủ => nợ vẫn OPEN, KQ DỪNG.

B · Helper: chỉ queue/out/*.json, completed queue/done và p02 snapshot superseded/noncurrent, quá 7 ngày, chứng minh không có pending/running/error, consumer/alert/current pin/P02/audit/recovery refs; queue/in và current state phải giữ. Dry-run exact candidates/hashes, Drive encrypted archive+readback+sample restore PASS §0B rồi mới recheck references, UNKNOWN => KEEP. Không sửa helper/HJW code; no concurrent HJW trước mọi mutation.

C · mcp-roots/gh: git fsck trước/sau; kiểm HEAD, refs/recovery/reflogs/bundles và P02 writer lock, chỉ native git repack -d (không dùng git gc, kể cả --prune=never, vì gc tự chạy reflog expire theo gc.reflogExpire 90d/unreachable 30d) nếu chứng minh tất cả refs/objects phục hồi còn nguyên. Cấm prune/reflog expire/ref rewrite; không đủ bằng chứng => nợ OPEN.

ONE VALVE: dùng lại công cụ hiện có trước. agent-data/helper không có retention cho A/B (P73), nhưng VPSC đã có người gác kho /opt/incomex/scripts/vps-retention.sh (R2–R5b: cron mỗi giờ /etc/cron.d/vps-retention, flock, log /var/log/incomex/vps-retention.log, luật (a)–(l), chế độ chỉ in danh sách + sha256 như --chi-l-thu, LOCKED trong code-ledger, đã là van cron=vps-retention\.sh của 4 dòng sổ). Mặc định: thêm luật A/B/C vào script đó, mỗi ngày một lượt theo giờ UTC như (k), qua incomex-config-apply-v0 + rollback, chạy lại chế độ thử của luật cũ để chứng minh không hồi quy; không sửa /etc/cron.d/vps-retention. Chỉ khi không làm được (ghi lý do đo được) mới tạo đúng một script retention dưới /opt/incomex/scripts/ + một systemd timer (service unit tối thiểu của nó) chạy hằng ngày, gọi A/B/C theo điều kiện an toàn, cài qua incomex-config-apply-v0 và đăng ký Code Ledger/Config Guard/coverage/rollback. Lượt đầu dry-run, test fail-closed với active/unknown/symlink/ref mismatch **và upload/readback/restore Drive lỗi**; rồi mới được thực thi cleanup sau §0B PASS trong quyền §0A. Mỗi lượt timer chạy trong shared lock, có receipt và quan sát actual bytes; có job khác thì SKIP, không sleep/WAIT.

Mọi source phải có PRE/POST bytes/slope, proof reference safety/restore; A/B bổ sung encrypted Drive archive/count/hash/readback/sample restore receipts theo §0B. status INSTALLED_AND_PROVEN|DRY_RUN_ONLY|BLOCKED; move cùng ổ, cap-only hay upload-only không chứng minh dọn đúng.

## 3. #11 REAL GREEN / POST GATE
- Any protected mutation must apply by `incomex-config-apply-v0` with exact target and validated rollback. Do not change registry debt due/status directly to hide `DEBT_OVERDUE`. Registry chỉ được đổi ba CONTROL_DEBT sang ROTATING khi van đã chạy thật có receipt, có proof cleanup/Guard/rollback; valve bắt buộc gồm cap= + phần sống: cron=vps-retention\.sh (kèm file=vps-retention.sh~<mã luật>) nếu dùng cron hiện có, hoặc fresh=<tệp dấu chỉ ghi khi lượt dọn chạy xong>@26 nếu là systemd timer — valve_ok cron= chỉ đọc crontab root + /etc/cron.d (storage-watch.py:412–417), không thấy systemd timer. cap=/file= đứng một mình là xanh giả, cấm. Không sửa storage-watch.py trong N2a; khe valve_ok cho qua cap-only (P73) ghi nợ VPSC lượt sau. Không đổi hạn debt/kind/threshold để né đỏ. If missing control, keep explicit RED/DEBT and explain.
- After each bounded candidate apply, validate source consumers/queue recovery/refs, Config Guard, existing retention paths. POST should be **same-or-better relative to legitimate PRE**: #11 GREEN, other 21 lamps no newly RED, Guard protected footprint exactly approved modifications with coverage, no secret leak. **Cổng XONG gồm ba điều đo thật + GDrive-FIRST bắt buộc:** (i) A/B đã upload Drive mã hóa, hash/readback và restore PASS trước DELETE; mỗi nguồn A/B/C có receipt lượt chạy thật của van + bytes PRE/POST đo được (cap=, file= hay sửa hạn nợ không tính); (ii) Kuma #11 GREEN với lý do mới do storage-watch tính lại; (iii) Protection Guard POST --coverage PASS, không đèn nào mới đỏ so với PRE_RED_SET. If #11 remains RED from these debts, KQ DỪNG, do NOT override it.
- If RED arises from another independent VPSC defect, give one bounded root cause/owner, no scope widening without separate authorization. No nightly/24h terminal wait, no background experiment; existing watcher/Guard monitors steady state after run.

## 4. KQ / SHARE SLOT WITH GRAPH
Report `KQ@VPSC-N2A-DISK11-CONTROLS-20261011-01 XONG|DỪNG` with Drive-first archive/readback/sample restore receipts (A/B) and evidence for each of the 3 debt sources, Config Guard PRE/POST, Kuma #11 final reason, no regressions, actual vs forecast disk and slope, tests, rollback, any unresolved debt and NEXT_TRIGGER. Write VPSC COLLAB (same commit release root busy) and existing BAO-CAO; leave Graph PROMPT/SHA untouched.
- If **XONG and #11 GREEN with Guard proof**, note `NEXT_TRIGGER=GRAPH_R10_HOST_FRESH_PRE_READY_EBF52956...`; host Graph independently does fresh Guard PRE and issues READY at its already signed SHA, then Owner manually pastes R10.
- If **DỪNG**, return exact smallest fix/Owner-only decision, do not ask Owner to run Graph against RED and do not relabel as green.

## 5. STEP WALK
| Phase | Who | Trigger | Proof | Fault |
|---|---|---|---|---|
| S0 | Claude Code | exact REVIEW+HOST READY+Owner pasted RUN | no concurrent + PRE snapshot/resource/protected footprint | KQ DỪNG before mutation |
| A transactions | Claude Code | S0 pass | operation/recovery reference proofs, native control candidate/dry-run | preserve evidence, continue independent sources |
| B helper | Claude Code | A measured | queue/P02 reference/TTL control tests | preserve evidence, continue |
| C gh | Claude Code | B measured | fsck/refs/GC non-destructive validation | preserve refs, no prune |
| POST | Claude Code | A-C accounted | actual control receipts, true #11 GREEN, all other lamps same-or-better | KQ DỪNG or rollback scoped delta |
| KQ | Claude Code | terminal | exact KQ, release root busy, no unapproved writes | next trigger VPSC or Graph R10 |

**DO NOT do C2, Graph, HJW mutation.** Claude P73 đã ký 4 sửa có điều kiện, Host P75 áp 4 sửa, Claude P76 ACCEPT bản cũ d4eeb15; vì Owner D23 thêm gate Drive-first materially nên Reviewer phải ký đúng PROMPT mới một lượt hẹp (được sửa DRAFT theo bằng chứng), rồi Host mới READY sau fresh Guard/shared VPS; không rà lại toàn bộ R7. P79 Claude đã sửa §0B và ACCEPT bản này; Host READY đúng SHA last-touch, không mở thêm vòng review.

</details>
