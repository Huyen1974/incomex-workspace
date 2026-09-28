# PROMPT — LANE B02R1 · Apply MOW Human-Step Contract v1

RUN_ID: MMIM-LANE-B02R1-20260928-01
PROCESS: CHUNG.APQUYTRINH
STATUS: Chỉ chạy sau PROCESS_GATE PASS + READY của Host.

Host: GPT Chat · Host_ID `GPT-MMIM-260920-A`
Executor: Codex

Write scope:
- `work/mow-mot-moit-mout/ban-duyet.html`
- `work/mow-mot-moit-mout/lane-b/COLLAB.md`

READ-ONLY:
- `cong-cu/dot-process-gate.py`
- `cong-cu/dot-walk-check.py`
- lane-a A02/A03 KQ
- lane-c C01 KQ
- Step/UI/VPS ui.

## 0. Gate

Đọc AGENTS → parent COLLAB D56–D65 → Lane A A02/A03 KQ → Lane B B01/B02 KQ → Lane C C01 KQ → file này.

Trước mutation:
`python3 ../cong-cu/dot-process-gate.py --prompt PROMPT.md --catalog ../ban-duyet.html --json`

FAIL → KQ DỪNG.

A03 đã chốt schema tương thích:
- process attrs **trên chính thẻ `<p ...>`**;
- `dot-walk-check` đã nhận `<p ...><b>CODE</b>`;
- proc-contract span rỗng không làm hỏng walk parser.

## 1. Việc duy nhất

Áp contract-v1 đã chuẩn bị ở B02 vào đúng 12 process:

`CHUNG.TIM · CHUNG.NEU · CHUNG.DUYET · CHUNG.BAT · CHUNG.NGUNG · MOW.TAO · MOW.LAP · MOW.KHAI · MOW.SUA · MOW.XOA · MOW.CHAY · MOT.CHAY`

Giữ nguyên:
- 39 mã/tên;
- thứ tự process;
- logic arrow/call hiện hành;
- read/write refs;
- 27 process còn lại.

Không thêm Human Step mới.

## 2. Process contract v1

Mỗi process trên thêm vào `<p>`:
- `data-contract-v="1"`
- `data-when`
- `data-input-contract`
- `data-output-contract`
- `data-return-contract`
- `data-contract-source="B02R1/D65"`

Mỗi direct Human Step thêm đúng một span rỗng ngay trong step:
`<span class="proc-contract" data-step-key="..." data-right-class="..." data-state-in="..." data-state-out="..." data-return="..." data-ui-intent="..."></span>`

Dùng đúng 15 step-key đã chuẩn bị B02:
`CHUNG.TIM.S01 · CHUNG.NEU.S01 · CHUNG.DUYET.S02 · CHUNG.BAT.S01 · MOW.TAO.S05 · MOW.TAO.S06 · MOW.TAO.S07 · MOW.LAP.S03 · MOW.KHAI.S01 · MOW.SUA.S05 · MOW.SUA.S08 · MOW.CHAY.S07 · MOT.CHAY.S03 · MOT.CHAY.S04 · MOT.CHAY.S08`

`CHUNG.NGUNG` và `MOW.XOA`: opt-in process contract nhưng không có direct Human Step span.

Controlled classes/intents theo A02, không invent ngoài bộ đó.

## 3. CHUNG.TIM bắt buộc

Input:
`target_catalog_code · object_type · query/name/meaning/label · scope(optional) · status/version constraints(optional)`

Output:
- `FOUND_EXACT`
- `FOUND_CANDIDATES`
- `NOT_FOUND`
- `SEARCH_INCOMPLETE`

Kèm candidate id/version + coverage/evidence.

Luật contract:
- `NOT_FOUND` chỉ khi coverage đủ;
- `SEARCH_INCOMPLETE` không được suy thành tạo mới;
- mọi outcome → caller.

Không thiết kế search engine trong RUN này.

## 4. Metadata Human Step

Dùng evidence B02/C01 đã ghi, không nghĩ lại từ đầu:

- tìm → REQUESTER / SEARCH
- nêu nhu cầu → REQUESTER / REQUEST
- duyệt/trả → APPROVER / REVIEW
- khai/sửa → EDITOR / EDIT
- config → CONFIGURATOR / CONFIGURE
- bật → ACTIVATOR / ACTIVATE
- nhận/làm/gửi → ASSIGNEE / EXECUTE
- tệp/bình luận → CONTRIBUTOR / ATTACH
- theo dõi → VIEWER / VIEW

State là semantic process state, không giả DB enum.
Return là step-key kế tiếp hoặc `CALLER` / `PROCESS_END`.
Nếu evidence hiện có không đủ cho một metadata bắt buộc → DỪNG trước mutation thay vì tự bịa.

## 5. Nhìn-thấy-thật

Trong phần summary Process hiện hành thêm một dòng gọn, không tạo UI/file mới:

`Contract v1 · 12/39 process · 15 direct Human Step · nguồn B02R1/C01 · TẠM CHỐT`

Không biến metadata attrs/span thành text dài trên mặt Owner.

## 6. Acceptance bắt buộc

Sau mutation đọc lại source qua gateway rồi chạy:

1. `dot-walk-check.py ban-duyet.html --json` → exit 0 · 84 Master · 39 process · baseline actor/label/calls không lệch.
2. `dot-process-gate.py --audit-contracts --catalog ban-duyet.html --json` → PASS · contract_processes=12 · contract_human_steps=15 · contract_errors=[].
3. E1 gate với prompt này → PASS.
4. 39 code/name + order unchanged.
5. 12 opt-in đúng set; 27 còn lại unversioned.
6. 15 step-key unique.
7. Map C01 25/25 instance → contract source trực tiếp/called; không có orphan.
8. CHUNG.TIM đủ 4 outcome + coverage rule.
9. Không sửa CAT-004/UI/VPS UI.
10. Không file mới.

Nếu A02 audit và walk không cùng PASS → DỪNG, không ghi bản nửa đạt.

## 7. KQ

Append lane-b/COLLAB:

`KQ@MMIM-LANE-B02R1-20260928-01 XONG|DỪNG`

`KQ@LANE-B B02R1 · PROCESS=CHUNG.APQUYTRINH · PROCESS_GATE=PASS|BLOCK · contract_process=12/39 · direct_human=15 · mapped_C01=25/25 · NEXT=C02|<...>`

Báo Owner ngắn:
`XONG · B02R1 · contract=12/39 · human=15 · C01=25/25 · walk=PASS · audit=PASS · NEXT=C02`

Dừng. Không tự C02/B03.
