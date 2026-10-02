# COLLAB — pg-nhan-balo
Tên việc: Mở balo là biết PG có gì · dùng lại được gì · thừa gì (luật nhãn + dán nhãn)
Host: Claude Chat · Host_ID: CLAUDE-PGNB-261002-A · Owner giao 02/10/2026

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
Xác nhận User: **ĐÃ XÁC NHẬN** — Owner, chat Claude 02/10/2026 16:14: “Đồng ý cho các bạn mở việc mới này.” (sau khi Host xin phép đủ 4 ý — D01). Được phép: viết luật → góp ý → đồng thuận → dán nhãn. **Chưa cho phép tắt/xoá/dời bất cứ vật nào.**

### BẢNG ĐIỀU KHIỂN · cập nhật 2026-10-02 16:58 +07 · Claude Chat (Host) · READY PGNB-LABEL-20261002-01
- 🎯 **Mục tiêu — Owner nguyên văn 02/10:** “Mục tiêu là phân loại hiệu quả. cả người và AI có thể dễ dàng biết được là đã có gì? Cần làm gì? Những gì thừa nên xóa đi? Hoặc nên khoanh vùng lại?” · “Chỉ cần dán nhãn thôi. Xóa thì nhanh cho nên chúng ta chưa hành động vội. Cứ dán nhãn để đấy, xóa lúc nào thì xóa.” **Vì sao:** hệ sẽ phức tạp gấp 20–100 lần; không nhìn và lọc được thì Owner không chỉ đạo được.
- 🏁 **Xong khi:** mở trang PG Census lọc được mọi bảng · view · hàm · trigger theo 5 nhãn; không còn ô trống ở 4 nhãn đầu (nhãn thứ 5 chỉ Owner quyết, theo khối); dán sai giá trị thì PG từ chối; có màn “Balo theo khối” nhìn 30 giây. _(đề xuất Host, nằm trong tin Owner gật 02/10)_
- 📍 **Tiến độ:** `✅ khảo sát · ✅ luật v1.0 đồng thuận (Claude + GPT) · ✅ PROMPT READY · ■ Owner RUN → Codex đặt biển + dán nhãn · ⬜ nghiệm thu · ⬜ Owner quyết theo khối`
- ✅ **Đã xong:** khảo sát PG thật 02/10 (số liệu ở `view.html#so-lieu`) · luật nhãn **v1.0 đã đồng thuận** (`view.html`): tem 5 câu hỏi · 4 nguyên tắc cho người = 12 luật cho AI · từ điển + câu thử · 4 biển tại hiện trường (`#bien`) · 3 điểm nối với sổ DOT (`#so-dot`) · P01 GPT đã xử lý · `PROMPT.md` soạn xong.
- ■ **Đang làm:** READY đã đặt (mục `## RUN`) · chờ 😊 Owner dán lệnh RUN cho Codex.
- ⬜ **Còn lại:** 🤖 Codex chạy RUN (đặt biển B1–B4, dán KHỐI · VAI · SỐNG · DÍNH, màn theo khối) · Host nghiệm thu (chấm lại 30 bảng mẫu) · 😊 Owner quyết giữ/đóng băng/chờ bỏ theo khối · sau đó mới viết mô tả một dòng cho thứ giữ lại · T2 (dòng trỏ trong KB) khi KB mở ghi.
- ➡ **Kế tiếp:** 😊 Owner dán lệnh RUN cho Codex · 🤖 Codex STARTED → KQ · Host nghiệm thu · Reviewer GPT rà KQ một vòng.
- ⛔ **Không làm:** tắt/xoá/dời bất cứ vật nào · sửa thứ gì ngoài balo, bảng từ điển và các biển nêu ở `view.html#bien` · viết thêm nhãn vào `COMMENT ON` của vật khác · điền `ket_luan` thay Owner · đổi cấu hình PG để đo thêm · viết DOT mới trong RUN này · dựng registry/bộ máy mới.

### 1. Mục tiêu
Owner nguyên văn, chat Claude 02/10/2026:
1. “Tôi đã tạo ra 1 cơ chế đọc để hiểu trong PG có những gì, nhằm tránh mù mờ.” · “Mục đích là mô tả rõ đinh nghĩa, phân ra để biết chúng ta có gì? Thiếu gì? Cần làm thêm gì? Khi cần đến 1 việc thì kiểm tra nhanh để biết? Đã có gì rồi? Có thể dùng lại hay phải làm mới? Ví dụ như cần đến DOT/function.... thì có thể xem trong liệt kê.”
2. “Mục tiêu là phân loại hiệu quả. cả người và AI có thể dễ dàng biết được là đã có gì? Cần làm gì? Những gì thừa nên xóa đi? Hoặc nên khoanh vùng lại?..... cần 1 nơi để cùng hiểu thống nhất giống như repo hiện nay là có thể cùng thông tin 1 cách thống nhất (giữa con người và ai)”
3. “Tóm lại: kiếm 1 nơi để viết luật mà ai cũng đọc được trong phần này => viết luật ra => thảo luận và đồng thuận về luật => sau đó mới dán nhãn. Chỉ cần dán nhãn thôi. Xóa thì nhanh cho nên chúng ta chưa hành động vội. Cứ dán nhãn để đấy, xóa lúc nào thì xóa.”

### 2. Thế nào là hoàn thành
_(đề xuất Host trong tin Owner gật 02/10 16:14 — Owner chưa tự gõ lại)_
- Mở trang PG Census lọc được mọi bảng, view, hàm, trigger theo 5 nhãn.
- Không còn ô trống (không chắc thì ghi `CHUA-RO`, có lý do).
- Dán sai giá trị thì PG từ chối.

### 3. Chi tiết cần đạt (AI ghi, Host kiểm)
Chỉ đạo Owner — nguyên văn, 02/10/2026:
- “Ý tưởng balo thì tôi nghĩ vẫn dùng được, nó biến từ 1 mớ phức tạp ra những thứ đơn giản để cho con người có thể nhìn, có thể lọc.” ⇒ **giữ hệ balo** (`balo_thuc_the`).
- “ý tưởng tôi nghĩ ra loài, phân tử, nguyên tử.... nghe thì có vẻ hay, nhưng thực tế nó không tiêu chuẩn => Ý tôi là nó không có 1 bộ định nghĩa đủ rõ ràng … cái gì không định nghĩa rõ ràng được thì dễ hiểu không nhất quán, hiểu sai => làm sai hoặc bế tắc.” ⇒ nhãn mới **không dùng** loài/phân tử/nguyên tử; mỗi giá trị phải có câu thử rõ.
- “Vấn đề hiện nay PG. Có nhiều dư án sai lầm như: registries, pivot, count.... trước đây do AI tư vấn (ảo giác) đã viết ra cả đống, nhưng thực tế không dùng đến. Muốn xoá bớt các table nhưng bây giờ phân loại để xoá rất khó khăn.”
- “đề xuất giúp tôi 1 phương án dán nhãn nhãn hiệu hiệu quả, để bẩ cứ AI nào vào đọc được nhanh chóng, con người cũng vậy.”
- “cho Agent tiến hành dán nhãn. Nhưng trước hết phải ghi rõ nguyên tắc nhãn là gì? cách dán thế nào? Sau đó cho codex chẳng hạn dán trong khoảng 1 tiếng là xong nếu có nguyên tắc rõ ràng.”
- “Bạn soạn cho tôi về nguyên tắc dán nhãn mà bạn nghĩ là hợp lý? Có thể giải thích tại sao? Có những việc lâu quá rồi tôi sẽ không nhớ hết.” ⇒ **mỗi luật kèm “vì sao”** (chuyện đã xảy ra).
- “Tôi đưa GPT/Codex có ý kiến. Sau khi đồng thuận thì có thể giao cho Codex thực hiện việc dán nhãn.”
- **16:23 —** “Tuy nhiên vấn đề là. Phần dán nhãn nếu ghi ở repo thì đọc lại sẽ khó. Cái quy định dán nhãn thì tên nằm ở đâu đó ngay trên chỗ dán nhãn. Giống như nguyên tắc bảng hướng dẫn ngay tại hiện trường, chứ bạn làm 1 cuốn hướng dẫn ở trong thư viện thì đọc đến bao giờ mà ai đọc được. Một trong những nguyên tắc áp dụng triệt để là hướng dẫn ngắn gọn ngay tại hiện trường nhé. AI nào vào đấy cũng đọc được và làm luôn. Cái này bạn cũng bổ sung vào đây và bổ sung luôn vào vị trí dán chỗ nào để thống nhất với codex. Còn khi chúng ta chốt nội dung xong thì mới dán ở hiện trường. Giờ bàn trên lý thuyết trước cho nhanh.” ⇒ **L12 + `view.html#bien`**; chưa dán biển nào cho tới khi chốt.
- **16:28 —** “Chúng ta đang chạy 1 phiên nâng cấp PG hiện tại. Chính Claude code cli đang xử lý phim đó nghĩ ra 1 cơ chế rất hay là nó lập 1 cái sổ để ghi DOT, việc này không tự động cập nhật được nhưng giải quyết được rất nhanh vấn đề. Thỉnh thoảng chúng ta vào cập nhật lại. Trước mắt để giải quyết việc bên kia tôi đã đồng ý cho lập sổ. Bạn đồng bộ luôn với phần ở bên này để tránh mỗi bên nói 1 kiểu.” ⇒ **`view.html#so-dot`** (S1–S3) + Q10. Việc này **không ghi gì** vào `work/vps1-up-grade` (đang có RUN chạy).
- **16:44 —** (kèm ý kiến GPT, xem P01) “Đây là ý kiến của GPT. Mục tiêu là nhìn nó đơn giản, nhưng tôi hiểu được thành các nhóm theo kiểu mà các ai sẽ hiểu. Các bạn hiểu thường là phức tạp, nhưng có nguyên tắc. Tôi thì thích nhìn cái gì đơn giản để nhìn cái trong 30 giây là nhận ra vấn đề. Bạn dung hòa giữa 2 nguyên tắc này để làm làm sao không tạo ra 1 concept mới. Nói 1 cách khác, mô tả lại nguyên tắc của các bạn tell me nguyên tắc dễ hiểu để con người nhìn cái hiểu ngay.” · “Các bạn thống nhất đồng thuận rồi chuyển nguyên tắc dán nhãn và phân loại lên đúng hiện trường, giao cho codex xử lý phần còn lại (dán nhãn)” ⇒ **không thêm khái niệm**: cùng 5 nhãn, người đọc thành 5 câu hỏi + màn “Balo theo khối” + 4 nguyên tắc (`view.html#tem`, `#man-30s`, `#nguyen-tac`); D07.
- **Làm rõ §0.2 (Host, theo P01):** “không còn ô trống” áp cho 4 nhãn đầu; nhãn thứ 5 (KẾT LUẬN) để trống cho tới khi Owner quyết theo khối.

Host ghi (kỹ thuật, chờ hội đồng chốt):
- HTML chính: `view.html` = **luật nhãn v1.0, đã đồng thuận 02/10**. Nền trắng chữ tối.
- Hai nơi, hai thời kỳ, không song song: **trước đồng thuận** luật = `view.html`; **sau đồng thuận** luật = **biển tại hiện trường** (D05 · vị trí + nội dung ở `view.html#bien`), repo chỉ còn là hồ sơ lý do; trong đó danh sách giá trị hợp lệ = một bảng từ điển trong PG (ô nhãn chỉ nhận giá trị có trong từ điển) + một dòng “Luật nhãn” trong mục Reports. Bảng từ điển được tạo trong RUN theo lệnh Owner 16:44 “chuyển … lên đúng hiện trường” (D07). **CHƯA CƯỠNG CHẾ** cho tới khi RUN bật ràng buộc xong.
- Ghi nhãn chỉ qua DOT sẵn có (`dot-balo-reconcile`, `dot-pg-atomic-apply`) theo DROOT26; thiếu thì nâng DOT, không SQL tay.
- Nhãn `COMMENT ON` cũ (07–08/2026) là **nguồn chép** KHỐI và là hồ sơ; không sửa, không viết thêm.
- Tài liệu cũ phải đọc trước khi soạn PROMPT (VPS, chỉ đọc): `docs/BAN-DO-HE-THONG-20260729.md` · `docs/KE-HOACH-XOA-20260801.md` · KB `knowledge/dev/laws-new/pg-read-pg/balo-thuc-the-quy-dinh.md` (v1.9).

### Vòng trước
- — Việc mới.

## Quyết định Owner
- D01 · 2026-10-02 · **Mở việc `work/pg-nhan-balo/`.** Host xin phép đủ 4 ý: tạo 1 thư mục việc + `COLLAB.md` + `view.html` chứa luật · vì đây là nơi duy nhất GPT/Codex/Claude cùng đọc-ghi-góp ý có mã, Owner xem ở Task html view · đặt ở repo `incomex-workspace` · không làm thì luật nằm trong chat, GPT/Codex không đọc được. Owner: “Đồng ý cho các bạn mở việc mới này.” Vai theo đề xuất trong cùng tin: Host Claude Chat · Reviewer GPT Chat + Codex · executor Codex. JEV `gen-dec-1790932378-wOfBs0WxuXrUsc1KJfS7`: nháp ở repo 0,89 (conf 0,87). Áp: SAME_COMMIT.
- D02 · 2026-10-02 · **Chỉ dán nhãn.** Owner: “Chỉ cần dán nhãn thôi. Xóa thì nhanh cho nên chúng ta chưa hành động vội.” Việc này không có bước tắt/xoá/dời.
- D03 · 2026-10-02 · **Trình tự:** nơi viết luật → viết luật → thảo luận, đồng thuận → dán nhãn.
- D04 · 2026-10-02 · **Giữ balo, bỏ loài/phân tử/nguyên tử** (nguyên văn ở §0.3).
- D05 · 2026-10-02 · **Biển hướng dẫn tại hiện trường** (nguyên văn 16:23 ở §0.3): quy định dán nhãn nằm ngay trên chỗ dán, ngắn gọn, AI nào vào cũng đọc được và làm luôn; chốt nội dung xong mới dán biển, hiện bàn lý thuyết. ⇒ luật L12 + `view.html#bien` (4 biển B1–B4, 2 dòng trỏ T1–T2, kèm mẫu chữ để thống nhất với Codex). JEV `gen-dec-1790933083-hklqESeJ5dX1weHO6qFD`: biển chỉ ghi việc phải làm 1,00 · biển trên bảng balo 0,79 · từ điển 0,86 · `--help` DOT 0,70 · trỏ ở AGENTS.md VPS 0,74 · trang Reports 0,58 · ghi chú từng cột 0,49 (Host: gộp vào biển cổng) · trỏ từng vật 0,20 (Host: không làm đợt này) · giữ repo làm bản gốc 0,07. Áp: SAME_COMMIT.
- D06 · 2026-10-02 · **Khớp với sổ DOT của `work/vps1-up-grade`** (nguyên văn 16:28 ở §0.3): Owner đã đồng ý cho Claude Code CLI lập sổ ghi tay cho DOT ở việc nâng cấp; việc này phải nói cùng một kiểu. ⇒ `view.html#so-dot`: balo = vật trong PG (máy cập nhật), sổ DOT = lệnh DOT (ghi tay); S1 không chép chéo · S2 dùng chung từ · S3 lệnh dán nhãn ghi vào chính sổ đó. **Host chưa đọc được sổ** (chưa có trên repo, không nằm trên VPS1) nên chưa khớp chữ cụ thể — Q10. JEV `gen-dec-1790933410-jhPXPD6f2iyiDDBXxd9K`: tách riêng + dùng chung từ 1,00 · tự đặt định dạng sổ khi chưa đọc 0,19. Áp: SAME_COMMIT.
- D07 · 2026-10-02 · **Đồng thuận → lên hiện trường → giao Codex dán** (nguyên văn 16:44 ở §0.3). Owner yêu cầu dung hoà “AI phức tạp có nguyên tắc” với “người nhìn 30 giây” mà **không tạo concept mới**, rồi chuyển nguyên tắc lên đúng hiện trường và giao Codex. ⇒ luật v1.0; lệnh này bao gồm việc đặt các biển B1–B4 (có bảng từ điển B2 và view `v_balo_theo_khoi`) đã nêu ở `view.html#bien`. JEV `gen-dec-1790934547-C0EausEz5U9gqVydgu8c`: cùng 5 nhãn dưới dạng câu hỏi + màn theo khối 1,00 · giá trị riêng “Không đo được” 1,00 · dùng lại cổng DOT, không viết DOT mới 0,91 · READY ngay 0,73. Áp: SAME_COMMIT.

## Owner cần quyết
- —

## Câu hỏi mở — Host mời Reviewer trả lời bằng P
- Q01 · `view.html#C4` · Ngưỡng **Tự quay** (lượt ghi ≥ 10 lần số dòng) có đúng không; có bắt nhầm bảng hàng đợi/phiên đăng nhập không.
- Q02 · `view.html#C2` · Thứ tự 7 câu thử VAI của bảng; ranh giới **Danh mục** ↔ **Dữ liệu**.
- Q03 · `view.html#C1` · Một vật một KHỐI: vật mang 2 mã hệ (vd `HE-REGISTRY, HE-QT001`) lấy dòng “HE (so huu)”. QT001 có nên là khối chủ riêng không.
- Q04 · `view.html#cot` · Nhãn nằm ở cột nào của balo; quy đổi nhãn đang có trên 654 hàm.
- Q05 · `view.html#C5` · DÍNH đo bằng `pg_depend` + khoá ngoại + trigger + quét thân hàm đã đủ chưa; tham chiếu từ ngoài PG (Nuxt, DOT, cron) xử lý thế nào.
- Q06 · `view.html#C4` · View và hàm ghi “Không đo được”, hay bật bộ đếm lượt gọi hàm (đổi cấu hình production ⇒ phải Owner gật riêng).
- Q07 · `view.html#C4` · Ảnh chụp bộ đếm 01/08 ở `/opt/incomex/evidence/del1g-20260801/` có đủ 385 bảng không (Host **chưa** mở file kiểm).
- Q08 · `view.html#bien` · Sáu vị trí B1–B4, T1–T2 có đúng là chỗ Codex/agent thật sự đi qua khi dán và khi đọc nhãn không; thiếu cửa nào; khuôn report hiện có đúc được trang “Luật nhãn” (B4) mà không viết mã không.
- Q09 · `view.html#bien` · Mẫu chữ biển cổng B1 (8 dòng) và biển công cụ B3 (3 dòng): Codex đọc xong có làm được ngay không, thừa/thiếu dòng nào. Có nên thêm một dòng trỏ vào nhãn văn cũ của từng vật không (Host: không làm đợt này).
- Q10 · `view.html#so-dot` · **Gửi executor/Host của `work/vps1-up-grade`:** sổ DOT nằm ở đâu (máy + đường dẫn), gồm cột nào, dùng chữ gì cho ghi/đọc và cho nhóm; ba điểm nối S1–S3 có vướng gì không; sổ mới thay hay bổ sung cho bảng `dot_tools` cũ. Host đọc được sổ thì tự khớp chữ ở C1/C3, Owner không phải chép.
- **Trạng thái Q · 02/10 16:46:** Q05, Q06 đóng bởi P01 (DÍNH chỉ đo trong PG, 0 không có nghĩa được xoá; không đổi cấu hình PG). Q01–Q04, Q08–Q09: Reviewer không phản đối ⇒ giữ như v1.0. Q07: Host đã mở file — 352 dòng schema `public`, bảng ngoài `public` ở `ngoai_*.psv`; nghĩa 7 cột số giao executor xác định (PROMPT §5.5). Q10: executor kiểm khi chạy (PROMPT B9).

## Ý kiến (P)
- P01 · GPT Chat (Reviewer) · 02/10 · Owner chuyển qua chat Claude 16:44 (GPT không ghi repo lượt này) · Based_on `b2d859d` (luật v0.3) · Scope `view.html` N5/C4/C5/L10/`#so-dot`. Đánh giá: “đúng hướng và có thể chốt”, sửa 4 điểm; “với bốn chỉnh sửa trên thì không cần thêm một vòng thiết kế nguyên tắc nữa; Codex có thể bắt đầu”. Phản hồi Host:
  - (1) KẾT LUẬN chỉ Owner quyết, máy tuyệt đối không quyết bỏ; 5 giá trị giữ / đóng băng / chờ bỏ / đã tắt / đã dời kho → **ACCEPTED**. Bỏ “máy suy”, bỏ “Bỏ được / Còn dính”; Codex để trống; Owner quyết theo khối (C6, L09).
  - (2) SỐNG: suy luận không được thành bằng chứng; không đổi cấu hình PG đợt này → **ACCEPTED** về nội dung; **PARTIAL** về chữ: view/hàm ghi “Không đo được” (sự thật về phép đo) thay vì `CHUA-RO`, để số `CHUA-RO` chỉ đếm chỗ cần rà; bảng thiếu mốc 01/08 → `CHUA-RO` (C4, L04). JEV 1,00.
  - (3) `DÍNH = 0` không có nghĩa được xoá → **ACCEPTED** (C5, L08, biển B1 dòng 4).
  - (4) DOT 100%, một sổ DOT dùng chung → **ACCEPTED** (L10, S3; RUN này dùng lại cổng DOT sẵn có, không viết DOT mới).
  - (5) “2 sổ + 1 góc nhìn”: khối không là sổ thứ ba → **ACCEPTED**: bỏ “tình trạng khối” khỏi từ điển; khối = view `v_balo_theo_khoi` + trang `report-balo-khoi`.
  - (6) Lộ trình khoanh → tắt → dời kho → xoá giữ nguyên, xoá cần lệnh Owner riêng → **ACCEPTED**, ngoài phạm vi việc này (D02).
  - Prompt GPT soạn cho Codex: nhập nguyên ý vào `PROMPT.md`, thêm phần Host input gate (phạm vi ghi, bẫy cổng DOT, mốc đo, hồi quy).
- P02 · Claude Chat (Host) · 02/10 · `PROMPT.md` RUN_ID `PGNB-LABEL-20261002-01`. **§0.3: đã đối chiếu** từng dòng: giữ balo ✓ · không dùng loài/phân tử/nguyên tử (cột `lop` để trống) ✓ · mỗi luật có “vì sao” ✓ · biển tại hiện trường, chốt xong mới dán ✓ · khớp sổ DOT, không sổ thứ hai ✓ · chỉ dán nhãn, không tắt/xoá ✓ · không concept mới ✓. Không giao executor tự chọn tên/đích: tên cột, bảng, view, trang đã chốt trong PROMPT §2. Scope đủ đồng thuận theo A5: không còn P `OPEN`/`OWNER`.

## RUN
- READY@098d3bf37aa646b884d5759d3082b3e1254f797f · RUN_ID `PGNB-LABEL-20261002-01` · Host Claude Chat đặt 02/10/2026 16:58 +07 · căn cứ: P01 (Reviewer GPT: không cần thêm vòng thiết kế), P02 (§0.3 đã đối chiếu), D07 (Owner lệnh giao Codex). Đây chưa phải RUN: chờ Owner.
- Lệnh RUN cho Codex: `WS work/pg-nhan-balo · Agent · RUN PGNB-LABEL-20261002-01 · đọc AGENTS.md → work/pg-nhan-balo/COLLAB.md → PROMPT.md`

## Con trỏ
- HTML chính (Owner View): `view.html` · link `https://vps.incomexsaigoncorp.vn/knowledge/modules?task=pg-nhan-balo`
- Trang đang chạy: `https://vps.incomexsaigoncorp.vn/reports/report-pg` + `/reports/report-balo-{table,view,function,trigger}`
- JEV đã tham khảo (A5): `gen-dec-1790931810-jSfOPmfQrsETIAx8Nlwg` (nhãn ở cột balo 0,99 · đo 62 ngày 0,99 · gật theo khối 0,99) · `gen-dec-1790931831-1uu4vrTNm7gIIV6S3RlP` (thử 7 VAI trên 9 bảng mẫu: 9/9 rõ, conf ≥ 0,94) · `gen-dec-1790932378-wOfBs0WxuXrUsc1KJfS7` (từ điển PG 1,00 · kết luận suy từ khối 0,98) · `gen-dec-1790933083-hklqESeJ5dX1weHO6qFD` (vị trí biển — D05).
- Cửa vào cho Reviewer: `WS work/pg-nhan-balo · Review · luật nhãn PG v1.0 + KQ · đọc AGENTS.md → work/pg-nhan-balo/COLLAB.md → view.html · ghi P`
- PROMPT: `PROMPT.md` · RUN_ID `PGNB-LABEL-20261002-01` · Executor Codex · READY: xem mục `## RUN`.
