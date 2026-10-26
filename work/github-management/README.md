# github-management — cửa vào công việc

**Trạng thái: Claude P63 ACCEPT C1B-CLOSE có sửa — gốc: main chưa là nguồn bản đang chạy (Web chạy Nuxt 4.5.2, main Nuxt 3) ⇒ PARITY trước deploy; 3 audit quyết sẵn; C3 không song song; cổng máy GitHub vào C3.0/C2. Chờ GPT Host READY@b467fddfb8d798c8323b03450da34396b741354e rồi Owner giao Codex. Runtime cũ healthy, 0 RUN active.**

Đọc theo đúng thứ tự:
1. AGENTS.md ở root repo (luật hội đồng, vai trò, cổng Owner).
2. work/github-management/COLLAB.md — §0 mục tiêu Owner, Bảng điều khiển, danh sách ghế, câu hỏi quyết định.
3. work/github-management/ROADMAP.md — V0.2 R0–R6, thứ tự và cổng nghiệm thu.
4. work/github-management/KE-HOACH.md — bảng đầu việc Codex, tiêu chí test, nguồn/rollback, đề bài Claude.
5. work/github-management/DRAFT-STANDARD.md — tài liệu tham khảo, không là lệnh RUN.
6. work/github-management/PROMPT.md — **DRAFT cho lượt khép C1B** RUN_ID `GHM-C1B-CLOSE-20261026-02`, Claude P63 đã sửa; **CHƯA READY / Owner RUN, không thi hành** cho tới khi Host ký READY@b467fddfb8d798c8323b03450da34396b741354e. Lệnh P58/C1B-01 đã KQ P61 và chỉ còn lịch sử trong Git; không lấy READY cũ cho DRAFT mới.

7. [C1A-RESUME-REPORT.md](C1A-RESUME-REPORT.md) — kết quả CI và bàn giao công khai đã lược thông tin; bằng chứng vận hành lưu riêng.
8. [runner/README.md](runner/README.md) — công cụ cài/gỡ/kiểm runner và trạng thái nghiệm thu.
9. [C1A-S3-CLOSE-REPORT.md](C1A-S3-CLOSE-REPORT.md) — báo cáo lịch sử P40. Kết quả mới nhất là **COLLAB P48**, có hash báo cáo riêng và manifest 47 tệp; giữ nợ/giới hạn toàn hệ tách khỏi C1A scoped.

10. [C1B-REPORT.md](C1B-REPORT.md) — KQ P61 hiện hành: phần đạt, blocker từng app/audit, CI/SHA, archive, bằng chứng riêng và đường tiếp.

Mục tiêu duy nhất của việc này: nhiều AI nhận nhiều việc, **viết mã song song trên branch/workspace riêng**, Chief duyệt PR trên nền mới nhất, Owner xem bảng kết quả sáng. R1 dùng Actions trong hạn mức miễn phí với hard budget $0; Owner 25/10 15:18: mọi run đặt trên VPS bằng runner tự host; ưu tiên 1 là CI/CD chạy được.

Một task gốc tại đây; khi sau này mở việc mã thật ở từng repo, Issue/PR của việc là hồ sơ thực thi gắn ID, không sao chép thông tin giữa nhiều nguồn.

Lưu ý: incomex-workspace hiện là repo **public**; mọi file ở đây chỉ chứa chuẩn quy trình/câu hỏi, không chứa secret, token, đường triển khai nhạy cảm, dữ liệu nội bộ. Nếu cần trao đổi bằng chứng nhạy cảm phải chọn nơi private và chỉ dẫn link đã kiểm soát.

**P8:** PROMPT R0+R1 hoàn thiện cho Claude ký SHA; đã bổ sung kiểm các đường ghi VPS theo P7 và S0 kiểm bận trùng phạm vi. READY/RUN chỉ khi Owner giao và điều kiện sạch; không thay GitHub/VPS trong bước soạn.

Đầu vào thảo luận: chỉ đạo Owner ngày 23/10/2026, đề xuất Claude về Pro/rulesets, và đối chiếu tài liệu GitHub chính thức được ghi trong DRAFT-STANDARD.md. DRAFT này là câu trả lời để hội đồng thảo luận; Owner mới là người chốt.
