# QTTH 006 — Làm đúng, ghi đủ, kiểm được

Phiên **1.1-signature-sources** · 71 bước, 7 mốc · Thiết kế ngoài PG, chưa nghiệm thu AI mới thực hiện.

**Phạm vi áp dụng từ chỉ đạo Owner 15/10/2026:** Đây là **quy trình thực hiện chi tiết dành cho triển khai thực tế (G2/G3), ghi/đổi dữ liệu thật, giao nhận và công việc rủi ro cao**; không dùng 71 bước làm điều kiện bắt buộc cho **G1 vẽ UI · chốt hợp đồng Field · rà Config khả thi trên vùng nháp**. G1 dùng đường thiết kế ngắn do Host trình Owner chốt (đề xuất MOW-TH-007 tại README/P49 V12), gọi từ nhánh Thiết kế của MOW-TH-001. MOW-TH-005 vẫn là khuôn quản lý chung; không phải bắt G1 lập toàn bộ hồ sơ. Ghi chú phân tuyến, **không xoá/sửa 71 bước, không thay đổi hiệu lực các biên nhận G1/P61 đã có**.

## Đọc trước khi làm
Mục tiêu: một con đường độc đạo — ai vào cũng chỉ có một lối, không thể lạc, muốn làm sai cũng không được.

1. Cần làm thế nào thì viết rõ, có thứ tự.
2. Làm đúng thứ tự đã viết và phải làm xong; không xong thì quay lại sửa quy định/luật.
3. Làm phải để lại bằng chứng: xong có ô tích, có thông tin chứng minh; cần tìm lại để sửa/nâng cấp thì dễ.

**Bắt đầu:** đọc yêu cầu gốc → kiểm quyền/phạm vi → tra mã việc → mở đúng hồ sơ CAT-227. Không tạo hồ sơ ở trang local thay nơi chuẩn.
**Xong cả việc:** đúng mục tiêu/sản phẩm/người nhận/tiêu chí/ngoài phạm vi đã được Owner duyệt trước chuẩn bị; đủ kết quả kiểm, Field thiết kế, chữ ký đúng phiên, 7 mốc và xác nhận nhận. Thẻ 3 ô tự tính; dấu xanh không nhập tay. Khép RUN khác hoàn thành sản phẩm.
**Dừng:** ghi vấn đề ở CAT-069, người xử lý, bước quay lại và điều kiện tiếp; báo 4 dòng, khép RUN, trả cờ. Không giữ máy chờ duyệt.

🤖 CHECK005 chặn dữ liệu sai hợp đồng ở đường kiểm; 📝 Host bắt buộc kiểm trước ghi và đọc lại. Chưa có cưỡng chế mọi endpoint trên máy chủ hoặc chứng thực danh tính người ký. Không tuyên bố lời dặn là máy đã bảo vệ.

## Mã và duyệt lần đầu
Mã dùng loại + số: CAT-227 (sổ việc), CV-001 (việc), FLD-0001 (Field), SC-001 (lần sửa). Ngắn, ổn định; không thêm tên task/ngày/trạng thái. Mã cũ là bí danh để đọc lịch sử, không cấp lại. ML-DEF-024 dùng mã đã hợp nhất ML-DEF-024; không mở danh mục DOT khác.
Master và mỗi bản ghi phải có mã riêng. User duyệt lần đầu đúng mã/phiên/phạm vi/bằng chứng trước đưa vào dùng; AI không tích thay. Chưa có bằng chứng thì hiện chưa xác minh. Duyệt không đóng băng thiết kế: đổi phải ghi sửa và rà ảnh hưởng.

## Thẻ việc và nơi ký
Năm ô: mục tiêu; sản phẩm có nơi kiểm; người nhận; tiêu chí đo được có cách kiểm; ngoài phạm vi. Owner duyệt đúng nội dung trước CP02. Đổi sau duyệt → CAT-016 + Owner duyệt lại, không tự dời đích.
Ba dòng tự tính: tiêu chí đạt/tổng; số Field dự kiến và đủ kiểm kê; chữ ký từng phiếu GPT/Claude/Owner. DESIGN chỉ cần kiểm kê thiết kế; số cột thực sự cần tạo PG vẫn chưa xác minh. DEPLOY mới cần bằng chứng PG. Không lấy thiếu truy cập PG làm khóa chết nghiệm thu thiết kế.
Reviewer mở Hộp chờ ký tại ô ③ hồ sơ CAT-227, lọc hãng và phạm vi → mở đúng nơi ký → ghi APPROVE/REJECT, người/hãng/thời điểm/bằng chứng/căn cứ thẩm quyền → đọc lại ô ký. Viết “OK” trong báo cáo không thay chữ ký tại phiếu. Ký rà quy trình/sổ không là ký nghiệm thu sản phẩm hoặc quyết định hoãn từng nợ. User duyệt lấy từ quyết định thật; chưa có để trống.

Hộp chờ ký tự liệt kê phiếu CAT-025, bộ kiểm và các mục đã đăng ký cần ký; Field và sổ nợ dùng cùng phiếu nguồn, không nhân chữ ký theo từng dòng. 🔴 Chưa ký/Cần sửa · 🟡 Cần ký lại/Chưa xác minh nguồn · ✅ Đã thông qua đúng nguồn. Ô Owner hiện riêng; lịch sử giữ để truy nguồn. Khi mở, máy kiểm byte UI hiện hành, nguồn tài liệu/bộ kiểm từ đúng revision đã xuất, và dữ liệu đúng phạm vi. Không lấy hash do người ký tự khai làm bằng chứng nguồn; lỗi đọc phải hiện chưa xác minh.
Lượt rà được khép khi mọi mục được giao đã có APPROVE hoặc REJECT đúng phiên; REJECT vẫn chặn chốt chuẩn. Quy trình chuẩn cần OpenAI và Anthropic cùng APPROVE đúng bản/phạm vi. Quyết định Owner và nghiệm thu sản phẩm là các việc riêng; không giữ RUN sống để đợi chữ ký.

## Thẻ bước: 9 câu tại nơi thao tác
Mỗi bước có làm gì; sau bước nào; đầu vào; ai; công cụ; xong khi; nơi ghi; khi báo cáo; lỗi đi đâu. Định nghĩa ghi sẵn, kết quả thực tế để trống tới khi có bằng chứng. Mở dấu ? ở bước để đọc đủ chín câu.
Đường chính phải hoàn thành phụ thuộc trước khi ghi DONE. Nhánh lỗi kích hoạt tại bước phát hiện, không cần đi tới cuối bảng. Nhánh không áp dụng phải có căn cứ và rà khác hãng theo luật bên dưới.

## CP01 · Khai việc

### CP01.01 · Đọc nguyên yêu cầu Owner và điều không được làm
- **Sau:** Đầu vào của nhánh / yêu cầu gốc
- **Đầu vào:** Hồ sơ đúng mã/phiên; yêu cầu gốc của Owner
- **Ai:** AI
- **Tool:** Thực hiện bằng tay, ghi người và bằng chứng
- **Xong khi:** Có mục tiêu/người giao/nguồn rõ
- **Ghi:** CAT-227 · Master tiến trình công việc (CAT-227)
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP01.01 rồi kiểm các bước phụ thuộc.

### CP01.02 · Xác nhận A0, quyền Owner và phạm vi trước khi mở hồ sơ
- **Sau:** CP01.01
- **Đầu vào:** Hồ sơ đúng mã/phiên; kết quả đã ghi của CP01.01
- **Ai:** AI
- **Tool:** Thực hiện bằng tay, ghi người và bằng chứng
- **Xong khi:** Đủ từng nghĩa vụ: CP01.02: Có phạm vi được xác nhận; CP01.07: Có một phạm vi được xác nhận gồm sản phẩm, các nhánh ngoài phạm vi và điều kiện mở lại
- **Ghi:** CAT-227 · Master tiến trình công việc (CAT-227)
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP01.02 rồi kiểm các bước phụ thuộc.

### CP01.04 · Tra trùng rồi mở hồ sơ, ghim phiên và khởi tạo chỗ ghi
- **Sau:** CP01.02
- **Đầu vào:** Hồ sơ đúng mã/phiên; kết quả đã ghi của CP01.02
- **Ai:** MACHINE
- **Tool:** TQT-CHECK-005 · Kiểm Master; —; TQT-CHECK-002 · Kiểm mã; TQT-CHECK-001 · Kiểm mô hình
- **Xong khi:** Đủ từng nghĩa vụ: CP01.03: Không tạo hồ sơ trùng; CP01.04: Hồ sơ mở được đúng ID; CP01.05: Hồ sơ trỏ 005@version và 006@version; không có vòng gọi 006; CP01.11: Có liên kết hồ sơ + phiên định nghĩa bất biến và sổ sự kiện bước; trạng thái ban đầu Trống
- **Ghi:** CAT-227 · Master tiến trình công việc (CAT-227)
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP01.04 rồi kiểm các bước phụ thuộc.

### CP01.06 · Đối chiếu đối tượng công việc và các đối tượng con theo nguồn chuẩn
- **Sau:** CP01.04
- **Đầu vào:** Hồ sơ đúng mã/phiên; kết quả đã ghi của CP01.04
- **Ai:** AI
- **Tool:** TQT-CHECK-005 · Kiểm Master
- **Xong khi:** Đúng mã/phiên/quan hệ con; với MOW tra đúng MOW/MOT, loại khác tra Master đối tượng tương ứng
- **Ghi:** CAT-227 · Master tiến trình công việc (CAT-227)
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP01.06 rồi kiểm các bước phụ thuộc.

### CP01.08 · Ghi nguồn đầu vào một lần để CP02 dùng lại
- **Sau:** CP01.06
- **Đầu vào:** Hồ sơ đúng mã/phiên; kết quả đã ghi của CP01.06
- **Ai:** AI
- **Tool:** MCP workspace_read/stat (có quyền)
- **Xong khi:** Có dữ liệu nguồn truy được
- **Ghi:** CAT-227 · Master tiến trình công việc (CAT-227)
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP01.08 rồi kiểm các bước phụ thuộc.

### CP01.09 · Khai người nhận cuối, nơi gọi và nơi trả
- **Sau:** CP01.08
- **Đầu vào:** Hồ sơ đúng mã/phiên; kết quả đã ghi của CP01.08
- **Ai:** AI
- **Tool:** Thực hiện bằng tay, ghi người và bằng chứng
- **Xong khi:** Đúng đích bàn giao
- **Ghi:** CAT-227 · Master tiến trình công việc (CAT-227)
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP01.09 rồi kiểm các bước phụ thuộc.

### CP01.10 · Khai người làm, người kiểm, người duyệt
- **Sau:** CP01.09
- **Đầu vào:** Hồ sơ đúng mã/phiên; kết quả đã ghi của CP01.09
- **Ai:** AI
- **Tool:** Thực hiện bằng tay, ghi người và bằng chứng
- **Xong khi:** Vai trò/quyền có căn cứ
- **Ghi:** CAT-227 · Master tiến trình công việc (CAT-227)
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP01.10 rồi kiểm các bước phụ thuộc.

### CP01.12 · Đối chiếu kết quả khai việc với CP01 của QTTH 05
- **Sau:** CP01.10
- **Đầu vào:** Hồ sơ đúng mã/phiên; kết quả đã ghi của CP01.10
- **Ai:** MACHINE
- **Tool:** TQT-CHECK-004 · Kiểm bản ghi/mốc
- **Xong khi:** Mốc CP01 được kiểm từ hồ sơ nguồn hoặc có Vướng/owner/return_to
- **Ghi:** CAT-227 · Master tiến trình công việc (CAT-227)
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP01.12 rồi kiểm các bước phụ thuộc.

## CP02 · Chuẩn bị đủ

### CP02.01 · Nạp câu hỏi bắt buộc theo MOW/MOT/phạm vi
- **Sau:** Đầu vào của nhánh / yêu cầu gốc
- **Đầu vào:** Hồ sơ đúng mã/phiên; bằng chứng kích hoạt: KHI(quy trình có bộ câu hỏi) · Bộ câu hỏi của MOW001 không phải yêu cầu mặc định cho mọi việc.
- **Ai:** MACHINE
- **Tool:** TQT-CHECK-003 · Kiểm khai
- **Xong khi:** Đủ bộ câu liên quan
- **Ghi:** CAT-227 · Master tiến trình công việc (CAT-227)
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP02.01 rồi kiểm các bước phụ thuộc.

### CP02.02 · Ghi đáp án, mã câu, người và nguồn
- **Sau:** Đầu vào của nhánh / yêu cầu gốc
- **Đầu vào:** Hồ sơ đúng mã/phiên; bằng chứng kích hoạt: KHI(có câu hỏi áp dụng) · Lặp theo item_key=câu hỏi, không tạo một bước định nghĩa mới cho từng câu.
- **Ai:** AI
- **Tool:** Thực hiện bằng tay, ghi người và bằng chứng
- **Xong khi:** Có đáp án hoặc ghi thiếu
- **Ghi:** CAT-227 · Master tiến trình công việc (CAT-227)
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP02.02 rồi kiểm các bước phụ thuộc.

### CP02.03 · Đọc lại và kiểm phiên/hash của nguồn đã ghi CP01.08
- **Sau:** Đầu vào của nhánh / yêu cầu gốc
- **Đầu vào:** Hồ sơ đúng mã/phiên; bằng chứng kích hoạt: KHI(có nguồn cần kiểm) · Dùng lại tham chiếu CP01.08; không nhập lại nguồn.
- **Ai:** AI
- **Tool:** MCP workspace_read/stat (có quyền)
- **Xong khi:** Đọc lại đúng phiên
- **Ghi:** CAT-239 · Master tệp/bằng chứng
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP02.03 rồi kiểm các bước phụ thuộc.

### CP02.04 · Kiểm quyền đọc dữ liệu từ nguồn thật
- **Sau:** CP01.12
- **Đầu vào:** Hồ sơ đúng mã/phiên; kết quả đã ghi của CP01.12
- **Ai:** MACHINE
- **Tool:** TQT-CHECK-004 · Kiểm ghi/mốc
- **Xong khi:** Có bằng chứng quyền
- **Ghi:** CAT-015 · Sổ kết quả kiểm
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP02.04 rồi kiểm các bước phụ thuộc.

### CP02.06 · Lập hợp đồng CAT-206 và ghim MOW/MOT/quy trình/luật theo phiên
- **Sau:** CP02.04
- **Đầu vào:** Hồ sơ đúng mã/phiên; kết quả đã ghi của CP02.04
- **Ai:** AI
- **Tool:** TQT-CHECK-004 · Kiểm ghi/mốc
- **Xong khi:** Có ID, contract_version, phụ thuộc và nguồn luật xác minh được
- **Ghi:** CAT-206 · Master hợp đồng đầu vào/đầu ra
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP02.06 rồi kiểm các bước phụ thuộc.

### CP02.07 · Định nghĩa từng field và ánh xạ nguồn–đích
- **Sau:** CP02.06
- **Đầu vào:** Hồ sơ đúng mã/phiên; kết quả đã ghi của CP02.06
- **Ai:** AI
- **Tool:** —; TQT-CHECK-004 · Kiểm ghi/mốc
- **Xong khi:** Đủ từng nghĩa vụ: CP02.07: Mỗi field có schema đủ nghĩa/type/unit/nullable/cardinality/miền giá trị; ca sai bị chặn; CP02.08: Có nguồn–đích thực, đúng loại/phiên và phép biến đổi rõ
- **Ghi:** CAT-206 · Master hợp đồng đầu vào/đầu ra
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP02.07 rồi kiểm các bước phụ thuộc.

### CP02.10 · Lập hợp đồng giao–nhận, đầu ra và nhánh lỗi
- **Sau:** CP02.07
- **Đầu vào:** Hồ sơ đúng mã/phiên; kết quả đã ghi của CP02.07
- **Ai:** AI
- **Tool:** TQT-CHECK-004 · Kiểm ghi/mốc; TQT-CHECK-004 · Kiểm giao–nhận; TOOL-CTCM-003 · Phủ nhánh (nếu dùng được)
- **Xong khi:** Đủ từng nghĩa vụ: CP02.09: Bên giao kiểm được payload; CP02.10: Bên nhận đủ đầu vào; CP02.11: Có điều kiện và đường xử lý
- **Ghi:** CAT-206 · Master hợp đồng đầu vào/đầu ra
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP02.10 rồi kiểm các bước phụ thuộc.

### CP02.12 · Lập một bộ ca nghiệm thu gồm ca đúng, sai, rỗng, sai phiên, sai người nhận
- **Sau:** CP02.10
- **Đầu vào:** Hồ sơ đúng mã/phiên; kết quả đã ghi của CP02.10
- **Ai:** AI
- **Tool:** TOOL-CTCM-005 · Rà dữ liệu/lỗi (nếu dùng được)
- **Xong khi:** CAT-012 có ca bắt buộc và expected theo contract/phiên đã chốt
- **Ghi:** CAT-012 · Danh mục bộ kiểm/ca thử
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP02.12 rồi kiểm các bước phụ thuộc.

### CP02.13 · Đối chiếu các giao điểm giữa MOT
- **Sau:** Đầu vào của nhánh / yêu cầu gốc
- **Đầu vào:** Hồ sơ đúng mã/phiên; bằng chứng kích hoạt: KHI(có nhiều bước giao nhận) · Đây là kết quả kiểm các cạnh từ CAT-206, không sửa contract bằng dấu PASS.
- **Ai:** AI
- **Tool:** TQT-CHECK-002 · Kiểm mã
- **Xong khi:** Không còn cạnh phải đoán
- **Ghi:** CAT-015 · Sổ kết quả kiểm
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP02.13 rồi kiểm các bước phụ thuộc.

### CP02.14 · Lập bảng nghĩa vụ thông tin và Master đích
- **Sau:** CP02.12
- **Đầu vào:** Hồ sơ đúng mã/phiên; kết quả đã ghi của CP02.12
- **Ai:** AI
- **Tool:** TQT-CHECK-005 · Kiểm Master; TQT-CHECK-004 · Kiểm ghi/mốc
- **Xong khi:** Đủ từng nghĩa vụ: CP02.05: Mỗi loại thông tin có mã+tên sổ, item_key hoặc issue nếu chưa xác minh; CP02.14: Không mất nghĩa vụ bắt buộc
- **Ghi:** CAT-227 · Master tiến trình công việc (CAT-227)
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP02.14 rồi kiểm các bước phụ thuộc.

### CP02.15 · Phân biệt sổ thiếu, chưa ghi, chưa có quyền
- **Sau:** CP02.14
- **Đầu vào:** Hồ sơ đúng mã/phiên; kết quả đã ghi của CP02.14
- **Ai:** AI
- **Tool:** TQT-CHECK-005 · Kiểm Master
- **Xong khi:** Có issue với từng thiếu sót
- **Ghi:** CAT-015 · Sổ kết quả kiểm
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP02.15 rồi kiểm các bước phụ thuộc.

### CP02.16 · Xác định các bước QTTH 006 áp dụng cho hồ sơ và từng item_key
- **Sau:** CP02.15
- **Đầu vào:** Hồ sơ đúng mã/phiên; kết quả đã ghi của CP02.15
- **Ai:** MACHINE
- **Tool:** TQT-CHECK-003 · Kiểm hồ sơ
- **Xong khi:** Ghim 006@version, phân loại lõi/điều kiện theo từng plan_id/MOT/field và biết bước đến hạn
- **Ghi:** CAT-227 · Master tiến trình công việc (CAT-227)
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP02.16 rồi kiểm các bước phụ thuộc.

### CP02.17 · Rà bước thêm, không áp dụng hoặc thay thế trước khi xác nhận kế hoạch
- **Sau:** Đầu vào của nhánh / yêu cầu gốc
- **Đầu vào:** Hồ sơ đúng mã/phiên; bằng chứng kích hoạt: KHI(có nhánh điều kiện/điều chỉnh) · Bước không áp dụng không tự là Hoàn thành; bước thêm được tính là nghĩa vụ bắt buộc khi đã duyệt
- **Ai:** AI
- **Tool:** TQT-CHECK-004 · Kiểm nghĩa vụ
- **Xong khi:** Mọi +/−/↔ có lý do, người kiểm, điều kiện xong, Master đích; không bỏ bước lõi không có phép
- **Ghi:** CAT-227 · Master tiến trình công việc (CAT-227)
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP02.17 rồi kiểm các bước phụ thuộc.

### CP02.18 · Lập kế hoạch việc con, đầu ra và nơi ghi
- **Sau:** CP02.16
- **Đầu vào:** Hồ sơ đúng mã/phiên; kết quả đã ghi của CP02.16
- **Ai:** AI
- **Tool:** TQT-CHECK-001 · Kiểm mô hình; TOOL-CTCM-001 · Lập hành trình (nếu dùng được)
- **Xong khi:** Đủ từng nghĩa vụ: CP02.18: Có P01…Pn hoặc tương đương, không vòng phụ thuộc; CP02.20: Mỗi plan_id có expected_output, Master mã+tên, product_key và tiêu chí đọc lại
- **Ghi:** CAT-228 · Sổ việc thật MOT/kết quả
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP02.18 rồi kiểm các bước phụ thuộc.

### CP02.19 · Giao actor/reviewer/recipient cho từng việc con
- **Sau:** CP02.18
- **Đầu vào:** Hồ sơ đúng mã/phiên; kết quả đã ghi của CP02.18
- **Ai:** AI
- **Tool:** Thực hiện bằng tay, ghi người và bằng chứng
- **Xong khi:** Mọi việc tới hạn có người
- **Ghi:** CAT-227 · Master tiến trình công việc (CAT-227)
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP02.19 rồi kiểm các bước phụ thuộc.

### CP02.23 · Kiểm cửa ghi và quyền ghi–đọc trước lần ghi chuẩn bị đầu tiên
- **Sau:** CP02.19
- **Đầu vào:** Hồ sơ đúng mã/phiên; kết quả đã ghi của CP02.19
- **Ai:** MACHINE
- **Tool:** TQT-CHECK-004 · Kiểm quyền kho tệp; MCP theo quyền hiện có
- **Xong khi:** Có đích/schema/khóa thật và biên nhận quyền đúng scope; thiếu quyền thì dừng ghi
- **Ghi:** CAT-015 · Sổ kết quả kiểm
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP02.23 rồi kiểm các bước phụ thuộc.

### CP02.21 · Tạo và ghi gói chuẩn bị P01 hoặc đầu ra chuẩn bị tương đương
- **Sau:** Đầu vào của nhánh / yêu cầu gốc
- **Đầu vào:** Hồ sơ đúng mã/phiên; bằng chứng kích hoạt: KHI(quy trình có bước chuẩn bị P01/tương đương) · BƯỚC ĐƯỢC CHUYỂN TỪ CP04 VỀ CP02; tạo trước khi kiểm CP03. Chỉ ghi sau CP02.23; gói nháp có thể soạn trước, chưa coi đã ghi.
- **Ai:** AI
- **Tool:** TQT-CHECK-004 --read-preparation
- **Xong khi:** Có sản phẩm chuẩn bị thật, đúng contract và nguồn; đọc lại trước CP03
- **Ghi:** CAT-228 · Sổ việc thật MOT/kết quả
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP02.21 rồi kiểm các bước phụ thuộc.

### CP02.22 · Chạy kiểm chuẩn bị của checkpoint 2
- **Sau:** CP02.23
- **Đầu vào:** Hồ sơ đúng mã/phiên; kết quả đã ghi của CP02.23
- **Ai:** MACHINE
- **Tool:** TQT-CHECK-003 · Kiểm khai
- **Xong khi:** Đạt CP02 hoặc ghi Vướng rõ
- **Ghi:** CAT-227 · Master tiến trình công việc (CAT-227)
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP02.22 rồi kiểm các bước phụ thuộc.

## CP03 · Xác nhận bắt đầu

### CP03.12 · Tiếp tục sau DỪNG tại đúng mốc đang dừng
- **Sau:** Đầu vào của nhánh / yêu cầu gốc
- **Đầu vào:** Hồ sơ đúng mã/phiên; bằng chứng kích hoạt: KHI(tiếp tục sau DỪNG) · Áp tại mọi mốc; không chờ tới CP03 mới kiểm; không hồi sinh RUN cũ.
- **Ai:** MACHINE
- **Tool:** CHECK004/005 + gateway hiện hữu
- **Xong khi:** Đọc KQ cũ, kiểm phiên/quyền/biên nhận và phạm vi thay đổi; chỉ tiếp phần còn thiếu, không lặp tác động đã ghi
- **Ghi:** CAT-227 + CAT-229 + CAT-015
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP03.12 rồi kiểm các bước phụ thuộc.

### CP03.01 · Tra và kiểm tính sẵn sàng của Tool/DOT sẽ dùng
- **Sau:** Đầu vào của nhánh / yêu cầu gốc
- **Đầu vào:** Hồ sơ đúng mã/phiên; bằng chứng kích hoạt: KHI(kế hoạch có Tool/DOT) · Tra nguồn ML-DEF-024 Master DOT, ML-DEF-023 Master Tool; không chạy chỉ vì có tên.
- **Ai:** MACHINE
- **Tool:** TQT-CHECK-006 · Chạy tổng
- **Xong khi:** Mỗi tool có ID/phiên/hash, nguồn, quyền và ca gần nhất, hoặc phương án làm tay
- **Ghi:** CAT-229 · Sổ lượt thực hiện/thử
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP03.01 rồi kiểm các bước phụ thuộc.

### CP03.02 · Xác thực người làm qua quyền ngoài hồ sơ
- **Sau:** CP02.22
- **Đầu vào:** Hồ sơ đúng mã/phiên; kết quả đã ghi của CP02.22
- **Ai:** MACHINE
- **Tool:** TQT-CHECK-004 · Kiểm ghi/mốc
- **Xong khi:** Có quyền thực, không tự khai
- **Ghi:** CAT-227 · Master tiến trình công việc (CAT-227)
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP03.02 rồi kiểm các bước phụ thuộc.

### CP03.03 · Kiểm lại reviewer đã được phân công và quyền kiểm
- **Sau:** Đầu vào của nhánh / yêu cầu gốc
- **Đầu vào:** Hồ sơ đúng mã/phiên; bằng chứng kích hoạt: KHI(cần người kiểm) · Không phân công reviewer mới trùng với bước phân vai ở CP01.
- **Ai:** MACHINE
- **Tool:** Thực hiện bằng tay, ghi người và bằng chứng
- **Xong khi:** Đúng người/phiên và mức độc lập theo quy định
- **Ghi:** CAT-227 · Master tiến trình công việc (CAT-227)
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP03.03 rồi kiểm các bước phụ thuộc.

### CP03.04 · Rà xác nhận kế hoạch đúng bản/phiên
- **Sau:** CP03.02
- **Đầu vào:** Hồ sơ đúng mã/phiên; kết quả đã ghi của CP03.02
- **Ai:** MACHINE
- **Tool:** TQT-CHECK-003 · Kiểm khai
- **Xong khi:** Kế hoạch đủ quyền/đầu ra
- **Ghi:** CAT-227 · Master tiến trình công việc (CAT-227)
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP03.04 rồi kiểm các bước phụ thuộc.

### CP03.05 · Rà độc lập trường/nguồn/đích hợp đồng
- **Sau:** Đầu vào của nhánh / yêu cầu gốc
- **Đầu vào:** Hồ sơ đúng mã/phiên; bằng chứng kích hoạt: KHI(cần review độc lập theo quy tắc) · Đây là kết quả review hợp đồng, không phải sửa CAT-206.
- **Ai:** REVIEWER
- **Tool:** TQT-CHECK-004 · Kiểm ghi/mốc
- **Xong khi:** Có kết luận đúng contract phiên
- **Ghi:** CAT-015 · Sổ kết quả kiểm
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP03.05 rồi kiểm các bước phụ thuộc.

### CP03.07 · Kiểm lại schema/đường ghi và hiệu lực biên nhận quyền
- **Sau:** CP03.04
- **Đầu vào:** Hồ sơ đúng mã/phiên; kết quả đã ghi của CP03.04
- **Ai:** MACHINE
- **Tool:** TQT-CHECK-004 · Kiểm ghi/mốc
- **Xong khi:** Đủ từng nghĩa vụ: CP03.06: Kết quả kiểm lại đúng phiên, không dùng địa chỉ/biên nhận cũ đã đổi; CP03.07: Biên nhận CP02.23 còn đúng actor/scope/nguồn; chỉ thử lại nếu điều kiện đã đổi
- **Ghi:** CAT-015 · Sổ kết quả kiểm; CAT-229 · Master lượt làm/thử
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP03.07 rồi kiểm các bước phụ thuộc.

### CP03.08 · Bên nhận độc lập đọc và đối chiếu kết quả chuẩn bị P01 hoặc tương đương
- **Sau:** Đầu vào của nhánh / yêu cầu gốc
- **Đầu vào:** Hồ sơ đúng mã/phiên; bằng chứng kích hoạt: KHI(có gói chuẩn bị) · Gộp kiểm nhận lặp từ bước cũ 058; cấm tới CP03 nếu chưa tạo kết quả chuẩn bị.
- **Ai:** REVIEWER
- **Tool:** TQT-CHECK-004 --read-preparation
- **Xong khi:** P01/tương đương đã được tạo trước CP03; đọc đúng schema/phiên/hash
- **Ghi:** CAT-015 · Sổ kết quả kiểm
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP03.08 rồi kiểm các bước phụ thuộc.

### CP03.09 · Giải quyết issue đang chặn bắt đầu
- **Sau:** Đầu vào của nhánh / yêu cầu gốc
- **Đầu vào:** Hồ sơ đúng mã/phiên; bằng chứng kích hoạt: KHI(có issue chặn CP03) · Không có blocker thì đánh − Không áp dụng, không tạo issue giả.
- **Ai:** AI
- **Tool:** TQT-CHECK-003 · Kiểm khai
- **Xong khi:** Không còn blocker CP03
- **Ghi:** CAT-069 · Sổ nhu cầu/góp ý/sai thiếu
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP03.09 rồi kiểm các bước phụ thuộc.

### CP03.10 · Ghi xác nhận bắt đầu đúng người và phiên
- **Sau:** CP03.07
- **Đầu vào:** Hồ sơ đúng mã/phiên; kết quả đã ghi của CP03.07
- **Ai:** AI
- **Tool:** TQT-CHECK-004 · Kiểm ghi/mốc
- **Xong khi:** Có quyết định và căn cứ
- **Ghi:** CAT-025 · Sổ phiếu duyệt/quyết định
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP03.10 rồi kiểm các bước phụ thuộc.

### CP03.11 · Tính lại CP01–03 trước khi vào làm
- **Sau:** CP03.10
- **Đầu vào:** Hồ sơ đúng mã/phiên; kết quả đã ghi của CP03.10
- **Ai:** MACHINE
- **Tool:** TQT-CHECK-004 · Kiểm ghi/mốc
- **Xong khi:** CP03 đạt bằng chứng
- **Ghi:** CAT-227 · Master tiến trình công việc (CAT-227)
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP03.11 rồi kiểm các bước phụ thuộc.

## CP04 · Làm theo quy trình

### CP04.01 · Chọn việc con có đủ các phụ thuộc trước
- **Sau:** CP03.11
- **Đầu vào:** Hồ sơ đúng mã/phiên; kết quả đã ghi của CP03.11
- **Ai:** MACHINE
- **Tool:** TQT-CHECK-001 · Kiểm mô hình
- **Xong khi:** Biết đúng việc đến lượt
- **Ghi:** CAT-227 · Master tiến trình công việc (CAT-227)
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP04.01 rồi kiểm các bước phụ thuộc.

### CP04.02 · Bên thực hiện đọc và kiểm gói đầu vào thật của việc con
- **Sau:** CP04.01
- **Đầu vào:** Hồ sơ đúng mã/phiên; kết quả đã ghi của CP04.01
- **Ai:** AI
- **Tool:** TQT-CHECK-004 · Kiểm ghi/mốc
- **Xong khi:** Gói hợp lệ theo trường/type/đơn vị/nguồn/phiên trước khi làm
- **Ghi:** CAT-015 · Sổ kết quả kiểm
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP04.02 rồi kiểm các bước phụ thuộc.

### CP04.04 · Chọn cách làm/tool đúng phiên rồi tạo sản phẩm việc con
- **Sau:** CP04.02
- **Đầu vào:** Hồ sơ đúng mã/phiên; kết quả đã ghi của CP04.02
- **Ai:** AI
- **Tool:** TQT-CHECK-006 · Chạy tổng; TOOL-CTCM-001 · Lập hành trình (nếu dùng được)
- **Xong khi:** Đủ từng nghĩa vụ: CP04.03: Có cách thực hiện hợp lệ; CP04.04: Có sản phẩm thật với đầy đủ identity và output_version
- **Ghi:** CAT-229 · Master lượt làm/thử; CAT-228 · Sổ việc thật MOT/kết quả
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP04.04 rồi kiểm các bước phụ thuộc.

### CP04.06 · Ghi an toàn: kiểm trước → khóa chống trùng → ghi → biên nhận → đọc lại
- **Sau:** CP04.04
- **Đầu vào:** Hồ sơ đúng mã/phiên; kết quả đã ghi của CP04.04
- **Ai:** MACHINE
- **Tool:** TQT-CHECK-004 · Kiểm ghi/mốc; MCP workspace_transaction (có quyền)
- **Xong khi:** Đủ từng nghĩa vụ: CP04.05: Đủ trường và đúng kiểu/scope/nguồn/phiên trước commit; CP04.06: Có biên nhận ghi hợp lệ; CP04.07: Nội dung bằng bản gửi; CP04.08: Retry không nhân tác động
- **Ghi:** CAT-015 · Sổ kết quả kiểm; CAT-228 · Sổ việc thật MOT/kết quả; CAT-238 · Sổ lệnh gửi–nhận–trả
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP04.06 rồi kiểm các bước phụ thuộc.

### CP04.09 · Bên nhận mở, kiểm gói nhận và xác nhận ACK bước con
- **Sau:** Đầu vào của nhánh / yêu cầu gốc
- **Đầu vào:** Hồ sơ đúng mã/phiên; bằng chứng kích hoạt: KHI(có giao nhận giữa bước/đơn vị) · ACK giao bước không thay Owner ACK nghiệm thu cuối.
- **Ai:** REVIEWER
- **Tool:** TQT-CHECK-004 · Kiểm giao–nhận
- **Xong khi:** Bên nhận kiểm payload đúng schema/phiên rồi mới ACK
- **Ghi:** CAT-238 · Sổ lệnh gửi–nhận–trả
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP04.09 rồi kiểm các bước phụ thuộc.

### CP04.10 · Nếu gửi trùng, chặn nhân tác động
- **Sau:** Đầu vào của nhánh / yêu cầu gốc
- **Đầu vào:** Hồ sơ đúng mã/phiên; bằng chứng kích hoạt: KHI(gửi trùng hoặc retry) · Nhánh không phát sinh phải ghi − Không áp dụng, không tô Hoàn thành.
- **Ai:** AI
- **Tool:** TQT-CHECK-004 · Kiểm ghi/mốc
- **Xong khi:** Giữ một kết quả hợp lệ
- **Ghi:** CAT-238 · Sổ lệnh gửi–nhận–trả
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP04.10 rồi kiểm các bước phụ thuộc.

### CP04.11 · Nếu phản hồi cũ, so phiên và từ chối
- **Sau:** Đầu vào của nhánh / yêu cầu gốc
- **Đầu vào:** Hồ sơ đúng mã/phiên; bằng chứng kích hoạt: KHI(phản hồi stale) · Không dùng giá trị green/đánh giá cũ; mở issue.
- **Ai:** AI
- **Tool:** TQT-CHECK-004 · Kiểm ghi/mốc
- **Xong khi:** Không dùng green cũ
- **Ghi:** CAT-069 · Sổ nhu cầu/góp ý/sai thiếu
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP04.11 rồi kiểm các bước phụ thuộc.

### CP04.12 · Nếu mất quyền, dừng và ghi sự cố
- **Sau:** Đầu vào của nhánh / yêu cầu gốc
- **Đầu vào:** Hồ sơ đúng mã/phiên; bằng chứng kích hoạt: KHI(permission_denied) · Ghi CAT-017, không tự nâng quyền.
- **Ai:** AI
- **Tool:** Thực hiện bằng tay, ghi người và bằng chứng
- **Xong khi:** Có người xử lý vấn đề quyền
- **Ghi:** CAT-017 · Sổ sự cố vận hành
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP04.12 rồi kiểm các bước phụ thuộc.

### CP04.13 · Nếu thiếu Master đích, tra lại và ghi issue
- **Sau:** Đầu vào của nhánh / yêu cầu gốc
- **Đầu vào:** Hồ sơ đúng mã/phiên; bằng chứng kích hoạt: KHI(chưa có sổ/đích ghi đúng) · Ghi CAT-069, chỉ rõ thiếu sổ khác chưa xác định sổ.
- **Ai:** AI
- **Tool:** TQT-CHECK-005 · Kiểm Master
- **Xong khi:** Biết sổ/người/bước sửa
- **Ghi:** CAT-069 · Sổ nhu cầu/góp ý/sai thiếu
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP04.13 rồi kiểm các bước phụ thuộc.

### CP04.14 · Nếu dữ liệu sai, gọi QTTH002 giải quyết
- **Sau:** Đầu vào của nhánh / yêu cầu gốc
- **Đầu vào:** Hồ sơ đúng mã/phiên; bằng chứng kích hoạt: KHI(sai dữ liệu/sản phẩm) · Gọi QUY TRÌNH MOW-TH-002 (không là Tool); giữ mốc trước không bị ảnh hưởng.
- **Ai:** AI
- **Tool:** Thực hiện bằng tay, ghi người và bằng chứng
- **Xong khi:** Có kết quả sửa được kiểm lại
- **Ghi:** CAT-069 · Sổ nhu cầu/góp ý/sai thiếu
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP04.14 rồi kiểm các bước phụ thuộc.

### CP04.15 · Nếu sửa quy trình/hợp đồng, theo QTTH003
- **Sau:** Đầu vào của nhánh / yêu cầu gốc
- **Đầu vào:** Hồ sơ đúng mã/phiên; bằng chứng kích hoạt: KHI(cần sửa quy trình/hợp đồng) · Áp dụng QUY TRÌNH MOW-TH-003; tăng phiên, đánh giá ảnh hưởng.
- **Ai:** AI
- **Tool:** Thực hiện bằng tay, ghi người và bằng chứng
- **Xong khi:** Tăng phiên và giữ lịch sử
- **Ghi:** CAT-016 · Sổ nhật ký thay đổi định nghĩa
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP04.15 rồi kiểm các bước phụ thuộc.

### CP04.16 · Nếu hủy, ghi lý do/phiên/nơi nhận/việc bù
- **Sau:** Đầu vào của nhánh / yêu cầu gốc
- **Đầu vào:** Hồ sơ đúng mã/phiên; bằng chứng kích hoạt: KHI(hủy/việc bù) · Ghi CAT-244 chỉ khi phát sinh, giữ receipt idempotency.
- **Ai:** AI
- **Tool:** TQT-CHECK-004 · Kiểm ghi/mốc
- **Xong khi:** Có bản ghi hủy khi phát sinh
- **Ghi:** CAT-244 · Sổ hủy và việc bù
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP04.16 rồi kiểm các bước phụ thuộc.

### CP04.17 · Kiểm dấu lịch sử bất biến của lần thực hiện, ghi bù nếu thiếu
- **Sau:** CP04.06
- **Đầu vào:** Hồ sơ đúng mã/phiên; kết quả đã ghi của CP04.06
- **Ai:** MACHINE
- **Tool:** TQT-CHECK-004 · Kiểm ghi/mốc
- **Xong khi:** Sự kiện/receipt/version được lưu chính xác, không xóa bản cũ
- **Ghi:** CAT-233 · Sổ sự kiện bản ghi/chống trùng
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP04.17 rồi kiểm các bước phụ thuộc.

### CP04.18 · Chỉ đóng việc con khi có output_ref thật
- **Sau:** CP04.17
- **Đầu vào:** Hồ sơ đúng mã/phiên; kết quả đã ghi của CP04.17
- **Ai:** MACHINE
- **Tool:** TQT-CHECK-004 · Kiểm ghi/mốc
- **Xong khi:** Có sản phẩm/bằng chứng đúng
- **Ghi:** CAT-228 · Sổ việc thật MOT/kết quả
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP04.18 rồi kiểm các bước phụ thuộc.

### CP04.19 · Chốt CP04 sau khi kiểm đầu ra tới hạn
- **Sau:** CP04.18
- **Đầu vào:** Hồ sơ đúng mã/phiên; kết quả đã ghi của CP04.18
- **Ai:** MACHINE
- **Tool:** TQT-CHECK-004 · Kiểm ghi/mốc
- **Xong khi:** Mọi việc con đến hạn CP04 có đầu ra + đọc lại hợp lệ; việc ở CP05/07 chưa bị ép đóng
- **Ghi:** CAT-227 · Master tiến trình công việc (CAT-227)
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP04.19 rồi kiểm các bước phụ thuộc.

## CP05 · Kiểm đầu ra

### CP05.03 · Reviewer nạp ca, tự mở đúng bản và chạy kiểm
- **Sau:** CP04.19
- **Đầu vào:** Hồ sơ đúng mã/phiên; kết quả đã ghi của CP04.19
- **Ai:** REVIEWER
- **Tool:** TQT-CHECK-004 · Kiểm ghi/mốc; TQT-CHECK-004 --read-designs (nếu là bản thiết kế); reader phù hợp loại khác
- **Xong khi:** Đủ từng nghĩa vụ: CP05.01: Tập ca áp dụng đủ, không tạo lại ca kiểm; CP05.02: Có log mở đúng ID/phiên/hash và nội dung; CP05.03: Mỗi ca có kết luận và CAT-015 đọc lại được
- **Ghi:** CAT-015 · Sổ kết quả kiểm
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP05.03 rồi kiểm các bước phụ thuộc.

### CP05.04 · Nếu là UI, thử nút/trạng thái/nhánh thật
- **Sau:** Đầu vào của nhánh / yêu cầu gốc
- **Đầu vào:** Hồ sơ đúng mã/phiên; bằng chứng kích hoạt: KHI(sản phẩm là UI) · Có UI thật mới kiểm giao diện, không lấy test mẫu.
- **Ai:** AI
- **Tool:** TQT-CHECK-004 --check-g1-ui (nếu phù hợp)
- **Xong khi:** Có bằng chứng UI đúng phiên
- **Ghi:** CAT-015 · Sổ kết quả kiểm
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP05.04 rồi kiểm các bước phụ thuộc.

### CP05.05 · Kiểm nội dung bản thiết kế từng MOT
- **Sau:** Đầu vào của nhánh / yêu cầu gốc
- **Đầu vào:** Hồ sơ đúng mã/phiên; bằng chứng kích hoạt: KHI(sản phẩm là thiết kế) · Kiểm đủ field/state/control/branch/rule_ref theo mã/phiên.
- **Ai:** AI
- **Tool:** TQT-CHECK-004 --read-designs
- **Xong khi:** Đủ trường/nút/nhánh/luật/hash
- **Ghi:** CAT-015 · Sổ kết quả kiểm
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP05.05 rồi kiểm các bước phụ thuộc.

### CP05.06 · Kiểm kết quả trả cuối đúng caller/phiên/kiểu
- **Sau:** Đầu vào của nhánh / yêu cầu gốc
- **Đầu vào:** Hồ sơ đúng mã/phiên; bằng chứng kích hoạt: KHI(có trả kết quả cho caller) · Chặng trả cuối phải kiểm giá trị, người nhận, kiểu, thời điểm.
- **Ai:** AI
- **Tool:** TQT-CHECK-004 · Kiểm ghi/mốc
- **Xong khi:** Không trả sai nơi nhận
- **Ghi:** CAT-015 · Sổ kết quả kiểm
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP05.06 rồi kiểm các bước phụ thuộc.

### CP05.07 · Nếu G2/G3, kiểm nguồn/evaluator/permission live
- **Sau:** Đầu vào của nhánh / yêu cầu gốc
- **Đầu vào:** Hồ sơ đúng mã/phiên; bằng chứng kích hoạt: KHI(có nguồn hoặc evaluator live trong phạm vi) · Không ép G2/G3 vào nghiệm thu G1 chỉ thiết kế.
- **Ai:** AI
- **Tool:** TOOL-CTCM-005 · Rà dữ liệu/lỗi (nếu dùng được)
- **Xong khi:** Không nhầm demo thành live
- **Ghi:** CAT-015 · Sổ kết quả kiểm
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP05.07 rồi kiểm các bước phụ thuộc.

### CP05.08 · Nếu ca FAIL, ghi issue/người sửa/bước quay
- **Sau:** Đầu vào của nhánh / yêu cầu gốc
- **Đầu vào:** Hồ sơ đúng mã/phiên; bằng chứng kích hoạt: KHI(ca kiểm FAIL) · Áp dụng MOW-TH-002, ghi CAT-069, quay về đúng nguồn lỗi.
- **Ai:** AI
- **Tool:** Thực hiện bằng tay, ghi người và bằng chứng
- **Xong khi:** Lỗi có cách khắc phục
- **Ghi:** CAT-069 · Sổ nhu cầu/góp ý/sai thiếu
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP05.08 rồi kiểm các bước phụ thuộc.

### CP05.10 · Chạy bộ kiểm tổng đúng phiên khi quy trình hoặc mức rủi ro yêu cầu
- **Sau:** Đầu vào của nhánh / yêu cầu gốc
- **Đầu vào:** Hồ sơ đúng mã/phiên; bằng chứng kích hoạt: KHI(cần fullsuite theo phạm vi) · Chạy trước CP05/Owner duyệt/ACK; thất bại quay bước sửa. Đổi sản phẩm sau kiểm thì kết quả cũ không còn hiệu lực.
- **Ai:** MACHINE
- **Tool:** TQT-CHECK-006 · Chạy bộ kiểm tổng
- **Xong khi:** Kết quả bộ tổng PASS có hash/biên nhận hoặc quyết định không yêu cầu đã ghi
- **Ghi:** CAT-015 · Sổ kết quả kiểm
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP05.10 rồi kiểm các bước phụ thuộc.

### CP05.09 · Chốt CP05 khi đủ ca và đúng phiên
- **Sau:** CP05.03
- **Đầu vào:** Hồ sơ đúng mã/phiên; kết quả đã ghi của CP05.03
- **Ai:** MACHINE
- **Tool:** TQT-CHECK-003 · Kiểm khai
- **Xong khi:** CP05 đạt hoặc Vướng rõ
- **Ghi:** CAT-227 · Master tiến trình công việc (CAT-227)
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP05.09 rồi kiểm các bước phụ thuộc.

## CP06 · Duyệt kết quả

### CP06.02 · Xác thực người duyệt/thẩm quyền theo phạm vi
- **Sau:** CP05.09
- **Đầu vào:** Hồ sơ đúng mã/phiên; kết quả đã ghi của CP05.09
- **Ai:** MACHINE
- **Tool:** TQT-CHECK-004 · Kiểm ghi/mốc
- **Xong khi:** Không dùng worker tự ký
- **Ghi:** CAT-025 · Sổ phiếu duyệt/quyết định
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP06.02 rồi kiểm các bước phụ thuộc.

### CP06.03 · Gom đúng sản phẩm/bằng chứng rồi trình người có quyền quyết định
- **Sau:** CP06.02
- **Đầu vào:** Hồ sơ đúng mã/phiên; kết quả đã ghi của CP06.02
- **Ai:** AI
- **Tool:** TQT-CHECK-005 · Kiểm Master; —
- **Xong khi:** Đủ từng nghĩa vụ: CP06.01: Người duyệt mở đúng bản; CP06.03: Có quyết định rõ ràng
- **Ghi:** CAT-025 · Sổ phiếu duyệt/quyết định
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP06.03 rồi kiểm các bước phụ thuộc.

### CP06.04 · Ghi quyết định kèm product_binding và phiên
- **Sau:** CP06.03
- **Đầu vào:** Hồ sơ đúng mã/phiên; kết quả đã ghi của CP06.03
- **Ai:** HUMAN
- **Tool:** TQT-CHECK-004 · Kiểm ghi/mốc
- **Xong khi:** Có phiếu duyệt đọc lại được
- **Ghi:** CAT-025 · Sổ phiếu duyệt/quyết định
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP06.04 rồi kiểm các bước phụ thuộc.

### CP06.05 · Chốt CP06 sau khi so quyết định với sản phẩm
- **Sau:** CP06.04
- **Đầu vào:** Hồ sơ đúng mã/phiên; kết quả đã ghi của CP06.04
- **Ai:** MACHINE
- **Tool:** TQT-CHECK-004 · Kiểm ghi/mốc
- **Xong khi:** CP06 đạt hoặc quay xử lý
- **Ghi:** CAT-227 · Master tiến trình công việc (CAT-227)
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP06.05 rồi kiểm các bước phụ thuộc.

## CP07 · Bàn giao · kết thúc

### CP07.01 · Tạo gói bàn giao P05 hoặc việc con cuối theo kế hoạch
- **Sau:** Đầu vào của nhánh / yêu cầu gốc
- **Đầu vào:** Hồ sơ đúng mã/phiên; bằng chứng kích hoạt: KHI(kế hoạch có việc bàn giao cuối P05/tương đương) · Không tạo kết quả bàn giao giả nếu quy trình không có việc con ấy.
- **Ai:** AI
- **Tool:** TQT-CHECK-004 · Kiểm ghi/mốc
- **Xong khi:** Có đầu ra để giao đúng bản; chỉ đóng P05 sau ACK thật CP07.04
- **Ghi:** CAT-228 · Sổ việc thật MOT/kết quả
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP07.01 rồi kiểm các bước phụ thuộc.

### CP07.02 · Kiểm hợp đồng nhận cuối và nơi trả
- **Sau:** CP06.05
- **Đầu vào:** Hồ sơ đúng mã/phiên; kết quả đã ghi của CP06.05
- **Ai:** MACHINE
- **Tool:** TQT-CHECK-004 · Kiểm giao–nhận
- **Xong khi:** Đúng người/sản phẩm/phiên
- **Ghi:** CAT-015 · Sổ kết quả kiểm
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP07.02 rồi kiểm các bước phụ thuộc.

### CP07.03 · Ghi giao đúng bản, người và nguồn sản phẩm
- **Sau:** CP07.02
- **Đầu vào:** Hồ sơ đúng mã/phiên; kết quả đã ghi của CP07.02
- **Ai:** MACHINE
- **Tool:** TQT-CHECK-004 · Kiểm ghi/mốc
- **Xong khi:** Có sổ bàn giao thật
- **Ghi:** CAT-232 · Sổ bàn giao/xác nhận nhận
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP07.03 rồi kiểm các bước phụ thuộc.

### CP07.04 · Lấy ACK thật từ bên nhận có thẩm quyền
- **Sau:** CP07.03
- **Đầu vào:** Hồ sơ đúng mã/phiên; kết quả đã ghi của CP07.03
- **Ai:** HUMAN
- **Tool:** TQT-CHECK-004 · Kiểm ghi/mốc
- **Xong khi:** Có biên nhận đúng bản
- **Ghi:** CAT-232 · Sổ bàn giao/xác nhận nhận
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP07.04 rồi kiểm các bước phụ thuộc.

### CP07.06 · Kiểm liên tục CP01–07 và nghĩa vụ áp dụng
- **Sau:** CP07.04
- **Đầu vào:** Hồ sơ đúng mã/phiên; kết quả đã ghi của CP07.04
- **Ai:** MACHINE
- **Tool:** TQT-CHECK-004 · Kiểm ghi/mốc
- **Xong khi:** 7/7 bằng chứng thật, P05 đóng sau ACK; không suy 006 đã đạt chỉ từ 005
- **Ghi:** CAT-227 · Master tiến trình công việc (CAT-227)
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP07.06 rồi kiểm các bước phụ thuộc.

### CP07.07 · Ghi bài học, công cụ đã dùng và vấn đề còn mở để dùng lần sau
- **Sau:** CP07.06
- **Đầu vào:** Hồ sơ đúng mã/phiên; kết quả đã ghi của CP07.06
- **Ai:** AI
- **Tool:** TQT-CHECK-006 · Chạy tổng
- **Xong khi:** Có liên kết tool/phiên/kết quả/issue và giới hạn nghiệm thu ở sổ nguồn
- **Ghi:** CAT-233 · Sổ sự kiện bản ghi/chống trùng
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP07.07 rồi kiểm các bước phụ thuộc.

### CP07.08 · Khép RUN và nhả cờ bận sau khi xác minh tiến trình/lease
- **Sau:** CP07.07
- **Đầu vào:** Hồ sơ đúng mã/phiên; kết quả đã ghi của CP07.07
- **Ai:** MACHINE
- **Tool:** MCP workspace_task_status/exec_status và gateway theo quyền
- **Xong khi:** Có KQ cùng RUN_ID XONG hoặc DỪNG, giữ STARTED; Bảng/root đồng bộ; không còn lease của RUN
- **Ghi:** CAT-233 · Sổ sự kiện bản ghi/chống trùng
- **Báo:** Kết thúc mốc, bị chặn, DỪNG hoặc cần Owner quyết: báo 4 dòng; khép RUN và nhả cờ khi dừng.
- **Lỗi:** Ghi CAT-069 → QTTH 002; cần sửa luật → QTTH 003/CAT-016; quay lại CP07.08 rồi kiểm các bước phụ thuộc.

## Ghi chép, thời gian, nhánh và sửa chữa
- Một nguồn: hồ sơ CAT-227; kết quả ghi vào Master liên quan rồi chiếu lại. Tra trước khi tạo. Bước lặp dùng item_key, danh sách dự kiến/đã kiểm; không gộp nhiều đối tượng thành một dấu đạt.
- DONE cần hành động và bằng chứng; BLOCKED cần lý do, mã vấn đề, người gỡ, bước quay lại, điều kiện làm tiếp. Ô trống nghĩa chưa ghi. NOT_DONE không thay nghĩa vụ bắt buộc.
- Giờ mốc lấy commit máy chủ, giờ ghi không thay giờ hoàn thành; thời lượng chỉ tính từ khoảng đã đo. UI hiện giờ Việt Nam, nguồn giữ ISO. Báo khi chốt mốc/DỪNG/bị chặn/cần Owner: đang ở đâu · đã xong gì · tắc gì · cần ai làm gì.
- HAS_COMMAND bắt lệnh và biên nhận đúng việc. NO_COMMAND cho làm tay ghi MANUAL_ASSISTED, người/bằng chứng và nợ tự động hóa. Không giả đã có robot.
- Không áp dụng: có đánh giá đúng phiên; nếu làm tay phải có reviewer khác hãng ký đúng assessment_binding ở CAT-015. UNKNOWN vẫn hiện để xử lý; nghĩa vụ LUÔN không được bỏ. Dùng CHECK005 --assessment-binding, --validate-dossier.
- Tiếp tục sau DỪNG: CP03.12 kiểm lại phiên/quyền, ghi previous_run_id và return_to trước khi tiếp tục.
- CAT-016 là hồ sơ sửa duy nhất: đối tượng, phiên trước/sau, lý do/mã vấn đề, người yêu cầu/sửa/kiểm/duyệt, giờ, diff, kết quả, chữ ký bị ảnh hưởng. Mỗi thay đổi mới có đúng một bản ghi mới, before_binding/after_binding bằng hash thực của đúng đối tượng trước/sau; sequence là số lần trước đó của đối tượng cộng một. Bản ghi cũ không che lần sửa mới; không sửa hoặc xóa phần lịch sử đã có. Số lần sửa do đếm bản ghi, không nhập tay. Lịch sử truy hồi thiếu bằng chứng phải ghi chưa xác minh, không bịa giờ hoặc người kiểm.
- Field: FLD là ID, db_code là tên cột dự kiến, name là tên hiển thị. Mỗi db_code một nghĩa; tên là danh từ đủ nghĩa, không có dấu hỏi, ưu tiên 30/tối đa 60 ký tự. Mô tả có ba phần: mục đích · giá trị/ví dụ · phân biệt với Field gần giống theo mã. Việc sinh ra có mã việc và nguồn; thiết kế cũ có thể ghi LEGACY_DESIGN cùng con trỏ/phiên nguồn bất biến, không gán đoán CV-001. Trước khi thêm tra mã/kiểu/mô tả và nơi dùng; nghĩa khác phải ghi quyết định. DESIGNED → NEEDS_CREATE → CREATED → ACCEPTED; hoặc DESIGNED → REUSED → ACCEPTED; ngừng dùng có bằng chứng. CREATED/REUSED/ACCEPTED cần bằng chứng PG, chưa PG giữ DESIGNED.

Bản kiểm kê Field của việc phải chỉ đúng phạm vi và đối chiếu từng định nghĩa với nguồn; số mới tự kiểm từ danh sách ID/nguồn gốc. Thiếu ánh xạ giữ INCOMPLETE và nêu số mục cần đối chiếu, không nhận 0 hoặc toàn danh mục là số mới. Trường nghiệp vụ của sản phẩm khác cột quản trị Master; cùng tên không đủ để gộp.

## Kiểm và bàn giao
CHECK005 kiểm hợp đồng/Field/thứ tự/chữ ký; CHECK006 chạy tổng trên snapshot có 5 đầu vào UI đúng hash. Dùng --ui-snapshot để chạy độc lập, không cần gọi VPS khi kiểm. Cả ca đúng và ca cố tình sai phải được kiểm; TEST không nghiệm thu việc thật. Trước công bố đọc lại nguồn/phiên, xem đúng UI, khép RUN và trả cờ.

## Lịch sử và giới hạn
Các phiên 0.5–0.9, bảng 87 nghĩa vụ →71 bước và chữ ký cũ giữ trong detailed_workflow_history/Git/P49. G1 đã nhận giữ nguyên; P46 là chẩn đoán. Bản1.0 không làm lịch sử thành đã thực hiện. Chưa PG, chưa chạy QT002, chưa xác thực danh tính ký ở server. Tách tệp lớn xử lý ở lượt khác.
