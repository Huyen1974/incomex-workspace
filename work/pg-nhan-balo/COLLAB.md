# COLLAB — pg-nhan-balo
Tên việc: Mở balo là biết PG có gì · dùng lại được gì · thừa gì (luật nhãn + dán nhãn)
Host: Claude Chat · Host_ID: CLAUDE-PGNB-261002-A · Owner giao 02/10/2026

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
Xác nhận User: **ĐÃ XÁC NHẬN** — Owner, chat Claude 02/10/2026 16:14: “Đồng ý cho các bạn mở việc mới này.” (sau khi Host xin phép đủ 4 ý — D01). Được phép: viết luật → góp ý → đồng thuận → dán nhãn. **Chưa cho phép tắt/xoá/dời bất cứ vật nào.**

### BẢNG ĐIỀU KHIỂN · cập nhật 2026-10-02 16:15 +07 · Claude Chat (Host) · D01 mở việc
- 🎯 **Mục tiêu — Owner nguyên văn 02/10:** “Mục tiêu là phân loại hiệu quả. cả người và AI có thể dễ dàng biết được là đã có gì? Cần làm gì? Những gì thừa nên xóa đi? Hoặc nên khoanh vùng lại?” · “Chỉ cần dán nhãn thôi. Xóa thì nhanh cho nên chúng ta chưa hành động vội. Cứ dán nhãn để đấy, xóa lúc nào thì xóa.” **Vì sao:** hệ sẽ phức tạp gấp 20–100 lần; không nhìn và lọc được thì Owner không chỉ đạo được.
- 🏁 **Xong khi:** mở trang PG Census lọc được mọi bảng · view · hàm · trigger theo 5 nhãn; không còn ô trống; dán sai giá trị thì PG từ chối. _(đề xuất Host, nằm trong tin Owner gật 02/10)_
- 📍 **Tiến độ:** `✅ khảo sát · ✅ luật nháp v0.1 · ■ GPT + Codex góp ý → đồng thuận · ⬜ PROMPT + READY · ⬜ Codex dán · ⬜ nghiệm thu + Owner xếp khối`
- ✅ **Đã xong:** khảo sát PG thật 02/10 (số liệu ở `view.html#so-lieu`) · luật nhãn nháp v0.1 (`view.html`).
- ■ **Đang làm:** chờ GPT Chat + Codex đọc `view.html` và ghi P (trả lời Q01–Q07 bên dưới).
- ⬜ **Còn lại:** Host hoà giải P → luật v1.0 · PROMPT cho Codex (chỉ dán nhãn, qua DOT) · READY · RUN · nghiệm thu · Owner xếp tình trạng từng khối.
- ➡ **Kế tiếp:** 😊 Owner đưa dòng cửa vào cho GPT/Codex · Reviewer ghi P · Host trả lời P và chốt v1.0 · 🤖 Codex dán sau READY + RUN.
- ⛔ **Không làm:** tắt/xoá/dời/sửa bất cứ vật nào ngoài bảng balo và bảng từ điển · viết thêm vào nhãn `COMMENT ON` cũ · dựng registry/bộ máy mới.

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

Host ghi (kỹ thuật, chờ hội đồng chốt):
- HTML chính: `view.html` = **luật nhãn nháp v0.1**. Nền trắng chữ tối.
- Hai nơi, hai thời kỳ, không song song: **trước đồng thuận** luật = `view.html`; **sau đồng thuận** danh sách giá trị hợp lệ = một bảng từ điển trong PG (ô nhãn chỉ nhận giá trị có trong từ điển) + một dòng “Luật nhãn” trong mục Reports. Tạo bảng từ điển là thứ mới ⇒ Host xin Owner gật riêng khi soạn PROMPT (DROOT16). Trước khi có chốt này: **CHƯA CƯỠNG CHẾ**.
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

## Ý kiến (P)
- — chưa có.

## Con trỏ
- HTML chính (Owner View): `view.html` · link `https://vps.incomexsaigoncorp.vn/knowledge/modules?task=pg-nhan-balo`
- Trang đang chạy: `https://vps.incomexsaigoncorp.vn/reports/report-pg` + `/reports/report-balo-{table,view,function,trigger}`
- JEV đã tham khảo (A5): `gen-dec-1790931810-jSfOPmfQrsETIAx8Nlwg` (nhãn ở cột balo 0,99 · đo 62 ngày 0,99 · gật theo khối 0,99) · `gen-dec-1790931831-1uu4vrTNm7gIIV6S3RlP` (thử 7 VAI trên 9 bảng mẫu: 9/9 rõ, conf ≥ 0,94) · `gen-dec-1790932378-wOfBs0WxuXrUsc1KJfS7` (từ điển PG 1,00 · kết luận suy từ khối 0,98).
- Cửa vào cho Reviewer: `WS work/pg-nhan-balo · Review · luật nhãn PG v0.1 · đọc AGENTS.md → work/pg-nhan-balo/COLLAB.md → view.html · ghi P, trả lời Q01–Q07`
- PROMPT: chưa có (soạn sau đồng thuận).
