# GSM Access Audit — đề bài kỹ thuật

## 1. Vì sao mở việc này

Owner muốn loại mọi cơ chế gọi Google Secret Manager (GSM) vô lý, dù chi phí tuyệt đối nhỏ. Mục tiêu là giảm phụ thuộc Google, quota/latency/rủi ro và chi phí nếu access calls thực sự vượt free tier.

**Không được nhầm:** báo cáo Billing gần nhất cho project `github-chatgpt-ggcloud` đang quy chi phí nhìn thấy vào SKU **Secret version replica storage**. Vì vậy audit call frequency là một bài toán kiến trúc/vận hành trước; nó chỉ giảm trực tiếp hóa đơn khi access operations thực sự vượt free tier hoặc kéo theo SKU khác.

## 2. Câu hỏi audit

Tạo ma trận:

| Caller | Secret | API/cách gọi | Trigger | Tần suất | Burst | Version ref | Có thể cache? | Lý do |
|---|---|---|---|---:|---:|---|---|---|

Phải phủ:
- app/service trên VPS;
- systemd;
- cron;
- Docker/container entrypoint;
- gateway/MCP/agent;
- health check;
- backup/deploy/update scripts;
- tool chạy tay nhưng lặp thường xuyên;
- mọi wrapper gọi `gcloud secrets versions access`, GSM REST/gRPC hoặc client library.

## 3. Cách đo — ưu tiên không mutation

1. **Static search:** tìm GSM API/client/wrapper và secret resource names trong code/config.
2. **Runtime mapping:** map process/container/unit/cron → script/binary → secret call.
3. **Existing evidence:** dùng log/metric/Billing/Audit log đã có; không bật logging mới có thể phát sinh chi phí nếu chưa được duyệt.
4. **Call-rate reconstruction:** từ cron cadence, request path, loop/retry và process restart frequency.
5. Nếu chưa đủ để định lượng, đề xuất một instrumentation nhỏ ở lượt sau; không tự cài trong GSM.1.

## 4. Kiến trúc mục tiêu — chưa phải quyết định triển khai

Ưu tiên từ đơn giản đến phức tạp:

### A. Startup fetch + in-memory cache
Phù hợp khi secret chỉ cần lúc service khởi động. Pin version cụ thể. Rotation qua deploy/restart có kiểm soát.

### B. In-memory TTL refresh
Cho process sống dài cần nhận rotation mà không restart. TTL chỉ đặt sau khi biết yêu cầu rotation. 1h/6h/24h là các phương án cần đánh giá, không phải mặc định.

### C. Event/reload có kiểm soát
Khi rotate secret, gửi reload/restart cho đúng service; tránh polling GSM liên tục.

### D. Local broker/cache
Chỉ khi nhiều process cùng đọc cùng secret và tổng call thực sự đáng kể. Tránh dựng thêm service nếu A/B đủ.

**Không mặc định env/file cache.** Google cảnh báo file system và environment variables có thể làm tăng nguy cơ lộ secret; nếu dùng phải nêu threat model và biện pháp che log/debug.

## 5. Tiêu chí thiết kế

Với từng caller phải chốt:
- max calls/day;
- max stale time của secret;
- behavior khi GSM unavailable;
- startup failure policy;
- rotation procedure;
- rollback;
- cách tránh thundering herd khi nhiều process restart;
- cách đo trước/sau.

## 6. Baseline giá và best practice

Nguồn chính thức:
- Pricing: https://cloud.google.com/secret-manager/pricing
  - 10.000 access operations/tháng đầu miễn phí;
  - active secret versions tính riêng;
  - destroyed versions không tính storage.
- Best practices: https://docs.cloud.google.com/secret-manager/docs/best-practices
  - ưu tiên pin version cụ thể;
  - workload thường đọc secret lúc startup;
  - không mặc định đưa secret vào file/env nếu không cần.

## 7. Deliverable vòng audit

Không cần tài liệu dài. Kết quả GSM.1–GSM.3 gom vào **§8 của file này** (chi tiết + bằng chứng) và `view.html` (màn hình Owner):
- top callers;
- calls/month hiện tại;
- root cause của call thừa;
- target call budget;
- phương án ít thay đổi nhất;
- tác động chi phí;
- rủi ro/rollback.

Không tạo thêm file progress/archive nếu không cần.

## 8. Kết quả GSM-A1 — khung cố định (agent điền, giữ nguyên tiêu đề 8.1–8.7)

Trạng thái: **XONG (agent) · chờ Host nghiệm thu** · RUN_ID `GSM-A1-20260922-01` · Claude Code CLI trên Mac · đo 2026-09-23 03:18–03:45 UTC · đề bài: `PROMPT.md`

Cửa sổ chuẩn: **30 ngày = 24/08–22/09/2026 (UTC)**; metric Google còn giữ 42 ngày (12/08–22/09). Nguồn: (A) metric `serviceruntime…/api/request_count` của `secretmanager.googleapis.com`, gộp theo method + tài khoản + mã lỗi; (B) log lệnh của gcloud CLI (mỗi lệnh một file, giữ 30 ngày) trên VPS và Mac — chỉ đếm tên lệnh + tên secret, không đọc giá trị — cộng mã/unit/cron/timer. Không lệnh nào đọc nội dung secret; không đổi gì ở VPS/Google/Mac.

### 8.1 Cho Owner (≤ 6 dòng)
- Tổng lượt Access/tháng · so với 10.000 miễn phí · tiền do lượt gọi: **167 lượt/30 ngày** (366/42 ngày) = **1,7 %** hạn miễn phí → **0 USD**.
- Tiền do lưu trữ version: **41 version tính tiền** (40 enabled + 1 disabled) − 6 miễn phí = 35 × 0,06 ≈ **2,10 USD/tháng** — đây là toàn bộ khoản ~2 USD của D02.
- Top 3 caller: (1) Mac — Claude Desktop MCP `lark-crud-gateway` lấy token mỗi lần khởi chạy ≈ **111** (66 %); (2) helper MCP khởi động lại lúc deploy 17–21/09: **16**; (3) cổng JEV khởi động lúc dựng 21/09: **12**.
- Có "rỉ máu" không, ở đâu: **Không.** Không caller nào gọi mỗi request / mỗi vòng health / cron ngắn; `jev-gw-health` 5 phút **không** gọi GSM; lỗi 4xx chỉ 2 lượt/42 ngày. Ở trạng thái không deploy: VPS ≈ 2 lượt/tuần (backup Lark), Mac ≈ 3–4 lượt/ngày.
- Đề xuất chính (một câu): giữ nguyên đường gọi trên VPS; tiền chỉ giảm được bằng dọn kho version (tối đa 2,10 → ≈ 0,72 USD/tháng nếu Owner duyệt huỷ 23 version không ai đọc 42 ngày), còn launcher Lark trên Mac gộp vào việc `work/mcp-token-argv`.

### 8.2 Ma trận caller
| # | Caller | Secret | Kích hoạt | Lượt/ngày (đo · ước) | Nguồn số | Màu | GSM sập thì sao |
|---|---|---|---|---:|---|---|---|
| 1 | `incomex-mcp-helper.service` → `ExecStartPre=+` `incomex-mcp-helper-key-fetch` (VPS) | MCP_WORKSPACE_GH_DEPLOY_KEY | mỗi lần unit khởi động · `Restart=on-failure` 5s · NRestarts=0 | đo 0,53 (16/30 ngày, toàn bộ 17–21/09 lúc deploy) · ổn định ≈ 0 | log gcloud VPS · `systemctl show` | xanh | unit không lên (fail-closed); tiến trình đang chạy không ảnh hưởng |
| 2 | Hermes: `hermes-key.service` + `hermes-telegram-key.service` (oneshot lúc boot, thử lại 12×15s) → `hermes-key-fetch` (+ `get-openrouter-key`), `hermes-telegram-key-fetch` | openrouter-api-key-main, QDRANT_LOCAL_API_KEY, AGENT_DATA_API_KEY, hermes-telegram-bot-token | boot / khởi động lại unit | đo 0,13 (4 = một lần khởi động 21/09) | log gcloud VPS · NRestarts=0 | xanh | Hermes không lên sau ≈ 3 phút thử; đang chạy thì dùng bản đã nạp ở `/run/hermes` |
| 3 | `jev-gw.service` → `ExecStartPre=+` `jev-gw-key-fetch gw` | openrouter-api-key-main, jev-mcp-path-secret | mỗi lần unit khởi động · NRestarts=0 | đo 0,40 (12 = 6 lần khởi động ngày dựng 21/09) · ổn định ≈ 0 | log gcloud VPS | xanh | cổng JEV không lên (fail-closed) |
| 4 | `jev-gw-health.timer` 5 phút → `jev-gw-key-fetch health` + `jev-gw-health` | — **không gọi GSM** (nhánh `health` chỉ đọc token Kuma + `/run/jev/servers.json`) | 288 vòng/ngày | đo 0 | mã + log gcloud | xanh | không phụ thuộc GSM |
| 5 | `lark_client/core.py` `_gsm_get` | LARK_APP_ID, LARK_APP_SECRET | chỉ khi thiếu cả env lẫn `docker/.env` | đo 0 | `docker/.env` có đủ 2 biến (`grep -c` = 1/1) | x | — |
| 6 | `lark-mcp-remote.service` → `factory._resolve_gpg_backup` (opt-in `LARK_BACKUP_GPG_PUBKEY_GSM` **đang bật** trong env của unit) | LARK_BACKUP_GPG_PUBKEY (khoá **công khai**) | khi dựng service ghi (lười) | đo 0,03 (1 lượt 02/09) | log gcloud VPS | xanh | thao tác ghi Lark fail-closed (thiếu khoá mã hoá backup) |
| 7 | `s177-lark-backup.timer` (Thứ Hai + Thứ Năm 03:15 UTC) → `s177-lark-backup-daily` `fetch_lark_creds` | LARK_APP_ID, LARK_APP_SECRET | chỉ khi `backup-check` thấy chưa có manifest mới → thực tế mỗi Thứ Hai | đo 0,33 (10 = 5 tuần × 2) | log gcloud VPS + journal timer | xanh | lượt backup đó dừng (fatal), lượt sau chạy lại |
| 8 | `dot/bin/dot-{env-restore,pg-restore-verify,e2e-test,schema-apply,…}` | nhiều | chỉ chạy tay; không cron/timer nào gọi | đo 0 | crontab root/incomex + timers | x | — |
| 9 | `tools/save_report.sh`, `tools/move_document.sh` | AGENT_DATA_API_KEY | khi env thiếu | đo 0 | log gcloud VPS | x | — |
| 10 | integrity `watchdog-monitor.sh` / `cron-integrity.sh` (bản cron đang gọi) | — | hằng giờ / 6 giờ | đo 0 | bản đang chạy: 0 lệnh GSM | x | — |
| 11 | `git-push-gh-daily.sh` v1 | gh_pat_sync_secrets | không lịch; cron gọi v2 (0 lệnh GSM) | đo 0 | crontab | x | — |
| 12 | Cloud Functions/Run/terraform cũ | — | — | đo 0 | metric A chỉ có 2 tài khoản gọi Access, cả hai đã khớp B | x | — |
| 13a | **Mac — Claude Desktop MCP `lark-crud-gateway` → `~/bin/s177-lark-crud-gateway-mcp`** (`gcloud … access latest` rồi `exec npx mcp-remote`) | S177_LARK_MCP_REMOTE_TOKEN | mỗi lần Desktop khởi chạy server MCP (mở app, phiên mới, reload) — thường cụm 2–3 lượt cùng giây | **đo 3,7** (≈ 111/30 ngày; max 16/ngày) | log gcloud Mac ↔ metric User | vàng | Lark MCP không kết nối trong Desktop/Cowork |
| 13b | Mac — agent/tay khi làm việc (Claude Code, Codex…) | jev-mcp-path-secret (9, trong đó 2 lỗi 4xx ngày 22/09), DIRECTUS_SUPERADMIN_BUNDLE (6) | tay | đo 0,5 (15/30 ngày) | log gcloud Mac | xanh | — |
| 14 | `work/mcp-token-argv/` (đưa Bearer gateway Lark về GSM) | S177_LARK_MCP_REMOTE_TOKEN | lúc đo: chưa thêm caller mới trên VPS (`lark-mcp-remote` chạy liên tục từ 11/09, không có ExecStartPre GSM) | đo 0 | unit + log gcloud VPS | xám | theo dõi: khi xong phải giữ "chỉ lúc khởi động" |
| 15 | Tay/deploy trên VPS (không mã đang chạy nào tham chiếu) | incomex-hvu-b2-webhook | 1 lượt 21/09 lúc dựng HVU-B2 | đo 0,03 | log gcloud VPS | xanh | — |
| **TỔNG** | VPS 44 + Mac 123 (metric) | | | **5,6/ngày** (167/30 ngày) · không deploy ≈ 4/ngày | A ↔ B lệch 1,8 % | | |

### 8.3 Tồn kho version (tiền lưu trữ)
| Secret | Replication | Version tính tiền | Mới nhất | Cũ nhất còn giữ | Còn nơi dùng? | Đề xuất |
|---|---|---:|---|---|---|---|
| jev-mcp-path-secret | automatic | 2 (v2 enabled, v1 **disabled**) | v2 · 21/09 | v1 · 21/09 | v2: `jev-gw` · v1: không | **huỷ v1** (−0,06 USD) |
| S177_LARK_MCP_REMOTE_TOKEN | user-managed · 1 | 1 (v1 đã destroyed) | v2 · 23/05 | v2 | Mac launcher (#13a) | giữ |
| Đang được đọc (10): AGENT_DATA_API_KEY, QDRANT_LOCAL_API_KEY, openrouter-api-key-main, LARK_APP_ID, LARK_APP_SECRET, LARK_BACKUP_GPG_PUBKEY (user-managed · 1, v1 22/05); hermes-telegram-bot-token (auto, 29/07); DIRECTUS_SUPERADMIN_BUNDLE (auto, 24/07); MCP_WORKSPACE_GH_DEPLOY_KEY (auto, 17/09); incomex-hvu-b2-webhook (auto, 21/09) | như cột trái | 10 × 1 | v1 | v1 | có — đo được lượt đọc trong 42 ngày | giữ |
| Dự phòng khẩn cấp, 0 lượt đọc 42 ngày (6): DIRECTUS_BACKUP_GPG_PRIVATEKEY_RECOVERY (19/07), LARK_BACKUP_GPG_PRIVATEKEY_RECOVERY, vps_contabo_id, vps_contabo_secret (22/05); vps2_ssh_key, vps2_root_password (auto, 08/08) | user-managed · 1 / auto | 6 × 1 | v1 | v1 | break-glass — "dùng" không đo được bằng lượt đọc | giữ |
| 0 lượt đọc 42 ngày, không job định kỳ nào đọc từ GSM (22): DIRECTUS_ADMIN_TOKEN, DIRECTUS_KEY, DIRECTUS_SECRET, DIRECTUS_TAC_ADMIN_TOKEN, DIRECTUS_TAC_AGENT_TOKEN, GCS_BUCKET_BACKUP, MCP_KB_CLAUDE_PATH_SECRET, MCP_REMOTE_AUTH_TOKEN, MCP_REMOTE_PATH_SECRET, MCP_UPSTREAM_KEY, MYSQL_ROOT_PASSWORD, OPENAI_API_KEY, PG_DATABASE, PG_HOST, PG_PASSWORD, PG_PORT, PG_USER, POSTGRES_DB, POSTGRES_PASSWORD, POSTGRES_USER, gh_pat_sync_secrets, smtp-password-nmhuyen | user-managed · 1 | 22 × 1 | v1 · 22/05 | v1 · 22/05 | không thấy caller chạy định kỳ; script DR chạy tay `dot-env-restore`/`dot-pg-restore-verify` còn nhắc OPENAI_API_KEY, POSTGRES_DB, POSTGRES_PASSWORD; `mysql-backup.sh` đã `.retired`; MCP_UPSTREAM_KEY chỉ có v1 22/05 trong khi khoá này đã xoay 09/2026 → bản trong GSM có thể đã cũ (không kiểm được vì cấm đọc giá trị) | Owner xét từng cái ở GSM.3 → tối đa −1,32 USD |
| hermes-telegram-permcheck-1785251293 | automatic | 0 (v1 đã destroyed) | — | — | không | xoá secret rỗng (0 USD, chỉ dọn) |
| **TỔNG** | 33 user-managed (1 location) + 8 automatic | **41** (40 enabled + 1 disabled; 2 destroyed không tính) | | | | (41−6)×0,06 ≈ **2,10 USD/tháng** → ≈ 0,72 nếu huỷ 23 |

Chỉ project `github-chatgpt-ggcloud` bật Secret Manager (project còn lại trong tài khoản không bật) → không có kho thứ hai ăn chung phần miễn phí.

### 8.4 Đối chiếu A (metric Google) ↔ B (dựng từ mã)
| Nhãn tài khoản | A: lượt/30 ngày | B: lượt/30 ngày | Lệch | Ghi chú |
|---|---:|---:|---:|---|
| SA-VPS (gcloud của root trên VPS; mọi unit/timer gọi GSM đều chạy bằng root) | 44 | 44 | 0 % | khớp từng ngày; 12–23/08 còn 39 lượt nằm ngoài hạn giữ log gcloud (30 ngày) |
| User-Mac (gcloud tài khoản người dùng trên Mac) | 123 (gồm 2 lỗi 4xx) | 126 | +2,4 % | 6 ngày lệch ±1 lượt (biên ngày / lượt hỏng trước khi tới API); 12–23/08 còn 160 lượt ngoài hạn giữ log (đỉnh 58 lượt ngày 19/08) |
| Khác | 0 | 0 | — | metric chỉ có đúng 2 tài khoản gọi Access |
| **TỔNG** | **167** | **170** | +1,8 % | < 20 % → không còn CALLER CHƯA RÕ |

Lượt quản trị (List/Get/Create/Add/Disable, không tính Access) 42 ngày: 85, gần hết do các việc dựng JEV/HVU và audit.

### 8.5 Trả lời 8 câu bắt buộc (COLLAB)
1. **Caller thực tế:** VPS — `incomex-mcp-helper`, Hermes (2 unit oneshot), `jev-gw`, `lark-mcp-remote` (khoá GPG công khai), `s177-lark-backup`; tất cả chỉ lúc khởi động/lúc chạy job. Mac — launcher MCP Lark của Claude Desktop + agent/tay. Các mục #5, #8–#12 còn mã nhưng không chạy.
2. **Có gọi mỗi request / health / cron ngắn không:** Không. `jev-gw-health` (5 phút) không gọi GSM; integrity hằng giờ đã sạch; nhánh dự phòng Lark không chạy vì `.env` đủ biến. Gần nhất với "lặp" là launcher Mac: mỗi lần Desktop khởi chạy server MCP.
3. **Secret đọc nhiều nhất:** S177_LARK_MCP_REMOTE_TOKEN ≈ 111/30 ngày (3,7/ngày, max 16/ngày, cụm 2–3 lượt cùng giây). VPS: MCP_WORKSPACE_GH_DEPLOY_KEY 16, openrouter-api-key-main 9 — đều dồn vào ngày deploy.
4. **Chỉ startup / cần refresh:** mọi caller VPS là startup-only (ExecStartPre hoặc oneshot boot) hoặc theo job ngắn (backup Lark). Không tiến trình sống dài nào cần refresh giữa vòng đời.
5. **Rotation:** 100 % caller dùng `latest`, không pin; không secret nào có lịch rotation. Xoay = thêm version + khởi động lại unit (vd jev-mcp-path-secret 21/09: v2 mới, v1 để disabled — vẫn tính tiền).
6. **Cache 1h/6h/24h/startup-only:** VPS đã là startup-only (giữ trong RAM hoặc tmpfs `/run`) → GSM sập chỉ chặn lần khởi động/job kế tiếp (unit fail-closed; Hermes thử 12×15s; backup Lark bỏ một lượt), dịch vụ đang chạy không ảnh hưởng. TTL chỉ có ý nghĩa với launcher Mac: cache 24h giảm ~3,7 → ≤ 1–2 lượt/ngày, đổi lại khoá cũ tối đa 24h sau khi xoay và phải có chỗ cất (Keychain) — xem 8.6.
7. **Có vượt 10.000/tháng không:** Không — 167/30 ngày (1,7 %). Khoản ~2 USD là lưu trữ: 41 version tính tiền − 6 miễn phí = 35 × 0,06 ≈ 2,10 USD.
8. **Trần hợp lý:** VPS ≤ 10 lượt/tháng khi không deploy (backup Lark 8–10) + đúng số secret × số lần khởi động unit; Mac launcher ≤ 5/ngày (≤ 2/ngày nếu cache); **trần báo động toàn hệ ≤ 1.000/tháng** (10 % miễn phí) hoặc > 60 lượt/ngày từ một tài khoản.

### 8.6 Nháp GSM.3 (chưa làm)
- **VPS (#1, #2, #3, #7) — giữ nguyên.** Đã đúng README §4A (khởi động mới lấy, giữ trong RAM/tmpfs). Có thể pin version thay `latest` theo best practice, nhưng mỗi lần xoay phải sửa unit/script → chỉ làm nếu Owner muốn quy trình xoay chặt; trần: như 8.5 câu 8.
- **#6 khoá GPG công khai của backup Lark:** là khoá công khai, không phải bí mật → có thể nạp một lần ra file qua `LARK_BACKUP_GPG_PUBKEY_PATH`/`_FPR` (factory đã hỗ trợ) để bỏ phụ thuộc GSM khi dựng service ghi; lợi ích nhỏ (≈ 1 lượt/tháng) nhưng bớt một điểm fail-closed. Rollback: bật lại opt-in `_GSM`.
- **#13a launcher Lark trên Mac (vàng):** gộp vào `work/mcp-token-argv` (việc đó đang sửa chính đường token này). Phương án ít thay đổi nhất: cache token trong macOS Keychain (mã hoá theo user, không file/env) với TTL 24h, hết hạn hoặc 401 thì lấy lại từ GSM; trần ≤ 2/ngày; khoá cũ tối đa 24h; rollback = trả bản script cũ. Nếu không làm: chi phí vẫn 0 USD.
- **Kho version:** huỷ jev-mcp-path-secret v1 (−0,06); Owner xét 22 secret "0 lượt đọc" ở 8.3 → nếu huỷ hết: 41 → 18 version, ≈ 2,10 → **0,72 USD/tháng**. Vì destroy không đảo ngược: disable trước ≥ 30 ngày, theo dõi lỗi, rồi mới destroy; kiểm riêng DR (`dot-env-restore`, `dot-pg-restore-verify`) trước khi đụng OPENAI_API_KEY / POSTGRES_*. Xoá secret rỗng `hermes-telegram-permcheck-…` (0 USD).
- **Đo trước/sau (GSM.5):** đọc lại cùng metric request_count (miễn phí) theo tài khoản + đếm log gcloud hai phía, 7 ngày sau thay đổi.
- **Ghi nhận ngoài phạm vi:** mỗi vòng `jev-gw-health` (5 phút) gọi `tools/call evaluate` qua cổng JEV → OpenRouter, tức ≈ 288 lượt gọi model trả phí/ngày chỉ để kiểm sức khoẻ — chuyển cho `work/jev-integration/` xem xét.

### 8.7 Chưa đo được + lý do
- 12–23/08: 199 lượt (Mac 160, VPS 39) chỉ có trong metric; log gcloud hai phía chỉ giữ 30 ngày nên không gán được caller. Đỉnh 42 ngày (58 lượt, 19/08) nằm trong khoảng này.
- Danh tính gcloud trên VPS không kiểm trực tiếp (lệnh liệt kê tài khoản bị bộ phân loại quyền chặn); gán SA-VPS dựa trên khớp 44 = 44 từng ngày giữa log gcloud root và metric.
- Entrypoint/Cmd container không đọc (`docker inspect` bị chặn); bù bằng đối chiếu A: không có tài khoản thứ ba gọi Access.
- Log gcloud của user `hermes` chỉ có 29/07 (ngoài cửa sổ); Hermes hiện lấy khoá qua unit chạy bằng root.
- Bảng giá không đọc lại trực tuyến; dùng baseline trong COLLAB (10.000 lượt miễn phí; 6 version miễn phí; 0,06 USD/version/location/tháng) — tổng tính ra khớp ~2 USD của D02.
- Chưa kiểm giá trị MCP_UPSTREAM_KEY trong GSM có còn khớp khoá đang chạy không (cấm đọc giá trị trong vòng này).
