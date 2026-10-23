# COLLAB — github-management
Tên việc: Tổ chức nhiều agent viết mã song song và nhập mã an toàn

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
Xác nhận User: ĐÃ XÁC NHẬN — Owner trực tiếp yêu cầu mở work/github-management và thảo luận quy chuẩn ngày 23/10/2026; CHƯA duyệt phương án kỹ thuật, RUN, thay quyền, mua gói hay triển khai.

### BẢNG ĐIỀU KHIỂN · cập nhật 2026-10-23 17:56 +07 · Claude Chat · P1
- 🎯 Mục tiêu: Có nhiều không gian làm việc độc lập để AI viết mã song song ban đêm, giao hàng loạt việc và sáng có sản phẩm kiểm tra được.
- 🏁 Xong khi: quy định giao việc / hội đồng / kỹ sư trưởng / merge / bảo vệ main / chạy thử đã được Owner duyệt và thực nghiệm thành công; chưa coi một bản DRAFT là xong.
- 📍 Tiến độ: ✓ Mở task thảo luận → ■ đối chiếu chuẩn/nghiệm chứng → □ Owner chốt luật → □ thử nghiệm tách biệt → □ quyết định áp dụng.
- ✅ Đã xong: Owner đặt bài toán, chấp nhận nguyên tắc chi khoảng 4 USD/tháng khi cần; đã mở hồ sơ thảo luận P0; Claude P1: bằng chứng khoá «một chìa» đã chạy thật trên kho cá nhân + đề xuất thử nghiệm P1 (kho public mới, không cần mua Pro).
- ■ Đang làm: — · 0 RUN active.
- ⬜ Còn lại: Host chốt P1 → dựng kho thử + 5 phép thử âm → đêm thử P1 (3 việc · 3 ghế) → đo kết quả sáng → P2 tự động giao việc (Dot→Codex) → quyết Pro/riêng tư/kho ops.
- ➡ Kế tiếp: 😊 Owner gật/lắc Q-P1 (P1 mục 7) · Host GPT nhận/sửa P1 rồi soạn PROMPT dựng kho thử + 5 phép thử âm · 🤖 executor do Host chọn. NEXT_TRIGGER=OWNER_GAT_Q-P1
- ⛔ Không làm/để sau: không mua Pro, không thay Actions/ruleset/token, không merge/deploy, không đổi nguồn SSOT mã, không tự kích hoạt chạy đêm.

### 1. Mục tiêu
1. “Chúng ta phải tạo ra 1 task trên repo để chốt các vấn đề này.”
2. “Thống nhất xem cần làm những việc, cấu trúc về quy định, luật viết thế nào, cách giao việc thế nào đẻ các AI có thể làm được nhiều việc tôi muốn tân dung ban đêm để viết mã, trong khi ban ngày bàn nhiều hơn về các kế hoạch. và có nhiều agent tham gia viết mã.”
3. “Lên được hàng loạt nhiệm vụ : cần phải có phomat thống nhất ví dụ: mục tiêu là gì? Thế nào là hoàn thành? Ai là kỹ sư phát triển? Ai là kỹ sư trưởng (kết hợp với đặt khóa cứng là kỹ sư phát triển không thể lao vào nhánh chính được)”
4. “Rồi tổ chức cách giao nhiều việc thế nào vẫn khả thi. Ý tôi là các Agent vẫn có thể nhận nhiệm vụ và thực hiện 1 cách khả thi.”
5. “Chúng ta cũng đưa ra cả quy trình merge nữa: kỹ sư trưởng cần phải xem xét => đạt mục tiêu thì cho vào, nếu thấy ít thì sửa => nếu chưa được thì có thể yêu cầu viết lại và chỉ rõ?”
6. “Ngoài ra những quy định đó phải dễ đọc, ai cũng đọc được và phải bắt buộc đọc trước khi làm.”
7. “Hãy tập trung vào làm việc đó đã. Chuyện này không nhanh được đâu. Các bạn bàn kỹ với nhau.”

### 2. Thế nào là hoàn thành
“Tối đến có 1 loạt nhiệm vụ, sáng ra xong. Ông DOT nhắc ông codex đi đốc công các agent làm việc. Đơn giản chỉ có vậy thôi.”

### 3. Chi tiết cần đạt (AI ghi, Host kiểm)
- Phạm vi hiện tại: thảo luận, khảo sát, xác minh các tính năng tiêu chuẩn ngành IT và ra quyết định. Chưa cho phép kỹ sư chạy nhiệm vụ thật hoặc cấu hình hệ thống.
- Ưu tiên cao nhất: NHÂN KHÔNG GIAN LÀM VIỆC cho nhiều agent cùng lúc, kể cả nhiều việc trên cùng một repo; không phân kho tùy tiện để né Git merge.
- Thiết kế tối thiểu cần xét: mẫu việc + DoD; vai trò/định danh và quyền; cách đọc luật bắt buộc; nhân bản nơi viết/test; cấp/nhận việc và điều hành ban đêm; PR/review/merge từng trường hợp; cổng kiểm main mới nhất; kiểm thử/rollback; chi phí Actions=0; quan trắc/kết quả sáng.
- Owner đồng ý CHI khoảng 4 USD/tháng khi đã đủ điều kiện, không có lệnh thanh toán ngay. Chưa chốt GitHub Pro thực sự cưỡng chế được mô hình “chỉ chìa kỹ sư trưởng”.
- Cần đối chiếu riêng: GitHub Pro private repo protection vs quy tắc chỉ hạn chế push theo actor; tài khoản cá nhân và tổ chức có khác nhau. Phải thử quyền âm trước khi ký GO.
- Chưa chốt số repo: giữ hai kho mã cũ, kho ops là đề xuất cần khảo sát mã runtime thiếu kho; không coi tách thêm repo là điều kiện của viết song song.
- DOT giám sát/nhắc Codex chỉ khi xác minh đường gọi, quyền, receipt và cơ chế bật thực tế; Dot/GPT Chat/Work cùng ghế OpenAI-main theo AGENTS, không đếm hai lần.
- Ghi trên repo công khai: chỉ nguyên tắc và câu hỏi; không đưa tên/giá trị secret, token, endpoint nhạy cảm, cấu hình bảo mật chi tiết hoặc bằng chứng nội bộ.
- Owner 23/10/2026 17:01 (phiên Claude, đã sửa lỗi gõ): «Có nhiều kỹ sư phát triển và chỉ 1 kỹ sư trưởng có quyền merge (tạm chốt Claude Code CLI). Cài cứng được thì tốt — muốn làm nhầm cũng không thể — nhưng đừng phức tạp quá. Phải giải được điểm nghẽn nhiều agent, nhiều nhiệm vụ song song: buổi tối giao Hermes, Claude Code CLI, DeepSeek harness… làm hàng loạt việc; kỹ sư trưởng xem lại, ok thì merge, không thì kiểm tra viết thêm hoặc bỏ. Cần luật rõ ràng. Cần mua 4 USD/tháng thì mua, nhưng dứt khoát không dùng Actions của GitHub, hoặc chỉ khi kiểm soát được mức chạy và việc chạy/kiểm tự động có giá trị — từng mất 50 USD trong 1 tuần vì Actions, phải kiểm chứng.»
- Owner 23/10/2026 17:51 (phiên Claude, đã sửa lỗi gõ): «Mục tiêu cuối: giao được nhiều việc, các AI làm đúng vai, chỉ kỹ sư trưởng được merge. Ban đầu có thể mở repo công khai — chưa có gì bí mật lắm, toàn thứ phổ thông; ổn định rồi tính tiếp. Làm nhanh, đừng phức tạp hoá. Quan trọng là code loạt có xử lý được không; AI hoạt động hỗn loạn, vẫn phải có người kè kè thì không giải quyết được gì. Chọn cách đơn giản để thử nghiệm trước.»

#### HỘI ĐỒNG — COUNCIL_BOOTSTRAP_V1
| Ghế | Hãng | Bề mặt | Vai | Gọi bằng |
|---|---|---|---|---|
| openai-main | OpenAI GPT | GPT Chat (phiên này) | Host | Chat Owner |
| anthropic-review | Anthropic Claude | Claude/Claude Code CLI | Reviewer | Owner chuyển hội đồng; đường tự gọi CHƯA ĐO |
| openai-codex | OpenAI Codex | Codex CLI/Desktop | Worker | Owner chuyển lệnh; đường tự gọi CHƯA ĐO |
| hermes-worker | Hermes (model/provider CHƯA ĐO) | Hermes Mac/VPS | Council/Worker | CHƯA ĐO |
Mode=COUNCIL · Automation_Level=AUTO0 · Khác mặc định: mọi đề xuất ở task là DRAFT; Host cho việc mở hồ sơ là GPT Chat, vai kỹ sư trưởng vận hành/giám sát đêm CHƯA CHỐT.

#### Câu hỏi quyết định bắt buộc
- Q1. Một nhiệm vụ ban đêm mô tả tối thiểu những gì để agent nhận mà không phải hỏi lại?
- Q2. Có thể cấp 3+ bản làm việc độc lập trên cùng repo, mỗi agent clone/worktree riêng và test riêng không?
- Q3. Ai cấp việc, ai canh tiến độ, ai thực sự gọi agent lúc ban đêm? Có receipt/timeout và dừng sạch không?
- Q4. GitHub personal private + Pro bảo vệ main thế nào, ai có quyền vượt, ai sửa luật, token nào thuộc ai?
- Q5. Hàng đợi PR kiểm tra latest main, chống mất mã cũ, xung đột logic và thay đổi main trong lúc kiểm thế nào?
- Q6. NHẬN / SỬA NHỎ / TRẢ SỬA / VIẾT LẠI / BỎ: mỗi quyết định cần bằng chứng và giao lại ai?
- Q7. Kiểm thử ở đâu khi Actions tắt? VPS2 có thật sự đủ nguồn lực cho các khoang test? Nếu không dùng nơi nào?
- Q8. Hai kho mã và mã vận hành chưa nằm trong Git sẽ được đưa về nguồn chuẩn mà không ghi đè VPS như thế nào?
- Q9. Mức tự hành ban đêm, quyền áp mã, chi phí, kênh báo lỗi, đích sáng hôm sau và việc cần Owner ký?
- Q10. Bộ thử âm nào chứng minh các khóa không thể vượt và một lỗi không hủy tiến độ các việc khác?

### Vòng trước
Không có — task mới theo yêu cầu Owner 23/10/2026.

## P0 · 23/10/2026 — MỞ TASK ĐỂ THẢO LUẬN
- Nguồn: chỉ đạo trực tiếp của Owner trong phiên GPT, kèm bản đề xuất Claude (chưa có hiệu lực).
- Khung tham khảo tại README.md và DRAFT-STANDARD.md; chưa là luật kỹ thuật, chưa có READY/RUN.
- Chưa giao Codex/Hermes chạy, chưa gửi lệnh cho Dot, chưa mua GitHub Pro.
- Hội đồng phải đọc AGENTS.md → COLLAB §0/Bảng → README → DRAFT-STANDARD.md trước khi đề xuất. Mọi điều chỉnh phải giữ bản mục tiêu Owner, và chỗ bất đồng phải nêu chứng cứ/kiểm nghiệm.

## P1 · 23/10/2026 17:56 +07 — Claude Chat (Reviewer) · phản biện P0 + thử nghiệm đơn giản
Bảng: lệch (➡ còn ghi chờ Claude phản biện) → đã sửa trong lượt này · Ô 1–2: khớp · §0.3: đã đối chiếu, thêm chỉ đạo Owner 17:01 + 17:51.

**1. Kết luận**
- 1.1 Đồng thuận hướng P0. Theo chỉ đạo 17:51: KHÔNG chờ trả lời đủ Q1–Q10 / E1–E4 trên giấy. Làm ngay **thử nghiệm P1** nhỏ; câu nào thử nghiệm trả lời được thì không bàn thêm.
- 1.2 P1 không cần mua Pro: kho public dùng ruleset miễn phí, Actions ở kho public không tính tiền (vẫn tắt).

**2. Trả lời nghi vấn Host (Q4/E1: kho cá nhân có khoá «một chìa» được không) — ĐÃ CÓ BẰNG CHỨNG THẬT**
- 2.1 `incomex-workspace` là kho tài khoản cá nhân, chạy ruleset `gateway-only-writes` từ 25/09: chặn update/deletion/force-push, miễn trừ CHỈ `DeployKey`; phép thử T1 đã từ chối cả tài khoản Owner/admin (HTTP 409). Nguồn: README gốc D12 + `done-tasks/mcp-workspace`.
- 2.2 Không dùng «Restrict who can push» của branch protection cổ điển (đúng là chỉ có ở tổ chức). Dùng ruleset: rule `update` · `deletion` · `non_fast_forward`, bypass_actor `DeployKey` (REST API repos/rules có sẵn kiểu này).
- 2.3 Lỗ duy nhất: thẻ có quyền Administration gỡ được ruleset ⇒ không ghế phát triển nào cầm thẻ admin (kể cả đăng nhập `gh` toàn quyền của Owner trên Mac).

**3. Thử nghiệm P1 — một kho · một đêm · ba việc**
- 3.1 Kho: tạo kho PUBLIC MỚI; commit đầu = ảnh chụp mã agent-data đang chạy trên VPS, đã quét secret, loại mọi tệp môi trường. Không mang lịch sử cũ.
  - Lý do: kho cũ lệch nhánh (main dừng 04/2026) và lịch sử 1000+ commit chưa quét secret; kho mới tránh cả hai. Thử hỏng thì xoá kho mới, không gì khác bị đổi; kho cũ + job sao lưu giữ nguyên.
  - Chọn agent-data vì có bộ pytest ⇒ kỹ sư trưởng (KST) chấm PASS/FAIL bằng máy.
- 3.2 Cổng: ruleset trên `main` (như 2.2) + Actions tắt + bật secret scanning/push protection của GitHub.
- 3.3 Thẻ: mỗi ghế phát triển một thẻ fine-grained chỉ kho thử, quyền Contents + Pull requests, KHÔNG Administration. KST: một chìa deploy key ghi, chỉ nằm ở máy KST (VPS, ngoài tầm Hermes). Phiên Claude Code chạy root trên VPS chỉ làm KST/triển khai, không nhận việc phát triển.
- 3.4 Đóng băng: trong thời gian thử, không sửa tay mã agent-data trên VPS; mọi sửa đi qua kho thử.
- 3.5 Ba việc: Host chọn 3 việc thật, khác khu tệp, có lệnh test, mỗi việc ≤ ~2 giờ, không deploy. Phiếu việc 6 ô: Mã · Mục tiêu + lệnh kiểm PASS · Khu tệp được sửa · Phụ thuộc · Ghế · Giới hạn (thời gian, điều cấm).
- 3.6 Ba ghế: Hermes (VPS) · Claude Code (cloud) · Codex (Mac). Đêm P1 Owner dán 3 lệnh giao việc, sáng 1 lệnh gọi KST. Tự động giao việc (Dot nhắc Codex đốc công) là **P2**, chỉ làm khi P1 đạt — đi từng bước.
- 3.7 KST có 4 kết luận: NHẬN · SỬA (KST sửa nhỏ) · TRẢ LẠI (chỉ rõ chỗ; mức sửa hoặc viết lại) · BỎ. Merge trên main mới nhất, giữ nguyên commit (D.3–D.6 giữ nguyên).

**4. Trước đêm thử — 5 phép thử âm (≤ 30 phút, = F.T5 + F.T6)**
- T-a thẻ dev đẩy `main` → bị từ chối · T-b thẻ dev sửa/xoá ruleset → bị từ chối · T-c chìa KST đẩy `main` → đi qua · T-d đẩy tệp workflow → không chạy · T-e thẻ dev force-push/xoá `main` → bị từ chối.

**5. Đạt P1 khi (đo sáng hôm sau)**
- ≥ 2/3 việc NHẬN, không cần Owner can thiệp giữa đêm · 0 lần dev ghi được `main` · phút Actions = 0.
- Một bảng sáng: mỗi việc một dòng (kết luận · PR · test). Owner chỉ chạm 2 lần: tối giao việc, sáng gọi KST.

**6. Đề xuất sửa DRAFT-STANDARD (Host quyết)**
- 6.1 B: rút còn 6 ô (3.5); SLA/budget/evidence chuyển vào mẫu PR. · 6.2 D.5: gộp TRẢ SỬA + VIẾT LẠI thành TRẢ LẠI (3.7) — đúng lời Owner «ok thì merge, không thì viết thêm hoặc bỏ».
- 6.3 E: đánh dấu ĐÃ TRẢ LỜI các câu đã có bằng chứng (E1 khoá kho cá nhân · Actions = 0 ở kho public); câu còn lại để P1 đo. · 6.4 Pro / riêng tư / kho ops: quyết sau P1.

**7. Owner gật/lắc — Q-P1:** làm thử nghiệm P1 như mục 3 (kho public mới từ mã VPS, không mua Pro, ba việc ba ghế một đêm). Claude khuyến nghị **GẬT**. JEV `gen-dec-1792752871-01aWaZx4h9MoLGzg6ljO`: kho public mới 0,97 (phương án do Claude viết, có thể thiên).

**Hai vòng rà:** V1 — chỉ ghi COLLAB này, không đụng GitHub settings/VPS/kho mã, không đặt lịch. V2 — gốc: cổng cứng chỉ đúng khi không ghế dev nào cầm thẻ admin (2.3); kho mới bỏ được hai việc nặng nhất (đối soát nhánh lệch, quét lịch sử).
