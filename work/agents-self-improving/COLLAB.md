# COLLAB — agents-self-improving
Tên việc: Nghiên cứu cách AI học từ lỗi để hỗ trợ khai báo quy trình, UI, Field, hợp đồng thông tin và Config.
**CHỈ THẢO LUẬN / NGHIÊN CỨU PHƯƠNG ÁN · CHƯA TRIỂN KHAI · KHÔNG READY/RUN · 0 RUN ACTIVE.**
**GIỚI HẠN:** Hồ sơ này không cấp quyền viết code, làm POC, cài công nghệ, tạo service/timer/collection, ghi PG/Directus/Graph/VPS, sửa Công thức hiện hành hay tự kích hoạt hội đồng. Có làm hay không do Owner quyết riêng sau thảo luận.

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
Xác nhận User: CHƯA XÁC NHẬN — Owner đã xác nhận yêu cầu mở **task thảo luận** và đường dẫn `work/agents-self-improving` ngày 22/10/2026; còn thiếu **chỉ định Host** theo AGENTS.md MT3-C. Không coi mục tiêu hoặc việc mở hồ sơ là quyền READY/RUN.
Host: CHƯA ĐƯỢC OWNER CHỈ ĐỊNH · đề xuất GPT Chat, vì đang tổng hợp thảo luận và có thể chuyển tay cho Claude/Gemini phản biện; Owner có thể chỉ định ghế khác.

### BẢNG ĐIỀU KHIỂN · cập nhật 2026-10-22 15:05 +07 · Claude Chat · P01
- 🎯 Mục tiêu (Owner 22/10): có 1 agent khai báo quy trình như hội đồng đang làm, tự học từ thực tế — AI tự ghi cái sai, đưa mã cải thiện — và có thể tham gia tạo cỗ máy sản xuất quy trình. Vì sao: phía sau còn hàng nghìn quy trình (Owner, tools-quy-trinh 15/10).
- 🏁 Xong khi: hội đồng có ý kiến độc lập về các lựa chọn, nguồn cộng đồng, reuse thực có, chi phí/rủi ro và kiến nghị để Owner quyết nghiên cứu tiếp hoặc dừng. Không cần phần mềm chạy được.
- 📍 Tiến độ: ✅ Tạo hồ sơ thảo luận → ■ Hội đồng phản biện (Claude P01 ✅ · GPT □ · Gemini □) → □ Host tổng hợp → □ Owner quyết nghiên cứu tiếp hay dừng.
- ✅ Đã xong: hồ sơ + ma trận PA0–PA5 (GPT P00) · Claude P01: kiểm sự thật Harness²/hạ tầng, đề xuất PA6 (Skill + Sổ lỗi + Ca thi), đính chính 2 giả định.
- ■ Đang làm: — · 0 RUN active · bước Hội đồng phản biện vòng 1/1, chỉ thảo luận.
- ⬜ Còn lại: Owner chỉ định Host; GPT + Gemini cho ý kiến độc lập về ma trận và P01; Host tổng hợp, chỉ sửa ma trận `view.html` sau khi chốt.
- ➡ Kế tiếp: 😊 Owner chỉ định Host (đề xuất GPT Chat) và chuyển P01 cho GPT · Host đọc P01, mời Gemini · NEXT_TRIGGER=Owner chuyển tay. Không phát lệnh chạy.
- ⛔ Không làm/để sau: RUN, POC, sửa ứng dụng, tạo engine, triển khai/cài Harness²/LangMem/DSPy/LangGraph mới; chạm dịch vụ/vùng dữ liệu đang chạy.

### 1. Mục tiêu
Thảo luận để tìm hướng nghiên cứu AI học từ những sai lầm trong khai báo quy trình, UI, Field, Info Contract và Config, dựa vào công nghệ có người sử dụng lâu dài và tận dụng Agent Data, vector, Graph cùng hạ tầng đang có. Công việc xây Công thức/Master/MMOW gốc vẫn tiếp tục độc lập; chưa quyết định có triển khai nghiên cứu hay không.
Owner bổ sung 22/10/2026: Cái quan trọng là tôi muốn có 1 agent xử lý khai báo các quy trình như chúng ta đang làm; tìm cách làm sao để agent có thể tự học được từ thực tế: AI tự ghi cái sai, đưa ra các mã cải thiện để agent chuyên biệt có thể xử lý tạo ra các quy trình, thậm chí có thể tham gia vào việc tạo ra cỗ máy sản xuất quy trình.

### 2. Thế nào là hoàn thành
Hội đồng so sánh các lựa chọn có dẫn chứng, nêu rõ giá trị, điều kiện thất bại, phần dùng lại, chi phí/rủi ro và đề xuất một hướng đáng nghiên cứu nhất hoặc đề xuất dừng. Owner xem kết luận và quyết có làm hay không trong bước riêng. Task này chỉ có kết quả thảo luận, không có RUN hay thử nghiệm thật.

### 3. Chi tiết cần đạt (AI ghi, Host kiểm)
#### HỘI ĐỒNG — COUNCIL_BOOTSTRAP_V1
| Ghế | Hãng | Bề mặt | Vai | Gọi bằng |
|---|---|---|---|---|
| openai-main | OpenAI/GPT | GPT Chat | Host đề xuất, CHƯA PHÂN CÔNG | Owner chuyển tay; CHƯA ĐO |
| claude-chat | Anthropic/Claude | Claude Chat | Reviewer đề xuất | Owner chuyển tay; CHƯA ĐO |
| google-main | Google/Gemini | Antigravity hoặc Gemini (Owner chọn 1 bề mặt) | Council đề xuất | Owner chuyển tay; CHƯA ĐO |
Mode=COUNCIL · Automation_Level=AUTO0 · Khác mặc định: DISCUSSION_ONLY, NO_BUILD, NO_READY, NO_RUN; roster và Host là đề xuất đến khi Owner chỉ định.
Không tính GPT Chat/Work/Dot là nhiều ghế; không tự ghi nhận phản hồi hay triệu tập.

#### C0. Chỉ đạo chi tiết Owner · 22/10/2026 14:57 · claude-chat nghe trực tiếp
1. Ưu tiên giải pháp đang được ứng dụng phổ biến thực tế và giải quyết được vấn đề; có thể kết hợp nhiều giải pháp.
2. Ưu tiên dùng lại những thứ sẵn có; code mới chỉ là phương án cuối cùng và rất hạn chế, vì tốn nhiều thời gian và xác suất thất bại cao.
3. Harness² của Google là hướng rất đáng chú ý, nhưng chưa chứng minh được trên thực tế; repo chưa chứng minh được sẽ sống dài hạn và được hỗ trợ.
4. Giai đoạn này chỉ thảo luận, tìm công nghệ và hướng đi, chưa chốt gì; GPT phác thảo ý kiến đầu, Claude nghiên cứu và cho ý kiến.

#### C1. Phạm vi bất biến
- **Hướng A** tiếp tục làm nền tảng MBM/MMOW/MOW, CT-000.x, Master, UI, Info Contract, Config như kế hoạch riêng. Không dùng task này để đổi hoặc chặn A.
- **Hướng B** chỉ nghiên cứu cơ chế truy xuất kinh nghiệm, nhận diện câu hỏi/điều kiện khai báo sai hoặc thiếu, phân biệt lỗi từng công đoạn, đề xuất một cải tiến nhỏ, lưu bài học đã được người/máy độc lập kiểm chứng.
- Không yêu cầu AI tự khai báo trọn vẹn quy trình; nếu tự cải thiện được một bước nhỏ với bằng chứng thì đã có thể tạo giá trị. AI kém hơn không được tự nghiệm thu sản phẩm của mình. ⚠ Lệch đích Owner 22/10 (ô 1): đích cuối là agent khai báo được quy trình; «bước nhỏ» chỉ là bậc 1 — xem P01.3, Host sửa.
- Không tự xây framework thay công nghệ phổ biến; công nghệ hôm nay có thể thay, còn Công thức/tri thức/ca lỗi/test phải là tài sản độc lập.
- Hướng Gemini, Harness² Google và các phương án GPT đều là **ứng viên**, không phải quyết định kiến trúc.

#### C2. Nội dung chính chỉ ghi ở HTML duy nhất cho Owner
- [Mở ma trận PA0–PA5 + câu hỏi hội đồng tại view.html](view.html): phương án Gemini (LangGraph + Graphiti + Propose/Probe/Diff), tái dùng mã Harness², reuse-first vector+graph+Agent Data, memory/evaluation tùy nhu cầu, tiêu chuẩn mở và đối chứng không xây mới.
- Không có kế hoạch triển khai hoặc PROMPT chạy trong task này. Mọi mức thời gian hay POC chỉ là **giả thuyết để thảo luận**.
- Không chép nguyên nội dung ma trận ở nhiều nơi; khi ý kiến hội đồng mới đến, lưu trong mục P của COLLAB, kết luận đã chốt cập nhật ma trận sau xác nhận.

#### C3. Bằng chứng bắt buộc trước khi kết luận
- Agent Data: xác minh runtime đã dùng LangChain/LangGraph gì, có tracing/evaluation/memory chưa; không suy theo tên framework. → P01.2(a): mã nguồn `docker/agent-data-repo` 0/186 tệp có «langchain»; phụ thuộc trực tiếp fastapi, openai, qdrant-client.
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

### Vòng trước
- Chưa có vòng hội đồng được triệu tập cho task này. Trao đổi GPT–Owner và ý kiến Gemini trong cuộc trò chuyện là nguyên liệu, không phải biên bản hội đồng.

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
Phản hồi Host: —

## Nguồn lịch sử liên quan
- [GitHub Issue #1](https://github.com/Huyen1974/incomex-workspace/issues/1) — nơi giữ bản đề cương trao đổi đầu tiên; từ nay task hiện hành là thư mục này, không dùng issue như task song song.
- [Harness² Google](https://github.com/google-research/harness2): tham khảo nghiên cứu, **không xác nhận production adoption**.

## Owner cần quyết
- Chỉ định Host và roster cho **vòng THẢO LUẬN**, không phải cho phép triển khai. Đề xuất GPT Chat Host, Claude Chat + Gemini phản biện.

## Quyết định Owner
- 21/10/2026: tạo task để bàn với hội đồng; «đây chỉ thảo luận thôi chưa làm», quyết có làm hay không sau.
- 22/10/2026: dùng chính xác đường dẫn `work/agents-self-improving`.
- 22/10/2026 14:57 · HUMAN_DIRECTIVE@ASI-20261022-01 EFFECTIVE · task=agents-self-improving · scope=thảo luận/nghiên cứu, không triển khai · step=Hội đồng phản biện · recorded_by=claude-chat · quote=«Bạn nghiên cứu và cho ý kiến» · text=mục tiêu bổ sung ghi ô 1, chỉ đạo chi tiết ghi C0 · audit=chưa.
