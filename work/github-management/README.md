# github-management — cửa vào công việc

**Trạng thái: P54 C1B KQ DỪNG tại S0 — chưa chứng minh cổng main/workflow hợp lệ cho Codex theo PROMPT P53. 0 mutation main/deploy/audit, 0 RUN active; VPS-GHI không nhận/giữ. Host xác minh capability hiện hữu rồi Owner giao tiếp cùng RUN; sáu safety P50/C1A giữ nguyên. Chi tiết và NEXT_TRIGGER tại COLLAB P54.**

Đọc theo đúng thứ tự:
1. AGENTS.md ở root repo (luật hội đồng, vai trò, cổng Owner).
2. work/github-management/COLLAB.md — §0 mục tiêu Owner, Bảng điều khiển, danh sách ghế, câu hỏi quyết định.
3. work/github-management/ROADMAP.md — V0.2 R0–R6, thứ tự và cổng nghiệm thu.
4. work/github-management/KE-HOACH.md — bảng đầu việc Codex, tiêu chí test, nguồn/rollback, đề bài Claude.
5. work/github-management/DRAFT-STANDARD.md — tài liệu tham khảo, không là lệnh RUN.
6. work/github-management/PROMPT.md — `GHM-C1B-CODEX-BASELINE-MANUAL-CD-20261026-01` cho **CODEX**, đã READY@cef559c90506b7fac5b66bfc847f5f58f7e6a680 trong COLLAB P53. PROMPT C1B cũ giao Claude Code CLI là SUPERSEDED_UNRUN; không dùng. Owner chuyển CODEX RUN khi VPS-GHI trống, Codex kiểm Guard/quyền trước mutation.

7. [C1A-RESUME-REPORT.md](C1A-RESUME-REPORT.md) — kết quả CI và bàn giao công khai đã lược thông tin; bằng chứng vận hành lưu riêng.
8. [runner/README.md](runner/README.md) — công cụ cài/gỡ/kiểm runner và trạng thái nghiệm thu.
9. [C1A-S3-CLOSE-REPORT.md](C1A-S3-CLOSE-REPORT.md) — báo cáo lịch sử P40. Kết quả mới nhất là **COLLAB P48**, có hash báo cáo riêng và manifest 47 tệp; giữ nợ/giới hạn toàn hệ tách khỏi C1A scoped.

Mục tiêu duy nhất của việc này: nhiều AI nhận nhiều việc, **viết mã song song trên branch/workspace riêng**, Chief duyệt PR trên nền mới nhất, Owner xem bảng kết quả sáng. R1 dùng Actions trong hạn mức miễn phí với hard budget $0; Owner 25/10 15:18: mọi run đặt trên VPS bằng runner tự host; ưu tiên 1 là CI/CD chạy được.

Một task gốc tại đây; khi sau này mở việc mã thật ở từng repo, Issue/PR của việc là hồ sơ thực thi gắn ID, không sao chép thông tin giữa nhiều nguồn.

Lưu ý: incomex-workspace hiện là repo **public**; mọi file ở đây chỉ chứa chuẩn quy trình/câu hỏi, không chứa secret, token, đường triển khai nhạy cảm, dữ liệu nội bộ. Nếu cần trao đổi bằng chứng nhạy cảm phải chọn nơi private và chỉ dẫn link đã kiểm soát.

**P8:** PROMPT R0+R1 hoàn thiện cho Claude ký SHA; đã bổ sung kiểm các đường ghi VPS theo P7 và S0 kiểm bận trùng phạm vi. READY/RUN chỉ khi Owner giao và điều kiện sạch; không thay GitHub/VPS trong bước soạn.

Đầu vào thảo luận: chỉ đạo Owner ngày 23/10/2026, đề xuất Claude về Pro/rulesets, và đối chiếu tài liệu GitHub chính thức được ghi trong DRAFT-STANDARD.md. DRAFT này là câu trả lời để hội đồng thảo luận; Owner mới là người chốt.
