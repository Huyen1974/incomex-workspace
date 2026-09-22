---
name: jev-reference
description: >-
  Luôn hỏi JEV (tool evaluate) trước khi chốt: chọn 1 trong N, xếp hạng, phân loại, lọc, định tuyến,
  rủi ro, có/không theo tiêu chí — kể cả khi thấy đáp án rõ. Không dùng để dịch, tính, viết.
---

# JEV — nguồn tham khảo cho quyết định có biên

JEV **không viết chữ**: nó nhận `state` + các câu hỏi đóng và trả về xác suất có kiểu. Kết quả là
**bằng chứng thêm** để bạn tự quyết — không phải chữ ký cho phép, không phải lệnh chặn. Quyết định cuối
và trách nhiệm vẫn là của bạn (và của Owner với việc phá huỷ).

Model, nhà cung cấp và phiên bản JEV do **JEV Gateway** quản lý. Skill này chỉ dạy khi nào nên gọi, khi
nào không, và cách dùng kết quả như bằng chứng; nó không chọn hay ghim phiên bản nào.

## Khi nào gọi
- NÊN: chọn 1 trong N, định tuyến việc, xếp hạng/chấm mức, phân loại, đánh giá rủi ro (ví dụ lệnh/prompt
  có xoá, dừng, ghi đè hay sửa production không), kiểm một điều kiện có/không trên văn bản, diff, log,
  prompt, kế hoạch — khi **tập lựa chọn hoặc tiêu chí đã biết**. Nhiều câu hỏi độc lập trên cùng một
  state thì gộp vào **một** lượt gọi.
- Gọi **trước khi chốt, kể cả khi bạn đã thấy đáp án rõ** (kể cả chỉ có 2 lựa chọn): JEV mất dưới 1 giây, gần như
  không tốn tiền, là ý kiến thứ hai độc lập để bắt lỗi chủ quan. Bỏ qua chỉ khi rơi vào danh sách KHÔNG dưới đây.
- KHÔNG: luật/mã tất định đã trả lời được; dịch; đếm, tính số, ngày tháng; viết code hay nội dung
  (sáng tạo, dài, mở); cần suy luận nhiều bước; câu hỏi chưa có lựa chọn/tiêu chí rõ.
- Không gửi secret/khoá/mật khẩu; hạn chế dữ liệu cá nhân không cần thiết.

## Cách gọi — tool `evaluate`
Tool `evaluate` của connector/app **JEV Reference**. Tên hiển thị tuỳ client: Codex `jev_reference.evaluate`
(`mcp__codex_apps__jev_reference_evaluate`); Claude Code `mcp__<tên server>__evaluate`; Claude Chat/Cowork:
connector JEV Reference → `evaluate`. Phiên không có tool này ⇒ lượt này không có tham khảo JEV.

```json
{"state": {"prompt_line": "Chạy: rm -rf /opt/app/data rồi restart dịch vụ."},
 "questions": {
   "destructive": {"type": "noul", "instructions": "Does `prompt_line` delete, stop, or overwrite something?"},
   "area": {"type": "choice", "instructions": "Which system does `prompt_line` touch?",
            "criteria": {"production": "live service or data", "scratch": "temporary test area", "none": "no system touched"}}}}
```
- **Không truyền `model`** — để JEV Gateway dùng phiên bản đang hoạt động. Trường `model` trong kết quả
  chỉ để ghi nhận, không dùng để quyết định.
- Ba kiểu: `noul` (xác suất điều kiện có/không đúng), `choice` (một mục trong `criteria` là object),
  `score` (`criteria` là **mảng** mức có thứ tự; đáp án đánh số từ 0).
- `state` là **bằng chứng thô** (văn bản, diff, log, trường dữ liệu), gọn, tốt nhất là JSON có tên trường;
  không nhét kết luận của bạn vào — JEV đọc kết luận như bằng chứng và chỉ đồng ý lại với bạn.
- `instructions` nêu **điều kiện cần kiểm**, không nêu kết luận mong muốn; id câu hỏi KHÔNG được gửi cho
  model nên instructions phải tự đủ nghĩa. Mặc định viết instructions bằng tiếng Anh; giữ nguyên ngôn ngữ
  gốc của state, không dịch làm mất nghĩa.
- `choice` nên có lựa chọn "không khớp". Mức `score` phải mô tả tình huống cụ thể.

## Đọc kết quả
- `noul` gần 0,5 = **không chắc**, không phải "mức trung bình". Confidence đo độ tập trung, không đo độ đúng.
- `score` 3,87 trên 5 mức nằm giữa mức 3 và 4 (đếm từ 0); đọc kèm `legend`/`probabilities`.
- Dùng như một ý kiến nhanh: đồng thuận với suy luận của bạn thì tăng tự tin; lệch thì xem lại bằng
  chứng — không làm theo máy móc. Không bắt Owner xem xác suất thô nếu không giúp quyết.

## Khi JEV lỗi
- Tool trả lỗi (`isError`) **hoặc** payload không có `answers` hợp lệ ⇒ **lượt này không có tham khảo
  JEV**. Nói rõ điều đó nếu liên quan, tiếp tục tự suy luận; không giả là đã tham khảo, không thử lại mù
  (lỗi tạm thời đã được thử lại phía gateway).
- Lỗi sai khuôn (thiếu `state`, `criteria` sai kiểu) báo đúng đường dẫn trường — sửa câu hỏi một lần rồi
  thôi. Lỗi nhắc tới `model` ⇒ bỏ hẳn `model` rồi gọi lại một lần.

---
Nguồn: hướng dẫn đặt câu hỏi rút gọn từ `instructions` của `itsmostafa/typesafe-mcp` (MIT, © its
authors); gateway không chuyển phần `instructions` đó tới client nên skill này mang thay. Bản nguồn:
`incomex-workspace/work/jev-integration/SKILL.md`; khi cài vào client đặt trong thư mục `jev-reference/`.
