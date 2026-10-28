# COLLAB — ai-council-karpathy
Tên việc: AI-council-Karpathy — hội đồng AI độc lập và quy trình công việc/code thống nhất
Host: GPT Chat
Host_ID: openai-main
Owner giao: 2026-10-28
HTML chính: view.html
Phạm vi ghi đợt mở hồ sơ: work/ai-council-karpathy/; không thay luật nền, không đổi repo, không chạy Agent.

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
Xác nhận User: ĐÃ XÁC NHẬN — Owner chỉ đạo trực tiếp ngày 28/10/2026: lập task **AI-council-Karpathy** để thảo luận; **chưa phê duyệt triển khai kỹ thuật, nâng cấp Workspace hoặc mở repo code mới**. GPT Chat làm Host hiện hành cùng Owner theo mô hình Owner đã mô tả; không tự suy quyền cho Host vĩnh viễn hoặc các AI khác.

### BẢNG ĐIỀU KHIỂN · cập nhật 2026-10-28 16:58 +07 · Claude Reviewer · P05
- 🎯 **Mục tiêu:** Xây quy trình hội đồng/doanh nghiệp **do chúng ta sở hữu**, mọi Host (DOT/Duet/Grokbot/GPT/AI khác) chỉ điều hành trong khung luật nội bộ, hoán đổi model/hãng dễ dàng; tận dụng Karpathy + Workspace, quản lý việc và code; chuẩn bị lộ trình Hội đồng Host.
- 🏁 **Xong khi:** Phương án kiến trúc phải nêu rõ engine/quy chế độc lập hãng, cách thay Host/model không phá trạng thái hoặc vượt quyền, các giai đoạn Owner chỉ định thủ công → Host tự điều hành có kiểm soát → Hội đồng Host có chữ ký; tiêu chí đo/nghiệm thu kỹ thuật sẽ do hội đồng đề xuất, Owner chốt sau.
- 📍 **Tiến độ:** ✓ G0 Mở hồ sơ → ✓ G1 P02/P03 phản biện + GPT Host kết luận P04 (không mở vòng 2) → ■ G2 rà cổng cưỡng chế/kiến trúc và Owner chốt phạm vi → □ G3 thiết kế/roadmap → □ G4 triển khai/nghiệm thu nếu Owner duyệt.
- ✅ **Đã xong:** Claude P02/P03 độc lập khác hãng; GPT Host P04 đối chiếu mã nguồn Karpathy (cả frontend) và chốt danh sách nhóm 14 mẫu chính + L2/L4 tùy chọn; chọn hướng C (1 đầu mối điều hành, code ở 2 repo) làm phương án trình Owner; khẳng định A9 chỉ đọc/view không đủ cưỡng chế, cần gate trước mọi WRITE; chưa thay luật/code. **Claude P05:** đồng ý P04 (VERDICT có điều kiện, 3 chỉnh nhỏ); UI theo chỉ đạo Owner 16:48: dựng lại màn hội đồng 3 tầng kiểu llm-council + Vue Flow cho toàn cảnh, không dùng giao diện Stately; kế hoạch + roadmap N0–N4 đủ ô từng node; `view.html` vẽ roadmap + màn hội đồng mẫu.
- ■ **Đang làm:** — · 0 RUN active. Đã kết luận thảo luận G1 tại P04; G2 = thống nhất kế hoạch + roadmap (P05 chờ Host chốt), KHÔNG có lệnh chạy.
- ⬜ **Còn lại:** Rà code gateway/A9/Owner View và cổng PR/CI/code thực (N0), xác định đường ghi có thể đi vòng; thiết kế vé ghi một lần + quorum/VERDICT + chuông giám sát; kiểm giấy phép nếu sao chép nguyên văn; Owner duyệt C và đường triển khai N1–N4; thử âm và Host lạnh.
- ➡ **NEXT_TRIGGER=HOST_CONCLUDE_PLAN_P05:** GPT Host đọc P05, chốt D02 (kế hoạch P05.4 + roadmap P05.5) không mở vòng 2; ghi 1 dòng `Owner cần quyết` (đề xuất GẬT); cùng lượt soạn PROMPT N0 chỉ đọc (Worker Claude Code CLI) + READY để Owner chuyển ngay khi gật.
- ⛔ **Không làm/để sau:** Không sửa AGENTS/luật gốc; không di chuyển mã hoặc dữ liệu, đổi quyền hay tạo repo code; không thêm task phụ; không triển khai công nghệ, không phát READY/PROMPT/RUN; không ép dùng API trả phí.

### 1. Mục tiêu
1. “Chúng ta hướng tới những tính năng tự động cao, nhưng hội đồng của chúng ta tổ chức theo 1 nguyên tắc là không bị phụ thuộc vào bất cứ nhà cung cấp nào. Tức là bất cứ ai cũng có thể tham gia.”
2. “Đồng ý về bản chất: Workflow Engine tức là, Có 1 AI (có thể bao gồm cả con người điều hành theo quy định) tức là mỗi bước nhỏ đều có khung rõ rõ ràng (quy định sau) và tất cả các AI làm việc trong khung đó, bao gồm những việc phải làm, vòng lặp phải kiểm tra, những ai phải tham gia? Thế nào là hoàn thành..... việc này chúng ta sẽ quy định chuẩn sau.”
3. “Đưa vào 1 công thức chung là: ý kiến cũng phải có sự đồng ý của ít nhất 1 ai khác hãng, bên cạnh Host (Host quyết).”
4. “Cách tiếp cận đơn giản là chúng ta dùng công nghệ của: Karpathy Như đã bàn để nâng cấp quy trình work space, tận dụng các cơ chế đã có của Karpathy kết hợp với các cơ chế mà chúng ta đã viết cho work space để có 1 hệ thống hoàn chỉnh.”
5. “Không chỉ ý kiến là cần hội đồng theo nguyên tắc, mỗi lần agent báo cáo kết quả, Host cũng cần đọc báo cáo, soạn prompt tiếp theo (theo roadmap) và cần ý kiến hội đồng (ít nhất 1 ý kiến của ai khác hãng) Host cân nhắc, nếu cần thiết sẽ mở thêm vòng thảo luận, hoặc quyết định soạn prompt tiếp theo và chỉ định agent thực hiện.”
6. “Tôi thì muốn là đồng bộ kể cả công việc lẫn việc viết code, quản lý cho đơn giản. Nhưng vì tính chất công việc hơi khác nhau => cái này cứ đưa lên rồi hội đồng cho ý kiến.”
7. “Trước hết chúng ta lập ra cái này để thảo luận, vì cái này AI-council-Karpathy là mức task. Còn chuyện nâng cấp Repo, hay mở thêm Repo code space đợi hội đồng cũng có ý kiến rồi chúng ta quyết định.”
8. “DOT/Duet/Grok bot... Có xu hướng là được thiết kế để điều hành, chúng ta vẫn dùng các sản phẩm này, nhưng chỉ cho phép điều hành trong khung hệ thống của chúng ta. Không cần phụ thuộc vào bất cứ hãng nào, và có thể đổi model điều hành dễ dàng. Mục tiêu ban đầu phải xây dựng dứt khoát là như vậy.” — Owner bổ sung 28/10/2026; **ràng buộc kiến trúc đầu tiên, không phải tính năng tùy chọn**.
9. “Hiện giờ thì User vẫn điều hành bằng tay => thông qua chỉ định Host. Nhưng khi quy trình đã tối ưu và các AI hoàn thiện hơn, các cơ chế như vector, graph... hỗ trợ hiệu quả hơn => sẽ chuyển dần do HOT điều hành, lúc này có thể có hội đồnhg Host (Host trưởng và các thành viên). Và ở trên này sẽ là đồng thuận (có chữ ký) => đó là cấu trúc sẽ hướng tới nhưng chúng ta phải vạch ra từ bây giờ để chuẩn bị các hạ tầng kĩ thuật.” — Owner bổ sung 28/10/2026; “HOT” hiểu theo ngữ cảnh là **Host**, giữ nguyên văn phát biểu Owner.
10. “Chúng ta giữ cái của chúng ta làm nòng cốt => nhưng hướng tới việc cưỡng chế chứ không phải quy định. Vì vậy nghiên cứu và bê những thứ cưỡng chế, view thứ tự nhìn từng bước mà bộ của Karrphthy đã làm về => đỡ phải làm.” — Owner 28/10/2026.
11. “Liệt kê được danh sách cụ thể các đồ cần dùng (hội đồng cần thống nhất) sau đó ghi thẳng lên task, có thể cho agent khảo sát cụ thể hơn nếu cần để đưa ra quyết định cuối cùng.” — Owner 28/10/2026.
12. “từng bước có Host điều hành, có hội đồng theo từng ghế cho ý kiến, có quy định thế nào là mở thêm vòng nữa, đi tiếp, dừng lại báo cáo user. Sau này có thể thêm cả vai trò Giám sát.” — Owner 28/10/2026.
13. “Nguyên tắc định danh và cưỡng chế. Viết rất ngắn gọn là quy định thì dễ bị vi phạm, trong khi cưỡng chế thì không thể vi phạm => ưu tiên phương án là cưỡng chế, tức không thể làm sai.” — Owner 28/10/2026.
14. “đọc thoải mái, nhưng muốn ghi, phải khai báo danh tính để lấy vé tạm 1 lần vào ghi” — Owner 28/10/2026, mô hình đề xuất để hội đồng thẩm định.

### 2. Thế nào là hoàn thành
“Cái lý tưởng tôi nhìn thấy là ở mỗi bước, chúng ta biết tiến độ đến đâu? biết bước gì tiếp theo? Biết đang ở bước nào? Biết bước nào tắt hay là mọi việc vẫn theo kế hoạch?” — Owner 28/10/2026 (trao đổi liền trước).
“Trước hết chúng ta lập ra cái này để thảo luận [...] đợi hội đồng cũng có ý kiến rồi chúng ta quyết định.” — Owner 28/10/2026.
“Không cần phụ thuộc vào bất cứ hãng nào, và có thể đổi model điều hành dễ dàng. Mục tiêu ban đầu phải xây dựng dứt khoát là như vậy.” — **tiêu chí kiến trúc bắt buộc** do Owner bổ sung 28/10/2026.
“Và ở trên này sẽ là đồng thuận (có chữ ký) => đó là cấu trúc sẽ hướng tới nhưng chúng ta phải vạch ra từ bây giờ để chuẩn bị các hạ tầng kĩ thuật.” — **tiêu chí thiết kế hướng tới Hội đồng Host**, chưa phải phép bật cơ chế nhiều người ký ở hiện tại.
**Đòi hỏi trong phương án trước khi trình Owner:** chỉ ra được cách hoán đổi Host/model/hãng mà không phải đổi quy chế, không mất trạng thái/nhật ký, không vượt quyền; lộ trình tăng tự động hóa từng cổng và hợp đồng chữ ký/đồng thuận của Hội đồng Host tương lai. Phép thử và chuẩn nghiệm thu chi tiết phải được hội đồng đề nghị rồi Owner duyệt.
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
- **Cưỡng chế, không mô tả — nhặt tối đa từ Karpathy (Owner 28/10/2026 15:50 · HUMAN_DIRECTIVE@AI-COUNCIL-KARPATHY-REUSE-20261028):** xem chi tiết từng khung của Karpathy, cái gì chép hoặc viết lại được thì lấy để đỡ phải viết; mỗi luật đưa vào phải kèm chốt máy; kết luận rõ dùng / không dùng + lý do (xem P03).
- **UI cho người — tận dụng tối đa cái làm sẵn (Owner 28/10/2026 16:48 · HUMAN_DIRECTIVE@AI-COUNCIL-UI-REUSE-20261028):** xem kỹ và tận dụng tối đa các UI đẹp, làm sẵn (mẫu hội đồng của llm-council…) cho phần người dùng, trong khuôn khổ cấu trúc ta cần; thống nhất kế hoạch rõ ràng + roadmap rồi vào triển khai (xem P05).
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

#### 3.5. TIÊU CHÍ KIẾN TRÚC BẮT BUỘC — HOST THAY ĐƯỢC, QUY CHẾ DO CHÚNG TA SỞ HỮU (Owner 28/10/2026)
- **Phân lớp không phụ thuộc hãng:** `Workflow Engine / State Machine + Council Governance + SSOT/Decision Ledger` là **hệ thống của chúng ta**; DOT, Duet, Grokbot, GPT hay bất kỳ model/AI điều hành nào chỉ là **Host Runtime/Adapter** được cấp ghế, định danh, quyền và phạm vi; sản phẩm ngoài không tự áp luật, tự đổi roadmap, tự chốt hay vượt quy trình.
- **Host có thể thay:** phân biệt `Host_Seat / Host_ID / quyền được ủy nhiệm` với `Model/Provider/Surface/Adapter`; khi đổi model hoặc hãng, nhiệm vụ, node, P/KQ, chữ ký cũ, trạng thái, bằng chứng, NEXT_TRIGGER vẫn đọc và kiểm chứng được. Đổi **người/ghế giữ quyền Host** hiện vẫn do Owner quyết theo A2; đổi model kỹ thuật không được là cách lách quyền Host.
- **Giai đoạn 0 — hiện tại:** User chọn Host và chuyển lệnh thủ công; GPT Chat + Owner điều hành task này, phản biện khác hãng theo A5; chỉ **một chữ ký READY của Host/Co-host hợp lệ** theo A6/DROOT58. Không giả định DOT/Duet/Grokbot đã có quyền hoặc đang chạy tự động.
- **Giai đoạn 1 — từng phần tự động:** Host AI nhận quyền điều hành theo lớp nhiệm vụ và cổng Owner phê duyệt, thực thi đúng state machine, có receipt, bằng chứng, rollback/dừng, danh tính và audit. Quyền Owner và cổng an toàn giữ nguyên, chỉ bỏ thao tác tay sau khi thử nghiệm/duyệt.
- **Giai đoạn 2 — Hội đồng Host:** hướng tới **Host trưởng + các Host thành viên** (có thể khác hãng/model) tại tầng điều hành phía trên Hội đồng AI nghiệp vụ; quyết định ở tầng Host theo cơ chế **đồng thuận có chữ ký xác thực**, chứng minh được ai ký, cho phương án/phiên bản/nút nào, điều kiện quorum và kiểm tra chống ký trùng hoặc giả. Phân vai ai đề xuất, ai duyệt, ai có quyền quyết khi bất đồng và khi nào Owner can thiệp phải đưa ra hội đồng/Owner chốt sau. **Không áp quy tắc đa chữ ký này vào READY hiện tại khi AGENTS chưa sửa hợp lệ.**
- **Vector/graph/tri thức:** thiết kế cổng dữ liệu và truy vết nguồn phục vụ lập kế hoạch, đối chiếu quyết định, tìm phụ thuộc và kiểm nghiệm; dữ liệu truy hồi **không được tự biến thành mệnh lệnh/quyền**, không buộc một nhà cung cấp vector/graph/model nào. Không triển khai trước khi hội đồng thống nhất nhu cầu, độ tin cậy và bảo mật.
- **Tiêu chí nghiệm thu cần lập kế hoạch đo:** thay runtime/model Host trên một task đang chạy mà không chuyển/hỏng SSOT; cùng quy chế điều hành không cần sửa theo hãng; model ngoài không thể bypass ký lệnh/quorum/Owner/Guard; giữ audit và node, KQ, chữ ký khi thay Host; chứng minh tương lai có thể kiểm chữ ký/quorum của Hội đồng Host. Các bài kiểm, độ sâu và cổng GO phải do hội đồng phê bình rồi Owner duyệt, chưa tuyên PASS.
- **Nguyên tắc kế thừa:** tái sử dụng LLM Council/AutoResearch (theo giấy phép) và cơ chế Workspace đã viết; không chọn kiến trúc chỉ vì DOT/Duet/Grokbot có orchestration sẵn, không tạo phụ thuộc bắt buộc vào API, hãng hoặc nguồn lưu trữ ngoài.

#### 3.6. KHUNG THIẾT KẾ G1 DO HOST KẾT LUẬN — cưỡng chế và view từng node (P04)
- **Bộ điều hành phải có quyền hạn máy kiểm được:** Owner xác định mục tiêu/quyền → Host hiện hành nêu node/giải pháp → các ghế đưa ý kiến độc lập + `VERDICT` bám đúng revision → Host quyết trong thẩm quyền → gate cho phép ký READY/vé ghi → Worker làm và nộp KQ máy kiểm → Reviewer khác hãng rà KQ → Host chọn `NEXT | REWORK | ESCALATE`. Mặc định 1 vòng; Host chỉ mở vòng 2/3 khi bất đồng thực chất hoặc bằng chứng chưa đủ, tối đa 3; còn xung đột hoặc quyền Owner ⇒ ESCALATE, không ghi đồng thuận giả. **Đây là yêu cầu kiến trúc**, chưa thay A5/A6 khi Owner chưa phê duyệt luật.
- **Giám sát độc lập (tương lai):** ghế `Supervisor` được giám sát từng node, mở `COUNCIL_ALERT` có evidence và báo Telegram tới Owner; alarm mở chặn chuyển bước đúng scope; người bị giám sát không được tự đóng. Kế thừa A5 hiện hữu, không tạo hệ chuông mới.
- **Ưu tiên một vé ghi một lần, thay vì ép mọi khách đọc phải đeo thẻ:** đọc nội dung **theo quyền đọc hiện có** không cần vé; muốn ghi, gateway/đường merge phải **xác thực danh tính thực từ kết nối/credential**, đối chiếu seat+role+Owner/Host+quorum+revision+scope rồi mới cấp một `WRITE_TICKET` một lần (actor, task, node, op/path, ref/SHA, expiry, nonce, idempotency). Vé được tiêu thụ nguyên tử, ghi audit; sửa theo bản mới hoặc vượt scope ⇒ từ chối và xin vé khác. **Tự nhập tên không phải xác thực.** Không có tính cưỡng chế nếu còn cổng Git/SSH/admin/agent tool ghi khác đi vòng được; N0 phải kiểm kê hết đường bypass trước khi hứa “không thể làm sai”.
- **Chỗ cưỡng chế đúng:** gateway + identity/permission cho Workspace; protected PR/CI/merge/runner cho repo code; Owner-only cho scope ngoài ủy quyền. **Bộ đọc A9 và Owner View chỉ là quan sát/phản ánh**: nó có thể tô đỏ sai nhưng không thay thế chặn mutation *trước khi ghi*.
- **Một view hiện hành, không SSOT thứ hai:** cùng trang Task từ `COLLAB.md`/Git + trạng thái PR/CI: `roadmap nodes | node đang ở đâu | ghế đủ/thiếu phiếu | verdict/quorum | KQ/CI | next trigger | alert giám sát`. Mẫu Stage1/2/3 tabs của llm-council là giao diện từng tầng trong *một câu hỏi*, **không phải sản phẩm roadmap đa node**; cần tự xây view phù hợp hoặc lấy thư viện UI có phép phù hợp. Không copy JSX/CSS của repo không LICENSE.
- **Cần khung máy đọc cho mỗi node (bản thiết kế):** `node_id; revision; goal; input_ref; worker/host/reviewer/supervisor; allowed_write; deadline/budget; doD/test_ref; evidence_ref; verdict_ref; open_alarm; next_transition; deferred_items`. Quy chế, quota, version và chữ ký Host/Hội đồng Host tương lai nằm ở ledger của ta, không để runtime provider tự định nghĩa.

### Vòng trước
- Chưa có. Khối mục tiêu đầu tiên do Owner giao ngày 28/10/2026; bổ sung mục 8–9 và tiêu chí ngày 28/10 được cập nhật trong vòng hiện hành, không xóa lịch sử.

## Q — Câu hỏi xin Hội đồng phản biện vòng đầu
- **Q01 (quorum):** “Đồng ý của ≥1 AI khác hãng” khác “đã nhận xét” ra sao? Khi reviewer bất đồng, ai quyết mở vòng tiếp/xin Owner, giữ tối đa 3 vòng thế nào? Một chữ ký READY của Host vẫn giữ hay cần bổ sung gate machine-readable?
- **Q02 (node):** Mẫu một node đủ gọn mà đủ: vào/ra, người tham gia, KQ, đo PASS/FAIL, quyền Host, tồn dư được chừa sang node sau; tránh chia quá nhỏ/vòng kiểm vô ích?
- **Q03 (KQ):** Rà soát khác hãng mỗi lần worker KQ; bảo đảm reviewer độc lập cả với worker; làm sao reuse nhận xét nếu không đổi kỹ thuật mà vẫn không bỏ qua KQ mới?
- **Q04 (repo):** Chọn A, B hay C; có phương án gọn hơn? Quan trọng: “một hệ thống điều hành” không nhất thiết “một kho Git chứa mọi loại code”.
- **Q05 (reuse):** Chính xác file/module nào từ LLM Council/AutoResearch được học hoặc tái dùng hợp pháp, không đem theo OpenRouter API/GPU hoặc bản chất nghiên cứu model? Cân nhắc state machine/UI có sẵn.
- **Q06 (adapter):** Cơ chế chung để bất kỳ AI/agent qua Chat/CLI/MCP/app/API đều nhận cùng một phiếu, có receipt/identity rõ, bảo đảm từng ghế/khác hãng, thay nhà cung cấp dễ?
- **Q07 (chi phí):** Phân ranh giới phần nào phải tự động, phần nào Owner chuyển tay trước; chứng minh không phát sinh API/Actions ngoài ý muốn và không tạo dependency bắt buộc?
- **Q08 (bộ điều hành thay được):** Cấu trúc tối thiểu nào giữ state machine/quy chế/ledger do ta làm chủ, trong khi DOT/Duet/Grokbot/GPT chỉ là runtime có thể thay ngay cả giữa nhiệm vụ, không mất quyền định danh/decision trail?
- **Q09 (Hội đồng Host và chữ ký):** Thiết kế từ bây giờ các trường/khối chuẩn nào cho chữ ký xác thực, quorum, phiên bản quyết định và phân vai Host trưởng/Host thành viên? Làm sao không lẫn với một chữ ký READY hiện tại và không thêm vòng duyệt vô ích?
- **Q10 (lộ trình tự trị và tri thức):** Tiêu chí đo nào đủ để chuyển từ Owner chỉ định Host thủ công → Host AI tự điều hành có hạn → Hội đồng Host có chữ ký; vai trò vector/graph, kiểm nguồn/sai lệch và cổng quay lại Owner ra sao?
- **Q11 (vé ghi):** Ai xác thực danh tính để cấp WRITE_TICKET một lần, ở đường ghi nào, chặn direct Git/CLI/admin ra sao, revoke/TTL/CAS/idempotency thế nào? Những đường chưa bị khoá phải công khai là NOT_ENFORCED.
- **Q12 (view):** Reuse thành phần tab 3 tầng từ Karpathy ở mức nào là hợp pháp/phù hợp, có nên giữ view hiện tại và tăng dần theo node? Chứng minh không tạo SSOT thứ hai; so sánh thư viện Vue Flow nếu thực sự cần graph.

## P — Ý kiến, kết luận, lệnh
### P01 — GPT Host ghi nhận đề bài Owner (KHÔNG PHẢI ý kiến độc lập/đồng thuận)
Ghế: openai-main · Bước/vòng: G0/mở hồ sơ · 0/1
- Based_on: chỉ đạo trực tiếp Owner ngày 28/10/2026; AGENTS A0/A2/A5/A6/A8/A9; HEAD đọc khi lập hồ sơ `1cef5dff4d33882615467e450639a4489a4074fd`.
- Scope: `work/ai-council-karpathy/COLLAB.md` (A0, Bảng, §3, Q) và `view.html` (sơ đồ phương án).
- Đã ghi đủ phạm vi và câu hỏi cho hội đồng; **chưa có ý kiến của Claude/các ghế khác**; **chưa phải đạt quorum**; không lập PROMPT hay phát READY.
- Host đề xuất chuyển câu hỏi Q01–Q10 (gồm chỉ đạo Owner mới về Host hoán đổi và Hội đồng Host) cho ghế Anthropic qua Owner; ghi P02 thật khi đã có phản biện, Host mới quyết vòng tiếp theo.

HUMAN_DIRECTIVE@AI-COUNCIL-HOST-FUTURE-20261028 EFFECTIVE · task=ai-council-karpathy · scope=§0.1/§0.2/§3.5/Q08–Q10 · step=G1/phạm vi thảo luận · recorded_by=openai-main (GPT Chat) · quote=«Không cần phụ thuộc vào bất cứ hãng nào, và có thể đổi model điều hành dễ dàng. Mục tiêu ban đầu phải xây dựng dứt khoát là như vậy.» · text=Luật/quy chế thuộc hệ thống ta; dùng DOT/Duet/Grokbot như bộ điều hành thay thế được; hiện Owner chọn Host thủ công; chuẩn bị chuyển dần sang Host AI và Hội đồng Host có chữ ký; chưa đổi luật nền hay quyền RUN. · audit=Owner trực tiếp bổ sung 28/10/2026; chờ phản biện độc lập.

### P02 — Claude phản biện độc lập G1 · Karpathy, công nghệ, Q01–Q10
Ghế: anthropic-review · Bước/vòng: G1 · 1/3
- Người góp ý: Claude Chat (Anthropic — khác hãng Host) · Trạng thái: **PARTIAL** (Host xử lý tại P04; không mở vòng 2)
- Based_on: `c95100e8c974817f3c69991825a8ef3753b77f3b` · Scope: task này §0–§3.5, Q01–Q10, P01, `view.html`; AGENTS A2/A3/A5/A5-AUTO/A6/A7(DROOT59)/A9/A10; Bảng `work/github-management` (P91).
- Chưa đọc: COLLAB gốc (367 KB), README Technical Contract, mã nguồn bộ đọc A9/gateway (chỉ suy từ luật, CHƯA ĐO).
- Nguồn ngoài đã kiểm 28/10/2026: trang GitHub `karpathy/llm-council`, `karpathy/autoresearch`; GitHub changelog (gh-aw 13/02/2026, required reviewer GA 17/02/2026); GitHub ToS (tài khoản máy); kubernetes.dev OWNERS; techstrong (AutoGen bảo trì). JEV tham khảo: repo=C (1.00) · nền=gateway+PG/Directus (1.00) · llm-council/autoresearch = chỉ học mẫu (0.86/0.94) · cần Vue Flow? 0.14 · GH Projects làm view? 0.10 — chỉ là bằng chứng phụ.

**VERDICT: ĐỒNG Ý-CÓ-ĐK** — đồng ý mục tiêu và phân lớp §3.5; **KHÔNG đồng ý** lấy XState / Vue Flow / Langroid / GitHub Projects / gh-aw làm nền; chọn **C**.

#### P02.1 Kết luận (đọc 30 giây)
1.1 Karpathy **không có “công nghệ hội đồng”** để ghép: llm-council là bản hack cuối tuần, tác giả tuyên bố không hỗ trợ, không giấy phép; autoresearch là thí nghiệm train mô hình trên GPU ⇒ **0 dòng mã lấy về, lấy 4 mẫu tư duy** (P02.3).
1.2 Hội đồng của ta **đã đủ khái niệm** (ghế, định danh, READY@SHA, cờ bận, chuông, AUTO0–3) — nhiều hơn mọi framework ngoài. Cái thiếu không phải engine, mà là: **(a)** luật 88 KB, AI không đọc hết; **(b)** luật quan trọng chưa máy cưỡng chế (R2); **(c)** Owner chưa thấy roadmap từng node.
1.3 Vì vậy: **không thêm engine/thư viện**; vá đúng 3 chỗ thiếu ngay trên cái đã có (repo + gateway + bộ đọc A9 + Owner View). Code mỏng chỉ ở 2 nơi đã tồn tại. `Bậc: 1 có sẵn + 3 code mỏng ở chỗ có sẵn`.

#### P02.2 Bảng chấm công nghệ (độ bền dài hạn)
| Thứ | Thực chất (đã kiểm) | Độ bền | Kết luận |
|---|---|---|---|
| llm-council | 5 commit; README tự nhận “vibe coded”, tác giả không hỗ trợ; không LICENSE; bắt buộc OpenRouter API | 🔴 bỏ hoang từ đầu | Chỉ học mẫu |
| autoresearch | MIT; train trên 1 GPU NVIDIA; `program.md` = “skill” 1 trang | 🟡 thí nghiệm | Chỉ học mẫu |
| XState | MIT, công ty Stately; v6 đang alpha (sắp đổi API) | 🟢 thư viện · 🔴 với ta | Không dùng: phải dựng thêm dịch vụ giữ trạng thái và bắt mọi lệnh ghi đi qua nó = viết lại gateway |
| Vue Flow | MIT, ~6.9k★, gần như 1 người duy trì | 🟡 | Không cần: Owner cần thanh tiến độ + ma trận màu, không cần trình vẽ đồ thị |
| Langroid | ~4.1k★, xoay quanh gọi LLM qua API | 🟡 | Loại: trái nguyên tắc hạn chế API |
| gh-aw | Technical preview (02/2026), chạy trên Actions, mặc định Copilot | 🔴 preview + rủi ro phí Actions | Loại |
| GitHub Projects | Kanban miễn phí | 🟢 | Loại cho task: là bản xem thứ 2 (A8 cấm) |
| **Repo + gateway + bộ đọc A9 + Owner View** | Đã chạy, đã nghiệm thu | 🟢 Git/GitHub + của ta | **Nền** |
Bài học độ bền: AutoGen của Microsoft đã vào chế độ bảo trì (04/2026, thay bằng Agent Framework) — framework đa agent thay đời rất nhanh; thứ sống lâu là Git, PR, CI, PG.

#### P02.3 Lấy gì từ Karpathy — 4 mẫu, 0 dòng mã *(đã thay bằng P03.2–P03.4 sau khi đọc mã nguồn)*
3.1 **`program.md` → Thẻ vai 1 trang:** mỗi vai (Host / Reviewer / Worker) một thẻ ≤1 trang rút từ AGENTS; AI vào ghế chỉ cần đọc thẻ + Bảng. Đánh thẳng lỗi “luật dài AI không đọc hết”.
3.2 **Một thước đo (val_bpb) → mỗi node 1 phép đo xong:** một lệnh/kiểm trả xanh/đỏ; task mã dùng luôn cổng CI `gate` GREEN đã có ở github-management.
3.3 **Ngân sách cố định + giữ/bỏ:** mỗi node có trần giờ/lượt; hết trần mà chưa đạt ⇒ bỏ hoặc tách node, không kéo dài.
3.4 **Ý kiến độc lập trước khi đọc nhau (llm-council giai đoạn 1):** với quyết định lớn (roadmap/kiến trúc), ghế khác hãng viết phương án riêng *trước* khi đọc đề xuất Host để tránh “hùa theo”. Không lấy phần ẩn danh — ta cần định danh để chịu trách nhiệm.

#### P02.4 Trả lời Q01–Q10
- **Q01:** “Đồng ý” = **một dòng máy đọc trong P vốn phải viết**, không phải chữ ký thứ hai: `VERDICT@<sha bản nháp> ĐỒNG Ý|ĐỒNG Ý-CÓ-ĐK|KHÔNG ĐỒNG Ý · by=<ghế>`. Host vẫn ký READY duy nhất (giữ DROOT58). READY hợp lệ khi có ≥1 VERDICT ĐỒNG Ý/CÓ-ĐK của ghế khác hãng Host, sau thay đổi kỹ thuật cuối (`REVIEW_REUSED` giữ nguyên cho sửa hành chính). KHÔNG ĐỒNG Ý ⇒ Host sửa và mở vòng 2/3, hoặc gọi thêm một ghế khác hãng; hết vòng 3 ⇒ Owner quyết một dòng. Không có “Host vượt”. Cần sửa A5/A6 (Founders đề xuất, Owner gật).
- **Q02:** Node 7 ô: mục tiêu · người làm · đọc gì · ghi gì · phép đo xong (đúng 1) · ngân sách giờ/lượt · phần chừa sang node sau. Đặt trong vùng máy sẵn có của COLLAB, không thêm file.
- **Q03:** Sau mỗi KQ: 1 VERDICT của ghế khác hãng Host, người rà ≠ chính Worker. Với 2 hãng chính, điều kiện “khác hãng Worker” của A5 tự thỏa (Host hoặc Reviewer luôn khác hãng Worker) ⇒ không cần ghế thứ ba. KQ là bằng chứng mới nên luôn cần VERDICT mới, nhưng chỉ rà phần chênh.
- **Q04:** **C.** Workspace public, không CI, chỉ ghi qua cổng — đem mã vào (A) phá cả ba; repo mới (B) đẻ thêm nơi thứ ba. Hai repo mã đã có PR + cổng CI GREEN (G1 PASS ở github-management). Nối bằng mã việc trong tên nhánh/PR `<task-id>/<node>-…`; Owner View đọc trạng thái PR/CI ⇒ Owner thấy chung một chỗ. “Một hệ thống điều hành ≠ một kho Git.”
- **Q05:** 0 mã từ hai repo (llm-council không giấy phép + không hỗ trợ; autoresearch là train GPU). Lấy 4 mẫu P02.3.
- **Q06:** Bộ chuyển **đã có** = gateway MCP + nhãn định danh phía máy chủ (bảng A9) + thẻ vai. AI mới = 1 hồ sơ + 1 dòng mapping + đọc thẻ vai. AI chưa có MCP ⇒ Owner chuyển tay (AUTO0). Không cần framework.
- **Q07:** Không dùng API, không Actions ở workspace; CI mã đã chạy runner trên VPS. Code mỏng chỉ ở bộ đọc A9/Owner View (tùy chọn thêm: gateway từ chối dòng READY thiếu VERDICT — mức cưỡng chế R2 đầy đủ).
- **Q08:** Cấu trúc tối thiểu đã đủ: luật + trạng thái + sổ quyết định ở repo, định danh ở gateway, Host = dòng `Host:` do Owner chỉ định. Thiếu đúng 2 thứ: thẻ vai Host + **phép thử “Host lạnh”**: một model khác hãng, không lịch sử chat, nhận Host giữa chừng và làm đúng bước kế chỉ từ repo. Đạt phép thử này = “đổi Host dễ” đã chứng minh. DOT/Duet/Grokbot chỉ hành động qua repo/gateway; tính năng tự điều phối riêng của sản phẩm không có hiệu lực với hội đồng.
- **Q09:** Chuẩn bị ngay, không xây: dòng `DECISION@<id> rev<n> · on=<sha> · by=<ghế>`. Commit qua gateway đã mang định danh ⇒ là chữ ký mức truy vết. Hội đồng Host sau này = đủ N ghế (≥2 hãng) ký cùng rev; nâng lên chữ ký mật mã bằng ký commit SSH chuẩn Git (GitHub hiện “Verified”) cho từng ghế tại gateway. Mẫu đã kiểm chứng ngoài đời: Kubernetes tách reviewer `/lgtm` và approver `/approve`. READY tách riêng: DECISION = chốt phương án, READY = cho chạy.
- **Q10:** Thang AUTO0–3 (DROOT46) đã đủ; chỉ thêm cổng đo: (a) đạt “Host lạnh”; (b) một loại việc chạy liền N node không có chuông vượt quyền, không vi phạm VERIFY-OR-RED ⇒ Owner nâng mức cho loại đó. Vector/graph chỉ là gợi ý có nguồn, không bao giờ là quyền; ngoài phạm vi N1–N4.

#### P02.5 Roadmap đề xuất (Host chốt; dừng sau N4)
| Node | Làm gì | Ai | Đo xong |
|---|---|---|---|
| N1 | Thẻ vai ×3 (≤1 trang), mẫu node 7 ô, dòng VERDICT/DECISION; bản sửa A5/A6 | Founders (GPT + Claude) | Owner gật 1 dòng |
| N2 | Bộ đọc A9 hiểu NODE/VERDICT; READY thiếu VERDICT khác hãng ⇒ đỏ; Owner View: thanh node (đúng 1 ô đang làm) + ô màu ghế đã/thiếu ý kiến + PR/CI của repo mã | Claude Code CLI | Thử âm: READY thiếu VERDICT hiện đỏ |
| N3 | Chạy thật 1 node (vd github-management F2) + thử “Host lạnh” | Host + Worker | Owner View đúng từng bước; Host mới làm đúng bước kế |
| N4 | Owner nhìn 30 giây | Owner | Owner nói “đạt” |
Ngoài phạm vi: Hội đồng Host thật, AUTO1+, vector/graph, repo mới, cài thư viện mới.

#### P02.6 Sửa dữ kiện trong §3.3 / P01
6.1 ~~autoresearch có giấy phép MIT (trang GitHub ghi rõ); §3.3 ghi “chưa tìm thấy LICENSE” là chưa đúng.~~ **Claude ghi sai — đã sửa ở P03.5.**
6.2 llm-council: ngoài thiếu giấy phép, README **tự tuyên bố không hỗ trợ** — rủi ro bỏ hoang là chắc chắn, nên ghi rõ.
6.3 Đếm đồng ý bằng phê duyệt GitHub PR theo từng ghế là **chưa khả thi**: ToS GitHub chỉ cho 1 tài khoản máy miễn phí/người; repo mã hiện chỉ một danh tính (P91: `KST_ONLY_MERGE_ENFORCED=NO`); phê duyệt của bot có thể không được tính. ⇒ Cổng đồng thuận đặt ở gateway (đã biết định danh từng ghế) — đúng mô hình «một thẻ · hai cổng» của Owner.

#### P02.7 Đề nghị Host
7.1 Chốt G1 **ngay vòng này** (không thấy bất đồng thực chất cần vòng 2): ghi D chọn C + nền “repo + gateway + A9”, loại 5 công nghệ ở P02.2, ghi lại 4 mẫu P02.3.
7.2 Đưa Owner đúng 1 dòng: «Duyệt hướng: không cài công nghệ mới; học 4 mẫu Karpathy; thêm thẻ vai + dòng đồng ý khác hãng; repo theo C. Đề xuất: GẬT.»
7.3 Sau khi chốt, sửa `view.html`: thay khối A/B/C bằng kết luận + thanh N1–N4, không giữ 3 phương án như còn mở.

Phản hồi Host (P04): **PARTIAL** — nhận C làm phương án đề xuất, nền gateway + Git + Owner View và vòng mặc định 1; nhưng không thể nói `A9 tô đỏ` là đã chặn ghi và không được loại XState/Vue Flow bằng lập luận phải thêm dịch vụ. Chi tiết ở P04.

### P03 — Claude bổ sung theo chỉ đạo Owner 15:50: đọc mã nguồn Karpathy, nhặt từng món
Ghế: anthropic-review · Bước/vòng: G1 · 1/3 (bổ sung cùng vòng; thay P02.3, sửa P02.6.1)
- Trạng thái: **PARTIAL** (Host xử lý tại P04) · Based_on: `57af19fac1429658b868d9aad9c547e93932f0de` + mã nguồn đã tải về đọc thật: `karpathy/autoresearch@228791f` (commit cuối 25/03/2026) và `karpathy/llm-council@92e1fcc` (cả 5 commit trong ngày 22/11/2025).
- Đã đọc: `program.md`, `prepare.py` (hằng số + `evaluate_bpb`), `train.py` (ngân sách, dừng sớm, khối in cuối), README; `backend/council.py` (3 giai đoạn, bộ đọc xếp hạng, điểm tổng), `CLAUDE.md`. Chưa đọc: frontend React, `analysis.ipynb`.
- JEV tham khảo: phần lớn dùng được 0.92 · giá trị K5 = cao 0.88 · ẩn danh khi rà KQ phù hợp? 0.16 · vòng giữ/bỏ cho việc bàn? 0.12 · chép nguyên văn llm-council an toàn pháp lý? 0.14.

#### P03.1 Kết luận dứt khoát
1.1 **DÙNG ĐƯỢC 16 món:** 10 món từ autoresearch (README ghi MIT ⇒ chép văn bản được, ghi nguồn) + 6 món từ llm-council (không giấy phép ⇒ không chép chữ/mã, tự viết lại ý; toàn bộ logic chỉ ~60 dòng).
1.2 **KHÔNG DÙNG 5 thứ** (P03.4): mã chạy của cả hai repo, 6 repo học AI, vòng giữ/bỏ cho việc bàn, ẩn danh khi rà KQ, bộ công nghệ GPT đề xuất.
1.3 **Phát hiện khi đọc mã:** Karpathy cũng chỉ chặn bằng máy 4 chỗ — file chấm cố định, ngân sách giờ, dừng sớm khi hỏng, khối số cuối do máy in. Còn lại là lời dặn trong `program.md` + git để hoàn tác. ⇒ Ta chép khuôn của ông, rồi gắn **mỗi món một chốt máy** ở cổng có sẵn (bộ đọc A9 / CI repo mã / gateway).
Ký hiệu cột chặn: 🤖 máy chặn thật · 📝 lời dặn.

#### P03.2 Nhặt từ autoresearch — chép được (MIT theo README)
| Mã | Món | Karpathy chặn bằng | Ta dùng thế nào | Chốt máy của ta |
|---|---|---|---|---|
| K1 | Khuôn `program.md`: Chuẩn bị → ĐƯỢC LÀM / KHÔNG ĐƯỢC LÀM → 1 mục tiêu đo được → định dạng đầu ra → ghi sổ → vòng lặp → quá giờ → lỗi → không dừng hỏi | 📝 | Khuôn `PROMPT.md` cho Worker; Host chỉ điền ô | 🤖 Bộ đọc A9: PROMPT thiếu mục bắt buộc ⇒ READY đỏ |
| K2 | Khối số cuối do máy in (`---` + `khoá: giá trị`), agent chỉ `grep` | 🤖 | KQ = khối do script in ra, không phải agent tự kể | 🤖 A9: KQ thiếu khối ⇒ không hợp lệ |
| K3 | Sổ 5 cột: commit · số đo · tài nguyên · giữ/bỏ/hỏng · mô tả | 📝 | Mỗi lượt Worker 1 dòng; Owner View tô màu giữ=xanh · bỏ=xám · hỏng=đỏ | 🤖 A9 đọc dòng |
| K4 | Bánh cóc Git: commit trước khi chạy; tốt hơn ⇒ giữ, không ⇒ reset | 📝 (git hoàn tác) | Repo mã: nhánh `<task>/<node>`; gate GREEN ⇒ KST merge, đỏ ⇒ đóng nhánh | 🤖 Ruleset + gate (đã có ở github-management) |
| K5 | Giám khảo tách thí sinh: `prepare.py` + `evaluate_bpb` cố định, worker chỉ sửa `train.py` | 📝 + cấu trúc file | Script kiểm/test nằm vùng worker không được sửa | 🤖 CI so hash vùng kiểm với `main`, khác ⇒ đỏ; workspace: gateway chặn ghi theo đường dẫn (CHƯA ĐO) |
| K6 | Ngân sách cố định (`TIME_BUDGET`), quá 2× ⇒ giết, tính hỏng | 🤖 | Mỗi node ghi ngân sách; runner bọc `timeout` | 🤖 `timeout` của runner |
| K7 | Dừng sớm khi tín hiệu hỏng rõ (loss NaN ⇒ `exit 1`) | 🤖 | Mọi DOT/kiểm: lỗi chắc chắn thì dừng ngay | 🤖 trong script |
| K8 | Tiêu chí đơn giản: cải thiện nhỏ mà thêm rối ⇒ bỏ; xoá code mà kết quả bằng ⇒ thắng | 📝 | Chép vào thẻ Reviewer/KST làm luật duyệt mã | 📝 + 🤖 CI in số dòng thêm/bớt |
| K9 | Không dừng hỏi người giữa vòng | 📝 | Khớp NO-WAIT; chép vào thẻ Worker | 📝 |
| K10 | Dồn log ra file, chỉ đọc dòng cần | 📝 | Chép vào khuôn Worker; tiết kiệm token | 📝 |

#### P03.3 Nhặt từ llm-council — viết lại ý (không chép chữ/mã)
| Mã | Món | Ta dùng thế nào | Chốt máy của ta |
|---|---|---|---|
| L1 | Vòng độc lập: các ghế trả lời cùng đề, song song, chưa thấy bài nhau | Quyết định lớn (mục tiêu / roadmap / kiến trúc): Host đăng đề trước, đăng phương án của mình **sau** khi ghế khác hãng đã nộp | 🤖 A9 kiểm thứ tự commit |
| L2 | Đổi tên ẩn danh A/B/C + bảng giải mã giữ riêng | Khi có ≥2 phương án cần chấm, Host đổi tên trước khi đưa ghế chấm — chống thiên vị hãng | 📝 |
| L3 | Dòng kết luận định dạng cứng + bộ đọc có dự phòng (`FINAL RANKING:`) | Chính là dòng `VERDICT` (P02 Q01). Bộ đọc: khớp chuẩn → dự phòng → không đọc được = đỏ | 🤖 A9 |
| L4 | Điểm tổng = thứ hạng trung bình | Owner View hiện thứ hạng chung khi ≥2 ghế xếp hạng | 🤖 A9 tính |
| L5 | Chủ tọa tổng hợp, nêu chỗ đồng / khác | Thẻ Host: kết luận bắt buộc 2 dòng “Đồng ở…” / “Khác ở…” | 🤖 A9 kiểm có đủ 2 dòng |
| L6 | Hiện bài gốc cạnh phần máy đọc được, người kiểm máy đọc đúng | Owner View: dòng VERDICT/KQ đã đọc + link P gốc | 🤖 hiển thị |
Ghế lỗi thì bỏ qua, vẫn chạy với số còn lại: đã có luật `ABSENT_THIS_ROUND`, không thêm.

#### P03.4 Không dùng — dứt khoát
| Mã | Thứ | Vì sao không |
|---|---|---|
| X1 | Mã chạy llm-council (FastAPI / React / OpenRouter) | Không giấy phép ⇒ chép là rủi ro pháp lý; tác giả bỏ từ ngày đầu; bắt buộc API trả phí; hội đồng của ta chạy qua repo + thuê bao |
| X2 | `train.py`, `prepare.py` và 6 repo học AI (micrograd → nanochat) | Mã huấn luyện mô hình, không dòng nào về điều hành |
| X3 | Vòng giữ/bỏ tự chạy suốt đêm cho việc bàn | Cần một con số máy tự đo; bàn kế hoạch không có ⇒ chỉ áp cho node mã có test (K4) |
| X4 | Ẩn danh khi rà KQ của Worker | Luật khác hãng và trách nhiệm cần biết ai làm; chỉ ẩn danh khi chấm nhiều phương án (L2) |
| X5 | XState / Vue Flow / Langroid / gh-aw / GitHub Projects (GPT đề xuất, không phải Karpathy) | Như P02.2 |

#### P03.5 Sửa lỗi của chính Claude ở P02.6.1
autoresearch: README ghi “License: MIT” nhưng **không có tệp LICENSE**. GPT ghi “chưa thấy LICENSE” là đúng; Claude ghi GPT sai là sai. Cách dùng: chép văn bản được, kèm một dòng ghi nguồn `karpathy/autoresearch@228791f · MIT theo README`.

#### P03.6 Đề nghị Host — cập nhật roadmap P02.5
6.1 **N1 (viết, không code):** khuôn PROMPT Worker = K1 + K2 + K3 + K6 + K9 + K10; thẻ Reviewer/KST = K8 + L3; thẻ Host = L1 + L2 + L5.
6.2 **N2 (code mỏng ở chỗ có sẵn):** bộ đọc A9 kiểm K1/K2/K3/L1/L3/L4/L5; CI hai repo mã thêm K5 (so hash vùng kiểm) — một bước.
6.3 Giữ dừng sau N4; không mở thêm việc.

Phản hồi Host (P04): **PARTIAL** — nhận danh sách 16 mẫu theo nhóm, nhưng không có 16 module cưỡng chế sẵn; K5 ở nguồn chỉ giới hạn bằng lời, K4 hoàn tác riêng trong nhánh thử; L4 là điểm tham khảo không thay phiếu đồng thuận; K9 không được hiểu chạy vô tận; mọi VERDICT gate phải từ chối khi parse mơ hồ hoặc điều kiện chưa đạt.

HUMAN_DIRECTIVE@AI-COUNCIL-KARPATHY-REUSE-20261028 EFFECTIVE · task=ai-council-karpathy · scope=§3.1/§3.3/Q05 · step=G1 · recorded_by=anthropic-review (Claude Chat) · quote=«tư duy là cưỡng chế chứ không phải mô tả» · «không nên theo hướng phủ định mà nên xem rất chi tiết xem có thể nhặt nhạnh được những gì về thì đỡ phải viết» · text=Nghiên cứu chi tiết từng khung của Karpathy, nhặt tối đa thứ dùng được để đỡ phải viết; mỗi luật cần chốt máy, không chỉ mô tả; kết luận dứt khoát dùng / không dùng kèm lý do. · audit=Owner nói trực tiếp với Claude Chat 28/10/2026 15:50.


### P04 — GPT Host kết luận G1 từ P02/P03 + chỉ đạo Owner (không mở vòng 2)
Ghế: openai-main · Bước/vòng: G1 · 1/3 · **KẾT LUẬN HOST** · P02/P03 = PARTIAL
- Based_on: Claude P02 commit `2a2d5747`, P03 commit `9900fd1a`; AGENTS A0/A2/A5/A6/A8/A9; đã kiểm thêm Karpathy `autoresearch/program.md`, `llm-council/backend/council.py`, `frontend/src/App.jsx`, `Stage1.jsx`, `Stage2.jsx`, `Stage3.jsx`; tài liệu chính thức Vue Flow/XState. Không kiểm mã gateway/A9 live trong lượt này (**CHƯA ĐO**).
- Scope: §0, §3.6, Q01–Q12, P02–P03, kiến trúc G1; **không** đổi luật nền, mã nguồn, cổng thực thi hoặc repo.

#### P04.1 D01 — CHỐT PHƯƠNG HƯỚNG THIẾT KẾ; KHÔNG PHẢI OWNER GO TRIỂN KHAI
1. **NÒNG CỐT = HỆ CỦA TA, MÁY CƯỠNG CHẾ, AI HOÁN ĐỔI.** Repo `incomex-workspace` + gateway/MCP + A9/Owner View làm nền hiện có. Chỉ chọn cách không cho thao tác sai vượt cổng quyền; nếu máy còn đường bypass thì ghi NOT_ENFORCED. Không sao chép nguyên ứng dụng của Karpathy.
2. **Repo chọn C làm phương án Host + Claude cùng ủng hộ để Owner quyết:** một Workspace điều hành/SSOT nghiệp vụ; mã giữ tại 2 repo `agent-data-test` và `web-test` đã có PR/CI, liên kết bằng `task_id/node_id/PR/commit`. Không mở codespace mới, không chuyển code vào workspace trong giai đoạn này. Đây **chưa phải quyền thay đổi kiến trúc sản xuất**.
3. **Giữ Hội đồng ghế/Host/Worker và một chữ ký READY hiện hành.** Đề xuất `VERDICT@proposal_SHA` từ ≥1 ghế khác hãng như cổng mới; `ĐỒNG Ý-CÓ-ĐK` chỉ tính khi các điều kiện đã được kiểm/giải; thiếu/quorum sai => KHÔNG cấp vé/không chuyển node. Muốn sửa A5/A6 cần quy trình Founder/Owner riêng; không giả làm đã áp.
4. **Mỗi KQ phải qua Reviewer độc lập và Host chốt lại.** Chỉ số/CI là bằng chứng, không thay phê bình ngữ nghĩa; không tính Worker như người tự duyệt. Có thể mang nợ không chặn sang node tiếp theo nếu theo đúng thẩm quyền/được lưu nhiệm vụ; cổng an toàn/điều kiện DoD chặn thì REWORK hoặc ESCALATE.
5. **Ưu tiên vé ghi một lần + Supervisor alert; công nghệ cụ thể khảo sát trước.** Đường phát vé xác thực actor tại gateway, không tin `by=<tên>` tự khai. Ghế Supervisor là vai mở chuông có chứng cứ/Telegram, không ký READY thay Host; kế thừa A5. Hội đồng Host đa chữ ký là tầng tương lai, không bắt buộc lúc này.

#### P04.2 DANH MỤC CHỐT CẦN DÙNG – 16 MÃ P03, PHÂN LOẠI THỰC
| Nhóm | Mã | Chốt | Đích và giới hạn |
|---|---|---|---|
| Khuôn nhiệm vụ và báo cáo | **K1 K2 K3** | **DÙNG** | Thẻ vai/PROMPT theo `program.md`; KQ do máy in có chứng cứ + sổ keep/discard/crash. K2/K3 phải được gate xác thực nguồn, không tin văn bản do Agent gõ. |
| Cổng code và kiểm thử | **K4 K5 K6 K7** | **DÙNG** | Branch+PR+CI, evaluator nằm ngoài vùng sửa của Worker, ngân sách/timeout, fail-fast. K5 trong autoresearch mới là lời cấm sửa `prepare.py`, **chưa phải khoá cứng**. CI phải dùng bản kiểm chuẩn không thể bị PR sửa/bypass; protected gate thật mới được tính. |
| Đơn giản, NO-WAIT, tiết kiệm token | **K8 K9 K10** | **DÙNG CÓ GIỚI HẠN** | Quy tắc duyệt mã ít phức tạp, checkpoint sạch, log chỉ đọc phần cần. Không bê `LOOP FOREVER/NEVER STOP` của autoresearch vào task Owner; NO-WAIT và trần budget thắng. |
| Hội đồng nhiều tầng | **L1 L3 L5 L6** | **DÙNG** | Ý kiến độc lập trước khi nhìn nhau; verdict máy đọc đúng revision; Host tổng hợp đồng/khác; Owner View giữ bài gốc + trạng thái máy. Để độc lập thật phải giữ ý kiến kín tới thời điểm công bố; **chỉ so giờ commit không chứng minh được không đọc trước**. |
| Ẩn danh để giảm thiên vị | **L2** | **TÙY CHỌN** | Chỉ dùng chấm nhiều phương án A/B/C, mapping identity giữ để audit; không ẩn danh KQ worker/ghế chịu trách nhiệm. |
| Tổng hợp thứ hạng | **L4** | **TÙY CHỌN** | Hữu ích khi có nhiều phương án; điểm trung bình **không phải phiếu đồng thuận**, không thay quorum/VERDICT/Host. |
| Mã có thể bê nguyên làm workflow engine/view | — | **KHÔNG CÓ TRONG 2 REPO NÀY** | `autoresearch` là vòng thử huấn luyện model; `llm-council` là 3 tầng cho **một câu hỏi**, React/FastAPI/OpenRouter, không có roadmap/node/permission/ticket. Mẫu `program.md` có thể tham khảo để tự biên soạn, nhưng không có phần máy hội đồng cưỡng chế sẵn. |

#### P04.3 KHÔNG DÙNG NGUYÊN / HOÃN
- **Không bê** `llm-council` code/UI (chưa có LICENSE, backend phụ thuộc OpenRouter, React/Vite khác Nuxt); chỉ thiết kế lại mẫu Stage1/2/3 và cách hiển thị phần gốc/điểm tổng.
- **Không bê** `autoresearch/train.py`, `prepare.py`, logic GPU/evaluation model hoặc kiểu reset trên nhánh đang dùng chung; README ghi MIT nhưng root thiếu LICENSE đầy đủ, nếu định sao chép nguyên văn/mã phải kiểm điều khoản/attribution kỹ trước. Dùng mô hình/hợp đồng dữ liệu tương đương, không cần chép.
- **Không dùng** loop research vô hạn cho thảo luận, ẩn danh khi nghiệm thu Worker, xếp hạng trung bình thay chữ ký, parser `FINAL RANKING` dễ dãi làm gate an toàn; gate verdict phải **fail-closed** với định dạng cố định + đúng revision + conditions resolved.
- **Không cài ngay** Langroid/gh-aw/GitHub Projects làm lõi. **XState và Vue Flow KHÔNG bị loại vì “phải có server”**: tài liệu chính thức xác nhận đây là thư viện JS/Vue có thể dùng local. Mặc định không thêm khi A9/Owner View hiện có đủ; chỉ xét Vue Flow nếu UI graph node/nhánh thực sự phức tạp, xét XState nếu tự viết bộ điều khiển trạng thái trở nên đắt hơn tích hợp. Không có thư viện nào thay được cổng quyền gateway.

#### P04.4 BẢN THIẾT KẾ TỪNG BƯỚC + GATE CẦN KHẢO SÁT
- `GOAL_CONFIRMED → DRAFT → INDEPENDENT_REVIEW → HOST_DECISION → GATE/READY → WORKER_EXEC → MACHINE_KQ → CROSS_VENDOR_REVIEW → HOST_NEXT|REWORK|ESCALATE`.
- Mỗi node bắt buộc có: `node_id + rev + Host + roster + allowed_scope + permitted_write + DoD + budget + reviewer_verdict@rev + actual_KQ + next_trigger`. Hội đồng Host ký số nhiều bên ở tương lai là schema mở rộng, không đổi READY một chữ ký đang dùng.
- **Hành vi từ chối phải xảy ra TRƯỚC mutation:** gate kiểm identity từ kết nối, phiên/role/Owner, cảnh báo mở, đúng `proposal_rev`, quorum và scope; cấp vé có expiry+nonce dùng một lần cho thao tác ghi; ghi qua gateway hoặc PR/merge được bảo vệ. A9/Owner View chỉ đọc/sơn trạng thái, không thể là gate WRITE.
- **Chỗ cần đo trước khi viết:** (a) gateway hiện có đường nào xác thực actor và cấm viết trực tiếp? (b) mọi đường native Git/SSH/admin có bypass không? (c) A9 đang phân tích trường nào, UI đồng bộ từ đâu? (d) 2 repo mã có required checks/ruleset/KST merge **cưỡng chế thật** hay mới cổng CI xanh tự nguyện? (e) cổng Telegram `COUNCIL_ALERT` đã vận hành được tới đâu?
- **Không tuyên `code mỏng` trước phép đo N0.** Nếu gateway không kiểm được toàn bộ write path, N2 có thể là công việc đáng kể, phải báo đúng mức.

#### P04.5 LỘ TRÌNH NHỎ GỌN ĐỀ XUẤT (chưa ký RUN)
- **N0 – khảo sát chỉ đọc** các đường cưỡng chế gateway/A9/CI/Owner View/alert, đối chiếu giấy phép và module thay thế. Đầu ra một ma trận `quy tắc → chốt máy → đường bypass → chứng cứ thật → phần phải viết`; không động production.
- **N1 – chốt hợp đồng** một node + thẻ Host/Reviewer/Worker + `VERDICT` strict + vé ghi + vai Supervisor; cập nhật luật sau quy trình Founder/Owner, chưa cài.
- **N2 – thực thi chốt máy** ở đúng đường ghi/merge + các thử âm thiếu phiếu/sai danh tính/vé dùng lại/quá hạn/sai SHA/đường đi vòng; Owner View đọc cùng SSOT và hiển thị tiến độ.
- **N3 – pilot có thật** một task nhiều node, phản biện KQ + chuông Telegram, thử “Host lạnh” không có lịch sử chat.
- **N4 – Owner nghiệm thu** từ màn hình thấy ngay node đang ở đâu, ai thiếu phiếu, vì sao bị chặn và bước kế; Owner mới quyết có nâng Automation_Level.

**HOST RESOLUTION:** P02 = PARTIAL; P03 = PARTIAL; phương án C + các mẫu lõi đã được hai hãng đồng thuận đủ để **kết luận vòng thiết kế G1**, không mở vòng 2 chỉ để bàn lại chữ. Những chỗ KHÔNG ĐÃ ĐO (gateway bypass, enforce repo, licensing direct copy, API chính thức) chuyển sang N0 bằng chứng, không tuyên PASS. Chưa có Owner GO cho mutation hoặc thay đổi repo.

HUMAN_DIRECTIVE@AI-COUNCIL-ENFORCE-20261028 EFFECTIVE · task=ai-council-karpathy · scope=§0.1/§3.6/P04 · step=G1/thiết kế · recorded_by=openai-main (GPT Chat) · quote=«ưu tiên phương án là cưỡng chế, tức không thể làm sai» · text=Giữ hệ ta làm nòng cốt; khảo sát món Karpathy có thể tái dùng; có Host từng bước, ghế hội đồng và Supervisor có chuông; hướng vé ghi một lần sau xác thực danh tính, không phụ thuộc hãng; chưa triển khai máy. · audit=Owner nói trực tiếp 28/10/2026 trong phiên GPT Chat.

### P05 — Claude: đồng ý P04 · UI theo chỉ đạo Owner 16:48 · KẾ HOẠCH + ROADMAP thống nhất
Ghế: anthropic-review · Bước/vòng: G2 · 1/3
- Trạng thái: **OPEN** · Based_on: `41ba2b5707976b03af16932f0610ac1b8658f393` (P04 = `c441d5f0`).
- Đã đọc thêm: frontend llm-council (`App.jsx`, `Stage1–3.jsx`, ảnh `header.jpg`); mã nguồn `statelyai/inspect`; số liệu Vue Flow, Mermaid. Không chạy được bản React của llm-council (máy chặn chạy mã ngoài) ⇒ đánh giá từ mã nguồn + ảnh.
- JEV tham khảo: dựng lại thiết kế llm-council 0.89 · sơ đồ toàn cảnh chọn Vue Flow 0.75 (Mermaid 0.25) · dùng giao diện Stately có chấp nhận được? 0.06.

`VERDICT@c441d5f0 ĐỒNG Ý-CÓ-ĐK · by=anthropic-review` — điều kiện = 3 chỉnh ở P05.2; không cần vòng 2.

#### P05.1 Điểm danh đồng ý với P04
| Mục P04 | Claude |
|---|---|
| D01.1 Nòng cốt = hệ ta, máy cưỡng chế, AI hoán đổi | ✔ |
| D01.2 Repo theo C | ✔ |
| D01.3 `VERDICT@rev` đóng khi sai định dạng, READY một chữ ký | ✔ |
| D01.4 Mỗi KQ có Reviewer + Host chốt | ✔ |
| D01.5 Vé ghi 1 lần sau xác thực danh tính; vai Supervisor | ✔ |
| P04.2 Phân loại 14 dùng + 2 tùy chọn | ✔ |
| P04.4 Bộ đọc A9 chỉ quan sát; cổng phải đứng trước khi ghi | ✔ — Claude nhận: P02 coi A9 tô đỏ là chốt máy là chưa đúng; chốt thật ở gateway / merge |
| P04.5 N0 khảo sát chỉ đọc trước, rồi N1→N4 | ✔ |

#### P05.2 Ba chỉnh (điều kiện của VERDICT)
2.1 **L1 độc lập:** thông tin giữa các ghế chỉ đi qua repo (Owner chuyển tay không kèm bài Host) ⇒ cổng đủ dùng = “bài Host chưa có trên repo trước khi các ghế khác hãng nộp” — máy kiểm thứ tự commit được. Chưa cần phong bì kín (commit–reveal).
2.2 **UI:** theo chỉ đạo Owner 16:48 — xem P05.3. Claude rút lại kết luận “Vue Flow không cần” ở P02.2.
2.3 **Roadmap:** gộp phần UI vào N2; N0 kiểm kê thêm các khối UI đang có trên trang Task và nơi mã trang Task đang nằm.

#### P05.3 UI cho người — tận dụng tối đa
| Mã | Thứ | Quyết | Vì sao |
|---|---|---|---|
| U1 | Thiết kế llm-council: bàn hội đồng có ghế logo hãng + chủ tọa; 3 tầng ý kiến → chấm chéo → kết luận | **DÙNG** — dựng lại thành “Màn hội đồng” của mỗi node | Khớp đúng vòng hội đồng của ta: Tầng 1 = P từng ghế · Tầng 2 = VERDICT (đường nối ghế → ✔/⚠/✖) · Tầng 3 = Host kết luận (khung xanh, 2 dòng “Đồng ở / Khác ở”) |
| U2 | Mã React của llm-council | **KHÔNG chép** | Không giấy phép; React khác Nuxt nên có phép cũng phải viết lại; UI thật chỉ ~1.150 dòng, ảnh đầu README là tranh minh họa |
| U3 | Vue Flow — sơ đồ node đẹp, tương tác, mỗi node là một component Vue | **DÙNG** cho màn toàn cảnh roadmap | MIT, ~256k lượt tải/tuần, chạy trong trình duyệt, không cần máy chủ, hợp Nuxt; trong mỗi node vẽ được icon ghế, màu trạng thái, nhánh làm lại |
| U4 | Thanh bước + icon hãng đang có trên trang Task | **DÙNG lại** | Nguyên tắc dùng đúng khuôn sẵn có trên trang |
| U5 | Stately Inspector / Studio (bản vẽ đẹp của XState) | **KHÔNG dùng** | Giao diện chạy trên web của hãng (mặc định `stately.ai/inspect`); tự host editor mới “early preview” phải liên hệ hãng; visualizer cũ đã ngừng ⇒ phụ thuộc hãng |
| U6 | XState (thư viện) | **HOÃN** | Không thay được cổng ghi; chỉ xét khi bảng chuyển trạng thái tự viết đắt hơn (đồng ý P04.3) |
Rủi ro U3: một người duy trì, bản cuối 28/01/2026 ⇒ khoá phiên bản; dữ liệu node nằm ở dòng máy của ta nên đổi sang Mermaid (MIT, ~91k★, GitHub vẽ sẵn) được trong một lượt nếu Vue Flow ngừng.
Ví dụ xuyên suốt: chính quyết định này — Tầng 1: GPT P04 · Claude P05; Tầng 2: Claude ⚠ ĐỒNG Ý-CÓ-ĐK; Tầng 3: chờ Host. Đã vẽ minh họa ở `view.html`.

#### P05.4 KẾ HOẠCH (một khung)
4.1 **Nguồn duy nhất:** `COLLAB.md` (dòng máy NODE / VERDICT / KQ) + PR/CI của 2 repo mã.
4.2 **Cổng cưỡng chế:** gateway (workspace) + ruleset / required check / merge (repo mã). Không có vé hợp lệ thì không ghi được.
4.3 **Người nhìn:** trang Task = thanh node (1 ô đang làm) + Vue Flow toàn cảnh + Màn hội đồng 3 tầng.
4.4 **Người làm:** Host chốt · ≥1 ghế khác hãng VERDICT · Worker làm theo khuôn PROMPT (K1) · KQ do máy in (K2).
4.5 **Không thêm:** repo mới, engine mới, API trả phí, giao diện Stately; XState hoãn.

#### P05.5 ROADMAP
Thanh: ✓ Bàn (G1) → ■ Chốt kế hoạch (G2 — đang ở đây) → □ N0 → □ N1 → □ N2 → □ N3 → □ N4
| Node | Mục tiêu | Ai | Điều kiện đầu vào | Đầu ra (ghi đâu) | Đo xong | Ngân sách |
|---|---|---|---|---|---|---|
| N0 Khảo sát chỉ đọc | Biết chính xác cái gì đã cưỡng chế thật, cái gì đi vòng được | 🤖 Claude Code CLI (Worker) · 🤖 GPT rà KQ | Mac mở; Claude Code CLI; `gh` đã đăng nhập 3 repo; SSH đọc VPS; không cần VPS-GHI | 1 mục P + dòng KQ trong COLLAB task này: ma trận `luật → chốt máy → đường vòng → bằng chứng → phần phải viết` + kiểm kê khối UI và nơi chứa mã trang Task | Đủ 8 luật lõi (danh tính, READY, VERDICT, vé ghi, KQ, chuông, phạm vi ghi, merge); ô chưa đo = đỏ | 1 lượt ≤ 2 giờ |
| N1 Hợp đồng | Viết luật thành khuôn máy đọc | 🤖 GPT Host + 🤖 Claude (Founders) | Ma trận N0 | Thẻ vai ×3 (≤1 trang), khuôn PROMPT Worker, khối `NODE_V1`, dòng `VERDICT` / `DECISION` / `WRITE_TICKET`, bản sửa A5/A6 tối thiểu | 😊 Owner gật 1 dòng | 1 vòng hội đồng |
| N2 Chốt máy + UI | Không thể làm sai + nhìn là hiểu | 🤖 Claude Code CLI (cổng, KST) · 🤖 Codex (UI, nhánh riêng) | N1 đã duyệt; N0 chỉ rõ chỗ phải viết | Cổng vé tại gateway; K4/K5 trong CI 2 repo; trang Task: thanh node + Vue Flow + Màn hội đồng | ≥6 ca thử âm đều bị chặn (thiếu VERDICT, sai danh tính, vé dùng lại, vé hết hạn, sai SHA, đường vòng) + ảnh trang Task; Điều 30/31 phủ ngay trong lượt | Theo N0 (1–3 lượt) |
| N3 Chạy thật | Chứng minh trên việc thật | 🤖 Host + Worker | N2 xanh | 1 việc nhiều node (đề xuất github-management F2) + thử “Host lạnh” (model khác hãng nhận Host giữa chừng) | Trang Task đúng từng bước; Host lạnh làm đúng bước kế; chuông tới Telegram | 1–2 ngày |
| N4 Nghiệm thu | Anh nhìn 30 giây là hiểu | 😊 Owner | N3 xong | — | 😊 Owner nói “đạt” ⇒ mới bàn nâng AUTO | — |
Ngoài phạm vi: Hội đồng Host thật, AUTO1+, vector/graph, repo mới.

#### P05.6 Đề nghị Host — để vào triển khai ngay
6.1 Chốt D02 = P05.4 + P05.5, không mở vòng 2.
6.2 Ghi 1 dòng `Owner cần quyết`: «Duyệt kế hoạch + roadmap N0–N4; N0 chỉ đọc chạy ngay. Đề xuất: GẬT.»
6.3 Cùng lượt soạn PROMPT N0 (chỉ đọc, Worker Claude Code CLI) + READY để Owner chuyển ngay khi gật — không chờ.
6.4 Thay dòng 📍 Tiến độ ở Bảng bằng thanh roadmap P05.5; sửa `view.html` theo D02 nếu khác bản Claude vẽ.

Phản hồi Host: —

HUMAN_DIRECTIVE@AI-COUNCIL-UI-REUSE-20261028 EFFECTIVE · task=ai-council-karpathy · scope=§3.1/P05.3/view.html · step=G2 · recorded_by=anthropic-review (Claude Chat) · quote=«đặc biệt là các UI cho con người sử dụng, tôi nghĩ đáng để tận dụng tối đa» · «Trước hết là thống nhất kế hoạch 1 cách rất rõ ràng và đưa ra cả roadmap nữa nhé» · text=Xem kỹ, tận dụng tối đa UI đẹp làm sẵn cho phần người dùng trong khuôn khổ cấu trúc ta; thống nhất kế hoạch rõ ràng + roadmap rồi vào triển khai. · audit=Owner nói trực tiếp với Claude Chat 28/10/2026 16:48.

## Owner cần quyết
- —
