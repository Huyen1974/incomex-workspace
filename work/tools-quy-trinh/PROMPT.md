# PROMPT — TQT GỐC CÂU HỎI · Chuỗi/Tầng/Bước (gồm Bước con)

## Phạm vi hiện hành · Owner giao trực tiếp 08/10/2026
Host: **Astra Codex**, phiên Owner chỉ định. Làm UI Câu hỏi cơ bản theo Công thức, ma trận câu hỏi là SSOT và bộ ghép nghiệp vụ UI/Test/Config. Giữ nội dung cũ; không thay định nghĩa Công thức hay dựng UI thứ 2. Mục tiêu nguyên văn: COLLAB.md §0 ô 1 bổ sung 08/10. Cách sửa nguồn và nộp góp ý: README.md.
Nguồn mới: `view.html#tqt-question-matrix`; bảng cho người và AI: `view.html#ma-tran-cau-hoi`. Bộ câu hỏi đang hiệu chỉnh, chưa nghiệm thu. Chỉ Host nhập ý kiến đã xem xét; thành viên khác chỉ đề xuất riêng.
Kiểm giao diện và liên kết thật sau đồng bộ; không lấy UI chạy được để tuyên bố bộ câu hỏi đã đủ.
Tiếp theo: thử MOW-NHC-001 với bộ câu hỏi áp dụng và quy tắc `rules` trong cùng JSON. Bàn giao câu trả lời theo mã/phạm vi, nguồn/phiên bản, bằng chứng hoặc chỗ thiếu; đối chiếu Nhóm cha/con, MOW/MOT và chỗ bàn giao. Chỉ ra căn cứ suy ra trường/nút/trạng thái UI, nguồn cần sửa, đề xuất tách bước nếu thật sự cần. Kết quả thử phải có DOER_CONFIRM đúng phạm vi; chưa có kết quả thì không nhận đã đủ. Không làm MOW 002.

## Hồ sơ yêu cầu trước — đã được chỉ đạo trên thay thế, giữ để truy nguồn
Các giới hạn READ-ONLY/Host GPT Chat trong phần lưu vết dưới đây không phải lệnh hiện hành cho Host mới.

STATUS: **DRAFT · READ-ONLY REVIEW REQUEST · CHƯA READY/RUN SỬA NGUỒN**
Host: GPT Chat (OpenAI-main) · Codex: người rà và đề xuất theo Owner 08/10.
PROCESS: CHUNG.APQUYTRINH — chỉ đối chiếu, chưa là lệnh RUN.
MOW001→002 UI PROMPT cũ: **SUPERSEDED TRƯỚC READY**, giữ bản cũ trong Git history; **KHÔNG vẽ MOW 001 hoặc 002 ở lượt này**.
Write zone: file đề xuất riêng `work/tools-quy-trinh/proposals/TQT-PR-20261008-codex-root-questions-01.md` nếu được phép ghi đề xuất; nếu không, trả toàn bộ nội dung dưới chat cho Host, không bypass/quét credential.
**CẤM sửa** `work/tools-quy-trinh/{COLLAB.md,README.md,view.html,PROMPT.md}`, mọi `ui/*`, file chuẩn `work/mow-mot-moit-mout/*`, bảng PG/Directus và công thức/Master chính. Không tạo task/Master/dữ liệu mới.

## 1 · Mục đích của lượt này
Owner chỉ ra: thiếu câu hỏi bắt buộc ngay trong công thức gốc, khiến lúng túng khi vẽ UI. Phải **đặt câu hỏi riêng ở gốc**, kiểm từng thành phần, rồi ghép và bổ sung bộ câu hỏi nghiệp vụ UI/Config. Nếu thêm một Bước con, nó tự có câu hỏi cần trả lời và kế thừa đúng câu hỏi gốc, không đắp vá hàng nghìn bản MOW/MOT.

**Ba nguyên liệu gốc:**
- `CT-001` **Bước** gồm **Bước lớn và Bước con** (không biến Bước con thành nguyên liệu độc lập thứ tư).
- `CT-002` **Tầng/đối tượng**: Field T0; MOIT/MOUT cùng T0.5 nhưng khác loại; MOT T1; MOW T2.
- `CT-002.1` **Chuỗi**: CTCM, VHCM, CMSXQT (SSOT mã/tên tại `ui/chuoi-data-v1.js`).

**Quy tắc ghép đang có, giữ nguyên:** CT-003 Chuỗi+Bước+Tầng⇒Nhóm cha; CT-004 Chuỗi+Bước con+Tầng⇒Nhóm con; CT-005 Chuỗi+Bước+Tầng+Nhóm cha⇒MOW; CT-005.1 Chuỗi+Nhóm con⇒MOT. Bộ câu hỏi chuyên môn (UI, Config…) chỉ thêm **SAU khi ghép**, không lẫn vào câu hỏi của nguyên liệu gốc.

## 2 · Đọc đúng nguồn, bản mới nhất
1. `AGENTS.md` → `work/tools-quy-trinh/COLLAB.md` §0/Host → `README.md` và `view.html#quy-trinh-hieu-chinh`, `#ra-ui` và 9 Tools; đọc `work/mow-mot-moit-mout/{README.md,FORMULA-AI-README.md,CHANGE-PROPAGATION.md,CHANGE-IMPACT-MAP.json}`.
2. Root `ui` READ ONLY: `definition-master-data-v1.js` CT001/002/002.1/003/004/005/005.1 và ML-DEF-001/002/004/005/021; `chuoi-data-v1.js`. Nguồn người: `work/mow-mot-moit-mout/ban-duyet.html#formula-root-1` (dùng nguồn formula nếu portal đăng nhập chặn). Ghi path/phiên bản thực tế; không đoán source từ chat.
3. Baseline cần kiểm: **9 Bước lớn; 23 Bước con B1–B7, B8/B9 chưa bóc; 5 loại Tầng; 3 Chuỗi**. Dataset CH-001 đã có 35 Nhóm cha, 115 Nhóm con, 35 MOW và MOT dẫn xuất. Đây là **số kiểm kê**, KHÔNG yêu cầu sinh tích 9×5×3 hay thêm B8/B9.
4. Một ca mẫu duy nhất: `MOW-NHC-001`, CH-001/CTCM+B1 Tìm+T0 Field+NHC-001 với Bước con 1.1 Tìm thường, 1.2 Tìm nâng cao, 1.3 Xác nhận phù hợp; 3 MOT từ 3 Nhóm con. **MOW 002 chưa làm**.

## 3 · Sản phẩm Codex phải đề xuất
**A. Rà gốc đã có/chưa có:** liệt kê nguồn định nghĩa và câu hỏi hiện hữu cho Chuỗi, Tầng, 9 Bước lớn và 23 Bước con; đánh `CÓ CÂU HỎI / CHỈ CÓ MÔ TẢ / THIẾU / KHÔNG ÁP DỤNG` kèm bằng chứng. B8/B9 thiếu Bước con không có nghĩa phải tự bổ sung. Chỉ ra câu chuyên môn UI/Config đang đặt nhầm tầng nếu có.

**B. Xây bộ câu hỏi tối thiểu và giao diện câu trả lời:** Mỗi câu có `Q_ID | LEVEL_OWNER (CHUOI/TANG/BUOC/BUOC_CON/CHUYEN_MON) | CÂU HỎI | ĐẦU VÀO/NGUỒN TRẢ LỜI | BẮT BUỘC hay N-A có lý do | CÁCH KIỂM | XONG KHI | ISSUE_REF`. Không hỏi trùng: câu ở cấp cha được con kế thừa bằng ID, không chép lại.

Nhóm câu khởi đầu để Codex rà, **chưa được Owner chốt**:
- Chuỗi: mục đích, đầu ra của tiến trình, giới hạn trách nhiệm.
- Tầng: đối tượng nào, Master/bằng chứng tồn tại, quan hệ và các ràng buộc chung theo loại.
- Bước lớn: một nhiệm vụ gì, vào/ra, nhánh kết quả, khi nào thực sự kết thúc, việc gì thuộc Bước khác.
- Bước con: hành động nguyên tử, ai/máy làm, đầu vào, kết quả ra, lỗi/quay lại, bằng chứng, khi nào xem là xong. Vẽ một UI hay tái sử dụng UI là câu hỏi bổ sung **sau khi ghép**, không ép 1 Bước con = 1 mã UI mới.
- Nghiệp vụ **thiết kế UI**: nêu bộ câu hỏi design trước khi vẽ, dùng lại UI cha; phân biệt với **8 câu rà/kiểm UI** hiện có. Nghiệp vụ **Config**: tái sử dụng **7 câu Config** hiện có, đề xuất delta, không ép mọi câu vào mọi bước.

**C. Định nghĩa phép ghép:** với một tổ hợp hợp lệ, dẫn chiếu đúng câu hỏi của Chuỗi, Tầng, Bước lớn, Bước con, sau đó ghép bộ câu hỏi UI hoặc Config. `MISSING` câu bắt buộc → `BLOCKED` có mã; `CONFLICT` hai lớp → chỉ đúng nguồn để quyết; `N-A` có lý do. Cấm sao chép full bộ câu hỏi trên từng dòng MOW/MOT. Định nghĩa rõ khi nào thiếu **Bước con thực sự** (nhiệm vụ mới, có vào/ra và điều kiện xong riêng), khi nào chỉ cần **thêm câu hỏi/nhánh**.

**D. Thử ghép MOW001 trên giấy, không tạo UI:** lập `Q_ID gốc → câu kế thừa → trả lời hiện hành → câu UI/Config thêm → bằng chứng/thiếu ở đâu` cho ba MOT. Không đổi CT-001.
- B1 **Tìm chỉ tìm ra/chưa tìm ra/chưa đủ căn cứ**, không thực thi B2 Dùng, không tạo Field, không biến điểm JEV thành giấy phép dùng.
- Với 1.1/1.2/1.3, xử lý mẫu hai vòng: vector tìm + JEV dựa dữ liệu được cấp; Xanh/Vàng/Đỏ và điều kiện dừng; Vàng có thể sửa yêu cầu/tìm lại; chưa có JEV thật thì ghi GAP OPEN-04, không bịa số liệu.
- Chứng minh câu hỏi nào đủ để xác định trạng thái/hiển thị UI, câu nào còn thiếu Config; điều kiện nào buộc bổ sung hỏi gốc thay vì vá UI ngọn.

**E. Đề xuất vị trí canonical + lan truyền:** mỗi delta `SOURCE_GỐC (CT001/002/002.1) → downstream CT003/004/005/005.1 → Master Nhóm/MOW/MOT → UI/Tools/test → phép kiểm/rollback`. Nếu cần bộ câu hỏi thành Master List, ưu tiên dùng lại Master đã có trước, không tự tạo mới. Việc sửa CT/ML canonical thuộc quyền Host của task MOW/Owner theo quy định, **không mặc nhiên do Codex được ghi**.

## 4 · Nghiệm thu bài ĐỀ XUẤT này
- Một khuôn Q_ID dùng được ở **3 nguyên liệu gốc / 4 cấp đọc**.
- Có kiểm kê 9 Bước lớn, 23 Bước con thực, 5 loại Tầng, 3 Chuỗi theo nguồn; kết quả ngắn gọn, không đòi tự điền tích chéo hàng nghìn tổ hợp.
- Thử ghép riêng MOW001 chứng minh phát hiện thừa/thiếu/xung đột; hai bộ câu hỏi chuyên môn UI và Config **không trùng gốc**.
- Mỗi điều cần sửa ghi đúng SOURCE, câu/bước, bằng chứng và impact; trường hợp chỉ là nhánh thì **không tạo Bước con**.
- Chính Codex ghi `DOER_CONFIRM=YES/NO/PARTIAL`: đọc nguồn có tổ chức được bộ câu hỏi và thử ghép không? Thiếu đầu vào nào vẫn BLOCKED?
- KQ đưa Host: `A. TÓM TẮT | B. BỘ CÂU HỎI GỐC | C. QUY TẮC GHÉP | D. THỬ MOW001 | E. DELTA + DOER_CONFIRM + FILE PROPOSAL`.
- Khi đủ, Host rà bằng chứng, trao đổi Reviewer khác hãng và Owner quyết các thay đổi nghĩa gốc; **chỉ sau đó** cập nhật root/propagation rồi mới phát RUN vẽ MOW001. Không tự xem đề xuất này đã có hiệu lực.
