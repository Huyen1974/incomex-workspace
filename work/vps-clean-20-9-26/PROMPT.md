# PROMPT — VPSC · R5 Vòng 2: đặt TRẦN cho image Docker + build cache (CÓ MUTATION)

RUN_ID: VPSC-R5-20260923-01
Soạn: Claude Chat (Host CLAUDE-VPSC-260920-A), 23/09/2026, sau khi GPT chặn nghiệm thu (P18): image ~10,7GiB + build cache ~0,82GiB còn tăng theo mỗi lần build, chỉ có báo số + cảnh báo 80% — chưa phải trần. **Chỉ làm đúng điểm này, không mở lại phần đã xong** (R1–R4b). Tham khảo JEV `typesafe/jev-1.13`: mở lại VPSC (0,86); gộp live-restore làm bước giảm rủi ro (0,60, Host chốt gộp).
Chỉ chạy khi COLLAB có **`GPT REVIEWED@` + `OWNER_APPROVED@` + Host `READY@` cùng full SHA** commit cuối chạm file này + lệnh RUN.
**Executor_Surface = Claude Code CLI trên Mac → shell root VPS qua SSH.** **Write_Path = `workspace_*`**; dự phòng `fs_*`. Không clone, không ghi repo bằng git.
**Chế độ (D08):** không hỏi quyền từng lệnh; luật cứng dưới đây thay van tự động. Trước mỗi thay đổi ghi trạng thái cũ + cách lùi; sau đó kiểm health; xấu đi → lùi ngay và DỪNG. Giờ ghi UTC (Z); VPS vẫn giờ Europe/Berlin (D11), cron đọc giờ máy và **bỏ qua `CRON_TZ`** (R4b).

## 0. Cổng (chỉ đọc)
1. Read-gate Write_Path: đọc `AGENTS.md` → `work/vps-clean-20-9-26/COLLAB.md` (A0 vòng 2, D08, D10–D12, P18) → `PROMPT.md`; giấy phép khớp SHA; lệch hoặc thiếu `GPT REVIEWED@` → DỪNG.
2. NO_CONCURRENT_VPS_MUTATION — kiểm lại đầu mỗi phần: không có `docker build`/`buildx`/`compose … --build`/`buildctl`/`docker pull`/deploy đang chạy (xem tiến trình); không RUN việc khác đang đụng VPS. Không đạt → chờ ≤15 phút → DỪNG.
3. Chụp trạng thái trước: `df -B1 /`; `docker ps` (12 container + health + StartedAt); web 200; Directus health; Qdrant green + points; `systemctl --failed`; `docker info --format '{{.LiveRestoreEnabled}} {{.Swarm.LocalNodeState}} {{.ServerVersion}}'`; `du -sxB1` thư mục gốc Docker (`DockerRootDir`) + `/var/lib/containerd` + thư mục buildkit (dưới DockerRootDir) bằng `nice ionice -c3`.
4. Hồ sơ: `/var/lib/incomex-audit/VPSC-R5-20260923/` (R4b đã xác nhận `/opt/incomex/work` nằm trong git cục bộ). Không để bí mật trong hồ sơ.

## 1. Luật cứng
- **CẤM (D10/D12):** mọi `docker buildx …`, `docker builder …`, `docker system df|prune`, `docker image prune`, và mọi `-f`/`--force` khi xoá image. Docker chỉ được: `docker ps`, `docker image ls`, `docker inspect`, `docker info`, `docker version`, `docker logs`, `docker image rm <repo:tag|ID>` (KHÔNG `-f`, chỉ phần C).
- Không stop/restart/recreate container; **không restart dockerd/containerd** — chỉ `systemctl reload docker` (SIGHUP), tối đa 2 lần (bật + lùi nếu cần), chỉ phần A.
- Bí mật: không in nội dung `.env`/token/cấu hình rclone; quét tham chiếu image bằng `grep -l`/`grep -o` chỉ lấy chuỗi tên image, không in dòng.
- Script trong `/opt/incomex`: commit git cục bộ trước/sau, `bash -n`, thử khô với `docker` giả. File ngoài git (`/etc/docker/daemon.json`): chép bản cũ vào hồ sơ + sha256 trước khi sửa.
- Người gác `scripts/vps-retention.sh`: luật (a)–(i) và (k) giữ nguyên từng byte (đặc biệt (f) Lark); chỉ THÊM luật (l).
- Không đụng Kuma, cron/timer khác, cấu hình backup Drive, múi giờ.
- Sau mỗi phần kiểm health như cổng 3; xấu đi → lùi phần đó → DỪNG. Phần A lỗi (đã lùi sạch) không chặn B, C.

## Phần A — Bật `live-restore` (giảm rủi ro: nếu dockerd sập, container vẫn chạy)
A1 Kiểm Swarm = inactive (live-restore không dùng với Swarm); chép `/etc/docker/daemon.json` vào hồ sơ + sha256.
A2 Tạo bản mới = bản cũ + `"live-restore": true` (bằng `jq`, giữ mọi khoá khác). Kiểm hợp lệ: `dockerd --validate --config-file <bản mới>` phải OK; không OK → bỏ phần A.
A3 Cài bản mới → `systemctl reload docker` → `docker info --format '{{.LiveRestoreEnabled}}'` = `true`; 12 container StartedAt KHÔNG đổi; health như cổng 3; journal dockerd không lỗi reload.
A4 Sai bất kỳ điểm nào → trả bản cũ → `systemctl reload docker` → kiểm lại → ghi `LIVE_RESTORE = KHONG_BAT · <lý do>` và tiếp phần B.

## Phần B — Trần build cache (không dùng lệnh builder)
B1 Ghi phiên bản: `docker version` (engine, containerd), image store (containerd snapshotter hay không), mục `builder` trong `daemon.json` (hiện có hay không).
B2 **Chứng minh chính sách GC mặc định của BuildKit tích hợp trong dockerd đúng phiên bản đang chạy**, bằng mã nguồn moby (+ buildkit vendored) đúng tag đó (đọc trên Mac qua GitHub; chỉ đọc) và/hoặc tài liệu chính thức của đúng phiên bản. Ghi vào báo cáo: tệp + dòng/đoạn; GC có bật mặc định không; trần là gì (% đĩa / số byte / khoảng trống tối thiểu); chạy khi nào. Quy ra số GiB trên đĩa 96GB này.
B3 Đo thật chỉ đọc: `du` thư mục buildkit + đối chiếu con số 0,82GiB của R4.
B4 Kết luận:
   - Chứng minh được GC mặc định bật + có trần ≤ 10% đĩa → `BUILD_CACHE = BOUNDED · GC mặc định · trần <X>GiB`, không đổi gì.
   - Không chứng minh được (hoặc trần > 10% đĩa) → thêm cấu hình GC tường minh vào `daemon.json` theo đúng cú pháp của phiên bản đang chạy (trần 5GB; kiểm `dockerd --validate`), gộp cùng thay đổi phần A nếu A chưa chạy, hoặc 1 lần `reload` riêng (tính vào giới hạn 2 lần). Ghi rõ cấu hình GC có hiệu lực ngay sau reload hay chỉ từ lần dockerd khởi động kế tiếp (theo mã nguồn) → `BUILD_CACHE = BOUNDED · cấu hình 5GB · hiệu lực <ngay|lần khởi động sau>`.
   - Thêm vào luật (l) dưới đây 1 trường `buildkit_du` (số byte) để theo dõi trần.

## Phần C — Trần image: luật giữ (l) hằng tuần
C1 Thêm luật (l) vào `scripts/vps-retention.sh` (chỉ thêm). **Tập GIỮ**, tính cho từng repository:
   1) mọi image mà bất kỳ container nào (chạy hoặc dừng) đang dùng — so theo ImageID (`docker inspect` của từng container);
   2) mọi tag/ID được nhắc nguyên văn trong tệp triển khai dưới `/opt/incomex` (compose, biến môi trường của compose, unit systemd, manifest/rollback của deploy) và `/etc/systemd/system` — liệt kê danh sách tệp/thư mục đã quét trong báo cáo;
   3) 2 tag mới nhất (theo Created) còn lại của mỗi repository (đường lùi).
   **Xoá:** các tag còn lại bằng `docker image rm <repo:tag>`; image `<none>` không container nào dùng bằng `docker image rm <ID>`. Không `-f`. Lỗi "in use/conflict" → bỏ qua, đếm.
   **Gác:** bỏ lượt nếu đang có tiến trình build/pull/deploy (như cổng 2); dùng chung khoá của người gác.
   **Lịch:** 1 lần/tuần, Chủ nhật, cổng `date -u +%u` = 7 và `date -u +%H` = giờ UTC trùng một lượt chạy thật của cron người gác, khác 18Z (backup Drive), 21Z (k), 01Z (Qdrant).
   **Ghi đúng 1 dòng** vào `/var/log/incomex/vps-retention.log`: số tag giữ/xoá/bỏ qua, số image còn lại, `du` kho image thật, `buildkit_du`. Thêm cờ `--chi-l` (chạy ngay) và `--chi-l-thu` (chỉ in danh sách sẽ xoá, không xoá).
   **Trần tính được:** mỗi repository ≤ (đang dùng + được tham chiếu + 2). Báo cáo quy ra GiB sau lượt đầu.
C2 `bash -n`; thử khô với `docker` giả: nhánh thường; image đang dùng không bao giờ vào danh sách xoá; tag được tham chiếu không vào; giữ đúng 2 tag mới nhất; có tiến trình build → bỏ lượt; socket lỗi → `(l) LOI …` rc=0; cổng giờ/ngày đúng/sai. diff so với bản hiện hành (`45d5bc3`) chỉ có dòng thêm. Commit git cục bộ.
C3 Chạy thật `--chi-l-thu` → danh sách sẽ xoá vào hồ sơ + tóm tắt vào báo cáo (repository · số tag giữ · số tag xoá). **Chốt an toàn trước lượt xoá đầu:** đối chiếu chéo lần hai — không ImageID nào của 12 container nằm trong danh sách; mỗi repository còn ≥ 1 image sau xoá; sai → DỪNG phần C, không xoá.
C4 Chạy thật `--chi-l` 1 lần → 1 dòng log; `du` kho image trước/sau; 12 container StartedAt không đổi + health như cổng 3. (Image đã xoá không lùi được; đường lùi vận hành là 2 tag giữ lại mỗi repository + build lại từ mã. Lùi luật: `git revert` commit (l).)

## Phần D — Kiểm cuối (hỏng cái nào → lùi phần gây ra → DỪNG)
- Kuma → Telegram: container Kuma running/healthy; `/etc/cron.d/kuma-push` nguyên; `kuma-push.sh cron|disk` rc=0; `incomex-kuma-push.service` không failed.
- Backup Drive: sha256 cấu hình rclone hiện hành trước = sau; crontab/cron.d/timer không đổi ngoài luật (l) trong script; `rclone lsf gdrive-backup:` rc=0.
- Health như cổng 3; `systemctl --failed` chỉ còn `cloud-init`, `systemd-networkd-wait-online`.

## Phần E — Báo cáo + ghi repo
- Chèn mục "R5 — Vòng 2: trần image + build cache · <ngày> · executor=Claude Code CLI (Mac → SSH root VPS) · write_path=<…> · KQ <XONG|STOPPED · bước>" lên ĐẦU `BAO-CAO.md` (trên mục KẾT): (1) CHO OWNER ≤5 dòng; (2) live-restore; (3) build cache: bằng chứng mã nguồn + trần GiB; (4) image: tập giữ/xoá theo repository, trần GiB, du trước/sau; (5) trạng thái trước/sau; (6) đường lùi + hồ sơ.
- Repo công khai: không secret/token, IP/tên miền nội bộ, tên tài khoản, output lệnh thô.
- COLLAB: sửa dòng `VPSC.8` thành `MACHINE_DONE · R5 · …` hoặc `STOPPED · <phần.bước> · <lý do>`; ngay dưới thêm đúng một dòng `KQ@VPSC-R5-20260923-01 XONG` hoặc `KQ@VPSC-R5-20260923-01 DỪNG`. XONG = phần B và C đều có trần ghi được thành số + phần D đạt (phần A `KHONG_BAT` đã lùi sạch vẫn XONG, kèm ghi chú).
- Trả Owner đúng một dòng: `XONG · VPSC-R5 · live-restore <bật|không> · build cache trần <GiB> (<cách>) · image <trước>→<sau>GiB, trần <GiB> (luật l hằng tuần) · trống <GiB> · xem BAO-CAO.md` hoặc `DỪNG · VPSC-R5 · <phần.bước> · <lý do>`.

## Sau R5 (không phải việc của agent)
Host nghiệm thu qua BAO-CAO + git + tự kiểm chỉ đọc → GPT xác nhận đóng P18 → `Đóng vps-clean-20-9-26`.
