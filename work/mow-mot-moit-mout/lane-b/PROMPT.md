# PROMPT — LANE B06 · Phục hồi phần cũ tab ★ Công thức bên dưới

RUN_ID: MMIM-LANE-B06-20260930-01
PROCESS: VEUI.MOW
STATUS: Chỉ chạy sau PROCESS_GATE PASS + READY của Host.

Host: GPT Chat · Host_ID `GPT-MMIM-260920-A`
Executor_Surface: Codex

Write_Path:
- `work/mow-mot-moit-mout/ban-duyet.html`
- `work/mow-mot-moit-mout/lane-b/COLLAB.md`

B06 là writer duy nhất của `ban-duyet.html`.
A08 read-only; C chờ review.

## 0. Luật Owner mới — PRESERVE BY DEFAULT
Chỉ sửa đúng phần Owner chỉ đạo.
**Không được tự xóa, ẩn, gập, dời hoặc viết lại nội dung hiện có ngoài scope.**
Ẩn/gập nội dung khỏi mặt Owner được coi là thay đổi nội dung nhìn thấy và cần Owner chỉ đạo.
Nếu cần tham chiếu bản cũ: dùng Git, không dựng lại bằng trí nhớ.

## 1. Hiện trạng cần sửa
B05 đã làm đúng phần mới:
- header `Công thức và định nghĩa`;
- công thức 7 bước có nhánh;
- định nghĩa Đối tượng;
- `1 Đối tượng = 2 view`.

Nhưng B05 đã bọc phần cũ bên dưới vào:
`<details id="cf-b05-legacy">...`
đóng mặc định.
Owner yêu cầu: **phần cũ đã làm phải tiếp tục hiện ở bên dưới; chỉ khi Owner chỉ đạo xóa mới được xóa.**

## 2. Nguồn phục hồi bắt buộc
Bản ngay trước mutation B05:
`PRE_B05_REF = cfd3764272e42421690a0788c1d9f4a0d632f23e`

Đọc đúng `ban-duyet.html#matrix-view-formula` tại PRE_B05_REF và current.

Không restore cả file/commit.
Không copy snapshot đè lên thay đổi mới.
Chỉ phục hồi phạm vi formula.

## 3. Patch tối thiểu
### Giữ nguyên phần mới phía trên
Các phần current sau phải giữ nguyên nội dung:
- `cf-b05-seven`
- `cf-b05-object`
- `cf-b05-views`
- header `Công thức và định nghĩa`

### Không phục hồi phần Owner đã yêu cầu bỏ/thay
- không phục hồi box `cf-quyet / Anh gật?` ở đầu;
- không đổi header về `Công thức`;
- không thay công thức 7 bước mới bằng 6 bước cũ.

### Phục hồi phần cũ bên dưới
Từ nguồn PRE_B05, phần bắt đầu tại:
`<div class="cf-big" id="cf-dap-an">...`
cho tới hết nội dung cũ của panel formula phải **hiện trực tiếp bên dưới phần mới, theo đúng thứ tự cũ**.

Cách ưu tiên:
1. Nếu current `cf-b05-legacy` đang chứa đủ byte/nội dung cũ → chỉ **unwrap** wrapper/summary/note của B05 để nội dung hiện lại.
2. Nếu thiếu đoạn nào → lấy đúng đoạn thiếu từ PRE_B05_REF.
3. Không biên tập/rút gọn/đổi tên nội dung cũ trong B06.

Giữ nguyên các `<details>` vốn đã tồn tại **bên trong bản cũ**; chỉ bỏ wrapper mới `cf-b05-legacy` do B05 thêm.

## 4. Kiểm chống mất dữ liệu
So pre-B05 với sau B06:
- mọi id cũ từ `cf-dap-an` đến cuối formula còn đủ;
- thứ tự các id cũ giữ nguyên;
- text cũ không bị mất, trừ đúng `cf-quyet` và phần Owner đã thay ở mặt đầu;
- không duplicate id;
- không thay tab khác.

Báo số:
`legacy_ids_before=<n> · restored=<n>/<n> · missing=<n> · duplicates=<n>`.

## 5. UI acceptance
Owner route:
`...section=matrix-view-formula`

Phải thấy:
1. phần 7 bước mới ở trên;
2. ngay bên dưới là toàn bộ phần cũ hiển thị như trước, **không cần mở một details tổng**;
3. các details nguyên gốc bên trong phần cũ vẫn hoạt động;
4. 390/1280 không tràn ngang mới;
5. console functional error=0.

Không sửa JS performance/tab trong B06.

## 6. KQ
`KQ@MMIM-LANE-B06-20260930-01 XONG|DỪNG`
`KQ@LANE-B B06 · PROCESS=VEUI.MOW · PROCESS_GATE=PASS|BLOCK · new_formula_preserved=PASS|BLOCK · legacy_restored=<n>/<n> · missing=<n> · duplicates=<n> · NEXT=C05_VERIFY_PRESERVE`
`COORD · NOW=XONG|DỪNG · NEXT=C05_VERIFY_PRESERVE · BLOCKED_BY=<...> · RESERVED_TARGETS=ban-duyet.html+lane-b/COLLAB.md · LAST_SYNC=PRESERVE-01/B06`

Dừng.
