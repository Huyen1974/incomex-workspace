# PROMPT — GHM-R0R1 · ĐO HIỆN TRẠNG + TẮT GITHUB ACTIONS (CHỈ 2 REPO)
RUN_ID: GHM-R0R1-20261024-01
STATUS: DRAFT_NOT_READY — KHÔNG TỰ RUN. Chỉ bắt đầu khi Claude Reviewer ACCEPT đúng full last-touch SHA PROMPT, GPT Host READY@cùng SHA trong COLLAB, Owner giao RUN trực tiếp cho Codex. Hiện mới duyệt kỹ thuật roadmap, chưa cấp RUN.

Executor_Surface: Codex CLI/Desktop; Write_Path: Incomex workspace_* root=workspace cho hồ sơ STARTED/KQ; GitHub Settings/API chỉ để Disable Actions và Dependabot auto-PR sau S1 gate. SSH/MCP VPS read-only chỉ quan sát, không mutation VPS.

ENTRY: root AGENTS.md → root COLLAB phần cờ VPS-GHI → work/github-management/COLLAB.md §0/Bảng/P5/P6 → README → ROADMAP V0.3 → KE-HOACH V0.2 → PROMPT này. Xác minh A6 & DROOT30/31 trước bất kỳ thao tác ghi. PROMPT cũ P1A đã superseded. Không làm R2/R3.

## S0 — KIỂM QUYỀN & TRẠNG THÁI (READ-ONLY)
- Kiểm đúng hai repo Huyen1974/agent-data-test và Huyen1974/web-test, private, actions status hiện thời, run gần nhất, required checks, webhook, dependabot, workflow theo lịch và triggers.
- Kiểm cờ VPS-GHI/Claude Code RUN và khu đang dùng. Codex được đọc độc lập, không dùng root production shell để sửa, không git fetch/reset/pull vào working tree Claude đang làm. Nếu lấy mẫu khi worktree đang chuyển đổi, ghi snapshot bất định; không tự kết luận sạch.

## S1 — R0: PHẢI CÓ KQ READ-ONLY TRƯỚC KHI TẮT
1. Kiểm từ VPS root thực tế của mã Agent Data / Web (dự kiến docker/agent-data-repo, docker/nuxt-repo): git branch, HEAD, status tracked/untracked, upstream/remotes đã che, nhánh backup vps-daily, GitHub refs. Kiểm mã thực đang chạy theo image/build labels, hashes/evidence: **HEAD không tự coi là image đang chạy**. Mã ui-preview không phải nguồn web-test.
2. Liệt kê từng GitHub Actions workflow, lịch, run, chức năng thật và phụ thuộc production; phân loại MIGRATE (đã có đường Guard/Kuma/backup vận hành) hay BỎ. Chỉ dẫn nguồn bằng chứng, đừng giữ Action «chạy vì có sẵn». Kiểm cron/reverse backup VPS→GH có thể gây merge/pull nhầm mà không đụng đến job đó.
3. Lập ma trận định danh/quyền có thể push/main/admin của 2 repo bằng tên actor + permission (KHÔNG lấy hoặc in token, SSH private key); Dependabot hiện có. R6 đọc thử đường gọi Dot→Codex, Codex cloud/Claude cloud; không có API/receipt thật ghi UNKNOWN (không chặn R1).
4. **HARD STOP S1→S2:** nếu một workflow hiện làm việc sản xuất/canh/backup mà chưa có đường thay đang hoạt động, hoặc Codex không đủ quyền chỉnh GH, hoặc có Claude Code RUN hiện hành đang phụ thuộc Actions, thì ghi DỪNG ở mốc này và KHÔNG tắt. Không chạy gì trên VPS để «tạo đường thay» trong RUN này.

## S2 — R1: CHỈ THAO TÁC GITHUB (SAU S1 PASS)
1. Disable GitHub Actions ở cấp hai repo (không xóa YAML; không bật lại secret, không tạo runner, không re-enable deploy). Tắt Dependabot tự mở PR nếu quyền GitHub cho phép theo đúng phạm vi đã duyệt; cảnh báo nếu thao tác này khác cảnh báo bảo mật readonly.
2. Kiểm run đang thực thi: chỉ hủy run khi R0 chứng minh không phục vụ job production/giám sát thiết yếu; không giả định tắt Actions là tự hủy run cũ. Không sửa branch/code/webhook trên GitHub.
3. POST bằng GitHub API/settings: Actions disabled tại cả 2 repo; không có run mới sau mốc disable. Không cần push code thử ngay ở R1; push/PR smoke để R4 kiểm (tránh thêm commit cũ). Billing hiện hành có thể có phút trước lúc disable; KHÔNG báo tổng lịch sử 0. Chi phí Pro/budget chỉ là bước Owner sau KQ R1, không tự tạo payment.

## S3 — KQ & HANDOFF
- Ghi KQ@GHM-R0R1-20261024-01 XONG|DỪNG trong COLLAB, cập nhật Bảng cùng commit, nhả các tài nguyên; evidence ngắn: GH Actions status từng repo, mốc last run, danh sách job cần thay, HEAD Agent Data & đúng Web, code running vs HEAD, permission matrix, R6 khả thi có/không và các blocker.
- Không tuyên bố R2/R3/R4 xong. Không tự phát RUN tiếp. Chỉ trình Owner mua Pro sau khi Action OFF thật, kiểm billing: ngân sách $0 + Stop usage là dự phòng không áp hồi tố cho usage trước đó.

STEP_WALK_V1:
| Bước | Ai/trigger | Deadline dự kiến | Evidence | Fail & owner | Kế |
|---|---|---|---|---|---|
| S0 | Codex/Owner RUN hợp lệ | ≤15 phút | rights + VPS-GHI + 2 repo | DỪNG ngay nếu mất quyền, Host/Owner | S1 |
| S1 | Codex/S0 PASS | ≤45 phút | Git VPS/code chạy, 2 repo workflows, identity, R6 path | thiếu critical backup⇒DỪNG, Host | S2 |
| S2 | Codex/S1 GATE PASS | ≤20 phút | Settings Actions OFF, Dependabot, run status | FAIL⇒DỪNG, không lách, Host | S3 |
| S3 | Codex/S2 XONG hoặc S1 DỪNG | ≤15 phút | KQ + Bảng + report | GPT Host đọc, Owner quyết | END |

KHÔNG ĐƯỢC: sửa runtime VPS/Git remote/cron/Guard/nginx/compose/DB/Graph; đổi quyền SSH/token, cấp root, mua Pro, làm R2–R6, mở public repo, tự merge hoặc deploy. Không giữ terminal/VPS-GHI chờ người; nếu gate FAIL thì kết thúc sạch với NEXT_TRIGGER.
