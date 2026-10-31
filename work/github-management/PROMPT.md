# PROMPT — GHM S1 SYNC-MAIN: main Agent Data chứa đúng mã đang chạy (Claude P157 · DRAFT chờ Host READY)

RUN_ID: GHM-SYNC-MAIN-20261031-15 · Người chạy: Claude Code CLI (KST) trên Mac · Phạm vi: chỉ GitHub `Huyen1974/agent-data-test` · 0 VPS-GHI · 0 deploy · 0 sửa mã.
STATUS: DRAFT_CLAUDE_P157 · NOT_READY đến khi GPT Host ký READY@last-touch SHA tệp này. Bản C2 cũ (đã xong) xem lịch sử git của tệp.

## Vì sao (đo 31/10 13:15–13:35 +07, gh API + vps_status)
1. AD đang chạy image `agent-data-hvu:w4q-20261029-06` = 46e0ba15 + đúng 3 tệp của PR #357 HEAD `36c682914c9f412078113b6d85319f11356d1130` (receipt trên PR #357, 29/10 21:45).
2. Ba tệp `agent_data/workspace_execution.py` · `workspace_runtime.py` · `workspace_tasks.py`: blob #357 = blob `vps-daily-20261031` (`493533a8…` · `789a22f8…` · `584a0d8e…`); main `6160f9ad` khác ⇒ ai viết mã AD từ main sẽ đè mất bản đang chạy.
3. `deploy-vps.yml` của AD = `disabled_manually` ⇒ merge vào main KHÔNG deploy. Ghi chú «merge vẫn bị cấm» trên #357 dựa giả định cũ.
4. #357 DRAFT, gate success 29/10 trên HEAD cũ, chậm main 4 commit (các merge lưu mã C2/PR360, không chồng 3 tệp).

## S0 — Kiểm vào (sai điểm nào ⇒ KQ DỪNG sạch, không sửa gì)
0.1 Đọc `AGENTS.md` gốc (L1, L2) → PROMPT này → COLLAB GHM P157.
0.2 RUN `HJW-G8-PREPROD-QUALIFICATION-20261031-25` đã có KQ ở HJW COLLAB; không RUN nào khác đang ghim main AD (Bảng HJW, Bảng VPSC2). Còn chạy ⇒ không chen: KQ `WAIT_HJW_RUN25`, dừng.
0.3 `gh api repos/Huyen1974/agent-data-test/actions/workflows` ⇒ `deploy-vps.yml` = `disabled_manually`; khác ⇒ DỪNG.
0.4 #357 HEAD vẫn `36c68291…`; diff chỉ 4 tệp (3 tệp trên + `tests/continuation/test_vpsc2_w4q05_queue.py`), 0 workflow/secret/Dockerfile.
0.5 Blob 3 tệp trên #357 = blob cùng path trên nhánh `vps-daily-<ngày mới nhất>`.

## S1 — KST merge (một lần, đúng luật L1)
1.1 `gh pr ready 357 -R Huyen1974/agent-data-test` → `gh pr update-branch 357 -R Huyen1974/agent-data-test` (merge thường, không rebase/force).
1.2 Theo dõi `gate` trên HEAD mới đến khi xong; xanh mới đi tiếp. Đỏ ⇒ DỪNG, ghi lý do; không sửa mã trong RUN này.
1.3 Review diff HEAD mới vs main: vẫn chỉ 4 tệp, nội dung 3 tệp không đổi so với 0.5.
1.4 Comment `KST_ACCEPT@<HEAD mới>` (lý do: ghi nhận mã đang chạy production, receipt VPSC2-08) → `gh pr merge 357 -R Huyen1974/agent-data-test --merge --match-head-commit <HEAD mới>`. Không `--admin`, không bypass.
1.5 Sau merge: blob 3 tệp trên main = 0.5; `gate` push-main success; không run deploy nào khởi chạy.
1.6 Comment trên #358: «#357 đã vào main tại `<merge SHA>`; nội dung #358 không đổi; lần tới cần update-branch theo main mới.» Không sửa/merge #358, #353, Web #683, #686.

## S2 — KQ
Ghi COLLAB GHM `P158` + Bảng + dòng đầu ROADMAP/README (qua gateway): `AD_MAIN_HAS_RUNNING_CODE=YES` (main ⊇ bản đang chạy; main còn hơn bản chạy các tệp chờ HJW G8 phát hành — HJW S3 và `pg_store.py`) · `WEB_MAIN_EQ_LIVE=YES` (cây `web/` main = `0bc47577` = bản deploy P131, đo lại 1 lệnh) · merge SHA · run ID · link comment. NEXT_TRIGGER=HOST_ACCEPT_S1_THEN_S2_BATCH1.

Cấm: ghi VPS/SSH ghi, deploy, sửa ruleset/workflow/secret, force-push, xoá nhánh, mở task/PR mới.
