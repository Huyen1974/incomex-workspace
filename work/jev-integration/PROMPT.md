# PROMPT — JEV.B1 · OpenAI first · off-the-shelf gateway + monitoring

RUN_ID: JEV-B1-OPENAI-20260921-01
Host: GPT Chat · Host_ID: GPT-JEV-20260920-A
Reviewer/Supervisor: Claude Chat
Executor_Surface: Claude Code CLI trên VPS, phiên có quyền root cho đúng các mutation hạ tầng được prompt này cho phép.
Write_Path: `workspace_*` đã audit cho mọi ghi vào incomex-workspace; runtime/config trên VPS sửa trực tiếp tại VPS vì VPS là SSOT của mã/runtime. CẤM git/GitHub native để ghi repo.

Chỉ chạy khi `work/jev-integration/COLLAB.md` có `READY@<40 SHA>` đúng commit cuối chạm file này + lệnh RUN hợp lệ. READY không phải RUN.

## 0. Cổng chỉ-đọc trước mutation
1. Một read-gate bằng đúng Write_Path; fail → **DỪNG**.
2. Đọc: root `AGENTS.md` → `work/jev-integration/COLLAB.md` A0/D01–D08/P08 → prompt này → `HERMES-REVIEW.md` + `HERMES-REVIEW-RESPONSE.md` → README D12/§11–§12.
3. Xác nhận phiên Claude Code có quyền root cần thiết. Không có → DỪNG trước mutation.
4. Kiểm độc lập, chỉ đọc:
   - không giả định report Hermes là PASS;
   - package/release/checksum của `itsmostafa/typesafe-mcp`;
   - gọi thật JEV qua OpenRouter phải có `answers`;
   - model pin `typesafe/jev-1.13` phải chạy; kiểm lại hành vi dạng có `~`;
   - `mcp-proxy==0.12.0` + `mcp==1.27.1` giữ initialize/tools/list/schema/isError qua streamable HTTP stateless;
   - route path-secret của `gpt-mcp` hiện hành;
   - chỉ liệt kê **TÊN biến** trong `/run/hermes/or.env`, tuyệt đối không in value;
   - port `172.18.0.1:8792` còn trống; nếu không, chọn port trống liền kề và ghi lại;
   - liệt kê process/listener thử nghiệm Hermes còn sống nếu có; **không kill/dừng/xoá** chúng trong cổng.
5. Sai khác thiết kế trọng yếu hoặc bằng chứng không tái lập được → DỪNG, ghi đúng blocker; không “sửa cho chạy” bằng kiến trúc mới.

## 1. Phạm vi cứng
Mục tiêu V0:
- một remote MCP JEV dùng chung;
- off-the-shelf first, tối thiểu code;
- OpenRouter là provider duy nhất;
- JEV chỉ tham khảo, không cho phép/chặn thay GPT/Claude/User;
- monitoring/phát hiện lỗi phải có trước khi client acceptance.

KHÔNG làm:
- không sửa TEST20 / Full All / agent-data / claude-mcp / cowork-runner / Zep / Graph / Cognee;
- không dọn disk/container ngoài artifact do RUN này tạo;
- không dựng provider fallback;
- không tối ưu routing/cost;
- không làm Claude-side client ở Bước 1;
- không thêm PreToolUse deny/allow;
- không mở direct Git write;
- không đổi luật nền AGENTS/README trong RUN này.

Rollback chỉ được stop/disable/remove **artifact mới do RUN này tạo** và khôi phục đúng backup nginx của RUN này. Không đụng dịch vụ khác.

## 2. Dựng runtime bằng đồ có sẵn

### J1 · typesafe-mcp
- Dùng release binary Linux phù hợp của `itsmostafa/typesafe-mcp`.
- Baseline Hermes báo: v0.4.2; checksum amd64 `dffec9ce534cc7ddb9497f7ac43e65216bc9f1d56743534678f3ed7081f26799`. Phải kiểm lại release + checksum trước khi dùng.
- Cài vào vùng riêng, ví dụ `/opt/jev/bin/evaluate`.
- Pin version; **không** bật `evaluate update` production.
- Tool giữ tên upstream `evaluate`, shape `{state, questions, model?}`; không viết adapter đổi tên nếu không cần.

### J2 · bridge
- Ưu tiên `mcp-proxy==0.12.0` + `mcp==1.27.1`, dedicated venv.
- Chạy streamable HTTP, stateless, bind host bridge IP hiện hành; port 8792 nếu còn trống.
- Upstream command: `evaluate mcp`.
- Nếu mcp-proxy không tái lập được trên máy thật → DỪNG và báo; không tự chuyển sang bridge khác trong cùng RUN trừ khi COLLAB đã ghi phương án dự phòng được Host duyệt.

### J3 · secret OpenRouter
- Không tạo OpenRouter key mới.
- Nếu `/run/hermes/or.env` chỉ chứa `OPENROUTER_API_KEY` + metadata vô hại cần thiết, có thể tái dùng qua group/read permission tối thiểu.
- Nếu file chứa secret khác không liên quan: **không** cho jev-gw đọc toàn file. Dùng pattern GSM → tmpfs/env riêng đã audit để đưa đúng `OPENROUTER_API_KEY` vào process; không in/copy value.
- Nếu phải tạo/lưu secret mới vì lý do kỹ thuật, source of truth = GSM theo D07; không plaintext trong repo hoặc file bền vững.
- Không log env/value.

### J4 · service
- Chạy trên host/systemd, không nhét vào network `claude_mcp_net`.
- Ưu tiên dedicated service user ít quyền; chỉ cần đọc credential cần thiết và chạy bridge/binary.
- Service bind nội bộ, không public trực tiếp.
- Restart/stop chỉ chính `jev-gw` do RUN này tạo.

## 3. Remote route cho OpenAI
- Nginx chỉ thêm route mới; không sửa semantics route hiện hữu.
- Auth theo mẫu ChatGPT production đã chứng minh: **path-secret**, không yêu cầu custom Authorization header từ ChatGPT.
- Ưu tiên tái dùng **cơ chế path-secret đã audit** mà không copy/in secret.
- Nếu cần path-secret mới: tạo/lưu ở GSM và materialize bằng pattern secret runtime hiện có; không commit/log value. Nếu hạ tầng hiện tại buộc plaintext bền vững mới chạy được → DỪNG và báo Host, không tự hạ chuẩn.
- Route dạng logic: `/jev-mcp/<SECRET>/mcp` → upstream nội bộ jev-gw.
- `access_log off` cho route bí mật; rate-limit theo pattern sẵn có; proxy streaming/timeouts theo MCP route đang chạy.
- Backup file nginx sẽ sửa; chạy `nginx -t`; chỉ reload khi test PASS.
- Sai path-secret phải không vào upstream (ưu tiên 404 như pattern hiện hành).

## 4. Smoke thật + lỗi
Sau service, trước khi coi machine done:

1. MCP initialize PASS.
2. tools/list: đúng một tool `evaluate`; schema upstream không bị bridge biến dạng.
3. Real call với `model=typesafe/jev-1.13` trả payload có `answers`.
4. Sai model / câu hỏi sai khuôn / thiếu field phải nổi `isError` hoặc tool error đọc được.
5. Kiểm “success nhưng không có answers”:
   - quy ước V0: **không có `answers` hợp lệ = không có tham khảo JEV**, dù transport/tool trả success;
   - ghi rõ quy ước này trong SKILL.md;
   - health check cũng phải coi là DOWN;
   - không viết wrapper quanh gateway trừ khi có bằng chứng thực tế rằng client không thể áp dụng quy ước trên và Host duyệt vòng sau.
6. Không retry mù ngoài retry upstream package đã có.

## 5. Monitoring tối thiểu, không đốt token
- Tạo đúng một health script mỏng + systemd timer (ưu tiên 5 phút theo pattern VPS hiện có).
- Probe phải đi qua MCP path/runtime thật: initialize → evaluate → parse `answers`.
- PASS chỉ khi có `answers`.
- Fail phải exit non-zero + journald message ngắn, không chứa state/secret.
- Nếu có thể tái dùng Uptime Kuma push/monitor theo pattern audit hiện có mà không cần mở credential rộng, nối vào; nếu việc tạo monitor cần một cơ chế chưa audit thì **không tự mở rộng** — giữ timer+journal và ghi OPEN cho Host. Client tool error vẫn phải nổi ngay theo từng call.
- Không gọi LLM cho health check.

## 6. SKILL.md — cơ chế nhớ tự nhiên
Tạo `work/jev-integration/SKILL.md` qua Write_Path, ngắn và dùng được lại ở Bước 2.

Nội dung tối thiểu:
- JEV = nguồn tham khảo cho bounded decisions, không phải authority.
- NÊN gọi khi: choice/routing/ranking/classification/risk/verification với tập lựa chọn/tiêu chí đã biết, hoặc nhiều câu hỏi độc lập trên cùng state.
- KHÔNG gọi khi: code/rule deterministic đã đủ; nhiệm vụ sáng tạo/open-ended; cần reasoning nhiều bước; cần sinh nội dung dài.
- Cách hỏi: state gọn, câu hỏi độc lập, typed criteria đúng; ưu tiên instructions tiếng Anh nếu acceptance cho thấy ổn định hơn, không dịch state làm mất nghĩa.
- Luôn pin `typesafe/jev-1.13` trong pilot.
- Kết quả chỉ là evidence cho GPT/Claude tự quyết.
- Tool error hoặc thiếu `answers` = JEV unavailable; model tiếp tục tự reasoning, không giả đã tham khảo.
- Không bắt Owner xem raw probabilities nếu không hữu ích.

Tái dùng nội dung guidance upstream/TypeSafe có ích; không copy dài và không biến skill thành manual SDK.

## 7. Repo/report
- Runtime/config production = VPS SSOT, không deploy từ incomex-workspace xuống VPS.
- Repo chỉ ghi tài liệu/trạng thái qua `workspace_*`.
- Không tạo file progress mới.
- Sản phẩm repo của RUN:
  1. `SKILL.md`;
  2. cập nhật `COLLAB.md` với kết quả machine;
  3. nếu cần, cập nhật ngắn `view.html` để Owner thấy trạng thái.
- Dòng máy đọc:
  - PASS: `KQ@JEV-B1-OPENAI-20260921-01 XONG`
  - FAIL: `KQ@JEV-B1-OPENAI-20260921-01 DỪNG · <mã> · <lý do>`
- Ghi đúng runtime version, bridge version, service/route status, health status; không ghi secret/path-secret value.

## 8. Tiêu chí MACHINE_DONE
Tất cả phải đạt:
- package/checksum/version pin rõ;
- bridge stateless thật;
- service/nginx route healthy;
- path-secret không lộ;
- real JEV call có `answers`;
- lỗi sai model/schema nổi rõ;
- health probe bắt được thiếu `answers`;
- SKILL.md hoàn tất;
- rollback path rõ;
- TEST20/Full All/agent-data/claude-mcp không đổi.

Nếu đạt: ghi KQ XONG và trả Owner đúng một dòng:
`XONG · JEV-B1-OPENAI · MACHINE_DONE · runtime=<...> · evaluate PASS · health PASS · chờ Claude review + client acceptance OpenAI`

Nếu không đạt:
`DỪNG · JEV-B1-OPENAI · <mục> · <lý do>`

## 9. Sau Agent — KHÔNG phải việc của Claude Code trong RUN này
1. Claude Chat (Supervisor) đọc diff/runtime evidence và xác nhận MACHINE_DONE hoặc yêu cầu fix đúng scope.
2. Sau Claude review, GPT Host + Owner thực hiện client-side:
   - ChatGPT Work: tạo/connect đúng app/plugin từ remote endpoint, Scan Tools thật;
   - ChatGPT Chat: thử cùng plugin nếu surface bind;
   - Codex: bind plugin/MCP + skill trên đúng client Owner dùng.
3. Acceptance hành vi: mỗi surface 10 ca nên gọi + 10 ca không nên gọi, prompt không nhắc chữ “JEV”; mục tiêu ≥7/10 tự gọi đúng và ≤2/10 gọi thừa.
4. Chỉ khi OpenAI Bước 1 đạt acceptance mới đánh DONE JEV.B1 và chuyển sang task riêng `work/hermes-joint-workspace/`.
