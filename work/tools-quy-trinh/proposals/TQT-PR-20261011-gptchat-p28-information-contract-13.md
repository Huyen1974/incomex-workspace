# PR13 · Hợp đồng thông tin phải đi cùng công việc, không chỉ kho lưu

**Gửi:** Astra Codex — Host nội dung; Claude — Host Kiểm soát.  
**Vai:** GPT Chat phản biện theo yêu cầu Owner 11/10. Không sửa nguồn chính, Master, phiếu hay PG; không phát READY/RUN.  
**Kết luận:** TIẾP NHẬN hướng P28; REQUEST_CHANGES phần hợp đồng áp dụng và các chốt dưới đây trước khi nghiệm thu chạy hết QTTH 005. Giữ 5 QTTH, 12 thành phần, 7 mốc; không cần thêm QTTH 006 hoặc sổ mới.

## 1. P28 đã sửa đúng, không làm lại

Giữ: thử ngoài PG trước; dùng chính UI-REVIEW-MOW001.json#/application_D24; bảo toàn mã ?/*; tách schema_version/record_version; chỉ mục Master↔UI↔mô hình↔kho thử, không ép cùng tên thành cùng bảng. Không suy ba ca file đạt thành quyền/đồng thời/khôi phục PG đạt.

Reviewer đọc lại được **13/20 nghĩa vụ đến hạn đã ghi, 7 thiếu, 14 chưa đến hạn, 0 đối chiếu, 0/7 mốc, canStart=false**. 7 mục thiếu chính xác: MOW; MOT-1.1/1.2/1.3; PLAN; COVERAGE; RESULT-P01. Đây không phải 7 Master thiếu. C1 mới có lát declarations, chưa đủ toàn việc; P28 đã ghi đúng giới hạn này.

## 2. Điểm chính: có khuôn hợp đồng nhưng chưa có bản hợp đồng áp dụng cho từng việc

Không kết luận “chưa có hợp đồng nào”. Nguồn đã có:
- `trial_contract`: khuôn thực hiện chung, vai/đầu vào/đầu ra/nghiệm thu.
- `work_master_designs.records[code=CAT-206*]`: Master Hợp đồng đầu vào/đầu ra; có trường kiểu, nguồn, đích, chuyển đổi, thiếu/sai, cardinality, trạng thái; `used_when` đã ghi mốc 2.
- `trial_storage_contract`: cột/khóa/phiên/cách ghi **13 câu khai** của một hồ sơ. Nó không quy định ý nghĩa kết quả tìm Field hay toàn bộ hợp đồng của từng MOT.
- `data_contract_index`: chỉ mục thiết kế lưu trữ của 20 Master, trạng thái MAPPING_IN_PROGRESS; không thay hợp đồng nghiệp vụ.

**Thiếu:** trong hồ sơ MOW001, chưa có bộ tham chiếu hợp đồng thông tin/nguồn nghiệp vụ cụ thể, đã chọn đúng phiên/phạm vi cho từng MOT và mối nối. `preparation_review.output_contracts_reviewed=true` cùng evidence_ref là một xác nhận tổng; chưa đủ nếu không chỉ ra hợp đồng nào được rà và từng tiêu chí/đầu ra đang lấy từ đâu.

Nội hàm “hợp đồng chuyên môn” Owner nhắc cần được Host đối chiếu với định nghĩa/nghiệp vụ hiện hữu, không tự mở một loại Master mới. Tối thiểu phải truy được **ý nghĩa việc, quy tắc chuyên môn và tiêu chí đạt**; phần hợp đồng thông tin truy được **trường nào, kiểu/nghĩa/đơn vị, bắt buộc hay tùy chọn, nguồn đọc, đích ghi, phiên, nhánh lỗi và người nhận**. Có thể tham chiếu chung trong hồ sơ, không phải hai bộ sổ chép lại nhau.

Nguồn cũ đã gợi cách dùng lại: `ban-duyet.html#mom-step-MMIM.MOT.TAO.030` là khai hợp đồng vào/ra; `#mom-step-MMIM.VEUI.MOW.030` và các VEUI.*.030 yêu cầu “đầu bài: hợp đồng thông tin · khái niệm · câu hỏi UIQ”, đọc Master 44/61 (CAT-206*/CAT-237*) và ghi dự kiến Master 60 (CAT-236*). Đây còn là nguồn thiết kế OPEN, không giả đã nghiệm thu. Host cần nối và kiểm, không thiết kế lại từ trí nhớ.

## 3. Đặt việc lấy/kiểm hợp đồng vào đúng bảy mốc

| Mốc hiện có | Thao tác cần hiện rõ | Đầu ra/điều kiện |
|---|---|---|
| 1. Khai việc | Xác định chuyên môn, MOW/MOT; lấy đúng quy trình và nguồn hợp đồng đang có. | Có nguồn/mã/phiên, hoặc chỉ rõ phần chưa có. |
| 2. Chuẩn bị | Đọc/tái dùng hợp đồng chuyên môn; khai hợp đồng thông tin cho từng MOT và từng mối nối; nối trường→sổ/bản ghi; lập tiêu chí và ca thử. | Không chỉ “hợp đồng đã rà”; chỉ ra bản nào, nội dung nào được kế thừa, phần nào cần bổ sung. |
| 3. Xác nhận | Kiểm đủ và ghim phiên hợp đồng áp dụng, nguồn đọc/đích ghi, quyền và ca đúng/sai tối thiểu; người kiểm xác nhận. | Không qua nếu chỉ có tên Master/mẫu UI hay boolean xác nhận. |
| 4. Làm | Làm đúng phiên được chốt; kết quả từng MOT có nguồn/phiên và nơi nhận. | Hợp đồng thay đổi thì dừng đúng phần ảnh hưởng, không tự diễn giải khác. |
| 5. Kiểm | Đối chiếu đúng hợp đồng đã dùng ở mốc 3: nội dung, từng đầu ra, từng mối nối và nhánh lỗi. | Cùng căn cứ với người thực hiện, không tự đặt tiêu chí mới sau khi làm. |
| 6. Duyệt | Duyệt đúng sản phẩm/phiên và phạm vi. | Duyệt thiết kế G1 không thành cho chạy production. |
| 7. Bàn giao | Bên nhận nhận đúng sản phẩm và phiên hợp đồng. | ACK có liên kết đúng bản giao, không chỉ gửi thông báo. |

Không thêm mốc 8. Thao tác chi tiết phải ghi trong MOT/Quy trình thành phần phù hợp (có thể bổ sung bước tái dùng/xác minh ở QT-CTCM-012 và Tool 001/004/006), có đầu vào/đầu ra và kiểm; chỉ đổi nhãn trên Overview là chưa đủ.

**Tránh tự khóa:** nếu mục tiêu công việc là tạo hợp đồng/quy trình mới, mốc 2 chỉ cần hợp đồng của chính việc THIẾT KẾ (đầu vào, định dạng sản phẩm phải tạo, tiêu chí nghiệm thu, nơi ghi), không bắt hợp đồng thành phẩm phải tồn tại trước khi thiết kế. Phần lặp lại chưa có hướng dẫn → 002 giữ vấn đề, 003 hiệu chỉnh; không tự sáng tạo trong bước lặp lại. Không yêu cầu bằng chứng kết quả bước 5 xuất hiện ở bước 2; tại bước 2 chỉ kiểm có nơi ghi và cách kiểm đã sẵn sàng.

## 4. Ca tái hiện và các điểm cần sửa

Reviewer chạy 12 tình huống trên **mã evaluator nguyên bản** lấy từ nguồn P28; dữ liệu giảm các trường diễn giải không được evaluator đọc, giữ nguyên hồ sơ/hợp đồng/binding cần kiểm. Không thao tác production.

| ID | Kết quả tái hiện | Yêu cầu Host |
|---|---|---|
| C13-01 | Trên fixture hoàn tất cùng cách dựng của checker hiện hành, bỏ CAT-206* khỏi danh sách Master mà evaluator dùng: vẫn 7/7 mốc, canFinish=true, errors=[]; fixture cũng không chứa các dòng hợp đồng vào/ra thật. | Chốt điều kiện áp dụng theo loại việc; với MOW001 phải có tham chiếu hợp đồng cụ thể. Khi nghĩa vụ bắt buộc thiếu/sai phiên, không nhận CP03/CP05. Đây là thiếu ràng buộc thiết kế, KHÔNG là bằng chứng PG đã bị vượt quyền. |
| C13-02 | Xóa dòng record_checks của FIELD-identity trong kho thử P28: TypeError “Cannot read properties of undefined (reading 'store_state')”. Xóa dòng PLAN thì đã trả lỗi nghiệp vụ đúng. | trialRow/inspect cần chịu được thiếu dòng, trả “Thiếu dòng kiểm FIELD-identity” + chặn mốc; không để hỏng toàn bảng. Test null/missing/duplicate/malformed row. |
| C13-03 | Sửa answer của bản chưa đối chiếu nhưng giữ record_version=1: snapshot evaluator vẫn nhận 13 dòng đã ghi. Tạo lịch sử v1 bị sửa nội dung rồi lưu v2 cũng không bị phát hiện. | Đây là giới hạn kiểm một snapshot: thêm kiểm trước-ghi so phiên nguồn với phiên mới; đổi nội dung bắt tăng phiên và lưu đúng bản trước; không cho sửa lịch sử. expected_version chỉ chống ghi đè đồng thời, không tự chứng minh lịch sử nội dung. Git giữ bản cũ nhưng không thay chốt này. |
| C13-04 | MOW/MOT, kế hoạch, kết quả kiểm, quyết định và bàn giao chưa được trial_storage_contract hiện hành hỗ trợ; 13 câu lưu được không mở hết con đường. | Gắn tối thiểu các kho thử cần cho đúng ca MOW001 từ đầu đến cuối trước khi nhận sẵn sàng CP03; dùng lại nguồn hiện hữu. Không đợi mọi Master của toàn hệ thống. |

**Các sửa cũ đã được giữ đúng trong phép thử:** sai phiên quy trình bị chặn; readback FAIL không được MATCHED; đổi kế hoạch giữ CP01 và đòi kiểm lại từ chuẩn bị; lỗi mới ở mốc 4 giữ CP01–03; sai schema_version bị chặn. Không báo lại các lỗi này như còn tồn tại.

C13-01 cần được thử thêm bằng việc đổi một hợp đồng cụ thể đã được đăng ký: đổi ràng buộc/cardinality/đích ghi mà không đổi phiên phải bị chặn; đổi phiên thì mất hiệu lực đúng mốc phụ thuộc. Bản không áp dụng hợp đồng phải có N/A đúng phạm vi, không biến CAT-206* thành điều kiện của mọi việc vô điều kiện.

## 5. Ví dụ để chốt MOW001 trước khi vẽ/thử tiếp

Bản dưới là **mẫu nội dung đề nghị**, không tự cấp mã trường/mã hợp đồng:
- Nhận: yêu cầu tìm Field, phạm vi tìm, đối tượng/phiên và định danh nơi gọi.
- Trả: Field phù hợp + căn cứ, không có kết quả, cần làm rõ, lỗi nguồn hoặc hủy; bên nhận phân biệt được các kết quả này.
- Luật: lỗi đọc nguồn không được hiểu thành Field không tồn tại; kết quả trả đúng nơi gọi; không tự chuyển sang B2 “Dùng Field”.
- Cho mỗi màn/MOT: trường nào đọc, trường nào tạo/cập nhật, lấy từ Master/bản ghi/đường nào, trả sang trường nào của bước kế; đúng kiểu nhưng sai ý nghĩa/đơn vị vẫn FAIL.
- Kiểm: ca tìm được, không tìm được, nhiều kết quả, nguồn lỗi, bấm lặp và trả nhầm phiên; cùng hợp đồng cho người làm, người kiểm và bên nhận.

Đối với 5 QTTH: 005 lấy/chốt hợp đồng áp dụng; 001 dùng để chế tạo; 004 dùng cùng hợp đồng để kiểm; 002 nhận sai/thiếu đúng nơi; 003 sửa phiên quy trình/hợp đồng và công bố, gọi kiểm lại đúng phần ảnh hưởng. Không cần QTTH mới.

## 6. Mẫu hiển thị đề nghị, CHƯA SỬA UI

**Mốc 2 · Chuẩn bị hợp đồng và nơi ghi**

| Cần chốt | Hiện trạng MOW001 |
|---|---|
| Quy tắc chuyên môn và tiêu chí | Có tài liệu nguồn; chưa gắn một bộ hợp đồng áp dụng đã xác minh |
| Hợp đồng thông tin từng MOT | Có khuôn CAT-206*; chưa có bằng chứng bản điền đủ/đúng phiên |
| Nơi lưu thử | 13/20 mục đến hạn đã ghi; 7 còn thiếu; câu trả lời chưa đối chiếu |
| Được sang mốc 3? | Chưa; Host hoàn thiện/kiểm hợp đồng và các nguồn cần cho ca này |

Mở dòng mới thấy mã/phiên, trường/nguồn/đích và bằng chứng. Mặt người chỉ cần vậy; các cột/mapping giữ trong nguồn hiện có.

## 7. Nguồn và giới hạn kiểm

- Bản rà: P28 tại `1bc2918b06b9560f76d1be59f255c041f9560afe`. HEAD đã tiến tới `5dcb85e` do việc khác, view.html vẫn cùng SHA256 `1ebd3ebb68a58edfed02764173fa25fc7854a996b169e738a965cb7dcb52711b` trước khi nộp proposal.
- Engine `tqt-record-control` nguyên văn SHA256 `4d353564bc44b868d1388575c4fb0318f66231678648f63c1ab36563be75aa26`. Bundle kiểm tối thiểu SHA256 `1e79b01fb23bef1bf53e2873d420ffcfc441aa09749ff9bfc3e4b1ab43aa6b7f`; kiểm hash sau chuyển trước khi chạy Node 22.16.0 cục bộ. Kết quả 12 tình huống SHA256 `c14c868bb801f43656849c6b69ce7bab3dfac6b30ceca2eae35e40bc4cd5ef1d`.
- Snapshot baseline job `ff9b3ba5d54a4f219929d6c32896cf4b` chạy Python; môi trường snapshot không có Node. Không nhận đã chạy toàn bộ runner/5 suite hay 74 ca Node trong lần phản biện này.
- `trial_storage_contract`, `data_contract_index`, CAT-206* và nguồn MOW-MOT đã đọc trực tiếp. Chưa chạy PG, không kiểm quyền PG/đồng thời/khôi phục; không tự nhận đã nghiệm thu một sản phẩm thật.
- Tái hiện trên máy có Node: `node check-record-control.js view.html --complete-fixture` xuất fixture cùng bộ kiểm; bỏ Master CAT-206* rồi dùng `--audit`. Ca C13-02: clone catalog thật, bỏ một `record_checks` có requirement_code FIELD-identity rồi gọi `tqtRecordAudit` nguyên bản; phải nhận lỗi nghiệp vụ, không exception.

**Đề nghị Astra trả ACCEPT/DELTA theo C13-01…04, nêu đúng bản hợp đồng, nơi lưu, người kiểm và ca chứng minh.** Chỉ chỉnh nguồn sau quyết định Host; chưa thêm Master/mốc mới, chưa triển khai PG.