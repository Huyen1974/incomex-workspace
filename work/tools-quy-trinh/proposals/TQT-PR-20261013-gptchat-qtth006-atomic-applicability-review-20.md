# PR20 — Rà từng bước QTTH 006 và biến thể theo từng hồ sơ (13/10/2026)

**Vai:** GPT phản biện và hiệu chỉnh bản nháp 006 theo chỉ đạo Owner; Codex là Host nội dung, Claude giữ §0. Bản cũ v0.1 có đúng 100 bước do cố đếm; bản v0.2 dùng số bước sau rà, không có chỉ tiêu.

## Kết luận và các sửa quan trọng

- Không ép 100. Bản mới có **85 bước** phân theo CP01–07 (**12 + 22 + 11 + 19 + 9 + 5 + 7**). 2 dòng cũ về quy tắc nhánh chung, bước cùng giao dịch/đích ghi được gộp; có bước mới về kiểm CP01, chọn áp dụng/N/A/bổ sung và kiểm tổng theo phạm vi.
- Gãy thứ tự: `006-057` (tạo P01) chuyển từ CP04 về CP02; `006-049/058` (bên sau tự đọc gói chuẩn bị) hợp lại ở CP03. Không có gói thì không được xác nhận bắt đầu.
- Gãy kiểm dữ liệu: `006-063` (kiểm hợp đồng đầu ra) chuyển trước bước ghi `006-061`. Bên nhận kiểm đủ schema/phiên trước khi xác nhận.
- Ca kiểm trùng: `006-032/033` + `006-078/079/080` thành một bước **lập bộ ca** ở CP02. CP05 chỉ **nạp/chạy và lưu kết quả thực**.
- Các nhóm trường CAT206 (`006-022..025`) gộp thành một bước *lặp theo field/item_key*, không bắt AI ghi năm lần cùng một mẫu. Nhiều loại công việc không phải MOW/UI/G1 nên biến thành bước có điều kiện.
- Nguồn tra cứu khác nơi ghi: **tra MOW/MOT không ghi vào Master MOW/MOT**, phải ghi liên kết/quyết định vào DEF00.1. Quy trình 002/003 không được ghi ở cột Tool.
- Việc thêm/bớt/đổi được ghi **tại application theo 006@version**, không xóa bước chuẩn; N/A phải có điều kiện/lý do, bước bắt buộc của 005 không tự được N/A. Bổ sung cần mã con, người, điều kiện xong, sổ đích và approval. Biến thể lặp lại mới xét nâng cấp quy trình chuẩn.
- MOW001 P37 chỉ chứng minh 005 đạt 7/7; không có biên nhận thực hiện 006 nên không hồi tố trạng thái 006.

## Bảng đối chiếu đầy đủ 100 bước cũ → bước v0.2

Định danh mới luôn gồm mã quy trình + phiên + checkpoint + bước. Bản v0.1 vẫn trong Git history, không ghi đè ký ức.

| Mã v0.1 | Kết quả rà | Ánh xạ sang v0.2 |
|---|---|---|
| 006-001 | GIỮ/SỬA | MOW-TH-006@0.2:CP01.01 |
| 006-002 | GIỮ/SỬA | MOW-TH-006@0.2:CP01.02 |
| 006-003 | GIỮ/SỬA | MOW-TH-006@0.2:CP01.03 |
| 006-004 | GIỮ/SỬA | MOW-TH-006@0.2:CP01.04 |
| 006-005 | GIỮ/SỬA | MOW-TH-006@0.2:CP01.05 |
| 006-006 | GỘP | MOW-TH-006@0.2:CP01.06 |
| 006-007 | GỘP | MOW-TH-006@0.2:CP01.06 |
| 006-008 | GỘP | MOW-TH-006@0.2:CP01.07 |
| 006-009 | GỘP | MOW-TH-006@0.2:CP01.07 |
| 006-010 | GIỮ/SỬA | MOW-TH-006@0.2:CP01.08 |
| 006-011 | GIỮ/SỬA | MOW-TH-006@0.2:CP01.09 |
| 006-012 | GIỮ/SỬA | MOW-TH-006@0.2:CP01.10 |
| 006-013 | BỎ BƯỚC BẮT BUỘC, GIỮ QUY TẮC NHÁNH | QUY TẮC CHUNG XỬ LÝ SAI/THIẾU |
| 006-014 | GIỮ/SỬA | MOW-TH-006@0.2:CP01.11 |
| 006-015 | GIỮ/SỬA | MOW-TH-006@0.2:CP02.01 |
| 006-016 | GIỮ/SỬA | MOW-TH-006@0.2:CP02.02 |
| 006-017 | GIỮ/SỬA | MOW-TH-006@0.2:CP02.03 |
| 006-018 | BỎ BƯỚC BẮT BUỘC, GIỮ QUY TẮC NHÁNH | QUY TẮC CHUNG XỬ LÝ SAI/THIẾU |
| 006-019 | GIỮ/SỬA | MOW-TH-006@0.2:CP02.04 |
| 006-020 | GIỮ/SỬA | MOW-TH-006@0.2:CP02.05 |
| 006-021 | GỘP | MOW-TH-006@0.2:CP02.06 |
| 006-022 | GỘP | MOW-TH-006@0.2:CP02.07 |
| 006-023 | GỘP | MOW-TH-006@0.2:CP02.07 |
| 006-024 | GỘP | MOW-TH-006@0.2:CP02.07 |
| 006-025 | GỘP | MOW-TH-006@0.2:CP02.07 |
| 006-026 | GỘP | MOW-TH-006@0.2:CP02.08 |
| 006-027 | GỘP | MOW-TH-006@0.2:CP02.08 |
| 006-028 | GỘP | MOW-TH-006@0.2:CP02.06 |
| 006-029 | GIỮ/SỬA | MOW-TH-006@0.2:CP02.09 |
| 006-030 | GIỮ/SỬA | MOW-TH-006@0.2:CP02.10 |
| 006-031 | GIỮ/SỬA | MOW-TH-006@0.2:CP02.11 |
| 006-032 | GỘP | MOW-TH-006@0.2:CP02.12 |
| 006-033 | GỘP | MOW-TH-006@0.2:CP02.12 |
| 006-034 | GIỮ/SỬA | MOW-TH-006@0.2:CP02.13 |
| 006-035 | GIỮ/SỬA | MOW-TH-006@0.2:CP02.14 |
| 006-036 | GIỮ/SỬA | MOW-TH-006@0.2:CP02.15 |
| 006-037 | GIỮ/SỬA | MOW-TH-006@0.2:CP02.18 |
| 006-038 | GIỮ/SỬA | MOW-TH-006@0.2:CP02.19 |
| 006-039 | GIỮ/SỬA | MOW-TH-006@0.2:CP02.20 |
| 006-040 | GIỮ/SỬA | MOW-TH-006@0.2:CP02.22 |
| 006-041 | GỘP | MOW-TH-006@0.2:CP03.01 |
| 006-042 | GỘP | MOW-TH-006@0.2:CP03.01 |
| 006-043 | GIỮ/SỬA | MOW-TH-006@0.2:CP03.02 |
| 006-044 | GIỮ/SỬA | MOW-TH-006@0.2:CP03.03 |
| 006-045 | GIỮ/SỬA | MOW-TH-006@0.2:CP03.04 |
| 006-046 | GIỮ/SỬA | MOW-TH-006@0.2:CP03.05 |
| 006-047 | GIỮ/SỬA | MOW-TH-006@0.2:CP03.06 |
| 006-048 | GIỮ/SỬA | MOW-TH-006@0.2:CP03.07 |
| 006-049 | GỘP | MOW-TH-006@0.2:CP03.08 |
| 006-050 | GIỮ/SỬA | MOW-TH-006@0.2:CP03.09 |
| 006-051 | GIỮ/SỬA | MOW-TH-006@0.2:CP03.10 |
| 006-052 | GIỮ/SỬA | MOW-TH-006@0.2:CP03.11 |
| 006-053 | GIỮ/SỬA | MOW-TH-006@0.2:CP04.01 |
| 006-054 | GỘP | MOW-TH-006@0.2:CP04.02 |
| 006-055 | GỘP | MOW-TH-006@0.2:CP04.02 |
| 006-056 | GIỮ/SỬA | MOW-TH-006@0.2:CP04.03 |
| 006-057 | GIỮ/SỬA | MOW-TH-006@0.2:CP02.21 |
| 006-058 | GỘP | MOW-TH-006@0.2:CP03.08 |
| 006-059 | GỘP | MOW-TH-006@0.2:CP04.04 |
| 006-060 | GỘP | MOW-TH-006@0.2:CP04.04 |
| 006-061 | GIỮ/SỬA | MOW-TH-006@0.2:CP04.06 |
| 006-062 | GIỮ/SỬA | MOW-TH-006@0.2:CP04.07 |
| 006-063 | GIỮ/SỬA | MOW-TH-006@0.2:CP04.05 |
| 006-064 | GỘP | MOW-TH-006@0.2:CP04.09 |
| 006-065 | GIỮ/SỬA | MOW-TH-006@0.2:CP04.08 |
| 006-066 | GỘP | MOW-TH-006@0.2:CP04.09 |
| 006-067 | GIỮ/SỬA | MOW-TH-006@0.2:CP04.10 |
| 006-068 | GIỮ/SỬA | MOW-TH-006@0.2:CP04.11 |
| 006-069 | GIỮ/SỬA | MOW-TH-006@0.2:CP04.12 |
| 006-070 | GIỮ/SỬA | MOW-TH-006@0.2:CP04.13 |
| 006-071 | GIỮ/SỬA | MOW-TH-006@0.2:CP04.14 |
| 006-072 | GIỮ/SỬA | MOW-TH-006@0.2:CP04.15 |
| 006-073 | GIỮ/SỬA | MOW-TH-006@0.2:CP04.16 |
| 006-074 | GIỮ/SỬA | MOW-TH-006@0.2:CP04.17 |
| 006-075 | GIỮ/SỬA | MOW-TH-006@0.2:CP04.18 |
| 006-076 | GIỮ/SỬA | MOW-TH-006@0.2:CP04.19 |
| 006-077 | GIỮ/SỬA | MOW-TH-006@0.2:CP05.01 |
| 006-078 | GỘP | MOW-TH-006@0.2:CP02.12 |
| 006-079 | GỘP | MOW-TH-006@0.2:CP02.12 |
| 006-080 | GỘP | MOW-TH-006@0.2:CP02.12 |
| 006-081 | GIỮ/SỬA | MOW-TH-006@0.2:CP05.02 |
| 006-082 | GỘP | MOW-TH-006@0.2:CP05.03 |
| 006-083 | GIỮ/SỬA | MOW-TH-006@0.2:CP05.04 |
| 006-084 | GIỮ/SỬA | MOW-TH-006@0.2:CP05.05 |
| 006-085 | GIỮ/SỬA | MOW-TH-006@0.2:CP05.06 |
| 006-086 | GIỮ/SỬA | MOW-TH-006@0.2:CP05.07 |
| 006-087 | GỘP | MOW-TH-006@0.2:CP05.03 |
| 006-088 | GIỮ/SỬA | MOW-TH-006@0.2:CP05.08 |
| 006-089 | GIỮ/SỬA | MOW-TH-006@0.2:CP05.09 |
| 006-090 | GIỮ/SỬA | MOW-TH-006@0.2:CP06.01 |
| 006-091 | GIỮ/SỬA | MOW-TH-006@0.2:CP06.02 |
| 006-092 | GIỮ/SỬA | MOW-TH-006@0.2:CP06.03 |
| 006-093 | GIỮ/SỬA | MOW-TH-006@0.2:CP06.04 |
| 006-094 | GIỮ/SỬA | MOW-TH-006@0.2:CP06.05 |
| 006-095 | GIỮ/SỬA | MOW-TH-006@0.2:CP07.01 |
| 006-096 | GIỮ/SỬA | MOW-TH-006@0.2:CP07.02 |
| 006-097 | GIỮ/SỬA | MOW-TH-006@0.2:CP07.03 |
| 006-098 | GIỮ/SỬA | MOW-TH-006@0.2:CP07.04 |
| 006-099 | GIỮ/SỬA | MOW-TH-006@0.2:CP07.06 |
| 006-100 | GIỮ/SỬA | MOW-TH-006@0.2:CP07.07 |

## Điểm Codex cần kiểm trước đăng ký Master

1. Mã Master đích (đặc biệt alias CAT-069?, CAT-227*/228*/239*) đã có đường ghi và quyền thực đúng phiên chưa? Mã thiết kế/UI khác một endpoint đã chạy.
2. Khuôn lưu biến thể áp dụng ở DEF 00.1 hiện **chưa có trường đã nghiệm thu cho từng bước 006**. Codex xác minh khả năng dùng `application` hiện tại để lưu `step_id + item_key + applicability + delta + reason + evidence` không đẻ Master mới; nếu thiếu schema thì trình thêm tại nguồn đúng vai.
3. Rà MOW-TH-005 có 6 MOT nguồn nhưng hiển thị 7 CP, tránh hiểu 006 là selected_process lồng vào 005; 006 là quy trình chi tiết hóa 005, không thay engine 005.
4. Kiểm bản chiếu UI QTTH006 phiên 0.1 nếu còn dùng phải được cập nhật theo 0.2 có hash/version; không cho hiển thị 100 bước đã lỗi như phiên hiện hành. Over view là khung, hồ sơ từng việc là sổ trạng thái.
5. Ghi một ca AI mới không lịch sử chat chạy một việc nhỏ, và một ca có `+ Bổ sung`/ `− Không áp dụng`; nếu chưa đạt chỉ để trạng thái THIẾT KẾ, không tự tăng tiến độ MOW001 hay đụng PG.

**Đề nghị điều hành:** Host Codex ACCEPT hoặc REQUEST_CHANGES kèm bằng chứng, ưu tiên sửa đúng nguồn/ít nhất. Không bắt Owner chờ toàn hệ thống PG mới xem được QTTH006. 
