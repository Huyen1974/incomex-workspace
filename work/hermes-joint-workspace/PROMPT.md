# CODEX — HJW-N2-DOT-NATIVE-MAX-20261027-05

RUN_ID: HJW-N2-DOT-NATIVE-MAX-20261027-05
TRẠNG THÁI: Chỉ RUN khi Host READY đúng last-touch PROMPT SHA ở HJW COLLAB + Owner chuyển lệnh. Không tự STARTED.
Executor_Surface: Codex Mac; Dot thật trên bề mặt OpenAI đã có.
Task: work/hermes-joint-workspace · Repo: Huyen1974/incomex-workspace
Write_Path: tài liệu qua workspace_* / fs_* D12; Dot/Codex Cloud/Work dùng native tools và quyền đang có; không ghi VPS production.

## 0. MỤC TIÊU NATIVE-MAX

Đọc AGENTS.md, HJW COLLAB §1–§3, P415–P422 và PROMPT. Owner chốt hướng KHAI THÁC TỐI ĐA năng lực Dot do hãng cung cấp và kết nối Incomex chạy ổn định. Dot đọc/nêu ý kiến hội đồng, báo cáo, trao đổi thoại, điều phối Codex/Work khi có sẵn; không dựng cổng/bridge/SSH/proxy/credential mới vì công cụ hãng không có một chức năng mong muốn.

Giữ AGENTS A2: chỉ 1 phiếu quorum cho 1 trusted server-side identity. Dot dùng chung gpt-web với GPT vẫn được nêu ý kiến và làm việc, nhưng KHÔNG tính một phiếu độc lập. Trong hồ sơ tách SOURCE_AUTHOR (Dot task/provider hoặc Owner-confirmed với mức chứng cứ rõ) và WRITE_ACTOR (principal do Gateway/công cụ thực thi xác minh). Tên client tự khai không biến thành trusted actor.

BA MỨC KẾT QUẢ:
A NATIVE_MAX_INDEPENDENT: actor Dot thực sự riêng với GPT, một phiếu không trùng, audit/receipt đủ; chỉ cập nhật roster/quorum khi tuân A2/A9 và quyền hợp lệ.
B NATIVE_MAX_WITH_LIMITS: Dot thật làm được việc hữu ích bằng đồ hãng với dấu vết đúng khả năng chứng minh, nhưng shared actor nên KHÔNG thêm phiếu. B là XONG giai đoạn native có giới hạn, không phải FULL_INDEPENDENT_SEAT; không mặc định đề nghị tạo chìa/cổng.
C CLIENT_ONLY_PENDING / VENDOR_LIMIT: còn thao tác chính chủ hoặc hãng không hỗ trợ; ghi chính xác, không giả PASS, không sinh dự án mở rộng.

Thoại/điều phối Codex được thử SONG SONG, không đợi ghế/quorum độc lập. Các mục Directus/PG/Graph/Lark, S4/root/GSM, +1 Agent Data recreate giữ lịch sử, KHÔNG là gate NATIVE-MAX; chỉ làm khi Owner chọn vì việc thực tế.

Tài liệu hãng: https://help.openai.com/en/articles/20001530-getting-started-with-your-dot
https://help.openai.com/en/articles/20001529-dots-privacy-security-and-safety-faqs
https://help.openai.com/en/articles/20001545-using-codex-cloud

## S0 — CỔNG THỰC DỤNG

Codex kiểm HJW HEAD, roster, Host READY đúng SHA, Owner RUN, STOP/active Codex sessions. Kiểm Dot/plugin đã có, không bắt tạo mới. Đọc repo không cần VPS-GHI. Nếu cần Owner bấm một nút UI, ghi một hướng dẫn ngắn sau; không giữ CLI hoặc lease để chờ. Không xin lại quyền Gmail/GSM/root đã có.

## S1 — DOT THẬT: ĐỌC, Ý KIẾN, DẤU VẾT

Dot thật (không phải GPT/Codex giả lập) đọc AGENTS, HJW COLLAB/Bảng và HEAD, đưa một nhận định ngắn về tình hình nhiệm vụ với commit hiện hành. Kiểm evidence hãng: Dot task/profile link hoặc ID nếu có, timestamp/kết quả, mức độ chắc chắn của SOURCE_AUTHOR.

Nếu Dot được phép ghi qua workspace Gateway D12, thử một ý kiến P CANARY NONVOTING và ghi operation_id/commit/receipt/WRITE_ACTOR thực. Nếu Dot chưa thể ghi thì Owner có thể giao Codex chuyển hộ nguyên văn, nhưng hồ sơ phải ghi WRITE_ACTOR=Codex, SOURCE_AUTHOR=Dot và link/Owner witness; không giả rằng Dot trực tiếp ghi. Không mở thêm key chỉ để đạt bước này.

Một thử âm nhỏ: tự chép tên Dot khi dùng gpt-web không được tính thành phiếu thứ hai. Không sửa A2/quorum để ép PASS. Nếu provider/B1 đã có trusted Dot principal thật thì đo và dùng, không bắt chờ một giải pháp mới.

## S2 — THOẠI VÀ CODEX/WORK THEO HÃNG

Owner có thể chủ động gọi Dot hỏi "HJW đang ở đâu?" để Dot đọc HEAD và báo. Nếu Owner chưa gọi thì VOICE_PENDING, không giữ terminal chờ và không giả PASS.

Nếu Codex Cloud environment đã publish, Dot thử một Cloud task CHỈ ĐỌC và trả task ID/kết quả. Không bắt thiết lập environment mới chỉ để nghiệm thu. Work/Codex Local chỉ thử khi Owner đã bật Computers > Your computer > Allow access và Mac online; nếu chưa thì LOCAL_PENDING, không chặn Cloud/Voice.

Không khẳng định Dot gọi được một phiên GPT/Claude đang mở nếu chưa có đường hãng. Không dựng courier/MCP bridge. Ghi repo qua D12 theo đúng quyền, không native push lách luật. Gmail đọc không hỏi/ghi hỏi trước; không gửi thư ra ngoài để thử.

## S3 — BÁO A/B/C, KHÔNG MUA THÊM RẮC RỐI

Bảng 6 ô bắt buộc: Dot đọc HJW/HEAD; Dot opinion/nguồn; WRITE_ACTOR/receipt; phiếu quorum có thêm không; Voice; Codex Cloud/Local. Mỗi ô PASS/PARTIAL/CLIENT_PENDING/VENDOR_LIMIT/NOT_TESTED, chỉ rõ bằng chứng hoặc giới hạn. Chốt A/B/C.

Không chạy lại suite TQT, image candidate P415 hay Guard #11 khi RUN không thay mã/VPS. DROOT59 giữ nợ giám sát đúng chủ, không gọi lỗi có trước thành blocker mới. Nếu B: báo "Dot tham gia được, chưa có phiếu quorum riêng"; không tự xin cấp chìa. Nếu A: chỉ thêm roster sau chứng cứ đầy đủ. Nếu C: chỉ một danh sách nút chính chủ cần bấm.

## S4 — KQ VÀ ĐÓNG PHIÊN

Ghi HJW COLLAB + Bảng/roadmap đúng cấp đạt, với SHA/receipt thật. KQ XONG cho NATIVE-MAX nếu có hành động Dot thực tế hữu ích và truy vết đúng cấp, kể cả B có giới hạn. Không gọi toàn N2 FULL_INDEPENDENT khi phiếu còn shared. Nếu không thử được Dot thật thì DỪNG/CLIENT_PENDING. Không mở task khác, không giữ process/lease chờ Owner.

CẤM: cấp/chuyển key/root/GSM, làm gateway/SSH/proxy/Agent Data recreate, thay Directus/PG/Graph/Lark, mở Auto hội đồng hay thay Host, tạo phiếu thứ hai từ gpt-web, sửa Gmail settings, ép dashboard xanh.

STEP_WALK_V1:
| Bước | Ai/Trigger | Evidence | Thiếu thì |
|---|---|---|---|
| S0 | Codex / Owner RUN + Host READY | HEAD/roster/scope | DỪNG |
| S1 | Dot thật/Codex chứng thực | Dot source vs Write Actor/receipt | mức B/C trung thực |
| S2 | Owner/Dot | Voice/Cloud/Local task khi có | CLIENT_PENDING |
| S3 | Codex | Bảng 6 ô + A/B/C + quorum | không bắt key mới |
| S4 | Codex | KQ/commit/0 VPS mutation/NEXT_TRIGGER | DỪNG có bằng chứng |

BÁO OWNER 3 CÂU: Dot làm được gì? Có thêm phiếu riêng không? Cần Owner bấm gì nếu có?
