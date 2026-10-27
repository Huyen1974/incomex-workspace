# PROMPT — GHM F1 KST REVIEW/MERGE + REAL WEB RELEASE (DRAFT)

RUN_ID: GHM-F1-KST-REVIEW-MERGE-WEB-20261027-05
STATUS: DRAFT · Claude P79 ACCEPT có sửa (merge đúng SHA một cách duy nhất; KST tự gỡ ngoại lệ thử ở PR676; F1_B = đưa production Web lên bản build từ GitHub main và giữ) · NOT_READY · NO_RUN. Claude Chat reviewer sửa một vòng, GPT Host ký READY theo last-touch rồi Owner chuyển cho **Claude Code CLI**, không phải Codex. P74 RUN F0 đã KQ P77, READY cũ không có hiệu lực.
EXECUTOR: Claude Code CLI KST dùng quyền Mac gh/SSH Owner hiện có; Codex chỉ developer PR, không tự merge/deploy. Repo code chỉ private agent-data-test và web-test, ghi trạng thái trong incomex-workspace/work/github-management.

## S0 — READ và DoD
Đọc AGENTS.md, COLLAB §0/P74–P79, ROADMAP §0.4, FAST-PR-LANE-REPORT, C1B-CLOSE-REPORT (P66: cách build/parity/deploy–lùi Web bằng script P61 — tra đường dẫn script trong code-ledger), PR350/#676 và 3 runs 40459074294/40459085757/40459402138. Pin PR HEAD/base/merge-test SHA mới nhất, kiểm draft/mergeable/reviews/CI + runtime. Không giữ VPS-GHI khi đọc/review.
F1 chia F1_A=KST review/merge hai PR + Web audit main đáng tin; F1_B=production Web chạy đúng bản build từ GitHub main (phát hành thật đầu tiên, giữ lại). F1_A + F1_B = chuỗi PR → KST merge → main → build → production; PR đổi mã ứng dụng đầu tiên để F2.

## S1 — Review Agent Data PR350
PR350 head hiện ce36577ff19026f7259e7092608b713498143afb; chỉ thêm tests/unit/test_kb_list_pagination.py; gate GREEN33. KST đọc diff/test xác minh đúng hợp đồng /kb/list, không nhầm AST/mock unit với DB integration. Khi đủ, ghi PR COMMENT KST_ACCEPT@exact-head-SHA + tests/DoD, chuyển draft→ready và merge bằng một cách duy nhất `gh pr merge <số> --merge --match-head-commit <SHA đã duyệt>` (giữ đúng SHA đã duyệt; không squash/rebase, không force) sau kiểm lại base/head; nếu chưa đạt ghi yêu cầu sửa. KHÔNG deploy Agent Data vì rollback old/Compose chưa đạt.

## S2 — Review Web PR676 và promote Health Check
PR676 head hiện 4556635ca22ada5bacba26b681ef638ec6f566ff; 3 file (sync-check.yml +2 scripts ghm), unit16 PASS, secret scan PASS, policy RED KST_REVIEW_REQUIRED chính vì workflow/secret reference. Ba file khớp blob audit candidate d3b1ec8 đã kiểm 13 CHECK (11 PASS/2 FAIL nghiệp vụ thật). KST đọc toàn diff, SHA/script, test helper, permissions, runner schedule/main-only.
**Trước merge (luật merge Owner mục tiêu #5: «thiếu ít thì sửa»):** KST tự gỡ ngoại lệ dispatch nhánh `c1b-audit-finalize-health` bằng 1 commit CHỈ XOÁ đúng điều kiện đó trên nhánh PR (ghi KST_FIX@SHA; không đổi dòng nào khác), giữ schedule 6h + workflow_dispatch CHỈ main; gate chạy lại trên head mới, đọc lại SHA/CI/diff. Không chờ Codex. Không tự bỏ guard, không cấp secret cho PR. Nếu có RED không thuộc đúng ngoại lệ workflow/secret-reference thì không merge.
Vì cả PR cùng GitHub Owner Huyen1974, Claude Code CLI không gọi APPROVE tự thân; review độc lập cấp agent và COMMENT KST_ACCEPT_WORKFLOW@SHA (manual policy exception có lý do/unit/scan/candidate), rồi ready→merge exact-head non-force. Nếu GitHub hiện có branch rule ngăn, không force/bypass trái luật; ghi blocker.
Sau merge gọi workflow_dispatch từ main chạy trên Web VPS runner, tối đa 2 lượt (lượt 2 chỉ khi lượt 1 lỗi hạ tầng, không phải FAIL nghiệp vụ); xác nhận 13 CHECK có kết quả đáng tin, đúng giờ/lịch main, 2 FAIL nghiệp vụ nếu còn thì **job/cảnh báo tiếp tục RED**, không đổi ngưỡng/autoheal hoặc disable chính workflow. Khi audit main đạt ⇒ AUDIT_EXECUTION_VERIFIED=PASS_MAIN/3 audit VPS; BUSINESS_HEALTH_FAIL ghi nợ ratio, 5 folders, 2 orphans. C1B AD rollback vẫn chưa PASS.

## S3 — F1_B: đưa production Web lên đúng bản build từ GitHub main (phát hành thật đầu tiên)
**Gốc (P79):** diễn tập P66 đã lùi về bản cũ ⇒ production Web hôm nay vẫn chạy bản dựng ngoài GitHub (lab + CWEB vá), chưa phải bản build từ main. Phát hành thật đầu tiên = đưa production lên bản build từ main và GIỮ — không phải «restart rỗng»: bytes phục vụ đổi sang dòng build GitHub (parity 166/166 đã chứng minh ở P66). Chưa làm bước này thì PR app đầu tiên sẽ gộp 2 thay đổi một lúc (đổi dòng build + đổi mã), lỗi khó khoanh.
1. Sau S1–S2, lấy Web main HEAD mới nhất (CI xanh đúng SHA); build Node 24.21.0 / Nuxt 4.5.2 bằng lockfile và cách P66.
2. PARITY với live như P66: 132 route VPSUP + 32 route CWEB + 2 tài nguyên + 34 contract tĩnh; khác ngoài danh sách đã biết ⇒ không deploy.
3. PRE (manifest/symlink/known-good = bản đang chạy, Guard, cờ VPS-GHI CAS, lease deploy mới đúng RUN này, Điều 30/31) → deploy qua **script P61/P66** → kiểm contract → **GIỮ** nếu đạt; lùi về known-good chỉ khi hỏng (≤1 restart deploy + ≤1 restart lùi; nginx reload theo công cụ P61).
4. Đạt ⇒ ghi `WEB_RUNTIME=MAIN@<SHA>`; bản cũ giữ nguyên làm known-good.
Không restart AD/DB/nginx config/VPS, không auto-CD. Thiếu bản lùi/test thì DỪNG riêng release, các merge PR đã đạt giữ nguyên. PR đổi mã ứng dụng đầu tiên KHÔNG làm trong RUN này: Host/Owner chọn việc thật cho Codex ở F2 (P79 gợi ứng viên: giảm dung lượng trang tri thức, việc hoãn của vps-clean phần D — cần Owner xác nhận còn hiệu lực).

## S4 — KQ độc lập
Báo F1_A review/merge, AUDIT_MAIN, BUSINESS_HEALTH, F1_B WEB_RUNTIME; SHA PR/main/CI, chữ ký review, release (+ lùi nếu có), Guard POST/receipt/VPS-GHI. F1_B PASS khi production Web chạy bản build từ main SHA đã ghi, contract đạt, known-good giữ; hỏng ⇒ lùi + FAIL_WITH_ROLLBACK (không bịa). C1B AD rollback vẫn chưa đạt. Ghi KQ+board/ROADMAP/README một lượt và trả cờ/lease nếu có, không tự mua Pro/C2 hoặc mở F2/C4. Không tạo work task mới.
