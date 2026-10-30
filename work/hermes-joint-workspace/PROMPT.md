# HJW · RUN20 — Claude Code CLI KST rà độc lập F1/F2 và CI của PR #358, KHÔNG MERGE/DEPLOY
RUN_ID: HJW-G8-KST-F1F2-CI-REVIEW-20261030-20
STATUS: FINAL_PROMPT; chỉ bắt đầu sau READY@full last-touch PROMPT commit do GPT Chat Host ký trong HJW COLLAB và Owner chuyển tay. NO AUTO_RUN.
Executor_Surface: Claude Code CLI trên MacBook (KST code reviewer, không phải Host); GPT Chat Host chốt. REVIEW_REUSED=P470/P476 cho thiết kế gốc; RUN20 là kiểm độc lập **delta mới** của RUN19 (không giả đã review).
Write_Path: Git/GitHub chỉ ĐỌC PR #357/#358/CI; worktree/lab có thể tạo trên Mac rồi dọn. HJW STARTED/P480/KQ/Bảng/evidence ghi qua Workspace Gateway D12 (không qua GitHub native direct write cho workspace). Không sửa mã nguồn trên GitHub hay VPS.
Read_First: AGENTS.md A0/A2/A5/A6/DROOT30/31/56/58/60 + GHM_CODE_CHANNEL → README §11/D12 → root COLLAB current busy → HJW COLLAB §0/§1–3/Bảng/P458/P476–P479 → PROMPT này → PR #358, PR #357, RUN19 evidence README+RED/GREEN+ci-evidence, GitHub Actions run 41025111338.

## A. Mục tiêu chốt / ranh giới
RUN19 Codex P478 đã XONG **G8_AD_F1F2_SOURCE_CI_PASS** trong phạm vi ứng viên. PR #358 vẫn OPEN/DRAFT, HEAD `58a44c0559bfd42e7e62f5faf8df49ebd2259e78`, base/main `b4c9ea19cf2e57594a231c2819e098fe0002c99a`, 8 tệp. RUN19 chỉ đổi **3 đường**:
- `agent_data/declaration_contract.py` — F1: `target_task` nhận diện đúng mã việc ở `work/done-tasks/<id>/...` và đóng/mở lại.
- `tests/unit/test_hjw_four_facts.py` — 118 regression tests check-in, test RED 20 fail/98 pass trước sửa và GREEN 118 pass sau.
- `.github/workflows/ghm-pr-gate.yml` — đúng một thay đổi mảng TESTS của Unit tests, gọi file HJW mới bắt buộc.
CI [run 41025111338](https://github.com/Huyen1974/agent-data-test/actions/runs/41025111338), job gate `123961272485` SUCCESS, HEAD `58a44c0…`, GH merge-test/executing workflow SHA `c22c9192d5f68588db89d6c2d00949b4b95da35a`, 151 PASS (33 cũ + 118 mới). Preflight `gate_matches_main=false`/`ci_change_kst_review=true` nên KST **phải review độc lập code của CI đã sửa**, không lấy CI tự kiểm làm chữ ký.
PR #357 OPEN/DRAFT HEAD `36c682914c9f412078113b6d85319f11356d1130`, queue 4-worker đã có trên VPS nhưng chưa nằm Git main; P476 đã review ghép nguồn với #358 trước RUN19 và để lại bản giải 2 dòng cho `workspace_tasks.py`.
**Đích duy nhất:** KST rà diff RUN19 + hiệu lực gate trên HEAD cụ thể + tác động lên hợp đồng cũ. Chốt `KST_SCOPED_F1F2_REVIEW_PASS` hoặc `KST_F1F2_NEEDS_FIX` kèm tối đa 3 lỗi cụ thể. **KST review PASS ≠ KST_ACCEPT@SHA cho merge hoặc G8_SYSTEM_PASS.**

**CẤM:** merge/rebase/push main/PR, đổi PR state, approve merge, KST_ACCEPT@SHA với ý nghĩa release, bật/rerun workflows, deploy, rsync VPS, Docker build/restart, sửa PR357/source/queue4/Hermes/Gemini/PG/Directus/config/Guard. `deploy-vps.yml` trong GH main còn mã on-push-main→rsync/build/recreate, KST P476 thấy `disabled_manually` nhưng có thể bật; giữ tuyệt đối **NO MERGE** cho đến GO Owner và release gate riêng. Không mở task mới.

## B. INPUT READY TABLE DROOT60
| Host-owned input | Evidence VERIFIED; chỉ recheck lúc RUN |
|---|---|
| Repo/refs | GH PR358 OPEN/DRAFT 58a44c0, PR357 OPEN/DRAFT 36c6829, main b4c9ea1; GitHub connected reads + prior Claude Code CLI KST P476 succeeded. Refresh head tại S0, drift thì diff và KQ hẹp, không review SHA mù |
| KQ/test | RUN19 P478+commit `7c768d2b705d67dbe4c56aaf1b1879f42ec784e9`; evidence 11 file; GH commit `58a44c0` thay đúng 3 đường; test RED/GREEN+negative missing/failing file; gate mới thực thi 151 |
| CI/review | GitHub job `123961272485` Unit tests SUCCESS, log có TESTS chứa HJW file + `151 passed in 8.94s`, note `CI_CHANGE_KST_REVIEW`. Reviewer độc lập so workflow base/executing diff, không tin duy nhất đèn xanh |
| Source/limit | Target P458 vẫn bốn facts AI/môi trường/task/lệnh với provenance & quyền A2 bất biến. RUN20 read-only Git/CI + Mac test nhẹ. Docker Mac/VPS build KHÔNG bắt buộc, không cần VPS-GHI |
| Rollback | 0 production mutation, cleanup worktree local; không KST merge/CI rewrite. Nếu không đọc được GH Mac, báo error với bằng chứng, không dựng tool/quyền mới |
0 HOST_UNVERIFIED trong phạm vi read-only; Git credentials/git refs/pytest outcome ở giờ thực thi là EXECUTOR_FRESHNESS.

## C. S0–S2, một lượt, checkpoint hợp lý ≤15 phút
**S0 (one read gate):** root/HJW READY SHA và STOP/STARTED, 3 GH refs, 3 changed paths của commit 58a44c0; ghi STARTED theo DROOT31. Đọc ghm-pr-gate.yml ở main và ở đúng head PR #358 (không dựa source deploy).
**S1 (KST độc lập):**
1. Xem F1 `target_task` đúng reserved `done-tasks`: path active/archived, directory vs file, đóng/mở lại, multiple from/to/operations, cross-task, path rỗng/độc hại/Unicode/backslash, falsified declared task vs derived task; ca sai không tạo mutation. Chỉ xét delta F1, không làm lại toàn bộ 4-facts P476.
2. Kiểm test suite 118 thực sự test code, độc lập và có negative; không mock chính logic đang kiểm; RED→GREEN P478 đáng tin. Có thể chạy vài ca targeted Mac nếu deps có; thiếu Docker/FastAPI không phải blocker review static khi nguồn/test đủ.
3. So workflow trước/sau: **chỉ một mục tests/unit/test_hjw_four_facts.py bắt buộc** trong Unit tests, không `if test -f`, không `|| true`/continue-on-error; preflight, actor lane, secrets scan, policy, runner, timeouts, permissions, trigger và branch protection không bị thay. Đối chiếu log HEAD `58a44c0`, merge-test SHA `c22c919…`, 151 tests và `CI_CHANGE_KST_REVIEW`. Nếu có lỗ hổng khiến gate xanh mà test không chạy, đánh NEEDS_FIX, không tự sửa CI.
4. Đánh giá giao thoa F1 với PR357 và baseline live queue 4-worker: RUN19 không sửa `workspace_tasks.py`, PR357 vẫn draft. Test integration P476 trước đó và RUN19 overlay regressions còn tương ứng; chỉ nếu F1 làm thay đổi task ID ảnh hưởng queue/schema thì nêu chính xác; KHÔNG rebase PR trong RUN20.
5. Ghi riêng những **coverage gap trước G8_SYSTEM**, không sửa: `workspace_exec` NON_SOURCE/state queue, KB write tools, trusted auto-derive actor/environment, PR357 fresh-DB SQLite bootstrap race, Linux AD rebuild/rollback, C1/C2 AI thật. Không chấp nhận G8 full vì CI 151 xanh.
**S2 (KQ):** KST ghi `P480/KQ` + Bảng trong HJW qua Gateway; evidence ngắn `work/hermes-joint-workspace/evidence/run20-kst-f1f2-ci-20261030/` có gh HEAD/base, exact 3 paths, checklist verdict per F1/test/CI, test/log receipts, 0 mutation, 1–3 câu sửa nhỏ nếu NEEDS_FIX; không thay đổi PR hoặc PROMPT. Nếu PASS, đề xuất Host điều hành Codex tiếp phần coverage trên một RUN riêng, **chưa merge/production**. Dọn local refs/worktree, đóng sạch.

## STEP_WALK_V1
| Bước | Actor / trigger | Receipt phải có | Hỏng thì |
|---|---|---|---|
| S0 | Claude Code CLI, Owner sau READY | Fresh refs + STARTED | drift: diff hẹp/partial, không sửa PR |
| S1 | KST code review + Mac targeted check | F1 paths, test legitimacy, 1-line CI diff, run41025111338, gaps | bug → NEEDS_FIX có hunk và repro |
| S2 | KST KQ Gateway, no live | P480, Bảng, evidence, 0 merge/deploy | Host chọn tiếp RUN coverage, không mở vô hạn review |

**Không chờ Claude Chat vòng khác, không xin Owner thao tác VPS, không tự tạo workflow/runner/task hay đổi quyền.**
