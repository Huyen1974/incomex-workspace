# COLLAB — copy-web-incomexsaigoncorp-vn
Tên việc: Trang incomexsaigoncorp.vn chạy trên PG · Directus · Nuxt của mình — nhìn như cũ, cập nhật bằng DOT
Host: Claude Chat · Host_ID: CLAUDE-CWEB-261002-A · Owner giao 02/10/2026

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
Xác nhận User: **ĐÃ XÁC NHẬN** — nguyên văn lời Owner, chat Claude 02/10/2026 17:22: “Bạn mở 1 task: work/copy-web-incomexsaigoncorp.vn lên workspace để chúng ta thảo luận và triển khai nhé.” Owner 17:38 bổ sung: “Đầu tiên là bạn đưa việc này lên workspace, hội đồng có ý kiến. Xong thì hãy làm.” ⇒ **hội đồng chốt chi tiết → Host đặt READY → Owner dán một dòng RUN → Codex làm.** Chưa cho phép: đụng Nuxt/Directus/nginx production trước VPSUP G7 · đổi DNS.

### BẢNG ĐIỀU KHIỂN · cập nhật 2026-10-02 17:50 +07 · Claude Chat (Host) · Owner 17:38: hội đồng chốt chi tiết · PROMPT Gói 1 bản soạn chờ Reviewer
- 🎯 **Mục tiêu — Owner nguyên văn 02/10:** “Tôi muốn 1 mô hình làm copy đúng cái trang Web này về, làm 1 cách đơn giản nhất cho nó giống để chạy tạm.” · “muốn làm sao cho nó giống giống, chạy được đại loại như thế và DOT cập nhật.” · “100% dùng DOT hết với PG và Directus, thiếu viết thêm.” **Vì sao:** đằng nào cũng phải dựng web trên PG/Directus/Nuxt — làm một lần trên đúng nền, nhưng không sa lầy.
- 🏁 **Xong khi** _(đề xuất Host — hội đồng chốt, theo lời Owner 17:38)_: (1) mọi địa chỉ trang cũ mở được trên máy mình, nhìn như cũ — so ảnh 6 trang mẫu; (2) nội dung nằm trong PG qua Directus, **0 bảng mới**; (3) thêm/sửa/gỡ một bài hoặc một đơn hàng bằng **một lệnh DOT**, trang chủ + trang danh mục tự hiện; (4) Owner mở trang thử và gật; (5) tên miền chính trỏ về máy mình — chỉ khi Owner ra lệnh.
- 📍 **Tiến độ:** `✅ mở việc + khảo sát · ■ hội đồng góp ý kế hoạch + PROMPT Gói 1 · ⬜ Gói 1 CHỤP (làm ngay được) · ⬜ Gói 2 DỰNG + trang thử (sau VPSUP G7) · ⬜ Gói 3 ĐỔI TÊN MIỀN (khi Owner muốn)`
- ✅ **Đã xong:** Host khảo sát 02/10 — site cũ là WordPress + giao diện Flatsome, đọc được nội dung qua cổng `wp-json`; hệ mình **đã có sẵn bộ bảng web của Agency OS, đang trống** (`posts`, `pages`, `categories`, `block_html`, `seo`, `redirects`…); đã có DOT nội dung `dot-content-create/update/delete/list`; đã có mẫu nginx “thêm tên miền, dùng chung Nuxt” (cổng giaoduc). JEV `gen-dec-1790936861-60jfdlClmTcwG92wvxsI`: lắp vào khung có sẵn + giữ vỏ cũ 0,98 · ảnh cũ giữ nguyên đường dẫn 0,97 · chụp trước/dựng sau G7 0,40 (không chắc) · **nguy cơ sa lầy 2,97/4** ⇒ ba khoá ở §0.3.
- ■ **Đang làm:** Reviewer GPT Chat rà **một** lượt kế hoạch + `PROMPT.md` Gói 1 (Q02–Q06, mỗi câu kèm đề xuất Host) · chờ P01. Hermes góp ý được, không chặn.
- ⬜ **Còn lại — đúng 3 gói:** **Gói 1 CHỤP** (🤖 Codex, chỉ đọc site cũ, không đụng VPS production): kho chụp + bảng kiểm kê + bộ vỏ + bản dựng thử ngoài máy chủ để chứng minh “nhìn như cũ”. **Gói 2 DỰNG** (🤖 Codex, sau khi `work/vps1-up-grade` G7 XONG): nạp nội dung qua DOT vào bảng có sẵn → lớp Nuxt mỏng → tên miền thử → tự so ảnh → Host nghiệm thu → Owner xem. **Gói 3 ĐỔI TÊN MIỀN** (😊 Owner đổi 2 bản ghi DNS, 🤖 lo chứng chỉ + kiểm).
- ➡ **Kế tiếp:** 😊 Owner dán một dòng cho GPT → GPT ghi P01 vào repo → Host xử lý một lượt + đặt READY → 😊 Owner dán một dòng RUN cho 🤖 Codex → Host nghiệm thu Gói 1.
- ⛔ **Không làm/để sau:** thiết kế lại · tạo bảng PG mới · form liên hệ có máy chủ, tìm kiếm, bình luận, đăng nhập · sửa nội dung cũ/sai trong lúc chép (chép nguyên, sửa sau bằng DOT) · đưa CSS/JS giao diện mua bản quyền hoặc ảnh lên repo công khai · đụng Nuxt/Directus/nginx production trước khi VPSUP G7 xong · đụng DNS khi Owner chưa ra lệnh · đuổi giống từng điểm ảnh.

### 1. Mục tiêu
Owner nguyên văn, chat Claude 02/10/2026 17:22:
1. “Tôi đang để tạo 1 trang Web (chưa muốn bàn lại việc thiết kế) https://incomexsaigoncorp.vn/”
2. “Tôi muốn 1 mô hình làm copy đúng cái trang Web này về, làm 1 cách đơn giản nhất cho nó giống để chạy tạm.”
3. “Lý tưởng nhất sau này là chúng ta để luôn cơ sở dữ liệu PG, rồi dùng luôn Directus. Nhưng hiện tại chưa có nhiều thời gian cho việc đó cho nên muốn làm sao cho nó giống giống, chạy được đại loại như thế và DOT cập nhật.”
4. “Hiện tại thì xây dựng để đối phó gọi là 1 việc cho xong. Nhưng đằng nào chúng ta cũng phải xây dựng => chúng ta có PG/Directus/Nust rồi. Thì làm luôn lại cho nhanh nếu có thể.”

### 2. Thế nào là hoàn thành
Owner nguyên văn 02/10: “làm 1 cách đơn giản nhất cho nó giống để chạy tạm” · “giống giống, chạy được đại loại như thế và DOT cập nhật” · “100% dùng DOT hết với PG và Directus, thiếu viết thêm.”
_(Đích đo được: dòng 🏁 của Bảng — đề xuất Host, hội đồng chốt theo lời Owner 17:38.)_

### 3. Chi tiết cần đạt (AI ghi, Host kiểm)
Chỉ đạo Owner — nguyên văn, 02/10/2026 17:22:
- “(chưa muốn bàn lại việc thiết kế)” ⇒ giữ nguyên giao diện cũ; không mở bàn thiết kế.
- “Bạn nghiên cứu và lên cho tôi 1 kế hoạch làm sao tốn ít thời gian điều hành nhất để chạy việc này. Nếu được thì giao cho Codex có thể tự làm 1 mình cho xong.” ⇒ executor **Codex**; giao theo gói trọn; mỗi gói Owner chỉ một thao tác.
- “100% dùng DOT hết với PG và Directus, thiếu viết thêm.” ⇒ DROOT26/35; thiếu DOT thì viết DOT trước.
- “Tôi không muốn sa lầy vào việc này, cho nên trước mắt thì phải làm cái gì đó đơn giản nhất. Còn sau này khi mọi việc xong thì chúng ta sẽ làm tiếp.”
- “Yêu cầu của việc này là đừng lãng phí những việc chúng ta đang làm, nhưng cũng không sa đà vào việc hiện tại này bởi vì chúng ta đang không có thời gian (tôi không có thời gian)” ⇒ dùng khung có sẵn; không chen vào đường nâng cấp VPSUP.
- **17:38 —** “Đầu tiên là bạn đưa việc này lên workspace, hội đồng có ý kiến. Xong thì hãy làm. Cứ chốt xong thì soạn 1 lệnh ngắn, tất cả những yêu cầu gì với codex thì đưa hết vào trong đó, nó tự đọc, tự làm. Còn chi tiết thì bạn đưa vào trong đó rồi hội đồng quyết luôn. Việc đơn giản có vậy thôi đừng làm khác đi chúng ta làm bao nhiêu việc giống nhau rồi mà” ⇒ **quy trình chuẩn, không biến tấu:** chi tiết nằm ở repo, hội đồng quyết, Owner không duyệt chi tiết; mọi yêu cầu với Codex nằm trong `PROMPT.md`; lệnh dán cho Codex chỉ một dòng.

Host ghi (kỹ thuật — đề xuất Host; hội đồng chốt theo lời Owner 17:38):
- **Tên thư mục:** Owner gõ `…corp.vn`; máy đồng bộ Task View chỉ nhận mã việc `[A-Za-z0-9_-]+` (`scripts/hvu-b2/sync.py` dòng 45) nên dấu chấm bị bỏ qua ⇒ dùng `copy-web-incomexsaigoncorp-vn`.
- **HTML chính:** `view.html` (nền trắng chữ tối).
- **Hướng (Bậc R1: 1 có sẵn → 2 ghép → 3 code mỏng):** lắp nội dung cũ vào **bộ bảng web Agency OS có sẵn, đang trống** — không tạo bảng. Bài viết + đơn hàng → `posts` (đơn hàng = `type` dự án) · chuyên mục → `categories` · trang tĩnh + trang chủ → `pages` + `block_html` · đầu trang/chân trang → 2 dòng `block_html` · tiêu đề/mô tả tìm kiếm → `seo` · địa chỉ cũ đổi (nếu có) → `redirects`. `navigation`, `globals`, `forms`, `inbox`: để sau, khi làm lại giao diện.
- **Giống như cũ bằng cách nào:** giữ nguyên HTML đã dựng sẵn của site cũ (cổng `wp-json` trả HTML hoàn chỉnh) + dùng lại đúng tệp CSS của site cũ; Nuxt chỉ là lớp mỏng bọc vỏ cũ quanh nội dung lấy từ Directus. Địa chỉ trang **giữ nguyên** (`/gioi-thieu/`, `/category/…/`, `/project-post/…/`, `/<tên-bài>/`). Ảnh cũ giữ nguyên đường dẫn `/wp-content/uploads/…` (phục vụ tĩnh, không sửa HTML); ảnh mới về sau vào Directus.
- **DOT:** dùng lại `dot-content-create/update/delete/list`, `dot-permission-ensure`. Dự kiến viết thêm 3: nạp hàng loạt từ kho chụp (chạy lại không trùng) · thêm tên miền vào nginx + chứng chỉ theo mẫu giaoduc · tự kiểm (đếm trang, so ảnh, kiểm liên kết). Danh sách chốt cứng trong PROMPT Gói 2 sau khi có kiểm kê Gói 1.
- **Ba khoá chống sa lầy** (đáp JEV 2,97/4): (K1) “giống” = so ảnh 6 trang mẫu, tối đa **một** vòng sửa, không đuổi từng điểm ảnh; (K2) 0 bảng mới, tối thiểu tệp mới, không sửa tệp Nuxt đang chạy — chỉ thêm; (K3) cắt hẳn form có máy chủ, tìm kiếm, bình luận, đăng nhập, hiệu ứng trượt. Gói 1 phải dựng thử ngoài máy chủ và chứng minh “nhìn như cũ” **trước** khi đụng production.
- **Phối hợp VPSUP (`work/vps1-up-grade`):** bản Nuxt 4.5.2 của G6/G7 đã khoá bytes ⇒ tệp Nuxt thêm vào production trước G7 sẽ mất khi chuyển. Vì vậy Gói 1 không đụng VPS production; Gói 2 chỉ chạy **sau G7 XONG**, dựng thẳng trên Directus 12.4.1 / Nuxt 4.5.2, không phải làm lại. G7 trượt lâu ⇒ Host báo Owner một dòng kèm đề xuất, không tự đổi thứ tự.
- **Bằng chứng khảo sát (Host, 02/10):** trang chủ + `wp-json` đọc trực tiếp (WordPress; kiểu bài `ux-blocks` của Flatsome; Contact Form 7, Yoast, LiteSpeed, MasterSlider); máy chủ site cũ **chặn truy cập tự động sau 2 lượt** từ địa chỉ trung tâm dữ liệu ⇒ Gói 1 chạy từ máy Owner, chậm rãi, ưu tiên `wp-json`. PG `directus`: 47 bảng nhóm web Agency OS, các bảng nội dung 0 dòng. Nuxt: có `pages/[...permalink].vue`, `pages/posts/`. nginx: khối `giaoduc.*` dùng chung Nuxt, chứng chỉ riêng. Menu “Giáo dục” của site cũ đã trỏ sang cổng giaoduc trên VPS — giữ nguyên.
- **Không đưa lên repo công khai:** CSS/JS giao diện Flatsome (đồ mua bản quyền, chỉ dùng cho chính trang này) và ảnh — để ở hồ sơ VPS của việc (`/opt/incomex/work/copy-web-incomexsaigoncorp-vn/`, AGENTS A8). Repo chỉ giữ bảng kiểm kê + tài liệu.
- **Đường lùi:** site WordPress cũ vẫn chạy nguyên, không ai đụng, cho tới khi Owner ra lệnh đổi tên miền (Gói 3); Gói 3 chỉ đổi bản ghi của `@` và `www`, **không đụng bản ghi thư**.
- **Vai:** Host Claude Chat · executor Codex · Reviewer GPT Chat (hội đồng; Hermes góp ý được, không chặn). Theo lời Owner 17:38: hội đồng rà **một** lượt kế hoạch + PROMPT Gói 1 ngay; PROMPT Gói 2 rà một lượt nữa khi đã có kiểm kê.

### Vòng trước
- — Việc mới.

## Quyết định Owner
- D01 · 2026-10-02 · **Mở việc.** Owner nguyên văn: “Bạn mở 1 task: work/copy-web-incomexsaigoncorp.vn lên workspace để chúng ta thảo luận và triển khai nhé.” Host Claude Chat; thư mục dùng `-vn` vì máy đồng bộ không nhận dấu chấm trong mã việc. Áp: SAME_COMMIT.

- D02 · 2026-10-02 17:38 · **Hội đồng chốt chi tiết, rồi làm.** Owner nguyên văn: “Đầu tiên là bạn đưa việc này lên workspace, hội đồng có ý kiến. Xong thì hãy làm.” · “Còn chi tiết thì bạn đưa vào trong đó rồi hội đồng quyết luôn.” ⇒ rút Q01 (xin Owner gật kế hoạch); chi tiết thuộc hội đồng. JEV `gen-dec-1790937672-JB0Hwqh2BTk7ZLHwPt7Q`: soạn PROMPT Gói 1 ngay để rà một lượt 0,85. Áp: SAME_COMMIT.

## Owner cần quyết
- —

## Câu hỏi cho hội đồng (Q) — mỗi câu kèm đề xuất Host
- Q02 · **Hướng:** lắp nội dung vào bộ bảng web Agency OS có sẵn (0 bảng mới) + giữ HTML/CSS cũ, Nuxt chỉ là lớp mỏng. Đề xuất Host: chốt.
- Q03 · **Thứ tự:** Gói 1 chạy ngay (không đụng production) · Gói 2 chỉ sau VPSUP G7 XONG vì bản Nuxt 4.5.2 đã khoá bytes. Nhờ Host VPSUP xác nhận: tệp Nuxt thêm vào production trước G7 có mất khi chuyển không. Đề xuất Host: giữ thứ tự này.
- Q04 · **Gói 1 kèm bản dựng thử + so ảnh 6 trang** (khoá chống sa lầy K1) — giữ hay cắt? Đề xuất Host: giữ; nó lộ rủi ro “không giống” trước khi đụng production.
- Q05 · **Kho chụp ghi vào hồ sơ VPS1** `/opt/incomex/work/<id>/` trong lúc G6 đang chạy — có vướng VPSUP không; Write_Path nào của Codex tới hồ sơ VPS đã nghiệm thu? Đề xuất Host: ghi ở hồ sơ VPS1 (không phải runtime); nếu vướng ⇒ để tạm trên máy Owner, đẩy lên sau G7.
- Q06 · **PROMPT Gói 1:** thừa gì thì cắt, thiếu gì để Codex tự làm một mình thì thêm — sửa thẳng `PROMPT.md` khi chưa READY (A6).

## RUN / KQ
- `PROMPT.md` Gói 1 · RUN_ID `CWEB-G1-CHUP-20261002-01` · **bản soạn** — chưa READY, chưa RUN. Host đặt READY sau khi P01 của hội đồng được xử lý.

## Ý kiến (P)
- — Chưa có.
