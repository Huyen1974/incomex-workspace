# PROMPT — copy-web-incomexsaigoncorp-vn · Gói 1 CHỤP
RUN_ID: CWEB-G1-CHUP-20261002-01
Trạng thái: xem `COLLAB.md` của việc. Chỉ chạy khi ở đó có dòng READY mang đúng SHA commit cuối chạm tệp này **và** Owner đã dán lệnh RUN.
Executor_Surface: Codex trên máy Owner (Mac).
Write_Path: (1) repo `incomex-workspace` qua cổng `workspace_*`, chỉ trong `work/copy-web-incomexsaigoncorp-vn/`, commit tiền tố `[Codex]`; (2) hồ sơ VPS1 `/opt/incomex/work/copy-web-incomexsaigoncorp-vn/` (tạo bằng `mkdir`, AGENTS A8) qua đường tới VPS1 đã nghiệm thu của Codex.
§0.3: đã đối chiếu (Host, 02/10/2026).

## 1. Bối cảnh — đọc trong 1 phút
- Owner muốn chép trang `https://incomexsaigoncorp.vn/` (WordPress + giao diện Flatsome, thuê máy chủ ngoài) về hệ PG · Directus · Nuxt của Incomex: **nhìn như cũ, cập nhật bằng DOT, không thiết kế lại, không sa lầy**. Lời Owner và kế hoạch 3 gói: `COLLAB.md` §0.
- Gói này (1/3) **chỉ chụp + kiểm kê + chứng minh “nhìn như cũ” ngoài máy chủ**. Không đụng production.
- Gói 2 (dựng trên production) chạy sau khi nâng cấp máy chủ (`work/vps1-up-grade` G7) xong, bằng PROMPT khác soạn từ kiểm kê của gói này.
- Hướng đã chọn cho Gói 2 (để biết chụp phục vụ cái gì): nội dung vào bộ bảng web Agency OS có sẵn (`posts`, `pages` + `block_html`, `categories`, `seo`, `redirects`), giữ nguyên HTML đã dựng + CSS cũ, giữ nguyên địa chỉ trang, ảnh cũ giữ nguyên đường dẫn `/wp-content/uploads/…`.

## 2. Giao gì — 4 đầu ra, làm trọn một lượt
**A. Kho chụp** — hồ sơ VPS, thư mục `chup-20261002/`:
- `api/`: JSON thô từ `wp-json`: `wp/v2/types`, `wp/v2/taxonomies`, và với **mỗi** kiểu nội dung công khai có `rest_base` (posts, pages, media, categories, tags, `ux-blocks`, kiểu “đơn hàng” có địa chỉ `/project-post/…`, và mọi kiểu khác liệt kê trong `types`): toàn bộ bản ghi, phân trang `per_page=100`, kèm `_embed=1`.
- `html/`: HTML đã dựng của **mọi** địa chỉ công khai (lấy từ `sitemap_index.xml` + trường `link` trong JSON + menu). Tên tệp theo đường dẫn.
- `tep/`: giữ nguyên cây đường dẫn gốc — mọi tệp `/wp-content/uploads/…` được nhắc tới trong JSON/HTML (kể cả các cỡ trong `srcset`), và CSS/JS/phông mà 6 trang mẫu nạp (kể cả tệp gộp của LiteSpeed).
- `MANIFEST.json`: đường dẫn · URL gốc · mã HTTP · bytes · sha256 · giờ lấy.

**B. Kiểm kê** — điền vào `view.html` mục `#kiem-ke`, một bảng, ít chữ:
- số lượng theo kiểu nội dung và theo chuyên mục · các mẫu địa chỉ · số ảnh + tổng MB;
- **thứ không khớp** hướng đã chọn: form, bản đồ nhúng, slider, video, shortcode chưa dựng, trang mà `content.rendered` khác nội dung trên trang thật;
- liên kết chết;
- đối chiếu trường với cột bảng đích (liệt kê dưới) — trường nào không có chỗ đặt;
- cuối mục: “Host cần chốt cho Gói 2”, tối đa 10 dòng.

**C. Bộ vỏ + bản dựng thử** — hồ sơ VPS:
- `vo/header.html`, `vo/footer.html` (cắt từ HTML trang chủ), `vo/head.json` (thứ tự CSS/JS, lớp của `<body>`).
- `dung-thu/`: 6 trang mẫu ghép từ **vỏ + dữ liệu JSON** (không chép nguyên trang HTML): nội dung bài/trang lấy `content.rendered`; trang danh mục và các khối “đơn hàng mới / tin mới” ở trang chủ sinh từ danh sách JSON theo đúng khuôn HTML cũ. Mọi đường dẫn tệp trỏ vào `tep/` cục bộ; mở được khi không có mạng tới site cũ.
- `cong-cu/`: kịch bản chụp + sinh trang, Python 3 thư viện chuẩn, chạy lại được.

**D. So ảnh** — 6 cặp (trang cũ ↔ bản dựng thử), Chrome không đầu, rộng 1366:
- ghép cạnh nhau thành 6 tệp JPEG ≤ 250 KB, đẩy vào repo `assets/so-anh/01.jpg … 06.jpg`, nhúng vào `view.html` mục `#so-anh`, mỗi trang kèm **một dòng** khác biệt còn lại;
- ảnh gốc đầy đủ để ở hồ sơ VPS `so-anh/`.

**6 trang mẫu (chốt cứng):** `/` · `/gioi-thieu/` · `/lien-he/` · `/category/don-hang/` · `/tin-vui-nhat-ban-mo-cua-don-lao-dong-viet-nam-tu-3-2022/` · `/project-post/don-hang-son-nha-cua/`

**Cột bảng đích (chỉ để đối chiếu — gói này KHÔNG truy cập PG/Directus):**
- `posts`: id, slug, title, summary, type, date_published, image, author, category, content, seo, sort, status, client, cost, built_with, video_url
- `pages`: permalink, title, summary, status, seo · khối `block_html.raw_html`
- `categories`: title, slug · `seo`: title, meta_description, canonical_url · `redirects`: url_old, url_new, response_code

## 3. Cách làm bắt buộc
- **Thứ tự:** read-gate (một lượt đọc qua Write_Path repo: `AGENTS.md` → `COLLAB.md` → tệp này; READY khớp SHA) → ghi `STARTED@<RUN_ID> <UTC> · executor=codex` vào `COLLAB.md` + sửa 3 dòng Bảng (■ Đang làm · ➡ Kế tiếp · `cập nhật`) → A → B → C → D → KQ.
- **Chụp từ máy Owner** (máy chủ site cũ chặn địa chỉ trung tâm dữ liệu sau vài lượt). Chỉ GET. Tối đa 1 yêu cầu/giây. User-Agent của trình duyệt thường.
- **Chạy tiếp được:** tệp đã có và đúng sha thì bỏ qua — máy Owner có thể đóng giữa chừng (DROOT28).
- Chụp vào thư mục tạm trên máy Owner; xong mới đẩy một lượt lên hồ sơ VPS; kiểm sha256 sau khi đẩy khớp `MANIFEST.json`.
- **“Giống”** = bố cục, màu, chữ, thứ tự khối, ảnh nhìn như cũ ở 6 trang mẫu. Tối đa **một** vòng sửa bản dựng thử; khác biệt còn lại thì ghi ra, không sửa tiếp. Hiệu ứng trượt/động không cần chạy.
- Giao theo đầu ra trọn gói: tự sửa lỗi kịch bản của mình và làm tiếp; không dừng xin duyệt giữa chừng.

## 4. Cấm
- Mọi thay đổi PG · Directus · Nuxt · nginx · Docker · DNS · cron trên VPS1/VPS2. Gói này không tạo mã production, không gọi DOT ghi, không đọc PG/Directus.
- Trên VPS chỉ ghi trong `/opt/incomex/work/copy-web-incomexsaigoncorp-vn/`.
- Với site cũ: không POST, không đăng nhập, không `/wp-admin`, không `wp-login.php`, không `wp/v2/users`, không bình luận; không vòng tránh cơ chế chặn (đổi IP, proxy).
- Repo công khai: không đẩy CSS/JS/phông của giao diện; không đẩy ảnh ngoài 6 tệp so ảnh; không tạo tệp nào khác ngoài `assets/so-anh/*.jpg`. Trong `view.html` chỉ điền `#kiem-ke` và `#so-anh`, không đổi mục khác. Trong `COLLAB.md` chỉ ghi STARTED/KQ + 3 dòng Bảng.
- Không sửa nội dung cũ, kể cả chỗ sai — chép nguyên.
- Không cài phần mềm toàn máy; cần thư viện thì dùng môi trường ảo trong thư mục tạm.

## 5. Dừng (ghi KQ DỪNG + lý do một dòng) khi
- READY không khớp SHA, hoặc `COLLAB.md` có `STOP_REQUESTED`/HOLD.
- Site cũ trả 403/429/thử thách liên tục: nghỉ 5 phút, thử lại tối đa 3 lần, vẫn chặn ⇒ dừng.
- Kho chụp > 3 GB, hoặc đĩa VPS1 còn trống < 15 GB trước khi đẩy.
- Không ghi được qua Write_Path.

## 6. Kết thúc
- Trước KQ: đọc bảng đèn (DROOT34), ghi `ĐÈN: n xanh · m đỏ`; không đọc được ⇒ ghi `CHƯA XEM ĐÈN`.
- Ghi vào `COLLAB.md` một dòng `KQ@<RUN_ID> XONG` hoặc `KQ@<RUN_ID> DỪNG · <lý do>` kèm số liệu một dòng (số bản ghi · số trang HTML · số tệp · MB · commit) + sửa 3 dòng Bảng, cùng commit.
- Trả Owner đúng một dòng: `XONG` hoặc `DỪNG`.
