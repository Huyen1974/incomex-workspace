# COLLAB — JEV Integration

Host: GPT Chat
Host_ID: GPT-JEV-20260920-A
Owner giao mở việc: 2026-09-20
HTML chính: `view.html`

## Phạm vi hiện tại
- DRAFT kiến trúc + kế hoạch tích hợp JEV để hội đồng AI phản biện.
- Chưa triển khai runtime, chưa sửa production, chưa tạo/publish plugin, chưa đưa secret/API key vào repo.
- Không tạo `PROMPT.md` cho tới khi scope đủ đồng thuận và Owner quyết RUN.

## Quyết định Owner
- D01 · 2026-09-20 · Chia công việc thành 2 bước:
  1. Bước 1: tích hợp JEV với hệ OpenAI; ưu tiên GPT Work + Codex, thử ChatGPT Chat nếu bề mặt hỗ trợ.
  2. Bước 2: tích hợp cùng nền JEV với Claude Code CLI + Claude/Cowork + Claude Chat nếu bề mặt hỗ trợ.
- D02 · 2026-09-20 · Những phần nền dùng chung cho Bước 2 phải được chuẩn bị ngay từ Bước 1 để không dựng lại backend.

## Đề xuất đang mở
### P01 · GPT Chat · OPEN
- Based_on: `3c28198b5e0ae324c9c808a48eb71efe2d1bec0a`
- Scope: `view.html` · PLAN-V01
- Chưa đọc/kiểm trực tiếp: runtime VPS dự kiến cho gateway; thao tác bind thực tế trên từng client.
- Đề nghị: dùng một `Incomex JEV Gateway` trung lập client, remote MCP, mặc định gọi OpenRouter Decisions API/JEV; Bước 1 đóng gói cho OpenAI bằng Plugin = Skill + MCP, Bước 2 tái dùng cùng gateway cho Claude.
- Lý do: một backend, một schema tool, một nơi giữ auth/log/version; client-specific guidance để ở skill/plugin thay vì nhét vào lõi JEV.
- Áp: SAME_COMMIT
- Host response: chờ Founder/Reviewer phản biện; chưa ACCEPT.

## Câu hỏi hội đồng
- Q01 · Có đồng ý `Incomex JEV Gateway` là lớp chung duy nhất cho cả OpenAI và Claude không?
- Q02 · Bước 1 tối thiểu nên expose 2 tool (`jev_decide`, `jev_batch`) hay thêm ngay `jev_review`?
- Q03 · Skill OpenAI nên chỉ hướng dẫn lúc nào gọi JEV, hay ngay Bước 1 đã thêm Codex hook bắt buộc review một số tool call?
- Q04 · Tiêu chí PASS của ChatGPT Chat: nếu plugin không xuất hiện ở Chat nhưng Work + Codex PASS thì có chốt Bước 1 không? D01 hiện cho phép.
- Q05 · Có pin model `typesafe/jev-1.13` trong giai đoạn nghiệm thu và chỉ chuyển `jev-latest` sau khi có policy version/rollback không?

## Owner cần quyết
- — Chưa có. Chờ hội đồng xử lý P01/Q01–Q05 trước.

## NEXT
- Founder/Reviewer đọc `AGENTS.md` → file này → `view.html`, rồi tạo Pxx theo đúng scope.
- Khi không còn P OPEN/OWNER liên quan, Host tổng hợp phương án; Owner mới quyết triển khai.
