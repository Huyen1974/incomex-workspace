# PROMPT — LANE A04 · Dứt điểm 5 List Master xanh

RUN_ID: MMIM-LANE-A04-20260928-01
PROCESS: VEUI.MOW
STATUS: Chỉ chạy sau PROCESS_GATE PASS + READY của Host.

Host: GPT Chat · Host_ID `GPT-MMIM-260920-A`
Executor_Surface: Codex

Write_Path:
- root=`ui`: chỉ `master-of-master-v1.html`, `master-home-v1.html`, `ui-child-content-v1.js` nếu cần.
- root=`workspace`: chỉ append KQ vào `work/mow-mot-moit-mout/lane-a/COLLAB.md`.
Không tạo file mới. Không sửa Process/Step/Tool/CAT-004.

## 0. Gate
Đọc `AGENTS.md` → `ui/AGENTS.md` → parent `work/mow-mot-moit-mout/COLLAB.md` D54/D55/D58/D67/D68 → lane-a/COLLAB → file này.
Chạy E1 process gate trên PROMPT + canonical catalog trước mutation. FAIL → DỪNG.

## 1. Owner checkpoint
Vòng này chỉ làm **List Master**. Không làm thêm việc khác.

Owner phải nhìn được:
`⌂ Master → ☷84 → chọn Master → List → thấy nội dung list → mở row → đọc Detail`.

Một List chỉ được ✓ nếu đã kiểm thật:
- có row/item baseline dùng được;
- row có các trường chuyên môn chính;
- mở row có Detail đủ đọc;
- Detail có source/evidence hoặc đường quay về nguồn;
- mock/chưa nối PG phải ghi rõ nhưng không tự làm mất ✓ nếu baseline thiết kế đã đủ dùng.

Tên/mã/route/UI tồn tại **không đủ** để ✓.

## 2. Host đã kiểm UI thật — trạng thái phải giữ

### MOW · CAT-003? · UI-001 = ✓
- List thật: 7 row.
- Row thấy: mã, tên, T3, T2, T1, máy/mục tiêu, vai, trạng thái.
- Detail mẫu WF-0001: bảng bước quy trình, 3 câu hỏi phát hành/kết nối/đo kết quả, checkpoint/data links.
- Ghi rõ runtime/PG còn gap, nhưng baseline thiết kế list+detail dùng được.

### MOT · CAT-009? · UI-002 = ✓
- List thật: 7 row.
- Row thấy: mã, tên, T3/T2/T1, vai, trạng thái.
- Detail mẫu TSK-0001: MOIT+MOUT, form, đường 7 tầng, trigger/hàng đợi/điều kiện, 3 vai, PG table.

### MOIT · CAT-204* · UI-013 = ✓ baseline thiết kế
- List thật: 6 row.
- Row thấy: mã, tên, T3/T2/T1, vai, trạng thái.
- Detail mẫu MOIT-F-0001: form/schema nhập, đường 7 tầng, PG status, link Config.
- Phải giữ nhãn `dữ liệu minh họa · chưa nối nguồn thật`; không được biến thành production-ready.

### MOUT · CAT-205* · UI-014 = ✓ baseline thiết kế
- List thật: 6 row.
- Row thấy: mã, tên, T3/T2/T1, vai, trạng thái.
- Detail mẫu RPT-0010: report/schema, đường 7 tầng, PG status, link Builder.
- Phải giữ nhãn minh họa/chưa nối PG.

### FIELD · CAT-202* · UI-022 = ◐, KHÔNG ✓
- Chỉ 3 row minh họa.
- Detail hiện generic; chưa chứng minh đủ thông tin đặc thù Field: kiểu dữ liệu, đơn vị, required, placeholder/help, format/validation/mapping.
- Giữ UI/List hiện có làm baseline đang làm; hạ List state về ◐ cho đến khi detail Field đủ.

JEV tham khảo: `gen-dec-1790563559-Hw8DqJpnhqbMiqGki3W3` thận trọng chấm WARN cả 5. Host không theo JEV cho 4 list đầu vì D55 định nghĩa xanh = baseline thiết kế dùng được, không phải production/PG hoàn tất; Host đồng ý WARN cho Field.

## 3. Đưa nội dung List đã kiểm vào Master of Master

Trong đúng 5 record pilot của `master-of-master-v1.html#catalog-data`, thêm metadata dẫn xuất `listBaseline` (tên field có thể khác nếu code hiện hành có convention tốt hơn) với tối thiểu:
- `state`: ok|warn
- `symbol`: ✓|◐
- `listCode`
- `rowCount`
- `rowFields`: các trường chính người nhìn thấy trên một row
- `detailSections`: các khối nội dung người đọc được khi mở row
- `sampleDetail`: mã mẫu đã kiểm
- `sourceUrl`
- `sourceFiles` + SHA/version đo lại lúc RUN
- `evidence`: tóm tắt ngắn bằng chứng UI thật
- `gap`
- `verifiedAt`: 2026-09-28
- `decision`: D67

Đây là **evidence snapshot đã kiểm**, không phải SSOT record nghiệp vụ. Không copy toàn bộ dữ liệu 7/6 row sang Master of Master.

79 Master khác giữ nguyên dữ liệu; tuyệt đối không tự gắn List ✓ cho chúng.

## 4. Hiển thị

### Master of Master
Không thêm cột mới nếu phá khuôn cha.
Nhưng 5 pilot phải nhìn nhanh được `List ✓7`, `List ✓6`, hoặc `List ◐3` trong vùng hiện có phù hợp (QL/summary/help), có tooltip giải thích.

### Master Home · tab List
Không được chỉ hiện:
`✅ UI-xxx · Mở danh sách`.

Phải hiện:
- `List ✓/◐ · <n> dòng · <UI code>`
- `Row gồm:` rowFields
- `Detail gồm:` detailSections
- `Nguồn:` source URL + version/hash
- `Gap:` nếu có
- nút `Mở List`
- link `Mở detail mẫu` tới sampleDetail thật.

Không rút gọn/mất các chi tiết trong UI xanh.

## 5. Test bắt buộc

1. 84 Master còn đủ, mã không đổi.
2. 5 pilot có listBaseline đúng verdict Host: 4 ✓ + Field ◐.
3. MOW: Master→List thấy 7 + schema; WF-0001 detail mở được.
4. MOT: 7 + TSK-0001 detail.
5. MOIT: 6 + MOIT-F-0001 detail; chữ minh họa/chưa nối nguồn thật vẫn rõ.
6. MOUT: 6 + RPT-0010 detail; chữ minh họa/chưa nối PG vẫn rõ.
7. Field: ◐3, không ✓; full_name detail mở được và gap Field-specific hiện rõ.
8. 79 Master khác không false-green List.
9. 1280 + 390: không horizontal overflow; List/detail links dùng được.
10. Functional console errors=0; CSP Google Fonts cũ không tính functional.
11. Parent hashes `master-list.js`, `mot-theme-v1.css`, `mot-master-v1.html` không đổi.
12. Không tạo dataset nghiệp vụ song song.

## 6. KQ
`KQ@MMIM-LANE-A04-20260928-01 XONG|DỪNG`
`KQ@LANE-A A04 · PROCESS=VEUI.MOW · PROCESS_GATE=PASS|BLOCK · list_checked=5/5 · list_green=4 · list_warn=1 · false_green=0 · HUMAN_CHECK=WAIT_OWNER · NEXT=OWNER_LOOK`

Báo Owner:
`XONG · A04 · MOW✓ MOT✓ MOIT✓ MOUT✓ FIELD◐ · Master→List→Detail=PASS · NEXT=OWNER_LOOK`

Dừng. Không tự mở A05/B/C.
