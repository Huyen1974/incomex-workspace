# PROMPT — copy-web-incomexsaigoncorp-vn · MỘT RUN từ đầu tới trang thử
RUN_ID: CWEB-E2E-20261002-01
Trạng thái: xem `COLLAB.md` của việc. Chỉ chạy khi ở đó có dòng READY mang đúng SHA commit cuối chạm tệp này **và** Owner đã dán lệnh RUN.
Executor_Surface: Codex (máy Owner + đường tới VPS1 đã nghiệm thu của Codex).
Write_Path: repo `incomex-workspace` qua cổng `workspace_*`, chỉ trong `work/copy-web-incomexsaigoncorp-vn/`, commit tiền tố `[Codex]` · VPS1: mọi thay đổi chỉ qua DOT/script-wrapper · hồ sơ việc `/opt/incomex/work/copy-web-incomexsaigoncorp-vn/` (tạo bằng `mkdir`).
§0.3: đã đối chiếu (Host, 02/10/2026 20:45).

## 0. Cổng vào — chỉ đọc; sai một điều thì DỪNG, không đổi gì
1. Đọc `AGENTS.md` → `COLLAB.md` của việc (Bảng + §0) → tệp này. READY khớp SHA.
2. `work/vps1-up-grade/COLLAB.md` đã có KQ **G7 XONG** (VPS1 đang chạy bộ mới: Directus 12.4.1 · Nuxt 4.5.2 · PG 18.6). Chưa có ⇒ DỪNG.
3. Ghi `STARTED@<RUN_ID> <UTC> · executor=codex` vào `COLLAB.md` + sửa 3 dòng Bảng (■ Đang làm · ➡ Kế tiếp · `cập nhật`).

## 1. Đầu bài — lời Owner, không diễn giải thêm
- Hợp đồng với bên làm web cũ hết hạn; không làm gì thì `https://incomexsaigoncorp.vn/` bị ngừng. Cần **giải pháp trung gian, làm tạm**: web chạy trên hệ PG · Directus · Nuxt của Incomex.
- “chỉ cần vẽ lại cho gần giống là được. Không cần giống tuyệt đối” · “chỉ tính copy giao diện và tính năng” · phần nhúng: “nhúng lại ở site mới là xong” · “có thể chưa sửa gì cũng được”.
- “100% dùng DOT hết với PG và Directus, thiếu viết thêm.”
- Làm lại toàn bộ web là việc khác, để sau. **Không cải tiến, không sửa nội dung.**

## 2. Đã biết về site cũ (Host điều tra 02/10 — kiểm lại nhanh, lệch thì ghi vào KQ)
- WordPress + giao diện Flatsome do bên cũ vận hành. `wp-json/wp/v2` đọc được: 5 trang · 14 bài · 9 chuyên mục · 16 thẻ · 73 ảnh. 29 địa chỉ nội bộ, đều 200. Trang `/project-post/…` (đơn hàng) không có trong `wp-json`, chỉ lấy từ HTML.
- Phần nhúng: khung Google Maps (chân trang) · khung YouTube (`/gioi-thieu/`) · liên kết Lark wiki (bài “các đơn hàng mới nhất”, `/category/don-hang/`) · liên kết menu “Giáo dục” sang cổng giaoduc. Tính năng: form liên hệ ở `/lien-he/`.
- Máy chủ bên cũ chặn truy cập tự động từ địa chỉ trung tâm dữ liệu ⇒ chụp từ máy Owner.
- Hệ mình: bộ bảng web Agency OS có sẵn, đang trống: `posts`, `categories`, `pages` (+ quan hệ khối tới `block_html`), `seo`, `redirects`, `forms`, `inbox`. DOT nội dung có sẵn: `dot-content-create|update|delete|list`, `dot-permission-ensure`.

## 3. Việc — làm liền một mạch, không xin duyệt giữa chừng
**A. Chụp tối thiểu** (từ máy Owner · chỉ GET · ≤ 1 yêu cầu/giây · chạy tiếp được): JSON `pages|posts|categories|tags|media` (`per_page=100`, `_embed=1`) · HTML của 29 địa chỉ (từ liên kết trang chủ + trường `link`) · 73 tệp ảnh đang dùng · ảnh chụp màn hình 6 trang mẫu rộng 1366 làm chuẩn so. Lưu ở hồ sơ việc `chup/` + `MANIFEST.json` (sha256).

**B. DOT trước, thao tác sau** (DROOT26/27/29/35): kê DOT dùng được trên bộ sau G7. Thiếu thì viết/nâng rồi dùng chính nó: nạp hàng loạt từ `chup/` (chạy lại không trùng, dry-run mặc định) · nạp ảnh vào Directus files · tự kiểm trang · đưa Nuxt lên (dùng đúng DOT/script đưa Nuxt lên mà VPSUP G7 bàn giao; không có thì bọc lệnh chính thức thành script-wrapper). Mỗi DOT mới có `--help`, dry-run, verify, rollback, mã thoát.

**C. Nạp vào bảng CÓ SẴN** — 0 bảng mới, 0 cột mới, chép nguyên chữ:
- 14 bài + các trang đơn hàng `/project-post/…` → `posts` (title · slug giữ nguyên · summary · content · date_published · category = một chuyên mục chính · image · status published). Đơn hàng thuộc chuyên mục `don-hang`.
- chuyên mục đang dùng → `categories` (title, slug).
- 5 trang → `pages` (permalink giữ nguyên) + nội dung vào `block_html`, nối theo đúng quan hệ khối của `pages` đang khai trong Directus.
- tiêu đề/mô tả tìm kiếm → `seo`.
- 73 ảnh → Directus files (một thư mục riêng); đường dẫn ảnh trong nội dung đổi sang tệp mới; `posts.image` = ảnh đại diện.
- Nội dung là HTML phần thân bài/trang đã gỡ lớp và thuộc tính riêng của giao diện cũ khi chúng không còn tác dụng.

**D. Vẽ lại gần giống** — lớp Nuxt mỏng, **chỉ thêm tệp**:
- Một layout riêng: đầu trang (logo + menu 8 mục như cũ) · chân trang (tên công ty, địa chỉ, điện thoại, email, bản đồ). CSS viết mới, nhìn theo 6 ảnh chuẩn: bố cục, màu chủ đạo, thứ tự khối. **Không chép CSS/JS/khuôn HTML giao diện của bên cũ.** Không thêm thư viện hay gói mới vào Nuxt.
- Các trang dưới tiền tố `/w/`: `/w/` (trang chủ: giới thiệu + dịch vụ + “đơn hàng đang tuyển” + tin mới — hai khối sau lấy tự động từ `posts`) · `/w/<permalink trang>` · `/w/category/<slug>` · `/w/<slug bài>` · `/w/project-post/<slug>`. Liên kết nội bộ sinh theo tiền tố đang phục vụ, để khi tên miền chính trỏ gốc `/` vào các trang này thì địa chỉ cũ giữ nguyên.
- Không dựng: tìm kiếm, bình luận, đăng nhập, hiệu ứng trượt.

**E. Nhúng lại — bê nguyên nguồn, không dựng lại:** khung Google Maps · khung YouTube · liên kết Lark wiki · liên kết cổng giaoduc. Nếu chính sách khung của máy chủ phục vụ trang thử chặn hai khung: thêm **đúng hai nguồn** `https://www.google.com` và `https://www.youtube.com` vào `frame-src` của đúng khối máy chủ đó, qua script-wrapper có sao lưu + kiểm cấu hình + rollback; không mở kiểu `*`.
- **Form liên hệ** (tính năng, không phải phần nhúng): dùng khối form + bảng `forms`/`inbox` có sẵn của Agency OS nếu chạy được mà không phải viết quá một tệp; không thì thay bằng khối liên hệ tĩnh (điện thoại · email) và ghi rõ trong KQ.

**F. Đưa lên + trang thử:** đưa Nuxt lên bằng DOT/script ở B · mở quyền **chỉ đọc, chỉ bản đã đăng** cho các bảng dùng tới bằng `dot-permission-ensure`. Trang thử: `https://vps.incomexsaigoncorp.vn/w/`. Không tạo tên miền, không đụng DNS.

**G. Tự kiểm — trình duyệt thật:**
- 29 địa chỉ cũ ↔ địa chỉ `/w/…` tương ứng: đều 200, không liên kết nội bộ chết, ảnh hiện.
- 4 phần nhúng/liên kết hoạt động.
- So ảnh 6 trang mẫu (cũ ↔ mới), rộng 1366; tối đa **một** vòng sửa; khác biệt còn lại ghi mỗi trang một dòng.
- Thử một lệnh DOT thêm bài thử → hiện ở trang chủ + chuyên mục → gỡ bài thử.
- Hồi quy: chạy lại bộ kiểm trang hiện có của hệ sau khi đưa lên — trang đang chạy không đổi.
- 6 ảnh ghép ≤ 250 KB → repo `assets/so-anh/01.jpg … 06.jpg`, nhúng vào `view.html` mục `#so-anh`; bổ sung số liệu vào `#kiem-ke`.

**6 trang mẫu (chốt cứng):** `/` · `/gioi-thieu/` · `/lien-he/` · `/category/don-hang/` · `/tin-vui-nhat-ban-mo-cua-don-lao-dong-viet-nam-tu-3-2022/` · `/project-post/don-hang-son-nha-cua/`

**H. Bảo vệ + đường lùi** (DROOT29/34): đăng ký tệp và DOT mới vào lớp bảo vệ hiện có · đường lùi một lệnh (trả Nuxt về bản trước + gỡ dữ liệu đã nạp theo danh sách id), đã thử dry-run · đọc bảng đèn, ghi `ĐÈN: n xanh · m đỏ` (không đọc được ⇒ `CHƯA XEM ĐÈN`, không ghi XONG).

## 4. Cấm
- Bảng mới, cột mới. Sửa tệp Nuxt đang chạy (buộc phải chạm một tệp cấu hình ⇒ sửa tối thiểu, ghi diff trong KQ).
- `psql`/SQL/REST/CLI trực tiếp với PG hay Directus — kể cả để đọc. Thiếu DOT thì viết DOT.
- Tự chọn/nâng phiên bản hay thêm thành phần: dùng đúng bộ đang chạy sau G7.
- DNS, tên miền mới, VPS2. Sửa nội dung cũ, kể cả chỗ sai.
- Với site cũ: POST, đăng nhập, `/wp-admin`, `wp/v2/users`, vòng tránh cơ chế chặn.
- Repo công khai: mã giao diện bên cũ, ảnh (trừ 6 ảnh so). Trong `view.html` chỉ điền `#kiem-ke`, `#so-anh`. Trong `COLLAB.md` chỉ ghi STARTED/KQ + 3 dòng Bảng.
- Xoá bất cứ thứ gì ngoài bài thử do chính RUN này tạo.

## 5. Dừng (ghi KQ DỪNG + lý do một dòng) khi
- Cổng vào sai · `COLLAB.md` có `STOP_REQUESTED`/HOLD · trước nhóm thay đổi production đầu tiên phải đọc lại `COLLAB.md` + tệp này (DROOT30).
- Site cũ chặn: nghỉ 5 phút, thử lại tối đa 3 lần, vẫn chặn ⇒ dừng.
- Hồi quy đỏ sau khi đưa lên ⇒ chạy đường lùi rồi dừng. Đèn đỏ do chính RUN này ⇒ chưa XONG.

## 6. Kết thúc
- Ghi vào `COLLAB.md` một dòng `KQ@<RUN_ID> XONG` hoặc `KQ@<RUN_ID> DỪNG · <lý do>` kèm số liệu một dòng (bài · trang · ảnh đã nạp · địa chỉ 200 · DOT mới · commit) + sửa 3 dòng Bảng, cùng commit.
- Trả Owner đúng một dòng: `XONG · https://vps.incomexsaigoncorp.vn/w/` hoặc `DỪNG`.
