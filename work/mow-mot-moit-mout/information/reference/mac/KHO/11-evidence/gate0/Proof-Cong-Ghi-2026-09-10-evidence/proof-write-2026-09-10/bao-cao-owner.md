# Báo PM — Proof cổng ghi, 10/09/2026

**Đã thực thi: cổng ghi PASS trong lát cắt lab, 66/66 ca; nộp PM xem xét, chưa tự nghiệm thu A/B.** Hai lỗi cũ đều tái hiện trước sửa rồi được chặn ở đường mới.

- **Chọn một cổng chung:** extension chuẩn Directus, endpoint + hook trong cùng bundle; dùng lại ItemsService/quyền/audit, Joi có sẵn, transaction/khóa/FK của PostgreSQL. Contract/profile lấy từ catalog PG; caller không được đổi profile để né kiểm.
- **Code thêm:** một component lab, 163 dòng JS lõi +2 dòng app export rỗng và metadata; 50 dòng SQL quan hệ/constraints. Không thêm dependency, fork, engine hay code riêng từng Field/MOW; harness và công chuẩn bị được kê riêng. Production triển khai0.
- **Đã chứng minh:** ghi/read-back hợp lệ, không nhân Field; chặn contract giả/sai version/unit/target/scope, note-only thiếu duration, spoof và các bypass đã thử. Hai writer cùng revision chỉ một commit (**200/409**); retry trả đúng kết quả cũ, khác payload409. Rollback cưỡng bức giữ nguyên dữ liệu/ref/audit. Lỗi nạp bundle làm app lab dừng; khôi phục xong guard/replay vẫn đạt.
- **Phiên mới:** Agent độc lập đọc checkpoint và catalog/trạng thái thật, tự ghi tiếp đúng một record **revision2→3**, không dựng lại object; root đối chiếu PG/audit xác nhận.
- **Còn thiếu:** `main` là Draft có thể sửa, chưa immutable release/publish. Native versions đã đóng cho business identities. **UI NOT RUN**: UForm còn submit inbox, thiếu nối action/revision/conflict/read-back; đã kèm request/response thực. **Runtime NOT RUN**, chưa cài pg-boss. Quản trị catalog production và full authoring/security chưa được chứng minh.
- **Lab đã dọn** đúng ownership; năm demo giữ trạng thái tiến trình và HTTP smoke. API hoạt động; full health503 do email bị chặn chủ ý, không gọi full health PASS. Không sửa production/nâng stack.

SSOT cập nhật **v1.6.12** một lần sau evidence, có backup/snapshot đúng hash. Factory DONE; FEAS PARTIAL; Gate0 DOING; O1–O3 NOT VERIFIED; R1 chưa mở. Tổng công người/LLM/debug NOT MEASURED, không suy tỷ lệ98%.

**Đề nghị PM:** review/nhận riêng proof cổng này; nếu nhận, giao bước nối UI hiện hữu trong cùng lát cắt. Chi tiết, từng ca, HTTP/PG, source/hash, corrections và cleanup có trong gói evidence.
