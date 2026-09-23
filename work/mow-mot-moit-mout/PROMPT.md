# PROMPT — MMIM.FIELD03 · Thiết kế kịch bản FIELD trên giấy

RUN_ID: MMIM-FIELD03-20260923-01

## 0. Gate
Lượt này **KHÔNG sửa HTML**. Chỉ thiết kế FIELD trên giấy.

- Executor_Surface: **Claude Code CLI**.
- Write_Path: **fs_*** đã audit; read-gate bằng `fs_read/fs_stat/fs_log`, ghi bằng `fs_*`.
- Đọc: `AGENTS.md` → `README.md` §0/D12 → `work/mow-mot-moit-mout/COLLAB.md` → prompt này.
- READY phải là commit cuối chạm `PROMPT.md`.
- HTML phải giữ nguyên SHA-256 `1e245ed6997f5dc117bd809807a9e963527068c89cc6985e442b8eeb133099e8`.

## 1. Mục tiêu
Thiết kế FIELD đủ rõ để **một nhân viên mới nhìn/đọc là biết phải làm gì trong mọi tình huống chính**, trước khi dựng UI/HTML tiếp.

Khung chuẩn:
- Use case / scenario matrix
- CRUD
- State machine
- Data Dictionary
- RBAC / approval
- Where-used / impact analysis
- ID scheme + code registry
- Validation / duplicate / recovery / audit

JEV chỉ dùng để **judge/phân loại** trên tập kịch bản đã liệt kê; không thay checklist sinh kịch bản.

## 2. Thứ tự sản phẩm — Owner nhìn 30 giây trước

### G. Bảng “Owner cần quyết gì” — ĐẶT ĐẦU TIÊN
Một bảng ngắn:
`Mã · Vấn đề · UI hiện có/thiếu · Đề xuất của hội đồng · Owner: Gật/Lắc/Khác · Hệ quả nếu lắc · Ảnh hưởng`.

Luật:
- **Không có đề xuất của hội đồng thì không được đưa câu hỏi lên Owner.**
- “Hệ quả nếu lắc” phải nói ngắn: phải đổi gì / thiếu gì / bước nào bị ảnh hưởng.
- Chỉ đưa các quyết định thật sự cần Owner; không đưa câu hỏi đã có source rõ.

### Sơ đồ nhìn 30 giây
Ngay sau bảng G, vẽ bằng Markdown/ASCII block + mũi tên, không phụ thuộc renderer:

`[MMIM.FIELD.S01 · Tìm] → [MMIM.FIELD.S02 · Khai] → [MMIM.FIELD.S03 · Gửi đề xuất] → [PENDING_APPROVAL] → [APPROVED] → [ACTIVE] → [SUSPENDED] → [ARCHIVED]`

Nhánh bắt buộc phải nhìn thấy:
- `PENDING_APPROVAL → REJECTED`
- trùng/đã có → quay về dùng lại Field;
- nhóm quản lý chưa có → tạo nhóm → quay lại đúng chỗ;
- sửa/xoá → kiểm where-used trước.

Không biến sơ đồ thành đoạn văn dài.

### A. Bảng kịch bản FIELD
Ba bước gốc:
- `MMIM.FIELD.S01` · Tìm / dùng lại hay tạo mới
- `MMIM.FIELD.S02` · Khai Field / tạo đề xuất
- `MMIM.FIELD.S03` · Gửi đề xuất / hoàn tất bước nhập

Nếu checklist sinh thêm bước thì thêm `MMIM.FIELD.S04, S05...` ở cuối; không đảo S01–S03.

Mỗi kịch bản một dòng:
`Mã kịch bản · Bước · Tình huống/trigger · Ai làm · Làm gì · UI nào · Kết quả · Hỏng thì về đâu · Trạng thái (CHOT/CHUA_CHOT/UI_THIEU/DEFER_P1) · Bằng chứng`.

**Khuôn mã bắt buộc có định danh việc:**
- bước: `MMIM.FIELD.S01`
- kịch bản: `MMIM.FIELD.<OPERATION>.<NNN>`, ví dụ `MMIM.FIELD.CREATE.001`
- registry vẫn có cột `work_id=mow-mot-moit-mout`
- machine_id = `AUTO_GENERATED`, không tự bịa UUID.

**Trần FIELD03:** tối đa **40 dòng kịch bản chính**; mục tiêu reviewable khoảng 35–40 nhưng **không bịa thêm để đủ 35**. Biến thể hiếm vẫn phải có mã/index và ghi `DEFER_P1`, không xoá khỏi coverage.

### B. Checklist tối thiểu phải có
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
- xem where-used: đang được form/quy trình/hợp đồng nào dùng.

**Update**
- đổi tên/mô tả nhưng giữ identity;
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

Không được bỏ scenario chỉ vì thiếu UI: ghi `UI_THIEU`. Biến thể hiếm có thể `DEFER_P1`.

### C. State machine
Dùng mô hình **đề xuất để Owner duyệt**:
`DRAFT → PENDING_APPROVAL → APPROVED | REJECTED → ACTIVE → SUSPENDED → ARCHIVED`.

Mapping UI hiện có:
- ACTIVE = Đang chạy
- SUSPENDED = Tạm dừng
- ARCHIVED = Lưu trữ

DRAFT/PENDING_APPROVAL/APPROVED/REJECTED nếu chưa có source/UI thật → `CHUA_CHOT/UI_THIEU`, không giả là production schema.

Mỗi transition:
`from · action · actor · condition · to · UI · lỗi/chặn`.

### D. Data Dictionary — thiết kế Master Field
Tối thiểu:
`field_code · display_name · data_type · description · management_group · required · lifecycle_status · version · aliases · where_used · created_by · approved_by · created_at · updated_at`.

Mỗi cột:
`Tên · Ý nghĩa · nguồn hiện có hay đề xuất mới · UI hiện có/thiếu`.

Không đưa config kỹ thuật/storage address vào FIELD03.

### E. Master mã / Code registry
Bảng:
`work_id · code · machine_id · loại (STEP/SCENARIO/FIELD/DEPENDENCY...) · đối tượng · tên · version · trạng thái · nơi dùng · ngày`.

Nguyên tắc:
- `work_id = mow-mot-moit-mout`;
- human code luôn có prefix việc `MMIM.`;
- mã ≠ tên hiển thị ≠ version;
- đổi tên không đổi identity;
- mọi thứ có mã phải tra được trong registry;
- mã bước/kịch bản không trùng giữa các việc;
- machine_id do máy sinh.

### F. Coverage matrix
Đủ 15 dòng:
`CRUD · lifecycle · approval · RBAC · duplicate · validation · where-used · version/migration · inline dependency · identifier registry · alias search · audit · concurrency · recovery · data dictionary`.

Mỗi dòng:
`COVERED / CHUA_CHOT / UI_THIEU / DEFER_P1` + tham chiếu mã kịch bản.

Không được defer khỏi FIELD03:
`CRUD · lifecycle · approval · RBAC · validation · duplicate · where-used · inline dependency · identifier registry · data dictionary`.

## 3. JEV
Host đã tham khảo:
- `gen-dec-1790154140-Rr1v83pDBUTboY7xCUo6` — gap chuẩn nghề.
- `gen-dec-1790154166-yNNIKxwR40A31z4AQMGk` — P0/P1.
- `gen-dec-1790154224-LefgUMv5RCl3pRFOcyaA` — lifecycle + ID.
- `gen-dec-1790155411-DvO7VLSj9m2ePlZ3ntQj` — decisions+diagram first = 1.00; work-prefix code = 0.90; cap 35–40/defer rare = 0.98.

Nếu Claude Code có JEV Reference, sau khi lập bảng dùng JEV để judge coverage hữu hạn; nếu không có ghi `JEV_UNAVAILABLE_SURFACE`, không block.

## 4. Luật chống bịa
- Dòng `CHOT` phải có evidence.
- Không có source → `CHUA_CHOT`.
- Không có UI → `UI_THIEU`.
- Đề xuất hội đồng phải ghi rõ là đề xuất, không giả là hệ thống đang có.
- Không sửa HTML, VPS runtime, HVU, connector, config.

## 5. Quy mô file
Mặc định ghi FIELD03 vào COLLAB.
- Trước/sau ghi phải đo bytes.
- Nếu COLLAB sau thiết kế **≤150 KB**: giữ toàn bộ trong COLLAB.
- Nếu sẽ **>150 KB**: tạo `work/mow-mot-moit-mout/FIELD-DESIGN.md` chứa A–F; COLLAB chỉ giữ **G + sơ đồ 30 giây + con trỏ file + KQ**.
- Không bàn lại threshold trong RUN.

## 6. Acceptance
1. HTML SHA không đổi.
2. Mở phần thiết kế thấy **G trước → sơ đồ → A–F**.
3. Mọi dòng G có **Đề xuất hội đồng + Hệ quả nếu lắc**.
4. Sơ đồ có S01/S02/S03 + lifecycle + reject + nhánh phụ thuộc/where-used.
5. Kịch bản chính **≤40 dòng**; rare variant được index `DEFER_P1`.
6. Tất cả step/scenario code có prefix `MMIM.`; registry có `work_id`.
7. S01/S02/S03 tách rõ; bước mới chỉ nối ở cuối.
8. Checklist B đủ các dòng bắt buộc.
9. Coverage đủ 15 dimension.
10. Có State machine.
11. Có Data Dictionary design.
12. Có Code registry.
13. Có Owner decision/UI gap list.
14. Không có CHOT thiếu evidence.
15. Quy tắc 150 KB được áp đúng.
16. Ghi `KQ@MMIM-FIELD03-20260923-01 XONG` hoặc `DỪNG`.

## 7. Báo cáo
`XONG · MMIM.FIELD03 · scenarios=<n<=40> · covered=15/15 · owner_decisions=<n> · ui_gaps=<n> · collab_bytes=<n> · html_unchanged=PASS`

Hoặc:
`DỪNG · MMIM.FIELD03 · <lý do>`
