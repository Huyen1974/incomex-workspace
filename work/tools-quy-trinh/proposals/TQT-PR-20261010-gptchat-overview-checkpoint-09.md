# PR09 · Một bảng checkpoint nhìn thấy ngay trong Over view

TQT-PROPOSAL: TQT-PR-20261010-gptchat-overview-checkpoint-09
TARGET: MOW-TH-005@1.1-design; catalog.work_form / application_preview; #tqt-work-board.
TESTED: Đọc D24/P23, D25/P24; mở Over view và chi tiết005; đối chiếu application_D24 với preview; chạy check-overview-consistency.py. Chỉ đọc và ghi proposal riêng; không sửa nguồn chính/sổ của task.
OBSERVED: Codex đã thêm khung 13 câu và phiếu, nhưng mặt Owner mới là bản tóm tắt một ca; chưa có bảng checkpoint trọn vòng và danh sách nơi ghi được kiểm. Yêu cầu Owner chưa đạt ở mặt nhìn.
PROPOSED_CHANGE: Giữ005 là quy trình chung; thay workBoard bằng một bảng kiểm hiển thị sẵn, lấy dữ liệu từ đúng phiếu. Không thêm TH06 chỉ để chữa phần hiển thị.

## 1. Kết luận rõ ràng

005 đã mở rộng đúng vai “khuôn thực hiện, lập kế hoạch, kiểm, duyệt và bàn giao mọi việc”. Bảng Owner cần là **bảng checkpoint của một lần áp dụng005**, không phải quy trình thứ6, không phải sổ thứ hai.

Một mẫu bảng chung; mỗi việc/lần làm có dữ liệu riêng theo application_id. Overview chọn việc rồi hiện cùng mẫu. Hiện mới nối một mẫu MOW001/G1, chưa được nói mọi việc đã được giám sát tự động. Việc con kế thừa phiếu, không tạo cửa005 lồng vô hạn.

Hiện renderer `workBoard` chỉ hiện tên MOW001 viết cứng, trạng thái Chuẩn bị, lý do và người làm tiếp. 13 mục cùng kế hoạch nằm trong `<details id="tqt-work-form">` đóng mặc định. Dãy bảy tên mốc chỉ là văn bản, không cho biết mốc nào đã đạt, căn cứ, nơi ghi hoặc có bỏ bước không. Đây là thiếu hiển thị thật, không chỉ Owner chưa tìm thấy nút.

## 2. Mặt Owner: một bảng duy nhất, không gập phần cần kiểm

Đầu bảng: **Mã việc + tên · mã lần làm · phạm vi G1/G2/G3 · quy trình/phiên · bước hiện tại · ĐƯỢC/CHƯA ĐƯỢC THỰC HIỆN · ai làm tiếp · cập nhật lúc nào**. Không viết cứng MOW001 trong renderer. Khi nguồn/phiên chưa xác minh, hiển thị cần kiểm lại thay xanh.

| Mốc kiểm của005 | Phải nhìn thấy ngay | Nơi ghi cần chỉ rõ | MOW001 hiện tại |
|---|---|---|---|
| 1. Khai việc | Mã/tên/Master; mục tiêu/phạm vi; nguồn vào và nơi nhận | Master + phiếu khai việc + ca nối vào/ra | Đã khai, chưa kiểm |
| 2. Chuẩn bị | Đầu vào/quyền/công cụ; đủ câu; kế hoạch; có mọi nơi ghi | Phiếu đủ/thiếu; kế hoạch; địa chỉ sổ/bằng chứng | Đang chuẩn bị; 13 mục đã khai, 0 mục có bằng chứng kiểm |
| 3. Xác nhận đủ | Ai xác nhận điều kiện và đúng phiên kế hoạch | start_confirmation + bằng chứng/phê duyệt bắt đầu | Chưa xác nhận; chưa được sang S3 |
| 4. Thực hiện | Đang ở MOT nào, làm đúng kế hoạch/nhánh nào, sản phẩm gì | Nhật ký lần làm/MOT + kết quả và phiên nguồn | 5 việc kế hoạch đều TODO |
| 5. Kiểm | Người kiểm; sản phẩm và hai đầu nối đạt/thiếu; hồ sơ cần sửa | Ca kiểm + kết quả + bằng chứng; sổ lỗi đúng nguồn | Chưa kiểm; hai đầu nối đều NOT_TESTED |
| 6. Duyệt | Người có quyền, quyết định, phạm vi/phiên được duyệt | Quyết định nghiệm thu/cho sử dụng | Chưa trình; chỉ G1, không phải duyệt production |
| 7. Bàn giao/xong | Đúng người nhận, đúng kết quả/phiên, xác nhận nhận | Biên nhận/ACK + lịch sử kết thúc | Chưa có ACK, chưa xong |

Bảy dòng là **mốc kiểm chiếu từ sáu MOT hiện có**, không thêm bảy quy trình/MOT: dòng1→S1; dòng2 và3→S2; dòng4→S3; dòng5→S4, lỗi đi S5 rồi quay lại; dòng6 và7→S6. Giữ mã MOT nhỏ cạnh từng mốc. 13 câu có ánh xạ tới dòng; không thay/bỏ câu vì rút giao diện.

Các cột tối thiểu: **Mốc/cần kiểm · Nơi ghi và tình trạng nơi ghi · Kết quả/bằng chứng · Người giữ/việc tiếp**. Chỉ nội dung dài, danh sách ca và lịch sử mới thu gọn. Không đặt trạng thái đủ/thiếu và danh sách nơi ghi sau nút mở.

## 3. “Các quyển sổ”: tên chức năng và đường ghi thật, không phải tám file mới

Cần công khai tám nơi ghi theo chức năng ngay trong cột bảng; nhiều nơi có thể là các mục của cùng một phiếu:
1. Mã/tên/phạm vi công việc → Master tương ứng + phiếu lần áp dụng.
2. Đầu vào, điều kiện, câu hỏi, hai đầu nối → declarations và bộ đáp án/ca áp dụng.
3. Kế hoạch → plan_ref, thứ tự/phụ thuộc/người làm/đầu ra.
4. Thực hiện/kết quả → nhật ký MOT, phiên sản phẩm và output_ref.
5. Sai/thiếu/yêu cầu bổ sung → issue_register_ref + issue_ref nếu đã phát sinh; lỗi sản phẩm giữ sổ MOW, lỗi quy trình giữ sổ TQT.
6. Kiểm thử → ca/tiêu chí/kết quả/bằng chứng, đúng application_id và đối tượng/phiên.
7. Phê duyệt → start_confirmation khi bắt đầu; release/decision_ref cho nghiệm thu hoặc sử dụng, phân biệt hai lần duyệt.
8. Bàn giao và vòng đời → recipient/return_to, ack_ref và history.

Mỗi nơi ghi phải hiển thị **tên + mã/đường dẫn hoặc JSON pointer + người được ghi/kiểm + trạng thái kiểm nơi ghi**. Tách: đã khai đường dẫn / đã xác minh tồn tại và đọc / đã xác minh quyền ghi-đọc lại. Có dòng chữ tên file không phải bằng chứng nơi ghi đã sẵn sàng. Cách kiểm ghi phải đúng quyền/môi trường, không chèn dữ liệu thử tùy tiện vào production.

Không buộc mở issue giả: issue_ref=null là hợp lệ khi chưa phát sinh lỗi, nhưng nơi tiếp nhận lỗi phải được khai và kiểm trước bắt đầu. Không bắt tạo tám file/sổ song song. Bổ sung cấu trúc địa chỉ và trạng thái ngay trong phiếu/khai báo hiện hữu; dẫn đúng Master phù hợp theo R11, không sinh loại đối tượng không có nguồn.

## 4. Bảng phải trả lời được “có làm đúng trình tự không?”

- Đọc kết quả checker `can_start`/`needs_before_start` và bằng chứng, không suy từ nhãn CHUAN_BI hoặc một checkbox người nhập.
- Nhận diện riêng **đã khai**, **đã kiểm đạt**, **chưa kiểm**, **bị chặn**, **cần kiểm lại**. Chưa kiểm không tự thành đạt, nhưng cũng không nói đã có vi phạm khi chưa chạy.
- Mỗi bước thực tế phải trỏ MOT, lần gọi, phiên kế hoạch, đầu vào, người thực hiện/kiểm, thời điểm và output/evidence. Chỉ DECLARE hoặc current_step không chứng minh đã đi đúng chuỗi.
- Check bỏ bước/trước xác nhận/đổi kế hoạch sau xác nhận/đổi nguồn sau kiểm/thiếu nơi ghi/ACK sai phiên bằng cùng luật005 và checker. Không viết một luật tính xanh khác trong HTML. Sai thì hiện đúng mốc, lý do, nơi xử lý và người giữ.
- Chưa đủ trước S3: vẫn được chuẩn bị/kiểm điều kiện; chưa được sửa sản phẩm. Phạm vi G1 không đòi backend đã triển khai; kiểm mô tả/khả thi kết nối G1 khác E2E của G2. Phần không áp dụng phải có lý do được duyệt, không tự bỏ hàng.
- Tổng trạng thái chỉ phản ánh bằng chứng của lần đang chọn. Với lượt hiện tại, không lấy 87 ca mô phỏng hoặc test vòng cũ làm dấu xanh.

## 5. Chỉ chạm đúng nguồn và kiểm xong bằng mắt Owner

Host nội dung Astra Codex sửa `catalog.work_form`/các MOT liên quan và renderer `workBoard`; dữ liệu kết quả vẫn tại `work/mow-mot-moit-mout/UI-REVIEW-MOW001.json#/application_D24`. Preview phải được sinh/đối chiếu từ phiếu đó. Claude giữ phần Kiểm soát theo D25. GPT chỉ nộp phản biện này.

Giữ #tqt-work-board ở đầu tab Over view, trước danh mục năm quy trình. Hộp⑤ trong Overview có liên kết rõ **“Bảng checkpoint của việc đang chọn”** tới đúng bảng. Chỉ một bảng chính, không thêm dashboard nhập tay, không tiếp tục nối báo cáo diễn giải xuống cuối trang.

Nghiệm thu giao diện: mở Over view không bấm thêm đã thấy đủ mốc và nơi ghi, mốc đang làm, thiếu gì/ai làm; mỗi đường ghi mở đúng nguồn; đổi nguồn thì bảng cập nhật và thông tin cũ không được tô xanh; mobile vẫn đọc được; dữ liệu đang có đủ13 khai/0 kiểm phải hiện đúng. Mở một việc khác phải dùng cùng khuôn, không còn MOW001 viết cứng. Khi chỉ có một việc nối dữ liệu, ghi rõ “1 việc đã có dữ liệu”, không giả có bộ điều phối mọi task.

## 6. Bằng chứng lượt rà

Nguồn đọc: D24/P23 + D25/P24; HEAD `3a0040dd584b7574ed41a1fbc5e8d2996328bbaa`, kiểm lại tại `2adbfe832e89c0afdaee860677542e9986f6d222`. `view.html` SHA256 `79ab0ee1312601e03ea6f100016c1298e64eba2b8c2e64113f4030a423ec834d`. Link Codex gửi là một revision cố định 9d7afd7; lượt rà này đã dùng bản xuất mới nhất, không chỉ bản cũ.

Browser #tqt-work-board HTTP200, console0: chỉ tóm tắt và nút mở13mục. #MOW-TH-005 HTTP200, console0: tên/phạm vi mới đã hiện nhưng chưa có checkpoint mỗi mốc. Sync-status fresh, nguồn=xuất.

Job `4b61200b0c1f401b8f72472966011a06`: preview==application_D24, 13 declarations, 0 PASS, 0 evidence_refs có dữ liệu; S2/CHUAN_BI; 5 kế hoạch TODO; questions_complete=false; requirements_checked=false; test_result/connection_tests.in/out=NOT_TESTED; release.NOT_REQUESTED, decision_ref/ack_ref=null; history chỉ có DECLARE. Một số nơi ghi kết quả/test còn nêu trong câu văn, chưa có pointer cho chính lượt mới. Đây không phải khẳng định toàn file sản phẩm không có kết quả/test lịch sử.

Job `c25ccdda16c0442a8ea741715bc6eb88`: checker exit0, 3 ca đúng/34 ca sai, MATCH_EXISTING_PRODUCT_RECEIPT; `can_start=false`; thiếu10 xác minh trường trước bắt đầu + xác nhận kế hoạch. 13 câu khai không đồng nghĩa13 điều kiện phải kiểm ở cùng một giai đoạn; lấy tập bắt buộc từ luật start_gate, không hardcode.

Kết luận: **đã có khung005 và dữ liệu chuẩn bị, chưa đạt bảng checkpoint người dùng yêu cầu, chưa đủ điều kiện sang S3**. Không mở rộng thêm TH06, không công nhận chạy tự động. Ghi yêu cầu hiển thị/bằng chứng này vào đúng R01/R02/R11/R19 và hồ sơ hiện hữu, không mở một sổ nữa.
