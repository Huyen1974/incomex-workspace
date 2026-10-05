# README · MMIM · START HERE

> **Cửa vào bắt buộc của việc `work/mow-mot-moit-mout`.**
> Nếu một file/quy trình/tool mới không được nối từ README / Bảng điều khiển / Master tương ứng thì coi như **chưa được đăng ký vận hành**.

## 1. Mỗi phiên phải đọc gì?

1. Root `AGENTS.md`.
2. `COLLAB.md` → đọc **§0 + BẢNG ĐIỀU KHIỂN** để biết việc hiện tại và hành động kế tiếp.
3. README này.
4. Nếu chạm Công thức / Định nghĩa / Master / UI / Coverage → `FORMULA-AI-README.md`.
5. Nếu thay đổi tiêu chí / trạng thái / tên / quan hệ có thể lan nhiều nơi → `CHANGE-PROPAGATION.md` + `CHANGE-IMPACT-MAP.json`.
6. `council/REGISTRY.md` để biết Host/Reviewer/NEXT.
7. Chỉ sau đó mới đọc file chuyên môn cần thiết.

## 2. Luật chống “làm xong rồi quên”

Mọi artifact vận hành mới (quy trình, tool, script, UI, Master, prompt, checklist) phải có **ít nhất một cửa đăng ký bắt buộc**:

- **Quy trình / luật làm việc** → README này + HANDOFF/AGENTS pointer.
- **Công thức / định nghĩa** → FORMULA-AI-README + Master Công thức/Định nghĩa.
- **UI đã duyệt** → Master UI con / UI cha tương ứng.
- **UI chưa duyệt** → review surface; **không** vào Master UI canonical.
- **Prompt/RUN đang chờ** → BẢNG ĐIỀU KHIỂN + council/REGISTRY.
- **Tool/script** → catalog/tool Master hiện hành + tài liệu gọi nó.

**Cấm:** tạo file rồi chỉ ghi tên file trong lịch sử COLLAB. Nếu ngày mai AI không biết *khi nào phải đọc/call nó* thì artifact đó chưa hoàn thành.

## 3. Quy trình thay đổi liên bảng

Khi một tiêu chí thay đổi, **không sửa một chỗ rồi XONG**.

Bắt buộc dùng:
- `CHANGE-PROPAGATION.md` — quy trình 8 bước.
- `CHANGE-IMPACT-MAP.json` — bản đồ machine-readable các bảng/view phải quét.

Chuỗi:
`Change Event → SSOT → quét impact trước → UPDATE/VERIFY/N-A → sửa → quét stale sau → kiểm live → evidence/KQ`.

## 4. Sổ vận hành ngắn

| Artifact | Dùng khi nào | Trạng thái |
|---|---|---|
| `FORMULA-AI-README.md` | Chạm Công thức/Định nghĩa/Master/UI/Coverage | BẮT BUỘC |
| `CHANGE-PROPAGATION.md` | Một thay đổi có thể ảnh hưởng >1 bảng/view | BẮT BUỘC |
| `CHANGE-IMPACT-MAP.json` | Agent cần biết phải quét/cập nhật đâu | BẮT BUỘC cùng Change Propagation |
| `PROMPT-CHANGE-PROPAGATION.md` | Codex audit case đầu tiên của quy trình mới | **PENDING RUN** |
| `HANDOFF-20261001.md` | Phiên Host mới tiếp quản lịch sử/tinh thần | BẮT BUỘC khi handoff |
| `COLLAB.md` | Trạng thái hiện hành + evidence + quyết định | SSOT trạng thái |
| `council/REGISTRY.md` | Ai đang Host/Review/NEXT | SSOT điều phối |

## 5. VIỆC ĐANG CHỜ — KHÔNG ĐƯỢC QUÊN

**PENDING:** giao Codex chạy audit Change Propagation đầu tiên.

- Based on commit: `61b691dfc7457b17467f5eff8d5a1f19da411e4d`
- Prompt: `work/mow-mot-moit-mout/PROMPT-CHANGE-PROPAGATION.md`
- RUN_ID: `MMIM-CHANGE-PROP-20261006-01`
- Mục tiêu: quét repo/current-live cho case UI con D144, sửa stale reference, bổ sung impact map nếu còn thiếu.
- Chỉ hết PENDING khi có:
  `KQ@MMIM-CHANGE-PROP-20261006-01 XONG`
  và Host nghiệm thu.

**Quy tắc Host:** nếu mở phiên mới mà PENDING này chưa có KQ XONG, phải nhắc Owner ngay trong phần “Kế tiếp”; không được âm thầm đi sang việc khác.

## 6. Câu giao Codex

> Đọc `work/mow-mot-moit-mout/PROMPT-CHANGE-PROPAGATION.md`, bám commit `61b691dfc7457b17467f5eff8d5a1f19da411e4d`, chạy đúng RUN_ID `MMIM-CHANGE-PROP-20261006-01`. Không đổi concept; audit/fix current-live theo Change Propagation và ghi KQ vào COLLAB.
