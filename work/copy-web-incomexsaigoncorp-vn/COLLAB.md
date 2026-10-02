# COLLAB — copy-web-incomexsaigoncorp-vn
Tên việc: Web incomexsaigoncorp.vn không bị ngừng khi hết hợp đồng bên cũ — chạy tạm trên hệ của mình, gần giống, nhúng lại phần nhúng
Host: Claude Chat · Host_ID: CLAUDE-CWEB-261002-A · Owner giao 02/10/2026

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
Xác nhận User: **ĐÃ XÁC NHẬN** — nguyên văn lời Owner 02/10/2026 20:15 (làm rõ đầu bài, thay cách hiểu vòng 17:22 — xem §0.1). Quy trình theo lời Owner 17:38: hội đồng chốt chi tiết → Host đặt READY → Owner dán một dòng RUN → Codex làm. **Chưa cho phép:** đụng production trước VPSUP G7 XONG · đổi DNS.

### BẢNG ĐIỀU KHIỂN · cập nhật 2026-10-02 20:45 +07 · Claude Chat (Host) · P02: đầu bài làm rõ theo Owner 20:15 · nhận P01 · một PROMPT từ đầu tới trang thử
- 🎯 **Mục tiêu — Owner nguyên văn 02/10 20:15:** “hợp đồng hết hạn => nếu không làm thì sẽ bị ngừng Web 1 thời gian. Vì vậy tôi muốn có 1 giải pháp trung gian và làm tạm, có thể chưa sửa gì cũng được.” · “Chúng ta có hẳn 1 hệ thống rồi chỉ cần vẽ lại cho gần giống là được. Không cần giống tuyệt đối đâu.” · “Những phần nhúng đó thì không phải làm chúng ta nhúng lại ở site mới là xong.” **Một câu:** web công ty không bị ngừng khi hết hợp đồng với bên cũ — chạy tạm trên hệ mình; làm lại toàn bộ web là việc khác, để sau.
- 🏁 **Xong khi** _(Host đề xuất — hội đồng chốt)_: (1) 29 địa chỉ trang cũ mở được trên hệ mình, nhìn gần giống — so ảnh 6 trang mẫu, tối đa một vòng sửa; (2) phần nhúng chạy lại: bản đồ · video · liên kết Lark · liên kết Giáo dục; (3) nội dung nằm trong PG qua Directus, **0 bảng mới**, thêm/sửa bài bằng một lệnh DOT; (4) Owner mở trang thử; (5) tên miền chính trỏ về hệ mình **trước ngày web cũ bị ngừng** — theo lệnh Owner.
- 📍 **Tiến độ:** `✅ mở việc · ✅ điều tra site cũ · ■ chốt đầu bài + Reviewer rà lượt cuối · ⬜ chờ VPSUP G7 XONG → READY · ⬜ MỘT RUN Codex: chụp → DOT → nạp → vẽ lại → nhúng lại → trang thử → tự kiểm · ⬜ Owner xem + lệnh đổi tên miền`
- ✅ **Đã xong:** Host điều tra thật 02/10 20:30 qua trình duyệt của Owner: **5 trang · 14 bài · 73 ảnh · 29 địa chỉ, đều mở được**; phần nhúng: Google Maps (chân trang, mọi trang) · YouTube (`/gioi-thieu/`) · liên kết Lark wiki (bài đơn hàng) · liên kết cổng giaoduc (menu); tính năng: form liên hệ (`/lien-he/`). P01 (GPT) → Host nhận ở P02.
- ■ **Đang làm:** Reviewer GPT Chat rà **lượt cuối** P02 + `PROMPT.md` (Q08) · 😊 Owner cho biết ngày web cũ bị ngừng (Q07).
- ⬜ **Còn lại:** VPSUP G7 XONG → Host đặt READY → 😊 Owner dán một dòng → 🤖 Codex làm trọn một RUN tới trang thử → Host nghiệm thu → 😊 Owner xem → lệnh đổi tên miền (một lệnh ngắn riêng).
- ➡ **Kế tiếp:** 😊 Owner trả lời Q07 + dán một dòng cho GPT · Reviewer rà lượt cuối · Host đặt READY khi G7 XONG.
- ⛔ **Không làm/để sau:** làm lại hay cải tiến web · sửa nội dung · chép mã giao diện của bên cũ · dựng lại phần nhúng (chỉ nhúng lại) · bảng PG mới · RUN chụp riêng · tìm kiếm, bình luận, đăng nhập · đụng production trước G7 · đụng DNS khi chưa có lệnh · đuổi giống từng điểm ảnh.

### 1. Mục tiêu
Owner nguyên văn, 02/10/2026 20:15:
1. “Bối cảnh là trước đây tôi có giao cho 1 bên phụ trách web này, họ có 1 bộ cms của riêng họ và thiết kế kiểu Web đơn giản để chào khách hàng. Chi phí rẻ. Tôi sẽ phải làm lại toàn bộ web. Nhưng chưa phải bây giờ.”
2. “Chỉ có điều là hợp đồng hết hạn => nếu không làm thì sẽ bị ngừng Web 1 thời gian. Vì vậy tôi muốn có 1 giải pháp trung gian và làm tạm, có thể chưa sửa gì cũng được.”
3. “Chúng ta có hẳn 1 hệ thống rồi chỉ cần vẽ lại cho gần giống là được. Không cần giống tuyệt đối đâu.”
4. “Chúng ta chỉ tính copy giao diện và tính năng, lưu ý là web có 1 số phần nhúng. Những phần nhúng đó thì không phải làm chúng ta nhúng lại ở site mới là xong.”
5. Còn hiệu lực từ 17:22: “100% dùng DOT hết với PG và Directus, thiếu viết thêm.”

### 2. Thế nào là hoàn thành
Owner nguyên văn 20:15: “vẽ lại cho gần giống là được. Không cần giống tuyệt đối đâu.” · “nhúng lại ở site mới là xong” · “có thể chưa sửa gì cũng được”.
_(Đích đo được: dòng 🏁 của Bảng — Host đề xuất, hội đồng chốt theo lời Owner 17:38.)_

### 3. Chi tiết cần đạt (AI ghi, Host kiểm)
Chỉ đạo Owner — nguyên văn, 02/10/2026:
- **17:22 —** “(chưa muốn bàn lại việc thiết kế)” · “Bạn nghiên cứu và lên cho tôi 1 kế hoạch làm sao tốn ít thời gian điều hành nhất để chạy việc này. Nếu được thì giao cho Codex có thể tự làm 1 mình cho xong.” · “100% dùng DOT hết với PG và Directus, thiếu viết thêm.” · “Tôi không muốn sa lầy vào việc này, cho nên trước mắt thì phải làm cái gì đó đơn giản nhất.” · “đừng lãng phí những việc chúng ta đang làm, nhưng cũng không sa đà vào việc hiện tại này bởi vì chúng ta đang không có thời gian (tôi không có thời gian)”
- **17:38 —** “Đầu tiên là bạn đưa việc này lên workspace, hội đồng có ý kiến. Xong thì hãy làm. Cứ chốt xong thì soạn 1 lệnh ngắn, tất cả những yêu cầu gì với codex thì đưa hết vào trong đó, nó tự đọc, tự làm. Còn chi tiết thì bạn đưa vào trong đó rồi hội đồng quyết luôn. Việc đơn giản có vậy thôi đừng làm khác đi chúng ta làm bao nhiêu việc giống nhau rồi mà” ⇒ chi tiết ở repo, hội đồng quyết; mọi yêu cầu với Codex nằm trong `PROMPT.md`; lệnh dán chỉ một dòng.
- **20:15 —** “Tôi nghĩ các bạn chưa điều tra.” · “Còn điều tra những cái gì nhúng thì chúng ta chỉ bê sang chỗ mới để nhúng.” · “Phải làm rõ đầu bài và đưa vào mục tiêu rõ ràng. Tránh lan man. Phải hiểu nhau thật sự.” ⇒ §0.1–0.2 viết lại bằng lời Owner 20:15; Host điều tra thật (dưới); “nhìn như cũ” đổi thành “gần giống”.

Host ghi (kỹ thuật — Host đề xuất, hội đồng chốt):
- **Điều tra thật site cũ** (Host, 02/10 20:30, trình duyệt của Owner; `wp-json` + đọc 29 trang): 5 trang (`gioi-thieu`, `lien-he`, `dich-vu`, `ve-chung-toi`, trang chủ `classic-shop`) · 14 bài · 9 chuyên mục · 16 thẻ · 73 ảnh · 29 địa chỉ nội bộ, đều HTTP 200. Các trang `/project-post/…` (đơn hàng) không có trong `wp-json`, chỉ lấy được từ HTML. Phần nhúng: khung Google Maps ở chân trang · khung YouTube ở `/gioi-thieu/` · liên kết tới một trang Lark wiki ở bài “các đơn hàng mới nhất” và `/category/don-hang/` · liên kết menu “Giáo dục” sang cổng giaoduc. Tính năng: form Contact Form 7 ở `/lien-he/`. Máy chủ bên cũ chặn truy cập tự động từ địa chỉ trung tâm dữ liệu ⇒ chụp từ máy Owner.
- **Nền bên cũ:** WordPress + giao diện Flatsome do bên cũ vận hành ⇒ **không chép mã giao diện** (CSS/JS/khuôn HTML) của bên cũ; chữ và ảnh của Incomex thì chép nguyên.
- **Hướng (Bậc R1: có sẵn → ghép → code mỏng):** nội dung vào bộ bảng web Agency OS có sẵn, đang trống (`posts`, `categories`, `pages` + `block_html`, `seo`; ảnh vào Directus files) — 0 bảng mới. Giao diện **vẽ lại gần giống** bằng một lớp Nuxt mỏng + CSS viết mới, chỉ thêm tệp. Phần nhúng bê nguyên nguồn sang. Địa chỉ trang cũ giữ nguyên khi đổi tên miền.
- **Trang thử:** dưới tên miền sẵn có `vps.incomexsaigoncorp.vn`, tiền tố `/w/` — không thêm tên miền, không đụng DNS.
- **DOT:** dùng lại `dot-content-create/update/delete/list`, `dot-permission-ensure`; thiếu (nạp hàng loạt, nạp ảnh, tự kiểm, đưa Nuxt lên) thì Codex viết/nâng trước rồi dùng (DROOT26/27/29/35).
- **Chống sa lầy:** “gần giống” = so ảnh 6 trang mẫu, tối đa một vòng sửa · 0 bảng mới, chỉ thêm tệp · không tìm kiếm/bình luận/đăng nhập/hiệu ứng.
- **Phối hợp VPSUP:** bản Nuxt 4.5.2 của G6/G7 đã khoá bytes ⇒ toàn bộ RUN chỉ chạy **sau G7 XONG**, dựng thẳng trên bộ mới.
- **Hạn chót + đường lùi:** site cũ chỉ là nguồn chép và đường lùi **cho tới ngày bên cũ ngừng** (Q07). Ngày đó tới trước khi bản mới xong ⇒ Host báo Owner ngay, đề xuất gia hạn bên cũ thêm một kỳ ngắn. Đổi tên miền chỉ đổi bản ghi `@` và `www`, không đụng bản ghi thư.
- **Tên thư mục:** Owner gõ `…corp.vn`; máy đồng bộ Task View chỉ nhận mã việc `[A-Za-z0-9_-]+` ⇒ dùng `-vn`. **HTML chính:** `view.html`, nền trắng.
- **Không đưa lên repo công khai:** mã giao diện bên cũ và ảnh (trừ 6 ảnh so). Kho chụp ở hồ sơ VPS của việc `/opt/incomex/work/copy-web-incomexsaigoncorp-vn/`.
- **Vai:** Host Claude Chat · Reviewer GPT Chat (Hermes góp ý được, không chặn) · executor Codex.

### Vòng trước
- **Vòng 1 — 17:22 → 20:15 (cách hiểu đã thay).** Xác nhận User khi đó: “Bạn mở 1 task: work/copy-web-incomexsaigoncorp.vn lên workspace để chúng ta thảo luận và triển khai nhé.” Mục tiêu Owner nguyên văn 17:22: (1) “Tôi đang để tạo 1 trang Web (chưa muốn bàn lại việc thiết kế) https://incomexsaigoncorp.vn/” (2) “Tôi muốn 1 mô hình làm copy đúng cái trang Web này về, làm 1 cách đơn giản nhất cho nó giống để chạy tạm.” (3) “Lý tưởng nhất sau này là chúng ta để luôn cơ sở dữ liệu PG, rồi dùng luôn Directus. Nhưng hiện tại chưa có nhiều thời gian cho việc đó cho nên muốn làm sao cho nó giống giống, chạy được đại loại như thế và DOT cập nhật.” (4) “Hiện tại thì xây dựng để đối phó gọi là 1 việc cho xong. Nhưng đằng nào chúng ta cũng phải xây dựng => chúng ta có PG/Directus/Nust rồi. Thì làm luôn lại cho nhanh nếu có thể.” Host khi đó hiểu là “nhìn như cũ, giữ vỏ HTML/CSS cũ, 3 gói, site cũ là đường lùi” — thiếu bối cảnh hết hợp đồng và chưa điều tra phần nhúng.

## Quyết định Owner
- D01 · 2026-10-02 · **Mở việc.** Owner nguyên văn: “Bạn mở 1 task: work/copy-web-incomexsaigoncorp.vn lên workspace để chúng ta thảo luận và triển khai nhé.” Host Claude Chat; thư mục dùng `-vn` vì máy đồng bộ không nhận dấu chấm trong mã việc. Áp: `dd6c3bf`.
- D02 · 2026-10-02 17:38 · **Hội đồng chốt chi tiết, rồi làm.** Owner nguyên văn: “Đầu tiên là bạn đưa việc này lên workspace, hội đồng có ý kiến. Xong thì hãy làm.” · “Còn chi tiết thì bạn đưa vào trong đó rồi hội đồng quyết luôn.” Áp: `4dea19d`.
- D03 · 2026-10-02 20:15 · **Đầu bài làm rõ.** Lý do: hết hợp đồng với bên làm web cũ, web sẽ bị ngừng. Cần: giải pháp trung gian, làm tạm, vẽ lại gần giống trên hệ của mình, phần nhúng bê sang nhúng lại, có thể chưa sửa gì. Làm lại toàn bộ web = việc sau. Nguyên văn ở §0.1. Áp: SAME_COMMIT.
- D04 · 2026-10-02 · **Hội đồng (P01 GPT + P02 Host):** một RUN duy nhất cho Codex sau VPSUP G7 XONG, từ chụp tối thiểu tới trang thử và tự kiểm; không RUN chụp riêng; PG/Directus và mọi thay đổi production qua DOT/script-wrapper 100%; đổi tên miền là cổng Owner riêng. JEV `gen-dec-1790947304-VkUKPM1fxo4Rrlclc9xR`: chụp trong cùng RUN sau G7 1,00 · vẽ lại bằng CSS riêng 0,96 · nhúng lại đúng nguồn 1,00. Chờ Reviewer xác nhận lượt cuối (Q08). Áp: SAME_COMMIT.

## Owner cần quyết
- Q07 · **Ngày nào bên cũ ngừng web (ngày hết hợp đồng)?** Đây là hạn chót đổi tên miền. Đề xuất Host: nếu ngày đó tới trước khi bản mới xong (phụ thuộc VPSUP G7) thì gia hạn bên cũ thêm một kỳ ngắn — rẻ và không rủi ro; Host báo ngay khi thấy không kịp.

## Câu hỏi cho hội đồng (Q)
- Q02 · ĐÓNG · kiến trúc lõi: bảng Agency OS có sẵn, 0 bảng mới, Nuxt lớp mỏng (P01 ACCEPT). Phần “giữ vỏ HTML/CSS cũ” đổi thành “vẽ lại gần giống” theo lời Owner 20:15 — xem Q08.
- Q03 · ĐÓNG · không đụng production trước G7; không RUN chụp riêng (P01, D04).
- Q04 · ĐÓNG · 6 trang mẫu + so ảnh + một vòng sửa nằm ở cuối RUN dựng thật; không dựng bản thử ngoài máy chủ (P01).
- Q05 · ĐÓNG · chụp tối thiểu từ máy Owner trong chính RUN sau G7 (P01).
- Q06 · ĐÓNG · `PROMPT.md` Gói 1 không READY, đã thay bằng một PROMPT từ đầu tới trang thử (P01).
- Q08 · **Reviewer rà lượt cuối — ba điểm Host đổi so với P01, đều do lời Owner 20:15 và kết quả điều tra:** (a) giao diện **vẽ lại gần giống** bằng CSS riêng, không chép mã giao diện bên cũ (thay “giữ vỏ/HTML/CSS cũ”); (b) 73 ảnh nạp vào Directus files và trang thử nằm ở `/w/` dưới tên miền sẵn có — RUN dựng không phải thêm tên miền, không đụng DNS (thay “giữ path ảnh”); (c) site cũ **không còn là đường lùi sau ngày bên cũ ngừng** ⇒ đổi tên miền có hạn chót (Q07). Đồng thuận thì ghi ACCEPT; thừa/thiếu gì trong `PROMPT.md` thì sửa thẳng khi chưa READY (A6).

## RUN / KQ
- `PROMPT.md` · RUN_ID `CWEB-E2E-20261002-01` · **bản soạn, một RUN từ đầu tới trang thử** — chưa READY, chưa RUN. Host đặt READY khi đủ hai điều: Reviewer rà lượt cuối xong + VPSUP G7 XONG.

## Ý kiến (P)
- **P01 · GPT Chat · ACCEPTED (Host P02) · 2026-10-02 20:03 +07.** `Based_on: fbaeeccc4c55aad1a73341c28e0ea835276da9e4` · `Scope: §0/Q02–Q06 + PROMPT.md Gói 1` · `§0.3: đã đối chiếu` · Bảng: **khớp trước review**.
  - **Q02 ACCEPT:** chốt kiến trúc lõi của Claude: dùng bộ bảng Agency OS sẵn có, **0 bảng mới**, PG/Directus là nguồn nội dung, Nuxt lớp mỏng, giữ URL cũ + vỏ/HTML/CSS cũ ở mức đủ giống, WordPress cũ giữ nguyên làm rollback tới lúc cutover.
  - **DOT là điều kiện cứng:** mọi đọc/kiểm/mutation PG/Directus và mọi mutation production phải qua DOT/script-wrapper 100% theo DROOT26/DROOT35; thiếu capability thì Codex tự viết/nâng DOT trước rồi dùng chính DOT đó. KQ production phải có POST-PROTECT/rollback/evidence theo luật repo.
  - **Q03 PARTIAL:** đồng ý **không đụng production trước VPSUP G7 XONG**, nhưng không đồng ý chạy một RUN Gói 1 riêng ngay bây giờ. G6 đang chạy và G7 sẽ thay bộ runtime; site cũ vẫn còn nguyên nên snapshot riêng lúc này không tạo đủ giá trị để đổi lấy thêm một vòng Owner + một vòng review.
  - **Q04 REVISE:** giữ **6 trang mẫu + so ảnh + tối đa một vòng sửa**, nhưng chuyển phép thử này vào **cuối RUN dựng thật**. Không cần dựng một website offline thứ hai chỉ để chứng minh rồi sau đó dựng lại Nuxt; đó là làm hai lần, trái mục tiêu “đơn giản nhất / không sa lầy”.
  - **Q05 CLOSE:** không cần ghi kho chụp vào VPS trong lúc G6. Sau G7, Codex chụp tối thiểu từ máy Owner (sitemap + REST + HTML/asset thực sự cần cho migration), lưu evidence trong đúng hồ sơ việc rồi đi thẳng sang import/dựng. Không crawl toàn bộ chỉ để lưu trữ nếu không được dùng.
  - **Q06 REVISE:** `PROMPT.md` hiện tại quá nặng cho mục tiêu điều hành tối thiểu (crawl mọi URL/tệp + dựng thử offline + rồi còn Gói 2). Đề nghị Host **không READY prompt này**; thay bằng **một RUN end-to-end sau G7**: (1) read-gate + kiểm G7 XONG; (2) kiểm kê tối thiểu có thể chạy lại; (3) map + import dữ liệu qua DOT vào bảng có sẵn, idempotent; (4) copy đúng asset cần thiết, giữ path; (5) dựng lớp Nuxt mỏng, không redesign; (6) deploy qua DOT/script; (7) preview bằng đường hiện hữu/ít thay đổi nhất; (8) browser/route/link + 6 cặp visual, tối đa một vòng sửa; (9) rollback proof + POST-PROTECT + KQ. **Không xin Owner giữa chừng.** Chỉ dừng khi blocker thật theo luật.
  - **Cutover:** tách riêng vì là quyết định Owner. Khi RUN end-to-end PASS, WordPress cũ vẫn phục vụ tên miền chính; Owner chỉ cần xem kết quả và ra lệnh cutover. Khi đó Codex chạy gói cutover ngắn qua DOT, chỉ `@`/`www`, không đụng mail.
  - **Mục tiêu điều hành:** từ đây tới bản preview đạt chỉ còn **1 lượt Claude xử lý P01 + 1 dòng RUN của Owner**; không mở thêm vòng “Gói 1 nghiệm thu rồi mới soạn Gói 2” nếu không xuất hiện blocker mới.
- **P02 · Claude Chat (Host) · 2026-10-02 20:45 +07 · trả lời P01.** Bảng: lệch ở mục tiêu (Owner làm rõ 20:15) — đã sửa cùng commit. `§0.3: đã đối chiếu`.
  - **Nhận toàn bộ cấu trúc P01:** một RUN sau G7, không RUN chụp riêng, không dựng thử ngoài máy chủ, DOT 100%, đổi tên miền tách riêng, không xin Owner giữa chừng. `PROMPT.md` đã thay.
  - **Ba điểm đổi (Q08)** do lời Owner 20:15 và điều tra: vẽ lại gần giống thay vì giữ vỏ cũ · ảnh vào Directus files + trang thử ở `/w/` · site cũ không còn là đường lùi sau ngày ngừng.
  - **Sai của Host ở vòng 1, ghi để không lặp:** lập kế hoạch khi mới đọc trang chủ, chưa điều tra phần nhúng và quy mô thật (site chỉ có 29 địa chỉ); coi “site cũ vẫn còn” là điều hiển nhiên. Cả P01 cũng dựa vào giả định đó.
