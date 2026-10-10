# PR11 — Hội đồng đánh giá câu hỏi Q1 và Q2 của Owner

**TQT-PROPOSAL:** TQT-PR-20261010-gptchat-two-questions-record-review-11
**Scope:** Over view tools-quy-trinh; Quy trình tổng hợp MOW-TH-005; MOW001/G1/application_D24.
**Vai:** GPT Chat sửa mặt Overview do Owner trực tiếp yêu cầu. Host nội dung là Astra Codex; Host Kiểm soát là Claude. Không sửa quy trình/Master/phiếu, không phát RUN.

## Đúng hai câu hỏi phải trả lời

**Q1 — Mỗi việc theo TH05 phải qua những checkpoint nào, hiện ở mốc nào?** 7 mốc là đường đi chung; bảng tiến độ là biểu hiện của một application. Hội đồng hãy đánh giá đủ/sai 7 mốc trước khi coi quy trình đã chốt. Chưa thêm TH06.

**Q2 — Từng thông tin của việc phải ghi vào sổ nào, đã có sổ chưa, đã ghi chưa?** 19 Master chung của hệ thống KHÔNG trả lời Q2. Mỗi đầu ra/câu trả lời/bằng chứng từ S1–S6 và P01–P05 cần địa chỉ sổ + bản ghi đúng code/phiên + kết quả đọc lại. Master/phiếu/nhật ký hiện có gọi chung là sổ, nhưng phải phân biệt sổ có và dữ liệu đã ghi.

## Câu hỏi bắt buộc cho Codex/Claude (ACCEPT hoặc REQUEST_CHANGES từng câu)

- **H1:** Có bỏ sót thông tin/đầu ra phải ghi từ 7 mốc và các P01–P05 hay không? Kiểm cả nhánh lỗi, từ chối, không áp dụng, giao nhận.
- **H2:** Từng dòng có sổ đích thực, mã bản ghi đúng MOW/MOT/phiên, người ghi, quyền ghi/đọc và bằng chứng đọc lại không? Cần chứng minh bằng một ca thật, không đủ nếu chỉ có tên Master.
- **H3:** Đã tách chính xác 5 trạng thái: chưa có sổ; có sổ chưa ghi; ghi rồi chưa kiểm; ghi và kiểm đúng; chưa phát sinh hoặc N/A có lý do chưa?
- **H4:** Chưa có sổ/địa chỉ ghi/phiên sai thì ai xử lý, ghi issue vào đâu, chặn mốc nào, quay lại bước nào? Không cản chuẩn bị; không cho qua S3 thiếu đầu vào/bằng chứng bắt buộc.
- **H5:** Phiên AI mới có trả lời được Q1/Q2 từ một hồ sơ MOW001/G1, không hỏi người cũ, không lấy mô tả đầu ra trong kế hoạch làm chứng cứ đã làm không?

## Bằng chứng hiện trạng để phản biện

- MOW001 có Master MOW, 3 MOT chưa được khớp hoàn chỉnh trong Master MOT.
- 13/13 mục khai trong application_D24, 0/13 được kiểm bằng chứng.
- Kế hoạch P01–P05 đều TODO, chưa có kết quả thực; start_confirmation=PENDING.
- history có một DECLARE; không có sự kiện làm. Test, hai đầu nối chưa kiểm; quyết định và ACK trống vì chưa đến mốc.
- Issue_ref null là bình thường khi chưa có lỗi mới. Sổ lỗi gốc có đường dẫn nhưng chưa thử quyền ghi/đọc.
- Bảng Q2 mới là mặt rà từ application_D24, chưa phải máy runtime tự phát hiện nghĩa vụ ghi bị bỏ sót cho mọi việc.

Yêu cầu Host Codex nhận phản biện: chỉ đúng dòng nào còn mơ hồ, dùng lại sổ nguồn nào, cần bổ sung trường/mapping nào tại nơi có thẩm quyền; khi kiểm được đầu ra thực mới chuyển PASS. Claude đối chiếu với mục tiêu A0/§0. Ghi kết luận ACCEPT/REQUEST_CHANGES kèm bằng chứng; không mở thêm sổ hoặc Master theo suy đoán.
