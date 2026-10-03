# COLLAB — copy-web-incomexsaigoncorp-vn
Tên việc: Web incomexsaigoncorp.vn không bị ngừng khi hết hợp đồng bên cũ — chạy tạm trên hệ của mình, gần giống, nhúng lại phần nhúng
Host: Claude Chat · Host_ID: CLAUDE-CWEB-261002-A · Owner giao 02/10/2026

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
Xác nhận User: **ĐÃ XÁC NHẬN** — chốt cuối 03/10/2026 22:30: mục tiêu là **copy web cũ sang VPS của Incomex, chạy giống cũ nhất có thể, rồi chuyển DNS sang để duy trì khoảng thời gian tạm trước khi xây lại toàn bộ**; web cũ dự kiến hết hạn khoảng 1 tuần nữa. Nếu dùng PG/Directus thì dữ liệu phải **tách thành nhóm/collection nhìn tên là biết thuộc web Incomex và có ghi chú rõ để không lẫn về sau**. Quy trình: hội đồng chốt kỹ thuật → Host READY → Owner dán một dòng RUN → Codex làm. **Chưa cho phép:** đổi DNS / chuyển tên miền chính trong RUN dựng trang thử.

### BẢNG ĐIỀU KHIỂN · cập nhật 2026-10-03 22:30 +07 · GPT Chat (Reviewer) · P05/D07: mục tiêu cuối + namespace riêng · READY cũ mất hiệu lực, chờ Host re-READY
- 🎯 **Mục tiêu — Owner chốt cuối 03/10 22:30:** copy toàn bộ web hiện tại từ bên cũ sang VPS của Incomex → kiểm cho chạy/hiển thị **giống cũ nhất có thể** → sau khi kỹ thuật đạt thì chuyển DNS sang VPS để chạy tạm; web cũ còn khoảng **1 tuần** trước khi hết hạn; xây lại toàn bộ web là việc sau. Phần nhúng bê đúng nguồn sang. Nếu dùng PG/Directus, dữ liệu web này phải có namespace/group/ghi chú riêng, không lẫn hệ khác.
- 🏁 **Xong khi:** (1) 29 địa chỉ cũ có bản tương ứng trên VPS, desktop/mobile nhìn giống cũ nhất có thể và không link/ảnh hỏng; (2) Maps · YouTube · Lark · Giáo dục và form liên hệ hoạt động/fallback đúng phạm vi; (3) dữ liệu web tạm nằm trong namespace Directus riêng `web_incomex`, collection/file đều ghi chú rõ nguồn/đích; **không ghi vào collection dùng chung**; (4) trang thử `/w/` PASS và có rollback/protection; (5) bước kỹ thuật tiếp theo chỉ còn cutover DNS theo lệnh Owner.
- 📍 **Tiến độ:** `✅ mở việc · ✅ điều tra site cũ · ✅ nâng cấp máy chủ XONG · ✅ mục tiêu chốt cuối · ✅ PROMPT v02 sửa namespace · ■ Host Claude re-READY · ⬜ Owner dán RUN → Codex làm trọn tới trang thử · ⬜ cutover DNS`
- ✅ **Đã xong:** Host điều tra thật 02/10 20:30 qua trình duyệt của Owner: **5 trang · 14 bài · 73 ảnh · 29 địa chỉ, đều mở được**; phần nhúng: Google Maps (chân trang, mọi trang) · YouTube (`/gioi-thieu/`) · liên kết Lark wiki (bài đơn hàng) · liên kết cổng giaoduc (menu); tính năng: form liên hệ (`/lien-he/`). P01 (GPT) → Host nhận ở P02.
- ■ **Đang làm:** Host Claude **chỉ re-READY** `PROMPT.md` v02 tại commit `39c1d17168a7948ea1498cc25b92739d82760b11`. READY v01 `17f5f0b…` đã vô hiệu vì Owner đổi yêu cầu dữ liệu sau đó. Không mở lại thiết kế/review.
- ⬜ **Còn lại:** Host re-READY → 😊 Owner dán một dòng → 🤖 Codex làm trọn một RUN tới trang thử → Host nghiệm thu → chuyển DNS theo lệnh Owner.
- ➡ **Kế tiếp:** Claude Host đặt READY đúng SHA prompt v02 → 😊 Owner dán RUN → 🤖 Codex chạy tới `https://vps.incomexsaigoncorp.vn/w/` → nghiệm thu → cutover DNS.
- ⛔ **Không làm/để sau:** làm lại hay cải tiến web · sửa nội dung · dựng lại phần nhúng (chỉ nhúng lại) · bảng PG mới · RUN chụp riêng · tìm kiếm, bình luận, đăng nhập · đụng production trước G7 · đụng DNS khi chưa có lệnh · đuổi giống từng điểm ảnh.

### 1. Mục tiêu
Owner chốt cuối, 03/10/2026 22:30 — **đọc trước:** “Mục tiêu cuối cùng là copy được trang Web từ cái cũ sang VPS của chúng ta => sau đó chuyển dns sang. Khoảng độ 1 tuần nữa là web cũ hết hạn => chúng ta sẽ chuyển tạm sang đây rồi xây dựng lại sau. Mục tiêu chỉ cần duy trì cho nó chạy giống với cái cũ nhất có thể.” · “Nếu sử dụng đến PG/Directus thì phải phân rõ nhóm là table/collection ghi chú là của web incomex … để sau này khỏi lẫn lộn.”

Owner trước đó, 03/10/2026 22:07: “tạo ra một trang giống nhất có thể, có thể lấy tạm 1 đường dẫn nào đó để chạy, sau khi ok chúng ta chuyển domain sang VPS của chúng ta. và coi như cho chạy tạm trên VPS này… những cái gì nhúng thì chuyển sang… còn lại thì copy nguyên trang Web đó sang bên chỗ mới… sao cho nhìn giao diện càng giống càng tốt.”

Bối cảnh — Owner nguyên văn, 02/10/2026 20:15 (còn hiệu lực; riêng mức giống nay theo 22:07: “giống nhất có thể”):
1. “Bối cảnh là trước đây tôi có giao cho 1 bên phụ trách web này, họ có 1 bộ cms của riêng họ và thiết kế kiểu Web đơn giản để chào khách hàng. Chi phí rẻ. Tôi sẽ phải làm lại toàn bộ web. Nhưng chưa phải bây giờ.”
2. “Chỉ có điều là hợp đồng hết hạn => nếu không làm thì sẽ bị ngừng Web 1 thời gian. Vì vậy tôi muốn có 1 giải pháp trung gian và làm tạm, có thể chưa sửa gì cũng được.”
3. “Chúng ta có hẳn 1 hệ thống rồi chỉ cần vẽ lại cho gần giống là được. Không cần giống tuyệt đối đâu.”
4. “Chúng ta chỉ tính copy giao diện và tính năng, lưu ý là web có 1 số phần nhúng. Những phần nhúng đó thì không phải làm chúng ta nhúng lại ở site mới là xong.”
5. Còn hiệu lực từ 17:22: “100% dùng DOT hết với PG và Directus, thiếu viết thêm.”

### 2. Thế nào là hoàn thành
Owner nguyên văn 03/10 22:07: “tạo ra một trang giống nhất có thể” · “sau khi ok chúng ta chuyển domain sang VPS của chúng ta” · “nhìn giao diện càng giống càng tốt”. Trước đó, 02/10 20:15: “vẽ lại cho gần giống là được. Không cần giống tuyệt đối đâu.” · “nhúng lại ở site mới là xong” · “có thể chưa sửa gì cũng được”.
_(Đích đo được: dòng 🏁 của Bảng — Host đề xuất, hội đồng chốt theo lời Owner 17:38.)_

### 3. Chi tiết cần đạt (AI ghi, Host kiểm)
Chỉ đạo Owner — nguyên văn, 02/10/2026:
- **17:22 —** “(chưa muốn bàn lại việc thiết kế)” · “Bạn nghiên cứu và lên cho tôi 1 kế hoạch làm sao tốn ít thời gian điều hành nhất để chạy việc này. Nếu được thì giao cho Codex có thể tự làm 1 mình cho xong.” · “100% dùng DOT hết với PG và Directus, thiếu viết thêm.” · “Tôi không muốn sa lầy vào việc này, cho nên trước mắt thì phải làm cái gì đó đơn giản nhất.” · “đừng lãng phí những việc chúng ta đang làm, nhưng cũng không sa đà vào việc hiện tại này bởi vì chúng ta đang không có thời gian (tôi không có thời gian)”
- **17:38 —** “Đầu tiên là bạn đưa việc này lên workspace, hội đồng có ý kiến. Xong thì hãy làm. Cứ chốt xong thì soạn 1 lệnh ngắn, tất cả những yêu cầu gì với codex thì đưa hết vào trong đó, nó tự đọc, tự làm. Còn chi tiết thì bạn đưa vào trong đó rồi hội đồng quyết luôn. Việc đơn giản có vậy thôi đừng làm khác đi chúng ta làm bao nhiêu việc giống nhau rồi mà” ⇒ chi tiết ở repo, hội đồng quyết; mọi yêu cầu với Codex nằm trong `PROMPT.md`; lệnh dán chỉ một dòng.
- **20:15 —** “Tôi nghĩ các bạn chưa điều tra.” · “Còn điều tra những cái gì nhúng thì chúng ta chỉ bê sang chỗ mới để nhúng.” · “Phải làm rõ đầu bài và đưa vào mục tiêu rõ ràng. Tránh lan man. Phải hiểu nhau thật sự.” ⇒ §0.1–0.2 viết lại bằng lời Owner 20:15; Host điều tra thật (dưới); “nhìn như cũ” đổi thành “gần giống”.
- **03/10 22:07 —** “Giờ việc nâng cấp đã xong hết, bạn xác nhận lại ok thì tôi sẽ giao cho codex dựng lại việc này…” ⇒ mức giống = **“giống nhất có thể”**; preview `/w/`; chuyển tên miền sau khi đạt; phần nhúng chuyển nguyên.
- **03/10 22:30 — chốt cuối:** mục tiêu kỹ thuật là **copy web cũ → VPS → kiểm đạt → chuyển DNS**, vì web cũ còn khoảng 1 tuần; xây lại sau. Nếu dùng PG/Directus thì **bắt buộc tách nhóm/table/collection và ghi chú rõ thuộc web Incomex**, không được trộn với dữ liệu hệ khác.

Host ghi (kỹ thuật — Host đề xuất, hội đồng chốt):
- **Điều tra thật site cũ** (Host, 02/10 20:30, trình duyệt của Owner; `wp-json` + đọc 29 trang): 5 trang (`gioi-thieu`, `lien-he`, `dich-vu`, `ve-chung-toi`, trang chủ `classic-shop`) · 14 bài · 9 chuyên mục · 16 thẻ · 73 ảnh · 29 địa chỉ nội bộ, đều HTTP 200. Các trang `/project-post/…` (đơn hàng) không có trong `wp-json`, chỉ lấy được từ HTML. Phần nhúng: khung Google Maps ở chân trang · khung YouTube ở `/gioi-thieu/` · liên kết tới một trang Lark wiki ở bài “các đơn hàng mới nhất” và `/category/don-hang/` · liên kết menu “Giáo dục” sang cổng giaoduc. Tính năng: form Contact Form 7 ở `/lien-he/`. Máy chủ bên cũ chặn truy cập tự động từ địa chỉ trung tâm dữ liệu ⇒ chụp từ máy Owner.
- **Nền bên cũ:** WordPress + giao diện Flatsome do bên cũ vận hành ⇒ theo lời Owner 03/10 22:07 (“copy nguyên trang Web đó sang… càng giống càng tốt”): **được dùng lại khuôn HTML + CSS mặt ngoài của site cũ**, chỉ nạp ở các trang `/w/`, không đưa lên repo công khai; chữ và ảnh của Incomex chép nguyên. (Bản 02/10 cấm chép — đã thay. Giao diện này là đồ mua kèm hợp đồng cũ; khi làm lại toàn bộ web sẽ thay.)
- **Hướng dữ liệu chốt sau yêu cầu 22:30:** **không dùng collection web chung**. Tạo group/namespace riêng `web_incomex` với đúng hai physical collections `web_incomex_content`, `web_incomex_inbox`, note metadata bắt đầu `[WEB_INCOMEX]` và mô tả rõ là bản tạm của `incomexsaigoncorp.vn`; Files folder riêng `web-incomex`. Đây là thay đổi có chủ đích so với quyết định cũ “0 bảng mới”, vì Owner yêu cầu tránh lẫn dữ liệu. Giao diện vẫn lớp Nuxt mỏng tại `/w/`, dùng lại khuôn/CSS mặt ngoài site cũ để giống nhất có thể.
- **Trang thử:** dưới tên miền sẵn có `vps.incomexsaigoncorp.vn`, tiền tố `/w/` — không thêm tên miền, không đụng DNS.
- **DOT:** dùng lại `dot-content-create/update/delete/list`, `dot-permission-ensure`; thiếu (nạp hàng loạt, nạp ảnh, tự kiểm, đưa Nuxt lên) thì Codex viết/nâng trước rồi dùng (DROOT26/27/29/35).
- **Chống sa lầy:** “giống nhất có thể” = so ảnh 6 trang mẫu, tối đa hai vòng sửa · 0 bảng mới, chỉ thêm tệp · không tìm kiếm/bình luận/đăng nhập/hiệu ứng.
- **Phối hợp VPSUP:** bản Nuxt 4.5.2 của G6/G7 đã khoá bytes ⇒ toàn bộ RUN chỉ chạy **sau G7 XONG**, dựng thẳng trên bộ mới. **03/10: VPSUP XONG (P130; việc đã chuyển sang `work/done-tasks/vps1-up-grade/`). Host kiểm trực tiếp: PG 18.6 · Directus 12.4.1 · Nuxt 4.5.2 · 12 container khoẻ.**
- **Collection dùng chung KHÔNG trống** (Host đếm thật 03/10) ⇒ **không đụng và không chấp nhận lẫn nữa**. Web công ty dùng namespace riêng nêu trên; `/posts` và dữ liệu cổng nội bộ phải giữ nguyên trước/sau RUN.
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
- D04 · 2026-10-02 · **Hội đồng (P01 GPT + P02 Host + P03 GPT):** một RUN duy nhất cho Codex sau VPSUP G7 XONG, từ chụp tối thiểu tới trang thử và tự kiểm; không RUN chụp riêng; PG/Directus và mọi thay đổi production qua DOT/script-wrapper 100%; đổi tên miền là cổng Owner riêng. JEV `gen-dec-1790947304-VkUKPM1fxo4Rrlclc9xR`: chụp trong cùng RUN sau G7 1,00 · vẽ lại bằng CSS riêng 0,96 · nhúng lại đúng nguồn 1,00. **Q08 ACCEPT; kỹ thuật khóa tại `PROMPT.md` commit `0fd82bd6a9667c0d18b7899a527400b03b96f81a`.** Áp: SAME_COMMIT.
- D05 · 2026-10-02 · **Ngày bên cũ ngừng web là thông tin tiến độ, không phải gate Owner.** Không bắt Owner trả lời để tiếp tục. RUN bắt đầu ngay sau G7; nếu tại read-gate nguồn cũ đã không còn truy cập được đủ để chụp thì Codex báo blocker, không tự suy đoán nội dung. Áp: SAME_COMMIT.

- D06 · 2026-10-03 22:07 · **Mục tiêu chốt lại + cho làm.** Owner: tạo trang giống nhất có thể, preview trước, sau khi đạt thì chuyển domain sang VPS. Đầy đủ ở §0.1. Áp: `0338c137`.
- D07 · 2026-10-03 22:30 · **Mục tiêu cuối + tách dữ liệu Web Incomex.** Owner chốt: copy web cũ → VPS → DNS; web cũ còn khoảng 1 tuần; đây là bản chạy tạm trước khi xây lại. Nếu dùng PG/Directus phải phân nhóm/table/collection và ghi chú rõ thuộc web Incomex. Hội đồng chốt phương án ngắn nhất: namespace `web_incomex` với `web_incomex_content` + `web_incomex_inbox` + Files folder `web-incomex`; không ghi vào collection dùng chung. D07 thay phần “0 bảng mới/dùng collection chung” của D04/P01/P04. Áp: SAME_COMMIT.

## Owner cần quyết
- — **Không có gate Owner ở giai đoạn dựng trang thử.** Ngày bên cũ ngừng web nếu biết thì chỉ dùng để cảnh báo tiến độ (D05), không chặn RUN.

## Câu hỏi cho hội đồng (Q)
- Q02 · ĐÓNG · kiến trúc lõi: bảng Agency OS có sẵn, 0 bảng mới, Nuxt lớp mỏng (P01 ACCEPT). Phần “giữ vỏ HTML/CSS cũ” đổi thành “vẽ lại gần giống” theo lời Owner 20:15 — xem Q08.
- Q03 · ĐÓNG · không đụng production trước G7; không RUN chụp riêng (P01, D04).
- Q04 · ĐÓNG · 6 trang mẫu + so ảnh + một vòng sửa nằm ở cuối RUN dựng thật; không dựng bản thử ngoài máy chủ (P01).
- Q05 · ĐÓNG · chụp tối thiểu từ máy Owner trong chính RUN sau G7 (P01).
- Q06 · ĐÓNG · `PROMPT.md` Gói 1 không READY, đã thay bằng một PROMPT từ đầu tới trang thử (P01).
- Q08 · ĐÓNG · lịch sử P03; phần CSS đã được Owner 22:07 thay bằng “giống nhất có thể/dùng lại khuôn + CSS mặt ngoài”.
- Q09 · **ĐÓNG · P05 GPT:** dữ liệu web Incomex dùng namespace riêng `web_incomex`, đúng 2 collection + folder file riêng + note metadata; không dùng collection chung.

## RUN / KQ
- ~~READY@17f5f0bf8d4c68134e85a5b1d3b2b1d74194c473 · RUN_ID `CWEB-E2E-20261003-01`~~ — **INVALID** do Owner 22:30 đổi yêu cầu data separation và `PROMPT.md` đã sửa.
- `PROMPT.md` v02 · commit cuối chạm prompt `39c1d17168a7948ea1498cc25b92739d82760b11` · RUN_ID `CWEB-E2E-20261003-02` · **chờ Host Claude re-READY đúng SHA này; không review lại trừ khi prompt bị sửa tiếp.**

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
- **P03 · GPT Chat (Reviewer) · ACCEPT · 2026-10-02 21:02 +07.** `Based_on: 0fd82bd6a9667c0d18b7899a527400b03b96f81a` · `Scope: P02/Q08 + PROMPT.md toàn bộ` · `§0.3: đã đối chiếu` · Bảng: **khớp sau sửa**.
  - Đồng thuận đủ ba thay đổi Q08. Đây đúng là **bản tạm chống gián đoạn**, không phải migrate WordPress hay làm lại website.
  - Phần nhúng chỉ mang nguồn sang nhúng lại; không tái xây Google Maps/YouTube/Lark/Giáo dục. Form liên hệ là tính năng riêng và PROMPT đã giới hạn: ưu tiên khối có sẵn, nếu không gọn thì fallback liên hệ tĩnh.
  - `PROMPT.md` hiện đủ để Codex tự đi từ nguồn cũ → DOT → PG/Directus → Nuxt/CSS mới → nhúng → preview `/w/` → browser/visual test → rollback/protection/KQ; không cần Owner duyệt giữa chừng.
  - **Không thêm bước, không thêm review.** Ngày hết hợp đồng không phải input kỹ thuật bắt buộc; bỏ Q07 khỏi gate. Dependency duy nhất trước RUN là **VPSUP G7 XONG**. Nếu PROMPT không đổi, Host chỉ đặt READY đúng SHA `0fd82bd6a9667c0d18b7899a527400b03b96f81a`.
- **P04 · Claude Chat (Host) · 2026-10-03 22:20 +07 · xác nhận sau nâng cấp + READY.** `§0.3: đã đối chiếu` · Bảng: lệch (mục tiêu Owner 22:07, VPSUP XONG) — đã sửa cùng commit.
  - **Kiểm thật:** VPSUP XONG (P130; KQ G7 XONG 03/10 10:52Z) · đang chạy PG 18.6 · Directus 12.4.1 · Nuxt 4.5.2 · 12 container khoẻ.
  - **`PROMPT.md` đổi ba chỗ so với bản P03 khoá ⇒ SHA mới `17f5f0b`:** (1) cổng vào trỏ `work/done-tasks/vps1-up-grade/` — đường cũ không còn, RUN sẽ dừng oan; (2) bảng web không trống — không đụng dòng của cổng nội bộ, trang vào không gian `/w/…`; (3) theo lời Owner 22:07 “giống nhất có thể… copy nguyên trang Web đó sang”: được dùng lại khuôn + CSS mặt ngoài của site cũ, chỉ nạp ở `/w/`, hai vòng sửa — thay Q08(a). JEV `gen-dec-1791040237-o8xlkbq0mqbkz7gnCAga`: dùng lại khuôn/CSS 0,91 · giữ bảng có sẵn + không gian riêng 0,91.
  - **Không mở vòng review mới** theo lời Owner 22:07 (“bạn xác nhận lại ok thì tôi sẽ giao cho codex”). Reviewer thấy sai thì ghi P và đặt cờ dừng theo DROOT30.
  - **Sai của Host, ghi để không lặp:** hôm 02/10 kết luận “bảng trống” từ số ước lượng thống kê, không đếm thật.
- **P05 · GPT Chat (Reviewer) · OPEN chờ Host re-READY · 2026-10-03 22:30 +07.** `Based_on: 0338c137 + Owner 22:30` · `Scope: mục tiêu + data model + PROMPT.md` · `§0.3: đã đối chiếu`.
  - Mục tiêu cuối đã ghi đúng: **copy web cũ sang VPS → chạy giống cũ nhất có thể → chuyển DNS; khoảng 1 tuần trước khi nguồn cũ hết hạn; xây lại sau**.
  - Phát hiện blocker thiết kế trong READY v01: dùng `posts/pages/categories/forms/inbox` chung sẽ lẫn với cổng nội bộ, trái chỉ đạo mới. Đã sửa prompt v02 sang namespace riêng tối thiểu: `web_incomex_content`, `web_incomex_inbox`, group `web_incomex`, Files folder `web-incomex`, note `[WEB_INCOMEX]`.
  - Đây là **thay đổi bắt buộc theo lời Owner**, không phải mở rộng thiết kế. Hai collection là mức tối thiểu để vừa chứa toàn bộ content vừa tách inbox; chuyên mục/thẻ để field JSON/string, không tạo thêm table.
  - G7 đã XONG và VPS health hiện xanh cho PG/Directus/Nuxt. Không còn blocker kỹ thuật đã biết ngoài việc Host phải re-READY đúng SHA prompt mới. Sau READY, Owner có thể giao Codex ngay; không mở thêm vòng hội đồng.
