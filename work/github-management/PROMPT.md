# PROMPT — GHM R1 · KHOÁ CHI PHÍ GITHUB ACTIONS (ACTIONS VẪN BẬT)
RUN_ID: GHM-R1-COST-20261025-01
STATUS: DRAFT — Claude soạn theo Owner 25/10 (COLLAB P14) và ký ACCEPT@last-touch; GPT Host đọc TOÀN BỘ PROMPT rồi READY@cùng SHA; Owner giao Codex. Thay bản DRAFT `GHM-R1-SELFHOST-FIT-20261025-01` (SUPERSEDED_UNRUN, lịch sử ở Git). RUN này không cần chờ cờ VPS-GHI (không đụng VPS).

**Mục tiêu duy nhất (Owner 25/10):** run GitHub không bao giờ gây chi phí mất kiểm soát. Actions **vẫn BẬT**; không cài runner; không tắt Actions cấp repo.

Executor_Surface: Codex CLI/Desktop trên Mac (`gh` đăng nhập Owner) + GitHub web UI · Write_Path: trang billing của tài khoản + cài đặt workflow của 2 repo `Huyen1974/agent-data-test`, `Huyen1974/web-test`; workspace_* root=workspace cho STARTED/KQ/Bảng. Không đụng VPS ngoài tệp bằng chứng root-only như P12. GitHub hỏi mật khẩu/2FA/passkey ⇒ dừng đúng bước nhờ Owner rồi làm tiếp; không lưu mã.

ENTRY: AGENTS.md → work/github-management/COLLAB.md §0/Bảng/P12–P14 → PROMPT này. Thiếu ACCEPT/READY cùng SHA hoặc Owner RUN ⇒ DỪNG.

## S0 — ĐO CHI PHÍ (chỉ đọc, ≤10′)
- 0.1 Gói tài khoản; có phương thức thanh toán không (chỉ CÓ/KHÔNG).
- 0.2 Budgets and alerts: có ngân sách sản phẩm Actions phạm vi cả tài khoản không · số tiền · có «Stop usage when budget limit is reached» không · cảnh báo 75/90/100% bật không.
- 0.3 Chu kỳ này: phút GitHub-hosted đã dùng / đã gồm, dung lượng Actions; tiền phát sinh tháng này và tháng trước (số tiền).
- 0.4 Copilot code review có bật ở 2 repo không (từ 06/2026 tính vào phút Actions).

## S1 — KHOÁ TIỀN (≤10′)
- 1.1 Chưa có ngân sách Actions $0 + Stop usage phạm vi cả tài khoản ⇒ tạo: github.com/settings/billing → Budgets and alerts → New budget → Product-level budget · Actions · cả tài khoản · số tiền 0 → tích «Stop usage when budget limit is reached» → tích «Receive budget threshold alerts» → Create budget. Đã có nhưng thiếu Stop usage hoặc cảnh báo ⇒ sửa đúng ô đó. Ngân sách chỉ tính từ lúc tạo ⇒ làm ngay trong RUN này.
- 1.2 Copilot code review đang bật ⇒ ghi lại, không tự tắt (Host quyết).
- 1.3 Không mua Pro, không thêm/xoá thẻ thanh toán.

## S2 — GIỮ PHÚT MIỄN PHÍ CHO 3 NHÓM KIỂM CẦN (≤15′)
- 2.1 Lấy danh sách workflow thuộc 3 nhóm cần giữ và các workflow BỎ từ báo cáo P12 (root-only) — không kiểm kê lại.
- 2.2 Tắt từng workflow BỎ đang active: `gh workflow disable <id> -R <repo>` (bật lại bằng `gh workflow enable`). Không sửa YAML/branch/code, không tắt Actions cấp repo, không động 3 nhóm cần giữ.
- 2.3 Ghi danh sách đã tắt + lệnh bật lại vào `/opt/incomex/work/github-management/GHM-R1-COST-20261025-01/` (tệp chỉ root đọc); không ghi được ⇒ trả chat cho Owner.
- 2.4 S1 không đạt vẫn làm S2 (giảm hao phút là an toàn), KQ ghi rõ S1 chưa đạt.

## S3 — KIỂM + KQ (≤10′)
- 3.1 POST: ngân sách Actions $0 + Stop usage tồn tại; workflow active mỗi repo chỉ còn các workflow thuộc 3 nhóm cần; Actions vẫn enabled.
- 3.2 KQ@GHM-R1-COST-20261025-01 XONG|DỪNG trong COLLAB + Bảng cùng commit. Repo PUBLIC ⇒ chỉ ghi: thẻ thanh toán CÓ/KHÔNG, ngân sách $0 + Stop CÓ/KHÔNG, phút đã dùng/đã gồm, tiền tháng này, số workflow active trước/sau, Copilot review CÓ/KHÔNG, blocker. Tên workflow và chi tiết ở tệp root-only.
- 3.3 Một dòng cho Host: ước phút/tháng của 3 nhóm cần (từ lịch + thời lượng 30 ngày) so với phút đã gồm. Vượt ⇒ đề xuất xét self-hosted runner ở bước sau, không tự làm.

STEP_WALK_V1:
| Bước | Ai/trigger | Hạn | Bằng chứng | Lỗi → ai | Kế |
|---|---|---|---|---|---|
| S0 | Codex / Owner RUN | ≤10′ | 0.1–0.4 | thiếu quyền ⇒ DỪNG, Host | S1 |
| S1 | Codex / S0 xong | ≤10′ | ngân sách $0 + Stop | passkey ⇒ nhờ Owner | S2 |
| S2 | Codex / S1 xong | ≤15′ | danh sách đã tắt | lỗi ⇒ DỪNG, Host | S3 |
| S3 | Codex / S2 xong | ≤10′ | POST + KQ | Host / Owner | END |

CẤM: tắt Actions cấp repo; cài runner; sửa YAML/branch/code/main; mua Pro; đổi secret/token/thẻ thanh toán; đụng VPS runtime; tự READY/RUN tiếp. Không giữ phiên chờ người; thiếu quyền/dữ kiện ⇒ UNKNOWN/DỪNG sạch.
