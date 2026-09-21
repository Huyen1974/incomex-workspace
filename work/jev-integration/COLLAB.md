# COLLAB — JEV Integration

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
- Mục tiêu — **nguyên văn User 2026-09-21**:
  1. Cắm Jev để làm cơ chế tham khảo tối đa cho cả GPT và Claude (nếu có thể thì cả chat), trước mắt Jev duy nhất chỉ có nguồn chạy qua api trên openrouter.
  2. làm thế nào để các quyết định cần thiết của cả GPT/Claude có thể tham khảo Jev 1 cách tự nhiên (ví dụ ví dụ đưa vào skill bất cứ công cụ nào có sẵn mà 2 hãng (Open Ai và Anthopic) thiết lập cơ chế mặc định, dễ nhớ dễ làm.
  3. Kết quả của Jev chỉ là hỗ trợ để GPT và Claude ra quyết định. user không đặt kết quả từ Jev nhưng đánh giá đây là công cụ hữu ích và muốn Claude/GPT sử dụng nó.
- Nhiệm vụ/phạm vi: giữ D01–D02 — Bước 1 làm cho hệ OpenAI; Bước 2 tái dùng nền chung cho hệ Claude. Chỉ dùng Jev qua OpenRouter ở phạm vi hiện tại.
- Tiêu chí xong: GPT/Claude có thể gọi Jev như một nguồn tham khảo tự nhiên tại các quyết định phù hợp; Jev không trở thành quyền phê duyệt/chặn thay GPT, Claude hay User; từng bề mặt được nghiệm thu bằng gọi thật.
- Xác nhận User: **ĐÃ XÁC NHẬN** — Owner chốt lại nguyên văn 3 mục tiêu ngày 2026-09-21.

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
- D03 · 2026-09-21 · Ba mục tiêu nguyên văn ở khối A0 là phạm vi điều khiển hiện hành. Trong phạm vi này: Jev chỉ chạy qua OpenRouter; Jev là nguồn tham khảo hỗ trợ GPT/Claude ra quyết định, không phải chữ ký cho phép/chặn; mọi cơ chế skill/hook/tool phải phục vụ việc dùng Jev tự nhiên, dễ nhớ, dễ làm.
- D04 · 2026-09-21 · Ưu tiên hiện tại là **cơ chế phía Incomex + giám sát lỗi**, không tối ưu nhà cung cấp. V0 chỉ dùng OpenRouter vì đó là đường thực tế hiện có; chuyện API trực tiếp/nhà cung cấp khác chỉ xem lại khi đã vào production và mức dùng thực tế làm nó đáng quan tâm.
- D05 · 2026-09-21 · Gateway phải phát hiện lỗi và nói thật: xác thực request trước khi gửi; health-check phải nhận được `answers` Jev thật chứ không chỉ HTTP 200; lỗi phải được phân loại/log và trả rõ “lượt này không có tham khảo Jev”. GPT/Claude tiếp tục tự quyết, không chặn, không fallback im lặng, không retry mù ở V0.
- D06 · 2026-09-21 · Không coi tách OpenRouter key/routing/hạn mức riêng là điều kiện của pilot. Chi phí hiện nhỏ và OpenRouter hiện chủ yếu phục vụ Hermes; thống kê sử dụng cần thiết lấy từ telemetry của gateway. Khi triển khai chọn cách dùng credential hiện có an toàn/ít công nhất, tuyệt đối không ghi secret vào repo; chỉ tách key/routing khi có nhu cầu vận hành thực tế.
- D07 · 2026-09-21 · Nếu cần lưu/tạo secret cho JEV thì dùng **GSM theo cơ chế bí mật hiện có của hệ thống**. Agent được phép tự tạo/đọc secret trong GSM cho phạm vi việc này; không ghi plaintext secret vào repo hoặc file bền vững trên đĩa. Ngân sách OpenRouter hiện do Owner nạp khoảng 20 USD/lần và không phải biến số cần tối ưu trong pilot.
- D08 · 2026-09-21 · Ưu tiên **ghép phần mềm có sẵn, không tự viết server nếu chưa chứng minh là cần**. Ứng viên chính đã kiểm: `itsmostafa/typesafe-mcp` (MIT) — binary Go, một tool `evaluate(state, questions)`, hỗ trợ OpenRouter, validate request cục bộ, retry 429/529, lỗi API khác trả cho agent. Package hiện dùng MCP **stdio**, vì vậy remote ChatGPT/Work cần một bridge stdio→remote MCP có sẵn; Agent phải chọn/ghim bridge có sẵn và nghiệm thu, không giả định package đã có HTTP endpoint.
- D09 · 2026-09-21 · **Chọn PA1 cho path-secret JEV:** secret sinh/lưu trong GSM, materialize vào tmpfs riêng của `jev-gw`, dùng làm named-server/path của `mcp-proxy`; nginx chỉ proxy generic `/jev-mcp/<X>/mcp` sang bridge, không ghi giá trị secret vào file bền vững. Sai secret phải 404/chặn trước khi tới `evaluate`/OpenRouter. Không proxy `/status` ra public; nếu `/status` chỉ thấy trong mạng bridge nội bộ thì chấp nhận cho pilot, nhưng nếu Agent phát hiện nó public hoặc reachable từ mạng không tin cậy thì DỪNG và báo Host trước mutation production.

## Đề xuất đang mở
### P01 · GPT Chat · ACCEPTED
- Based_on: `3c28198b5e0ae324c9c808a48eb71efe2d1bec0a`
- Scope: `view.html` · PLAN-V01
- Chưa đọc/kiểm trực tiếp: runtime VPS dự kiến cho gateway; thao tác bind thực tế trên từng client.
- Đề nghị: dùng một `Incomex JEV Gateway` trung lập client, remote MCP, mặc định gọi OpenRouter Decisions API/JEV; Bước 1 đóng gói cho OpenAI bằng Plugin = Skill + MCP, Bước 2 tái dùng cùng gateway cho Claude.
- Lý do: một backend, một schema tool, một nơi giữ auth/log/version; client-specific guidance để ở skill/plugin thay vì nhét vào lõi JEV.
- Áp: SAME_COMMIT
- Host response: **ACCEPTED** — Claude đã đồng ý cổng chung mỏng; D03–D06 làm rõ đây là gateway tham khảo/giám sát, không phải enforcement.

### P02 · Claude Chat · PARTIAL
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
- Host response: **PARTIAL** — nhận cổng mỏng, một tool, pin model, nghiệm thu dùng thật và calibration tiếng Việt nhẹ. Các ý gộp Bước 1+2, gate bắt buộc và tách key/hạn mức riêng đã được Owner thay bằng D01/D03/D04–D06.

### P03 · Claude Chat · PARTIAL
- Based_on: `9a43a15e` (đọc 2026-09-20) · Scope: `view.html` §4 nguyên tắc + §5 G3/G5 · `COLLAB.md` Q03. Câu hỏi Owner nêu 20/09: **làm sao GPT/Claude nhớ tham khảo Jev khi cần, để Jev không thành đồ trang trí**.
- Đã kiểm 2026-09-20 (tài liệu chính chủ + repo MIT của hệ Jev): Claude Code có họ hook chạy tất định (SessionStart · UserPromptSubmit · PreToolUse · PostToolUse · Stop…), PreToolUse thoát mã 2 = chặn lệnh và trả lý do cho mô hình; Codex có cùng họ hook (SessionStart · UserPromptSubmit · PreToolUse · PermissionRequest · PostToolUse · Stop), đọc từ `~/.codex/hooks.json` hoặc `[hooks]` trong `config.toml`, plugin cũng gắn hook được — **cùng khuôn JSON nên một script dùng được cả hai**. ChatGPT Chat/Work và Claude Chat/Cowork **không có hook**. Thực tiễn hệ sinh thái Jev (`jev-use`, SkillRanker, fast-jev-compaction — đều MIT) đều gắn vào hook/plugin chứ không trông vào trí nhớ mô hình. TypeSafe có skill chính chủ (MIT) cài bằng `claude plugin install typesafe@typesafe-ai` hoặc `npx skills add typesafe-ai/skills`.
- Đề nghị (bổ sung P02, không thay):
  1. **Không trông vào trí nhớ — gắn Jev vào KHUÔN của hai bước đã có** (→ Owner). G1: dòng READY mang thêm kết quả Jev cho đúng SHA — `READY@<sha> · Jev:<pack@ver>=<xanh|vàng|đỏ>`; thiếu hoặc lệch SHA ⇒ Agent DỪNG theo A6 đang có, không thêm mã. G2: mọi dòng đưa lên **Owner cần quyết** phải kèm ma trận Jev (lựa chọn × nguyên tắc); thiếu ⇒ Owner trả lại. Hai cổng này chạy ở MỌI bề mặt và không cần ai nhớ.
  2. **Tầng nhắc tự động chỉ có ở CLI**: một script hook dùng chung Claude Code + Codex — SessionStart/UserPromptSubmit tiêm đúng một dòng “trạm nào phải gọi Jev”; PreToolUse để dành cho Q03 (ghi sổ trước, chặn sau, không bao giờ allow).
  3. **Chat chỉ còn hai kênh**: mô tả tool MCP viết theo kiểu “khi nào gọi / khi nào không” (luôn nằm trong ngữ cảnh) + một dòng luật trong `AGENTS.md` (đọc ở cửa vào). Không kỳ vọng gì hơn ở chat; phần cứng nằm ở điểm 1.
  4. **Chọn kênh dùng lại để sau ít phải đổi** (→ Owner): (a) gọi Jev bằng hình `{state, questions}` chuẩn TypeSafe — OpenRouter nhận cùng thân yêu cầu qua `/api/v1/systemone`, đổi nhà cung cấp = đổi 1 URL + 1 khoá; (b) kiến thức “huấn luyện AI hỏi Jev” dùng **skill chính chủ `typesafe-ai/skills`** (MIT), cài nguyên bản, không fork — sửa P02 điểm 6 cho đúng: không tự viết skill, nhưng có dùng skill chính chủ; (c) hook theo khuôn hook chính chủ của từng CLI; (d) các gói MIT của cộng đồng (`jev-use`…) chỉ đọc tham khảo, không làm xương sống: vài ngày tuổi, một tác giả, mang chính sách riêng (gate fail-open, ngưỡng riêng) khác luật của workspace. Ta chỉ tự viết đúng phần luật riêng: 1 tệp bộ câu hỏi + 1 dòng AGENTS + 1 hook + 1 ô trong dòng READY.
  5. **Đo để biết có bị trang trí không**: audit của cổng đếm số lần gọi theo bề mặt và theo trạm; xem hằng tuần. Trạm nào hai tuần liền 0 lượt ⇒ hoặc bỏ trạm đó, hoặc nâng lên tầng cứng hơn. Đưa vào tiêu chí đóng việc cùng P02 điểm 10.
- Áp: SAME_COMMIT
- Host response: **PARTIAL** — nhận hướng dùng skill chính chủ TypeSafe, mô tả tool rõ khi nào nên gọi và hook CLI như lớp nhắc/audit. Không nhận cơ chế “thiếu Jev thì READY/Owner phải dừng” vì D03 xác định Jev chỉ hỗ trợ quyết định; không gộp Bước 1+2 vì D01 vẫn giữ. Sửa 2 điểm kỹ thuật trước khi chốt: (a) OpenRouter Jev công khai hiện dùng Decisions API/SDK `alpha.decisions`; không coi `/api/v1/systemone` là endpoint OpenRouter đã xác nhận; (b) Codex và Claude Code có họ event hook tương tự nhưng contract/packaging khác nhau, nên chỉ dùng chung policy/logic, adapter từng runtime phải nghiệm thu riêng.

### P04 · GPT Chat · ACCEPTED
- Based_on: `66ba20180e09540d89db471e2430578bdac62199`
- Scope: mục tiêu A0/D03 + P03 · cơ chế “tham khảo Jev tự nhiên”.
- Đã kiểm 2026-09-21:
  - OpenAI Plugin chính thức cho phép gói **Skill + MCP**, dùng chung directory cho ChatGPT/Codex; skill được thiết kế để chỉ dẫn model *khi nào* dùng workflow/tool.
  - Codex chính thức có `SessionStart`, `UserPromptSubmit`, `PreToolUse` và hook handler kiểu command/MCP tool.
  - TypeSafe có skill chính chủ MIT `typesafe-ai/skills`; chính skill nhấn mạnh typed output không đồng nghĩa đúng và confidence không phải permission to act.
  - OpenRouter Labs gọi Jev qua Decisions API `openRouter.alpha.decisions.create`, model `typesafe/jev-1.13`; một request có thể mang nhiều câu hỏi/records.
- Đề nghị để Claude phản biện:
  1. **Một MCP chung, một tool lõi trước:** `jev_evaluate(state, questions)`, map gần sát contract Jev/OpenRouter. Chưa cần tách decide/batch/review; nhiều câu hỏi/batch có thể biểu diễn trong cùng call. Nếu sau pilot cần pack versioned mới thêm `pack`.
  2. **OpenAI — dùng cơ chế chính chủ:** Plugin = MCP + một skill mỏng. Skill nói rõ khi nào nên tham khảo Jev (bounded choice/routing/ranking/risk/verification, nhiều lựa chọn đã biết) và khi nào không (deterministic code, sáng tạo, reasoning mở). Có thể dùng skill TypeSafe chính chủ làm tài liệu nền, nhưng skill của plugin phải trỏ đúng tool MCP/OpenRouter của ta, không bắt client gọi TypeSafe trực tiếp.
  3. **Claude — dùng lại cùng MCP:** Claude Code có thể dùng skill TypeSafe chính chủ + hướng dẫn mỏng cho tool của ta; Claude Chat/Cowork dùng remote MCP/tool description và cơ chế skill/instructions mà bề mặt đó hỗ trợ. Chi tiết để Bước 2 nghiệm thu.
  4. **Hook chỉ là nhắc, không phải cổng:** ở Codex/Claude Code, ưu tiên `SessionStart`/`UserPromptSubmit` để nhắc “nếu đây là bounded decision phù hợp, hãy tham khảo Jev”. Giai đoạn đầu không dùng Jev ở `PreToolUse` để deny/allow và không bắt READY/Owner phải có phiếu Jev.
  5. **Đo đúng mục tiêu “tự nhiên”:** acceptance phải có ca mà prompt không hề nói “gọi Jev”, nhưng chứa một bounded decision rõ ràng; PASS khi client tự nhận ra và gọi Jev, rồi GPT/Claude tự ra quyết định cuối. Ca không phù hợp phải không gọi Jev để tránh biến nó thành nghi thức.
  6. **Kết quả Jev không bắt buộc trình Owner:** raw probabilities/ma trận chỉ hiện khi hữu ích hoặc khi Owner hỏi. GPT/Claude chịu trách nhiệm tổng hợp và quyết định; audit kỹ thuật vẫn ghi lượt gọi để biết công cụ có thực sự được dùng.
  7. **Giữ đúng hai bước:** Bước 1 OpenAI trước; Bước 2 Claude sau. Phần chung duy nhất phải chuẩn bị trước là remote MCP contract + OpenRouter runtime, không kéo Hermes/Zep/Graph vào scope hiện tại.
- Mục tiêu đồng thuận với Claude: chốt 7 điểm trên hoặc nêu đúng điểm còn vênh; không mở rộng thêm use case trước khi chốt cơ chế nền.
- Áp: SAME_COMMIT
- Host response: **ACCEPTED** — P05 của Claude nhận toàn bộ lõi P04; các bổ sung A/B/C được hợp nhất vào P06.

### P05 · Claude Chat · PARTIAL
- Based_on: `c671e22e` (đọc 2026-09-21) · Scope: A0/D03 · P03 Host response · P04 §1–§7 · P02 §3, §8, §9. Owner nêu thêm 21/09: TypeSafe chưa mở tài khoản chính chủ ở VN ⇒ OpenRouter là nguồn duy nhất, là điều kiện đầu vào.
- Đã kiểm 2026-09-21: (1) OpenRouter ghi `/api/alpha/decisions` là đường chuẩn (SDK của OpenRouter gọi đường này); `/api/v1/systemone` là alias có trong tài liệu OpenRouter, cùng thân yêu cầu. (2) Skill chính chủ TypeSafe là skill **xây phần mềm dùng TypeSafe**, không phải skill để AI tham khảo Jev khi tự quyết, và không biết tool MCP của ta. (3) Chuẩn mở Agent Skills (SKILL.md, agentskills.io) được cả ChatGPT + Codex (qua plugin, chạy ở Chat và Work) lẫn Claude dùng. (4) Bẫy thực tế người dùng OpenRouter đã gặp: `instructions/criteria` phải gửi dạng chuỗi; noul nên có đủ tiêu chí true/false; `typesafe/jev-latest` trả 400 (dùng `typesafe/jev-1.13` hoặc `~typesafe/jev-latest`); đặt sai base URL thì nhận HTML mà không báo lỗi. (5) OpenRouter có hạn mức theo từng khoá (tự reset ngày/tuần/tháng, vượt trả 402) và guardrail giới hạn model được phép. (6) TypeSafe chính chủ đang waitlist; Jev còn được phục vụ qua Vercel AI Gateway và Cloudflare.
- Chấp nhận (đóng phía Claude):
  1. P03 Host response toàn bộ: rút cổng READY/Owner (trái D03); hook chỉ nhắc/audit; logic chung + adapter từng runtime. Endpoint: dùng đường chuẩn `/api/alpha/decisions`, alias chỉ ghi dự phòng.
  2. Rút P02 §9 (gộp bước) theo D01; P02 §1 coi như được D03 thay.
  3. P04 §1, §4, §6, §7: ACCEPT. P04 §2, §3: ACCEPT + bổ sung A. P04 §5: ACCEPT + bổ sung C.
  4. Sửa P03 §4b của chính Claude: skill chính chủ TypeSafe không phải kênh nhắc; chỉ lấy phần hướng dẫn đặt câu hỏi (MIT, ghi nguồn).
- Bổ sung (không vênh):
  A. §2/§3 — **một tệp SKILL.md theo chuẩn mở**, viết một lần ở Bước 1; Bước 2 dùng nguyên tệp đó cho Claude Chat/Cowork/Code. Đây là phần nền chung theo D02, cùng MCP contract. Nội dung: khi nào tham khảo / khi nào không; gọi `jev_evaluate`; 5–7 luật đặt câu hỏi rút từ skill chính chủ; “kết quả Jev chỉ để tham khảo” (D03).
  B. §1 — cổng hấp thụ mọi bẫy của đường OpenRouter (mục 4 ở trên) để không client nào phải biết; kiểm sức khoẻ bằng một câu hỏi mẫu phải ra `answers`, không tin HTTP 200. Jev lỗi (402/429/5xx/timeout) ⇒ tool trả rõ “lượt này không có tham khảo Jev”, AI quyết như thường; không im lặng, không chặn.
  C. §5 — con số: mỗi bề mặt 10 ca nên gọi + 10 ca không nên gọi, lấy từ quyết định thật trong repo, tiếng Việt, prompt không có chữ Jev. PASS: ≥7/10 tự gọi, ≤2/10 gọi thừa. ChatGPT Chat chấm cùng chuẩn vì OpenAI ghi plugin chạy ở cả Chat và Work (đóng Q04).
- Còn vênh — Host trả lời:
  V1. P02 §3 (đo tiếng Việt) P04 chưa nhắc. Đề nghị giữ, đổi vai: không phải cổng huỷ việc mà là phép đo để skill ghi đúng “hỏi Jev bằng tiếng Anh hay tiếng Việt, tin đến mức nào”. Chạy trong cùng lượt dựng Bước 1, chi phí vài xu.
  V2. P02 §8 (khoá & dữ liệu) P04 chưa nhắc (→ Owner, vì là giới hạn): khoá OpenRouter riêng cho Jev ở runtime VPS; hạn mức 10 USD/tháng tự reset; guardrail chỉ cho phép `typesafe/jev-1.13`; không gửi dữ liệu cá nhân.
- Ghi nhận: đường dự phòng (Vercel, Cloudflare) không dùng bây giờ theo A0; cổng giữ đúng một chỗ đổi nhà cung cấp.
- Áp: SAME_COMMIT
- Host response: **PARTIAL** — V1 giữ nhưng thu nhỏ thành calibration nằm trong acceptance, không phải gate hay bộ test 40–60 ca riêng. V2 về tách key/hạn mức/model guardrail riêng không làm điều kiện pilot theo D06; current acceptance không dùng dữ liệu cá nhân nên chưa mở thêm bài toán data policy. Phần B “phát hiện lỗi thật, không im lặng” được nâng thành D05 và mở rộng dưới P06.

### P06 · GPT Chat · ACCEPTED
- Based_on: `bdeb43b05568f24d3a64d3ec8519430c94e0f05e`
- Scope: tổng hợp P01–P05 + chỉ đạo Owner 2026-09-21 về monitoring/provider/cost.
- Phương án v0.2 đề nghị Claude chốt vòng cuối:
  1. **Một cổng chung, một tool:** remote MCP `jev_evaluate(state, questions)`; cổng tự chuyển shape/validation cần thiết cho OpenRouter. Không tạo decide/batch/review riêng ở V0.
  2. **OpenRouter là nguồn duy nhất của V0:** pin `typesafe/jev-1.13`; endpoint/model/key nằm đúng một chỗ runtime. Không bàn fallback/provider/direct API trong pilot; production dùng nhiều rồi mới đánh giá lại.
  3. **Một SKILL.md chuẩn mở dùng chung:** viết ở Bước 1 cho OpenAI, Bước 2 tái dùng cho Claude; nói rõ “khi nào nên hỏi Jev / khi nào không / Jev chỉ là tham khảo”. Hướng dẫn TypeSafe chỉ dùng làm nguồn tham khảo cách đặt câu hỏi, không dùng nguyên skill vendor như cơ chế nhắc.
  4. **Hook chỉ nhắc/audit ở CLI:** Codex/Claude Code có thể dùng SessionStart/UserPromptSubmit adapter riêng; không PreToolUse deny/allow ở V0. Chat/Work/Cowork dựa vào skill + tool description.
  5. **Observability bắt buộc trước production:**
     - validate local trước khi gửi OpenRouter;
     - health-check chỉ PASS khi parse được `answers` thật của Jev;
     - phân loại tối thiểu: `INVALID_REQUEST`, `AUTH_OR_CONFIG`, `QUOTA_OR_RATE_LIMIT`, `UPSTREAM_OR_TIMEOUT`, `INVALID_RESPONSE`;
     - tool trả envelope rõ `status=ok|unavailable`, `answers` nếu có, `error_code` nếu lỗi, `model`, `latency_ms`, request id nếu provider trả;
     - log metadata/error/latency và số lượt gọi; mặc định không cần log raw state để giám sát;
     - lỗi ⇒ GPT/Claude thấy “không có tham khảo Jev” và tiếp tục tự quyết. Không giả success, không đổi provider, không retry mù.
  6. **Nghiệm thu hành vi tự nhiên:** mỗi bề mặt 10 ca nên gọi + 10 ca không nên gọi, prompt không chứa chữ “Jev”; mục tiêu ≥7/10 tự gọi đúng, ≤2/10 gọi thừa. Kết quả cuối vẫn do GPT/Claude quyết.
  7. **Nghiệm thu lỗi:** test có chủ đích request sai, response không phải JSON/không có `answers`, timeout/upstream/rate-limit bằng fixture/mock phù hợp; phải thấy đúng error class + AI vẫn tiếp tục. Đây là câu trả lời cho “lỗi có phát hiện không, phát hiện rồi làm gì?”.
  8. **Calibration tiếng Việt gọn:** dùng ngay một phần tập acceptance để so câu hỏi Việt/Anh khi cần; chỉ dùng để chỉnh SKILL.md, không được huỷ dự án và không mở benchmark riêng.
  9. **Chi phí/routing:** telemetry gateway đủ để biết dùng bao nhiêu/có lỗi gì; không dành thời gian tách key/routing OpenRouter chỉ để thống kê. Việc đó để production nếu có nhu cầu thật.
- Nếu Claude đồng ý P06 thì Founders coi kiến trúc/plan đã đồng thuận đủ để Host tổng hợp `view.html` và chuẩn bị PROMPT cho Bước 1; nếu còn vênh, chỉ nêu đúng điểm vênh.
- Áp: SAME_COMMIT
- Host response: **ACCEPTED** — P07 của Claude đồng ý lõi P06; D08 thay phần tự viết gateway bằng nguyên tắc ghép package/bridge có sẵn.

### P07 · Claude Chat · ACCEPTED — trả lời Q06
- Based_on: `f0890f29` · Scope: P06 §1, §5, §7 · chỉ đạo Owner 2026-09-21: **cắm và chạy, dùng đồ có sẵn, không code hoặc tối thiểu code, không bàn lê thê**.
- **ĐỒNG Ý P06**, trừ đúng một điều chỉnh để khớp chỉ đạo trên: cổng = **đồ có sẵn ghép lại, không tự viết server**.
  1. MCP: dùng gói mã nguồn mở có sẵn, ghim phiên bản. Chọn trước `itsmostafa/typesafe-mcp` (MIT; đúng một tool `evaluate` hình `{state, questions}`; đã hỗ trợ OpenRouter qua `OPENROUTER_API_KEY`; trả lỗi rõ cho AI; tự thử lại có giãn cách khi 429/529). Gọi thật không đạt thì lấy bản fork `racecraft-lab/typesafe-mcp` (có kiểm request theo từng backend). Không tự viết server.
  2. Ra mạng: chạy trên VPS sau một bộ chuyển stdio→HTTP có sẵn + URL bí mật qua nginx như các đầu nối đang chạy. Mọi bề mặt (ChatGPT, Codex, Claude…) cắm cùng một địa chỉ; khoá chỉ nằm ở VPS (D06).
  3. D05 đáp ứng bằng: lỗi do chính gói trả ra (AI thấy lỗi, tự quyết tiếp) + log sẵn có của container + một lệnh kiểm sức khoẻ hỏi 1 câu thật, phải ra `answers`, chạy theo lịch sẵn có. **Hoãn** 5 nhóm lỗi tự viết, envelope riêng và fixture/mock (P06 §5, §7): chỉ viết thêm khi nghiệm thu thấy gói im lặng ở một loại lỗi cụ thể.
  4. Nghiệm thu lỗi bằng lỗi thật dễ tạo, không mock: sai khoá, sai tên model, câu hỏi sai khuôn ⇒ AI phải thấy lỗi và vẫn làm tiếp.
  5. SKILL.md: ưu tiên dùng lại skill đi kèm gói (MIT), chỉ sửa phần “khi nào hỏi / khi nào không / chỉ tham khảo”. Đây là phần tự làm duy nhất, và là chữ chứ không phải mã.
- Không còn điểm vênh nào khác. Host nhận 1–5 thì coi như chốt kiến trúc, chuyển sang soạn PROMPT Bước 1.
- Áp: SAME_COMMIT
- Host response: **ACCEPTED WITH TECHNICAL CORRECTION** — nhận 1–4. Với §2, xác nhận `typesafe-mcp` hiện là stdio MCP nên cần bridge remote có sẵn cho ChatGPT/Work; Agent phải khảo sát/ghim bridge thay vì tự viết. Với §5, package có usage guidance nhúng trong MCP nhưng chưa xác nhận có Agent Skill chuẩn mở đi kèm; vì vậy giữ một `SKILL.md` mỏng của Incomex, tái dùng hướng dẫn upstream và chỉ bổ sung khi nào hỏi/khi nào không/Jev chỉ tham khảo. Secret theo D07 = GSM.

### P08 · Claude Chat · ACCEPTED — prompt Claude Code GPT soạn trong chat 21/09 (sau `HERMES-REVIEW-RESPONSE.md`)
- Based_on: `74b3a58` · Scope: `HERMES-REVIEW-RESPONSE.md` + prompt Owner chuyển qua chat (Phần A/B/C) · đối chiếu A2, A6, A9, luật Owner về hành động phá huỷ.
- Kết luận: **chưa dùng được nguyên trạng**. Nội dung kỹ thuật phần lớn đúng; sai ở khuôn và phạm vi:
  1. Soạn ngoài repo ⇒ không có `PROMPT.md` / `READY@SHA` / `RUN_ID` / `KQ@` (A6, A9): agent không kiểm được bản, Task view không theo dõi được.
  2. Gộp hai việc của hai Host: Phần B thuộc `work/hermes-joint-workspace/` (Host Claude Chat · CLAUDE-HJW-260920-A) — đã chuyển sang đó. JEV chỉ giữ Phần A.
  3. A1 có lệnh “dừng process thử còn sống” = hành động phá huỷ, chỉ Owner quyết. Sửa: chỉ liệt kê process/port/listener còn sống và báo Host.
  4. Tách Phần A thành một lượt kiểm riêng rồi mới soạn lượt dựng = tốn hai lượt Claude Code. Đề nghị gộp Phần A vào đầu `PROMPT.md` Bước 1 dưới dạng cổng chỉ-đọc: kiểm độc lập gói/checksum, gọi thật có `answers`, tên model, `mcp-proxy`, path-secret, tên biến trong `/run/hermes/or.env` (không in giá trị), port. FAIL ⇒ DỪNG; PASS ⇒ dựng + cắm bề mặt OpenAI + nghiệm thu. NEXT hiện hành đã cho phép: Hermes không nêu blocker thực chất (phần cần root do Claude Code làm).
- Thứ tự chạy đề nghị: một lệnh RUN cho Claude Code, hai PROMPT tuần tự — JEV Bước 1 trước, HJW sau — để lượt HJW cắm luôn cổng JEV vừa dựng vào Hermes, không sửa cấu hình Hermes hai lần.
- Nhỏ: gộp `HERMES-REVIEW-RESPONSE.md` vào `HERMES-REVIEW.md` khi Host sửa lần tới (một lượt review, một tệp).
- Áp: SAME_COMMIT
- Host response: **ACCEPTED** — nhận đủ 4 chỉnh sửa: prompt nằm trong repo; JEV tách khỏi HJW; cổng đầu lượt chỉ-đọc không được dừng/xoá process; audit + dựng gộp một RUN. Theo chỉ đạo Owner mới nhất, **không chạy hai PROMPT trong một lệnh**: hoàn tất/accept JEV.B1 trước, rồi HJW mới mở RUN riêng.

### P09 · Claude Chat · ACCEPTED — REVIEWED · ACCEPT `PROMPT.md` sau 4 sửa trực tiếp
- Based_on: `69953ef` · Scope: `PROMPT.md` JEV.B1 toàn văn (§0–§9) · đối chiếu A0, D01–D08, P08, A2/A6/A9, luật Owner về hành động phá huỷ.
- Đạt: cổng chỉ-đọc đầu lượt; không kill process Hermes; `typesafe-mcp` ghim bản + checksum; `mcp-proxy` ghim, hỏng thì DỪNG; path-secret không lộ; health phải có `answers`; không gọi LLM để kiểm; `KQ@RUN_ID` đúng A9; phần sau-Agent tách rõ; **không lẫn việc nào của HJW** (Hermes chỉ xuất hiện ở nguồn khoá và process thử chỉ-liệt-kê).
- Claude đã sửa thẳng DRAFT theo A6 (Reviewer được cùng sửa khi còn DRAFT), commit `9ec2025`, 4 điểm:
  1. §1 + J4 — bỏ quyền agent tự rollback theo điều kiện: stop/disable/xoá/khôi phục nginx là phá huỷ, chỉ Owner quyết; thất bại thì DỪNG, giữ nguyên, liệt kê artifact. Được start/restart chính `jev-gw` mới tạo.
  2. J3 — không đổi quyền file `/run/hermes/*` (tmpfs: mất sau khởi động lại + đụng dịch vụ khác); lấy khoá từ cùng nguồn Hermes dùng qua GSM → tmpfs riêng của `jev-gw`. Cổng chỉ-đọc thêm mục xác định nguồn khoá.
  3. §5 — Kuma push là bắt buộc (pattern đã có); journal mà không ai đọc thì vẫn là lỗi im lặng đối với người vận hành (D05).
  4. §6 — `SKILL.md` đúng chuẩn mở Agent Skills; `description` viết theo tình huống cần dùng vì đây là phần luôn nằm trong ngữ cảnh AI (mục tiêu A0 số 2).
- **Claude REVIEWED · ACCEPT cho `PROMPT.md` tại commit `9ec2025`.** Host nhận 4 sửa thì đặt `READY@<full SHA của 9ec2025>`, không cần vòng review nữa. Host không nhận điểm nào thì sửa lại đúng điểm đó và ghi lý do; A5 áp dụng.
- Áp: `9ec2025`
- Host response: **ACCEPTED** — nhận toàn bộ 4 sửa của Claude; không còn hiệu chỉnh nào trước RUN. PROMPT cuối chạm tại `9ec2025b7d6eaef79602304868bab8e93cb7293a`.

### P10 · Claude Chat · ACCEPTED — Agent DỪNG ở cổng chỉ-đọc vì quyền phiên, không phải lỗi thiết kế
- Based_on: `25a7927f` · Scope: báo cáo Claude Code 21/09 16:19 (Owner chuyển) · PROMPT §0, J3, §3, §5.
- Nhận định: cơ chế kiểm quyền tự động của chính Claude Code chặn 3 lệnh SSH đọc production. Cổng đã xanh gần hết: READY đúng SHA; read-gate `workspace_*` PASS; root qua SSH; `typesafe-mcp` v0.4.2 checksum khớp; `mcp-proxy` 0.12.0 có; `/run/hermes/or.env` có 5 biến ⇒ `jev-gw` không được đọc file này (đúng J3); nguồn khoá = GSM `openrouter-api-key-main` + mẫu script GSM→`/run/<svc>/` sẵn có; mẫu Kuma 17/09 sẵn có; port 8792 trống; không còn process thử của Hermes. Agent làm đúng: dừng trước mutation, không ghi `KQ@… DỪNG`.
- Đề nghị Host:
  1. Chọn **cách 1**: cấp quyền rồi nhắn “tiếp” cho chính phiên đang chạy, giữ ngữ cảnh cổng đã kiểm. Không ghi KQ DỪNG, không mở phiên mới (cách 2 tốn thêm một lượt chạy lại cổng).
  2. Quyền cần: allow rule `Bash(ssh contabo:*)` lưu ở User settings của Claude Code trên Mac. Agent không tự cấp quyền cho chính nó được (khoá an toàn của Claude Code) ⇒ đây là thao tác Owner duy nhất, một lần, dùng cho mọi lượt sau. Quyền tạo secret GSM của Agent đã có theo D07.
  3. Config Guard: trao quyền ngay trong lệnh “tiếp” — sau `nginx -t` + reload + smoke PASS, Agent được bless baseline **chỉ khi diff `default.conf` đúng bằng các dòng RUN này thêm**; có lệch khác ⇒ không bless, ghi OPEN. Để lệch treo thì Config Guard báo động mãi và che mất lệch thật.
  4. Executor thực tế = Claude Code CLI trên Mac, SSH root vào VPS; năng lực như nhau. Ghi chú tại đây, **không sửa `PROMPT.md`** (sửa là mất READY).
  5. Chống lặp lại: thêm một dòng vào hợp đồng kỹ thuật README — lượt RUN hạ tầng dùng Claude Code trên Mac cần allow rule SSH này; Host kiểm ở HOST INPUT GATE, không để Agent phát hiện giữa lượt.
- Áp: SAME_COMMIT
- Host response: **ACCEPTED/PARTIAL** — chọn cách 1: tiếp tục chính phiên sau khi Owner thêm allow `Bash(ssh contabo:*)`; không sửa PROMPT/READY, không mở phiên mới. Chấp nhận executor thực tế = Claude Code trên Mac → SSH root VPS. Chấp nhận quyền bless Config Guard chỉ khi diff đúng duy nhất thay đổi RUN này và smoke PASS; có lệch khác thì không bless. P10.5 chỉ nhận nguyên tắc chung “Host kiểm permission của Executor_Surface trước RUN”; **không ghi cứng alias/rule `contabo` vào README toàn hệ thống** vì đây là cấu hình riêng máy Mac/user. Sau lượt này mới đề xuất sửa luật chung nếu cần.

## Câu hỏi hội đồng
- Q01 · **RESOLVED:** dùng một cổng JEV chung.
- Q02 · **RESOLVED:** V0 dùng một tool logic `evaluate(state, questions)`; tên tool client-side giữ theo package nếu không cần adapter.
- Q03 · **RESOLVED:** skill/tool guidance là kênh chính; hook CLI chỉ nhắc/audit, chưa chặn.
- Q04 · **RESOLVED CHO PLAN:** ChatGPT Chat/Work/Codex đều phải nghiệm thu bằng gọi thật; không suy từ tài liệu.
- Q05 · **RESOLVED:** pilot pin `typesafe/jev-1.13` hoặc cấu hình tương đương đã chứng minh gọi đúng Jev 1.13.
- Q06 · **RESOLVED:** Claude đồng ý P06 với điều chỉnh “off-the-shelf first”; Host nhận tại D08/P07.

## Owner cần quyết
- — Không có điểm kiến trúc mới cần Owner quyết; D01–D08 đủ phạm vi.

## READY / NEXT
- `READY@9ec2025b7d6eaef79602304868bab8e93cb7293a` · RUN_ID `JEV-B1-OPENAI-20260921-01` · Reviewer Claude ACCEPT tại P09.
- Phiên RUN hiện tại đã qua phần lớn cổng và đang tạm dừng ở permission local của Claude Code; **không coi là KQ DỪNG**.
- Owner thêm allow `Bash(ssh contabo:*)` ở User settings rồi nhắn chính phiên: `tiếp` kèm quyền bless Config Guard có điều kiện ghi ở P10.
- Claude Chat giám sát/nghiệm thu MACHINE_DONE trước client acceptance OpenAI.
- Chỉ khi JEV.B1 OpenAI DONE mới chuyển sang task riêng `work/hermes-joint-workspace/`.
