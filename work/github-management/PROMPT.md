# PROMPT — GHM R2-A · KHOÁ `main` + LUẬT REPO TRÊN GITHUB (2 REPO)
RUN_ID: GHM-R2-ACCESS-20261025-01
STATUS: DRAFT — GPT Host soạn (P18); Claude P19 sửa tại chỗ 5 điểm (đếm deploy key ghi · khoá main trước rồi mới mở nhánh · thử chặn bằng danh tính mạnh nhất · việc tự động đang ghi main · tiêu chí XONG rõ) rồi ACCEPT@last-touch. GPT Host READY đúng SHA; Owner giao Codex. Chưa có RUN.

Executor_Surface: Codex CLI/Desktop (Mac, `gh` đăng nhập Owner) · Write_Path: GitHub API/gh CLI (rulesets, nhánh, PR nháp) của `Huyen1974/agent-data-test`, `Huyen1974/web-test`; workspace_* root=workspace ghi STARTED/KQ + Bảng. KHÔNG shell/SSH ghi VPS, không sinh/thay chìa KST, không đổi production. Chi tiết actor/token/đường ghi chỉ lưu root-only tại `/opt/incomex/work/github-management/GHM-R2-ACCESS-20261025-01/` (như P17); repo public chỉ tóm tắt số đếm.

ENTRY: AGENTS.md root → root COLLAB cờ/luật → work/github-management/COLLAB.md §0/Bảng/P17–P19 → ROADMAP V0.3 → KE-HOACH R2 → PROMPT này. DROOT30/31 freshness/STARTED/KQ trước mutation. Thiếu ACCEPT/READY cùng SHA hoặc Owner RUN ⇒ DỪNG. R1 đã nghiệm thu (P18), không chạy lại.

## S0 — KIỂM TRƯỚC (chỉ đọc, ≤15′)
- 0.1 Tài khoản đã lên GitHub Pro (Owner tự mua); 2 repo PRIVATE, default branch `main`, dùng được rulesets. Pro chưa active ⇒ KQ DỪNG, NEXT_TRIGGER=OWNER_PRO_ACTIVE. **Không tự mua gói, không thêm/thay phương thức thanh toán.**
- 0.2 Ngân sách Actions cả tài khoản $0 + **Stop usage** còn nguyên sau khi lên Pro (= T-d); 3 nhóm kiểm cần vẫn active; 15 workflow BỎ vẫn disabled; Dependabot động chỉ là ngoại lệ khi đúng loại GitHub-managed + runner tiêu chuẩn (không larger). Mất hard-stop ⇒ DỪNG trước mọi thay đổi, báo Owner.
- 0.3 **Lỗ khoá (P19):** bypass loại `DeployKey` = MỌI deploy key có quyền ghi. Đếm deploy key `read_only=false` từng repo (P12 đo 0). >0 ⇒ KHÔNG xoá, ghi root-only, KQ DỪNG cho Host.
- 0.4 Liệt kê việc tự động đang đẩy thẳng vào `main` (workflow giữ lại, app/bot). Ruleset sẽ chặn cả chúng ⇒ chỉ ghi lại cho Host, không sửa YAML, không dừng.
- 0.5 Không có RUN khác đang sửa rulesets/quyền/nhánh chính của 2 repo. Không cần VPS-GHI (chỉ GitHub).

## S1 — KHOÁ `main` (≤25′)
- 1.1 Mỗi repo 1 ruleset tên `chief-only-main`: enforcement=active, target CHỈ `~DEFAULT_BRANCH` (main); luật `update` · `deletion` · `non_fast_forward`; bypass DUY NHẤT loại `DeployKey` — y mẫu `gateway-only-writes` của incomex-workspace. KHÔNG dùng `~ALL` (chặn cả nhánh dev); không cho admin/dev bypass; không tạo deploy key nào ở bước này ⇒ sau S1 chưa ai ghi được main cho tới R2-B (đúng ý).
- 1.2 Đọc lại: ruleset active, đích chỉ main; `GET /repos/{repo}/rules/branches/main` trả đủ 3 luật. Số actor bypass theo loại/số đếm; ID chi tiết chỉ root-only.
- 1.3 **T-a thử chặn (P19):** dùng chính `gh` hiện tại (Owner admin = quyền mạnh nhất; mạnh nhất bị chặn ⇒ thẻ dev yếu hơn chắc chắn bị chặn) đẩy 1 commit RỖNG vào `main` mỗi repo (git push hoặc API refs) ⇒ phải bị từ chối (GH013 / 409 như incomex-workspace 25/09). Lỡ được nhận ⇒ DỪNG, KHÔNG revert/force, báo Host (commit rỗng vô hại; R3 cất main cũ vào tag). Admin chỉ dùng cho phép thử CHẶN, không dùng để chứng minh quyền dương của worker.
- 1.4 T-e (force-push/xoá) KHÔNG thử thật: chứng minh bằng 1.2 + T-a cùng ruleset. T-b (thẻ dev không sửa được ruleset) + T-c (chìa KST đi qua) ⇒ R2-B/R3, khi đã có thẻ dev và chìa KST.
- 1.5 Chìa KST: Claude Code CLI tự sinh và giữ ở R2-B (Đ30/31, VPS-GHI). Codex không cầm/đọc/gửi private key, không tự push main; không lấp chỗ thiếu chìa bằng cách cho admin bypass.

## S2 — LUẬT REPO (≤20′, SAU S1)
- 2.1 Tận dụng luật AGENTS gốc, không dựng hệ mới: `AGENTS.md` ≤ 1 trang + mẫu Issue/PR 6 ô (TASK_ID · mục tiêu/DoD + lệnh test · khu tệp được/cấm sửa · phụ thuộc/base SHA · ghế dev + KST · giới hạn thời gian/điều cấm); quy tắc nhánh `dev/<ghế>/<mã việc>`; KST 4 kết luận NHẬN/SỬA/TRẢ LẠI/BỎ.
- 2.2 Đẩy lên nhánh `dev/codex/GHM-R2A-rules` của mỗi repo và mở 1 PR NHÁP vào `main` (không merge — R3.3 KST merge). Đẩy SAU khi ruleset active ⇒ đây chính là phép thử «nhánh dev + PR vẫn mở». Bị chặn ⇒ DỪNG kèm bằng chứng, không gỡ ruleset. Không đưa secret/khoá/địa chỉ nhạy cảm vào tệp.

## S3 — KIỂM + KQ (≤15′)
- 3.1 Mỗi repo: ruleset active chỉ main · deploy key ghi = 0 · T-a bị chặn · nhánh + PR nháp có · Actions vẫn ON 3 nhóm · ngân sách $0 + Stop còn.
- 3.2 **XONG khi đủ 3.1 ở cả 2 repo.** T-b, T-c ghi `PENDING_R2B` là ĐÚNG KẾ HOẠCH, không phải lý do DỪNG. DỪNG chỉ khi một mục 3.1 hỏng.
- 3.3 KQ@GHM-R2-ACCESS-20261025-01 XONG|DỪNG trong COLLAB + Bảng cùng commit: số đếm, URL nhánh/PR, kết quả T-a, mục 0.4. Chi tiết actor/khoá chỉ root-only. NEXT_TRIGGER khi XONG = `KST_R2B_KEY` (Claude Code CLI sinh chìa; Codex gắn deploy key; thẻ dev + hạ quyền admin — R2.2). Không tự làm R2-B/R3.

STEP_WALK_V1:
| Bước | Ai/trigger | Hạn | Bằng chứng | Lỗi → ai | Kế |
|---|---|---|---|---|---|
| S0 | Codex / Owner RUN | ≤15′ | Pro · ngân sách · deploy key · ghi main tự động | Pro chưa có / key>0 / mất Stop ⇒ DỪNG, Owner/Host | S1 |
| S1 | Codex / S0 đạt | ≤25′ | ruleset đọc lại + T-a bị chặn | T-a lọt ⇒ DỪNG, Host | S2 |
| S2 | Codex / S1 đạt | ≤20′ | nhánh + PR nháp | nhánh bị chặn ⇒ DỪNG, Host | S3 |
| S3 | Codex / S2 xong | ≤15′ | KQ + Bảng | Host nghiệm thu, Owner giao R2-B | END |

CẤM: mua Pro, đổi thẻ thanh toán/ngân sách; push/merge/delete/reset/force vào main (ngoại lệ DUY NHẤT: 1 commit rỗng thử chặn T-a mỗi repo); merge PR; tạo deploy key/chìa KST hoặc đưa chìa cho Codex; thay token/secret; SSH/ghi VPS; cài runner; sửa YAML/runtime. Gặp blocker ⇒ KQ DỪNG + NEXT_TRIGGER, không giữ phiên chờ Owner.
