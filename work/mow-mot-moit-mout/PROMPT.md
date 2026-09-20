# PROMPT — MMIM.2 · Thu thập và tổ chức information

## 0. Lệnh và phạm vi
Owner đã giao việc này ngày 2026-09-20. Đây là lượt THU THẬP / TỔ CHỨC TÀI LIỆU, không phải lượt sửa sản phẩm.

Trước khi làm:
1. Đọc `AGENTS.md` ở root repo.
2. Đọc `work/mow-mot-moit-mout/COLLAB.md`, đặc biệt khối §0.
3. Đọc toàn bộ prompt này.
4. Kiểm tra commit READY trong COLLAB đúng là commit cuối chạm `PROMPT.md`. Nếu lệch: DỪNG.

Nguồn trên Mac:
`/Users/nmhuyen/Desktop/quy trình`

Đích duy nhất của lượt MMIM.2:
`work/mow-mot-moit-mout/information/`

File gốc/HTML chính — CẤM SỬA trong lượt này:
`work/mow-mot-moit-mout/mow-mot-moit-mout.html`

Bản HTML trên repo là bản làm việc chuẩn của việc này. Các bản cùng/ gần tên trên Mac chỉ đọc để đối chiếu, không được chép đè lên repo.

## 1. Mục tiêu
Khảo sát toàn bộ `/Users/nmhuyen/Desktop/quy trình` để tìm các file thực sự liên quan tới hồ sơ MOW · MOT · MOIT · MOUT và file HTML chính hiện hành. Các tài liệu FIELD/UI liên quan trực tiếp được đưa vào cùng phạm vi nguồn của lượt thu thập, nhưng MMIM.2 không tự thay đổi mục tiêu nghiệp vụ đã xác nhận ở COLLAB §0.

Tự đề xuất cấu trúc dễ hiểu trong `information/`, rồi COPY các file cần thiết vào đó. Mục tiêu của `information/` là: AI hoặc người mới vào việc có thể biết đâu là phụ thuộc trực tiếp, nguồn nghiệp vụ/thiết kế, tham khảo và legacy — mà không phải mò lại toàn bộ Desktop.

## 2. Trình tự khảo sát và nguyên tắc chọn file
Trước khi tự phân loại, nếu còn tồn tại thì đọc các sổ chỉ đường:
- `00-DOC-TRUOC.md`
- `KHO/00-CANH-BAO-DOC-TRUOC.txt`
- `KHO/00-NHAT-KY-DON-DEP.txt`

Kế thừa các nhãn “cũ/hết hiệu lực/không dùng” đã có căn cứ; không phân loại lại từ đầu chỉ dựa vào tên file.

Rà theo bốn lớp:

**A · Phụ thuộc trực tiếp của HTML chính**
- Quét các tham chiếu file tương đối từ `src`, `href`, manifest/fetch/import và metadata. Bỏ qua URL `http(s)`, fragment `#...`, `javascript:`, `mailto:` và `data:`.
- Bộ ảnh hiện hành đang dùng tiền tố thư mục Unicode dạng NFD. Trong MMIM.2 KHÔNG cố tái tạo tên thư mục NFD ở Git và KHÔNG sửa HTML. Stage bộ phụ thuộc vào một cây cha ASCII an toàn dưới:
  `information/direct-dependency/source-assets/`
  rồi giữ cấu trúc con cần thiết ở bên trong.
- Với 16 ảnh + `image-manifest.json`, tính hash nguồn/đích và kiểm manifest trỏ tới file có thật trong cây staged. Không nhân bản cùng hash.
- README bắt buộc có bảng `LINK-MAP`: địa chỉ tương đối cũ trong HTML → file nguồn Mac → file staged trong repo hoặc `MISSING`. Đây là dữ liệu để Host xử lý đường dẫn ở một lượt riêng sau MMIM.2; Codex không vá HTML.

**B · Nguồn được HTML chính nêu đích danh**
- HTML/MD/JSON/JS/CSS/ảnh/tài liệu mà nội dung/comment/metadata file chính dẫn tới.
- Đặc biệt rà các nguồn thiết kế/quy trình như `00-NGUON-THIET-KE.html`, `cấu trúc hệ thống.html`, `BAN-DO-BUOC-UI-AGENT.html`, `TAO-MOT-QUY-TRINH.html` và các file tương tự thực sự được dẫn.
- Nếu HTML ghi sẵn SHA cho một nguồn thì tính SHA file Mac và ghi MATCH/MISMATCH; không tự thay nguồn để “khớp”.

**C · Tài liệu làm việc hiện hành có liên quan trực tiếp**
- file mô tả/triển khai MOW, MOT, MOIT, MOUT, FIELD, UI cha/UI con, quy trình tạo, config, ma trận, test;
- chỉ copy khi có lý do sử dụng rõ.

**D · Lịch sử / legacy / bản chép runtime**
- backup, phiên bản cũ, script cập nhật cũ, tài liệu hết hiệu lực chỉ giữ nếu cần đối chiếu;
- HTML/JS/CSS trên Mac là bản chép của các UI đang chạy tại VPS `/ui-preview/mcp-writes/` KHÔNG được xếp CURRENT. Nếu cần giữ, xếp D và ghi rõ: `MAC_COPY_ONLY · current_runtime_source = VPS root ui`.
- MMIM.2 không fetch/copy runtime VPS.

Không copy mù toàn bộ thư mục. Không lấy `.git`, `node_modules`, cache/temp, file hệ thống, file không liên quan hoặc bản sao trùng hash.

## 3. Cách tổ chức — Codex tự đề xuất
Codex được quyền quyết định cây bên trong `information/` sau khi khảo sát thật, với các chốt:
- ít tầng, tên dễ hiểu;
- phân biệt rõ `DIRECT-DEPENDENCY` / `CURRENT` / `REFERENCE` / `LEGACY`;
- cây staging phụ thuộc trực tiếp phải dùng cha ASCII như §2A để tránh bẫy NFD/NFC;
- không đổi tên file nghiệp vụ nếu làm mất truy vết; nếu buộc phải đổi tên ở bản staged thì README phải có mapping nguồn → đích;
- cùng nội dung trùng hash chỉ giữ một bản và ghi mọi đường nguồn trùng.

Không tạo file tiến độ. Báo cáo duy nhất:
`work/mow-mot-moit-mout/information/README.md`

## 4. README bắt buộc
README tối thiểu có:
1. Cây `information/` và lý do.
2. Inventory: nguồn Mac → đích repo → A/B/C/D → lý do → bytes → SHA-256.
3. `LINK-MAP` cho mọi tham chiếu file tương đối của HTML chính: địa chỉ cũ → nguồn thật → đích staged hoặc `MISSING`. Nêu riêng 16 ảnh, manifest và mọi link `../`/file-local đã gãy nếu có.
4. Phụ thuộc trực tiếp: đã copy đủ/chưa đủ; manifest PASS/FAIL.
5. File đã xem nhưng không copy + lý do, dùng nhãn `OMITTED_PUBLIC_SENSITIVE`, `OUT_OF_SCOPE`, `DUPLICATE`, `MAC_RUNTIME_COPY` khi phù hợp.
6. Trùng hash và bản giữ lại.
7. SHA đối chiếu bản HTML trên Mac nếu tìm thấy; SHA nguồn nào đã được HTML ghi sẵn.
8. Cảnh báo Unicode/đường dẫn tương đối.
9. UNKNOWN còn lại; không tự suy thành “đủ”.
10. Tổng số file/dung lượng theo A/B/C/D.

README là mục lục ngắn, không phải bài thuyết minh.

## 5. Công khai và an toàn
Repo được Owner chấp nhận công khai để ưu tiên tốc độ/chất lượng, nhưng KHÔNG đưa thông tin quá nhạy cảm hoặc không cần thiết lên public repo.

Không copy:
- credential, secret, token, private key, session/cookie;
- CCCD/hộ chiếu/tài khoản ngân hàng, hồ sơ tài chính/cá nhân, địa chỉ/SĐT cá nhân khi không cần cho công việc;
- hợp đồng/tài liệu có điều khoản, giá hoặc thông tin đối tác mang tính không công khai nếu không cần thiết cho việc này;
- dữ liệu người thật có thể gây rủi ro riêng tư khi ghép nhiều trường định danh.

Tên người/tên công ty hoặc thông tin nghiệp vụ đã công khai không tự động bị loại nếu thực sự cần cho tài liệu công việc. Với xlsx/docx/pdf nghi có dữ liệu nhạy cảm, mở kiểm nội dung trước khi copy; không quyết định chỉ từ tên file.

Nếu một file >50 MB hoặc tổng phần dự định copy >250 MB: không đưa file lớn đó vào commit ngay; ghi README và tiếp tục các file khác để Host quyết, tránh làm chậm toàn lượt.

Các chốt khác:
- CẤM sửa nội dung/format/metadata/tên/vị trí `mow-mot-moit-mout.html`.
- CẤM xoá/di chuyển/đổi tên nguồn dưới `/Users/nmhuyen/Desktop/quy trình`.
- Chỉ COPY từ Mac sang `information/`.
- Không đụng VPS/runtime/production.
- Không ghi đè file đích khác nội dung.
- Sau copy, hash nguồn = hash đích mới PASS.

## 6. Đúng bản và kiểm trước khi kết thúc
Bắt buộc:
- HTML chính trên repo vẫn đúng SHA-256:
  `f4aac30c492f104ec54ff7a03ace54ce70d802e2dd49a417ad9b7285897a050c`.
- Nếu thấy bản gốc Mac `quy trình/từ thực tế đã làm.html`, tính SHA và ghi vào README. Nếu khác SHA repo: KHÔNG copy đè hoặc “hòa giải”; repo vẫn là bản làm việc chuẩn, ghi divergence để Host xử lý.
- Bản cùng tên nằm trong thư mục con mà tài liệu đã đánh dấu cũ không được dùng làm current.
- Không có thay đổi ngoài:
  - `work/mow-mot-moit-mout/information/**`
  - và cập nhật trạng thái `work/mow-mot-moit-mout/COLLAB.md`.
- mỗi file copy có hash nguồn = hash đích;
- README phản ánh file thật, không ghi “đã copy” từ suy đoán.

## 7. Commit và báo cáo
Tuân thủ AGENTS/README về concurrency, expected HEAD, không force push và secret guard.

Khi hoàn tất:
- commit `information/` + cập nhật COLLAB đúng workflow repo;
- MMIM.2 → `MACHINE_DONE`, ghi số file/dung lượng và `information/README.md`;
- không tự nghiệm thu nghiệp vụ, không sửa HTML chính, không sửa hợp đồng Owner View.

Thông báo cuối:
`XONG · MMIM.2 · information=<số file>/<dung lượng> · main_html_sha=PASS · xem information/README.md`

Nếu không truy cập được Mac, conflict/secret không xử lý an toàn, hoặc hash HTML repo thay đổi:
`DỪNG · MMIM.2 · <lý do cụ thể>`
