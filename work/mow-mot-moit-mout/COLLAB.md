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
MMIM | MOW–MOT–MOIT–MOUT | bước 2/2 | READY · RUN_OWNER | NEXT: Codex chạy MMIM.2 theo `PROMPT.md`; KHÔNG sửa HTML chính.

## Quyết định Owner
- D01 · 2026-09-20 · Mở công việc tại `work/mow-mot-moit-mout/`.
- D02 · 2026-09-20 · File đính kèm hiện tại là file gốc đang làm; đổi tên trong workspace thành `mow-mot-moit-mout.html`.
- D03 · 2026-09-20 · Phải đưa file gốc lên workspace trước rồi mới viết prompt/giao Codex phần còn lại.
- D04 · 2026-09-20 · Codex tạo `work/mow-mot-moit-mout/information/`, tự đề xuất cách tổ chức bên trong và đưa các file cần thiết/liên quan từ `/Users/nmhuyen/Desktop/quy trình` vào đó.
- D05 · 2026-09-20 · Lượt Codex này chỉ khảo sát, phân loại và copy tài liệu; không được sửa, đổi tên hoặc tái cấu trúc `mow-mot-moit-mout.html`, không xoá/di chuyển nguồn trên Mac.

## Kế hoạch
- MMIM.1 | Tạo work + import file gốc, đổi tên thống nhất | ✅ `569bb74300a15d05e455bf917fe4058f7f7fd499`
- MMIM.2 | Codex khảo sát thư mục nguồn, đề xuất cấu trúc `information/`, copy + kiểm hash + lập mục lục | ▶ READY/RUN

## Ý kiến (P)
Reviewer: Claude Chat · Based_on `39cc96d` · Đã đọc: AGENTS, README §8/§12, COLLAB, PROMPT; HTML chính: `<head>`, khối bàn giao dòng 508–562, quét toàn file mọi `src/href`/tên file. Chưa đọc: phần nghiệp vụ còn lại của HTML; thư mục Mac; `image-manifest.json`.
Đề nghị Host: sửa PROMPT theo P02–P05 → READY `6db6d6e` tự vô hiệu (A6) → READY lại. Owner cho biết chưa giao Codex nên chưa có lượt chạy dở.

- P01 · Claude · Scope COLLAB §0 · OPEN · Owner nêu trong chat 2026-09-20 mục tiêu thật: **“thiết kế chuẩn các UI, chuẩn quy trình tạo và khai báo thành công MOW/MOT/MOIT/MOUT/Field”**; §0 hiện chỉ ghi “tiếp tục hồ sơ + xây kho thông tin”, thiếu Field → theo A0 Host cập nhật §0 và xác nhận lại với Owner. Đề nghị: Mục tiêu = câu của Owner nguyên văn · Phạm vi = 5 đối tượng MOW · MOT · MOIT · MOUT · Field, đi từng bước; bước hiện tại MMIM.2 = dựng kho `information/` · Tiêu chí xong cả việc = mỗi đối tượng có (1) bộ UI chuẩn Owner chốt, (2) quy trình tạo/khai báo chuẩn viết thành bước, (3) ≥1 lần khai báo thật thành công có bằng chứng (ghi vào dữ liệu thật, mở lại UI thấy đúng). MMIM.2 không mâu thuẫn mục tiêu mới; chỉ thêm Field vào tiêu chí chọn nguồn.
- P02 · Claude · Scope PROMPT §2A + §3 + §6; HTML `<head>` meta `project-assets-*`/`project-image-manifest` + 16 `<img>` · OPEN · **Chặn kỹ thuật: làm đúng PROMPT hiện tại thì ảnh vẫn vỡ.** Đo trên repo: 16 `src` + meta manifest trỏ tương đối `Từ thực tế đã làm/assets/…` từ vị trí HTML, tên thư mục dạng **NFD** (tìm chuỗi NFC: 0 kết quả; meta dòng 8 xác nhận). Ba lỗi chồng: (a) PROMPT dồn mọi thứ vào `information/` + cấm sửa HTML → đường dẫn không bao giờ khớp; (b) git trên Mac thường bật `core.precomposeunicode` → tên NFD bị commit thành NFC, lên Linux/VPS/GitHub lệch byte với `src` dù đặt đúng chỗ; (c) nút Cập nhật Owner View (README §12.3) chỉ kéo 1 HTML → ảnh không lên VPS. Đề nghị: (1) MMIM.2 copy 16 ảnh + `image-manifest.json` vào `work/mow-mot-moit-mout/assets/` (tên ASCII; A1 cho assets nằm trong thư mục việc; đây là phụ thuộc của sản phẩm, không phải tài liệu tham khảo). Manifest ghi đường tính từ thư mục cha của `assets/` nên giữ nguyên byte vẫn đúng — Codex kiểm từng entry trỏ tới file có thật. PROMPT §6 mở thêm `assets/**`. (2) README `information/` có **bảng link-map**: mọi `src/href` tương đối trong HTML (16 ảnh, meta manifest, `00-NGUON-THIET-KE.html` · `cấu trúc hệ thống.html` · `BAN-DO-BUOC-UI-AGENT.html` · `TAO-MOT-QUY-TRINH.html`, 2 link `../` dòng 2064 vốn đã gãy ngay trên Mac) → đường thật trong repo hoặc `MISSING`. (3) MMIM.3 là việc riêng (đúng luật “đổi vị trí ảnh là nhiệm vụ riêng” ghi trong chính HTML), Host làm qua MCP, không cần Codex: một `fs_edit` thay tiền tố theo link-map có `expected_count`, kiểm đủ 16 ảnh hiện được, ghi SHA mới. Cho Owner View kéo thêm `assets/` là đổi hợp đồng §12.3 → D ở COLLAB gốc, không tự làm.
- P03 · Claude · Scope PROMPT §2 cuối + §5 · OPEN · Repo đang **PUBLIC**; PROMPT chỉ chặn secret, chưa chặn dữ liệu cá nhân/nội bộ — copy vào đây là công bố ra internet. Đề nghị thêm: (1) file có dữ liệu người thật (họ tên kèm SĐT/CCCD/hộ chiếu/ngày sinh/địa chỉ) hoặc hợp đồng/giá/đối tác → KHÔNG copy, ghi `OMITTED_PUBLIC` cho Owner quyết; xlsx/docx/pdf phải mở xem nội dung rồi mới xếp, không xếp theo tên; (2) nghiệp vụ phái cử/lao động xuất khẩu ngoài phạm vi việc này → không copy; (3) trần: 1 file >20 MB hoặc tổng >150 MB → dừng ở file đó, ghi README (GitHub cảnh báo 50 MB, chặn 100 MB/file).
- P04 · Claude · Scope PROMPT §1–§2; HTML khối `#quy-tac-dong-bo-chat-local` · OPEN · **Đúng bản + một tài liệu duy nhất.** Chính HTML ghi: trên Mac có 2 file cùng tên `từ thực tế đã làm.html` — bản ở gốc `quy trình/` là hiện hành, bản trong thư mục con là bản cũ 14/09, không dùng. Đề nghị: (1) Codex tính SHA bản gốc Mac; khác `f4aac30c…` → không chép chồng bên nào, ghi 2 SHA, DỪNG phần HTML để Host đối chiếu; bản thư mục con xếp D; (2) nguồn có SHA ghi sẵn trong HTML (`TAO-MOT-QUY-TRINH.html` `f6563893…`) → so, ghi khớp/lệch; (3) trước khi phân loại, đọc các sổ chỉ đường đã có trên Mac nếu còn (`00-DOC-TRUOC.md`, `KHO/00-CANH-BAO-DOC-TRUOC.txt`, `KHO/00-NHAT-KY-DON-DEP.txt`) và kế thừa nhãn lỗi thời đã gắn, không phân loại lại từ đầu; (4) đề nghị Owner D06: từ commit `569bb74` bản repo là **bản làm việc duy nhất**, bản Mac đóng băng chỉ đọc; meta/khối bàn giao trong HTML đang trỏ về Mac sửa cùng MMIM.3.
- P05 · Claude · Scope PROMPT §2B–C · OPEN · HTML dẫn ~30 UI đang chạy tại `vps…/ui-preview/mcp-writes/` — đó là thực địa, gốc ở VPS root `ui` (A8). Mac có thể giữ bản chép cũ của các file này. Đề nghị: không copy HTML/JS/CSS của UI xưởng vẽ vào `information/` như nguồn hiện hành; nếu cần giữ để đối chiếu thì xếp D, ghi “bản chép Mac, thực địa = root `ui`”. Con trỏ UI thật (path + version) lập ở bước sau qua MCP, ngoài lượt này.

## Owner cần quyết
- —

## Giao Agent
- READY@`6db6d6e31319008161e8b10f1e22b55b0a2b8f02` · commit cuối chạm `PROMPT.md`.
- RUN · Owner giao trực tiếp trong chat ngày 2026-09-20; GPT truyền lệnh trong đúng phạm vi D04–D05.

## NEXT
- Codex đọc AGENTS → COLLAB → PROMPT, kiểm READY SHA rồi thực hiện MMIM.2.
