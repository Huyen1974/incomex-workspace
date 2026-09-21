# PROMPT — HVU.B3 · Vừa làm + Đang làm tự động theo từng việc

RUN_ID: HVU-B3-20260921-01
Host: GPT Chat · `GPT-HVU-20260921-A`
Executor_Surface: Codex/GPT Work
Mục tiêu/semantics chuẩn: AGENTS A9 + `work/hpml-view-for-user/COLLAB.md` §0 và Contract B3.

## 0. Cổng trước mutation
1. Đọc AGENTS → COLLAB việc này → PROMPT → README §11–§12.
2. Commit cuối chạm PROMPT phải khớp READY trong COLLAB; lệch → DỪNG.
3. B2/B2.1 đang production và đã PASS: không redesign UI, không thay webhook/backstop/retention nếu không cần cho adapter B3.
4. Khảo sát runtime thật của cả hai gateway trước khi sửa: Claude gateway/FastMCP và Agent-data JSON-RPC. Ghi rollback point từng gateway. Không đoán client identity.
5. Mã/runtime là VPS SSOT theo README §11; workspace chỉ giữ tài liệu điều hành.

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

## 3. Vừa làm — Git memory per task
- Mọi commit do gateway tạo phải override **author name** bằng display label server-side; email giữ fixed gateway email hiện hành. Caller không được điều khiển author.
- Áp cho tất cả đường ghi/commit hiện có: edit/write/import/upload final/copy/move/transaction/restore và write chạy qua task queue. Với job async, identity phải được inject ẩn vào request/job lúc enqueue để worker commit đúng surface; không đổi schema tool công khai chỉ để AI phải truyền surface.
- Commit có thể chạm nhiều task → cùng author trở thành last actor của từng task đó.
- B2 `sync.py` đổi nguồn `lastActors`: commit mới nhất chạm task, đọc Git author name/provenance. Author legacy chung `AI via Incomex Workspace` / `Claude via MCP` hoặc commit không đủ provenance → unknown/xám.
- **Per-task persistence bắt buộc:** task A không đổi last actor khi commit task B. Không TTL. Commit tiếp theo chạm A mới thay A.
- Không cần trailer `Surface:`; không parse `[GPT]`, `[Claude]` hay subject để đoán actor.

## 4. Đang làm — presence per surface × task
- Tạo một helper chung `extract_work_ids(tool,args)`: chỉ nhận path rõ `work/<id>/...`; transaction/copy/move có thể ra nhiều id; list/search toàn `work/` không đánh dấu.
- Khi tool call bắt đầu, gateway cập nhật `(surface_key, display_label, work_id, last_seen)`; throttle ghi tối đa 1 lần/30 giây/cặp.
- State nhỏ/bounded trên VPS, ưu tiên tái dùng state/service hiện hữu. Không Git, không lịch sử vô hạn, không DB nghiệp vụ mới. Nếu hai container không chia sẻ file an toàn, dùng một internal-only receiver hiện hữu/nhỏ, có auth nội bộ; không mở public write endpoint.
- Async task/job: lưu hidden `surface_key + work_ids` cùng job; queued/running dùng heartbeat hiện hữu để giữ active; terminal thì ngừng.
- **Commit success transition:** sau push thành công, clear presence của chính surface trên các task commit vừa chạm. Surface khác đang active trên cùng task không bị clear. Nếu clear trực tiếp thất bại, adapter B2 khi thấy commit mới phải clear cùng surface/task như fallback.
- TTL mặc định 10 phút. Presence mất sau reboot là chấp nhận được.

## 5. Truyền xuống UI
- `Vừa làm`: đi cùng Git/B2 snapshot; webhook thường vài giây, backstop <=15 phút.
- `Đang làm`: xuất một state/public JSON chỉ đọc đã sanitize (hoặc endpoint read-only cùng host), atomic và bounded. UI poll 15–30 giây.
- UI bảng Tình trạng không còn 6 hàng hard-code: union các display label thật đã gặp ở last actor hoặc presence; nhãn chưa biết hiện nguyên văn. Có thể có alias hiển thị đẹp nhưng alias không quyết identity.
- Dưới bảng phải hiện đúng ghi chú:
  - **Vừa làm:** “Lần ghi Git thành công gần nhất của riêng việc này; giữ nguyên cho tới lần ghi tiếp theo vào chính việc.”
  - **Đang làm:** “Có hoạt động qua gateway trong 10 phút gần nhất; xám = không thấy tín hiệu gần đây.”
  - “SSH/local ngoài gateway có thể không hiện Đang làm.”
- Khi surface S commit task A: UI phải có thể thấy A `Vừa làm=S`; `Đang làm=S` tắt ngay/ở poll kế tiếp. Tool call sau đó của S trên A làm Đang làm sáng lại.

## 6. Warning A9 — phụ, không được làm chậm lõi B3
- Khi commit `COLLAB.md`, nếu có thể gọi/tái dùng parser A9 hiện hành mà không copy luật, trả warning-only cho format READY/KQ/Owner cần quyết.
- Nếu phải nhân đôi parser hoặc mở coupling lớn, ghi OPEN và bỏ qua trong B3; actor/presence vẫn phải PASS.

## 7. Acceptance — bắt buộc kiểm thực tế
1. Regression B2/B2.1: webhook, backstop, 3-revision retention, last-good, UI stages/HTML vẫn PASS.
2. Identity: ghi lại nhãn thật quan sát được sau deploy. Synthetic test chỉ chứng minh code; không được dùng thay live identity.
3. Có ít nhất một live call qua Agent-data gateway và một live call qua Claude gateway. Nếu Agent không tự tạo được live call ở surface kia, triển khai code + synthetic test và ghi rõ `LIVE_CROSS_SURFACE_PENDING`; Host sẽ gọi thật sau, không giả PASS.
4. **Memory per-task:** X commit task A → A last=X; Y commit task B → A vẫn X, B=Y; Z commit A → A=Z.
5. **Presence:** X gọi read/search/edit scoped A → A active X trong <=30–60s; commit A của X → active X clear và last=X; gọi tiếp → active lại.
6. TTL test dùng cấu hình rút ngắn trong môi trường test → tự xám; production giữ 10 phút.
7. Hai surface cùng active trên A: commit của X không được xoá Y.
8. Presence không tạo commit, không làm `data/revisions` tăng, state có trần kích thước/GC entry cũ.
9. Commit legacy/unknown không được gán nhầm surface. Direct SSH/local ghi rõ giới hạn.
10. Nginx/build/health check và rollback point PASS trước deploy.

## 8. Báo cáo
- Không tạo progress file mới.
- Cập nhật COLLAB việc này: nhãn client thật đã thấy, runtime refs, acceptance PASS/OPEN.
- Ghi `KQ@HVU-B3-20260921-01 XONG` chỉ khi core actor + presence đã chạy production và acceptance có bằng chứng; nếu cross-surface live còn chờ thì dùng `DỪNG` hoặc trạng thái OPEN phù hợp, không gọi XONG giả.
- Kết thúc một dòng: `XONG · HVU.B3 · <refs>` hoặc `DỪNG · HVU.B3 · <lý do>`.
