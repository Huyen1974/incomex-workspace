# PROMPT — C2 KHOÁ MAIN HAI REPO PRIVATE BẰNG CỔNG `gate` (Claude P91 đã sửa · chờ Host READY)

RUN_ID: GHM-C2-PRIVATE-MAIN-PROTECT-20261028-07
STATUS: P91_CLAUDE_ACCEPT_WITH_EDITS · NOT_READY/NO_RUN đến khi GPT Host ký READY@last-touch SHA của tệp này và Owner RUN từng phần.
Hai phần, cùng RUN_ID: **Phần A — Codex** (không cần Pro, làm ngay). **Phần B — Claude Code CLI (KST)**, chỉ sau khi Owner đã nâng GitHub Pro và giao B. Không cần Host ký lại giữa A và B nếu A đạt DoD A. Không F2/C4/deploy/sửa dữ liệu; không tạo tài khoản/token/bot/deploy key; không đổi visibility, ngân sách Actions, secret.
Repo private: `Huyen1974/agent-data-test`, `Huyen1974/web-test`. Sổ chung: `work/github-management` (repo public — không ghi tên/giá trị secret).

## Mục tiêu (đo bằng gh API, không dựa báo cáo)
1. `GH_BRANCH_PROTECTION_ENFORCED`: trên `main` hai repo, không ai — kể cả Owner/admin — push thẳng, force-push, xoá nhánh; chỉ merge qua PR khi check `gate` của GitHub Actions = success trên head mới nhất và nhánh đã cập nhật theo main.
2. `GH_NONPILOT_BLOCKED`: PR ngoài làn pilot ra **RED**, không còn «skipped» (GitHub tính job bỏ qua do điều kiện = Success với required check — docs «Troubleshooting required status checks»).
3. `KST_ONLY_MERGE_ENFORCED=NO` báo trung thực: Codex và Claude Code CLI dùng chung danh tính `Huyen1974`; repo cá nhân không có «chỉ người X được push» theo danh tính. Đường duy nhất để thành YES ghi ở COLLAB P91 §4 — Owner quyết ở F2, không làm trong C2.

## Sự thật đã đo (Claude P91, gh API 28/10 15:10 +07) — S0 đo lại, lệch nhỏ thì ghi, không dừng
- main AD `a636ffe57d23f3716cb016082dba1867882d5454`, Web `4f8405a900170106fdb2b2a60ad10c1785ad6f91`, `gate` push main success (40623332810, 40623377993). Cả hai `protected:false`.
- Web còn lưu bảo vệ nhánh kiểu cũ đòi 4 check của workflow đã tắt (Pass Gate, Quality Gate, check-critical-files, Contract Schema Validation). **Khi Pro có hiệu lực, cấu hình này bắt đầu chặn ⇒ mọi merge Web kẹt** cho tới khi B1 xoá.
- `gate` hiện bỏ qua (skipped) PR ngoài làn bằng `if` mức job ⇒ lỗ hổng khi bật required check. PR mở cũ: AD 11 Dependabot (#325–#334, #349), Web #117/#327/#669 — không đụng; Dependabot đã tắt tạo PR mới (`updates: []`).

## Phần A — Codex (mỗi repo 3 PR nhỏ; không merge)
**S0** Đọc AGENTS.md → COLLAB P89–P91 → ROADMAP §0.4b → PROMPT. Đo lại main/runner/workflow. Không VPS-GHI.
**A1 · PR-1 `dev/codex-<ad|web>/c2-fail-closed`** — sửa `.github/workflows/ghm-pr-gate.yml` + `scripts/ghm/gate_policy.py` + test:
- `if` mức job chỉ còn bỏ qua sự kiện `closed`. Mọi PR khác: job chạy; **bước đầu tiên** kiểm làn (tác giả/actor `Huyen1974`, nhánh `dev/codex*` hoặc `dev/claude-code/*`, không fork) **trước mọi fetch/checkout mã PR, trước setup-node**; sai ⇒ RED `OUT_OF_PILOT`, không chạy mã PR.
- Giữ nguyên byte các bước quét secret, unit, actionlint và luật G1; push/dispatch main không đổi. Thêm ca hồi quy cho `OUT_OF_PILOT`.
**A2 · PR-2 `dev/codex-<ad|web>/c2-merge-rule`** — từ main hiện tại, độc lập PR-1: thêm vào `AGENTS.md` của repo mục «Luật merge» ≤5 dòng, giống nhau hai repo: chỉ KST merge; điều kiện `gate` success đúng head + nhánh mới nhất; lệnh `gh pr merge <số> --merge --match-head-commit <SHA>`; agent phát triển không merge, không push main. (Biển chỉ đường cho agent F2; dùng luôn để thử «nhánh lạc hậu» ở B.)
**A3 · PR-3 `c2-neg/out-of-lane`** — nhánh ngoài làn, tách từ nhánh PR-1, thêm 1 dòng chú thích vô hại; mở PR vào main ⇒ phải RED `OUT_OF_PILOT`, log cho thấy không có bước fetch/checkout mã PR. Để OPEN cho B, không merge.
**DoD A:** PR-1, PR-2 GREEN đúng head; PR-3 RED đúng lý do; bảng run ID từ gh API; 0 merge. Ghi KQ_A vào COLLAB + bảng. NEXT_TRIGGER=OWNER_NANG_PRO_VA_GIAO_KST_PHAN_B.

## Phần B — Claude Code CLI (KST), sau DoD A và Owner đã nâng Pro
**B0** `gh api user --jq .plan.name` phải là `pro`; khác ⇒ KQ DỪNG `NEEDS_PRO`, không chờ. Đọc PROMPT/KQ_A; PROMPT last-touch = READY.
**B1 Web trước:** đọc rồi lưu JSON bảo vệ kiểu cũ (bằng chứng private), xoá nó (`DELETE /repos/Huyen1974/web-test/branches/main/protection`). Không giữ song song hai cơ chế.
**B2 Mỗi repo một ruleset `main-code-gate`**, đích `main`, enforcement `active`, **bypass rỗng**, đúng 4 luật: `deletion` · `non_fast_forward` · `pull_request` (0 approval — một danh tính không tự duyệt được) · `required_status_checks` strict=true, 1 check `gate` ghim nguồn GitHub Actions (integration_id 15368). Đọc lại `GET /repos/<repo>/rules/branches/main`: đúng 4 luật, bypass rỗng; lưu JSON.
**B3 Thử thật, mỗi repo, đúng thứ tự:**
1. PR-3 (RED, nhánh vẫn mới nhất nên chỉ vì đỏ) ⇒ `gh pr merge` bằng chính tài khoản admin phải bị từ chối (chứng minh không bypass) ⇒ đóng PR.
2. PR-1 (GREEN, nhánh mới nhất) ⇒ KST_ACCEPT@head rồi merge ⇒ được phép; `gate` push main success.
3. PR-2 lúc này lạc hậu ⇒ `gh pr merge` phải bị từ chối ⇒ `gh pr update-branch` ⇒ chờ `gate` GREEN trên head mới ⇒ KST_ACCEPT@head mới rồi merge được.
4. Push thẳng: từ bản clone KST, `git commit --allow-empty` rồi push lên main ⇒ phải bị từ chối. Lỡ lọt ⇒ DỪNG, mở PR revert ngay, báo FAIL.
5. Force-push và xoá nhánh: chỉ chứng minh bằng đọc lại luật ở B2, **không thử thật** (thử hỏng là mất lịch sử main).
**Bẻ khoá khẩn cấp (chỉ khi gate hỏng làm kẹt mọi merge):** đặt ruleset `disabled`, ghi lý do vào COLLAB, sửa xong bật lại cùng lượt. Không xoá ruleset, không thêm bypass.
**B4 KQ:** `GH_BRANCH_PROTECTION_ENFORCED` · `GH_NONPILOT_BLOCKED` · `KST_ONLY_MERGE_ENFORCED=NO` · `GH_CODE_GATE=PASS` giữ · ngân sách Actions sau Pro: đọc bằng API nếu được, không được thì ghi `BUDGET_CHECK=OWNER_UI` · bảng run ID/từ chối (thông báo lỗi nguyên văn) · Bảng/ROADMAP/README. 0 deploy, 0 VPS-GHI.
NEXT_TRIGGER=HOST_ACCEPT_C2 — Host và Claude tự đối chiếu bằng gh API trước khi ACCEPT.
