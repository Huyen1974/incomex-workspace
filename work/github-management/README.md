# github-management — cửa vào công việc

**Trạng thái: GPT Host P6 đã đồng thuận kỹ thuật với Claude P5; đang chờ Owner GO và ký PROMPT R0+R1. CHƯA RUN.**

Đọc theo đúng thứ tự:
1. AGENTS.md ở root repo (luật hội đồng, vai trò, cổng Owner).
2. work/github-management/COLLAB.md — §0 mục tiêu Owner, Bảng điều khiển, danh sách ghế, câu hỏi quyết định.
3. work/github-management/ROADMAP.md — V0.2 R0–R6, thứ tự và cổng nghiệm thu.
4. work/github-management/KE-HOACH.md — bảng đầu việc Codex, tiêu chí test, nguồn/rollback, đề bài Claude.
5. work/github-management/DRAFT-STANDARD.md — tài liệu tham khảo, không là lệnh RUN.
6. work/github-management/PROMPT.md — DRAFT GHM-R0R1 chỉ khảo sát Git và tắt Actions sau hard stop; Claude ký SHA/Host READY/Owner RUN mới thi hành. Pilot P1A cũ SUPERSEDED_UNRUN (lưu lịch sử Git).

Mục tiêu duy nhất của nhánh việc này: tạo cơ chế để nhiều AI được giao nhiều nhiệm vụ, **viết mã song song trong các không gian riêng**, PR an toàn, người duyệt nhập theo thứ tự, sáng Owner xem kết quả. Không dùng GitHub Actions cho việc chạy mã; chưa quyết định nền tảng thử nghiệm.

Một task gốc tại đây; khi sau này mở việc mã thật ở từng repo, Issue/PR của việc là hồ sơ thực thi gắn ID, không sao chép thông tin giữa nhiều nguồn.

Lưu ý: incomex-workspace hiện là repo **public**; mọi file ở đây chỉ chứa chuẩn quy trình/câu hỏi, không chứa secret, token, đường triển khai nhạy cảm, dữ liệu nội bộ. Nếu cần trao đổi bằng chứng nhạy cảm phải chọn nơi private và chỉ dẫn link đã kiểm soát.

**P6:** Claude P5 và GPT Host chốt V0.3 kèm 4 cổng R3/R5/R6, đã soạn PROMPT mới R0+R1 trạng thái DRAFT. Chỉ Codex R0 READ-ONLY có thể cùng lúc Claude Code hoạt động nếu không đụng cùng khu/tệp; GH Actions chỉ tắt sau S1 gate và Owner RUN. Chưa thay mã/quyền/Actions/VPS.

Đầu vào thảo luận: chỉ đạo Owner ngày 23/10/2026, đề xuất Claude về Pro/rulesets, và đối chiếu tài liệu GitHub chính thức được ghi trong DRAFT-STANDARD.md. DRAFT này là câu trả lời để hội đồng thảo luận; Owner mới là người chốt.
