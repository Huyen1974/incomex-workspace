# HJW — RUN12: Candidate offline trước, refresh client đúng thời điểm

RUN_ID: HJW-DECLARATION-GATE-PHASED-20261028-12
STATUS: HOST_FINAL_PENDING_READY · NO_RUN
Executor_Surface: Codex Desktop/Work (Owner giao tay SAU Host READY đúng SHA)
Task: Huyen1974/incomex-workspace · work/hermes-joint-workspace
Write_Path: repo báo cáo qua `workspace_*` D12; mã Gateway chỉ qua repo source/operator/apply đã audit, VPS-GHI CAS và Guard khi thực sự mutation production.
Read_First: AGENTS.md A0/A2/A5/A6/A9/A10 → HJW COLLAB §0, Bảng, P442–P449 → PROMPT này. **RUN11 KQ DỪNG tại P448, không tiếp tục READY cũ.**
Scope: một contract `declared_actor` tại hai Gateway AD/workspace + Claude/fs hiện hữu; giữ quyền, profile, D12 GitHub protected main, A2 quorum; không mở task, server, DB, bridge, endpoint, cron, account hoặc cấp secret mới.

## Mục tiêu và C1/C2 không đổi
AI có quyền ghi phải được tools/list hướng dẫn ngay về `declared_actor`; thiếu/sai tên trả `DECLARATION_REQUIRED` có field, ví dụ và cách tự gọi lại, 0 side effect; lần gọi hợp lệ ghi đúng một lần với receipt cả `declared_actor` (AI tự khai) và `authenticated_actor` (credential thật). Không có bước xin vé/token.
- **C1:** ít nhất một AI/client thật tự thực hiện **thiếu tên → lỗi có hướng dẫn → gửi lại đúng schema → commit/receipt** không Owner điền hộ. Unit tests không thay thế.
- **C2:** mọi client còn schema cũ/stale cần xác định rõ; ghi cách refresh thực tế, ảnh hưởng client active; không gắn PASS cho surface chưa được thử. Không bật enforcement nếu client đang ghi quan trọng chưa thể khai.
- Cả AD và FS, upload/import/queue/helper/`write_file` phải được test phủ; không coi 11 file là KPI.

## B0 — S0 chỉ preflight các điều kiện thực sự chặn sửa source
- Đọc HEAD/task/prompts và READY chính xác, STOP/VPS-GHI/Guard/diff; trả cờ sạch nếu S0 không đủ. P448 Guard PRE đã PASS nhưng phải đo mới trước **mutation production**, không dùng log cũ để hợp thức hóa.
- Recheck image/digest và runtime hashes của AD/Claude/helper P448, pin baseline, bảo toàn source Git, phục hồi/rollback byte đúng. Checkout không bằng runtime: **lấy byte runtime làm gốc patch**, không dùng latest checkout để ghi đè dịch vụ. Thiếu baseline/source/rollback ⇒ dừng trước ghi code/runtime; không tự reset/hủy môi trường live.
- Đọc tài liệu hãng: custom MCP direct, plugin published/marketplace và Codex local là ba đường khác nhau. Xác định từ manifest/config hiện hữu đường Incomex của client là loại nào, không suy từ tên plugin. **Không cần đăng nhập UI/kiểm nút Refresh lúc này** vì server chưa có schema mới để refresh. Trang chưa có phiên đăng nhập là `UI_SESSION_UNAVAILABLE`, không phải blocker để tạo candidate offline. Không thao tác GUI Codex bị công cụ cấm.
- Có quyền thì chỉ dùng native `codex mcp list`/`/mcp` hoặc app-server `mcpServerStatus/list` (read-only) để hiểu Codex local; `config/mcpServer/reload` chỉ trên bề mặt thật sự hỗ trợ và khi đến pha refresh, không dùng thay cho nút plugin Cloud. Không đặt chìa mới/đổi kết nối đang phục vụ.

## B1 — S1 patch candidate biệt lập, có sản phẩm dù chưa có UI refresh
- Dùng hai runtime/code baselines đã pin để soạn **patch nhỏ nhất** vào source repo hiện hữu có quyền, giữ nguồn và diff/hash + manifest build/rollback. Không sửa production tại bước này, không tạo service/cổng mới. Có thể dùng môi trường fixture/snapshot hiện hữu, không truy cập secret từ model.
- Một validator/schema/error contract dùng ở hai adapter, không copy chính sách vào mọi tool. Chặn source write ngay sau auth/scope, **trước staging, enqueue, idempotency preparing, commit**. Trường optional ở giai đoạn **advertise-only tương thích** nếu chọn staging; chỉ enforce sau C1/C2 readiness.
- Phủ create/edit/copy/move/transaction/restore, upload begin/append/commit, import, queue/task, helper và `write_file`; context AI khai khi bắt đầu logical write, server carry qua chunk/background. Chưa có trường trong schema cũ không được đưa client vào vòng lỗi không thể tự sửa.
- Test fixture: tools/list descriptions, empty/null/type-invalid, deny=0 mutation, retry same id, actor swap không reuse receipt, legacy journal/queued jobs, read-only unchanged, fail closed với writer chưa phân loại, rollback/Guard procedure. Ghi candidate commit/digest và checklist test PASS/FAIL vào P/KQ; test chỉ trên nguồn thử, không canary production giả.

## B2 — S2 phân loại plugin và quyết định thời điểm Refresh thực tế
- Tài liệu chính thức: https://developers.openai.com/plugins/deploy/connect-chatgpt#refresh-metadata (MCP trực tiếp **deploy/restart rồi Refresh**, chat mới); https://help.openai.com/en/articles/12584461-connecting-custom-mcp-servers-in-chatgpt (workspace-approved snapshot/tools list có thể cần admin review); https://learn.chatgpt.com/docs/plugins (plugin published/new session), https://learn.chatgpt.com/docs/extend/mcp (Codex local).
- Nếu có cửa **advertise-only** trên runtime production mà hoàn toàn tương thích client cũ, phải kiểm Guard PRE, VPS-GHI và đường rollback trước đưa nó lên; chứng minh hiện hữu tool còn ghi được. **Không bật enforcement** khi chưa biết client tương thích và một client thật nhìn/gửi được `declared_actor`; không tự thử trên các phiên làm việc đang active.
- Nếu UI native Refresh cần Owner, **chỉ lúc này** nêu **một thao tác UI chính xác**, không yêu cầu user đăng nhập/chia mật khẩu từ trước, không bảo Owner bấm Refresh cho schema chưa có. Nếu thiếu quyền truy cập/bề mặt, báo `CLIENT_REFRESH_HUMAN_ONLY`, giữ candidate + production nguyên trạng hoặc đang advertise-safe với đường lùi, dừng sạch. Đừng viết app/browser automation lách hạn chế `com.openai.codex`.
- Có thể **đánh giá trên giấy** phương án tương thích schema cũ bằng field `message` của tools đã có nếu không Refresh được, nhưng **không tự thay** contract `declared_actor` hay triển khai parser legacy nếu Host chưa quyết; ghi gọn tính khả thi và phần tool không có message.

## B3 — S3 enforce/kiểm client nếu hội đủ gate
- Client thật đã nhận metadata hoặc có native đường dùng field: chạy C1 `missing → DECLARATION_REQUIRED → tự khai lại → receipt/Git SHA`; không dùng unit tests làm C1. Báo C2 riêng từng client; không làm khách hàng hiện hữu bị mất quyền ghi.
- Chỉ sau C1 readiness, suite/fixtures đủ hai Gateway và Guard/rollback/vps lease PASS mới bật enforce đúng scope qua đường apply hiện hữu. Guard POST kiểm theo footprint. Bất kỳ lỗi: dừng/rollback bản áp mới (không lùi sản phẩm khác) và KQ DỪNG, giữ evidence.
- C1 thử production chỉ với một ghi canary vô hại trong HJW task đã duyệt, tránh đụng dữ liệu kinh doanh. Giữ các trạng thái `LIVE_NOT_TESTED`/`CLIENT_SCHEMA_STALE` trung thực, không suy Dot/Live đã có ghế/quorum riêng.

## Kết quả
- KQ@HJW-DECLARATION-GATE-PHASED-20261028-12 **XONG** chỉ khi feature hai Gateway thật sự enforce + C1 client thực + C2 đã phân loại + Guard/rollback không lỗi. Nếu mới có patch candidate/fixture PASS nhưng refresh blocked, ghi **DỪNG có kết quả**: source commit/digest, test, blocker duy nhất, next action thật, 0 lease/job tạm. Không ghi FEATURE PASS hay xin Owner bấm UI khi chưa cần.
- Ghi một P450/KQ vào duy nhất HJW COLLAB qua D12, cập nhật Bảng/NEXT_TRIGGER và giữ evidence ở nguồn, không tạo task khác. Báo Owner 3 câu: đã làm, còn thiếu gì, có cần một thao tác Owner-only không.
STEP_WALK_V1: S0 preflight+pin runtime → S1 candidate+fixture → S2 đúng loại plugin/advertise-safe rồi refresh/canary nếu khả thi → S3 enforce+Guard+C1/C2 → KQ/return. **STOP trước bất kỳ bước production thiếu Guard/lease/rollback/client safe.**
