# PROMPT — HVU.B3-RERUN · Vừa làm + Đang làm tự động theo từng việc

RUN_ID: HVU-B3-RERUN-20260921-02
Host: GPT Chat · `GPT-HVU-20260921-A`
Executor_Surface: Codex/GPT Work
Mục tiêu/semantics chuẩn: AGENTS A9 + `work/hpml-view-for-user/COLLAB.md` §0 và Contract B3.

## 0. Cổng trước mutation
1. Đọc AGENTS → COLLAB việc này → PROMPT → README §11–§12.
2. Commit cuối chạm PROMPT phải khớp READY trong COLLAB; lệch → DỪNG.
3. B2/B2.1 đang production và đã PASS: không redesign UI, không thay webhook/backstop/retention nếu không cần cho adapter B3.
4. Khảo sát runtime thật của cả hai gateway trước khi sửa: Claude gateway/FastMCP và Agent-data JSON-RPC. Ghi rollback point từng gateway. Không đoán client identity.
5. Mã/runtime là VPS SSOT theo README §11; workspace chỉ giữ tài liệu điều hành.
6. BẮT BUỘC P16/P17: pre/post tools/list canonical hash, schema/hash, serverInfo/version, auth/URL và tool request/response/error semantics phải giữ nguyên; không bump version. Git author attribution được phép đổi theo §3 vì không đổi client-visible MCP contract. Deploy Agent-data trước, PASS rồi mới Claude gateway.
7. **State machine rollout, không được tự diễn giải:** sau mỗi deploy chỉ quan sát container/health. `STARTING` = compose đã hoàn tất, container còn running và chưa healthy, elapsed <5 phút → KHÔNG gọi MCP, KHÔNG rollback, KHÔNG cancel/restart/chạy compose chồng; poll health 5–10s. `TỐT` = healthy ổn định 2 lần liên tiếp cách nhau >=10s, sau đó initialize/tools/list/serverInfo giống baseline và live read + live write PASS. `HỎNG` = container exited/dead, hoặc >=5 phút chưa healthy, hoặc đã healthy ổn định nhưng contract khác / live read-write fail 3 lần liên tiếp trong 30s. Chỉ khi HỎNG mới rollback bằng đúng MỘT lệnh đã ghi trước; sau rollback cũng chờ healthy theo cùng state machine rồi mới báo.

## 1. Mục tiêu đo được
Sau B3, dashboard phải tự trả lời theo từng `work/<id>/`:
- **Vừa làm:** surface có commit Git thành công gần nhất chạm đúng task. Không TTL; giữ cho tới commit sau chạm đúng task.
- **Đang làm:** surface có hoạt động gateway trên đúng task trong 10 phút gần nhất hoặc async job còn running.
AI/User không phải thêm bước báo tay, heartbeat Git hay tiền tố commit.

## 2. Identity tại hai gateway
### 2.1 Claude gateway
- Dùng client/session metadata của FastMCP Context; ưu tiên `clientInfo.name`, giữ version riêng nếu hữu ích.
- Sanitize label: Unicode printable, bỏ control/newline, giới hạn hợp lý (ví dụ 80 ký tự). Không nhận label từ arguments của tool.

### 2.2 Agent-data Workspace gateway
- Hiện `initialize` bỏ qua `params.clientInfo`; sửa để ghi nhớ clientInfo theo transport/session.
- Khóa phiên ưu tiên `Mcp-Session-Id`; nếu không có thì dùng fingerprint server-side đã có từ route + client host + User-Agent. Không log raw secret/header nhạy cảm.
- Mọi `tools/call` lấy identity từ session store; fallback User-Agent sanitize nếu không có clientInfo. Session store bounded/TTL và được phép mất khi restart.
- Không map cứng sang GPT/Claude/Codex/Hermes. Display label = nhãn thật đã thấy; nếu hai client trùng nhãn thì coi cùng surface, không tự bịa cách tách.
- Tạo `surface_key` server-side ổn định từ provenance/label để state dùng key an toàn; UI chỉ thấy display label đã sanitize.

## 3. Vừa làm — Git author là SSOT per task
- Tại mọi đường commit của hai gateway, **author name = display label server-side**; caller không truyền/điều khiển author. **Giữ nguyên author email cố định hiện có của từng gateway** và giữ nguyên commit message/committer policy hiện hành.
- Agent-data hiện có 3 điểm commit; Claude gateway phải rà đủ mọi helper/đường commit hiện hành. Gom helper nếu an toàn để không sót, nhưng không đổi tool schema/result.
- Async queue/job phải mang hidden identity từ request/session tới worker để commit dùng đúng author; không thêm input field cho AI.
- B2 `sync.py`: lấy commit mới nhất chạm task và đọc `%an` + `%ae`. Chỉ khi `%ae` thuộc email gateway đã cấu hình thì `lastActors=[%an]`; email khác → unknown/xám. Không parse `[GPT]`, `[Claude]` hay subject.
- **Per-task persistence bắt buộc:** task A không đổi last actor khi commit task B. Không TTL. Commit tiếp theo chạm A mới thay A.
- Bỏ/không triển khai `writers/provenance` ledger bền trên VPS. Candidate đã có `hvu_signals.py` thì chỉ giữ phần session identity/presence cần cho §4.
- H12: author attribution là Git metadata server-side, không làm client cần rediscover tools. Có thể làm rõ comment H12 theo câu này; **không đổi `CONNECTOR_SCHEMA_VERSION`/`SERVER_VERSION`**.

## 4. Đang làm — presence per surface × task
- Tạo một helper chung `extract_work_ids(tool,args)`: chỉ nhận path rõ `work/<id>/...`; transaction/copy/move có thể ra nhiều id; list/search toàn `work/` không đánh dấu.
- Khi tool call bắt đầu, gateway cập nhật `(surface_key, display_label, work_id, last_seen)`; throttle ghi tối đa 1 lần/30 giây/cặp.
- State nhỏ/bounded trên VPS, ưu tiên state path/volume hiện hữu ngoài webroot. Không Git, không lịch sử vô hạn, không DB nghiệp vụ mới. Nếu hai gateway không chia sẻ state an toàn, mỗi gateway có store nhỏ riêng để B2 merge; chỉ khi bất khả thi mới dùng internal-only receiver có auth, không public write endpoint.
- Async task/job: lưu hidden `surface_key + work_ids` cùng job; queued/running dùng heartbeat hiện hữu để giữ active; terminal thì ngừng.
- **Commit success transition:** sau push thành công, clear presence của chính surface trên các task commit vừa chạm. Surface khác đang active trên cùng task không bị clear. Nếu clear trực tiếp thất bại, adapter B2 khi thấy commit mới phải clear cùng surface/task như fallback.
- TTL mặc định 10 phút. Presence mất sau reboot là chấp nhận được.

## 5. Truyền xuống UI
- `Vừa làm`: B2 đọc Git author name/email của commit cuối chạm task; webhook thường vài giây, backstop <=15 phút.
- `Đang làm`: xuất một state/public JSON chỉ đọc đã sanitize (hoặc endpoint read-only cùng host), atomic và bounded. UI poll 15–30 giây.
- UI bảng Tình trạng không còn 6 hàng hard-code: union các display label thật đã gặp ở last actor hoặc presence; nhãn chưa biết hiện nguyên văn. Có thể có alias hiển thị đẹp nhưng alias không quyết identity.
- Dưới bảng phải hiện đúng ghi chú:
  - **Vừa làm:** “Lần ghi Git thành công gần nhất của riêng việc này; giữ nguyên cho tới lần ghi tiếp theo vào chính việc.”
  - **Đang làm:** “Có hoạt động qua gateway trong 10 phút gần nhất; xám = không thấy tín hiệu gần đây.”
  - “SSH/local ngoài gateway có thể không hiện Đang làm.”
- Khi surface S commit task A: UI phải có thể thấy A `Vừa làm=S`; `Đang làm=S` tắt ngay/ở poll kế tiếp. Tool call sau đó của S trên A làm Đang làm sáng lại.

## 6. Warning A9 — HOÃN khỏi B3
P16 yêu cầu giữ nguyên tool output/behavior contract. Không thêm warning/linter vào tool result trong B3. Việc này mở riêng sau nếu cần.

## 7. Acceptance — bắt buộc kiểm thực tế
1. **Contract freeze:** pre/post tools/list canonical hash + schema/hash + serverInfo/version giống hệt ở từng gateway; auth/URL và tool result/error semantics không đổi. Git author name được phép khác theo client label, email gateway phải giữ nguyên. Regression B2/B2.1 vẫn PASS.
2. Identity: ghi lại nhãn thật quan sát được sau deploy. Synthetic test chỉ chứng minh code; không được dùng thay live identity.
3. Có ít nhất một live call qua Agent-data gateway và một live call qua Claude gateway. Nếu Agent không tự tạo được live call ở surface kia, triển khai code + synthetic test và ghi rõ `LIVE_CROSS_SURFACE_PENDING`; Host sẽ gọi thật sau, không giả PASS.
4. **Memory per-task:** X commit task A → A last=X; Y commit task B → A vẫn X, B=Y; Z commit A → A=Z.
5. **Presence:** X gọi read/search/edit scoped A → A active X trong <=30–60s; commit A của X → active X clear và last=X; gọi tiếp → active lại.
6. TTL test dùng cấu hình rút ngắn trong môi trường test → tự xám; production giữ 10 phút.
7. Hai surface cùng active trên A: commit của X không được xoá Y.
8. Presence không tạo commit, không làm `data/revisions` tăng, state có trần kích thước/GC entry cũ.
9. Commit legacy/unknown/SSH có author email không thuộc gateway → actor unknown; không giữ/gán nhầm surface.
10. Nginx/build/health check và rollback point PASS trước deploy.

## 8. Báo cáo
- Không tạo progress file mới.
- Cập nhật COLLAB việc này: nhãn client thật đã thấy, runtime refs, acceptance PASS/OPEN.
- Ghi `KQ@HVU-B3-RERUN-20260921-02 XONG` chỉ khi core actor + presence đã chạy production và acceptance có bằng chứng; nếu cross-surface live còn chờ thì ghi `KQ@HVU-B3-RERUN-20260921-02 DỪNG · LIVE_CROSS_SURFACE_PENDING`, không gọi XONG giả.
- Kết thúc một dòng: `XONG · HVU.B3 · <refs>` hoặc `DỪNG · HVU.B3 · <lý do>`.
