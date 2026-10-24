# PROMPT — GHM-R0R1 · ĐO HIỆN TRẠNG + TẮT GITHUB ACTIONS (CHỈ 2 REPO)
RUN_ID: GHM-R0R1-20261024-01
STATUS: DRAFT_REVIEW_READY — ĐÃ SOẠN ĐỦ ĐỂ KÝ, CHƯA READY/RUN. Claude Reviewer kiểm một lượt, ghi ACCEPT@full SHA last-touch PROMPT; GPT Host chỉ ghi READY@SHA khi Owner chuẩn bị RUN và cổng VPS-GHI/đích đang rảnh phù hợp. Owner chuyển RUN cho Codex. Không tự chạy khi cờ chuyển trống.

Executor_Surface: Codex CLI/Desktop; Write_Path: Incomex workspace_* root=workspace cho hồ sơ STARTED/KQ; GitHub Settings/API chỉ để Disable Actions và Dependabot auto-PR sau S1 gate. SSH/MCP VPS read-only chỉ quan sát, không mutation VPS.

ENTRY: root AGENTS.md → root COLLAB phần cờ VPS-GHI → work/github-management/COLLAB.md §0/Bảng/P5/P6 → README → ROADMAP V0.3 → KE-HOACH V0.2 → PROMPT này. Xác minh A6 & DROOT30/31 trước bất kỳ thao tác ghi. PROMPT cũ P1A đã superseded. Không làm R2/R3.

## S0 — KIỂM QUYỀN & TRẠNG THÁI (READ-ONLY)
- Kiểm đúng hai repo Huyen1974/agent-data-test và Huyen1974/web-test, private, actions status hiện thời, run gần nhất, required checks, webhook, dependabot, workflow theo lịch và triggers.
- Trước Owner RUN: kiểm VPS-GHI + phạm vi phiên Claude Code đang làm; nếu đang ghi cùng nguồn/đích thì **KHÔNG khởi RUN**, không mở phiên chờ; chỉ giữ PROMPT đã ký để giao lại khi cờ trống. Lúc Codex chạy S0 phải kiểm lại VPS-GHI và hoạt động Claude Code thực; nếu trùng khu đang ghi hoặc không xác định được trạng thái ⇒ ghi KQ DỪNG, NEXT_TRIGGER=VPS_GHI_FREE_AND_SCOPE_CLEAR, trả mọi tài nguyên. Cờ VPS-GHI trống không tự chứng minh phiên Claude Mac đã dừng.
- Codex chỉ READ-ONLY GitHub/VPS ở S0–S1, không giữ VPS-GHI cho phép đọc, không dùng root production shell để sửa, không git fetch/reset/pull vào working tree Claude đang làm. Nếu snapshot đang chuyển đổi, ghi UNKNOWN; không tự kết luận sạch.

## S1 — R0: PHẢI CÓ KQ READ-ONLY TRƯỚC KHI TẮT
1. Kiểm từ VPS root thực tế của mã Agent Data / Web (dự kiến docker/agent-data-repo, docker/nuxt-repo): git branch, HEAD, status tracked/untracked, upstream/remotes đã che, nhánh backup vps-daily, GitHub refs. Kiểm mã thực đang chạy theo image/build labels, hashes/evidence: **HEAD không tự coi là image đang chạy**. Mã ui-preview không phải nguồn web-test.
2. Liệt kê từng GitHub Actions workflow, lịch, run, chức năng thật và phụ thuộc production; phân loại MIGRATE (đã có đường Guard/Kuma/backup vận hành) hay BỎ. Chỉ dẫn nguồn bằng chứng, đừng giữ Action «chạy vì có sẵn». Kiểm cron/reverse backup VPS→GH có thể gây merge/pull nhầm mà không đụng đến job đó.
2a. **P7 — inventory WRITE PATHS CHỈ ĐỌC:** xác định tất cả tác nhân/script/process **đang ghi hoặc có khả năng ghi** tại hai thư mục mã `docker/agent-data-repo` và `docker/nuxt-repo` (bao gồm build Nuxt, backup `.git`, dịch vụ systemd, MCP workspace root, shell/SSH, hooks/cron); ghi tên chức năng + write scope + thời điểm chạy + quyền, không đọc credential, không sửa/khóa quyền. Đây là đầu vào cho R5.2, **không thực hiện khóa read-only R5 tại RUN này**.
3. Lập ma trận định danh/quyền có thể push/main/admin của 2 repo bằng tên actor + permission (KHÔNG lấy hoặc in token, SSH private key); Dependabot hiện có. R6 đọc thử đường gọi Dot→Codex, Codex cloud/Claude cloud; không có API/receipt thật ghi UNKNOWN (không chặn R1).
4. **HARD STOP S1→S2:** trước khi ghi GitHub phải kiểm lại sự kiện/đích mà Claude Code đang thao tác; nếu một workflow phục vụ production/canh/backup hoặc RUN Claude đang phụ thuộc Actions mà chưa có đường thay hoạt động, hoặc Codex không đủ quyền chỉnh GH, thì ghi DỪNG mốc này và KHÔNG tắt. Không dùng cờ trống từ snapshot cũ để cấp phép, không chạy gì trên VPS để «tạo đường thay» trong RUN này. Nếu S1 PASS, S2 chỉ chạm GitHub settings và không cần VPS-GHI; không chờ/cướp cờ VPS.

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

KHÔNG ĐƯỢC: sửa runtime VPS/Git remote/cron/Guard/nginx/compose/DB/Graph; đổi quyền SSH/token, cấp root, mua Pro, làm R2–R6, mở public repo, tự merge hoặc deploy. Không giữ terminal/VPS-GHI chờ người; nếu gate FAIL thì kết thúc sạch với NEXT_TRIGGER. **RUN chỉ do Owner giao cho Codex khi điều kiện đã sạch; sự kiện VPS-GHI nhả cờ tự nó không phải RUN hoặc lệnh nền.**
