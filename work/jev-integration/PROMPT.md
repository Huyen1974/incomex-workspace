# PROMPT — JEV hậu kiểm lần 2: skill mới trên claude.ai + thử lại Claude Chat/Cowork (Codex)

RUN_ID: JEV-B2-VERIFY-CODEX-20260922-02

- Host: **Claude Chat** · Host_ID `CLAUDE-JEV-B2-260922-A` (Host Bước 2, D10).
- Executor_Surface: **Codex app trên Mac của Owner, chế độ điều khiển máy tính (computer use)**.
- Write_Path: `workspace_*` (connector Agent Data của Codex) — chỉ để ghi mục KQ vào cuối `work/jev-integration/COLLAB.md`. Không có `workspace_*` thì trả nguyên khối KQ cho Owner, Host ghi hộ.
- Đọc trước: `AGENTS.md` → `work/jev-integration/COLLAB.md` (Trạng thái, KQ `JEV-B2-VERIFY-CODEX-20260922-01`) → file này.

## 0. Vì sao có lượt này
Lượt -01: Claude Chat bỏ qua Jev ở câu chọn 2 phương án (bridge) — bản ghi cho thấy Chat **không mở skill** vì thấy đáp án hiển nhiên. Host đã sửa `SKILL.md` (commit `60fdb01`): mô tả bắt đầu bằng “Luôn hỏi JEV … kể cả khi thấy đáp án rõ”, thêm “lọc”. Lượt này xác nhận bản mới đã lên claude.ai và Chat/Cowork gọi đúng.

## 1. Cấm / an toàn (giữ nguyên lượt -01)
- Chỉ thao tác trong app Claude/claude.ai. **Không mở trang chi tiết connector JEV Reference**; lỡ thấy địa chỉ `https://vps…/jev-mcp/…` thì không chép/ghi, đóng ngay.
- Không đổi cài đặt nào ngoài việc được giao ở S1. Không đụng connector/skill khác, không xoá chat.
- Không gõ chữ “JEV” vào câu thử; mỗi câu một chat/task **MỚI**; không trả lời thêm (Claude xin quyền dùng JEV thì cho phép một lần và ghi lại).
- Bất thường ngoài kịch bản ⇒ DỪNG, ghi lại.

## 2. Kịch bản
- **S1 · skill mới đã lên chưa.** claude.ai → **Customize → Skills** → mở `jev-reference`, đọc dòng mô tả. Bắt đầu bằng “Luôn hỏi JEV” ⇒ ghi `NEW`, sang S2. Còn “Hỏi JEV … tham khảo” ⇒ tìm cuộc chat Claude gần nhất có thẻ tệp **jev-reference** do Host gửi, bấm **Save skill** trên thẻ mới nhất; kiểm lại mô tả. Nếu UI chỉ cho thay bằng cách gỡ bản cũ: **Host cho phép gỡ đúng skill tên `jev-reference` rồi Save bản mới** — không gỡ skill nào khác. Vẫn không lên bản mới ⇒ DỪNG.
- **S2 · Claude Chat** — 4 chat mới, lần lượt Q1, Q2, Q3, Q4.
- **S3 · Cowork** — 2 task mới: Q1, Q3.
- Mỗi câu ghi: có mở skill `jev-reference` không · có gọi **JEV Reference · evaluate** không · có lỗi không. Chụp ảnh vùng trả lời + khối công cụ để tự đối chiếu; không đưa ảnh vào repo.

## 3. Câu thử (dán nguyên văn)
- **Q1 · nên hỏi (2 lựa chọn, câu bị bỏ qua ở lượt -01):**
  > Hai bridge đều chạy được: bridge X strict hơn về Accept header, bridge Y stateless và tương thích rộng hơn với nhiều client. Cần phục vụ nhiều loại client khác nhau. Chọn bridge nào?
- **Q2 · nên hỏi (lọc/phân loại):**
  > Phân loại 5 phản hồi khách hàng sau vào đúng một nhóm: khiếu nại / hỏi thông tin / khen / khác. (1) “Giao hàng trễ 3 ngày, tôi rất bực.” (2) “Cho hỏi khoá học tháng 10 khai giảng ngày nào?” (3) “Nhân viên tư vấn rất nhiệt tình, cảm ơn.” (4) “Tôi muốn đổi số điện thoại liên hệ.” (5) “Phí học cao hơn quảng cáo, đề nghị giải thích.”
- **Q3 · không nên hỏi:**
  > Dịch câu “The service is healthy” sang tiếng Việt.
- **Q4 · nên hỏi (2 lựa chọn hiển nhiên, câu mới):**
  > Nhóm 5 người đều dùng Slack hằng ngày và ít mở email. Gửi báo cáo tuần qua email hay qua Slack thì hợp hơn?

## 4. PASS
- S1 = `NEW`.
- Chat: Q1, Q2, Q4 có gọi `evaluate`, không lỗi; Q3 **không** gọi.
- Cowork: Q1 có gọi; Q3 **không** gọi.

## 5. KQ (một khối ở cuối `COLLAB.md`)
```
## KQ — JEV-B2-VERIFY-CODEX-20260922-02
- `KQ@JEV-B2-VERIFY-CODEX-20260922-02 XONG|DỪNG` · <giờ UTC> · Executor: Codex computer use trên Mac Owner
- S1: <NEW sẵn | đã Save skill | đã gỡ-và-Save | DỪNG> · mô tả hiện: “<12 chữ đầu>”
- Chat: Q1 <skill có/không · evaluate có/không · lỗi> · Q2 <…> · Q3 <…> · Q4 <…>
- Cowork: Q1 <…> · Q3 <…>
- Bất thường: <không | mô tả ngắn>
- FINAL: <PASS|FAIL> theo §4
```
Báo Owner một dòng: `XONG · skill <NEW|…> · Chat <x/3 gọi, Q3 <..>> · Cowork Q1 <..>, Q3 <..>`.
