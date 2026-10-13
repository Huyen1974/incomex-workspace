# PR21 — Host Codex tiếp nhận QTTH 006 v0.2, gắn vào hồ sơ từng việc

**Chỉ đạo Owner 13/10/2026:** không ép khoảng 100 bước; mỗi bước nguyên tử, làm theo là ra kết quả. Theo dõi cả bước chuẩn áp dụng, **+ bước bổ sung**, **− bước không áp dụng**, **↔ bước thay thế** trong đúng hồ sơ việc. QTTH05 là tổng quan; QTTH06 là chi tiết ở ngay dưới, cùng một trang dài có mở/thu. Chủ thể ký/nhận G1 P37 và lịch sử P38 không được thay.

**Nguồn mới nhất:** `work/tools-quy-trinh/MOW-TH-006.md` phiên `0.2-reviewed-draft`, 85 bước (12/22/11/19/9/5/7). 100 mã v0.1 được đối chiếu tại `proposals/TQT-PR-20261013-gptchat-qtth006-atomic-applicability-review-20.md`. Bản cũ PR18/PR19 đề cập **100 bước** chỉ là lịch sử, KHÔNG dùng làm yêu cầu cố định.

**Đã làm UI đọc chung:** `ui/qtth006-overview-v1.js` hiện chiếu 85 bước v0.2 với mã/phiên/hash nguồn. `view.html` đã được Host GPT liên kết một dòng tại commit `c401c8063fa3d3bed0dac11be18b462ca9bedab5`, chèn vào phía sau phần QTTH05 trước phần các quy trình thành phần. Trên bản xuất đã xác nhận `#tqt006-overview-guide` có tiêu đề 85 bước, mặc định đóng, mobile HTTP200/không có JS error ở lần đo được. **Đây là quy trình chung chưa có trạng thái mỗi việc.**

## Còn phải làm, theo đúng thứ tự

**A. Đăng ký định nghĩa 006:** đối chiếu các Master/DOT/tool có trong 85 bước và xác nhận mã/tên/endpoint (chú ý CAT-069?, CAT-227*, CAT-228* là mã thiết kế/alias; chưa được tự suy mọi nơi ghi PG đã tồn tại). Chỉ ghi một mã `MOW-TH-006` trong Master quy trình tổng hợp. Relation 006 = quy trình chi tiết hóa 005 (implements/operational_detail_for), **không đưa 006 làm `selected_process` của 005** gây vòng gọi; giữ nguyên bảy checkpoint và sáu MOT của 005. Chọn một SSOT bước chung, khi chuyển Markdown vào catalog chỉ giữ bản trỏ hash, tránh nhân bảng nhập sửa hai nơi.

**B. Gắn vào đúng hồ sơ DEF 00.1:** trong mỗi `application_id`, chọn phiên `006@version` và trình bày toàn bộ bước theo 7 nhóm dưới phần tổng hợp 005, **cùng 8 cột**: Bước; AI phải làm gì; Thế nào là xong; Nơi ghi kết quả (Master mã + tên); Tool use; Tình trạng; Điều chỉnh (+/−); Ghi chú. Status chỉ có `Trống/Hoàn thành/Vướng`; `− Không áp dụng` nằm ở cột Điều chỉnh, **không tính Hoàn thành giả**.

**C. Bản áp dụng theo việc, không nhân SSOT:** giữ bản định nghĩa bất biến, hồ sơ chỉ lưu `application_id, process_version, target_version, step_id, item_key, applicability, adjustment, status, result_ref, evidence_ref, issue_ref, owner, return_to, revision` và `reason/approved_by/replaced_by_step_id` khi có. Đối tượng/MOT/ca/field lặp thì `item_key` tách từng bản thực hiện. Dùng đúng Master hiện có (DEF00.1/CAT227*, CAT228*, CAT015, CAT069?, CAT233...), không mở Master mới để lưu trạng thái QT06 và không chạm PG.

**D. Thêm/bớt có quyền và lịch sử:** 
- Bước chuẩn có điều kiện không xảy ra ⇒ đánh `☑ − Không áp dụng`, giữ mã bước và lý do/điều kiện; không đòi người dùng lập bản ghi lỗi giả.
- Bước chuẩn **bắt buộc** không được đánh N/A chỉ để qua checkpoint. Nếu đổi phạm vi phải có căn cứ phê duyệt/phiên, hoặc chuyển sang `Vướng` đúng CP.
- Việc thêm riêng `+ Bổ sung` ⇒ bước `<parent_step_id>+B01`, khai đầu vào/đầu ra, phụ thuộc, điều kiện xong, nơi ghi đúng Master, tool nếu có, người làm và quyết định; sau khi duyệt phải tính vào nghĩa vụ CP của việc đó. Bước thay thế `↔` giữ dòng gốc với quan hệ `replaced_by_step_id`.
- Đối chiếu điều chỉnh lặp nhiều việc để đề nghị chỉnh 006 bằng QTTH003; **không sửa định nghĩa chuẩn vì một ngoại lệ**.

**E. Không hồi tố sai:** MOW001 G1/P37 đã 7/7 trên 005. Vì 006@0.2 chưa có receipts lịch sử chi tiết, mọi bước chưa có bằng chứng ở MOW001 hiện **Trống** và có dòng giải thích `chưa theo dõi QT06 ở P37`. MOW002 chưa mở hồ sơ không được mượn trạng thái MOW001. Quy trình 005 không phải bị phá khi gắn 006.

## Ca tối thiểu trước nghiệm thu

1. Việc bình thường: 005/006 đúng mã/phiên, từng bước áp dụng đúng thứ tự, đủ Master và bằng chứng, checkpoint đúng.
2. Việc có N/A hợp lệ: sản phẩm **không có UI** ⇒ bước kiểm UI được ghi `− không áp dụng`, đủ lý do/điều kiện, không gây lỗi hay làm tăng giả tỷ lệ hoàn thành.
3. Cố bỏ bước **lõi**: phải BLOCKED, không cho qua CP.
4. Có bước +B01: phải xuất hiện ngay dưới bước cha và ảnh hưởng mẫu số CP; chưa có output/biên nhận thì chưa được XONG.
5. Thay phiên hợp đồng/công cụ hoặc sản phẩm: phải làm mất hiệu lực chính những bước phụ thuộc, giữ dấu phiên cũ.
6. Hai hồ sơ khác nhau và `item_key` khác nhau không trộn kết quả; trình bày Desktop/mobile 7 khối thu/mở, không lỗi JS.
7. Đọc lại đúng nguồn/phiên/hash của các Master và đủ bằng chứng khi thật sự thử **một AI mới**; nếu AI phải hỏi tác giả quy trình thì ghi Vướng và hiệu chỉnh, không đánh hoàn thành.

**Quyết định:** đây là yêu cầu Host tiếp nhận/kiểm nghiệm thu. Không tự RUN, không thay Owner duyệt G1, không sửa COLLAB §0 do Claude giữ. Khi chưa có một ca AI mới, QTTH006 mới ở **thiết kế v0.2**, không công bố “AI cứ làm theo là tự chạy được” như sự thật đã kiểm.
