# PROMPT — HJW / N3 · HERMES MAC: LOCAL OPENROUTER + REMOTE VPS
RUN_ID: HJW-N3-MAC-DUAL-20261011-01
STATUS: DRAFT_P285_REVIEWER_EDITED · OWNER_SCOPE_11_10_19H24 · Claude Reviewer sửa ba chỗ khi còn DRAFT (AGENTS A6: nút Update, bằng chứng giao diện, hỏi key trong lượt) và ký ở P285 theo SHA last-touch của tệp này · CHƯA READY/RUN
Host: GPT Chat · GPT-HJW-260922-A
Reviewer: Claude Chat · claude-main (một lượt review theo A6, đúng SHA)
Executor_Surface: Claude Code CLI chạy TRÊN MACBOOK CỦA OWNER, Owner tự dán khi Host đã READY
Write_Path: Mac local qua CLI trong scope được Owner cho phép; sổ Git chỉ qua Incomex workspace_* và version/CAS
Node: N3 · K3, PHA MAC LOCAL+REMOTE. Không phải hoàn thành toàn bộ N3.
Owner_steps: Sau Reviewer ACCEPT và Host READY, Owner dán đúng một lệnh cho Claude Code CLI trên MacBook. Nếu cần OpenRouter key mới, chỉ một yêu cầu Owner thao tác kín qua trang nhà cung cấp; không dán key vào chat/repo/log. Trong lượt chạy Owner ở cạnh máy để bấm vài bước trên Hermes Desktop khi CLI hỏi; mỗi câu hỏi có hạn 10 phút.

## 0. MỤC TIÊU (CHỈ VIỆC NÀY)
Hermes VPS đã hoạt động và đã gọi được. Giữ nguyên hoàn toàn Hermes-VPS. Trên MacBook, đảm bảo hai chế độ:
1. Hermes Desktop vẫn kết nối **Remote** để làm màn hình cho Hermes VPS đang chạy.
2. **Hermes Local** chạy backend/agent riêng trên MacBook, dùng **API model OpenRouter**, có session, config, credential, data và nhận diện riêng, không lẫn với Hermes VPS.
Một ứng dụng Desktop có Local + Remote và registry đa kết nối là ưu tiên. KHÔNG giả định phải cài hai ứng dụng; phải kiểm chứng khả năng của phiên bản đang cài. Kết quả hiện hữu không phá hỏng.
**Ngoài phạm vi:** Không nghiên cứu hay gọi API vào tài khoản thuê bao ChatGPT/Claude, không xin API key Anthropic/OpenAI, không tạo Claude Routine, không thử chuyển tin tự động tới AI web trong lượt này, không xây gateway/DB/cron/transport mới, không sửa máy chủ VPS. Không sửa N1/N2/N4–N6/T1–T9.

## 1. STEP_WALK (MỘT LƯỢT, KHÔNG MỞ PRE-CHECK THÀNH RUN KHÁC)
| Bước | Người làm / kích hoạt | Chứng cứ cần đạt | Nếu vướng |
|---|---|---|---|
| 1. Gate + kiểm kê | Claude Code trên Mac, sau READY/Owner paste | Đọc AGENTS A0/A6/A9/A10, root COLLAB, HJW A0/0.17/Bảng/P284+chỉ đạo mới, PROMPT hiện tại; kiểm 0 STARTED/STOP; xem binary/app version, Local/Remote, profile/gateway, khoá đồng bộ phiên bản Mac↔VPS; không đọc/in secret | Thiếu quyền/không khớp READY: DỪNG sạch, một lý do |
| 2. Giữ cái đang chạy | Claude Code | Thử Remote UI→VPS hoạt động trước sửa; sao lưu có thể khôi phục phần config Mac sắp đụng; không lấy credential VPS sang Local | Remote lỗi: ghi lỗi, không đụng VPS |
| 3. Bật Local | Claude Code | Theo docs đúng version đang cài, tận dụng Hermes Local runtime/profile đã có; nếu chưa có mới cài tối thiểu tương thích, không auto-update phá cơ chế ghim version; Local state/config riêng. Tài liệu hãng đọc 11/10: hermes-agent.nousresearch.com/docs/user-guide/multi-connection-desktop. **Cấm bấm nút Update, "Update all instances" và cấm chạy `hermes update` trong lượt này:** theo tài liệu đó, khi app có nhiều kết nối thì nút Update gửi lệnh cập nhật tới mọi kết nối đủ điều kiện, tức có thể cập nhật cả Hermes VPS | Không hỗ trợ/khác version: DỪNG, nêu một phương án nhỏ nhất; không tự nâng cả VPS |
| 4. OpenRouter | Claude Code/Owner nếu thiếu key | Dùng credential Mac riêng đã được phép, model OpenRouter được hỗ trợ; khóa không vào chat, repo, process args hay log; chi phí có giới hạn | Thiếu key: hỏi Owner đúng một lần ngay trong lượt, kèm hướng dẫn từng bước bấm; Owner tự tạo key có hạn mức ở trang OpenRouter và dán vào ô nhập khoá của Hermes Desktop khi đang chọn kết nối Local (hoặc cách nhập kín khác do CLI chỉ), không dán vào CLI/chat. Hạn 10 phút; quá hạn thì KQ DỪNG, nhả terminal |
| 5. Thử thật cả hai | Claude Code | (a) Local gửi một yêu cầu đơn giản → provider OpenRouter trả lời thật; (b) Remote kết nối lại Hermes VPS và đọc được phiên đang có; (c) chuyển đi/về không trộn lịch sử, profile, model, credential; (d) Local ngắt thì VPS vẫn chạy và Remote vẫn dùng. Chọn và chuyển kết nối chỉ làm được trên giao diện Hermes Desktop (tài liệu hãng không có lệnh CLI): CLI đưa Owner từng bước bấm ngắn và xác nhận bằng ảnh chụp màn hình hoặc một câu có/không của Owner, mỗi câu hạn 10 phút; không suy ra PASS chỉ từ tệp cấu hình | Fail thì rollback đúng phần Mac mới đổi, giữ VPS nguyên |
| 6. Ghi KQ | Claude Code | Một KQ XONG hoặc DỪNG ở HJW COLLAB + Bảng, có bản Hermes/version, đường Local/Remote, PASS/FAIL từng thử, Mac files đã đổi (không secret), điểm lùi, một dòng cảnh báo Owner không bấm Update trong Hermes Desktop khi chưa có lệnh của Host; không mở việc mới | Chưa chứng minh thì KHÔNG tuyên bố MAC_PASS |

## 2. ĐIỀU KIỆN XONG
- **MAC_PASS** khi Remote→Hermes VPS và Local→OpenRouter đều chạy thật và độc lập; khi đổi chế độ không mất/chồng dữ liệu; không thay đổi VPS; rollback có thể làm được.
- **N3 chưa PASS chỉ vì MAC_PASS.** Sau phần này mới làm tiếp courier/điều khiển AI bằng công cụ Hermes theo khả năng và chính sách cho phép, T9 và các residual thực tế. Không lấy kết quả Hermes gọi model OpenRouter làm phiếu của GPT/Claude trong hội đồng.
- Lỗi vé -05/WRITE_CONFLICT N3-2a và thử bấm muộn vẫn là residual của N3; xử lý gọn riêng đúng chủ, không biến thành gate chặn cài Hermes Local trên Mac.
- MacBook có thể ngủ/tắt; điều đó không được ảnh hưởng Hermes-VPS. Không mở cổng inbound mới, không đặt Mac luôn trực 24/7.
- Không đưa bất kỳ key/token/cookie vào báo cáo; không tắt Guard/bảo vệ; thay đổi chỉ trong phạm vi Mac đã được Owner giao; không nâng phiên bản chỉ để đạt một tính năng chưa kiểm chứng.

## 3. QUYỀN VÀ TRẠNG THÁI
Đây là DRAFT thay thế hoàn toàn PROMPT N3-2B official API/Routine đã bị Owner bác về phạm vi. Git giữ lịch sử bản cũ. Reviewer Claude Chat rà 1 lượt đúng SHA, Host mới READY; Owner mới tự giao Claude Code. Không có STARTED/automatic RUN khi chưa đạt A6. Nếu điều kiện kỹ thuật khó thật mới hỏi một lần đúng blocker, không tạo thêm roadmap hay test riêng.
