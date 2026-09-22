# PROMPT — JEV hậu kiểm Claude bằng điều khiển máy (Codex)

RUN_ID: JEV-B2-VERIFY-CODEX-20260922-01

- Host: **Claude Chat** · Host_ID `CLAUDE-JEV-B2-260922-A` (Host Bước 2, D10).
- Executor_Surface: **Codex app trên Mac của Owner, chế độ điều khiển máy tính (computer use)**.
- Write_Path: `workspace_*` (connector Agent Data của Codex) — chỉ để ghi mục KQ vào `work/jev-integration/COLLAB.md`. Không có `workspace_*` thì trả nguyên khối KQ cho Owner, Host ghi hộ.
- Đọc trước: `AGENTS.md` → `work/jev-integration/COLLAB.md` (mục Trạng thái, KQ JEV-B2) → file này.

## 0. Mục tiêu
Xác nhận bằng thao tác thật trên máy rằng Claude **Chat** và **Cowork** tự nhớ tham khảo Jev khi gặp quyết định có biên, không hỏi Jev ở việc không hợp, và công tắc Jev trong Chat giữ nguyên ở chat mới. Đây là hậu kiểm; không đổi thiết kế.

## 1. Cấm / an toàn
- Chỉ thao tác trong app Claude (hoặc claude.ai trên trình duyệt). Không mở app/trang khác ngoài việc ghi KQ.
- **Không mở trang chi tiết của connector JEV Reference** (trang đó hiện địa chỉ bí mật). Nếu địa chỉ `https://vps…/jev-mcp/…` lỡ hiện trên màn hình: không chép, không ghi, không đưa vào KQ; đóng ngay.
- Không đổi cài đặt nào, trừ đúng một việc được phép ở T1: bật công tắc JEV Reference cho Chat nếu đang tắt.
- Không gõ chữ “JEV” vào các câu thử. Mỗi câu thử dán vào **một chat/task MỚI**. Không trả lời thêm; nếu Claude hỏi xin quyền dùng công cụ JEV thì bấm cho phép **một lần** và ghi lại.
- Không xoá chat, không sửa skill, không đụng connector khác.
- Gặp điều bất thường ngoài kịch bản ⇒ DỪNG, ghi lại, không tự xử lý.

## 2. Ba câu thử (dán nguyên văn)
- **Q1 · nên hỏi (chọn 1 trong N):**
  > Hai bridge đều chạy được: bridge X strict hơn về Accept header, bridge Y stateless và tương thích rộng hơn với nhiều client. Cần phục vụ nhiều loại client khác nhau. Chọn bridge nào?
- **Q2 · nên hỏi (lọc/phân loại):**
  > Phân loại 5 phản hồi khách hàng sau vào đúng một nhóm: khiếu nại / hỏi thông tin / khen / khác. (1) “Giao hàng trễ 3 ngày, tôi rất bực.” (2) “Cho hỏi khoá học tháng 10 khai giảng ngày nào?” (3) “Nhân viên tư vấn rất nhiệt tình, cảm ơn.” (4) “Tôi muốn đổi số điện thoại liên hệ.” (5) “Phí học cao hơn quảng cáo, đề nghị giải thích.”
- **Q3 · không nên hỏi:**
  > Dịch câu “The service is healthy” sang tiếng Việt.

## 3. Kịch bản
- **T1 · công tắc Chat giữ nguyên.** Mở chat mới (chế độ Chat) → bấm **+** → **Connectors**. Ghi: JEV Reference `ON` / `OFF` / `KHÔNG CÓ TRONG DANH SÁCH`. Nếu không `ON`: **+ → Connectors → Manage connectors** → bật JEV Reference → ghi “đã bật”. Mở thêm một chat mới nữa, kiểm lại, ghi kết quả lần hai.
- **T2 · Claude Chat.** Ba chat mới, lần lượt Q1, Q2, Q3. Chờ trả lời xong. Mở các khối hoạt động/công cụ trong câu trả lời và ghi cho từng câu: có đọc skill `jev-reference` không; có gọi **JEV Reference · evaluate** không; có báo lỗi không; câu trả lời có nói đã tham khảo Jev không.
- **T3 · Cowork.** Chuyển sang **Cowork**, ba task mới, lần lượt Q1, Q2, Q3; ghi đúng các mục như T2.
- Mỗi câu thử chụp một ảnh vùng câu trả lời + khối công cụ để tự đối chiếu. **Không đưa ảnh vào repo.**

## 4. PASS
- T1: lần kiểm thứ hai là `ON`.
- Chat và Cowork, mỗi bên: Q1 và Q2 có gọi `evaluate`, không lỗi; Q3 **không** gọi.

## 5. KQ (ghi vào cuối `COLLAB.md`, một khối)
```
## KQ — JEV-B2-VERIFY-CODEX-20260922-01
- `KQ@JEV-B2-VERIFY-CODEX-20260922-01 XONG|DỪNG` · <giờ UTC> · Executor: Codex computer use trên Mac Owner
- T1: lần 1 <ON|OFF|KHÔNG CÓ> · hành động <không|đã bật> · lần 2 <ON|OFF>
- Chat: Q1 <skill có/không · evaluate có/không · lỗi có/không> · Q2 <…> · Q3 <…>
- Cowork: Q1 <…> · Q2 <…> · Q3 <…>
- Bất thường: <không | mô tả ngắn>
- FINAL: <PASS|FAIL> theo §4
```
Báo Owner một dòng: `XONG · T1 <..> · Chat <x/2 gọi, Q3 <..>> · Cowork <x/2 gọi, Q3 <..>>`.
