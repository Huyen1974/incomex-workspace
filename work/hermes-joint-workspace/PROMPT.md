# PROMPT — HJW.2B · Hermes Phase 1

RUN_ID: HJW-2B-20260923-01
STATUS: FINAL FOR READY — KHÔNG RUN cho tới khi COLLAB có READY@ đúng commit cuối chạm file này

Executor_Surface: Claude Code CLI trên Mac
Runtime_Write_Path: SSH/root-operator tới VPS (runtime SSOT)
Report_Write_Path: connector family `fs_*` vào repo/workspace (không GitHub native, không git push trực tiếp)
Work: `work/hermes-joint-workspace/`

## CHECKPOINT BẮT BUỘC

1. Đọc `AGENTS.md` → `work/hermes-joint-workspace/COLLAB.md` → file này.
2. Kiểm `READY@<40 hex>` trong COLLAB khớp commit cuối chạm PROMPT.md; chưa khớp ⇒ DỪNG trước mutation.
3. Runtime/config Hermes trên VPS là SSOT; Git chỉ giữ tài liệu/evidence. Không deploy runtime từ Git.
4. Đọc KQ GSM-A1 trong `work/gsm-access-audit/README.md §8`: Access 167/30 ngày, không rỉ máu; Hermes lấy secret theo root oneshot lúc start. Không tối ưu call GSM trong HJW.
5. Assembly First. Không server/proxy/framework mới nếu relay/unit/cơ chế Hermes hiện hữu đáp ứng.
6. Không in/log secret, token, env value, URL chứa secret/path-secret.

## MỤC TIÊU

Đưa Hermes vào Phase 1 của hội đồng AI bằng đường tối thiểu nhưng an toàn:
- đọc/ghi workspace qua relay Agent Data đã audit;
- tự phát hiện assignment bằng gate deterministic 0-token;
- làm đúng vai được giao, với automated turn bị giới hạn capability;
- nhắc đúng lượt + canh RUN treo;
- health độc lập qua Kuma;
- có STOP-AUTO / STOP-DISPATCH / HARD-STOP;
- giữ secret boundary: user/process Hermes không giữ credential GSM và không giữ `AGENT_DATA_API_KEY` nếu relay hiện hữu có thể cung cấp capability thay thế.

Phase 1 KHÔNG bật Hermes webhook platform, KHÔNG mở port 8644, KHÔNG sửa Owner View synchronizer, KHÔNG sửa luật gốc A9, KHÔNG làm bản tin sáng.

## GATE 0 — READ-ONLY, CHƯA MUTATION

### G0.1 Hermes thực tế
Xác nhận bản đang cài và primitive cần dùng. Baseline đã đo: v0.21.4 có `--script`, `--no-agent`, execution ledger, pause/resume, Telegram.
- Đường chính cho gate LLM: pre-run `--script`; dòng stdout **không rỗng cuối cùng** `{"wakeAgent": false}` = không gọi LLM, `{"wakeAgent": true, "context": {...}}` = wake + truyền context.
- **Fail-closed phải tự viết:** mọi nhánh lỗi (mạng lỗi, timeout, parse lỗi, không xác định SHA, đọc COLLAB lỗi, exception) đều phải kết thúc bằng đúng dòng `{"wakeAgent": false}`. Script im lặng / JSON sai / thiếu flag = Hermes **WAKE**, không phải fail closed.
- Mọi network probe trong gate, đặc biệt `git ls-remote`, phải bọc `timeout ≤20s`; không cho scheduler chờ timeout mặc định dài.
- `--monitor-script` chỉ dự phòng nếu có lý do đo được.
- Không nâng cấp Hermes trong RUN này. Nếu primitive bắt buộc thiếu ⇒ DỪNG và báo.

### G0.2 Agent Data relay + secret boundary
Đo nhưng không in giá trị secret:
- trạng thái `hermes-agentdata-relay.service`, bind/listen và cổng đích;
- nguồn auth hiện tại của relay;
- tên biến env hiện hữu của Hermes (chỉ tên, không value), xác nhận có/không `AGENT_DATA_API_KEY` / `AGENT_DATA_URL`;
- khả năng gọi `workspace_*` qua relay 127.0.0.1:6533 mà client Hermes KHÔNG phải cầm Agent Data key;
- **relay boundary test:** thử từ một process/user local khác hoặc request không có client-ticket/auth riêng (không dùng/đọc secret) để xác định relay có tự gắn credential cho mọi caller loopback hay không.

Quyết định bắt buộc:
- Nếu relay hiện hữu cung cấp được `workspace_*` mà không lộ key cho user/process Hermes **và** caller bị giới hạn bằng cơ chế sẵn có (ACL/UNIX socket permission/client-ticket hoặc tương đương) ⇒ tiếp tục và loại `AGENT_DATA_API_KEY` + URL nhạy cảm tương ứng khỏi môi trường Hermes-readable; key chỉ ở nguồn root/relay tối thiểu.
- Nếu relay hiện đang mở cho mọi process loopback, trước hết phải thử **siết bằng cơ chế đã có** của relay/OS, không dựng server/proxy mới. Nếu không siết được bằng cấu hình/quyền hiện hữu ⇒ **DỪNG** để Host quyết; không coi việc giấu key nhưng để capability write mở cho mọi local process là đạt D08.
- Nếu relay cần chính key đó ở phía Hermes, hoặc muốn sửa backend Agent Data / dựng proxy mới mới làm được ⇒ DỪNG, ghi blocker. KHÔNG chấp nhận giữ write-capable Agent Data key trong Hermes env chỉ vì Git rollback được.

### G0.3 Đọc SSOT không token
Xác nhận công thức:
`git ls-remote <public repo> HEAD` → SHA → đọc `work/*/COLLAB.md` tại đúng SHA bất biến.
Không xác định được SHA/freshness ⇒ fail closed: gate phải in `{"wakeAgent": false}` ở dòng stdout cuối, không wake LLM.
Không dùng GitHub credential.

### G0.4 JEV
Đọc hồ sơ `work/done-tasks/jev-integration/` + runtime hiện có; tái dùng gateway JEV đã nghiệm thu. Không dựng JEV backend mới, không đổi provider/key/routing trong HJW.

### G0.5 Kuma — watchdog độc lập
Đo cơ chế Kuma hiện hữu. Mục tiêu là watchdog nằm NGOÀI process/user Hermes:
- ưu tiên Kuma probe trực tiếp health endpoint hoặc root-owned checker/pusher hiện có;
- token Kuma giữ root-only; KHÔNG cấp token monitor cho user Hermes nếu có cách external monitor;
- chỉ khi cơ chế hiện hữu không biểu diễn được Hermes health mới tạo tối thiểu một root-owned checker/unit, không mở public port.
Phải xác nhận cảnh báo thực sự tới kênh Owner.

### G0.6 Entry paths + stop
Liệt kê thật: cron/ticker, Telegram gateway, serve/UI, CLI/manual và đường khác nếu có.
Xác định đường nào STOP-DISPATCH bao phủ và đường nào chỉ HARD-STOP mới chặn.

Nếu Gate 0 FAIL ở G0.2 hoặc phát hiện thay đổi kiến trúc ngoài scope ⇒ DỪNG trước mutation, ghi `KQ@HJW-2B-20260923-01 DỪNG`.

## TRIỂN KHAI — CHỈ SAU GATE 0 PASS

### A. Backup/rollback
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
