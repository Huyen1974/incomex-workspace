# XƯỞNG VẼ INCOMEX

`/opt/incomex/docs/mcp-writes` là nguồn gốc duy nhất để Owner, Claude Cowork,
Codex và Claude Code cùng thiết kế:

- giao diện;
- luồng nghiệp vụ;
- hợp đồng thông tin;
- dữ liệu mẫu và tài liệu nghiệm thu.

## Quy tắc ngắn

1. Đọc `AGENTS.md` trước khi sửa.
2. Không tự sửa phần Owner đã chốt.
3. Không tạo một bản UI “mới hơn” ở thư mục khác.
4. Cấu trúc dùng nhiều nơi phải có một renderer/source; nhân bản bằng dữ liệu.
5. Trước và sau thay đổi lớn, ghi mỏ neo:

   ```bash
   mcp-writes-git snapshot "ly do"
   ```

6. Timer Git tự chạy mỗi 5 phút là lưới an toàn, không thay thế nghiệm thu.
7. Không push repo này. Đây là sổ quay lui cục bộ trên VPS.

## Xưởng vẽ và hệ thống chạy thật

- Xưởng vẽ trả lời: UI trông thế nào, người thao tác ra sao, nghiệp vụ và hợp
  đồng thông tin là gì.
- Repo ứng dụng/PG trả lời: code chạy thật, quyền, API, bảng và triển khai.
- Khi chuyển một thiết kế sang hệ thống chạy thật, ghi lại commit nguồn của
  xưởng. Không sửa ngược thiết kế gốc chỉ để chiều theo chi tiết triển khai.

## Đường dẫn

- Xưởng trên đĩa: `/opt/incomex/docs/mcp-writes`
- Preview: `https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/`
- New MODT: `https://vps.incomexsaigoncorp.vn/admin-new-modt`
- Git local: `/usr/local/bin/mcp-writes-git`

`ui-preview` trong xưởng chỉ là symlink tương thích cho yêu cầu cũ; nó trỏ về
chính thư mục này và không phải bản sao.

---

## Quy tắc mang thiết kế ra ngoài (bổ sung 2026-07-27)

Khi cần đấu nối thật với PostgreSQL, Directus, API hoặc repo ứng dụng:

1. **COPY ra, không MOVE đi.** File gốc phải ở lại xưởng. Sau khi copy, xưởng
   vẫn là bản thiết kế tham chiếu.
2. **Không sửa ngược.** Chi tiết triển khai (tên bảng, endpoint, quyền) thuộc về
   bản copy ở ngoài. Không mang chúng về sửa file xưởng.
3. **Ghi mỏ neo hai đầu.**
   - Trước khi copy: `mcp-writes-git snapshot "copy <ten-file> sang <dich>"`
   - Ở bản copy: ghi commit nguồn của xưởng vào header file hoặc README của repo đích.
4. **Xưởng không bao giờ là output.** Không build, không generate, không đồng bộ
   ngược từ repo ứng dụng về đây.
5. **Cần đổi thiết kế thì đổi ở xưởng trước**, rồi copy lại ra. Không sửa ở bản
   ngoài rồi mới nhớ ra phải cập nhật xưởng.

Chiều duy nhất được phép:

```text
xưởng vẽ  ──copy──▶  repo ứng dụng / PG / API
xưởng vẽ  ◀──────    KHÔNG BAO GIỜ đi ngược
```


## Màn hình đã loại — Owner xác nhận 12/09/2026

Danh mục riêng: [Màn hình đã loại](man-hinh-da-loai.html), mở bằng mục **Đã loại** màu đỏ ngay sau **Master** trên cùng thanh. Owner yêu cầu đặt tại đây để người và AI luôn tìm lại được qua các phiên. Các màn cũ chỉ tra cứu qua danh mục này, không đưa trở lại các mục MOW/MOT/MOIT/MOUT/Master. Khi hoàn tất dọn các màn cũ, gỡ luôn mục Đã loại theo chỉ đạo Owner.

- `mow-master-v1.html`: **ĐÃ LOẠI**, thiết kế cũ; đã gỡ khỏi menu MOW, Master và lối vào tại Master tổng. URL cũ còn dải đỏ lớn cho người và AI nhận biết.
- File còn tại chỗ để truy nguồn, chưa xóa. Chưa chỉ định URL thay thế.
- Bổ sung các màn khác vào đúng danh mục này khi Owner chỉ định; không tự loại theo suy đoán.

- 13/09/2026: Owner loại `modt-builder-v1.html`. Tra cứu tại `man-hinh-da-loai.html#modt-builder-v1`; URL gốc giữ nguyên, có cảnh báo đỏ. Gỡ khỏi menu MOT và danh mục UI hiện hành. Chưa xóa file.

## UI con và tìm kiếm chung · UI-B01 · 16/09/2026

- `child-ui-registry.json`: bản xuất danh mục chuẩn từ HTML Từ thực tế đã làm trên máy Owner; 29 mã UI-001…UI-029. Giữ mã khi đổi tên/URL. UI con chưa có bản riêng chỉ liên kết mẫu cha.
- `danh-muc-ui-con-v1.html` + `.js`: tra mã/tên, mở đúng UI; phân biệt màn hiện có, mẫu chờ áp dụng và khung mới.
- `child-ui-badge.js`: gắn mã UI con và lối vào tìm kiếm qua eco-nav, không đổi renderer nghiệp vụ.
- `tim-kiem-chung-v1.html` + `.js`: UI-029, một khung từ khóa/nâng cao theo tầng/loại. MOIT và MOUT riêng ở T0,5.
- `search-demo-data.json`: dữ liệu minh họa công khai cho thử thiết kế, không là dữ liệu vận hành.

Trạng thái: khung mới chờ Owner xem; nhãn/config/quyền và kết nối nguồn thật chưa nghiệm thu. Tìm kiếm nội bộ không gửi dữ liệu Google. Kết quả hiện mở UI tầng/loại (task có ngữ cảnh khi có); chưa cam kết định vị từng bản ghi thật. Bước tiếp: Owner rà UI-029 rồi kiểm nhãn UI con theo mã. Khi sửa danh mục, cập nhật tại HTML chuẩn và xuất lại registry này cùng lượt.

UI-B02: danh mục UI con một bảng 7 cột theo MOW/MOT/MOIT/MOUT/FIELD/T3–T7/Dùng chung. Bản chuẩn trong UI Master, dưới mẫu cha. Mã giữ nguyên; đếm mỗi UI một lần dù dùng nhiều bước. Kanban có 🔍 Tìm kiếm đầu hàng Thường/Đề xuất/Vận hành.

## UI-B03 · MOIT/MOUT dùng nguyên mẫu cha · 16/09/2026
- `moit-master-v1.html` UI-013, `mout-master-v1.html` UI-014: dùng nguyên Master MOT và shared Master renderer; nhãn/dữ liệu theo mẹ.
- `moit-studio-v1.html` UI-015, `mout-studio-v1.html` UI-016: dùng nguyên Studio MOT, F/L/E/C cùng nguồn.
- `moit-config-v1.html` UI-017: dùng nguyên New MODT, nhãn nhập liệu; URL edit được giữ.
- `ui-child-from-parent-v1.js`: nạp đúng nguồn cha tại thời điểm mở, không fork CSS/renderer. `ui-child-content-v1.js`: chỉ dữ liệu/nhãn/đường dẫn theo mẹ.
- Menu MOIT/MOUT có các entry riêng; Master MOUT tổng trỏ về UI-014.
Trạng thái: UI con được dựng, dùng dữ liệu mẫu; hợp đồng nhãn/config và PG chưa nghiệm thu. Field UI-018/UI-022 ngoài phạm vi lần này. Chuẩn và kiểm đếm cập nhật tại HTML chính của Owner.

## T0,5 / T0 · 16/09/2026
- Kanban chính: cùng 10 nút tầng ở Thường, Đề xuất, Vận hành, Quản trị; MOIT/MOUT là hai nhánh riêng ở T0,5.
- `lower-tier-navigation-v1.js`: Config/New MODT (và MOIT Config dùng mẫu này) dẫn các tầng thấp về Kanban gốc, giữ chế độ. Không nhân renderer hoặc sửa thiết kế T1.
- `kanban-field-v1.js`: UI-018 khai báo Field qua dấu + T0; dùng CSS/modal/form có sẵn. Tên, định dạng, mô tả, nhóm quản lý; context task/form tự lấy. Field là tầng cuối, không sinh tầng con.
- Dữ liệu đề xuất trong sessionStorage của trình duyệt, tách task/MOIT/MOUT; chỉ hiển thị trong Đề xuất, không coi là dữ liệu Vận hành. Nhóm quản lý minh họa từ phòng ban; chưa nối PG/quyền/luồng duyệt.
- `master-list.js` dùng chung: cây/bộ lọc có T0,5 (MOIT/MOUT) và T0; không đổi cột bảng. Thiếu field data thì để trống.
- Registry UI-B04: UI-018 có khung, còn rà nhãn/config; UI-022 Master Field vẫn chưa có bản riêng. Các mẫu cha khác giữ nguyên.

## UI-B05 · UI đã có · 16/09/2026
`field-master-v1.html` UI-022 dùng nguyên nguồn Master list qua adapter nhãn/dữ liệu chung; khai báo/sửa nối UI-018 theo mã Field. Bộ dữ liệu minh họa MOIT của T01. Owner xác nhận UI-029 tìm kiếm OK. Registry: 29/29 có khung UI, không đồng nghĩa hoàn tất nhãn/config/PG. Nguồn chuẩn kiểm đếm vẫn là tài liệu local; bảng con đã chuyển sang dựng trạng thái từ registry để tránh nhãn cũ.

17/09: UI-029 có nút Quay lại; child-ui-badge truyền return cùng tầng/chế độ/ngữ cảnh. Chỉ nhận đường dẫn cùng hệ. Đã kiểm browser Đề xuất/Thường ở T0,5 MOUT.

## T1 Đề xuất — khôi phục toàn bộ Config · 17/09/2026
Owner xác nhận Config đầy đủ là phần tiêu chuẩn của Kanban T1 Đề xuất.
`t1-proposal-config-v1.js` + `.css`: nguồn chung tách từ New MODT, gồm bảng
kết nối, căn hàng và ba phần Nguyên tắc giao việc / Ai làm & ai nhận / Chạy & kết thúc.
Kanban và New MODT cùng sử dụng; T1 Thường giữ renderer hiện có. Không nhân bản UI.
Nguyên nhân thiếu: nhánh render Đề xuất ở Kanban chỉ dựng MOIT/MOUT rồi return;
AGENTS và chuẩn T1 cũ còn yêu cầu một cột. Đã cập nhật cả hai theo Owner.
Kiểm trên VPS: Kanban proposal row-sync=ok, modules=3; T1 Thường audit=ok;
T2 Đề xuất cards=6, config=false; New MODT proposal row-sync=ok, modules=3.
Bẫy đã gặp trong lượt tích hợp: hai trang có cấu trúc editSt khác nhau;
đã sửa adapter đọc editor, rồi tải lại kiểm. Đây vẫn là UI mẫu, chưa nối PG.


## T1 Đề xuất · danh sách dọc và thêm mới · Owner 17/09/2026
T1 Đề xuất hiển thị các task theo chiều dọc: thu gọn còn một dòng, mở task hiện toàn bộ Config hai cột. Dấu + trước/giữa/sau dùng lại form thêm mới; tạo task đồng thời có MOIT/MOUT, bảng bên phải và ba nhóm Config. Một task mở tại một thời điểm.
Nguồn giữ nguyên: `t1-proposal-config-v1.js/.css`; cả Kanban và New MODT cùng gọi. Không thêm file UI hoặc loại view. Task mới trống, đề xuất lưu minh họa trong sessionStorage theo nhiệm vụ; chỉ chiếu ở Đề xuất. Thu gọn/đổi task giữ DOM Config riêng trong phiên. Chưa nối PG/duyệt thật. Chuẩn audit bỏ qua workspace đã bị thay khỏi DOM, vẫn kiểm workspace đang hiện.
