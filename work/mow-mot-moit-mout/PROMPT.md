# PROMPT — MMIM-MOM03 · ⌂ Master Home trước · ký hiệu/màu trước chữ

RUN_ID: MMIM-MOM03-20260927-01
STATUS: Chỉ chạy sau READY đúng commit cuối chạm PROMPT.md và RUN của Owner/GPT Host.

Host: GPT Chat · Host_ID `GPT-MMIM-260920-A`
Executor: Codex
Write: `workspace_*` root `workspace` + root `ui`
GitHub native/App/API/CLI: READ-ONLY.

## 0. Gate

Đọc repo:
`AGENTS.md` → README D12 → `work/mow-mot-moit-mout/COLLAB.md` §0 + D44/D46/D49–D54 + KQ MOM02 → file này.

Đọc root `ui`:
`AGENTS.md`, `README.md`, `eco-nav.js`, `master-home-v1.html`, `master-of-master-v1.html`,
`ui-child-content-v1.js`, `ui-child-from-parent-v1.js`, `master-list.js`, `mot-theme-v1.css`,
`mot-master-v1.html`, `child-ui-registry.json`.

Đọc `ban-duyet.html#ui-master` + phần Master/Step/UI hiện hành CHỈ để lấy evidence đã có.
Không nghiên cứu lại lịch sử/PG/Directus/JEV.

Giữ toàn bộ MOM02 đã đạt:
84/84 · 5 pilot · 10/10 menu đỏ · regression 3/3.
Không rollback.

Nếu nguồn hiện hành làm các khóa dưới đây sai → DỪNG trước mutation.

## 1. Owner chốt UX mới

MOM02 đúng dữ liệu nhưng khó dùng.

Nguyên tắc mới:

> **Bấm Master một lần → vào ⌂ Trang chủ Master trước.**
> **Từ Home mới vào ☷ 84 (Master of Master) hoặc từng Master/khu vực.**

Không bắt người chọn 1 mã trong dropdown 84 dòng trước.
Không đổ bảng dài ở Home.
Không dùng câu dài khi ký hiệu + màu thay được.

Vòng điều hướng bắt buộc:

```
[Master] → ⌂ HOME → ☷84 → 1 Master → HOME của Master
            ↑                         ↓
            └────────── ⌂ ───────────┘
```

Không dead-end.

## 2. Ngôn ngữ hình/màu duy nhất

Ưu tiên hình/ký tự đã quen hơn chữ:

- **xanh + ✓** = chốt/đạt
- **vàng + ◐** = đang làm / có bản / chờ chốt
- **đỏ + !** = vướng
- **xám + ○** = chưa làm / chưa có evidence

**Không dùng cam.**
Màu luôn đi cùng ký hiệu.
Dùng biến màu sẵn trong `mot-theme-v1.css`: `--ok`, `--warn`, `--bad`, neutral/ink; không tạo palette mới.

Mặt người chỉ dùng mã ngắn:
- `TK` = Thiết kế
- `LB` = Label
- `CF` = Config / trường config
- `ST` = Step
- `UI` = UI
- `Σ` = Tổng

Ví dụ mặt chính:
`TK ✓   LB ◐   CF ○   ST ◐   UI ◐   Σ ◐`

Chữ đầy đủ + nguồn evidence chỉ ở:
`title` / tooltip / aria-label / panel chi tiết khi bấm.

### Quy tắc Σ
1. Có blocker thật → đỏ !
2. Cả 5 trục ○ → xám ○
3. Cả 5 trục ✓ → xanh ✓
4. Còn lại → vàng ◐

## 3. Evidence: không tô xanh bằng suy đoán

Mỗi dấu ✓ phải có evidence pointer.

### TK
Nguồn `ban-duyet.html#ui-master` hiện ghi:
**“UI Master (đã duyệt)” / “ĐÃ DUYỆT”**
và quy chuẩn UI cha → UI con.

Vì 5 Master pilot MOW/MOT/MOIT/MOUT/Field:
- đều có Master list canonical đang dùng,
- đều đi theo UI.MASTER đã duyệt,

=> trong RUN này **TK của 5 pilot = xanh ✓**.
Tooltip phải ghi nguồn: `UI Master · ĐÃ DUYỆT`.

Không suy TK ✓ cho 79 Master còn lại nếu chưa chứng minh cùng điều kiện.

### LB
Registry/nguồn đang có nhiều dòng “Rà nhãn/config sau”.
Có label nhưng chưa chốt → vàng ◐.
Không có evidence label → xám ○.
Chỉ xanh ✓ nếu có quyết định Owner/evidence ghi rõ label đã chốt.

### CF
Có config/trường config bản nháp hoặc cần rà → vàng ◐.
Chưa thấy config → xám ○.
Có mâu thuẫn/blocker → đỏ !.
Chỉ xanh ✓ khi nguồn ghi rõ config/trường config đã chốt.

### ST
Có danh sách Step hiện hành nhưng chưa được Owner chốt toàn bộ → vàng ◐.
Chưa có → xám ○.
Chỉ xanh ✓ khi có evidence Step đã chốt.

### UI
Có mapping/UI hiện hành → vàng ◐, trừ khi nguồn ghi rõ bộ UI của Master đó đã chốt.
UI đỏ không được tính đạt.
Không có mapping → xám ○.
Blocker/mâu thuẫn → đỏ !.

**Không dùng “có file” = ✓.**

## 4. Việc A — nút Master mở HOME ngay

Sửa tối thiểu `eco-nav.js`:

- MOW/MOT/MOIT/MOUT giữ popup/hành vi hiện tại.
- Chip `Master` bấm 1 lần → điều hướng thẳng:
  `./master-home-v1.html`
- Không mở popup Master khi bấm chip.
- Master active/on khi đang ở:
  `master-home-v1.html` hoặc `master-of-master-v1.html`.
- Giữ toàn bộ dữ liệu children cũ trong source; không xóa lịch sử.
- 10/10 đỏ của 4 Mẹ giữ nguyên.

Không tạo nút mới ở thanh 4 Mẹ.

## 5. Việc B — biến master-home-v1.html thành HOME thật

**Không tạo file mới.**
Dùng chính:
`master-home-v1.html`

Hai mode:

### B1. Không có `?master=` → ⌂ MASTER HOME GỐC

**Xóa dropdown 84 Master khỏi mặt người.**

Tầng 1 phải là hub cực ngắn, không cuộn ở 1280:

Trung tâm:
`M` hoặc `⌂ MASTER`

Các nút lớn quanh/bao hub:
- `☷ 84` → Master of Master
- `T2` / MOW → Home MOW
- `T1` / MOT → Home MOT
- `I` / MOIT → Home MOIT
- `O` / MOUT → Home MOUT
- `F` / Field → Home Field

Có thể dùng layout vòng/hub-and-ring hoặc grid vòng kín, nhưng phải nhìn như **một trung tâm → các khu vực**, không như bảng/menu dài.

Mỗi nút pilot chỉ thêm:
- 1 ký hiệu Σ màu
- tối đa 1 số nhỏ nếu cần
- không đoạn mô tả.

Dòng tổng hợp cực ngắn:
`☷84 · TK✓<n> · !<n>`
(n lấy từ dữ liệu thực).

Không có bảng 84 ở Home gốc.

### B2. Có `?master=<code>` → HOME của một Master

**Không dropdown.**

Đầu trang:
- `⌂` → Home gốc
- `☷` → Master of Master
- mã + tên Master

Ngay dưới:
`TK [state]  LB [state]  CF [state]  ST [state]  UI [state]  Σ [state]`

Sau đó 5 nút/khu vực, ưu tiên icon:
- `☷` = List
- `→` = Step
- `▦` = UI
- `⚙` = CF
- `i` = nguồn/chi tiết

**Home chính là Tổng quan nên bỏ tab “Tổng quan”.**

Nút có count nhỏ:
- List: số dòng nếu biết
- Step: số Step
- UI: số UI
- CF: số trường/config nếu biết; chưa biết = ○
- i: không cần count

Ở desktop có thể có chữ cực ngắn dưới icon.
Ở mobile ưu tiên icon; aria-label/title giữ chữ đầy đủ.

Mỗi nhánh dùng dữ liệu MOM02 đã có.
Không invent thêm Step/UI/config.

## 6. Việc C — Master of Master ưu tiên tiến độ bằng ký hiệu

Vẫn dùng UI.MASTER parent.
**Không sửa** `master-list.js`, `mot-theme-v1.css`, `mot-master-v1.html`.

Giữ 84/84 và search/filter.

Mặt bảng đổi label dài thành ngắn tối đa, ưu tiên:
- Mã
- Tên
- Nhóm
- QL
- TK
- LB
- CF·ST·UI
- Σ

Không tăng số cột nếu parent không hỗ trợ; nếu cần, gom `CF ST UI` trong một cell.

Cell tiến độ chỉ hiện ký hiệu/màu:
ví dụ `○ ◐ ◐`, tooltip mới ghi CF/ST/UI.

Không viết “CHƯA RÀ / ĐANG RÀ / CHỜ OWNER...” trong cell mặt chính.

Đầu trang:
- link/nút `⌂` → Home gốc
- summary cực ngắn, ví dụ `84 · TK✓5 · !2`
- dòng “Tiếp theo...” dài hiện tại → bỏ khỏi mặt đầu hoặc gập xuống i.

Mỗi row vẫn mở:
`master-home-v1.html?master=<code>`.

## 7. Việc D — tiến độ 5 pilot

Pilot:
MOW · MOT · MOIT · MOUT · Field.

Bắt buộc:
- TK = xanh ✓ theo evidence §3.
- LB/CF/ST/UI: rà đúng nguồn đang có và gán ○ / ◐ / ! / ✓ theo §3.
- **Không có ✓ nếu không có evidence.**
- Mỗi trục lưu kèm `evidence` trong data/adapter để tooltip đọc được.
- Nếu nguồn mâu thuẫn: !, không tự chọn một phía.

79 Master còn lại:
- không làm đầy nghiệp vụ;
- chỉ chuyển metadata MOM02/RUN02 thành 4-state khi đủ evidence;
- thiếu evidence = ○, không bịa.

## 8. Vòng kín / không lạc

Acceptance điều hướng:

1. Từ bất kỳ UI 4 Mẹ → bấm `Master` đúng 1 lần → Home gốc.
2. Home gốc → `☷84` → Master of Master.
3. Master of Master → bấm 1 row → Home Master đó.
4. Home Master → `⌂` → Home gốc.
5. Home Master → `☷` → Master of Master.
6. Back/forward browser không mất mode/query.
7. Không cần dropdown để đi vòng chính.

## 9. Giới hạn

Không:
- file mới
- UI ID mới
- PG/Directus/runtime
- sửa `ban-duyet.html`
- sửa parent renderer/theme UI.MASTER
- làm đầy 79 Master
- Tool/Process/Factory
- phát RUN tiếp.

Được sửa tối thiểu:
- `eco-nav.js`
- `master-home-v1.html`
- `ui-child-content-v1.js`
- `ui-child-from-parent-v1.js` chỉ nếu CAT topbar/route thực sự cần.

Stat/hash/version trước sửa; expected_version + operation_id.

## 10. Acceptance

1. Master chip: 1 click → `master-home-v1.html`; không popup.
2. Home gốc: không dropdown; có `☷84 · T2 · T1 · I · O · F`; 1280 không cuộn mới hiểu.
3. 390: không tràn ngang; nút vẫn nhận biết bằng hình/ký hiệu.
4. Home pilot: không dropdown; có `⌂ · ☷ · TK/LB/CF/ST/UI/Σ · ☷/→/▦/⚙/i`.
5. 5 pilot TK xanh ✓ và tooltip evidence đúng `UI Master · ĐÃ DUYỆT`.
6. Không false green trên LB/CF/ST/UI.
7. Master of Master 84/84; row có tiến độ ký hiệu/màu, không text dài trạng thái.
8. Master of Master có `⌂` về Home.
9. Vòng điều hướng §8 PASS.
10. 10/10 đỏ 4 Mẹ vẫn PASS.
11. Field/MOIT/MOUT child master regression 3/3.
12. `master-list.js`, `mot-theme-v1.css`, `mot-master-v1.html` hash không đổi.
13. Console error mới = 0.
14. KQ:
`KQ@MMIM-MOM03-20260927-01 XONG`
hoặc
`KQ@MMIM-MOM03-20260927-01 DỪNG`.

Báo Owner:
`XONG · MMIM-MOM03 · home=PASS · dropdown=0 · loop=PASS · masters=84/84 · pilot_TK_green=5/5 · false_green=0 · menu_red=10/10 · regressions=3/3 · url=<home>`

## 11. Dừng

XONG cũng dừng.
Owner phải nhìn ⌂ Home + ☷ Master of Master + 1 Master Home trước khi làm tiếp.
