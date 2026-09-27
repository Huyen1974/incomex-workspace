# PROMPT — VPSUP G0 · khảo sát chỉ đọc VPS1 + VPS2 + Google Drive

RUN_ID: VPSUP-G0-20260927-01
STATUS: Chỉ thực thi sau khi COLLAB có READY đúng SHA commit cuối chạm file này và Owner/GPT Host phát RUN.
Host: GPT Chat · GPT-VPSUP-20260926-A
Executor_Surface: Claude Code CLI trên Mac Owner.
Report_Write_Path: **fs_* / Incomex VPS MCP · root gh → incomex-workspace/main**.
Runtime_Read_Path: SSH/read-only VPS1/VPS2 + rclone read-only + Contabo API GET + nguồn chính thức web/GitHub.
Không có Write_Path dự phòng. Không bind được fs_* ⇒ DỪNG trước mọi việc.

## 0. Read gate

1. Gọi đúng một read-gate: fs_stat work/vps1-up-grade/COLLAB.md.
2. Đọc: AGENTS.md → COLLAB.md (§0, D14–D18, P06–P09) → PROMPT.md → view.html §5–§9.
3. Kiểm READY@<40hex> trong COLLAB phải đúng commit cuối chạm PROMPT.md. Sai/missing ⇒ DỪNG.
4. Runtime VPS là nguồn hiện trạng chuẩn; repo/backup chỉ tham chiếu.

## 1. Mục tiêu duy nhất

Chụp hiện trạng **chỉ đọc** của VPS1, VPS2 và Google Drive đủ để Host lập bước 3–10:
- version/image/digest/dependency;
- Directus/PostgreSQL quyền thực;
- backup coverage + restore evidence;
- route/caller/side-effect;
- dung lượng và năng lực VPS2 làm rehearsal lab;
- Contabo snapshot/backup capability;
- cơ chế licensing Directus 12 từ source chính thức;
- blocker/risk cần xử lý trước clone/cutover.

Không sửa lỗi, cleanup, install, restart, nâng cấp hay fault injection.

## 2. Đường vào máy

### VPS1
Dùng SSH alias hiện hữu của Owner. Không tạo/sửa alias, key, SSH config.

### VPS2
Chỉ dùng đường SSH/secret-loader đã tồn tại và đã audit.
Nếu cần GSM: chỉ nạp secret tạm vào process/ssh-agent bằng cơ chế hiện hữu; không in giá trị, không ghi key ra đĩa, không tạo credential mới.
Không suy VPS2 IP từ DNS nếu domain có thể qua proxy/CDN.
Không xác định được đường vào an toàn ⇒ VPS2 = ⚪ CHƯA ĐO, tiếp tục phần khác.

## 3. Luật cứng — G0 thật sự read-only

### Cấm trên VPS1/VPS2
- restart/stop/start/kill/reload;
- docker pull/run/compose up/down/rm/prune; docker exec lệnh ghi;
- apt/npm/pip install/update;
- tạo/sửa/xóa file/thư mục; mkdir/touch/cp/mv; redirect > hoặc tee;
- chmod/chown; sửa cron/systemd/nginx/DNS/firewall;
- POST/PATCH/PUT/DELETE tới Directus/Kuma/Contabo/Drive/API ngoài;
- rclone copy/sync/move/delete/mkdir;
- pg_dump/mysqldump/restore/snapshot;
- fault injection;
- đăng ký/kích hoạt/deactivate license;
- đổi clock/token/PUBLIC_URL/key/policy.

**Không tạo hồ sơ/evidence file trên VPS1 hoặc VPS2.**

### Được
- lệnh hệ thống chỉ đọc;
- docker inspect/ps/system df; docker exec chỉ version/GET/SQL READ ONLY;
- HTTP GET/HEAD;
- Contabo API GET;
- rclone lsf/lsjson/size/about;
- đọc source/config đã tồn tại, không in secret;
- DB transaction READ ONLY.

### Dữ liệu/secret
- Không xuất record nghiệp vụ/cá nhân; chỉ metadata/count/size/name.
- Không in email user Directus; chỉ tổng theo nhóm.
- Không in token/password/key/cookie/private key/secret.
- Env chỉ ghi tên + có/không, trừ giá trị cấu hình không bí mật được yêu cầu rõ.
- Phép đo nào buộc phải copy DB/file trên VPS ⇒ không làm, ghi ⚪.

### SQL
Mỗi phiên: BEGIN READ ONLY; SET LOCAL statement_timeout='10s'; ...; ROLLBACK.

### Tải
du/find chỉ khi cần: nice -n 19 ionice -c3, -xdev, timeout hợp lý.
Load 1 phút VPS1 >4 ⇒ bỏ/hoãn phần nặng; không chờ vô hạn.

### Dấu hiệu an ninh
Nếu thấy admin/Studio lạ, cron/process lạ gọi ra ngoài, dấu hiệu compromise hoặc nguy cơ lộ secret:
DỪNG phần liên quan, ghi 🔴 bằng chứng tối thiểu đã che, không tự xử lý.

## 4. Nội dung đo A–J

Mọi số liệu có UTC + nguồn/lệnh đo. Không đo được ⇒ ⚪ + lý do. Không lấy số lịch sử thay live.

### A · Version/drift — VPS1 + VPS2
Mỗi container/service quan trọng:
- name, image tag, image ID/digest/RepoDigest;
- version chạy thật: PG, Directus, Nuxt/Nitro+Node, Qdrant, nginx;
- Docker Engine/Compose, OS/kernel;
- service Incomex ngoài Docker;
- cron mọi user, /etc/cron.d, systemd timers.
Đánh dấu tag trôi và cơ chế có thể pull/recreate image. Không suy restart Docker tự pull.

### B · Directus — VPS1
Chỉ metadata:
- user tổng theo Studio/admin/API-only/inactive, không email/token;
- policy App/Admin Access; tài khoản máy có Studio hay không;
- collections, flows active/trigger, operations/exec, extensions + host range;
- Public role permission counts và write có/không;
- cấu hình không bí mật: WEBSOCKETS_ENABLED, GraphQL enable nếu có, PUBLIC_URL, IP_TRUST_PROXY, tên DB_POOL keys, CACHE enable/store type, STORAGE_LOCATIONS, email transport type;
- nginx route Upgrade/WebSocket;
- PostGIS có/không;
- advisory Directus Critical/High 2026: ÁP DỤNG / KHÔNG ÁP DỤNG / CHƯA ĐỦ BẰNG CHỨNG theo cấu hình thật.
Không gọi advisory là bằng chứng đã bị khai thác.

### C · PostgreSQL — VPS1
- danh sách DB + size;
- mỗi DB: số table/schema chính, 10 bảng lớn nhất, extensions;
- roles: rolsuper/rolbypassrls/rolcanlogin; role Directus/agent-data/gateway bằng tên/config ref, không secret;
- RLS enabled tables, policy count, owner bảng nghiệp vụ;
- connection counts theo usename/application_name/datname.
Riêng directus_gov_test_20260602: phân loại LIVE / TEST-DERIVED / UNKNOWN bằng usage metadata, xact counters nhiều mẫu và runtime references; không đụng DB.

### D · Backup + Google Drive — trọng điểm
Inventory mọi backup job: script, schedule, DB/path, retention, encryption, GPG recipient count, last-success evidence.

Lập bảng:
DB | vai trò BUSINESS/CONFIG/TEST-DERIVED/DEFAULT/UNKNOWN | cần backup? | local coverage | Drive coverage | restore proof/date.

**Xác nhận/bác bỏ F6:** pg-backup.sh và backup-to-gdrive.sh có chỉ dump DB directus không; incomex_metadata/workflow có ở backup khác không.
Không yêu cầu backup mọi DB chỉ vì DB tồn tại.

Kiểm thêm Qdrant snapshot/backup, uploads/files, source/runtime config DR, nginx/TLS, VPS2 e-learning backup.

Drive chỉ read: lsf/lsjson/size/about; số bộ, newest, size, free/quota khi provider hỗ trợ; restore evidence hiện có.

### E · Route + caller
- nginx live host × location × upstream;
- Nuxt routes/pages; giaoduc.* ↔ e-learning;
- Kuma monitor: name/type/target + notification type. Nếu live DB chỉ đọc trực tiếp an toàn được thì đọc; nếu cần copy file ⇒ ⚪;
- consumer Directus/PG: container/service/cron/DOT → target → read/write.

### F · Side effects để cách ly clone
Inventory nơi gửi Telegram, ghi GitHub, webhook, mail, Agent Data sync, Drive, API ngoài, Directus schedule/webhook/request Flow.
Mỗi dòng: component · channel · trigger · singleton?
Firewall egress chỉ đọc nếu quyền cho phép.

### G · VPS2 capacity + e-learning
- CPU/RAM/disk/swap; container/service;
- e-learning runtime/web/DB/domain/TLS expiry;
- DB e-learning chỉ size/table counts, không record;
- source/uploads size.
“Sổ nguồn sinh”: filesystem top-level, Docker images/layers/build cache/volumes, logs/journal, backup cũ, tmp/cache, deleted-open files, bind dirs lớn.
Mỗi dòng: bytes + GIỮ / OFFLOAD DRIVE / DỌN ĐƯỢC / CHƯA RÕ + lý do.
So với Owner hypothesis ~3GB, không ép khớp.

### H · Contabo/failure domain
Chỉ API GET:
- plan VPS1/VPS2;
- snapshot limit/current snapshots/Auto Backup;
- region/datacenter nếu có;
- IP/ASN/failure-domain để đánh giá canh chéo độc lập.
Thiếu credential/quyền ⇒ ⚪, không hỏi Owner giữa RUN.

### I · Lab capacity
Từ A–H tính:
- disk/RAM CURRENT clone;
- disk/RAM TARGET rehearsal;
- có cần mang directus_gov_test hay không;
- headroom VPS2;
- một đề xuất: dọn/offload/tạm nâng gói hay không.
Chỉ đề xuất, không làm.

### J · Directus 12 licensing/source
Nguồn chính thức, exact tag 12.3.1 và stable mới nhất lúc G0:
- license/telemetry endpoints/domain nếu source/docs cho biết;
- validation_interval lấy từ đâu;
- entitlement/cache/last-success state ở đâu và monitor hợp lệ thế nào;
- downgrade Core/lock behavior;
- endpoint/capability bị ảnh hưởng theo source/docs, không đoán;
- restart cache semantics;
- DB restore/PUBLIC_URL/binding/activation semantics;
- offline mode thuộc tier nào.

G0 không fault-inject licensing. Không chứng minh được bằng source/docs ⇒ UNKNOWN cho LC lab sau.

## 5. Đầu ra duy nhất

Không tạo report/evidence file mới.

### view.html
Chỉ sửa §9, đúng div#g0-result:
- matrix A–J;
- cột phù hợp VPS1 / VPS2 / Drive / Kết luận;
- 🔴 tắc · 🟡 cảnh báo · 🟢 ổn · ⚪ chưa đo · ✕ N/A;
- tối đa một dòng/ô;
- dưới bảng ≤12 phát hiện đỏ/vàng + đề xuất bước kế tiếp;
- UTC + source note ngắn.
Không sửa section khác.

### COLLAB.md
Chỉ:
- cập nhật Dòng hiện hành;
- thêm đúng một dòng KQ@VPSUP-G0-20260927-01 XONG hoặc DỪNG + tóm tắt ngắn;
- blocker Owner mới thật sự mới đưa một dòng vào Owner cần quyết; không hỏi lại việc đã chốt.

### Commit
- dùng fs_transaction qua Write_Path để sửa view.html + COLLAB.md trong một commit;
- message: [Claude Code] VPSUP-G0 · khảo sát read-only VPS1 VPS2 Drive;
- không tạo file mới;
- kết thúc Owner đúng một dòng: XONG hoặc DỪNG — lý do ngắn.

## 6. XONG / DỪNG

XONG khi:
- A–J đo phần có thể đo;
- UNKNOWN ghi rõ;
- không runtime mutation;
- không lộ secret/data;
- view + COLLAB commit/push đúng Write_Path;
- KQ đúng RUN_ID.

DỪNG toàn RUN nếu:
- read-gate/READY fail;
- cần runtime mutation để tiếp tục;
- compromise/admin lạ;
- sắp lộ secret/data;
- Write_Path không thể report an toàn.

Một nguồn riêng lẻ không đọc được (VPS2/Contabo/Drive) mà không phải safety blocker:
- ghi ⚪ + lý do;
- tiếp tục phần còn lại;
- cuối RUN vẫn có thể XONG theo scope đo được; không biến UNKNOWN thành PASS.
