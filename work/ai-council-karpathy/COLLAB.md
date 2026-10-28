# COLLAB — ai-council-karpathy
Tên việc: AI-council-Karpathy — hội đồng AI độc lập và quy trình công việc/code thống nhất
Host: GPT Chat
Host_ID: openai-main
Owner giao: 2026-10-28
HTML chính: view.html
Phạm vi ghi đợt mở hồ sơ: work/ai-council-karpathy/; không thay luật nền, không đổi repo, không chạy Agent.

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
Xác nhận User: ĐÃ XÁC NHẬN — Owner chỉ đạo trực tiếp ngày 28/10/2026: lập task **AI-council-Karpathy** để thảo luận; **chưa phê duyệt triển khai kỹ thuật, nâng cấp Workspace hoặc mở repo code mới**. GPT Chat làm Host hiện hành cùng Owner theo mô hình Owner đã mô tả; không tự suy quyền cho Host vĩnh viễn hoặc các AI khác.

### BẢNG ĐIỀU KHIỂN · cập nhật 2026-10-28 15:00 +07 · GPT Host · P01
- 🎯 **Mục tiêu:** Task thảo luận AI-council-Karpathy: hội đồng AI không phụ thuộc hãng, Host điều hành theo bước có quy định; tận dụng dự án Karpathy kết hợp Workspace hiện có, quản lý được cả việc và code.
- 🏁 **Xong khi:** Giai đoạn mở hồ sơ: ghi đầy đủ chỉ đạo, câu hỏi và roster; kết thúc *toàn task* cần hội đồng thảo luận/Owner chốt tiêu chí kỹ thuật sau, chưa được tự nhận hoàn tất.
- 📍 **Tiến độ:** ✓ G0 Mở hồ sơ → ■ G1 Hội đồng phản biện các phương án → □ G2 Owner/Host quyết cấu trúc → □ G3 Roadmap/thiết kế theo quy định → □ G4 triển khai + nghiệm thu nếu Owner giao.
- ✅ **Đã xong:** Đối chiếu AGENTS A0/A2/A5/A6/A8/A9 và nguyên tắc Owner; lập hồ sơ yêu cầu, danh mục vấn đề cần phản biện; không thay luật nền.
- ■ **Đang làm:** — · 0 RUN active. G1 ở trạng thái **BÀN** (không phải STARTED/RUN); vòng hội đồng chưa có phiếu phản biện.
- ⬜ **Còn lại:** Ý kiến độc lập khác hãng; phân biệt “đồng ý” với “đã bình luận”; chọn ranh giới Workspace/code; chốt khả năng tái dùng và giấy phép; tiêu chí nghiệm thu; quyết định kỹ thuật/roadmap về sau.
- ➡ **NEXT_TRIGGER=INDEPENDENT_COUNCIL_REVIEW_AI_COUNCIL_KARPATHY:** Owner chuyển nội dung task cho Claude Chat (ghế khác hãng) nhận xét; GPT Host đối chiếu và chốt kết luận bước thảo luận theo quy chế, chưa phát RUN.
- ⛔ **Không làm/để sau:** Không sửa AGENTS/luật gốc; không di chuyển mã hoặc dữ liệu, đổi quyền hay tạo repo code; không thêm task phụ; không triển khai công nghệ, không phát READY/PROMPT/RUN; không ép dùng API trả phí.

### 1. Mục tiêu
1. “Chúng ta hướng tới những tính năng tự động cao, nhưng hội đồng của chúng ta tổ chức theo 1 nguyên tắc là không bị phụ thuộc vào bất cứ nhà cung cấp nào. Tức là bất cứ ai cũng có thể tham gia.”
2. “Đồng ý về bản chất: Workflow Engine tức là, Có 1 AI (có thể bao gồm cả con người điều hành theo quy định) tức là mỗi bước nhỏ đều có khung rõ rõ ràng (quy định sau) và tất cả các AI làm việc trong khung đó, bao gồm những việc phải làm, vòng lặp phải kiểm tra, những ai phải tham gia? Thế nào là hoàn thành..... việc này chúng ta sẽ quy định chuẩn sau.”
3. “Đưa vào 1 công thức chung là: ý kiến cũng phải có sự đồng ý của ít nhất 1 ai khác hãng, bên cạnh Host (Host quyết).”
4. “Cách tiếp cận đơn giản là chúng ta dùng công nghệ của: Karpathy Như đã bàn để nâng cấp quy trình work space, tận dụng các cơ chế đã có của Karpathy kết hợp với các cơ chế mà chúng ta đã viết cho work space để có 1 hệ thống hoàn chỉnh.”
5. “Không chỉ ý kiến là cần hội đồng theo nguyên tắc, mỗi lần agent báo cáo kết quả, Host cũng cần đọc báo cáo, soạn prompt tiếp theo (theo roadmap) và cần ý kiến hội đồng (ít nhất 1 ý kiến của ai khác hãng) Host cân nhắc, nếu cần thiết sẽ mở thêm vòng thảo luận, hoặc quyết định soạn prompt tiếp theo và chỉ định agent thực hiện.”
6. “Tôi thì muốn là đồng bộ kể cả công việc lẫn việc viết code, quản lý cho đơn giản. Nhưng vì tính chất công việc hơi khác nhau => cái này cứ đưa lên rồi hội đồng cho ý kiến.”
7. “Trước hết chúng ta lập ra cái này để thảo luận, vì cái này AI-council-Karpathy là mức task. Còn chuyện nâng cấp Repo, hay mở thêm Repo code space đợi hội đồng cũng có ý kiến rồi chúng ta quyết định.”

### 2. Thế nào là hoàn thành
“Cái lý tưởng tôi nhìn thấy là ở mỗi bước, chúng ta biết tiến độ đến đâu? biết bước gì tiếp theo? Biết đang ở bước nào? Biết bước nào tắt hay là mọi việc vẫn theo kế hoạch?” — Owner 28/10/2026 (trao đổi liền trước).
“Trước hết chúng ta lập ra cái này để thảo luận [...] đợi hội đồng cũng có ý kiến rồi chúng ta quyết định.” — Owner 28/10/2026.
**Chưa có nghiệm thu kỹ thuật/hệ thống cuối do Owner chốt**: việc mở hồ sơ không đồng nghĩa công nghệ được chọn hay task hoàn thành.

### 3. Chi tiết cần đạt (AI ghi, Host kiểm)
#### HỘI ĐỒNG — COUNCIL_BOOTSTRAP_V1
| Ghế | Hãng | Bề mặt | Vai | Gọi bằng |
|---|---|---|---|---|
| openai-main | OpenAI GPT | GPT Chat (phiên hiện hành) | Host | Chat trực tiếp Owner; gateway workspace được audit |
| anthropic-review | Anthropic Claude | Claude Chat | Reviewer | Owner chuyển tay AUTO0; đường tự gọi CHƯA ĐO |
Mode=COUNCIL · Automation_Level=AUTO0 · Khác mặc định: — (đây là task **BÀN**, không có READY/RUN). Thành viên/Worker khác chỉ tính là ghế khi được phân công đúng identity/surface và cập nhật roster; không đồng nhất provider/model với quyền biểu quyết. Owner có quyền đổi Host, roster, worker theo AGENTS.

#### 3.1. Yêu cầu nghiệp vụ Owner — chưa biến thành luật nền
- **Workflow Engine độc lập:** Host (AI hoặc AI + con người theo ủy quyền) điều hành; mỗi bước/node về sau phải có **đầu vào, việc phải làm, thành viên/ghế bắt buộc, giới hạn vòng lặp, bằng chứng kiểm, tiêu chí hoàn thành, người chốt, các nhánh chuyển tiếp và phần được chừa sang bước sau**. Bộ quy định chi tiết sẽ xây và duyệt sau, không giả định đã có.
- **Vòng quyết định:** Owner + AI xác định mục tiêu → các ghế thảo luận phương án/roadmap → phản biện/đồng thuận theo quy chế → Host chốt và chia node, ký lệnh hợp lệ → Agent được chỉ định thi hành/báo cáo → Host đọc KQ và đối chiếu roadmap/evidence → hội đồng có ý kiến độc lập khác hãng → Host quyết **bổ sung ngay / chuyển node / chuyển phần chưa chặn sang bước sau / dừng và xin Owner**. Lặp lại ở *mỗi* KQ, không chỉ vòng đầu.
- **Nguyên tắc đồng thuận mới do Owner nêu:** với ý kiến/phương án mà Host chốt, cần **ít nhất một AI khác hãng đồng ý** bên cạnh Host; Host vẫn là người quyết định cuối trong thẩm quyền. **LƯU Ý XUNG ĐỘT CẦN HỘI ĐỒNG XỬ LÝ:** AGENTS A5/DROOT57 hiện yêu cầu ít nhất một ý kiến/nhận xét khác hãng, *không bắt buộc reviewer đồng ký/đồng ý*. Chưa sửa luật gốc trong task mở này; cần đề xuất cách định nghĩa “đồng ý”, xử lý bất đồng và quyền Host/Owner mà không biến reviewer thành người ký READY thứ hai.
- **Sau KQ worker:** luôn có ít nhất một AI khác hãng nhận xét độc lập với Host; giữ nguyên tắc độc lập với **cả Worker** theo A5; reviewer không tự nghiệm thu phần mình thi hành. Host cân nhắc nếu khác biệt thực chất mới quyết mở vòng 2/3, không tự chạy vòng thừa; Host lập và ký PROMPT node kế khi đủ điều kiện.
- **Tính hoán đổi:** các ghế có định danh/role/quyền theo task; AI khác hãng/AI mới tham gia được qua adapter và roster; ghế được thay đổi; AI/agent viết code được lựa chọn theo từng node, không phụ thuộc API hãng. Tách ghế Host/Reviewer/Courier/Worker và năng lực gọi được qua App/CLI/MCP/thủ công/API.
- **Tính trực quan:** người xem biết ngay mục tiêu, roadmap, node hiện tại, đã xong, còn lại, ai đã/thiếu ý kiến, các nhánh lệch/blocked, KQ bằng chứng, NEXT_TRIGGER và ai chịu trách nhiệm tiếp; trạng thái người đọc không được tạo một SSOT thứ hai.
- **Chi phí/kiểm soát:** API thương mại chỉ tùy chọn; ưu tiên sử dụng thuê bao/app/CLI/MCP và xử lý tại hạ tầng mình; không mở đường chạy tự động không có quyền, receipt, giới hạn chi phí và kiểm chứng.

#### 3.2. Kế thừa Workspace hiện hữu (đã có quy định, cần kiểm tình trạng thực tế)
- AGENTS A0/MT3/MT4: mục tiêu Owner, Bảng điều khiển và trạng thái từng task.
- A2/COUNCIL_BOOTSTRAP_V1: ghế, identity, Host/Reviewer/Worker, quorum; A5/DROOT57: phản biện khác hãng, mặc định 1 vòng, tối đa 3; A6/DROOT58: Host/Co-host hợp lệ ký READY một chữ ký; sau KQ có rà khác hãng.
- A9: thư mục task/Owner View; trạng thái READY → STARTED → KQ XONG|DỪNG, NEXT_TRIGGER và luật NO-WAIT. Phần được máy cưỡng chế và phần mới có chữ quy định phải được đo riêng; không suy “đã tự động” từ luật trên giấy.
- Giữ nguyên cơ chế ghế/định danh/nguồn chuẩn/phiếu P/quyền Host đã xây; không sao chép nguyên một ứng dụng khác rồi bỏ luật hiện hành.

#### 3.3. Các nguồn công nghệ cần hội đồng đánh giá (chưa chọn/cài)
- **Karpathy LLM Council:** https://github.com/karpathy/llm-council — tham khảo thu ý kiến độc lập, đánh giá chéo và Chairman. Bản gốc dùng OpenRouter API/React/FastAPI; **không phù hợp dùng nguyên trạng** với yêu cầu không lệ thuộc provider và dùng thuê bao/CLI. Chưa tìm thấy tệp LICENSE ở thư mục gốc lúc khảo sát 28/10/2026: **không chép mã nguồn trước khi xác minh quyền sử dụng/giấy phép**.
- **Karpathy AutoResearch:** https://github.com/karpathy/autoresearch — lấy nguyên lý vòng lặp agent **sửa → thử/đo → giữ hoặc lùi → ghi log → thử lại**, và chỉ dẫn ở `program.md`. Bản gốc là thí nghiệm huấn luyện model trên GPU, **không phải máy hội đồng đa hãng**; chưa tìm thấy LICENSE tại root khi khảo sát 28/10/2026, cũng phải rà quyền trước khi copy.
- **XState** (state machine), **Vue Flow** (biểu diễn graph), GitHub Projects/Issues/PR/CI và **Langroid**: chỉ là các ứng viên để đánh giá tương thích với Nuxt/Directus/GitHub hiện tại; không chốt kiến trúc, tránh thêm nền tảng vận hành thừa. Các repo micrograd/nn-zero-to-hero/minbpe/nanoGPT/llm.c/nanochat chủ yếu để học/train AI, không phải quy trình hội đồng.
- **Tiêu chí chọn thành phần:** tự vận hành; thay được hãng, API và worker; rõ license; lưu/khôi phục state; gắn được quy chế/quorum/evidence; chi phí/thời gian/độ bền; dùng được phần lớn mã đã có, không dựng lại UI/workflow từ đầu.

#### 3.4. Quyết định ranh giới repo — chỉ đưa ra hội đồng
- **A — Nâng cấp một `incomex-workspace`** quản cả công việc và không gian làm code, có phân ranh giới quyền/runtime rõ.
- **B — Workspace công việc + một repo `incomex-codespace` riêng** cho workflow/code, liên kết bằng mã task/node/PR.
- **C — Một đầu mối điều hành ở Workspace, code tiếp tục ở các repo mã hiện hữu** (`agent-data-test`, `web-test`), liên kết task ↔ branch/PR/KQ; không tạo kho mới nếu không cần.
- Đánh giá theo: một SSOT nghiệp vụ, tránh trùng dữ liệu, khác nhau giữa vòng đời thảo luận và vòng đời mã, kiểm soát quyền ghi/merge/CI/deploy, độ đơn giản trong Owner View, tốc độ agent chạy song song, chi phí vận hành. **Chưa chọn A/B/C; chưa tạo repo, nhánh, runner, script, rule hay migration nào.**

### Vòng trước
- Chưa có. Khối mục tiêu đầu tiên do Owner giao ngày 28/10/2026.

## Q — Câu hỏi xin Hội đồng phản biện vòng đầu
- **Q01 (quorum):** “Đồng ý của ≥1 AI khác hãng” khác “đã nhận xét” ra sao? Khi reviewer bất đồng, ai quyết mở vòng tiếp/xin Owner, giữ tối đa 3 vòng thế nào? Một chữ ký READY của Host vẫn giữ hay cần bổ sung gate machine-readable?
- **Q02 (node):** Mẫu một node đủ gọn mà đủ: vào/ra, người tham gia, KQ, đo PASS/FAIL, quyền Host, tồn dư được chừa sang node sau; tránh chia quá nhỏ/vòng kiểm vô ích?
- **Q03 (KQ):** Rà soát khác hãng mỗi lần worker KQ; bảo đảm reviewer độc lập cả với worker; làm sao reuse nhận xét nếu không đổi kỹ thuật mà vẫn không bỏ qua KQ mới?
- **Q04 (repo):** Chọn A, B hay C; có phương án gọn hơn? Quan trọng: “một hệ thống điều hành” không nhất thiết “một kho Git chứa mọi loại code”.
- **Q05 (reuse):** Chính xác file/module nào từ LLM Council/AutoResearch được học hoặc tái dùng hợp pháp, không đem theo OpenRouter API/GPU hoặc bản chất nghiên cứu model? Cân nhắc state machine/UI có sẵn.
- **Q06 (adapter):** Cơ chế chung để bất kỳ AI/agent qua Chat/CLI/MCP/app/API đều nhận cùng một phiếu, có receipt/identity rõ, bảo đảm từng ghế/khác hãng, thay nhà cung cấp dễ?
- **Q07 (chi phí):** Phân ranh giới phần nào phải tự động, phần nào Owner chuyển tay trước; chứng minh không phát sinh API/Actions ngoài ý muốn và không tạo dependency bắt buộc?

## P — Ý kiến, kết luận, lệnh
### P01 — GPT Host ghi nhận đề bài Owner (KHÔNG PHẢI ý kiến độc lập/đồng thuận)
Ghế: openai-main · Bước/vòng: G0/mở hồ sơ · 0/1
- Based_on: chỉ đạo trực tiếp Owner ngày 28/10/2026; AGENTS A0/A2/A5/A6/A8/A9; HEAD đọc khi lập hồ sơ `1cef5dff4d33882615467e450639a4489a4074fd`.
- Scope: `work/ai-council-karpathy/COLLAB.md` (A0, Bảng, §3, Q) và `view.html` (sơ đồ phương án).
- Đã ghi đủ phạm vi và câu hỏi cho hội đồng; **chưa có ý kiến của Claude/các ghế khác**; **chưa phải đạt quorum**; không lập PROMPT hay phát READY.
- Host đề xuất chuyển câu hỏi Q01–Q07 cho ghế Anthropic qua Owner; ghi P02 thật khi đã có phản biện, Host mới quyết vòng tiếp theo.

## Owner cần quyết
- —
