# PROMPT — TQT-UI-MOW001 → MOW002 · Node A / chuẩn bị Node B
STATUS: DRAFT — CHƯA READY / CHƯA RUN · Host GPT Chat · Owner chỉ đạo 08/10/2026
RUN_ID_DRAFT: TQT-UI-MOW001-20261008-01
PROCESS: CHUNG.APQUYTRINH
Executor_Surface: Codex — phiên Owner giao (xác thực binding khi bắt đầu)
Write_Path: Incomex workspace_* root `ui` (bản UI sống) + root `workspace` (phiếu kiểm tại task MOW, proposal của tools-quy-trinh).
GitHub connector: READ ONLY. Không giả quyền ghi dựa trên tên model; không dùng SQL/PG/Directus ngoài DOT.
GATE: Chỉ được mutation UI/phiếu khi Host đã ghi READY@<full SHA last-touch PROMPT.md>, Owner/Host phát RUN hợp lệ, process gate PASS và một lần read-gate Write_Path PASS. Chưa đủ ⇒ chỉ đọc, ghi proposal, KQ DỪNG; không giữ terminal chờ.

## 0 · Đích Owner — không thiết kế lại công thức
Công thức đã tạo phần lớn quy trình: CT-005 `Chuỗi + Bước + Tầng + Nhóm cha ⇒ MOW`, CT-005.1 `Chuỗi + Nhóm con ⇒ MOT`. Master List dùng lại khi đối tượng có ≥2 dòng; không mở master trùng. Chủ ý công thức phủ phần lớn (~98% là định hướng, không phải đo đã đạt); trường hợp đặc biệt tách issue để bàn riêng.

Đây là **đợt thiết kế UI cho quy trình hướng tới production**, đang ở giai đoạn REVIEW/test phương pháp, chưa phải phát hành backend/ghi dữ liệu production. **Không thay CT-005/005.1, Master MOW, mã MOW/MOT, semantic Owner chốt, không cấp UI canonical mới khi chưa được duyệt.**

NODE A — **hoàn thiện thiết kế UI theo 3 MOT MOW-NHC-001 (B1 · Tìm Field)** và kiểm xem quy trình vẽ UI trong tools-quy-trinh có đủ để agent làm được. Sau KQ, Host sửa/bổ sung quy trình theo proposal, kiểm độc lập rồi mới phát riêng NODE B.

NODE B — **vẽ thử theo 2 MOT MOW-NHC-002 (B2 · Dùng Field)** bằng bản quy trình đã sửa, **trong phiên Codex mới không dùng trí nhớ phiên A**, để chứng minh khả năng tái sử dụng. **NODE B CHƯA ĐƯỢC RUN từ bản prompt này**; có thể đọc nguồn để kiểm kê khi đang làm A.

## 1 · READ-GATE: đọc đúng nguồn, đo thiếu trước khi sửa
1. Repo `Huyen1974/incomex-workspace`: đọc `AGENTS.md`; `work/tools-quy-trinh/COLLAB.md` §0 và Host/roster, `README.md` và `view.html#quy-trinh-hieu-chinh`, `#ra-ui` (6 bước, **8 câu/MOT × 3 và 7 câu Config**, Tool 001…008). **Ba file chính của tools-quy-trinh là Host-only**; Codex chỉ góp ý bằng `proposals/TQT-PR-...`.
2. Task sản phẩm `work/mow-mot-moit-mout/`: đọc `COLLAB.md` §0/Host, `README.md`, `FORMULA-AI-README.md`, `UI-DESIGN-STANDARD.md`, `UI-REVIEW-CONTRACT.json`, `UI-REVIEW-MOW001.json`, `council/REGISTRY.md` và Rules R39–R48 tại `ban-duyet.html`. Nếu thay đổi tiêu chí/tác động nhiều nguồn: đọc `CHANGE-PROPAGATION.md` + `CHANGE-IMPACT-MAP.json`.
3. UI sống root `ui`: đọc `AGENTS.md`, `definition-master-data-v1.js` các row `ML-DEF-004/005/017/018`, `mow-ui-walkthrough-v1.{html,js}`, `tim-kiem-chung-v1.html`, `field-flow-v1.js/css`, `field-flow-model-v1.js`, chính source có liên quan; kiểm phiên bản/hash và các run/owner khác đang chạm cùng path. Không tạo bản sao ở repo thay source VPS. Dùng tool Incomex đúng root/expected_version; git HEAD task khác đổi thì diff target, không tự overwrite.
4. Phải khớp danh tính trước mutation:
   - `MOW-NHC-001` CTCM B1 Tìm T0 Field: **3 MOT/màn** Tìm Field → Tìm nâng cao → Xác nhận phù hợp. 2 đường đi 1→3 hoặc 1→2→3. Nguồn MOW1 hiện ở REVIEW, dữ liệu thực/JEV/nơi nhận thiếu theo OPEN-03/04/08/09/10.
   - `MOW-NHC-002` CTCM B2 Dùng T0 Field: **2 MOT** `TSK-NHCN-004` Người chọn Dùng (`NHCN-004`), `TSK-NHCN-005` Máy áp dụng & xác nhận (`NHCN-005`). Bản UI hiện báo 0/2 bước có UI. Chỉ **đọc/kiểm kê**, không vẽ MOW2 trong NODE A.
5. Nếu check process/READY/roster/owner guard, ui Write_Path, runtime shared busy, quyền hay source version FAIL ⇒ `KQ DỪNG` và ghi blocker rõ; không tự tạo READY, không chờ, không hỏi Owner những gì nguồn đã trả lời.

## 2 · NODE A — MOW001 · làm xong thiết kế có bằng chứng
A1. Lập bản đồ **3 MOT × 8 câu hỏi**: mục đích, vào/ra, nguồn dữ liệu, thao tác, trạng thái rỗng/tìm/kết quả/lỗi, các nhánh thoát/quay lại và nơi nhận. Đối chiếu **7 câu Config**; mỗi câu ghi `ĐÃ TRẢ LỜI + NGUỒN` / `N-A có lý do` / `THIẾU (mã hồ sơ)`, không suy câu thiếu thành PASS.
A2. Với từng MOT, kiểm reusable UI cha/con trước; giữ mẫu UI.MASTER/UI-029 phần đã có, UI step3 thiết kế theo nguồn đã chốt hoặc ghi rõ quyết định chưa chốt; chỉ sửa đúng source chung/binding khi đã có quyền trong phạm vi. Màn đầu phải trống, dữ liệu minh họa tách khỏi dữ liệu thật, đầu vào không mất vô ý, không có nút lưu giả; cấu trúc phải hướng tới sản phẩm production. Không tự nối backend, không tạo Field thật, không chuyển UI demo thành canonical.
A3. Mỗi nhánh: `Given · When · Then`, có expected lấy từ SSOT; gồm tìm trực tiếp, tìm nâng cao, chọn/xác nhận, trống/kết quả rỗng/nhiều kết quả, timeout/không quyền/dữ liệu đổi/bấm lặp, back/cancel, bàn phím/focus/tooltip, UI cha parity, màn 390px và desktop. N-A phải có căn cứ. Không thể thử do thiếu backend/decision ⇒ `BLOCKED` với issue gốc, vẫn làm xong các phần thiết kế độc lập.
A4. Kiểm live đúng phiên nguồn (HTML/DOM/ảnh, các nút thật, console), kiểm pure-model tách với browser E2E, đọc lại kết quả/binding, chạy `check-ui-review.py` hợp lệ với phiếu. Phiếu duy nhất tại `work/mow-mot-moit-mout/UI-REVIEW-MOW001.json`; không tạo sổ/phiếu song song. Sửa UI nào phải đo hồi quy consumers dùng chung; không tô PASS cho phần chưa đo. Gate exit 1 giữ nguyên nếu blocker thật.
A5. Bàn giao thiết kế **DESIGN_DONE** chỉ khi đủ 3 MOT với đầu vào/đầu ra, luồng chính/nhánh và các trạng thái nhìn thấy/chạy thử được trong phạm vi thiết kế, dùng lại UI cha đúng, có phiếu kiểm + bằng chứng thực tế + unresolved issues. **PRODUCTION_READY** chỉ khi có backend/quyền/nơi nhận thật, không suy từ DESIGN_DONE. Nếu một phần thiết kế phụ thuộc quyết định chưa chốt, ghi `DESIGN_PARTIAL`, không tự hạ tiêu chí.

## 3 · Feedback là bắt buộc (mục tiêu chính của tools-quy-trinh)
- Trong chính lượt này, xác nhận `DOER_CONFIRM=YES|NO|PARTIAL`: **tôi đã đọc quy trình và hoàn thành thiết kế/phiếu đúng phạm vi mà không phải hỏi thêm chưa?** Tách khỏi `UI_PRODUCT_STATUS`. Cho cả phần đã đạt và phần chưa đạt, nêu mã bước/câu/nhánh thiếu, ví dụ cụ thể.
- Khi thấy hướng dẫn vẽ/kiểm UI còn thiếu, chỉ **tạo file proposal riêng** `work/tools-quy-trinh/proposals/TQT-PR-20261008-codex-01.md` theo khuôn 6 dòng README, kèm mẫu bổ sung chính xác (câu hỏi, thứ tự bước, expected/evidence, xong khi). Không sửa `work/tools-quy-trinh/{README.md,COLLAB.md,view.html}`, không tự sửa sổ TQT hay copy thành SSOT mới. Nếu proposal path không ghi được, gửi nguyên nội dung cho Host và KQ DỪNG, không bypass.
- Các lỗi thuộc **sản phẩm MOW** theo hồ sơ OPEN hiện có tại source MOW (không tự nhập bản chép TQT). Với điểm nghiệp vụ chưa chốt, trả đúng một câu hỏi tối thiểu cần Owner quyết (nếu thực sự chặn thiết kế), không kéo toàn bộ đặc biệt làm phức tạp công thức phổ biến.
- KQ ngắn cho Host: `MOW001 DESIGN_DONE|DESIGN_PARTIAL|DỪNG`, URL 3 màn, phiên nguồn, số câu trả lời Q1–Q8 và Config, số nhánh/ca đo, link receipt, các OPEN liên quan, danh sách file/commit sửa, `DOER_CONFIRM`, `UI_PRODUCT_STATUS`, proposal mã/path, lý do chưa PASS. Kiểm thực tế không dựa vào tự nhận xét.

## 4 · Thứ tự chạy, quyền và bước sau
| Bước | Ai | Kích hoạt | SLA/mốc | Bằng chứng phải có | Hỏng thì ai biết | Bước sau |
|---|---|---|---|---|---|---|
| A0 Read-gate & process-gate | Codex | READY + RUN hợp lệ | Trước mutation | SHA task/path, quyền, tool gate, source UI | Codex báo Host ngay trong KQ DỪNG | A1 |
| A1 Map 3 MOT / 8+7 câu | Codex | A0 PASS | Trước sửa UI | bảng Q/binding/gap và nguồn | Host đọc KQ khi thiếu | A2 |
| A2 Sửa thiết kế review MOW001 | Codex | A1 đủ nguồn và path lease | Cùng RUN, không chờ ngoài | version/diff UI, ảnh/cấu trúc từng màn | Host nhận cảnh báo KQ DỪNG nếu blocked | A3 |
| A3 Kiểm UI live + phiếu | Codex | A2 có sản phẩm | Trước ghi XONG | browser, parity, responsive, checker + receipt | Host so evidence sau KQ | A4 |
| A4 DOER_CONFIRM + proposal | Codex | A3 kết thúc | Cuối RUN | KQ, link phiếu và proposal riêng | Host tiếp nhận trong vòng nghiệm thu | HOST |
| HOST xét & cập nhật quy trình | GPT Chat + Reviewer | Codex KQ | Trong lượt review tiếp theo, không giữ RUN sống | ACCEPT/PARTIAL và TQT phiên mới | Host chịu trách nhiệm | Node B DRAFT |
| NODE B: MOW002 | **phiên Codex mới** | **Host cấp READY/RUN riêng** sau Node A | Node riêng | 2 UI, phiếu và chứng minh không cần chat cũ | Host xem KQ | Nghiệm thu tiến bộ công thức |

Không được tự chuyển NODE B, tự tạo task hay mở rộng quy trình nghiệp vụ. RUN này dừng sau A4; khi gặp gate phụ thuộc thì `KQ DỪNG` và nhả cờ bận, không giữ terminal chờ. Để Owner/Host đọc bất cứ lúc nào, update có bằng chứng tại sổ/phiếu chính của task sản phẩm, không báo “đang làm” chỉ vì đã có checklist.

## 5 · Quyền và các điều cấm
- Preserve by default. Không sửa `AGENTS.md`, công thức CT-005/005.1, ML-DEF-004/005, Master khác, MOW bất kỳ ngoài 001; không sửa MOW002 UI trong RUN này.
- Không ghi PG/Directus ngoài DOT; không chạy script trong DB, không đổi production data; không tạo/cấp UI con/cha canonical mới nếu chưa phê duyệt.
- Không viết trực tiếp 3 file chính/sổ thuộc tools-quy-trinh: proposal only. Reviewer/Worker không tự giao lượt tiếp hay tự đóng TQT issue.
- Không coi tỷ lệ ~98%/gần hết 35 MOW đã sinh là tỷ lệ UI đã hoàn tất. Đọc Master trước, tái sử dụng, trường hợp đặc biệt ghi sổ riêng.
