# PROMPT — MMIM-MOM01 · Master of Master + hệ danh mục chế tạo Máy

RUN_ID: MMIM-MOM01-20260927-01
STATUS: Chỉ thực thi sau READY đúng SHA commit cuối chạm file này và RUN của Owner/GPT Host.

Host: GPT Chat · Host_ID `GPT-MMIM-260920-A`
Executor_Surface: **Codex** trên bề mặt có Incomex VPS MCP + gateway workspace.
Report_Write_Path: **workspace_*** · root `workspace` · repo `Huyen1974/incomex-workspace` · main.
UI_Write_Path: **fs_*** · root `ui` · VPS `/opt/incomex/docs/mcp-writes/` → public `/ui-preview/mcp-writes/`.
GitHub native/App/API/CLI: **READ-ONLY**, cấm dùng để ghi repo.

## 0. Gate bắt buộc

1. Một read-gate cho `workspace_*`: đọc đúng `AGENTS.md` → `README.md` phần D12/§11/§12 → `work/mow-mot-moit-mout/COLLAB.md` (§0, D44–D47, Dòng hiện hành) → file prompt này.
2. Một read-gate cho root `ui`: đọc/inspect ít nhất:
   - `mow-unified-canvas-v2.html`
   - các CSS/JS mà chính file đó đang gọi cho Master/Kanban/List nếu có;
   - link mẫu Owner đang dùng: `https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/mow-unified-canvas-v2.html?tang=T2&che-do=thuong`.
3. READY phải khớp **commit cuối chạm PROMPT.md**, không so HEAD chung.
4. Thiếu `workspace_*` hoặc root `ui`, không đọc được UI mẹ, hoặc phát hiện D44/D46 bị thay thế bởi quyết định mới hơn → **DỪNG trước mutation**.
5. Không sửa production PG/Directus, service, nginx, compose, auth, MCP, connector. Chỉ đọc nguồn production khi cần đối chiếu.
6. Không tạo task/repo/project mới. Không tạo framework/library/pipeline mới.
7. Owner đã cho phép **một đầu mối UI “Master of Master” trên VPS ui** và tối đa **01 file UI mới**. Kiến trúc mặc định của RUN: dựng **`master-of-master-v1.html`** riêng ngay root `ui`, nhưng reuse style/component/shell hiện có của UI mẹ; **chỉ sau khi file mới PASS standalone mới sửa UI mẹ đúng một điểm: thêm link ✅ Master of Master**. Không nhét toàn bộ logic/view mới vào UI mẹ trừ khi source hiện tại đã có extension point rõ ràng và phương án đó thực sự ít diff hơn.
8. Không xoá/move UI cũ trong RUN này. D44 “nơi lưu UI ở VPS” không phải quyền dọn lịch sử.
9. Trước mọi mutation root `ui`: ghi lại **path · version/hash · sha256** của từng file sẽ sửa. Mọi ghi phải dùng expected version/lock của cổng; sau ghi kiểm lại. Nếu regression do RUN → khôi phục đúng version trước của **chính file RUN đã sửa**, không đụng file người khác.

## 1. Mục tiêu RUN

Không tiếp tục bàn lý thuyết chung. RUN này phải tạo **đầu mối nhìn được và dùng được** để từ đó hoàn thiện dần toàn bộ “Nhà máy chế tạo Máy tạo quy trình”.

Kết quả chính:

**A. Master of Master V1**
- Một đường vào duy nhất trong UI mẹ, dưới mục **Master**, hiển thị **✅ Master of Master** ở vị trí đầu.
- Tích xanh chỉ có nghĩa: **đầu mối Master of Master đã tồn tại và mở được**; tuyệt đối không có nghĩa toàn bộ Master bên dưới đã hoàn thiện.
- Bấm vào mở được màn **Master of Master** trên VPS, dùng lại style/shell/interaction hiện có của 4 UI mẹ tối đa có thể.
- Đây là nơi tập hợp tất cả Master hiện có/đang thiết kế/chưa hoàn thiện, và là đầu mối để sau này đi tới từng Master con.

**B. Hệ danh mục thực chiến**
Phải gom và chuẩn hoá dữ liệu hiện có thành 5 danh mục đang cần xử lý lâu dài:
1. Master list.
2. Step người dùng sử dụng “Máy tạo quy trình”.
3. UI.
4. Công cụ/check chéo.
5. Quy trình của **Nhà máy chế tạo Máy** — không trộn quy trình thương mại.

Mục tiêu không phải bịa đủ “hàng trăm” trong một lượt. Mục tiêu là:
- mọi thứ **đã có trong nguồn hiện tại** phải được tìm thấy, gắn mã/nhóm/trạng thái;
- mọi khoảng trống phải hiện thành **một dòng cụ thể cần làm tiếp**;
- từ sau RUN này, hội đồng/agent xử lý **từng dòng còn thiếu**, không quay lại tranh luận chung chung.

**CHECKPOINT BẮT BUỘC TRONG CÙNG RUN:** làm **PHẦN A trước**. Chỉ được sang PHẦN B khi Master of Master đạt tối thiểu acceptance **1–16**. Nếu A không đạt hoặc phải rollback → ghi KQ `DỪNG/PARTIAL`, giữ phần an toàn đã đạt và **không tiếp tục B**.

## 2. Nguyên tắc D46 — bắt buộc ở mọi view

Mọi màn cho người phải theo đúng:

**Tầng 1 · 10 giây Tổng quan → Tầng 2 · Theo nhóm ~1 phút → Tầng 3 · Chi tiết khi bấm**

Tầng 1 bắt buộc trả lời được:
1. Có bao nhiêu phần/nhóm?
2. Chỗ nào bất thường, thiếu, OPEN hoặc có vấn đề?
3. User cần xem/quyết/đi tiếp ở đâu?

Nếu phải đọc bảng dài mới biết vấn đề → **FAIL**, dù dữ liệu dưới đầy đủ.

Mặc định:
- phần đạt/bình thường được gập hoặc giảm nhấn;
- phần OPEN/trùng/thiếu/không rõ nguồn/không có UI phải nổi;
- màu luôn đi cùng chữ/ký hiệu, không dùng màu làm thông tin duy nhất.

**Bài kiểm D46 định lượng cho Tầng 1:**
- ở viewport 1280px, **không cuộn** vẫn thấy đủ **3 vùng cố định**:
  1. **4 thẻ chính:** Tổng Master · Số nhóm · 🔴 Có vấn đề · 🟢 Sẵn sàng;
  2. **1 dải trạng thái:** ⚪ Chưa làm · 🟡 Đang làm · 🔴 Có vấn đề · 🟢 Sẵn sàng;
  3. **“Cần xem ngay” tối đa 5 dòng** — chỉ ngoại lệ ưu tiên;
- số nghi trùng/chưa nguồn/chưa config/chưa UI đặt gọn trong “Cần xem ngay” hoặc badge phụ, không tạo thêm bảng số trên mặt đầu;
- **không hiển thị bảng 84 row trước các vùng trên**;
- không cần mở chi tiết vẫn trả lời được 3 câu D46;
- bấm từ card/cảnh báo ở Tầng 1 phải đi được xuống đúng Tầng 2/3 đã lọc;
- 390px được phép cuộn dọc nhưng **không cuộn ngang** để hiểu tổng quan.

## 3. PHẦN A — dựng Master of Master V1 trên VPS

### A1. Reuse UI mẹ nhưng cô lập rủi ro

Inspect UI mẹ trước để lấy đúng:
- breadcrumb/header/tabs/layout/màu/khoảng cách;
- component/card/table/search/filter đang có;
- Master popover/menu hiện tại.

**Thứ tự mutation bắt buộc:**
1. Tạo `master-of-master-v1.html` riêng trong root `ui`.
2. Reuse CSS/JS/component hiện có bằng import/link khi phù hợp; nếu phải chép block style nhỏ thì ghi rõ nguồn. Không dựng design system mới.
3. Nạp mock/catalog data của RUN và nghiệm thu standalone: HTTP 200 · console sạch · D46 Tầng 1/2/3 · responsive.
4. **Chỉ sau PASS bước 3**, tìm đúng extension point của Master popover/menu. Chỉ được sửa khi target:
   - xác định DUY NHẤT;
   - có before-version/hash;
   - thay đổi chỉ là đúng một link/hook:
     - **✅ Master of Master**
     - mô tả: **Danh mục tất cả Master**
     - href → file mới;
   - ghi qua **fs_transaction/expected-version** hoặc cơ chế atomic tương đương của cổng đã audit.
5. Nếu extension point không duy nhất, file đã lệch cấu trúc, hoặc không có transaction/version-lock → **không sửa UI mẹ**; giữ Master of Master standalone, ghi `LINK_BLOCKED` và KQ PARTIAL/DỪNG để Host xử lý. Không dùng search/replace mù.
6. Regression-check UI mẹ; FAIL → rollback UI mẹ về before-version, không cố vá tiếp trong cùng file mẹ.

UI mẹ không được chứa dữ liệu 84 Master hoặc logic catalog mới; nó chỉ giữ link/hook.

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
   `KQ@MMIM-MOM01-20260927-01 XONG` hoặc `DỪNG`.
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

Không viết thêm bài luận trong chat; Host sẽ đọc repo/UI để nghiệm thu.
