# COLLAB — JEV Integration

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
- Mục tiêu: tích hợp JEV vào môi trường làm việc để phục vụ OpenAI trước, sau đó tái dùng cùng nền cho Claude, tránh dựng hai hệ riêng.
- Nhiệm vụ/phạm vi: Bước 1 cho GPT Work + Codex và ChatGPT Chat nếu hỗ trợ; Bước 2 cho Claude Code CLI + Claude/Cowork + Claude Chat nếu hỗ trợ; phần nền dùng chung phải được chuẩn bị từ Bước 1.
- Tiêu chí xong: kiến trúc/kế hoạch được hội đồng và User chốt trước RUN; triển khai từng bước dùng chung backend, không nhân đôi hạ tầng không cần thiết.
- Xác nhận User: **ĐÃ XÁC NHẬN** — Owner giao trực tiếp 2026-09-20; D01–D02 của việc này.

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

### P02 · Claude Chat · OPEN
- Based_on: `d45b1c2` · Scope: `COLLAB.md` P01 + Q01–Q05 · `view.html` PLAN-V01 §1–§10.
- Chưa kiểm trực tiếp: chưa gọi thật Jev (phiên Claude Chat không ra được openrouter.ai); chưa thử Plugin OpenAI trên client.
- Đã kiểm 2026-09-20 (docs.typesafe.ai: system-one · models · jaggedness 1.13; openrouter.ai/docs typesafe-sdk): Jev chỉ trả lời câu hỏi ĐÓNG (choice · score · noul) kèm xác suất + confidence, không viết chữ; **tiếng Anh là ngôn ngữ chính, ngôn ngữ khác nhà sản xuất khuyên tự đo trước**; state ≤32k token; đọc sát nghĩa đen, kém đếm/số/ngày/suy luận nhiều bước, state thừa làm giảm độ đúng; 0,042 USD/1 triệu token vào, ra miễn phí; OpenRouter có alias `/api/v1/systemone` (không mang chữ alpha). `claude-mcp` chạy mạng `internal: true` — không ra internet (`code:claude-mcp/docker-compose.claude-mcp.yml` dòng 136).
- Đề nghị:
  1. **Mục tiêu viết theo việc** (→ Owner): Jev = máy chấm câu hỏi đóng của hội đồng — chấm nhanh, rẻ, đều ở nhiều trạm kiểm; không thay GPT/Claude/Hermes suy nghĩ. Jev chỉ được báo DỪNG/cần xem, không bao giờ là chữ ký cho phép; hành động phá huỷ vẫn chỉ Owner.
  2. **Ba ca dùng, theo thứ tự**: UC1 soát `PROMPT.md` trước READY (từng dòng: có lệnh xoá/dừng/ghi đè/sửa prod? prompt khảo sát có lệnh hành động?). UC2 ma trận lựa chọn × nguyên tắc Owner (7 mục tiêu cốt lõi + triết lý + D04) → ô đỏ/vàng/xanh cho các lựa chọn MOW/MOT. UC3 chấm hàng loạt dữ liệu MOW/MOT — chỉ khi việc MOW/MOT tới bước 1–2 (không nhảy cóc); chạy script trên VPS để dữ liệu không đi qua ngữ cảnh LLM; người chạy dự kiến Hermes; lượt này không dựng gì cho UC3.
  3. **G0 đo tiếng Việt trước khi dựng**: 40–60 ca thật có đáp án lấy từ Git/KB (PROMPT cũ + quyết định Owner đã có lý do), so 2 cách hỏi (lời hỏi Việt / Anh trên dữ liệu Việt). PASS: UC1 bắt 100% dòng phá huỷ, báo nhầm ≤20%; UC2 khớp ≥80% phán quyết Owner, ca lệch phải ra VÀNG (confidence thấp) chứ không xanh/đỏ tự tin. Trượt → DỪNG, không dựng cổng.
  4. **Q01 PARTIAL**: đồng ý một cổng chung cho mọi client + Hermes, nhưng là dịch vụ MỎNG riêng: không nhét vào `claude-mcp` (phá cách ly mạng §3H), không vào agent-data/Full All (đang đóng băng; đổi schema là phải tạo lại app GPT); chỉ ra internet tới openrouter.ai; tái dùng khung MCP + kiểu xác thực URL bí mật đang chạy; audit theo §7 plan.
  5. **Q02 PARTIAL**: một tool `jev_evaluate` giữ nguyên hình `{state, questions}` của Jev (một lượt đã hỏi được nhiều câu) + tham số tuỳ chọn `pack=<id@version>` nạp bộ câu hỏi đã duyệt. Không tách decide/batch/review: cùng một lời gọi, tách ra là thêm từ vựng phải bảo trì; review là một bộ câu hỏi, không phải một tool.
  6. **Hướng dẫn dùng ở MỘT chỗ**: một dòng luật trong `AGENTS.md` (trạm nào gọi Jev, bộ câu hỏi nào) + MỘT tệp bộ câu hỏi có version trong thư mục này. Mọi client đã đọc AGENTS.md ở cửa vào, nên không cần Skill/Plugin riêng từng client; chỉ thêm Plugin nếu đo thấy client không gọi khi cần. Sửa cách chấm = sửa tệp, không sửa mã.
  7. **Q03**: chưa hook bắt buộc; sau pilot chạy hook chế độ chỉ ghi sổ 1–2 tuần rồi mới xét bật chặn (deny/ask, luôn đứng sau luật cứng, không bao giờ allow). **Q04**: ChatGPT Chat không để best-effort — đường app MCP tự tạo đã chạy thật (Full All 2), PASS như Work. **Q05**: ĐỒNG Ý pin `typesafe/jev-1.13`, ghi trường `model` trả về mỗi lượt; lên bản mới phải chạy lại bộ ca G0.
  8. **Khoá & dữ liệu** (→ Owner, vì là giới hạn): khoá OpenRouter RIÊNG cho Jev, nằm ở runtime VPS như khoá Hermes, hạn mức 10 USD/tháng; chưa gửi dữ liệu cá nhân (hồ sơ lao động, học viên) cho Jev ở giai đoạn này.
  9. **D01 + thứ tự** (→ Owner): gộp Bước 1+2 thành MỘT lượt: G0 → dựng cổng → cắm mọi bề mặt (GPT Chat/Work/Codex · Claude Chat/Code/Cowork · Hermes) → nghiệm thu từng bề mặt; cổng trung lập client nên Bước 2 chỉ còn cắm dây, tách hai lượt tốn thêm một vòng READY/RUN. Thứ tự liên việc: R03 CLOSED → HJW.2–3 → JEV.
  10. **PASS cuối = dùng thật**: sau cắm dây, UC1 chạy trên PROMPT kế tiếp và UC2 trên một lựa chọn MOW/MOT thật; ghi số ca Jev bắt đúng / báo nhầm. Cắm được mà không trạm nào gọi = chưa xong.
- Áp: SAME_COMMIT
- Host response: —

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
