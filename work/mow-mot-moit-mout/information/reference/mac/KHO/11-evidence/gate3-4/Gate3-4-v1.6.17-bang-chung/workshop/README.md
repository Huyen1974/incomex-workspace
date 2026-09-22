# Workshop — đọc file này trước

Cập nhật: **11/09/2026**. Đây là bản tương tác để rà đường đi **ý tưởng → tìm/dùng lại → bổ sung phần thiếu → khai báo → kiểm/duyệt → vận hành → cải tiến**. Ví dụ dùng quy trình ghi nhận thời lượng xử lý.

**Nguồn chuẩn của dự án:** [file cấu trúc hệ thống](<../cấu trúc hệ thống.html>). README này chỉ quản lý thư mục workshop. Quyết định, vấn đề mới và trạng thái hiện hành cập nhật ở file chính; không lập thêm sổ việc tại đây.

## Bắt đầu

1. Mở [index.html](index.html) bằng trình duyệt; chạy trực tiếp trên máy, không cần cài thư viện hay dựng máy chủ.
2. Chọn tình huống, bấm **Bắt đầu tình huống**, rồi theo nút bước tiếp. Khi bị chặn, đọc nguyên nhân và dùng nút khắc phục.
3. Năm góc nhìn dùng cùng ngữ cảnh: **Thư viện → Rà soát → Editor đúng owner → Runtime → Vòng đời/Help/phản hồi**. Chuyển góc nhìn là tùy chọn; nút tiếp tự đưa tới bước thích hợp. Dấu vết và số đo nằm cuối trang.

Tất cả là **mô phỏng TEST**, gồm cả duyệt, phát hành, quyền và AUTO. Trang không gọi API nghiệp vụ, không chạy worker thật. Trạng thái chỉ nằm trong bộ nhớ trang: tải lại hoặc bắt đầu tình huống mới sẽ đặt lại lượt diễn tập. “Diễn bước máy” là nút điều khiển diễn tập, không phải việc người dùng sản phẩm phải làm.

## Trong thư mục có gì?

| File | Vai trò / khi cần đọc |
|---|---|
| [README.md](README.md) | Điểm vào cho người/Agent; phạm vi, danh mục, cách tiếp tục và dọn thư mục. |
| [index.html](index.html) | Trang mở workshop; khung giao diện, nạp CSS và JavaScript. |
| [fixture.js](fixture.js) | **Một nguồn dữ liệu mẫu**: ngữ cảnh, nguyên liệu, năm vai người, H1–H5, năm góc nhìn, 19 trạng thái và 10 tình huống lỗi. Đọc khi sửa ví dụ/kịch bản. |
| [workshop.js](workshop.js) | Chuyển bước, giữ ngữ cảnh, render năm góc nhìn, chặn/khắc phục lỗi, số đo và trace. Đọc khi sửa hành vi mô phỏng. |
| [reused-patterns.css](reused-patterns.css) | CSS trích từ Master/Nháp2 có sẵn; giữ nền trình bày tái dùng. |
| [workshop.css](workshop.css) | Bố cục ghép workshop và hiển thị màn hình nhỏ. Chỗ ưu tiên sửa trình bày riêng của workshop. |
| [reuse-provenance.json](reuse-provenance.json) | Hai nguồn CSS, SHA256 và số rule đã trích. Chỉ đọc khi cần kiểm nguồn/tái trích; chưa phải rác. |

Trang nạp `reused-patterns.css` → `workshop.css`, rồi `fixture.js` → `workshop.js`. Năm file này cần đi cùng nhau. Thư mục hiện có **7 file**, không có dependency cài ngoài hay thư mục build.

## Đã làm và phần cần tiếp tục

Mốc bàn giao Gate2 ngày 11/09 đã kiểm **happy path và 10 tình huống lỗi**: tìm chưa đủ/mơ hồ, thiếu nguyên liệu, xung đột bản cũ, thiếu quyền, thiếu người/ủy quyền hết hạn, test fail, duyệt bị từ chối/hết hạn, AUTO retry, thiếu output, retire còn nơi sử dụng. Mỗi lỗi có đường khắc phục/tiếp tục; năm góc nhìn giữ cùng object/package/scope.

Đã sửa việc nhầm test/approval của bản cũ với bản nháp mới. Bản cải tiến v2 vẫn là nháp, lượt đang chạy giữ release v1; Help hiện lệch phiên bản và phản hồi có liên kết ngữ cảnh.

**Giới hạn:** đây là bằng chứng thiết kế, chưa phải quy trình thật từ Agent tới production. Các số đo thuộc kịch bản mô phỏng, không chứng minh tỷ lệ tự động hóa. PM đã ACCEPT WITH FOLLOW-UP / DONE Gate2 về design ngày 11/09/2026; D04 chưa được Owner quyết. Gate3/4 hiện PARTIAL, xem [hồ sơ mới](../gate3-4/README.md). Trạng thái mới hơn xem file cấu trúc hệ thống. Việc tiếp theo phải theo chỉ đạo PM; các điều kiện kỹ thuật còn lại gồm license Directus12, tương thích Nuxt/session và khóa dữ liệu/lifecycle đầy đủ. Proof pin của một lát cắt đã đạt ở Gate3/4; workshop vẫn chỉ mô phỏng, không dùng kết quả lab để đổi màu thành production.

## Tiếp cận và bảo trì

- Agent mới đọc README → phần hiện hành trong file cấu trúc hệ thống → mở workshop. Chỉ đọc file code hoặc bằng chứng liên quan tới nhiệm vụ được giao.
- Mỗi lần thêm/sửa/xóa file hoặc đổi kịch bản, **cập nhật README ngay trong cùng lượt**: bảng file, cách chạy, phạm vi đã kiểm và điều còn mở. Đối chiếu toàn bộ thư mục để không bỏ sót file.
- Giữ một fixture và một ngữ cảnh chung; ưu tiên sửa thành phần hiện có. Ý tưởng mới ghi vào nơi theo dõi trong file chính, phân biệt đề xuất/quyết định/đã làm; ghi nhận không tự mở rộng việc đang được giao.
- Dọn file tạm, bản trùng và đầu ra đã hết giá trị. Hoàn tất một việc không có nghĩa xóa thành phần đang chạy hoặc bằng chứng còn cần truy nguồn. Trước khi xóa, kiểm trang có nạp file đó không và các liên kết còn dùng ở đâu; sau đó kiểm lại danh mục/liên kết. Chỉ chạy lại kiểm thử hành vi khi code hoặc fixture thay đổi.

## Dọn gọn và truy nguồn khi cần

Ngày 11/09 đã xóa **`fixture.json`**: bản sao dữ liệu trùng hoàn toàn với `fixture.js`, không được trang nạp. Sáu file cũ còn lại giữ nguyên nội dung; chỉ thêm README này. Không tạo thêm bản sao lưu hay nhật ký rời cho lần dọn này.

[Gói bằng chứng Gate2 đã bàn giao](/Users/nmhuyen/Documents/Codex/2026-09-08/ch/outputs/Gate2-R9-v1.6.16-2026-09-11-evidence.zip) giữ nguyên snapshot cũ, gồm cả file đã dọn. Khi cần kiểm lại, tra đúng `design/r9-walkthrough.md`, `browser/workshop/run-summary.json`, ảnh/trace ca liên quan hoặc `platform/platform-verdict.md` trong gói. Manifest cũ xác minh snapshot trong ZIP; không đại diện cho thư mục làm việc đã thêm README và dọn file trùng. Không cần đọc toàn bộ gói để bắt đầu.

Đường dẫn workshop cũ trong thư mục phiên Codex là liên kết tới thư mục này, giúp các liên kết đã gửi vẫn mở được; đây là **một bản làm việc**, không phải hai bản chuẩn.

Cập nhật v1.6.17: chỉ sửa nhãn trạng thái PM trong trang và README; không sửa fixture hoặc hành vi mô phỏng. Hồ sơ Gate3/4 và bằng chứng mới đặt cạnh workshop, không nhét thêm dữ liệu thử vào thư mục này.
