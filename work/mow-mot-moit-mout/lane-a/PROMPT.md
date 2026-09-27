# PROMPT — LANE A02 · Process Contract Gate v2

RUN_ID: MMIM-LANE-A02-20260928-01
PROCESS: CHUNG.APQUYTRINH
STATUS: Chỉ chạy sau PROCESS_GATE PASS + READY của Host.

Host: GPT Chat · Host_ID `GPT-MMIM-260920-A`
Executor: Codex
Write scope:
- `work/mow-mot-moit-mout/cong-cu/dot-process-gate.py`
- `work/mow-mot-moit-mout/lane-a/COLLAB.md`
Canonical `ban-duyet.html`: READ-ONLY.

## 0. Gate
Đọc AGENTS → parent COLLAB D56–D61 → lane-a/COLLAB → file này → gate v1.
Trước mutation chạy gate v1 trên chính prompt + catalog. FAIL → DỪNG.

## 1. Mục tiêu
Giữ nguyên E1 hiện hành và thêm kiểm contract v1 mà B02 sẽ gắn vào process.

### Process contract v1
Một definition opt-in bằng:
`data-contract-v="1"`

Khi đã opt-in, process phải có đủ:
- `data-when`
- `data-input-contract`
- `data-output-contract`
- `data-return-contract`
- `data-contract-source`

Mỗi **human step trực tiếp** trong process đó phải có đúng 1 span rỗng gắn ngay trong step:
`<span class="proc-contract" data-step-key="..." data-right-class="..." data-state-in="..." data-state-out="..." data-return="..." data-ui-intent="..."></span>`

Span không được thêm text hiển thị và không làm thay đổi parser bước v1.

## 2. Kiểm mới
- Nếu process không opt-in contract v1: E1 behavior giữ nguyên, không BLOCK vì thiếu contract.
- Nếu opt-in: thiếu bất kỳ field/process-meta/human-step-meta → BLOCK process đó.
- `data-step-key` unique toàn catalog đối với contract-v1.
- controlled right-class: `REQUESTER|APPROVER|EDITOR|CONFIGURATOR|ACTIVATOR|ASSIGNEE|CONTRIBUTOR|VIEWER`.
- controlled ui-intent: `SEARCH|REQUEST|REVIEW|EDIT|CONFIGURE|ACTIVATE|EXECUTE|ATTACH|VIEW`.
- state-in/state-out/return phải non-empty; không phán semantic đúng/sai.
- process-level input/output/return chỉ kiểm có dữ liệu, không phán nghiệp vụ.

Thêm CLI:
`--audit-contracts`
Output JSON/text tối thiểu:
`process_count · contract_processes · contract_human_steps · contract_errors[] · unversioned_processes[]`.
Audit không mutation.

## 3. Test
Fixture riêng:
1. v1 old catalog still PASS.
2. opt-in process đủ metadata PASS.
3. thiếu process attr BLOCK.
4. human step thiếu span BLOCK.
5. duplicate step-key BLOCK.
6. invalid right-class BLOCK.
7. invalid ui-intent BLOCK.
8. machine-only process opt-in không cần step meta.
9. --audit-contracts trả coverage đúng.
Không sửa catalog để test.

## 4. Không làm
- không sửa ban-duyet/CAT-003;
- không thêm process;
- không E3 gateway hard-block;
- không Step/UI.

## 5. KQ
`KQ@MMIM-LANE-A02-20260928-01 XONG|DỪNG`
`KQ@LANE-A A02 · PROCESS=CHUNG.APQUYTRINH · PROCESS_GATE=PASS|BLOCK · contract_gate=PASS|BLOCK · NEXT=<một việc>`
Dừng.
