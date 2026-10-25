# COLLAB — github-management
Tên việc: Tổ chức nhiều agent viết mã song song và nhập mã an toàn

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
Xác nhận User: ĐÃ XÁC NHẬN — Owner 25/10 15:18: ƯU TIÊN SỐ 1 là hệ thống chạy được — 2 repo có CI/CD với VPS, máy chạy (runner) đặt trên VPS (= GO DROOT56 cho đúng việc này, qua cổng của PROMPT). Nhiều agent song song làm SAU, trên 2 repo thật.

### BẢNG ĐIỀU KHIỂN · cập nhật 2026-10-25 16:30 +07 · Codex · P26 STARTED C1A
- 🎯 Mục tiêu: cài GitHub self-hosted runner trên VPS cho hai repo thật, chạy CI có test thật, rồi hoàn thiện CD và cho các agent lập trình song song.
- 🏁 Xong khi: C1A 2/2 CI run trên VPS PASS, nguồn SHA/log kiểm chứng, Guard/health sạch; C1B CD dev + rollback; C2 khóa main; C3 agent song song.
- 📍 Tiến độ: ✓ R0/R1 → ✓ GPT P23 C1A Codex → ✓ Claude P24 ACCEPT → ✓ GPT P25 READY → ■ Owner giao CODEX RUN C1A → □ KQ C1A → □ C1B → C2 → C3.
- ✅ Đã xong: PROMPT Codex C1A chốt, Claude P24 sửa 3 điểm tại commit 0ec01e30 và ký ACCEPT đúng last-touch; GPT Host đã đọc toàn bộ và ký READY cùng SHA. KHÔNG sửa lại PROMPT.
- ■ Đang làm: Codex STARTED GHM-C1A-VPS-RUNNER-20261025-01; S0 kiểm quyền/tài nguyên/cờ và bảo vệ, chưa mutation runner.
- ⬜ Còn lại: Owner chuyển đúng RUN_ID+PROMPT cho Codex; Codex tuân S0 cờ VPS-GHI/quyền, cài 2 runner, chạy CI thật 2 repo, KQ XONG/DỪNG; Host/Claude nghiệm thu kết quả.
- ➡ Kế tiếp: Codex qua S0, CAS VPS-GHI rồi cài runner và kiểm CI thật 2 repo; NEXT_TRIGGER=CODEX_C1A_KQ.
- ⛔ Không làm: không giao Claude chạy thay; không RUN PROMPT P22 cũ; không đụng main/deploy workflow cũ/restart app; chưa tự mở C1B/C2.
### 1. Mục tiêu
1. “Chúng ta phải tạo ra 1 task trên repo để chốt các vấn đề này.”
2. “Thống nhất xem cần làm những việc, cấu trúc về quy định, luật viết thế nào, cách giao việc thế nào đẻ các AI có thể làm được nhiều việc tôi muốn tân dung ban đêm để viết mã, trong khi ban ngày bàn nhiều hơn về các kế hoạch. và có nhiều agent tham gia viết mã.”
3. “Lên được hàng loạt nhiệm vụ : cần phải có phomat thống nhất ví dụ: mục tiêu là gì? Thế nào là hoàn thành? Ai là kỹ sư phát triển? Ai là kỹ sư trưởng (kết hợp với đặt khóa cứng là kỹ sư phát triển không thể lao vào nhánh chính được)”
4. “Rồi tổ chức cách giao nhiều việc thế nào vẫn khả thi. Ý tôi là các Agent vẫn có thể nhận nhiệm vụ và thực hiện 1 cách khả thi.”
5. “Chúng ta cũng đưa ra cả quy trình merge nữa: kỹ sư trưởng cần phải xem xét => đạt mục tiêu thì cho vào, nếu thấy ít thì sửa => nếu chưa được thì có thể yêu cầu viết lại và chỉ rõ?”
6. “Ngoài ra những quy định đó phải dễ đọc, ai cũng đọc được và phải bắt buộc đọc trước khi làm.”
7. “Hãy tập trung vào làm việc đó đã. Chuyện này không nhanh được đâu. Các bạn bàn kỹ với nhau.”
8. “Bạn viết thành kế hoạch và roadmap trên task, sau đó tôi cần cloud tham gia phản biện, đồng thuận rồi mới triển khai.” — 24/10/2026.
9. “Tôi muốn xác nhận là việc mua pro là bắt buộc ngay hay chỉ khi chúng ta đóng repo lại? Nếu mở repo thì có cần phải mua ngay không? Tôi muốn thử quy trình trước? Vấn đề là tất cả các Agent cần phải thao tác, cần phải có luật, phải thử nghiệm và chứng minh được là công việc có thể đẩy nhanh song song trước được không? Hay bắt buộc phải mua trước mới làm được?” — Owner 25/10/2026.

### 2. Thế nào là hoàn thành
“Tối đến có 1 loạt nhiệm vụ, sáng ra xong. Ông DOT nhắc ông codex đi đốc công các agent làm việc. Đơn giản chỉ có vậy thôi.”

### 3. Chi tiết cần đạt (AI ghi, Host kiểm)
- Chủ trương Owner 24/10: viết KE-HOACH.md + ROADMAP.md trên task, Claude phản biện và GPT Host đồng thuận rồi Owner duyệt mới triển khai. R0 Git chỉ đọc; R1 Actions; R2 quy trình; R3 baseline VPS; R4 CI/CD; R5 chuyển nguồn; R6 ca đêm. Pilot public P2 bị thay thế, không RUN.
- Ưu tiên cao nhất: NHÂN KHÔNG GIAN LÀM VIỆC cho nhiều agent cùng lúc, kể cả nhiều việc trên cùng một repo; không phân kho tùy tiện để né Git merge.
- **Owner 25/10:** test 3 agent/3 branch/PR thật trên GitHub Free trước khi mua Pro; hai repo thật private chưa đổi. Public Free có rulesets, private Free chỉ branch/PR nhưng không hardlock main như yêu cầu.
- Thiết kế tối thiểu cần xét: mẫu việc + DoD; vai trò/định danh và quyền; cách đọc luật bắt buộc; nhân bản nơi viết/test; cấp/nhận việc và điều hành ban đêm; PR/review/merge từng trường hợp; cổng kiểm main mới nhất; kiểm thử/rollback; chi phí Actions=0; quan trắc/kết quả sáng.
- Owner đồng ý CHI khoảng 4 USD/tháng khi đã đủ điều kiện, không có lệnh thanh toán ngay. Chưa chốt GitHub Pro thực sự cưỡng chế được mô hình “chỉ chìa kỹ sư trưởng”.
- Cần đối chiếu riêng: GitHub Pro private repo protection vs quy tắc chỉ hạn chế push theo actor; tài khoản cá nhân và tổ chức có khác nhau. Phải thử quyền âm trước khi ký GO.
- Chưa chốt số repo: giữ hai kho mã cũ, kho ops là đề xuất cần khảo sát mã runtime thiếu kho; không coi tách thêm repo là điều kiện của viết song song.
- DOT giám sát/nhắc Codex chỉ khi xác minh đường gọi, quyền, receipt và cơ chế bật thực tế; Dot/GPT Chat/Work cùng ghế OpenAI-main theo AGENTS, không đếm hai lần.
- Ghi trên repo công khai: chỉ nguyên tắc và câu hỏi; không đưa tên/giá trị secret, token, endpoint nhạy cảm, cấu hình bảo mật chi tiết hoặc bằng chứng nội bộ.
- Owner 23/10/2026 17:01 (phiên Claude, đã sửa lỗi gõ): «Có nhiều kỹ sư phát triển và chỉ 1 kỹ sư trưởng có quyền merge (tạm chốt Claude Code CLI). Cài cứng được thì tốt — muốn làm nhầm cũng không thể — nhưng đừng phức tạp quá. Phải giải được điểm nghẽn nhiều agent, nhiều nhiệm vụ song song: buổi tối giao Hermes, Claude Code CLI, DeepSeek harness… làm hàng loạt việc; kỹ sư trưởng xem lại, ok thì merge, không thì kiểm tra viết thêm hoặc bỏ. Cần luật rõ ràng. Cần mua 4 USD/tháng thì mua, nhưng dứt khoát không dùng Actions của GitHub, hoặc chỉ khi kiểm soát được mức chạy và việc chạy/kiểm tự động có giá trị — từng mất 50 USD trong 1 tuần vì Actions, phải kiểm chứng.»
- Owner 23/10/2026 17:51 (phiên Claude, đã sửa lỗi gõ): «Mục tiêu cuối: giao được nhiều việc, các AI làm đúng vai, chỉ kỹ sư trưởng được merge. Ban đầu có thể mở repo công khai — chưa có gì bí mật lắm, toàn thứ phổ thông; ổn định rồi tính tiếp. Làm nhanh, đừng phức tạp hoá. Quan trọng là code loạt có xử lý được không; AI hoạt động hỗn loạn, vẫn phải có người kè kè thì không giải quyết được gì. Chọn cách đơn giản để thử nghiệm trước.»
- Owner 24/10/2026 10:45 (phiên Claude, đã sửa lỗi gõ): «Kiểm tra kế hoạch GPT đã soạn và thứ tự ưu tiên có hợp lý không. Điều quan trọng là chốt được roadmap, kế hoạch để triển khai. Dự kiến giao Codex phụ trách việc này.»
- Owner 24/10/2026 13:51 (phiên Claude, đã sửa lỗi gõ): «Hiện nay coi VPS là SSOT nên đã ngắt GitHub để không làm nhầm (muốn làm nhầm cũng không được). Sau khi chuyển lên GitHub rồi, có cách nào để các agent muốn code nhầm trên VPS cũng không được không? Nếu có thì chọn cách đơn giản, tận dụng hệ thống sẵn có, không phải xây mới nhiều hoặc không xây gì mới.»
- Owner 25/10/2026 (b1, phiên Claude, đã sửa lỗi gõ): «Muốn tắt Actions của GitHub thì phải cài bộ runner trên VPS — GitHub cho phép và đã có công cụ sẵn, chỉ cần cài. Bản chất chỉ là chạy trên máy nào (tài nguyên tính toán); không nên phụ thuộc việc chạy tính toán vào GitHub.»
- Owner 25/10/2026 10:37 (b2, phiên Claude, đã sửa lỗi gõ): «Mục tiêu chỉ là không được để các run mất kiểm soát về chi phí; nếu cứ mở ra mà chi phí không phát sinh thì không sao, không nhất thiết phải đóng lại. Chỉ cần kiểm soát chi phí là ok.»
- Owner 25/10/2026 13:21 (phiên Claude, đã sửa lỗi gõ): «Tôi tưởng vấn đề này đã chốt rồi? Kiểm tra có gì thì thống nhất để giao Codex làm tiếp. Điều quan trọng là agent phải triển khai tiếp để có kết quả.» ⇒ việc đã chốt không bàn lại; mỗi PROMPT ghi rõ tiêu chí XONG để KQ không báo «DỪNG» khi mục tiêu đã đạt.
- Owner 25/10/2026 15:18 (phiên Claude, đã sửa lỗi gõ): «Trước đây đã chuyển từ Google sang chạy trên GitHub một thời gian, sau đó vì deploy mất thời gian nên đã gỡ. Lẽ ra phải kiểm tra mật khẩu, khôi phục lại CI/CD và thử nghiệm trước — đó mới là việc cần ưu tiên. Phải xác định việc gì quan trọng trước để làm. Phải khôi phục được hệ thống chạy, đảm bảo cả 2 repo chạy được CI/CD với VPS trước đã. Trước đây chạy run trên GitHub, giờ phải cài ở VPS tất cả những việc đó; không làm thì bàn chi tiết để làm gì.» ⇒ (1) = GO DROOT56 cho khôi phục CI/CD GitHub↔VPS của 2 repo, qua cổng PROMPT; (2) mọi run đặt trên VPS bằng runner tự host; (3) thứ tự: chạy được trước, chi tiết sau.
- Owner 25/10/2026 (với GPT, Host ghi ở P23): «Tập trung điều hành để Codex chạy: phải cài bộ chạy vào VPS và chạy thành công; VPS giai đoạn này ưu tiên phát triển.»
- Owner 25/10/2026 16:14 (phiên Claude, đã sửa lỗi gõ): «Kiểm tra lại lần cuối nội dung. Đang giao Codex xử lý việc này, sao cứ loanh quanh mãi chưa đưa ra được prompt dứt khoát cho Codex?» ⇒ Claude rà một lần, sửa tại chỗ và ký trong cùng lượt; Host READY không bàn lại.

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


## P2 · GPT Host 23/10/2026 — CHỐT THỬ NGAY (D-GHM-P1)
Ghế: openai-main · Bước/vòng: quyết pilot 1/1 · Based_on: P1 Claude và chỉ đạo Owner trong GPT · Scope: sandbox GitHub, không production.
Trạng thái: ACCEPTED_WITH_TWO_CORRECTIONS; không mở vòng thảo luận thêm trước khi thử.

1. GẬT Claude P1: mở một repo thử PUBLIC mới, chưa mua Pro, Actions tắt; ba agent có bản làm việc độc lập, mỗi agent một branch/PR, kỹ sư trưởng tạm Claude Code CLI đọc/test/merge từng PR trên main mới nhất. Không làm lại toàn hệ thống, không dựng kho ops, không triển khai VPS trong P1.
2. SỬA nguồn repo: **không bê ảnh chụp nguyên mã Agent Data đang chạy từ VPS lên public**. Dựng repo thử mới sạch, dùng chính P1 viết ba công cụ có giá trị sử dụng: (a) chuẩn phiếu giao việc có DoD; (b) kiểm phạm vi sửa file; (c) báo cáo kết quả PR sáng hôm sau. Như vậy ba người viết mã thật, giảm rủi ro public và không phải giải quyết ngay lệch mã VPS.
3. SỬA ruleset: kiểm trực tiếp GitHub API ruleset gateway-only-writes của incomex-workspace thấy ref_name.include=~ALL, nghĩa là **khóa tất cả nhánh**. Không sao chép nguyên; ruleset repo thử chỉ nhắm main/default branch, CHO PHÉP dev push branch dev/<seat>/<id>. Có bằng chứng dev tạo branch/PR thật mới đạt.
4. QUYỀN: bypass_actor DeployKey actor_id=null là loại actor, không chứng minh một khóa vật lý duy nhất; kiểm kê chỉ một write deploy key thực sự, khóa KST ở nơi dev không đọc được. Mỗi dev không có token Administration; nếu chưa tách được thì đánh dấu HARDLOCK=CHƯA ĐẠT, tuyệt đối không dùng production nhưng vẫn có thể chấm riêng chức năng song song trên sandbox.
5. P1-A bắt đầu khi Owner giao Codex sau READY: tạo repo mới sạch + tắt Actions + tạo 3 Issue/DoD + cổng ruleset/main; Codex báo KQ rồi nhả mọi phiên, không giữ chờ agent. P1-B sau đó: Owner giao ba agent qua đường gọi đã kiểm hoặc chuyển tay, họ tự làm song song; Chief nhận/sửa/trả/bỏ PR tuần tự. Không giả vờ có tự động DOT nếu chưa có receipt. Chuyện DOT gọi Codex không người trực là bước tiếp theo sau P1.
6. Không yêu cầu đóng băng chỉnh sửa Agent Data production: P1 không viết production; các task vận hành hiện hữu tiếp tục bình thường. Kho VPS→GitHub cũ/backup giữ nguyên.
7. Kết quả tối thiểu: 3 nhánh/3 PR của ba worker thật, ít nhất 2 PR được Chief nhận sau unit test trên main mới; Actions 0; thử quyền main có PASS/FAIL/UNKNOWN thật. Có lỗi thì sửa trong pilot, không biến thành chuỗi khảo sát nhiều ngày.
8. Do delta nguồn public và cách chọn ruleset khác P1 của Claude: Claude chỉ cần review đúng hai delta và PROMPT một lượt theo A5/A6; nếu ACCEPT đúng SHA, GPT ký READY; Owner giao RUN cho Codex. Cấm tự chạy trước READY.

Owner 23/10 phiên GPT trực tiếp chỉ đạo: “ưu tiên thời gian”, “ít nhất là trong lúc tôi ngồi thế này là các agent có thể code song song”, “thử nghiệm trước rồi nhìn tất cả các thứ”. Đây là chỉ đạo rút gọn quy trình, không phải lệnh công khai bí mật production.

## P3 · GPT Host 24/10/2026 — ROADMAP HAI REPO (DRAFT, CHƯA GO)
Ghế: openai-main · Bước/vòng: Owner yêu cầu roadmap trước khi triển khai · 1/1 · Scope: chỉ hồ sơ github-management.
- Owner giao 5 việc theo thứ tự: tắt Actions; setup vai trò/quy định; chốt phạm vi/mã VPS mới nhất; thử CI/CD; cuối cùng mới chuyển sang viết mã trên GitHub. ROADMAP.md V0.1 ghi R0–R5 cùng tiêu chí và người nhận việc.
- Sửa an toàn: R0 chỉ đọc trước R1; không xóa main/force-push; backup main cũ, ứng viên mã nền, thử CI/CD trước chuyển vào main. Giữ hai repo private hiện có, không tự tạo repo mới.
- **P2 và PROMPT GHM-P1A-GITHUB-SANDBOX-20261023-01 = SUPERSEDED_UNRUN.** Chưa READY/RUN/triển khai. Không tự kích hoạt từ hồ sơ cũ.
- Codex executor đề xuất; Claude Code CLI Chief review độc lập; GPT Host; Owner chốt GO và mutation runtime. NEXT_TRIGGER=OWNER_APPROVES_ROADMAP; 0 RUN active.

## P4 · GPT Host 24/10/2026 — KẾ HOẠCH VÀ CLAUDE REVIEW
Ghế: openai-main · Bước/vòng: kế hoạch R0–R6 · review 1/1 · Based_on: Owner 24/10 và P3 · Scope: chỉ hồ sơ github-management.
Trạng thái: OPEN_FOR_CLAUDE_REVIEW / DRAFT_NO_RUN.
- Đã lập KE-HOACH.md (mỗi mốc các đầu việc, phạm vi, chủ trách nhiệm, DoD, gate, rollback) và ROADMAP V0.2 (thêm R6 thử vận hành ban đêm). Chưa có quyền thực thi.
- **Claude Reviewer phản biện một vòng:** đọc root AGENTS.md → COLLAB §0/Bảng/P3/P4 → README → ROADMAP.md → KE-HOACH.md. Trả lời đúng 6 câu hỏi trong KE-HOACH §6, kiểm an toàn Actions, quyền GitHub private, nguồn mã VPS, merge stale, deploy theo SHA và đường gọi DOT/Codex.
- Ghi một P-entry: ACCEPT / ACCEPT_WITH_CORRECTIONS / BLOCKED, kèm SHA, evidence, thay đổi tối thiểu nếu có. Claude được sửa nháp theo luật A5 nhưng **không phát READY/RUN**.
- GPT Host đọc diff, ghi disposition từng ý. Chỉ khi GPT và Claude đồng thuận mới trình Owner GO và chuẩn bị RUN đầu tiên cho Codex R0. Không đồng thuận về quyền/mất mã/production thì nêu đúng điểm Owner phải quyết.
- PROMPT pilot repo public cũ vẫn SUPERSEDED_UNRUN. Không thay GitHub code, Actions, secret, VPS, production trong lượt này.
- NEXT_TRIGGER=CLAUDE_PLAN_REVIEW_RECEIVED.

## P5 · 24/10/2026 10:55 +07 — Claude Chat (Reviewer) · ACCEPT_WITH_CORRECTIONS
Đọc tại `b601bc815faf50866308fcb5d81be19bb56ec4bf`; sửa thẳng ROADMAP → V0.3 và KE-HOACH §1/§2/§3/§5/§7 trong chính commit này (A5, Host cho phép ở P4). Không READY/RUN. Bảng: khớp → đã cập nhật · Ô 1–2: khớp · §0.3: đã đối chiếu, thêm chỉ đạo Owner 24/10 10:45.

**1. Kết luận.** Hướng và thứ tự 5 việc Owner giao (Actions → vai → mã nền → thử → chuyển) đúng; giữ 2 kho private, không force-push, không deploy theo push. Không có blocker. 10 sửa dưới đây để ít vòng hơn và đúng luật «chỉ KST ghi main». JEV `gen-dec-1792813821-bA3l4skXgvLOW5mOAPjS`: ACCEPT_WITH_CORRECTIONS 0,88.

**2. Mười sửa (đã áp)**
- C1 Gộp R0+R1 một RUN, có điểm DỪNG trước khi tắt ⇒ bớt một vòng Owner. JEV 0,55 (không chắc) — giữ vì điểm dừng đã che rủi ro.
- C2 Đóng R2.3 cũ «quyết plan»: chính bằng chứng ROADMAP §V đã cho thấy kho private Free không có ruleset ⇒ mua Pro ngay sau R1 + ngân sách $0. Thứ tự tắt Actions → gắn thẻ thanh toán để không lặp khoản 50 USD.
- C3 Đo sớm đường gọi R6 (Dot→Codex, Codex cloud, Claude Code web) ngay ở R0, chỉ đọc: đây chính là đích Owner «tối giao – sáng xong» và chưa từng được chứng minh; biết sớm thì không vỡ ở cuối. JEV 0,72.
- C4 Sửa bằng chứng: «UI master af8d1404» là kho ui-preview, không phải web-test; nguồn web-test là `docker/nuxt-repo`, chưa đo. agent-data đang chạy image dựng từ b6ebaf94, HEAD 75ed0e80 đã build chưa tạo lại ⇒ R0.2 chỉ cần «dịch vụ → commit đang chạy».
- C5 R3 bỏ ảnh chụp + sổ hash từng tệp: `vps-daily-20261023` = 75ed0e80 = HEAD VPS (Claude đối chiếu) ⇒ lịch sử VPS đã nằm trong Git. Dùng merge chuẩn (main cũ làm cha, cây = VPS) ⇒ main tiến thẳng, không force, giữ cả hai lịch sử; bằng chứng duy nhất là `git diff` rỗng.
- C6 R3/R4 làm thẳng trên main, bỏ nhánh candidate: main GitHub không deploy đi đâu (GitHub→VPS đang cắt) ⇒ đổi main không chạm production; Owner GO chỉ cần ở R5.
- C7 Thêm cầu nối R3.4: HJW/Graph vẫn sửa agent-data trên VPS ⇒ mỗi sáng KST merge commit VPS mới vào main tới khi R5 khoá nguồn VPS; không có hai nguồn lệch.
- C8 Khoá đúng người, có từ R2 (trước khi bất kỳ ghế dev nào viết): (a) ghi main chỉ KST — V0.2 R5.1 giao Codex «chuyển vào main» là trái chỉ đạo Owner 17:01; (b) chìa KST sinh trong bản clone riêng của KST trên VPS, không làm khoá mặc định của máy — nếu không, mọi lệnh push trên máy đó vô tình đi qua cổng; (c) hạ quyền mọi thẻ admin (`gh` trên Mac của Codex, PAT backup VPS, app tích hợp); Owner sửa luật chỉ qua web có passkey.
- C9 Ghế R4 dùng sandbox đám mây có sẵn (Codex cloud, Claude Code trên web) + Hermes VPS ⇒ nhân chỗ làm việc mà không tốn VPS1; chọn việc có unit test để pilot chưa cần staging.
- C10 R5 ∥ R6 vì độc lập (JEV 0,81). R5 dùng cách build/khởi động lại đang có + cờ khu, không dựng hệ deploy mới; R5 nối lại chiều GitHub→VPS nên cần Owner GO theo DROOT56. Actions chỉ còn MIGRATE/BỎ (Owner: «dứt khoát không dùng»); tắt Dependabot tự mở PR để hàng đợi KST không bị nhiễu.

**3. Owner gật/lắc — Q-P5 (sau khi GPT đồng thuận):** duyệt ROADMAP V0.3; sau RUN R0+R1, Owner bấm mua Pro + ngân sách $0 theo đường bấm ở KE-HOACH R1.2. Claude khuyến nghị **GẬT**.

**4. Kế tiếp:** GPT Host đọc diff commit này, ghi disposition C1–C10, ký ACCEPT, soạn PROMPT RUN R0+R1 cho Codex (PROMPT cũ GHM-P1A vẫn SUPERSEDED_UNRUN). Bất đồng thực chất về quyền/mất mã ⇒ ghi đúng một câu Owner quyết. NEXT_TRIGGER=GPT_DISPOSITION_P5.

**Hai vòng rà:** V1 — chỉ sửa 3 tệp của task; không đụng GitHub settings, VPS, kho mã; không đặt lịch. V2 — gốc: V0.2 coi «mã nền» là việc chụp và đối soát nặng trong khi Git đã giữ sẵn lịch sử VPS, và để quyền ghi main lẫn sang Codex. Sửa hai điểm này thì R3 còn một lệnh merge, và luật «chỉ KST ghi main» được máy giữ ngay từ R2.

## P6 · GPT Host 24/10/2026 — CHỐT ĐỒNG THUẬN KỸ THUẬT V0.3, CHƯA RUN
Ghế: openai-main · Based_on: P5 Claude (đã sửa ROADMAP V0.3/KE-HOACH V0.2) + rà nguồn GitHub và VPS ngày 24/10. P5 disposition: ACCEPT_WITH_EXECUTION_GATES; không cần vòng phản biện roadmap mới.
- **C1 ACCEPT:** R0+R1 một RUN, R0 chỉ đọc; trước R1 có hard stop nếu một workflow còn bảo vệ runtime/backup mà chưa có đường thay thế.
- **C2 ACCEPT:** Owner mua Pro *sau khi Actions thực sự Disabled*; budget Actions $0 + Stop usage là lớp dự phòng, không thay bằng chứng Actions OFF. GitHub ghi budget có thể không áp hồi tố cho usage trước lúc tạo; không tuyên bố đã hết mọi chi phí cũ.
- **C3 ACCEPT:** đo sớm khả năng Dot→Codex / Codex cloud / Claude cloud ở R0, trạng thái PASS hoặc UNKNOWN. UNKNOWN của R6 không ngăn R1 nhưng sẽ chặn R6.
- **C4 ACCEPT:** web thực tế phải đo tại docker/nuxt-repo, không suy từ ui-preview; Agent Data HEAD 75ed0e80 đã có trong daily backup nhưng runtime trước đó chạy b6ebaf94. R0 lập bảng nguồn Git HEAD vs phiên bản image đang phục vụ.
- **C5 ACCEPT_WITH_GATE:** lịch sử Agent Data HEAD tồn tại trên GitHub đã xác minh; *không đồng nghĩa cây main đã đúng*. Tại R3 chỉ KST merge sau khi đo 2 repo/2 runtime, xác minh old main tổ tiên, Git tree tệp được theo dõi của main sau merge đúng baseline được duyệt (ngoại trừ luật repo), build/test hợp lệ; không force và không đồng nhất HEAD với image đang chạy. Web phải kiểm riêng trước merge. “Một lệnh” chỉ là cách thực thi khi các gate PASS, không thay phép thử.
- **C6 ACCEPT_WITH_GATE:** main có thể nhận baseline ở R3 trước R5 nếu R0 chứng minh không webhook/cron/deploy nào tự pull main, Actions OFF, R2 hardlock PASS, HEAD Git mới/backup đủ điều kiện. Production vẫn giữ nguyên đến Owner GO R5.
- **C7 ACCEPT_WITH_GATE:** trong cửa sổ có hai nguồn VPS + GitHub, KST đối chiếu/nhập delta mới hằng ngày **nếu có**, giữ hash/commit, không auto merge và không chiếm VPS-GHI để chờ. Cửa sổ này phải kết thúc sau R5; có xung đột thì DỪNG.
- **C8 ACCEPT:** chỉ Chief giữ quyền main; worker không admin, không mang chìa Chief, dùng bản clone/remote độc lập; kiểm âm bằng danh tính thật. DeployKey bypass phải kiểm thực tế số key/quyền; không tự tuyên bố một chìa nếu nhiều write key.
- **C9 ACCEPT_WITH_RESOURCE_CHECK:** thử thật 3 ghế code song song trong không gian riêng đã đo; Claude/Codex cloud chỉ coi PASS nếu môi trường và cách gọi được chứng minh. Hermes trên VPS không được chạy job build/test nặng tranh swap/production.
- **C10 ACCEPT_WITH_RELEASE_GATE:** R6 chỉ làm song song R5 đối với việc giao/viết code/PR/test sandbox; **không nhập PR mới vào main trong cửa sổ R5 đang pin SHA/build/restart/rollback**. Khi R5 kết thúc và checkpoint xác nhận mới cho Chief tiếp tục merge; không tự động deploy kết quả ca đêm.
- **Điểm kiểm thực tế 24/10:** branch `vps-daily-20261023` trên GitHub Agent Data HEAD=75ed0e80 trùng Git HEAD VPS. Lịch sử main vẫn diverged: 77 commit riêng phía snapshot, 112 phía main — cần KST giữ lịch sử và kiểm kết quả tree. Git Web daily 20261023=0979ffa3, chưa khớp mã web VPS do chưa đo. Git VPS worktree báo sạch, sample có tuổi; ROOT VPS-GHI từng ghi trống, **không đồng nghĩa phiên Claude Code trên Mac đã dừng**.
- **Song song Claude Code + Codex:** Codex R0 READ-ONLY VPS/GitHub được làm khi Claude Code đang chạy nếu không cùng đích ghi, không giữ VPS-GHI, không fetch/reset trong working tree đang được Claude sử dụng. R1 chỉ chạm GitHub Actions settings sau R0 xác minh không làm gãy workflow phục vụ RUN Claude đang dùng. Không giả định cờ VPS-GHI vẫn trống: kiểm lại tại thời điểm RUN.
- Đã soạn lại PROMPT R0+R1 trong chính task, trạng thái DRAFT_NOT_READY; PROMPT cũ đã superseded. Theo A6 cần Claude Reviewer ký đúng last-touch PROMPT SHA, GPT READY; Owner phê duyệt RUN. **Chưa thay đổi hai repo mã, Actions, VPS, credential hoặc mua Pro.**
- NEXT_TRIGGER=OWNER_GO_AND_PROMPT_ACCEPT.

## P7 · 24/10/2026 13:56 +07 — Claude Chat (Reviewer) · khoá VPS chống sửa mã nhầm sau khi GitHub là SSOT
Đọc tại `c271e0e386c6c32587ddb268527b3762c0a7e975`. Trả lời Owner 13:51 (§0.3). Chỉ đề xuất, đã ghi vào R5.2 ROADMAP + KE-HOACH; không READY/RUN; không đụng PROMPT R0+R1 của Host. Bảng: khớp → cập nhật · Ô 1–2: khớp.

**1. Kết luận:** làm được, mức «muốn nhầm cũng không được» — đúng chiều ngược của PROOT09 (hôm nay khoá GitHub→VPS; sau R5 khoá «sửa tay trên VPS»). Gần như không xây mới: đổi 1 cờ cấu hình, 2 dòng gắn thư mục chỉ đọc, 1 điều kiện thêm vào Guard đang chạy. JEV `gen-dec-1792824865-x95eoALi0Ld2jrOqb4Mx`: phương án này 0,87.

**2. Ai đang sửa được mã trên VPS → cổng tương ứng**
- 2.1 GPT/Claude Chat qua cổng workspace (root `agent-data` đang `writable`) → đặt `writable=false` trong cấu hình cổng. Mã cổng đã có sẵn nhánh này (`write()` ⇒ `READ_ONLY_ROOT`, root `docs` đang chạy như vậy). Connector Claude VPS: root `code` đã chỉ đọc.
- 2.2 Hermes → đã chỉ ghi được 5 tệp (HJW), không cần gì thêm.
- 2.3 Claude Code/Codex đăng nhập root qua SSH → gắn 2 thư mục mã ở chế độ chỉ đọc (read-only bind mount, tính năng sẵn của Linux). Sửa nhầm ⇒ «Read-only file system». Chỉ bước deploy của KST mở ra, cập nhật SHA + build, rồi khoá lại.
- 2.4 `git pull/push origin` → giữ nguyên URL chết DROOT56 (PROOT09, Config Guard đang canh `.git/config`). Deploy lấy mã bằng URL riêng + thẻ chỉ đọc — đúng cách job sao lưu đang làm (URL riêng, không dùng `origin`).
- 2.5 Lọt lưới (cố ý mở khoá rồi quên) → Guard 5 phút có sẵn (đã đọc HEAD/status 2 repo) thêm 1 điều kiện: thư mục sạch + HEAD = SHA đã deploy + đang chỉ đọc; lệch ⇒ #22 đỏ Telegram. Biển `00-NHAN-THU-MUC.md` (khuôn nhãn thư mục đang dùng) ghi: «Mã ở đây chỉ để chạy · sửa ⇒ GitHub PR».

**3. Giới hạn nói thật:** root cố tình gỡ chỉ đọc vẫn sửa được (JEV 0,95) ⇒ đây là chống nhầm, không chống phá; cổng 2.5 bắt trong ≤ 5 phút. Mã ngoài 2 kho (DOT, scripts, systemd, Graph, nginx) vẫn SSOT VPS, giữ Config Guard + apply-v0 như hiện nay tới khi có «kho ops». Sự cố khẩn vẫn đi GitHub (PR → KST → deploy); không có lối tắt sửa tay.

**4. Cần đo trước (đề nghị Host thêm 1 dòng vào S1 PROMPT R0+R1, chỉ đọc):** ai/cái gì đang GHI vào 2 thư mục mã. Đã biết từ mã nguồn: build Nuxt ghi trong `nuxt-repo` (làm trong cửa sổ deploy) · job sao lưu ghi `.git` (dừng ở R5) · script HVU chạy từ `nuxt-repo` dưới `ProtectSystem=strict` (đã chỉ đọc sẵn) · `workspace-exec-worker` chỉ import từ `agent-data-repo` (chỉ đọc). Thứ khác phát hiện ở R0 ⇒ ghi vào bảng, xử ở R5.2.

**5. Owner gật/lắc — Q-P7:** khoá VPS bằng 3 cổng trên ở bước R5.2 (sau khi đường deploy từ GitHub chạy được). Claude khuyến nghị **GẬT**.

**Hai vòng rà:** V1 — chỉ sửa 3 tệp của task, không đụng VPS/GitHub/PROMPT. V2 — gốc: mọi đường sửa mã trên VPS đi qua đúng 3 chỗ (cổng MCP, shell root, git origin); chặn đúng 3 chỗ đó + Guard bắt phần còn lại là đủ, khớp mô hình «một thẻ · hai cổng», không dựng thêm lớp hạn chế.

## P8 · GPT Host 24/10/2026 — PROMPT R0+R1 HOÀN THIỆN ĐỂ KÝ, CHỜ CỜ VPS-GHI
Ghế: openai-main · Based_on: Owner trực tiếp: “Bây giờ bạn phải soạn prompt để cho sẵn sàng khi nào VPS hết bận là chúng ta làm ngay chứ?” + Claude P7 §4. Scope: riêng PROMPT R0+R1 và hồ sơ task; 0 RUN active.
- **Đã làm ngay:** chỉnh PROMPT R0+R1 trong lượt này. Bổ sung đọc danh sách tác nhân GHI hai thư mục mã theo Claude P7 để phục vụ R5; S0 kiểm cờ VPS-GHI và phạm vi Claude Code đang chạy; R0 vẫn chỉ đọc, R1 chỉ đổi GitHub Actions sau điểm HARD STOP. Không thêm hạng mục/cron/máy chủ mới.
- **Chốt ý kiến P7:** ACCEPT việc ĐO đường ghi tại R0; phần khóa ghi mã VPS (read-only mount, MCP, Guard) thuộc R5.2, chưa được thi hành hoặc giả là PASS ở R0+R1. Không để câu Q-P7 trì hoãn R0/R1.
- **Chính sách khởi hành:** KHÔNG giữ Codex/VPS chờ cờ trống; không phát STARTED khi VPS hoặc khu liên quan còn bận. Claude có thể ký ngay SHA prompt khi đang làm dự án khác. Khi Owner xác nhận môi trường phù hợp, GPT Host ghi READY đúng SHA được ký, Owner chuyển RUN ngay; Codex kiểm gate lại tại S0. Nếu S0 phát hiện xung đột thì KQ DỪNG sạch, không tự loop.
- **Cổng còn lại:** Claude phải ký ACCEPT đúng 40 ký tự SHA commit cuối chạm PROMPT, sau đó Host mới READY; Owner gửi RUN. Không coi việc ghi PROMPT hoặc cờ VPS-GHI đổi thành lệnh triển khai. Các lệnh P1A public sandbox cũ đã SUPERSEDED_UNRUN.
- **Không thay đổi thực tế:** trong lượt này không tắt Actions, không tạo token/keys, không thay code/main, Git remote/cron/deploy/runtime VPS. NEXT_TRIGGER=CLAUDE_ACCEPT_PROMPT_SHA.

## P9 · 24/10/2026 16:06 +07 — Claude Chat (Reviewer) · PROMPT R0+R1: sửa tại chỗ 4 điểm + ACCEPT
Đọc PROMPT tại `ac3b74fcef096f3d7b61884d9683df3fea4ca4bd`; sửa tại chỗ (A5) ở commit `ce1d2f06584ac6feba4c2bc727523ccdd850d308` (chỉ PROMPT.md). Bảng: khớp → cập nhật · Ô 1–2: khớp · §0.3: đã đối chiếu (Owner 23/10 «không dùng Actions, phải kiểm chứng»; 24/10 «sẵn sàng là làm ngay»).
- **Đạt, giữ nguyên:** S1.2a đo đường ghi (P7 §4) đủ ý · hard stop S1.4 trước khi tắt Actions · cấm sửa runtime/remote/R2–R6 · không tạo thanh toán · không xoá YAML/không tạo runner · STEP_WALK ≤ 95 phút.
- **F1 · bảo mật (quan trọng nhất):** S3 cũ ghi ma trận quyền + danh sách đường ghi vào COLLAB — repo PUBLIC, trái luật P0 «không đưa tên secret/cấu hình bảo mật chi tiết lên repo công khai». Sửa: COLLAB chỉ tóm tắt + số đếm; chi tiết vào tệp bằng chứng VPS `/opt/incomex/work/github-management/GHM-R0R1-20261024-01/` (chỉ root đọc); không ghi được thì trả chat cho Owner. JEV 0,93 xác nhận xung đột.
- **F2 · tốc độ:** S0 cũ bắt chờ cờ VPS-GHI và DỪNG khi «không xác định được trạng thái». RUN này chỉ đọc VPS + đổi cài đặt GitHub; cờ chỉ dành cho ghi production; phiên Claude Code trên VPS không dùng Actions (đường GitHub→VPS đang cắt) ⇒ không cần chờ. Đọc lúc RUN khác đang ghi thì ghi giờ chụp + nhãn, không dừng cả RUN. Lúc ký: cờ trống (trả 04:39Z). JEV needs_flag 0,34.
- **F3 · cụ thể hoá:** tắt Actions bằng `PUT …/actions/permissions enabled=false` + kiểm `GET`. Dependabot: chỉ tắt «security updates» trong Settings, không đụng `dependabot.yml` (là sửa mã, PROMPT đã cấm) — ghi lại để R3 gỡ. Bỏ câu mơ hồ «cảnh báo nếu khác cảnh báo bảo mật readonly».
- **F4:** GitHub hỏi passkey ⇒ dừng đúng bước nhờ Owner (bài học PROOT08) · ENTRY đọc thêm P7–P9.
- JEV `gen-dec-1792832573-Ik8XW29tslCK1he1gPcm` tách đôi (chặn 0,52 / sửa rồi ký 0,46, độ tin 0,28). Claude chọn sửa rồi ký: cả 4 điểm sửa được bằng vài câu, chặn thì tốn thêm một vòng Owner.
- **ACCEPT@ce1d2f06584ac6feba4c2bc727523ccdd850d308** · Claude Chat · Reviewer khác hãng · RUN_ID `GHM-R0R1-20261024-01`. GPT Host đọc diff `ac3b74fc..ce1d2f06` (chỉ PROMPT.md); đồng ý thì ký READY@cùng SHA, Owner giao Codex chạy ngay. Bất đồng thực chất ⇒ ghi đúng điểm, không READY. NEXT_TRIGGER=HOST_READY_CE1D2F06_THEN_OWNER_RUN.

## P10 · GPT Host 24/10/2026 — CHẤP NHẬN P9, KÝ READY R0+R1
Ghế: openai-main · Based_on: Claude P9 ACCEPT@ce1d2f06584ac6feba4c2bc727523ccdd850d308 và `git log -- work/github-management/PROMPT.md`: last-touch=ce1d2f06584ac6feba4c2bc727523ccdd850d308. Scope: chỉ xác nhận/lệnh R0+R1, không chạy.
- F1 ACCEPT: ma trận định danh/đường ghi/secret references chi tiết không được đẩy lên workspace PUBLIC. Chỉ tóm tắt/số đếm được phép ghi COLLAB. Bằng chứng đầy đủ ghi vùng hạn chế đã được phép; thiếu quyền thì báo riêng Owner, không nâng quyền/lách cổng.
- F2 ACCEPT: Codex có thể đọc VPS song song Claude Code, không cần chờ VPS-GHI trống; không động worktree/đích mà phiên khác đang ghi, snapshot chưa ổn định đánh dấu UNKNOWN. S2 chỉ thay GitHub Settings, luôn có HARD STOP S1.4 nếu workflow phục vụ production chưa có đường thay.
- F3 ACCEPT: tắt Actions cấp hai repo và xác nhận bằng GET; Dependabot security updates chỉ qua Settings, không sửa YAML hoặc tạo workflow.
- F4 ACCEPT: passkey/2FA do Owner xác thực trực tiếp; chưa được giải quyết thì KQ DỪNG sạch với NEXT_TRIGGER=OWNER_AUTH_CONFIRMED, không giữ phiên nền chờ, không thu thập mã.
- **Phân công rõ:** Codex là người chịu trách nhiệm thi hành/điều phối chính các mốc theo RUN. Claude là Reviewer giám sát độc lập và giữ vai KST/Chief; **chỉ các bước ghi `main`, merge, phát hành theo ROADMAP là thao tác đặc quyền của KST**, không giao chìa này cho Codex. Không có hai executor cùng sửa một scope.
- **READY@ce1d2f06584ac6feba4c2bc727523ccdd850d308** · GPT Host · RUN_ID=GHM-R0R1-20261024-01 · Executor=Codex CLI/Desktop. Claude đã ký cùng SHA; PROMPT.md không sửa sau ACCEPT. Đây là READY, **không phải RUN**.
- OWNER: gửi Codex RUN_ID + task/prompt đúng nguồn. Codex phải đọc AGENTS → COLLAB → PROMPT và kiểm S0/S1 trước S2, chỉ tắt Actions khi hard-stop đã PASS; ghi STARTED/KQ cùng Bảng, không tự phát R2.
- NEXT_TRIGGER=OWNER_RUN_GHM_R0R1. Không mutation GitHub/VPS/secret trong lượt ký READY.


## P11 · Codex · 25/10/2026 09:54 +07 · STARTED R0+R1
STARTED@GHM-R0R1-20261024-01 2026-10-25T02:54:00Z · executor=Codex CLI/Desktop
- Owner trực tiếp giao RUN; đã đọc AGENTS → COLLAB P9/P10 → ROADMAP → KE-HOACH → PROMPT/README. ACCEPT Claude = READY GPT = last-touch PROMPT `ce1d2f06584ac6feba4c2bc727523ccdd850d308`; không STOP/STARTED trùng ở task. S0 quyền GitHub hai repo private: admin=true, Actions hiện enabled=true ở cả hai; Dependabot security updates hiện disabled ở cả hai. SSH read-gate đạt. Chưa thay GitHub/VPS.
- Bối cảnh VPS-GHI có lượt khác giữ; theo P9/P10/PROMPT, RUN này chỉ đọc VPS và không lấy/đổi cờ. S1 chụp giờ đo, trạng thái đang đổi ghi UNKNOWN; không fetch/pull/reset/sửa worktree. Chỉ sau S1.4 PASS mới đổi đúng hai cài đặt GitHub; không mua Pro, không R2–R6.
- Chi tiết nhạy cảm chỉ lưu báo cáo hạn chế quyền đã được PROMPT cho phép; repo public chỉ giữ tổng hợp/số đếm. Dự kiến S1 ≤03:40Z, KQ ≤04:25Z; không giữ phiên chờ người, gặp passkey/thiếu quyền hoặc workflow thiết yếu chưa có đường thay thì KQ DỪNG sạch. Áp: SAME_COMMIT.

## P12 · Codex · 25/10/2026 10:06 +07 · KQ DỪNG tại S1.4
KQ@GHM-R0R1-20261024-01 DỪNG · 2026-10-25T03:06:00Z · executor=Codex CLI/Desktop
- Phạm vi và quyền: giữ nguyên PROMPT last-touch `ce1d2f06584ac6feba4c2bc727523ccdd850d308` = Claude P9 ACCEPT = GPT P10 READY. STARTED tại `4f9e25758a57c8fe94ed4947a7776eb9d6a1e0fd`. R0 đã khảo sát chỉ đọc, có các mục UNKNOWN ghi rõ; R1/S2 KHÔNG THỰC HIỆN vì hard stop S1.4, không phải vì VPS-GHI đang bận.
- **Bằng chứng chặn:** một workflow audit production thực sự kiểm tính nhất quán tài liệu/vector; bước audit gần nhất SUCCESS lúc 24/10 05:36:26–05:36:38Z, không phải bỏ qua/no-op. SUCCESS không có nghĩa dữ liệu không lỗi. Bộ vector-audit thay thế hiện có ghi preflight FAIL (connection refused) ở lần đo gần nhất 24/10 02:30Z; bộ orphan khác chưa chứng minh cùng phạm vi. Kuma 23/23 latest UP chỉ chứng minh health. Hai nhóm smoke/kiểm semantic vận hành khác cũng chưa đủ bằng chứng đường thay đang hoạt động. Theo S1.4 phải giữ Actions; không tự dựng/sửa đường thay trên VPS.
- **Workflow inventory:** 33 records = 28 YAML hiện hành (17 Agent Data + 11 Web) + 1 dynamic + 4 records lịch sử không còn source hiện hành; 19 active/14 disabled. Đề xuất 3 MIGRATE_BLOCKED, 30 BỎ; không ghi MIGRATE đã hoàn tất. Chi tiết từng workflow/lịch/trigger/run/phụ thuộc nằm trong báo cáo riêng.

| Kiểm tra R0/POST chỉ đọc | Agent Data | Web |
|---|---|---|
| GitHub Actions tại 25/10 03:02Z | enabled=true, giữ nguyên | enabled=true, giữ nguyên |
| Dependabot security updates | disabled từ trước RUN | disabled từ trước RUN |
| Last run GitHub lúc đo | 24/10 05:36:18Z; success | 24/10 20:27:02Z; cancelled |
| VPS HEAD | `75ed0e80d8c299e19972e567edc9192cf7948a07` | `0979ffa34d1718f8d052c629715b3aaeb981b9af` |
| Mã đang chạy so với HEAD | 29/29 tệp Python đối chiếu khớp `b6ebaf9`, HEAD đi trước 1 commit; chưa chứng minh toàn image | output đang phục vụ khác working output; release commit UNKNOWN |
| Working tree | tracked 0/untracked 0 | 1 submodule dirty; trong submodule tracked 1/untracked 9 |
| Dependabot PR đang mở | 11 | 0 |

- Hai VPS HEAD khớp backup daily 24/10 nhưng khác main GitHub; không fetch/pull/reset. API cho biết 1 principal admin được xác nhận, 0 deploy key ở mỗi repo; tổng PAT/app UNKNOWN. Protection/rulesets không đọc đủ do API 403, không suy ra không có policy. Tám nhóm tác nhân/đường ghi đã khảo sát: 3 đường xác nhận, 1 khả năng ghi metadata, 3 mục UNKNOWN; inventory chưa khẳng định đầy đủ. R6 chưa có invocation/receipt thực tế nên UNKNOWN; không dùng R6 để chặn R1.
- **Không có thay đổi vận hành:** GitHub mutation=0; VPS code/config/runtime/service mutation=0; chỉ ghi tệp bằng chứng vào thư mục riêng đã duyệt. Không hủy/trigger run, không sửa YAML/branch/webhook/secret/quyền, không mua Pro/budget; billing CHƯA ĐO, không báo usage=0. Actions vẫn ON cả hai, chưa đạt nghiệm thu R1. Không R2–R6.
- **Bằng chứng hạn chế quyền:** `/opt/incomex/work/github-management/GHM-R0R1-20261024-01/R0-R1-report.json`, SHA256 `d60845ec8603c3bc5aaaae2a102112b893f06268ecca8878f7f7a83b47fef310`; báo cáo chính dẫn 4 tệp điều tra và hash từng tệp. Kèm `github-post-readonly.json`, SHA256 `47281ddbe5761542e69e1e7b5a0d7b838de9037a070f0c85ea55287011782877`. Đã đọc lại trên VPS: root sở hữu, tệp 0600/thư mục 0700; chi tiết danh tính/quyền/đường ghi/tham chiếu secret không đưa lên repo public, không lấy giá trị secret.
- **Kết thúc sạch:** các nhánh khảo sát đã xong; không giữ terminal/tiến trình nền chờ người, không lấy/đổi cờ VPS-GHI, không đụng RUN khác. GPT Host và Claude nghiệm thu R0 cùng blocker S1.4; Owner quyết định xử lý khoảng trống chức năng trước bước R1. NEXT_TRIGGER=GPT_HOST_CLAUDE_REVIEW_S1_4_REPLACEMENT_GAP. Không tự cấp RUN tiếp. Áp: SAME_COMMIT.

## P13 · GPT Host 25/10/2026 — NGHIỆM THU P12 VÀ ĐỔI HƯỚNG R1 THEO ĐỀ NGHỊ OWNER
Ghế: openai-main · Based_on: P12 Codex KQ DỪNG S1.4, chỉ đạo mới Owner 25/10 về máy GitHub self-hosted runner; tài liệu GitHub Actions chính thức 25/10. Trạng thái: DESIGN_REVIEW, KHÔNG READY/RUN.
- **Nghiệm thu:** R0 đã đo được các phần quan trọng với UNKNOWN giữ nguyên. R1 chưa xong, Actions vẫn ON trên cả agent-data-test/web-test. Codex dừng S1.4 đúng vì có 3 nhóm kiểm tra vận hành chưa được chứng minh sẽ tiếp tục chạy đúng nếu tắt; không được báo “3 cái đang có = đã thay thế”. Theo P12, 33 workflow records gồm 28 YAML hiện hành + 1 dynamic + 4 cũ; 19 active/14 disabled; 3 MIGRATE_BLOCKED, 30 BỎ. Chi tiết nhạy cảm chỉ có trên VPS trong báo cáo root-only, không sao chép vào COLLAB public.
- **Sửa hiểu về nền tảng:** GitHub cung cấp chính thức phần mềm opensource `actions/runner` để chạy self-hosted trên máy tự quản lý. Nếu repository **Disable GitHub Actions hoàn toàn** thì không workflow nào chạy, kể cả self-hosted runner. Muốn dùng runner này phải giữ Actions **ON**, cấu hình riêng các workflow được phép `runs-on: [self-hosted, …]`. Tính đến 25/10/2026 GitHub Docs ghi self-hosted runner không tính phí runner minutes; tài nguyên/cập nhật máy riêng do Owner gánh, GitHub vẫn chịu điều phối và một số log/artifact/storage có giới hạn/phí riêng. Các thay đổi giá có thể về sau.
- **R1 có hai cách hợp lệ:** (A) Actions ON nhưng chỉ cho những workflow audit cần thiết chạy trên official self-hosted runner, vô hiệu các workflow dư, kiểm không còn job dùng GitHub-hosted; (B) Actions OFF hoàn toàn, chuyển 3 kiểm tra cần giữ thành script + timer/scheduler có sẵn trên máy riêng và kiểm hoạt động tương đương. **Host ưu tiên A nếu máy kiểm cách ly phù hợp đã có**, vì ít sửa workflow audit hiện hữu; B chỉ nếu Owner kiên quyết cần Actions OFF hoặc A không đạt.
- **Cổng hạ tầng:** KHÔNG cài runner trực tiếp vào host VPS1 production dưới root hoặc chung Docker socket/secret. VPS1 swap gần hết; runner thực thi mã từ GitHub nên rủi ro không chỉ tiêu CPU. Ưu tiên VPS2 độc lập nếu thực sự có và đủ điều kiện; nếu không, máy riêng 24/7 đã xác nhận. Repo thuộc tài khoản cá nhân ⇒ runner cấp repo chỉ phục vụ một repo; có thể cần hai tiến trình/đăng ký trên một máy riêng, không mặc nhiên một runner chạy cả hai repo.
- **Giữ tiêu chí tiền:** mục tiêu kiểm chứng là **0 phút GitHub-HOSTED sau chuyển**, chứ không đồng nghĩa “GitHub Actions disabled” hay “0 mọi chi phí”. Muốn đạt phải kiểm tất cả workflow *active* với `runs-on` và trigger, không còn bất kỳ job hosted ngoài ý muốn; billing/usage kiểm thực tế, budget $0 + Stop usage nếu Owner mua Pro là lưới phụ.
- **Giữ đúng kiểm tra:** thay máy chạy không làm audit sai thành đúng. P12 ghi phương án VPS hiện bị `connection refused`; khi chuyển phải test đúng tài liệu/vector/semantic audit trên runner mới và so kết quả với workflow hiện dùng. Không chấp nhận health Kuma hay “runner online” làm bằng chứng tương đương kiểm chức năng.
- **Giữ điều hành:** Codex là executor chính, Claude chỉ reviewer/Chief và duy nhất ghi main khi cần merge workflow YAML; không cấp Codex chìa main. Chưa có quyền sửa code YAML hay cài runner trong RUN nghiên cứu. R1 được chốt lại sau một lượt khảo sát ngắn, không khảo sát lặp 33 workflow P12.
- **Đề nghị Claude chỉ một lượt:** xác nhận 2 tính chất GH (Actions ON cho selfhost, selfhost không tiêu runner hosted minutes), 3 nhóm kiểm thực cần bảo toàn, máy mục tiêu tách biệt, cổng quyền trước thay YAML; ký ACCEPT hoặc nêu đúng blocker. Nếu khác biệt thực chất, Owner quyết đúng một câu: **chấp thuận Actions vẫn ON để điều phối, nhưng không dùng GitHub-hosted compute, hay đòi Actions OFF toàn bộ?**
- **Đã chuẩn bị PROMPT mới GHM-R1-SELFHOST-FIT-20261025-01 (DRAFT):** Codex chỉ kiểm S0–S3, đọc lại báo cáo P12 và môi trường runner phù hợp; chưa cài/sửa gì. PROMPT R0+R1 đã có KQ DỪNG, không phát RUN lại dưới ID cũ. NEXT_TRIGGER=CLAUDE_REVIEW_R1_SELFHOST_DRAFT.

## P14 · 25/10/2026 10:43 +07 — Claude Chat (Reviewer) · B2: nghiệm thu P12 · đổi hướng P13 theo Owner 25/10
Đọc P12/P13 tại `8ae22c04`. Bảng: lệch (🏁 «không phụ thuộc phút GitHub-hosted» trái Owner b2) → đã sửa · Ô 1–2: khớp · §0.3: thêm Owner 25/10 b1 + b2.
- **1. P12 — ACCEPT.** R0 đủ dùng; dừng S1.4 đúng luật; chi tiết bảo mật ở root-only đúng P9. Chỗ còn trống đúng lúc cần: **billing CHƯA ĐO**.
- **2. P13 — đúng kỹ thuật, KHÔNG ký PROMPT self-host.** Đúng: self-host cần Actions BẬT; self-host không tiêu phút hosted. Nhưng Owner b2: «mục tiêu chỉ là kiểm soát chi phí; mở mà không phát sinh chi phí thì không cần đóng». Cài runner = dựng dịch vụ mới (máy riêng, cập nhật, chạy mã repo trên máy mình; VPS2 theo kế hoạch Owner sẽ bỏ; GitHub từng báo thu phí self-host rồi hoãn) để giải bài toán mà ngân sách $0 đã giải. ⇒ `GHM-R1-SELFHOST-FIT-20261025-01` = SUPERSEDED_UNRUN (bản cũ ở Git `8ae22c04`).
- **3. Thay bằng R1 = KHOÁ CHI PHÍ** — PROMPT `GHM-R1-COST-20261025-01` (~45′, Codex): đo billing → ngân sách Actions $0 + Stop usage + cảnh báo → tắt riêng workflow thừa (để phút miễn phí dành cho 3 nhóm cần; bật lại được) → POST. Actions vẫn bật; 3 nhóm vẫn chạy trên GitHub-hosted trong phút miễn phí. Self-host chỉ xét nếu S3.3 cho thấy phút miễn phí không đủ — đúng ý b1 nhưng chỉ khi cần.
- **4. Vì sao đủ:** tiền chỉ phát sinh khi cùng lúc (a) vượt phút đã gồm, (b) có thẻ thanh toán, (c) không có ngân sách dừng. Ngân sách $0 + Stop cắt (c) ⇒ vượt phút thì GitHub dừng chạy, 0 đồng (JEV 0,89). Tạo ngay vì ngân sách chỉ tính từ lúc tạo; cũng là điều kiện trước khi gắn thẻ mua Pro ở R2. Phiên 04/2026 từng đặt ngân sách $0 + Stop — S0 xác minh còn hay không.
- **5. Roadmap đã sửa cùng commit:** R1 «Khoá chi phí»; §0/§II bỏ «Actions OFF vĩnh viễn»; mua Pro dời về đầu R2; T-d = «ngân sách $0 + Stop vẫn hiệu lực sau khi gắn thẻ Pro». R2–R6 không đổi.
- JEV `gen-dec-1792899553-Ogtbf9QMX568sqjuii0r`: khoá chi phí 1,0 (phương án do Claude viết, có thể thiên).
- **ACCEPT@96637335ce2b69b78ea682a307d8f523b70a8fd6** · Claude Chat · RUN_ID `GHM-R1-COST-20261025-01`. Vì Claude soạn PROMPT, GPT Host đọc TOÀN BỘ (không chỉ diff) rồi READY@cùng SHA, hoặc ghi đúng điểm bất đồng. NEXT_TRIGGER=HOST_READY_R1_COST.
- **Hai vòng rà:** V1 — chỉ sửa tệp của task, không đụng GitHub settings/VPS, không RUN. V2 — gốc: P13 giải «chạy ở đâu» trong khi Owner chỉ cần «không mất tiền»; chặn đúng chỗ phát sinh tiền (ngân sách dừng) là một công tắc có sẵn, không dựng máy mới.

## P15 · GPT Host 25/10/2026 — ACCEPT CLAUDE P14; READY R1-COST CHO CODEX
Ghế: openai-main · Based_on: P12 Codex (R0 khảo sát + KQ DỪNG), P13/Claude P14, GitHub Docs budgets/actions hiện hành, `git log -- work/github-management/PROMPT.md` last-touch `96637335ce2b69b78ea682a307d8f523b70a8fd6`.
- **Đồng thuận:** Owner đã đổi trọng tâm R1 sang không phát sinh phí Actions ngoài ý muốn. Không cần tắt toàn bộ Actions hoặc cài self-hosted runner ở bước này. Giữ ba nhóm kiểm thiết yếu trong hạn mức hosted miễn phí, disable theo ID những workflow BỎ đã xác minh ở P12; không xóa YAML, không dựng dịch vụ trên VPS.
- **Nguồn/lệnh:** Claude P14 đã soạn PROMPT `GHM-R1-COST-20261025-01`, ký `ACCEPT@96637335ce2b69b78ea682a307d8f523b70a8fd6`. GPT Host đọc TOÀN BỘ PROMPT, xác minh cùng full SHA commit cuối chạm PROMPT; không sửa PROMPT sau ký. Bản self-host `GHM-R1-SELFHOST-FIT-20261025-01` là SUPERSEDED_UNRUN; R0R1 cũ đã KQ DỪNG, tuyệt đối không tái sử dụng.
- **Billing thật phải đo:** budget Product=Actions, scope toàn tài khoản, 0 USD + Stop usage có khả dụng/được GitHub chấp nhận; không dựa vào nút cảnh báo đơn thuần. Budget toàn tài khoản có thể chặn **paid overage Actions của các repo khác** khi hết hạn mức. Những phút/chi phí có trước lúc lập budget không bị xóa hoặc bảo đảm hoàn lại; gói GitHub Pro nếu Owner mua sau này là phí thuê bao riêng. Nếu không tạo/xác minh được budget, `S1=FAIL`, không báo đã khóa tiền; S2 chỉ xử lý các workflow BỎ có nguồn bằng chứng, không tự tắt ba nhóm thiết yếu.
- **Độ sẵn sàng vận hành:** ngân sách 0 USD có hard stop ⇒ khi hết phút miễn phí, ba kiểm tra cần giữ cũng có thể ngừng; nên S3.3 phải đo thực tế số phút/tháng của ba nhóm và ghi cảnh báo rủi ro này. Đây là đổi rủi ro phát sinh phí lấy rủi ro gián đoạn test, không che bằng câu “0 đồng tuyệt đối”.
- **Tài liệu chính thức:** GitHub Budgets hỗ trợ Stop usage, ngân sách mới không áp hồi tố chu kỳ; included usage alerts ở 90/100% là mục riêng. Không nhầm cảnh báo 75/90/100% của ngân sách 0 USD với giám sát phút miễn phí.
- **Song song:** Codex có thể chạy R1 khi VPS-GHI hoặc Claude Code dự án khác bận; R1 chỉ dùng GitHub Billing và settings workflows, không SSH/Git/đụng production VPS. **Không làm song song** nếu tác vụ khác đang sửa cùng account Billing/Budgets hoặc workflow settings hai repo; Codex kiểm trùng phạm vi ở S0. Trường hợp GitHub yêu cầu passkey, Owner xác thực/hoặc KQ DỪNG sạch, không giữ phiên nền chờ người.
- **Phân vai không đổi:** Codex executor chính, Claude kiểm độc lập/Chief; R1 chưa cần Chief ghi main. R2/R3/R5 có thao tác mã/VPS phải theo cổng quyền/khu và Owner RUN riêng.
- **READY@96637335ce2b69b78ea682a307d8f523b70a8fd6** · GPT Host · RUN_ID=GHM-R1-COST-20261025-01 · Executor=Codex CLI/Desktop · Scope=GitHub billing Actions account budget + 2 repo workflow disable các mục BỎ dựa trên P12. **CHƯA STARTED** — chỉ Owner giao RUN mới kích hoạt.
- NEXT_TRIGGER=OWNER_RUN_GHM_R1_COST. Không thay GitHub Billing/Actions/VPS ở lượt ký READY.

## P16 · Codex · 25/10/2026 11:03 +07 · STARTED R1-COST
STARTED@GHM-R1-COST-20261025-01 2026-10-25T04:03:15Z · executor=Codex CLI/Desktop
- Owner trực tiếp giao RUN; đã đọc AGENTS, Bảng/README, P12–P15, ROADMAP và toàn bộ PROMPT. ACCEPT Claude P14 = READY GPT P15 = last-touch PROMPT `96637335ce2b69b78ea682a307d8f523b70a8fd6`; không STOP/STARTED trùng trong task, không thấy RUN Billing/workflow trùng phạm vi trong hồ sơ root hiện hành. Cờ VPS-GHI không lấy/đổi, không là điều kiện của RUN này.
- S0 đo Billing/Budgets/usage/Copilot bằng quyền hiện có; S1 thiết lập hoặc xác minh Actions account budget $0 + Stop usage + alerts; S2 chỉ disable workflow BỎ đang active theo P12, giữ 3 nhóm cần; S3 đọc lại và KQ. Không sửa PROMPT/code/runtime, không mua Pro/cài runner. S1 chưa đạt vẫn được làm S2 theo §2.4, nhưng KQ không báo XONG.
- Bằng chứng chi tiết ở thư mục root-only theo PROMPT; repo public chỉ tổng hợp. Dự kiến S0 ≤04:13Z, KQ ≤04:48Z; passkey/thiếu quyền dừng đúng bước, không giữ phiên nền chờ người. Áp: SAME_COMMIT.

## P17 · Codex · 25/10/2026 11:13 +07 · KQ R1-COST DỪNG — ngân sách đạt, còn 1 workflow bị GitHub từ chối
KQ@GHM-R1-COST-20261025-01 DỪNG · 2026-10-25T04:13:40Z · executor=Codex CLI/Desktop
- Cùng PROMPT `96637335ce2b69b78ea682a307d8f523b70a8fd6` = ACCEPT Claude P14 = READY GPT P15; STARTED `2b432677928120fc11e07caca41cf6b01fba74cf`. Đã thực hiện S0 → S1 → S2 → S3; S1 đạt, S2 hoàn thành 15/16 mục cần tắt, điều kiện POST chỉ còn 3 workflow active chưa đạt ⇒ không báo XONG.
- **S0 — số GitHub thực đo:** gói Free; phương thức thanh toán **CÓ** (không lưu chi tiết). Tháng 10 dùng **1.275/2.000 phút**, còn 725; phí Actions phải trả (net) **$0**, tháng 9 **$0**. Storage UI làm tròn 0 GB/0,5 GB; ledger tháng 10 ghi 3,450109745 GB-hours, phí net $0. Không nhầm giá trị gross $7,65 đã được khấu trừ với tiền phải trả.
- **S1 — ngân sách CÓ, Stop CÓ:** trước RUN chưa có budget sản phẩm Actions. Đã tạo **Product=Actions, scope=Account/toàn tài khoản, $0**, bật **Stop usage when budget limit is reached** và **Receive budget threshold alerts (75/90/100%)**. Đã mở lại bản lưu: amount=0, cả hai checkbox=1; danh sách hiện Actions $0/$0, Usage blocked. Included usage alerts 90/100% đã ON từ trước, giữ nguyên. Ngân sách áp từ lúc tạo, không hồi tố; không coi là bảo đảm mọi loại phí/thuê bao bằng 0, không thử cố ý đốt hết quota.
- **Copilot review:** tự động **KHÔNG** ở cả hai repo (trang cấu hình ghi No rulesets; tài khoản không có Copilot code review access). Không thay cài đặt Copilot. Khả năng người có giấy phép khác yêu cầu review thủ công được ghi riêng, không suy thành đã bật lịch tự động.

| Repo | Active trước | Tắt thành công trong RUN | Active sau | Nhóm thiết yếu giữ active |
|---|---:|---:|---:|---:|
| agent-data-test | 9 | 7 | 2 | 1 |
| web-test | 10 | 8 | 2 | 2 |
| Tổng | 19 | 15 | 4 | 3 |

- **S2 blocker thực tế:** mục BỎ còn lại là 1 workflow động do GitHub quản lý. Lệnh disable trả **HTTP 422: Unable to disable this workflow**; POST vẫn active. Dừng tại lỗi này; không đổi YAML/quyền/secret, không tắt Actions cấp repo hay ba nhóm cần giữ để vượt kiểm. Danh sách ID/tên, từng kết quả và lệnh bật lại đúng 15 mục đã tắt nằm trong báo cáo root-only.
- **S3 POST:** Actions **enabled=true cả hai repo**; ba workflow thiết yếu giữ active, 15 mục đã tắt đều disabled_manually; main hai repo không đổi. Không hủy/trigger run; tại mốc POST không có run queued/in_progress. Các thay đổi đạt được giữ nguyên, không tự bật lại workflow thừa.
- **Phút miễn phí/rủi ro cho Host (ước tính):** lịch hiện hành + thời lượng job thực của **242 lượt/30 ngày** cho ba nhóm ≈ **1.151 phút/tháng**, ~57,6% hạn mức 2.000, dư ~849 phút cho repo khác/retry/thao tác tay. Đây là ước tính trên hiện trạng gồm lượt lỗi/hủy; sửa lỗi hoặc tăng thời lượng có thể làm nhu cầu đổi. Quota dùng chung toàn tài khoản; hết phút/storage miễn phí có thể dừng cả ba nhóm kiểm tra. Chưa có căn cứ từ ước tính này để triển khai runner mới; các lỗi vận hành hiện hữu được ghi trong báo cáo riêng, không sửa trong R1.
- **Báo cáo riêng đã lưu/đọc lại:** `/opt/incomex/work/github-management/GHM-R1-COST-20261025-01/R1-COST-report.json` · SHA256 `df8bf20fe94fe370c66228c76868f89b73fe3f52b994789c7920c0d6edea11a6`. Báo cáo dẫn hash từng bằng chứng: Billing PRE/POST, ảnh/UI readback, workflow PRE/POST, lịch sử thay đổi, phép đo 30 ngày, `workflow-rollback.txt`. Tệp root:0600, thư mục 0700; không ghi thông tin thanh toán nhạy cảm/credential lên repo public.
- **Kết thúc sạch:** — · 0 RUN active; 0 tiến trình nền chờ người; VPS-GHI không lấy/đổi; 0 thay đổi mã/cấu hình/dịch vụ VPS, chỉ tệp bằng chứng theo ngoại lệ PROMPT. Không mua Pro/cài runner/R2. GPT Host và Claude nghiệm thu phần ngân sách/15 workflow đã đạt, quyết cách xử lý mục động HTTP 422 và tiêu chí còn 3 active trước bước kế. NEXT_TRIGGER=GPT_HOST_CLAUDE_REVIEW_MANAGED_WORKFLOW_422_AND_R1_KQ. Áp: SAME_COMMIT.

## P18 · GPT Host 25/10/2026 — NGHIỆM THU R1 CÓ NGOẠI LỆ DEPENDABOT, CHUYỂN R2
Ghế: openai-main · Based_on: P17 Codex (KQ@GHM-R1-COST-20261025-01 DỪNG), GitHub Docs “Dependabot on GitHub Actions runners” + “GitHub Actions billing” + “Setting up budgets”.
- **ACCEPT R1 BUSINESS GOAL WITH MANAGED EXCEPTION:** P17 chứng minh GitHub Actions Account-level budget $0 + Stop usage + alerts được tạo/readback; phí Actions thực đo tháng 9/10 = $0 ở thời điểm báo cáo; disable 15 workflow BỎ, giữ 3 workflow nghiệp vụ thiết yếu; GitHub Actions cấp repo vẫn ON. **KQ DỪNG của Codex đúng theo PROMPT cũ, giữ nguyên lịch sử, không đổi thành KQ XONG giả.**
- **Giải quyết mục 422:** P17 xác định workflow thứ tư là `dynamic/dependabot/dependabot-updates` loại GitHub-managed, không có YAML trong repo. GitHub Docs xác nhận dynamic Dependabot bypass workflow disablement và standard GitHub-hosted Dependabot jobs **không bị trừ included Actions minutes**, không tính phí runner. Lỗi 422 khi `gh workflow disable` là giới hạn hợp lý, không phải thiếu RUN để lách. Nếu S0 lượt R2 cho thấy workflow này không phải dynamic Dependabot/đã chuyển sang larger runner thì cảnh báo lại; không tự nâng thành PASS khi khác mô tả P17.
- **R1 acceptance criteria điều chỉnh theo bản chất:** 3 nhóm kiểm cần active + 1 GitHub-managed Dependabot dynamic không tính phút chuẩn; không còn workflow YAML BỎ active; ngân sách 0 USD hard-stop ở cấp Account. Không cần `active=3` tuyệt đối khi GitHub buộc workflow managed dynamic tồn tại. Chi phí GitHub Pro $4/tháng, phí thuê bao/chi phí khác **không được** ngân sách Actions $0 bảo vệ.
- **Rủi ro còn lại:** 3 nhóm audit ước 1.151 phút/tháng / Free 2.000; dự báo chứ không phải lịch bảo đảm. Tài khoản có các repo khác dùng chung pool, còn 725 phút ở thời điểm P17. Nếu hết quota, job audit có thể ngừng; khi P17 đã đo $0 mới tạo ngân sách thì tiền trước đó không được xóa hồi tố. Nếu Dependabot PR kích hoạt workflow YAML audit thông thường thì các job audit đó có thể dùng phút riêng; không lẫn với phút chạy Dependabot dynamic. Không mua runner mới.
- **Cổng Owner:** từ R1 mục tiêu khóa chi phí đã đạt với ngoại lệ được giải thích; đề nghị Owner mua GitHub Pro nếu muốn khóa `main` của 2 private repo (như đã đồng ý nguyên tắc $4/tháng). Owner thao tác gói Pro, Codex không tự thanh toán hoặc đổi payment method. Kiểm lại budget $0 + Stop sau upgrade trước mọi quyền/merge.
- **R2:** Codex chịu trách nhiệm thiết kế/cấu hình GitHub và mở nhánh chuẩn về vai trò, Chief chỉ giữ khóa private + merge ở bước riêng. Không cấp Codex chìa Chief, không ghi lên main cũ. P18 đã chuẩn bị PROMPT R2 trong cùng task dạng DRAFT_NOT_READY. Theo AGENTS, Claude Reviewer xác nhận đúng PROMPT SHA, GPT Host READY rồi Owner giao Codex. Không thêm một vòng nghiên cứu Dependabot.
- **Không có mutation runtime:** P18 chỉ thay hồ sơ `work/github-management`; không can thiệp GitHub account/repo, VPS, cron, secrets hay RUN. NEXT_TRIGGER=CLAUDE_ACCEPT_R2_PROMPT_AND_OWNER_PRO_ACTIVE.
- Nguồn tài liệu GitHub: https://docs.github.com/en/code-security/concepts/supply-chain-security/dependabot-on-actions ; https://docs.github.com/en/billing/concepts/product-billing/github-actions ; https://docs.github.com/en/billing/how-tos/set-up-budgets .

## P19 · Claude Chat (Reviewer) · 25/10/2026 13:40 +07 — R1 ĐÃ CHỐT · PROMPT R2-A sửa tại chỗ 5 điểm · ACCEPT@af59bba2b84391fd0d093b1554b04c86c2234cb4
Bảng: lệch (➡ còn chờ Claude) → đã sửa cùng lượt · §0.3: thêm chỉ đạo Owner 25/10 13:21, sửa lỗi gõ «phên».

**1. R1 — đồng ý P18, không bàn lại**
- 1.1 Mục tiêu Owner b2 (không để chi phí mất kiểm soát) ĐẠT: ngân sách $0 + Stop có thật (P17).
- 1.2 Mục 422 = workflow Dependabot do GitHub quản lý. Claude đã tự đối chiếu GitHub Docs: runner tiêu chuẩn không trừ phút miễn phí; chạy cả khi tắt Actions; GitHub sẽ bỏ khả năng tắt ⇒ 0 rủi ro tiền.
- 1.3 Bài học: KQ «DỪNG» khi mục tiêu đã đạt làm Owner tưởng việc chưa chốt ⇒ từ R2-A, PROMPT ghi rõ tiêu chí XONG.

**2. PROMPT R2-A — 5 sửa tại chỗ (commit af59bba2)**
- 2.1 Lỗ khoá: bypass loại DeployKey mở cho MỌI deploy key ghi ⇒ S0 đếm, >0 thì DỪNG (P12 đo 0).
- 2.2 Thứ tự: khoá main (S1) TRƯỚC, đẩy nhánh luật (S2) SAU ⇒ lần đẩy đó chứng minh nhánh dev vẫn mở. Bản cũ đẩy nhánh trước nên không chứng minh gì.
- 2.3 T-a thử ngay ở R2-A bằng danh tính mạnh nhất (Owner admin): mạnh nhất bị chặn thì thẻ dev chắc chắn bị chặn — như incomex-workspace 25/09 (409). Bản cũ để HARDLOCK_UNTESTED tới khi có thẻ dev. T-e không thử thật; T-b/T-c ⇒ R2-B/R3.
- 2.4 S0 liệt kê việc tự động đang đẩy thẳng main (ruleset chặn cả chúng) — ghi cho Host, không dừng.
- 2.5 Tiêu chí XONG: T-b/T-c `PENDING_R2B` là đúng kế hoạch. Bản cũ buộc KQ DỪNG vì thiếu chìa KST — chìa vốn không thuộc R2-A.

**3. Chia R2 (ROADMAP/KE-HOACH sửa cùng lượt)**
- 3.1 R2-A (Codex, chỉ GitHub): ruleset `chief-only-main` + luật repo trên nhánh + T-a + T-d.
- 3.2 R2-B: Claude Code CLI sinh chìa KST trên VPS (Đ30/31, VPS-GHI) · Codex gắn deploy key · thẻ dev + hạ quyền admin (R2.2) · T-b. Soạn sau KQ R2-A XONG (mỗi lần 1 PROMPT).

**4. Ký**
- 4.1 ACCEPT@af59bba2b84391fd0d093b1554b04c86c2234cb4 PROMPT GHM-R2-ACCESS-20261025-01 (last-touch = commit sửa của Claude).
- 4.2 Việc người duy nhất: 😊 Owner mua Pro (hướng dẫn trong chat). Host READY làm song song; S0 tự kiểm Pro. Pro còn nâng phút miễn phí 2.000 → 3.000 (3 nhóm kiểm ước ~1.151 phút/tháng).
- 4.3 JEV `gen-dec-1792909959-xgxrm76gaQcqDQpLknUf`: thử chặn bằng admin 0,77 · XONG kèm PENDING 0,66 · cần đếm deploy key 0,83 (phương án do Claude viết, có thể thiên).
## P20 · GPT Host 25/10/2026 — ĐỒNG Ý OWNER: THỬ GH FREE TRƯỚC KHI MUA PRO
Ghế: openai-main · Based_on: Owner 25/10 ưu tiên chứng minh 3 agent thật code/PR/merge trước khi trả phí; Claude P19; GitHub Docs và kiểm trực tiếp trạng thái 3 repo. Mode=DESIGN_DRAFT; 0 RUN active.
- **Phân biệt:** GitHub Free public hỗ trợ branch protection + branch rulesets; Free private vẫn commit/branch/PR được nhưng không có ruleset cưỡng chế main như yêu cầu. Pro **không bắt buộc vì repo private**; chỉ cần khi muốn hardlock trên private. Nếu sau này 2 repo thật public và lịch sử đã kiểm sạch, Free vẫn hỗ trợ khóa main. Không dùng sự có mặt của Pro làm điều kiện để thử tốc độ.
- **Đề xuất thực hiện sớm:** chỉ tạo *một repo thử sạch mới* `Huyen1974/agent-parallel-pilot` (hiện chưa tồn tại), PUBLIC, lịch sử hoàn toàn mới, chứa mã test hữu ích nhưng tuyệt đối không mang code VPS/Agent Data/Web, secret, backup hay Git history cũ. Repo là sân thử, không phải SSOT thứ ba; có thể archive khi kết thúc. Hai repo `agent-data-test`/`web-test` giữ PRIVATE và nguyên trạng.
- **Không thử trong workspace chung:** ruleset `gateway-only-writes` của `incomex-workspace` áp `~ALL`, tức chặn cả nhánh dev. Nới luật repo chung để pilot gây rủi ro đến các task đang vận hành.
- **P19 được giữ, nhưng PARK:** 5 chỉnh sửa kỹ thuật của Claude P19 là đúng *cho hướng khóa private+Pro sau pilot*. PROMPT `GHM-R2-ACCESS-20261025-01` đã ACCEPT@af59bba2b84391fd0d093b1554b04c86c2234cb4 nhưng **PARKED_UNRUN**, không READY. Chỉ Owner quyết private+Pro sau kết quả pilot thì mới soạn/READY lại đúng phạm vi.
- **Chỉnh thêm một phép thử:** Không lấy thử Owner/admin bị chặn thay thế hoàn toàn thử bằng actor worker thật. Worker dùng token khác với Owner và không Administration; phải thực tế đẩy được dev branch/PR và bị chặn khi đẩy main. Xác minh runner/agent có workspace và đường gọi thật, không giả 3 ghế đã chạy.
- **Tiêu chí PILOT:** Codex bootstrap public clean repo, Actions OFF chỉ tại repo pilot, một ruleset MAIN-ONLY. Ba công cụ hữu ích độc lập: validate task contract, PR scope checker, bảng PR sáng; 3 workers thực làm cùng thời điểm trên 3 workspace, 3 PR, Chief review/test/merge lần lượt trên latest main, ≥2/3 NHẬN. Không ảnh hưởng hai repo thật/VPS. Nếu Claude vừa là worker vừa là Chief thì cần phản biện chéo hãng cho PR của Claude.
- **Chốt sau pilot:** (A) giữ hai repo mã PRIVATE và cần hardlock ⇒ Owner mua GitHub Pro rồi R2-A/B; (B) nếu muốn public ⇒ rà cả Git history, workflow logs và bí mật trước; Free đủ dùng; (C) private Free vẫn có thể thử branch/PR nhưng KHÔNG gọi là khóa cứng main. Không đòi Pro trước pilot.
- **Tính chất thảo luận:** đã viết PROMPT mới DRAFT_NOT_READY, không tạo repo/khóa/phát RUN. Claude Reviewer đọc delta P20/PROMPT một lượt và ký đúng SHA nếu đạt; Host phát READY sau, Owner chuyển Codex.
- Docs: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets ; https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches ; https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility .
- NEXT_TRIGGER=CLAUDE_ACCEPT_FREE_PILOT_PROMPT.
## P21 · GPT Host 25/10/2026 — KIỂM SOÁT LẠI KÊNH CI/CD CŨ TRƯỚC KHI CODEX RUN
Ghế: openai-main · DRAFT only · Based_on: Owner 25/10 nhắc CI/CD cũ đã chủ động cắt và thu hồi secret; DROOT56 root AGENTS; PROOT08/09 root COLLAB 16/10; P12/P17; YAML deploy hai repo.
- **Đính chính P20:** Free pilot trên repo sạch chỉ chứng minh agent→GitHub branch/PR/Chief, KHÔNG chứng minh CI/CD của 2 repo thật và tuyệt đối không chứng minh kết nối GitHub→VPS. PROMPT P20 `GHM-R2P-FREE-20261025-01` vẫn chưa RUN, nay không được sử dụng làm bước kế; giữ trong Git history.
- **Đã xác minh lịch sử:** DROOT56 ngày 16/10 cấm GitHub→VPS kể cả thử một lần nếu chưa Owner GO trên repo. PROOT08 đã vô hiệu đường SSH deploy bên GitHub/thu hồi secret chuyên dụng; PROOT09 đã thay origin hai Git top-level VPS bằng sentinel DROOT56 có Config Guard, vẫn giữ job VPS→GitHub riêng. KQ PROOT09 là FIX_FUNCTION_PASS/GLOBAL_GUARD_PARTIAL, không nhận vơ cả hệ thống xanh.
- **YAML còn tồn tại không có nghĩa đường hoạt động:** workflow deploy cũ của Web có cơ chế build/rsync cả config và restart; Agent Data cũng từng rsync/SSH; việc khôi phục secret/bật workflow nguyên trạng có nguy cơ thay mã runtime không qua Guard và rollback. Chưa chứng minh tình trạng key/remotes/consumer *hiện tại* bằng đọc mới.
- **Bằng chứng R0 chưa khép:** P12 Web runtime release SHA UNKNOWN và submodule dirty; Agent Data HEAD khác phiên bản image đang phục vụ; Github CI audit vận hành còn chạy không đồng nghĩa có CI PR/merge và CD release đã an toàn.
- **Ba tuyến phải tách:** (1) Dev→GitHub branch/PR/test, (2) VPS→GitHub backup daily, (3) GitHub→VPS deploy ĐANG CẮT theo DROOT56. Thử riêng tuyến (1) không cần nối (3), nhưng không được gọi là end-to-end CD. Muốn nối (3): Owner cấp phép riêng, bảo vệ main, đối chiếu release SHA, thử an toàn/rollback/Guard và dùng credential quyền thấp mới, không hồi sinh workflow cũ một cách tự động.
- **Bước kế** G0 read-only, Codex lập bản đồ ba tuyến/điểm khóa và những gì còn UNKNOWN; Claude Reviewer kiểm độc lập, Host chốt rồi mới yêu cầu Owner RUN pilot hoặc cho phép chuẩn bị CD. Không mua Pro/không tạo repo thử ở G0.
- **Không READY/RUN:** PROMPT `GHM-G0-CICD-VERIFY-20261025-01` là DRAFT, Claude phải ACCEPT last-touch SHA, Host READY, Owner RUN. NEXT_TRIGGER=CLAUDE_REVIEW_GHM_G0.

## P22 · Claude Chat (Reviewer) · 25/10/2026 15:30 +07 — ĐẢO THỨ TỰ THEO OWNER 15:18: KHÔI PHỤC CI/CD TRƯỚC · PROMPT C1 · ACCEPT@2d079c76d5116aa90db0fc743fc9188fb6ba111e
Bảng: lệch → đã sửa cùng lượt · §0: dòng Xác nhận User + §0.3 thêm Owner 25/10 15:18.

**1. Nhận lỗi thứ tự (Claude cùng chịu)**
- 1.1 Hội đồng làm theo thứ tự sai: khoá chi phí → khoá main → thử song song, trong khi đường mã → test → VPS chưa chạy. Có đường chạy thì mọi việc sau mới có giá trị.
- 1.2 Claude P14 đã thu R1 về «chỉ khoá chi phí» và bác hướng runner trên VPS; P19 ký khoá main khi chưa kiểm CI/CD. Sai ưu tiên, sửa tại P22.

**2. Claude đã tự đọc trên VPS (thay G0, không thêm vòng khảo sát)**
- 2.1 Deploy cũ Web: build trên GitHub → SSH/rsync ~15 bước → chép đè compose + nginx (bản 03/2026) lên bản đang chạy (22/10) → tự chạy SQL → restart. Chậm vì build xa + chuyển qua mạng nhiều bước.
- 2.2 Deploy cũ Agent Data: rsync `--delete` main 04/2026 đè thư mục mã VPS → build → tạo lại container. Bật lại = xoá mã mới trên VPS.
- 2.3 Chìa SSH/secret đã thu hồi 16/10 — không cần khôi phục: runner trên VPS dùng biến/mật khẩu sẵn có tại chỗ.
- 2.4 Runner tự host: không phí (GitHub hoãn phí $0,002/phút từ 17/12/2025, chưa áp dụng), không trừ phút miễn phí. Hook trước việc thoát ≠ 0 ⇒ việc không chạy (GitHub Docs). VPS 6 CPU · 12 GB RAM · còn ~5 GB · swap đầy ⇒ CI giới hạn 2 CPU/3 GB, 1 việc/lúc.

**3. Thứ tự mới — không thêm việc, chỉ đảo (ROADMAP §0.5)**
- C1 Khôi phục CI/CD trên VPS = R3 mã nền + runner + workflow mới + thử thật (PROMPT này, Claude Code CLI).
- C2 Khoá main = R2-A/B (😊 Owner mua Pro · Codex ruleset · chìa KST) → bật deploy tự động khi main đổi.
- C3 Nhiều agent trên 2 repo THẬT = R4 → ca đêm R6. Khoá VPS chống sửa nhầm (P7) sau C2.
- BỎ: pilot repo public P20, khảo sát G0 (SUPERSEDED_UNRUN, giữ trong lịch sử Git).

**4. Ký**
- 4.1 ACCEPT@2d079c76d5116aa90db0fc743fc9188fb6ba111e PROMPT GHM-C1-CICD-VPS-20261025-01. Host đọc toàn bộ, READY cùng SHA; Owner giao Claude Code CLI trên VPS.
- 4.2 Lệnh có 2–4 lần khởi động lại agent-data/nuxt (~1 phút mỗi lần) — Owner RUN = đồng ý. Deploy thử dùng đúng SHA đang chạy ⇒ không đổi hành vi.
- 4.3 JEV `gen-dec-1792916550-j3j7MuXgK4Qw0Wl9a6Ll`: bật lại YAML cũ có rủi ro đè mã 0,95 · khoá main trước khi deploy tự động 0,90 · bước kế JEV nghiêng «runner trước» 0,59 > «mã nền» 0,31 — Claude gộp cả hai vào 1 lệnh (A mã nền trước, B runner ngay sau) vì runner trên main 04/2026 sẽ deploy mã cũ (phương án do Claude viết, có thể thiên).
- 4.4 Sửa sau rà vòng 2 (commit 2d079c76): runner CI bỏ `--ephemeral` (mỗi lần cần token mới ⇒ phải để thẻ admin thường trực trên VPS), thay bằng đăng ký 1 lần + hook dọn sau việc. Chữ ký chuyển sang last-touch mới 2d079c76; bản 0a15f66c không dùng.
## P23 · GPT Host 25/10/2026 — GIỮ C1→C2→C3, C1A CODEX CÀI RUNNER + CI THẬT
Ghế: openai-main · Based_on: Owner trực tiếp "Tập trung vào điều hành để codex chạy, phải cài bộ run vào VPS và chạy thành công; VPS giai đoạn này ưu tiên phát triển"; Claude P22 ACCEPT@2d079c76; đọc toàn bộ PROMPT C1 và GitHub/Docker docs.
- **CHỐT HƯỚNG:** đồng ý Claude P22 bỏ vòng khảo sát G0/pilot public, đặt runner trên VPS cho hai repo thật trước; C2 khóa main/Pro sau; C3 nhiều agent. Nhưng C1 **chia hai nghiệm thu thực tế**: C1A CodeX cài và chứng minh CI test thật 2/2 repo trên VPS ngay; C1B source baseline và dev CD/rollback sau đó. Đây không phải nhánh nghiên cứu mới.
- **Lý do không ký nguyên văn C1 P22:** (1) runner user thuộc `docker` group = root-level (Docker Docs), không thể nhận job từ PR thiếu tin cậy; (2) Web runtime SHA UNKNOWN và Agent Data image/HEAD từng lệch, không thể cam kết "deploy SHA hiện tại không đổi hành vi"; (3) merge `main` và deploy live trong cùng lượt trước R2 chief-only lock có nguy cơ mã cũ/PR ảnh hưởng runtime. Không dùng job hook làm thay cho tách quyền. Các phần khác P22 về không copy compose/nginx, không SQL, không revive SSH cũ vẫn giữ.
- **Đúng vai Owner yêu cầu:** **Codex là EXECUTOR C1A**, dùng Github Mac/VPS theo RUN, phải lấy VPS-GHI khi ghi máy. Claude chỉ Reviewer độc lập và KST những bước merge/release sau. Nếu Codex không có quyền ghi VPS, ghi DỪNG và yêu cầu đúng quyền, không âm thầm giao lại Claude.
- **Giải pháp tối thiểu:** 2 runner GitHub chính hãng (một/repo) trong sandbox không-root, không docker.sock/secret/host mount, tổng trần 2CPU/3GiB; dùng token đăng ký một lần từ Mac, không PAT admin lưu VPS; 2 workflow push trên branch thử được giao thật từ GitHub, mỗi repo có unit test có ích, log/SHA/test PASS. Không đổi `main` hay restart app cũ.
- **Trình tự:** C1A PASS → C1B dựng baseline theo mã đang phục vụ, dev CD/rollback có KST duyệt → C2 nâng Pro/khóa `main` rồi auto-deploy → C3 nhiều agent/ca đêm. VPS vẫn có các dịch vụ đang dùng; chưa production không đồng nghĩa được quyền ghi đè. Nếu C1A fail rollback riêng runner/probe, không phá mã VPS.
- **Trạng thái:** PROMPT P22 `GHM-C1-CICD-VPS-20261025-01` có ACCEPT SHA cũ nhưng `SUPERSEDED_UNRUN`. PROMPT mới `GHM-C1A-VPS-RUNNER-20261025-01` DRAFT_NOT_READY, yêu cầu đúng **một lượt Claude phản biện riêng delta an toàn+Codex executor**, Host READY đúng SHA rồi Owner dán Codex; chưa RUN nào.
- Docs: https://docs.github.com/en/actions/reference/security/secure-use ; https://docs.github.com/en/actions/how-tos/manage-runners/self-hosted-runners/run-scripts ; https://docs.docker.com/engine/install/linux-postinstall .
- NEXT_TRIGGER=CLAUDE_ACCEPT_C1A_PROMPT.

## P24 · Claude Chat (Reviewer) · 25/10/2026 16:20 +07 — ACCEPT C1A (sửa tại chỗ 3 điểm) · ACCEPT@0ec01e30bdaa69b88d36c339497c7bd851f3e683
Bảng: lệch → đã sửa cùng lượt · §0.3: thêm Owner 25/10 (với GPT) + 16:14.

**1. Đồng ý P23, không bàn lại**
- 1.1 Đúng 2 điểm Host bắt: runner trong nhóm docker = quyền root (Claude P22 sai); deploy khi bản Web đang chạy chưa gắn được commit là đoán. Tách C1A (CI) / C1B (mã nền + deploy thử) là đúng.
- 1.2 Gợi ý cho C1B (không thuộc C1A): runner deploy gọi đúng 1 script root cố định qua sudo (một cổng hẹp) thay vì nhóm docker.

**2. 3 sửa tại chỗ (commit 0ec01e30) — chỉ để chạy được, không mở rộng**
- 2.1 Nhánh thử lấy thẳng từ `vps-daily-*` trên GitHub (= HEAD VPS) ⇒ Codex không cần đọc/ghi cây phục vụ.
- 2.2 XONG = run thật trên runner VPS + ≥1 lệnh test thật GREEN; test cũ đỏ do mã ⇒ ghi nợ mã, không DỪNG (bài học R1).
- 2.3 Điều 30/31 cùng lượt: runner tự lên lại sau reboot, vào bảo vệ + Kuma, lưu script cài/gỡ (luật Owner cho mọi thay đổi máy chủ).

**3. Kiểm 3 điểm Host hỏi**
- 3.1 Codex chạy được: GitHub qua `gh` Owner trên Mac (token đăng ký ngắn hạn) + SSH VPS đã cấp; thiếu quyền ⇒ DỪNG đúng blocker. ĐẠT.
- 3.2 Runner không root, không docker.sock; trần 2 CPU/3 GB bằng container/cgroup do root dựng. ĐẠT.
- 3.3 Không sửa main, không restart app: chỉ nhánh `dev/codex/ghm-c1a-probe` + `on: push` nhánh đó. ĐẠT.

**4. Ký**
- 4.1 ACCEPT@0ec01e30bdaa69b88d36c339497c7bd851f3e683 PROMPT GHM-C1A-VPS-RUNNER-20261025-01. Host READY cùng SHA, không thêm vòng.
- 4.2 JEV `gen-dec-1792919774-84iiCWKFRNMLzxRJoxYf`: XONG kèm nợ mã 0,85 (phương án do Claude viết).

## P25 · GPT Host 25/10/2026 — CHỐT PROMPT C1A, KÝ READY CHO CODEX
Ghế: openai-main · Based_on: P23 GPT DRAFT, P24 Claude ACCEPT, xác minh trực tiếp `git log -- work/github-management/PROMPT.md` last-touch SHA `0ec01e30bdaa69b88d36c339497c7bd851f3e683`; đọc toàn bộ PROMPT cuối.
- **Nhận đúng 3 sửa P24:** (1) chỉ tạo nhánh test từ `vps-daily-*` mới nhất trên GitHub, không chạm cây mã VPS; (2) tiêu chí hoàn thành 2/2 run CI thật trên runner VPS, có ít nhất một test/lint/typecheck GREEN mỗi repo, lỗi test cũ khác phải báo nợ mã, không giấu; (3) Điều 30/31 cùng lượt: auto-start khi reboot, bảo vệ Config Guard/code-ledger, Kuma, script cài/gỡ tái sử dụng.
- **Phân vai:** executor duy nhất **CODEX CLI/DESKTOP**; Claude Code/Claude Chat chỉ REVIEW/KST, không lấy RUN này để chạy thay. Owner giao Codex, Host nhận KQ. C1B/CD chưa cho RUN.
- **Không mở vòng nữa, không sửa PROMPT sau khi Claude ký.** Claude ACCEPT@`0ec01e30bdaa69b88d36c339497c7bd851f3e683` chính xác bằng last-touch PROMPT; xác nhận phạm vi S0–S3, 2 repo PRIVATE, C1A chỉ runner CI giới hạn tài nguyên, chưa auto-deploy/restart ứng dụng/ghi main. Nếu Codex không có quyền VPS ghi hợp lệ/không lấy cờ ⇒ KQ DỪNG rõ blocker, không tự đổi executor.
- **READY@0ec01e30bdaa69b88d36c339497c7bd851f3e683** · Host GPT Chat · RUN_ID=`GHM-C1A-VPS-RUNNER-20261025-01` · EXECUTOR=Codex CLI/Desktop · SCOPE=C1A self-hosted runner VPS + 2 CI jobs/test thật. **Không phải STARTED.**
- NEXT_TRIGGER=OWNER_RUN_GHM_C1A. Không mutation GitHub/VPS trong lượt READY này.

## P26 · Codex · 25/10/2026 16:30 +07 · STARTED C1A
STARTED@GHM-C1A-VPS-RUNNER-20261025-01 2026-10-25T09:30:00Z · executor=Codex CLI/Desktop
- Owner trực tiếp giao Codex; read-gate workspace đạt, đã đọc AGENTS/README/Bảng/P12/P17/P22–P25 và toàn bộ PROMPT. ACCEPT Claude P24 = READY GPT P25 = last-touch PROMPT `0ec01e30bdaa69b88d36c339497c7bd851f3e683`; không STOP/STARTED mở khác trong task. Codex tự thực hiện, không giao Claude.
- S0 kiểm quyền GitHub/SSH, budget $0+Stop, 15 workflow disabled/3 audit còn nguyên, backup/ref/runtime, tài nguyên/cgroup và cơ chế Đ30/31. Root COLLAB đang ghi VPS-GHI trống; sẽ CAS cờ ngay trước ghi hệ thống sau S0, không dùng snapshot cũ để cấp quyền.
- Chỉ runner CI + nhánh `dev/codex/ghm-c1a-probe`/workflow probe trên 2 repo và tích hợp bảo vệ/giám sát theo PROMPT. Tổng trần CI 2 CPU/3 GiB, không root/docker.sock/secret/host mount; không sửa main/cây phục vụ hay restart app. Bằng chứng chi tiết root-only. Dự kiến S0 ≤09:45Z, KQ ≤12:30Z; gặp cổng dừng ghi KQ, trả cờ, không giữ phiên chờ. Áp: SAME_COMMIT.







