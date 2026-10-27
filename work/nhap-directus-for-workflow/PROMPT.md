# PG-L0 · TIÊU CHÍ 0 / PG-FIRST · CHỨNG MINH CÁC KHẢ NĂNG NATIVE ĐÃ CÓ — G0 CHỈ ĐỌC
RUN_ID: NDW-TS2L0-PGFS-PREFLIGHT-20261027-01
TASK: work/nhap-directus-for-workflow
EXECUTOR_SURFACE: Claude Code CLI
READ_PATH: claude-mcp `query_pg` **chỉ khi đã chứng minh hiện bind và validator/role context_pack_readonly/transaction READ ONLY**, `vps_status`, các DOT/script-wrapper **chỉ đọc** đã audit, workspace/Git read. WRITE_PATH: chỉ ghi STARTED/KQ trong đúng task COLLAB bằng workspace_edit; 0 mutation runtime.
STATUS: G0 READ-ONLY. Chỉ chạy khi Host `READY@<last-touch PROMPT full SHA>` trong COLLAB và Owner gửi đúng 1 câu DROOT38, không STOP_REQUESTED/COUNCIL_ALERT; không cần G1/G2 vì 0 thay đổi production. Nếu nguồn SQL không bind, các hạng mục không lệ thuộc vẫn chạy, kết quả PG_SQL=UNKNOWN và KQ MỘT PHẦN — KHÔNG chuyển sang admin psql/docker exec/REST ad hoc.

## Mục tiêu đã chốt P66/P67 — sử dụng thứ đang có, không sáng tác
PG native trước: pg_catalog/pg_depend/recursive SQL/4 DB/VIEW, tệp DOT-live chỉ nếu PG file privilege/mount an toàn, S4 quyết định và PG queue `SKIP LOCKED`/`NOTIFY` khi nghiệp vụ cần. Directus12.4 Flow/Schema khi PG thiếu phần orchestration. EXT-B giới hạn 5 biên: Kuma/Guard tick, Telegram, Docker RO mount, nginx auth Reports/API, Graph/Cognee cho code-to-PG. RAG/Vector/Qdrant hỗ trợ tìm ngữ nghĩa, không SSOT. Tiêu chí 0: PG? Directus? công cụ hãng? sửa yêu cầu cho phù hợp? cuối cùng mới code (0 code mới mặc định).
Thay đổi mục tiêu được phép: mở báo cáo là đọc sống; N phút giám sát chỉ nếu monitor chứng minh SQL BUSINESS FAIL→đèn RED, không yêu cầu file push tức thì. Git chỉ ghi lịch sử file đã COMMIT (P60 14/31 ngoài Git), hash cần baseline được duyệt; thiếu baseline/đọc lỗi giữ UNKNOWN.

## S0 — Gate/CÔNG CỤ 0 mutation
Đọc AGENTS → COLLAB root VPS-GHI → task COLLAB Tiêu chí 0/P60–P67/§3.TQ/§3.KH → PROMPT, đúng RUN/READY/STOP/roster và sức khoẻ VPS resources PSI/si/so/Guard. Không giành VPS-GHI vì G0, nếu GitHub/VPS đang nặng thì dừng sớm có biên nhận, không giữ terminal.
**Test query_pg trước S1, tránh dừng lần thứ tư:** kiểm trong tool list *của phiên Claude Code hiện tại* có `query_pg` từ cổng claude-mcp RO đã dùng ở Graph GS-R6D (`context_pack_readonly`, READ ONLY, 0 INSERT), kiểm tool validator/role/bound; chỉ template SELECT catalog/system version/pg_available_extensions và SHOW, giới hạn kết quả, statement_timeout, không dùng hàm user/side effect. Không mở credential, không SELECT nội dung bảng nghiệp vụ. Nếu thiếu query_pg, chỉ thử DOT RO đã xác minh trả được dòng; không có thì `PG_SQL=UNKNOWN`, tiếp tục S2–S4, KQ MỘT PHẦN, không lách DROOT26.

## S1 — PostgreSQL/Directus native qua source RO hợp lệ
Kiểm server_version PG (bằng chứng cũ 18.6), bản Directus đang chạy (bằng chứng VPSUP 12.4.1), pg_catalog/pg_depend/pg_namespace/pg_database, 3 DB còn lại và authentication READ ONLY nếu có; không count(*) bảng lớn, không mở dữ liệu nhạy cảm. Đếm native extensions/availability theo pg_catalog: postgres_fdw/file_fdw/pg_cron, pgvector/trgm/FTS; đã cài vs có thể cài vs chưa có. `pg_boss` kiểm lịch sử worker Node/bảng PG thật, không gọi PG core tự xử lý callback. Directus Flows bản ghi 7 từ phiếu Mac 11/09 chỉ lịch sử, xác minh trong runtime bằng approved RO capability nếu có.

## S2 — Filesystem PG-LIVE & Docker (chỉ xem metadata)
Đọc đúng compose/container PG18 production theo đường RO, không suy từ repo cũ `postgres:16`. Lấy sơ đồ mount/UID/GID/secret paths *đã làm sạch*, phạm vi nhỏ nhất `bin/` + `00-SO-DOT.tsv` nếu tồn tại và thực canonical, symlink/hardlink/special files, size p95/max phục vụ băm 253 DOT theo P60; KHÔNG hash nội dung hàng loạt, không đọc source/secret. Kiểm mô hình PG `pg_read_server_files` có quyền toàn filesystem PG user đọc được (NOLOGIN/SECURITY DEFINER không giới hạn PATH mặc định); cách cô lập, rollback, outage/downtime khi Docker recreate, nguồn file baseline Git chỉ committed. `file_fdw` cho fixed manifest nếu an toàn, không tự biết file mới ngoài manifest. Không CREATE ROLE/FUNCTION/VIEW/EXTENSION, không GRANT hoặc mount/restart.

## S3 — Kuma/Guard và nginx, chính xác tính năng của phiên đang chạy
Kuma: xác minh version live, monitor loại PostgreSQL có custom SQL, role RO/nguồn SQL và có hay không **condition trên GIÁ TRỊ query result**. Upstream issue #7728 (17/08/2026) cho biết query thành công dù trả business-bad thường vẫn xanh. Không gọi E1 PASS nếu chỉ SELECT chạy; cần bằng chứng result→DOWN/RED từ testcase/monitor logic đã tồn tại; nếu không `E1=NOT_PROVEN`, kiểm đường Guard/Kuma-push/HTTP JSON monitor hiện có đã cho kết quả business trạng thái thật, Telegram sender/delivery proof lịch sử. Không đổi monitor, gửi test mới, tạo alert hoặc cố tình làm lỗi SQL.
nginx/Nuxt: read-only current nginx location/server/proxy cho `/reports`, `/api/reports`, `/api/reports/live`, alias/đường trực tiếp origin; auth_basic và existing htpasswd có hay không (chỉ đọc path/perms, không giá trị hash), HTTPS, route exempt cho public, app backend bảo vệ hay chưa; P52 unauth status200 là blocker. Không `nginx -s reload`, không tạo htpasswd, không đổi auth. Kết luận chỉ `P0_OPEN | PATH_COVERAGE_UNKNOWN | READY_FOR_SEPARATE_SECURITY_G2`, không tuyên đã sửa.

## S4 — Graph/RAG/Vector/Directus Flow dùng lại & ma trận Hai Nhóm
Chỉ đọc chứng cứ hiện có của Graph index (hiện PARTIAL/key thiếu DB), Cognee code graph, Qdrant/RAG semantic, Directus Flows, pg-boss. Phân loại `PG_NATIVE_NOW | PG_NATIVE_WITH_SAFE_BOUNDARY | EXISTING_EXTERNAL_PROVEN | EXTERNAL_UNVERIFIED | UNKNOWN` cho 5 E1–E5, nêu WHY_NOT_PG khi thật sự ngoài. Không xây vector store, graph reader, bot, queue, cron mới. PG-A1 catalog 4DB đi trước độc lập PG-L1 file mount/Graph; PG-L1 chỉ sau L0 chứng minh role file đủ an toàn và Owner G1/G2.

## S5 — KQ, không triển khai production
Ghi mục P kế tiếp, một bảng gọn S0–S4 PASS/FAIL/UNKNOWN với nguồn và mốc, nhận xét `query_pg` có bind/RO không, PG18/Directus/Kuma exact versions, 5 EXT-B tool thực và hậu quả nếu thiếu, quyền file nguy hiểm, mô hình mount/backup, 0 ghi runtime/0 cờ/0 process/temp. NEXT_TRIGGER=GPT_HOST_NGHIEM_THU_PG_L0. KQ XONG có giới hạn khi trả lời đủ capability matrix; KQ MỘT PHẦN nếu SQL tool không sẵn hay E1 result chưa chứng minh; không giả PASS, không tự chạy L1/TS3.

## Bảng bước DROOT48 (một executor, không chờ bất kỳ người nào trong RUN)
| Bước | Ai | Trigger / hạn | Chứng cứ | Nếu lỗi ai biết / bước kế |
| S0 | Claude Code | Owner dispatch, ≤3′ | Gates/RO gateway | Không bound SQL → UNKNOWN, tiếp S2; STOP thật → KQ DỪNG |
| S1 | Claude Code | S0, ≤5′ | PG/Directus/extensions/Flows | Thiếu nguồn RO → UNKNOWN, S2 |
| S2 | Claude Code | S1, ≤6′ | compose/mount/size/privileges | Security risk → mark BLOCKED_FOR_L1, S3 |
| S3 | Claude Code | S2, ≤6′ | Kuma result condition / nginx paths | Status không chứng minh → UNKNOWN/P0, S4 |
| S4-S5 | Claude Code | S3, ≤7′ | 2 nhóm/5 E + KQ repo | Agent dừng sạch, Host xét L1 |
Hard stop 30′; tránh cạnh tranh GH, giới hạn truy vấn nhỏ và không quét mã/tệp hàng loạt. Owner chỉ giao một câu DROOT38 khi tới lượt; không tạo thời gian chờ nền.

REFERENCES PG18 https://www.postgresql.org/docs/18/functions-admin.html ; https://www.postgresql.org/docs/18/file-fdw.html ; Kuma issue https://github.com/louislam/uptime-kuma/issues/7728 ; Nginx https://nginx.org/en/docs/http/ngx_http_auth_basic_module.html ; pg-boss https://github.com/timgit/pg-boss .