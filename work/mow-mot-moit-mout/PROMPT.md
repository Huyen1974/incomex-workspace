# PROMPT — MMIM.2 · Thu thập và tổ chức information

## 0. Lệnh và phạm vi
Owner đã giao việc này ngày 2026-09-20. Đây là lượt THU THẬP / TỔ CHỨC TÀI LIỆU, không phải lượt sửa sản phẩm.

Trước khi làm:
1. Đọc `AGENTS.md` ở root repo.
2. Đọc `work/mow-mot-moit-mout/COLLAB.md`.
3. Đọc toàn bộ prompt này.
4. Kiểm tra commit READY trong COLLAB đúng là commit cuối chạm `PROMPT.md`. Nếu lệch: DỪNG.

Nguồn trên Mac:
`/Users/nmhuyen/Desktop/quy trình`

Đích:
`work/mow-mot-moit-mout/information/`

File gốc/HTML chính — CẤM SỬA trong lượt này:
`work/mow-mot-moit-mout/mow-mot-moit-mout.html`

## 1. Mục tiêu
Khảo sát toàn bộ `/Users/nmhuyen/Desktop/quy trình` để tìm các file thực sự liên quan tới hồ sơ MOW · MOT · MOIT · MOUT và file HTML chính hiện hành. Tự đề xuất cấu trúc dễ hiểu trong `information/`, rồi COPY các file cần thiết vào đó.

Mục tiêu của `information/` là: một AI hoặc người mới vào việc có thể biết tài liệu nào là phụ thuộc trực tiếp, tài liệu nào là nguồn nghiệp vụ/thiết kế, tài liệu nào chỉ là lịch sử/tham khảo — mà không phải mò lại toàn bộ Desktop.

## 2. Nguyên tắc chọn file
Rà theo bốn lớp, ưu tiên từ trên xuống:

**A · Phụ thuộc trực tiếp của HTML chính**
- file/thư mục được HTML gọi bằng `src`, `href`, manifest, fetch/import hoặc metadata;
- đặc biệt kiểm tra cây assets/ảnh/manifest đang được tham chiếu;
- giữ nguyên tên Unicode và cấu trúc tương đối cần thiết, không tự normalize tên làm hỏng đường dẫn.

**B · Nguồn được HTML chính nêu đích danh**
- HTML/MD/JSON/JS/CSS/ảnh/tài liệu mà nội dung hoặc comment/metadata của file chính dẫn tới;
- các tài liệu nguồn cho MOW/MOT/MOIT/MOUT, UI, ma trận, quy trình, config, test, handoff.

**C · Tài liệu làm việc hiện hành có liên quan trực tiếp**
- file trong `quy trình` mà nội dung/tên cho thấy đang mô tả hoặc triển khai MOW, MOT, MOIT, MOUT, FIELD, UI cha/UI con, quy trình tạo MOT/MOW, config, ma trận, test;
- chỉ copy khi có lý do sử dụng rõ.

**D · Lịch sử/legacy**
- backup, phiên bản cũ, script cập nhật cũ, tài liệu đã hết hiệu lực chỉ giữ nếu cần để hiểu lịch sử hoặc đối chiếu;
- phải để riêng khỏi nguồn hiện hành, không trộn để AI dùng nhầm.

Không copy mù toàn bộ thư mục. Không lấy `.git`, `node_modules`, cache/temp, file hệ thống, file không liên quan, bản sao trùng hash. Không copy credential, secret, token, key hoặc file cấu hình nhạy cảm; nếu gặp thì bỏ qua và ghi `OMITTED_SENSITIVE` trong mục lục.

## 3. Cách tổ chức — Codex tự đề xuất
Codex được quyền quyết định cây thư mục bên trong `information/` sau khi khảo sát thật.

Yêu cầu bắt buộc:
- cấu trúc ít tầng, tên dễ hiểu;
- phân biệt rõ CURRENT / DIRECT-DEPENDENCY với REFERENCE và LEGACY;
- không đổi tên file nguồn nếu việc đổi tên làm mất truy vết; nếu cần gom, giữ tên file và ghi mapping trong README;
- nếu một cây assets là phụ thuộc trực tiếp, ưu tiên giữ nguyên cây con của nó thay vì rải file ảnh ra nhiều nơi;
- cùng nội dung trùng hash chỉ giữ một bản và ghi các đường nguồn trùng.

Không tạo nhiều file báo cáo tiến độ. Báo cáo duy nhất của lượt này là:
`work/mow-mot-moit-mout/information/README.md`

## 4. README bắt buộc
README phải có tối thiểu:
1. Cây tổ chức `information/` và lý do chọn cấu trúc.
2. Bảng inventory: đường nguồn Mac → đường đích repo → loại A/B/C/D → lý do liên quan → bytes → SHA-256.
3. Danh sách phụ thuộc trực tiếp của `mow-mot-moit-mout.html`; đánh dấu đã copy đủ/chưa đủ.
4. Danh sách file liên quan đã xem nhưng KHÔNG copy và lý do.
5. Trùng lặp: file nào trùng hash, giữ bản nào.
6. Cảnh báo Unicode/đường dẫn tương đối nếu có.
7. Các điểm còn UNKNOWN, tuyệt đối không tự suy thành “đủ”.
8. Tổng số file và tổng dung lượng đã copy theo từng lớp A/B/C/D.

README là mục lục để GPT/Claude/Hermes dùng về sau, không phải bài mô tả dài.

## 5. An toàn
- CẤM sửa nội dung, format, metadata, tên hoặc vị trí của `mow-mot-moit-mout.html`.
- CẤM xoá/di chuyển/đổi tên bất kỳ file nào dưới `/Users/nmhuyen/Desktop/quy trình`.
- Chỉ COPY từ Mac sang `information/`.
- Không đụng VPS/runtime/production.
- Không ghi đè một file đích khác nội dung. Nếu collision tên: dừng ở file đó, đặt tên phân biệt có truy vết và ghi README.
- Sau copy, tính SHA-256 nguồn và đích; chỉ coi PASS khi khớp.
- Nếu file quá lớn hoặc có vẻ chứa dữ liệu nhạy cảm, không copy vội; ghi vào README để Host quyết.

## 6. Kiểm trước khi kết thúc
Bắt buộc kiểm:
- HTML chính vẫn đúng SHA-256 ban đầu:
  `f4aac30c492f104ec54ff7a03ace54ce70d802e2dd49a417ad9b7285897a050c`
- không có thay đổi ngoài:
  - `work/mow-mot-moit-mout/information/**`
  - và cập nhật trạng thái `work/mow-mot-moit-mout/COLLAB.md`.
- mỗi file đã copy có hash nguồn = hash đích;
- README phản ánh đúng file thật, không ghi “đã copy” từ suy đoán.

## 7. Commit và báo cáo
Tuân thủ AGENTS/README hiện hành về concurrency, expected HEAD, không force push và secret guard.

Khi hoàn tất:
- commit phần `information/` + cập nhật COLLAB theo đúng workflow repo;
- dòng hiện hành trong COLLAB chuyển MMIM.2 thành `MACHINE_DONE`, ghi số file/dung lượng và đường `information/README.md`;
- không tự tuyên bố nghiệm thu nội dung nghiệp vụ, không sửa HTML chính.

Thông báo cuối cho Owner chỉ một dòng:
`XONG · MMIM.2 · information=<số file>/<dung lượng> · main_html_sha=PASS · xem information/README.md`

Nếu không thể truy cập đường Mac, phát hiện conflict/secret hoặc không giữ được SHA file chính:
`DỪNG · MMIM.2 · <lý do cụ thể>`
