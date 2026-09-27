# PROMPT — MMIM-MOM02 · Master nhiều tầng + Master Home pilot

RUN_ID: MMIM-MOM02-20260927-01
STATUS: Chỉ chạy sau READY đúng commit cuối chạm PROMPT.md và RUN của Owner/GPT Host.

Host: GPT Chat · Host_ID `GPT-MMIM-260920-A`
Executor: Codex
Write: `workspace_*` root `workspace` + root `ui`
GitHub native/App/API/CLI: READ-ONLY.

## 0. Gate

Đọc: repo `AGENTS.md` → README D12 → `work/mow-mot-moit-mout/COLLAB.md` §0 + D44/D46/D49–D53 + KQ -03 → file này.
Root `ui`: `AGENTS.md`, `README.md`, `eco-nav.js`, `master-of-master-v1.html`, `ui-child-from-parent-v1.js`, `ui-child-content-v1.js`, `master-list.js`, `mot-theme-v1.css`, `mot-master-v1.html`, `child-ui-registry.json`.

Đọc `ban-duyet.html` CHỈ các phần dữ liệu Master/Step/UI hiện hành để lấy dữ liệu đã có; không nghiên cứu lại lịch sử/PG/Directus/JEV.

Giữ toàn bộ phần RUN -03 đã đạt; không rollback.
Nếu nguồn thay đổi làm quyết định dưới đây sai → DỪNG trước mutation.

## 1. Chốt kết quả RUN -03

Host chấp nhận phần lõi RUN -03:
- Master of Master đã dùng đúng UI.MASTER live;
- 84/84 mã/tên;
- renderer/theme/parent không đổi;
- 7 mục APPS đã đỏ đúng.

RUN -03 DỪNG chỉ vì `eco-nav.js` còn 3 mục APPEND MOW không xanh:
- Nháp 1 - MOW Master list
- Ghép miếng - SSOT
- Nháp MOW T1

Theo Owner, cả ba cũng **KHÔNG DÙNG · CHỈ THAM KHẢO**.

## 2. Kiến trúc nhiều tầng đã chốt

```
Master
└─ Master of Master                   L0
   ├─ Master MOW / T2
   ├─ Master MOT / T1
   ├─ Master MOIT / T0.5
   ├─ Master MOUT / T0.5
   ├─ Master Field / T0
   ├─ Master T3…T7 và Master dùng chung khi có nguồn
   └─ ... đủ 84 Master
        ↓ mở một Master
      Master Home                     L1
        ├─ Tổng quan
        ├─ Danh sách                  1 nhánh
        ├─ Step                       1 nhánh
        └─ UI                         1 nhánh
```

Không ép Master dùng chung/Tool/Process/UI vào T0–T7 nếu nguồn không nói vậy.

**Một Home cha duy nhất** cho mọi Master: không tạo 84 file.
Route logic: `master-home-v1.html?master=<MASTER_CODE>`.

Trong RUN này chỉ làm dữ liệu pilot cho:
**MOW · MOT · MOIT · MOUT · Field**.
79 Master còn lại mở Home cùng khuôn nhưng ghi rõ CHƯA LÀM/CHƯA GẮN DỮ LIỆU; không bịa.

## 3. Tiến độ con người nhìn được

Không dùng trạng thái kỹ thuật dài làm mặt chính.

Mỗi Master có 5 trục tiến độ:
1. **Thiết kế**
2. **Label**
3. **Step**
4. **UI**
5. **Tổng**

Từ vựng chuẩn:
- Thiết kế: `CHƯA CÓ` · `CÓ BẢN` · `CHỜ OWNER CHỐT` · `ĐÃ CHỐT`
- Label: `CHƯA RÀ` · `ĐANG RÀ` · `CHỜ OWNER CHỐT` · `ĐÃ CHỐT`
- Step: `CHƯA CÓ` · `CÓ DANH SÁCH` · `ĐANG RÀ` · `ĐÃ CHỐT`
- UI: `CHƯA GẮN` · `CÓ UI` · `ĐANG RÀ` · `ĐÃ CHỐT`
- Tổng: `⚪ CHƯA LÀM` · `🟡 ĐANG LÀM` · `🟠 CHỜ OWNER` · `🔴 VƯỚNG` · `🟢 ĐÃ CHỐT`

**Cấm suy “ĐÃ CHỐT” từ việc có file/UI.**
Chỉ ĐÃ CHỐT khi COLLAB/nguồn có quyết định Owner rõ.
MOW/MOT/MOIT/MOUT/Field hiện có nhiều thiết kế/UI nên ít nhất có thể là CÓ BẢN/CÓ UI; mức cao hơn phải có bằng chứng.

Metadata kỹ thuật cũ Design/Config/UI/Nguồn của RUN -02 vẫn giữ dưới chi tiết, không mất.

## 4. Việc A — đóng hygiene menu

Trong runtime DOM của đúng 4 Mẹ MOW/MOT/MOIT/MOUT:
- mọi mục bắt đầu `✅` giữ nguyên;
- mọi mục còn lại phải hiển thị `🔴 KHÔNG DÙNG · <tên>`;
- description bắt đầu `Chỉ tham khảo ·`;
- URL giữ nguyên.

Current baseline = **10 đỏ** = 7 APPS + 3 APPEND.
Acceptance đếm **DOM sau tất cả APPEND**, không chỉ mảng APPS.
Không áp luật này cho nhóm Master hoặc Đã loại trong RUN này.

Ưu tiên sửa nguồn 3 APPEND cụ thể; không thêm engine/framework.

## 5. Việc B — Master of Master V2

Vẫn dùng UI.MASTER parent; **không sửa** `master-list.js`, `mot-theme-v1.css`, `mot-master-v1.html`.

Mặt list giữ nguyên layout cha. Adapter được đổi label/data để người thấy:
- Mã
- Tên Master
- Nhóm / tầng nếu đã biết
- Quản lý gì
- Thiết kế
- Label
- Tổng

Step/UI chi tiết nằm ở Master Home, không nhồi thêm cột làm vỡ cha.

Mỗi row click/open phải đi tới:
`master-home-v1.html?master=<code>`
không đi thẳng vào một UI cũ bất kỳ.

Ở summary đầu Master of Master phải thấy:
- tổng 84
- bao nhiêu CÓ BẢN thiết kế
- bao nhiêu CHỜ OWNER
- bao nhiêu VƯỚNG
- việc tiếp theo ngắn gọn.

Không tự đổi mã/tên 84.

## 6. Việc C — tạo một UI cha mới: UI.MASTER.HOME candidate

Được tạo đúng **01 file mới**:
`master-home-v1.html`

Đây là **candidate parent**, chưa cấp UI-xxx và chưa thêm menu 4 Mẹ/Master.
Mọi Master dùng chung file qua query `?master=<code>`.

Thiết kế phải “nhìn cái hiểu ngay”:
Tầng 1 không cuộn:
- Tên + mã Master
- Nhóm/tầng
- 5 trạng thái Thiết kế/Label/Step/UI/Tổng
- 3 số: số dòng trong List (nếu biết) · số Step · số UI đang dùng
- **Việc tiếp theo** tối đa 2 dòng.

Ngay dưới là 4 nhánh, cùng vị trí cho mọi Master:
1. `Tổng quan`
2. `Danh sách`
3. `Step`
4. `UI`

Không thêm nhánh khác trong RUN này.

### Nhánh Danh sách
- chỉ link UI đang được phép dùng (✅) nếu có;
- UI đỏ chỉ hiện dưới mục nhỏ `Tham khảo · không dùng`, không làm nút chính;
- nếu chưa có list canonical xanh → ghi `CHƯA CHỐT LIST`, không lấy màn đỏ làm thay.

### Nhánh Step
Lấy dữ liệu đã có trong `ban-duyet.html` cho đúng Master pilot.
Mỗi dòng tối thiểu: Mã Step · Người làm gì · UI dùng · Trạng thái.
Không invent Step mới.

### Nhánh UI
Lấy từ `child-ui-registry.json` + menu runtime:
- ✅ = `ĐANG DÙNG`
- 🔴 = `CHỈ THAM KHẢO`
Mỗi dòng: Mã/nhãn · Tên · parent_id/cha · URL · trạng thái.
Không coi UI có file là đã chốt label/config.

## 7. Pilot 5 Master

Phải làm đầy Home cho:
- MOW
- MOT
- MOIT
- MOUT
- Field

Dùng dữ liệu nguồn hiện có. Không cần toàn bộ 84.

Đối với mỗi Home, đầu trang phải trả lời trong 10 giây:
1. Master này quản lý cái gì?
2. Thiết kế/label/step/UI đang đến đâu?
3. Có bao nhiêu Step và UI đã kê?
4. Đang vướng gì?
5. Tiếp theo làm gì?

Những gì chưa có nguồn → OPEN; không suy.

## 8. Không làm trong RUN này

- không PG/Directus/runtime
- không thêm UI ID mới
- không sửa renderer/theme/parent UI.MASTER
- không hoàn thiện 79 Master còn lại
- không Tool/Process/Factory
- không sửa Step/UI nghiệp vụ; chỉ đưa dữ liệu đã bàn lên Home
- không tạo file ngoài `master-home-v1.html`
- không sửa `ban-duyet.html`

## 9. Acceptance

1. Menu runtime 4 Mẹ: 10 đỏ, 0 mục không-✅ mà chưa đỏ; các ✅ không đổi URL/label.
2. Master of Master vẫn 84/84, đúng UI.MASTER parent.
3. Mỗi row mở đúng Master Home theo code.
4. Master Home là 1 file dùng chung; query đổi Master đổi dữ liệu, layout không đổi.
5. 5 pilot MOW/MOT/MOIT/MOUT/Field có dữ liệu thật; 79 còn lại ghi OPEN/CHƯA LÀM.
6. Không có trạng thái ĐÃ CHỐT nếu không có evidence Owner.
7. 5 pilot có nhánh Tổng quan/Danh sách/Step/UI đúng cùng thứ tự.
8. Step/UI pilot lấy từ nguồn hiện có, không invent.
9. UI đỏ không được dùng làm action chính.
10. 1280 và 390: mặt đầu Home hiểu được, không tràn ngang trang.
11. `master-list.js`, `mot-theme-v1.css`, `mot-master-v1.html` hash không đổi.
12. Field/MOIT/MOUT child masters vẫn regression PASS.
13. Ghi:
`KQ@MMIM-MOM02-20260927-01 XONG`
hoặc
`KQ@MMIM-MOM02-20260927-01 DỪNG`.

Báo Owner:
`XONG · MMIM-MOM02 · masters=84/84 · pilot_home=5/5 · menu_red=10/10 · step_rows=<n> · ui_rows=<n> · false_chot=0 · regressions=<n> · home=<url>`

## 10. Dừng

XONG cũng dừng. Owner phải nhìn Master Home + Master of Master trước khi cho làm đầy 79 Master còn lại.
