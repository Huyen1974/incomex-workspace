# HERMES REVIEW — JEV Integration trước triển khai

Bạn đang là **Reviewer kỹ thuật độc lập**, KHÔNG phải Agent triển khai ở lượt này.

## Cửa vào bắt buộc
Đọc theo thứ tự:
1. `AGENTS.md`
2. `work/jev-integration/COLLAB.md` — đặc biệt A0, D01–D08, P06–P07
3. `work/jev-integration/view.html`

GitHub/workspace là nguồn tài liệu chuẩn. Không tự sửa production, không cài package, không tạo secret, không reload nginx/systemd/container trong lượt review này.

## Mục tiêu Owner đã chốt
1. Cắm JEV để GPT và Claude có thêm một nguồn **tham khảo** khi ra quyết định; nếu Chat/Work/Cowork dùng được thì càng tốt.
2. JEV phải được dùng tự nhiên bằng cơ chế mặc định/dễ nhớ như Skill, tool description, hook nhắc ở CLI; JEV không phải chữ ký cho phép/chặn.
3. V0 chỉ dùng Jev qua OpenRouter.
4. Chia 2 bước: OpenAI trước (GPT Work + Codex + thử ChatGPT Chat), Claude sau; nền chung phải tái dùng.
5. Ưu tiên **dùng phần mềm có sẵn, tối thiểu code**.
6. Ưu tiên **giám sát và phát hiện lỗi** hơn tối ưu provider/chi phí.
7. Nếu cần secret: dùng **GSM theo cơ chế hiện có**. Agent triển khai được Owner cho phép tự tạo/đọc secret GSM. Không plaintext trong repo/đĩa bền vững.
8. Chi phí OpenRouter hiện không phải vấn đề cần tối ưu; Owner nạp khoảng 20 USD/lần, rủi ro mất thời gian quan trọng hơn.

## Phương án hội đồng hiện đã gần chốt
- Package chính: `itsmostafa/typesafe-mcp` (MIT), pin version/tag/commit phù hợp.
- Package expose đúng một MCP tool `evaluate(state, questions)`, hỗ trợ `OPENROUTER_API_KEY`, validate request cục bộ, retry 429/529, trả lỗi API khác cho agent.
- Package là **stdio MCP**, không phải remote HTTP MCP.
- Với ChatGPT/Work cần một **bridge stdio → remote MCP/HTTP có sẵn**, sau nginx/URL xác thực tương tự hạ tầng hiện hành. Không tự viết bridge/server nếu chưa chứng minh không có đồ phù hợp.
- Codex có thể dùng cùng remote endpoint nếu bề mặt/plugin hiện hành hỗ trợ; nếu local stdio là đường chính chủ và đơn giản hơn thì chỉ đề xuất sau khi đối chiếu với mục tiêu “một cổng dùng chung”.
- Một `SKILL.md` mỏng dùng chung: khi nào nên hỏi JEV, khi nào không, cách hỏi, và kết quả chỉ để tham khảo. Tái dùng usage guidance upstream, không tự phát minh dài dòng.
- Health check phải gọi **một câu JEV thật** và nhận được `answers`; HTTP 200/port open không đủ.
- Nếu JEV lỗi: GPT/Claude phải thấy rõ “không có tham khảo JEV” và tiếp tục tự quyết. Không success giả, không chặn công việc.
- V0 nghiệm thu lỗi bằng lỗi thật dễ tạo: request sai khuôn, model sai, auth sai/secret test phù hợp; chỉ viết thêm wrapper nếu package/bridge thực sự im lặng.

## Việc bạn cần REVIEW trên VPS thật
Chỉ khảo sát/đọc, không triển khai:

### R1 — Package
- Kiểm tra `itsmostafa/typesafe-mcp` có phù hợp với Linux/architecture/runtime hiện tại không.
- Xác nhận chính xác cách pin version/release/commit để rollback được.
- Xác nhận OpenRouter path/model behavior hiện tại và biến môi trường cần thiết.
- Xem có blocker nào khiến package không phù hợp làm lõi V0 không. Nếu có, nêu đúng blocker và tối đa 1 phương án thay thế.

### R2 — Remote MCP bridge
- Xác định trên VPS hiện đã có bridge/runtime nào dùng được cho stdio → remote MCP hay chưa.
- Nếu chưa có, khảo sát **tối đa 2** giải pháp mã nguồn mở/mature hiện có; chọn 1 giải pháp ít công, ít code, dễ rollback nhất.
- Phải trả lời rõ: bridge có giữ nguyên MCP tool schema/error hay làm biến dạng? Có stream/session/auth gì cần chú ý với ChatGPT plugin/Work không?
- Không tự viết bridge.

### R3 — GSM / secret path
- Kiểm tra cơ chế GSM hiện hữu đang nạp secret vào VPS (đã từng dùng cho MCP workspace).
- Đề xuất flow tối thiểu: GSM → runtime env/tmpfs → process, không plaintext bền vững.
- Xác nhận Agent triển khai có đủ quyền create/read GSM như Owner nói; nếu có thiếu quyền kỹ thuật cụ thể thì nêu đúng thiếu gì.
- Không tạo secret trong lượt review.

### R4 — Service / nginx / isolation
- Xác định chỗ chạy hợp lý theo mẫu hiện có: container hay systemd/process riêng; ưu tiên tái dùng pattern đã vận hành.
- Đề xuất URL/path/auth tối thiểu cho remote MCP, không làm thay đổi TEST20/Full All.
- Xác định egress chỉ cần OpenRouter và inbound chỉ cho client cần dùng; không thiết kế firewall phức tạp nếu hạ tầng hiện tại chưa cần.

### R5 — Observability và lỗi
- Với package + bridge được chọn, lỗi nào đã tự nổi lên cho agent/log?
- Health check thực tế nên chạy bằng cơ chế sẵn có nào trên VPS?
- Khi upstream/OpenRouter lỗi, đảm bảo client thấy tool error/unavailable thay vì “đã tham khảo JEV”.
- Chỉ đề xuất code bổ sung nếu chỉ ra được **một lỗi im lặng cụ thể** mà đồ có sẵn không phát hiện.

### R6 — Bề mặt OpenAI Bước 1
- Đánh giá cách cắm tối thiểu cho:
  - GPT Work
  - Codex
  - ChatGPT Chat nếu hỗ trợ
- Phân biệt rõ cái nào bạn đã kiểm trên tài liệu/hạ tầng, cái nào phải nghiệm thu client-side sau deploy.
- Không triển khai client trong lượt này.

### R7 — Acceptance
Đề xuất checklist ngắn để Agent triển khai chứng minh:
- gọi JEV thật trả `answers`;
- 1–2 lỗi thật được client nhìn thấy;
- client vẫn tiếp tục quyết định khi JEV unavailable;
- ca không nhắc chữ “JEV” nhưng bounded decision phù hợp thì model tự gọi theo skill/tool guidance;
- ca không phù hợp thì không gọi thừa;
- rollback package/bridge/service rõ ràng.

## Câu hỏi cần bạn trả lời dứt khoát
1. Kiến trúc “typesafe-mcp stdio + bridge có sẵn + nginx + GSM” có khả thi trên VPS hiện tại không?
2. Bridge cụ thể nào bạn khuyên dùng và vì sao?
3. Có cần viết code riêng ở Bước 1 không? Nếu có, đúng phần nào và vì sao đồ có sẵn không đủ?
4. Có blocker nào phải xử lý trước khi giao Agent không?
5. Kết luận cuối: **GO / GO WITH ADJUSTMENT / BLOCK**.

## Định dạng trả lời
Ngắn nhưng cụ thể:
1. Kết luận 3–5 dòng.
2. Bảng: hạng mục | hiện trạng thật | đề xuất | blocker.
3. Bridge khuyến nghị + secret flow GSM.
4. Checklist triển khai/rollback.
5. Kết luận GO/ADJUST/BLOCK.

Không mở rộng sang Zep/Graph/Cognee/Hermes orchestration. Không thiết kế lại mục tiêu. Không triển khai trong lượt review này.
