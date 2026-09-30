# PROMPT — LANE C04 · Kiểm “1 Đối tượng = Master List + Kanban”

RUN_ID: MMIM-LANE-C04-20260930-01
PROCESS: VEUI.MOW
STATUS: Chỉ chạy sau PROCESS_GATE PASS + READY của Host.

Host: GPT Chat · Host_ID `GPT-MMIM-260920-A`
Executor_Surface: Codex

Write_Path: chỉ append KQ vào `work/mow-mot-moit-mout/lane-c/COLLAB.md`.
Canonical + root ui: READ-ONLY.

## 0. Registry / concurrency
Đọc `../council/REGISTRY.md` READ-ONLY.
B05 đang sửa formula; C04 không sửa `ban-duyet.html`.

## 1. Câu hỏi Owner cần câu trả lời
Trong công thức mới:
**Đối tượng = thứ có danh tính + vòng đời riêng, cần tìm/dùng/tạo/sửa/ngừng độc lập.**
**Mỗi Đối tượng cần 2 view: Master List + Kanban.**

C04 phải kiểm xem công thức này có khớp kiến trúc/UI cha đã thực sự có hay không.

## 2. Kiểm đúng 5 đối tượng lõi trước
`MOW · MOT · MOIT · MOUT · Field`

Với mỗi đối tượng, trả:
- Master List hiện có? UI code/route/source/parent?
- Kanban hiện có? UI code/route/source/parent?
- Kanban có thật sự dùng chung khuôn cha đã duyệt không?
- 2 view đang là production/baseline/mock/gap?
- có phải tạo renderer mới không? (mong đợi: không nếu parent đủ)

## 3. “Thứ nhỏ ×18”
Không mặc định chúng là Đối tượng.
Kiểm tiêu chuẩn:
- có identity riêng?
- lifecycle riêng?
- cần reuse độc lập?
- cần Master List riêng?
- cần Kanban riêng?

Chỉ báo:
`QUALIFIES / NOT_PROVEN / NOT_OBJECT`.
Không thiết kế UI mới.

## 4. “6 khuôn cha”
Kiểm xem con số 6 hiện có còn nghĩa gì trong kiến trúc mới.
Không tự sửa.
Trả một trong:
- `KEEP_6` + evidence;
- `REPLACE_WITH_2_VIEW_PARENTS` + evidence;
- `UNKNOWN`.

## 5. Output nhìn cái hiểu ngay
Mặt đầu ≤12 dòng:
- 5 object × [List? Kanban?]
- verdict công thức 2 view = PASS/PARTIAL/BLOCK
- “Thứ” có nên loại khỏi Owner UI = YES/NO
- “6 khuôn cha” = KEEP/REPLACE/UNKNOWN

Chi tiết bảng evidence dưới.

## 6. KQ
`KQ@MMIM-LANE-C04-20260930-01 XONG|DỪNG`
`KQ@LANE-C C04 · PROCESS=VEUI.MOW · PROCESS_GATE=PASS|BLOCK · core_objects=5 · two_view_formula=PASS|PARTIAL|BLOCK · small18=<verdict> · parent6=<verdict> · NEXT=<one thing>`
`COORD · NOW=XONG|DỪNG · NEXT=<...> · BLOCKED_BY=<...> · RESERVED_TARGETS=lane-c/COLLAB.md · LAST_SYNC=FORMULA-01/C04`

Dừng.
