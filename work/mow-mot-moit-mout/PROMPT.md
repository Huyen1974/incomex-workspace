# PROMPT — MMIM-MOM01 · Master of Master đúng UI cha

RUN_ID: MMIM-MOM01-20260927-03
STATUS: Chỉ chạy sau READY đúng commit cuối chạm PROMPT.md và lệnh RUN của Owner/GPT Host.

Host: GPT Chat · Host_ID `GPT-MMIM-260920-A`
Executor_Surface: Codex
Repo_Write: `workspace_*` · root `workspace`
UI_Write: `workspace_*` · root `ui`
GitHub native/App/API/CLI: READ-ONLY.

## 0. Đọc đúng, không khảo sát lan man

Đọc:
1. `AGENTS.md` + README D12 của root `workspace`.
2. `work/mow-mot-moit-mout/COLLAB.md` §0 + D44 + D46 + D49–D52 + KQ RUN -02.
3. File prompt này.
4. Root `ui`: `AGENTS.md`, `README.md`, rồi CHỈ các file:
   - `eco-nav.js`
   - `master-list.js`
   - `mot-theme-v1.css`
   - `mot-master-v1.html`
   - `ui-child-from-parent-v1.js`
   - `ui-child-content-v1.js`
   - `field-master-v1.html`
   - `child-ui-registry.json`
   - `master-of-master-v1.html`

Không đọc lại kho lịch sử để “nghiên cứu thêm 84 Master”. Dữ liệu 84 dòng đã có trong
`master-of-master-v1.html#catalog-data` của RUN -02 và **phải dùng lại nguyên liệu đó**.

Nếu các file/sha hiện hành đã đổi làm các khẳng định dưới đây sai → DỪNG, ghi blocker; không tự chọn UI cha khác.

## 1. Hai quyết định đã khóa

### 1A. UI cha của Master

Trong RUN này, UI.MASTER canonical được khóa như sau:

- renderer chung: `master-list.js`;
- theme chung: `mot-theme-v1.css`;
- shell/parent live đang dùng: `mot-master-v1.html`;
- cơ chế UI con: `ui-child-from-parent-v1.js` + `ui-child-content-v1.js`.

Căn cứ hiện hành: `mot-master-v1.html` có ✅ trong `eco-nav.js`; các Master Field/MOIT/MOUT hiện đang tải parent này qua `ui-child-from-parent-v1.js`.

**CẤM dùng làm cha:** `master-hub.html`, `mow-master-nhap2-v1.html`, màn demo/cũ/tham khảo, hoặc bất kỳ trang nào chỉ “trông giống Master”.
Các file đó được giữ để tra nguồn, không phải parent mới.

Quy tắc Owner: UI con **giống tuyệt đối cha về shell/layout/cột/font/khoảng cách/màu/icon/nút/cách mở detail/cách lọc**. Chỉ được thay **nhãn + dữ liệu + link đúng đối tượng**. Không fork CSS/renderer.

### 1B. Dấu xanh / đỏ ở 4 Mẹ

Trong đúng các menu **MOW · MOT · MOIT · MOUT**:
- mục bắt đầu bằng `✅` = đang được dùng;
- mục không có `✅` = **không dùng, chỉ giữ để tham khảo**.

Tại baseline hiện tại phải có đúng 7 mục không xanh:
1. MOW · `MODW · Biến MOW chạy được`
2. MOT · `Quy trình MOT`
3. MOT · `Cấu trúc table`
4. MOIT · `MOIT · Tạo form nhập liệu`
5. MOIT · `MODIT · Biến MOIT chạy được`
6. MOIT · `Kiến trúc input → DB`
7. MOUT · `MODUT · Biến MOUT chạy được`

Nếu không còn đúng 7 → DỪNG trước sửa menu.

## 2. Việc chính — Master of Master

Mục tiêu cực đơn giản:

> **Một Master list gốc, chứa tên của tất cả các Master khác.**

Không làm lại inventory. Không thiết kế dashboard mới.

### 2.1 Giữ URL, bỏ renderer riêng

Giữ URL:
`/ui-preview/mcp-writes/master-of-master-v1.html`

Nhưng biến file này từ page tự vẽ thành **UI con của UI.MASTER**:
- không có CSS riêng;
- không copy `master-list.js`;
- không copy DOM/list renderer;
- wrapper theo cùng nguyên tắc như `field-master-v1.html`;
- được giữ dữ liệu 84 dòng inline nếu cần, vì đó là data chứ không phải renderer.

Được sửa tối thiểu:
- `master-of-master-v1.html`
- `ui-child-from-parent-v1.js` — chỉ thêm config cho page này;
- `ui-child-content-v1.js` — chỉ thêm adapter label/data cho page này;
- `eco-nav.js` — mục 3 bên dưới.

**Không sửa:** `master-list.js`, `mot-theme-v1.css`, `mot-master-v1.html`.

### 2.2 Dữ liệu

Đọc JSON hiện có trong `#catalog-data`, phải accounted **84/84**.
Không đổi mã/tên, không merge hai dòng nghi trùng, không query lại PG/Directus.

Mặt người trước tiên cần:
- tiêu đề: **Master of Master · Danh sách tất cả Master**;
- thấy ngay **84 Master**;
- bảng theo đúng UI cha;
- cột/nhãn có thể đổi nghĩa cho phù hợp nhưng **không đổi số cột, vị trí, kích thước, kiểu hiển thị**;
- tối thiểu phải thấy rõ: **Mã · Tên Master · Nhóm · Quản lý gì · Tình trạng**;
- thông tin chưa có để OPEN/đang hoàn thiện; không bịa để lấp ô.

Dữ liệu chi tiết Thiết kế/Config/UI/Nguồn từ RUN -02 phải **không mất**, nhưng được để ở detail/drawer hoặc metadata; không đổ lên mặt đầu.

Không có nút “Tạo Master” trong RUN này.

### 2.3 “Nhìn cái hiểu ngay” nhưng không phá cha

D46 trong RUN này đạt bằng **chính ngôn ngữ UI.MASTER**, không thêm dashboard/card riêng:
- title nói đây là danh sách gốc;
- summary nói tổng 84 và tình trạng tổng hợp ngắn;
- search/filter của parent hoạt động;
- bảng bắt đầu ngay, tên Master là thông tin chính;
- chi tiết mở khi bấm.

Nếu muốn thêm thành phần UI chưa tồn tại ở cha → KHÔNG làm; ghi gap cho Host.

## 3. Việc phụ — đánh đỏ UI không dùng

Chỉ sửa `eco-nav.js`, đúng 7 mục §1B:
- label thành `🔴 KHÔNG DÙNG · <tên cũ>`;
- description thêm `Chỉ tham khảo · ` trước mô tả cũ;
- **giữ nguyên URL** để còn tra lịch sử/thông tin.

Không đổi bất kỳ mục ✅ nào.
Không chạm nhóm Master/Đã loại trong bước này.
Thêm một comment ngắn ở đầu `eco-nav.js`: Owner 27/09/2026 — trong 4 Mẹ chỉ mục ✅ được dùng; 🔴 chỉ tham khảo.

Mục `✅ Master of Master` hiện có giữ nguyên label/URL, nhưng chỉ được coi PASS khi §2 đã chuyển đúng parent.

## 4. Kỷ luật sửa

- Stat/version/hash trước mọi file sửa.
- `workspace_edit/transaction` với expected_version + operation_id.
- Không delete/move.
- Không tạo file mới.
- Không reformat file chung.
- Shared loader/adapter chỉ thêm nhánh nhỏ cho Master of Master; existing child behavior phải giữ.
- Không production PG/Directus/runtime.
- Không sửa `ban-duyet.html` trong RUN này: map MOM01 đã có sẵn.
- Nếu phát hiện cần sửa renderer cha để làm được → DỪNG, không tự sửa cha.

## 5. Acceptance

1. `master-of-master-v1.html` mở HTTP 200, console error do RUN = 0.
2. Source file Master of Master **không có renderer/CSS riêng**; dùng parent `mot-master-v1.html`.
3. Runtime xác nhận parent source = `mot-master-v1.html`.
4. Hash `master-list.js`, `mot-theme-v1.css`, `mot-master-v1.html` không đổi.
5. 84/84 row accounted; mã + tên khớp dữ liệu RUN -02.
6. Owner nhìn đầu trang biết ngay: đây là **Master list gốc** và có **84 Master**.
7. Search mã/tên hoạt động; mở ít nhất 1 detail hoạt động.
8. 1280px và 390px không có regression/tràn ngang mới.
9. `field-master-v1.html`, `moit-master-v1.html`, `mout-master-v1.html` vẫn mở và dùng parent như trước.
10. Trong MOW/MOT/MOIT/MOUT có đúng **7 label 🔴 KHÔNG DÙNG**, đúng danh sách §1B.
11. Tất cả mục ✅ cũ giữ nguyên label + URL; `✅ Master of Master` mở đúng page đã sửa.
12. Không file mới; không PG/Directus; không sửa renderer/theme/parent.
13. Ghi vào COLLAB:
`KQ@MMIM-MOM01-20260927-03 XONG`
hoặc
`KQ@MMIM-MOM01-20260927-03 DỪNG`

Dòng báo Owner khi XONG:
`XONG · MMIM-MOM01-03 · masters=84/84 · parent=UI.MASTER · red_reference=7/7 · regressions=0 · url=<url> · sha=<sha>`

## 6. Dừng sau RUN

XONG cũng **không làm tiếp Step/UI/Tool/Process**.
Owner phải nhìn Master of Master trước rồi mới chỉ đạo vòng sau.
_new`; dùng theme/navigation/component hiện có khi phù hợp, không tạo design system mới và không nhân bản renderer chung nếu đã có component dùng lại được.
3. Nạp catalog data của RUN và nghiệm thu standalone: HTTP 200 · console sạch · D46 Tầng 1/2/3 · responsive.
4. **Chỉ sau PASS bước 3**, sửa `eco-nav.js` bằng `workspace_edit`/transaction với expected_version, target DUY NHẤT; thêm đúng **entry đầu tiên** trong `Master.children`:
   - **✅ Master of Master**
   - mô tả: **Danh mục tất cả Master**
   - href: `master-of-master-v1.html`.
5. Không đổi/xoá/reorder các Master entry cũ ngoài việc chèn entry mới ở đầu. Không sửa `master-hub.html` trong RUN này.
6. Nếu target menu không duy nhất, version lệch, hoặc cần sửa lớn file hiện hữu → **không cố làm**; giữ page standalone, ghi `LINK_BLOCKED` và DỪNG/PARTIAL để Host xử lý.
7. Regression-check toàn eco-nav và ít nhất UI mẹ MOW + `master-hub.html`; FAIL → rollback đúng delta của RUN.

**Luật snapshot xưởng:** `ui/AGENTS.md` yêu cầu snapshot thủ công trước/sau **thay đổi lớn**. RUN này cố ý giới hạn existing-file mutation ở một hook nhỏ. Nếu Codex phát hiện phải thay đổi lớn file hiện hữu, chỉ được tiếp tục khi surface có capability tạo mỏ neo theo luật xưởng; nếu không → DỪNG.

### A2. Dữ liệu đầu vào

Nguồn đầu tiên bắt buộc:
- **84 ứng viên** hiện có trong tab Master list / tài liệu MMIM;
- Master/UI đã có trong UI mẹ;
- registry/catalog hiện có đọc được qua nguồn chỉ đọc;
- quyết định/nguồn trong COLLAB hiện hành.

Không:
- coi 84 là con số cuối;
- tự xoá/gộp row vì thấy giống nhau;
- tự đổi mã cũ;
- tự tuyên bố Master “đạt” khi thiếu bằng chứng.

Mỗi ứng viên trong 84 phải được **accounted**:
- một row riêng; hoặc
- nếu nghi trùng thì vẫn giữ row + cờ `DUP_CANDIDATE` + liên kết row nghi trùng.
Không mất row âm thầm.

### A3. Trạng thái Master — tách các trục, không gộp mơ hồ

Chi tiết mỗi Master tối thiểu quản lý:

`Mã · Tên · Nhóm · Quản lý gì · Thiết kế · Config · UI · Nguồn/đối chiếu · Tổng · Vấn đề · Link`

Bộ trạng thái chuẩn V1:

**Thiết kế**
- `CHUA_THIET_KE`
- `DANG_THIET_KE`
- `DA_THIET_KE`
- `DA_RAT_THIET_KE`

**Config**
- `CHUA_RAT_CONFIG`
- `DANG_RAT_CONFIG`
- `DA_RAT_CONFIG`
- `CONFIG_CO_VAN_DE`

**UI**
- `CHUA_CO_UI`
- `CO_UI`
- `UI_DA_KIEM`

**Nguồn/đối chiếu**
- `CHUA_RO_NGUON`
- `CO_NGUON`
- `DA_DOI_CHIEU`

**Tổng — chỉ để người nhìn nhanh, dẫn xuất từ các trục trên**
- ⚪ `CHUA_LAM`
- 🟡 `DANG_LAM`
- 🔴 `CO_VAN_DE`
- 🟢 `SAN_SANG`

Không tự đặt `SAN_SANG` nếu các trục bắt buộc chưa đạt.

### A4. Tầng 1 của Master of Master

Phải nhìn được mà không đọc bảng dài:

- Tổng số ứng viên hiện có.
- Số nhóm Master.
- ⚪ Chưa làm.
- 🟡 Đang làm.
- 🔴 Có vấn đề.
- 🟢 Sẵn sàng.
- Số nghi trùng.
- Số chưa rõ nguồn/config/UI.
- “Cần xem ngay”: chỉ các nhóm/row có vấn đề.

Có thể dùng card + biểu đồ đơn giản + bảng ngoại lệ; không dùng chart trang trí không giúp ra quyết định.

### A5. Tầng 2

Theo nhóm Master:
- tên nhóm;
- tổng;
- số bình thường;
- số OPEN/vấn đề;
- click để lọc danh sách dưới.

Codex được đề xuất grouping dựa trên dữ liệu hiện có nhưng:
- grouping phải có quy tắc rõ;
- chưa chắc thì gắn `GROUP_OPEN`;
- không biến grouping đề xuất thành quyết định cuối của Owner.

### A6. Tầng 3

Bảng đầy đủ, search/filter:
- filter theo nhóm;
- filter theo Tổng;
- filter riêng từng trục Thiết kế/Config/UI/Nguồn;
- tìm theo mã/tên;
- click link UI con nếu có;
- row chưa có link phải hiện rõ `CHUA_CO_UI`, không giấu.

## 4. PHẦN B — gom các danh mục còn lại thành việc cụ thể

Sau khi Master of Master V1 mở được, rà nguồn hiện có và cập nhật **bản đồ GitHub** trong các tab/khối sẵn có của `ban-duyet.html`. Không thêm tab mới.

### B1. Step sử dụng Máy

Chỉ lấy **step người dùng sử dụng Máy tạo quy trình**.
Không trộn:
- step xây Nhà máy;
- step của tool kiểm;
- step vận hành hạ tầng.

Mỗi row:
`Mã Step · Người làm gì · Đầu vào · Kết quả · UI đang dùng/cần · Trạng thái · Nguồn · Gap`

Từ nguồn hiện có:
- rà số “60 bước” cũ;
- phân loại lại;
- không coi 60 là đáp án.

Kết quả phải có:
- count tổng row đã phân loại;
- count thật sự thuộc “Step sử dụng Máy”;
- count còn OPEN;
- danh sách gap cụ thể.

### B2. UI catalog

Mỗi row:
`Mã UI · Tên · Step sử dụng · loại UI · URL VPS · version/hash · trạng thái thiết kế · trạng thái kiểm · gap`

Luật:
- actual UI HTML/CSS/JS nằm VPS `ui` theo D44;
- GitHub chỉ giữ map/link/status;
- một UI dùng nhiều Step chỉ tính một UI;
- UI cũ 29/18 chỉ là input để rà, không là đáp án cuối.

### B3. Tool catalog

Rà ít nhất:
- 28 ứng viên hiện có;
- 17 phạm vi kiểm;
- các cổng/tool đã dùng thật.

Mỗi row:
`Mã · Tên · Check gì · Input · Output · Nguồn · Đã thử? · Sẵn dùng? · Vấn đề · Ai giữ nếu biết`

Phải làm nổi:
- phạm vi trống;
- tool chồng;
- tool chỉ có tên nhưng chưa chạy;
- tool đã thử nhưng chưa đạt “sẵn dùng”.

Không tự viết hàng loạt tool mới trong RUN này trừ khi cần một thay đổi rất nhỏ để chính Master of Master hoạt động và đã được scope cho phép.

### B4. Quy trình của Nhà máy chế tạo Máy

Chỉ gom **quy trình phục vụ xây/kiểm/phát hành/bảo trì Máy tạo quy trình**.
Không trộn quy trình thương mại.

Mỗi row:
`Mã · Tên · Mục đích · Input · Output · Công cụ dùng · Trạng thái · Nguồn · Gap`

Rà toàn bộ quy trình đã có trong MMIM/COLLAB/ban-duyet.
Kết quả:
- count đã tìm thấy;
- count có nguồn;
- count đã thử/chứng minh;
- count còn thiếu/OPEN;
- nhóm gap cụ thể.

Không bịa cho đủ “100+”. Chỉ ghi số thật từ nguồn; phần chưa có trở thành backlog có tên/phạm vi cụ thể.

## 5. PHẦN C — GitHub chỉ giữ bản đồ, không nhét UI nặng

Sau UI mutation, cập nhật `work/mow-mot-moit-mout/ban-duyet.html` và `COLLAB.md`:

**GitHub/workspace giữ:**
- mã;
- tên;
- nhóm/loại;
- trạng thái;
- quan hệ Step↔UI / phạm vi tool / phạm vi process;
- URL VPS;
- version/hash;
- vấn đề/gap;
- quyết định.

**Không copy toàn bộ HTML/CSS/JS của Master of Master vào repo.**

Trong tab Master list:
- đặt đường link rõ tới Master of Master;
- ghi URL VPS + hash/version;
- ghi trạng thái thực tế, không “đã xong” giả.

Trong ★ Ý kiến HĐ:
- 06 D44 chỉ chuyển trạng thái thực thi khi bằng chứng đạt;
- 01 Master list **không tự CLOSED**; RUN này cung cấp UI + dữ liệu để Claude/Owner rà và chốt danh sách cuối.
- D46: đánh dấu “Master of Master đã áp D46” chỉ khi nghiệm thu Tầng 1/Tầng 2/Tầng 3 PASS.

## 6. Vòng làm việc từ sau RUN — chống quay lại bàn chung

Sau inventory:
- mọi thiếu sót phải là **row có mã/nhóm/trạng thái/gap**;
- NEXT chọn từng nhóm/row để hoàn thiện;
- không tạo thêm “ý tưởng chung” nếu không chỉ được nó cập nhật row nào;
- thứ đã thiết kế/config/UI rồi phải dùng lại, không làm lại từ đầu.

Mục tiêu dài hạn:
- Master, Step, UI, Tool, Factory Process đều dần đi từ `CHUA_LAM → DANG_LAM → CO_VAN_DE/SAN_SANG`;
- số OPEN phải giảm qua các RUN;
- Owner luôn nhìn được tổng thể ở Tầng 1.

## 7. Safety / không được làm

- Không ghi production PG/Directus.
- Không sửa code runtime ngoài root `ui`.
- Không dùng GitHub native để ghi.
- Không đổi mã cũ chỉ để đẹp.
- Không xoá row/file cũ.
- Không tự tạo thêm tab của Owner View.
- Không tự đóng 01–05 chỉ vì đã có danh sách.
- Không đánh dấu “✅” cho cả Master nếu chỉ mới dựng hub.
- Không cài package/library mới nếu không cần; nếu thiếu thư viện cho screenshot thì dùng công cụ đã có hoặc báo rõ, không cài production.
- Không biến mock/design thành production claim.
- Với file UI mẹ đang được dùng chung: diff phải **tối thiểu**, chỉ chạm block cần cho Master of Master; không format/rewrite toàn file cho đẹp.
- Trước/sau mỗi file UI sửa phải có sha256/version; báo rollback target rõ. Không có before-hash → không mutation file đó.

## 8. Acceptance — Host sẽ nghiệm thu từng mục

### Gate/UI
1. Read-gate `workspace_*` PASS.
2. Read-gate root `ui` PASS.
3. `master-of-master-v1.html` PASS standalone **trước khi** sửa UI mẹ.
3a. UI mẹ trước/sau không mất các tầng/tab/chức năng hiện có; diff UI mẹ chỉ là link/hook tối thiểu.
4. Menu Master có **✅ Master of Master** ở vị trí đầu.
5. Tích xanh có mô tả/semantics rõ: hub tồn tại, không phải toàn bộ Master hoàn tất.
6. Link Master of Master mở HTTP 200.
7. Console của UI mới không có lỗi JS do thay đổi RUN gây ra.
8. 1280px và 390px không tràn ngang không kiểm soát.
8a. Ảnh/inspect 1280px **không scroll** nhìn thấy tổng số · số nhóm · 4 trạng thái tổng · khu “Cần xem ngay”; chi tiết 84 row nằm dưới.
8b. Click ít nhất 01 card/cảnh báo Tầng 1 lọc/đưa tới đúng Tầng 2/3.
8c. Có before/after hash cho mọi file root `ui` đã sửa; regression check của UI mẹ PASS.

### Dữ liệu Master
9. 84/84 ứng viên đầu vào được accounted; không row nào biến mất.
10. Mỗi row có Mã/Tên/Quản lý gì hoặc ghi rõ `OPEN`.
11. Có đủ 4 trục Thiết kế/Config/UI/Nguồn + Tổng dẫn xuất.
12. Nghi trùng được đánh cờ, không tự merge/xoá.
13. Item đã có UI/config/source phải gắn bằng chứng/link thật khi nguồn cho phép.
14. Tầng 1 trả lời được count + nhóm + vấn đề + chỗ cần xem.
15. Tầng 2 lọc theo nhóm.
16. Tầng 3 search/filter + row detail/link.

### 4 danh mục còn lại
17. Step catalog có count + row + gap, tách khỏi step Nhà máy.
18. UI catalog có Step↔UI + URL/version/hash, không copy UI code vào GH.
19. Tool catalog phản ánh tối thiểu 28 ứng viên/17 phạm vi và chỉ ra vùng trống/chồng.
20. Factory Process catalog tách khỏi quy trình thương mại, có count thật và gap cụ thể.

### D46 / SSOT
21. Tầng 1 Master of Master có đúng cấu trúc **4 thẻ chính + dải trạng thái + tối đa 5 “Cần xem ngay”** trước bảng chi tiết.
22. Master of Master áp 3 tầng D46; bảng 84 row không nằm trên Tầng 1.
23. VPS `ui` là nguồn UI thiết kế; GH chỉ map/link/status.
24. Không production mutation.
25. Không file/task/repo mới ngoài tối đa 01 UI file VPS đã được Owner cho phép.

### Báo cáo/KQ
26. Ghi trong `COLLAB.md`:
   `KQ@MMIM-MOM01-20260927-02 XONG` hoặc `DỪNG`.
27. Báo cáo một dòng cuối:
   `XONG · MMIM-MOM01 · masters_input=<n> · accounted=<n> · groups=<n> · issues=<n> · steps=<n> · uis=<n> · tools=<n> · factory_processes=<n> · mom_url=<url> · mom_sha=<sha> · D46=PASS|PARTIAL`
28. Nếu PARTIAL/DỪNG: nêu đúng blocker + phần đã giữ được; không tự mở scope khác.

## 9. Nghiệm thu bằng mắt bắt buộc

Trước KQ XONG:
- chụp/inspect Master of Master Tầng 1 ở 1280px **trước khi scroll**;
- ảnh đầu phải tự chứng minh nhìn thấy: **tổng số · số nhóm · ⚪/🟡/🔴/🟢 · tối đa 5 mục “Cần xem ngay”**;
- Host/Owner phải có thể nhìn thấy ngay tổng số, nhóm, cảnh báo và nơi bấm tiếp;
- kiểm Master menu có ✅ Master of Master;
- kiểm một row có UI thật mở được;
- kiểm một row chưa có UI hiện rõ `CHUA_CO_UI`;
- kiểm một nghi trùng không bị merge mất;
- kiểm filter nhóm + trạng thái.

Nếu UI kỹ thuật đúng nhưng lớp trên vẫn buộc User đọc bảng dài để tìm vấn đề → **D46 FAIL**, không KQ XONG.

## 10. Kết thúc

Agent chỉ trả một trong hai:
- `XONG · MMIM-MOM01 · <metrics như §8>`
- `DỪNG · MMIM-MOM01 · <blocker ngắn>`

**MODE = MANUAL_OWNER:** không tạo watcher/automation/webhook, không tự sửa PROMPT cho vòng sau, không tự phát RUN kế tiếp. Sau KQ phải dừng và chờ Owner/GPT Host điều hành.

Không viết thêm bài luận trong chat; Host sẽ đọc repo/UI để nghiệm thu.
