# PROMPT — HJW.2B1 · SEC-CLEAN + Scoped Capability Audit

RUN_ID: HJW-2B1-20260923-02
STATUS: DRAFT — KHÔNG RUN cho tới khi Host ghi READY@ đúng SHA cuối chạm file này

Executor_Surface: Claude Code CLI trên Mac
Runtime_Write_Path: SSH/root-operator tới VPS
Report_Write_Path: fs_* vào work/hermes-joint-workspace/
Work: work/hermes-joint-workspace/

## Mục tiêu

Sau KQ DỪNG G0.2 của HJW-2B:
1. Giảm rủi ro L1 ngay: gỡ AGENT_DATA_* khỏi môi trường Hermes nếu xác nhận hiện không consumer nào dùng.
2. Giữ Hermes/Telegram/serve hoạt động bình thường sau cleanup.
3. Chỉ-read khảo sát phương án cấp capability hẹp bằng **thành phần hiện hữu**; chưa triển khai proxy/backend mới trong RUN này.
4. Trả lời dứt khoát: có thể tạo endpoint cho Hermes mà **không lộ master key** và endpoint tự enforce capability hẹp (tool + write scope HJW) hay không.

Không tiếp tục automation Phase 1 trong RUN này.

## Checkpoint

- Đọc AGENTS.md → COLLAB.md → PROMPT.md.
- Kiểm READY@ đúng commit cuối chạm PROMPT.
- Đọc KQ@HJW-2B-20260923-01 DỪNG + evidence G0.2.
- Không in/log/hash-compare giá trị secret mới; bằng chứng chỉ dùng tên biến, quyền, route, tool list, status code.
- Không chạm QDRANT key, OpenRouter key, Telegram token, GSM versions, JEV config.

## A. Read-gate trước cleanup

Xác nhận lại:
- Hermes config chưa có mcp_servers;
- hermes cron list = 0;
- tìm theo **tên biến** AGENT_DATA_API_KEY / AGENT_DATA_URL trong config/unit/script/runtime để xác định consumer thực tế, không in value;
- xác định chính xác file/script/root oneshot nào đưa AGENT_DATA_* vào /run/hermes/or.env và unit nào EnvironmentFile file đó.

Nếu có consumer hiện hành ngoài workspace MCP hoặc bỏ biến sẽ làm hỏng chức năng đang dùng ⇒ DỪNG trước mutation.

## B. SEC-CLEAN — mutation nhỏ, rollback rõ

Nếu A PASS:
1. Backup đúng file/script/unit sẽ sửa vào hồ sơ VPS HJW; không backup plaintext secret.
2. Sửa nguồn nạp để **không còn materialize AGENT_DATA_API_KEY** cho Hermes. Gỡ AGENT_DATA_URL khỏi Hermes env nếu không consumer nào cần; URL không phải secret nhưng không giữ cấu hình chết.
3. Không thay các secret khác trong /run/hermes/or.env.
4. Trước restart gateway/serve: gửi Owner một dòng Telegram báo Hermes sẽ gián đoạn vài phút. Gửi không thành công ⇒ DỪNG trước restart.
5. Pause cron, restart đúng service cần thiết, smoke:
   - Telegram Owner ↔ Hermes;
   - hermes-serve/local health;
   - process env chỉ kiểm **tên biến**: AGENT_DATA_API_KEY không còn;
   - OpenRouter/Telegram chức năng vẫn sống.
6. Rollback ngay nếu smoke fail; báo DỪNG.

## C. CAP-PATH-AUDIT — CHỈ ĐỌC, KHÔNG triển khai

Khảo sát các thành phần đang có: systemd socket/proxyd, nginx hiện hữu, Agent Data routes /mcp*, route/tool filters, OS ACL/socket permission, MCP client config của Hermes.

Phải trả lời riêng 3 lớp:

### C1. Secret isolation
Có thể để master Agent Data key ở root/server side và không cho user/process Hermes đọc được không?

### C2. Caller boundary
Có thể giới hạn endpoint cho đúng caller dự kiến bằng mechanism sẵn có (UNIX socket ACL, systemd socket permission, client ticket sẵn có...) không?

**Lưu ý:** chỉ C2 PASS vẫn chưa đủ, vì threat model L1 chính là user/process Hermes bị chiếm.

### C3. Capability boundary — BẮT BUỘC
Endpoint phải **tự enforce ở phía server/relay**, không dựa vào config/toolset của Hermes:
- chỉ expose đúng tool cần cho Phase 1;
- write chỉ được vào work/hermes-joint-workspace/**;
- cấm delete/destructive/exec/root khác;
- caller không thể dùng raw HTTP/MCP để vượt scope.

Được phép tận dụng route/filter/config/code **đã tồn tại**. Không viết backend mới, không thêm proxy service mới, không sửa R03 contract trong RUN này.

Kết luận:
- FEASIBLE_EXISTING nếu C1+C2+C3 đều làm được bằng thành phần/config hiện hữu, nêu chính xác cách và rollback.
- NOT_FEASIBLE nếu thiếu C3 hoặc phải sửa backend/viết proxy mới.
- Không được gọi một proxy chỉ “giấu master key” là đạt D08 nếu capability phía sau vẫn là master/full-write.

## D. Báo cáo

Cập nhật COLLAB.md + view.html:
- KQ cleanup: PASS/ROLLBACK/DỪNG;
- AGENT_DATA_* còn/không còn trong env Hermes (chỉ tên biến);
- CAP-PATH-AUDIT = FEASIBLE_EXISTING hoặc NOT_FEASIBLE;
- nếu feasible: mô tả tối thiểu kiến trúc, không triển khai;
- nếu not feasible: nêu chính xác thiếu lớp nào C1/C2/C3.

Evidence runtime vào hồ sơ VPS của HJW theo AGENTS A8.

Kết thúc:
- KQ@HJW-2B1-20260923-02 XONG nếu cleanup PASS và audit có kết luận rõ;
- KQ@HJW-2B1-20260923-02 DỪNG nếu cleanup không an toàn/rollback hoặc không thể thu thập evidence cần thiết.

Không tự tiếp tục HJW.2B automation sau RUN này. Host sẽ quyết bước kế tiếp.
Trước sửa runtime:
- lưu backup đúng các config/unit/script sắp chạm vào hồ sơ VPS của việc theo AGENTS A8;
- ghi hash/path và lệnh rollback;
- không backup secret plaintext.

### B. Workspace + JEV
1. Trước mọi restart gateway/serve để khai `mcp_servers`: gửi Owner **một dòng Telegram báo trước** rằng Hermes sẽ mất liên lạc vài phút; xác nhận tin đã gửi thành công rồi mới restart. Nếu không gửi được ⇒ DỪNG trước restart. Backup `config.yaml`, pause cron trước mutation, có lệnh rollback rõ.
2. Khai `workspace_*` trong Hermes qua relay 127.0.0.1:6533.
3. Loại Agent Data key khỏi môi trường user/process Hermes theo G0.2; không làm hỏng relay.
4. Nạp skill/luật mỏng: mỗi task đọc AGENTS → A0 → vai; Agent chỉ chạy khi READY + RUN_ID hợp lệ; Reviewer không tự triển khai; Host chỉ khi Owner giao.
5. Cắm JEV qua gateway hiện hữu như nguồn tham khảo, không quyền phê duyệt/chặn.

### C. Assignment Phase 1 — capability confinement
Phase 1 chỉ nghiệm thu execution assignment trong chính `work/hermes-joint-workspace/`; sau PASS mới tổng quát A9 ở HJW.4.

Gate deterministic chạy khoảng 2 phút/lần:
- resolve HEAD bằng network call có `timeout ≤20s` → đọc COLLAB tại chính SHA; mọi lỗi phải in `{"wakeAgent": false}` ở dòng cuối;
- chỉ quan tâm dấu strict `ASSIGN@... to=Hermes ... state=open`;
- author/client label chỉ là telemetry/phòng vệ phụ, KHÔNG coi là authentication;
- role=Agent phải có `run=<RUN_ID>` và agent phải kiểm READY đúng SHA trước mutation;
- role=Host chỉ hợp lệ khi COLLAB có quyết định Owner giao Host;
- **dedupe chính = `assignment_id + state`; SHA chỉ là điều kiện phụ**. Commit `claimed`/`done` của chính Hermes không được làm assignment tự wake lần hai;
- ghi persistent ledger trên đĩa cho wake/claim/retry/daily-count; không giữ trần chỉ trong RAM;
- mặc định mỗi assignment wake một turn. Nếu đã wake nhưng sau 15 phút vẫn chưa `claimed` và assignment vẫn `open` tại cùng HEAD ⇒ cho đúng **1 lần retry**. Nếu retry vẫn không claim ⇒ không wake thêm; ghi `exhausted` trong ledger + Telegram, và nếu write path còn hoạt động thì chuyển `blocked`; nếu write path không hoạt động thì để Host reconcile, tuyệt đối không loop;
- max_parallel=1; Phase 1 đặt trần an toàn 24 automated LLM wakeups/24h **tính từ persistent ledger**; chạm trần ⇒ blocked/alert, không tự vượt;
- state runtime/dedupe có thể lưu cache/ledger, nhưng COLLAB/KQ vẫn là SSOT.

Automated turn dùng **confinement cấu hình cron**, không cần profile thứ hai ở Phase 1:
- cấu hình `platform_toolsets.cron` làm allowlist cho cron; dùng `agent.disabled_toolsets` cho deny cứng khi cần. **Không tìm cờ `--toolset` vì CLI hiện không có cờ đó**;
- nếu cấu hình restriction không đọc/parse được thì run phải **bị từ chối**, không fallback về full/default tools; nghiệm thu điều này;
- được **đọc** `work/**` để nhắc/handoff, nhưng Phase 1 chỉ được **ghi** `work/hermes-joint-workspace/**` qua relay; mở rộng write scope chỉ sau HJW.4;
- KHÔNG terminal/exec, sudo/root, secret/IAM, service control, destructive/delete;
- cron worker không có interactive approval path; **không thiết kế dựa trên hộp thoại xin phép**. Nếu assignment đòi capability không có trong allowlist ⇒ automated turn phải kết thúc `blocked` + Telegram bằng capability còn được phép; CẤM auto-approve;
- nếu bản Hermes không enforce được restriction trên bằng cấu hình sẵn có ⇒ DỪNG, không tự code sandbox mới.

### D. Job Phase 1
Chỉ 4 nhóm:
1. assignment gate / self-wake;
2. nhắc đúng lượt + canh RUN treo bằng script/`--no-agent`, dedupe cảnh báo; **phải kiểm STOP-DISPATCH trước khi gửi Telegram**;
3. health/watchdog qua cơ chế Kuma độc lập ở G0.5;
4. stop controls.

Không làm bản tin sáng, không webhook, không sửa Owner View.

### E. Stop controls
- STOP-AUTO: `hermes pause`.
- STOP-DISPATCH: một cờ root-owned, persistent, ngoài quyền ghi user Hermes (ưu tiên `/etc/incomex/hermes-automation.stop` hoặc vị trí chuẩn hiện hữu tương đương). Tất cả HJW gate scripts **và job `--no-agent` gửi Telegram** phải check cờ trước hành động. Nói rõ giới hạn: gate script nằm trong vùng user Hermes có thể sửa, nên STOP-DISPATCH chống **agent đi sai chính sách**, không phải hàng rào chống user `hermes` đã bị chiếm.
- HARD-STOP: runbook root/operator dựa trên entry paths thật; phải dừng các service/process có thể khởi tạo agent và chặn run mới. Nếu inference credential runtime cần được vô hiệu hoá để ngăn manual CLI, nêu rõ cách làm/rollback; không rotate/revoke provider key trong RUN này.
- Không test HARD-STOP làm gián đoạn phiên Owner đang dùng; nếu đang active, ghi test này sang HJW.3. STOP-DISPATCH phải test trong RUN này.

## NGHIỆM THU TRONG RUN

Tối thiểu:
- relay read + write thử trong `work/hermes-joint-workspace/_thu-nghiem/hermes/`; stale expected_version bị reject;
- Hermes process/user không còn đọc được Agent Data credential sau khi relay PASS; không có GSM credential;
- **N8 relay boundary:** gọi relay không có client-ticket/auth riêng từ caller local khác. Nếu relay mở, thử siết bằng cơ chế sẵn có; không siết được ⇒ DỪNG theo G0.2;
- JEV gọi thật trả `answers`;
- 3 tick không đổi HEAD/assignment ⇒ 0 LLM wake;
- **N1:** giả lập `ls-remote` timeout/mạng lỗi ⇒ 0 LLM wake, stdout cuối là `{"wakeAgent": false}`, có log lý do;
- assignment thử hợp lệ ⇒ wake/claim trong mục tiêu ≤5 phút, không chạy trùng;
- **N2:** wake rồi dừng worker trước claim ⇒ sau 15 phút đúng 1 retry, không retry thứ hai; có ledger/alert;
- **N3:** HEAD đổi do chính commit `claimed` ⇒ không wake lần hai;
- **N4:** trong turn cron gọi capability ngoài allowlist ⇒ capability/tool **không tồn tại trong schema**; lưu danh sách tool thực tế vào evidence;
- **N5:** kiểm fail-closed của `platform_toolsets.cron` bằng fixture/cách an toàn không làm hỏng live config; restriction unreadable ⇒ run bị từ chối, không full-tool fallback. Nếu không có cách test live an toàn, dùng fixture/code-path evidence và ghi rõ giới hạn để HJW.3 kiểm tiếp;
- assignment cần capability ngoài allowlist ⇒ blocked + Telegram, không có interactive approval, không auto-approve;
- STOP-DISPATCH đặt ⇒ 0 HJW automated run/notification mới qua ít nhất 3 tick; gỡ ⇒ hoạt động lại, không chạy bù trùng;
- **N6:** khi STOP-DISPATCH bật, tin nhắn trực tiếp của Owner tới Telegram vẫn có thể tạo LLM turn; ghi đúng giới hạn này, không gọi STOP-DISPATCH là HARD-STOP;
- Kuma/external watchdog báo được tới Owner;
- **N7:** secret-redaction test chỉ dùng **synthetic canary**, tuyệt đối không yêu cầu/in secret OpenRouter/Telegram/AgentData thật; canary phải bị che trong output/log/delivery;
- **N-mem:** chạy một automated turn test rồi đo có ghi persistent memory hay không; không giả định `skip_memory`. Nếu có memory write và cấu hình hiện hữu có cách tắt riêng cho cron thì tắt; nếu không thì ghi rủi ro + evidence, không tự viết memory subsystem mới;
- ghi model/runtime usage đủ để đo T6, nhưng ngân sách nằm ngoài HJW theo D10.

HJW.3 sẽ làm cross-check cuối T1–T10 và HARD-STOP nếu RUN này chưa test được an toàn.

## CẤM

- Không mở port/webhook 8644.
- Không tạo server/proxy thứ hai.
- Không sửa mã backend Agent Data hoặc contract R03.
- Không đưa GitHub Owner credential, GSM credential, Agent Data key plaintext vào Hermes.
- Không bật auto-approve.
- Không xoá secret/version GSM; hai quyết định dọn 23 version và Lark thuộc việc GSM/mcp-token-argv, không nằm trong HJW.
- Không thay JEV health cadence trong HJW.
- Không log/copy secret vào repo, evidence hoặc chat.

## BÁO CÁO / AP-CLOSE

- Evidence runtime vào hồ sơ VPS của `hermes-joint-workspace` theo AGENTS A8.
- Cập nhật đúng `COLLAB.md` + `view.html`, không tạo file progress mới.
- Ghi rõ before/after, rollback, PASS/FAIL từng gate.
- Kết thúc:
  - `KQ@HJW-2B-20260923-01 XONG` nếu mọi điều kiện trong scope PASS;
  - hoặc `KQ@HJW-2B-20260923-01 DỪNG` + blocker cụ thể.
- Chỉ trả Owner một dòng XONG hoặc DỪNG; Host tự nghiệm thu từ Git/evidence.
