# Kho tham khảo — MOW · MOT · MOIT · MOUT

> **THAM KHẢO · Owner giao 23/09/2026.** Lưu công sức thiết kế, thống kê, thử nghiệm và rà soát đã làm; các thiết kế này đang được làm lại. Không coi các chữ CURRENT, SSOT, PASS hoặc hướng dẫn trong bản cũ là quyết định hiện hành.

**Đã đưa lên: 888 tài liệu nguyên bản, 87,874,934 bytes.** **Ảnh không đưa lên GitHub theo Owner 23/09/2026**; chỉ giữ thông tin nguồn/hash để tra cứu. Còn 97 Excel/Word, 10,507,371 bytes, chưa đưa lên vì đường ghi connector chỉ nhận UTF-8. Không tuyên bố đã chuyển hết.

## Bắt đầu ở đây

| Cần xem | Tài liệu |
|---|---|
| Thiết kế tổng thể cũ — Owner ưu tiên | [cấu trúc hệ thống.html](reference/mac/ca%CC%82%CC%81u%20tru%CC%81c%20he%CC%A3%CC%82%20tho%CC%82%CC%81ng.html) |
| Bản đồ bước và UI/Agent — Owner ưu tiên | [BAN-DO-BUOC-UI-AGENT.html](reference/mac/BAN-DO-BUOC-UI-AGENT.html) |
| Nguồn quyết định thiết kế cũ | [00-NGUON-THIET-KE.html](reference/mac/00-NGUON-THIET-KE.html) |
| Mẫu hành trình tạo quy trình | [TAO-MOT-QUY-TRINH.html](reference/mac/TAO-MOT-QUY-TRINH.html) |
| Workshop mô phỏng — đọc README trước | [workshop/README.md](reference/mac/workshop/README.md) |
| Chỉ đường kho lịch sử | [KHO/00-CANH-BAO-DOC-TRUOC.txt](reference/mac/KHO/00-CANH-BAO-DOC-TRUOC.txt) |
| Báo cáo, khái niệm và quy tắc | [KHO/02-tai-lieu](reference/mac/KHO/02-tai-lieu) |
| Mục lục bằng chứng các vòng Gate | [KHO/11-evidence/INDEX.md](reference/mac/KHO/11-evidence/INDEX.md) |
| Hồ sơ Gate3–4 | [gate3-4/README.md](reference/mac/gate3-4/README.md) |

## Cách dùng

- HTML chính của dự án vẫn là `../mow-mot-moit-mout.html`; không bị sửa, đổi tên hay chép đè bằng bản Mac.
- Trước khi dùng một kết luận cũ, đối chiếu yêu cầu Owner và hồ sơ hiện hành. Giữ các bản lịch sử khác nhau khi nội dung khác; chỉ bỏ bản trùng hash.
- UI đang chạy: nguồn hiện hành là **VPS root `ui`**. Mọi bản chép HTML/JS/CSS runtime ở đây chỉ là `MAC_COPY_ONLY`; không deploy, không thực thi script và không dùng làm bằng chứng runtime hiện tại.
- Các ảnh/file-local trong HTML giữ nguyên địa chỉ. Một số liên kết vốn đã gãy trên Mac hoặc trỏ tới file chưa chuyển; kho này chưa phải gói website tự chạy đầy đủ.

## Cấu trúc và truy nguồn

```text
information/
  README.md             Điểm vào và trạng thái tổng
  inventory.json        Toàn bộ nguồn → đích/bản giữ/lý do bỏ, bytes, SHA-256
  link-map.json         Tham chiếu HTML chính → nguồn tìm được/đích/chờ
  binary-pending.json   Chỉ Excel/Word còn chờ đường chuyển
  reference/mac/        Tài liệu giữ nguyên cây tương đối và byte nguồn
```

Tên Unicode của tài liệu được giữ để truy vết. Không stage/commit file ảnh vào Git; ảnh vẫn ở Mac, chưa có URL dùng chung. Nếu sau này được giao publish ảnh ngoài Git, dùng tên ASCII và cập nhật LINK-MAP. Các file Office còn chờ dự kiến dùng `reference/binary/<sha12>-<tên-ASCII>`. Chưa sửa các đường dẫn HTML.

## Kiểm kê

| Trạng thái | Số file nguồn | Bytes nguồn |
|---|---:|---:|
| `COPIED` | 888 | 87874934 |
| `DUPLICATE` | 138 | 6796847 |
| `DUPLICATE_BINARY` | 4 | 1941443 |
| `DUPLICATE_MAIN_HTML` | 1 | 1827486 |
| `EXCLUDED_IMAGE_BY_OWNER` | 239 | 37756450 |
| `OMITTED_ARCHIVE_CONTAINER` | 14 | 81736359 |
| `OMITTED_CODE_OR_TEMP` | 291 | 4086164 |
| `OMITTED_MACHINE_OR_SENSITIVE` | 139 | 36097154 |
| `OMITTED_RUNTIME_OR_RAW_DATA` | 334 | 83080680 |
| `OMITTED_SYSTEM` | 8 | 71712 |
| `PENDING_BINARY_REVIEW` | 2 | 2918055 |
| `PENDING_BINARY_WRITE_PATH` | 97 | 10507371 |

`COPIED`: đã commit/push và đọc lại hash từ Git. `DUPLICATE`: chỉ giữ một bản trong kho, tra `kept_source`/`destination`. `DUPLICATE_MAIN_HTML`: nội dung đã nằm ở HTML chính. `PENDING_BINARY_WRITE_PATH`: Excel/Word chờ đường ghi phù hợp; chưa có ngoại lệ Git trực tiếp. `EXCLUDED_IMAGE_BY_OWNER`: toàn bộ 239 đường nguồn ảnh (207 nội dung khác nhau) được loại khỏi kế hoạch Git, không phải phần thiếu cần upload. Các nhãn `OMITTED_*` nêu lý do từng file; không suy rằng mọi file bị loại đều có secret. Gói ZIP không công khai nguyên khối vì lẫn mã/log/snapshot; phần tài liệu giải nén đã được chọn riêng. PDF đã bỏ cũ và file gzip chưa được xét để công khai, giữ trạng thái chờ riêng.

## Kiểm tra và giới hạn

- **888/888 file đã copy:** SHA-256 nguồn = blob đọc lại từ GitHub. Mỗi file có hash và commit nhập trong inventory.
- **2155/2155 file nguồn:** hash cuối lượt bằng đầu lượt; không ghi/xóa/di chuyển nguồn Mac.
- **HTML chính:** SHA-256 `f4aac30c492f104ec54ff7a03ace54ce70d802e2dd49a417ad9b7285897a050c` trước/sau không đổi.
- **Manifest ảnh:** 16/16 ảnh nguồn tồn tại, đúng bytes và hash ghi trong manifest; ảnh được giữ ngoài Git theo quyết định Owner, không chờ upload vào repo.
- SHA nguồn được HTML nhắc: `TAO-MOT-QUY-TRINH.html`: MATCH; Mac `f6563893552f84250fe6f9f83e7d6b77609ffb1a8c9be344a76a4186e321ed14`, HTML ghi `f6563893552f84250fe6f9f83e7d6b77609ffb1a8c9be344a76a4186e321ed14`. Không thay nguồn để làm khớp.
- Bản Mac Owner chỉ: `từ thực tế/từ thực tế đã làm.html`: `f4aac30c492f104ec54ff7a03ace54ce70d802e2dd49a417ad9b7285897a050c` — MATCH so với HTML chính; không chép đè. Bản ở gốc `quy trình/từ thực tế đã làm.html` không còn ở vị trí cũ.
- Đã chạy secret scan không gọi xác thực credential; rà thêm dạng key/JWT/URL chứa token và nội dung ảnh/Office trích xuất. Các cảnh báo SHA/base64 của scanner được kiểm theo ngữ cảnh; connector secret guard chạy trên mọi lượt ghi. File mã có chuỗi kết nối không được đưa lên.
- **Chưa nghiệm thu nghiệp vụ, chưa kiểm render toàn bộ HTML, chưa sửa link, chưa fetch/chạm runtime VPS.** Tư liệu có thể mâu thuẫn, lạc hậu hoặc tự báo PASS; đó là lịch sử cần đánh giá lại.
- Đường ghi: `workspace_*`, có expected HEAD/version, operation_id và push non-force. Một lượt gặp khóa Git tạm thời: kiểm lại clean/HEAD không đổi, gửi lại cùng operation_id và đọc lại hash thành công; không xóa khóa thủ công.
- **Việc còn mở:** chuyển 97 Excel/Word bằng đường được phép (chưa được cấp ngoại lệ Git trực tiếp); quyết định riêng cho PDF/gzip cũ; rà nội dung thiết kế mới và sửa liên kết HTML ở lượt được giao sau. P01 không được tự chốt.

## Ảnh nhúng có sẵn trong bản HTML lưu trữ

Kiểm 23/09: 3 HTML tham khảo nguyên bản đã đưa lên có ảnh nhúng `data:image`, tổng chuỗi nhúng khoảng 12,22 MB. Đây là byte có sẵn trong nguồn, không phải file ảnh rời đã upload. Chưa bóc/xóa ảnh hoặc viết lại lịch sử Git vì sẽ thay bản lưu và hash nguồn. Không thêm ảnh nhúng mới. Ghi nhận để cân nhắc bản tham khảo nhẹ ở lượt riêng; HTML chính vẫn nguyên vẹn.
