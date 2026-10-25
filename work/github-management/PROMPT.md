# PROMPT — GHM R2-A · THIẾT LẬP QUY ĐỊNH VÀ CỔNG NHÁNH GH (2 REPO)
RUN_ID: GHM-R2-ACCESS-20261025-01
STATUS: DRAFT_NOT_READY — KHÔNG RUN. Claude Reviewer phải ACCEPT last-touch full SHA sau khi rà. GPT Host READY đúng SHA; Owner giao Codex. Chưa có RUN cho mốc này.

Executor_Surface: Codex CLI/Desktop (Mac) · Write_Path: GitHub API/gh CLI quyền quản lý rulesets/branch, Incomex workspace_* root=workspace ghi STARTED/KQ + Bảng. KHÔNG shell/SSH ghi VPS, không sinh/thay Chief private key, không đổi production. Chi tiết actor/token/đường ghi chỉ lưu trong vùng hạn chế quyền P17, repo public chỉ tóm tắt.

ENTRY: đọc AGENTS.md root → root COLLAB cờ/luật → work/github-management/COLLAB.md §0/Bảng/P17/P18 → ROADMAP V0.3 → KE-HOACH R2 → PROMPT này. DROOT30/31 freshness/STARTED/KQ trước mutation. R1 đã ACCEPTED_WITH_EXCEPTION nhưng KQ gốc DỪNG không tái chạy.

## S0 — PRECHECK HARD-GATE (read-only, ≤15 phút)
- Xác minh Account GitHub Pro đã được Owner nâng cấp, hai repo `Huyen1974/agent-data-test` và `Huyen1974/web-test` đang PRIVATE, default branch `main`, quyền repo rulesets có thể dùng; nếu Pro chưa active ⇒ `KQ DỪNG` và `NEXT_TRIGGER=OWNER_PRO_ACTIVE`. **Không tự mua gói hoặc thêm/thay phương thức thanh toán.**
- Đọc lại bằng chứng mới: Actions account budget Product=Actions toàn Account, amount=$0, **Stop usage=true**, Actions workflow ba nhóm nghiệp vụ vẫn active, 15 workflow BỎ vẫn disabled. GitHub-managed Dependabot dynamic chỉ là ngoại lệ nếu đối chiếu được đúng loại + runner standard (không larger). Nếu budget hard-stop không còn ⇒ DỪNG trước cấp quyền/thiết lập chính sách, báo Owner.
- Xác minh không có RUN khác đang sửa **GitHub rulesets/permissions/branch chính** của 2 repo; không cần VPS-GHI cho đọc và quản trị GitHub nhưng phải tránh đụng cùng scope. Không dùng tài khoản/credential Owner admin để giả làm worker trong phép thử quyền.

## S1 — LUẬT NGẮN/PHẠM VI (≤20 phút)
- Tận dụng luật AGENTS gốc, không nhân một hệ thống mới. Dự thảo `AGENTS.md` ≤1 trang + Issue/PR mẫu 6 ô (TASK_ID, mục tiêu/DoD+test, allowed/forbidden paths, dependency/base SHA, worker+Chief, quota/stop), quy tắc `dev/<seat>/<task-id>`, review 4 kết luận NHẬN/SỬA/TRẢ LẠI/BỎ.
- Soạn tài liệu ở đúng nhánh chuẩn bị riêng của mỗi repo, KHÔNG push vào `main` cũ; nếu ruleset cản tạo nhánh thì dừng với bằng chứng, không bỏ ruleset. Không đẩy danh sách secret/keys/địa chỉ nhạy cảm vào code.

## S2 — KHÓA `main` Ở CẤP GITHUB (≤25 phút)
- Dùng rulesets của GitHub Pro trên **hai repo private** chỉ áp cho `~DEFAULT_BRANCH` / refs/heads/main; chặn update/deletion/non-fast-forward của dev theo phương án đã có trên `incomex-workspace`. KHÔNG sao y ruleset `~ALL` (sẽ chặn cả các nhánh dev). Bypass chỉ cho loại Chief DeployKey theo mô hình Owner duyệt, tránh actor admin/dev; không tạo bất kỳ *write deploy key* mới nào ở bước Codex này.
- Đọc lại ruleset `enforcement=active`, target branch chỉ `main`; đọc danh sách runner/actor có quyền bypass theo loại/số đếm, không lộ ID chi tiết lên repo public. Xác minh worker có thể tạo branch/PR riêng và không có Administration trên token dev. Không thực hiện phép thử xóa/force-push **main thật** nếu protection chưa chắc chắn; nếu chưa có credential dev độc lập thì `HARDLOCK_UNTESTED` thay vì báo PASS.
- KST/Claude Code CLI **giữ riêng** bước tạo và bảo vệ private key (theo Đ30/31, một RUN khác và cờ VPS-GHI nếu ghi VPS). Chỉ Chief được chứng minh bypass/ghi `main` tại R2-B/R3; Codex không cầm/đọc/gửi private key và không tự push main. Không tự giải quyết thiếu public key bằng cách cho admin bypass.

## S3 — ĐO CỔNG & BÀN GIAO (≤15 phút)
- Báo từng repo: nhánh dev mở được (kiểm an toàn), ruleset active, worker không có quyền ghi main/admin theo nguồn GitHub; ghi rõ thử âm nào PASS/UNKNOWN, đặc biệt `Chief push main` còn `PENDING_CHIEF_KEY_TEST`. Xác minh Actions vẫn ON ba nhóm audit và budget $0+Stop còn hiệu lực sau nâng Pro.
- Ghi biên nhận/URL nhánh cấu hình/PR draft + trạng thái từng cổng vào P tiếp trong COLLAB, chỉ số đếm công khai; bằng chứng actors/keys chỉ trong root-only workspace hiện hữu, không đăng nhập root VPS để sửa. Nếu thiếu private KST key là điều kiện chính để chốt R2, KQ `DỪNG` với `NEXT_TRIGGER=KST_R2B_KEY_TEST` và nêu phần Codex đã làm đạt, **không cố làm hộ Chief**.
- Không tự triển khai R3; kế tiếp Host/Claude xác nhận cổng, Owner giao mốc Key/Chief riêng theo roadmap. Không đổi `main`/deploy/cron/VPS/secret.

STEP_WALK_V1:
| Step | Ai/trigger | Budget tham chiếu | Evidence | Fail/owner | Kế |
|---|---|---|---|---|---|
| S0 | Codex / Owner RUN | ≤15 phút | Pro/budget/scopes/identities | DỪNG nếu plan chưa đúng, Host/Owner | S1 |
| S1 | Codex / S0 PASS | ≤20 phút | nhánh luật/PR templates | DỪNG nếu repo không cho phép nhánh, Host | S2 |
| S2 | Codex / S1 PASS | ≤25 phút | ruleset active chỉ main, quyền least-privilege | HARDLOCK_UNTESTED→giao Chief, Host | S3 |
| S3 | Codex / S2 đạt hoặc bị chặn | ≤15 phút | KQ/nhánh/ứng viên/test logs | Host nghiệm thu, Owner quyết R2-B | END |

CẤM: mua GitHub Pro, thay thẻ thanh toán/budget, gh push/merge/delete/reset/force vào main, cấp Claude Chief key cho Codex, thay token/secret, gọi root SSH/VPS ghi, cài Actions runner, đổi workflow YAML hoặc runtime. Gặp blocker thì KQ DỪNG + NEXT_TRIGGER, không giữ phiên đợi Owner.
