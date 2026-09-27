# PROMPT — LANE C01 · MOW Human Step → UI

RUN_ID: MMIM-LANE-C01-20260928-01
PROCESS: VEUI.MOW
STATUS: Chỉ chạy sau PROCESS_GATE PASS + READY của Host.

Host: GPT Chat · Host_ID `GPT-MMIM-260920-A`
Executor: Codex
Write scope: chỉ `work/mow-mot-moit-mout/lane-c/COLLAB.md`.
Canonical parent + VPS UI: READ-ONLY.

## 0. Gate
Đọc `AGENTS.md` → parent `COLLAB.md` D36/D46/D56–D59 → lane-c/COLLAB.md → file này.
Đọc:
- `../ban-duyet.html#ml5-cho-ai`: MOW.TAO/LAP/KHAI/SUA/XOA/CHAY + CHUNG.* mà chúng gọi.
- CAT-004 Step + UI catalog/parent standards trong ban-duyet.
- MOM04 KQ: 16 UI xanh + 470 requirements/5 pilot; 470 chỉ là evidence.
- UI xanh thực của MOW: Kanban UI-005 · Master UI-001 · Góp ý UI-004; phụ thuộc UI MOT/MOIT/MOUT chỉ đọc khi process MOW thật sự gọi tới.

Trước mutation lane-c/COLLAB:
`python3 ../cong-cu/dot-process-gate.py --prompt PROMPT.md --catalog ../ban-duyet.html --json`.
FAIL → KQ DỪNG.

## 1. Chỉ làm MOW
Đi bộ 6 process MOW.* và process CHUNG.* được gọi.

Tách:
- **Machine Step instance**: máy làm, không tính H.
- **Human Step instance**: có thao tác/quyết định người.
- **Human Step canonical candidate**: gộp instance chỉ khi cùng
  `intent + input người cung cấp + output + state transition + quyền + điểm quay về`.

Không gộp chỉ vì tên gần giống.
Không tách chỉ vì đối tượng MOW/MOT/Field khác nếu interaction thực giống nhau.

## 2. Map UI
Mỗi Human Step canonical candidate:
- UI hiện có xanh nào dùng được;
- dùng cùng UI cha + label/config;
- hay thật sự thiếu UI.

Chữ ký UI để gộp:
`UI parent + loại dữ liệu nhập + hành động chính + state transition`.

Phân biệt:
- UI instance/route;
- UI child/config variant;
- **UI unique** người dùng thực sự phải học/tương tác.

## 3. Trình bày D46
Mặt đầu lane C chỉ ≤10 dòng:
- MOW process đã đi: 6/6;
- human step instances = n;
- canonical Human Step candidates = H_MOW;
- UI routes gặp = n;
- UI unique candidates = U_MOW;
- UI thiếu = n;
- 3–5 điểm OPEN quan trọng.

Chi tiết mapping gập dưới.

## 4. JEV
Nếu có 2–5 candidate merge mơ hồ, dùng JEV choice/noul để hỗ trợ.
Không dùng JEV khi exact rule đủ.
Nếu không bind JEV, ghi OPEN.

## 5. Không làm
- không sửa CAT-004/UI catalog/ban-duyet;
- không sửa VPS UI;
- không làm FORM/MOT/FIELD ở C01;
- không đếm 470 requirements thành Step;
- không cấp mã Step/UI mới;
- không tự C02.

## 6. KQ
Append lane-c/COLLAB:
- Human Step instance table;
- canonical candidate table;
- Step→UI mapping;
- OPEN/ambiguous + JEV evidence;
- NEXT đúng một batch.

KQ:
`KQ@MMIM-LANE-C01-20260928-01 XONG|DỪNG`
`KQ@LANE-C C01 · PROCESS=VEUI.MOW · PROCESS_GATE=PASS|BLOCK · HEAD=<sha> · H_MOW=<n> · U_MOW=<n> · UI_MISSING=<n> · NEXT=<một việc>`

Dừng.
