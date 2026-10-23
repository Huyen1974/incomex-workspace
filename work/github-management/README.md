# github-management — cửa vào công việc

**Trạng thái: DRAFT / THẢO LUẬN, chưa kích hoạt phát triển hay deploy.**

Đọc theo đúng thứ tự:
1. AGENTS.md ở root repo (luật hội đồng, vai trò, cổng Owner).
2. work/github-management/COLLAB.md — §0 mục tiêu Owner, Bảng điều khiển, danh sách ghế, câu hỏi quyết định.
3. work/github-management/DRAFT-STANDARD.md — đề xuất bộ quy tắc IT thông dụng để hội đồng phản biện; KHÔNG có hiệu lực vận hành khi chưa duyệt.

Mục tiêu duy nhất của nhánh việc này: tạo cơ chế để nhiều AI được giao nhiều nhiệm vụ, **viết mã song song trong các không gian riêng**, PR an toàn, người duyệt nhập theo thứ tự, sáng Owner xem kết quả. Không dùng GitHub Actions cho việc chạy mã; chưa quyết định nền tảng thử nghiệm.

Một task gốc tại đây; khi sau này mở việc mã thật ở từng repo, Issue/PR của việc là hồ sơ thực thi gắn ID, không sao chép thông tin giữa nhiều nguồn.

Lưu ý: incomex-workspace hiện là repo **public**; mọi file ở đây chỉ chứa chuẩn quy trình/câu hỏi, không chứa secret, token, đường triển khai nhạy cảm, dữ liệu nội bộ. Nếu cần trao đổi bằng chứng nhạy cảm phải chọn nơi private và chỉ dẫn link đã kiểm soát.

**Chưa làm**: cài GitHub Pro, thay quyền, bật/tắt Actions, tạo keys, sửa workflow, chuyển code, chạy ban đêm tự động, đổi luật repo gốc.

Đầu vào thảo luận: chỉ đạo Owner ngày 23/10/2026, đề xuất Claude về Pro/rulesets, và đối chiếu tài liệu GitHub chính thức được ghi trong DRAFT-STANDARD.md. DRAFT này là câu trả lời để hội đồng thảo luận; Owner mới là người chốt.
