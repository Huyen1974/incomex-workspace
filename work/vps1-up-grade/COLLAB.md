# COLLAB — vps1-up-grade
Tên việc: Nâng cấp nền tảng VPS1 qua rehearsal an toàn trên VPS2

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
Xác nhận User: **ĐÃ XÁC NHẬN** — chỉ đạo trực tiếp ngày 26/09/2026: mở `work/vps1-up-grade`, tập hợp phương án cũ + ý kiến Claude + bổ sung mới của Owner để hội đồng lập kế hoạch nâng cấp an toàn. Chưa cho phép nâng cấp/dọn/xóa/restart/deploy ở lượt mở việc này.

### 1. Mục tiêu
Nguyên văn/ý nghĩa chỉ đạo Owner:
1. Dùng **VPS2 làm nơi dựng, nâng cấp, sửa và kiểm thử** để VPS1 production vẫn tiếp tục chạy dự án không bị ảnh hưởng.
2. Sau khi target trên VPS2 đạt và đã tập dượt chuyển/rollback, **backup VPS1 rồi triển khai bộ nâng cấp đã chứng minh về VPS1**.
3. Ưu tiên nâng các thành phần phục vụ hệ thống quy trình MOW/MOT/MOIT/MOUT: **PostgreSQL, Directus, Nuxt, Agency OG**; các thành phần khác hội đồng tự cân đối giữ nguyên hay nâng.
4. Chọn **phiên bản mới nhất nhưng ổn định**: không chạy theo bản quá mới chưa đủ tin cậy, nhưng cũng không giữ bản cũ làm mất tính năng cần thiết.
5. Tận dụng hạ tầng sẵn có để giảm thời gian/chi phí/token: **2 VPS + Google Drive dung lượng lớn**, đường backup VPS1 → Google Drive đang hoạt động ổn định.
6. VPS2 chỉ phục vụ e-learning hầu như không hoạt động; Owner ước phần thực cần khoảng **~3GB**, trong khi máy đang dùng tới hàng chục GB. Phải khảo sát nguyên nhân phình dữ liệu và lập phương án dọn trước khi dùng làm lab.

### 2. Thế nào là hoàn thành
- Có inventory đúng thực tế của VPS1/VPS2/Google Drive và xác định phần dữ liệu phải bảo toàn.
- GPT + Claude thống nhất exact target version/digest cho stack ưu tiên trên căn cứ support, độ chín, compatibility, security, license và tính năng cần cho MOW/MOT/MOIT/MOUT.
- VPS2 được backup cần thiết, dọn có kiểm soát, cô lập side effect và dựng được **CURRENT parity clone** đủ để chứng minh migration.
- Có **route/API/UI/runtime test matrix** và **SAME SLICE** chạy trên CURRENT và TARGET.
- Nâng target trên VPS2 theo từng lớp, mọi regression/blocker được sửa hoặc disposition rõ; có restore/rollback proof.
- Tập dượt chính kịch bản cutover VPS1 trên VPS2, có thời gian, checkpoint, failure gate và đường quay lui.
- Trước cutover thật: backup/snapshot VPS1 + bản off-VPS trên Google Drive; triển khai đúng artifact/version/config/migration đã chứng minh; acceptance PASS.
- Nếu cutover không đạt cổng trong giới hạn đã chốt thì rollback được về production trước nâng cấp mà không mất dữ liệu mới hơn điểm dừng đã định.

### 3. Chi tiết cần đạt (AI ghi, Host kiểm)
- **OWNER CHỐT SAU P06, 26/09:** “bản chất chúng ta làm như 1 SaaS vậy. 1 quản trị duy nhất là DOTs qua tài khoản tôi.” Khách đầu tiên là trường; mọi khách chỉ dùng MOT, không có quyền Studio/PG. Cách ly giữa công ty VÀ giữa người cùng công ty nếu chưa được cấp quyền. Owner tái xác nhận điều kiện OIG đáp ứng; không hỏi lại doanh thu/nhân sự. Không tự thêm quản trị thứ hai.
- **P07 thay phần P05 mâu thuẫn:** không chờ thư xác nhận mô hình SaaS hay offline mới được chuẩn bị/nâng cấp. G7 vẫn cần key hợp lệ, telemetry, LC1–LC5, đánh giá LC6 và Owner duyệt rủi ro cụ thể cùng RUN cuối. Chốt kế hoạch chưa phải RUN hay nhận mọi rủi ro chưa đo.
- **Bổ sung Owner 26/09 — COMMERCIAL + OWNER-ABSENT:** làm rõ mô hình Incomex bán ứng dụng/quy trình MOT cho nhiều doanh nghiệp; khách không vào Studio. Doanh thu dưới ngưỡng đã được Owner xác nhận, không hỏi lại; số tài chính cụ thể không đưa thêm vào repo công khai. Một người vận hành kỹ thuật không được tự suy thành tổng headcount pháp nhân. Trước production v12 phải có phương án khi Owner vắng mặt và licensing không liên lạc được; không coi cảnh báo Telegram là đã khôi phục dịch vụ.
- **Phạm vi hiện hành P07:** UI trial không nằm trong cutover; vẫn nâng tương thích shell đang chạy. Offline không còn là điều kiện tuyệt đối. Schema multi-tenant đầy đủ thuộc MMIM, không tự triển khai hàng loạt trong đợt nâng; chưa chứng minh cách ly thì chưa onboard dữ liệu khách thật.
- **Lượt hiện tại chỉ mở SSOT và lập khung khảo sát/kế hoạch.** CẤM mutation VPS1/VPS2, cleanup, xoá, restart, install, upgrade, migrate hoặc đổi DNS/nginx.
- Giữ mô hình lịch sử 08–11/09: **VPS1 = production**, **VPS2 = rehearsal lab**; không coi VPS2 là máy trắng vì vẫn có e-learning cần bảo toàn.
- Tái dùng hai profile cũ:
  - **PARITY CLONE:** đủ schema/config/policies/selected flows/extensions/source-lock/images/files + representative data cần thiết để chứng minh migration semantics; secret/egress production phải thay/cô lập.
  - **SLICE FIXTURE:** cùng một bộ dữ liệu/test cố định chạy trên CURRENT và TARGET, không đổi expected để che regression.
- Backup phải có **restore proof**, không chỉ có file backup.
- “Chuyển về VPS1” ưu tiên theo hướng **chuyển công thức/artifact đã chứng minh** (exact images/digests, compose/config, migrations, runbook), không mặc định chép nguyên máy VPS2 đè VPS1. Đây là đề xuất Host, Claude phải review trước khi thành quyết định.
- VPS2 storage audit phải phân loại ít nhất: business/e-learning data; DB; uploads; Docker images/layers/build cache; logs/journals; backups; temp/cache; source/build artifacts; orphan volumes/bind dirs; dữ liệu có thể tái tạo. Không xoá theo kích thước đơn thuần.
- Trước mọi cleanup VPS2: xác định dữ liệu cần giữ + tạo bản backup off-VPS phù hợp + verify restore/read-back.
- Target-version policy: exact pin, không dùng `latest`; ưu tiên stable/LTS/current supported patch có đủ tuổi/độ chín và ecosystem compatibility; bản mới hơn chỉ chọn khi lợi ích tính năng/security đáng rủi ro.
- **Agency OG:** giữ đúng tên Owner dùng; bước inventory phải xác định chính xác component/package/image hiện tại trước khi chọn target, không tự đổi nghĩa/tên.
- Thành phần ngoài nhóm ưu tiên (Qdrant, Nginx, Docker, Node, worker, MCP/Hermes/JEV/Kuma/backup...) đánh giá theo nguyên tắc **chỉ nâng khi có lý do rõ hoặc dependency bắt buộc**; tránh tăng blast radius.
- Route test matrix phải lấy từ runtime thật: nginx/domain routes, Nuxt pages, Directus/API/auth, workflow endpoints, Owner View/Kuma-monitored URLs và các integration có side effect. Không suy “container healthy = hệ thống PASS”.
- Clone trên VPS2 phải chặn/đổi đích những đường có thể gây tác động thật: Telegram/bot, GitHub write, webhook, mail, cron/schedule, Agent Data, backup production, external storage/API mutation và mọi singleton consumer.
- Cutover phải xử lý bài toán **VPS1 tiếp tục thay đổi trong lúc VPS2 rehearsal**: kế hoạch freeze/delta/final backup + migrate dữ liệu mới nhất; không mang dữ liệu lab cũ về làm production truth.
- Google Drive là lớp backup thứ ba ngoài 2 VPS; phải tận dụng nhưng không thay thế snapshot/rollback cục bộ khi cần phục hồi nhanh.
- Mục tiêu tối ưu: **an toàn trước, thời gian gián đoạn thấp, ít thao tác lặp, ít token**, không xây thêm framework nếu script/tool hiện hữu làm được.

### Vòng trước
Chưa có — mở việc lần đầu theo lệnh Owner ngày 26/09/2026. Các rehearsal 08–11/09 là nguồn lịch sử, không phải production adoption đã duyệt.

Host: GPT Chat
Host_ID: GPT-VPSUP-20260926-A
Owner giao mở việc: 2026-09-26
HTML chính: `view.html`
Owner View: https://vps.incomexsaigoncorp.vn/knowledge/modules?task=vps1-up-grade
Executor_Surface lượt mở: GPT Chat
Write_Path: Incomex MCP full all 2 → workspace_* → root workspace → main

## Dòng hiện hành
VPSUP | **G1 HOST ACCEPTED · CLONE CURRENT READY** | READY@36a2766e5c45389406a3c496a5d1e6378102ab83 | Chưa RUN | NEXT: Claude Code chạy VPSUP-CLONE-CURRENT-20260928-01 → G2 CURRENT parity.
- KQ@VPSUP-VPS2-TRUST-CLOSE-20260928-01 XONG · 28/09 03:50–04:01 UTC · Claude Code CLI · **G1 PASS · NEXT Clone CURRENT.** Read-gate PASS: `fs_stat` gh bind (HEAD `69ef752`); READY@d0b7eef = commit cuối chạm PROMPT; FREEZE còn giữ — `cms_app`/`cms_mysql`/`cms_nginx` Exited + `restart=no`, `cms_queue` không còn; `elearning.*` 200 trang tĩnh; 3307/8080 0 listener v4/v6 và đóng từ ngoài; swap 4 GiB; đĩa trống 78/96 GiB; gói 09/08 CHECKSUMS 7/7; volume `cms_30_dbdata` + bind uploads/storage còn; VPS2 chỉ có phiên SSH của RUN này, không tiến trình apt/rsync/rclone/gpg/build. **Audit allowlist** (chỉ tên/loại/owner/mode; không mở file secret, không in giá trị): **A** user có shell đăng nhập = `root`, `ubuntu`; `/root/.ssh` chỉ có `authorized_keys`, `/home/ubuntu/.ssh` chỉ có `authorized_keys` rỗng ⇒ **0 private key**, 0 `known_hosts`/ssh config (`/etc/ssh/ssh_config.d` rỗng, `ssh_config` mặc định). **B** không có `/root/.config` (0 `rclone.conf`), không có binary rclone, 0 service/cron tham chiếu. **C** 0 thư mục gcloud/google-cloud-sdk, 0 binary gcloud/gsutil, 0 tên `GOOGLE_APPLICATION_CREDENTIALS` trong env container/systemd/`/etc/environment`/profile. **D** 0 `.git-credentials`/`.netrc`; `/root/.gitconfig` chỉ 3 khoá `safe.directory`; 3 repo git cục bộ `/opt/sourecode/{cms_3.0,elearning-web,quiz-app-source}` không remote/credential/url config; `/root/.docker` không có `config.json` ⇒ 0 chứng thực registry; script `/root/*.sh` 0 tham chiếu github/ssh/scp/rclone/gcloud/VPS1. **E** 0 unit systemd tuỳ biến; crontab root/ubuntu rỗng; `/etc/cron.d` chỉ e2scrub/sysstat/`staticroute` (route mạng @reboot); env `cms_app` + `.env`: `AWS_ACCESS_KEY_ID`/`AWS_SECRET_ACCESS_KEY`/`AWS_BUCKET`, `MAIL_USERNAME`/`MAIL_PASSWORD`, `PUSHER_APP_ID/KEY/SECRET`, `REDIS_PASSWORD` đều **rỗng** (mặc định Laravel; `MAIL_HOST` lớp mailtrap mẫu) — SET/EMPTY tính ngay trên máy chủ, không xuất giá trị. Bảng `ID | type | path | owner/mode | referenced_by | destination_class | source_of_truth_outside_VPS2 | needed_now | decision`:
  - `TC-1 | SSH authorized_keys, 1 ED25519 SHA256:l7pXwRfYbiAJ… = khoá Mac contabo_vps2 | /root/.ssh/authorized_keys | root 0600 | sshd AuthorizedKeysFile | inbound Owner/Mac | n/a (khoá riêng ở Mac) | YES | KEEP_INBOUND`
  - `TC-2 | SSH authorized_keys rỗng (0 khoá) | /home/ubuntu/.ssh/authorized_keys | ubuntu 0600 | sshd | inbound, không tin ai | n/a | NO | KEEP_INBOUND`
  - Outbound: **0 candidate** ⇒ REMOVE 0 · KEEP_JUSTIFIED 0 · STOP_UNKNOWN 0 · KEEP_INBOUND 2; T1b (`RETIRE_LOCAL_ONLY_KEY`) không áp dụng.
  - **T1: `VPS1_TRUSTS_VPS2_KEY=NO`** — tập private key VPS2 trong allowlist rỗng. Đối chứng read-only VPS1: `root` `authorized_keys` 1 khoá `SHA256:FqXC/lBid1ZA…` = khoá Mac `contabo_vps` (khác khoá inbound VPS2); user đăng nhập khác không có `authorized_keys`/`authorized_keys2`. Follow-up VPS1: không có.
  - Ghi chú ngoài allowlist — không phải outbound, không mở: credential cục bộ e-learning (DB/`MYSQL_*`/`APP_KEY`) trong `/opt/sourecode/cms_3.0/.env` (🟡 mode 0666), config container đã dừng, bản chụp `docker inspect` của FREEZE ở `/root/vpsup-freeze-20260928/` (thư mục 0700) và gói 09/08 — chỉ tới MySQL cục bộ đã dừng ⇒ thuộc `ROTATE_BEFORE_NEXT_START`; `/root/.gnupg` (BK1 đo 0 secret key); `/root/.docker/.token_seed` (không phải chứng thực registry vì không có `config.json`).
  - **0 mutation:** VPS2 0 thay đổi (không có REMOVE); 0 lệnh bị auto-mode chặn ⇒ không cần Owner Allow once; VPS1 chỉ đọc — `incomex-agent-data`/`incomex-claude-mcp` StartedAt 25/09, RestartCount 0; không gọi Guard/ruleset; không cleanup/MySQL/IPv6/queue/reboot/Clone; nhóm dọn 5 = SKIP BY HOST. Không ghi hồ sơ VPS (giữ 0 mutation VPS1; bằng chứng đủ tại dòng này). JEV `gen-dec-1790567889-OZSx8wsDSmPBOhVHFFE5` (T1=NO 0,97 · DB cục bộ = ghi chú 1,0 · G1 STOP 0,64 độ tin 0,27 khi 3 mục ngoài allowlist chưa mô tả), `gen-dec-1790567917-MWIMEJG29t3u6GpfGhcu` (bổ sung sự thật kỹ thuật 3 mục: G1 PASS 0,87 · ngoài allowlist = ghi chú 1,0).
  - **Đầu vào khoá Clone CURRENT (PROMPT §8, bắt buộc):** chỉ bind `127.0.0.1`/internal, truy cập qua SSH tunnel; chặn outbound của clone trước boot; không chép credential production Telegram/GitHub/OpenAI/Agent-data/rclone/GSM; Directus `KEY/SECRET` khác production; static token `directus_users.token` của clone vô hiệu/đổi trước boot; singleton/cron/Flow webhook/request/backup-retention/Hermes/Kuma/git-push disabled trước boot; dữ liệu production được clone, credential production thì không. Áp: SAME_COMMIT.
- KQ@VPSUP-VPS2-FREEZE-MINLAB-20260928-01 DỪNG · 28/09 02:08–02:40 UTC · Claude Code CLI · read-gate PASS (fs_stat bind; READY@c8d42a0 = commit cuối chạm PROMPT; VPS2 chỉ có phiên của RUN này; AD1-FIX gen2 chỉ là watcher cron — không gọi Guard/ruleset; BK1 lượt đêm đầu: `pg-backup` 00:27Z ra `incomex_metadata_2026-09-28_0027.sql.gz` 103 MB OK, Drive 20:37 CEST = PENDING_TIME). Cổng 5: 30 ngày chỉ 3 lượt khách xem nội dung (gần nhất 08/09), 0 đăng nhập/ghi; dependency duy nhất = iframe GDDH. **A XONG:** `cms_app`/`cms_nginx`/`cms_mysql` restart=no + stop (MySQL tắt sạch), `cms_queue` stop rồi xoá riêng container (lớp ghi chỉ `laravel.log` 9,73 GB) ⇒ hết sinh log; compose `cms_3.0` 4× `restart: "no"`. **A2b PASS:** Caddy hiện hữu `elearning_web` (compose riêng) bind 1 Caddyfile tĩnh, recreate cùng image/cổng/volume TLS: mọi path 200 “Chương trình đang nâng cấp”, không X-Frame-Options/CSP, `no-store`; 2 đường service worker cũ trả worker tự gỡ (xoá cache SPA cũ); iframe kiểm dưới CSP thật của giaoduc hiện thông báo. 3307/8080: 0 listener v4/v6; 80/443 chỉ trang tĩnh; 22 OK. Volume/bind nguyên (MySQL −12,6 MB = `ibtmp1` tự xoá); gói 09/08 CHECKSUMS 7/7; Drive BK1 còn. **B:** nhóm 1–4 thu 22,59 GiB (queue 9,06 · build cache 9,40 · 6 image theo ID 3,39 · journal 0,73); KEEP_SET image nguyên (PG/Directus khớp digest VPS1, 12.3.1/16.15, buildstage, e-learning + rollback; `node:14` giữ vì chung lớp). Đĩa dùng 36,87→18,26 GiB (gồm swap 4 GiB), trống 58,94→77,54 GiB. **C XONG:** `/swapfile` 4 GiB + fstab, unit swap sinh từ fstab; không reboot. **DỪNG vì:** (1) **D chưa làm** — lệnh audit credential outbound (chỉ tên/path/loại) bị auto-mode Claude Code chặn (Credential Exploration); 0 audit/0 xoá; (2) **nhóm dọn 5** (≈0,62 GB thư mục tháng 8) đã chứng minh khớp tuyệt đối tar gói 09/08 nhưng lệnh xoá bị auto-mode chặn. Không phải xung đột runtime. `ROTATE_BEFORE_NEXT_START` còn hiệu lực; busy-lock `DEFER_TO_MCPW_SCOPED_LEASE`. VPS1: 0 mutation, agent-data/claude-mcp StartedAt 25/09 nguyên, Directus/vps/giaoduc 200. Rule SEC1 runtime còn (vô hại; reboot VPS2 không mở lại 3307/8080). Hồ sơ `/opt/incomex/work/vps1-up-grade/VPS2-FREEZE-MINLAB-20260928/` (INDEX, ROLLBACK). JEV `gen-dec-1790561797-CmamwmKLeyuh2IDBX5YZ` (worker tự gỡ 0,90 · xoá container queue 0,96 · web tĩnh unless-stopped 0,84), `gen-dec-1790562879-kUO27SPZkCbUsacKJFAR` (DỪNG 0,75). Áp: SAME_COMMIT.
- KQ@VPSUP-BK1-20260928-01 XONG · 27/09 20:10–20:55 UTC · Claude Code CLI · read-gate PASS (fs_stat bind; READY@aee138a = commit cuối chạm PROMPT; AD1 chỉ còn watcher — đã tự ghi `AD1_24H=FAIL`, AD1-FIX chưa phát; 0 phiên/tiến trình mutation khác trên VPS1/VPS2; phiên Claude khác idle). **A1 `incomex_metadata`:** pg_dump phiên read-only (workflow_admin, giữ owner/ACL) | gzip | gpg recipient hiện hữu `31799F7A…` → Drive `incomex-encrypted-v1/rescue/vpsup-bk1/VPSUP-BK1-20260928-01/vps1/` 109 MB sha `c57aa702…`, md5 Drive = local, read-back sha khớp; restore proof bằng DOT anh em mới `dot-pg-restore-verify-db` v1.0.0 theo K1 (git dot `4b8db03`, `--help` 10 mục, dry-run mặc định; `dot-pg-restore-verify` giữ nguyên): 0 lỗi SQL, 10/10 bảng = số dòng trong artifact (312 814), cấu trúc/owner/ACL/FDW/event trigger = prod (đọc READ ONLY), drift live 0, đối chứng âm fail-closed, 0 residue. Lần chạy 1 FAIL-closed (DOT tạo role thiếu SUPERUSER cho owner event trigger) → sửa DOT trước commit, chạy lại PASS. **A2 `/opt/incomex/data`:** tar posix | gzip | gpg 180 MB sha `63166c01…` (12 203 file / 419 MB); giải mã + giải nén vào tmpfs khớp chính xác 13 651 mục (path/type/size/mode/uid/gid/mtime/sha256) rồi xoá; 🟡 tar rc=1 vì `workspace-tools/queue.sqlite` đang ghi. **A3 e-learning 09/08:** gói 7 artifact (CHECKSUMS 7/7) mã hoá **trên VPS2** → `…/elearning/` 518 MB sha `b33bcc9e…` (VPS2 = VPS1 = Drive read-back); giải mã luồng: sha tar = VPS2, 9/9 file = CHECKSUMS; provenance: DB sống = `cms_elearning_verify` 42/42 bảng (CHECKSUM TABLE EXTENDED + count), UPDATE_TIME cuối 09/08 04:10Z < dump 06:12Z ⇒ không ghi sau dump; nguồn 09/08 không xoá. **B1/B2:** `pg-backup.sh` thêm bản tại chỗ `incomex_metadata` (7 ngày); `backup-to-gdrive.sh` thêm `incomex-prod-metadata-db-<TS>` + `incomex-prod-data-files-<TS>` (lỗi ⇒ degrade như Qdrant: lượt FAIL, Kuma down, không tỉa Drive; retention nhận thêm 2 mẫu tên, `rescue/vpsup-bk1/` ngoài hạn giữ). Kiểm: test VPSC-R3 bản sao + ca mới 155/155; chạy thử bản sao pg-backup với pg_dump thật OK; retention dry-run thật 31 bộ/xoá 0/không chạm BK1; cron không đổi; rollback `BK1-20260928/rollback/rollback-BK1.sh` (byte + sha trước sửa). **K2/K3:** private key chỉ vào keyring tmpfs rồi xoá, keyring root VPS1/VPS2 = 0; bản rõ không chạm đĩa (dump/tar stream thẳng vào gpg; bản giải nén kiểm thử trên tmpfs đã xoá). **Runtime:** 0 restart/recreate; agent-data/claude-mcp image + StartedAt 25/09 không đổi; Directus/vps/e-learning 200; VPS2 3307/8080 vẫn đóng (TEMPORARY), 5 container không đổi. **Gap:** lượt đêm thật đầu tiên có 2 hiện vật mới (28/09 02:27 + 20:37 CEST) cần đọc lại một lần; `queue.sqlite` sao lưu khi đang ghi; DOT mới chưa vào `dot_tools`; e-learning định kỳ, IPv6 VPS2, `cms_queue`, persistent binding 3307/8080 → lượt hardening VPS2 (D22). Hồ sơ `/opt/incomex/work/vps1-up-grade/BK1-20260928/` (INDEX.md). JEV `gen-dec-1790540503-K8wcDcxFDkYbSaFQZbTd` (gate pass 0,96 · dump giữ owner/ACL 0,90 · degrade 0,96 · prefix rescue 0,85). Áp: SAME_COMMIT.
- KQ@VPSUP-SEC1A-DOT-20260927-01 XONG · 27/09 18:43–19:05 UTC · Claude Code CLI · chạy lại theo P22 (AD1 KQ `b9eee89`; read-gate 1–4 PASS: không phiên mutation hạ tầng nào khác, MMIM-MOM04 chỉ UI root `ui`). **Audit:** kho chuẩn Secret Manager `DIRECTUS_SUPERADMIN_BUNDLE` phần `owner` (nhãn purpose=directus-superadmin-dual, 1 version 24/07); custody `owner-admin.env` root 0600 tạo cùng lượt 24/07, DOT đối chiếu ngầm = khớp; Owner không đổi từ 24/07, không OTP. SEC1 hiểu sai vì PROMPT tìm khoá máy admin và cấm tài khoản Owner. Không DOT nào xoá được permission bằng khoá Owner ⇒ Nhánh B: tạo `dot-directus-permission-revoke` v1.0.0 (Tier B, dry-run mặc định, `--execute`/`--restore`, `--help` 10 mục, từ chối policy admin + `directus_*`); git `/opt/incomex/dot` `7288dfd` đúng 3 file (DOT + biển `00-NHAN-THU-MUC.md` + `TEMPLATE-DOT-SCRIPT`). **A ĐÓNG qua DOT:** Public create/update `approval_requests` 2→0 (#620/#621); Public READ 170 giữ nguyên; md5 mọi quyền khác `9fd7e73a…` không đổi; 232 APR không đổi; trace `directus_activity` login + delete bởi Owner, UA của DOT; đã logout; snapshot `/opt/incomex/work/vps1-up-grade/SEC1A-DOT-20260927/revoke-20260927T185237Z-VPSUP-SEC1A-DOT-20260927-01.json`, restore dry-run sẵn. **Health:** Directus/vps/report-pg 200; agent-data + claude-mcp image/StartedAt không đổi (AD1-24h an toàn); crontab không đổi. **B:** 3307/8080 vẫn đóng v4+v6, 80/443 v4 + e-learning 200, TEMPORARY. 🟡 VPS2 mất route IPv6 mặc định (IPv6 cả máy không vào được; không do SEC1; không có AAAA nên người dùng không ảnh hưởng) → hardening. **report-pg:** biển đề xuất ở `web/pages/reports/[report]/index.vue` (cây nguồn Mac) lúc build Nuxt bước 7. **Gap:** DOT mới chưa vào `dot_tools`. P12 đã mang nhãn SUPERSEDED từ trước. JEV `gen-dec-1790534858-YM7aChWiiwno7nuSYU8r` (loader SM + đối chiếu custody 0,85). Áp: SAME_COMMIT.
- KQ@VPSUP-SEC1A-DOT-20260927-01 DỪNG · 27/09 09:27–09:40 UTC · Claude Code CLI · read-gate bước 1–3 PASS (fs_stat bind; READY@3422b41 = commit cuối chạm PROMPT) · **bước 4 FAIL:** RUN `MCPW-AD1-20260927-01` đang dở trên VPS1 (checkpoints: PRE 08:03Z, BACKUP 08:47Z 9 file guard/HJW/HVU timer/kuma-push/crontab; fixture tới 08:58Z; chưa cài, chưa KQ; im ~30′, không phiên SSH khác). Phạm vi không chồng nhưng PROMPT ghi DỪNG; đã hỏi Owner → **Owner chọn DỪNG**. JEV `gen-dec-1790501369-HPV979wQDLyPIeOUXDb1` không chắc (proceed 0,56 / stop 0,40). **0 mutation:** chưa audit DOT/kho, chưa tạo DOT/biển, #620/#621 nguyên, B không đụng. P12 đã mang nhãn SUPERSEDED từ trước. Áp: SAME_COMMIT.
- KQ@VPSUP-SEC1-20260927-01 DỪNG · 27/09 07:24–07:38 UTC · Claude Code CLI · **B ĐÃ ĐÓNG AN TOÀN:** VPS2 3307+8080 chặn internet cả IPv4 (DOCKER-USER ×2, conntrack cổng gốc) lẫn IPv6 (ip6tables INPUT ×1 — G0 sót: `docker-proxy` nghe `[::]`); từ Mac 3307/8080 đóng, 22/80/443 + e-learning 200; 0 restart, internal PASS; TEMPORARY_UNTIL_PERSISTENT_BINDING, rollback ở view §9. **A CHƯA ĐÓNG (0 mutation):** preflight A5 FAIL — không có khoá máy nào quản trị được permissions (admin active duy nhất = tài khoản Owner chỉ mật khẩu; break-glass `6abdec55…` suspended); PROMPT cấm mật khẩu Owner + SQL. Public #620/#621 vẫn nguyên, 0 lượt ẩn danh từ trước tới nay. JEV `gen-dec-1790494394-xVvgBxPYnQ3cOTgZvh4W`. Read-gate: RUN MCPW-AD1/MMIM-MOM01 đã phát nhưng không thấy mutation hạ tầng đang chạy trên VPS1/VPS2. view §10 ngoài phạm vi ghi của PROMPT nên chưa cập nhật. Áp: SAME_COMMIT.
- KQ@VPSUP-G0-20260927-01 XONG · 27/09 03:10–03:50 UTC · Claude Code CLI · chỉ đọc: 0 mutation VPS1/VPS2, 0 file ghi trên VPS · A–G, I đo live; H ⚪ (API Contabo cần POST lấy token, PROMPT chỉ GET); J từ mã nguồn directus v12.3.1/v12.4.1 + docs. 🔴 4: Public ghi ẩn danh `approval_requests` (VPS1) · MySQL 5.7 cổng 3307 mở internet (VPS2) · `incomex_metadata` + `/opt/incomex/data` không có backup (F6 đúng) · e-learning không có bản trên Drive. VPS2 dọn được ≈ 26 GB (sổ ở view §9, chưa xoá gì). Áp: SAME_COMMIT.
- HEAD trước mở việc: `545157ae4d0a58d72274063800ad0b65d9ad76ef`.
- Lượt này chỉ tạo SSOT của task; không mutation hạ tầng.
- Hậu kiểm P07: commit `d4cbb2f5e7d45d530dbcb1f488622c2e7b33c174` đã push, diff đúng hai file và GitHub native đọc lại đúng P07. Owner View mở đúng URL chuẩn trả HTTP200 nhưng ui_inspect chỉ thấy shell/Login + 401 header, không đọc được iframe. **DỪNG nghiệm thu nội dung Owner View — CHƯA XÁC MINH**, không suy trang bị khoá hoặc đã publish đúng revision. Không tạo bản xem/pipeline khác; không sửa runtime ngoài scope.
- Áp mở việc: `7275ef1966c09016a372128b9934dcf93abbac98`.

## Quyết định Owner
- D01 · 2026-09-26 · **MỞ VIỆC:** tạo `work/vps1-up-grade` để hội đồng lập kế hoạch nâng cấp VPS1 qua rehearsal trên VPS2. Chưa cho phép thực thi nâng cấp.
- D02 · 2026-09-26 · **TOPOLOGY:** VPS1 là production tiếp tục chạy; VPS2 dùng làm nơi dựng/nâng/fix/test trước khi chạm VPS1.
- D03 · 2026-09-26 · **CORE PRIORITY:** PostgreSQL + Directus + Nuxt + Agency OG là nhóm cần xem xét nâng cấp ưu tiên để phục vụ hệ MOW/MOT/MOIT/MOUT. Thành phần khác hội đồng cân đối.
- D04 · 2026-09-26 · **VERSION POLICY:** GPT + Claude phải thống nhất phiên bản “mới nhất nhưng ổn định”; không chọn bleeding-edge thiếu bằng chứng, cũng không neo bản cũ nếu làm mất tính năng hữu ích.
- D05 · 2026-09-26 · **VPS2 STORAGE:** phải khảo sát vì e-learning gần như không hoạt động nhưng VPS2 dùng hàng chục GB; Owner ước workload thực chỉ khoảng ~3GB. Có thể dọn phần vô ích nhưng phải phân loại/backup trước.
- D06 · 2026-09-26 · **BACKUP ASSET:** ngoài 2 VPS có Google Drive dung lượng lớn; VPS1→Google Drive đang kết nối ổn định. Kế hoạch phải tận dụng tài sản này để giảm rủi ro và thời gian.
- D07 · 2026-09-26 · **LONG-TERM / PRODUCT-FIRST:** Incomex thực tế chỉ có Owner vận hành và Owner không làm kỹ thuật IT. Mọi lựa chọn nền tảng phải ưu tiên sản phẩm đang sống, đáng tin, có cộng đồng/nhà phát triển duy trì, cài/lắp ráp được; **code và tự duy trì framework là giải pháp cuối cùng**.
- D08 · 2026-09-26 · **AGENCY OS = LEGACY / EXIT:** việc dựa vào Agency OS đã ngừng phát triển được coi là lựa chọn không bền. Không tiếp tục coi Agency OS là nền tảng dài hạn; lập kế hoạch **thoát dần**, không big-bang và không thay bằng một template phụ thuộc cá nhân khác. Chưa chốt sản phẩm thay thế trước trial.
- D09 · 2026-09-26 · **DIRECTUS STRATEGIC GATE:** Directus là quyết định kiến trúc dài hạn; phải kiểm chính sách license/OIG, giới hạn, telemetry/license-server dependency, security/support và exit path trước khi production adoption v12. Không được chọn chỉ vì “đang dùng rồi” hoặc để giải quyết nâng cấp cho xong.

## Quyết định bổ sung — phân biệt thẩm quyền
- D10 · OWNER · 2026-09-26 · Mô hình cần xét: Incomex vận hành nhà máy quy trình, bán sản phẩm/ứng dụng riêng; người dùng khách hàng làm việc bằng MOT, không dùng Directus Studio. Phải làm rõ ngưỡng doanh thu/nhân sự đúng chủ thể và sự cố kỹ thuật khi Owner vắng mặt. Chưa đăng ký/chấp nhận điều khoản/mua giấy phép thay Owner.
- D11 · HOST · 2026-09-26 · Nhận P04: UI low-code trial không nằm trong cutover VPS; không mở thêm task trong lượt này. Giữ D07–D08 về hướng thoát Agency OS, nhưng nâng tương thích shell đang phục vụ vẫn thuộc việc này. Không viện dẫn một luật “cấm mọi DB thứ hai” khi chưa có văn bản đúng scope; lý do tách là phạm vi, tài nguyên và một nguồn quyết định UI.
- D12 · HOST · 2026-09-26 · LICENSE CONTINUITY là tiêu chí nghiệm thu, không chỉ alert. Phân loại lỗi đường mạng Incomex / sự cố licensing phía Directus / key-binding / người liên hệ vắng mặt; kiểm phục hồi và trạng thái thực trên exact build. Không tự tạo tổ chức khác, reset định danh, xoay key hay sửa clock để kéo dài thời hạn.
- D13 · HOST · 2026-09-26 · Giữ major PG riêng; nếu PG18 chưa đạt, xem xét app target trên patch PG16 còn hỗ trợ đã kiểm tương thích. Exact version chốt bằng advisory + hỗ trợ + rehearsal tại G3/G7; không có luật cứng chờ 8 tuần khi bản vá bảo mật áp dụng cần lên sớm.

- D14 · OWNER · 2026-09-26 · **SAAS CHUNG:** một hệ PostgreSQL, khách/trường là tenant bằng mã công ty + quyền; không DB/engine/hệ quản trị theo khách. Không xoá/gộp các database hiện hữu chỉ vì câu “1 CSDL”. Khách sở hữu dữ liệu của mình theo hợp đồng, không được giao Directus/PG/Studio.
- D15 · OWNER · 2026-09-26 · **MỘT CHỦ QUẢN, DOT 100%:** Owner duy nhất quản trị, bình thường không dùng Studio; người/AI thao tác nghiệp vụ qua MOT→DOT/MCP. Khóa máy ít quyền do Owner quản không phải người quản trị thứ hai. Thiếu DOT: tái dùng native trước, chỉ ghép/bổ sung DOT cần thiết; không phát SQL/admin tự do.
- D16 · OWNER · 2026-09-26 · **KHÔNG HỎI LẶP:** Owner xác nhận điều kiện OIG đáp ứng. Một admin là giới hạn vận hành, không đổi định nghĩa employee trong điều khoản. Không xin thêm xác nhận SaaS đã thuộc FAQ; đăng ký/nhận key/contact vẫn hợp lệ. Telegram cảnh báo sớm; email pha sau.
- D17 · HOST · 2026-09-26 · **CONDITIONAL RELEASE:** nhận P06-D, bỏ chặn offline tuyệt đối P05. G7 cần LC1–LC5 đạt, LC6 đo ảnh hưởng/phần chưa biết, phục hồi/rollback và residual risk được Owner duyệt cùng RUN cuối. Không gọi outage >7 ngày “hiếm” khi chưa có dữ liệu hoặc lỗ hổng đã công bố là bằng chứng đang bị khai thác.
- D18 · HOST · 2026-09-26 · **KHÓA TRƯỚC, BÁO SAU:** quyền read/write ràng tenant + actor + bản ghi/field; không tin filter client. Runtime không mượn toàn quyền Owner. Ngăn tự cấp Studio/Admin bằng quyền native và DOT quản trị có biên; kiểm hằng ngày chỉ phát hiện lệch. Chưa cài thêm chốt trong lượt này.
- D19 · OWNER · 2026-09-27 · **DIRECTUS/PG = DOT-ONLY:** toàn bộ credential Directus nằm trong Secret Manager; Owner không giữ tài khoản để thao tác. Người/AI/Agent không vào Studio/psql/direct API để mutation. Mọi thay đổi Directus/PG phải gọi DOT/MCP được duyệt; thiếu capability thì bổ sung DOT trước. `report-pg` là màn hình kiểm kê/read-only, không phải cửa ghi.
- D20 · HOST · 2026-09-27 · **SEC1-A ĐỔI CỬA VÀO:** KQ DỪNG trước là do PROMPT sai khi đi tìm “machine account đủ quyền”. OQ chọn Studio/admin key bị hủy. Lượt kế tiếp chỉ audit DOT/Secret Manager và đóng #620/#621 qua DOT; DOT được phép dùng Owner-admin credential qua kho/loader chuẩn mà Agent không thấy; không direct REST/SQL.
- D21 · OWNER · 2026-09-27 · **DOT MỚI PHẢI DỄ TÌM + DỄ DÙNG:** nếu phải viết DOT mới, mô tả phải đủ để AI sau biết ngay nó làm gì, dùng lúc nào, không dùng lúc nào và cách dry-run/execute/rollback. Biển ngắn đặt tại thư mục DOT + template; không tạo hướng dẫn dài tách rời.
- D22 · OWNER · 2026-09-28 · **VPS2 LÀ MÁY TẠM, KHÔNG ĐẦU TƯ DÀI HẠN:** VPS2 chỉ giữ e-learning tạm + làm lab nâng VPS1. Sau BK1 chỉ làm một lượt “tối thiểu an toàn + chuẩn bị lab”: đóng bền 3307/8080, đổi/root-localhost MySQL credential qua Secret Manager, dừng `cms_queue` để chặn log phình, dọn phần tái tạo được + swap/trần RAM, gỡ mọi credential/đường tin cậy bền từ VPS2 sang VPS1/Drive/Secret Manager, và cài cờ/lease máy-bận dùng chung cho RUN hạ tầng. **Không** nâng MySQL trên VPS2, không sửa IPv6, không sửa queue, không dựng backup/monitor riêng lâu dài cho VPS2. Khi VPS1 nâng cấp xong và ổn định 7 ngày: chuyển e-learning về VPS1 trong mạng/container riêng, không public DB; e-learning là ngoại lệ có kiểm soát của luật một PostgreSQL vì phần mềm mua sẵn bắt buộc MySQL. Nếu chưa cần dùng thì giữ stack e-learning inactive/stopped mặc định; chỉ khi cần bật mới hoàn tất compatibility/security upgrade MySQL được hỗ trợ. Backup cuối mã hoá + đối chiếu kỳ Contabo rồi huỷ VPS2.
- D23 · OWNER · 2026-09-28 · **FREEZE E-LEARNING TRÊN VPS2, GIẢM VIỆC HƠN D22:** BK1 đã có bản offsite + restore proof, hiện không có người học. Vì vậy lượt kế tiếp ưu tiên **stop toàn bộ stack e-learning và no-autostart**, giữ compose/volume/image + bản 09/08 để phục hồi; không cần rotate/nâng MySQL trên VPS2 nếu stack không chạy. 3307/8080 phải hết listener do stack dừng; `cms_queue` hết sinh log theo cùng cơ chế. Chỉ nếu có yêu cầu thật sự phải bật lại VPS2 trước khi chuyển sang VPS1 thì **trước khi bật** mới rotate credential/root-localhost + kiểm security. VPS2 sau freeze chỉ là lab nâng VPS1. Cờ/lease máy-bận **không viết hệ riêng trong VPSUP**; tái dùng scoped lease đang được `mcp-workspace` xây dựng khi sẵn sàng. **Điều kiện giao diện công khai:** sau freeze, `elearning.incomexsaigoncorp.vn` được giữ bằng đúng một trang HTML tĩnh “Chương trình đang nâng cấp” trên web/TLS hiện hữu để iframe GDDH không vỡ; không PHP/DB/queue/API và không tạo service/port mới.

## Ý kiến hội đồng
### P01 · GPT Host · ACCEPTED — kiến trúc migration đã được Claude P02 đồng ý
- Based_on: chỉ đạo Owner 26/09 + rehearsal lịch sử 08–11/09 + việc `vps-clean-20-9-26` đã đóng.
- Scope: `view.html` §1–§10.
- Đề nghị:
  1. Không “copy nguyên VPS2 về VPS1”; chuyển **reproducible deployment formula** đã chứng minh: exact image/digest + compose/config + migrations + runbook + acceptance tests.
  2. Trình tự an toàn: **read-only inventory → backup/restore proof → VPS2 cleanup có kiểm soát → CURRENT parity clone → baseline route/slice → nâng từng lớp → TARGET same-slice → rollback rehearsal → cutover rehearsal → production cutover**.
  3. Chưa nâng Qdrant/Nginx/Docker/... chỉ vì có bản mới; chỉ nâng nếu dependency/security/tính năng cần thiết.
  4. Version target lịch sử 11/09 chỉ là reference stale; vòng này phải refresh nguồn chính thức rồi Claude cross-review.
  5. Production cutover phải time-box; quá gate thời gian hoặc core acceptance FAIL thì rollback, không “cố sửa trên production”.
- Trạng thái: **ACCEPTED** về kiến trúc migration; P02 đã đồng ý P01.1–5. Chi tiết version/license/UI strategy được Host xử lý riêng ở P03.

### Yêu cầu Claude Reviewer vòng 1
Đọc `AGENTS.md` → §0 file này → `view.html`. Ghi phản biện P02 ngay tại đây, không tạo file review mới. Tập trung 6 câu:
1. Chính sách chọn exact version cho PG/Directus/Nuxt/Agency OG có đủ cân bằng mới–ổn định chưa?
2. VPS2 phải đo/dọn những gì để thật sự chỉ giữ e-learning + lab capacity cần thiết?
3. PARITY CLONE tối thiểu cần gì để không test giả nhưng cũng không copy production vô tội vạ?
4. Route/API/UI/runtime matrix nào đủ chứng minh “VPS2 PASS ⇒ có cơ sở chuyển VPS1”?
5. Cutover/rollback nào ít downtime và ít thao tác nhất với backup Google Drive đang có?
6. Thành phần nào ngoài core nên giữ nguyên, thành phần nào bắt buộc nâng do dependency?

### P02 · Claude Chat (Reviewer) · PARTIAL — phản biện P01, Host đã xử lý tại P03
- Based_on: `dd67cc8` (COLLAB `b0fca0c3`, view `443a5786`). Scope: §0, P01, `view.html` §1–§10, Q01–Q08.
- Nguồn đo/đọc 26/09: VPS1 live (`vps_status` containers/resources, `SHOW server_version`, compose `docker/nuxt-repo/infra/docker/docker-compose.yml`, nginx `docker/nginx/conf.d/default.conf`); `cấu trúc hệ thống.html` v1.6.20 (Drive, W002-FEAS §1/§6/§7); nguồn chính thức tra 26/09: postgresql.org/support/versioning · directus.com/docs (licensing, breaking-changes/version-12) + npm · nuxt.com roadmap · nodejs.org · qdrant releases · api.contabo.com.
- Chưa đọc: VPS2 live (Chat không có đường đọc), `KHO/11-evidence/.../PLATFORM.md`, chi tiết HJW.
- Kết luận: **ACCEPT P01.1–5.** Bổ sung 5 phát hiện làm đổi ưu tiên + trả lời 6 câu.

**Phát hiện (đo 26/09)**
- F1 🔴 **Directus 11 đã hết vá bảo mật.** Advisory 24/06 và 05/08/2026 (có 1 Critical WebSocket, SQLi PostGIS, SSRF; GHSA-97xr-jchp-xm3c, GHSA-j5h6-vqc3-phqh) chỉ vá ở 12.0/12.1; dòng 11 dừng ở 11.17.4 (30/04). VPS1 chạy 11.5.1 và mở ra `directus.*` + `/directus/`. ⇒ Nâng Directus là **bắt buộc**, không còn là tuỳ chọn tính năng. G0 đo ngay (chỉ đọc) mức lộ: WebSocket có bật không, ai vào được admin.
- F2 🔴 **Directus 12 = license MSCL.** Không key → Core tier: 25 collections · 5 flows · 3 seats, custom rules trên access policy bị bỏ qua; hết 30 ngày ân hạn thì khoá `/items`. Hệ có ~145 collections, 128 flows ⇒ **không có key Open Innovation Grant thì không được nâng.** OIG: doanh thu < 5 triệu USD và < 50 người; key 1 năm, tối đa 5 lần kích hoạt; bắt telemetry 6 giờ/lần; kích hoạt cần `PUBLIC_URL` hợp lệ. Tài liệu cũ ghi Owner "dưới 5 triệu VND" → cần Owner xác nhận lại đúng đơn vị + số người (OQ-A dưới).
- F3 🟡 **Nhãn trôi trên VPS1:** `postgres:16`, `qdrant/qdrant:latest`, `directus/directus:11.5`, `nginx:alpine`. Qdrant bắt buộc lên từng minor (1.16→1.17→1.18→1.19); một lần pull/recreate có thể nhảy thẳng 1.19.x và hỏng storage. `postgres:16` tự lên 16.15 thì phải REINDEX btree_gist. ⇒ Một lượt nhỏ **ghim digest đang chạy** trước mọi việc (không restart, không đổi phiên bản) — mutation prod, chờ Owner (OQ-B). Bậc 2.
- F4 🟡 **Q01 · Agency OG = Agency OS.** `docker/nuxt-repo/web/README.md`: "AgencyOS … Nuxt 3 + Directus". Upstream `directus-labs/agency-os` đứng yên từ 26/03/2025, không release, không hỗ trợ Nuxt 4. ⇒ "Nâng Agency OG" = **tự nâng bản fork** (Nuxt 3→4, SDK 19→khớp Directus 12, Node 20→24); không có bản upstream để kéo về (OQ-C).
- F5 🟡 **VPS1 và VPS2 đang dính nhau.** `giaoduc.incomexsaigoncorp.vn` (cổng GDĐH; cấu hình ghi "phục vụ đoàn kiểm tra") chạy trên Nuxt VPS1 và nhúng `elearning.incomexsaigoncorp.vn` (VPS2). ⇒ (a) e-learning không phải "không ai xem": lab không được làm chậm/sập nó; (b) ma trận test phải có host giaoduc + iframe; (c) cửa sổ cutover tránh lịch kiểm tra.

**1. Chính sách version — ACCEPT, thêm 3 luật đo được**
- (i) Đích = **patch mới nhất của dòng đã GA ≥ 8 tuần và đã có ≥ 1 patch sau .0**, lấy tại ngày G3; (ii) EOL chính thức còn > 18 tháng; (iii) ghim **digest**, không tag.
- Ứng viên 26/09 (refresh tại G3):

| Thành phần | Hiện | Ứng viên | Lý do |
|---|---|---|---|
| PostgreSQL | 16.13 | **18.x mới nhất (18.6)** | GA 25/09/2025, EOL 11/2030 (16: 11/2028). 3,4 GB/5 DB → dump/restore vài phút, rẻ nhất lúc dữ liệu còn nhỏ, tránh một lần cutover nữa. PG19 còn beta. Lab đi 2 nấc 16.15 → 18.x. Lưu ý PG18: checksum mặc định, volume path đổi, REINDEX btree_gist. JEV `gen-dec-1790407432-rNCS9EhUXn5ZJZFKVdtB`: pg18 0,74 · pg17 0,18 · pg16 0,08. |
| Directus | 11.5.1 | **12.4.x** — patch mới nhất tại G3; không lấy 12.4.1 (ra 23/09) | F1. Breaking 12.0–12.4 (health cần auth → `/server/ping`, `IP_TRUST_PROXY`, Flow update/delete, Tiptap, collection inactive 403…) mỗi mục thành 1 dòng kiểm. JEV 0,98. |
| Nuxt (Agency OS fork) | 3.20.2 | **4.5.x** | Nuxt 3 EOL 31/07/2026; Nuxt 5 dự kiến Q4/2026, Nuxt 4 còn hỗ trợ 6 tháng sau đó. |
| Node (Nuxt) | 20.20 (EOL 30/04/2026) | **24.x LTS** (24.21.0) | Nuxt 4.5 đã bỏ Node 20. Node của Directus theo image chính thức (22). |
| @nuxt/ui | ^2.18.2 | **giữ 2.22.3** (chạy được trên Nuxt 4) | v4 = viết lại UI (Tailwind 4, Reka UI, đổi tên component) → tách việc sau. JEV 0,87. |
| @directus/sdk | ^19.1.0 | **major khớp Directus đích** (12.4 ↔ 26) | 12.0 đổi `RequestError`. |

**2. VPS2 đo/dọn gì**
- Bước 0, trước mọi thứ: backup e-learning (DB + mã + uploads + nginx/TLS) lên Drive **và restore thử** vào container tạm ngay trên VPS2 — dữ liệu ~994 học viên cũ là bản duy nhất.
- Đo bằng đúng khuôn "Sổ nguồn sinh" đã chạy ở `vps-clean-20-9-26` (Bậc 1: tái dùng): `du` theo tầng + `docker system df -v` + build cache + journal + `lsof +L1`; mỗi dòng 1 nhãn giữ / offload Drive / purge / chưa rõ.
- Đích năng lực lab (ước, G0 kiểm): full clone ~4 GB dữ liệu × 2 (CURRENT/TARGET) + ~10 GB image + build cache ⇒ **≈30 GB đĩa trống + ≈5 GB RAM rảnh**. Thiếu RAM → tạm nâng gói VPS2 trong thời gian dự án (Bậc 1, vài USD) thay vì tối ưu thủ công. Container lab đặt trần CPU/RAM như lượt 09/09 để không đè e-learning (F5).

**3. PARITY CLONE tối thiểu mà thật — đổi mặc định sang FULL DATA**
- Mang đủ: 5 DB (3,4 GB) + uploads (8 KiB) + Qdrant (227 MB) + Nuxt output + extension/hook `l2-checkpoint-guard` + 128 Flow giữ nguyên trạng thái. Nhỏ nên subset không đáng công thiết kế manifest, lại dễ test giả. JEV 0,74.
- Chỉ dựng chuỗi phục vụ: **postgres · directus · nuxt · nginx · agent-data · qdrant**. Không dựng Hermes, claude-mcp/claude-kb, cowork-*, agent-api-executor, JEV, Kuma, cron backup (không nâng — chỉ test phía gọi ở §4-D).
- Cách ly phải **cưỡng chế** (A10 R2), không dựa lời nhắc: network Docker `internal: true` + firewall chặn egress container lab (chỉ mở registry và máy chủ license Directus); thay toàn bộ secret bằng secret lab (Directus KEY/SECRET, token mới); không mang `.env` prod nguyên xi. Flow schedule/webhook bị chặn bằng egress, không sửa từng Flow (giữ parity). Kích hoạt OIG ở lab tốn 1/5 lượt — dành: lab 1 · prod 1 · dự phòng.

**4. Ma trận chứng minh "VPS2 PASS ⇒ có cơ sở chuyển" — máy tự sinh, chạy y hệt trên CURRENT và TARGET rồi diff**
- A · Route: sinh từ nginx live — 4 host (vps.*, directus.*, ops.*, giaoduc.*), ≈105 `location` gồm 27 collection `/ops/items/*`, các nhóm `/api/*`, `/hooks/hermes/incomex-dispatch`, `/api/mcp-agent`, `/gpt-mcp/`, `/jev-mcp/`, `/ui-preview/` + monitor Kuma + trang Nuxt từ build manifest. Ghi status · redirect · cookie · 1 marker nội dung.
- B · Dữ liệu: đếm dòng + checksum từng bảng 5 DB trước/sau; diff `--schema-only` sau khi loại thay đổi migration Directus đã biết.
- C · Người dùng (Playwright): Directus admin login, Knowledge, Reports, Registries, GDĐH giaoduc + iframe e-learning, xưởng `/ui-preview/` — chụp ảnh so sánh.
- D · Phía gọi: mỗi consumer của Directus/PG (agent-data, `directus_*`/`query_pg` của gateway, DOT scripts, Điều 31 runner, backup cron, Kuma) 1 lệnh đọc + 1 lệnh ghi vào vùng test.
- PASS khi A–D không còn diff chưa disposition **và** G6 tập dượt bằng dữ liệu VPS1 mới lấy vẫn PASS. Bậc 1–2 (Playwright, Kuma, pg_dump có sẵn; script so mỏng).

**5. Cutover/rollback ít downtime + ít thao tác (Bậc 1–2)**
- Tại chỗ trên VPS1, cửa sổ đêm; người dùng chủ yếu là Owner + AI; tránh ngày kiểm tra GDĐH. Không blue-green (thêm bản sao DB + nginx phức tạp; cửa sổ ngắn đã chấp nhận được).
- Trình tự: ① tắt nguồn ghi (công tắc STOP Owner đã có ở HJW cho Hermes; cron; ghi qua gateway; cowork-runner) → ② Contabo snapshot qua API (GSM có `vps_contabo_id/secret` — G0 xác nhận là khoá API) + `pg_dumpall` + snapshot Qdrant → Drive qua `backup-to-gdrive.sh` sẵn có → ③ chạy công thức: image ghim digest, dump/restore sang PG18, Directus migrate, Nuxt/Node mới, Qdrant từng minor → ④ bộ test A–D → ⑤ mở ghi.
- Time-box = 1,5 × thời gian đo ở G6 (dự kiến ≤ 2 giờ). Quá → quay lui nhanh = compose cũ + restore dump vừa lấy (không có ghi mới trong cửa sổ ⇒ không mất dữ liệu). Quay lui cuối = Contabo snapshot (xoá snapshot mới hơn, đưa cả cấu hình VPS về cũ, tự xoá sau 30 ngày, gói chỉ 1–3 snapshot — G0 đo gói VPS1).
- Code freeze từ G6 đến cutover: cấm sửa lõi (compose, nginx, schema Directus) trên VPS1 trừ sự cố; thay đổi VPS1 sau lúc clone ghi vào 1 danh sách delta để công thức mang theo. Chốt cưỡng chế: Config Guard (`incomex-config-drift-check`) sẵn có, baseline = lúc clone.
- G0 kiểm thêm: backup Drive hiện có phủ đủ **5 DB** hay chỉ `directus`; đã có restore proof chưa.

**6. Ngoài core**
- **Bắt buộc nâng theo dependency:** Node của Nuxt; `@directus/sdk`; mọi extension Directus (hook `l2-checkpoint-guard` khai host ^11 → build lại bằng extensions-sdk 18 hoặc thay bằng policy native); client Qdrant của agent-data nếu nâng Qdrant.
- **Nên nâng, lớp riêng:** Qdrant 1.16.3 → 1.19.x từng minor (1.18.2 vá bypass xác thực REST). Không kịp thì tối thiểu ghim 1.16.3.
- **Giữ nguyên, chỉ ghim digest:** nginx, Kuma, Docker engine, Hermes, claude-mcp/claude-kb, cowork-*, JEV, agent-api-executor — chỉ chạy §4-D sau nâng. Agent Data chỉ rebuild nếu driver PG không hợp PG18 (kiểm ở G2).

**Đề nghị Host đưa lên `## Owner cần quyết` (Reviewer không tự ghi mục đó):**
- OQ-A · Incomex (gồm công ty liên quan) < 50 người và doanh thu < 5 triệu **USD**/năm → đăng ký key miễn phí OIG của Directus, chấp nhận gửi thống kê sử dụng. Đề xuất: **gật** (không key thì không lên 12; ở 11 là chạy bản đã lộ lỗ hổng).
- OQ-B · Cho một lượt nhỏ ghim digest các image đang chạy trên VPS1, không restart, không đổi phiên bản. Đề xuất: **gật**.
- OQ-C · Xác nhận "Agency OG" = Agency OS = khung web Nuxt hiện tại. Đề xuất: **gật**.
- Trạng thái: **OPEN** — chờ Host xử lý.

### P03 · GPT Host · PARTIAL — xử lý P02 theo chỉ đạo chiến lược Owner 26/09
- Based_on: P02 + nguồn chính thức Directus kiểm 26/09 + upstream Agency OS GitHub + nghiên cứu product-first Appsmith/ToolJet/Budibase + JEV Reference `gen-dec-1790409009-6nBmJnaxqIC1W6kcHLr7`.
- **ACCEPT:** P02 về ưu tiên security upgrade, pin digest, VPS2 storage audit/backup/restore, route/data/user/consumer test matrix, cutover time-box, F5 quan hệ `giaoduc`↔e-learning, và Agency OG đã được xác định bằng source là **Agency OS**.
- **SỬA F2 — quan trọng:** Core v12 đúng là có giới hạn **3 seats / 25 collections / 5 flows**, nên hệ hiện tại không thể chạy Core. Nhưng **OIG hiện không có các giới hạn này**: nếu đủ điều kiện (< USD 5M annual revenue và < 50 employees theo điều khoản hiện hành), OIG cho **unlimited seats / collections / flows + custom access policies**. Với doanh nghiệp thuộc nhóm cùng sở hữu, doanh thu được xét trên nhóm; số tài khoản Studio không thay thế điều kiện headcount. Ngày **10/09/2026**, Directus sửa OIG thành **perpetual, không hết hạn/không renew**; 5 activations/project. App/API users không đăng nhập Studio không tính vào Studio users. Vì vậy con số ~145 collections/128 flows **không phải blocker nếu OIG hợp lệ**.
- **Rủi ro Directus còn lại phải quản như dependency thật:** OIG bắt telemetry; không offline/air-gapped; không gồm product support. Sau activation, mất kết nối license server >7 ngày sẽ downgrade về Core; nếu vượt Core limits thì instance lock. Nếu sau này vượt ngưỡng eligibility phải làm việc với Directus trong 90 ngày. Do đó cần monitor license/telemetry, runbook mất license-server, lưu grant terms/key/evidence và một **exit path** có test.
- **Kết luận chiến lược Directus của Host — PROVISIONAL, chờ Claude vòng 2:** chưa có lý do đủ mạnh để bỏ Directus ngay. PostgreSQL vẫn là canonical durable truth; Directus được coi là **replaceable API/permission/Studio façade**, không được giữ business truth chỉ Directus mới đọc được. Chỉ production-adopt v12 sau khi OIG eligibility được attested + activation/telemetry/license-failure rehearsal PASS + export/restore/exit proof. JEV phụ: `retain_directus_v12_oig` p=0.99, confidence=0.98.
- **SỬA target Directus:** P02 tự mâu thuẫn khi đặt luật “GA ≥8 tuần” nhưng đề xuất 12.4.x mới ra 22–23/09. Host **không chấp nhận 12.4.1 làm production target lúc này**. 12.4.1 có thể probe ở lab; **12.3.1 là production candidate tạm thời** vì đã ra 25/08 và là security floor cho advisory 02/09. Exact target vẫn chốt lại tại G3 theo security + soak + compatibility, không khóa hôm nay.
- **PostgreSQL:** PG18.6 là candidate có cơ sở dài hạn, nhưng major 16→18 phải là gate độc lập; không trộn mọi major upgrade vào một lần nếu làm tăng rollback complexity. Rehearsal phải chứng minh dump/restore, extensions/opclass/index và app/driver compatibility.
- **Nuxt:** Nuxt4/Node24 vẫn là candidate hợp lý. Nhưng **Agency OS không được “nâng fork rồi nuôi tiếp” như chiến lược dài hạn**. Bản upstream `directus-labs/agency-os` hiện không archived nhưng commit cuối là 26/03/2025; đó là starter/template không còn đủ tiêu chuẩn làm nền Incomex.
- **Hướng UI mới — ASSEMBLY FIRST:** không thay Agency OS bằng template khác. Tạo một trial độc lập trên VPS2 cho **một lát cắt MMIM thật**: Appsmith CE là ứng viên trial đầu; ToolJet là đối chứng; Budibase giữ ứng viên phụ. UI trial mặc định đi qua **Directus REST/GraphQL/API** để giữ permission/audit; không cho low-code UI ghi thẳng PG production theo mặc định. Custom Nuxt/Nuxt UI chỉ giữ cho màn hình public/đặc thù mà low-code không đáp ứng.
- **Tiêu chí trial UI:** upstream activity/ownership; license/self-host; backup/export/versioning; auth/RBAC/audit; Directus/API fit; Agent/MCP automation; responsive UX; runtime footprint; restore/upgrade; khả năng rời sản phẩm mà không mất data/business definition; công sức người/AI để làm cùng một MOIT/MOT slice.
- **Không migration UI ngay:** core security/platform upgrade và Agency OS exit là hai trục có checkpoint riêng. Trong giai đoạn chuyển tiếp giữ màn hình hiện tại hoạt động; chỉ chuyển module sau khi replacement trial PASS.
- **Owner chưa cấp mutation:** đề xuất P02 “ghim digest ngay trên VPS1” là hợp lý nhưng vẫn là production mutation; **chưa RUN**. Việc này sẽ nằm trong prompt riêng sau khi hội đồng chốt read-only inventory và Owner/Host phát RUN theo luật.
- Trạng thái P02: **PARTIAL** — phần migration/test/cutover được nhận; F2/license lifetime và target 12.4 được sửa; Agency OS target bị thay bằng EXIT strategy.

### Yêu cầu Claude Reviewer vòng 2
Phản biện đúng P03, không mở thêm file:
1. Xác minh lại Directus OIG hiện hành: perpetual/unlimited, telemetry, 7-day license-server behavior và ngưỡng group/Studio user.
2. Phản biện mô hình **PG canonical + Directus replaceable façade + exit proof** có đủ giảm vendor risk dài hạn không.
3. So lại **12.3.1 vs 12.4.1** theo security/soak/breaking changes, không dùng “latest” làm lý do.
4. Phản biện Agency OS EXIT và trial **Appsmith CE vs ToolJet** (Budibase phụ): có sản phẩm nào phù hợp Incomex hơn theo tiêu chí Owner không.
5. Chỉ sau đồng thuận mới soạn khảo sát read-only và trial plan; chưa mutation VPS.

### P04 · Claude Chat (Reviewer, vòng 2) · PARTIAL — Host xử lý tại P05; phần còn mở chuyển thành bài kiểm
- Based_on: `68ac2f3` (COLLAB `aa43dcb5`). Scope: P03, D07–D09, Q04. Nguồn kiểm 26/09: directus.com/resources/making-the-oig-perpetual-and-clearer (10/09/2026) · directus.com/oig/faq · directus.com/pricing · npm `directus` (trường `time`) · github.com/directus/directus/security/advisories. JEV `gen-dec-1790409992-Vm1bXb4JcrTXQn0dzGC7`.
- Chưa kiểm: "advisory 02/09" và "lỗi registration vá ở 12.3.1" P03 nêu — trang advisories GitHub không có mục nào tháng 9/2026; Host cho link nếu có.

**1. OIG — Host đúng, P02 F2 sai ở 2 điểm.** Trang docs `licensing/open-innovation-grant` vẫn ghi "valid for one year" nhưng bài 10/09/2026 và FAQ ghi: *"granted in perpetuity … no expiration date … previously granted keys have already had their expiration removed"*; unlimited seats/collections/flows + custom access policies; người dùng app/API không tính Studio user; nhóm công ty cùng chủ sở hữu tính gộp. Rút F2 phần "1 năm" và "25 collections là blocker". **Còn lại đúng và phải quản:** telemetry bắt buộc (*"For the Core and OIG licenses, anonymous product usage telemetry is required"*); *"can't reach the license server for more than 7 days → downgrades to Core"* → với ~145 collections = khoá `/items`. ⇒ Thêm chốt: (a) monitor Kuma cho trạng thái license + egress tới license server, cảnh báo Telegram ở ngày 3; (b) firewall egress VPS1 phải mở đích license/telemetry của Directus (chưa biết tên miền — đo ở G2 bằng lab); (c) 5 activation gắn `PUBLIC_URL`+DB: lab dùng URL riêng (1), prod (1); tập dượt restore DB prod vào lab phải thử xem có tốn activation không (G2).

**2. "PG là sự thật, Directus là lớp thay được" — đúng làm đích, chưa đúng hôm nay.** Hiện logic nghiệp vụ nằm ở 8 nơi (register MMIM §8): 128 Flow, policy/permission, `directus_*` metadata, revisions, hook, Nuxt. JEV: mệnh đề đúng-hôm-nay 0,22. Đề nghị cụ thể hoá D09 thành 2 dòng đo được, không dựng thêm gì: (i) **exit proof = pg_dump restore vào PG sạch + 5 truy vấn nghiệp vụ trả đúng không cần Directus** (đã có dữ liệu, chỉ chạy); (ii) **danh sách logic chỉ Directus mới hiểu** = register 8 nơi có sẵn, mỗi dòng ghi đường ra (Flow → PG function/DOT; policy → RLS/DOT). Không xây lớp API thứ hai.

**3. 12.3.1 vs 12.4.x — ACCEPT 12.3.1 làm sàn, thêm một điều kiện.** (P02 không đề xuất 12.4.1 hôm nay mà "patch mới nhất tại G3 theo luật ≥8 tuần"; Host đọc lệch, không sao.) Mốc npm: 12.3.0 18/08 · 12.3.1 25/08 · 12.4.0 22/09 · 12.4.1 23/09. Quan sát: dòng 11 không nhận bản vá nào sau khi 12.0 ra (advisory 24/06, 05/08 chỉ vá ở 12.x) ⇒ Directus chỉ vá dòng mới nhất. **Luật đề nghị:** 12.3.1 = sàn; tại G3 lấy 12.4.x nếu GA ≥8 tuần và ≥1 patch; **nếu có advisory sau 25/08 chỉ vá ở 12.4+ thì 12.4.x bắt buộc**, bỏ điều kiện ngấm. Kiểm lại lần cuối tại G7. JEV 1,00.

**4. Agency OS EXIT — ACCEPT D07/D08. Trial low-code — REJECT đặt trong việc này; đề nghị tách.**
- Lý do: (a) việc này giờ là **nâng cấp vì an toàn** (Directus 11 hết vá, Node 20/Nuxt 3 EOL); gắn thêm chọn sản phẩm UI 2–3 ứng viên là mở việc bước sau khi bước này chưa xong — trái luật Owner "đi từng bước". (b) Bản fork Nuxt vẫn **bắt buộc nâng** trong việc này: giaoduc.* (cổng kiểm tra), knowledge, reports, registries, ui-preview đang chạy trên nó và phải chạy sau cutover; JEV 0,86. "Exit dần" diễn ra sau, từng module. (c) Quyết định nền UI thuộc hội đồng `quy-trinh-ve-UI` / `mow-mot-moit-mout` (đang thiết kế quy trình vẽ UI, FIELD, master list); để 2 việc cùng quyết UI là 2 nguồn sự thật. (d) VPS2 RAM đang chia với e-learning; Appsmith/Budibase kéo thêm engine riêng (Mongo/Redis; CouchDB/MinIO/Redis) tranh tài nguyên đúng lúc tập dượt. JEV: tách việc riêng 1,00.
- Đề nghị: D07/D08 giữ nguyên làm nguyên tắc; mở việc riêng (tên do Host/Owner đặt, vd `work/ui-platform-trial`) Host GPT, chạy trên lab VPS2 **sau G2** dùng chính clone CURRENT, **không bao giờ gate G7**. Hai tiêu chí phải thêm vào trial đó: **số engine DB mới phải cài trên VPS** (Điều 33: PG là DB duy nhất; JEV 0,82) và **giới hạn gói free self-host** (ToolJet: builder/end user/app/workflow) — hai điều này quyết định trước cả tính năng. Mọi UI trial ghi qua đúng một đường ghi (DOT/Directus), không thêm writer.

**5. PG 16→18 gate riêng — ACCEPT.** Cutover một cửa sổ nhưng có checkpoint sau bước PG; lab PG18 FAIL thì cutover chỉ 16.15 + app, PG18 làm lượt sau.

**Đề nghị Host đưa lên `## Owner cần quyết`:**
- OQ-A (rút gọn) · Xác nhận Incomex + công ty cùng chủ sở hữu: < 50 người, doanh thu < 5 triệu USD/năm → đăng ký OIG (vô thời hạn, có telemetry). Đề xuất: **gật**.
- OQ-D · Tách trial low-code thành việc riêng, không gate cutover. Đề xuất: **gật**.
- Trạng thái: **OPEN** — chờ Host. Sau đồng thuận: soạn **một** prompt khảo sát chỉ đọc VPS1 + VPS2 + Drive (G0), cấm lệnh hành động.

### P05 · GPT Host · PARTIAL — lịch sử; SaaS/LC6/EDU đã được P07 thay theo mô hình Owner chốt
- Based_on: P04 `f5d53eb`, snapshot workspace `7826adb28e379491b9aca2a4953c6b4e9f5e7132`; nguồn S01–S07 trong view.html §2A, kiểm ngày 26/09. Scope: §0.3, D10–D13, view.html §2A/§5–§10. Chưa kiểm live VPS2, key thực, cache/refresh/restart trên instance target, DR thật hay báo giá offline.
- **Xử lý P04:** ACCEPT tách low-code, giữ tương thích các trang Nuxt, PG major riêng, dữ liệu PG không đồng nghĩa app thay được. PARTIAL cảnh báo ngày 3: cảnh báo phải sớm, tự xử lý có biên và giám sát độc lập; ngày 3 chỉ là mốc escalation, không lần phát hiện đầu. Không còn bất đồng scope UI phải hỏi Owner.
- **SaaS:** FAQ và Terms phân biệt sản phẩm của Incomex với giao Directus/Studio cho khách. Ngưỡng áp cho tổ chức dùng Studio; khách chỉ dùng MOT/API không cộng thành nhân sự hay doanh thu của Incomex. Thu phí dịch vụ là doanh thu của Incomex; doanh thu nhóm cùng kiểm soát phải xét hợp nhất. Account có policy App Access/Admin Access vẫn tính Studio seat dù không đăng nhập. Không dùng một shared admin cho mọi khách; giữ identity/tenant/permission/audit đúng người. Điều khoản 2.6 về resale/sublicense/competitive service cần Directus xác nhận bằng văn bản cho mô hình “nhà máy quy trình” tổng quát trước bán rộng; không suy mọi hình thức white-label/giao instance cho khách đều được.
- **EDU / Trường nghề Lai Châu:** chính sách công khai hiện hành không có một tier “education” tự động tốt hơn OIG. OIG FAQ ghi rõ **students at a school do not count as employees**; người dùng app/MOT không tính eligibility/seat. Nếu chỉ Incomex đăng nhập Studio thì FAQ đo eligibility theo Incomex, kể cả client lớn; nếu người của trường cũng đăng nhập Studio thì trường phải tự đạt ngưỡng <USD5M/<50 employees. Nếu trường là non-profit dưới ngưỡng thì OIG áp bình thường; nếu vượt ngưỡng phải làm việc với Sales. FAQ hiện loại **government customer** khỏi OIG. Founder từng công khai nói Directus vẫn hỗ trợ discount cho educational institutions lớn, nhưng current Pricing/OIG không công bố mức/tier tự động — chỉ coi đó là căn cứ để hỏi Sales, không phải quyền đã có. Với mô hình “giao trường làm chủ sở hữu hệ thống nhưng Incomex duy nhất vận hành Studio”, cần Directus xác nhận bằng văn bản project/license owner + data/infrastructure ownership + operator relationship trước mẫu hợp đồng đầu tiên.
- **Vô thời hạn khác offline:** OIG lifetime không loại license-server dependency. Telemetry mỗi 6 giờ, còn kiểm license theo `validation_interval` trong exact license; source v12.3.1 api/src/schedules/license.ts xác nhận cơ chế đó. Không gọi là “tuần mới liên lạc một lần”. FAQ ghi quá 7 ngày mất liên lạc sau activation thì Core/lock; ngày giờ và hành vi restart/khôi phục cần test, không suy từ health200.
- **Phương án B không dùng tổ chức giả/dự phòng danh nghĩa:** dự án độc lập có thể xin key riêng cùng tổ chức; staging/DR dự án này dùng activation đúng điều khoản. Key mới vẫn cần license service, nên không giải quyết outage chung. Không chuyển grant sang pháp nhân khác khi chưa có quyền tương ứng. Chưa tạo account/key, chưa gửi hồ sơ ra ngoài.
- **Bậc 1–2, đề xuất cần kiểm:** giám sát last successful validation/entitlement expiry + trạng thái API nghiệp vụ; kiểm licensing và telemetry riêng; retry có backoff, đường HTTPS dự phòng hợp lệ giữ TLS/telemetry nếu đường hiện tại lỗi; không restart Directus mù. Dự kiến warning sau 12 giờ không validation thành công (chỉnh theo interval thật), escalations 24/48 giờ. Monitor/recovery không được phụ thuộc cổng Directus đang có nguy cơ khoá; một kênh ngoài VPS1 và cách xử lý khi Owner không xác nhận là bài kiểm bắt buộc. Không tự cấp quyền sửa rộng cho AI.
- **Outage licensing toàn nhà cung cấp >7 ngày:** hai VPS, hai key và backup GGD không tạo offline entitlement. Phải xác minh lựa chọn offline/emergency-token cấp hợp pháp, thời hạn/giá/renewal và điều kiện bật đã chuẩn bị trước. Docs công khai chỉ cấp offline cho Enterprise. Nếu không có phương án phù hợp, ghi residual risk và chưa nghiệm thu v12 đáp ứng “Owner vắng mặt, vẫn chạy”; đánh giá backend thay thế bằng sản phẩm có sẵn là contingency chiến lược, KHÔNG mở lại trial UI.
- **Exit proof hai cấp:** dump + 5 query chỉ DATA PORTABILITY. BUSINESS CONTINUITY phải chứng minh đúng quyền/tenant, CRUD, Flow/worker, audit, file và một MOT thiết yếu khi đổi tầng thực thi. Chưa có sản phẩm thay thế/test nên không tuyên bố “chỉ đổi Directus là chạy”. Không mặc định chuyển 128 Flow/policy sang code PG/DOT; không bypass quyền bằng direct PG khi sự cố. Backup chống mất dữ liệu, không tự cấp quyền chạy phần mềm.
- **Sửa nguồn an ninh P04:** đã thấy GHSA-8xp8-xrh2-88vr (02/09, patched12.3.1; điều kiện MySQL/MariaDB collation, không áp mặc định PG) và GHSA-7h45-q5jx-7r87 (02/09, patched12.3.1; phải kiểm permission thực). Link S06–S07. Không biến sự tồn tại advisory thành khẳng định VPS đã bị khai thác; không chốt cả bản an toàn chỉ bằng hai advisory.
- **G0 có thể chuẩn bị song song với licensing gate:** đúng một phạm vi chỉ đọc, bằng chứng gộp vào view.html/COLLAB hiện hữu; không cần chờ vendor để kiểm disk/routes/backup. Claude đối chiếu ba nhóm ở §9 rồi Host phát một PROMPT khi đủ đầu vào; hiện chưa PROMPT/READY/RUN, không thử mất mạng/restart/restore trên production.
- Áp: SAME_COMMIT. P04 đã xử lý; P05 còn OPEN cho bằng chứng pháp lý/kỹ thuật mới, không lặp hội đồng vô hạn.

### P06 · Claude Chat (Reviewer) · ACCEPTED — Host nhận hướng chính; điều hành chính xác theo P07 và view.html
- Based_on: `183041c` (COLLAB `f0af414a`, view `c41ef3a6`). Scope: P05, D10–D13, view.html §2A/§5/§6 LC/§8/§9. Đo live 26/09 (chỉ đọc, `query_pg` db directus): 14 user · 6 active · **1 tài khoản có quyền Studio** (admin, không static token) · 5 tài khoản máy có static token, không quyền Studio · 167 collection ngoài `directus_*` · 111/128 Flow active · 1 extension. JEV `gen-dec-1790413813-C3TP0QYOikggCbQVS5fu`.
- **ACCEPT P05** trừ một điểm (mục D). Xử lý Owner chốt 26/09 16:07 qua Claude Chat — nguyên văn, đề nghị Host ghi D14–D16:
  - D14 · “Chỉ 1 CSDL. chúng ta chỉ thêm nhãn, thêm table/collection. Không thêm hệ thống quản trị riêng. Chúng ta sẽ thiết kế như vậy, kể cả cho nhiều công ty.”
  - D15 · “chỉ có tài khoản duy nhất của tôi được vào Directus (để cho phép DOT qua tài khoản của tôi). Tôi cũng không vào trong Directus … yêu cầu 100% dùng DOT, thiếu DOT viết thêm. Vừa để tự động, làm nhanh và chính xác. Vừa đỡ phức tạp.”
  - D16 · “Cảnh báo ngay qua telegram nếu liên lạc bị lỗi, sau này cần làm cảnh báo qua email nữa nếu lỗi (đề phòng cả telegram hỏng).”
  - Owner yêu cầu: chốt mô hình · nâng gì · vision · kế hoạch 1,2,3 thứ tự trước/sau; GPT + Claude thống nhất hết trước khi triển khai.

**A. Mô hình dài hạn — 7 luật (V1–V7)**
- V1 · **Một hệ PostgreSQL.** Công ty/khách/trường = một **nhãn công ty** trên bảng nghiệp vụ + một bảng danh mục công ty; không DB/engine/hệ quản trị riêng theo khách. Tách dữ liệu giữa công ty cưỡng chế ở PG (khoá công ty bắt buộc + RLS/constraint), policy Directus là lớp hai. Cụm hiện có 5 database: giữ nguyên trong việc này; bảng nghiệp vụ mới vào database Directus phục vụ. Thiết kế nhãn thuộc MMIM, không làm trong đợt nâng.
- V2 · **Ghi 100% qua DOT**; thiếu DOT → viết DOT; không người/AI nào ghi tay.
- V3 · **Studio đúng 1 tài khoản = Owner.** Đo 26/09: **đã đúng sẵn**. Cách hiểu D15 đề nghị: DOT chạy bằng token máy do Owner cấp, không dùng mật khẩu Owner — lộ một token thì thu token đó, không khoá Owner; tài khoản máy chỉ-API không tính ghế Studio. Cưỡng chế (R2): kiểm hằng ngày “số tài khoản có quyền Studio = 1”, lệch → Telegram. JEV: token máy 1,00; vẫn giữ ý Owner 0,90.
- V4 · **Khách/trường chỉ dùng MOT, không bao giờ vào Studio** ⇒ OIG xét theo nhóm Incomex (pháp nhân cùng chủ sở hữu tính gộp: cán bộ trường nghề tính, học sinh không tính). Theo V1, trường Lai Châu = một nhãn công ty trong hệ Incomex, sở hữu dữ liệu của mình bằng hợp đồng + xuất dữ liệu theo nhãn ⇒ **không cần instance riêng**, bỏ được câu hỏi “khách sở hữu project” ở P05. Còn đúng một câu hỏi hãng: bán ứng dụng quy trình trên Directus có nằm trong Terms §2.6.
- V5 · **Giao diện:** nâng tương thích fork Nuxt bây giờ; thoát Agency OS dần, việc riêng, không gate cutover (đã đồng thuận P04/P05/D11).
- V6 · **AI** (Hermes, agent, JEV) chỉ đi qua DOT/MCP; không phụ thuộc Studio.
- V7 · **Hạ tầng:** VPS1 = production · VPS2 = lab + e-learning + **trạm canh VPS1** · Drive = bản ngoài · mọi image ghim digest.

**B. Nâng gì / giữ gì — bảng chốt (exact digest chốt tại G3, kiểm lại tại G7)**

| Thành phần | Hiện | Đích | Ghi chú |
|---|---|---|---|
| PostgreSQL | 16.13 | 18.x mới nhất tại G3 | Checkpoint riêng; lab FAIL → 16.15 + app, PG18 lượt sau (D13). |
| Directus | 11.5.1 | sàn 12.3.1 · 12.4.x theo luật P04 | Advisory chỉ vá ở dòng mới hơn → bắt buộc lên, không chờ ngấm (khớp D13). |
| Nuxt / Node / SDK | 3.20.2 / 20.20 / ^19.1 | 4.5.x / 24 LTS / major khớp Directus | `@nuxt/ui` giữ 2.22.3. |
| Extension `l2-checkpoint-guard` | host ^11 | build lại cho 12 hoặc thay policy native | Lớp Directus. |
| Qdrant | 1.16.3 (`latest`) | ghim ngay; 1.19.x từng minor | Cửa sổ nhỏ riêng **sau** cutover. |
| nginx, Docker, Kuma, Hermes, MCP, JEV, agent-api-executor, agent-data | giữ | ghim digest | agent-data chỉ rebuild nếu driver không hợp PG18. |

**C. Giám sát liên lạc Directus (D16) — Bậc 1: Uptime Kuma sẵn có**
- 3 đồng hồ, chạy ngoài Directus: (1) đường ra tới máy chủ license Directus mỗi 5 phút, đo từ đúng mạng container Directus; (2) lần xác minh license thành công gần nhất — vị trí đọc đo ở lab; (3) `/server/ping` + một lệnh đọc `/items` bằng token máy.
- Báo: lỗi 2 lần liên tiếp (~10 phút) → **Telegram ngay** (lọc 1 lần chập chờn). Còn lỗi 24 giờ → nhắc lại + Hermes chạy runbook đã duyệt (mạng/DNS/tường lửa phía Incomex). 72 giờ → báo khẩn “còn 4 ngày trước khoá”. Mốc ngày 3 của P04 thay bằng mốc này.
- **Canh chéo 2 VPS:** thêm một Kuma trên VPS2 canh VPS1; VPS1 chết hẳn vẫn có báo.
- **Email = pha sau:** Kuma có SMTP sẵn; cần một hộp gửi (Owner tạo 1 lần theo hướng dẫn từng bước, khoá lưu GSM), rồi mọi đồng hồ báo cả Telegram lẫn email.

**D. Điểm còn vênh với Host — LC6 / G7**
- ACCEPT LC1–LC5 là bài kiểm bắt buộc.
- Không đồng ý câu “outage dài chưa giải thì chưa PASS” nếu nó chặn cutover. Đề nghị G7 qua khi đủ 4 điều: LC1–LC5 đạt; đo xong **vùng ảnh hưởng khi bị khoá** (đọc mã nguồn 12.x + thử lab phần thử được, không sửa đồng hồ); rủi ro còn lại (hãng mất dịch vụ > 7 ngày) ghi rõ và Owner chấp nhận; song song hỏi hãng offline/emergency + giá.
- Lý do: ở lại 11.5.1 là rủi ro **chắc chắn và đang có** — lỗ hổng Critical/High đã công bố, không còn vá. Hãng sập > 7 ngày là rủi ro hiếm và có 7 ngày để xử lý. OIG không có offline, nên chặn cứng nghĩa là không bao giờ lên được 12. JEV: cho qua có đo 0,86 · chặn 0,14.
- Giảm vùng ảnh hưởng (hướng dài hạn, không làm trong việc này): đường ghi DOT PG-native (`dot-pg-atomic-apply`) vẫn ghi được khi Directus khoá; danh sách trang chết khi khoá = đầu vào cho việc thoát Agency OS.
- Nếu Host vẫn giữ chặn cứng: chuyển D này lên `Owner cần quyết` theo A5, phần còn lại chạy tiếp.

**E. Kế hoạch 10 bước — đúng một bước đang làm (🤖 máy · 😊 Owner)**

| # | Việc | Ai | Ra được gì |
|---|---|---|---|
| 1 | Chốt kế hoạch: Host hợp nhất P06 vào view.html; Owner gật một lần | 😊🤖 | Kế hoạch đã duyệt |
| 2 | G0 khảo sát **chỉ đọc**, một PROMPT, cấm lệnh hành động: VPS1 · VPS2 · Drive · user/policy/token Directus · backup phủ mấy DB + restore proof · route từ nginx live · gói Contabo (số snapshot, khoá API) · WebSocket v11 có lộ không | 🤖 | Sổ giữ/offload/purge VPS2 · danh sách caller · route list |
| 3 | Một thư gửi Directus: đăng ký OIG + xác nhận mô hình bán ứng dụng + offline/emergency và giá + tên miền license để mở tường lửa. AI soạn sẵn, Owner gửi | 😊 | Key OIG (chờ trả lời, cần trước bước 7) |
| 4 | Khoá nhãn + canh gác VPS1 (mutation nhỏ, Owner RUN): ghim digest không restart · Kuma canh chéo VPS1↔VPS2 + Telegram · kiểm “Studio = 1” · nếu G0 thấy WebSocket v11 lộ thì chặn tạm ở nginx | 🤖 | VPS1 hết trôi nhãn, có báo động |
| 5 | VPS2 sẵn sàng: backup e-learning → Drive + thử khôi phục · dọn theo sổ · đủ ≈30 GB đĩa / 5 GB RAM (thiếu → tạm nâng gói) | 🤖 | G1 |
| 6 | Clone CURRENT full data, cách ly cưỡng chế · chạy bộ test A–D lấy mốc | 🤖 | G2 |
| 7 | Nâng từng lớp trên lab: PG → Directus (key lab) → Nuxt/Node/SDK/extension; mỗi lớp chạy lại A–D · LC1–LC5 · đo vùng khoá · gắn đồng hồ license | 🤖 | G3–G4 |
| 8 | Tập quay lui + tập chuyển nhà bằng bản VPS1 mới lấy, đo giờ. Từ đây khoá sửa lõi VPS1 (Config Guard) | 🤖 | G5–G6 |
| 9 | Chuyển VPS1 thật: Owner chọn đêm + RUN; quá giờ tự quay lui | 😊🤖 | G7 |
| 10 | Theo dõi 7 ngày → đóng · rồi Qdrant từng minor · email cảnh báo · diễn tập “thoát Directus” mỗi năm | 🤖 | Đóng việc |

- Tách ra sau, không gate: thoát Agency OS / chọn nền UI; thiết kế nhãn công ty V1 (MMIM).
- Đề cương G0 (view.html §9): ACCEPT G0-A/B/C, cộng 4 mục trong bảng bước 2.

**Đề nghị Host đưa lên `## Owner cần quyết` sau khi hoà giải:**
- OQ-A · Tổng nhân sự nhóm Incomex (gồm trường nghề nếu cùng chủ sở hữu; học sinh không tính) < 50 → đăng ký OIG. Doanh thu đã xác nhận, không hỏi lại. Đề xuất: **gật**; khi trường tuyển cán bộ thì đếm lại.
- OQ-E · Chỉ nếu còn vênh mục D: luật G7 “đo + chấp nhận rủi ro còn lại” thay cho “chặn tới khi có offline”. Đề xuất: **gật**.
- **Host xử lý tại P07:** OQ-A không hỏi lại theo xác nhận Owner; OQ-E đã hòa giải bằng D17, không còn chờ quyết định mô hình. Phần trên giữ nguyên làm lịch sử đề nghị P06.

### P07 · GPT Host · ACCEPTED — hòa giải P06, chuyển sang soạn lệnh G0
- Based_on: P06 `2a28f81a93ae53dfe26578b8fd637eee7bce0dca`; rebase `7ac3a934173cf24aa450f0b413712a14ec4a8a06` đã diff task = rỗng. Scope: §0.3, D14–D18, view.html §2A/§5–§10. Nguồn S01–S03/S10–S12 kiểm 26/09. Chưa đo live VPS trong lượt này; số 1 Studio/5 account máy/167 collections là báo cáo Claude P06, không phải GPT đo lại.
- **Nhận P06:** SaaS chung, DOT/MCP, một Owner + khóa máy phân quyền, nâng shell hiện tại, PG major riêng, pin image, canh chéo VPS và Drive; tách UI. G7 theo D17 thay chặn offline; không còn bất đồng mô hình phải hỏi Owner ngay. Rủi ro thực đưa một lần cùng RUN cuối, không tự ghi Owner đã nhận trước.
- **Tài khoản/quyền:** thay mặt Owner không là chia admin credential cho tất cả giao dịch. Service identity API-only không App/Admin Access, ít quyền, thu hồi riêng, có actor/tenant/DOT/operation_id. DOT đặc quyền tách allowlist/trace; cấm tự tạo admin hoặc mở policy. Native trước, wrapper cần thiết sau; không framework phân quyền riêng.
- **Tenant:** server xác minh tenant AND phạm vi được cấp; cùng tenant không mặc nhiên đọc nhau. Directus policy cộng OR/admin không bị item policy giới hạn; PG superuser/BYPASSRLS và thường table owner bỏ qua RLS. G0 phải kiểm effective role/context/reset connection pool, không mặc định Directus tự truyền user xuống RLS. Chưa chứng minh thì ghi gap; không biến việc nâng VPS thành triển khai schema SaaS toàn hệ. Không mặc định tạo table cho từng khách.
- **Bước 3:** OIG đăng ký chuẩn, không thư xin duyệt SaaS hoặc chờ offline. FAQ có commercial SaaS/API-only rõ. Vẫn cần người có thẩm quyền chấp nhận terms, key, telemetry/contact; chỉ hỏi hãng khi key/activation lỗi hay đổi phạm vi thực. Không che số user, đổi pháp nhân, giả token hoặc sửa clock để né giấy phép. Không đăng ký/gửi mail trong lượt này.
- **Monitor:** ba tín hiệu: kết nối licensing từ mạng Directus; last validation/cache expiry; ping + đọc nghiệp vụ có quyền. Probe không POST refresh/activation mỗi 5 phút. Hai lần lỗi liên tiếp ~10 phút báo Telegram. Recovery an toàn có biên khi đã chẩn đoán, 24/72h là escalation không trì hoãn sửa; thời gian còn lại theo entitlement thật, không hứa cứng “còn 4 ngày”. VPS2 canh VPS1 không khắc phục outage licensing chung. Hermes chỉ chạy bước thực sự có quyền; không tự nâng profile thành shell/root. Monitor có heartbeat và độc lập Directus; mailbox liên hệ key vẫn phải nhận thông báo, kênh email-monitor làm sau được.
- **LC6/rollback:** đánh giá đạt khi có bảng endpoint/chức năng bị ảnh hưởng, source/lab + phần chưa thử + residual risk + incident runbook. Không gán UNKNOWN=PASS, không gọi là đã có offline/backend dự phòng. Không dựa PG-native DOT chưa kiểm để hứa giữ MOT; không tự dựng đường ghi tắt hoặc rollback về v11/snapshot cũ để né license. Đã mở ghi mới thì phải bảo toàn/reconcile.
- **Version:** dãy 18/12.3+/4.x/24 là candidate P06; patch/digest kiểm official/security/compatibility G0/G3/G7. Không suy SDK major bằng major server. Qdrant hoãn cửa nâng riêng chỉ khi security/exposure được giảm thiểu; ghim digest không là vá lỗi. Docker engine pin package version, không phải image digest.
- **Giao Claude:** soạn đúng một nội dung lệnh G0 tại `view.html` §9 hiện hữu; được sửa riêng §9 và ghi trace trong COLLAB, không tạo task/file/PROMPT mới trong lượt soạn. Chỉ rõ Executor_Surface Claude Code CLI, Write_Path gateway đã bind, đúng hai host từ cấu hình đã có, runtime VPS là nguồn chuẩn, đầu ra mục G0 hiện hữu. Cấm mutation/restore/dump dữ liệu nhạy cảm/secret/fault injection/POST nghiệp vụ. Host kiểm lệnh trước RUN; không mở lại OIG/mô hình. G0 chỉ khảo sát, chưa cài chốt.
- JEV bổ trợ đổi gate: `gen-dec-1790415416-3Nnbp9l9QnOtwQFcEnci` → conditional_release p0.97/confidence0.95, không xác suất outage hay xác nhận luật/test. Áp: SAME_COMMIT. Hướng chính P06 đã hòa giải; chốt P07 là điều hành Host, không claim Claude đã review lệnh G0.

### P08 · Claude Chat (Reviewer) · ACCEPTED — đồng thuận P07 + Host dùng làm nền cho PROMPT G0
- Based_on: `abbabda` (COLLAB `2aa9f28d`, view `5d1de710`). Scope: P07, D14–D18, view.html §9 (chỉ sửa §9 theo giao P07).
- **ACCEPT P07 và D14–D18, không còn bất đồng.** Owner 26/09 17:05 nhắc lại qua Claude Chat: “Chốt luôn là 1 Saas, đảm bảo 1 người quản trị, hạn chế phụ thuộc vào các cơ chế duyệt tay … thiết kế hệ thống theo đúng các điều kiện quy định” — khớp D14–D16, không phát sinh D mới.
- **Đã soạn lệnh G0** trong `<details>` của §9 (RUN_ID `VPSUP-G0-20260926-01`, Executor Claude Code CLI, Write_Path `workspace_*` → dự phòng `fs_*`, read-gate một lần, VPS1 = alias `contabo`, VPS2 = alias tra theo IP của `elearning.*` hoặc khoá GSM qua ssh-agent). 10 mục đo A–J; chỗ ghi duy nhất trên VPS = hồ sơ A8 `/opt/incomex/work/vps1-up-grade/G0-20260926/`; kết quả vào đúng `div#g0-result` + một dòng KQ. Host chuyển nguyên văn vào `PROMPT.md` khi đặt READY (A6); đến lúc đó không có file mới nào.
- **F6 🟡 (đo 26/09, chỉ đọc):** `scripts/pg-backup.sh` (DB_NAME=directus) và `scripts/backup-to-gdrive.sh` (`pg_dump -d directus`) chỉ sao lưu DB `directus`. Cụm 5 DB: directus 1,77 GB · directus_gov_test_20260602 1,20 GB · incomex_metadata 419 MB · workflow 7,6 MB · postgres 7,5 MB ⇒ `incomex_metadata` + `workflow` chưa thấy trong backup nào. G0-D xác nhận; nếu đúng, vá backup thuộc bước 4 (trước mọi clone/cutover). Sửa số P02: “3,4 GB/5 DB” gồm 1,2 GB DB thử; dữ liệu thật ≈ 2,2 GB.
- G0 thêm mục J (đọc mã nguồn license 12.x) để có tên miền mở tường lửa + chỗ đọc “lần xác minh gần nhất” cho đồng hồ D16 + bảng endpoint bị khoá cho LC6 — không cần chờ hãng.
- Trạng thái: **OPEN** — chờ Host kiểm lệnh, tạo PROMPT.md + READY; Owner RUN.

### P09 · GPT Host · ACCEPTED — kiểm lệnh G0, tạo PROMPT và đặt READY
- Based_on: P08 + view.html §9 + AGENTS A4/A6/A10; task không đổi qua commit chen ngang trước lúc tạo prompt.
- Đồng thuận toàn bộ mục tiêu/phạm vi A–J. Chỉnh kỹ thuật trước READY: **một Write_Path duy nhất = fs_* / root gh**; **không ghi bất kỳ file/evidence nào lên VPS1/VPS2** trong G0.
- F6 backup là hypothesis cần xác nhận. G0 phân loại DB BUSINESS/CONFIG/TEST-DERIVED/DEFAULT/UNKNOWN rồi mới kết luận thiếu backup; không đòi backup mọi DB chỉ vì tồn tại.
- Kuma/live DB chỉ đọc trực tiếp bằng chế độ read-only an toàn; nếu muốn đo buộc phải copy file thì ghi UNKNOWN.
- Prompt chuẩn: `work/vps1-up-grade/PROMPT.md`, RUN_ID `VPSUP-G0-20260927-01`, commit cuối chạm prompt `79ed9b9a3655662ec6cd84d2e9b892ce6789898b`.
- **READY@79ed9b9a3655662ec6cd84d2e9b892ce6789898b**. READY không phải RUN.
- Sau RUN, Claude Code chỉ được khảo sát runtime read-only; mutation duy nhất là report cuối vào `view.html` + `COLLAB.md` qua `fs_transaction`.
- Trạng thái: **ACCEPTED/READY**; không còn P OPEN/OWNER chặn G0.

### P10 · Claude Chat (Reviewer) · ACCEPTED — đồng thuận PROMPT G0
- Based_on: `92c48ae`; PROMPT `1a98afea` (commit cuối chạm = `79ed9b9` = READY, RUN_ID khớp). ACCEPT hai chỉnh của Host: Write_Path cố định `fs_*` (không bind ⇒ DỪNG ở read-gate, an toàn) và G0 read-only tuyệt đối, không evidence trên VPS. F6 để G0 xác minh, không mặc định mọi DB phải backup — đồng ý.
- Lưu ý nghiệm thu, không sửa PROMPT: Contabo API cần POST lấy OAuth token trước mọi GET, nên với luật "chỉ GET" mục H nhiều khả năng ⚪ — chấp nhận, không phải blocker; gói/snapshot lấy ở bước 4.

### P11 · GPT Host · ACCEPTED/READY — nghiệm thu G0 và chọn SEC1 trước backup
- Based_on: KQ G0 commit `4a80ec47bc6a87627b9d42b90bb0764c01b305ae`; task diff từ G0 tới lúc review = không đổi; view.html §9 A–J; MySQL official xác nhận 5.7.44 là release cuối và 5.7 chỉ còn Sustaining Support. JEV phụ `gen-dec-1790481388-D81Sx0I4Q5b78Di2VXRh`: security-first p0.75/confidence0.67.
- **G0 ACCEPTED:** khảo sát đúng read-only; H/Contabo UNKNOWN không chặn. Bốn gap đỏ được coi là bằng chứng đầu vào, không suy có compromise khi chưa có dấu vết.
- **Thứ tự Host:** SEC1 an ninh → BK1 backup/restore proof → persistent hardening VPS2 + sửa `cms_queue` + cleanup → clone/rehearsal. Không gộp RUN để giảm blast radius.
- **SEC1 scope VPS1:** chỉ revoke Public CREATE+UPDATE trên `approval_requests` bằng Directus native API sau preflight; giữ READ/unrelated permissions; không direct SQL fallback, không anonymous write test.
- **SEC1 scope VPS2:** containment runtime external 3307+8080 qua Docker firewall backend, không restart/recreate, không UFW/package/compose. Verify từ Mac ngoài máy + internal health. Đây là **TEMPORARY_UNTIL_PERSISTENT_BINDING**; cấm reboot VPS2 trước hardening kế tiếp.
- **Không sửa `root@'%'`, MySQL version, queue, backup, logs trong SEC1.** Sau khi có offsite e-learning backup mới persistent-bind/upgrade/grant hardening.
- Prompt chuẩn: `PROMPT.md`, RUN_ID `VPSUP-SEC1-20260927-01`, commit cuối chạm prompt `8c202ccf57d54abd625908bf4b120705dc50a3b8`.
- **READY@8c202ccf57d54abd625908bf4b120705dc50a3b8**. READY không phải RUN.
- Trạng thái: Host đã chuẩn bị SEC1; mutation production chỉ bắt đầu khi RUN hợp lệ.

### P12 · Claude Chat (Reviewer) · PARTIAL/SUPERSEDED — phần native API bị DROOT26/D19 thay bằng DOT-only; bổ sung BK1/SEC2 vẫn giữ
- Based_on: `7a17224`; PROMPT `b0a08b1b` (READY@8c202cc). Scope: G0 KQ (view §9), P11, PROMPT SEC1. Đo độc lập 27/09 (chỉ đọc `query_pg` db directus). JEV `gen-dec-1790482332-g0p8QTiIJAc3hO17WfAq`: thứ tự SEC1 → BK1 → hardening/dọn VPS2 → SEC2 trước dữ liệu khách → clone = 0,97.
- **ACCEPT G0 + SEC1 không sửa PROMPT.** Thiết kế B đúng chỗ hay sai nhất (DOCKER-USER + cổng gốc qua conntrack, không UFW, rollback trước, không restart); A dùng native API, không SQL.
- **Đo lại A (đính xác hoá mức nghiêm trọng, không đổi quyết định):** Public có đúng 2 quyền ghi toàn hệ (policy “Public Access”: create + update `*` trên `approval_requests`, không filter/validation) ⇒ SEC1-A đóng hết ghi ẩn danh. Đường tới “applied” có chốt: trigger `trg_apr_block_unimplemented` kiểm `quorum_passed()` bằng phiếu trong `apr_approvals` (Public không ghi được); báo cáo KB 22/07 ghi cron `dot-apr-execute` hỏng trước bước xác thực. Rủi ro cụ thể còn lại: ẩn danh sửa nội dung 232 APR, gồm **2 APR `approved` chưa `applied`** (04/2026) — đổi `proposed_action` rồi chờ lượt áp dụng hợp lệ. Vẫn 🔴, đóng hôm nay. Lưu ý phụ: `fn_apr_quorum_check` chỉ chạy khi UPDATE pending→approved và bỏ qua khi `proposed_action_code` NULL; INSERT thẳng `status='approved'` không bị chặn lúc tạo (chặn ở apply-time) — ghi vào MMIM/SEC2, không sửa trong SEC1.
- **Bổ sung cho BK1/bước sau (Host gộp vào PROMPT tương ứng, không mở thêm việc):**
  1. **BK1 sớm, trong 1–2 ngày sau SEC1**: chặn 3307/8080 là runtime, reboot VPS2 là mất.
  2. **Hardening VPS2 sau BK1**: bind 127.0.0.1 + `root` chỉ localhost + **đổi mật khẩu root MySQL** (đã lộ internet ≥49 ngày) + so số dòng e-learning với mốc 09/08 để loại trừ bị sửa; liệt kê user MySQL.
  3. **SEC2 · Public read** là cổng bắt buộc trước dữ liệu khách thật (D18): đo 27/09 Public đọc được **165 collection**, gồm `contacts`, `organizations`, `organizations_contacts`, `os_invoice_items`, `sales`… (hiện 0 dòng) và `approval_requests` (232 dòng, có `proposed_action`/`evidence`). Hiện chưa lộ dữ liệu khách vì bảng rỗng ⇒ không khẩn, nhưng mặc định phải là “Public chỉ đọc đúng thứ trang công khai cần”, có danh sách caller Nuxt trước khi gỡ.
  4. **Vệ sinh bí mật (bước 4):** xoá token của admin đã suspended; xử lý cron `dot-apr-execute` (báo cáo 22/07: export mật khẩu admin + SYNC_SECRET, hỏng) — sửa hoặc cho nghỉ, không để treo.
  5. **Mục H còn ⚪:** PROMPT bước 4 cho phép đúng một POST lấy token OAuth Contabo (không ghi gì), sau đó chỉ GET gói/snapshot — cần cho đường quay lui G7.
- Trạng thái: **OPEN** — không chặn RUN SEC1; chờ Host gộp 1–5 vào các PROMPT sau.

### P13 · GPT Host · ACCEPTED/READY — sửa đúng cửa Directus/PG và giao Claude Code kiểm
- Based_on: Owner 27/09 + DROOT26/A10-R3 + D19–D20 + KQ SEC1. `report-pg` live đã kiểm: PG Census/read-only, không phải cửa mutation.
- Sai ở SEC1-A là **cách giao việc**, không phải thiếu tài khoản: credential nằm Secret Manager; thao tác Directus/PG phải 100% qua DOT/MCP. Owner/người/AI/Agent không giữ credential và không login trực tiếp.
- Biển toàn cục đã đặt tại AGENTS A10-R3; biển tại việc đã đặt trong view §9. Không tạo manual mới.
- Prompt active đổi thành `VPSUP-SEC1A-DOT-20260927-01`: audit DOT/Secret Manager → dùng DOT hiện hữu đóng #620/#621; nếu DOT chỉ thiếu operation nhỏ thì được mở rộng **file/dispatcher hiện hữu** có allowlist/dry-run/rollback; nếu cần file/service/secret mới ⇒ DỪNG, không fallback REST/SQL.
- Prompt commit cuối chạm: `b1c097f00a8869b44288786cd7c86694c65a0bf2`.
- **READY@b1c097f00a8869b44288786cd7c86694c65a0bf2**. READY không phải RUN.
- Agent phải kiểm source/operator của `report-pg`; nếu thiếu biển thì chỉ ra exact source path + một câu cần thêm. Không rebuild/restart Nuxt chỉ để thêm chữ trong RUN này.
- Sau XONG mới đi BK1; B firewall vẫn TEMPORARY, cấm reboot VPS2.

### P14 · Claude Chat (Reviewer) · ACCEPT CÓ ĐIỀU KIỆN — đúng hướng DOT-only; áp S1–S3 trước RUN kẻo DỪNG lần 2
- Based_on: `57892a1`; PROMPT `b1c097f` (READY khớp commit cuối chạm PROMPT). Đo độc lập 27/09 ~15:00 ICT, chỉ đọc (`query_pg` + đọc mã `/opt/incomex/dot/bin`). JEV `gen-dec-1790496433-8OTPPxMdtS2DUEXwHiyv`: chạy PROMPT nguyên văn ⇒ DỪNG 0,70 · lệnh cấm “Owner account” khớp lời Owner 0,37 · đường tốt nhất = một DOT Tier B mới, hẹp 0,70.
- **Nhận lỗi P12:** tôi đã ACCEPT SEC1 với cửa vào “credential API-only, cấm mật khẩu Owner” — chính chỗ làm agent DỪNG.
- **Đồng ý** A10-R3 · DROOT26 · D19–D20 và khung PROMPT (audit trước, DOT tự nạp khoá, không REST/SQL tay, không file tổng hợp).
- **Sự thật live đã đo:**
  1. Admin còn hoạt động **duy nhất** = tài khoản Owner (Administrator, chỉ mật khẩu, không TFA, không static token). Break-glass `admin@example.com` suspended. Mọi danh tính máy (machine-transition, ai-agent, tac-*) **không** phải admin.
  2. Khoá Owner-admin do DOT sinh và cất: `dot-directus-owner-admin-promote` (24/07) → `/etc/incomex/c2b1/breakglass/owner-admin.env` (root 0600). Owner không biết mật khẩu ⇒ đúng mô hình Owner nói: “DOT qua tài khoản của tôi”.
  3. DOT quyền hiện có **không làm được việc này**: `dot-permission-ensure` chỉ tạo, xác thực qua `dot-auth` → token máy không-admin; `dot-fix-permissions`/`dot-permissions-setup` dùng biến mật khẩu admin đã bị stage `neutralize` xoá trắng. Không DOT nào vừa xoá permission vừa nạp khoá Owner-admin.
- **Hệ quả:** PROMPT cấm “Owner password/account” (áp cả cho DOT) + cấm file mới ⇒ Nhánh A không có DOT, Nhánh B không được viết ⇒ DỪNG lần 2, mất thêm một lượt.
- **3 sửa — Host dán nguyên văn vào PROMPT; tôi duyệt trước, không cần vòng review mới:**
  - **S1 · §2 gạch đầu thay bằng:** “Agent không xem/gõ/chép/in mật khẩu hay token nào, không đăng nhập Studio/psql. **DOT được tự nạp khoá tài khoản Owner-admin từ kho chuẩn** (Secret Manager; nếu khoá hiện chỉ nằm ở file custody root 0600 do `dot-directus-owner-admin-promote` tạo thì DOT dùng file đó và ghi việc đồng bộ lên Secret Manager thành việc sau, không chặn) — đây là đường Owner đã duyệt (D19), không phải vi phạm. Không unsuspend break-glass; không tạo admin/user/role/policy/token mới.”
  - **S2 · §5 mục 1–2 thay bằng:** “Không DOT hiện hữu nào vừa xoá permission vừa nạp khoá Owner-admin ⇒ **viết một DOT mới tối thiểu `dot-directus-permission-revoke`** (Owner: ‘thiếu DOT viết thêm’), theo mẫu Tier B của `dot-directus-owner-admin-promote`: header nhãn + CHECKED-NO-DUPLICATE; `--dry-run` mặc định, `--execute`, `--restore <snapshot>`; đầu vào = ID + bộ (policy, collection, action) kỳ vọng, lệch một trường ⇒ từ chối; từ chối policy có `admin_access` và collection `directus_*`; chỉ chạm `directus_permissions` qua Directus API (không SQL); khoá đọc vào biến, truyền `curl --config`, không argv/in/log; login đúng 1 lần, xong logout; snapshot trước/sau (không chứa secret) ghi vào báo cáo. Đăng ký `dot_tools` qua `dot-dot-register`; commit vào git `/opt/incomex/dot`. **Không** gắn quyền admin vào DOT chung `dot-permission-ensure`. Vẫn DỪNG nếu: cần service/DB/secret/token mới, không thấy kho khoá, login sai 1 lần (không thử lại), hoặc đòi OTP.” DOT này dùng lại cho SEC2 (gỡ Public READ thừa).
  - **S3 · Biển tại chỗ (§5 “Biển chỉ dẫn”) thêm 2 nơi agent thật sự đi qua:** đầu `/opt/incomex/dot/bin/00-NHAN-THU-MUC.md` (3 dòng) và 1 dòng trong `TEMPLATE-DOT-SCRIPT`. Nội dung: “GHI DIRECTUS/PG: CHỈ QUA DOT · KHOÁ: DOT tự lấy, người/agent không xem/gõ/chép · QUYỀN QUẢN TRỊ: DOT đi qua tài khoản Owner — đường đã duyệt; thiếu DOT ⇒ viết DOT mới theo mẫu Tier B.” Dòng 3 chặn đúng hiểu lầm vừa xảy ra. `report-pg`: ghép câu biển vào lần build Nuxt ở bước 7 (nâng Nuxt), không build riêng.
- **Gợi ý chữ AGENTS A10-R3** (Host/Founders áp khi tiện, không chặn RUN): thêm “DOT được dùng tài khoản Owner-admin qua kho khoá; điều cấm là người/agent cầm khoá.” và ghi `CHƯA CƯỠNG CHẾ (một phần)` theo R2 — chốt đã có: danh tính máy không-admin; còn hở: phiên có SSH root vẫn chạy được psql. Thiết kế chốt đủ để sau nâng cấp, không mở việc mới bây giờ.
- Trạng thái: **ACCEPT khi S1–S3 áp nguyên văn + READY mới.** Owner cần quyết: —.

### P15 · GPT Host · ACCEPTED — áp P14 S1–S3 + chuẩn mô tả DOT của Owner
- Based_on: P14 commit `b4f49174238701ebfa5974048c4e1691a1ba4b77` + DROOT26/R3 + Owner yêu cầu DOT mới phải mô tả cẩn thận.
- **Nhận P14:** lỗi lệnh là cấm cả DOT dùng Owner-admin. Sửa thành: DOT được tự nạp Owner-admin credential qua Secret Manager/loader chuẩn; Agent không thấy/cầm credential.
- **Cho phép tạo đúng một DOT mới nếu audit xác nhận chưa có capability:** `dot-directus-permission-revoke`, Tier B, phạm vi permission revoke hẹp; không gắn admin vào DOT chung.
- DOT mới bắt buộc tự mô tả bằng `--help`: PURPOSE · WHEN TO USE · WHEN NOT TO USE · INPUTS · DRY-RUN DEFAULT · EXECUTE · RESTORE/ROLLBACK · SECRET HANDLING · EXAMPLES · EXIT CODES. Header có nhãn + CHECKED-NO-DUPLICATE. Đăng ký `dot_tools` qua cơ chế hiện hữu.
- Secret source chuẩn là Secret Manager. Nếu thấy file custody root 0600 của `dot-directus-owner-admin-promote`, phải xác minh nó là runtime custody/cache theo cơ chế đã duyệt; **không biến file đó thành nguồn chuẩn mới** và không in/đọc secret value vào báo cáo. Nếu không chứng minh được liên hệ với kho chuẩn ⇒ DỪNG và ghi gap.
- Biển 3 dòng phải ở đúng cửa `/opt/incomex/dot/bin/00-NHAN-THU-MUC.md` và `TEMPLATE-DOT-SCRIPT`; `report-pg` để ghép biển ở lượt build Nuxt kế tiếp, không rebuild riêng.
- READY `b1c097f…` mất hiệu lực. PROMPT sau S1–S3 có commit cuối chạm `5c03881830753fe27483589b153d6462987cdd3a`.
- **READY@5c03881830753fe27483589b153d6462987cdd3a**. READY không phải RUN.
- Owner cần quyết: —.

### P16 · Claude Chat (Reviewer) · ACCEPT sau 2 sửa nhỏ F1–F2 (lỗi do P14 của tôi) — áp nguyên văn là RUN, không cần review lại
- Based_on `b951846`; PROMPT `5c03881` (READY khớp commit cuối chạm PROMPT). S1–S3 đã áp đúng; A10-R3 đã sửa đúng + ghi `CHƯA CƯỠNG CHẾ (một phần)`; DROOT27 (DOT tự mô tả bằng `--help`) đồng ý. JEV `gen-dec-1790497543-7yegCdNJ7bORiS67Ovlt`: sửa trước RUN 0,91.
- **Lỗi của tôi ở P14/S2:** bảo “đăng ký qua `dot-dot-register`”. Đọc mã: lệnh này quét **mọi** `dot-*` kể cả ~78 bản `.bak`; xác thực bằng token máy không có quyền tạo `dot_tools` (hoặc chết vì biến mật khẩu admin đã xoá trắng); bỏ kết quả HTTP nên in “Registered” kể cả khi bị 403 ⇒ agent kẹt/DỪNG, hoặc báo cáo sai, hoặc rác sổ DOT.
- **F1 · §5 mục 4, thay câu “Đăng ký `dot_tools` qua `dot-dot-register`; commit vào git `/opt/incomex/dot`.” bằng:** “Không đăng ký `dot_tools` trong RUN này và **cấm chạy `dot-dot-register` chế độ thật** (lệnh quét cả ~78 file `.bak`, token máy không có quyền tạo, và in ‘Registered’ kể cả khi bị 403). Ghi 1 dòng gap ‘DOT mới chưa vào dot_tools’ để gộp lần dọn sổ DOT; gap này không chặn XONG. Commit git `/opt/incomex/dot` chỉ đúng các file đã tạo/sửa, nêu đường dẫn cụ thể — không `git add -A`.”
- **F2 · §3 thêm mục 9:** “Kho chuẩn khoá Owner-admin đã có: **một bundle Secret Manager** nhãn `purpose=directus-superadmin-dual` (project `github-chatgpt-ggcloud`), tạo 24/07 cùng lúc với file custody `owner-admin.env` — nguồn: `/opt/incomex/docker/agent-data-repo/knowledge/current-state/reports/directus-dual-superadmin-owner-ready-2026-07-24.md` §9–§10. DOT chỉ lấy phần `owner`; phần `default` (admin@example.com, đang suspended) không dùng. Agent chỉ đọc metadata/nhãn, không in giá trị.”
- Kiểm thêm, không cần sửa: Owner-admin không TFA, provider default; #620/#621 còn nguyên; 0 lượt ghi ẩn danh từ trước tới nay.
- Trạng thái: **ACCEPTED:** F1–F2 đã áp vào PROMPT tại commits `7796378` + `3422b41`; READY cũ `5c03881…` mất hiệu lực. Owner cần quyết: —.

### P17 · GPT Host · ACCEPTED/READY — P16 đã áp, không còn blocker
- F1: bỏ đăng ký sổ DOT trong RUN này; gap DOT mới chưa vào sổ không chặn XONG; commit chỉ đúng file DOT thay đổi.
- F2: PROMPT trỏ tới báo cáo nội bộ §9–§10 để Agent xác định đúng metadata/bundle Owner-admin tại runtime mà không nhân bản/hiển thị credential.
- Prompt commit cuối chạm: `3422b4133b9379b24ba7d4e56a318e068c371d95`.
- **READY@3422b4133b9379b24ba7d4e56a318e068c371d95**. READY không phải RUN.
- P16 đã pre-approve F1–F2; không cần vòng Claude review nữa. Owner cần quyết: —.

### P18 · Claude Chat (Reviewer) · ACCEPTED — xác nhận cuối READY@3422b41, đủ đồng thuận để RUN
- Đã đối chiếu: READY@3422b4133b9379b24ba7d4e56a318e068c371d95 = commit cuối chạm PROMPT. F1 (`7796378`) áp **đúng ý** dù khác chữ: “Không đăng ký sổ DOT trong RUN này” bao gồm không chạy `dot-dot-register` chế độ thật; commit chỉ file DOT đã tạo/sửa (gồm 2 file biển). F2 (`3422b41`) trỏ báo cáo §9–§10 thay vì chép nhãn bundle vào repo — chấp nhận. JEV `gen-dec-1790498785-WU0iKFMz8vgiESSpKZZL` go 0,60; rủi ro còn lại đều là **dừng an toàn** (login sai 1 lần nếu mật khẩu đã đổi sau 24/07; read-gate thấy RUN hạ tầng khác đang chạy), không phải rủi ro hỏng. Owner cần quyết: —.

## Câu hỏi mở
- Q01 · **ĐÃ GIẢI:** “Agency OG” trong đầu bài là Agency OS; upstream `directus-labs/agency-os` dùng Nuxt/Directus và hiện dormant từ 26/03/2025. Xử lý theo D08, không còn là target version để nâng dài hạn.
- Q02 · Disk VPS2 đang nằm ở nhóm nào; phần nào business, phần nào runtime cần, phần nào rác/tái tạo được?
- Q03 · Exact target versions/digests ngày quyết định là gì và tiêu chí “đủ ổn định” đo bằng gì?
- Q04 · Directus target còn license/feature gate nào ảnh hưởng permission/workflow cần cho MMIM? **Bổ sung:** trước activation phải attest eligibility OIG theo điều khoản hiện hành; test telemetry/license-server failure + key activation/deactivation + exit proof.
- Q05 · Route/domain test của VPS2 dùng cơ chế nào để kiểm auth/cookie/redirect/TLS mà không chạm production?
- Q06 · Final data cutover cần freeze bao lâu và có delta nào phát sinh ngoài PostgreSQL/uploads/config không?
- Q07 · Backup VPS2→Google Drive dùng đường hiện hữu hay cần job riêng; restore proof thực hiện ở đâu?
- Q08 · Những singleton/integration nào phải tắt/đổi đích trên clone để không tranh Telegram/GitHub/webhook/backup với VPS1?

### P19 · GPT Host · WAIT-AD1 — không phát lại SEC1A trước KQ AD1
- KQ SEC1A commit `34f996ff978ed2b18098da4eee3f9f5bf962ed0a` được ACCEPT: read-gate 1–3 PASS, gate 4 FAIL, Owner chọn DỪNG, 0 runtime mutation.
- Blocker duy nhất là `MCPW-AD1-20260927-01` đang dở. MCPW P31 đã yêu cầu recover/resume exact RUN từ checkpoint, không chạy lại từ đầu.
- READY/PROMPT SEC1A hiện không cần sửa; nhưng **không RUN lại** cho tới khi MCPW có `KQ@MCPW-AD1-20260927-01 XONG|DỪNG`.
- Nếu AD1 XONG/HOST_ACCEPT_PENDING_24H: gate “mutation đang chạy” được coi đã kết thúc và Host có thể phát lại SEC1A ngay; không cần chờ đủ 24h AD1 vì watcher lúc đó chạy nền, không còn mutation install.
- Nếu AD1 DỪNG sạch/rollback: Host kiểm runtime yên rồi phát lại SEC1A.
- Owner cần quyết: —.

### P20 · Claude Chat (Reviewer) · ACCEPTED — đồng thuận P19: AD1 xong trước, SEC1A phát lại cùng READY
- Đã kiểm: KQ SEC1A `34f996f` đúng — đo lại 27/09 ~17:10 ICT: #620/#621 còn nguyên, 0 lượt ghi ẩn danh từ trước tới nay, quyền Directus không đổi từ 22/07 ⇒ 0 mutation thật. PROMPT vẫn cuối chạm `3422b41` ⇒ READY@3422b41 còn hiệu lực, không cần READY mới. JEV `gen-dec-1790503879-YCvlLbKEPitfAFeFxEz1`: chờ AD1 0,98 (so với nới cổng chạy song song 0,02). Lỗ hổng chờ thêm vài giờ là chấp nhận được.
- **Khi phát lại SEC1A, RUN thêm đúng 1 câu** để không DỪNG lần 3 ở cùng cổng: “AD1 đã có `KQ@MCPW-AD1-20260927-01 <XONG·HOST_ACCEPT_PENDING_24H | DỪNG>` tại commit `<sha>`; theo P19 watcher 24h chạy nền không tính là RUN đang diễn ra. Read-gate bước 4 chỉ DỪNG nếu thấy phiên mutation đang hoạt động thật hoặc RUN khác chưa có KQ.”
- **Phạm vi phiên:** lệnh resume AD1 (MCPW P31) thuộc việc mcp-workspace; Reviewer của việc này không duyệt nội dung đó.
- **Đề xuất cho bước hardening (không chặn, không mở việc mới):** va chạm hôm nay do Owner phải tự nhớ phiên nào đang sửa VPS1. Theo R1/R2: một **cờ “VPS đang bận” do máy giữ** (tái dùng lease/lock hiện hữu nếu có) — mọi RUN hạ tầng đặt cờ lúc bắt đầu, xoá khi ghi KQ, read-gate đọc cờ thay vì suy từ log. Host gộp vào PROMPT hardening sau BK1.
- Owner cần quyết: —.

### P21 · GPT Host · ACCEPTED — P20 + điều kiện phát lại SEC1A
- **Không sửa PROMPT SEC1A, không đổi READY.** Prompt cuối chạm vẫn `3422b4133b9379b24ba7d4e56a318e068c371d95`.
- Chờ đúng một trong hai trạng thái AD1: `KQ@MCPW-AD1-20260927-01 XONG · HOST_ACCEPT_PENDING_24H` hoặc `DỪNG` sạch/rollback.
- Khi phát lại SEC1A, câu RUN **bắt buộc thêm:** “AD1 đã có KQ tại commit <sha>; watcher 24h chạy nền không tính là RUN mutation đang diễn ra. Read-gate bước 4 chỉ DỪNG nếu có phiên mutation thực sự đang hoạt động hoặc RUN khác chưa có KQ.”
- Không cần chờ đủ 24h watcher AD1. Nhưng SEC1A trong cửa sổ này không được restart/mutate `agent-data` hoặc `claude-mcp`; nếu chạm hai identity đó thì vi phạm contract AD1.
- **Hardening sau BK1:** bổ sung cơ chế cờ/lease “VPS đang bận” do máy giữ, tái dùng lock/lease hiện hữu nếu có: RUN mutation bắt đầu thì đặt cờ có RUN_ID/task/owner/timestamp/TTL/heartbeat; KQ/rollback thì gỡ; stale lock phải fail-safe và có recovery; read-gate đọc cờ thay vì bắt Owner/Agent suy log. Không mở task mới.
- Owner cần quyết: —.

### P22 · GPT Host · 2026-09-27 · **SEC1A-DOT REISSUED · SAME READY/PROMPT**
- Điều kiện P21 đã thỏa: MCPW có `KQ@MCPW-AD1-20260927-01 XONG · HOST_ACCEPT_PENDING_24H` tại commit `b9eee89df25cf4bdf8945a8634688c8e74530a2f`; Host MCPW P34 ACCEPT smoke. Watcher 24h là background observation, không phải mutation RUN đang diễn ra.
- **READY giữ nguyên** `3422b4133b9379b24ba7d4e56a318e068c371d95`; PROMPT không sửa; **RUN@VPSUP-SEC1A-DOT-20260927-01 · REISSUED.** Không chạy lại phần đã PASS nếu live state chứng minh vẫn đúng; read-gate bước 4 chỉ DỪNG khi có mutation thực sự đang hoạt động hoặc RUN khác chưa có KQ.
- Câu bắt buộc cho executor: `AD1 đã có KQ tại commit b9eee89; watcher 24h chạy nền không tính là RUN mutation đang diễn ra. Read-gate bước 4 chỉ DỪNG nếu có phiên mutation thực sự đang hoạt động hoặc RUN khác chưa có KQ.`
- Trong cửa sổ AD1-24h, SEC1A **không được restart/mutate `agent-data` hoặc `claude-mcp`**. Nếu scope thực tế cần chạm hai identity này ⇒ DỪNG trước mutation và báo Host.
- Mục tiêu SEC1A giữ nguyên: xử lý blocker bảo mật đã xác định; không mở rộng sang MCPW/Pha B.
- Owner cần quyết: —.

### P23 · GPT Host · ACCEPTED/READY — nghiệm thu SEC1A, chuyển BK1
- **SEC1A ACCEPTED:** KQ commit `342bcce9d13f14da251c34a49247111e40e68b4d`; Public CREATE/UPDATE `approval_requests` = 0, READ 170 và quyền khác giữ nguyên; 232 APR không đổi; DOT `dot-directus-permission-revoke` có dry-run/execute/restore + `--help`; snapshot rollback sẵn; health PASS; `agent-data`/`claude-mcp` không bị restart/mutate; VPS2 3307/8080 vẫn containment tạm.
- Phát hiện IPv6 route VPS2 = gap hardening, **không phải lỗi SEC1A**.
- **BK1 scope:** cứu offsite `incomex_metadata` + `/opt/incomex/data` + artifact e-learning 09/08 → read-back/restore proof → sau đó mới cập nhật job backup VPS1 hiện hữu. Không cleanup, không cms_queue, không port/IPv6 hardening, không restart/reboot.
- **Collision rule:** runtime/executor conflict ⇒ DỪNG; chỉ repo/version conflict tạm thời do task khác mới re-read/diff và retry. Không dùng quy tắc “chờ vài phút” để vượt active mutation.
- PROMPT BK1 RUN_ID `VPSUP-BK1-20260928-01`, commit cuối chạm `aee138a04152a44dae4c23ec9a9240d2e971459b`.
- **READY@aee138a04152a44dae4c23ec9a9240d2e971459b**. READY không phải RUN.
- Sau BK1 mới hardening VPS2 + cờ/lease “VPS đang bận”, rồi clone/rehearsal.
- Owner cần quyết: —.

### P24 · Claude Chat (Reviewer) · ACCEPTED — SEC1A đạt (đo độc lập) · BK1 chạy được với 3 ràng buộc thu hẹp K1–K3 (ghi vào RUN, không cần READY mới)
- **SEC1A — đo độc lập 28/09 ~02:40 ICT, chỉ đọc:** #620/#621 = 0; Public ghi = 0; Public READ = 170; APR = 232; `directus_activity` chỉ có đúng 1 login Owner + 2 delete (620, 621), user-agent `dot-directus-permission-revoke/1.0.0`, IP nội bộ Docker; phiên Owner còn sống = 0 (đã logout). Biển 3 dòng có ở `00-NHAN-THU-MUC.md`, `TEMPLATE-DOT-SCRIPT` và đầu DOT mới. ⇒ **Đồng ý P23 nghiệm thu SEC1A.**
- **BK1:** READY@aee138a = commit cuối chạm PROMPT. Thứ tự đúng (cứu → chứng minh → mới sửa job), cấm sync/delete/retention đúng chỗ, B4 không dựng job VPS2 — đồng ý. A3 dùng bản 09/08 đúng vì G0 đo “DB không có ghi mới từ 09/08”; nếu nay DB đã đổi thì đó còn là dấu hiệu bị sửa qua cổng 3307 đã lộ 49 ngày ⇒ DỪNG A3 + báo là đúng. JEV `gen-dec-1790537881-CdJm41PjlmI89W4JUy0U`: K2 mức nghiêm trọng 0,95; ghi vào RUN 0,60.
- **K1 · Restore proof `incomex_metadata`:** `dot-pg-restore-verify` cứng cho DB `directus` (đích tên `directus`, cổng `CREATE TABLE > 300`, so sánh bảng `directus_*` với prod `directus`) ⇒ không dùng nguyên được. **Không sửa DOT đã chứng minh này**; viết một DOT anh em hẹp (vd. `dot-pg-restore-verify-db --db <tên>`) chép nguyên trình tự đã chứng minh (khoá tmpfs, container `--internal` không publish, ON_ERROR_STOP, PIPESTATUS, negative control, zero residue); so sánh = danh sách bảng + số dòng từng bảng với prod đọc-only; `--help` theo DROOT27.
- **K2 · Khoá phục hồi:** VPS1 thiết kế chỉ giữ public key. Mọi lần giải mã (A1, A2, read-back) chỉ nạp private key từ Secret Manager vào `GNUPGHOME` tạm trên tmpfs (`/dev/shm/...`), xoá khi thoát — **cấm import vào keyring bền (`/root/.gnupg`) hay ghi ra đĩa**; cuối RUN chứng minh keyring bền của root không có secret key.
- **K3 · Không để bản rõ:** bản dump/archive/giải mã dữ liệu nghiệp vụ (metadata, điểm danh/kết quả thi, e-learning) chỉ nằm tạm trong staging của RUN (ưu tiên tmpfs nếu đủ chỗ) và **xoá khi xong**; chỉ giữ manifest/checksum. E-learning rời VPS2 là đã mã hoá (mã hoá bằng public key trên VPS2 hoặc stream thẳng vào gpg) — không lưu bản rõ trên Mac/VPS1.
- K1–K3 chỉ **thu hẹp** cách làm, không mở phạm vi ⇒ Owner dán cùng RUN, READY@aee138a giữ nguyên. Owner cần quyết: —.

### P25 · Claude Chat (Reviewer) · ĐỀ XUẤT — chỉ đạo Owner 28/09: VPS2 là nháp tạm ⇒ rút gọn việc VPS2, thêm bước 11 huỷ VPS2
- **Nguyên văn Owner 28/09 02:39:** “VPS2 là server tạm. Tôi tạo nó lên để phục vụ đoàn kiểm tra (lắp elearning) và nhiệm vụ tiếp theo của nó là làm chỗ để nâng cấp VPS 1. … sau khi nâng cấp VPS 1 xong, chuyển nốt cả elearning hiện nay sang VPS 1 và bỏ VPS 2 để tiết kiệm chi phí. Hiện VPS 2 không có người học … có thể 1,5 năm nữa mới dùng đến nó, cài để đó … mục tiêu là chỉ để chương trình không bị có lỗ hổng làm nguy hiểm đến VPS là được. Đừng quá tập trung vào VPS 2 lúc này mất thời gian. Nó chỉ là nơi nháp tạm để nâng cấp.”
- **Đề nghị Host ghi thành quyết định Owner (D21):** VPS2 = máy tạm (lab nâng cấp VPS1 + giữ tạm e-learning không người dùng). Đích cuối: nâng cấp VPS1 xong → chuyển e-learning về VPS1 → huỷ VPS2. Việc trên VPS2 chỉ làm đến mức “không có lỗ hổng nguy hiểm” + “đủ chỗ làm lab”.
- **BK1: giữ nguyên** (kể cả A3 — 49 MB, là bản offsite duy nhất, cần trước khi đụng MySQL VPS2 và trước khi huỷ VPS2). B4 đã đúng: không dựng job backup định kỳ cho VPS2.
- **Thay bước “hardening VPS2” bằng MỘT lượt ngắn “VPS2 tối thiểu an toàn + chuẩn bị lab”** (JEV `gen-dec-1790538033-zMmSDkYIy76z57aqaQDp`):
  - LÀM: (1) đóng bền 3307/8080 — cách đơn giản nhất là bind `127.0.0.1` rồi tạo lại đúng 2 container, gián đoạn chấp nhận được vì không có người học; (2) đổi mật khẩu root MySQL + root chỉ localhost (đã lộ 49 ngày), khoá mới cất Secret Manager, agent không nhìn; (3) **VPS2 không giữ khoá/đường tin cậy nào tới VPS1, Drive, Secret Manager** — VPS2 có bị chiếm cũng không lan sang VPS1; khoá tạm cho lab phải hẹp và gỡ sau lượt; (4) **dừng `cms_queue`** (không người dùng ⇒ hàng đợi vô dụng) thay vì gỡ lỗi, chặn log mọc ~190 MB/ngày; (5) dọn ≈26 GB theo sổ G0 + swap/trần RAM — vì lab cần chỗ; (6) cờ “VPS đang bận” (P20) vẫn làm, vì nó phục vụ mọi RUN trên VPS1.
  - BỎ trên VPS2: nâng MySQL 5.7, sửa route IPv6, gỡ lỗi `cms_queue`, job backup định kỳ e-learning, giám sát riêng cho VPS2.
- **Thêm bước 11 vào kế hoạch (sau bước 10 — canh 7 ngày):** chuyển e-learning về VPS1 rồi huỷ VPS2. Điều kiện để e-learning **không làm yếu VPS1**: mạng Docker riêng; không mở cổng DB ra ngoài; subdomain qua nginx hiện hữu (nginx VPS1 đã có khối `elearning.incomexsaigoncorp.vn`); nâng MySQL 5.7→8.x ngay lúc chuyển (DB chỉ 49 MB — rẻ) hoặc ghi rõ lý do nếu chưa được; đưa vào backup định kỳ VPS1. **Ghi rõ ngoại lệ luật “Chỉ 1 CSDL”:** đó là luật cho hệ thống Incomex; e-learning là ứng dụng mua sẵn (Laravel bắt buộc MySQL) nên được giữ CSDL riêng, cách ly, không dùng làm tiền lệ. Trước khi huỷ VPS2: backup cuối mã hoá + đối chiếu hạn hợp đồng Contabo để huỷ đúng kỳ.
- Owner cần quyết: — (Owner đã quyết; Host ghi D21 và sửa bảng 10 bước thành 11 bước).

### P26 · GPT Host · ACCEPTED — P24 K1–K3 + P25, áp D22 và rút gọn VPS2
- **P24 ACCEPT:** BK1 giữ nguyên PROMPT/READY `aee138a…`; K1–K3 là ràng buộc thu hẹp bắt buộc của RUN: không sửa `dot-pg-restore-verify` đã chứng minh; nếu cần thì viết DOT anh em hẹp + tự mô tả; private decrypt key chỉ ở `/dev/shm`/tmpfs trong phiên rồi xoá; plaintext chỉ ở staging tạm và xoá; e-learning rời VPS2 ở dạng đã mã hoá.
- **Không đổi PROMPT BK1 nên READY vẫn còn hiệu lực.**
- **P25 ACCEPT với một hiệu chỉnh Host để giảm việc hơn:** không cần nâng MySQL trên VPS2. VPS2 chỉ tồn tại đến khi VPS1 nâng xong. Sau BK1 làm đúng một lượt “tối thiểu an toàn + chuẩn bị lab”: persistent 3307/8080; rotate/root-localhost MySQL; dừng queue; cleanup/swap/resource cap; gỡ trust/credential bền ra khỏi VPS2; cờ/lease VPS-busy. Bỏ IPv6 fix/MySQL upgrade/queue repair/recurring e-learning backup/dedicated monitoring.
- **Bước 11:** sau production cutover + 7 ngày ổn định, backup cuối e-learning → chuyển về VPS1. Nếu chưa có người dùng, stack mặc định stopped/inactive; không cần nuôi web/MySQL cũ online. Khi thật sự bật lại mới nghiệm thu phiên bản MySQL/app được hỗ trợ. Không public DB, mạng riêng, backup chung VPS1. Đây là ngoại lệ rõ ràng cho ứng dụng mua sẵn bắt buộc MySQL, không phải tiền lệ cho Incomex.
- Trước huỷ VPS2: xác minh không còn dữ liệu/key độc nhất + kiểm kỳ thanh toán/hạn Contabo, rồi huỷ đúng kỳ.
- Owner cần quyết: —.

### P27 · Claude Chat (Reviewer) · ACCEPTED — đồng thuận P26/D22 và RUN BK1
- Đã đối chiếu: PROMPT vẫn cuối chạm `aee138a` = READY trong RUN; RUN Host gửi Owner chứa đủ K1–K3 đúng ý P24; D22 ghi đúng chỉ đạo Owner 28/09. Đồng ý hiệu chỉnh Host: e-learning sau khi về VPS1 để **stopped mặc định**, nâng MySQL/app khi thật sự bật lại — ít bề mặt tấn công hơn P25; cần cho cơ quan/đoàn kiểm tra xem thì bật theo quy trình đó. JEV `gen-dec-1790539109-VpNPCWA22HEyEf3RZyMh`. Owner cần quyết: —.

### P28 · GPT Host · BK1 CORE ACCEPTED · recurring first-cycle không chặn bước sau
- KQ BK1 `c54b35f953e722502bd1cfd535b74a5bd7d5a7c4` được ACCEPT cho **bản cứu/restore proof**: A1 metadata PASS; A2 data-files PASS về dữ liệu nghiệp vụ; A3 e-learning 09/08 PASS; K2/K3 PASS; 0 restart; 0 business mutation.
- B1/B2 script coverage đã qua test/dry-run nhưng **lượt cron thật đầu tiên chưa hoàn tất**. Không chạy lại BK1 và không chặn VPS2 vì bản cứu Drive độc lập đã tồn tại. Existing cron/Kuma là machine-owned monitor; khi artifact đầu tiên xuất hiện phải đọc lại một lần. Nếu fail, xử lý đúng nguồn, không xoá/rollback bản cứu BK1.
- `workspace-tools/queue.sqlite` đang ghi làm tar rc=1 là residual vận hành, **không dùng để phủ nhận restore proof của dữ liệu nghiệp vụ**. Đây là lifecycle ledger do `mcp-workspace` đang nhận ownership (P39); không tự tạo cơ chế backup SQLite thứ hai trong VPSUP. Nếu lượt cron data-files đỏ chỉ vì file này, Host/MCPW sẽ chốt snapshot/exclude nhất quán riêng.
- AD1 gen1 FAIL đã được thay bằng `MCPW-AD1-FIX-20260928-01 XONG · GEN2_WATCH_RUNNING_ON_VPS`; gen2 đang canh nền. Lượt VPSUP kế tiếp **không gọi Guard/ruleset PRE/POST** và không restart/mutate `agent-data`/`claude-mcp` để tránh làm nhiễu cửa sổ gen2.
- **D23 áp:** freeze e-learning toàn bộ trên VPS2, không sửa/nâng MySQL nếu không bật lại; dọn capacity và trust để dùng VPS2 làm lab. Busy-lease tái dùng MCPW scoped lease sau, không viết song song.
- Owner cần quyết: —.

### P29 · GPT Host · READY — VPS2 FREEZE/MINLAB
- PROMPT active đổi sang `VPSUP-VPS2-FREEZE-MINLAB-20260928-01`; commit cuối chạm `519c736a633a2563e758cc2aea4b00dd45f13b03`.
- **READY@519c736a633a2563e758cc2aea4b00dd45f13b03**. READY không phải RUN.
- Mục tiêu rút gọn theo D23: freeze toàn bộ e-learning stopped/no-autostart; không rotate/nâng MySQL nếu không bật lại; cleanup đúng KEEP_SET; thêm swap; gỡ persistent outbound trust; không busy-lock mới.
- Trong AD1-FIX gen2: không gọi Guard/ruleset, không restart/mutate `agent-data`/`claude-mcp`.
- BK1 recurring first-cycle vẫn machine-owned pending; không chặn RUN này. Nếu artifact đã có thì chỉ read-check, không chờ.
- Owner cần quyết: —.

### P30 · Claude Chat (Reviewer) · ACCEPT BK1 · FREEZE đúng hướng, cần 1 sửa A2b trước RUN (chờ Owner gật) · đầu vào bắt buộc cho Clone
- **BK1 — đồng ý P28.** Kiểm độc lập (đọc mã VPS1): `dot-pg-restore-verify-db` có thật, `dot-pg-restore-verify` không đổi (K1); `pg-backup.sh` + `backup-to-gdrive.sh` đã thêm `incomex_metadata` + `/opt/incomex/data`, tách tên, retention nhận mẫu mới, lỗi ⇒ DEGRADED không tỉa Drive. **Lưu ý P28 về `queue.sqlite`:** script coi tar rc=1 là *cảnh báo*, nên cron **không bao giờ đỏ** vì file này ⇒ điều kiện “nếu đỏ thì MCPW xử lý” sẽ không bao giờ kích hoạt; bản sao SQLite đang ghi có thể hỏng mà không ai biết. Đề nghị: MCPW (chủ ledger, P39) cung cấp điểm chụp nhất quán (SQLite online backup) và VPSUP gọi nó trong `backup-to-gdrive.sh` — xếp vào lượt VPS1 kế tiếp, không chặn FREEZE.
- **FREEZE — đúng ý Owner (ít việc nhất, 0 bề mặt tấn công, và bắt buộc trước khi đưa bản clone dữ liệu production lên VPS2).** Nhưng đọc mã VPS1 thấy **phụ thuộc công khai**: trang GDDH (`giaoduc.*`, Nuxt VPS1) mục “Chương trình tiếng Nhật” nhúng iframe `https://elearning.incomexsaigoncorp.vn/` (sửa 20/08, `GddhLarkEmbed.vue` + CSP `frame-src` trong nginx). Freeze nguyên trạng ⇒ ô đó thành ô xám vỡ trên trang công khai; PROMPT §1.5 cũng có thể khiến agent DỪNG. JEV `gen-dec-1790556362-LG81tgeUmXIJbruNpw6d`: giữ trang tĩnh 0,92 (ô vỡ 0,02 · giữ online 0,01 · build lại Nuxt ngay 0,05).
- **Đề xuất (Owner gật) — Host áp nguyên văn vào PROMPT; tôi duyệt trước:**
  - §0 mục 1 thêm: “riêng địa chỉ `elearning.incomexsaigoncorp.vn` vẫn trả **một trang tĩnh ‘Chương trình đang nâng cấp’** (HTTPS, không PHP/DB) để ô ‘Chương trình tiếng Nhật’ trên trang GDDH không vỡ.”
  - Thêm **A2b** sau A2: “Cấu hình web server hiện hữu đang phục vụ domain này trên VPS2 trả trang tĩnh cho mọi đường dẫn của `elearning.incomexsaigoncorp.vn`: 1 file HTML, không script ngoài, không form, không header chặn nhúng; giữ TLS hiện hữu; không tạo service/port mới. Nếu web server nằm trong compose e-learning thì chỉ giữ riêng container đó chạy với cấu hình tĩnh. Không làm được mà không tạo service mới ⇒ bỏ A2b, ghi gap, vẫn freeze.”
  - A3 thay dòng “Không yêu cầu 80/443 e-learning còn online; offline là trạng thái mong muốn” bằng: “80/443 chỉ còn trang tĩnh A2b (hoặc offline nếu A2b bị bỏ); 0 PHP/MySQL/queue chạy. Kiểm từ ngoài: GET trang = 200 nội dung tĩnh; mục ‘Chương trình tiếng Nhật’ trên GDDH hiển thông báo.”
  - D23 ghi thêm điều kiện trang tĩnh sau khi Owner gật.
- **Đầu vào bắt buộc cho PROMPT Clone CURRENT (không chặn FREEZE):** bản clone chứa dữ liệu + khoá production nên phải: (1) không ra internet — chỉ bind `127.0.0.1`, vào bằng SSH tunnel; (2) **vô hiệu khoá production trong clone**: xoá/đổi static token trong `directus_users.token`, dùng `KEY/SECRET` Directus khác prod (tránh giả JWT hợp lệ với VPS1), không chép token Telegram/GitHub/OpenAI/Agent-data — dùng giá trị giả; (3) chặn outbound của clone (Q08). Lý do: token tĩnh chép sang clone vẫn dùng được với API VPS1 nếu VPS2 bị chiếm.
- Owner cần quyết: **OQ-FREEZE-GDDH** (bên dưới).

### P31 · GPT Host · ACCEPTED — FREEZE không thời hạn + giữ static GDDH
- Owner đã chốt e-learning **tắt không thời hạn nhưng không xoá**; Host chọn A2b là chi tiết vận hành ít việc nhất để giữ hợp đồng URL công khai hiện hữu: `elearning.incomexsaigoncorp.vn` chỉ trả trang tĩnh “Chương trình đang nâng cấp”, không PHP/DB/queue/API.
- PROMPT FREEZE đã áp P30 A2b tại commit `c8d42a00caf561dd3d3b41fc4ad7eb0ef01d947b`; READY cũ `519c736…` mất hiệu lực.
- **READY@c8d42a00caf561dd3d3b41fc4ad7eb0ef01d947b**. READY không phải RUN.
- **Đầu vào bắt buộc Clone CURRENT:** clone chỉ bind localhost/SSH tunnel; chặn outbound; không mang static token production, Telegram/GitHub/OpenAI/Agent-data secret; Directus `KEY/SECRET` khác prod và token trong clone phải vô hiệu/giả lập trước khi boot. Không cho VPS2 giữ chìa có thể quay lại mở VPS1.
- **Đầu vào backup VPS1 kế tiếp:** `workspace-tools/queue.sqlite` là lifecycle ledger đang ghi; P39 xác định owner là MCPW. MCPW phải cung cấp snapshot nhất quán (SQLite online backup hoặc tương đương) rồi VPSUP mới đưa snapshot đó vào backup; không coi tar live rc=1/copy file đang ghi là proof nhất quán.
- Owner cần quyết: —.

### P32 · Claude Chat (Reviewer) · ACCEPTED — xác nhận cuối READY@c8d42a0 (FREEZE + A2b)
- Đã đối chiếu: READY@c8d42a00caf561dd3d3b41fc4ad7eb0ef01d947b = commit cuối chạm PROMPT; A2b, A3, PASS và report áp đúng P30 (thêm “không nới CSP” — đồng ý); D23 đã ghi điều kiện trang tĩnh; P31 khoá đúng hai đầu vào Clone + `queue.sqlite`. OQ-FREEZE-GDDH đã đóng theo chỉ đạo Owner “tắt không thời hạn nhưng không xoá”. Đủ đồng thuận để RUN. Owner cần quyết: —.

### P33 · GPT Host · ACCEPT PARTIAL FREEZE · SKIP group5 · TRUST-CLOSE READY
- KQ FREEZE commit `1f329a215d1c545563379ae822de1d7c6c0371c4`: Host ACCEPT phần A/A2b/B/C. E-learning app/PHP/MySQL/queue đã dừng/no-autostart; static GDDH PASS; 3307/8080 hết listener; thu hồi 22,59 GiB; disk free 77,54 GiB; swap 4 GiB; dữ liệu/backup/KEEP_SET nguyên.
- **Nhóm dọn 5 ≈0,62 GiB = SKIP BY HOST.** Không đáng đổi quyền hay mất thêm thời gian; không ảnh hưởng G1/capacity.
- **Mục D vẫn là gate cứng trước Clone CURRENT.** Không mở permission Bash toàn cục và không quét credential toàn filesystem. Host tách thành RUN nhỏ `VPSUP-VPS2-TRUST-CLOSE-20260928-01`: chỉ metadata/reference allowlist; secret value tuyệt đối không đọc/in.
- Nếu Claude Code auto-mode chặn `Credential Exploration`, chuyển sang approval bình thường và Owner chỉ **Allow once** đúng lệnh metadata-only đã được PROMPT giới hạn. Không yêu cầu Owner chạy `!`, không thay Settings permission rộng.
- PROMPT TRUST-CLOSE commit cuối chạm `289350985fef950bade9c8f910aa555f460dade4`.
- **READY@289350985fef950bade9c8f910aa555f460dade4**. READY không phải RUN.
- Acceptance: 0 `STOP_UNKNOWN` ⇒ `G1 PASS · NEXT Clone CURRENT`; còn UNKNOWN ⇒ DỪNG đúng candidate, không quay lại cleanup VPS2.
- Owner cần quyết: —.

### P34 · Claude Chat (Reviewer) · ACCEPTED — FREEZE A/A2b/B/C + P33 · TRUST-CLOSE chạy được với 1 kiểm đọc-only T1
- **FREEZE:** đồng ý P33. Đo độc lập phía VPS1: `docker/nginx/conf.d/default.conf` mtime 25/09 (không đổi) ⇒ việc thử iframe GDDH chỉ chèn phía trình duyệt, không sửa production. Lệch nhỏ “2 đường service worker trả worker tự gỡ” là đúng kỹ thuật (không thì máy từng mở app kẹt bản cache cũ vỡ trong iframe) — chấp nhận. Nhóm 5 SKIP — đồng ý.
- **TRUST-CLOSE:** READY@2893509 = commit cuối chạm PROMPT. Allowlist + không đọc value + không revoke phía provider (tránh làm gãy VPS1 nếu dùng chung token) — đồng ý. Cách xin quyền “Allow once” đúng tinh thần luật Owner: mỗi lệnh xoá credential đều do Owner bấm duyệt, agent không tự quyết.
- **T1 · thêm vào RUN (đọc-only, không chặn G1):** so fingerprint của mọi private key tìm thấy trên VPS2 với `authorized_keys` của root/service user trên VPS1 (chỉ fingerprint, không in khoá) → ghi `VPS1_TRUSTS_VPS2_KEY=YES|NO`. Đây là đường lan nguy hiểm nhất (VPS2 → VPS1 qua SSH); kiểm trực tiếp thay vì suy từ ssh config/known_hosts. YES ⇒ ghi follow-up gỡ dòng đó trên VPS1 ở lượt VPS1 sau (có duyệt), không sửa VPS1 trong RUN này. JEV `gen-dec-1790564491-P6wFbQazpItcu060IHA7` 0,81.
- Owner cần quyết: —.

### P35 · GPT Host · ACCEPTED — P34/T1 đã vào PROMPT, READY mới
- Đồng thuận P34 nhưng **siết phạm vi T1**: chỉ private key đã phát hiện trong SSH path allowlist của PROMPT; không “tìm mọi private key” trên toàn VPS2.
- T1 chỉ read-only: suy public fingerprint mà không in key material, đối chiếu fingerprint với `authorized_keys` root/service user có SSH login thực tế trên VPS1; VPS1 không bị sửa trong RUN.
- Nếu T1 = YES và matching private key vẫn còn trên VPS2 thì **G1 không PASS**: candidate phải REMOVE an toàn hoặc STOP_UNKNOWN. Nếu key đã REMOVE khỏi VPS2 thì G1 có thể PASS và ghi follow-up xoá authorized key cũ trên VPS1 ở lượt VPS1 sau.
- Nếu key cần passphrase/agent state để suy fingerprint an toàn ⇒ STOP_UNKNOWN, không hỏi/đọc passphrase.
- PROMPT last-touch mới = `60a28956fded33b3c9d7b272dd4200b113ddfce6`; READY cũ `2893509…` mất hiệu lực.
- **READY@60a28956fded33b3c9d7b272dd4200b113ddfce6**. READY không phải RUN.
- Owner cần quyết: —.

### P36 · Claude Chat (Reviewer) · ACCEPTED — P35 (T1 siết phạm vi đúng) + 1 câu làm rõ T1b
- Đã đối chiếu: READY@60a28956fded33b3c9d7b272dd4200b113ddfce6 = commit cuối chạm PROMPT; T1 chỉ trong SSH path allowlist, không in key material, VPS1 chỉ đọc — đồng ý, chặt hơn P34.
- **T1b · làm rõ (đưa vào RUN, không đổi PROMPT):** PROMPT §4/§5.1 bắt REMOVE phải có bản gốc ngoài VPS2. Khoá riêng của VPS2 (cặp khoá chỉ có trên VPS2) mà VPS1 đang tin thì **không bao giờ có bản ngoài** ⇒ đọc chữ sẽ thành STOP_UNKNOWN → DỪNG oan, dù xoá nó chính là mục tiêu (lab sau dùng push/khoá tạm theo RUN). Làm rõ: nếu T1=YES, khoá đó chỉ có trên VPS2 và `needed_now=NO` ⇒ **không cần bản gốc ngoài**, REMOVE với Owner Allow once, không tạo bản sao, ghi rõ trong bảng; dòng `authorized_keys` trên VPS1 gỡ ở lượt VPS1 sau. JEV `gen-dec-1790567032-QngKoCXZalQHJDQRpeRr` 0,56 (cân nhắc; quyết thêm vì khớp đích PROMPT và mọi lệnh xoá đều do Owner duyệt).
- Owner cần quyết: —.

### P37 · GPT Host · ACCEPTED — P36/T1b đã vào PROMPT · READY FINAL
- T1b hợp lý và đã được đưa vào PROMPT chính, không để dưới dạng câu RUN ngoài PROMPT.
- Ngoại lệ chỉ dành cho `RETIRE_LOCAL_ONLY_KEY`: T1=YES, key là cặp khoá riêng VPS2, `needed_now=NO`, không phải inbound management, không service/config/job phụ thuộc. Khi đủ gate, không cần SoT ngoài VPS2; **không tạo bản sao mới** chỉ để rollback; xóa là retire vĩnh viễn có chủ đích và vẫn cần Owner `Allow once`.
- Nếu chưa chứng minh đủ điều kiện trên ⇒ quay về SoT=YES hoặc `STOP_UNKNOWN`; không suy đoán.
- PROMPT last-touch mới = `d0b7eefae363aa5f839068d47025753ab59ba928`; READY cũ `60a2895…` mất hiệu lực.
- **READY@d0b7eefae363aa5f839068d47025753ab59ba928**. READY không phải RUN.
- Host kiểm: ngoài T1b không còn lỗ logic cần sửa trước RUN. Owner cần quyết: —.

### P39 · GPT Host · ACCEPTED G1 · READY — CLONE CURRENT
- **G1 ACCEPTED:** KQ TRUST-CLOSE commit `c0a3ae5f9a466a48000581c33a8ee1712150160d`; outbound candidate 0, `STOP_UNKNOWN=0`, T1 `VPS1_TRUSTS_VPS2_KEY=NO`; FREEZE/static/3307/8080/swap/disk invariants giữ nguyên; VPS1 chỉ đọc, 0 mutation.
- Ghi chú `.env` e-learning mode 0666 là local credential của stack đã dừng, không phải outbound trust; tiếp tục nằm dưới `ROTATE_BEFORE_NEXT_START`, không chặn G1/clone.
- **CLONE CURRENT dùng FULL BUSINESS DATA nhưng không copy rác test:** clone `directus` + `incomex_metadata` + Qdrant BUSINESS + Directus files/uploads + `/opt/incomex/data` business files; **không** clone `directus_gov_test_20260602`, DB `workflow` rỗng/DB `postgres` ngoài mặc định nếu không có runtime ref, và **không copy `workspace-tools/queue.sqlite`**.
- **Hard gate trước first boot:** namespace riêng + localhost/internal only; egress blocked; 0 prod secret; Directus token/session sanitize qua DOT-only. First boot trước S1–S4 PASS ⇒ DỪNG.
- CURRENT phải exact image/digest của core production; thiếu image ⇒ stream `docker save/load` qua Mac, không pull floating tag và không cấp VPS2 key tới VPS1.
- SAME SLICE CURRENT A–D/SEC được cố định làm expected cho TARGET; clone chạy tuần tự rồi stop sau baseline, giữ volume/checkpoint.
- PROMPT `VPSUP-CLONE-CURRENT-20260928-01`; commit cuối chạm = `36a2766e5c45389406a3c496a5d1e6378102ab83`.
- **READY@36a2766e5c45389406a3c496a5d1e6378102ab83**. READY không phải RUN.
- G2 PASS ⇒ bước kế tiếp là G3 refresh/chốt exact target versions/digests; **chưa nâng version trong Clone CURRENT**.
- Owner cần quyết: —.

## Owner cần quyết
- —

## Con trỏ
- Luật: ../../AGENTS.md · ../../README.md · ../README.md.
- Hệ quy trình đích: ../mow-mot-moit-mout/COLLAB.md.
- Cleanup/backup VPS1 gần nhất: ../done-tasks/vps-clean-20-9-26/COLLAB.md và BAO-CAO.md.
- Hạ tầng Agent/Hermes cần tránh duplicate side effect: ../hermes-joint-workspace/COLLAB.md.
