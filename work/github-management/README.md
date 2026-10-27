# github-management — cửa vào công việc

**Trạng thái: P71 KQ XONG CÓ GIỚI HẠN C1B-FINALIZE. AD source/main5bc8a3f, CI14/canary0DDL PASS; deploy–rollback chưa đạt (Compose gate + exact old bootstrap DDL). Web Health candidate chạy13 CHECK nhưng auth401, bản sửa d3b1ec8 chưa được chạy do auto-review chặn lượt thứ hai; chưa promote, main728fa1d giữ nguyên. Web và2 audit P66 giữ đạt. POST25/25 footprint0, receipt309, VPS-GHI trả; C1B_SCOPED=FAIL, AUDIT_EXECUTION_VERIFIED=PARTIAL, GLOBAL_GUARD PARTIAL#24. Host xem P71/[C1B-FINALIZE-REPORT.md](C1B-FINALIZE-REPORT.md), xử lý blocker/cấp rõ lượt tiếp trước C3.0→C3→C2→C4.**

Đọc theo đúng thứ tự:
1. AGENTS.md ở root repo (luật hội đồng, vai trò, cổng Owner).
2. work/github-management/COLLAB.md — §0 mục tiêu Owner, Bảng điều khiển, danh sách ghế, câu hỏi quyết định.
3. work/github-management/ROADMAP.md — V0.2 R0–R6, thứ tự và cổng nghiệm thu.
4. work/github-management/KE-HOACH.md — bảng đầu việc Codex, tiêu chí test, nguồn/rollback, đề bài Claude.
5. work/github-management/DRAFT-STANDARD.md — tài liệu tham khảo, không là lệnh RUN.
6. work/github-management/PROMPT.md — **CANONICAL RUN duy nhất** `GHM-C1B-FINALIZE-20261027-03`, Claude P68 ACCEPT, GPT Host P69 READY@88fbbda8c3da2043539d8e41701f21649b3ea64a. Owner chuyển lệnh cho Codex; không dùng bản chat/DRAFT hoặc chữ ký P64 từ RUN cũ.

7. [C1A-RESUME-REPORT.md](C1A-RESUME-REPORT.md) — kết quả CI và bàn giao công khai đã lược thông tin; bằng chứng vận hành lưu riêng.
8. [runner/README.md](runner/README.md) — công cụ cài/gỡ/kiểm runner và trạng thái nghiệm thu.
9. [C1A-S3-CLOSE-REPORT.md](C1A-S3-CLOSE-REPORT.md) — báo cáo lịch sử P40. Kết quả mới nhất là **COLLAB P48**, có hash báo cáo riêng và manifest 47 tệp; giữ nợ/giới hạn toàn hệ tách khỏi C1A scoped.

10. [C1B-FINALIZE-REPORT.md](C1B-FINALIZE-REPORT.md) — KQ mới nhất P71: AD source/CI/canary đạt; deploy và Web audit còn blocker; Guard/receipt/cờ đóng.
11. [C1B-CLOSE-REPORT.md](C1B-CLOSE-REPORT.md) — KQ P66 C1B-CLOSE: Web đạt, 2/3 audit đạt; blocker AD/Web Health, bằng chứng và đường tiếp.
12. [C1B-REPORT.md](C1B-REPORT.md) — KQ P61 kế thừa: phần đạt, blocker từng app/audit, CI/SHA, archive, bằng chứng riêng và đường tiếp.

Mục tiêu duy nhất của việc này: nhiều AI nhận nhiều việc, **viết mã song song trên branch/workspace riêng**, Chief duyệt PR trên nền mới nhất, Owner xem bảng kết quả sáng. R1 dùng Actions trong hạn mức miễn phí với hard budget $0; Owner 25/10 15:18: mọi run đặt trên VPS bằng runner tự host; ưu tiên 1 là CI/CD chạy được.

Một task gốc tại đây; khi sau này mở việc mã thật ở từng repo, Issue/PR của việc là hồ sơ thực thi gắn ID, không sao chép thông tin giữa nhiều nguồn.

Lưu ý: incomex-workspace hiện là repo **public**; mọi file ở đây chỉ chứa chuẩn quy trình/câu hỏi, không chứa secret, token, đường triển khai nhạy cảm, dữ liệu nội bộ. Nếu cần trao đổi bằng chứng nhạy cảm phải chọn nơi private và chỉ dẫn link đã kiểm soát.

**P8:** PROMPT R0+R1 hoàn thiện cho Claude ký SHA; đã bổ sung kiểm các đường ghi VPS theo P7 và S0 kiểm bận trùng phạm vi. READY/RUN chỉ khi Owner giao và điều kiện sạch; không thay GitHub/VPS trong bước soạn.

Đầu vào thảo luận: chỉ đạo Owner ngày 23/10/2026, đề xuất Claude về Pro/rulesets, và đối chiếu tài liệu GitHub chính thức được ghi trong DRAFT-STANDARD.md. DRAFT này là câu trả lời để hội đồng thảo luận; Owner mới là người chốt.
