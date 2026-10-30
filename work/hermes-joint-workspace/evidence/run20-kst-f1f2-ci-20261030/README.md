# RUN20 · KST rà độc lập F1/F2 + CI của PR #358 (commit `58a44c0`)

RUN_ID `HJW-G8-KST-F1F2-CI-REVIEW-20261030-20` · executor Claude Code CLI/MacBook (KST) · READY@`c51f9b5b` · STARTED `3e0f0bc0` · đo 2026-10-30 09:26–09:35Z.
**Kết luận: `KST_SCOPED_F1F2_REVIEW_PASS`.** Không phải `KST_ACCEPT@SHA`, không cho merge/release, không phải G8_SYSTEM.

## S0 · Pin (đọc tươi lúc 09:26Z và 09:35Z)
| Ref | Giá trị | Trạng thái |
|---|---|---|
| PR #358 | head `58a44c0559bfd42e7e62f5faf8df49ebd2259e78`, base `b4c9ea19…`, 8 files | OPEN/DRAFT |
| PR #357 | head `36c682914c9f412078113b6d85319f11356d1130` | OPEN/DRAFT |
| main | `b4c9ea19cf2e57594a231c2819e098fe0002c99a` | không đổi |
| commit `58a44c0` | parent `4851f6cd`; đúng 3 path: `ghm-pr-gate.yml` +1/−1, `declaration_contract.py` +9/−3, `tests/unit/test_hjw_four_facts.py` +311 (mới) | khớp P478/P479 |
| Ruleset `main-code-gate` | active, bypass rỗng, PR + required `gate` (15368), cập nhật 29/10 08:01 +07 (trước RUN19) | không đổi |
| `deploy-vps.yml` | `disabled_manually` | không đổi |

## S1.1 · F1 `target_task`
| Ca | Kết quả |
|---|---|
| `work/alpha[/…]`, `work/done-tasks/alpha[/…]`, có/không `/` cuối | `alpha` |
| đóng/mở lại `work/alpha` ↔ `work/done-tasks/alpha` (thư mục và tệp), nhiều operations, lồng `arguments` của `workspace_task_start` | `alpha` |
| khác task (`alpha` → `done-tasks/beta`) | `Denied CONTEXT_CLARIFICATION_REQUIRED` |
| `work`, `work/done-tasks`, rỗng, `/`, `..`, `.`, `//`, `\`, ký tự điều khiển, `​`, chữ toàn khổ, dấu gạch Unicode, `Work/` | `None` (không suy) |
| khai task `beta` khi path thuộc `alpha` | Denied, 0 mutation |
| Path độc hại bị bỏ qua có làm sai task khi ghi thật không? Ghi thử `work//beta`, `work/./beta`, `work/alpha/../beta`, `work/beta\q` với task khai `alpha` | gateway trả `PATH_NOT_ALLOWED`, **0 tệp** ⇒ bỏ qua an toàn |
| `target_task` có dùng cho quyền không | không — chỉ `resolve()` gọi; ACL Hermes riêng |

## S1.2 · 118 test mới
- Mac Python 3.11.6, đúng bộ deps CI: tệp mới **118 passed**; danh sách TESTS CI (6 tệp) **151 passed**.
- **RED độc lập:** thay `declaration_contract.py` bằng bản ở parent `4851f6cd` ⇒ **20 failed / 98 passed**; trả lại ⇒ 118 passed (khớp P478).
- Mock chỉ `ensure_supervisor`, `os.nice`, `socket`/`urllib` (công cụ import); contract + `workspace_tools` chạy thật trên filesystem tạm; ca âm kiểm byte trước/sau = 0 mutation. Không mock logic đang kiểm.

## S1.3 · Workflow CI
- `git diff main…58a44c0 -- .github` = **đúng 1 dòng**: thêm `tests/unit/test_hjw_four_facts.py` vào mảng `TESTS` của bước Unit tests. Không `if test -f`, không `|| true`, không `continue-on-error`; `set -euo pipefail` giữ nguyên ⇒ thiếu tệp thì pytest thoát ≠0 (P478 đo exit 4).
- Trigger, permissions `contents: read`, concurrency, runner, timeout, preflight (actor/lane/fork/EXECUTING_WORKFLOW_MISMATCH), gitleaks, actionlint/policy, summary: **không đổi**.
- Run [41025111338](https://github.com/Huyen1974/agent-data-test/actions/runs/41025111338) job `123961272485` `gate`: success; meta `head_sha=58a44c05…`, `merge_test_sha=executing_workflow_sha=c22c9192…`, `gate_matches_main=false`, `ci_change_kst_review=true`, policy GREEN, actionlint success; log TESTS chứa tệp mới; `151 passed in 8.94s`, **0 skipped/deselected**.

## S1.4 · Giao thoa PR #357 / quyền Hermes
- RUN19 không chạm `workspace_tasks.py`/queue/schema; F1 chỉ đổi giá trị fact `task_id`, không đổi khoá job hay cột queue.
- Ghép PR357 lên PR358 trên Mac với bản giải 2 dòng P476 (`'_declaration'` vào `request`, `payload_hash(declaration.bind_hash(a))`), chạy 4facts + `tests/continuation/test_vpsc2_w4q05_queue.py` 5 lần: 3 lần **125 passed**, 2 lần đỏ đúng ca `test_two_processes_same_id_at_once_queue_one_job`. **PR357 chạy riêng cũng đỏ ca này 2/5** ⇒ nợ fresh-DB SQLite có sẵn (P476/P477), không do F1.
- `test_declaration_does_not_grant_hermes_tools_or_paths` PASS; `workspace_declaration.py` không đổi trong RUN19.

## Ghi chú không chặn (để Host gom vào RUN coverage)
1. Khai `task_id` dạng `done-tasks/alpha` hoặc `work/done-tasks/alpha`: có path ⇒ bị từ chối (fail-closed, 0 mutation, lời nhắn chưa chỉ ra cần khai `alpha`); không có path ⇒ ghi canonical `done-tasks/alpha` ≠ `alpha`. Do `canonical()` (không thuộc delta) chưa bỏ tiền tố `done-tasks/` như `target_task`.
2. Tệp test mới không có marker `unit`: chạy `pytest` mặc định theo `pytest.ini` (`-m unit`) sẽ bỏ qua; CI dùng `-o addopts=''` nên không ảnh hưởng gate.
3. Coverage trước G8_SYSTEM (P477/PROMPT S1.5, chưa làm): `workspace_exec` NON_SOURCE/state queue · KB write tools · trusted auto-derive actor/environment · PR357 fresh-DB bootstrap race · Linux AD rebuild/rollback · C1/C2 AI thật. CI 151 xanh **không** chứng minh các mục này.

## 0 mutation
0 push/merge/rebase/đổi trạng thái PR, 0 rerun/bật workflow, 0 VPS/Docker. Clone/venv/overlay chỉ trong scratch Mac, đã xoá sau lượt.
