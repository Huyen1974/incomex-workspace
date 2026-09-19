# PROMPT — R02 đóng kết nối lần cuối

RUN_ID: R02-CLOSEOUT-20260919-03

Chỉ chạy khi COLLAB ghi READY@<full-sha> đúng commit cuối chạm PROMPT.md và có RUN hợp lệ. Đây là lượt **đóng tầng máy** của R02; không được tuyên bố client/cross-client PASS.

## Mục tiêu
Sau lượt này không còn nợ kỹ thuật nào trong phạm vi connector có thể làm sai nghiệm thu. Phần còn lại duy nhất phải là K1–K9 trên hai chat thật.

## Việc phải làm
1. Đọc AGENTS.md, COLLAB P07–P11 và KB §13 rev mới nhất. Áp PL1–PL3 của P10.
2. **Commit chứng tích K10** vào đúng hai repo mã bằng stage theo đúng path; không đụng 171 file bẩn ngoài phạm vi:
   - Claude: test_fsroots_persistence_k10_20260919.py
   - GPT: test_persistence_k10_20260919.py
3. **Làm test-harness đáng tin một lần:**
   - Claude: có một lệnh chính thức chạy toàn bộ suite connector mà không sinh đỏ giả do env cấp module; sửa fixture/runner tối thiểu, không đổi runtime nếu không cần.
   - GPT: bỏ phụ thuộc may rủi tải máy ở test background cũ; chờ theo điều kiện/tín hiệu với timeout hữu hạn phù hợp production. Chứng minh test cũ không còn lúc xanh lúc đỏ.
4. **Audit minimum shared capability — không chạy theo số tool.** Cả hai chat phải có đường tương đương cho:
   discover/list · read/search/stat · edit/create · diff/log · copy/move · multi-file transaction · expected version/head · freshness · idempotency.
   Tool riêng từng client được phép khác. Thiếu năng lực bắt buộc thì sửa; không tạo tool trùng chỉ để bằng số lượng.
5. **Audit schema/release gate:**
   - ghi exact live tool surface + schema/version/hash của mỗi server;
   - mọi tool có thay schema phải được phản ánh trong tools/list; operation_id đúng ở mọi entry point đã thiết kế;
   - kiểm standard MCP version/listChanged hoặc cơ chế chuẩn mà server/client thực sự hỗ trợ; không phát minh workaround riêng nếu client không dùng;
   - chốt quy tắc: thay schema => client cũ không được dùng để nghiệm thu; reconnect/refresh + chat mới là release gate.
6. Tạo **một lệnh nghiệm thu chuẩn** cho mỗi connector bằng test/runner nằm trong repo mã hiện hữu (không tạo tài liệu mới). Một lệnh phải trả rõ PASS/FAIL cho regression + capability/schema checks. Nếu runner mới không cần thiết, ghi chính xác lệnh hiện hữu thay thế.
7. Chạy lại toàn bộ regression bằng chính lệnh chuẩn và kiểm live server sau đó. Nếu phát hiện lỗi runtime: test đỏ trước, sửa tối thiểu, deploy theo PL2/PL3. Nếu không có lỗi runtime: không restart.
8. Cập nhật **KB §13 hiện hữu**: bảng CODE / SERVER / CLIENT / CROSS. Agent chỉ được đánh PASS CODE+SERVER; CLIENT+CROSS phải để PENDING và ghi exact expected surface cho K1–K9.
9. Không sửa AGENTS/README/COLLAB/PROMPT. Không xoá dữ liệu/nhánh/image, không đổi auth/URL/secret.

## Điều kiện Agent được báo XONG
- K10 tests đã commit.
- Hai test suites chạy bằng quy trình ổn định, không đỏ giả đã biết.
- Minimum capability đủ ở cả hai connector hoặc có BLOCK rõ.
- Live server đúng schema/version/surface đã ghi.
- Không còn nợ connector-side chưa xử lý; chỉ còn client refresh + K1–K9.
- KB §13 có bằng chứng và không ghi "production ready".

## Trả lời Owner
Một dòng:
`R02-CLOSEOUT-20260919-03: XONG — chỉ còn client K1–K9; xem KB §13`
hoặc
`R02-CLOSEOUT-20260919-03: DỪNG — BLOCK ở KB §13`
