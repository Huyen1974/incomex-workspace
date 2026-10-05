# FORMULA-AI-README · MMIM
## SSOT cho AI khi làm Công thức / Định nghĩa / Master / UI / Coverage

**Project:** `work/mow-mot-moit-mout`  
**Owner-gated concept:** Công thức và nghĩa khái niệm.  
**AI-owned implementation:** schema Master, UI chi tiết, coverage, test, bằng chứng, reuse mapping, kỹ thuật triển khai.  
**Cập nhật gần nhất:** 2026-10-06 · D141.

> BẮT BUỘC ĐỌC FILE NÀY trước khi sửa Công thức, Định nghĩa, Master List, UI con/cha, coverage hoặc config liên quan MMIM.

Nếu file này mâu thuẫn với **quyết định Owner mới hơn trong COLLAB**, quyết định Owner mới hơn thắng và AI phải cập nhật lại README này ngay trong cùng lượt làm.

---

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
5. Bất cứ việc gì phát sinh phải **ghi Master trước khi xử lý**, rồi cập nhật chính bản ghi đó.
6. Một Master/Công thức chỉ là canonical khi có nguồn/decision rõ; draft/test phải ghi trạng thái.
7. Không tạo Cartesian product mù. Mọi tổ hợp phải qua **Applicability Gate**.
8. Không tuyên bố “đủ UI” bằng cảm giác; phải có **Coverage + Evidence**.

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
- **NTGV:** nguyên tắc giao việc; quy định ai/AI làm gì, nhận gì, giao gì, cho ai, theo điều kiện nào.
- **Người làm:** tác nhân thực hiện theo NTGV.
- **Trigger:** sự kiện/điều kiện kích hoạt. Hiện dùng trong CT-007 nhưng **chưa có định nghĩa riêng trong bộ 27**.
- **MOW / MOT / MOIT / MOUT / Field:** các đối tượng canonical của hệ, xem mục 6.

---

# 5. MASTER CÔNG THỨC HIỆN HÀNH · OWNER ĐÃ DUYỆT

| CT | Nickname | Công thức |
|---|---|---|
| CT-001 | **Bước** | `Tìm → { Dùng | Tạo mới | Sửa | Vô hiệu }` |
| CT-002 | **Tầng** | `Field => { MOIT | MOUT } => MOT => MOW` · T3→T7 chỉ bối cảnh, thu gọn |
| CT-003 | **Nhóm cha** | `Bước + Tầng ⇒ Nhóm cha` |
| CT-004 | **Nhóm con** | `Bước con + Tầng ⇒ Nhóm con` |
| CT-005 | **Quy trình** | `Bước + Tầng + Nhóm ⇒ Quy trình` |
| CT-006 | **UI Con** | `Bước + Tầng + Nhóm + UI cha ⇒ UI Con` |
| CT-007 | **Config** | `Bước + Tầng + Nhóm + UI cha + Bản ghi + Người làm (NTGV) + Trigger ⇒ Config` |

**Luật Master:** một dòng CT-xxx = một công thức hoàn chỉnh. Các node nội bộ 1–9 / 1.x của CT-001 không phải công thức Master riêng.

---

# 6. 27 ĐỊNH NGHĨA HIỆN HÀNH

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
- Chuyên môn
- Trạng thái

Chi tiết dùng UI.MASTER cha và giữ:
- công thức nguồn CT-004;
- Bước con/Tầng/Nhóm cha kế thừa;
- Chuyên môn;
- mục tiêu/phần kế thừa/chuẩn riêng;
- config key + required + ý nghĩa.

**Phát hiện quan trọng:** `Chuyên môn` hiện là `OPEN · chưa gắn` vì CT-004 không cung cấp chiều này. Không được tự sửa formula.

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
- Quét T0 trước, không mở toàn hệ thống.
- Rà D139 với Owner; nếu chốt mới nhân sang tầng khác.

## P1 · cần kiểm bằng làm thật
- CT-004 Nhóm con: **ĐÃ TEST D141 tại 1.x + T0**; còn OPEN việc Chuyên môn thuộc công thức hay config/instantiate.
- Chạy CT-005 Quy trình trên một slice thật.
- Chạy CT-006 UI Con và map reuse UI cha.
- Chạy CT-007 Config trên một bản ghi thật.
- Kiểm xem CT-007 có thực sự cần thêm **Trạng thái / Quyền / Điều kiện** hay không. **Không tự thêm vào công thức** trước khi có evidence + Owner duyệt.
- Trigger đang dùng trong CT-007 nhưng chưa có định nghĩa riêng trong 27 definitions.
- NTGV/Người làm cần map rõ với Role/Quyền nếu implementation thực tế đòi hỏi.

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
Ảnh hưởng tới CT/UI/Master: Master Nhóm con, naming, coverage, CT-005/006/007 downstream.
Có thể giải quyết bằng implementation mà không thêm công thức không? CHƯA CHẮC.
Owner cần quyết: A hay B khi muốn canonical hóa Nhóm con.
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

