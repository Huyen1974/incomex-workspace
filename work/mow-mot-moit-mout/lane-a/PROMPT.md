# PROMPT — LANE A05 · List Master acceptance + Field gap

RUN_ID: MMIM-LANE-A05-20260928-01
PROCESS: VEUI.MOW
STATUS: Chỉ chạy sau PROCESS_GATE PASS + READY của Host.

Host: GPT Chat · Host_ID `GPT-MMIM-260920-A`
Executor_Surface: Codex
Write_Path:
- root=ui: chỉ `master-of-master-v1.html`, `master-home-v1.html`, `ui-child-content-v1.js` khi thật sự cần.
- root=workspace: chỉ append KQ vào `work/mow-mot-moit-mout/lane-a/COLLAB.md`.

## 0. Concurrency
Đây là RUN song song A/B/C. Lane khác có thể làm HEAD workspace đổi.
Trước mỗi mutation workspace: re-read HEAD + version của đúng file mình ghi.
- own target không đổi → dùng HEAD mới và tiếp tục;
- own target đã đổi ngoài RUN này → DỪNG `PARALLEL_CONFLICT`.
Không sửa file lane B/C hay ban-duyet.


## 0A. Council Registry / phối hợp

Trước mọi phân tích/mutation:
- đọc `../council/REGISTRY.md` **READ-ONLY**;
- kiểm entry `CODEX-MMIM-A`: Active_RUN đúng `MMIM-LANE-A05-20260928-01`, Reserved_Targets không xung đột scope này;
- nếu Registry nói RUN/scope/Reserved_Targets khác → DỪNG `COORD_CONFLICT`, không tự sửa Registry.

Không sửa `council/REGISTRY.md`; Host quản summary chung.

Khi ghi KQ vào lane-a/COLLAB, thêm trong cùng KQ block:
`COORD · NOW=XONG|DỪNG · NEXT=<một việc> · BLOCKED_BY=<none|lý do> · RESERVED_TARGETS=<ui List targets + lane-a/COLLAB> · LAST_SYNC=D72-D73/A05`.

## 1. Mục tiêu duy nhất
Giữ checkpoint A04: `Master → List → row → Detail`.
MOW/MOT/MOIT/MOUT đã ✓ baseline; **không làm lại**.
A05 chỉ:
1. test lại đường click/keyboard/link của 5 List sau A04;
2. kiểm nguồn Field đã có để xem có đủ dữ liệu thật để nâng FIELD ◐ → ✓ hay chưa;
3. nếu đủ, bổ sung đúng dữ liệu đã có vào Field List/detail và listBaseline;
4. nếu chưa đủ, giữ ◐ và hiển thị chính xác các field còn thiếu, không suy đoán.

## 2. Nguồn Field bắt buộc đọc
- parent `ban-duyet.html`: Field pilot/detailRequirements + FIELD.TAO/LAP/KHAI/SUA/XOA + parent UI standards;
- `master-of-master-v1.html` record CAT-202* + listBaseline A04;
- `ui-child-content-v1.js` Field adapter;
- UI-022 thật + UI-018/config nguồn liên quan nếu được dẫn từ source.

Không tự suy `full_name=text`, `phone_number=tel`... chỉ vì tên trường. Chỉ ghi giá trị nếu source thật chứng minh.

## 3. Điều kiện FIELD được ✓
Mỗi sample row phải đọc được tối thiểu:
`code/name · data type · required · format/validation · mapping/storage`
và nếu source có thì thêm:
`unit · placeholder/help · default/foreign-key`.

Detail phải hiện các giá trị cụ thể cho row, không chỉ form generic dùng chung.
Nếu thiếu bất kỳ lõi bắt buộc nào → giữ ◐.

## 4. Test 5 List
MOW WF-0001; MOT TSK-0001; MOIT MOIT-F-0001; MOUT RPT-0010; FIELD full_name.
1280 + 390.
Kiểm: List text, row count, detail route, visible content, source/gap, no horizontal overflow.
Google Fonts CSP cũ không tính functional error.

## 5. Không làm
Không Process/Step/Tool/PG. Không đổi 4 List ✓ nếu không phát hiện regression thật. Không false-green Field.

## 6. KQ
`KQ@MMIM-LANE-A05-20260928-01 XONG|DỪNG`
`KQ@LANE-A A05 · PROCESS=VEUI.MOW · PROCESS_GATE=PASS|BLOCK · lists=5/5 · FIELD=✓|◐ · click_path=PASS|BLOCK · HUMAN_CHECK=WAIT_OWNER · NEXT=<one thing>`

Dừng.
