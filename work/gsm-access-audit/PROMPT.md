# PROMPT — GSM · A1 Audit lượt gọi Google Secret Manager (CHỈ ĐỌC — KHÔNG MUTATION)

RUN_ID: GSM-A1-20260922-01
Soạn: Claude Chat (Host `CC-GSM-0922`), 22/09/2026, từ A0 + D01–D03 + README (GPT mở việc `e112211`) + quét tĩnh của Host trên `/opt/incomex` (§6). Trạng thái chỉ tin `work/gsm-access-audit/COLLAB.md`. Chỉ chạy khi COLLAB có Host `READY@` đúng full SHA commit cuối chạm file này và có lệnh RUN.
**Executor_Surface = Claude Code CLI trên máy Mac**: (a) shell VPS qua SSH — **chỉ lệnh đọc**; (b) `gcloud`/REST Google trên Mac bằng tài khoản đang đăng nhập — **chỉ list/describe/đọc metric**; (c) file cấu hình agent/MCP trên chính máy Mac — chỉ đọc tên file + số dòng khớp. **Write_Path = `workspace_*`**; dự phòng `fs_*`. Cấm git/GitHub native để ghi repo; không clone.
**Phạm vi:** GSM.1 + GSM.2 + nháp GSM.3. Chỉ ghi đúng 3 file: `README.md` §8, `view.html`, `COLLAB.md` (dòng hiện hành + tick kế hoạch + KQ). Không tạo file mới. Không sửa file này.

## 0. Cổng
1. Read-gate qua Write_Path: `AGENTS.md` → `work/gsm-access-audit/COLLAB.md` → file này; `READY@` khớp full SHA commit cuối chạm `PROMPT.md` (không so HEAD); lệch → DỪNG.
2. `gcloud config list`: chỉ để biết đang dùng loại tài khoản nào; mọi lệnh ghi rõ `--project=github-chatgpt-ggcloud`. Thiếu quyền đọc chỗ nào → ghi rõ, KHÔNG xin/cấp quyền, KHÔNG đổi IAM.
3. Ghi mốc bắt đầu (UTC). Việc khác đang chạy trên VPS (vd `work/mcp-token-argv/`, `work/vps-clean-20-9-26/`, `work/jev-integration/`) không chặn vì audit chỉ đọc; nhưng restart/deploy của chúng trong cửa sổ đo có thể làm số lượt gọi phồng lên → ghi lại khi thấy.

## 1. Luật cứng — CHỈ ĐỌC
- **CẤM phía Google:** `secrets versions access` (không đọc nội dung bất kỳ secret nào — audit không cần), `versions add/enable/disable/destroy`, `secrets create/update/delete`, mọi lệnh IAM, `services enable/disable`, bật Audit Logs/Data Access, tạo metric/alert/sink/log bucket, Cloud Shell.
- **CẤM phía VPS/Mac:** `systemctl start/stop/restart/reload/enable/disable/daemon-reload/edit`, `crontab -e/-r`, `launchctl load/unload`, `docker restart/stop/rm/exec/compose`, sửa/tạo/xoá file, cài gói, kill tiến trình, chạy thử bất kỳ script nào có gọi GSM.
- **Được đọc:** `crontab -l -u <mọi user>`, `/etc/cron*`, `/var/spool/cron`, `systemctl list-timers --all`, `systemctl list-units --all`, `systemctl cat <unit>`, `systemctl show -p NRestarts,Restart,RestartUSec,StartLimitBurst,ActiveEnterTimestamp <unit>`, `journalctl -u <unit> --since … | grep -c …`, `docker inspect --format` (chỉ Entrypoint/Cmd/RestartCount/StartedAt; KHÔNG in Env), `grep -rl/-rn/-c` trên mã, `ps -eo pid,etimes,comm` (KHÔNG in args), `~/Library/LaunchAgents` (chỉ tên + lịch).
- **Luật bí mật:** không in giá trị secret/token/khoá ra màn hình, log hay repo. File `.env`/cấu hình chứa bí mật chỉ được `grep -cE '^TÊN_BIẾN=.+'` (in số đếm) để biết nhánh nào đang chạy. Không `env`, `set -x`, `cat` file khoá, không in args tiến trình. Token gọi REST Google đi qua header file/stdin, không nằm trên dòng lệnh, không in.
- **Metric Google:** tối đa 10 lượt đọc Monitoring API, luôn gộp (group by) để số chuỗi trả về nhỏ (chi phí ≈ 0). Lệnh list/describe của Secret Manager là management operation (miễn phí); chúng hiện trong metric với method List*/Get* — không tính vào lượt Access.
- **Repo công khai:** không ghi email, email service account, project number, `credential_id` thô, IP, tên miền nội bộ, output lệnh thô. Tên secret được ghi (không phải giá trị); nếu secret-guard của Write_Path từ chối thì thay bằng mã `S01…` + mô tả ngắn, không lách guard.
- **Thời gian:** mục tiêu ≤ 90 phút. Phần nào không đo được trong ngân sách → ghi `CHƯA ĐO · <lý do>`, làm tiếp phần khác, không bỏ dở báo cáo.

## 2. A — Đo từ trên xuống: ai thật sự gọi GSM (nguồn sự thật chính)
A1. Đọc metric có sẵn `serviceruntime.googleapis.com/api/request_count`, resource `consumed_api`, `resource.label.service = secretmanager.googleapis.com`, cửa sổ dài nhất còn lưu (~42 ngày), căn theo ngày (ALIGN_SUM, 86400s), gộp theo `method` + `credential_id` + `response_code_class`. gcloud không có lệnh list time series ổn định → gọi REST `projects.timeSeries.list`.
A2. Đổi `credential_id` thành nhãn: service account (map uniqueId → tên SA bằng `gcloud iam service-accounts list`), tài khoản người dùng/gcloud trên Mac, khác. Trong repo chỉ ghi nhãn (vd `SA-VPS`, `User-Mac`, `SA-khác-1`).
A3. Cần ra: lượt `AccessSecretVersion`/ngày và tổng 30 ngày theo từng nhãn; ngày cao nhất (burst); tỉ lệ lỗi 4xx/5xx; so với 10.000 lượt/tháng miễn phí.
A4. Metric không đọc được (API chưa bật/thiếu quyền) → KHÔNG bật; ghi `A = CHƯA ĐO · <lý do>` và dựa vào B.
A5. **Tồn kho lưu trữ (nơi tiền thật nằm theo D02):** `gcloud secrets list` (tên, replication, rotation, ngày tạo) + mỗi secret: số version ENABLED và DISABLED (cả hai đều tính tiền), version mới nhất, ngày của version cũ nhất còn giữ. Tính: tổng version tính tiền (automatic = 1 location; user-managed = số location) − 6 miễn phí, × 0,06 USD → so với ~2 USD/tháng của D02. Liệt kê ứng viên huỷ (version cũ không còn nơi nào dùng) — CHỈ ĐỀ XUẤT; huỷ là không đảo ngược, Owner quyết ở lượt sau.
A6. `gcloud projects list`: project nào khác còn bật Secret Manager (chỉ `services list --enabled`, đếm secret/version) — phần miễn phí được cộng chung theo billing account.

## 3. B — Dựng từ dưới lên: đường mã nào gọi, vì sao, bao nhiêu
B1. Xuất phát từ danh sách quét tĩnh của Host ở §6 — xác nhận từng mục ĐANG CHẠY hay CHẾT (có crontab/systemd/timer/container/launchd/script khác gọi tới không). Quét thêm ngoài `/opt/incomex`: `/usr/local/sbin`, `/usr/local/bin`, `/etc/systemd/system`, `/etc/cron*`, `/var/spool/cron`, `/root`, `/home/*`, `/var/lib/hermes`, `/opt/jev`, Entrypoint/Cmd các container; trên Mac: file cấu hình MCP/agent (Claude Desktop, Claude Code, Codex…), `~/Library/LaunchAgents`, script local. Mẫu tìm: `secretmanager`, `secrets versions access`, `access_secret_version`, `AccessSecretVersion`, `SecretManagerServiceClient`, `GoogleSecretManagerSettingsSource`, `key-fetch`, `_gsm_get`.
B2. Mỗi caller ĐANG CHẠY ghi 1 dòng: caller · secret · cách gọi (gcloud/REST/thư viện) · kích hoạt (boot / ExecStartPre / timer / cron / mỗi tiến trình / mỗi request / tay) · nhịp · số secret mỗi lần · `latest` hay pin version · lượt/ngày = số lần kích hoạt/ngày × số secret · bằng chứng (NRestarts kể từ boot, số dòng log thành công/thất bại theo ngày, lịch cron/timer).
B3. Soi riêng 4 chỗ dễ "rỉ máu":
  (a) Unit có `ExecStartPre` lấy khoá + `Restart=always|on-failure`: NRestarts, RestartSec, StartLimit — crash-loop thì mỗi lần khởi động lại là thêm lượt gọi.
  (b) Nhánh dự phòng "env → `.env` → GSM" (vd `lark_client/core.py`, `tools/save_report.sh`, `tools/move_document.sh`, các `dot-*`): biến đã có trong env/`.env` chưa (`grep -c`) → nhánh GSM có thực sự chạy không.
  (c) Health check/timer ngắn — đặc biệt `jev-gw-health.timer` (5 phút/lần): mỗi vòng có lấy khoá từ GSM không, hay đọc bản đã nạp ở `/run`. Ghi thêm (ngoài phạm vi, chỉ ghi nhận): mỗi vòng health có gọi dịch vụ trả phí (model qua OpenRouter) không.
  (d) Lượt lỗi lặp (PERMISSION_DENIED, secret đã xoay/chết) — gọi mà vô ích.
B4. Tài khoản người dùng trên Mac (agent đọc khoá khi làm việc): đếm qua A; không đọc transcript.
B5. Nếu A có nhãn không thuộc VPS/Mac: tìm nguồn chỉ bằng lệnh list — `gcloud run services list`, `gcloud functions list`, `gcloud scheduler jobs list` (mọi region), `gh workflow list` / `gh run list` của repo có bước lấy GSM. Không tắt gì.

## 4. C — Đối chiếu · D — Kết luận · E — Nháp GSM.3
C. Cộng B theo từng nhãn tài khoản, so với A cùng cửa sổ. Lệch > 20% hoặc có nhãn không rõ → đỏ `CALLER CHƯA RÕ`, đào tiếp trong ngân sách; không ra thì để mở và ghi rõ.
D. Trả lời ngắn 8 câu ở COLLAB mục "Câu hỏi bắt buộc". Phân loại từng caller theo màu chuẩn của view: **xanh** = cần (chỉ lúc khởi động, hợp lý) · **vàng** = giảm được · **đỏ** = thừa/vô ích (dự phòng chạy vì thiếu biến, khoá chết, mỗi request, vòng health, crash-loop) · **x** = chết (mã còn nhưng không ai gọi) · **xám** = chưa đo. Mỗi caller ghi thêm: GSM sập thì dịch vụ ra sao (không khởi động được / chạy tiếp bằng bản đã nạp).
E. Nháp GSM.3 (KHÔNG làm): mỗi caller vàng/đỏ một phương án ít thay đổi nhất + trần lượt/ngày + thời gian cũ tối đa của khoá + rủi ro/rollback; kho lưu trữ: số version đề xuất huỷ + tiền/tháng trước/sau. Mặc định theo README §4A (khởi động mới lấy + giữ trong RAM hoặc bản nạp tmpfs sẵn có); không đề xuất env/file mới nếu chưa nêu threat model.

## 5. Báo cáo — đúng 3 file, 1 commit nếu Write_Path có transaction
- `README.md` §8: điền vào khung Host đã dựng, giữ nguyên tiêu đề mục 8.1–8.7; sửa dòng `Trạng thái:` của §8.
- `view.html`: điền các ô ma trận + bảng Tiền (đổi class màu `xanh/vang/do/x/xam`, thêm dòng nếu có caller mới, dòng TỔNG cộng từ dưới lên); khối "Hôm nay anh cần quyết": mỗi dòng một câu hỏi kèm đề xuất PM để anh gật/lắc (không có thì ghi "Không có"); thanh tiến độ: ô 1–2 `xong`, ô 3 `dang`; dòng trạng thái đầu trang.
- `COLLAB.md`: tick GSM.1/GSM.2, sửa dòng hiện hành; thêm đúng một dòng `KQ@GSM-A1-20260922-01 XONG` hoặc `KQ@GSM-A1-20260922-01 DỪNG · <bước> · <lý do>` vào mục "Giao Agent". Không có transaction → sửa README + view trước, COLLAB sau với `Áp: <hash>`.
- Trả Owner đúng một dòng: `XONG · GSM-A1 · Access <n>/tháng (miễn phí 10.000) · lưu trữ <v> version ≈ <x> USD/tháng · top: <caller1>, <caller2> · rỉ máu: <có: chỗ nào | không> · xem README §8` hoặc `DỪNG · GSM-A1 · <bước> · <lý do>`.

## 6. Quét tĩnh của Host (22/09 · chỉ `/opt/incomex` qua đầu nối đọc · CHƯA xác nhận runtime)
**Nền đã có — đọc trước:** báo cáo 24/07/2026 trong `/opt/incomex/docker/agent-data-repo/knowledge/current-state/reports/`: `integrity-sm-fallback-r0-2026-07-24.md` và `directus-dual-superadmin-owner-ready-2026-07-24.md` §11. Lúc đó đo được: lượt đọc GSM khi chạy bình thường = 0, sau khi gỡ nhánh dự phòng của 2 script integrity (trước đó 28 lượt/ngày tới một khoá đã chết). Mọi mục dưới đây là thứ cần kiểm lại hoặc mới xuất hiện sau mốc đó. Danh sách là điểm xuất phát, không phải giới hạn — tìm thấy caller mới thì thêm dòng.

| # | Caller (đường dẫn) | Secret | Kích hoạt dự đoán | Cần xác nhận |
|---|---|---|---|---|
| 1 | `/usr/local/sbin/incomex-mcp-helper-key-fetch` ← `ExecStartPre=+` của `incomex-mcp-helper.service` | deploy key repo workspace (1 lượt) | mỗi lần unit khởi động | NRestarts; chính sách Restart |
| 2 | `hermes-key-fetch` (`/usr/local/sbin`) → `/run/hermes/` | khoá OpenRouter + Qdrant + Agent Data của Hermes | mỗi lần unit Hermes khởi động | unit nào gọi; số secret; NRestarts |
| 3 | `jev-gw-key-fetch gw` ← `ExecStartPre=+` của `jev-gw.service` | `openrouter-api-key-main`, `jev-mcp-path-secret` (2 lượt) | mỗi lần unit khởi động | NRestarts |
| 4 | `/usr/local/sbin/jev-gw-health` ← `jev-gw-health.timer` 5 phút | (nghi) path-secret để dựng URL | 288 vòng/ngày | **nghi phạm số 1**: nếu mỗi vòng lấy từ GSM ≈ 8.600 lượt/tháng |
| 5 | `lark-client/lark_client/core.py` `_gsm_get` | `LARK_APP_ID`, `LARK_APP_SECRET` | mỗi tiến trình tạo LarkCore, CHỈ khi env và `docker/.env` thiếu | biến có trong env/`.env` không; tiến trình nào (gateway, backup cron, `lark_tool`) |
| 6 | `lark_client/gpg_backup.py` (bật bằng biến `LARK_BACKUP_GPG_PUBKEY_GSM`) | khoá GPG công khai backup Lark | mỗi lần `build_service` | biến opt-in có đặt không |
| 7 | Script backup/cron Lark gọi `timeout 30 $GCLOUD secrets versions access` cho 2 khoá Lark (đầu nối che đường dẫn; thấy bản sao trong `evidence/`) | 2 khoá Lark | theo lịch backup Lark | tìm bản đang chạy + lịch |
| 8 | `dot/bin/dot-{env-restore,pg-restore-verify,e2e-test,schema-apply,knowledge-sync-agentdata,verify-ai-connections,ai-manifest}` | nhiều | 24/07: chỉ chạy tay | nay có cron/timer nào gọi không (vd kiểm khôi phục backup) |
| 9 | `docker/agent-data-repo/tools/{save_report,move_document}.sh` | khoá Agent Data | mỗi lần agent gọi, khi env thiếu | ai gọi, bao lâu một lần |
| 10 | `deploys/web-test/scripts/integrity/{watchdog-monitor,cron-integrity}.sh` | đã gỡ 24/07 | hằng giờ / 6 giờ | bản đang chạy vẫn là bản đã vá (sha); bản trong `docker/nuxt-repo` còn nhánh dự phòng nhưng không được gọi |
| 11 | `scripts/git-push-gh-daily.sh` (v1, đã thay bằng v2 dùng `.env`) | PAT GitHub | không lịch | xác nhận v2 không gọi GSM |
| 12 | Mã Cloud Functions/terraform cũ trong `docker/agent-data-repo` | nhiều | chỉ khi còn deploy trên GCP | đối chiếu A + B5 |
| 13 | Máy Mac: Claude Code/Codex được phép `gcloud secrets versions access`; cấu hình MCP có thể lấy khoá mỗi lần mở app | tuỳ phiên | tay/agent/mỗi lần mở app | đếm qua A; B1 phía Mac |
| 14 | Việc đang chạy `work/mcp-token-argv/` (đưa Bearer của lark-crud-gateway/mcp-remote về GSM) | khoá gateway Lark | có thể thêm caller mới | ghi hiện trạng lúc đo |

**Kho lưu trữ đã biết:** `jev-mcp-path-secret` v1 còn `enabled` nhưng không dùng (xem `work/jev-integration/`) → ứng viên huỷ.
