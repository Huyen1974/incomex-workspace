# COLLAB — mow-mot-moit-mout

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
- Mục tiêu: tiếp tục hồ sơ MOW · MOT · MOIT · MOUT từ đúng file gốc Owner đang làm và xây kho thông tin liên quan có tổ chức để phục vụ rà soát/phát triển tiếp.
- Nhiệm vụ/phạm vi hiện tại: giữ nguyên file gốc; tạo `information/`, khảo sát/phân loại và copy các file cần thiết từ `/Users/nmhuyen/Desktop/quy trình`; chưa sửa nội dung HTML chính ở lượt gom tài liệu.
- Tiêu chí xong của lượt hiện tại: tài liệu liên quan được copy có kiểm hash/mục lục, nguồn Mac không bị xoá/di chuyển, file gốc không bị sửa.
- Xác nhận User: **ĐÃ XÁC NHẬN** — Owner giao trực tiếp 2026-09-20; D01–D05 của việc này.

Host: GPT Chat · Host_ID: GPT-MMIM-260920-A · Owner giao: 2026-09-20
HTML chính: `mow-mot-moit-mout.html`
File gốc Owner giao: `mow-mot-moit-mout.html` · SHA-256 `f4aac30c492f104ec54ff7a03ace54ce70d802e2dd49a417ad9b7285897a050c` · import nguyên byte ở commit `569bb74300a15d05e455bf917fe4058f7f7fd499`.
Kho thông tin: `information/`
Agent prompt: `PROMPT.md`

## Dòng hiện hành
MMIM | MOW–MOT–MOIT–MOUT | bước 2/2 | READY · RUN_OWNER_REISSUED | NEXT: Codex chạy MMIM.2 theo PROMPT mới; KHÔNG sửa HTML chính.

## Quyết định Owner
- D01 · 2026-09-20 · Mở công việc tại `work/mow-mot-moit-mout/`.
- D02 · 2026-09-20 · File đính kèm hiện tại là file gốc đang làm; đổi tên trong workspace thành `mow-mot-moit-mout.html`.
- D03 · 2026-09-20 · Phải đưa file gốc lên workspace trước rồi mới viết prompt/giao Codex phần còn lại.
- D04 · 2026-09-20 · Codex tạo `work/mow-mot-moit-mout/information/`, tự đề xuất cách tổ chức bên trong và đưa các file cần thiết/liên quan từ `/Users/nmhuyen/Desktop/quy trình` vào đó.
- D05 · 2026-09-20 · Lượt Codex này chỉ khảo sát, phân loại và copy tài liệu; không được sửa, đổi tên hoặc tái cấu trúc `mow-mot-moit-mout.html`, không xoá/di chuyển nguồn trên Mac.
- D06 · 2026-09-20 · `work/mow-mot-moit-mout/mow-mot-moit-mout.html` là bản làm việc chuẩn của việc này; các bản HTML trên Mac chỉ đọc/đối chiếu, không chép đè.
- D07 · 2026-09-20 · Owner chấp nhận repo/tài liệu việc này có thể công khai để ưu tiên tốc độ và chất lượng; không đưa credential, dữ liệu cá nhân nhạy cảm hoặc nội dung không công khai không cần thiết lên repo.

## Kế hoạch
- MMIM.1 | Tạo work + import file gốc, đổi tên thống nhất | ✅ `569bb74300a15d05e455bf917fe4058f7f7fd499`
- MMIM.2 | Codex khảo sát thư mục nguồn, đề xuất cấu trúc `information/`, copy + kiểm hash + lập mục lục | ▶ READY/RUN

## Ý kiến (P)
Reviewer: Claude Chat · Based_on `39cc96d` / commit review `f5f97fc`. Host GPT đã đối chiếu lại HTML chính và README §12 trước khi xử lý.

- P01 · Scope COLLAB §0 · **REJECTED trong lượt này** · Claude đề nghị mở rộng mục tiêu toàn việc sang “thiết kế chuẩn UI + quy trình tạo/khai báo thành công MOW/MOT/MOIT/MOUT/Field”. Đây là thay đổi A0; trong tin nhắn hiện tại Owner chỉ quyết rõ việc công khai có lọc nhạy cảm, chưa xác nhận lại câu mục tiêu rộng đó. Giữ nguyên §0 đã xác nhận. Khi Owner xác nhận mục tiêu rộng, mở D mới và cập nhật A0 riêng; không dùng lời Reviewer để thay Owner. · Claude vòng 2 (Based_on `17b5470`): câu mục tiêu không phải đề xuất của Reviewer mà là nguyên văn Owner gõ khi giao Claude review (chat 2026-09-20). Đồng ý A0 cần Owner xác nhận rõ → chuyển **OWNER**. Không chặn MMIM.2 (thu thập không mâu thuẫn mục tiêu rộng).
- P02 · Scope PROMPT §2A/§3/§6 · **PARTIAL** · ACCEPT chẩn đoán NFD và yêu cầu `LINK-MAP`; GPT kiểm thật meta `project-assets-root` ghi NFD và README §12.3 hiện chỉ mirror một HTML. Không nhận đề nghị đưa `assets/` ra cạnh HTML ngay trong MMIM.2 vì D04–D05 của Owner yêu cầu lượt này chỉ gom vào `information/` và cấm sửa sản phẩm. PROMPT mới stage phụ thuộc dưới cha ASCII `information/direct-dependency/source-assets/`, kiểm 16 ảnh + manifest + mọi file-ref tương đối. Việc đổi đường dẫn HTML/Owner View là lượt riêng sau MMIM.2, chưa RUN.
- P03 · Scope public safety · **ACCEPTED theo quyết định Owner 2026-09-20** · repo được phép công khai để ưu tiên tốc độ/chất lượng; chỉ loại thông tin thật sự quá nhạy cảm/không cần thiết. PROMPT chặn credential/secret, định danh cá nhân rủi ro, dữ liệu tài chính/cá nhân và tài liệu không công khai cần bảo vệ; không tự loại tên người/tên công ty/thông tin nghiệp vụ công khai. File >50MB hoặc tổng >250MB được ghi nhận để tránh làm chậm/đẩy file lớn.
- P04 · Scope đúng bản · **ACCEPTED** · bản repo `mow-mot-moit-mout.html` là working SSOT của việc; Mac read-only. Codex đọc các sổ chỉ đường nếu có, so SHA bản Mac và SHA nguồn được HTML ghi; lệch thì ghi divergence, không chép đè.
- P05 · Scope UI runtime · **ACCEPTED** · UI đang chạy lấy VPS root `ui` làm thực địa theo A8; bản HTML/JS/CSS tương ứng trên Mac không được xếp CURRENT. Nếu cần đối chiếu thì LEGACY/MAC_RUNTIME_COPY; MMIM.2 không fetch runtime VPS.

## Owner cần quyết
- P01 · Xác nhận mục tiêu toàn việc (A0): “thiết kế chuẩn các UI, chuẩn quy trình tạo và khai báo thành công MOW/MOT/MOIT/MOUT/Field”; tiêu chí xong = mỗi đối tượng có UI chuẩn Owner chốt + quy trình tạo/khai báo viết thành bước + ≥1 lần khai báo thật thành công có bằng chứng. Đề xuất: GẬT → Host mở D08 + sửa §0; MMIM.2 không phải chạy lại.

## Giao Agent
- READY@`7d8e1df9e50cfdd5a4b7cfaf8c66cad9343e26f3` · commit cuối chạm `PROMPT.md` sau xử lý P02–P05.
- RUN · GPT phát lại theo ủy quyền Owner hiện hành, đúng phạm vi D04–D07; thay RUN cũ đã mất hiệu lực khi prompt đổi.

## NEXT
- Codex đọc AGENTS → COLLAB → PROMPT, kiểm READY SHA rồi thực hiện MMIM.2. Không sửa HTML chính, không đổi Owner View.
