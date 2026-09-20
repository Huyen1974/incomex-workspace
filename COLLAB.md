# COLLAB — Incomex Workspace · điều phối gốc

Host: GPT · Owner giao: 2026-09-20
Cấu trúc bắt buộc: root chỉ có `AGENTS.md`, `README.md`, `COLLAB.md`, `work/`.

## Đang làm
- `work/mcp-workspace/` · R03 · chốt MCP Git + VPS để quay lại công việc nghiệp vụ.
- `work/jev-integration/` · PLAN-V01 · mở việc, đang lấy ý kiến hội đồng; chưa RUN triển khai.
- `work/hermes-joint-workspace/` · HJW · Claude mở việc, chờ GPT review; nối Hermes khi R03 MACHINE_DONE.
- NEXT: Claude Code run hiện tại tiếp tục theo bridge P16 tại `work/mcp-workspace/COLLAB.md` (commit `3117f3a247d41d6023683c9a1ea8ac6b8382b5ff`) → MACHINE_DONE → tạo/connect MCP app mới một lần → nghiệm thu cuối.

## Quyết định Owner
- DROOT01 · 2026-09-20 · Mọi công việc nằm dưới `work/<work-id>/`; không đặt prompt/test/evidence/archive của công việc ở root.
- DCLIENT01 · 2026-09-20 · Tài khoản ChatGPT Pro hiện tại không có Refresh app. Sau backend/schema cuối, GPT phải tạo MCP app mới từ đúng server hiện hữu, Scan Tools/so schema trước khi Owner connect tay; giữ app cũ làm rollback tới khi app mới PASS.
- DROOT02 · 2026-09-20 · Hội đồng AI gồm 3 thành viên: GPT · Claude · Hermes. Hermes vào qua kênh Agent Data và làm việc khi nối xong; được làm gì do lệnh điều hành. Chi tiết và việc sửa AGENTS A2/A4: `work/hermes-joint-workspace/`.

## Owner cần quyết
- —
