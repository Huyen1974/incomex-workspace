# PROMPT — copy-web-incomexsaigoncorp-vn · MỘT RUN từ đầu tới trang thử
RUN_ID: CWEB-E2E-20261003-02
Trạng thái: xem `COLLAB.md` của việc. Chỉ chạy khi ở đó có dòng READY mang đúng SHA commit cuối chạm tệp này **và** Owner đã dán lệnh RUN.
Executor_Surface: Codex (máy Owner + đường tới VPS1 đã nghiệm thu của Codex).
Write_Path: repo `incomex-workspace` qua cổng `workspace_*`, chỉ trong `work/copy-web-incomexsaigoncorp-vn/`, commit tiền tố `[Codex]` · VPS1: mọi thay đổi chỉ qua DOT/script-wrapper · hồ sơ việc `/opt/incomex/work/copy-web-incomexsaigoncorp-vn/` (tạo bằng `mkdir`).
§0.3: đã đối chiếu (Host P04 + Reviewer GPT P05, 03/10/2026 22:30).

## 0. Cổng vào — chỉ đọc; sai một điều thì DỪNG, không đổi gì
1. Đọc `AGENTS.md` → `COLLAB.md` của việc (Bảng + §0) → tệp này. READY khớp SHA.
2. Nâng cấp máy chủ đã XONG — Host kiểm 03/10: `work/done-tasks/vps1-up-grade/COLLAB.md` có KQ G7 XONG; VPS1 đang chạy PG 18.6 · Directus 12.4.1 · Nuxt 4.5.2. Kiểm lại bằng DOT/health sẵn có; lệch phiên bản ⇒ DỪNG.
3. Không executor nào khác đang thay đổi VPS1 (bảng ai-đang-làm của MCPW + `COLLAB.md` gốc). Có ⇒ DỪNG, báo một dòng.
4. Tiền tố `/w` chưa được dùng trong Nuxt và nginx. Đã dùng ⇒ DỪNG.
5. Ghi `STARTED@<RUN_ID> <UTC> · executor=codex` vào `COLLAB.md` + sửa 3 dòng Bảng (■ Đang làm · ➡ Kế tiếp · `cập nhật`).

## 1. Đầu bài — lời Owner 03/10/2026 22:07, không diễn giải thêm
> “tạo ra một trang giống nhất có thể, có thể lấy tạm 1 đường dẫn nào đó để chạy, sau khi ok chúng ta chuyển domain sang VPS của chúng ta. và coi như cho chạy tạm trên VPS này. Cách bật rõ những cái gì nhúng thì chuyển sang (vì nhúng là nguồn của chúng ta) còn lại thì copy nguyên trang Web đó sang bên chỗ mới, dựng lại trên nền tảng của chúng ta. (sao cho nhìn giao diện càng giống càng tốt)”

- Vì sao (Owner 02/10): hợp đồng với bên làm web cũ hết hạn; không làm gì thì `https://incomexsaigoncorp.vn/` bị ngừng. Đây là giải pháp tạm; làm lại toàn bộ web là việc khác, để sau.
- “100% dùng DOT hết với PG và Directus, thiếu viết thêm.”
- **Không cải tiến, không sửa nội dung, không thiết kế lại.** Việc của RUN này dừng ở trang thử; chuyển tên miền là lệnh riêng của Owner.

## 2. Đã biết (Host điều tra 02–03/10 — kiểm lại nhanh, lệch thì ghi vào KQ)
- **Site cũ:** WordPress + giao diện Flatsome do bên cũ vận hành. `wp-json/wp/v2` đọc được: 5 trang · 14 bài · 9 chuyên mục · 16 thẻ · 73 ảnh. 29 địa chỉ nội bộ, đều 200. Trang `/project-post/…` (đơn hàng) không có trong `wp-json`, chỉ lấy từ HTML. Máy chủ bên cũ chặn truy cập tự động từ địa chỉ trung tâm dữ liệu ⇒ chụp từ máy Owner.
- **Phần nhúng (nguồn của Incomex — chuyển nguyên sang):** khung Google Maps (chân trang) · khung YouTube (`/gioi-thieu/`) · liên kết Lark wiki (bài “các đơn hàng mới nhất”, `/category/don-hang/`) · liên kết menu “Giáo dục” sang cổng giaoduc. Tính năng: form liên hệ ở `/lien-he/`.
- **Hệ mình sau nâng cấp:** các collection web dùng chung (`posts`, `categories`, `pages`, `block_html`, `seo`, `forms`, `inbox`) đang có dữ liệu của cổng nội bộ. **RUN này tuyệt đối không ghi vào các collection dùng chung đó.** Owner 03/10 yêu cầu dữ liệu web Incomex phải nhìn tên là nhận ra và có ghi chú để sau này không lẫn.
- **Namespace chốt cứng:** Directus group/folder hiển thị `Web Incomex — incomexsaigoncorp.vn` (key/group `web_incomex`, metadata-only nếu cơ chế group hỗ trợ) · physical collections chỉ gồm `web_incomex_content`, `web_incomex_inbox` · Directus Files folder `web-incomex`. Mỗi collection phải có note/description bắt đầu `[WEB_INCOMEX]` và nêu rõ `temporary mirror of incomexsaigoncorp.vn, created for 2026 continuity cutover; do not mix with Agency OS shared content`.
- Mã Nuxt: `/opt/incomex/docker/nuxt-repo/web` (có `pages/[...permalink].vue`, `pages/posts/`). DOT dùng chung hiện có chỉ tái dùng khi đúng scope; thiếu schema/content capability cho namespace mới thì viết/nâng DOT trước, không fallback thao tác trực tiếp.

## 3. Việc — làm liền một mạch, không xin duyệt giữa chừng
**A. Chụp** (từ máy Owner · chỉ GET · ≤ 1 yêu cầu/giây · chạy tiếp được): JSON `pages|posts|categories|tags|media` (`per_page=100`, `_embed=1`) · HTML của 29 địa chỉ (từ liên kết trang chủ + trường `link`) · 73 tệp ảnh đang dùng · CSS, phông, biểu tượng mà 6 trang mẫu nạp · ảnh chụp màn hình 6 trang mẫu rộng 1366 và 390 làm chuẩn so. Lưu ở hồ sơ việc `chup/` + `MANIFEST.json` (sha256).

**B. DOT trước, thao tác sau** (DROOT26/27/29/35): kê DOT dùng được trên bộ hiện tại. Thiếu thì viết/nâng rồi dùng chính nó. Bắt buộc có một đường bootstrap idempotent cho namespace `web_incomex`: tạo/verify Directus group + đúng 2 collection + fields + notes + Files folder; dry-run mặc định; chạy lại không nhân đôi; rollback chỉ chạm namespace này. Tiếp đó dùng DOT cho nạp hàng loạt từ `chup/`, nạp ảnh, permission read-only published, tự kiểm trang và deploy Nuxt (tái dùng DOT/script mà việc nâng cấp bàn giao; thiếu thì bọc lệnh chính thức thành script-wrapper). Mỗi DOT mới có `--help`, dry-run, verify, rollback, secret handling và mã thoát.

**C. Namespace dữ liệu riêng — ngắn nhưng sạch, không lẫn hệ khác:**
- Tạo/verify collection `web_incomex_content` dưới group `web_incomex`. Tối thiểu các field: `id`, `source_id`, `kind` (`page|post|project`), `path` (unique), `slug`, `title`, `excerpt`, `content_html`, `published_at`, `primary_category`, `categories_json`, `tags_json`, `featured_image` (M2O `directus_files`), `seo_title`, `seo_description`, `status`, `source_url`, `sort`. Note bắt buộc theo §2.
- Tạo/verify collection `web_incomex_inbox` dưới cùng group cho form liên hệ: `id`, `date_created`, `name`, `phone`, `email`, `message`, `source_path`, `status`. Note bắt buộc theo §2.
- 5 trang + 14 bài + các `/project-post/…` → `web_incomex_content`; `path` giữ URL nghiệp vụ cũ (không chứa `/w` trong DB). Chuyên mục/thẻ giữ trong field của content, không tạo collection thứ ba. Đơn hàng dùng `kind=project`, `primary_category=don-hang` khi đúng nguồn.
- 73 ảnh → Directus Files folder `web-incomex`; `featured_image` trỏ file tương ứng; HTML đổi asset URL sang file mới khi cần.
- Không ghi bất kỳ row nào vào `posts/pages/categories/block_html/seo/forms/inbox` dùng chung. Nội dung chữ giữ nguyên; HTML phần thân giữ cấu trúc cần thiết để giao diện cũ áp được.

**D. Dựng lại giống nhất có thể** — lớp Nuxt mỏng, **chỉ thêm tệp**:
- Một layout riêng cho `/w/**`: dùng lại khuôn HTML đầu trang/chân trang và **CSS mặt ngoài của site cũ** (CSS, phông, biểu tượng đã chụp), đặt trong một thư mục tĩnh riêng. **Chỉ nạp ở layout `/w/`** — không được làm đổi bất kỳ trang nào khác của cổng. Không mang theo PHP/plugin; JS cũ chỉ lấy phần cần cho menu di động. Không thêm thư viện hay gói mới vào Nuxt. Không đẩy các tệp giao diện cũ lên repo công khai nào.
- Các trang dưới tiền tố `/w/`: `/w/` (trang chủ: giới thiệu + dịch vụ + “đơn hàng đang tuyển” + tin mới — lấy từ `web_incomex_content`) · `/w/<trang>` · `/w/category/<slug>` · `/w/<slug bài>` · `/w/project-post/<slug>`. Liên kết nội bộ sinh theo tiền tố đang phục vụ; khi tên miền chính trỏ gốc `/`, cùng dữ liệu phải phục vụ đúng địa chỉ cũ.
- Không dựng: tìm kiếm, bình luận, đăng nhập. Hiệu ứng trượt không bắt buộc.

**E. Nhúng lại — chuyển nguyên nguồn, không dựng lại:** khung Google Maps · khung YouTube · liên kết Lark wiki · liên kết cổng giaoduc. Nếu chính sách khung của máy chủ phục vụ trang thử chặn hai khung: thêm **đúng hai nguồn** `https://www.google.com` và `https://www.youtube.com` vào `frame-src` của đúng khối máy chủ đó, qua script-wrapper có sao lưu + kiểm cấu hình + rollback; không mở kiểu `*`.
- **Form liên hệ** (tính năng): giữ hình dạng gần cũ và ghi submission vào `web_incomex_inbox` qua endpoint/DOT phù hợp; không dùng `forms/inbox` dùng chung. Nếu gửi thật gặp blocker ngoài phạm vi, vẫn phải giữ UI form + validation và fallback hiển thị điện thoại/email, ghi blocker trong KQ.

**F. Đưa lên + trang thử:** đưa Nuxt lên bằng DOT/script ở B · mở quyền public **chỉ đọc, chỉ `status=published`** cho `web_incomex_content`; `web_incomex_inbox` chỉ cho endpoint ghi tối thiểu cần thiết, không public read. Trang thử: `https://vps.incomexsaigoncorp.vn/w/`. Không tạo tên miền, không đụng DNS.

**G. Tự kiểm — trình duyệt thật:**
- 29 địa chỉ cũ ↔ địa chỉ `/w/…` tương ứng: đều 200, không liên kết nội bộ chết, ảnh hiện.
- 4 phần nhúng/liên kết hoạt động.
- So ảnh 6 trang mẫu (cũ ↔ mới), rộng 1366 và 390; tối đa **hai** vòng sửa; khác biệt còn lại ghi mỗi trang một dòng.
- Thử một lệnh DOT thêm row thử vào `web_incomex_content` → hiện ở trang chủ + chuyên mục → gỡ row thử.
- Hồi quy: chạy lại bộ kiểm trang hiện có của hệ sau khi đưa lên — toàn bộ trang/các collection dùng chung phải không đổi; `/posts` của cổng nội bộ không được xuất hiện bài web công ty.
- 6 ảnh ghép ≤ 250 KB → repo `assets/so-anh/01.jpg … 06.jpg`, nhúng vào `view.html` mục `#so-anh`; bổ sung số liệu vào `#kiem-ke`.

**6 trang mẫu (chốt cứng):** `/` · `/gioi-thieu/` · `/lien-he/` · `/category/don-hang/` · `/tin-vui-nhat-ban-mo-cua-don-lao-dong-viet-nam-tu-3-2022/` · `/project-post/don-hang-son-nha-cua/`

**H. Bảo vệ + đường lùi** (DROOT29/34): đăng ký tệp và DOT mới vào lớp bảo vệ hiện có · đường lùi một lệnh (trả Nuxt về bản trước + gỡ dữ liệu đã nạp theo danh sách id của chính RUN này), đã thử dry-run · đọc bảng đèn, ghi `ĐÈN: n xanh · m đỏ` (không đọc được ⇒ `CHƯA XEM ĐÈN`, không ghi XONG).

## 4. Cấm
- Tạo collection/table ngoài đúng namespace đã chốt (`web_incomex_content`, `web_incomex_inbox`) hoặc thêm field ngoài spec mà không có lý do bắt buộc. Không ghi dữ liệu web công ty vào collection dùng chung. Sửa tệp Nuxt đang chạy (buộc phải chạm một tệp cấu hình ⇒ sửa tối thiểu, ghi diff trong KQ).
- Sửa/xoá dữ liệu hoặc file sẵn có của cổng nội bộ. Để CSS cũ lọt ra ngoài `/w/`.
- `psql`/SQL/REST/CLI trực tiếp với PG hay Directus — kể cả để đọc. Thiếu DOT thì viết DOT.
- Tự chọn/nâng phiên bản hay thêm thành phần: dùng đúng bộ đang chạy.
- DNS, tên miền mới, VPS2. Sửa nội dung cũ, kể cả chỗ sai.
- Với site cũ: POST, đăng nhập, `/wp-admin`, `wp/v2/users`, vòng tránh cơ chế chặn.
- Repo công khai: tệp giao diện bên cũ, ảnh (trừ 6 ảnh so). Trong `view.html` chỉ điền `#kiem-ke`, `#so-anh`. Trong `COLLAB.md` chỉ ghi STARTED/KQ + 3 dòng Bảng.
- Xoá bất cứ thứ gì ngoài bài thử do chính RUN này tạo.

## 5. Dừng (ghi KQ DỪNG + lý do một dòng) khi
- Cổng vào sai · `COLLAB.md` có `STOP_REQUESTED`/HOLD · trước nhóm thay đổi production đầu tiên phải đọc lại `COLLAB.md` + tệp này (DROOT30).
- Site cũ chặn hoặc đã ngừng: nghỉ 5 phút, thử lại tối đa 3 lần, vẫn không lấy đủ ⇒ dừng, không tự suy đoán nội dung.
- Hồi quy đỏ sau khi đưa lên ⇒ chạy đường lùi rồi dừng. Đèn đỏ do chính RUN này ⇒ chưa XONG.

## 6. Kết thúc
- Ghi vào `COLLAB.md` một dòng `KQ@<RUN_ID> XONG` hoặc `KQ@<RUN_ID> DỪNG · <lý do>` kèm số liệu một dòng (bài · trang · ảnh đã nạp · địa chỉ 200 · DOT mới · commit) + sửa 3 dòng Bảng, cùng commit.
- Trả Owner đúng một dòng: `XONG · https://vps.incomexsaigoncorp.vn/w/` hoặc `DỪNG`.
