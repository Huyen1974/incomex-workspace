# CHANGE-PROPAGATION · Quy trình lan truyền thay đổi

## Mục tiêu
Một thay đổi ở **concept / công thức / Master / UI / trạng thái / tên / nguồn** không được coi là xong khi chỉ sửa đúng một chỗ. Agent phải quét tác động, cập nhật các bề mặt liên quan và kiểm lại số đếm/link/trạng thái.

**Nguyên tắc:** máy phải nhớ hộ người. Không bắt Owner nhắc từng bảng phải sửa.

**Cơ chế nhớ/điều hành:** event-driven. Change Event, STARTED/KQ, Owner decision và status transition phải cập nhật Bảng/NEXT/REGISTRY. **Không dùng schedule/polling nền chỉ để nhắc việc nội bộ**; automation chỉ khi có trigger thời gian/điều kiện thật, Owner duyệt và lợi ích đủ bù quota.

## Gate bắt buộc
Trước khi sửa, phân loại thay đổi:

- **DRAFT / REVIEW:** chưa được đưa vào Master/canonical registry đã chốt.
- **APPROVED / CANONICAL:** phải lan truyền tới toàn bộ SSOT + view/index liên quan.
- **REVOKED / SUPERSEDED:** phải rút khỏi canonical nhưng giữ lịch sử/evidence.

Ví dụ UI con:
- Có màn phác thảo ≠ UI con canonical.
- Chỉ khi Owner duyệt mới thêm vào `child-ui-registry.json` và `ML-DEF-018`.
- Khi chưa duyệt, chỉ giữ ở review surface + COLLAB/README.

---

# Quy trình 8 bước

## 1. Tạo Change Event
Ghi một event ngắn:

```text
CE-YYYYMMDD-NNN
TYPE:
ENTITY:
OLD:
NEW:
STATE: DRAFT | APPROVED | REVOKED
OWNER/EVIDENCE:
IMPACT_PROFILE:
```

## 2. Xác định SSOT
Không sửa view trước SSOT. Tra `CHANGE-IMPACT-MAP.json` để biết nguồn chuẩn.

## 3. Quét ảnh hưởng TRƯỚC khi ghi
Tìm ít nhất theo:
- ID/mã;
- tên cũ;
- tên mới;
- status cũ;
- URL/source;
- số đếm/tổng nếu có.

Lập danh sách target: **UPDATE / VERIFY / N/A + lý do**.

## 4. Applicability Gate
Không phải target nào tìm thấy cũng phải sửa:
- lịch sử/KQ cũ → preserve;
- current/live/canonical → update;
- derived view → không viết tay nếu nguồn tự sinh, chỉ verify;
- draft → không được lọt vào canonical.

## 5. Cập nhật cùng một lượt
Ưu tiên một transaction cho các file cùng root. Không để trạng thái nửa cũ/nửa mới.

## 6. Quét lại SAU khi ghi
Lặp lại đúng các từ khóa ở bước 3 để tìm stale reference.
Không được kết luận XONG nếu còn stale reference current/live chưa giải thích.

## 7. Kiểm live
Tối thiểu:
- SSOT đúng số lượng;
- Master/index đúng số lượng/trạng thái;
- link đi đúng đích;
- UI review không tự nhận canonical;
- không sinh duplicate.

## 8. Ghi bằng chứng và đóng
Append COLLAB + REGISTRY:
- Change Event;
- file/bảng đã update;
- target VERIFY/N/A;
- URL live;
- blocker còn lại.

Chỉ đóng khi tất cả target = **PASS hoặc N/A có lý do**.

---

# Quy tắc đặc biệt

## A. Thay đổi trạng thái UI con
### DRAFT → APPROVED
Phải kiểm/cập nhật:
1. review surface;
2. `ui/child-ui-registry.json`;
3. `ML-DEF-018 · Master UI con`;
4. entity/master nào tham chiếu UI đó;
5. danh mục UI con + số đếm;
6. Master index / design review;
7. README/COLLAB/REGISTRY;
8. URL live.

### APPROVED → DRAFT/REVOKED
Làm ngược lại; giữ lịch sử, không tái sử dụng ID đã cấp cho entity khác.

### DRAFT chưa duyệt
**Cấm** đưa vào child-ui-registry hoặc ML-DEF-018.

## B. Thay đổi Công thức
Kiểm:
- mặt Công thức;
- ML-DEF-021;
- FORMULA-AI-README;
- các Master sinh từ công thức;
- Coverage;
- formula candidate/discovery downstream.

## C. Thay đổi định nghĩa / tên khái niệm
Giữ ID ổn định. Quét:
- README/definition;
- Master registry/data;
- Master of Master;
- công thức dùng thành phần đó;
- UI labels;
- aliases/tên cũ để tương thích.

## D. Thay đổi schema Master
Kiểm:
- definition-master-registry;
- definition-master-data;
- list renderer;
- drawer/detail;
- index;
- design review;
- dữ liệu hiện có;
- live page.

---

# Quy tắc số đếm
Mọi số kiểu `29/29`, `27 Master`, `7 công thức` chỉ được sửa ở **current/live summary**. Không rewrite báo cáo/KQ lịch sử.

# Quy tắc lịch sử
COLLAB và KQ cũ là evidence. Nếu quyết định mới đảo quyết định cũ:
- append quyết định mới;
- đánh `SUPERSEDED` trong README/current state nếu cần;
- không sửa lịch sử thành như chưa từng xảy ra.

# Checklist đóng việc
- [ ] Có Change Event.
- [ ] Đã phân loại DRAFT/APPROVED/REVOKED.
- [ ] Đã đọc impact map.
- [ ] Đã quét trước khi sửa.
- [ ] Đã phân UPDATE/VERIFY/N/A.
- [ ] Đã update SSOT trước view.
- [ ] Đã quét stale reference sau sửa.
- [ ] Đã kiểm live.
- [ ] Số đếm khớp.
- [ ] Không draft nào lọt canonical.
- [ ] COLLAB/REGISTRY có evidence.
