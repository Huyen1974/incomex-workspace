# PROMPT — LANE B03 · Contract batch FIELD/FORM/MOT authoring

RUN_ID: MMIM-LANE-B03-20260928-01
PROCESS: CHUNG.APQUYTRINH
STATUS: Chỉ chạy sau PROCESS_GATE PASS + READY của Host.

Host: GPT Chat · Host_ID `GPT-MMIM-260920-A`
Executor_Surface: Codex
Write_Path:
- `work/mow-mot-moit-mout/ban-duyet.html`
- `work/mow-mot-moit-mout/lane-b/COLLAB.md`

## 0. Concurrency
RUN song song A/B/C. Trước mutation re-read own target version + current HEAD.
HEAD đổi nhưng own target không đổi → dùng HEAD mới, tiếp tục.
Own target bị lane khác chạm → DỪNG PARALLEL_CONFLICT.
Không sửa lane-a/lane-c/PROMPT khác.


## 0A. Council Registry / phối hợp

Trước mọi phân tích/mutation:
- đọc `../council/REGISTRY.md` **READ-ONLY**;
- kiểm entry `CODEX-MMIM-B`: Active_RUN đúng `MMIM-LANE-B03-20260928-01`, Reserved_Targets đúng `ban-duyet.html + lane-b/COLLAB.md`;
- nếu Registry nói RUN/scope/Reserved_Targets khác → DỪNG `COORD_CONFLICT`, không tự sửa Registry.

Không sửa `council/REGISTRY.md`; Host quản summary chung.

Khi ghi KQ vào lane-b/COLLAB, thêm trong cùng KQ block:
`COORD · NOW=XONG|DỪNG · NEXT=<một việc> · BLOCKED_BY=<none|lý do> · RESERVED_TARGETS=ban-duyet.html+lane-b/COLLAB.md · LAST_SYNC=D72-D73/B03`.

## 1. Giữ nguyên 12 contract B02R1
Tuyệt đối không đổi:
CHUNG.TIM/NEU/DUYET/BAT/NGUNG · MOW.* 6 · MOT.CHAY.
Đó là snapshot C02 đang đọc.

## 2. Batch ứng viên mới
Chỉ xét 13 process đã tránh các definition branch mơ hồ B01:
- CHUNG.CAPMA · CHUNG.KIEM
- FIELD.LAP · FIELD.SUA · FIELD.XOA
- FORM.TAO · FORM.LAP · FORM.SUA · FORM.XOA
- MOT.TAO · MOT.LAP · MOT.SUA · MOT.XOA

Mục tiêu: opt-in contract-v1 **chỉ những process đủ evidence**.
Không ép đủ 13. Một process thiếu quyền/state/return/input/output → để unversioned + OPEN, không bịa.

## 3. Contract
Dùng schema A02/B02R1:
process attrs: when/input/output/return/source.
Direct Human Step: step-key/right-class/state-in/state-out/return/ui-intent.

Giữ code/name/order/logic/read-write refs.
Machine-only process có thể opt-in mà không có human span.
Step-key unique toàn catalog.

## 4. Acceptance
- walk-check 39 / 0 lỗi;
- contract audit 0 lỗi;
- 12 B02R1 process byte-equivalent contract attrs/spans trước/sau;
- new opt-in set chỉ nằm trong 13 candidate;
- không sửa CAT-004/UI;
- báo `new_contract=<n>/13`, `open=<n>`, `total_contract=12+n`.
- với OPEN, ghi lý do cụ thể và NEXT batch; không gọi nó “đạt”.

## 5. KQ
`KQ@MMIM-LANE-B03-20260928-01 XONG|DỪNG`
`KQ@LANE-B B03 · PROCESS=CHUNG.APQUYTRINH · PROCESS_GATE=PASS|BLOCK · new_contract=<n>/13 · total_contract=<n>/39 · open=<n> · NEXT=<one thing>`

Dừng.
