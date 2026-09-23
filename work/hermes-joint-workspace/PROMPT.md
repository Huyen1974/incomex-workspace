# PROMPT — HJW.2B1 · SEC-CLEAN + Scoped Capability Audit

RUN_ID: HJW-2B1-20260923-02
STATUS: DRAFT — KHÔNG RUN cho tới khi Host ghi READY@ đúng SHA cuối chạm file này

Executor_Surface: Claude Code CLI trên Mac
Runtime_Write_Path: SSH/root-operator tới VPS
Report_Write_Path: fs_* vào work/hermes-joint-workspace/
Work: work/hermes-joint-workspace/

## Mục tiêu

Sau KQ DỪNG G0.2 của HJW-2B:
1. Giảm rủi ro L1 ngay: gỡ AGENT_DATA_* khỏi môi trường Hermes nếu xác nhận không consumer hiện hành nào cần.
2. Giữ Hermes/Telegram/serve hoạt động bình thường sau cleanup.
3. Chỉ-read khảo sát phương án cấp capability hẹp bằng **thành phần hiện hữu**; chưa triển khai proxy/backend/capability route mới trong RUN này.
4. Trả lời dứt khoát: có thể tạo endpoint cho Hermes mà **không lộ master key** và endpoint tự enforce capability hẹp (tool + write scope HJW) hay không.

**Không tiếp tục automation Phase 1 trong RUN này.**

## Checkpoint

- Đọc AGENTS.md → COLLAB.md → PROMPT.md.
- Kiểm READY@ đúng commit cuối chạm PROMPT.
- Đọc KQ@HJW-2B-20260923-01 DỪNG + evidence G0.2.
- Không in/log/hash-compare giá trị secret mới; bằng chứng chỉ dùng tên biến, quyền, route, tool list, status code.
- Không chạm QDRANT key, OpenRouter key, Telegram token, GSM versions, JEV config.

## A. Read-gate trước cleanup

### A1. Consumer thật
Định nghĩa **consumer** = process/unit/job/script/config tự động đang chạy hoặc sẽ tự chạy và thực sự cần AGENT_DATA_*.
- xác nhận Hermes core không tham chiếu AGENT_DATA_*;
- xác nhận config không có mcp_servers;
- xác nhận `hermes cron status/list` và thư mục cron. **Kỳ vọng 0 job** theo hậu kiểm Hermes. Nếu tại RUN xuất hiện bất kỳ job nào ⇒ DỪNG trước mutation; không tự pause/resume;
- tìm theo **tên biến** AGENT_DATA_API_KEY / AGENT_DATA_URL trong unit/script/config/notepad/skills/cache và process/socket tới 127.0.0.1:6533;
- tài liệu skill/cache chỉ nhắc biến nhưng không chạy **không phải consumer**; liệt kê chúng là tài liệu stale để Host xử lý sau, không dùng làm lý do DỪNG;
- xác định relay 6533 trước đây phục vụ KB/workspace hay chức năng nào và hiện có kết nối active hay không.

Nếu có consumer chạy thật hoặc bỏ biến sẽ phá chức năng đang dùng ⇒ **DỪNG trước mutation** và nêu đúng consumer.

### A2. Nguồn env + hai service
Xác nhận:
- `/run/hermes/or.env` do `hermes-key.service` sinh, không phải nguồn bền;
- cả `hermes-serve.service` và `hermes-gateway.service` đều đọc cùng EnvironmentFile và file là bắt buộc;
- xác định source script/resolver tạo AGENT_DATA_* (kỳ vọng `/usr/local/sbin/hermes-key-fetch` + resolver liên quan).
**Cấm sửa trực tiếp /run/hermes/or.env như giải pháp.**

### A3. Tránh xung đột safe-update
Trước mutation:
- đọc `systemctl list-timers hermes-safe-update.timer`;
- đọc `hermes-safe-update status` và lock/state hiện hữu.
Nếu safe-update đang chạy/giữ lock, hoặc timer kế tiếp ≤15 phút ⇒ DỪNG, không tranh restart.

## B. SEC-CLEAN — thứ tự bắt buộc

Chỉ sau A PASS:
1. Backup **source script/resolver thực sự sẽ sửa** + metadata unit cần rollback vào hồ sơ VPS HJW; không backup plaintext secret.
2. Sửa **source bền** để không còn materialize AGENT_DATA_API_KEY; bỏ AGENT_DATA_URL nếu không consumer nào cần. **Không sửa /run/hermes/or.env trực tiếp.**
3. Không thay QDRANT_LOCAL_API_KEY/QDRANT_URL hoặc secret khác. Báo cáo phải ghi rõ **L1 chỉ giảm một phần**, vì Qdrant vẫn ngoài scope.
4. Gửi Owner một dòng Telegram: `hermes-serve` + `hermes-gateway` sẽ restart, Telegram và desktop có thể gián đoạn vài phút. Không gửi được ⇒ DỪNG trước restart.
5. Root chạy tay `systemctl restart hermes-key.service`.
6. **Trước khi restart Hermes:** xác nhận `/run/hermes/or.env` tồn tại, permission hợp lệ, các tên biến bắt buộc khác vẫn có, AGENT_DATA_API_KEY không còn; không in value. File thiếu/hỏng ⇒ rollback source ngay, chưa chạm serve/gateway.
7. Restart **`hermes-serve.service` trước**, chờ active + local status OK.
8. Restart **`hermes-gateway.service` sau**, chờ active + Telegram connected.
9. Kiểm `/proc/<MainPID>/environ` của **cả serve và gateway** theo tên biến: AGENT_DATA_API_KEY/AGENT_DATA_URL phải vắng; không đọc/in value khác.
10. Smoke chính bằng `hermes-safe-update health` (root); phải PASS unit, serve/API, Telegram, version/code và model call. Đọc lại `hermes-safe-update status`.
11. Đây là phép thử bền qua regenerate: source đã sửa → key.service sinh lại env → hai service nạp env mới. Không coi chỉnh tmpfs thủ công là PASS.
12. Nếu bước 5–10 FAIL: rollback đúng thứ tự:
    - restore source script/resolver;
    - restart hermes-key.service;
    - kiểm env file hợp lệ;
    - start/restart serve;
    - start/restart gateway;
    - chạy hermes-safe-update health;
    rồi ghi KQ DỪNG.
13. Cron baseline = 0 job nên **không pause/resume**. Nếu runtime khác baseline và có job ⇒ A đã phải DỪNG trước mutation.

## C. CAP-PATH-AUDIT — CHỈ ĐỌC, KHÔNG triển khai

Đọc mã/config Agent Data đang chạy và audit đủ:
- `/mcp`
- `/mcp-readonly`
- `/mcp-gpt`
- `/mcp-gpt-full`
- **`POST /mcp/tools/{tool_name}` legacy**
- `require_api_key` / auth model
- `_mcp_filtered_handler` + allowlists
- mọi guard write theo path/document_id.

Phải trả lời:

### C1. Secret isolation
Có cách giữ master Agent Data key ở server/root side để user/process Hermes không đọc được không? Nêu rõ nếu cần listener/socket/header injection mới.

### C2. Caller boundary
Có thể hạn chế caller bằng UNIX socket/SocketMode/SocketUser/SocketGroup/client ticket hiện hữu không? C2 PASS **không tự động** làm C3 PASS.

### C3. Capability boundary
Server-side phải tự enforce:
- đúng tool cần;
- nếu có write repo thì chỉ `work/hermes-joint-workspace/**`;
- cấm delete/destructive/exec ngoài scope;
- raw HTTP/MCP không bypass được.

Phân biệt rõ guard path KB/document_id với guard path repo workspace; không coi hai thứ là tương đương.

### Kết luận bắt buộc — 3 nhánh
- **FEASIBLE_EXISTING**: C1+C2+C3 đạt bằng config/component hiện hữu, không code change/new listener/service.
- **FEASIBLE_WITH_MIN_CODE_CHANGE**: không đạt hiện hữu nhưng có thể đạt bằng thay đổi mã nhỏ có review trong Agent Data hiện tại. Phải nêu **chính xác file + route/function tái dùng + guard cần thêm**, nhưng **không sửa mã trong RUN này**.
- **NOT_FEASIBLE**: cần server/proxy/framework mới hoặc thay đổi lớn hơn một route/guard hẹp.

Không được gọi “giấu master key” là đủ nếu capability vẫn full-write hoặc legacy route bypass còn mở.

## D. Báo cáo

Cập nhật COLLAB.md + view.html:
- SEC-CLEAN PASS/ROLLBACK/DỪNG;
- AGENT_DATA_* còn/không còn trong env của **cả hai service**;
- ghi rõ **L1 giảm một phần** vì Qdrant vẫn ngoài scope;
- danh sách skill/doc stale tham chiếu Agent Data (không sửa trong RUN này);
- `hermes-safe-update health/status` sau cleanup;
- CAP-PATH-AUDIT = một trong 3 nhánh + evidence;
- nếu MIN_CODE_CHANGE: nêu đúng file/route/function/guard nhỏ nhất;
- ghi ứng viên tạm thời **S1-lite**: đọc repo public + Telegram cho nhắc lượt/canh RUN/heartbeat, 0 Agent Data, **không triển khai trong RUN này**.

Nếu kết luận là FEASIBLE_WITH_MIN_CODE_CHANGE, đưa Owner đúng **một câu hỏi** sau KQ:
“Có cho phép một RUN riêng, có review, sửa mã nhỏ ở Agent Data để tạo đường ghi hẹp cho Hermes không?”
Không cho ⇒ Hermes ở mức read-only + thông báo; đó là giới hạn đã biết.

Evidence runtime vào hồ sơ VPS HJW theo AGENTS A8.

## CẤM

- Không tiếp tục automation Phase 1 trong RUN này.
- Không khai mcp_servers/workspace_* cho Hermes.
- Không dựng route/proxy/listener/socket/service mới.
- Không sửa backend Agent Data/R03.
- Không sửa skill docs trong RUN này.
- Không mở webhook/port mới.
- Không chạm/rotate/xoá QDRANT, OpenRouter, Telegram, GSM version hoặc JEV config.
- Không đưa master Agent Data key trở lại env Hermes sau cleanup.
- Không log/copy plaintext secret vào repo/evidence/chat.

## BÁO CÁO / AP-CLOSE

- Chỉ dùng RUN_ID `HJW-2B1-20260923-02`; không ghi lại KQ RUN HJW-2B cũ.
- KQ@HJW-2B1-20260923-02 XONG nếu SEC-CLEAN PASS và audit có kết luận rõ một trong 3 nhánh.
- KQ@HJW-2B1-20260923-02 DỪNG nếu read-gate chặn, cleanup không an toàn, rollback xảy ra hoặc không đủ evidence.
- Không tự chạy S1-lite/S2 hay nhánh khác sau KQ. Host quyết.
