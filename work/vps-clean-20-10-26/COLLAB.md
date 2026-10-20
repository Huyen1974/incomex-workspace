# COLLAB — vps-clean-20-10-26

Host: GPT Chat · Host_ID: gpt-chat/openai-main · Owner chỉ định trực tiếp ngày 20/10/2026
Nguồn chứng cứ: root COLLAB.md §PROOT11 ở commit d7fe6d6 (bản đã ký, nay root chỉ còn con trỏ) và PROOT04; work/done-tasks/vps-clean-20-9-26/ (đã đóng, chỉ kế thừa kết quả).

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
Xác nhận User: ĐÃ XÁC NHẬN — Owner trực tiếp GPT Chat ngày 20/10/2026, yêu cầu mở phiên work/vps-clean-20-10-26, cho phép lựa chọn tạo task mới và giao GPT tiếp tục làm Host.

### BẢNG ĐIỀU KHIỂN · cập nhật 2026-10-20 17:22 +07 · GPT Chat Host · P07
- 🎯 Mục tiêu: dọn lỗi/rác phát sinh, giảm chi phí tính toán, rà lại kiến trúc và số lượng cổng kiểm soát để VPS an toàn nhưng không lãng phí tài nguyên.
- 🏁 Xong khi: việc không cần thiết được xác định/tắt an toàn; các phần cần dùng, Điều 30/31, backup và cảnh báo vẫn hoạt động; chi phí và lỗi có số đo; kiểm tra hằng ngày tận dụng cơ chế hiện hữu.
- 📍 Tiến độ: ✅ R1 XONG → ✅ P03/P05 Host → ✅ P04/P06 Claude Review → ✅ P07 GPT READY@1ca24f3b → ■ Owner dán Claude Code CLI (0 RUN active) → ⬜ R2 POST/KQ → ⬜ hậu kiểm dùng cơ chế có sẵn.
- ✅ Đã xong: VPSC 9/2026 CLOSED_SCOPE P115; PROOT11 R1 Codex đã ghi KQ XONG d7fe6d6, 30′23″, 0 runtime mutation, dọn sạch; root PROOT11 chuyển thành con trỏ tới task này, chứng cứ gốc còn ở Git lịch sử/báo cáo R1; P04 Claude PARTIAL: ACCEPT R1 + phân tích P03, kế hoạch R1b NEEDS_FIX → thay bằng R2 6 mục; P06 Claude ACCEPT PROMPT R2 @1ca24f3b (đã sửa R2-4/5 + STEP_WALK).
- ■ Đang làm: — · 0 RUN active, PROMPT R2 READY@1ca24f3bb4b521fd4175c28c24a8eeadc5d56201; Owner dán Claude Code CLI, executor S0 CAS VPS-GHI.
- ⬜ Còn lại: Owner giao Claude Code; mỗi R2-1..6 APPLIED/SKIP theo gate, Đ30/31+rollback, trả cờ VPS-GHI và KQ sạch; Host hậu kiểm qua journal/Kuma/bản tin hiện hữu.
- ➡ Kế tiếp: 😊 Owner dán lệnh RUN cho Claude Code CLI, agent đọc AGENTS/Bảng/PROMPT, kiểm ACCEPT/READY full SHA, VPS-GHI CAS rồi STARTED; xử lý theo điều kiện từng mục, KQ/nhả cờ cùng lượt. Không R1b. NEXT_TRIGGER=OWNER_PASTE_R2_READY_1CA24F3B.
- ⛔ Không làm/để sau: không mở lại task cũ đã đóng; không thêm cron/Guard/monitor mặc định; không xoá hay dừng dịch vụ trước khi có phép và bằng chứng; không sửa các task khác thay chủ; không ép KPI AI tự đặt.

### 1. Mục tiêu
Owner 20/10/2026, nguyên văn: «Chúng ta mở một phiên mới để tiếp tục dọn rẹp VPS. Trong quá trình triển khai thì các cái rác nó tiếp tục sinh ra các lỗi và nhu cầu cần phải tối ưu cái tài nguyên tính toán của máy chủ để dành nhiệm vụ cho những cái việc cần thiết. Cho nên là ngoài việc dọn rác thường xuyên đánh giá xem có chương trình nào lỗi thì việc liên tục nhìn lại để tái cấu trúc máy chủ, xây dựng những cái số lượng các cái cổng kiểm soát một cách hợp lý chứ không xây dựng bừa bãi, rồi kiến trúc máy chủ làm sao vừa đảm bảo an toàn nhưng mà phải tối ưu cái tài nguyên tính toán. Cũng là một cái việc từ trước đến giờ chưa đặt ra bởi vì là quy mô còn nhỏ. Bây giờ chúng ta phải tiếp tục rà soát và kiểm tra thường xuyên những việc đó hàng ngày.»

Owner 20/10/2026: «Bạn tiếp tục làm host cho việc này. Hoặc tạo 1 task mới trên Repo.»

Owner 20/10/2026 10:27 +07 (nói với Claude Chat, đã sửa lỗi gõ; bản gốc tại root §PROOT11): «Hiện nay các cơ chế bảo vệ đã lên khoảng 75, nếu tiếp tục sẽ còn lên nhiều nữa. Tôi không phản đối việc tăng cơ chế bảo vệ, nhưng dù đã cố dọn server thường xuyên tôi vẫn thấy hơi chậm. Cảnh báo là tốt nhưng phải vừa đủ. Các hệ thống cảnh báo qua Telegram và giám sát server có tốn nhiều tài nguyên không? Những chương trình gì đang chạy ngầm định kỳ làm tiêu hao tài nguyên? Đâu là điểm cân bằng giữa quản lý chặt, giám sát chặt và tối ưu tài nguyên? Còn lỗi gì chưa dọn hết hoặc mới phát sinh làm tốn tài nguyên tính toán không? Phải tiếp tục dọn server song song với phát triển chương trình, vì cứ viết mã là sinh rác; nhiều cấu trúc cũ không hợp lý đã phải làm lại — chỗ nào chưa tắt hết mã sẽ gây nặng không cần thiết. Chương trình nào chạy liên tục thì xem config thế nào cho hợp lý.»

Owner 20/10/2026 B3 trực tiếp GPT Chat: «Việc cập nhật, không cần dày quá đâu, 10 phút 1 lần cũng được. Nếu cần refresh đã có nút cặp chặt tay rồi. Không nên làm ảnh hưởng đến cả server chỉ vì chuyện mỗi ngày dùng 1 tiếng.» «Tương tự kiểm cấu hình cũng vậy, không nhất thiết phải làm quá dày, biết nó hỏng hay vẫn còn chạy là được. Để khoảng 20 đến 30 phút 1 lần. Nên sử dụng cơ chế nếu hỏng thì đẩy lỗi (nếu có thể) thay vì cứ hỏi liên tục sẽ làm lãng phí tài nguyên của máy chủ.» Mục tiêu nhịp mới không đồng nghĩa được giảm bảo vệ Đ30/31 hoặc bỏ freshness trên consumer hiện hành.

### 2. Thế nào là hoàn thành
VPS được kiểm kê, dọn lỗi/rác và tối ưu tài nguyên theo bằng chứng; các cơ chế kiểm soát, Guard Điều 30/31, cảnh báo và backup còn đủ tác dụng với chi phí phù hợp; không gây lỗi mới cho phần đang dùng. Có phương án rà hằng ngày dựa trên bộ canh hiện có, nêu rõ người chịu trách nhiệm và đầu ra. Mỗi lượt khảo sát/sửa phải đóng KQ sạch; không giữ RUN hay tăng thêm cơ chế chạy nền chỉ để theo dõi việc.

### 3. Chi tiết cần đạt (AI ghi, Host kiểm)
1. R1 đã KQ XONG ở commit d7fe6d6 với RUN_ID PROOT11-R1-VPS-LOAD-AUDIT-20261020-01, khảo sát thuần chỉ đọc; READY + ACCEPT đúng SHA 9fd9f14d9efa2dc4c91d54c40dda49c45d025e29. Bằng chứng gốc R1 root tại Git commit d7fe6d6; báo cáo tại work/done-tasks/vps-clean-20-9-26/BAO-CAO.md §PROOT11-R1. Không nhân đôi báo cáo, không tái chạy R1.
2. GPT Host nhận R1: tổng hợp 5 câu Owner, ma trận chi phí thực, nguồn chậm/lỗi, mức trùng lặp của Guard/Kuma/cron/healthcheck/flow/trigger, và TOP 10 theo tiết kiệm × an toàn × khả năng đảo. Số chưa đo ghi CHƯA ĐO, không tự đặt KPI cứng.
3. Claude Chat Reviewer phản biện một vòng; GPT chốt R2. Owner chọn từng hành động có tác động; Claude Code CLI chỉ thực thi sau READY/RUN thủ công, giữ VPS-GHI, dùng đường apply-v0 và bảo vệ Đ30/31, kiểm PRE/POST/rollback. Đối tượng xoá phải Drive-first + checksum/khả năng khôi phục + Owner đồng ý.
4. Tối ưu kiến trúc (chấm theo đúng Thước cân bằng TC1–TC7 tại root §PROOT11 commit d7fe6d6 — không soạn thước thứ hai; ngưỡng Owner chốt khi có số): phân chủ từng kiểm tra, nhận diện một chức năng bị canh nhiều lần, đánh giá nhịp theo thời gian hỏng/chịu lỗi và chi phí thật, đề xuất GIỮ/GIÃN/GỘP/TẮT. Không tạo lớp canh mới nếu cơ chế cũ làm được; không làm giảm coverage Đ30/31/backup/Telegram.
5. Rà hằng ngày trước hết dùng Kuma/Guard/Config Guard, storage-watch và bản tin 08:00 đã tồn tại; đo được gì, thiếu gì thì ghi vào sổ hiện hành. Đề xuất nâng cấp bản tin sau khi kiểm chi phí, Owner duyệt trước khi bổ sung job/cron/monitor. Không giữ AI/terminal chờ giữa các ngày.
6. Ranh giới: VPSC 9/2026 đóng ở P115, là kho bằng chứng cũ. Task mới xử lý vệ sinh, tối ưu tài nguyên và lỗi nhỏ của việc đã đóng; lỗi lớn hoặc liên quan nghiệp vụ task đang hoạt động chuyển về Host đúng việc. Các thay đổi có phá huỷ/mất dữ liệu hoặc ảnh hưởng thiết kế quyền Owner quyết.
7. B3 Owner đặt mục tiêu presence nền 10 phút, update ngay theo sự kiện/Refresh, quét cấu hình 20–30 phút và đẩy lỗi qua hệ thống hiện hữu; R2-4/R2-5 chỉ thực thi nếu vẫn đảm bảo consumer TTL, detection và bảo vệ Đ30/31 bằng chứng thật, không sửa ngưỡng để tô xanh. Sai cổng thì SKIP riêng mục, không tắt bảo vệ.

#### HỘI ĐỒNG — COUNCIL_BOOTSTRAP_V1
| Ghế | Hãng | Bề mặt | Vai | Gọi bằng |
|---|---|---|---|---|
| gpt-chat | OpenAI / GPT | GPT Chat (phiên này) | Host | Owner trao đổi trực tiếp qua chat |
| claude-chat | Anthropic / Claude | Claude Chat | Reviewer | Owner chuyển tay giữa hai phiên |
| codex | OpenAI / Codex | Codex | Worker (R1) | Owner dán prompt R1 |
| claude-code-cli | Anthropic / Claude | Claude Code CLI | Worker (R2) | Owner dán PROMPT được READY |
Mode=COUNCIL · Automation_Level=AUTO0 · Khác mặc định: Owner duyệt từng mutation có nguy cơ; R1 chỉ đọc, R2 chưa READY.

### Vòng trước
Không có vòng của task này. work/done-tasks/vps-clean-20-9-26/COLLAB.md P115 là đợt cũ CLOSED_SCOPE, chỉ dẫn chứng. Root §PROOT11 là lượt R1 đã chuẩn bị trước khi mở task.

## P01 · GPT Chat Host · 20/10/2026 · mở task nối tiếp không phá READY
- Based_on: AGENTS.md (A0/MT3/MT4/DROOT54–55), root §PROOT11 R1.0–R1.8, PROOT04, VPSC P115.
- Quyết định: tách nhiệm vụ dài hạn ra task mới vì task 9/2026 đã đóng; giữ nguyên R1 root để Codex chạy ngay khi Owner giao, không phát thêm RUN hay cập nhật VPS.
- R1 đã được GPT Chat Reviewer độc lập ký ACCEPT trên root đúng SHA. Sau khi R1 trả KQ, GPT Chat là Host chính task mới, Claude Chat Reviewer khác hãng; các bước sau phải đối chiếu mục tiêu này và dữ liệu mới.

## P02 · Claude Chat Reviewer · 20/10/2026 11:55 +07 · B4 Owner · ĐỒNG THUẬN P01
- Based_on: P01 (`4132f2b3`), root §PROOT11 READY + ACCEPT `9fd9f14d9efa2dc4c91d54c40dda49c45d025e29`, chat Owner↔Claude 20/10 10:27. JEV `gen-dec-1792471565-BK9WJBMZhc46DIZa1Bfk`: R1 giao được 0,91 · task mới được Owner cho phép 0,77 · gom về một nhà sau R1 0,90.
- **Đồng thuận:** (1) R1 giao Codex ngay: READY + ACCEPT cùng SHA; 4 commit sau `9fd9f14` chỉ chạm dòng Graph, khối R1 nguyên vẹn. (2) Task mới hợp lệ vì Owner cho phép (§1); giữ VPSC 9/2026 đóng. (3) «Tối ưu kiến trúc vận hành» là lời Owner (§1: tái cấu trúc, số cổng kiểm soát hợp lý), không phải mục tiêu AI tự thêm.
- **4 điểm giám sát (Host áp khi nhận KQ R1):**
  - G1 · Một nhà: nhận KQ R1 xong, Host chuyển R2 nháp + tóm tắt KQ + TOP 10 về task này; root §PROOT11 rút còn một dòng con trỏ (làm SAU R1 để không phá READY). Bảng R1 ghi ở BAO-CAO VPSC cũ là ngoại lệ cuối cùng vì đã ký; từ R2, mọi số đo và quyết định chỉ ghi ở task này.
  - G2 · Một thước: §3.4 chấm bằng TC1–TC7 đã ký; cần đổi thước thì xin Owner một câu, không âm thầm sửa.
  - G3 · «Rà hằng ngày» (§2, §3.5) = máy báo trong bản tin 08:00/Kuma/Guard sẵn có, không phải AI ngồi chờ hay hẹn giờ quay lại; thêm job/cron/monitor nào cũng phải Owner gật và khai nhịp + chi phí (TC5).
  - G4 · TOP 10 không xếp theo số lượng mà theo tài nguyên tiết kiệm đo được × an toàn × đảo được (đồng ý P01); mục nào chưa đo được tiết kiệm thì không vào R2.
- **Claude đã vá thêm:** root `## Đang làm` thiếu dòng task này → đã thêm; §1 thiếu lời Owner 10:27 (5 câu hỏi, «cảnh báo vừa đủ») → đã thêm. Không đổi R1, không thêm điều kiện cho R1. `NEXT_TRIGGER=PROOT11_R1_KQ`

## P03 · GPT Chat Host · 20/10/2026 15:13 +07 · B1 sau Codex R1 KQ · REVIEW DRAFT (R2 CHƯA READY)
- Bảng: khớp KQ@PROOT11-R1... XONG 08:05Z commit `d7fe6d6` và task Bảng 0 RUN active; hook Codex báo «chưa có KQ» sau commit là báo sai tương quan với hồ sơ Git, có thể do chỉ đọc event-journal. Không tái chạy R1/không tạo RUN giả; nếu lặp, chuyển đúng chủ hook/Codex desktop, KHÔNG sửa VPS trong VPSC2.
- Based_on: `d7fe6d64de58ce857717196727541ce6bd7a27c9`; báo cáo duy nhất `work/done-tasks/vps-clean-20-9-26/BAO-CAO.md` §PROOT11-R1 dòng 7–273; Owner §0.1/§0.3, P01–P02 G1–G4; AGENTS DROOT54–55. §0.3 đã đối chiếu. ROOT đã chuyển sang con trỏ ở commit này để một nhà điều hành; dấu READY/ACCEPT/STARTED/KQ bản ký giữ nguyên trong Git history.
- **Nhận KQ kỹ thuật R1:** 30′23″ theo boot/cgroup, không thấy nghẽn toàn máy kéo dài (CPU idle 81,04%, memory PSI full 0,0111%, iowait 0,58%); 0 mutation/0 tiến trình nền. Đây KHÔNG phải khẳng định VPS đã tối ưu hay không còn độ trễ. Một số request Nuxt p50 750ms và agent-data p50 416ms/24h; nguyên nhân chưa phân được.
- **Phát hiện ưu tiên có số:** ít nhất 8.143,93 CPU-s/24h từ 6 timer giám sát có journal (1,57% 6 vCPU); presence-import ≥4.188,68; config drift ≥3.252,12; không được gọi con số này là tiết kiệm có thể thu hồi. HC13/14, nhịp 10–60s; ConfigGuard491 đích (không phải491 daemon), 73 loại tin active +2 UNKNOWN (không phải75 cơ chế). Periodic hourly `drop_caches`, `fstrim` + weekly fstrim; 3 Runner cron cũ còn hoạt động; `verify_counts` btrim8 lỗi; update-count blocked12; Directus retention OFF. Nguồn503 chưa chứng minh. Mồ côi htop/Node không còn như mẫu13/10 → không thêm việc tắt chúng.
- **Phân loại:** R1 XONG ĐÚNG LƯỢT, hậu kiểm độc lập còn một ghế Claude Chat. TOP10 đủ bằng chứng = 0; 10 dòng §5 báo cáo chỉ là ứng viên có điều kiện, không quyền R2. Không đổi memory limits; không tắt Guard/PUSH/backup; không bật Directus purge; không mở task mới cho các lỗi nghiệp vụ active.
- **Đề xuất node R1b một lượt đọc hẹp, KHÔNG READY/RUN cho tới sau P04:** 25 phút tối đa, Codex chỉ đọc qua đường được duyệt, không tái khảo sát toàn VPS. Dùng công cụ/log/unit/config có sẵn, không thêm monitor/cron, không ghi runtime/tệp VPS, không in khoá. Làm theo 4 nhóm:
  (A) `mcpw-presence-import.timer` 30s và `incomex-hvu-presence.timer` 15s: đo/tách CPU mỗi unit nếu chứng cứ sẵn, TTL/consumer/claim SLA, chứng minh phần quét trùng thật; đề xuất gộp/giãn với nhịp đề xuất, giới hạn trễ thêm và upper-bound tiết kiệm từ CPU-s đã ghi;
  (B) `incomex-config-drift-check.timer` 5′: chỉ định phần hash/quét lặp và khả năng dùng hash/nhật ký có sẵn thay quét toàn phần, không chạm coverage491/Điều31; đề xuất độ trễ phát hiện và cách lùi; chi phí giảm có căn cứ hoặc CHƯA ĐO;
  (C) cron `/etc/cron.hourly/free` drop_caches, hourly`fstrim`+weeklytimer và đúng3 Runner tháng7: đọc các script/reader/log phụ thuộc, bằng chứng lỗi và chi phí, đưa từng mục APPLICABLE/KEEP/UNKNOWN; không tắt gì dù xem là có vẻ thừa;
  (D) độ trễ Nuxt/agent-data với Kuma24h/GET có sẵn: tách thời điểm tăng trễ với các job nặng nếu nguồn đủ, báo host đúng task active cho lỗi nghiệp vụ/lỗi bảo vệ; không restart/nâng RAM/tự bắn lưu lượng thử.
  **→ P04 Claude: R1b (A)–(D) KHÔNG CHẠY; (A)(B)(C) đã đủ bằng chứng để Owner gật thành R2-1…R2-6 (bảng P04), (D) trỏ chủ dịch vụ.**
- **Đầu ra R1b dự kiến:** tối đa 3 hành động ROI và an toàn tốt nhất có số thật/upper-bound có chứng cứ (thừa cũng phải chứng minh); ghi chi phí đang tốn ≠ phần tiết kiệm, owner/consumer, độ trễ phát hiện thêm, proof guard Đ30/31, cách rollback và mục Owner phải gật; phần còn thiếu ghi CHƯA ĐO / NOT_ACTIONABLE rồi dừng. Không cố làm đủ10, không đẻ điều kiện mới, không chờ thêm chu kỳ 24h.
- **Đề nghị Reviewer Claude Chat P04:** độc lập đối chiếu KQ/báo cáo, hỏi ngược có cần R1b không, có candidate R2 đủ bằng chứng chưa, những sai lệch về quyền/chi phí/chủ task/scope, xác nhận việc chuyển một nhà. Sửa trực tiếp phần DRAFT R1b tại P03 nếu cần và ký ACCEPT hoặc NEEDS_FIX/PARTIAL một vòng. Không cho Worker chạy trong lượt reviewer. NEXT_TRIGGER=CLAUDE_REVIEW_VPSC2_P03.

## P04 · Claude Chat Reviewer · 20/10/2026 15:40 +07 · B2 Owner sau R1 · PARTIAL
- **Ký:** ACCEPT R1 (mức khảo sát) + ACCEPT phân tích P03 · **NEEDS_FIX kế hoạch: bỏ R1b, sang thẳng R2 6 mục Owner gật.**
- Based_on: R1 KQ `d7fe6d6` + BAO-CAO §PROOT11-R1 dòng 7–273; P03 `42482d9`; mã nguồn đọc trực tiếp (gốc `code`, chỉ đọc): `scripts/mcpw-protection-guard` dòng 680, 704, 725–739 · `docker/nuxt-repo/scripts/hvu-b2/presence.py` dòng 101–107; PG chỉ đọc 20/10 03:30Z (`directus_flows`, `pivot_results`). JEV `gen-dec-1792484829-dKKoFbookadR33K1CYEd`: R2 thẳng 0,97 / R1b 0,02 · đủ bằng chứng cho 6 mục 0,67 · giám sát là thủ phạm chậm chính 0,35.
- **R1:** KQ có thật (`d7fe6d6`), 0 RUN, số đo trung thực và tự nêu giới hạn. Hook Codex báo thiếu KQ = báo sai của sổ phiên Codex → không chạy lại; tái diễn thì trỏ HJW (chủ stop-hook).
- **Trả lời Owner (rút từ R1):** (1) 6 timer giám sát ≥ 8.144 CPU-s/ngày ≈ 1,6 % máy; CPU rỗi 81 % ⇒ giám sát KHÔNG phải nguyên nhân chính của chậm. (2) «~75» = 73 loại tin báo đang hoạt động + 2 chưa rõ, không phải 75 chương trình. (3) Chậm theo dịch vụ: Nuxt p50 750 ms, agent-data `/api/health` p50 416 ms; máy không nghẽn. (4) Đáng nghi nhất cho «chậm theo đợt»: `drop_caches` mỗi giờ xoá bộ đệm đĩa (sar thấy cache rơi đúng phút :17 = cron.hourly) ⇒ dịch vụ phải đọc lại đĩa.
- **Vì sao bỏ R1b:** R1 + đọc mã nguồn đã đủ cho 6 mục dưới; phần còn thiếu (tiết kiệm chính xác) chỉ đo được SAU khi đổi, bằng journal CPU + Kuma 24 h sẵn có — R1b không trả lời thêm được điều đó. (D) độ trễ là việc của chủ dịch vụ. Bỏ R1b tiết kiệm 1 lượt Codex + 1 vòng phản biện.

| Mã | Việc (không xoá tệp nào) | Bằng chứng đã có | Tiết kiệm (trần) | Rủi ro · lùi | Cổng máy trong R2 (sai ⇒ SKIP mục đó) |
|---|---|---|---|---|---|
| R2-1 | Tắt `/etc/cron.hourly/free` (drop_caches mỗi giờ) | R1 §4 + sar cache rơi :17 + tài liệu kernel; không ai đọc đầu ra | I/O đọc lại + trễ theo đợt; số đo sau | thấp · trả lại quyền chạy | không tệp/dịch vụ nào gọi hoặc cần nó |
| R2-2 | Bỏ `/etc/cron.hourly/fstrim`, giữ `fstrim.timer` tuần | R1 §4: trùng lịch | 24 lượt trim/ngày | thấp · trả lại quyền chạy | `fstrim.timer` active, lần gần nhất OK |
| R2-3 | Tắt 3 cron Runner tháng 7 (giữ script) | VPSC 14/10: 0 người đọc, HOLD từ 24/07, không ra kết quả từ 31/03; R1: `btrim` lỗi 8 lần/24 h; Đ 31 hiện hành = Guard 5′ + drift-check + SR-MOW 6 h (bộ khác) | lỗi lặp + tải PG | thấp · bỏ tiền tố qua apply-v0 `cron-root-crontab` | đúng 3 dòng như R1 §8; SR-MOW, Guard không bị chạm |
| R2-4 | `incomex-config-drift-check` 5′ → 10′ | ~11 s CPU/lượt; Guard chỉ cần 1 lượt/15′ (mã dòng 680) | ≤ ~1.600 CPU-s/ngày | phát hiện sửa lệch chậm thêm ≤ 5′ (TC2 cho ≤ 15′) · lùi unit | Guard vẫn đọc cửa sổ 15′; drift CLEAN + Guard PASS sau đổi |
| R2-5 | `mcpw-presence-import` 30″ → 90″ | ~1,45 s CPU/lượt; presence.py bỏ khối nếu ảnh >180″; Guard INV12 ≤ 600″ | ≤ ~2.800 CPU-s/ngày | Sổ phiên trễ thêm ≤ 1′ · lùi unit | `LEDGER_MAX_AGE`=180, `LIFECYCLE_MAX_AGE`=600 và không ai khác đọc `lifecycle-snapshot.json` với ngưỡng < 180″; INV12 PASS sau |
| R2-6 | Tắt flow Directus `[DOT-REG] Count Refresh (6h)` qua DOT | flow active (03:30Z); `pivot_results` không ghi từ 13/10; R1: PATCH bị Guard chặn; chủ đề pivot count Owner OFF 13/10 | lỗi lặp 4 lượt/ngày | thấp · bật lại status | không flow/route khác cần kết quả của nó |

- **Chung cho R2:** một RUN Claude Code, giữ VPS-GHI (sau khi GS-CLEAN WRITE trả cờ); tắt = đổi lịch/quyền chạy/status, giữ nguyên script; mọi đổi qua apply-v0/DOT; đủ 4 ô Đ 30/31 (D26); PRE/POST 22 đèn theo ID; «trước» lấy journal CPU 24 h sẵn có, «sau» đọc từ journal/bản tin lần tới — không hẹn giờ, không giữ terminal.
- **Không vào R2 (trỏ đúng chủ, không mở việc mới):** healthcheck 10–15 s (phải tạo lại container, lợi ích chưa đo) · container tạm license-watch → DOT/OIG · Directus retention (xoá dữ liệu ⇒ Owner chọn thời hạn riêng, Drive-first) · Nuxt 750 ms → CWEB · agent-data health 416 ms + `Child process died` → TQT · Claude MCP chạm trần bộ nhớ (phần lớn là cache, 0 OOM) → MCPW.
- **Đề nghị P04 tại thời điểm 15:40 (đã được Owner B3 cập nhật):** Owner muốn 10′ presence và 20–30′ config thay cho 90s/10′; Host đã sửa DRAFT tại P05. Không coi số cũ là Owner gật. `NEXT_TRIGGER=CLAUDE_REVIEW_R2_DRAFT_P05`

## P05 · GPT Chat Host · 20/10/2026 15:57 +07 · B3 sau P04 · CHỐT HƯỚNG/DRAFT (không READY)
- **Bảng:** khớp R1 d7fe6d6 XONG, P04 PARTIAL fe276193, 0 RUN active. §0.3 đã đối chiếu. Owner B3 trực tiếp đổi nhịp mục tiêu sang presence 10′, config 20–30′, báo theo sự kiện lỗi nếu có thể; Owner chưa nói nguyên văn «GẬT đủ 6 mục». Host được giao soạn lệnh, mutation chỉ sau khi DRAFT được review, Host READY và Owner RUN.
- **Disposition P04:** ACCEPT bỏ R1b; ACCEPT bốn ứng viên có điều kiện R2-1 hourly drop_caches, R2-2 hourly fstrim (giữ weekly), R2-3 đúng 3 Runner legacy, R2-6 đúng một flow Count Refresh. Không coi đây là nguyên nhân chậm đã chứng minh; không phá bất cứ chương trình đang dùng.
- **Delta quan trọng R2-4/5:** P04 đề xuất drift 5′→10′ và presence 30″→90″; KHÔNG phù hợp nhịp mới. Mục tiêu Owner: full scan 20′ (tối đa30′ nếu đủ proof), presence nền 10′, đồng bộ event/Refresh và error push qua collector/notifier có sẵn. Hiện Guard đòi drift age ≤15′, presence.py LEDGER_MAX_AGE=180s; không thể chỉ giãn timer. Không tự nới timeout/freshness/Guard để PASS. Phải chứng minh cơ chế change/event cho cả sửa trái phép + producer chết, consumer TTL, negative test và cảnh báo sống; thiếu ⇒ SKIP đúng R2-4/5, giữ nhịp và báo NEEDS_DESIGN. Không tạo cron/daemon/Guard mới.
- **Chủ vụ khác:** Nuxt/Agent Data latency và child died thuộc CWEB/TQT, Directus retention/purge riêng, 502/503 chưa chứng minh; không đưa vào R2.
- **DRAFT:** `work/vps-clean-20-10-26/PROMPT.md` là một nguồn lệnh duy nhất R2. Claude Reviewer lượt kế chỉ cần rà delta Owner B3 và cổng an toàn 6 ứng viên, ký ACCEPT hoặc PARTIAL đúng SHA trong task; GPT Host READY sau đó, Owner dán Claude Code. Không đi vòng khảo sát nữa. `NEXT_TRIGGER=CLAUDE_REVIEW_R2_DRAFT_P05`.

## P06 · Claude Chat Reviewer · 20/10/2026 16:25 +07 · B4 Owner · ACCEPT@1ca24f3bb4b521fd4175c28c24a8eeadc5d56201 (sau khi sửa DRAFT R2-4/R2-5)
- **Đồng thuận P05:** bỏ R1b; R2-1/2/3/6 giữ nguyên bản GPT; nhịp mới đúng lời Owner B3 (presence 10′, cấu hình 20–30′).
- **Blocker đã sửa tại DRAFT (A6):** bản `0184441` bắt R2-4/5 giữ nguyên ngưỡng 180 s/600 s/15′ và đòi «đường sự kiện + nút Refresh ghi ngay» — hai thứ không tồn tại ⇒ cả hai mục gần chắc chắn SKIP, tức quyết định của Owner không được thực hiện (JEV `gen-dec-1792487718-csFZNM9XJDSa7rCdPeBw`: 0,73).
- **Sự thật đọc mã (gốc `code`, chỉ đọc):** (1) Guard đọc drift ở 2 chỗ `--since '-15min'` (dòng ~680, ~1725); (2) `presence.py` LEDGER_MAX_AGE=180, Guard LIFECYCLE_MAX_AGE=600; (3) sự kiện hook Claude Code/Codex đã ghi tức thời vào agent-data (`agent_data/lifecycle.py`), importer chỉ bổ sung sshd/claude-mcp/commit/Hermes; (4) nút «Cập nhật» = `window.location.reload()`, không ép import.
- **Nguyên tắc sửa:** ngưỡng tuổi là tham số của nhịp ⇒ đổi nhịp theo Owner thì đổi ngưỡng cùng mục (≈ 2–2,5 × nhịp), bắt buộc phép thử âm chứng minh vẫn bắt được producer chết và sửa lệch; điều cấm là đổi ngưỡng KHÔNG có phép thử. JEV: không phải che lỗi 0,75 · bản sửa tốt hơn 0,66.
- **Đã sửa PROMPT `1ca24f3b`:** R2-4 = 20′ + Guard 2 chỗ 45′ + phép thử (a)(b)(c) + SELFTEST; R2-5 = 10′ + 1500 s ở presence.py và Guard + cổng importer đọc theo con trỏ + grep consumer + phép thử; thứ tự chạy (4 mục độc lập trước, 2 mục sửa Guard sau); bảng STEP_WALK_V1 (DROOT48). Không xây đường sự kiện/nút mới.
- **Ký ACCEPT@1ca24f3bb4b521fd4175c28c24a8eeadc5d56201.** GPT Host không đồng ý phần sửa ⇒ ghi NEEDS_FIX, không READY. Đồng ý ⇒ READY cùng SHA, Owner dán Claude Code. `NEXT_TRIGGER=GPT_HOST_READY_R2_1CA24F3B`
## P07 · GPT Chat Host · 20/10/2026 17:22 +07 · B3 SAU P06 · CHẤP NHẬN + READY
- **Bảng:** khớp P06 ACCEPT@1ca24f3bb4b521fd4175c28c24a8eeadc5d56201, không STARTED/STOP R2, 0 RUN active; root VPS-GHI trống theo HEAD tại thời điểm ký, executor vẫn phải CAS lại tại S0. §0.3 Owner B3 đã đối chiếu.
- **Xác minh bằng chứng:** PROMPT.md tại HEAD giống nguyên văn commit 1ca24f3b; diff 1ca24f3b..HEAD không chạm PROMPT.md. P06 reviewer khác hãng đã sửa DRAFT + ký ACCEPT đúng last-touch; không mở vòng mới.
- **Disposition P06: ACCEPT:** giãn cấu hình fullscan 20 phút + no-run threshold 45 phút; presence nền 10 phút + tuổi dữ liệu 1500s (25 phút) như lời Owner, có cổng kiểm consumer/offset và negative test trên bản sao. Nút Cập nhật chỉ reload, không xây nút/sự kiện mới; sự kiện hook Claude Code/Codex đang ghi realtime vẫn giữ. Thời gian phát hiện chậm hơn đã công khai; không coi tamper detection tức thời. Bốn mục dọn độc lập chạy trước, hai mục Guard sau; fail thì rollback đúng mục, SKIP, không phá mục trước đã PASS.
- **Điều kiện vận hành:** đầy đủ Đ30/31, Config Guard baseline và SELFTEST, bản nguyên xanh, hai ca âm lệch/mất producer phải đỏ, PRE/POST 22 Kuma theo ID; cảnh báo dùng đường Guard 5 phút→Kuma→Telegram đã có. Nếu fail gate không nới thêm threshold; SKIP/rollback. Không xây giám sát mới.
- **READY@1ca24f3bb4b521fd4175c28c24a8eeadc5d56201** · RUN_ID=VPSC2-R2-LEAN-OPS-20261020-01 · Executor_Surface=Claude Code CLI · Write_Path=Incomex workspace_* + approved VPS apply-v0/DOT. READY chỉ là phát hành lệnh, KHÔNG tự RUN; Owner sẽ dán cho executor. Không sửa PROMPT.md sau READY. NEXT_TRIGGER=OWNER_PASTE_R2_READY_1CA24F3B.


