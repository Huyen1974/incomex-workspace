# PROMPT — VPSUP BK1 · đóng gap backup + restore proof

RUN_ID: VPSUP-BK1-20260928-01
STATUS: Chỉ thực thi sau khi COLLAB có READY đúng SHA commit cuối chạm file này và Owner/GPT Host phát RUN.
Host: GPT Chat · GPT-VPSUP-20260926-A
Executor_Surface: Claude Code CLI trên Mac Owner.
Report_Write_Path: **fs_* / Incomex VPS MCP · root gh → incomex-workspace/main**.
Runtime_Write_Path: SSH/operator hiện hữu tới VPS1/VPS2 + rclone/Drive + DOT/MCP hiện hữu.
Runtime VPS/Drive là SSOT của trạng thái thực. Không có fallback direct mutation Directus/PG.

## 0. Mục tiêu duy nhất

Đóng các gap backup đỏ của G0/SEC1A, theo thứ tự **cứu dữ liệu trước → chứng minh đọc/restore được → mới sửa job định kỳ**:

1. VPS1 `incomex_metadata` (BUSINESS) có local/offsite backup mã hoá + restore proof.
2. VPS1 `/opt/incomex/data` (BUSINESS files) có offsite backup mã hoá + read-back/restore proof.
3. VPS2 e-learning: bản backup 09/08 được đưa ra Google Drive prefix riêng + đọc lại xác minh; tận dụng restore proof hiện hữu nếu đúng cùng artifact.
4. Chỉ sau 1–3 PASS mới cập nhật **job backup hiện hữu** để coverage VPS1 không tái hở.
5. Không dọn VPS2, không sửa `cms_queue`, không hardening port/IPv6, không reboot/restart, không nâng phần mềm.

## 1. Read gate / collision gate

1. `fs_stat work/vps1-up-grade/COLLAB.md`.
2. Đọc: `AGENTS.md` A10-R3/DROOT25–27 → task COLLAB (§0, G0 KQ, SEC1/SEC1A KQ, P19–P23) → PROMPT này → view.html §9.
3. READY phải khớp commit cuối chạm PROMPT.
4. Xác minh AD1 chỉ còn watcher nền hoặc đã kết thúc; **watcher nền không phải mutation RUN**.
5. Xác minh không có executor/RUN khác đang mutation VPS1/VPS2 hoặc cùng script/Drive prefix. Có ⇒ DỪNG, không “chờ vài phút rồi tự làm”.
6. Chỉ với **repo/version conflict tạm thời** do task khác: re-read/diff; nếu task path không đổi thì có thể đợi ngắn rồi retry gateway. Runtime/executor conflict tuyệt đối không coi là repo conflict.
7. Trong cửa sổ AD1-24h: không restart/mutate `agent-data` hoặc `claude-mcp`.

## 2. Luật cứng

### Directus/PG
**DIRECTUS/PG = DOT ONLY · Secrets = Secret Manager.**
- Người/Agent không xem/gõ/chép credential.
- `pg_dump`/read-only metadata được phép vì không mutation DB.
- Mọi **restore/write vào PostgreSQL**, kể cả DB verify cô lập, phải qua DOT/MCP được duyệt.
- Reuse DOT restore-verify hiện hữu nếu có; nếu thiếu capability thì chỉ được bổ sung/viết DOT hẹp theo A10-R3/DROOT27, không direct SQL.

### Backup/Drive
- Không dùng `rclone sync/move/delete/purge` trong phần cứu dữ liệu.
- Không chạy retention/xoá Drive trước khi BK1 proof PASS.
- Bản cứu BK1 dùng prefix riêng, append-only trong RUN.
- Không overwrite artifact đã upload; tên gồm timestamp + checksum/meta.
- Mã hoá bằng cơ chế/GPG recipient hiện hữu; không tạo key/secret mới.
- Không in credential/rclone token/GPG private material.
- Mọi upload phải kiểm remote size + provider hash khi có; nếu provider hash không tương đương local thì download read-back + sha256 local.

### Runtime
- Không restart/recreate container/service.
- Không reboot VPS1/VPS2.
- Không sửa firewall/DNS/Caddy/nginx.
- Không dọn log/cache/image/tmp hiện hữu ngoài **temporary BK1 staging** của chính RUN.
- Không sửa `cms_queue`, MySQL grants/version, IPv6.
- Cấm xoá source backup 09/08 trên VPS2 trong BK1.

## 3. PRE — audit đúng cơ chế hiện hữu

Chụp trước:
- disk/free/load VPS1/VPS2;
- Drive quota/free;
- health Directus/PG/Qdrant/e-learning;
- `agent-data` + `claude-mcp` image/StartedAt;
- 3307/8080 containment còn hiện hữu;
- backup jobs/scripts + cron/timer hiện tại;
- GPG recipient count/fingerprint reference (không private key);
- newest Drive backup + retention config.

Xác nhận live:
- `pg-backup.sh` và `backup-to-gdrive.sh` hiện cover gì;
- `incomex_metadata` size + read-only consistency metadata;
- `/opt/incomex/data` size/file count/ownership/mode/mtime summary, không đọc nội dung nghiệp vụ;
- artifact e-learning 09/08 path, size, checksum; đối chiếu artifact đã restore thử với `cms_elearning_verify`;
- tìm DOT restore/verify PostgreSQL hiện hữu và chạy `--help`/dry-run nếu có; không tự suy từ tên.

PRE fail, source artifact không xác định được, Drive không đủ chỗ, GPG/remote lỗi, containment VPS2 mất, hoặc có mutation khác ⇒ DỪNG trước backup modification.

## 4. Pha A — bản cứu offsite độc lập, chưa sửa job

Tạo hồ sơ runtime đúng task:
`/opt/incomex/work/vps1-up-grade/BK1-20260928/`
Chỉ chứa manifest/checksum/log sanitized/staging cần cho BK1; không secret/business record.

### A1 · `incomex_metadata`
- Tạo dump consistent/read-only bằng cơ chế backup hiện hữu hoặc `pg_dump` read-only.
- Lưu local staging có sha256 + size + dump metadata.
- Mã hoá bằng đúng GPG recipient/cơ chế đang dùng cho Drive production.
- Upload vào prefix BK1 riêng; không retention.
- Verify remote object + download read-back + decrypt.
- **Restore proof:** ưu tiên DOT restore-verify hiện hữu vào PG cô lập/verify namespace không phục vụ production. Không dùng production DB name, không thay `incomex_metadata`.
- Acceptance restore: restore thành công; schema/table/count metadata đối chiếu nguồn theo read-only snapshot ở mức đủ chứng minh; sau proof cleanup verify target bằng chính DOT nếu DOT có cleanup; nếu cleanup không an toàn thì giữ isolated verify target và ghi rõ, không tự SQL xoá.

### A2 · `/opt/incomex/data`
- Tạo archive từ đúng path hiện hữu, giữ relative path + mode + uid/gid + mtime cần thiết.
- Manifest: file count, total bytes, sha256 archive + checksum list hoặc Merkle/list phù hợp; không đưa nội dung file vào report.
- Mã hoá + upload prefix BK1.
- Download/decrypt vào staging cô lập.
- Restore proof ra thư mục verify riêng: số file/bytes + checksum khớp; không overwrite path production.
- Không thay đổi file nguồn.

### A3 · E-learning VPS2 09/08
- Dùng **đúng artifact 09/08 đã xác minh**, không tạo dump mới nếu DB không đổi và artifact/source proof khớp.
- Upload vào prefix e-learning/BK1 riêng trên Drive.
- Verify remote + download read-back checksum.
- Nếu checksum artifact upload đúng artifact đã restore thành công vào `cms_elearning_verify`, có thể dùng proof đó + read-back checksum làm restore proof BK1.
- Nếu artifact không khớp proof cũ hoặc DB đã thay đổi sau 09/08: DỪNG A3 và báo; không tự dump/restore MySQL trong lượt này ngoài cơ chế đã duyệt.

Pha A chỉ PASS khi cả A1–A3 đạt hoặc một mục DỪNG có lý do an toàn rõ. Không sửa job định kỳ khi A1/A2 chưa PASS.

## 5. Pha B — cập nhật coverage định kỳ VPS1 sau proof

Chỉ khi A1 + A2 PASS.

### B1 · `incomex_metadata`
Ưu tiên sửa **script/job hiện hữu**, không tạo job/service mới:
- local backup hằng ngày cùng lớp `pg-backup.sh`, retention tương tự `directus`, nhưng file/prefix tách rõ DB;
- Drive encrypted backup cùng lượt `backup-to-gdrive.sh`;
- không đổi backup `directus` hiện hữu ngoài phần tối thiểu để thêm DB;
- fail-closed: dump/upload verify fail ⇒ không đánh dấu lượt PASS và không tỉa artifact mới.

### B2 · `/opt/incomex/data`
- thêm vào **gói config/data encrypted hiện hữu** nếu semantics phù hợp; nếu gói hiện hữu không phù hợp thì thêm artifact thứ ba trong cùng script/job, không tạo cron mới;
- retention cùng bộ timestamp, nhưng không để một artifact lỗi làm xóa bản tốt cũ;
- upload verify trước retention.

### B3 · retention
- Trước apply: chạy dry-run và chứng minh retention chỉ nhắm pattern production hiện hữu + artifact mới đúng schema tên.
- Bản cứu `BK1/...` phải **nằm ngoài retention**.
- Không tỉa thật trong BK1 nếu không cần để chứng minh coverage; ưu tiên để lượt cron thật sau tự thực thi retention.
- Nếu sửa script có test/mô phỏng hiện hữu: chạy test đó. Không dựng framework test mới.

### B4 · e-learning
- BK1 **không tạo recurring job mới trên VPS2**. Chỉ đóng gap offsite hiện tại.
- Lịch/retention e-learning dài hạn sẽ chốt ở hardening sau BK1 cùng persistent binding/MySQL cleanup.

## 6. Postcheck / rollback

Postcheck:
- source business data unchanged;
- Directus/PG/e-learning health như PRE;
- `agent-data`/`claude-mcp` StartedAt/image unchanged;
- containment 3307/8080 vẫn còn;
- Drive có đủ BK1 artifacts + checksum/read-back proof;
- job/script VPS1 syntax + dry-run/test PASS;
- cron/timer schedule không đổi ngoài coverage trong script;
- không có secret trong logs/git/artifacts.

Rollback script:
- lưu exact bytes/hash trước edit;
- nếu B fail, restore script bytes cũ; **không xóa BK1 offsite artifacts**.
- không rollback bản cứu A đã upload vì đó là safety asset.

## 7. XONG / DỪNG

XONG khi:
- `incomex_metadata`: offsite encrypted + read-back + restore proof PASS;
- `/opt/incomex/data`: offsite encrypted + read-back + restore proof PASS;
- e-learning 09/08: offsite Drive + read-back + restore proof provenance PASS;
- recurring VPS1 coverage được cập nhật an toàn cho metadata + data;
- 0 service/container restart; 0 business data mutation;
- B firewall containment vẫn PASS/TEMPORARY;
- báo cáo rõ gap còn lại: e-learning recurring, DOT registry cleanup, IPv6 route, cms_queue, persistent port binding.

DỪNG nếu:
- có active runtime executor/RUN conflict;
- restore cần direct SQL ngoài DOT;
- backup artifact/secret/Drive state mơ hồ;
- read-back/hash không khớp;
- source data/health thay đổi bất thường;
- script rollback không chứng minh được.

## 8. Report

Không tạo repo file mới.

### `view.html` §9
Thêm/cập nhật khối `BK1` một màn hình:
- A1/A2/A3: source → Drive → read-back → restore proof;
- B1/B2 coverage trước→sau;
- PASS/DỪNG + bytes/checksum rút gọn + UTC;
- remaining gaps + NEXT hardening VPS2.

### `COLLAB.md`
- Dòng hiện hành;
- `KQ@VPSUP-BK1-20260928-01 XONG|DỪNG`;
- chỉ thêm Owner blocker nếu thật sự cần quyết định mới.

### Commit
Dùng `fs_transaction` cho `view.html` + `COLLAB.md`:
`[Claude Code] VPSUP-BK1 · backup offsite và restore proof`

Kết thúc Owner đúng một dòng: `XONG` hoặc `DỪNG — <lý do>`.

## 9. Sau BK1 — không làm trong RUN này

Host mới phát hardening VPS2:
- persistent-bind 3307/8080 + firewall bền;
- MySQL account/password/version hardening;
- sửa `cms_queue`;
- xử lý IPv6 route;
- cleanup ≈26 GB;
- swap/RAM;
- cơ chế cờ/lease “VPS đang bận” do máy giữ;
- sau đó clone CURRENT/rehearsal.

Không tự nhảy bước.
