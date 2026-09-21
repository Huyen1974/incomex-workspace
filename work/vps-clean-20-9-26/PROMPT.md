# PROMPT — VPSC · R1 Kiểm toán đĩa VPS (AUDIT / NO PRODUCTION MUTATION): vì sao đầy lại nhanh + sổ nguồn sinh + danh sách dọn đề xuất

RUN_ID: VPSC-R1-20260920-01
Soạn: Claude Chat (Host việc này), 2026-09-20; đã sửa theo P01–P12 + D04 (xem COLLAB). Owner giao: đánh giá vì sao đĩa VPS đầy nhanh; đề xuất dọn phần không dùng để có chỗ cài Graph DB. Trạng thái KHÔNG ghi ở file này: chỉ tin giấy phép trong `work/vps-clean-20-9-26/COLLAB.md`.
Chỉ chạy khi COLLAB đó có `REVIEWED@` của Founder không soạn (GPT) + Host `READY@` (hoặc `OWNER_APPROVED@`) đúng full SHA commit cuối chạm file này, cộng lệnh RUN hợp lệ.
**Chế độ: AUDIT / NO PRODUCTION MUTATION.** Không thay đổi runtime, config, data, service trên VPS. Chỉ được ghi đúng 3 chỗ ở §2: thư mục bằng chứng thô ngoài Git trên VPS, file báo cáo `work/vps-clean-20-9-26/BAO-CAO.md` trên repo, và một dòng trạng thái VPSC.2 trong COLLAB. Mọi kết quả R1 mang nhãn `UNVERIFIED_R1` cho tới khi Host + thẩm tra độc lập kiểm xong.

## 0. Trước khi làm — cổng đầu vào (DROOT04/DROOT06)
1. Đo `df -h /` TRƯỚC mọi việc khác: Used ≥90% hoặc Available <8GB → chỉ làm phần nhẹ (§3 Docker/log/lsof, §5), bỏ scan toàn cây, báo số.
2. **Executor_Surface = Claude Code CLI** (chạy trên VPS).
3. **Write_Path** theo capability đã audit (README §0/D12), không theo hãng: ưu tiên `workspace_*` (Agent Data); nếu chính phiên này không bind `workspace_*` nhưng bind `fs_*` ("Incomex VPS") đã audit thì dùng `fs_*`. Mọi đọc/ghi repo đi qua đúng family đã chọn, không đổi family giữa chừng. CẤM `git add/commit/push`, GitHub native/App/API/CLI để ghi repo. KHÔNG clone repo (không vào /tmp hay bất kỳ đâu); không đọc thẳng các clone của đầu nối (`mcp-roots/gh`, `data/workspace-tools/…`).
4. Gọi đúng MỘT read-gate của Write_Path đã chọn: đọc `work/vps-clean-20-9-26/COLLAB.md` (`workspace_read` hoặc `fs_read`). Gate fail → DỪNG trước mọi việc, nêu tool đã thử. Ghi `WRITE_PATH=<workspace_*|fs_*>` vào báo cáo.
5. Kiểm giấy phép: full SHA 40 ký tự của commit cuối chạm file này (log theo path qua Write_Path) phải khớp `READY@`/`OWNER_APPROVED@` trong COLLAB — so với commit cuối chạm PROMPT, KHÔNG so với HEAD repo; thiếu/lệch → DỪNG.
6. Đọc `AGENTS.md` (A0 trước tiên) → README §0/§12 → `work/vps-clean-20-9-26/COLLAB.md` (khối 0 trước tiên) + `view.html`, và KB `knowledge/current-state/reports/vps-clean-minimum-2026-07-24.md` — MỐC so sánh, CHỈ ĐỌC (số liệu, danh sách đã dọn, mọi chỗ cách ly ngày 24/07).
7. Đọc dòng R03 trong `work/mcp-workspace/COLLAB.md`: đang deploy thì CHỜ xong mới đo; chưa CLOSED thì áp khoá chéo ở §2.

## 1. Bối cảnh (bạn không nhớ phiên trước)
- **Chính sách storage của Owner (D02, 21/09/2026)** — khung để phân loại và kết luận: VPS chỉ giữ dữ liệu nghiệp vụ + phần runtime thật sự cần để chạy. Dữ liệu vận hành KHÔNG được tăng vô hạn: cần giữ dài thì đưa ra ngoài VPS (Drive/off-VPS) kèm hạn giữ; tái tạo được thì đặt TTL rồi xoá tại chỗ — không mang rác sang Drive để đổi chỗ vòi rò. `3GB/tháng ngoài nghiệp vụ` là NGƯỠNG ĐỎ phải điều tra, không phải mức được phép.
- Ổ `/dev/sda1` 96GB NVMe, Ubuntu 24.04, Docker; mã SSOT tại `/opt/incomex`.
- 24/07/2026 mission VPS-CLEAN-MINIMUM dọn 87% → 61% (trống 13 → 39GB, thu 27,4GB).
- 20/09: ~01Z 83/96GB (trống 14GB); ~12Z 84/96GB (trống 13GB) — thêm ~1GB trong ~11 giờ, trùng lượt build R03 final-close. 21/09 ~02Z: 84/96GB, 88%, trống 13GB. Nhịp TB từ 24/07 ≈ 0,45GB/ngày (~13–14GB/tháng): toàn bộ phần đã dọn bị ăn lại. Hệ gần như chưa có dữ liệu nghiệp vụ mới ⇒ giả thiết công tác: gần như toàn bộ mức tăng là dữ liệu vận hành — phải chứng minh hoặc bác bằng số ở §4.
- Nghi vấn Claude Chat đã thấy (CHƯA đo GB — bạn đo):
  a) `/opt/incomex/deploys/`: ~67 bản sao `nuxt-output.*` (sao 1 bản mỗi lần deploy Nuxt; 12 bản chỉ trong 13–15/09), không hạn xoá.
  b) Image build lại liên tục với tag mới (`agent-data-r03:*`, `claude-mcp-local:*`, `claude-kb-local:*`); claude-mcp có 6 Dockerfile mới trong 17–19/09, mỗi bản FROM tag trước (chuỗi cha–con). Bệnh ~32GB image tháng 7; phần "giữ N tag / dọn sau deploy" của W2 dường như chưa từng làm.
  c) `incomex-nuxt` chạy image KHÔNG TAG (`72715a92885c`).
  d) `/opt/incomex/context-pack-staging/`: gói 3 giờ/lần từ 11/09, 66 gói ~2MB, không xoá gói cũ.
  e) DB `directus_gov_test_20260602` (1,2GB) còn, dù tháng 7 xếp lịch drop; tháng 7 DB này từng chưa có bản off-site. Chấm theo `DB_DELETE_GATE` §6, không theo gate file.
  f) Không thấy giới hạn log (max-size) trong các compose đọc được.
  g) Loại trừ sơ bộ: PG tổng ~3,4GB (max_wal_size 1GB, không replication slot, archive off); uptime-kuma 30MB.

## 2. Luật cứng
- CẤM tuyệt đối: rm, mv, truncate, ghi đè file; mọi docker rm/rmi/prune (kể cả builder prune), docker save/tag/pull/build; docker compose up/down/restart; journalctl --vacuum; apt clean/autoremove; git gc/prune; VACUUM; DROP; sửa cron/systemd/config; kill tiến trình; tải backup từ Drive về VPS; giải mã backup ra đĩa. Không ngoại lệ, không "tiện tay".
- Ngưỡng: bất kỳ lúc nào Used ≥90% hoặc Available <8GB → DỪNG mọi scan nặng, báo số, không tự xoá gì.
- du/find chạy `nice -n 19 ionice -c3`, luôn `-x`, có timeout; không quét /proc, /sys.
- Không in nội dung .env, secret, backup mã hoá, dump — chỉ tên + dung lượng + thời gian.
- Không chắc → xếp `UNKNOWN_HOLD` + lý do. Không hỏi Owner.
- **Hard-KEEP** (R1 không được xếp vào lớp xoá hay cách ly): container + image đang chạy và MỌI image cha của chúng; image Nuxt không tag đang chạy; tag rollback R03 (`claude-mcp-local:r03-*`, `agent-data-r03:*`) tới khi R03 CLOSED; `postgres:16` (dùng chung); volume đang gắn.
- Registry Google đã chết → image local-only không dựng lại được từ mã trên VPS = `RESCUE_BEFORE_DELETE`. Cấm đề xuất `docker system prune -a`.
- R03 chưa CLOSED: mọi đề xuất dọn/image/tag/rescue/restart có thể ảnh hưởng runtime hoặc rollback phải ghi rõ "chờ R03 CLOSED".
- Chỉ ghi ra 3 chỗ: (1) bằng chứng thô tại `/var/lib/incomex-audit/VPSC-R1-20260920/` — LUÔN ngoài mọi cây Git: trước khi ghi, `git -C <thư mục cha gần nhất đã có> rev-parse --is-inside-work-tree` phải báo KHÔNG nằm trong work tree; nằm trong → DỪNG. Tổng ≤200MB, lưu bảng tổng hợp chứ không lưu danh sách file thô toàn cây, đã che secret, có `INDEX.md`. Không bao giờ commit/push, không chép vào repo nào; (2) repo: `work/vps-clean-20-9-26/BAO-CAO.md` theo §9 — bản tóm tắt đã làm sạch; (3) repo: đúng một dòng trạng thái `VPSC.2` trong `COLLAB.md` (§9). Không sửa `PROMPT.md`, `view.html`, `AGENTS.md`, `README.md` hay file nào khác; không ghi KB.
- Repo CÔNG KHAI: `BAO-CAO.md` chỉ chứa số liệu tổng hợp, tên nhóm, đường dẫn, tên image/container/DB và GB. KHÔNG ghi: secret/token/khoá, nội dung .env/config, IP hay tên miền nội bộ, ID thư mục/tệp Google Drive, tên tài khoản, dữ liệu người thật, output lệnh thô. Nghi ngờ → để ở bằng chứng thô trên VPS, báo cáo chỉ dẫn đường tới đó.

## 3. Đo tổng + đối soát
- `df -h /`, `df -i /`.
- du theo tầng: `/` (depth 1); `/var/lib`, `/opt`, `/opt/incomex`, `/root`, `/home` (depth 2, gồm thư mục ẩn).
- Docker: `docker system df -v`; `docker buildx du` (tổng + top 20); `docker ps -a -s` (lớp ghi từng container); du `/var/lib/docker` và `/var/lib/containerd` TÁCH RIÊNG.
- Log: từng `*-json.log` (map ra tên container); `/etc/docker/daemon.json` + LogConfig từng container; `journalctl --disk-usage`; du `/var/log`.
- File đã xoá nhưng còn bị giữ: `lsof +L1` (tổng GB).
- Đối soát: du và df KHÔNG nhất thiết bằng nhau. Giải thích phần lệch bằng: file đã xoá còn mở, hardlink, file thưa (sparse), layer Docker dùng chung / đếm trùng docker–containerd, metadata và block dự trữ của filesystem. Lệch >3GB mà chưa giải thích → không kết luận.

## 4. Sổ nguồn sinh (Generator Registry) — trị tận gốc
Bảng bắt buộc, mỗi dòng một nguồn sinh:
`Nguồn sinh · path · LOẠI · trigger (cron/systemd/script/mission/agent) · tần suất · GB hiện tại · tăng từ 24/07 · GB/tháng · có cần nằm trên VPS không (lý do 1 câu) · trần local đề xuất (N bản / D ngày / GB) · mức ổn định tính ra (= tốc độ sinh × hạn giữ) · nếu phải giữ dài: nơi đưa ra ngoài + ngân sách GB/tháng ở đích + hạn giữ ở đích · nếu tái tạo được: quy tắc xoá tại chỗ · quy tắc giữ hiện có · tự dọn? · nguyên nhân rò · chủ (dịch vụ/agent/mission chịu trách nhiệm)`
LOẠI chọn đúng một trong bốn: `BUSINESS_LIVE` (dữ liệu nghiệp vụ thật) · `RUNTIME_WORKING_SET` (thứ hệ thống đang cần để chạy: image đang chạy và cha của nó, volume đang gắn, DB sống) · `NONBUSINESS_KEEP` (phải giữ dài nhưng không cần nằm trên VPS: backup, archive, bản cứu, bằng chứng) · `DISPOSABLE_REBUILDABLE` (tái tạo được: build cache, log cũ, tmp, artifact, clone/cache công cụ).
Chấm cho mọi nguồn KHÔNG phải `BUSINESS_LIVE`: phải kết thúc ở một trong ba trạng thái — (1) có trần local, mức ổn định tính được từ tốc độ sinh × hạn giữ; (2) đưa ra ngoài VPS, có hạn giữ VÀ ngân sách ở đích; (3) xoá tại chỗ theo TTL. Nguồn nào không rơi vào ba trạng thái đó — tức còn tăng đều theo thời gian — ghi thẳng `FAIL_UNBOUNDED`, dù hiện mới vài trăm MB.
Cấm đề xuất mang `DISPOSABLE_REBUILDABLE` sang Drive: đó là đổi chỗ vòi rò, không phải khoá.
Phủ ĐỦ các nhóm sau; nhóm nào không đo được vẫn có dòng ⚪ + lý do:
Docker image · build cache · volume · lớp ghi container · bản rollback deploy (`deploys/nuxt-output*` — đo trong 1 lần du, báo có hardlink không) · log docker/journal/nginx/`/var/log` · backup local · `evidence/`, `staging/`, `tmp/`, `work/`, `artifacts/`, `exports/`, `context-pack*` · công cụ AI (`~/.claude`, `~/.codex`, `~/.gemini`, Hermes) · git clone/snapshot (.git các repo, sổ git 5 phút của gốc ui, clone incomex-workspace, `mcp-roots`) · npm/pip/playwright cache · node_modules/venv (nuxt-repo, agent-data-repo, venv-xlsx) · PostgreSQL + pg_wal · Qdrant storage + snapshots · swapfile, /tmp, /var/tmp, snap, apt cache, kernel cũ · 2 file >64MB trong `/opt/incomex` · mọi chỗ cách ly do mission 24/07 tạo.
Cách đo "tăng từ 24/07": `find / -xdev -type f -newerct 2026-07-24` CHỈ để KHOANH VÙNG (ctime là lần đổi inode, không phải ngày tạo; dùng thay mtime vì `cp -a` giữ mtime cũ). Đối chứng bằng: btime (`stat -c %W` nếu filesystem hỗ trợ), CreatedAt của Docker, ngày trong tên file, log của trình sinh, số trong báo cáo 24/07.
Kèm theo: top 30 thư mục tăng mạnh nhất; top 50 file >100MB; chuỗi cha–con của image local (history/inspect); giải thích vì sao `incomex-nuxt` chạy image không tag, compose đang tham chiếu gì, nếu compose recreate thì lên image nào; đo lại df + thư mục "nóng" ở CUỐI mission (ghi giờ).

## 5. Backup — chưa chứng minh đủ thì mọi file liên quan backup = `UNKNOWN_HOLD`
1. Cron/systemd/script nào chạy backup (`backup-to-gdrive.sh`, `code-backup-to-gdrive.sh` và mọi cái khác tìm thấy).
2. 5–10 lượt gần nhất mỗi loại: SUCCESS/FAIL, theo log và status marker.
3. Bản remote mới nhất trên Google Drive: liệt kê CHỈ ĐỌC bằng công cụ/cấu hình sẵn có (không tải về, không xoá).
4. Retention thực tế local và remote so với cấu hình (LOCAL_KEEP, REMOTE_KEEP…).
5. Tồn dư `.tmp` / `.partial` / retry / staging.
6. Backup có lồng backup, deploy, evidence, cache, node_modules không — đo phần lồng.
7. Khôi phục: KHÔNG diễn tập restore trong R1 (đĩa 87%, restore tạm cần thêm GB, là việc DR riêng). Chỉ kiểm không tốn đĩa: sha256 khớp `.meta.json`; cấu trúc gói mã hoá đọc được (ví dụ `gpg --list-packets`, không giải mã ra đĩa); dẫn bằng chứng restore gần nhất (mission, ngày, kết quả). Bằng chứng cũ hơn 30 ngày → ghi rủi ro, đề xuất diễn tập sau khi dọn.

## 6. Manifest — phân loại từng ứng viên dọn
Mỗi dòng: đường dẫn/ID · GB · lớp · bằng chứng · cái gì tham chiếu/phụ thuộc · cách lùi · nhóm (để thẩm tra PASS/REVISE/BLOCK theo nhóm).
Lớp: `DELETE_PROVEN_SAFE` · `QUARANTINE_FIRST` · `RESCUE_BEFORE_DELETE` · `KEEP_PRODUCTION` · `KEEP_ROLLBACK_UNTIL_<ngày|R03_CLOSED>` · `UNKNOWN_HOLD`.
- `DELETE_PROVEN_SAFE` chỉ khi đủ CẢ: (a) không container nào (kể cả đã dừng) dùng hoặc gắn; (b) không compose, systemd, cron (mọi user), script nào tham chiếu — grep theo path, tag VÀ digest trong `/opt/incomex`, `/etc`, crontab, unit systemd; (c) không phải rollback còn hạn, không là cha/phụ thuộc của thứ đang dùng; (d) có bản mới hơn hoặc dựng lại được, ghi cách làm; (e) không thuộc Hard-KEEP §2. Thiếu một điều → hạ lớp.
- `DB_DELETE_GATE` — database, schema, bảng lớn KHÔNG dùng gate file ở trên. Chỉ được xếp `DELETE_PROVEN_SAFE` khi đủ CẢ: (a) đúng target: tên, owner, kích thước, ngày tạo; (b) 0 kết nối đang mở (`pg_stat_activity`) VÀ không có hoạt động: chỉ số `pg_stat_database` (xact_commit, tup_*) đọc 2 lần cách nhau ≥30 phút không tăng, tăng thì ghi lý do; (c) không app/DSN/env/compose/cron/job/script/Directus/agent nào tham chiếu tên DB — grep chỉ tên, không in giá trị secret; (d) không phụ thuộc: FDW/dblink, publication/subscription, role/view chéo DB; (e) có backup off-VPS của đúng DB đó + checksum + bằng chứng/cách restore. Thiếu một → `UNKNOWN_HOLD`. R1 chỉ chấm gate; DROP chỉ ở lượt dọn sau khi Owner duyệt.
- `RESCUE_BEFORE_DELETE`: ghi dung lượng ước tính khi cứu, nơi cất NGOÀI VPS (không cất lên chính ổ đang đầy), checksum sẽ kiểm, lệnh khôi phục. Chỉ lập kế hoạch — không save trong R1.
- Cộng: GB thu hồi nếu duyệt toàn bộ `DELETE_PROVEN_SAFE`; GB nếu duyệt thêm `QUARANTINE_FIRST`; GB cần chỗ ngoài VPS để cứu.

## 7. Đề xuất khoá vòi — CHỈ đề xuất, KHÔNG làm
- Mỗi nguồn sinh ở §4: sửa ở đâu (script deploy / cron dọn định kỳ / luật cho agent), quy tắc giữ bằng con số (N bản / D ngày) + lý do. Đúng dạng: "rollback Nuxt giữ 3 bản mới nhất + bản mốc lớn", không chung chung.
- Chuông đĩa 80% vàng / 90% đỏ — dùng lại công cụ có sẵn (uptime-kuma, cron hiện có) trước khi đề xuất cái mới.
- Đích (T1–T3 trong `view.html`): (a) sau dọn trống ≥45GB (≤55%); (b) MỌI nguồn không phải nghiệp vụ đều bounded — có trần local tính được, hoặc đưa ra ngoài có hạn giữ, hoặc tự xoá theo TTL; còn một nguồn `FAIL_UNBOUNDED` là chưa đạt, dù tổng tăng nhỏ; (c) `3GB/tháng ngoài nghiệp vụ` chỉ là ngưỡng đỏ để điều tra, đo theo cửa sổ trượt 14 ngày — không được dùng làm mức "đạt".
- Cộng lại và báo: tổng mức ổn định local dự kiến sau khi áp mọi trần/TTL/offload (GB); so với ổ 96GB; biên còn lại cho Graph và cho 12 tháng tăng trưởng nghiệp vụ; tổng GB/tháng sẽ đổ thêm ra ngoài VPS và đích đó có chịu nổi không (dung lượng Drive còn trống, thời gian đẩy mỗi lượt).

## 8. Chỗ cho Graph — chỉ ước lượng
Theo Điều 39 (dự thảo): Graph = Apache AGE, extension trong PG hiện có, không thêm DB riêng. Ước lượng: image postgres có AGE; dữ liệu graph dựa trên `universal_edges` (đo bảng + index); biên an toàn. Kết luận: sau dọn có đủ không.

## 9. Báo cáo — ghi TRƯỚC khi trả Owner
- Tạo (nếu chưa có) hoặc sửa `work/vps-clean-20-9-26/BAO-CAO.md` — tài liệu báo cáo DUY NHẤT của việc này cho mọi lượt (R1 → thẩm tra Codex → dọn); lượt mới chèn mục mới lên ĐẦU, giữ nguyên mục cũ. Mục của lượt này có tiêu đề "R1 — 09/2026 · UNVERIFIED_R1 · executor=Claude Code CLI · write_path=<…>". Ghi qua Write_Path đã chọn; commit nghiệp vụ `[Claude] VPSC.2 · work/vps-clean-20-9-26/BAO-CAO.md · R1 kiểm toán đĩa (executor=Claude Code CLI)`. KB 24/07 chỉ đọc, không ghi.
- Thứ tự mục mới: (1) CHO OWNER ≤1 trang: tối đa 3 câu "anh cần quyết gì", mỗi câu kèm đề xuất PM; ma trận hàng = nhóm nguồn sinh §4, cột = LOẠI · Hiện tại GB · Tăng từ 24/07 · GB/tháng · Bounded? (trần local / đưa ra ngoài / TTL / `FAIL_UNBOUNDED`) · Mức ổn định dự kiến GB · Thu hồi an toàn GB · Màu (🔴 rò mạnh hoặc `FAIL_UNBOUNDED` · 🟡 cảnh báo · 🟢 ổn · ⚪ chưa đo · ✖ không cần); cộng dồn theo từng LOẠI rồi tổng, đối soát với df. Ngay dưới ma trận: hai con số tách bạch — dung lượng NGHIỆP VỤ và dung lượng VẬN HÀNH (hôm nay, và mức ổn định dự kiến sau khi áp trần). (2) CHO PM: Sổ nguồn sinh §4 · backup §5 · manifest §6 · khoá vòi §7 · Graph §8. (3) KHO BẰNG CHỨNG: đường dẫn + INDEX + tổng dung lượng evidence + lệnh đã chạy.
- Viết để 3 tuần sau đọc vẫn hiểu; không kể nhật ký.
- df lần cuối: chứng minh không thay đổi gì trên VPS ngoài thư mục bằng chứng. Không commit/push bằng chứng thô ở bất kỳ đâu; không để lại file tạm nào ngoài thư mục bằng chứng.
- Cập nhật COLLAB: CHỈ sửa dòng kế hoạch `VPSC.2` thành `MACHINE_DONE · UNVERIFIED_R1 · xem BAO-CAO.md` (hoặc `STOPPED · <lý do ngắn>`), có expected_version; không sửa dòng khác.
- Sau khi ghi repo: đọc lại `BAO-CAO.md` + diff commit, xác nhận chỉ đúng 2 file (`BAO-CAO.md`, `COLLAB.md`) thay đổi và máy quét bí mật không chặn.
- Timeout/`OUTCOME_UNKNOWN`/`RECOVERY_REQUIRED`: đọc lại/journal/commit trước, retry cùng idempotency key; không ghi mù. Ghi repo thất bại hẳn sau khi đã kiểm toán xong → để báo cáo tại `/var/lib/incomex-audit/VPSC-R1-20260920/BAO-CAO.md` và DỪNG kèm đường dẫn đó (Host chuyển lên repo).
- Trả Owner đúng một dòng: `XONG · VPSC-R1 · executor=Claude Code CLI · write_path=<workspace_*|fs_*> · UNVERIFIED_R1 · <3 nguồn sinh chính kèm GB/tháng> · thu hồi an toàn <GB> · xem work/vps-clean-20-9-26/BAO-CAO.md` hoặc `DỪNG · VPSC-R1 · <mục> · <lý do cụ thể>`.

## 10. Sau Agent (không phải việc của Agent)
VPSC.3: Host tự đo lại bằng công cụ của mình (không tin báo cáo), đưa phần đã kiểm vào `view.html`; Codex thẩm tra độc lập theo D03 (GPT soạn đề bài, Claude review), PASS/REVISE/BLOCK từng nhóm, kết quả là mục mới trong chính `BAO-CAO.md`. VPSC.4: Owner duyệt các nhóm đã PASS. Dọn + khoá vòi là lượt sau: sửa chính file này, review/READY lại.
