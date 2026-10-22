# COLLAB — agents-self-improving
Tên việc: Nghiên cứu cách AI học từ lỗi để hỗ trợ khai báo quy trình, UI, Field, hợp đồng thông tin và Config.
**CHỈ THẢO LUẬN / NGHIÊN CỨU PHƯƠNG ÁN · CHƯA TRIỂN KHAI · KHÔNG READY/RUN · 0 RUN ACTIVE.**
**GIỚI HẠN:** Hồ sơ này không cấp quyền viết code, làm POC, cài công nghệ, tạo service/timer/collection, ghi PG/Directus/Graph/VPS, sửa Công thức hiện hành hay tự kích hoạt hội đồng. Có làm hay không do Owner quyết riêng sau thảo luận.

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
Xác nhận User: ĐÃ XÁC NHẬN — Owner 22/10/2026 chỉ định GPT Chat làm Host cho **việc THẢO LUẬN/NGHIÊN CỨU PHƯƠNG ÁN**; chưa quyết định có làm hay không. Xác nhận Host/mục tiêu KHÔNG cấp quyền READY/RUN, xây thử hay sửa hệ thống.
Host: GPT Chat — Owner trực tiếp 22/10/2026: «bạn làm host»; Host_ID: openai-main; Host_Surface: GPT Chat. Phạm vi Host chỉ là nghiên cứu, điều phối phản biện và ghi kiến nghị; không giao chạy.

### BẢNG ĐIỀU KHIỂN · cập nhật 2026-10-22 15:20 +07 · GPT Chat Host · P02
- 🎯 Mục tiêu (Owner 22/10): nghiên cứu cơ chế AI học từ sai lầm để dần khai báo quy trình/cỗ máy; **trọng số cao: khai thác tối đa năng lực có ích trên VPS (JEV, Vector, Graph, PG, Directus, Agent Data, công cụ kiểm)**; tìm thêm những câu hỏi và mục tiêu còn thiếu trước khi chọn hướng.
- 🏁 Xong khi: hội đồng làm rõ mục tiêu cần đạt và giới hạn, kiểm chứng reuse-vs-new, phản biện PA0–PA6 và các ứng viên mới; Host tổng hợp kiến nghị để Owner cân nhắc. **Không đồng nghĩa duyệt triển khai.**
- 📍 Tiến độ: ✅ Mở hồ sơ → ■ Thảo luận xác định mục tiêu/khả năng (Claude P01 ✅ · Host P02 ✅ · Gemini □) → □ So sánh cách tiếp cận → □ Owner xem xét có nghiên cứu tiếp hoặc dừng.
- ✅ Đã xong: ma trận PA0–PA5; P01 Claude đề xuất PA6/đính chính LangChain; P02 Host ghi phản biện và câu hỏi khai thác JEV/Vector/Graph/PG/Directus.
- ■ Đang làm: — · 0 RUN active · chỉ trao đổi tài liệu, chưa có lựa chọn được thông qua.
- ⬜ Còn lại: ý kiến độc lập Google/Gemini; xác minh khả năng thực có; bổ sung/loại câu hỏi mục tiêu qua phản biện; chọn tiêu chí so sánh; chưa lựa chọn công nghệ.
- ➡ Kế tiếp: Host chuyển đề bài P02 cho Gemini thông qua Owner (chuyển tay); Gemini phản biện P01/P02, nêu mục tiêu/công đoạn còn thiếu · NEXT_TRIGGER=nhận ý kiến Gemini đúng ghế. Không phát RUN.
- ⛔ Không làm/để sau: chạy thử, tự cài framework, sửa App/PG/Directus/Graph/VPS, viết engine, mở task con, sửa Công thức gốc hoặc phát READY/RUN.

### 1. Mục tiêu
Thảo luận để tìm hướng nghiên cứu AI học từ những sai lầm trong khai báo quy trình, UI, Field, Info Contract và Config, dựa vào công nghệ có người sử dụng lâu dài và tận dụng Agent Data, vector, Graph cùng hạ tầng đang có. Công việc xây Công thức/Master/MMOW gốc vẫn tiếp tục độc lập; chưa quyết định có triển khai nghiên cứu hay không.
Owner bổ sung 22/10/2026: Cái quan trọng là tôi muốn có 1 agent xử lý khai báo các quy trình như chúng ta đang làm; tìm cách làm sao để agent có thể tự học được từ thực tế: AI tự ghi cái sai, đưa ra các mã cải thiện để agent chuyên biệt có thể xử lý tạo ra các quy trình, thậm chí có thể tham gia vào việc tạo ra cỗ máy sản xuất quy trình.
Owner bổ sung trong phiên GPT Chat 22/10/2026: «Một trong những trọng số quan trọng là: phải khai thác tối đa được những năng lực mà VPS đang có.» Và trong quá trình thảo luận cần **bổ sung những câu hỏi/mục tiêu cần đạt được từ nhu cầu thực tế, sau đó mới thống nhất lựa chọn**. JEV tham khảo, vector, Graph, PG, Directus đang xây phải được khảo sát khả năng đóng góp; không tạo hệ mới khi những thứ đã có làm được tốt. Tận dụng tối đa **giá trị**, không ép mọi yêu cầu đều gọi mọi công nghệ.

### 2. Thế nào là hoàn thành
Hội đồng so sánh các lựa chọn có dẫn chứng, nêu rõ giá trị, điều kiện thất bại, phần dùng lại, chi phí/rủi ro và đề xuất một hướng đáng nghiên cứu nhất hoặc đề xuất dừng. Owner xem kết luận và quyết có làm hay không trong bước riêng. Task này chỉ có kết quả thảo luận, không có RUN hay thử nghiệm thật.

### 3. Chi tiết cần đạt (AI ghi, Host kiểm)
#### HỘI ĐỒNG — COUNCIL_BOOTSTRAP_V1
| Ghế | Hãng | Bề mặt | Vai | Gọi bằng |
|---|---|---|---|---|
| openai-main | OpenAI/GPT | GPT Chat | Host — Owner chỉ định 22/10 | Chat Owner trực tiếp; chuyển tay cho hội đồng |
| claude-chat | Anthropic/Claude | Claude Chat | Reviewer đề xuất | Owner chuyển tay; CHƯA ĐO |
| google-main | Google/Gemini | Antigravity hoặc Gemini (Owner chọn 1 bề mặt) | Council đề xuất | Owner chuyển tay; CHƯA ĐO |
Mode=COUNCIL · Automation_Level=AUTO0 · Khác mặc định: DISCUSSION_ONLY, NO_BUILD, NO_READY, NO_RUN; Host GPT Chat đã được Owner chỉ định. Claude Chat đã có P01; ghế Google/Gemini còn cần bề mặt duy nhất và ý kiến độc lập trước khi tính vòng hội đồng.
Không tính GPT Chat/Work/Dot là nhiều ghế; không tự ghi nhận ý kiến vắng hoặc tự gọi máy chạy.

#### C0. Chỉ đạo chi tiết Owner · 22/10/2026 14:57 · claude-chat nghe trực tiếp
1. Ưu tiên giải pháp đang được ứng dụng phổ biến thực tế và giải quyết được vấn đề; có thể kết hợp nhiều giải pháp.
2. Ưu tiên dùng lại những thứ sẵn có; code mới chỉ là phương án cuối cùng và rất hạn chế, vì tốn nhiều thời gian và xác suất thất bại cao.
3. Harness² của Google là hướng rất đáng chú ý, nhưng chưa chứng minh được trên thực tế; repo chưa chứng minh được sẽ sống dài hạn và được hỗ trợ.
4. Giai đoạn này chỉ thảo luận, tìm công nghệ và hướng đi, chưa chốt gì; GPT phác thảo ý kiến đầu, Claude nghiên cứu và cho ý kiến.
5. Owner (phiên GPT Chat 22/10) chỉ định GPT Chat làm Host; phải bổ sung các câu hỏi/mục tiêu chưa nhận diện trước khi bàn chọn công nghệ. Không được ép hội đồng chọn một phương án ngay chỉ vì có P01.
6. Trọng số quan trọng: khai thác tối đa năng lực hữu ích của JEV, Vector, Graph/Cognee, PG, Directus, Agent Data và bộ kiểm VPS đang có; không dựng mới một hệ thống nửa vời. Không đồng nghĩa phải buộc tất cả thành phần chạy trong mỗi ca hoặc mặc định PG schema hiện tại là kiến trúc cuối.

#### C1. Phạm vi bất biến
- **Hướng A** tiếp tục làm nền tảng MBM/MMOW/MOW, CT-000.x, Master, UI, Info Contract, Config như kế hoạch riêng. Không dùng task này để đổi hoặc chặn A.
- **Hướng B** chỉ nghiên cứu cơ chế truy xuất kinh nghiệm, nhận diện câu hỏi/điều kiện khai báo sai hoặc thiếu, phân biệt lỗi từng công đoạn, đề xuất một cải tiến nhỏ, lưu bài học đã được người/máy độc lập kiểm chứng.
- **Đích dài hạn để thảo luận:** agent chuyên biệt có thể hỗ trợ tự khai báo quy trình, tự rút kinh nghiệm từ lỗi và có thể tham gia cỗ máy tạo quy trình; **không giả định đã khả thi**. Công đoạn nhỏ dễ kiểm chứng là giả thuyết phạm vi ban đầu, không phải giới hạn vĩnh viễn. AI không được tự nghiệm thu bằng đánh giá của chính mình.
- Không tự xây framework thay công nghệ phổ biến; công nghệ hôm nay có thể thay, còn Công thức/tri thức/ca lỗi/test phải là tài sản độc lập.
- Hướng Gemini, Harness² Google và các phương án GPT đều là **ứng viên**, không phải quyết định kiến trúc.

#### C2. Nội dung chính chỉ ghi ở HTML duy nhất cho Owner
- [Mở ma trận PA0–PA6 + câu hỏi MỤC TIÊU MỚI tại view.html](view.html): Gemini/Harness², reuse-first Vector+Graph+JEV+Agent Data, memory/evaluation, Skill+Sổ lỗi+Ca thi (P01), tiêu chuẩn mở và đối chứng không xây mới. **Không chọn PA6 hoặc PA3 mặc định**.
- Không có kế hoạch triển khai hoặc PROMPT chạy trong task này. Mọi mức thời gian hay POC chỉ là **giả thuyết để thảo luận**.
- Không chép nguyên nội dung ma trận ở nhiều nơi; khi ý kiến hội đồng mới đến, lưu trong mục P của COLLAB, kết luận đã chốt cập nhật ma trận sau xác nhận.

#### C3. Bằng chứng bắt buộc trước khi kết luận
- Agent Data: P01.2(a) kiểm mã `docker/agent-data-repo` 0/186 tệp có «langchain», phụ thuộc trực tiếp fastapi/openai/qdrant-client; GitHub code search trong hai repo agent-data cũng chưa thấy «langchain». **Tạm bác tiền đề LangChain sẵn có**; phiên bản runtime đang phục vụ vẫn cần đối chiếu bằng chứng trước kết luận tuyệt đối. Không mặc nhiên kéo LangGraph.
- Graph Server: kiểm Neo4j, Cognee, graph-v1/JEV theo bằng chứng mới. **Graphiti là ứng viên đang nghiên cứu, không mặc định đã cài chạy**.
- Search: kiểm pgvector/Qdrant/Neo4j vector/hybrid search cái nào đã chạy, tránh thêm DB/service vì sở thích.
- Nguồn công thức: `work/mow-mot-moit-mout/FORMULA-AI-README.md`, `work/mbm-qtth-07-ve-ui-mow/COLLAB.md`, `work/tools-quy-trinh/README.md`, `work/graph-server/view.html`.
- Phân biệt sao/fork và phản hồi cộng đồng về Harness² với người dùng sản xuất được kiểm chứng; thu thập phản biện, bảo trì/lifecycle, phụ thuộc/licensing, khả năng tháo bỏ.
- Tiêu chí đo cho **đề xuất thử sau này**, không chạy: tỷ lệ lỗi đúng phát hiện, lỗi bỏ sót, câu hỏi thừa, khả năng truy nguồn/giải thích, hồi quy, chi phí thực theo ledger, thời gian và số lượt Owner/AI phải sửa.

#### C4. Gợi ý trình tự thảo luận — chưa kích hoạt
1. GPT/Gemini/Claude mỗi ghế chọn tối đa hai phương án có lợi nhất, nêu một phương án cần loại và bằng chứng phản chứng; đánh giá PA0 baseline.
2. Chỉ ra một bước nhỏ nhất đáng học đầu tiên, ví dụ phát hiện một câu hỏi Field/Quy trình bị thiếu, thay vì tự sinh cả UI.
3. Nêu cách phát hiện thất bại ở khâu truy xuất → graph → suy luận → khai báo → kiểm; ai nghiệm thu và cách đưa người/model mạnh vào khi AI thất bại.
4. So sánh tận dụng hiện có và phần **thật sự cần mua/cài/viết mới**, đánh giá nguy cơ phụ thuộc sản phẩm bị ngừng hỗ trợ.
5. Host tổng hợp kiến nghị để Owner quyết có nghiên cứu tiếp/không; không tự tạo task thử nghiệm hoặc ra RUN.

#### C5. BỘ CÂU HỎI/MỤC TIÊU MỞ — HOST P02, CHƯA CHỐT THÀNH YÊU CẦU TRIỂN KHAI
**Mục đích:** tìm thiếu sót trong chính đề bài. Hội đồng được sửa/bổ sung câu hỏi; không được suy rằng 3 bậc hay một công nghệ đã được Owner thông qua.
- **M1 — Năng lực đích:** «agent tự khai báo» nghĩa là soạn nháp, điền mẫu, tự tìm Field, kiểm lỗi, sửa khai báo, hay tạo trọn MOW? Đầu ra nào người Owner nhìn được trong một màn, kiểm được từng bước? Đâu là mục tiêu dài hạn, đâu chỉ là kết quả nhỏ đầu tiên?
- **M2 — Khả năng thực trên VPS:** mỗi thành phần Agent Data/Hermes/Vector (Qdrant, pgvector nếu có)/Graph (Neo4j, Cognee, graph-v1)/JEV/PG/Directus/DOT/CAT-015 có **đầu vào, đầu ra, câu hỏi trả lời được, nguồn dữ liệu, quyền, giới hạn và bằng chứng vận hành** nào? Mục nào đã có nhưng chưa tận dụng? Mục chưa có chỉ nêu GAP.
- **M3 — Ghép đúng vai:** Vector tìm tình huống tương tự; Graph tìm quan hệ/ảnh hưởng/trust và truy tới nguồn; PG/Directus chứa dữ liệu/quy tắc/phiên bản; JEV chỉ phân loại/xếp hạng câu hỏi hữu hạn khi luật cứng không giải được; test/DOT quyết định đạt. Có thể ghép qua những tool hiện hữu nào, giảm lần gọi và tránh tự tạo pipeline/trùng SSOT?
- **M4 — Sự thật để học:** Lỗi nào đã được xác nhận; sự cố (CAT-017), vấn đề (CAT-069), thay đổi (CAT-016), kiểm (CAT-015), quyết định (CAT-025), Field/Contract/Config và các kết quả MMOW đang ở đâu? Có liên kết nguồn gốc, bản đúng/sai, thời điểm, loại lỗi, người xác nhận, tình trạng chưa biết không? Không coi chat/log/suy đoán AI là chân lý.
- **M5 — Tại sao sai:** cần phân tách lỗi truy xuất/kho cũ, bản dữ liệu chưa cập nhật, graph thiếu cạnh, hiểu sai công thức, thiếu Field, quy tắc mâu thuẫn, phân quyền, kiểm thử bỏ lọt và chỉ dẫn skill đọc sót; thiếu trace ở đâu thì ghi UNKNOWN, không tự suy nguyên nhân.
- **M6 — Tự cải thiện chính xác là gì:** chỉ nhớ lỗi? gợi hỏi? sinh trường khai báo? đề xuất cập nhật Skill? hay đề xuất công thức/tình huống kiểm? Tách «retrieval = tìm lại» với «learning = thay đổi có kiểm chứng và dùng lại được». Ai phê duyệt nâng mức tự động?
- **M7 — Khả năng thay đổi:** khi công thức/Field/quan hệ đổi, bài học trước còn hiệu lực không; graph/source_id/trust/snapshot nào báo lỗi thời? Học sai, skill drift, nhồi nhiễu/hallucination, test bị học thuộc phòng thế nào?
- **M8 — Đo giá trị và chi phí:** mỗi khâu tiết kiệm bao nhiêu công Owner/AI, số lỗi tránh được, có thể truy nguồn, hồi quy, false positive, latency/token/chi phí ledger? Có nhóm đối chứng, tập dữ liệu chưa từng thấy và ngưỡng dừng không? **Không mặc định 50 ca thử bảo đảm độ tin cậy.**
- **M9 — Bảo toàn hệ thống:** số service mới = 0 là ưu tiên nghiên cứu, không được khẳng định khả thi khi chưa đo. Trường hợp cần bổ sung, có tái dùng MCP/DOT/Graph/Cognee/Python checker trước không? Có thể tháo bỏ mà không động mã/PG production không?
- **M10 — Chiến lược PG scale-first:** không thiết kế theo schema PG cũ; giai đoạn mô phỏng/Directus nháp bên việc khác đi trước, rồi mới một lần thiết kế schema PG. Nghiên cứu này chỉ hỏi PG có khả năng hỗ trợ gì, không tự sửa PG hiện tại.
- **M11 — Chuẩn cộng đồng:** Skill mở giúp phát chỉ dẫn cho agent nhưng **không phải máy tự học**; graph memory, hybrid RAG, evaluation/observability, Harness² có bằng chứng triển khai thật gì, phụ thuộc/duy trì bao nhiêu? Phần nào đã có trong Cognee/Hermes/JEV mà PA6/PA3 chưa tính?
- **M12 — Quyết định đúng thời điểm:** hội đồng hiện chỉ cần xác lập tập câu hỏi/năng lực và tiêu chí so sánh; cho phép kết luận «CHƯA BIẾT / KHÔNG ĐÁNG LÀM» chứ không buộc chọn một nền tảng hay mở POC.
- **Ví dụ để hội đồng diễn giải, KHÔNG thử:** quy trình cần một bước duyệt mà UI thiếu Field «người duyệt»; tìm ca tương tự bằng vector, Graph xác nhận quan hệ của bước duyệt, PG/Directus cung cấp quy tắc/Field đã duyệt, JEV chỉ tham khảo khi cần phân loại trường hợp, checker quyết định thiếu/đủ; đề xuất bổ sung 1 câu kiểm và gắn ca hồi quy. Đánh dấu từng phần hôm nay **đã có bằng chứng / chưa biết / cần điều tra**.

### Vòng trước
- Chưa có vòng hội đồng hoàn tất. Claude P01 và Host P02 là đóng góp vòng thảo luận đang mở; Gemini chưa phản biện.

## P — Ý kiến hội đồng

### P01 · Claude Chat · OPEN
Ghế: claude-chat · Bước/vòng: Hội đồng phản biện · 1/1 · Người góp ý: Claude Chat (Owner giao trực tiếp 22/10 14:57) · Based_on: bda5b66 · Scope: COLLAB §0–C4 + `view.html` (PA0–PA5) + Issue #1 · Chưa đọc: `FORMULA-AI-README.md`, `tools-quy-trinh/README.md`.
Bảng: lệch (chưa ghi vòng hội đồng, 🎯 chưa có lời Owner 22/10) → sửa cùng commit · Ô 1–2: ô 1 thiếu lời Owner 22/10 → đã thêm; ô 2 khớp.

**P01.1 Harness² — theo dõi, chưa dùng làm lõi.**
Bằng chứng 22/10: paper nộp 09/10/2026; repo 3 commit, 87 PR mở, 26 issue, chưa có release; README ghi «not an officially supported Google product»; chỉ thử trên 3 benchmark (JobBench, LAB, WorkBuddy-Bench); mặc định chạy Vertex AI; khi chạy để mạng tự do và tắt sandbox Codex; chế độ song song thử 2k bản/việc ⇒ chi phí nhân lên. 15,8k sao là độ chú ý, không phải người dùng.
Giữ ý tưởng Propose–Probe–Compose (thử vài bản vá, so kết quả, ghép bản tốt) cho bậc 3. Xem lại khi đủ 3 tín hiệu: có release chính thức · PR được merge đều · có người dùng production độc lập công bố.

**P01.2 Sự thật hạ tầng — đính chính.**
(a) Agent Data không dùng LangChain: tìm «langchain» trong 186 tệp py/toml/requirements của `docker/agent-data-repo` = 0; phụ thuộc trực tiếp fastapi, openai, qdrant-client ⇒ không có «LangChain sẵn có» để tận dụng; LangGraph là framework mới.
(b) Graphiti chưa cài; Graph Server vẫn ở lượt thử (Neo4j + Cognee 1.6.1).
(c) Hermes VPS v0.21.4 đã cài và có sẵn vòng học (skills/, memories/MEMORY.md, .curator_backups) — ma trận chưa nhắc. Bài học tại chỗ HJW P58: Hermes tự đánh giá lệch vì dựa trí nhớ riêng ⇒ tự ghi skill/memory không qua cổng là rủi ro đã xảy ra.

**P01.3 Đích lệch.** C1 «Không yêu cầu AI tự khai báo trọn vẹn quy trình» hẹp hơn ô 1 (Owner 22/10). Đề xuất Host: giữ «bước nhỏ» làm bậc 1 của thang (P01.6), đích cuối theo ô 1.

**P01.4 Đề xuất PA6 — Skill + Sổ lỗi + Ca thi (= PA0 thêm 2 thói quen).**
Công thức: Agent chuyên biệt = Agent có sẵn (Claude Code/Codex/Hermes) + Skill + Sổ lỗi + Ca thi. Vòng học: Lỗi → Ca thi → Bản vá → Thi lại mọi ca cũ → Ghế khác hãng duyệt → Git (rollback được).
Phổ biến: Skill (SKILL.md) là chuẩn mở từ 12/2025, ~40 công cụ hỗ trợ (Codex, Gemini CLI, Copilot, Claude Code; Hermes tương thích). OpenAI (cookbook self-evolving 11/2025), Anthropic (dreaming 05/2026), Nous (Hermes), Google (Harness²) đều chạy cùng một vòng: làm → chấm → rút bài học → sửa phần bao quanh model → thi → áp dụng.
Đúng gốc: lỗi lặp vì luật dài, AI đọc sót và không có gì bắt; ca thi biến bài học thành thứ máy bắt được («muốn sai cũng khó»); skill chỉ nạp khi cần nên ngắn. Skill, ca thi là tệp chữ trong repo ⇒ đổi agent/công cụ không mất.

**P01.5 Ví dụ xuyên suốt — MMOW 07, vẽ UI QT 0001 (ví dụ giả định).**
1. Agent vẽ UI QT 0001, quên field «người duyệt» ở bước có duyệt; bộ kiểm DOT bắt lỗi.
2. Agent tự ghi 1 dòng sổ CAT-069: QT 0001 · khâu = khai báo Field · thiếu field người duyệt.
3. Lỗi thành ca thi: «bước có duyệt ⇒ phải có field người duyệt» (mã đặt theo Master khi Owner duyệt).
4. Agent đề xuất bản vá: thêm 1 dòng vào skill Vẽ UI; thi lại toàn bộ ca cũ, đạt hết mới trình.
5. Ghế khác hãng duyệt ⇒ commit; từ QT 0002 không mắc lại.

**P01.6 Thang 3 bậc** — lên bậc khi đạt chỉ số P01.8; mức tự áp bản vá do Owner nâng (A5-AUTO).
Bậc 1 · Bắt thiếu: agent chỉ làm 1 khâu — tìm câu/field còn thiếu trong khai báo MMOW 07. 0 dịch vụ, 0 code mới: 1 skill (trỏ về công thức SSOT, không chép) + sổ CAT-069 thêm 2 cột «Khâu sai», «Ca thi». Chấm bằng DOT/script kiểm có sẵn (đúng/sai máy kiểm được ⇒ ít nhiễu).
Bậc 2 · Khai báo trọn 1 MOW: khi có khoảng ≥ 50 ca thi thật (ước tính — paper 2026 tối ưu SKILL: 20–26 ca/repo chưa tách được cải thiện khỏi nhiễu), chạy thi tự động bằng đồ có sẵn: evals của skill-creator hoặc promptfoo CLI (MIT; OpenAI mua 03/2026, cam kết giữ mã mở). Hermes VPS chạy thi theo sự kiện; tắt tự ghi skill/memory (bài học P58) — cách tắt CHƯA ĐO.
Bậc 3 · Tham gia cỗ máy (chỉ khi Owner giao): MBM đóng gói thành skill «đẻ skill» (đúng mô hình skill-creator: skill tạo skill) ⇒ agent soạn MMOW mới, cùng vòng học áp lên chính MBM. Lúc này mới xét tối ưu tự động: GEPA optimize_anything (ICLR 2026, có trong DSPy/MLflow, cần ~100–500 lượt chấm) hoặc Harness² nếu đủ 3 tín hiệu P01.1.

**P01.7 Loại / hoãn.** PA1 loại (thêm LangGraph + Graphiti; Agent Data không có LangChain). PA2 loại làm lõi (P01.1). PA3 hoãn: chỉ dùng `search_knowledge` của Agent Data (Qdrant có sẵn) khi sổ lỗi lên hàng trăm dòng, không thêm DB. PA4 hoãn: Langfuse self-host cần thêm ClickHouse ⇒ dịch vụ mới; Git + COLLAB + CAT-069 đủ làm vết cho bậc 1. PA5 loại: trùng Công thức CT-000.x. PA0 thiếu cơ chế biến lỗi thành ca thi ⇒ PA6 chính là PA0 cộng phần đó.

**P01.8 Đo (cho đề xuất thử sau này, không chạy).** Bắt đúng · bỏ sót · báo nhầm · hồi quy (ca cũ hỏng) · lượt người sửa · chi phí thật từ ledger (không có ⇒ UNKNOWN). Người chấm cuối = ghế khác hãng; Master dùng lần đầu do Owner duyệt; agent không tự nghiệm thu.

**P01.9 Đối chiếu luật.** ONE SSOT (skill trỏ, không chép công thức) · Luật Nhà (skill đăng ký ở Master Tool, không đẻ sổ mới) · VERIFY-OR-RED (bản vá chỉ xanh khi thi lại đạt) · NO-WAIT / không lịch hẹn (vòng học chạy theo sự kiện «có lỗi mới», không cron) · A5-AUTO (tự áp bản vá = AUTO3, chỉ Owner nâng).

JEV tham khảo (22/10, jev-1.14-20261014): hướng chính PA6 0,96 · Harness² làm lõi lúc này 0,09 · khâu học đầu = bắt thiếu 0,95 · tự sửa skill không cổng 0,06 · tối ưu tự động sau khi đủ ca 1,0. Lưu ý thiên lệch: PA6 do Claude viết, mô tả chi tiết hơn các PA khác.
Nguồn: [Harness² repo](https://github.com/google-research/harness2) · [arXiv 2610.14224](https://arxiv.org/abs/2610.14224) · [agentskills.io](https://agentskills.io) · [OpenAI cookbook self-evolving agents](https://developers.openai.com/cookbook/examples/partners/self_evolving_agents/autonomous_agent_retraining) · [Hermes docs](https://hermes-agent.nousresearch.com/docs) · [GEPA](https://github.com/gepa-ai/gepa) · [arXiv 2609.12742 Skill Issue](https://arxiv.org/pdf/2609.12742) · [Langfuse joins ClickHouse](https://langfuse.com/blog/joining-clickhouse) · [OpenAI to acquire Promptfoo](https://openai.com/index/openai-to-acquire-promptfoo/)
Phản hồi Host: Xem P02. Tiếp nhận PA6 như **ứng viên bổ sung có giá trị**; không chốt loại PA3/PA5, chưa chốt mốc số ca hoặc ba bậc; cần ý kiến Gemini độc lập.

### P02 · GPT Chat Host · OPEN · 22/10/2026
Ghế: openai-main · Bước/vòng: Hội đồng thảo luận xác định mục tiêu/phương án · 1/1 · Based_on: `2375f0c7` (P01 Claude) + nguồn hiện hành `work/graph-server/view.html` · Scope: task `agents-self-improving` §0, C0–C5, P01, view.html; chỉ sửa **hồ sơ thảo luận**, không chạy hệ thống. Chưa kiểm được runtime trực tiếp của mọi thành phần VPS: các capability cần bằng chứng mới sẽ giữ CHƯA ĐO.

**1. Điểm đồng thuận với Claude P01 (PARTIAL, không phải nghiệm thu kiến trúc).**
- Harness² đáng tham khảo **triết lý cải tiến hai cấp**, chưa chọn làm framework sản xuất; repo tự ghi không phải Google product chính thức. Những kết quả benchmark không chứng minh hiệu quả với khai báo MOW.
- Đường Skill + Sổ lỗi + Ca thi của PA6 giúp biến lỗi lặp thành điều kiện kiểm máy; giữ bài học trong Git/version và kiểm hồi quy trước khi dùng lại. Agent Skills có đặc tả mở, nhiều client dùng được.
- Chấp nhận đính chính: **không được tiếp tục coi Agent Data đã có LangChain**; kiểm mã của Claude 0/186 và code search không thấy, nhưng vẫn cần xác minh version đang chạy. Không đề xuất thêm LangGraph vì tưởng đã có.
- Giữ cách tiến từng phần nhỏ; **đích dài hạn vẫn là agent khai báo quy trình và tham gia cỗ máy**, không bó về một Field mãi mãi.

**2. Chỗ chưa đồng thuận/cần Gemini và hội đồng phản biện.**
- PA6 là **cách mang hướng dẫn và kiểm bài học**, không tự giải được khâu tìm đúng lỗi, truy nguyên nhân, truy quan hệ ảnh hưởng hoặc phân biệt luật hết hiệu lực. Vì vậy **PA6 có thể bổ trợ PA3**, không loại PA3 theo tiêu chí hàng trăm lỗi. Vector/Graph/JEV có sẵn phải được đánh giá công bằng **ngay ở khâu tìm lỗi**, nhưng không ép gọi tất cả khi một phép kiểm cứng đã đủ.
- PA5 (BPMN/DMN/JSON Schema) là **tiêu chuẩn biểu diễn/kiểm máy có thể tham khảo**, không đương nhiên đòi thay CT-000.x; không loại chỉ vì Công thức đã tồn tại. Ngược lại không tạo ontology/công thức gốc thứ hai.
- Mốc «≥50 ca thi để lên bậc 2» **không có căn cứ thống kê chung**. Paper Skill Issue nói 20–26 ca held-out không đủ phân biệt kết quả **trong thí nghiệm đó**; không suy ra 50 ca là đủ. Nếu bàn thử sau này phải tính độ nhiễu, độ lớn cải thiện, loại lỗi và tập độc lập.
- **Skill không tự học**: `SKILL.md` là cách đóng gói/nạp instruction; cơ chế tìm bằng chứng → phát hiện sai → kiểm → ghi nhớ/áp bản mới nằm ngoài file skill. Không để trí nhớ/suy luận AI thay chứng cứ đã duyệt.
- Điểm JEV PA6 0,96 chỉ là tham khảo xác suất theo lựa chọn/cách mô tả, **không chứng minh PA6 tốt hơn Graph/Vector**. JEV hữu dụng nhất khi quyết định hữu hạn, có luật và evidence, không làm giám khảo cuối của công thức đúng/sai.

**3. Nguyên tắc thảo luận mới từ Owner.** Tạo bộ câu hỏi M1–M12 trong C5, ưu tiên bản đồ tận dụng **Vector/Qdrant → Graph/Cognee/Neo4j → JEV bounded semantic → PG/Directus nguồn dữ liệu → kiểm máy/DOT**. Đây là sơ đồ phân vai để so khả năng, **không phải pipeline đã duyệt**. Phải phân biệt: dữ liệu đã có ở đâu, truy được qua tool nào, trust/freshness, cái gì chưa biết và cái gì thật sự cần xây mới. PG scale-first không lấy schema cũ làm khuôn.
 
**4. Cách phân tích một ca nhỏ mà không chạy.** Đề nghị hội đồng lấy ca sai/thiếu thật đã nghiệm thu ở MMOW 07 hoặc Field/Config để trả lời: (i) nguồn chuẩn; (ii) kết quả sai và hậu quả; (iii) khâu sai; (iv) khả năng Vector truy tương tự; (v) quan hệ Graph cần dùng; (vi) JEV có cần không; (vii) checker độc lập chấm được gì; (viii) kỹ thuật bổ sung tối thiểu và chi phí; (ix) có giữ được kiến thức đã học khi đổi agent không? Nếu dữ liệu chưa có, ghi UNKNOWN thay vì tự dựng ví dụ thành chứng cứ.
 
**5. Đề nghị cho Gemini phản biện độc lập.** Gemini phải đề xuất ít nhất một câu hỏi/mục tiêu còn thiếu trong C5 và tự tranh luận phản chứng với PA6/PA3/hướng ban đầu LangGraph–Graphiti–Harness². Trả lời dựa **bằng chứng kỹ thuật + trạng thái hiện hành**. Không vote quyết định triển khai, không tạo prompt READY/RUN, không sửa production. Khi nhận ý kiến, Host tổng hợp điểm mới và còn vênh, chỉ xin Owner quyết **sau khi khung nhu cầu đủ rõ**.

**Nguồn kiểm:** [Agent Skills](https://agentskills.io/home) (format không là learning engine) · [Harness²](https://github.com/google-research/harness2) (hai vòng và benchmark, không chính thức) · [Skill Issue](https://arxiv.org/abs/2609.12742) (20–26 held-out chưa đủ trong nghiên cứu) · [Cognee](https://docs.cognee.ai/reference/colab_notebooks) (kết hợp graph/vector search; kiểm bản đang cài) · [OpenTelemetry GenAI](https://opentelemetry.io/blog/2026/genai-observability/) (tracing tham khảo khi thiếu).
**Trạng thái:** BÀN TIẾP · PA0–PA6 CHƯA CHỐT · 0 RUN ACTIVE.

## Nguồn lịch sử liên quan
- [GitHub Issue #1](https://github.com/Huyen1974/incomex-workspace/issues/1) — nơi giữ bản đề cương trao đổi đầu tiên; từ nay task hiện hành là thư mục này, không dùng issue như task song song.
- [Harness² Google](https://github.com/google-research/harness2): tham khảo nghiên cứu, **không xác nhận production adoption**.

## Owner cần quyết
- —
(Owner đã chỉ định GPT Chat Host trong chat 22/10. Chưa có quyết định công nghệ/triển khai cần Owner duyệt; hội đồng tiếp tục làm rõ mục tiêu và chờ ý kiến Gemini.)

## Quyết định Owner
- 21/10/2026: tạo task để bàn với hội đồng; «đây chỉ thảo luận thôi chưa làm», quyết có làm hay không sau.
- 22/10/2026: dùng chính xác đường dẫn `work/agents-self-improving`.
- 22/10/2026: Owner chỉ định GPT Chat làm Host; chỉ THẢO LUẬN, trong lúc thảo luận bổ sung mục tiêu/câu hỏi còn thiếu, trọng số quan trọng là khai thác tối đa **năng lực hữu ích sẵn có trên VPS** (JEV, Vector, Graph, PG, Directus). Chưa chấp thuận bất kỳ thiết kế/POC/RUN nào.
- 22/10/2026 14:57 · HUMAN_DIRECTIVE@ASI-20261022-01 EFFECTIVE · task=agents-self-improving · scope=thảo luận/nghiên cứu, không triển khai · step=Hội đồng phản biện · recorded_by=claude-chat · quote=«Bạn nghiên cứu và cho ý kiến» · text=mục tiêu bổ sung ghi ô 1, chỉ đạo chi tiết ghi C0 · audit=chưa.
