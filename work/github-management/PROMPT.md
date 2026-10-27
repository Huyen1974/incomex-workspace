# PROMPT — G1 GITHUB CODE CHECKS MUST BE GREEN (DRAFT)

RUN_ID: GHM-GH-GREEN-GATE-20261027-06
STATUS: P83_DRAFT_FOR_CLAUDE_P84 · NOT_READY/NO_RUN. Claude phản biện một vòng, Host ký READY SHA rồi Owner giao Codex developer; Chief Claude Code CLI review/merge theo policy, không tự C2/Pro/F2.
Repo private: Huyen1974/agent-data-test và Huyen1974/web-test; task sổ chung work/github-management, không task/repo mới.

## Mục tiêu
CODE_PR_GATE và MAIN_SOURCE_CHECK GREEN thật, đúng latest SHA trên hai repo, required tests âm RED ngăn merge; không manual merge khi required code check RED như Web PR676 trước chỉ đạo mới. Health business RED giữ RED, không giả toàn GitHub xanh. Nếu cần Pro/identity để hard-enforce, ghi OWNER_GO_REQUIRED, không auto purchase.

## S0 GitHub audit đo lại
Đọc AGENTS.md → COLLAB §0/P80-P83 → ROADMAP §0.4a → F1 report P82, main/PR/workflows/checks/GH Actions API thật. P83 baseline Web100 runs 48fail/15success/37cancel (Health41/41 FAIL, PR gate3/3 FAIL, ops-smoke37 cancelled lịch sử); AD20fail/80success. GH branch protection AD false; Web true với required checks legacy không phải gate mới. Đọc log AD40478406281, Web40478954350 BASE_MOVED postmerge và Web40478663324 policy RED.

## S1 Sửa CODE gate native, không tạo thêm hệ thống
Codex branch/PR GitHub; KST giữ quyền review/merge. Required check trên SHA PR/latest main là GREEN chỉ khi unit/secret scan/security phù hợp; RED thật phải chặn. Với event đến muộn sau PR MERGED, xác thực GH PR merged SHA rồi kết luận stale/neutral không giả TEST_PASS; PR OPEN base đổi vẫn FAIL đòi test mới. Main check xanh tự chạy đúng một lượt nhẹ khi main đổi hoặc trusted dispatch, không duplicate PR CI/không kéo nặng VPS. Existing runner1CPU/1.5GiB + flock, không secrets/docker.sock/root cho PR.
Khi đổi workflow/secret cần Chief review có GitHub-native mechanism và proof SHA; không cho CODE required check GREEN nếu Chief chưa duyệt. Nếu old gate cố ý RED khi PR sửa chính workflow, phải đề xuất bootstrap giới hạn xin Owner GO riêng, KHÔNG bypass âm thầm. Không sửa RED thành GREEN bằng continue-on-error/exit0 hoặc bỏ security scan. C2 Pro/Chief identity/ruleset thực cần thử âm; chung account Owner không tự APPROVE độc lập.

## S2 Giữ Health business RED và lịch sử
Web Health main 11 PASS/2 FAIL nghiệp vụ: CHECK2 ratio2,02 sync warning, CHECK7 5 thư mục; 2 orphan. Chỉ kiểm rule + source read-only để giao đúng chủ, không auto dọn data/đổi threshold/disable audit. 37 ops cancelled và 15 lint fail cũ không xóa/rerun lấy màu; phân biệt latest active per workflow và GH main SHA.

## S3 Giao KQ
Thử positive PR source trên mỗi repo có gate GREEN, negative unit/security RED không merge; postmerge stale neutral và PR OPEN moved RED; main check SHA thật GREEN; Chief review kiểm. Báo GH_CODE_GATE_PASS và GH_HARDLOCK_ENFORCED riêng, Web Health BUSINESS_HEALTH_FAIL giữ đỏ đến khi chữa đúng; F1 runtime P82 giữ nguyên. Trường hợp cổng cần Pro/Owner GO hay bootstrap, dừng đúng nhánh và hoàn thành phần độc lập, không đợi trong RUN. Ghi KQ + COLLAB/ROADMAP/README/Guard nếu có host mutation, trả cờ, không tự F2/C4.
NEXT_TRIGGER=HOST_REVIEW_GH_CODE_GREEN_RESULT.