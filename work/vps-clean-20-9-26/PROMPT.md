# PROMPT — VPSC · Khảo sát CHỈ ĐỌC: vì sao đĩa VPS đầy lại nhanh + danh sách dọn + đề xuất khoá vòi rò

RUN_ID: VPSC-R1-20260920-01
Soạn: Claude Chat (Host việc này), 2026-09-20. Owner giao: đánh giá vì sao đĩa VPS đầy nhanh; đề xuất dọn phần không dùng để có chỗ cài Graph DB. Trạng thái KHÔNG ghi ở file này: chỉ tin giấy phép trong `work/vps-clean-20-9-26/COLLAB.md`.
Chỉ chạy khi COLLAB đó có `REVIEWED@` của Founder không soạn (GPT) + Host `READY@` (hoặc `OWNER_APPROVED@`) đúng full SHA commit cuối chạm file này, cộng lệnh RUN hợp lệ.
**Chế độ: CHỈ ĐỌC.** Không xoá, không sửa, không restart gì trên VPS. Không ghi gì vào repo workspace.

## 0. Trước khi làm
1. Clone repo công khai vào /tmp mới; kiểm giấy phép đủ 40 ký tự; thiếu/lệch → DỪNG.
2. Đọc `AGENTS.md`, `work/vps-clean-20-9-26/COLLAB.md` + `view.html`, và KB `knowledge/current-state/reports/vps-clean-minimum-2026-07-24.md` — MỐC so sánh (số liệu, danh sách đã dọn, mọi chỗ cách ly ngày 24/07).
3. Đọc dòng R03 trong `work/mcp-workspace/COLLAB.md`: đang deploy thì CHỜ xong mới đo; chưa CLOSED thì áp khoá chéo ở §2.

## 1. Bối cảnh (bạn không nhớ phiên trước)
- Ổ `/dev/sda1` 96GB NVMe, Ubuntu 24.04, Docker; mã SSOT tại `/opt/incomex`.
- 24/07/2026 mission VPS-CLEAN-MINIMUM dọn 87% → 61% (trống 13 → 39GB, thu 27,4GB).
- 20/09: ~01Z 83/96GB (trống 14GB); ~12Z 84/96GB (trống 13GB) — thêm ~1GB trong ~11 giờ, trùng lượt build R03 final-close. Nhịp TB từ 24/07 ≈ 0,45GB/ngày: toàn bộ phần đã dọn bị ăn lại.
- Nghi vấn Claude Chat đã thấy (CHƯA đo GB — bạn đo):
  a) `/opt/incomex/deploys/`: ~67 bản sao `nuxt-output.*` (sao 1 bản mỗi lần deploy Nuxt; 12 bản chỉ trong 13–15/09), không hạn xoá.
  b) Image build lại liên tục với tag mới (`agent-data-r03:*`, `claude-mcp-local:*`, `claude-kb-local:*`); claude-mcp có 6 Dockerfile mới trong 17–19/09, mỗi bản FROM tag trước (chuỗi cha–con). Bệnh ~32GB image tháng 7; phần "giữ N tag / dọn sau deploy" của W2 dường như chưa từng làm.
  c) `incomex-nuxt` chạy image KHÔNG TAG (`72715a92885c`).
  d) `/opt/incomex/context-pack-staging/`: gói 3 giờ/lần từ 11/09, 66 gói ~2MB, không xoá gói cũ.
  e) DB `directus_gov_test_20260602` (1,2GB) còn, dù tháng 7 xếp lịch drop.
  f) Không thấy giới hạn log (max-size) trong các compose đọc được.
  g) Loại trừ sơ bộ: PG tổng ~3,4GB (max_wal_size 1GB, không replication slot, archive off); uptime-kuma 30MB; `backup-to-gdrive.sh` và `code-backup-to-gdrive.sh` có giữ-N bản local.

## 2. Luật cứng
- CẤM tuyệt đối: rm, mv, truncate, ghi đè file; mọi docker rm/rmi/prune (kể cả builder prune); docker compose up/down/restart; journalctl --vacuum; apt clean/autoremove; git gc/prune; VACUUM; DROP; sửa cron/systemd/config; kill tiến trình. Không ngoại lệ, không "tiện tay".
- du/find chạy `nice -n 19 ionice -c3`, luôn `-x`, có timeout; không quét /proc, /sys.
- Không in nội dung .env, secret, backup mã hoá, dump — chỉ tên + dung lượng + thời gian.
- Đĩa chạm ≥93% trong lúc làm → DỪNG, báo số, không tự xoá gì.
- Không chắc → xếp `UNKNOWN_HOLD` + lý do. Không hỏi Owner.
- Ràng buộc từ tháng 7 (còn hiệu lực): registry Google đã chết → image local-only không dựng lại được từ mã trên VPS = `RESCUE_BEFORE_DELETE`. Image đang chạy, và image là CHA của image đang chạy = KEEP. `postgres:16` dùng chung nhiều container. Cấm đề xuất `docker system prune -a`.
- Khoá chéo R03 (khi chưa CLOSED): image đang chạy + tag rollback R03 (`claude-mcp-local:r03-*`, `agent-data-r03:*`) = `KEEP_ROLLBACK_UNTIL_R03_CLOSED`.
- Chỉ ghi ra 2 nơi: (1) `/opt/incomex/evidence/VPSC-R1-20260920/` — output thô, KHÔNG đưa lên repo công khai; (2) KB theo §8.

## 3. Đo tổng + đối soát — mọi con số phải cộng về được df
- `df -h /`, `df -i /`.
- du theo tầng: `/` (depth 1); `/var/lib`, `/opt`, `/opt/incomex`, `/root`, `/home` (depth 2, gồm thư mục ẩn).
- Docker: `docker system df -v`; `docker buildx du` (tổng + top 20); `docker ps -a -s` (lớp ghi từng container); du `/var/lib/docker` và `/var/lib/containerd` TÁCH RIÊNG — nói rõ có đếm trùng không, con số nào là thật, vì sao.
- Log: từng `*-json.log` (map ra tên container); `/etc/docker/daemon.json` + LogConfig từng container; `journalctl --disk-usage`; du `/var/log`.
- File đã xoá nhưng tiến trình còn giữ: `lsof +L1` (tổng GB).
- Đối soát: tổng các nhóm so với Used của df. Lệch >3GB → tìm ra phần lệch rồi mới kết luận.

## 4. Tìm vòi rò — cái gì tăng từ 24/07, nhanh cỡ nào, cái gì sinh ra
- `find / -xdev -type f -newerct 2026-07-24` (dùng ctime, KHÔNG mtime: `cp -a` giữ mtime cũ) → cộng bytes theo thư mục cấp 2–3; top 30 thư mục tăng mạnh nhất; top 50 file >100MB bất kể ngày.
- Image/container/volume tạo sau 24/07: cộng GB. Vẽ chuỗi cha–con của image local (history/inspect) để biết tag nào gỡ được mà không đứt image đang chạy.
- So từng nhóm với số trong báo cáo 24/07 → tăng bao nhiêu GB, quy ra GB/tháng.
- Rà ĐỦ, không bỏ sót: `deploys/nuxt-output*` (đo trong 1 lần du, báo có hardlink không); image + build cache; lớp ghi container; log docker/journal/nginx; `backups/` local (số bản thật so với LOCAL_KEEP trong 2 script backup — thừa thì vì sao); `evidence/`, `staging/`, `tmp/`, `work/`, `artifacts/`, `exports/`, `context-pack*`; git (.git các repo, sổ git 5 phút của gốc ui, clone incomex-workspace, `mcp-roots`); node_modules/venv (nuxt-repo, agent-data-repo, venv-xlsx); công cụ AI trên VPS: `~/.claude`, `~/.codex`, `~/.gemini`, Hermes, `~/.npm`, `~/.cache` (gồm ms-playwright), pip cache; Qdrant storage + snapshots; PG data dir + pg_wal; swapfile, /tmp, /var/tmp, snap, apt cache, kernel cũ; 2 file >64MB trong `/opt/incomex`; mọi chỗ cách ly do mission 24/07 tạo (còn chiếm chỗ không).
- Mỗi vòi: tiến trình sinh ra nó (script/cron/systemd/mission; đường dẫn + dòng), tần suất, vì sao không có hạn xoá.
- Giải thích: vì sao `incomex-nuxt` chạy image không tag; compose đang tham chiếu gì; nếu compose recreate thì container lên image nào.
- Đo lại df + các thư mục "nóng" ở CUỐI mission (ghi giờ) để thấy cái gì đang tăng ngay lúc này.

## 5. Manifest — phân loại từng ứng viên dọn
Mỗi dòng: đường dẫn/ID · GB · lớp · bằng chứng an toàn · cái gì tham chiếu tới · cách lùi.
Lớp: `DELETE_PROVEN_SAFE` · `QUARANTINE_FIRST` · `RESCUE_BEFORE_DELETE` · `KEEP_PRODUCTION` · `KEEP_ROLLBACK_UNTIL_<ngày|R03_CLOSED>` · `UNKNOWN_HOLD`.
- PROVEN = có bằng chứng: grep đường dẫn/tag trong `/opt/incomex`, crontab, systemd, compose → 0 tham chiếu; có bản mới hơn; dựng lại được hoặc không cần.
- Cộng: GB thu hồi nếu duyệt toàn bộ `DELETE_PROVEN_SAFE`; GB nếu duyệt thêm `QUARANTINE_FIRST`.

## 6. Đề xuất khoá vòi — CHỈ đề xuất, KHÔNG làm
- Mỗi vòi: sửa ở đâu (script deploy / cron dọn định kỳ / luật cho agent), quy tắc giữ bằng con số (N bản / D ngày) + lý do. Đúng dạng: "rollback Nuxt giữ 3 bản mới nhất + bản mốc lớn", không chung chung.
- Chuông đĩa 80% vàng / 90% đỏ — dùng lại công cụ có sẵn (uptime-kuma, cron hiện có) trước khi đề xuất cái mới.
- Đích (T1–T2 trong `view.html`): trống ≥45GB (≤55%) VÀ tăng ≤3GB/tháng ngoài dữ liệu nghiệp vụ. Nói rõ đạt được không, thiếu bao nhiêu, cần gì thêm.

## 7. Chỗ cho Graph — chỉ ước lượng
Theo Điều 39 (dự thảo): Graph = Apache AGE, extension trong PG hiện có, không thêm DB riêng. Ước lượng: image postgres có AGE; dữ liệu graph dựa trên `universal_edges` (đo bảng + index); biên an toàn. Kết luận: sau dọn có đủ không.

## 8. Báo cáo — ghi TRƯỚC khi trả Owner
- Sửa KB `knowledge/current-state/reports/vps-clean-minimum-2026-07-24.md`: chèn mục "ĐỢT 2 — 20/09/2026 · VPSC-R1" lên ĐẦU, giữ nguyên phần cũ bên dưới. Không tạo tài liệu KB mới.
- Thứ tự mục mới: (1) CHO OWNER ≤1 trang: tối đa 3 câu "anh cần quyết gì", mỗi câu kèm đề xuất PM; ma trận hàng = image · build cache · log · deploys/nuxt-output · backup local · công cụ AI · git/repo · PG · Qdrant · khác; cột = Hiện tại GB · Tăng từ 24/07 GB · GB/tháng · Tự dọn? · Thu hồi an toàn GB · Màu (🔴 rò mạnh · 🟡 cảnh báo · 🟢 ổn · ⚪ chưa đo · ✖ không cần); dòng cuối cộng dồn, khớp df. (2) CHO PM: top vòi rò + tiến trình gây ra + đề xuất khoá vòi; manifest đầy đủ. (3) KHO BẰNG CHỨNG: đường dẫn evidence + lệnh đã chạy.
- Viết để 3 tuần sau đọc vẫn hiểu; không kể nhật ký.
- df lần cuối: chứng minh không thay đổi gì ngoài thư mục evidence và tài liệu KB. Thư mục evidence thuộc cây git đang theo dõi thì commit, ghi hash; không thì ghi rõ.
- Trả Owner đúng một dòng: `VPSC-R1-20260920-01: XONG — <3 nguyên nhân chính kèm GB/tháng> · thu hồi an toàn <GB> · KB ĐỢT 2` hoặc `VPSC-R1-20260920-01: DỪNG ở <mục> — lý do ở KB ĐỢT 2`.

## 9. Sau Agent (không phải việc của Agent)
Host tự đo lại bằng công cụ của mình (không tin báo cáo), đưa ma trận + danh sách dọn vào `view.html`, lên Owner cần quyết. Dọn + khoá vòi là lượt sau: sửa chính file này, review/READY lại.
