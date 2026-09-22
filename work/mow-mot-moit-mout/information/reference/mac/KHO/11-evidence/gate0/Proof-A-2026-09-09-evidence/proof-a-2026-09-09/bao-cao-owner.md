# Proof A · Kết quả thực thi 09/09/2026

**SUBMITTED / PM REVIEW · PARTIAL.** Đã chạy bốn phép đo trên PostgreSQL tạm riêng, không đổi hệ hiện hữu.

| Corpus | A0 · Exact | A1 · Lexical/mô tả |
|---|---|---|
| 14 concept nháp | 8/12 (66.7%) · 3.0 ms | 12/12 (100.0%) · 5.4 ms |
| 14 concept + 1.438 metadata | 8/12 (66.7%) · 10.8 ms | 12/12 (100.0%) · 79.9 ms |

Mỗi ô: **hit trong top5 / 12 ca positive E06** và median truy vấn ấm. Cấu hình giữ nguyên; mục tiêu đã gán nhãn đều ở hạng 1 với A1, không đổi khi thêm nhiễu. Đây là bài hồi quy đã biết; chưa có nhãn đầy đủ cho metadata mở rộng.

**Chưa đủ cho auto-reuse:** “ngày sửa đổi” vẫn trả về “Ngày lập” từ câu mô tả phủ định; trạng thái runtime/Definition và giờ/phút còn cần contract. Admission thật chưa chạy, nên false-reuse/false-new/NEEDS_DECISION = **NOT MEASURED**. Sáu ca guard tổng hợp đạt 6/6 chỉ kiểm phép so trong harness. Concept thật có contract_ref 0/14; chưa thể tự điền bằng suy đoán.

**Công người/LLM:** lookup dùng 0 LLM calls/tokens; chuẩn bị do Codex thực hiện, chưa đo tổng token/thời gian người. Không yêu cầu Owner gán nhãn thêm; không suy thành đạt mục tiêu 98% AI.

**Đề nghị PM:** tiếp tục lexical để tìm ứng viên cho pilot, rồi kiểm phần authoring/contract còn thiếu; chưa có lý do cài vector từ bộ này. Chưa đo intent→declaration→validator→PG read-back/checkpoint→test version, UI cùng ID/version hoặc runtime. Toàn Proof A chưa đóng; B/C chưa chạy; Factory DONE, FEAS PARTIAL, Gate0 DOING.

Đã dọn container/network/volume/credential lab; năm container demo không restart/thay thế. [Bằng chứng và cách tái chạy](./README.md), [từng ca](./case-results.json), [kết quả máy đọc](./summary.json).

SSOT đã cập nhật một lần lên **v1.6.10**, có backup nguyên bản v1.6.9 và kiểm hash/read-back. [Dấu vết cập nhật](./ssot-update.json).
