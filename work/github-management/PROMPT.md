# PROMPT — GHM RUN15: chốt nguồn AD theo HJW P493 + chuẩn bị F2 thật, KHÔNG MERGE

RUN_ID: GHM-SYNC-MAIN-20261031-15
STATUS: NOT_READY · chờ GPT Host ký READY@<full last-touch SHA> tại GHM COLLAB. Theo HJW P491/P493: NO_GO_RELEASE; RUN15 không merge #357/#358.

## Vì sao (đo 31/10 13:15–13:35 +07, gh API + vps_status)
1. AD đang chạy image `agent-data-hvu:w4q-20261029-06` = 46e0ba15 + đúng 3 tệp của PR #357 HEAD `36c682914c9f412078113b6d85319f11356d1130` (receipt trên PR #357, 29/10 21:45).
2. Ba tệp `agent_data/workspace_execution.py` · `workspace_runtime.py` · `workspace_tasks.py`: blob #357 = blob `vps-daily-20261031` (`493533a8…` · `789a22f8…` · `584a0d8e…`); main `6160f9ad` khác ⇒ ai viết mã AD từ main sẽ đè mất bản đang chạy.
3. `deploy-vps.yml` của AD có trigger push main, đo 31/10 = `disabled_manually`; HJW P493 yêu cầu đọc lại và không merge trước build/canary. Đây chỉ là thông tin tham khảo, không phải lý do để merge.
4. #357 DRAFT, gate success 29/10 trên HEAD cũ, chậm main 4 commit (các merge lưu mã C2/PR360, không chồng 3 tệp).

## S0 — Kiểm vào (sai điểm nào ⇒ KQ DỪNG sạch, không sửa gì)
0.1 Đọc `AGENTS.md` gốc (L1, L2) → PROMPT này → COLLAB GHM P157–P158. Phần merge #357/#358 và phần chờ HJW RUN25 trong hai mục đó đã hết hiệu lực, PROMPT này thắng.
0.2 HJW RUN25 đã KQ P491 và Host P493 ACCEPT_PARTIAL_PREPROD/NO_GO_RELEASE; không merge trong lượt này. Không dùng HJW stage1 làm lý do STOP khi thực hiện F2.
0.3 GitHub workflow deploy trạng thái tham khảo, không là cổng của RUN chỉ đọc/no-merge/no-deploy. Ghi nguồn và thời điểm nếu khác.
0.4 #357 HEAD vẫn `36c68291…`; diff chỉ 4 tệp (3 tệp trên + `tests/continuation/test_vpsc2_w4q05_queue.py`), 0 workflow/secret/Dockerfile.
0.5 Blob 3 tệp trên #357 = blob cùng path trên nhánh `vps-daily-<ngày mới nhất>`.

## S1 — HJW P491/P493 ĐÃ CHỐT, KHÔNG MERGE #357 HAY #358
1.1 HJW RUN25 KQ P491/Host P493 = ACCEPT_PARTIAL_PREPROD, NO_GO_RELEASE. PR358 (HEAD235dc880) đã chứa mã PR357 (HEAD36c68291). Linux image/rollback/staging chưa nghiệm thu. Host quyết định KHÔNG nhập riêng #357 vào main, cũng KHÔNG merge #358 trong GHM. Không coi đây là S0 blocker.
1.2 Read-only: ghi 3 queue source đã có trên PR357/358; main AD 6160f9ad chưa có parity với mã đang chạy. Nếu main/PR thay đổi sau nguồn này, phân loại lại theo SHA thật; không tự đóng/mở PR, không làm mã HJW bị trùng.
1.3 Đường nhập main+triển khai sau thuộc HJW G8 và Owner GO, KHÔNG là cổng của mẻ F2 viết mã. S1 hoàn thành khi trạng thái và chủ phụ thuộc được ghi chính xác, không cần merge.

## S1b — Chuẩn bị luôn hai phiếu F2 từ backlog có thật, không tạo task mới
- **AD CONN-REPAIR PR353:** test-only `tests/continuation/test_p02_snapshot_k8.py`, nhánh `dev/claude-code-ad/conn-repair-03c-p02-sync` trusted, HEAD `362e2e50`, base cũ (hơn main `6160f9ad` 1 commit, chậm 10, đo 31/10); KST kiểm ghép main mới, gate/test rồi quyết độc lập (không tự duyệt PR mình viết).
- **Web:** WEB-71 PR327 đã bỏ khỏi danh sách F2 vì `dot/bin/dot-start-all` trên PR327 = main `8100ae6f` (blob `33db3f45`, đo 31/10). Ứng viên Web phải có phần việc còn thiếu thật và được chủ task cho phép: GS-UC1 PR683 chỉ khi task Graph còn việc code-only và chủ task cho phép, hoặc việc Web khác có lỗi/diff thật trong task hiện hữu. Không có ứng viên đạt ⇒ ghi đúng nguồn thiếu, không tạo PR giả. Các PR cũ không được tính là 2 agent đang chạy song song.
- Mỗi phiếu đúng 6 ô: Task/goal, DoD/test, files được sửa, base SHA và phụ thuộc, dev seat, KST/review + giới hạn; có thể giao ngay khi có worker thật, không đợi P119.
- C4 automatic overnight không được tô xanh chỉ vì Owner dán lệnh một lần; nếu chỉ Claude CLI sẵn, ghi 1 seat, không giả 3 dev seats.

## S2 — KQ
Ghi KQ P161 (P159/P160 là Host) + Bảng và ROADMAP qua Gateway. SOURCE_PRESENT_ON_GH=YES_SCOPED; AD_MAIN_RUNTIME_BLOB_PARITY=NO nếu chưa có chứng cứ mới; HJW_P493=NO_GO_RELEASE; 0 merge/deploy. Hai phiếu F2 6 ô phải có công việc thật, mỗi phiếu có dev seat/reviewer phù hợp. NEXT_TRIGGER=OWNER_DISPATCH_F2_BATCH1_CODE_ONLY hoặc thiếu đúng một nguồn/seat cụ thể. Không dừng vì #357 không được merge, không đóng toàn GHM khi C4 chưa nghiệm thu.

Cấm: merge (gồm #357/#358), ghi VPS/SSH ghi, deploy, sửa ruleset/workflow/secret, force-push, xoá nhánh, mở task/PR mới.
