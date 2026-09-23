# PROMPT — MMIM.FIELD01 · FIELD pilot MAP-R3

RUN_ID: MMIM-FIELD01-20260923-01

## 0. Gate bắt buộc
Lượt này chỉ làm **FIELD pilot** để nghiệm thu khuôn trước khi nhân sang MOUT/MOIT/MOT/MOW.

- Executor_Surface: **Codex**.
- Write_Path: **workspace_*** đã audit. Bắt đầu bằng một read-gate `workspace_read` hoặc `workspace_stat`; mutation dùng `workspace_transaction`/tool cùng family. Cấm Git CLI/native/API để ghi.
- Đọc đúng thứ tự: `AGENTS.md` → `README.md` §0/D12 → `work/mow-mot-moit-mout/COLLAB.md` → prompt này.
- Tra READY bằng `workspace_log` trên chính Write_Path; phải khớp **commit cuối chạm PROMPT.md**, không so HEAD repo.
- Baseline HTML Host đã kiểm: `work/mow-mot-moit-mout/mow-mot-moit-mout.html`, SHA-256 `e5432de39716c761fea7d6ab11692791b404b494e13d36edb655ad29c6b26422`. Nếu SHA khác: đọc diff phần `#list-quy-trinh-shell`; nếu target block đã bị thay đổi thì DỪNG để Host hòa giải, không ghi đè.

## 1. Mục tiêu FIELD01
Triển khai một mẫu hoàn chỉnh cho FIELD theo MAP-R3:
1. cập nhật quy ước trong file;
2. chuyển cột UI sang thang 5 trạng thái;
3. FIELD có đúng 8 bước S01–S08;
4. có 8 bảng chi tiết ổn định;
5. mọi nội dung nghiệp vụ có bằng chứng;
6. không tự tô xanh;
7. không chạm deep-link viewer/VPS;
8. bốn đối tượng MOUT/MOIT/MOT/MOW chưa điền nội dung ở lượt này.

JEV Host: rollout FIELD pilot = 1.00 và evidence gate = 1.00 (`gen-dec-1790134092-aO1ALXq7oHvk0kKWxh8g`).

## 2. Phạm vi mutation
Chỉ sửa:
- `work/mow-mot-moit-mout/mow-mot-moit-mout.html`
- `work/mow-mot-moit-mout/COLLAB.md`

Không sửa:
- mã/runtime VPS, `hpml-view-for-user`, connector/MCP;
- nguồn Mac;
- phần HTML ngoài Step quy trình, trừ CSS cực nhỏ nếu bắt buộc cho chính khối này;
- body MOUT/MOIT/MOT/MOW ngoài việc đổi header cột 7.

Deep-link R3.8 đã tách sang `work/hpml-view-for-user/`.

## 3. G2/G3/G4 — vỏ bảng và sửa an toàn
### 3.1 Quy ước trong file
Cập nhật `#step-quy-trinh-quy-uoc` trong CÙNG transaction:
- 8 bước chuẩn: S01 Tìm · S02 Tạo mới · S03 Khai định danh/nghĩa nghiệp vụ · S04 Gắn phụ thuộc · S05 Sắp xếp/nối · S06 Config máy · S07 Test · S08 Lưu/đăng ký + trả về;
- lifecycle mapping theo JEV `gen-dec-1790134441-cc5M3quXTJLHbOyhLsDI`: S01=Tìm; S02=Tạo; S03=Tạo; S04=Tạo; S05=Tạo; S06=Config; S07=Test; S08=Master; object-step không áp dụng → `x`;
- UI_state 5 giá trị: `UI_OK` xanh · `UI_CAN_SUA` vàng · `UI_THIEU` đỏ · `CHUA_RA` xám · `KHONG_CAN_UI` x;
- Agent không được tự gán `UI_OK`; xanh chỉ khi có bằng chứng + ngày Owner chốt;
- S04 branch chuẩn + `return_to_step`;
- cardinality MAP-R3 gồm HMITL/AUTO;
- hai cột tổng chỉ tính từ detail đã có evidence; trống ≠ 0.

### 3.2 Header
Trong CẢ 5 bảng `list-quy-trinh-{field|mout|moit|mot|mow}`, đổi cột 7 từ `Check UI` sang `Trạng thái UI` + chú thích 5-state. Không điền body của 4 bảng còn lại.

### 3.3 FIELD summary
Chỉ `#list-quy-trinh-field tbody` thành đúng 8 row:
- `id="step-row-field-s0x"`
- `data-step-code="FIELD.S0x"`
- STT 1..8
- Mã Bước link `#step-detail-field-s0x`
- Tên Bước đúng xương chung
- Nội dung FIELD ngắn, chỉ từ MAP-R3/evidence
- hai cột tổng để trống nếu detail chưa đủ danh sách có evidence
- UI_state thuộc 5 giá trị; **pilot không có UI_OK**

FIELD S04 và S05 = `x` / `KHONG_CAN_UI`.

### 3.4 FIELD detail
Ngay sau bảng FIELD, tạo `<section id="step-details-field">` chứa đúng 8 detail block:
`step-detail-field-s01` ... `step-detail-field-s08`.

Mỗi detail block có:
`lifecycle_state · Điểm vào/UI · Bấm/Hành động · Khai tay · Config máy · Phụ thuộc/nhánh · Kết quả mong đợi · Lỗi/quay về · Nơi quản lý sau tạo · Thông tin quản lý · UI_state · Bằng chứng · manual_count · config_count`.

Không đổi ID bảng hiện có.

## 4. G5 — evidence gate
### 4.1 Nguồn được phép
Factual content chỉ điền khi có ít nhất một:
- URL UI thật đã kê trong HTML;
- path + anchor/dòng/khối tài liệu repo;
- quyết định Dxx/MAP-R3 trong COLLAB;
- commit cụ thể chứa nguồn/quyết định.

FIELD evidence đã định vị:
- `child-UI-018` · Field khai báo trường;
- `child-UI-021` · Kanban FIELD;
- `child-UI-022` · Master Field.

### 4.2 Cấm bịa
- Không có evidence → `CHUA_RA`/để trống.
- Không dùng kiến thức chung để lấp field/config.
- UI tồn tại nhưng chưa có bằng chứng Owner chốt cho đúng step → tối đa `UI_CAN_SUA`.
- manual/config count chỉ ghi khi từng item đã liệt kê và có evidence.

### 4.3 Marker kiểm máy
Mỗi record detail:
- `data-record-state="EVIDENCED|UNKNOWN|NA"`
- EVIDENCED có `data-evidence-ref` không rỗng
- UNKNOWN hiển thị `CHUA_RA`
- NA hiển thị `x`

Cuối lượt:
- `filled_records` = EVIDENCED
- `evidenced_records` = EVIDENCED có evidence-ref hợp lệ
- `unknown_records` = UNKNOWN

Bắt buộc `filled_records === evidenced_records`. Lệch = FAIL.

## 5. Nội dung FIELD được phép
- S01: tìm ở Master Field — UI-022.
- S02: tạo/khai Field — UI-018.
- S03: chỉ dùng các mục thực sự đọc được từ UI-018; nguồn hiện nêu khung tên, định dạng, mô tả, nhóm quản lý.
- S04: `x`.
- S05: `x`.
- S06: Config kỹ thuật Field; chi tiết thiếu evidence → CHUA_RA.
- S07: Test Field/chỗ dùng; chi tiết thiếu evidence → CHUA_RA.
- S08: quản lý ở Master Field + return ID/version theo MAP-R3; schema cụ thể thiếu nguồn → CHUA_RA.

## 6. Kỹ thuật sửa
- File ~1,8 MB; không rewrite toàn file, không prettify/reformat.
- Neo bằng ID duy nhất: `step-quy-trinh-quy-uoc`, `list-quy-trinh-field` và từng table ID khi đổi header.
- Cấm replace generic ba hàng trống giống nhau.
- Dùng expected_version và **một workspace_transaction** cho HTML + COLLAB.
- Không đổi ID hiện có từ D17.

## 7. Acceptance
1. SHA HTML trước/sau + bytes delta.
2. `#list-quy-trinh-field tbody > tr = 8`.
3. MOUT/MOIT/MOT/MOW body vẫn đúng 3 hàng trống.
4. Đúng 8 summary code `FIELD.S01..S08`.
5. Đúng 8 detail ID `step-detail-field-s01..s08`.
6. Header cột 7 của cả 5 bảng = `Trạng thái UI`.
7. Không có `UI_OK` do Agent tạo.
8. `filled_records === evidenced_records`; báo thêm `unknown_records`.
9. Quy ước chứa 8-step + 5-state + evidence + branch/return.
10. Diff không chạm ngoài scope.
11. Nếu mirror VPS đã ở revision mới: mở `/knowledge/modules?task=mow-mot-moit-mout` và kiểm FIELD; nếu chưa, ghi `VIEW_PENDING_REVISION`, Host kiểm sau — không sửa VPS.
12. Mọi record `data-record-state="UNKNOWN"` chỉ chứa nhãn `CHUA_RA`, không chứa mô tả nghiệp vụ; record `NA` chỉ chứa `x`. Vi phạm = FAIL, tự sửa trước khi báo XONG.

## 8. KQ
Cập nhật COLLAB trong cùng transaction:
- RUN_ID
- SHA trước/sau
- field_rows=8 · detail_blocks=8
- filled/evidenced/unknown
- UI_state của 8 step
- PASS/FAIL từng acceptance
- Ghi vào COLLAB trong cùng transaction một dòng `KQ@MMIM-FIELD01-20260923-01 XONG` hoặc `KQ@MMIM-FIELD01-20260923-01 DỪNG`, rồi mới trả Owner dòng XONG/DỪNG theo mẫu.

Báo:
`XONG · MMIM.FIELD01 · field=8/8 · detail=8/8 · evidence=<filled>/<evidenced> · unknown=<n> · ui_ok=0 · main_html_sha=<new> · Owner review FIELD trước khi scale`

Hoặc:
`DỪNG · MMIM.FIELD01 · <lý do cụ thể>`
