# PROMPT — LANE C02 · Chốt MOW Human Step unique + UI unique

RUN_ID: MMIM-LANE-C02-20260928-01
PROCESS: VEUI.MOW
STATUS: Chỉ chạy sau PROCESS_GATE PASS + READY của Host.

Host: GPT Chat · Host_ID `GPT-MMIM-260920-A`
Executor_Surface: Codex
Write_Path: chỉ `work/mow-mot-moit-mout/lane-c/COLLAB.md`.
Canonical + root ui READ-ONLY.

## 0. Concurrency
RUN song song A/B/C. Chỉ ghi lane-c/COLLAB.
Nếu HEAD đổi do lane khác, re-read lane-c version + sources liên quan.
B03 bị cấm đổi 12 contract B02R1; nếu hash/contract của 12 process đó đổi thì DỪNG CONFLICT, nếu không thì tiếp tục.


## 0A. Council Registry / phối hợp

Trước mọi phân tích/mutation:
- đọc `../council/REGISTRY.md` **READ-ONLY**;
- kiểm entry `CODEX-MMIM-C`: Active_RUN đúng `MMIM-LANE-C02-20260928-01`, Reserved_Targets chỉ `lane-c/COLLAB.md`;
- nếu Registry nói RUN/scope/Reserved_Targets khác → DỪNG `COORD_CONFLICT`, không tự sửa Registry.

Không sửa `council/REGISTRY.md`; Host quản summary chung.

Khi ghi KQ vào lane-c/COLLAB, thêm trong cùng KQ block:
`COORD · NOW=XONG|DỪNG · NEXT=<một việc> · BLOCKED_BY=<none|lý do> · RESERVED_TARGETS=lane-c/COLLAB.md · LAST_SYNC=D72-D73/C02`.

## 1. Nguồn bắt buộc
- C01 25 Human Step instances.
- B02R1 map 25/25 → 15 direct step-key/contract source.
- canonical 12 process contract-v1.
- UI xanh/baseline thật: UI-001/004/005 + dependency UI-010/029/011/012 và các parent standards cần cho chữ ký.
- A04 List metadata chỉ tham khảo, không dùng để suy Step.

## 2. Chốt H_MOW
Gộp 25 instance chỉ khi contract chứng minh cùng:
`intent + human input + output + state transition + right-class + return point`.

Cùng step-key qua nhiều caller mặc định là cùng canonical Human Step **trừ khi caller context làm thay đổi một thành phần chữ ký**.
Khác step-key vẫn có thể gộp nếu cả chữ ký thật sự đồng nhất; phải nêu evidence.

Kết quả phải có:
- instances=25;
- canonical Human Step groups = H_MOW;
- mỗi group: members, signature, source step-key, confidence/evidence;
- ambiguity còn lại.

Nếu có 2–5 lựa chọn merge hữu hạn mơ hồ, dùng JEV; ghi result id + confidence. Không dùng JEV thay exact evidence.

## 3. Chốt U_MOW
Từ H groups, gộp UI theo:
`UI parent + human data shape + primary action + state transition`.

Phân loại từng H:
- EXISTING_GREEN/BASELINE;
- VARIANT_CONFIG_LABEL;
- MISSING_UI;
- OPEN_EVIDENCE.

Không đếm route/instance thành UI unique.
Phải trả:
`U_MOW=<n>`
`UI_MISSING=<n>`
và bảng H→UI.

Nếu một count chưa thể chốt, ghi UNKNOWN + đúng blocker; không ép số.

## 4. Kiểm UI thật
Mở các route cần thiết read-only để xác nhận ít nhất một representative cho mỗi UI group.
Không mutate UI.

## 5. KQ
`KQ@MMIM-LANE-C02-20260928-01 XONG|DỪNG`
`KQ@LANE-C C02 · PROCESS=VEUI.MOW · PROCESS_GATE=PASS|BLOCK · instances=25 · H_MOW=<n|UNKNOWN> · U_MOW=<n|UNKNOWN> · UI_MISSING=<n|UNKNOWN> · NEXT=<one thing>`

Dừng. Không sửa canonical.
