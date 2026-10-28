# GHM-R1-COST-POSTPRO-20261028-08 — COST GUARD SAU GITHUB PRO
Executor: Codex Desktop/CLI, Owner chuyển lệnh. Task hiện hữu work/github-management. Chỉ RUN khi Host ký READY@full SHA của file này ở COLLAB.
Mục tiêu: chỉ trả phí thuê bao GitHub Pro $4/tháng, không phát sinh phí usage-based từ Actions hay các sản phẩm khác. Không làm lại C2-A hoặc thay đổi PROMPT C2-B P92.

## Rào
- Đúng tài khoản personal Huyen1974. S0 kiểm AGENTS, COLLAB §0/P17–P19/P99–P100, ROADMAP, file này; không đụng repo khác ngoài phần đối chiếu Actions account.
- Không mua gói, thêm payment/credit/seat/key/bot, đổi visibility, secret, branch ruleset, main, PR, CI YAML, VPS, runner, production. Không phát run mới, rerun, workflow_dispatch, deploy hoặc trigger GitHub-hosted.
- R1 P17 đã có Account Actions budget $0 + Stop và tắt 15 workflow; 3 nhóm thiết yếu vẫn chạy self-hosted VPS, dynamic Dependabot do GitHub quản. Kiểm lại thực tế trước khi sửa. Không tắt all Actions nếu phá CODE gate. Không đăng dữ liệu thanh toán/secret lên repo public.
- Nếu thấy RUN khác sửa Billing/workflow trùng phạm vi, hoặc phải xác thực passkey: DỪNG an toàn, không đoán và không giữ phiên chờ.

## S0 — CHỈ ĐỌC
1) Xác minh user Huyen1974, Pro active; hai private repo agent-data-test/web-test GET rulesets đọc được. Không tạo ruleset.
2) Billing Overview/Usage thực trong cycle: Pro $4, gross metered, included discount, net billable, next due/payment history; breakdown Actions phút & storage, Codespaces, LFS, Packages, Models, Copilot AI credits, Spark/cloud agent, mọi usage product đang có. Ảnh Owner 28/10 cho gross $8.28 = included $8.28, CHƯA phải overage; cần xem hóa đơn thực, không tự nhân giá.
3) Budgets and alerts: Actions scope Account amount $0; Stop usage when budget limit is reached = ON; alerts = ON; included-usage 90/100% = ON. Đọc tất cả budgets có thể overlap. Kiểm workflow của các repo account và runner self-hosted/GitHub-hosted, scheduled/queued/in_progress. Không chạy run để kiểm.

## S1 — KHÓA PHÍ, CHỈ THAY CÁI THIẾU
1) Nếu Actions account $0 hard stop thiếu/sai, khôi phục cấu hình R1 P17 và readback. Nếu không làm được thì KQ DỪNG COST_HARD_STOP_UNVERIFIED, tuyệt đối không tiếp tục C2-B.
2) Với từng sản phẩm usage-based khác đang bật: đặt budget $0 với Stop hard-stop nếu được phép; tắt tính năng tự tiêu phí không cần thiết khi tác động đã rõ. Nếu sản phẩm không có khóa hoặc số dư cũ, ghi RESIDUAL_RISK, tuyệt đối không tuyên bảo đảm 100%.
3) Workflow thừa/GitHub-hosted có thể tiêu phí: disable đúng workflow và xác nhận; chỉ hủy run đang chạy khi đã biết chắc không liên quan production. Giữ nguyên 3 CI/gate thiết yếu trên self-hosted; 15 disabled không bật lại; Dependabot dynamic 422 giữ ngoại lệ nếu chuẩn GitHub-managed. Không reset quota hay tăng ngân sách.
4) Không làm B1 Web legacy protection, B2 rulesets, B3 merge/negative push, không deploy — tất cả thuộc Claude Code CLI trong C2-B canonical.

## S2 — READBACK, KQ
- Chỉ PASS khi readback thật: Pro $4/tháng; NET metered hiện tại $0; Actions budget Account $0 + Stop=ON; không còn GitHub-hosted paid workflow tự chạy; 3 CI thiết yếu không bị phá. Bảng từng product gross/included/net/budget/unknown và workflow active/runner, thay đổi/đường lùi.
- Nếu thiếu chứng cứ, DỪNG với blocker cụ thể, không tiếp tục C2-B. Báo giới hạn thuế/phí FX và usage trước thời điểm tạo budget, không đoán sẽ được hoàn tiền.
- Ghi KQ ở COLLAB/Bảng và cập nhật README/ROADMAP bằng gateway expected_version; bằng chứng chi tiết riêng, công khai chỉ thông tin đã lược. NEXT_TRIGGER=HOST_ACCEPT_COST_THEN_CLAUDE_C2_B.
