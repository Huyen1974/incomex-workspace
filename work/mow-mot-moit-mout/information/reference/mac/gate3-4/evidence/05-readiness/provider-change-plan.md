# Quyết định kỹ thuật trước thử sửa

Readiness lần đầu đã chạy trên hai Draft revision2 và ghi FAIL vào PG. Có bốn lỗi vật chất: note chưa được form khai báo; một MOUT dùng chung đòi output chưa tồn tại ở HMITL; completion AUTO chưa bao gồm record kế thừa; Capability chỉ mô tả bằng câu, chưa có binding thực thi.

I0–I3: dùng nguyên cổng ghi/form declaration v2, native Fields, native Flow Condition/Transform/Read, generic report host hiện có. Không thêm page/UI hoặc business Script. Sửa ngữ nghĩa bằng Definition/Version mới và cập nhật Draft có CAS; không sửa material published tại chỗ. Các sửa này do harness material-owner thực hiện sau proof fresh, không ghi thành quyết định tự làm của hai Agent.

I4–I5: một Flow native đọc Condition từ exact release của Instance, ghi output trong transaction của cổng ghi. Source Flow hiện là cấu hình mutable; chỉ lưu Flow ID không đủ pin. Nếu composition chạy được, guard cần kiểm hash execution configuration của Flow/operations và khóa đọc trong cùng transaction. Đây là adapter generic, không chứa field/threshold/Pilot ID. Thay đổi source phải rerun bộ runtime P1–P4 liên quan. Không triển khai lên production.
