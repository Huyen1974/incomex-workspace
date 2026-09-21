# HERMES REVIEW RESPONSE — JEV Integration

Nguồn: báo cáo Hermes do Owner chuyển ngày 2026-09-21. Đây là bản kết luận/evidence tóm lược để hội đồng và Agent đọc trong SSOT; bằng chứng thô vẫn nằm trên VPS tại scratch của Hermes và phải được Claude Code kiểm độc lập trước production.

## Kết luận Hermes
- **GO WITH ADJUSTMENT.**
- Hermes đã thử thật trong scratch, không cài production: tải `itsmostafa/typesafe-mcp` binary, kiểm SHA256/version; gọi JEV thật qua OpenRouter và nhận `answers`; thử 2 bridge stdio→HTTP.
- Model pin đúng: `typesafe/jev-1.13` (không có `~`). Dạng `~typesafe/jev-1.13` trả 400. `~typesafe/jev-latest` chạy; `typesafe/jev-latest` trả 400.
- Đề xuất bridge: `mcp-proxy==0.12.0 --stateless`, ghim `mcp==1.27.1`; dự phòng `supergateway 4.0.0`.
- ChatGPT/Work cần route theo mẫu **path-secret** đang chạy ở `gpt-mcp`; không dựa vào custom Authorization header.
- V0 có thể dùng OpenRouter key đã nằm trong tmpfs `/run/hermes/or.env`; không cần tạo secret mới nếu kiểm tra file này không chứa secret không liên quan.
- Service phù hợp hơn trên host/systemd, không đặt trong `claude_mcp_net` vì network đó `internal: true` và không ra OpenRouter.
- Package tự nổi lỗi sai model/sai schema/thiếu state dưới dạng MCP `isError=true`; 429/529 có retry.
- Lỗ hổng im lặng đã thấy: upstream HTTP 200 nhưng payload không có `answers` thì package không tự coi là lỗi. Hermes đề xuất health-check phải gọi JEV thật và chỉ PASS khi parse được `answers`.
- Blocker production do Hermes nêu: cài service/nginx/root path cần quyền root; user `hermes` hiện không sudo được vì `NoNewPrivileges=1`.

## Số đo/chi tiết Hermes báo cáo
| Hạng mục | Hermes đo được | Đề xuất Hermes |
|---|---|---|
| Package | `typesafe-mcp v0.4.2`, binary Linux amd64, SHA256 OK | Pin release + checksum; không `evaluate update` ở production |
| OpenRouter | `/api/alpha/decisions`, `OPENROUTER_API_KEY` | Pin model bằng argument call |
| JEV real call | Có `answers`, ~0.3–0.5s/lượt | Dùng key hiện có trong pilot |
| Bridge 1 | `supergateway 4.0.0` chạy nhưng strict hơn về `Accept` | Chỉ dự phòng |
| Bridge 2 | `mcp-proxy 0.12.0` + `mcp 1.27.1` chạy | Chọn bridge chính |
| Auth | Route ChatGPT thật đang dùng path-secret | Dùng chung path-secret URL |
| Runtime | Host systemd có egress; docker Claude MCP bị isolated | systemd host |
| Port | `172.18.0.1:8792` trống tại thời điểm review | Có thể dùng, phải đo lại lúc deploy |
| Health | Uptime Kuma push + timer pattern đã có | Probe thật JEV, có `answers` mới `up` |
| Codex | `codex mcp add --url` hỗ trợ streamable HTTP | Dùng cùng remote endpoint |
| Hermes | Hermes config hỗ trợ remote MCP URL | Có thể cắm cùng endpoint |
| ChatGPT | Full All hiện dùng path-secret | Phải Scan Tools / client acceptance |

## Rollback Hermes đề xuất
1. Disconnect client/connector.
2. Bỏ nginx include / khôi phục backup cấu hình.
3. Disable/stop `jev-gw`.
4. Gỡ binary/venv của JEV gateway.
5. Không chạm TEST20 / Full All / agent-data / claude-mcp / cowork-runner.

## Hermes và workspace — hiện trạng Hermes tự đo
Hermes **đọc được** repo nhưng chưa có đường ghi hợp lệ:
- không ghi được helper queue hiện tại;
- chưa đăng nhập `gh`;
- không có SSH deploy key;
- clone helper đọc được nhưng không ghi được.

Hermes đề xuất 3 đường, trong đó có direct deploy key. **Host lưu ý:** README/D12 hiện quy định direct Git/GitHub write là read-only đối với AI/Agent; vì vậy direct deploy key không được dùng làm mặc định. Việc đưa Hermes thành thành viên phải ưu tiên bind vào capability đã audit (`workspace_*`/`fs_*`) hoặc helper/queue có cùng guardrail.

## Những điểm Claude Code bắt buộc kiểm độc lập
1. Package/version/checksum/model pin và kết quả real JEV.
2. `mcp-proxy` + `mcp==1.27.1` compatibility, schema/error preservation.
3. Path-secret compatibility với ChatGPT/Work.
4. Nội dung **tên biến** trong `/run/hermes/or.env` (không in value): nếu có secret khác OpenRouter thì không cho `jev-gw` đọc cả file một cách không cần thiết.
5. Per-call rule: không có `answers` = **không có tham khảo JEV**, dù HTTP/MCP trả thành công; ưu tiên giải bằng tool/skill guidance nếu đủ.
6. Root actions thực sự cần gì; không cấp sudo rộng.
7. Không dọn disk/container ngoài scope JEV.
8. Hermes full-member phải tiếp tục theo `work/hermes-joint-workspace/`, không tạo đường direct Git mới.

## Evidence trên VPS theo Hermes
- Scratch: `/var/lib/hermes/.hermes/cache/scratch/`
- Các probe Hermes nêu: `jev_probe.py`, `jev_mcp_probe.py`, `bridge_probe.py`, `sse_probe.py`
- Binary thử: `jev/evaluate`
- Bản báo cáo Hermes nêu: `/var/lib/hermes/work/bao-cao/jev-hermes-review-2026-09-21.md`

Claude Code phải coi các path này là evidence cần kiểm, không coi báo cáo này tự thân là PASS production.
