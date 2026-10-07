# FORMULA-AI-README · MMIM

## Quy chuẩn thị giác UI.MASTER — bắt buộc · Owner 07/10/2026

CE-20261007-MASTER-EMPHASIS · APPROVED theo yêu cầu Owner. Phạm vi: mọi Master hiện tại và tương lai dùng UI.MASTER; không đổi dữ liệu/khái niệm.
- **SSOT giao diện:** `ui/master-list.js`, khuôn `ui/mot-master-v1.html`. UI con chỉ khai dữ liệu, nhãn và cột; không tự dựng CSS hoặc tắt phân cấp thị giác.
- **Master định nghĩa:** cột **Tên** và **Trạng thái** (key `state`/`readiness`, khi có) là điểm nhấn đậm. Các cột STT, ID, Chuỗi, Bước, Tầng, tham chiếu và thông tin phụ giữ nhạt theo UI cha. Không làm mọi cột đậm. “Nhạt” không có nghĩa là ẩn hoặc vô hiệu hóa.
- Kế thừa đúng token hiện có: tên/trạng thái nội dung #1d1d1f, weight 700; tiêu đề chính #515154, weight 700; nội dung phụ #b0b0b5, weight 400; tiêu đề phụ #bcbcc1, weight 400. Trạng thái đạt giữ xanh semantic sẵn có. Bảng cây cũ giữ các cột T3/T2/T1 theo chuẩn cha hiện hữu.
- Renderer tự bật chuẩn cho bảng có `definitionColumns`; không được gán `focusFourColumns:false` trong adapter Master. Cột mới mặc định là phụ; muốn thêm điểm nhấn phải có quyết định Owner và sửa SSOT chung.
- Dùng chung cả điều hướng, tìm kiếm/lọc, chi tiết và dấu ? của UI cha. Ngoại lệ phải ghi rõ lý do/phạm vi và được Owner chốt; không nhân bản mẫu theo từng Master.
- **Trước khi sửa:** đọc mục này, đối chiếu renderer và adapter; tìm override ảnh hưởng tất cả Master.
- **Trước khi báo xong:** mở đúng URL Owner, kiểm computed style của tên/trạng thái/cột phụ, thử tìm kiếm và mở/đóng chi tiết; kiểm thêm một Master cùng renderer và Config khi có ảnh hưởng. Đối chiếu số bản ghi không đổi. Phải phân biệt kiểm nguồn với kiểm live; chưa kiểm được thì ghi rõ, không báo PASS.
- Thay đổi lần này: bỏ override tắt chuẩn ở nhóm/derived và Config; đưa mặc định vào renderer chung. Tài liệu này là đầu mối quy chuẩn, không sao chép quy tắc sang nhiều README.
- Kiểm live 07/10/2026: MOW 35 dòng; Tên/Trạng thái weight 700, màu rgb(29,29,31); cột phụ weight 400, rgb(176,176,181). Tìm MOW-NHC-001 còn 1 dòng; mở/đóng drawer đạt và xoá tìm kiếm trả lại danh sách. Config đạt cùng token; Nhóm cha 35 dòng kế thừa ml-focus-four. Đã xem screenshot MOW. Phạm vi kiểm live: 3 Master đại diện; không tuyên bố đã bấm từng trang của toàn bộ 29 Master.


## Điều hướng chung · Owner 07/10/2026
SSOT UI: `ui/design-navigation-v1.js`; được nạp từ khuôn `mot-master-v1.html`, renderer `master-list.js` và shell `eco-nav.js`. Trang review và chi tiết CT nạp trực tiếp, mount idempotent. 28 Master định nghĩa + Config cùng kế thừa UI.MASTER; không hardcode danh sách 29 vào bộ điều hướng.

Chuẩn cho mọi tầng mới: **Quay lại · Trang chủ thiết kế · Danh sách Master** luôn nhìn thấy ở đầu màn hình. Home cố định `master-design-review-v1.html`; index cố định `definition-master-index-v1.html`. Đóng chi tiết trong bảng phải giữ bộ lọc/danh sách. Mở trang khác từ iframe ra top window. Không lấy URL ngoài hệ làm đích quay lại.

Trang dùng UI cha tự kế thừa; trang độc lập phải nạp `/ui-preview/mcp-writes/design-navigation-v1.js`. Với tầng riêng, khai `window.DESIGN_NAV_CONFIG={parentUrl:'<đường cha cùng origin>'}` trước khi nạp. Công thức có fallback về Master Công thức; các Master fallback về index. Cơ chế này không tự suy cây nghiệp vụ cho trang chưa thiết kế.

## SSOT cho AI khi làm Công thức / Định nghĩa / Master / UI / Coverage

**Project:** `work/mow-mot-moit-mout`  
**Owner-gated concept:** Công thức và nghĩa khái niệm.  
**AI-owned implementation:** schema Master, UI chi tiết, coverage, test, bằng chứng, reuse mapping, kỹ thuật triển khai.  
**Cập nhật gần nhất:** 2026-10-06 · D158.

> BẮT BUỘC ĐỌC FILE NÀY trước khi sửa Công thức, Định nghĩa, Master List, UI con/cha, coverage hoặc config liên quan MMIM.
>
> **Nếu thay đổi một tiêu chí/trạng thái/tên/UI/Master có thể ảnh hưởng nhiều nơi:** đọc tiếp `CHANGE-PROPAGATION.md` + `CHANGE-IMPACT-MAP.json` và chạy Change Event trước khi sửa.

Nếu file này mâu thuẫn với **quyết định Owner mới hơn trong COLLAB**, quyết định Owner mới hơn thắng và AI phải cập nhật lại README này ngay trong cùng lượt làm.

---

## Config · Nguyên tắc Owner 06/10/2026 22:09 +07

Khai báo nguyên tắc nếu/thì một lần để hệ thống nhận diện theo ngữ cảnh; Config tham chiếu nguồn chung. Bảy câu hỏi: (1) bắt đầu từ đâu; (2) kết thúc ở đâu; (3) điều kiện — NTĐK/thiết lập lẻ; (4) trigger — NTTG/từng trigger; (5) ai làm — NTGV; (6) báo cáo cho ai — nguyên tắc báo cáo/cá nhân; (7) chuyển tiếp cho ai — nguyên tắc chuyển tiếp/cá nhân. Điều kiện và trigger là hai mục riêng. Bản ghi: cần mô tả nguyên tắc xác định bản ghi áp dụng; chi tiết chưa chốt. Chưa chốt ưu tiên/xử lý nhiều rule cùng khớp; không tự lập runtime engine hoặc gán giá trị cho bản ghi demo.

SSOT nội dung: `ui/config-master-data-v1.js#CONFIG_PRINCIPLES`, được dùng chung trong chi tiết CT-007 và drawer Master Config. CT-007 giữ nguyên công thức, chỉ bổ sung nguyên tắc chi tiết. Đây là nguyên tắc thiết kế, chưa phải bằng chứng tự động hóa đã chạy.

## Master Config · D152 · 06/10/2026
- UI đang rà: [Master Config](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/config-master-v1.html), dòng 28 trong bảng duyệt hiện hành.
- Dùng nguyên UI.MASTER cha `mot-master-v1.html`; schema/nhãn SSOT tại `ui/config-master-data-v1.js#CONFIG_MASTER_SCHEMA`. Không còn renderer bảng riêng.
- Mặt danh sách: **STT · ID · Tên · Loại config · Mục đích · Áp dụng cho · Phạm vi sử dụng · Người phụ trách · Trạng thái**. “Loại config” không gộp Nhóm cha/con; người phụ trách quản lý khác người thực hiện theo NTGV.
- Chi tiết: UI cha, người thực hiện, kích hoạt khi, phiên bản, tham số, bằng chứng áp dụng, nguồn/ghi chú. Thông tin chưa biết hiển thị chưa khai báo/chưa phân công, không tự bịa.
- `CFG-TEST-001` giữ toàn bộ trường gốc và trạng thái nháp/test. Chưa nối DB hoặc có UI CRUD. FC-002 vẫn OPEN; chưa quyết nghĩa canonical của Config hay quan hệ định nghĩa/lần áp dụng.

## D153 · Danh mục Nhóm cha / Nhóm con T0–T2 · 06/10/2026

Đã ghi vào hai Master hiện hữu theo chỉ đạo Owner: **35 Nhóm cha** (B1–B7 × 5 nhánh) và **115 Nhóm con** (23 Bước con × 5 nhánh). Nguồn Bước/Bước con: CT-001 trong `ML-DEF-021`; đối tượng/tầng: CT-002. MOIT và MOUT cùng T0.5 nhưng là hai nhánh riêng.

| Tầng / đối tượng | Nhóm cha | Nhóm con |
|---|---:|---:|
| T0 · Field | 7 | 23 |
| T0.5 · MOIT | 7 | 23 |
| T0.5 · MOUT | 7 | 23 |
| T1 · MOT | 7 | 23 |
| T2 · MOW | 7 | 23 |
| Tổng | 35 | 115 |

- [Master Nhóm cha](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/definition-master-v1.html?stt=1): `NHC-001…035`; thêm 28, giữ nguyên 7 dòng cũ.
- [Master Nhóm con](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/definition-master-v1.html?stt=2): `NHCN-001…115`; thêm 112, giữ nguyên 3 dòng cũ.
- Số Bước con B1→B7: **3, 2, 4, 4, 3, 3, 4 = 23**. Không tạo B8/B9 hoặc bước con chưa có nguồn.
- Khóa chống trùng hiện hành D158: `chainId + stepRef + tierRef`; mỗi Nhóm con có `parentGroupId` cùng đối tượng/tầng, đúng Bước gốc. `tierRef` phân biệt MOIT/MOUT tại T0.5.
- **Độ phủ danh mục: FULL cho phạm vi Owner giao.** Rule/config/bộ trường bắt buộc chưa hoàn thiện vẫn hiển thị thiếu; Chuyên môn Nhóm con giữ OPEN. Đây không phải kết luận các nhóm đã được duyệt để vận hành. Không đổi công thức/khái niệm hoặc canonical UI.

## D158 · Master Quy trình · Owner 06/10/2026 21:48 +07

ML-DEF-004 hiện có **35 quy trình CH-001**, dẫn xuất một-một từ Nhóm cha: B1–B7 × Field/T0, MOIT/T0.5, MOUT/T0.5, MOT/T1, MOW/T2. Không ghép chéo Bước/Tầng với Nhóm cha khác. Tên = Quy trình · Tên Chuỗi · Bước · Tầng/Đối tượng; sourceGroupId trỏ Nhóm cha, trường chung đọc từ SSOT. CT-005 giữ nguyên.

ID mặc định MOW-NHC-xxx; riêng NHC-005 reuse bản review CT005-B5-T0-001 và processRef FIELD.KHAI đã có. Mục tiêu riêng cũ được giữ, mục tiêu chưa có hiển thị chưa khai báo. Các dòng là DANH MỤC · CHƯA HOÀN THIỆN CẤU HÌNH, chưa phê duyệt vận hành. Total tự đếm35. URL mow-master-nhap2-v1.html mở Master mới; `?legacy=1` và link chi-tiet cũ vẫn giữ7 demo legacy. mow-master-v1.html và backend không sửa. Ghi chú 'MOW giữ nguyên' ở mục 18:09 là lịch sử trước cập nhật này.

## D158 · Đồng bộ danh mục từ Nhóm con · Owner 06/10/2026 18:09 +07

- Tên nhóm: `Nhóm cha/con · Tên Chuỗi · Bước/Bước con · Tầng/Đối tượng`, sinh từ trường SSOT, giữ ID và legacyName. ParentGroup cập nhật theo parentGroupId; coverageKey gồm chainId.
- **35 cha / 115 con; Task, MOIT, MOUT mỗi loại 115 dòng** trong phạm vi CH-001. ML-DEF-005/006/007 là view dẫn xuất từ ML-DEF-002, không chép ba bộ dữ liệu độc lập. Tên/Chuỗi/Bước con/Tầng/Gộp/Tách đều lấy nhóm gốc; thêm nhóm gốc thì danh sách và Total đổi theo khi tải lại.
- ID mới ổn định: TSK-NHCN-xxx / MOIT-NHCN-xxx / MOUT-NHCN-xxx. sourceGroupId trỏ NHCN-xxx. Các ID demo cũ không tái sử dụng hoặc tự ánh xạ; demo giữ tại URL cũ với `?legacy=1`.
- Đường vào mot-master-v1.html, moit-master-v1.html, mout-master-v1.html hiện mở danh mục dẫn xuất, cùng UI.MASTER cha; bảng ngoài đọc Total từ danh mục này. MOW giữ nguyên.
- Đây là **đồng bộ danh mục thiết kế**, trạng thái DANH MỤC · CHƯA CẤU HÌNH; chưa tạo task chạy thật, form nghiệp vụ hay migrate PG/Directus. Các ghi chú lịch sử nói danh sách còn 7/6/6 hoặc chưa đồng bộ UI bị thay thế bởi mục này; mapping demo/backend vẫn chưa thực hiện.

## D158 · Chuỗi là nguyên liệu · 06/10/2026

- **CT-002.1 · Chuỗi** đặt dưới Tầng. SSOT mã/tên/định nghĩa/icon tại `ui/chuoi-data-v1.js`: CH-001 Chế tạo cỗ máy; CH-002 Vận hành cỗ máy; CH-003 Cỗ máy sản xuất quy trình.
- **Nguyên liệu dùng chung:** Bước/Bước con (CT-001), Tầng (CT-002); Chuỗi (CT-002.1) xác định tiến trình. Từ CT-003 đến CT-007, kể cả 005.1/.2/.3, thêm Chuỗi vào đầu. Công thức chung hiển thị chữ **Chuỗi**, tuyệt đối không thay biến này bằng icon hay giá trị CH-001. CT-002.1 giới thiệu ba icon kèm tên luôn hiển thị. Không hiểu Chuỗi là trạng thái vòng đời record.
- **SSOT Nhóm con giữ nguyên:** Task/MOIT/MOUT/UI con và ngoại lệ Gộp/Tách tham chiếu Nhóm con **cùng Chuỗi**. Chuỗi đầu công thức là ngữ cảnh ràng buộc, không tạo thêm tổ hợp khác Chuỗi của Nhóm con.
- **Master:** schema có `chainId`; nhãn lấy từ danh mục Chuỗi. Bộ dữ liệu thiết kế đang bàn khai báo CH-001 ở scope review, item override khi có chỉ đạo; không suy từ tên record. Mỗi Master có thể mở rộng dữ liệu theo ba Chuỗi; hiện chỉ xử lý Chế tạo cỗ máy, nên cột Chuỗi của toàn bộ dữ liệu review là CH-001. Chưa sinh bản ghi cho CH-002/003, không đổi ID hoặc nhân ba số lượng hiện tại. Riêng Master Chuỗi vẫn giữ đủ ba tên định nghĩa; cột Chuỗi mô tả phạm vi thiết kế CH-001, khác với ID của giá trị được định nghĩa. Khóa nhóm mở rộng `chainId + stepRef + tierRef`; liên kết cha/con phải khớp Chuỗi. Chưa là migration PG/Directus hoặc bằng chứng backend cưỡng chế.
- **Master Chuỗi:** ML-DEF-028 / KNI-024 / STT28, dùng UI.MASTER hiện có, 3 giá trị từ cùng nguồn; không chép bộ enum riêng. Có 28 Master định nghĩa + Config = 29 dòng ngoài; Total vẫn ngay sau Tên, Chuỗi kế tiếp. Công thức: 11 gốc.
- **Icon:** dùng nguyên ba SVG vector Owner cung cấp: `machine-building.svg` (CH-001), `machine-operation.svg` (CH-002), `automated-process.svg` (CH-003), tổng 29.600 bytes. Mapping SSOT tại `chuoi-data-v1.js`; CSS `chuoi-ui-v1.css`; CT-002.1 dùng icon kèm tên; các công thức lắp ráp dùng chữ Chuỗi; Master dùng tên giá trị Chuỗi. Asset raster cũ chỉ lưu để rollback, không dùng trong UI hiện tại.
- **Mặt người:** giải thích dài CT-003→007 thu vào Chi tiết; nội dung/nguồn vẫn giữ cho AI. CT-001/002 không thêm Chuỗi và giữ bố cục.

## D157 · Một gốc Nhóm con; ba tiến trình · 06/10/2026

> Lịch sử: D158 chốt tên Chuỗi, bổ sung vào công thức và Master; tổng 10 và đề xuất bộ chọn dưới đây đã được cập nhật bởi D158.

- **Chỉ đạo Owner:** Nhóm con là SSOT cho cấu trúc chung của Task, MOIT, MOUT và UI con. CT-005.1 = Nhóm con ⇒ Task; CT-005.2 = Nhóm con ⇒ MOIT; CT-005.3 = Nhóm con ⇒ MOUT. Tổng hiện tại 10 công thức gốc.
- **Gộp/Tách:** một hồ sơ ngoại lệ tại Nhóm con; các đối tượng phụ thuộc tham chiếu cùng hồ sơ. Không chỉnh cơ cấu/ngoại lệ độc lập ở Task, MOIT, MOUT hoặc UI con. Trường đặc thù mỗi loại vẫn thuộc đối tượng đó.
- **Ký hiệu:** ⇒ chỉ quan hệ dẫn xuất/tương ứng. Không dùng chuỗi dấu = để suy đồng nhất kiểu dữ liệu, ID hoặc tự suy số lượng 1:1. CT-002 vẫn mô tả cấu trúc thành phần; không bị thay bằng quan hệ SSOT này. CT-006 vẫn giữ đầu vào UI cha, lấy ngữ cảnh chung từ Nhóm con khi mapping được xác minh.
- **Diễn giải đề xuất để Owner góp ý:** Chế tạo máy = tạo/nâng cấp năng lực máy; Vận hành máy = điều khiển, theo dõi và duy trì máy hoạt động đúng; Sản xuất quy trình = dùng máy tạo quy trình nghiệp vụ cụ thể. Phân biệt theo mục đích/đầu ra, không chỉ theo tên Field/Form/MOT/MOW. Hiện đang thiết kế chế tạo máy (khớp mục tiêu §0).
- **Đề xuất biểu diễn:** một bức tranh dùng chung, chọn ngữ cảnh ba tiến trình ở đầu; chỉ mở công thức/chi tiết liên quan khi cần. Ngữ cảnh phải hiện bằng chữ, không chỉ màu. Dùng lại công cụ không tạo bản sao danh mục. Phân loại theo lần sử dụng; một công cụ có thể phục vụ nhiều tiến trình. Đây là đề xuất, chưa thay bộ giá trị Thuộc cũ hoặc tạo filter production.
- **Giới hạn thực thi:** đã cập nhật công thức/ghi chú; chưa migrate các Master mẫu và chưa cưỡng chế đồng bộ dữ liệu. 115 Nhóm con, 7 MOT, 6 MOIT, 6 MOUT là các tập hiện hữu khác quy mô, không tự bịa mapping. Cần liên kết về Nhóm con có evidence trước khi coi SSOT vận hành đã hoàn tất. Không sinh bản ghi hàng loạt, không thay ID/canonical UI.
- **Tránh nhầm cho AI:** tách loại đối tượng, ngữ cảnh sử dụng và trạng thái triển khai; không hiểu “dùng chung concept” là “cùng bản ghi”. Việc chạy quy trình nghiệp vụ đã sản xuất là sử dụng sản phẩm, không tự gộp vào “vận hành máy tạo quy trình”.

## D156 · Lịch sử công thức Task và hồ sơ ngoại lệ · 06/10/2026

> Phần đầu vào CT-005.1 và tổng 8 dưới đây đã được D157 thay thế; giữ để tra lịch sử.

- **CT-005:** `Bước + Tầng + Nhóm cha ⇒ Quy trình`.
- **CT-005.1:** `Bước con + Tầng ⇒ Task`, độc lập, đặt ngay sau CT-005. Tạm có cùng đầu vào với CT-004; không coi Task và Nhóm con là một đối tượng.
- Master Công thức hiện có **8 công thức gốc**; Total đếm tự động. Các cấu trúc con bên trong công thức không tính thêm.
- Master Nhóm con và MOT/Task có cột **Gộp** (`mergeCaseIds`) và **Tách** (`splitCaseIds`), trước Trạng thái. Dấu “?” theo UI cha: gộp hai hoặc nhiều task thành một; tách một task thành hai hoặc nhiều task. Ô cột chỉ giữ mã hồ sơ riêng; không phải nút thực thi. `—` = chưa ghi nhận hồ sơ, không khẳng định đã rà và không có ngoại lệ.
- **Phần chuẩn theo công thức; ngoại lệ có hồ sơ riêng.** “99%” là mục tiêu thiết kế Owner nêu, chưa phải tỷ lệ đo.
- Hợp đồng hồ sơ riêng khi có ca thực tế: ID hồ sơ, loại Gộp/Tách, loại đối tượng, danh sách mã nguồn, danh sách mã kết quả, Bước con/Tầng và phiên bản công thức, lý do, quyết định/người duyệt, trạng thái, bằng chứng, liên kết thay thế/kế thừa. Gộp: ≥2 nguồn → 1 kết quả. Tách: 1 nguồn → ≥2 kết quả. Các bản ghi liên quan cùng tham chiếu một hồ sơ để không tạo các bản giải thích khác nhau.
- Chưa có ca ngoại lệ thật được cung cấp: không bịa hồ sơ hoặc sửa/xóa bản ghi; không tự gộp/tách. Chưa có backend/form CRUD hồ sơ ngoại lệ. Khi phát sinh ca đầu tiên dùng hợp đồng trên để hoàn thiện chỗ lưu riêng và UI phù hợp trong phạm vi Owner giao.
- Giữ 115 Nhóm con và 7 Task hiện có; lượt này chưa giao sinh toàn bộ Task từ CT-005.1. Không đổi CT-006/007 hoặc các UI canonical khác.


# 1. RANH GIỚI QUYẾT ĐỊNH

## 1.1. Phải đưa Owner duyệt
Các thay đổi sau là **CONCEPT / FORMULA**:
- tạo CT-xxx mới;
- thêm/bớt thành phần trong một công thức;
- đổi nghĩa của công thức;
- đổi nghĩa canonical của Bước, Tầng, Nhóm, UI, MOW/MOT/MOIT/MOUT/Field, Bản ghi, NTGV, Trigger;
- đổi nghĩa ký hiệu `+`, `⇒`, `=>`, `→`, `{A|B}`;
- biến một khái niệm con thành khái niệm gốc hoặc ngược lại.

AI được phép **đề xuất** nhưng không tự coi canonical.

## 1.2. AI tự phản biện và xử lý
Không cần kéo Owner vào chi tiết IT phổ quát nếu không đổi concept:
- cột Master List và drawer/detail phù hợp;
- cấu trúc config key;
- reuse UI cha / mapping UI con;
- trạng thái coverage và cách quét;
- test case, PASS/FAIL, bằng chứng;
- validation, error handling, accessibility, layout kỹ thuật;
- kỹ thuật tìm/reuse/dedupe;
- cách lưu log, evidence, version kỹ thuật;
- refactor implementation theo Preserve by default;
- phản biện giữa GPT / Claude / Codex / Hermes rồi tự chọn cách kỹ thuật tốt nhất.

Chỉ escalates Owner khi kết quả phản biện dẫn tới **một công thức/khái niệm mới hoặc thay đổi concept**.

---

# 2. NGUYÊN TẮC GỐC

1. **Công thức = ghép các thành phần đã định nghĩa.**
2. Một vấn đề phức tạp phải được chia thành các thành phần đơn giản đủ rõ rồi mới ghép.
3. Mặt người: nickname + công thức + hình họa; text dài để AI đọc.
4. **Preserve by default. Reuse before create.**
5. **MASTER FIRST / LIST FIRST:** bất cứ loại thứ gì có thể phát sinh nhiều bản ghi/biến thể (Nhóm, Quy trình, UI, Config, Tool, Trigger...) phải **có Master List để ghi trước khi xử lý sâu**. Chưa chốt hết định nghĩa/loại không phải lý do để để đối tượng trôi ngoài Master; ghi trước → phân loại sau → chuẩn hóa dần.
6. Bất cứ việc gì phát sinh phải **ghi Master trước khi xử lý**, rồi cập nhật chính bản ghi đó. Nếu chưa biết Master nào phù hợp thì đó là một gap phải mở ngay, không được xử lý xong rồi mới nghĩ nơi ghi.
7. Một Master/Công thức chỉ là canonical khi có nguồn/decision rõ; draft/test phải ghi trạng thái.
8. **OWNER REVIEW SURFACE LÀ HỢP ĐỒNG DANH SÁCH:** nếu Owner đã chốt một bảng/trang để rà Master (hiện là bảng Master trong `master-design-review-v1.html`), Master liên quan phải **có đúng một dòng trong chính bảng đó** với trạng thái/UI/link phù hợp. Không tự nhúng cả trang chi tiết, không dựng dashboard song song, không chuyển Owner sang luồng khác. Trang riêng chỉ là đích khi bấm dòng.
9. Không tạo Cartesian product mù. Mọi tổ hợp phải qua **Applicability Gate**.
10. Không tuyên bố “đủ UI” bằng cảm giác; phải có **Coverage + Evidence**.
11. **Change propagation bắt buộc:** thay đổi một tiêu chí không được sửa một chỗ rồi dừng; phải quét impact map, update/verify toàn bộ current/live target và chỉ đóng khi không còn stale reference.

---

# 3. QUY ƯỚC KÝ HIỆU · KHÓA NGHĨA

| Ký hiệu | Nghĩa bắt buộc |
|---|---|
| `A + B` | Ghép hai chiều/thành phần định nghĩa để tính ra một khái niệm khác; không hàm ý cha-con hay thời gian. |
| `A ⇒ B` | Công thức/ghép ở vế trái **tạo ra / xác định** B. |
| `A => B` | **Lắp ráp thấp → cao / nhỏ → lớn**; A được lắp vào B. Dùng rõ nhất ở CT-002. |
| `A → B` | Thứ tự / vòng đời / diễn biến; B xảy ra sau A. |
| `{A | B}` | Hai nhánh/lựa chọn/cơ chế khác nhau; không tự hiểu A và B là cha-con. |

**Cấm:** tự đổi `=>` thành `<=`, tự dùng `+` thay cho chiều lắp ráp, hoặc dùng `→` để diễn tả quan hệ cấu trúc nếu chưa được chốt.

---

# 4. CÁC THÀNH PHẦN HUMAN-FIRST ĐANG DÙNG TRONG CÔNG THỨC

- **Bước:** giai đoạn hiện tại của vòng đời công việc; nickname của CT-001.
- **Bước con:** phần bóc nhỏ bên trong một Bước. Không tự đồng nhất Bước con = MOT.
- **Tầng:** hệ phân loại T7→T0; nickname của CT-002.
- **Nhóm cha:** chuẩn/rule/config dùng toàn hệ thống hoặc diện rộng.
- **Nhóm con:** chuẩn/rule/config dùng trong một chuyên môn, kế thừa Nhóm cha rồi bổ sung phần riêng.
- **Nhóm:** placeholder trong công thức khi ngữ cảnh có thể resolve về Nhóm cha hoặc Nhóm con; không tạo khái niệm thứ ba.
- **UI cha:** khuôn giao diện + hành vi dùng chung.
- **UI Con:** UI áp khuôn cha vào đúng Bước/Tầng/Nhóm/ngữ cảnh.
- **Quy trình:** một quy trình được tạo từ công thức CT-005; không đồng nghĩa “List Quy trình”.
- **Bản ghi:** instance/case thực tế của một định nghĩa.
- **NTGV:** nguyên tắc giao việc; quy định ai/AI làm gì, nhận gì, giao gì, cho ai, theo điều kiện nào. Nguồn Master cũ liên quan: CAT-218 (loại nguyên tắc) + CAT-219 (nguyên tắc NẾU…THÌ…).
- **Người làm:** tác nhân thực hiện theo NTGV; nguồn người/vai hiện có ở CAT-213/CAT-214.
- **Trigger:** sự kiện/điều kiện kích hoạt. Dùng trong CT-007; chưa có định nghĩa riêng trong bộ 27 nhưng **đã có Master cũ CAT-221 · Danh mục trigger tín hiệu**.
- **MOW / MOT / MOIT / MOUT / Field:** các đối tượng canonical của hệ, xem mục 6.

---

# 5. MASTER CÔNG THỨC HIỆN HÀNH · OWNER ĐÃ DUYỆT

| CT | Nickname | Công thức |
|---|---|---|
| CT-001 | **Bước** | `Tìm → { Dùng | Tạo mới | Sửa | Vô hiệu }` |
| CT-002 | **Tầng** | `Field => { MOIT | MOUT } => MOT => MOW` · T3→T7 chỉ bối cảnh, thu gọn |
| CT-002.1 | **Chuỗi** | `CH-001 · CH-002 · CH-003` — ba icon; tên hiện khi hover/focus |
| CT-003 | **Nhóm cha** | `Chuỗi + Bước + Tầng ⇒ Nhóm cha` |
| CT-004 | **Nhóm con** | `Chuỗi + Bước con + Tầng ⇒ Nhóm con` |
| CT-005 | **Quy trình** | `Chuỗi + Bước + Tầng + Nhóm cha ⇒ Quy trình` |
| CT-005.1 | **Task** | `Chuỗi + Nhóm con ⇒ Task` |
| CT-005.2 | **MOIT** | `Chuỗi + Nhóm con ⇒ MOIT` |
| CT-005.3 | **MOUT** | `Chuỗi + Nhóm con ⇒ MOUT` |
| CT-006 | **UI Con** | `Chuỗi + Bước + Tầng + Nhóm + UI cha ⇒ UI Con` |
| CT-007 | **Config** | `Chuỗi + Bước + Tầng + Nhóm + UI cha + Bản ghi + Người làm (NTGV) + Trigger ⇒ Config` |

**Luật Master:** một dòng CT-xxx = một công thức hoàn chỉnh. Các node nội bộ 1–9 / 1.x của CT-001 không phải công thức Master riêng.

---

# 6. 28 ĐỊNH NGHĨA HIỆN HÀNH

28. **KNI-024 · Chuỗi** — thành phần xác định một trong ba tiến trình; danh mục và nghĩa tại D158/chuoi-data-v1.js. Bước/Tầng là nguyên liệu dùng chung.

## A. Cấu trúc lõi · 1–9
1. **KNI-002 · Nhóm cha** — tập quy tắc/quy định/config dùng chung toàn hệ thống hoặc diện rộng; có thể chuyên môn hóa thành Nhóm con; nếu không cần Nhóm con thì dùng Nhóm cha + config trực tiếp.
2. **KNI-003 · Nhóm con** — tập quy tắc/quy định/config dùng chung trong một chuyên môn; kế thừa Nhóm cha rồi bổ sung phần riêng.
3. **KNI-004 · Đối tượng** — định nghĩa/template nằm dưới Nhóm con hoặc được config trực tiếp từ Nhóm cha; có mã và được quản lý để dùng lại.
4. **OBJ-MOW · MOW / Quy trình** — định nghĩa một quy trình có thể dùng lại.
5. **OBJ-MOT · MOT / Công việc** — định nghĩa công việc nằm trong MOW/quy trình.
6. **OBJ-MOIT · MOIT** — định nghĩa đầu vào/biểu mẫu nhập cho công việc.
7. **OBJ-MOUT · MOUT** — định nghĩa đầu ra/báo cáo cần sinh hoặc hiển thị.
8. **OBJ-FIELD · Field** — đơn vị dữ liệu nhỏ nhất cần khai báo, nhập, tính hoặc hiển thị; đối tượng độc lập ở T0.
9. **KNI-005 · Bản ghi** — instance/giá trị thực tế khi một định nghĩa được áp vào một case cụ thể.

## B. Quản lý định nghĩa · 10–15
10. **KNI-006 · Mã** — danh tính máy đọc ổn định của một khái niệm/đối tượng.
11. **KNI-007 · Master List** — danh mục chuẩn các định nghĩa/đối tượng cùng loại để tìm, quản lý và dùng lại; không trộn với bản ghi runtime.
12. **KNI-008 · Master of Master** — danh mục quản lý các Master List.
13. **KNI-009 · Phiên bản** — mốc nội dung của một định nghĩa để dùng và truy nguyên.
14. **KNI-010 · Vòng đời** — bộ trạng thái + luật chuyển trạng thái; vòng đời định nghĩa và vòng đời bản ghi không mặc định giống nhau.
15. **KNI-011 · Trạng thái** — một vị trí hiện tại bên trong một vòng đời.

## C. UI / View · 16–20
16. **KNI-012 · View** — cách con người nhìn/thao tác trên một nguồn dữ liệu; không sở hữu dữ liệu.
17. **KNI-013 · UI cha / Khuôn cha** — hợp đồng giao diện + hành vi chuẩn để nhiều UI con kế thừa.
18. **KNI-014 · UI con** — UI áp khuôn cha vào một đối tượng/ngữ cảnh cụ thể; chỉ đổi dữ liệu/config/nhãn theo luật.
19. **KNI-015 · List View** — View để tra/tìm/chọn định nghĩa trong Master List.
20. **KNI-016 · Kanban View** — View để nhìn/xử lý luồng việc và trạng thái.

## D. Logic / độ tin cậy · 21–27
21. **KNI-017 · Công thức** — cách ghép các thành phần đã định nghĩa thành một công thức/quy luật dùng lại.
22. **KNI-018 · Step** — **OPEN:** chưa chốt quan hệ chuẩn giữa Step và MOT; không tự đồng nhất.
23. **KNI-019 · Tool / Công cụ** — khả năng thực thi một thao tác có input/output.
24. **KNI-020 · DOT** — **OPEN:** đang được dùng lẫn với Tool; cần định nghĩa chuẩn trước khi công thức hóa.
25. **KNI-021 · Test** — phép kiểm có điều kiện đầu vào và kết quả kiểm được.
26. **KNI-022 · Bằng chứng** — dữ liệu/source cho phép người khác kiểm lại một kết luận.
27. **KNI-023 · Quyết định** — kết luận được tạo từ bằng chứng theo một luật/quy trình.

---

# 7. PHÁT HIỆN THỰC TẾ ĐÃ CÓ

| ID | Phát hiện | Hệ quả |
|---|---|---|
| DISC-001 | Xử lý trước rồi mới ghi Master là ngược. | Việc phát sinh phải ghi Master ngay, sau đó cập nhật trạng thái. |
| DISC-002 | Formula internal node và formula Master là hai cấp khác nhau. | CT-001 chỉ 1 dòng Master; 1–9/1.x là cấu trúc nội bộ. |
| DISC-003 | Field không phải con của MOIT/MOUT. | CT-002 đặt Field/T0 trái cùng và lắp thấp→cao bằng `=>`. |
| DISC-004 | MOIT và MOUT cùng T0.5 nhưng cơ chế khác nhau. | Không gộp thành một đối tượng; phải giữ hai nhánh riêng. |
| DISC-005 | Mặt người dễ rối khi xổ toàn bộ chi tiết. | Progressive disclosure: nhìn gốc; bấm mới mở con; text kỹ thuật mờ/ẩn. |
| DISC-006 | CT-003 có thể sinh Master thật. | Test T0 đã tạo NHC-001→007 từ B1→B7. |
| DISC-007 | Master list và Detail có nhiệm vụ khác nhau. | List chỉ giữ cột quét nhanh; Detail tích lũy rule/config key. |
| DISC-008 | Liệt kê trực tiếp dễ sót và nhanh thành “đống rác”. | Phải quét bằng công thức + coverage. |
| DISC-009 | Tích Descartes toàn bộ sẽ sinh nhiều tổ hợp vô nghĩa. | Bắt buộc Applicability Gate trước khi tạo/thiết kế. |
| DISC-010 | Không thể nói “đủ UI” nếu chưa có bằng chứng độ phủ. | Cần Coverage Matrix và trạng thái từng ô. |
| DISC-011 | CT-004 `Bước con + Tầng ⇒ Nhóm con` sinh được candidate Nhóm con, nhưng định nghĩa Nhóm con lại yêu cầu `trong 1 chuyên môn`. | Không tự thêm Chuyên môn vào CT-004. Master test giữ cột Chuyên môn = OPEN; cần Owner quyết đây là dimension của công thức hay dimension config/instantiate sau. |
| DISC-012 | `Cùng chuyên môn / ngoài chuyên môn` là phân loại có ý nghĩa thực tế, nhưng chưa đủ evidence để thành khái niệm mới. | TREO: ưu tiên thử như thuộc tính/quan hệ của Nhóm con với T3 trước; chỉ đề xuất concept mới nếu nó có logic, reuse hoặc vòng đời độc lập. |
| DISC-013 | SUPERSEDED BY DISC-014 · Bản phác thảo Nhóm cha/Nhóm con từng được gán thử UI-030/UI-031 trước khi Owner duyệt. | Không dùng làm canonical. |
| DISC-014 | Master UI con chỉ chứa UI con đã OK/chốt; bản phác thảo chưa duyệt không được nhập Master UI con. | Khôi phục `child-ui-registry.json` về 29 UI established; `ML-DEF-018` đồng bộ đủ 29. Nhóm cha/Nhóm con tiếp tục dùng màn review nhưng không có UI-xxx canonical cho tới khi Owner duyệt. |
| DISC-015 | CT-005 test tại `B5 + T0 + NHC-005` không cần sinh quy trình mới ngay: process map đã có `FIELD.KHAI`. | Reuse-before-create. Master MOW cần lưu/tra được Bước + Tầng + Nhóm cha (D156); schema UI-001 T3/T2/T1 hiện là legacy, chưa đổi canonical khi chưa map 7 dòng hiện có. |
| DISC-016 | CT-006 cùng slice với `UI.CONFIG` resolve được về `UI-018 · Field · khai báo trường`. | Master UI con 5 cột hiện đủ nếu dùng cột `Ngữ cảnh` chứa Bước/Tầng/Nhóm. Không ép Chuyên môn thành cột. Đồng thời phát hiện 3/29 UI established (`UI-008/011/012`) chưa có UI cha. |
| DISC-017 | CT-007 sinh `Config` nhưng không có Master Config/định nghĩa Config trong bộ 27. `UI.CONFIG` chỉ là **khuôn UI cha**, không phải Config output. | Không tự tạo Master mới. CAT-226 `Sổ áp dụng · bật nơi · lúc` là ứng viên liên quan nhưng chưa chứng minh cùng nghĩa; mở FC-002. |
| DISC-018 | Master Field cũ có `Form cha` + `Bắt buộc`, mâu thuẫn CT-002 vì Field T0 độc lập và có thể dùng nhiều form. | Đã sửa Master Field thành `Kiểu dữ liệu · Nhóm quản lý · Nguồn dữ liệu · Validation chung · Trạng thái`; required/default theo nơi dùng thuộc liên kết Field↔Form (CAT-208*)/Config. |
| DISC-019 | Quy tắc “mọi Master chỉ 5 cột” không nên tuyệt đối hóa. | CT-007 prototype cần 6 cột để không mất input: `Ngữ cảnh · UI cha · Bản ghi · Người làm(NTGV) · Trigger · Trạng thái`. Giữ list gọn nhưng không cắt dữ liệu bắt buộc. |
| DISC-020 | Owner chốt lại nguyên tắc tổng quát: Config có thể có nhiều loại và còn hiệu chỉnh dài, nhưng **danh sách phải tồn tại trước**. | Tạo `CAT-248* · Master Config` + `config-master-v1.html`; ghi `CFG-TEST-001` ngay. Việc phân loại/định nghĩa Config tiếp tục OPEN, không chặn việc quản lý danh sách. |
| DISC-021 | SUPERSEDED BY DISC-022 · D149 đúng là thiếu Master Config trong bảng rà, nhưng D150 lại over-correct bằng cách nhúng 3 bảng lớn vào cùng trang. | Không dùng cách iframe nhúng dài. |
| DISC-022 | Owner chốt nghĩa đúng của mặt rà: **một bảng duy nhất liệt kê các Master; dòng nào có UI/list thật thì đánh xanh**. | D151 bỏ 3 iframe, giữ bảng duy nhất; đổi row 4 thành `Master Quy trình / MOW`, giữ `Master UI con` row 18, thêm row 28 `CAT-248* · Master Config` xanh. |

### D139 · bằng chứng đầu tiên của cách tiếp cận
`CT-003 = Bước + Tầng ⇒ Nhóm cha` tại **T0 Field** đã sinh 7 bản ghi B1→B7 trong `ML-DEF-001`.

List thử hiện dùng 5 cột:
- Bước
- Tầng
- Chuẩn dùng chung
- Khai báo bắt buộc
- Trạng thái

Chi tiết dùng UI.MASTER cha và giữ:
- công thức nguồn;
- Bước/Tầng/Phạm vi/Mục tiêu;
- chuẩn dùng chung;
- khai báo bắt buộc;
- config key + required + ý nghĩa;
- ghi chú/evidence.

**Trạng thái:** `NHÁP · TEST GHÉP`, chưa canonical, chưa nối PG.

### D141 · test CT-004 Nhóm con tại T0
`CT-004 = Bước con + Tầng ⇒ Nhóm con` với Bước con **1.1 / 1.2 / 1.3** và **T0 Field** đã sinh 3 candidate trong `ML-DEF-002`:
- `NHCN-001 · 1.1 Tìm thường · T0 Field`
- `NHCN-002 · 1.2 Tìm nâng cao · T0 Field`
- `NHCN-003 · 1.3 Xác nhận phù hợp · T0 Field`

Cả 3 kế thừa Nhóm cha `NHC-001 · B1 Tìm · T0 Field`.

List thử Nhóm con dùng 5 cột:
- Bước con
- Tầng
- Nhóm cha
- Phạm vi chuyên môn
- Trạng thái

Chi tiết dùng UI.MASTER cha và giữ:
- công thức nguồn CT-004;
- Bước con/Tầng/Nhóm cha kế thừa;
- Chuyên môn;
- mục tiêu/phần kế thừa/chuẩn riêng;
- config key + required + ý nghĩa.

**Phát hiện quan trọng:** `Chuyên môn` hiện là `OPEN · chưa gắn` vì CT-004 không cung cấp chiều này. Không được tự sửa formula.

**OPEN-SPECIALTY-SCOPE · TREO, CHƯA BỎ:**
- `Cùng chuyên môn / ngoài chuyên môn` là một classification cần giữ lại để kiểm tiếp.
- Chưa tạo khái niệm mới.
- Thứ tự thử trước khi đề xuất concept mới: (1) reuse quan hệ với T3 Chuyên môn; (2) thử attribute/config kiểu `specialty_scope = SAME | CROSS | OPEN` trên Nhóm con hoặc instance; (3) nếu nhiều slice cho thấy nó chi phối công thức, mới đề xuất thêm `Chuyên môn` vào CT-004; (4) chỉ tạo Master/khái niệm riêng nếu phạm vi chuyên môn có lifecycle/reuse/rule độc lập.

**UI review D144:**
- Master Nhóm cha và Master Nhóm con **đã có màn phác thảo/review**, nhưng chưa được tính là UI con canonical.
- Chưa cấp/gắn UI-xxx vào Master UI con cho tới khi Owner chốt UI.
- `child-ui-registry.json` và `ML-DEF-018 · Master UI con` chỉ chứa **29 UI con đã OK** từ baseline trước đó.
- Sau khi Owner duyệt UI Nhóm cha/Nhóm con, mới cấp/khôi phục ID UI-xxx và thêm vào Master UI con.

### D148 · test CT-005/006/007 trên đúng một slice B5/T0
**Slice duy nhất:** `B5 · Khai báo + T0 · Field + NHC-005`. CT-006/007 thêm `UI.CONFIG`; CT-007 thêm bản ghi demo `full_name`, người khai báo theo NTGV và trigger mở bước Khai báo.

- **CT-005 · Quy trình:** `B5 + T0 + NHC-005 ⇒ Quy trình` → tìm thấy `FIELD.KHAI` trong process map ⇒ **REUSE candidate**, không sinh quy trình mới. Schema review tạm cho Master MOW: `Bước · Tầng · Nhóm · Mục tiêu · Trạng thái`. UI-001 hiện vẫn schema legacy T3/T2/T1; chỉ ghi review row `CT005-B5-T0-001`, không đụng 7 MOW canonical.
- **CT-006 · UI Con:** `B5 + T0 + NHC-005 + UI.CONFIG ⇒ UI Con` → **reuse UI-018**. Master UI con giữ 5 cột `UI cha · Ngữ cảnh · Đối tượng · URL · Trạng thái`; `Ngữ cảnh` là nơi mang Bước/Tầng/Nhóm. Không tạo UI mới.
- **CT-007 · Config:** prototype `CFG-TEST-001` cần `Ngữ cảnh · UI cha · Bản ghi · Người làm(NTGV) · Trigger · Trạng thái`. D149 đã tạo `CAT-248* · Master Config` để ghi ngay; `CFG-TEST-001` là dòng đầu tiên. Semantics/loại Config vẫn OPEN, nhưng **việc có Master List không còn OPEN**.

**Rà Master cùng lượt:**
- ML-DEF-017 Master UI cha: điền 6 UI cha thật từ `parent_id` của 29 UI con; 26/29 đã gắn, `UI-008/UI-011/UI-012` còn OPEN cha.
- ML-DEF-018 Master UI con: đổi label `Chuyên môn / Ngữ cảnh` → `Ngữ cảnh`; 3 UI thiếu cha hiển thị `OPEN · chưa gắn` thay vì dấu `—`.
- ML-DEF-008 Master Field: bỏ `Form cha` và `Bắt buộc` khỏi schema intrinsic theo DISC-018.
- ML-DEF-002: đổi label `Chuyên môn` → `Phạm vi chuyên môn` để phản ánh đây vẫn là vấn đề OPEN.
- Các Master 3, 9–16, 19–27 chưa lộ mâu thuẫn trong slice D148 ⇒ preserve; không sửa chỉ để đồng bộ hình thức.

### D149 · MASTER CONFIG · GHI TRƯỚC, PHÂN LOẠI SAU
Owner chốt nguyên tắc chung: “có nhiều Config khác nhau, là cái gì còn bàn dài; đầu tiên phải có chỗ để ghi danh sách”.

Đã làm:
- tạo `CAT-248* · Danh mục Config` trong Master of Master (85→86 Master);
- tạo `config-master-v1.html` + `config-master-data-v1.js`;
- ghi ngay `CFG-TEST-001 · Config · Khai báo Field · full_name` từ ca CT-007;
- Master Config tạm hiển thị: `Loại/Nhóm · Ngữ cảnh · Đối tượng/Bản ghi · UI cha · Người làm(NTGV) · Trigger · Trạng thái`;
- bảng Master ngay dưới vùng CT-005/006/007 là nơi duy nhất Owner rà danh sách: row 4 `Master Quy trình / MOW` xanh UI-001; row 18 `Master UI con`; row 28 `Master Config` xanh. Không nhúng các list dài vào vùng CT.

**Khóa nghĩa:** Master Config tồn tại là quyết định đã chốt. Phân loại/semantics Config còn OPEN và được hiệu chỉnh dần trên chính Master này.

---

# 8. COVERAGE · CÁCH AI PHẢI QUÉT THIẾU

## 8.1. Không quét mù
Mỗi candidate phải đi qua:

`Sinh candidate → Applicability Gate → Tìm/reuse → Phân loại → Master → Test/Evidence → Coverage`

## 8.2. Trạng thái coverage tối thiểu
- **OPEN** — chưa phân loại.
- **N/A** — công thức không áp dụng ở ô này; phải có lý do.
- **REUSE** — đã có thứ dùng lại được; link nguồn.
- **HAVE** — đã có đúng đối tượng/UI cần thiết; link nguồn.
- **NEED_CREATE** — áp dụng nhưng chưa có.
- **VERIFIED** — đã kiểm/test có bằng chứng.

Không coi coverage hoàn thành khi còn **OPEN**.

## 8.3. Thứ tự quét đề xuất
1. **T0 · Field**
2. **T0.5 · MOIT/MOUT**
3. **T1 · MOT**
4. **T2 · MOW**
5. **T3→T7** chỉ mở khi bối cảnh/quản trị thực sự ảnh hưởng.

Trong từng tầng:
- Bước 1→7;
- nếu một Bước quá phức tạp thì mở Bước con;
- sau đó Nhóm cha → Nhóm con (nếu cần) → Quy trình → UI Con → Config.

## 8.4. Mục tiêu của Coverage UI
Mỗi ô cuối cùng phải trả lời:
- UI không áp dụng?
- UI đã có?
- reuse UI cha/UI con nào?
- cần thiết kế mới?
- config nào cần?
- bằng chứng nào xác nhận?

Đây là cơ sở duy nhất để nói “đã liệt kê đủ UI theo mô hình hiện tại”.

---

# 9. VIỆC CÒN THIẾU / OPEN

## P0 · cần làm để chứng minh mô hình
- Tạo Coverage Matrix cho `Bước/Bước con × Tầng`.
- Dùng status OPEN/N-A/REUSE/HAVE/NEED_CREATE/VERIFIED.
- D153 Owner đã giao mở danh mục Nhóm đến T2: đủ 35 cha/115 con. Coverage danh mục hoàn tất; coverage UI/vận hành vẫn phải kiểm theo ca thực tế.
- Giữ nội dung chi tiết D139 đã có; nhóm mới chỉ điền nguồn/quan hệ chắc chắn, chưa tự chốt rule/config hay Chuyên môn.

## P1 · cần kiểm bằng làm thật
- CT-004 Nhóm con: **D141 test 1.x + T0; D153 đã ghi đủ 115 nhóm cho 1.x–7.x × 5 nhánh T0–T2**; UI vẫn review-only, chưa canonical; còn OPEN việc Phạm vi chuyên môn thuộc công thức, quan hệ T3 hay config/instantiate.
- CT-005 Quy trình: **ĐÃ TEST D148 B5/T0/NHC-005**; reuse candidate `FIELD.KHAI`. OPEN: map review schema `Bước/Tầng/Nhóm cha` vào 7 dòng Master MOW legacy trước khi đổi UI-001 canonical.
- CT-006 UI Con: **ĐÃ TEST D148**; reuse `UI-018`, không tạo UI. OPEN: xác định UI cha cho `UI-008/UI-011/UI-012`.
- CT-007 Config: **ĐÃ TEST D148 bằng 1 bản ghi demo; D149 đã có Master Config CAT-248***. OPEN chỉ còn semantics/phân loại Config (FC-002) + quyền/điều kiện nếu ca thật chứng minh cần.
- Trigger: nguồn Master hiện có `CAT-221`; chưa đưa thành định nghĩa trong bộ 27.
- NTGV/Người làm: nguồn hiện có CAT-218/219 + CAT-213/214; cần map quyền khi implementation thực tế đòi hỏi.

## P2 · định nghĩa còn mở
- Step ↔ MOT: chưa chốt.
- Tool ↔ DOT: chưa chốt.
- Khuôn mã canonical.
- Quy tắc version.
- Mã hóa vòng đời/trạng thái.
- PASS/FAIL/UNKNOWN cho Test.
- Quyết định YES/NO/UNKNOWN nếu cần.
- T2 source cũ còn tên “Nhiệm vụ / Workflow” trong khi MOW đang dùng “Quy trình”; không tự hòa giải nếu Owner chưa chốt.

---

# 10. LOOP LÀM VIỆC CHO AI

1. Đọc README này + quyết định Owner mới nhất.
2. Chọn **một slice nhỏ**.
3. Sinh candidate từ công thức đã duyệt.
4. Applicability Gate: loại N/A.
5. Tìm/reuse source thật trước khi tạo.
6. Ghi candidate/đối tượng vào đúng Master.
7. Thiết kế list + detail bằng UI cha hiện có.
8. Chạy test/evidence.
9. Cập nhật Coverage.
10. Ghi phát hiện mới vào **Discovery Log** bên dưới.
11. Nếu phát hiện chỉ là kỹ thuật IT → AI tự phản biện và xử lý.
12. Nếu cần công thức/khái niệm mới → lập **FORMULA CANDIDATE**, không tự canonical.

---

# 11. FORMULA CANDIDATE · KHUÔN ĐỀ XUẤT OWNER

Khi công thức hiện có không đủ, AI ghi:

```text
FC-xxx · Tên ngắn
Vấn đề thực tế:
Evidence:
Công thức hiện tại không đủ vì:
Đề xuất:
Thành phần mới (nếu có):
Ảnh hưởng tới CT/UI/Master:
Có thể giải quyết bằng implementation mà không thêm công thức không? YES/NO
Owner cần quyết:
```

**Nguyên tắc:** cố giải bằng định nghĩa/công thức hiện có trước; chỉ đề xuất CT mới khi có evidence thực tế.

### FC-001 · Chuyên môn trong Nhóm con?
```text
Vấn đề thực tế: CT-004 sinh candidate Nhóm con từ Bước con + Tầng nhưng không cho biết chuyên môn nào.
Evidence: D141 · ML-DEF-002 · NHCN-001..003 đều phải để Chuyên môn = OPEN.
Công thức hiện tại không đủ vì: định nghĩa KNI-003 nói Nhóm con dùng trong 1 chuyên môn.
Đề xuất A: giữ CT-004; Chuyên môn là dimension config/instantiate sau, không nằm trong formula.
Đề xuất B: sửa CT-004 thành Bước con + Tầng + Chuyên môn ⇒ Nhóm con.
Đề xuất C: chưa đổi formula; dùng quan hệ T3 + thuộc tính `specialty_scope = SAME | CROSS | OPEN` để test việc cùng/ngoài chuyên môn. Chỉ nâng thành concept mới nếu có rule/lifecycle/reuse độc lập.
Ảnh hưởng tới CT/UI/Master: Master Nhóm con, naming, coverage, CT-005/006/007 downstream.
Có thể giải quyết bằng implementation mà không thêm công thức không? CHƯA CHẮC; ưu tiên test C trước.
Owner cần quyết: A/B/C khi muốn canonical hóa Nhóm con; hiện trạng TREO, không bỏ.
```

### FC-002 · Config được phân loại/lưu như thế nào?
```text
Owner D149 đã chốt một phần: BẤT KỂ semantics cuối cùng, Config phải có Master List trước. CAT-248* · Master Config đã tồn tại và nhận record ngay khi phát sinh.
Vấn đề còn OPEN: Config là định nghĩa dùng lại, bản ghi áp dụng/runtime, hay cần cả hai lớp?
Evidence: D148 · slice B5/T0/NHC-005 + UI.CONFIG + bản ghi full_name + người khai báo + trigger; D149 · CFG-TEST-001 đã được ghi vào Master Config.
Điểm cần phân biệt: UI.CONFIG = khuôn giao diện; Config output = kết quả cấu hình/binding, không phải một thứ.
Đề xuất A: một dòng Master Config là definition/reusable config; runtime/application record nằm sổ khác.
Đề xuất B: một dòng Master Config chính là config instance/binding; CAT-226 có thể là nguồn runtime liên quan.
Đề xuất C: Master Config quản lý definition, và liên kết tới application/runtime records khi cần.
Ảnh hưởng: CT-007, CAT-248*, CAT-226, UI Config, Bản ghi, Trigger, NTGV, Coverage.
Owner cần quyết: A/B/C khi có thêm evidence. Không được xóa/hoãn Master Config trong lúc chờ.
```

---

# 12. DISCOVERY LOG · AI TỰ DUY TRÌ

Mỗi phát hiện mới ghi một dòng:

```text
DISC-xxx · YYYY-MM-DD · [AREA]
Evidence:
Finding:
Impact:
AI action:
Owner gate: NO | YES (lý do)
Status: OPEN | RESOLVED
```

Không xóa discovery cũ; nếu sai thì đánh **SUPERSEDED BY DISC-xxx** để giữ lịch sử.

---

# 13. CHECKLIST TRƯỚC KHI AI TUYÊN BỐ XONG

- [ ] Đã đọc README này.
- [ ] Không đổi concept/formula nếu chưa Owner duyệt.
- [ ] Đã kiểm source thật/reuse trước khi tạo.
- [ ] Candidate đã qua Applicability Gate.
- [ ] Đã ghi đúng Master.
- [ ] UI dùng đúng UI cha hoặc có evidence vì sao không reuse.
- [ ] Có test/evidence.
- [ ] Coverage không còn OPEN trong scope đã tuyên bố.
- [ ] Discovery mới đã cập nhật README.
- [ ] Nếu phát sinh formula candidate, đã tách riêng để Owner duyệt.



## Tên và mức thị giác công thức · Owner 07/10/2026
Tên chuẩn hiển thị: **MOW** (trước gọi Quy trình), **MOT** (trước gọi Task). Master MOW35, Master MOT115; ID và dẫn xuất từ Nhóm cha/Nhóm con không đổi. Công thức và Master/detail phải lấy cùng cách gọi. Giữ mã TSK-* vì mã ổn định, không đổi tên Chuỗi “Cỗ máy sản xuất quy trình”.

Treeview công thức: mức0 Nhóm cha + MOW; mức1 Nhóm con + MOT + MOIT + MOUT + UI con; mức2 Config. Đây là độ thụt phục vụ con người, **không phải quan hệ dữ liệu mới**. Không tự thêm parentId, không sửa thứ tự CT hoặc công thức ghép vì độ thụt.
