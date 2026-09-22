# PROMPT — VPSC · R4b Khép việc: dọn dấu vết SEC-01 + báo image (chỉ xem) + sửa dịch vụ failed + đổi múi giờ VPS sang GMT+7 (CÓ MUTATION)

RUN_ID: VPSC-R4B-20260923-01
Soạn: Claude Chat (Host CLAUDE-VPSC-260920-A), 23/09/2026, sau R4 DỪNG ở A3 (BAO-CAO mục R4, commit `3884ba5`). Thay toàn bộ R4 cũ; **bỏ hẳn luật (j) tỉa build cache (D10)**. Tham khảo JEV `typesafe/jev-1.13`: config-drift → sửa trong lượt theo H1 (0,84); `unless-stopped` không tự lên → chỉ chẩn đoán (0,94); unit kuma-push → JEV 0,97 cho "tắt" với GIẢ ĐỊNH nó là bản cũ trùng cron; Host tra mã thấy giả định SAI (đó là bộ nạp token Kuma) ⇒ Host chốt: chỉ chạy lại, cấm tắt (3.2). Trạng thái chỉ tin COLLAB. Chỉ chạy khi COLLAB có `OWNER_APPROVED@` + Host `READY@` đúng full SHA commit cuối chạm file này + lệnh RUN.
**Executor_Surface = Claude Code CLI trên Mac → shell root VPS qua SSH** (phần 1 có thêm shell Mac cục bộ). **Write_Path = `workspace_*`**; dự phòng `fs_*` nếu chính phiên bind. Không clone, không ghi repo bằng git.
**Chế độ (D08):** không hỏi quyền từng lệnh; luật cứng dưới đây thay cho van tự động. Trước mỗi thay đổi ghi trạng thái cũ + cách lùi; sau đó kiểm health; xấu đi → lùi ngay và DỪNG phần đó. Không làm hỏng thứ đang chạy là ưu tiên số 1.
Giờ trong báo cáo: UTC (Z). Sau phần 4, "giờ máy" = giờ VN.

## 0. Cổng (chỉ đọc)
1. `df -B1 /`; read-gate Write_Path: đọc `AGENTS.md` → `work/vps-clean-20-9-26/COLLAB.md` (A0, D08–D10, Handoff H1) → `PROMPT.md`; giấy phép khớp SHA (commit cuối chạm PROMPT, không so HEAD); lệch → DỪNG.
2. NO_CONCURRENT_VPS_MUTATION — kiểm lại ĐẦU MỖI PHẦN: không có `docker build/compose/pull/run` hay deploy đang chạy; không container nào có StartedAt mới hơn 22/09 21:30:05Z mà không giải thích được; không RUN việc khác đang đụng VPS (mcp-token-argv, HJW, HVU…). Không đạt → chờ ≤15 phút → DỪNG.
3. Chụp trạng thái trước: df; `docker ps` (12 container + health); web 200; Directus health; Qdrant green + số points; `systemctl --failed`; `timedatectl`.
4. Hồ sơ lượt (DROOT12): `mkdir -p /opt/incomex/work/vps-clean-20-9-26/R4b/`. Nếu thư mục đó nằm trong phần git cục bộ `/opt/incomex` đang theo dõi (kiểm `git check-ignore`/`git status`) → dùng `/var/lib/incomex-audit/VPSC-R4B-20260923/` và ghi lý do. Không để bí mật trong hồ sơ.

## 1. Luật cứng
- **CẤM mọi lệnh `docker buildx …`, `docker builder …`, `docker system df|prune`, `docker image prune`** (bẫy làm dockerd panic 22/09). Docker chỉ được dùng: `docker ps`, `docker image ls`, `docker inspect`, `docker info`, `docker logs`.
- Không xoá/tag/untag image; không stop/restart/recreate container; không restart dockerd/containerd.
- Bí mật: không in token/khoá/nội dung cấu hình rclone/.env; bí mật chỉ qua biến/pipe; so khớp bằng biến, chỉ in số đếm và đường dẫn.
- Chỉ dừng tiến trình theo PID/launchd. **KHÔNG `pkill rclone`** (từng làm rớt mount Drive trên Mac).
- Script trong `/opt/incomex`: commit git cục bộ trước/sau, `bash -n`, thử khô/mô phỏng nhánh lỗi. File ngoài git (crontab, `/etc/cron.d`, unit systemd): chép bản cũ vào hồ sơ + sha256 trước khi sửa; viết sẵn script lùi trong hồ sơ, script tự tìm thư mục của chính nó.
- Người gác `scripts/vps-retention.sh`: luật (a)–(i) giữ nguyên từng byte, đặc biệt (f) Lark phải giữ thư mục JSONL mới nhất + thư mục mà `daily/_latest_manifest.json` trỏ tới (backup_gate của Lark đọc nó).
- Sau mỗi phần: kiểm health như cổng 3. Xấu đi → lùi phần đó → DỪNG. Một phần lỗi thì lùi phần đó, ghi STOPPED; phần sau vẫn làm nếu không phụ thuộc. **Phần 4 chỉ chạy khi phần 1–3 không để lại thay đổi dở.**

## Phần 1 — SEC-01: dọn dấu vết chìa cũ (chỉ khi chìa cũ đã chết)
1.1 Tìm bản cấu hình cũ `rclone.conf.pre-VPSC-R3-*` trên VPS (cạnh cấu hình rclone của root) và trên Mac (cạnh cấu hình rclone của user). Chỉ in đường dẫn + số lượng.
1.2 Thử chìa cũ bằng từng bản cũ: `rclone --config <bản cũ> lsf <remote>: --max-depth 1` (VPS: remote `gdrive-backup`; Mac: lấy tên bằng `listremotes`). Bỏ stdout; stderr giữ trong biến. Chỉ in OK/LỖI + mã thoát + có/không dấu hiệu lỗi xác thực (đếm `invalid_grant|unauthorized|401` trong biến). **Còn OK ở bất kỳ bản nào → `SEC-01 = PENDING_REVOKE`, bỏ 1.3–1.5.**
1.3 Kiểm chìa mới còn sống TRƯỚC khi xoá: VPS `rclone lsf gdrive-backup: --max-depth 1` bằng cấu hình hiện hành → OK; Mac: mount `drive-workspace` (launchd) đọc được một thư mục. Lỗi → DỪNG phần 1, không xoá gì.
1.4 Xoá dấu vết: nạp token cũ từ bản cấu hình cũ vào biến (không in). `grep -rlF` trong: Mac `~/.claude/`, thư mục cấu hình rclone của user, `~/Downloads`; VPS `/root`, `/var/lib/incomex-audit/`, hồ sơ việc này. Loại trừ cấu hình hiện hành. Nếu khớp file transcript của chính phiên đang chạy → DỪNG phần 1, báo. Tổng 1–5 file → xoá các file đó rồi xoá 2 bản cấu hình cũ. >5 file → không xoá, ghi danh sách đường dẫn vào báo cáo. Sau đó grep lại phải = 0. (Không có đường lùi: đây là dấu vết của chìa đã chết.)
1.5 Kiểm lại như 1.3 → `SEC-01 = REVOKED_CLEAN`.

## Phần 2 — Báo image hằng ngày (chỉ lệnh xem)
2.1 Kiểm `scripts/vps-retention.sh` hiện hành = nội dung `c5b7615` (commit lùi `e9bb42b`); lệch → DỪNG phần 2. **Không dùng bản `vps-retention.sh.r4-sua`** (chứa luật (j) đã bỏ).
2.2 Thêm luật (k), chỉ thêm, không sửa (a)–(i): chạy 1 lần/ngày, cổng giờ dùng **UTC cố định** (`date -u +%H`). Chọn một giờ UTC trùng một lượt chạy thật của cron người gác và khác 03Z (Qdrant). Mỗi lần ghi đúng 1 dòng vào `/var/log/incomex/vps-retention.log` gồm: số image; tổng Size danh nghĩa từ `docker image ls --format`; số image không container nào dùng (so với `docker ps -a` + `docker inspect`); số tag theo từng repo; dung lượng thật của kho image = `nice ionice -c3 du -sxB1` trên thư mục dữ liệu lấy từ `docker info --format '{{.DockerRootDir}}'` (cộng thư mục containerd nếu image store là containerd). Không xoá gì. Lỗi → 1 dòng `(k) LOI …`, không ảnh hưởng (a)–(i). Thêm cờ chạy tay `--chi-k`.
2.3 `bash -n`; thử khô với `docker` giả: nhánh thường → đúng 1 dòng; socket lỗi → `(k) LOI`; cổng giờ đúng/sai. diff so với `c5b7615` chỉ có dòng thêm.
2.4 Commit git cục bộ; chạy thật `--chi-k` 1 lần → 1 dòng log; health không đổi.

## Phần 3 — Dịch vụ systemd failed
3.1 `systemctl --failed`. Với từng unit: `systemctl status`, `journalctl -u <unit> -n 80`, đọc file unit (+ timer) và script nó gọi. Phân loại nguyên nhân: Docker sập 22/09 21:25Z / cấu hình / bản cũ trùng chức năng / hệ điều hành.
3.2 `incomex-kuma-push.service`: **KHÔNG disable, KHÔNG xoá.** Host đã tra: đây là unit nạp token push Uptime Kuma từ `kuma.db` vào tmpfs (`ExecStart=/usr/local/sbin/incomex-kuma-push-fetch`), các monitor nhịp tim khác phụ thuộc nó — KHÁC với `/etc/cron.d/kuma-push` của R3 (đọc token ở `/etc/incomex/kuma-push/`). Hai cơ chế đều cần. Làm: đọc journal → nếu lỗi do container Kuma chưa lên lúc Docker sập 22/09 21:25–21:30Z (hoặc lỗi tạm khác) → kiểm container Kuma đang chạy → `systemctl reset-failed` + `systemctl start` 1 lần → phải active/exited thành công. Lỗi khác → không sửa, báo cáo nguyên nhân. Sau đó: `kuma-push.sh cron` và `kuma-push.sh disk` rc=0.
3.3 `incomex-config-drift-check.service`: đối chiếu Handoff H1 trong COLLAB. Nếu đúng H1 (baseline `mcp-compose` còn `claude-mcp-local:r03-finalclose-20260920`, runtime chạy `claude-mcp-local:hvu-b3-rerun-02-final`):
   - Xác minh bằng `docker inspect` rằng runtime claude-mcp đang chạy đúng image B3.
   - Tìm cổng audited `incomex-config-apply-v0` / config-guard. Có cổng → dùng đúng cổng đó để cập nhật baseline. Chỉ đổi baseline: không đổi image/compose/container, không đổi MCP contract. Sau đó chạy drift-check 1 lần, phải MATCH/sạch.
   - Không có cổng audited, hoặc cổng đòi đổi runtime → không sửa tay baseline, ghi `H1 = CHO_CONG`.
   - Nguyên nhân khác H1 → do Docker sập thì chạy lại 1 lần; khác thì báo cáo.
3.4 `cloud-init.service`, `systemd-networkd-wait-online.service` (của hệ điều hành): chỉ ghi nguyên nhân 1 dòng, không sửa.
3.5 Chẩn đoán chỉ đọc: vì sao 11/12 container `unless-stopped` không tự lên sau panic 22/09 21:25Z. Xem journal dockerd/containerd quanh mốc, `docker inspect` RestartPolicy, `/etc/docker/daemon.json` (live-restore), phụ thuộc unit docker/containerd. Không sửa, không restart. Báo cáo nguyên nhân + đề xuất 1 phương án.

## Phần 4 — Đổi múi giờ Europe/Berlin → Asia/Ho_Chi_Minh, GIỮ NGUYÊN thời điểm chạy thật
Bối cảnh: Berlin đang CEST = UTC+2 (tới 25/10/2026); VN = UTC+7 → giờ trong lịch chạy theo giờ máy phải **+5 giờ**. Qua nửa đêm thì chỉnh ngày trong tuần/ngày trong tháng. Ví dụ: `37 20 * * *` → `37 1 * * *`; `0 3 * * *` → `0 8 * * *`; `0 22 * * 0` → `0 3 * * 1`.
4.1 Kiểm kê (chỉ đọc) → bảng trong hồ sơ, gồm:
   - crontab của root và mọi user;
   - `/etc/cron.d/*`, `/etc/crontab`, file incomex trong `/etc/cron.{hourly,daily,weekly,monthly}`;
   - systemd timer (`systemctl list-timers --all` + file trong `/etc/systemd/system`, user timer nếu có);
   - biến múi giờ: `/etc/environment`, `/etc/default/cron`, `scripts/cron-env.sh`, dòng `CRON_TZ=`/`TZ=` trong crontab;
   - script có cổng giờ bên trong dùng giờ máy (`date +%H/%u/%w/%a/%d` không `-u`, không `TZ=`; đã biết: `scripts/vps-retention.sh` dòng `date +%H` = "04");
   - container mang múi giờ host (Mounts có `/etc/localtime`|`/etc/timezone`, Env có `TZ`).
4.2 **Xác định cron có tôn trọng `CRON_TZ` không.** Căn cứ: gói cron thực tế + giờ UTC thật của các lượt gần nhất trong log/syslog. Crontab root đang có `CRON_TZ=Asia/Ho_Chi_Minh` (code-backup `0 8,12,15,20`) và `CRON_TZ=UTC` (Qdrant `0 3`); báo cáo R3 lại gọi Qdrant là "03:00 giờ máy". Kết luận dòng nào đang chạy theo giờ máy (phải đổi) và dòng nào theo CRON_TZ (giữ nguyên). **Không kết luận được bằng bằng chứng → DỪNG phần 4.**
4.3 Bảng quy đổi mọi dòng chạy theo giờ máy: cũ → mới, UTC trước = UTC sau, tự kiểm từng dòng bằng tính toán. Dòng lặp theo phút/giờ (`*/10`, mỗi giờ) không đổi. Dòng không quy đổi chính xác được → **DỪNG phần 4, không đổi gì**. Được tách 1 dòng thành 2 nếu vẫn đúng tuyệt đối. Trường hợp không quy đổi được: ngày trong tháng ≥28 qua nửa đêm, hoặc danh sách giờ bị cắt qua nửa đêm mà tách không đúng.
   - Cổng giờ trong script: đổi sang `date -u +%H` với giờ UTC tương đương hiện tại (vd 04 Berlin → "02"), để hết phụ thuộc múi giờ.
   - Container mang múi giờ host: KHÔNG restart/recreate. Chỉ ghi bảng: container nào sẽ đổi giờ ở lần tạo lại sau, container nào có lịch bên trong bị ảnh hưởng.
   - Lịch trong container (Directus flow, pg_cron, Kuma) theo múi của container: không đổi, chỉ ghi nếu thấy.
   - File incomex trong `/etc/cron.daily…`: ghi bảng, không đổi.
4.4 Chuẩn bị (chưa áp): lưu bản cũ (crontab từng user, `/etc/cron.d`, unit timer, script) vào hồ sơ + sha256; soạn sẵn bản mới. Soạn `lui-mui-gio.sh`: trả `Europe/Berlin` + khôi phục đúng các file cũ + restart cron + `daemon-reload`. Thử khô nó (in bước, không chạy). Sửa script: commit git cục bộ.
4.5 Chọn phút áp: theo bảng không có job nào (kể cả `*/10` như kuma-push, phái cử ~10 phút/lần) trong ±5 phút; không có tiến trình backup/rclone/deploy đang chạy; khoá `flock` của cron phái cử không bị giữ.
4.6 Áp liền một khối (<2 phút): cài crontab/cron.d/timer/script mới → `timedatectl set-timezone Asia/Ho_Chi_Minh` → restart dịch vụ cron (chỉ cron) → `systemctl daemon-reload` → restart các timer đã sửa.
4.7 Kiểm:
   - `timedatectl` = Asia/Ho_Chi_Minh (+07).
   - `systemctl list-timers`: NEXT (quy UTC) của từng timer incomex = trước khi đổi; không timer nào bắn ngoài lịch.
   - Crontab mới khớp bảng 4.3; log cron không có lỗi.
   - Health như cổng 3; lượt đẩy Kuma #10 kế tiếp OK.
   - Sai bất kỳ điểm nào → chạy `lui-mui-gio.sh` → kiểm lại → DỪNG.

## 4b. HAI TÍNH NĂNG PHẢI SỐNG SAU LƯỢT (kiểm cuối cùng; hỏng cái nào → lùi phần gây ra → DỪNG)
- **Kuma → Telegram (cảnh báo về máy Owner):** không đụng container Kuma, cấu hình Kuma, thông báo Telegram. Cuối lượt: container Kuma running; `/etc/cron.d/kuma-push` còn nguyên (`*/10` không đổi); `kuma-push.sh cron|disk` rc=0; đọc chỉ-đọc trên BẢN SAO `kuma.db` (không mở file đang chạy) → monitor #10 "Cron Heartbeat" và #11 "Disk Usage" có heartbeat UP mới sau lần đổi giờ; `incomex-kuma-push.service` không failed. Không gửi thông báo Telegram thử.
- **Backup lên Google Drive (cron):** cấu hình rclone hiện hành không bị sửa (sha256 trước = sau); mọi job backup Drive (backup chính, code-backup, chuỗi Lark, phái cử) còn trong lịch với thời điểm UTC trước = sau (bảng 4.3); `rclone lsf gdrive-backup:` bằng cấu hình hiện hành OK; lượt phái cử ~10 phút kế tiếp sau đổi giờ rc=0; mount Drive trên Mac đọc được. Tên file backup theo ngày sẽ nhảy +5 giờ: kiểm không có trường hợp hai lượt ra cùng tên (ghi đè) — có nguy cơ → không đổi giờ, DỪNG phần 4.

## 5. Báo cáo + ghi repo
- Chèn mục "R4b — Khép việc · <ngày> · executor=Claude Code CLI (Mac → SSH root VPS) · write_path=<…> · KQ <XONG|STOPPED · bước>" lên ĐẦU `BAO-CAO.md`, gồm:
  (1) CHO OWNER ≤6 dòng;
  (2) SEC-01;
  (3) image + luật (k);
  (4) dịch vụ failed + chẩn đoán `unless-stopped`;
  (5) múi giờ: bảng lịch cũ → mới (giờ VN) + UTC, cron có tôn trọng CRON_TZ không, container mang giờ host;
  (6) trạng thái trước/sau;
  (7) đường lùi từng phần + nơi để hồ sơ.
- Repo công khai: không secret/token, IP/tên miền nội bộ, ID Google Drive, tên tài khoản, output lệnh thô.
- COLLAB:
  - Sửa dòng `VPSC.5f` thành `MACHINE_DONE · R4b · …` hoặc `STOPPED · <phần.bước> · <lý do>`.
  - Ngay dưới, thêm đúng một dòng `KQ@VPSC-R4B-20260923-01 XONG` hoặc `KQ@VPSC-R4B-20260923-01 DỪNG`. XONG = phần 1–4 không STOPPED (`H1 = CHO_CONG` hoặc `SEC-01 = PENDING_REVOKE` vẫn là XONG, kèm ghi chú).
- Trả Owner đúng một dòng: `XONG · VPSC-R4b · SEC-01 <REVOKED_CLEAN|PENDING_REVOKE> · image <GiB> (báo hằng ngày) · failed <trước>→<sau> · múi giờ <Asia/Ho_Chi_Minh|giữ Berlin> · trống <GiB> · xem BAO-CAO.md` hoặc `DỪNG · VPSC-R4b · <phần.bước> · <lý do>`.

## 6. Sau R4b (không phải việc của agent)
Codex V3 chỉ đọc sau một đêm chạy thật: backup Drive 18:37Z (= 01:37 VN), Qdrant, người gác (a)–(i) + (k), Kuma, lịch sau đổi giờ, df. PASS → VPSC.6 theo dõi 2 tuần → đóng việc.
