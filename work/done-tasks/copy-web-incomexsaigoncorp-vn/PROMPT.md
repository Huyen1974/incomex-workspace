# PROMPT — copy-web-incomexsaigoncorp-vn · RUN-04 hoàn thiện độc lập + cutover-ready
RUN_ID: CWEB-E2E-20261004-04
Trạng thái: xem `COLLAB.md` của việc. Chỉ chạy khi ở đó có dòng READY mang đúng SHA commit cuối chạm tệp này **và** Owner đã dán lệnh RUN.
Executor_Surface: Codex (máy Owner + đường tới VPS1 đã nghiệm thu của Codex).
Write_Path: repo `incomex-workspace` qua cổng `workspace_*`, chỉ trong `work/copy-web-incomexsaigoncorp-vn/`, commit tiền tố `[Codex]` · VPS1: mọi thay đổi chỉ qua DOT/script-wrapper · hồ sơ việc `/opt/incomex/work/copy-web-incomexsaigoncorp-vn/` (tạo bằng `mkdir`).
§0.3: đã đối chiếu (Host P04 + Reviewer GPT P05, 03/10/2026 22:30).

## 0. Cổng vào — chỉ đọc; sai một điều thì DỪNG, không đổi gì
1. Đọc `AGENTS.md` → `COLLAB.md` của việc (Bảng + §0) → tệp này. READY khớp SHA.
1a. Đây là **RUN hoàn thiện sau RUN-03**. Trang `https://vps.incomexsaigoncorp.vn/w/` đã chạy thật; 27 content + 73 Directus Files, 32 route, form/nhúng, hồi quy và POST-PROTECT đã PASS ở RUN-03. **Không dựng lại và không nạp lại dữ liệu** nếu verify hiện trạng khớp; chỉ sửa phần độc lập tài nguyên/cutover-ready và lỗi phát hiện thật.
2. Nâng cấp máy chủ đã XONG — Host kiểm 03/10: `work/done-tasks/vps1-up-grade/COLLAB.md` có KQ G7 XONG; VPS1 đang chạy PG 18.6 · Directus 12.4.1 · Nuxt 4.5.2. Kiểm lại bằng DOT/health sẵn có; lệch phiên bản ⇒ DỪNG.
3. Không executor nào khác đang thay đổi VPS1 (bảng ai-đang-làm của MCPW + `COLLAB.md` gốc). Có ⇒ DỪNG, báo một dòng.
3a. Đọc bảng đèn. `INV15.kuma_telegram_coverage` / #22 `MCPW Protection Guard` phải xanh trước mutation. Nếu vẫn đỏ ⇒ DỪNG đúng DROOT37 và chỉ trỏ `work/hermes-joint-workspace`; **không sửa HJW trong CWEB**.
4. Tiền tố `/w` chưa được dùng trong Nuxt và nginx. Đã dùng do một RUN CWEB hợp lệ trước đó thì kiểm trạng thái và tiếp tục idempotent; do việc khác dùng ⇒ DỪNG.
5. Ghi `STARTED@<RUN_ID> <UTC> · executor=codex` vào `COLLAB.md` + sửa 3 dòng Bảng (■ Đang làm · ➡ Kế tiếp · `cập nhật`).

## 1. Đầu bài — lời Owner 03/10/2026 22:07, không diễn giải thêm
> “tạo ra một trang giống nhất có thể, có thể lấy tạm 1 đường dẫn nào đó để chạy, sau khi ok chúng ta chuyển domain sang VPS của chúng ta. và coi như cho chạy tạm trên VPS này. Cách bật rõ những cái gì nhúng thì chuyển sang (vì nhúng là nguồn của chúng ta) còn lại thì copy nguyên trang Web đó sang bên chỗ mới, dựng lại trên nền tảng của chúng ta. (sao cho nhìn giao diện càng giống càng tốt)”

- Vì sao (Owner 02/10): hợp đồng với bên làm web cũ hết hạn; không làm gì thì `https://incomexsaigoncorp.vn/` bị ngừng. Đây là giải pháp tạm; làm lại toàn bộ web là việc khác, để sau.
- “100% dùng DOT hết với PG và Directus, thiếu viết thêm.”
- **Không cải tiến, không sửa nội dung, không thiết kế lại.** Owner 04/10 bổ sung: site phải **độc lập trên VPS/Directus**, ảnh và tài nguyên cần để khách xem web không phụ thuộc GitHub hay máy chủ web cũ; sau khi duyệt, chỉ còn cutover domain/DNS để khách dùng cùng URL cũ mà không cảm giác đổi hệ thống.

## 2. Đã biết (Host điều tra 02–03/10 — kiểm lại nhanh, lệch thì ghi vào KQ)
- **Site cũ:** WordPress + giao diện Flatsome do bên cũ vận hành. `wp-json/wp/v2` đọc được: 5 trang · 14 bài · 9 chuyên mục · 16 thẻ · 73 ảnh. 29 địa chỉ nội bộ, đều 200. Trang `/project-post/…` (đơn hàng) không có trong `wp-json`, chỉ lấy từ HTML. Máy chủ bên cũ chặn truy cập tự động từ địa chỉ trung tâm dữ liệu ⇒ chụp từ máy Owner.
- **Phần nhúng (nguồn của Incomex — chuyển nguyên sang):** khung Google Maps (chân trang) · khung YouTube (`/gioi-thieu/`) · liên kết Lark wiki (bài “các đơn hàng mới nhất”, `/category/don-hang/`) · liên kết menu “Giáo dục” sang cổng giaoduc. Tính năng: form liên hệ ở `/lien-he/`.
- **Hệ mình sau nâng cấp:** các collection web dùng chung (`posts`, `categories`, `pages`, `block_html`, `seo`, `forms`, `inbox`) đang có dữ liệu của cổng nội bộ. **RUN này tuyệt đối không ghi vào các collection dùng chung đó.** Owner 03/10 yêu cầu dữ liệu web Incomex phải nhìn tên là nhận ra và có ghi chú để sau này không lẫn.
- **Namespace chốt cứng:** Directus group/folder hiển thị `Web Incomex — incomexsaigoncorp.vn` (key/group `web_incomex`, metadata-only nếu cơ chế group hỗ trợ) · physical collections chỉ gồm `web_incomex_content`, `web_incomex_inbox` · Directus Files folder `web-incomex`. Mỗi collection phải có note/description bắt đầu `[WEB_INCOMEX]` và nêu rõ `temporary mirror of incomexsaigoncorp.vn, created for 2026 continuity cutover; do not mix with Agency OS shared content`.
- Mã Nuxt: `/opt/incomex/docker/nuxt-repo/web` (có `pages/[...permalink].vue`, `pages/posts/`). DOT dùng chung hiện có chỉ tái dùng khi đúng scope; thiếu schema/content capability cho namespace mới thì viết/nâng DOT trước, không fallback thao tác trực tiếp.

## 3. Việc — làm liền một mạch, không xin duyệt giữa chừng
**A. Nguồn — ĐÃ XONG ở RUN-02:** verify snapshot/manifest theo §0.1a rồi đi thẳng B. Không lặp lại crawl/chụp nếu verify PASS.

**B. DOT trước, thao tác sau** (DROOT26/27/29/35): kê DOT dùng được trên bộ hiện tại. Thiếu thì viết/nâng rồi dùng chính nó. Bắt buộc có một đường bootstrap idempotent cho namespace `web_incomex`: tạo/verify Directus group + đúng 2 collection + fields + notes + Files folder; dry-run mặc định; chạy lại không nhân đôi; rollback chỉ chạm namespace này. Tiếp đó dùng DOT cho nạp hàng loạt từ `chup/`, nạp ảnh, permission read-only published, tự kiểm trang và deploy Nuxt (tái dùng DOT/script mà việc nâng cấp bàn giao; thiếu thì bọc lệnh chính thức thành script-wrapper). Mỗi DOT mới có `--help`, dry-run, verify, rollback, secret handling và mã thoát.

**C. Namespace dữ liệu riêng — ngắn nhưng sạch, không lẫn hệ khác:**
- Tạo/verify collection `web_incomex_content` dưới group `web_incomex`. Tối thiểu các field: `id`, `source_id`, `kind` (`page|post|project`), `path` (unique), `slug`, `title`, `excerpt`, `content_html`, `published_at`, `primary_category`, `categories_json`, `tags_json`, `featured_image` (M2O `directus_files`), `seo_title`, `seo_description`, `status`, `source_url`, `sort`. Note bắt buộc theo §2.
- Tạo/verify collection `web_incomex_inbox` dưới cùng group cho form liên hệ: `id`, `date_created`, `name`, `phone`, `email`, `message`, `source_path`, `status`. Note bắt buộc theo §2.
- 5 trang + 14 bài + các `/project-post/…` → `web_incomex_content`; `path` giữ URL nghiệp vụ cũ (không chứa `/w` trong DB). Chuyên mục/thẻ giữ trong field của content, không tạo collection thứ ba. Đơn hàng dùng `kind=project`, `primary_category=don-hang` khi đúng nguồn.
- 73 tệp nguồn nội dung (69 ảnh + 4 PDF) → Directus Files folder `web-incomex`; `featured_image` trỏ file tương ứng; HTML đổi asset URL sang tệp trên hệ mình. **Mọi ảnh/PDF khách nhìn thấy phải phục vụ từ VPS/Directus của Incomex, không từ GitHub/raw.githubusercontent và không từ host WordPress cũ.**
- Không ghi bất kỳ row nào vào `posts/pages/categories/block_html/seo/forms/inbox` dùng chung. Nội dung chữ giữ nguyên; HTML phần thân giữ cấu trúc cần thiết để giao diện cũ áp được.

**D. Dựng lại giống nhất có thể** — lớp Nuxt mỏng, **chỉ thêm tệp**:
- Một layout riêng cho `/w/**`: dùng lại khuôn HTML đầu trang/chân trang và **CSS mặt ngoài của site cũ**; CSS/JS/phông/icon/favicon cần thiết phải được self-host trên VPS trong vùng CWEB hoặc Directus Files, không phụ thuộc GitHub/CDN/web cũ. **Chỉ nạp ở layout `/w/`** — không được làm đổi bất kỳ trang nào khác của cổng. Không mang theo PHP/plugin; JS cũ chỉ lấy phần cần cho menu di động. Không thêm thư viện/gói mới nếu không bắt buộc.
- Các trang dưới tiền tố `/w/`: `/w/` (trang chủ: giới thiệu + dịch vụ + “đơn hàng đang tuyển” + tin mới — lấy từ `web_incomex_content`) · `/w/<trang>` · `/w/category/<slug>` · `/w/<slug bài>` · `/w/project-post/<slug>`. Liên kết nội bộ sinh theo tiền tố đang phục vụ; khi tên miền chính trỏ gốc `/`, cùng dữ liệu phải phục vụ đúng địa chỉ cũ.
- Không dựng: tìm kiếm, bình luận, đăng nhập. Hiệu ứng trượt không bắt buộc.

**E. Nhúng lại — chuyển nguyên nguồn, không dựng lại:** khung Google Maps · khung YouTube · liên kết Lark wiki · liên kết cổng giaoduc. Nếu chính sách khung của máy chủ phục vụ trang thử chặn hai khung: thêm **đúng hai nguồn** `https://www.google.com` và `https://www.youtube.com` vào `frame-src` của đúng khối máy chủ đó, qua script-wrapper có sao lưu + kiểm cấu hình + rollback; không mở kiểu `*`.
- **Form liên hệ** (tính năng): giữ hình dạng gần cũ và ghi submission vào `web_incomex_inbox` qua endpoint/DOT phù hợp; không dùng `forms/inbox` dùng chung. Nếu gửi thật gặp blocker ngoài phạm vi, vẫn phải giữ UI form + validation và fallback hiển thị điện thoại/email, ghi blocker trong KQ.

**F. Trang thử + cutover-ready:** giữ `https://vps.incomexsaigoncorp.vn/w/` để Owner duyệt. Đồng thời chuẩn bị routing/config để khi Host là `incomexsaigoncorp.vn` hoặc `www.incomexsaigoncorp.vn`, các URL cũ phục vụ ở **root** (`/`, `/gioi-thieu/`, `/category/...`, `/project-post/...`) mà không còn `/w`. Chưa đổi DNS. Kiểm bằng **trình duyệt thật** với tên miền chính ánh xạ tạm về VPS ngay trong máy thử (host-resolver/local resolve), không ảnh hưởng domain đang chạy: đủ 6 trang mẫu ở root, bấm menu/liên kết nội bộ vẫn ở root, không lỗi console. Dưới tên miền chính **chỉ phục vụ site công ty**: đường dẫn của cổng nội bộ (vd `/knowledge`, `/posts`, `/reports`, `/login`) phải trả 404 của site, không lộ cổng nội bộ. Kiểm luôn kế hoạch TLS: nếu đã có cert hợp lệ/wildcard dùng được cho **cả apex `incomexsaigoncorp.vn` và `www.incomexsaigoncorp.vn`** thì verify; nếu chưa có thì chuẩn bị đường **không có khoảng hở**: cấp cert **trước** khi đổi `@`/`www` bằng xác thực DNS-01 (Owner thêm bản ghi TXT), dùng đúng công cụ cấp chứng chỉ đang dùng cho các tên miền hiện có. RUN này chỉ chuẩn bị DOT/script và dry-run tới bước in ra TXT cần thêm; lượt cutover phải theo thứ tự **Owner thêm TXT → cấp/cài cert thật → kiểm cert + HTTPS root bằng local resolve/SNI tới VPS → chỉ khi PASS mới đổi `@`/`www`**. **HTTP-01 sau khi đã chuyển traffic không phải đường PASS** vì có thể tạo cảnh báo/gián đoạn; nếu DNS-01/cert chưa PASS thì chưa cutover. Không hỏi Owner giữa RUN này.

**G. Tự kiểm — trình duyệt thật:**
- 29 địa chỉ cũ ↔ địa chỉ `/w/…` tương ứng: đều 200, không liên kết nội bộ chết, ảnh hiện.
- 4 phần nhúng/liên kết hoạt động.
- So ảnh 6 trang mẫu (cũ ↔ mới), rộng 1366 và 390; tối đa **hai** vòng sửa; khác biệt còn lại ghi mỗi trang một dòng.
- Thử một lệnh DOT thêm row thử vào `web_incomex_content` → hiện ở trang chủ + chuyên mục → gỡ row thử.
- Hồi quy: chạy lại bộ kiểm trang hiện có của hệ sau khi đưa lên — toàn bộ trang/các collection dùng chung phải không đổi; `/posts` của cổng nội bộ không được xuất hiện bài web công ty.
- **Audit độc lập tài nguyên trên đủ 32 route:** 0 request runtime tới `github.com`, `raw.githubusercontent.com`, `githubusercontent.com`, host WordPress cũ hoặc CDN cho tài nguyên site-owned. Cho phép đúng các nguồn ngoài có chủ ý: Google Maps, YouTube, Lark, cổng Giáo dục và outbound links. Ảnh/PDF/CSS/JS/font/icon/favicon site-owned phải 200 từ VPS/Directus và đúng MIME. Hiện đã thấy hai lỗi phải xử lý: Google Fonts/FontAwesome đang bị CSP chặn và một stylesheet `/w/assets/*.bin` trả `application/octet-stream`; self-host font/icon và sửa mapping/MIME rồi kiểm lại console/resource.
- **6 JPEG so ảnh là bằng chứng QA, không phải runtime asset và không được chặn XONG chỉ vì GitHub không nhận binary.** Lưu chúng tại `/opt/incomex/work/copy-web-incomexsaigoncorp-vn/evidence/so-anh/01.jpg…06.jpg` + manifest SHA256. `view.html#so-anh` ghi bảng kết quả/đường dẫn bằng chứng trên VPS nếu có route xem nội bộ; không bắt push JPEG lên GitHub.

**6 trang mẫu (chốt cứng):** `/` · `/gioi-thieu/` · `/lien-he/` · `/category/don-hang/` · `/tin-vui-nhat-ban-mo-cua-don-lao-dong-viet-nam-tu-3-2022/` · `/project-post/don-hang-son-nha-cua/`

**H. Bảo vệ + đường lùi** (DROOT29/34): đăng ký tệp và DOT mới vào lớp bảo vệ hiện có · đường lùi một lệnh (trả Nuxt về bản trước + gỡ dữ liệu đã nạp theo danh sách id của chính RUN này), đã thử dry-run · đọc bảng đèn, ghi `ĐÈN: n xanh · m đỏ` (không đọc được ⇒ `CHƯA XEM ĐÈN`, không ghi XONG).

## 4. Cấm
- Tạo collection/table ngoài đúng namespace đã chốt (`web_incomex_content`, `web_incomex_inbox`) hoặc thêm field ngoài spec mà không có lý do bắt buộc. Không ghi dữ liệu web công ty vào collection dùng chung. Sửa tệp Nuxt đang chạy (buộc phải chạm một tệp cấu hình ⇒ sửa tối thiểu, ghi diff trong KQ).
- Sửa/xoá dữ liệu hoặc file sẵn có của cổng nội bộ. Để CSS cũ lọt ra ngoài `/w/`.
- `psql`/SQL/REST/CLI trực tiếp với PG hay Directus — kể cả để đọc. Thiếu DOT thì viết DOT.
- Tự chọn/nâng phiên bản hay thêm thành phần: dùng đúng bộ đang chạy.
- DNS, tên miền mới, VPS2. Sửa nội dung cũ, kể cả chỗ sai.
- Với site cũ: POST, đăng nhập, `/wp-admin`, `wp/v2/users`, vòng tránh cơ chế chặn.
- **GitHub không phải kho runtime asset.** Không đưa ảnh/PDF/font/icon/CSS giao diện cần cho web chạy lên GitHub để website tham chiếu. Repo chỉ giữ code/text/config/tài liệu. 6 JPEG QA cũng không bắt buộc lên GitHub; lưu evidence trên VPS. Trong `view.html` chỉ điền `#kiem-ke`, `#so-anh`. Trong `COLLAB.md` chỉ ghi STARTED/KQ + 3 dòng Bảng.
- Xoá bất cứ thứ gì ngoài bài thử do chính RUN này tạo.

## 5. Dừng (ghi KQ DỪNG + lý do một dòng) khi
- Cổng vào sai · `COLLAB.md` có `STOP_REQUESTED`/HOLD · trước nhóm thay đổi production đầu tiên phải đọc lại `COLLAB.md` + tệp này (DROOT30).
- #22/HJW vẫn đỏ theo §0.3a; không điều hành/sửa việc khác từ CWEB.
- Snapshot đã verify ở RUN-02 bị thiếu/hỏng và site cũ không thể lấy lại phần bắt buộc ⇒ dừng, không tự suy đoán nội dung.
- Hồi quy đỏ sau khi đã tự sửa các lỗi thuộc phạm vi CWEB và thử lại ⇒ chạy đường lùi rồi dừng. **Không DỪNG vì lỗi code/DOT/CSS/config do chính RUN này tạo nếu còn có thể tự sửa trong phạm vi; tự sửa → verify → tiếp tục đến trang thử.** Đèn đỏ do chính RUN này ⇒ chưa XONG.

## 6. Kết thúc
- Ghi vào `COLLAB.md` một dòng `KQ@<RUN_ID> XONG` hoặc `KQ@<RUN_ID> DỪNG · <lý do>` kèm số liệu một dòng (bài · trang · ảnh đã nạp · địa chỉ 200 · DOT mới · commit) + sửa 3 dòng Bảng, cùng commit.
- Chỉ được trả `XONG · https://vps.incomexsaigoncorp.vn/w/ · CUTOVER_READY` khi browser thật desktop 1366 + mobile 390 PASS; đủ route hiện hành PASS; nhúng/form PASS; collection/file đúng namespace; hồi quy ngoài `/w/` PASS; **runtime 0 phụ thuộc GitHub/web cũ cho tài nguyên site-owned; font/icon/CSS/JS/ảnh/PDF/favicons tự host và MIME/CSP sạch**; mô phỏng Host `incomexsaigoncorp.vn`/`www` ở root URL cũ PASS; TLS cutover path đã xác định; POST-PROTECT + receipt PASS; và đã đối chiếu chi tiết với bản cũ/chi tiết con người duyệt. Nếu còn dependency khiến DNS chuyển xong web không tự chạy thì **chưa CUTOVER_READY/XONG**.
