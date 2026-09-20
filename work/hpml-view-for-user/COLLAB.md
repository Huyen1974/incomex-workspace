# COLLAB — hpml-view-for-user

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC

**Mục tiêu**
- Tạo một lớp mỏng để hiển thị các file HTML của từng công việc từ `incomex-workspace` lên khu vực view trên VPS; GitHub là SSOT của kế hoạch và file thuộc công việc.
- Tạo một nơi quản lý tập trung cho User: mỗi `work/<work-id>/` chỉ có **một view** đại diện, có thể quản lý số lượng hàng trăm hoặc nhiều hơn theo thời gian và tách được công việc đang làm với công việc đã hoàn tất.

**Nhiệm vụ/phạm vi User đã giao**
1. Thiết kế view trên KB tại `https://vps.incomexsaigoncorp.vn/knowledge/modules`.
2. Dùng vị trí hiện tại của nút **Modules** và đổi tên thành **Tasks now**.
3. Loại bỏ các nội dung/chức năng liên quan đến Modules khỏi khu vực này.
4. Dùng bố cục hai cột tương tự Knowledge: cột trái là danh sách công việc/tên file; cột phải là view HTML của công việc đang chọn.
5. Có công cụ tìm kiếm chuẩn cho khu vực quản lý task/view.
6. Kiến trúc phải giữ vai trò **lớp hiển thị mỏng**; không biến VPS/KB thành SSOT mới thay cho GitHub.

**Tiêu chí xong ở mức mục tiêu hiện tại**
- Mỗi công việc có đúng một view HTML có thể truy cập từ khu quản lý tập trung.
- View phản ánh file thuộc workspace/GitHub theo cơ chế được thiết kế, không tạo nguồn kế hoạch song song trên VPS.
- `Tasks now` hỗ trợ danh sách lớn, tìm kiếm và xem nội dung theo bố cục hai cột.
- Có cách quản lý/chuyển các công việc đã hoàn tất ra khỏi nhóm đang làm mà vẫn tra cứu được về sau.
- Phương án đủ rõ để hội đồng GPT · Claude · Hermes review trước khi giao Agent triển khai.

**Xác nhận User:** CHƯA XÁC NHẬN — chờ User xác nhận lại đúng mục tiêu/nhiệm vụ trên theo `AGENTS.md#A0_OBJECTIVE`.

## Trạng thái
- HVU00 · 2026-09-20 · Đã mở công việc và ghi nhận nguyên tắc/mục tiêu User.
- Chưa lập kế hoạch kỹ thuật, chưa tạo `PROMPT.md`, chưa RUN/triển khai production do đang ở cổng A0.

## Ý kiến (P)
Reviewer: Claude Chat · Based_on `17b5470` (HVU không đổi từ `3d4d8cf`) · Chỉ góp ý khối §0 (cổng A0), không lập kế hoạch. Đã đọc: AGENTS A0–A8, README §0–§12, COLLAB gốc, file này. Thực địa (chỉ đọc): menu KB `web/components/navigation/TheHeader.vue`, route `pages/knowledge/modules/*`, danh mục meta CAT-002/CAT-009, đếm Directus `modules`/`tasks`, nginx `default.conf`. Chưa đọc: mã trang Knowledge 2 cột, Agent Data KB — để bước khảo sát sau A0.

- P01 · Scope §0 Nhiệm vụ 1–3 · OPEN · Thực địa: menu KB có cả `Modules` và `Tasks`. `Modules` = Directus `modules` 5 dòng (tạo 28/03/2026, chưa sửa lần nào); `Tasks` → `/knowledge/current-tasks` = Directus `tasks` 10 dòng (sửa lần cuối 29/03/2026); cả hai có hồ sơ danh mục meta (CAT-002, CAT-009); link chi tiết module của trang Discovery trỏ `/knowledge/modules/:id`. Đề nghị ghi rõ trong §0: (a) "loại bỏ Modules" = gỡ khỏi menu/giao diện, KHÔNG xoá bảng, dữ liệu, mã; phần mã gỡ ra đưa vào lưu trữ; thay đổi Nuxt production do Owner RUN riêng; (b) §0.1 là vị trí nút trên menu, không bắt buộc `Tasks now` dùng lại URL `/knowledge/modules`; (c) `Tasks` cũ nằm sát `Tasks now` tạo hai chỗ "công việc" — Claude đề xuất gỡ menu `Tasks` cũ theo đúng cách (a). Mục (c) là mở rộng phạm vi → **OWNER** quyết, Host không tự ghi vào §0.
- P02 · Scope §0 Nhiệm vụ 6 + Tiêu chí 2, 4 · OPEN · Gốc rễ của "lớp mỏng": nội dung HTML lấy từ Git đã rõ, nhưng danh sách việc + trạng thái Đang làm/Đã xong chưa nói lấy ở đâu; nếu ghi trạng thái ở Directus/VPS thì VPS thành SSOT thứ hai, trái §0.6. Đề nghị thêm vào §0: danh sách, tên, trạng thái việc đều đọc từ Git (COLLAB gốc/COLLAB từng việc), VPS chỉ đọc và hiển thị; chuyển sang Đã xong không đổi thư mục/URL (ID ổn định, link cũ vẫn mở). Ghi thêm ràng buộc: việc này là lần đầu hiện thực A8 + README §12 (nginx `default.conf` chưa có vùng Owner View, chỉ có `/ui-preview/` của xưởng vẽ); mã Nuxt/dịch vụ Cập nhật theo §11 (sửa trên VPS, dựng tại chỗ, đẩy bản sao lên GitHub).
- P03 · Scope §0 Tiêu chí xong 1, 3, 5 · OPEN · Đề nghị tiêu chí đo được: (a) README §12.3 chỉ cho nút Cập nhật kéo 1 file HTML → HTML có ảnh sẽ vỡ (MMIM: HTML 1,8 MB + 16 ảnh, xem MMIM P02); tiêu chí: view hiển thị đủ HTML chính + asset khai báo trong thư mục việc, và việc này được đề xuất sửa §12.3 qua D gốc + Owner quyết; (b) việc chưa có HTML chính (hiện: `mcp-workspace` và chính việc này) hiện "chưa có view"; tạo HTML cho việc khác không thuộc phạm vi; (c) "tìm kiếm chuẩn" = gõ tên/mã/chữ trong nội dung view → lọc ngay, lọc theo Đang làm/Đã xong; (d) thử thật với danh sách ≥300 việc; (e) "hội đồng GPT · Claude · Hermes review" sẽ treo vì Hermes chưa nối (DROOT02, HJW chờ R03) → sửa thành "GPT · Claude review; Hermes khi đã nối".
- P04 · Scope đầu file · OPEN · Thiếu dòng `Host · Host_ID` (A2) và `HTML chính` (A8) như các việc khác; thiếu Host_ID thì theo A2 mọi phiên mặc định là Reviewer. Tên `hpml-view-for-user` có vẻ gõ nhầm `html`; đổi lúc này chỉ tốn 1 `fs_move` + 1 dòng COLLAB gốc, đổi sau khi có URL Owner View thì link gãy. Đề nghị `work/owner-view/` (thuật ngữ chuẩn A8/README §12); Host đổi khi Owner gật.

## Owner cần quyết
- Xác nhận hoặc sửa khối `0. MỤC TIÊU/NHIỆM VỤ USER` ở trên.
