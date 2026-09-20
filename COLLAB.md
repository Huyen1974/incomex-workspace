# COLLAB — Incomex Workspace · điều phối gốc

Host: GPT · Owner giao: 2026-09-20
Cấu trúc bắt buộc: root chỉ có `AGENTS.md`, `README.md`, `COLLAB.md`, `work/`.

## Đang làm
- `work/mcp-workspace/` · R03 · chốt MCP Git + VPS để quay lại công việc nghiệp vụ.
- `work/jev-integration/` · PLAN-V01 · mở việc, đang lấy ý kiến hội đồng; chưa RUN triển khai.
- `work/hermes-joint-workspace/` · HJW · Claude mở việc, chờ GPT review; nối Hermes khi R03 CLOSED.
- `work/vps-clean-20-9-26/` · VPSC · Claude mở việc: đĩa VPS 87% (trống 13GB, ~3 tuần chạm 95%) — PROMPT khảo sát chỉ đọc chờ GPT review; xoá thật chờ R03 CLOSED.
- NEXT: R03 backend đã MACHINE_DONE/frozen. Tạo đúng MỘT MCP app GPT mới từ Full All hiện hữu → Scan theo cổng `work/mcp-workspace/COLLAB.md` → Owner Connect tay → reconnect Claude/open phiên mới → bài 9 bước × 4 surface + VPS/CROSS → CLOSED.

## Quyết định Owner
- DROOT01 · 2026-09-20 · Mọi công việc nằm dưới `work/<work-id>/`; không đặt prompt/test/evidence/archive của công việc ở root.
- DCLIENT01 · 2026-09-20 · Tài khoản ChatGPT Pro hiện tại không có Refresh app. Sau backend/schema cuối, GPT phải tạo MCP app mới từ đúng server hiện hữu, Scan Tools/so schema trước khi Owner connect tay; giữ app cũ làm rollback tới khi app mới PASS.
- DROOT02 · 2026-09-20 · Hội đồng AI gồm 3 thành viên: GPT · Claude · Hermes. Hermes vào qua kênh Agent Data và làm việc khi nối xong; được làm gì do lệnh điều hành. Chi tiết và việc sửa AGENTS A2/A4: `work/hermes-joint-workspace/`.

## Owner cần quyết
- —
