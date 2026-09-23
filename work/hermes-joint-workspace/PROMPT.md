# PROMPT — HJW.2B · Hermes Phase 1

RUN_ID: HJW-2B-20260923-01
STATUS: DRAFT — KHÔNG RUN cho tới khi Host ghi READY@ đúng SHA của file này

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
- Đường chính cho gate LLM: pre-run `--script`; dòng stdout cuối `{"wakeAgent": false}` = không gọi LLM, `{"wakeAgent": true, "context": {...}}` = wake + truyền context.
- `--monitor-script` chỉ dự phòng nếu có lý do đo được.
- Không nâng cấp Hermes trong RUN này. Nếu primitive bắt buộc thiếu ⇒ DỪNG và báo.

### G0.2 Agent Data relay + secret boundary
Đo nhưng không in giá trị secret:
- trạng thái `hermes-agentdata-relay.service`, bind/listen và cổng đích;
- nguồn auth hiện tại của relay;
- tên biến env hiện hữu của Hermes (chỉ tên, không value), xác nhận có/không `AGENT_DATA_API_KEY` / `AGENT_DATA_URL`;
- khả năng gọi `workspace_*` qua relay 127.0.0.1:6533 mà client Hermes KHÔNG phải cầm Agent Data key.

Quyết định bắt buộc:
- Nếu relay hiện hữu cung cấp được `workspace_*` mà không lộ key cho user/process Hermes ⇒ tiếp tục và loại `AGENT_DATA_API_KEY` + URL nhạy cảm tương ứng khỏi môi trường Hermes-readable; key chỉ ở nguồn root/relay tối thiểu.
- Nếu relay cần chính key đó ở phía Hermes, hoặc muốn sửa backend Agent Data / dựng proxy mới mới làm được ⇒ DỪNG, ghi blocker. KHÔNG chấp nhận giữ write-capable Agent Data key trong Hermes env chỉ vì Git rollback được.

### G0.3 Đọc SSOT không token
Xác nhận công thức:
`git ls-remote <public repo> HEAD` → SHA → đọc `work/*/COLLAB.md` tại đúng SHA bất biến.
Không xác định được SHA/freshness ⇒ fail closed, không wake LLM.
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
1. Khai `workspace_*` trong Hermes qua relay 127.0.0.1:6533.
2. Loại Agent Data key khỏi môi trường user/process Hermes theo G0.2; không làm hỏng relay.
3. Nạp skill/luật mỏng: mỗi task đọc AGENTS → A0 → vai; Agent chỉ chạy khi READY + RUN_ID hợp lệ; Reviewer không tự triển khai; Host chỉ khi Owner giao.
4. Cắm JEV qua gateway hiện hữu như nguồn tham khảo, không quyền phê duyệt/chặn.

### C. Assignment Phase 1 — capability confinement
Phase 1 chỉ nghiệm thu execution assignment trong chính `work/hermes-joint-workspace/`; sau PASS mới tổng quát A9 ở HJW.4.

Gate deterministic chạy khoảng 2 phút/lần:
- resolve HEAD → đọc COLLAB tại chính SHA;
- chỉ quan tâm dấu strict `ASSIGN@... to=Hermes ... state=open`;
- author/client label chỉ là telemetry/phòng vệ phụ, KHÔNG coi là authentication;
- role=Agent phải có `run=<RUN_ID>` và agent phải kiểm READY đúng SHA trước mutation;
- role=Host chỉ hợp lệ khi COLLAB có quyết định Owner giao Host;
- một assignment chỉ wake tối đa một automated LLM turn; max_parallel=1;
- Phase 1 đặt trần an toàn 24 automated LLM wakeups/24h; chạm trần ⇒ blocked + Telegram, không tự vượt;
- state runtime/dedupe có thể lưu cache/ledger, nhưng COLLAB/KQ vẫn là SSOT.

Automated turn phải dùng profile/toolset tối thiểu:
- cho phép capability cần thiết để đọc/ghi `work/**` qua relay + JEV;
- KHÔNG terminal/exec, sudo/root, secret/IAM, service control, destructive/delete;
- deny-by-default; gặp thao tác cần approval ⇒ kết thúc `blocked` + Telegram, CẤM auto-approve;
- nếu bản Hermes không enforce được capability profile/toolset tối thiểu bằng cấu hình sẵn có ⇒ DỪNG, không tự code sandbox mới.

### D. Job Phase 1
Chỉ 4 nhóm:
1. assignment gate / self-wake;
2. nhắc đúng lượt + canh RUN treo (ưu tiên script/no-agent, dedupe cảnh báo);
3. health/watchdog qua cơ chế Kuma độc lập ở G0.5;
4. stop controls.

Không làm bản tin sáng, không webhook, không sửa Owner View.

### E. Stop controls
- STOP-AUTO: `hermes pause`.
- STOP-DISPATCH: một cờ root-owned, persistent, ngoài quyền ghi user Hermes (ưu tiên `/etc/incomex/hermes-automation.stop` hoặc vị trí chuẩn hiện hữu tương đương). Tất cả HJW gate scripts phải check cờ trước wake.
- HARD-STOP: runbook root/operator dựa trên entry paths thật; phải dừng các service/process có thể khởi tạo agent và chặn run mới. Nếu inference credential runtime cần được vô hiệu hoá để ngăn manual CLI, nêu rõ cách làm/rollback; không rotate/revoke provider key trong RUN này.
- Không test HARD-STOP làm gián đoạn phiên Owner đang dùng; nếu đang active, ghi test này sang HJW.3. STOP-DISPATCH phải test trong RUN này.

## NGHIỆM THU TRONG RUN

Tối thiểu:
- relay read + write thử trong `work/hermes-joint-workspace/_thu-nghiem/hermes/`; stale expected_version bị reject;
- Hermes process/user không còn đọc được Agent Data credential sau khi relay PASS; không có GSM credential;
- JEV gọi thật trả `answers`;
- 3 tick không đổi HEAD/assignment ⇒ 0 LLM wake;
- assignment thử hợp lệ ⇒ wake/claim trong mục tiêu ≤5 phút, không chạy trùng;
- assignment cần capability ngoài allowlist ⇒ blocked + Telegram, không auto-approve;
- STOP-DISPATCH đặt ⇒ 0 automated run mới qua ít nhất 3 tick; gỡ ⇒ hoạt động lại, không chạy bù trùng;
- Kuma/external watchdog báo được tới Owner;
- secret-redaction test chỉ dùng **synthetic canary**, tuyệt đối không yêu cầu/in secret OpenRouter/Telegram/AgentData thật;
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
