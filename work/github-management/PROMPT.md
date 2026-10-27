# PROMPT — GHM F1 KST REVIEW/MERGE + REAL WEB RELEASE (DRAFT)

RUN_ID: GHM-F1-KST-REVIEW-MERGE-WEB-20261027-05
STATUS: DRAFT_P78_FOR_CLAUDE_P79 · NOT_READY · NO_RUN. Claude Chat reviewer sửa một vòng, GPT Host ký READY theo last-touch rồi Owner chuyển cho **Claude Code CLI**, không phải Codex. P74 RUN F0 đã KQ P77, READY cũ không có hiệu lực.
EXECUTOR: Claude Code CLI KST dùng quyền Mac gh/SSH Owner hiện có; Codex chỉ developer PR, không tự merge/deploy. Repo code chỉ private agent-data-test và web-test, ghi trạng thái trong incomex-workspace/work/github-management.

## S0 — READ và DoD
Đọc AGENTS.md, COLLAB §0/P74–P78, ROADMAP §0.4, FAST-PR-LANE-REPORT, PR350/#676 và 3 runs 40459074294/40459085757/40459402138. Pin PR HEAD/base/merge-test SHA mới nhất, kiểm draft/mergeable/reviews/CI + runtime. Không giữ VPS-GHI khi đọc/review.
F1 chia F1_A=KST review/merge hai PR + Web audit main đáng tin; F1_B=PR ứng dụng Nuxt4 thật được KST merge, build/deploy/rollback trên VPS. Chỉ F1_B mới chứng minh full GH code→production release.

## S1 — Review Agent Data PR350
PR350 head hiện ce36577ff19026f7259e7092608b713498143afb; chỉ thêm tests/unit/test_kb_list_pagination.py; gate GREEN33. KST đọc diff/test xác minh đúng hợp đồng /kb/list, không nhầm AST/mock unit với DB integration. Khi đủ, ghi PR COMMENT KST_ACCEPT@exact-head-SHA + tests/DoD, chuyển draft→ready và merge PR non-force sau kiểm lại base/head; nếu chưa đạt ghi yêu cầu sửa. KHÔNG deploy Agent Data vì rollback old/Compose chưa đạt.

## S2 — Review Web PR676 và promote Health Check
PR676 head hiện 4556635ca22ada5bacba26b681ef638ec6f566ff; 3 file (sync-check.yml +2 scripts ghm), unit16 PASS, secret scan PASS, policy RED KST_REVIEW_REQUIRED chính vì workflow/secret reference. Ba file khớp blob audit candidate d3b1ec8 đã kiểm 13 CHECK (11 PASS/2 FAIL nghiệp vụ thật). KST đọc toàn diff, SHA/script, test helper, permissions, runner schedule/main-only.
**Trước merge:** YAML PR còn điều kiện cho dispatch trên branch c1b-audit-finalize-health; yêu cầu Codex tác giả gỡ ngoại lệ chỉ dùng để thử, giữ schedule 6h + workflow_dispatch CHỈ main; PR head đổi thì kiểm lại SHA/CI và diff. Không tự bỏ guard, không cấp secret cho PR. Nếu có RED không thuộc đúng ngoại lệ workflow/secret-reference thì không merge.
Vì cả PR cùng GitHub Owner Huyen1974, Claude Code CLI không gọi APPROVE tự thân; review độc lập cấp agent và COMMENT KST_ACCEPT_WORKFLOW@SHA (manual policy exception có lý do/unit/scan/candidate), rồi ready→merge exact-head non-force. Nếu GitHub hiện có branch rule ngăn, không force/bypass trái luật; ghi blocker.
Sau merge gọi đúng 1 workflow_dispatch từ main chạy trên Web VPS runner; xác nhận 13 CHECK có kết quả đáng tin, đúng giờ/lịch main, 2 FAIL nghiệp vụ nếu còn thì **job/cảnh báo tiếp tục RED**, không đổi ngưỡng/autoheal hoặc disable chính workflow. Khi audit main đạt ⇒ AUDIT_EXECUTION_VERIFIED=PASS_MAIN/3 audit VPS; BUSINESS_HEALTH_FAIL ghi nợ ratio, 5 folders, 2 orphans. C1B AD rollback vẫn chưa PASS.

## S3 — Release Web ứng dụng thật, không nghiệm thu giả
KST rà backlog đã được Owner phê duyệt, tìm 1 PR thay mã Nuxt4 ứng dụng thật dưới web/ có DoD nhỏ và test rõ; không chọn PR cũ từ nền Nuxt3/Directus cũ chỉ để có PR. Codex là developer chuẩn bị PR nếu cần Owner giao worker riêng; KST không viết mã rồi tự duyệt. Nếu chưa có PR app hợp lệ, ghi F1_B=PENDING_CODE_PR và trả quyền, không chiếm VPS-GHI hoặc restart Web rỗng.
Khi có PR app trên main mới nhất, đã KST review/merge, CI chính xác SHA: build Node24.21.0 Nuxt4 bằng script/lockfile P66, kiểm 132 VPSUP +32 CWEB +2 asset và contract diff; PRE manifest/symlink/known-good/runtime Guard/cờ VPS-GHI/Đ30–31 rồi deploy và rollback qua **script P61/P66 trên VPS**. Không restart AD/DB/nginx config/VPS, không auto-CD. Thiếu bản lùi/test thì DỪNG riêng release, các merge PR đã đạt giữ nguyên.

## S4 — KQ độc lập
Báo F1_A review/merge, AUDIT_MAIN, BUSINESS_HEALTH, F1_B WEB_APP_RELEASE; SHA PR/main/CI, Chủ ký review, release + rollback, Guard POST/receipt/VPS-GHI. Chỉ F1_B PASS khi app code thật được deploy/rollback; nếu không có PR app, F1_A có thể DONE và F1_B PENDING_CODE_PR (không bịa). C1B AD rollback vẫn chưa đạt. Ghi KQ+board/ROADMAP/README một lượt và trả cờ/lease nếu có, không tự mua Pro/C2 hoặc mở F2/C4. Không tạo work task mới.
