# PROMPT — VPSC · R5b tiếp nối R5: nạp trần build cache (B5) + tập GIỮ image hữu hạn (KEEP_SET v2) — CÓ MUTATION, KHÔNG XOÁ IMAGE

RUN_ID: VPSC-R5B-20260924-01
Soạn: Claude Chat (Host CLAUDE-VPSC-260920-A), 23/09/2026, sau R5 DỪNG ở B5 (BAO-CAO mục R5, `40c7b73`) và P25 của GPT. **Không chạy lại A, C của R5** (live-restore đã bật; luật (l) đã cài; 3 tag đã xoá hợp lệ). Chỉ làm: (B5) restart dockerd 1 lần có kiểm soát để nạp trần 5GiB; (C') đổi tập GIỮ của luật (l) sang KEEP_SET v2 hữu hạn, cài ở **chế độ thử (không xoá)**, lập kế hoạch xoá cho Host duyệt. Lượt xoá thật là R5c sau khi Host duyệt (nguyên tắc Owner: hành động phá huỷ không để agent tự quyết; JEV host_checkpoint 0,66).
Chỉ chạy khi COLLAB có **`GPT REVIEWED@` + `OWNER_APPROVED@` + Host `READY@` cùng full SHA** commit cuối chạm file này + lệnh RUN.
**Executor_Surface = Claude Code CLI trên Mac → shell root VPS qua SSH, mở bằng `claude --dangerously-skip-permissions`** (Owner cho phép rõ 1 lần `systemctl restart docker` theo B5 — D13). **Write_Path = `fs_*` (gh)**, dự phòng `workspace_*`. Không clone, không ghi repo bằng git.
**Chế độ (D08):** luật cứng dưới đây thay van tự động. Nếu một lệnh vẫn bị bộ phân quyền của phiên chặn → **không lách**, ghi lại và áp nhánh DỪNG tương ứng. Giờ ghi UTC (Z); VPS giữ Europe/Berlin; cron đọc giờ máy và bỏ qua `CRON_TZ`.

## 0. Cổng (chỉ đọc)
1. Read-gate: đọc `AGENTS.md` → `work/vps-clean-20-9-26/COLLAB.md` (A0 vòng 2, D08, D10–D13, P18–P25) → `PROMPT.md` → mục R5 của `BAO-CAO.md`; giấy phép khớp SHA; thiếu `GPT REVIEWED@` → DỪNG.
2. NO_CONCURRENT_VPS_MUTATION — kiểm lại đầu mỗi phần: không `docker build`/`buildx`/`compose … --build`/`buildctl`/`docker pull`/deploy đang chạy; không RUN việc khác đang đụng VPS.
3. Chụp trạng thái trước: `df -B1 /`; `docker ps` (12 container + health + StartedAt); `docker info --format '{{.LiveRestoreEnabled}} {{.ServerVersion}}'` phải `true 29.2.1`; `/etc/docker/daemon.json` sha256 = bản A của R5 (`3ceba3d8…`); web 200; Directus health; Qdrant green + points; `systemctl --failed`; `incomex-kuma-push` active; sha256 cấu hình rclone hiện hành; `ss -ltn`.
4. Hồ sơ: `/var/lib/incomex-audit/VPSC-R5B-20260924/`; dùng lại tệp của R5 ở `/var/lib/incomex-audit/VPSC-R5-20260923/` (`12-daemon.json.B`, `cua-so.py`) sau khi kiểm sha256 khớp BAO-CAO R5.

## 1. Luật cứng
- **CẤM:** `docker buildx …`, `docker builder …`, `docker system df|prune`, `docker image prune`, **`docker image rm` (mọi dạng — lượt này không xoá image)**, mọi `-f/--force`. Docker chỉ được: `docker ps`, `docker image ls`, `docker inspect` (kể cả `--type=image`), `docker info`, `docker version`, `docker logs`, `docker compose … config --images` (chỉ đọc), `docker start <container>` (chỉ trong nhánh lùi B5, đúng container bị dừng, không recreate).
- dockerd: `systemctl restart docker` **đúng 1 lần ở B5** (+ 1 lần lùi nếu B5 hỏng); tuyệt đối không restart khi `LiveRestoreEnabled` ≠ true. Không stop/restart/recreate container; không restart containerd.
- Bí mật: không in nội dung `.env`/token/cấu hình rclone.
- Script trong `/opt/incomex`: commit git cục bộ trước/sau, `bash -n`, thử khô. File ngoài git (`/etc/docker/daemon.json`): bản cũ + sha256 vào hồ sơ trước khi sửa.
- Người gác `scripts/vps-retention.sh`: luật (a)–(k) giữ nguyên từng byte; chỉ sửa phần luật (l).
- Không đụng Kuma, cron/timer, cấu hình backup Drive, múi giờ.
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
B5.2 **Cửa sổ (P24, giữ nguyên):** dùng `cua-so.py` của R5 — không job nào đang chạy/giữ khoá, lượt trước đã xong, job giờ cố định không rơi trong 15 phút tới, job lặp ≤ 60 phút còn ≥ 5 phút, job ≤ 5 phút bắt đầu ngay sau lượt vừa xong và kiểm lượt kế. Theo R5 cửa sổ thực là **00:02Z (07:02 VN) hoặc 18:02Z (01:02 VN)**. Nếu chưa tới cửa sổ: làm C' trước rồi chờ, **tối đa 90 phút**; quá → `BUILD_CACHE = PENDING_RESTART` → DỪNG.
B5.3 Ngay trước: cổng NO_CONCURRENT + chụp lại như cổng 3. Cài `12-daemon.json.B` → `systemctl restart docker` đúng 1 lần.
B5.4 Kiểm (≤3 phút): `systemctl is-active docker`; `LiveRestoreEnabled` = true; 12 container running, **StartedAt không đổi**, health như cổng 3; web 200; Directus ok; Qdrant green + đủ points; cổng nghe như trước; Kuma running + `incomex-kuma-push` active (unit `Requires=docker` sẽ khởi động lại theo) + `kuma-push.sh cron|disk` rc=0; `rclone lsf gdrive-backup:` rc=0; journal dockerd không lỗi; lượt kế tiếp của các job ≤ 5 phút và các job `*/10` gọi `docker exec` chạy bình thường → `BUILD_CACHE = BOUNDED · 5GiB · đã nạp qua restart`.
B5.5 Hỏng bất kỳ điểm nào → cài lại bản A (`3ceba3d8…`) → `systemctl restart docker` (lần lùi) → container nào dừng thì `docker start` đúng container đó → kiểm lại → `BUILD_CACHE = LUI` → DỪNG. Lệnh restart bị bộ phân quyền chặn → `PENDING_RESTART` → DỪNG (không lách).

## Phần D — Kiểm cuối (hỏng → lùi phần gây ra → DỪNG)
- Kuma → Telegram: container Kuma running/healthy; `/etc/cron.d/kuma-push` nguyên; `kuma-push.sh cron|disk` rc=0; `incomex-kuma-push` active.
- Backup Drive: sha256 cấu hình rclone không do lượt này ghi (token tự làm mới bởi cron phái cử được ghi chú nếu đổi); mọi tệp cron/timer trùng byte bản chụp; `rclone lsf gdrive-backup:` rc=0.
- Health như cổng 3; `systemctl --failed` chỉ còn `cloud-init`, `systemd-networkd-wait-online`; số image không đổi (lượt này không xoá).

## Phần E — Báo cáo + ghi repo
- Chèn mục "R5b — Tiếp nối: B5 + KEEP_SET v2 · <ngày> · executor=… · write_path=… · KQ <XONG|STOPPED · bước>" lên ĐẦU `BAO-CAO.md`: (1) CHO OWNER ≤5 dòng; (2) B5; (3) KEEP_SET v2: 5 diễn giải đã áp, bảng theo repository, danh sách sẽ xoá, trần v2 bằng số, sha256 kế hoạch; (4) trước/sau; (5) đường lùi + hồ sơ.
- Repo công khai: không secret/token, IP/tên miền nội bộ, tên tài khoản, output lệnh thô.
- COLLAB: sửa dòng `VPSC.9` thành `MACHINE_DONE · R5b · … · kế hoạch xoá sha256=<…> chờ Host duyệt` hoặc `STOPPED · <phần.bước> · <lý do>`; ngay dưới thêm đúng một dòng `KQ@VPSC-R5B-20260924-01 XONG` hoặc `KQ@VPSC-R5B-20260924-01 DỪNG`. **XONG** = B5 `BOUNDED` đã nạp + C' cài ở `L_XOA=0` + kế hoạch xoá có sha256 + đối chiếu đạt + unresolved làm mất trần = 0 + D đạt. `PENDING_RESTART`, `LUI`, `PENDING_UNRESOLVED` → DỪNG.
- Trả Owner đúng một dòng: `XONG · VPSC-R5b · build cache trần 5GiB đã nạp · KEEP_SET v2 <trước>→<sau> ImageID, sẽ xoá <n> (~<GiB>) chờ Host duyệt · trống <GiB> · xem BAO-CAO.md` hoặc `DỪNG · VPSC-R5b · <phần.bước> · <lý do>`.

## Sau R5b (không phải việc của agent)
Host duyệt kế hoạch xoá (ghi `HOST_APPROVED_DELETE@<sha256 kế hoạch>` vào COLLAB) → R5c ngắn: tính lại kế hoạch, chỉ xoá nếu sha256 trùng bản đã duyệt, đặt `L_XOA=1` → GPT đóng P18/P25 → Đóng việc.
