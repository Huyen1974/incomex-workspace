# PROMPT — MMIM-MOM01 · Master of Master đúng UI cha

RUN_ID: MMIM-MOM01-20260927-03
STATUS: Chỉ chạy sau READY đúng commit cuối chạm PROMPT.md và lệnh RUN của Owner/GPT Host.

Host: GPT Chat · Host_ID `GPT-MMIM-260920-A`
Executor: Codex
Write: `workspace_*` root `workspace` + root `ui`
GitHub native/App/API/CLI: READ-ONLY.

## 0. Đọc đúng, không khảo sát lan man

Đọc repo: `AGENTS.md` → README D12 → `work/mow-mot-moit-mout/COLLAB.md` (§0, D44, D46, D49–D52, KQ -02) → file này.

Đọc root `ui`: `AGENTS.md`, `README.md`, rồi CHỈ:
`eco-nav.js`, `master-list.js`, `mot-theme-v1.css`, `mot-master-v1.html`,
`ui-child-from-parent-v1.js`, `ui-child-content-v1.js`, `field-master-v1.html`,
`child-ui-registry.json`, `master-of-master-v1.html`.

Dữ liệu 84 dòng đã có trong `master-of-master-v1.html#catalog-data`; dùng lại, không điều tra lại PG/Directus/kho lịch sử/JEV.

Nếu nguồn hiện tại làm các khóa dưới đây không còn đúng → DỪNG trước mutation.

## 1. Khóa kiến trúc

### UI.MASTER canonical
- renderer: `master-list.js`
- theme: `mot-theme-v1.css`
- shell/parent live: `mot-master-v1.html`
- child mechanism: `ui-child-from-parent-v1.js` + `ui-child-content-v1.js`

Căn cứ hiện hành: `mot-master-v1.html` có ✅ trong menu và các Master Field/MOIT/MOUT đang tải parent này qua child loader.

**CẤM dùng làm cha:** `master-hub.html`, `mow-master-nhap2-v1.html`, demo/cũ/tham khảo, hoặc trang chỉ “trông giống Master”.

**Known stale metadata:** một số dòng `child-ui-registry.json` còn `template_url=mow-master-nhap2-v1.html`; D52 xác định đây không phải cha live của RUN này. Không coi lệch này là blocker và **không sửa registry trong RUN -03**.

UI con phải giống cha về shell/layout/số cột/vị trí/font/khoảng cách/màu/icon/nút/detail/filter. Chỉ thay label + data + link. Không fork CSS/renderer.

### Dấu xanh / đỏ trong 4 Mẹ
Trong MOW/MOT/MOIT/MOUT: có `✅` = dùng; không có `✅` = không dùng, chỉ tham khảo.

Baseline phải có đúng 7 mục không xanh:
1. MOW · `MODW · Biến MOW chạy được`
2. MOT · `Quy trình MOT`
3. MOT · `Cấu trúc table`
4. MOIT · `MOIT · Tạo form nhập liệu`
5. MOIT · `MODIT · Biến MOIT chạy được`
6. MOIT · `Kiến trúc input → DB`
7. MOUT · `MODUT · Biến MOUT chạy được`

Không đúng 7 → DỪNG trước sửa menu.

## 2. Việc chính — Master of Master

Mục tiêu duy nhất:

> **Một Master list gốc, chứa tên của tất cả các Master khác.**

Giữ URL `/ui-preview/mcp-writes/master-of-master-v1.html`.

Biến file hiện tại từ page tự vẽ thành UI con của UI.MASTER:
- không CSS riêng;
- không copy DOM/list renderer;
- không copy `master-list.js`;
- wrapper theo cùng nguyên tắc `field-master-v1.html`;
- được giữ 84 dòng data inline.

Được sửa tối thiểu:
- `master-of-master-v1.html`
- `ui-child-from-parent-v1.js`: chỉ thêm config page này
- `ui-child-content-v1.js`: chỉ thêm adapter label/data page này
- `eco-nav.js`: mục §3

**Không sửa:** `master-list.js`, `mot-theme-v1.css`, `mot-master-v1.html`.

### Dữ liệu
Parse JSON `#catalog-data`: accounted 84/84. Không đổi mã/tên, không merge nghi trùng, không query lại nguồn.

Mặt đầu:
- title `Master of Master · Danh sách tất cả Master`
- thấy ngay `84 Master`
- đúng bảng/UI cha
- tối thiểu nhìn được: Mã · Tên Master · Nhóm · Quản lý gì · Tình trạng
- chưa có thông tin thì OPEN/đang hoàn thiện, không bịa.

Thiết kế/Config/UI/Nguồn đã thu ở RUN -02 không được mất; để detail/metadata, không đổ lên mặt đầu.
Không có nút tạo Master trong RUN này.

D46: dùng chính ngôn ngữ UI.MASTER — title + summary + search/filter + bảng + detail. **Không thêm dashboard/card riêng.** Nếu D46 đòi thành phần chưa có ở cha, ghi gap; không sửa cha.

## 3. Việc phụ — đánh đỏ UI không dùng

Chỉ trong `eco-nav.js`, đúng 7 mục §1:
- label → `🔴 KHÔNG DÙNG · <tên cũ>`
- description → `Chỉ tham khảo · <mô tả cũ>`
- giữ nguyên URL.

Không đổi bất kỳ mục ✅ nào.
Không chạm nhóm Master/Đã loại, ngoài việc giữ nguyên `✅ Master of Master`.
Thêm comment đầu file: Owner 27/09/2026 — trong 4 Mẹ chỉ mục ✅ được dùng; 🔴 chỉ tham khảo.

## 4. Kỷ luật

- stat/version/hash trước sửa; expected_version + operation_id.
- không delete/move; không file mới; không reformat file chung.
- không PG/Directus/runtime.
- không sửa `ban-duyet.html`; map MOM01 đã có.
- nếu cần sửa renderer/theme/parent để làm được → DỪNG.

## 5. Acceptance

1. Master of Master HTTP 200; console error do RUN = 0.
2. Source `master-of-master-v1.html` không có renderer/CSS riêng; runtime parent = `mot-master-v1.html`.
3. Hash `master-list.js`, `mot-theme-v1.css`, `mot-master-v1.html` không đổi.
4. 84/84 row; mã + tên khớp data RUN -02.
5. Không scroll nghiên cứu: đầu trang nói rõ Master list gốc + tổng 84.
6. Search mã/tên hoạt động; mở ít nhất 1 detail hoạt động.
7. 1280px và 390px không regression/tràn ngang mới.
8. `field-master-v1.html`, `moit-master-v1.html`, `mout-master-v1.html` vẫn mở và dùng parent như trước.
9. MOW/MOT/MOIT/MOUT có đúng 7 label `🔴 KHÔNG DÙNG`; đúng 7 tên §1.
10. Tất cả mục ✅ cũ giữ nguyên label + URL; `✅ Master of Master` mở đúng page đã sửa.
11. Không file mới; không PG/Directus; không sửa renderer/theme/parent.
12. Ghi COLLAB:
`KQ@MMIM-MOM01-20260927-03 XONG`
hoặc `KQ@MMIM-MOM01-20260927-03 DỪNG`.

Báo Owner khi XONG:
`XONG · MMIM-MOM01-03 · masters=84/84 · parent=UI.MASTER · red_reference=7/7 · regressions=0 · url=<url> · sha=<sha>`

## 6. Dừng sau RUN

XONG cũng không làm tiếp Step/UI/Tool/Process. Owner phải nhìn Master of Master trước.
