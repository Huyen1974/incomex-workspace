# PROMPT — GHM S1 SYNC-MAIN: main Agent Data chứa đúng mã đang chạy (Claude P157 · DRAFT chờ Host READY)

RUN_ID: GHM-SYNC-MAIN-20261031-15 · Người chạy: Claude Code CLI (KST) trên Mac · Phạm vi: chỉ GitHub `Huyen1974/agent-data-test` · 0 VPS-GHI · 0 deploy · 0 sửa mã.
STATUS: HOST_P158_DRAFT · NOT_READY khi HJW RUN25 còn STARTED; PR358 chứa PR357 nên không được dùng S1 merge cũ. Chỉ Host ký READY sau HJW KQ và đối chiếu main/PR hiện hành.

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

## S1 — KST chốt MỘT đường nhập, không tự merge PR357
1.1 Bắt buộc đọc **HJW RUN25 KQ** cùng hiện trạng **PR358**: PR358 đã chứa commit PR357 36c68291 (có merge fe948016) và hiện DRAFT. P489 HJW không cho merge trùng. Nếu RUN25 còn STARTED, không mở S1, báo sự kiện thật và không giữ terminal chờ.
1.2 Nếu HJW KQ/Host đã chọn PR358 là đường gộp duy nhất: KHÔNG merge PR357. Trạng thái đúng: AD source ở GH PR358/357, AD main khác runtime; HJW G8 chịu trách nhiệm hợp nhất main/release sau Linux image+rollback. Không tuyên SYNC_MAIN_PASS.
1.3 Chỉ nếu HJW KQ **cho phép rõ** đưa PR357 trước, chứng nhận không ảnh hưởng PR358 và có đường cập nhật base PR358: KST rà 4 tệp + 3 live queue blob, kiểm fresh `deploy-vps.yml=disabled_manually`, main/HEAD/cổng required gate; `gh pr ready` và `gh pr update-branch` #357; đợi CI GREEN đúng HEAD/main hiện tại, KST_ACCEPT@exact SHA; merge --match-head-commit, kiểm 3 blob, push-main gate, 0 deploy; ghi comment cho HJW PR358 rebase sau. Không đổi workflow hay VPS. Có xung đột/bất đồng thì KHÔNG force, giữ an toàn.
1.4 Nếu PR358 đã merge trước S1, đo main 3 blob/thực chạy; bỏ thao tác #357 (đóng PR nếu superseded theo HJW) và ghi đúng parity.
1.5 Không gọi lỗi 'thiếu source trên GitHub': #357 và #358 hiện chứa source. PR358 bản ghép không nhất thiết blob bằng image đang chạy; phân biệt SOURCE_PRESENT, MAIN_PARITY và LIVE_IMAGE riêng.

## S1b — Chuẩn bị luôn hai phiếu F2 từ backlog có thật, không tạo task mới
- **AD CONN-REPAIR PR353:** test-only `tests/continuation/test_p02_snapshot_k8.py`, nhánh `dev/claude-code-ad/conn-repair-03c-p02-sync` trusted, base cũ; KST kiểm ghép main mới, gate/test rồi quyết độc lập (không tự duyệt PR mình viết).
- **Web WEB-71 PR327:** `dot/bin/dot-start-all`, nhánh hiện `docs/web-71-closure` KHÔNG trusted; 1 worker dùng branch `dev/claude-code-web/web71-stats` từ main mới, mang đúng delta và thêm/kiểm regression, CI gate rồi KST review. Không bypass OUT_OF_PILOT. Các PR cũ là backlog, **không tính là hai agent mới chạy đêm song song**.
- Mỗi phiếu đúng 6 ô: Task/goal, DoD/test, files được sửa, base SHA và phụ thuộc, dev seat, KST/review + giới hạn; có thể giao ngay khi có worker thật, không đợi P119.
- C4 automatic overnight không được tô xanh chỉ vì Owner dán lệnh một lần; nếu chỉ Claude CLI sẵn, ghi 1 seat, không giả 3 dev seats.

## S2 — KQ
Ghi KQ P159 (P158 là quyết định Host, không ghi đè) + Bảng + ROADMAP qua Gateway: `AD_SOURCE_PRESENT_ON_GH=YES_SCOPED`; `AD_MAIN_RUNTIME_BLOB_PARITY=YES|NO|PARTIAL` chỉ theo readback thật; nếu merge #357 có CI xanh, ghi merge SHA và 0 deploy; nếu HJW chọn #358/chưa đủ gate, báo `GHM_S1_HJW_DEPENDENCY` và không giả pass. `WEB_MAIN_EQ_LIVE=YES_SCOPED` chỉ khi đo đúng cây app. Hai phiếu F2 6 ô cần có. NEXT_TRIGGER=F2_BATCH_CODE_WORKERS_READY hoặc đúng blocker HJW. Không đóng toàn task khi C4 chưa nghiệm thu.

Cấm: ghi VPS/SSH ghi, deploy, sửa ruleset/workflow/secret, force-push, xoá nhánh, mở task/PR mới.
