# PROMPT — MMIM-MOM04 · Kế thừa chi tiết · ? giải thích · ★ cá nhân

RUN_ID: MMIM-MOM04-20260928-01
STATUS: Chỉ chạy sau READY đúng commit cuối chạm PROMPT.md và RUN của Owner/GPT Host.

Host: GPT Chat · Host_ID `GPT-MMIM-260920-A`
Executor: Codex
Write: `workspace_*` root `workspace` + root `ui`
GitHub native/App/API/CLI: READ-ONLY.

## 0. Gate — không làm lại từ đầu

Đọc:
`AGENTS.md` → README D12 → `work/mow-mot-moit-mout/COLLAB.md` §0, **§3 Chi tiết cần đạt**, D44/D46/D49–D55, KQ MOM03 → file này.

Root `ui` đọc:
- `AGENTS.md`, `README.md`
- `master-home-v1.html`, `master-of-master-v1.html`
- `ui-child-content-v1.js`, `ui-child-from-parent-v1.js`
- `master-list.js`, `mot-theme-v1.css`, `mot-master-v1.html`, `child-ui-registry.json`
- **nguồn chi tiết đã làm, chỉ để kế thừa:** `mow-master-nhap2-v1.html`, `nhap2-items.js`, `nhap2-render.js`, `master-drawer-view-v1.js`, `mow-help-doc.js`, `mow-drawer-scope.js`, `moit-master-v1.html`, `mout-master-v1.html`, `field-master-v1.html`.

Đọc `ban-duyet.html#ui-master` và các phần Master/Step/UI/Field hiện hành CHỈ để lấy evidence/label/config đã có.

**Luật:** UI cha là phần tổng quát hoá. Các Mẹ/thiết kế cũ chứa chi tiết nghiệp vụ phong phú hơn và phải được kế thừa. Không được thấy UI cha gọn rồi kết luận hệ thống chỉ có chừng đó.

`mow-master-nhap2-v1.html` là **nguồn tham khảo chi tiết/hành vi đã làm**, không phải parent canonical mới.

Giữ nguyên MOM03 đã đạt:
- Home-first
- 84/84
- 5 pilot
- 10/10 menu đỏ
- TK✓ 5/5 có evidence
- regression 3/3
- ký hiệu/màu 4-state.

Nếu nguồn hiện hành khác các facts trên → DỪNG trước mutation.

## 1. Mục tiêu RUN

Không thiết kế lại kiến trúc.

RUN này chỉ:
A. làm ký hiệu/viết tắt **tự giải thích cho người lần đầu**;
B. thêm **★ yêu thích cá nhân** lưu trình duyệt;
C. đưa **chi tiết đã làm sẵn** của 5 pilot vào `Chi tiết cần đạt` để từ nay làm đầy dần thay vì quay lại từ đầu.

Không làm 79 Master còn lại.

## 2. Cơ chế ? — dùng đúng mẫu đã có

Nguồn chuẩn đã có trong `master-list.js`:
- `.t1-mapping-table__head`
- `.t1-mapping-table__head-label`
- `.t1-mapping-table__help`
- `.t1-mapping-table__tip`

Hành vi chuẩn:
- hover/focus tên cột → hiện `?` + tooltip;
- hover/focus `?` → tooltip;
- tooltip là chữ đầy đủ, dễ hiểu;
- keyboard focus được;
- không tạo kiểu tooltip thứ hai.

### A1. Master of Master — TẤT CẢ tên cột

Mọi header đang nhìn thấy đều phải có help theo đúng cơ chế trên:
- ★ / utility → “Đánh dấu Master yêu thích trên trình duyệt này”
- # → “Số thứ tự”
- Mã → “Mã Master”
- Tên → “Tên Master / danh mục”
- Nhóm → “Nhóm hoặc tầng quản lý”
- QL → “Master này quản lý nội dung gì”
- TK → “Thiết kế”
- LB → “Label / nhãn hiển thị”
- CF·ST·UI → giải thích đủ “Config · Step · UI”
- Σ → “Tình trạng tổng”

Tooltip trạng thái phải giải thích:
`✓ chốt · ◐ đang làm/chờ chốt · ! vướng · ○ chưa làm/chưa có evidence`.

**Không sửa `master-list.js`.**
Adapter CAT post-process DOM sau render để gắn help vào header bằng đúng class/style đã có.

### A2. Home — icon + viết tắt

Mọi ký hiệu người dùng có thể bấm/đọc phải có:
- `title` đầy đủ;
- `aria-label` đầy đủ;
- hover/focus hiện tooltip cùng ngôn ngữ thị giác với cơ chế `?`.

Bắt buộc cho:
`⌂ · ☷84 · T2 · T1 · I · O · F · TK · LB · CF · ST · UI · Σ · ☷ · → · ▦ · ⚙ · i · ☆/★`.

Ví dụ:
- `TK` → “Thiết kế”
- `CF` → “Config / các trường cấu hình cần quản lý”
- `→` → “Step / các bước”
- `▦` → “UI / giao diện”
- `★` → “Đã đánh dấu yêu thích trên trình duyệt này”

Mặt thường vẫn chỉ hiện ký hiệu/ngắn gọn.

## 3. ★ yêu thích cá nhân — browser only

Tạo một cơ chế duy nhất:
- off = `☆`
- on = `★`
- lưu `localStorage`
- key cố định: `incomex.master.starred.v1`
- value: JSON array các Master code.

Tham khảo cách parse/persist an toàn từ `mow-danh-tu-v1.html`; không copy nghiệp vụ GIỮ/GỘP/BỎ.

### Vị trí ★
1. Master of Master: ★/☆ trong **utility cell hiện có**, không tăng cột. Click star phải `stopPropagation`, không mở Home.
2. Master Home: ★/☆ cạnh mã/tên Master.
3. Home gốc: một dải nhỏ `★ n`; nếu n>0 hiển thị tối đa 6 Master đã star bằng mã/tên ngắn; >6 → `+n`. Nếu 0 chỉ hiện `☆0`, không câu dài.

Star:
- chỉ là sở thích cá nhân;
- không đổi TK/LB/CF/ST/UI/Σ;
- không ghi backend/repo;
- reload/navigation/browser reopen vẫn còn;
- click lại để bỏ star;
- localStorage lỗi/bị chặn → UI vẫn chạy, star chỉ không persist và không console error.

## 4. Không làm từ đầu — lập “Chi tiết cần đạt” từ nguồn đã có

### 4.1 Nguồn MOW đã làm nhiều chi tiết

Phải kế thừa ít nhất các capability/source-backed đã có:
- `mow-master-nhap2-v1.html` → shell + list;
- `nhap2-items.js` → code · name · anchor · date · maker · 3 roles · status · liên kết MOT/MOIT/MOUT;
- `master-list.js` → search/filter · edit pencil · open detail · context/tầng · role/status · drawer;
- `master-drawer-view-v1.js` → schema/detail view; field normalization gồm key/type/label/required/placeholder/unit/hint/text/form/fields/options khi nguồn có;
- `nhap2-render.js`, `mow-help-doc.js`, `mow-drawer-scope.js` → các detail/help/contract/support đã tồn tại.

**Không được giảm MOW thành chỉ “List/Step/UI”.**
Home chỉ là cửa vào; chi tiết cần đạt phải ghi lại những gì đã có và những gì còn thiếu.

### 4.2 5 pilot

Pilot:
MOW · MOT · MOIT · MOUT · Field.

Cho mỗi pilot tạo/duy trì một danh sách `detailRequirements` trong data hiện hành của Master đó, không file mới.

Mỗi mục:
- `axis`: LB | CF | ST | UI | DATA | DETAIL
- `key`: mã ổn định nội bộ của yêu cầu
- `label`: tên ngắn dễ hiểu
- `state`: ✓ | ◐ | ! | ○
- `source`: file/section nguồn
- `evidence`: ghi ngắn bằng chứng hiện có
- `next`: việc còn phải làm, nếu chưa ✓

**Chỉ đưa mục có nguồn thật. Không invent field/label/config mới.**

### 4.3 Các chi tiết tối thiểu phải đối chiếu

Không phải checklist cuối cùng; đây là mức sàn để không làm mất thứ đã có:

**MOW**
- trường/dữ liệu của Master list hiện hữu: mã, tên, anchor/tầng, ngày lập, người/máy lập, 3 vai trò, trạng thái, liên kết MOT/MOIT/MOUT;
- tìm/lọc, sửa, mở chi tiết;
- detail/drawer/help/contracts/support có nguồn;
- Step/UI đã kê MOM02.

**MOT**
- mã, tên, anchor, ngày/người lập, MOIT, MOUT, 3 vai trò, trạng thái;
- Studio/Config/Bàn làm việc/List đang dùng;
- Step/UI đã kê.

**MOIT**
- Master list + Studio + Config đang dùng;
- form nhập / các trường config hiện có trong nguồn;
- liên hệ Field nếu nguồn đã ghi;
- Step/UI đã kê.

**MOUT**
- Master list + Builder/Studio đang dùng;
- cấu hình báo cáo đã có trong Builder/source;
- Step/UI đã kê.

**Field**
- Master list;
- khai báo hiện có tối thiểu: tên · định dạng · mô tả · nhóm quản lý (theo ban-duyet);
- các field properties khác chỉ lấy khi source thực có;
- Step/UI đã kê.

Nếu nguồn giàu hơn danh sách sàn → **thêm**, không cắt.

## 5. UI “i · Chi tiết cần đạt”

Trong Home của 5 pilot:
- nút `i` đổi nghĩa rõ thành “Chi tiết cần đạt / nguồn” qua tooltip;
- mở panel nhóm theo LB / CF / ST / UI / DATA / DETAIL;
- đầu panel chỉ hiện count:
  `✓n · ◐n · !n · ○n`;
- mỗi dòng mặt chính: `ký hiệu + label ngắn`;
- source/evidence/next gập hoặc hover/bấm mới xem;
- không đẩy source dài lên mặt đầu.

5 trục LB/CF/ST/UI trên Home phải có tooltip dẫn đến các requirements liên quan.
**Không tự nâng ✓** chỉ vì requirement có source; ✓ vẫn theo evidence Owner/đã chốt.

## 6. “Chi tiết cần đạt” là hợp đồng tiến triển

Trong KQ, Codex phải báo:
- mỗi pilot tìm được bao nhiêu requirement theo từng axis;
- nguồn nào đã kế thừa;
- nguồn nào còn chưa ánh xạ;
- không được báo “đã hoàn thiện” chỉ vì đã đưa lên UI.

Không xóa các detail/gap MOM02/MOM03 đang có.

## 7. Phạm vi sửa

Được sửa tối thiểu:
- `master-home-v1.html`
- `ui-child-content-v1.js`
- `master-of-master-v1.html` chỉ để bổ sung `detailRequirements` vào 5 pilot nếu cần; không đổi 84 code/name.
- `ui-child-from-parent-v1.js` chỉ nếu cần lifecycle hook sau render.

Không sửa:
- `master-list.js`
- `mot-theme-v1.css`
- `mot-master-v1.html`
- các Mẹ nguồn tham khảo
- `ban-duyet.html`
- `eco-nav.js` nếu không có lỗi thực tế MOM03.

Không file/UI ID mới.
Không PG/Directus/runtime.
Không làm 79 Master còn lại.

## 8. Acceptance

1. MOM 84/84, code/name không đổi.
2. Tất cả 10 header MOM có `?`/tooltip đầy đủ; hover/focus PASS.
3. Tất cả icon/viết tắt Home §2 có full title/aria/tooltip; người lần đầu hiểu mà mặt thường vẫn gọn.
4. ★/☆ toggle ở MOM + Master Home; cùng một code đồng bộ trạng thái qua reload/navigation.
5. `localStorage['incomex.master.starred.v1']` persist; star không đổi progress.
6. Home gốc hiện `★n` + tối đa 6 favorite; không dropdown/bảng dài.
7. 5 pilot đều có `detailRequirements` source-backed, không rỗng.
8. MOW requirements chứng minh đã kế thừa nguồn §4.1, không chỉ Step/UI của MOM02.
9. Field có ít nhất tên/định dạng/mô tả/nhóm quản lý với source đúng; không bịa field khác.
10. Panel i hiển thị count ✓/◐/!/○ và drill-down source/evidence/next.
11. Không false ✓ mới trên LB/CF/ST/UI.
12. Home-first/loop MOM03 vẫn PASS.
13. 10/10 menu đỏ vẫn PASS.
14. Field/MOIT/MOUT regression 3/3.
15. Parent hashes `master-list.js`, `mot-theme-v1.css`, `mot-master-v1.html` không đổi.
16. 1280 + 390: không horizontal page overflow; tooltip không tràn viewport.
17. console error mới = 0.
18. KQ:
`KQ@MMIM-MOM04-20260928-01 XONG`
hoặc
`KQ@MMIM-MOM04-20260928-01 DỪNG`.

Báo Owner:
`XONG · MMIM-MOM04 · help_headers=10/10 · help_home=PASS · starred=PASS · requirements=<n> · pilot=5/5 · false_green=0 · loop=PASS · regressions=3/3 · home=<url>`

## 9. Dừng

XONG cũng dừng.
Owner phải nhìn:
⌂ Home → ☷84 → hover tên cột/? → ★ một Master → mở Home → i Chi tiết cần đạt.
Không tự làm 79 Master.
