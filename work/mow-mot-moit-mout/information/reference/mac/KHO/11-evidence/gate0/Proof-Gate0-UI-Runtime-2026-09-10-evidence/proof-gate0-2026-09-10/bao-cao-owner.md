# Báo cáo PM — UI + Runtime Gate0 · 10/09/2026

1. **UI:** dùng lại `Form block → UForm → FormCustom`, thêm một adapter ghi dùng chung; không tạo renderer riêng cho form.
2. **AI khai báo → UI đổi: PASS.** V1 chỉ có thời lượng; Agent thêm Field ghi chú sẵn có ở V2, UI tự hiện sau reload. 36 hash source/build không đổi.
3. **Ghi/đọc lại/mở lại/xung đột: PASS.** Sai kiểu →422; revision cũ →409, giữ bản nháp, phải chủ động đối chiếu rồi ghi; gửi lại đúng yêu cầu không thêm hiệu ứng.
4. **Runtime:** chọn pg-boss12.30.0; dùng sẵn queue/claim/retry/ACK. Queue PG cũ thiếu semantics đã thấy trong source, không tự vá thành engine mới.
5. **Event→AUTO→ACK: PASS.** Worker tự chạy bằng service identity; truy đủ event→instance→attempt→receipt→Directus audit. Không Agent thao tác ở giữa.
6. **Trùng/phiên bản/restart: PASS trong lát cắt.** 3 sự kiện hợp lệ cùng hồ sơ →3 lượt/3 kết quả; bản gửi trùng không thêm. Lượt V1 vẫn dùng V1 sau V2; việc chờ xử lý được sau restart. Release là fixture TEST ONLY.
7. **Chi phí:** 179 dòng mới +UForm 9 dòng thêm/1 bỏ; giữ guard163+2 dòng cũ; thêm33 dòng DDL. 2 dependency trực tiếp/21 package khóa version, 1 worker riêng. Harness kê riêng; 0 production deploy, lab đã dọn, 5 demo không đổi.
8. **READY FOR PM GATE0 EXIT REVIEW.** SSOT v1.6.13 đã cập nhật một lần. Gate0 vẫn DOING, O1–O3 NOT VERIFIED, R1 chưa mở. Production auth, release governance và crash/load/DR chưa được chứng minh.

Bằng chứng: `README.md`, `verification.json`, `runtime-trace.json`, browser HTTP/ảnh và ZIP kèm manifest. Đây là candidate chứng minh khả thi để PM xét, chưa phải kiến trúc production cuối cùng.
