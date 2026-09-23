# PROMPT — MMIM.FIELD03 · Thiết kế kịch bản FIELD trên giấy

RUN_ID: MMIM-FIELD03-20260923-01

## 0. Gate
Lượt này **KHÔNG sửa HTML**. Chỉ thiết kế FIELD trong `work/mow-mot-moit-mout/COLLAB.md`.

- Executor_Surface: **Claude Code CLI**.
- Write_Path: **fs_*** đã audit; read-gate bằng `fs_read/fs_stat/fs_log`, ghi bằng `fs_*`.
- Đọc: `AGENTS.md` → `README.md` §0/D12 → COLLAB → prompt này.
- READY phải là commit cuối chạm `PROMPT.md`.
- HTML phải giữ nguyên SHA-256 `1e245ed6997f5dc117bd809807a9e963527068c89cc6985e442b8eeb133099e8`.

## 1. Mục tiêu
Thiết kế FIELD đủ rõ để **một nhân viên mới đọc là biết phải làm gì trong mọi tình huống chính**, trước khi dựng UI/HTML tiếp.

Dùng khung chuẩn:
- **Use case / scenario matrix**
- **CRUD**
- **State machine**
- **Data Dictionary**
- **RBAC / approval**
- **Where-used / impact analysis**
- **ID scheme + code registry**
- **Validation / duplicate / recovery / audit**

JEV là công cụ **chấm/phân loại**, không phải công cụ tự sinh kịch bản.

## 2. Sản phẩm duy nhất trong COLLAB

### A. Bảng kịch bản FIELD
Tách rõ 3 khối đang có:
- `FIELD.S01` · Tìm / dùng lại hay tạo mới
- `FIELD.S02` · Khai Field / tạo đề xuất
- `FIELD.S03` · Gửi đề xuất / hoàn tất bước nhập

Nếu checklist sinh thêm bước thì chỉ thêm `FIELD.S04, S05...` ở cuối; không đảo S01–S03.

Mỗi kịch bản một dòng:
`Mã kịch bản · Bước · Tình huống/trigger · Ai làm · Làm gì · UI nào · Kết quả · Hỏng thì về đâu · Trạng thái (CHOT/CHUA_CHOT/UI_THIEU) · Bằng chứng`.

Mã kịch bản dùng khuôn dễ tìm:
`FIELD.<OPERATION>.<NNN>` — ví dụ `FIELD.CREATE.001`.
Không tự sinh machine ID thật; cột machine_id để `AUTO_GENERATED`.

### B. Checklist tối thiểu phải có dòng
**Create**
- tìm trước khi tạo;
- trùng tên / trùng nghĩa;
- thiếu field bắt buộc / sai định dạng;
- Nhóm quản lý chưa có → tạo tại chỗ → quay lại đúng chỗ;
- bỏ dở giữa chừng;
- lưu/gửi đề xuất thất bại → retry/return;
- đề xuất → ai duyệt → approve/reject → khi nào thành Field vận hành;
- sinh mã / chống trùng mã.

**Read**
- Data Dictionary / Master Field sau khi lưu;
- tìm theo mã/tên; alias nếu có;
- mở chi tiết;
- xem **where-used**: đang được form/quy trình/hợp đồng nào dùng.

**Update**
- đổi tên hiển thị / mô tả nhưng giữ identity;
- đổi Nhóm quản lý;
- đổi định dạng khi đã có dữ liệu → version/migration;
- sửa đồng thời/stale edit;
- thay đổi có cần duyệt lại hay không.

**Deactivate/Delete**
- tạm dừng / kích hoạt lại;
- lưu trữ;
- xoá hẳn khi chưa được dùng;
- đang được dùng → chặn xoá + chỉ rõ where-used;
- quyền ai được ngừng/xoá.

**Cross-cutting**
- quyền đề xuất / duyệt / sửa / ngừng / xoá;
- audit: ai đổi gì, khi nào;
- recovery/rollback;
- alias/search;
- code registry.

Có thể thêm kịch bản mới nếu source cho thấy; không được bỏ dòng chỉ vì UI chưa có — ghi `UI_THIEU`.

### C. Bảng State machine
Dùng mô hình **đề xuất để Owner duyệt**:
`DRAFT → PENDING_APPROVAL → APPROVED | REJECTED → ACTIVE → SUSPENDED → ARCHIVED`.

Mapping UI hiện có:
- ACTIVE = Đang chạy
- SUSPENDED = Tạm dừng
- ARCHIVED = Lưu trữ

Các state DRAFT/PENDING_APPROVAL/APPROVED/REJECTED nếu chưa có nguồn/UI thật → ghi `CHUA_CHOT/UI_THIEU`, không giả là production schema.

Mỗi transition ghi:
`from · action · actor · condition · to · UI · lỗi/chặn`.

### D. Data Dictionary — thiết kế bảng Master Field
Thiết kế danh sách cột để Owner chốt, tối thiểu:
`field_code · display_name · data_type · description · management_group · required · lifecycle_status · version · aliases · where_used · created_by · approved_by · created_at · updated_at`.

Mỗi cột ghi:
`Tên · Ý nghĩa · nguồn hiện có hay đề xuất mới · UI hiện có/thiếu`.

**Không đưa config kỹ thuật/storage address vào FIELD03.**

### E. Master mã / Code registry
JEV Host đã chọn: **human-readable stable code + machine ID ổn định**.

Bảng:
`code · machine_id · loại (STEP/SCENARIO/FIELD/DEPENDENCY...) · đối tượng · tên · version · trạng thái · nơi dùng · ngày`.

Nguyên tắc:
- mã ≠ tên hiển thị ≠ version;
- đổi tên không đổi identity;
- mọi thứ có mã phải tra được trong registry;
- mã bước không trùng giữa các việc;
- machine_id do máy sinh, không tự bịa UUID trong bản thiết kế.

### F. Coverage matrix
Phải có đủ 15 dòng:
`CRUD · lifecycle · approval · RBAC · duplicate · validation · where-used · version/migration · inline dependency · identifier registry · alias search · audit · concurrency · recovery · data dictionary`.

Mỗi dòng:
`COVERED / CHUA_CHOT / UI_THIEU / DEFER_P1` + tham chiếu mã kịch bản.

Owner đã nêu trực tiếp nên các mục sau **không được defer khỏi FIELD03**:
`CRUD · lifecycle · approval · RBAC · validation · duplicate · where-used · inline dependency · identifier registry · data dictionary`.

### G. Danh sách UI thiếu / Owner cần quyết
Cuối cùng chỉ một bảng ngắn:
`Mã · vấn đề · UI hiện có hay thiếu · quyết định cần Owner chốt · ảnh hưởng`.

Không dựng UI trong lượt này.

## 3. JEV
Host đã tham khảo:
- `gen-dec-1790154140-Rr1v83pDBUTboY7xCUo6` — CRUD/validation/where-used/lifecycle/data dictionary/approval/RBAC là các gap nặng.
- `gen-dec-1790154166-yNNIKxwR40A31z4AQMGk` — phân tầng P0/P1.
- `gen-dec-1790154224-LefgUMv5RCl3pRFOcyaA` — lifecycle MODEL_A 0.92; human code + machine ID = 1.00.

Nếu bề mặt Claude Code có JEV Reference, sau khi lập bảng hãy dùng JEV để **judge coverage trên tập đáp án hữu hạn**. Nếu không có thì ghi `JEV_UNAVAILABLE_SURFACE`; không block RUN.

## 4. Luật chống bịa
- Mọi dòng `CHOT` phải có bằng chứng nguồn.
- Không có nguồn → `CHUA_CHOT`.
- Không có màn hình → `UI_THIEU`.
- Không biến đề xuất hội đồng thành “hệ thống hiện đang có”.
- Không sửa HTML, runtime VPS, HVU, connector, config.

## 5. Acceptance
1. HTML SHA không đổi.
2. COLLAB có đủ A–G.
3. S01/S02/S03 tách rõ; bước mới chỉ nối ở cuối.
4. Checklist B không thiếu dòng.
5. Coverage matrix đủ 15 dimension.
6. Có State machine.
7. Có Data Dictionary design.
8. Có Code registry.
9. Có UI gap/Owner decision list.
10. Không có dòng CHOT thiếu evidence.
11. Ghi trong COLLAB:
   `KQ@MMIM-FIELD03-20260923-01 XONG` hoặc `DỪNG`.

## 6. Báo cáo
`XONG · MMIM.FIELD03 · scenarios=<n> · covered=15/15 · owner_decisions=<n> · ui_gaps=<n> · html_unchanged=PASS`

Hoặc:
`DỪNG · MMIM.FIELD03 · <lý do>`
