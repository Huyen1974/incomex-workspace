# incomex-workspace

Kho làm việc CÔNG KHAI (PUBLIC từ 17/09/2026 — không commit secret; secret scanning + push protection đang bật) để Claude/ChatGPT đọc–sửa file qua đầu nối MCP "Incomex VPS" (gốc `gh`).
Commit từ GPT workspace dùng tác giả "AI via Incomex Workspace"; connector Claude hiện hữu giữ tác giả riêng. Không force-push lên `main`.

GPT dùng app "Incomex AgentData MCP — GPT Full b1gdc", root `workspace`: đọc cửa sổ nhỏ → exact edit với expected_version → commit/push → kiểm diff. File lớn hoặc HTML một dòng dùng workspace_read/search/edit; GitHub native dùng browse, PR/review và file nhỏ.

Các file `acceptance/gpt-*` là bản sao kiểm thử ngày 17/09/2026, không phải nguồn ứng dụng business.

**File thử — agent đừng đọc cả file:** `acceptance/gpt-*`, `acceptance/moved/*`, `acceptance-20260918-*.html` (~2,2 MB), `chatgpt-direct-upload-*.html` (~1,8 MB) là file thử của GPT (tác giả "AI via Incomex Workspace"), giữ nguyên chỗ vì GPT có thể còn dùng; chứng tích thử của Claude đã gom vào `_luu-tru-chung-tich-claude/` (xem INDEX.md trong đó, cũng không đọc). Đã kiểm file 314 KB và một dòng 2,21 MB, stale HEAD/SHA và commit chen ngang. App GPT cần Refresh để nhận đủ 20 tool; giữ nguyên URL/secret.

## Shared Workspace Contract — v1.0, 2026-09-18

Hai đầu nối độc lập (GPT: AgentData `workspace_*`; Claude: "Incomex VPS" `fs_*`) dùng chung nơi làm việc theo MỘT hợp đồng. Phạm vi SSOT của GitHub là các file **thuộc repo này**; KB, source các repo khác và file UI chưa quản lý trong repo không phải cùng nguồn.

1. **Tài nguyên** — `workspace`/`gh` = hai clone riêng của repo này, cùng nhánh `main`; `ui` = MỘT thư mục vật lý trên VPS (`/opt/incomex/docs/mcp-writes`, phục vụ tại `/ui-preview/mcp-writes/`); `docs` chỉ đọc.
2. **Khoá** — `ui`: một khoá `flock` chung (cùng inode) cho cả hai bên: ghi giữ exclusive, đọc giữ shared; chờ ngắn rồi trả BUSY (`WORKSPACE_BUSY` / `[DENIED:busy]`) kèm retry, không treo. Snapshot 5 phút của sổ git `ui` gom cả thay đổi do GPT ghi thẳng: đó là **lịch sử chung**, không phải rác để rollback. `main`: không cần khoá chung — bảo vệ bằng push non-force + kiểm HEAD.
3. **Phiên bản** — mọi sửa/ghi đè/di chuyển/sao chép mang `expected_version` (hash nội dung đã đọc) và, với Git, `expected_head`/`expected_HEAD` (commit đã đọc). Lệch → từ chối có mã (`VERSION_CONFLICT` / `[DENIED:version_mismatch|head_mismatch]`), đọc lại rồi sửa trên bản mới; không lấy HEAD mới để hợp thức hoá yêu cầu cũ.
4. **Commit/push** — trong vùng khoá: fetch/pull → kiểm HEAD + phiên bản → chuẩn bị → guard → commit ĐÚNG các file của thao tác (không commit lẫn file người khác) → push fast-forward, không bao giờ force. Giao dịch nhiều file = validate tất cả trước, một commit, lỗi ở op nào báo op đó và không đổi gì.
5. **Retry & mất phản hồi** — mỗi thao tác ghi có khoá idempotency (Claude: `operation_id`; GPT: `upload_id`/commit idempotent — `operation_id` cho edit/transaction còn OPEN): cùng id + cùng payload = trả kết quả cũ, không commit lần hai; khác payload = từ chối. Push bị từ chối chắc chắn → chỉ phục hồi thay đổi của chính thao tác. Mất mạng/timeout → `OUTCOME_UNKNOWN`/`RECOVERY_REQUIRED` + id; kiểm journal/commit/remote trước, không rollback hay push lại mù.
6. **Xuất công khai** — repo này PUBLIC và `ui` là trang web: nội dung đi vào bằng bất kỳ đường nào (write/edit/copy/import/transaction) đều qua kiểm bí mật; gốc `code` (mã hạ tầng) không bao giờ là nguồn sao chép.
7. **Chi phí** — tìm rồi sửa ngay khi đủ ngữ cảnh; đọc theo cửa sổ; copy/move/transaction server-side; inspect trước ảnh; kết quả dài có cursor/continuation, chỉ đọc tiếp khi cần.

Hướng dẫn riêng từng đầu nối: GPT `docs/WORKSPACE_TOOLS.md` (repo agent-data); Claude `claude-mcp/00-NHAN-THU-MUC.md` + báo cáo KB `knowledge/current-state/reports/mcp-incomex-vps-nang-cap-fs-roots-2026-09-17.md` §12.
