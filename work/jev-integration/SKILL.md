---
name: jev-reference
description: >-
  Dùng khi bạn sắp chốt một quyết định có tập lựa chọn hoặc tiêu chí đã biết: chọn 1 trong N
  phương án, xếp hạng hay chấm mức, phân loại, định tuyến việc, đánh giá rủi ro (ví dụ lệnh/prompt có
  xoá, dừng, ghi đè hay sửa production không), hoặc kiểm một điều kiện có/không trên văn bản, diff,
  log, prompt, kế hoạch — nhất là khi có nhiều câu hỏi độc lập trên cùng một nội dung. Skill chỉ cách
  hỏi JEV (model typesafe/jev-1.13 qua tool `evaluate` của MCP JEV Incomex) để lấy xác suất tham khảo
  nhanh (~0,5 s) và rẻ, rồi bạn TỰ quyết. JEV chỉ là nguồn tham khảo, không phải quyền phê duyệt hay
  chặn. Không dùng để viết code/văn bản, việc sáng tạo, suy luận nhiều bước, đếm/tính/ngày tháng, hoặc
  khi luật/mã tất định đã trả lời được. Use for bounded choice, ranking, classification, routing, risk or
  yes/no verification against known options or criteria.
---

# JEV — nguồn tham khảo cho quyết định có biên

JEV (TypeSafe System One, qua OpenRouter) **không viết chữ**: nó nhận `state` + các câu hỏi đóng và
trả về xác suất có kiểu. Kết quả là **bằng chứng thêm** để GPT/Claude tự quyết — không phải chữ ký cho
phép, không phải lệnh chặn. Quyết định cuối và trách nhiệm vẫn là của bạn (và của Owner với việc phá huỷ).

## Khi nào gọi
- NÊN: chọn/định tuyến/xếp hạng/phân loại/đánh giá rủi ro/kiểm điều kiện với **tập lựa chọn hoặc tiêu
  chí đã biết**; nhiều câu hỏi độc lập trên cùng một state (gộp vào **một** lượt gọi).
- KHÔNG: code/luật tất định đã đủ; việc sáng tạo hay mở; cần suy luận nhiều bước; đếm, tính số, ngày
  tháng; cần sinh nội dung dài; không gửi secret/khoá/mật khẩu, hạn chế dữ liệu cá nhân không cần thiết.

## Cách gọi — tool `evaluate`
```json
{"model": "typesafe/jev-1.13",
 "state": {"prompt_line": "Chạy: rm -rf /opt/app/data rồi restart dịch vụ."},
 "questions": {
   "destructive": {"type": "noul", "instructions": "Does `prompt_line` delete, stop, or overwrite something?"},
   "area": {"type": "choice", "instructions": "Which system does `prompt_line` touch?",
            "criteria": {"production": "live service or data", "scratch": "temporary test area", "none": "no system touched"}}}}
```
- **Luôn ghim `model: "typesafe/jev-1.13"`** trong pilot (dạng `~typesafe/jev-1.13` và `typesafe/jev-latest` trả 400).
- Ba kiểu: `noul` (xác suất điều kiện có/không đúng), `choice` (một mục trong `criteria` là object),
  `score` (`criteria` là **mảng** mức có thứ tự; đáp án đánh số từ 0).
- `state` là **bằng chứng thô** (văn bản, diff, log, trường dữ liệu), gọn, tốt nhất là JSON có tên trường;
  không nhét kết luận của bạn vào — Jev đọc kết luận như bằng chứng và chỉ đồng ý lại với bạn.
- `instructions` nêu **điều kiện cần kiểm**, không nêu kết luận mong muốn; id câu hỏi KHÔNG được gửi cho
  model nên instructions phải tự đủ nghĩa. Mặc định viết instructions bằng tiếng Anh; giữ nguyên ngôn ngữ
  gốc của state, không dịch làm mất nghĩa (calibration Việt/Anh sẽ chỉnh dòng này sau nghiệm thu).
- `choice` nên có lựa chọn "không khớp". Mức `score` phải mô tả tình huống cụ thể.

## Đọc kết quả
- `noul` gần 0,5 = **không chắc**, không phải "mức trung bình". Confidence đo độ tập trung, không đo độ đúng.
- `score` 3,87 trên 5 mức nằm giữa mức 3 và 4 (đếm từ 0); đọc kèm `legend`/`probabilities`.
- Dùng như một ý kiến nhanh: đồng thuận với suy luận của bạn thì tăng tự tin; lệch thì xem lại bằng
  chứng — không làm theo máy móc. Không bắt Owner xem xác suất thô nếu không giúp quyết.

## Khi JEV lỗi
- Tool trả lỗi (`isError`) **hoặc** payload không có `answers` hợp lệ ⇒ **lượt này không có tham khảo
  JEV**. Nói rõ điều đó nếu liên quan, tiếp tục tự suy luận; không giả là đã tham khảo, không thử lại mù
  (gói đã tự thử lại 429/529).
- Lỗi sai khuôn (thiếu `state`, `criteria` sai kiểu) báo đúng đường dẫn trường — sửa câu hỏi một lần rồi thôi.

---
Nguồn: hướng dẫn đặt câu hỏi rút gọn từ `instructions` của `itsmostafa/typesafe-mcp` v0.4.2 (MIT,
© its authors) — bridge `mcp-proxy` không chuyển phần `instructions` đó tới client nên skill này mang
thay. Dựng cho Incomex, RUN `JEV-B1-OPENAI-20260921-01`; khi cài vào client đặt trong thư mục `jev-reference/`.
