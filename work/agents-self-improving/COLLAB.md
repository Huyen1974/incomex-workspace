# COLLAB — agents-self-improving
Tên việc: Nghiên cứu cách AI học từ lỗi để hỗ trợ khai báo quy trình, UI, Field, hợp đồng thông tin và Config.
**CHỈ THẢO LUẬN / NGHIÊN CỨU PHƯƠNG ÁN · CHƯA TRIỂN KHAI · KHÔNG READY/RUN · 0 RUN ACTIVE.**
**GIỚI HẠN:** Hồ sơ này không cấp quyền viết code, làm POC, cài công nghệ, tạo service/timer/collection, ghi PG/Directus/Graph/VPS, sửa Công thức hiện hành hay tự kích hoạt hội đồng. Có làm hay không do Owner quyết riêng sau thảo luận.

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
Xác nhận User: CHƯA XÁC NHẬN — Owner đã xác nhận yêu cầu mở **task thảo luận** và đường dẫn `work/agents-self-improving` ngày 22/10/2026; còn thiếu **chỉ định Host** theo AGENTS.md MT3-C. Không coi mục tiêu hoặc việc mở hồ sơ là quyền READY/RUN.
Host: CHƯA ĐƯỢC OWNER CHỈ ĐỊNH · đề xuất GPT Chat, vì đang tổng hợp thảo luận và có thể chuyển tay cho Claude/Gemini phản biện; Owner có thể chỉ định ghế khác.

### BẢNG ĐIỀU KHIỂN · cập nhật 2026-10-22 14:45 +07 · GPT Chat · P00
- 🎯 Mục tiêu: tìm công nghệ/cách làm bền vững, dùng lại tối đa để AI học từ lỗi khai báo, cải thiện một bước nhỏ mỗi lần; hai hướng xây nền tảng và nghiên cứu chạy song song.
- 🏁 Xong khi: hội đồng có ý kiến độc lập về các lựa chọn, nguồn cộng đồng, reuse thực có, chi phí/rủi ro và kiến nghị để Owner quyết nghiên cứu tiếp hoặc dừng. Không cần phần mềm chạy được.
- 📍 Tiến độ: ■ Tạo hồ sơ thảo luận → □ Owner chỉ định Host → □ Hội đồng phản biện → □ Tổng hợp → □ Owner cân nhắc có nghiên cứu tiếp hay không.
- ✅ Đã xong: ghi nhận mục tiêu, giới hạn không triển khai và ma trận lựa chọn ở `view.html`.
- ■ Đang làm: — · 0 RUN active.
- ⬜ Còn lại: Owner chọn Host/roster; hội đồng đọc lựa chọn trong `view.html` và phản biện bằng chứng; Host tổng hợp bất đồng/kiến nghị.
- ➡ Kế tiếp: NEXT_TRIGGER=Owner chỉ định Host và quyết bắt đầu vòng THẢO LUẬN. Không phát lệnh chạy.
- ⛔ Không làm/để sau: RUN, POC, sửa ứng dụng, tạo engine, triển khai/cài Harness²/LangMem/DSPy/LangGraph mới; chạm dịch vụ/vùng dữ liệu đang chạy.

### 1. Mục tiêu
Thảo luận để tìm hướng nghiên cứu AI học từ những sai lầm trong khai báo quy trình, UI, Field, Info Contract và Config, dựa vào công nghệ có người sử dụng lâu dài và tận dụng Agent Data, vector, Graph cùng hạ tầng đang có. Công việc xây Công thức/Master/MMOW gốc vẫn tiếp tục độc lập; chưa quyết định có triển khai nghiên cứu hay không.

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

#### C1. Phạm vi bất biến
- **Hướng A** tiếp tục làm nền tảng MBM/MMOW/MOW, CT-000.x, Master, UI, Info Contract, Config như kế hoạch riêng. Không dùng task này để đổi hoặc chặn A.
- **Hướng B** chỉ nghiên cứu cơ chế truy xuất kinh nghiệm, nhận diện câu hỏi/điều kiện khai báo sai hoặc thiếu, phân biệt lỗi từng công đoạn, đề xuất một cải tiến nhỏ, lưu bài học đã được người/máy độc lập kiểm chứng.
- Không yêu cầu AI tự khai báo trọn vẹn quy trình; nếu tự cải thiện được một bước nhỏ với bằng chứng thì đã có thể tạo giá trị. AI kém hơn không được tự nghiệm thu sản phẩm của mình.
- Không tự xây framework thay công nghệ phổ biến; công nghệ hôm nay có thể thay, còn Công thức/tri thức/ca lỗi/test phải là tài sản độc lập.
- Hướng Gemini, Harness² Google và các phương án GPT đều là **ứng viên**, không phải quyết định kiến trúc.

#### C2. Nội dung chính chỉ ghi ở HTML duy nhất cho Owner
- [Mở ma trận PA0–PA5 + câu hỏi hội đồng tại view.html](view.html): phương án Gemini (LangGraph + Graphiti + Propose/Probe/Diff), tái dùng mã Harness², reuse-first vector+graph+Agent Data, memory/evaluation tùy nhu cầu, tiêu chuẩn mở và đối chứng không xây mới.
- Không có kế hoạch triển khai hoặc PROMPT chạy trong task này. Mọi mức thời gian hay POC chỉ là **giả thuyết để thảo luận**.
- Không chép nguyên nội dung ma trận ở nhiều nơi; khi ý kiến hội đồng mới đến, lưu trong mục P của COLLAB, kết luận đã chốt cập nhật ma trận sau xác nhận.

#### C3. Bằng chứng bắt buộc trước khi kết luận
- Agent Data: xác minh runtime đã dùng LangChain/LangGraph gì, có tracing/evaluation/memory chưa; không suy theo tên framework.
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

## Nguồn lịch sử liên quan
- [GitHub Issue #1](https://github.com/Huyen1974/incomex-workspace/issues/1) — nơi giữ bản đề cương trao đổi đầu tiên; từ nay task hiện hành là thư mục này, không dùng issue như task song song.
- [Harness² Google](https://github.com/google-research/harness2): tham khảo nghiên cứu, **không xác nhận production adoption**.

## Owner cần quyết
- Chỉ định Host và roster cho **vòng THẢO LUẬN**, không phải cho phép triển khai. Đề xuất GPT Chat Host, Claude Chat + Gemini phản biện.

## Quyết định Owner
- 21/10/2026: tạo task để bàn với hội đồng; «đây chỉ thảo luận thôi chưa làm», quyết có làm hay không sau.
- 22/10/2026: dùng chính xác đường dẫn `work/agents-self-improving`.
