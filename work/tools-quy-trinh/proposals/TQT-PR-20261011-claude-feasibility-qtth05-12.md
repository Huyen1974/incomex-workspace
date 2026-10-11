# TQT-PR-20261011-claude-feasibility-qtth05-12
## Phản biện tính khả thi QTTH 05 trước triển khai + đề xuất đổi cách tiếp cận

TQT-PROPOSAL: TQT-PR-20261011-claude-feasibility-qtth05-12
TARGET: MOW-TH-005@1.1-design · 7 mốc · 11 nhóm ghi RG01–RG11 · 48 Master thiết kế · tool_registry CAT-006 · phiếu MOW-NHC-001-G1-20261010-01 · Over view.
TESTED: Claude-review đọc COLLAB/README/view.html @64bfc31; tự chạy `python3 run-tqt-checks.py --verify` (5 suite + runner: PASS cục bộ, pg NOT_RUN); đọc phiếu `UI-REVIEW-MOW001.json#/application_D24`; render Over view bằng Chromium và xem trang Owner thật; đếm lời gọi/mã bằng script; đọc schema + đếm dòng PG thật (chỉ SELECT). JEV xếp hạng mức chặn 9 phát hiện và chọn hướng đi.
BLOCKER_TYPE: THIEU_SAN_PHAM (chưa có nơi ghi thật) · LOI_QUY_TRINH (thiết kế nở ra trước khi chạy)
OBSERVED: Sau 36 giờ và 35 commit, toàn bộ là thiết kế/UI/bộ kiểm. Ca thật duy nhất MOW001/G1 vẫn CHUAN_BI, mốc 2/7, 5/5 việc TODO, 0/34 nghĩa vụ đã ghi, start_confirmation PENDING từ 10/10. Mọi bộ kiểm trả DESIGN_ONLY / SIMULATION_ONLY / pg NOT_RUN. Không Master nào có nơi lưu đã kiểm. Trong khi đó PG đang chạy thật đã có checkpoint_instances (121 dòng), checkpoint_types (31), approval_requests (232), lifecycle_log (851), dot_tools (314), event_outbox (219.312).
PROPOSED_CHANGE: Đóng băng thiết kế. Dùng bảng PG đang có làm nơi ghi thật. Đi hết MOW001/G1 qua 7 mốc với bản ghi thật, ghi mọi chỗ vướng vào 002. Chỉ thêm Master nào lượt đi chứng minh là thiếu. Chi tiết mục 3–5.

---

## 0. Nhìn 30 giây

| | Thiết kế | Chạy thật |
|---|---|---|
| Quy trình ⑤ (7 mốc, 6 MOT, 11 trạng thái) | 🟢 đủ, có bộ kiểm 59 ca | 🔴 chưa ca nào qua mốc 1 |
| Nơi ghi (11 nhóm, 20 Master) | 🟡 có UI mẫu | 🔴 0 Master kiểm được ghi/đọc |
| Ca MOW001/G1 | 🟡 phiếu khai đủ 13 mục | 🔴 0/34 nghĩa vụ đã ghi, 2 ngày không nhúc nhích |
| Bộ kiểm (5 + runner) | 🟢 PASS máy cục bộ | 🟡 VPS thiếu Node → BLOCKED |
| Người kiểm độc lập | — | 🔴 Codex tự làm, tự kiểm, tự duyệt |
| Đường "ý tưởng → quy trình chạy được" (R04) | ⬜ chưa thiết kế | ⬜ chưa có ca |
| Owner nhìn là hiểu | 🟡 2 bảng dài, mã CAT-227*/RG03 | — |

**Kết luận:** khả thi về kiến trúc, **chưa khả thi để triển khai** vì chưa có một nơi ghi thật nào và chưa ai đi hết một lượt. Cỗ máy đang xây thêm chỗ để ghi thay vì ghi.

---

## 1. Phản biện cái đã làm · F01–F10

| # | Phát hiện | Bằng chứng | Mức | Đề xuất |
|---|---|---|---|---|
| F01 | **Không có nơi ghi thật.** 11 nhóm ghi đều "Nguồn lưu chưa xác minh / Chưa khai / chưa kiểm ghi-đọc". "Đã ghi" không bao giờ thành true. | Over view bảng 1; record_control.status = DESIGN_TRIAL_NOT_PG; record_checks store_state UNVERIFIED | 🔴 chặn | Mục 3 A1: dùng bảng PG đang có. |
| F02 | **PG đã có sẵn các sổ tương đương** nhưng thiết kế đang vẽ Master mới song song: CAT-015 ≈ `checkpoint_instances` (121 dòng, có target_collection/target_item_id/status/verified_by/evidence) · CAT-025 ≈ `approval_requests` (232, có entity_code/proposed_action/reviewed_by) · CAT-233* ≈ `lifecycle_log` (851, from/to_status/performed_by/approval_ref) · CAT-006 ≈ `dot_tools` (314) · chống gửi trùng ≈ `event_outbox`. Trái R18 "nền = chuẩn có sẵn" và D22 "hạn chế khái niệm mới". | pg_schema + SELECT count 11/10 17:48 | 🔴 chặn | Ánh xạ 11 RG → bảng PG có sẵn trước; chỉ Master nào không ánh xạ được mới thiết kế mới. |
| F03 | **Thiết kế nở ra trước khi chạy:** 10/10 → 11/10 thêm 8 Master, 11 RG, 2 checker JS, runner, DEF 00.1; view.html 442 KB → 868 KB. Ca thật không đi thêm bước nào. | git log; phiếu history 1 sự kiện DECLARE | 🔴 chặn | Đóng băng: không thêm Master/UI/checker cho tới khi MOW001 qua mốc 4. |
| F04 | **Tự kiểm, tự duyệt.** actor = reviewer = approver = Astra Codex; Reviewer khác hãng "CHƯA ĐO". Ô 2 đòi "người/AI mới làm theo, không hỏi thêm" → chưa có ai mới. | application_D24.reviewer "tự kiểm kỹ thuật, không phải kiểm độc lập" | 🟡 | Mốc 3 và mốc 6 do một phiên AI khác (Claude Code / Codex phiên mới) thực hiện, chỉ đọc README. |
| F05 | **VPS không chạy được bộ kiểm** (thiếu Node) → "máy kiểm trước, agent sau" chưa có ở nơi hệ thống sống. | P26; runner exit 3 trên VPS | 🟡 | Việc hạ tầng có mã riêng, giao đúng quy trình VPS; trong khi chờ, 2 checker JS chạy ở máy Host và ghi hash báo cáo. |
| F06 | **005 tựa vào cổng chưa nghiệm thu:** S1 bind CHUNG.APQUYTRINH "chưa nghiệm thu toàn cổng"; S3 chọn 001 mà 13/21 lời gọi của 001 còn trỏ vào tab "Tham chiếu cũ". | catalog.records[005].workflow.steps; PR-07 C2 | 🟡 | Ca MOW001 làm S1 thủ công theo work_form, ghi rõ "thủ công"; 001 gọi con bằng mã trước khi G1 kết thúc. |
| F07 | **Bốn cách đếm cho một quy trình:** 7 mốc · 6 MOT · 11 trạng thái · 13 trường · 11 RG · 34 nghĩa vụ. AI đọc không sót là khó; người thì không nhớ. | work_form, record_control, Over view | 🟡 | Một bảng ánh xạ duy nhất mốc → MOT → trạng thái → nhóm ghi → bảng PG; các bảng khác chỉ là cách xem. |
| F08 | **Mã có dấu ? và \*** (CAT-003?, CAT-227*) là mã tạm/mã chưa chắc trong Master of Master, nay thành khoá chính của hồ sơ. Trái "không gì là không có mã". | 46 lần CAT-227*, 14 lần CAT-069? trong view.html | 🟡 | Chốt mã thật trong Master of Master trước khi ghi bản ghi đầu tiên; không mang ?/\* vào khoá. |
| F09 | **Chưa có đường "ý tưởng → quy trình chạy được".** MOW001 là ca thiết kế UI, không chứng minh được mục tiêu 1. R04 vẫn ⬜. | ô 3 R04 | 🔴 chặn (với M1) | Mục 4: ca thứ hai ngay sau MOW001, dùng đúng các bảng MOW001 đã dùng. |
| F10 | **Over view chưa "nhìn là hiểu".** Trang cao ~4.900 px; hai bảng 11 hàng × 5 cột toàn mã trước; tình trạng ca thật nằm dưới. | ảnh render 11/10 | 🟡 | Mục 3 A5: đảo thứ tự, 1 dòng/ca, màu trước chữ. |

JEV (gen-dec-1791715670): I2 nơi ghi = chặn (1,0); I1 nở thiết kế 0,67 chặn; I9 thiếu ca ý tưởng 0,68 chặn; gốc rễ = no_store 0,6 / scope 0,4; hướng đi B (đóng băng, đi ca thật) 0,72.

---

## 2. Cái đã làm tốt · giữ nguyên
- ⑤ đúng vai khuôn chung; 13 câu khai khớp 13 ý Owner; nhánh ĐẠT/CHƯA ĐẠT/BLOCKED rõ. Không cần TH-06.
- Luật "Đã ghi ≠ chuẩn bị", "Đã đối chiếu độc lập với Đã ghi", "lỗi mốc sau không xoá bằng chứng mốc trước" là đúng và nên giữ khi chuyển sang PG.
- Runner có preflight BLOCKED, hash công cụ, không tô PASS giả. Giữ.
- Tách "hướng dẫn chung" khỏi "hồ sơ từng việc". Giữ.

---

## 3. Đổi cách tiếp cận · A1–A5

**A1 · Nơi ghi thật = bảng PG đang chạy, không phải Master mới.**
Ánh xạ tối thiểu cho ca MOW001 (đề xuất, Host nội dung kiểm cột thật trước khi ghi):

| Nhóm ghi | Bảng PG có sẵn | Khoá |
|---|---|---|
| RG03 hồ sơ việc / mốc hiện tại | `checkpoint_instances` (target_collection = 'mow', target_item_id = 'MOW-NHC-001', code = application_id, layer = số mốc) | code + layer |
| RG05 kết quả kiểm | `checkpoint_instances`.status/evidence/verified_by | như trên |
| RG06 quyết định, xác nhận bắt đầu, duyệt | `approval_requests` (entity_code = application_id, request_type_code = CP03/CP06, status, reviewed_by) | code |
| RG07 lịch sử | `lifecycle_log` (entity_code = application_id, from/to_status = 11 trạng thái, approval_ref) | id |
| RG08 sai/thiếu | `approval_requests` request_type = ISSUE, hoặc sổ TQT-ISS hiện có | code |
| CAT-006 công cụ | `dot_tools` (đã 314 dòng) | code |
| RG01/02 định nghĩa MOW/MOT | Master định nghĩa hiện có (ML-DEF-004/ML-MOW-TH-001) | mã |

Chỉ RG04 (việc con), RG09 (bàn giao), RG10 (huỷ/bù), RG11 (đổi định nghĩa) là có thể chưa có bảng; **để sau**, ghi tạm vào `lifecycle_log.metadata` cho ca đầu, tính là 🟡.
Ghi/đọc PG đi qua DOT theo luật hiện hành (R08 "chạm PG bắt buộc DOT"); ca đầu có thể dùng DOT có sẵn + quyền ghi được duyệt riêng, không viết API mới.

**A2 · Đóng băng thiết kế tới khi ca thật qua mốc 4.** Không thêm Master, UI, checker, trang. Mọi "thiếu" phát hiện trong lượt đi → ghi vào 002 với mã, xử lý sau mốc 4. Lý do: 36 giờ vừa rồi chứng minh thiết kế có thể nở vô hạn mà không chạm thực tế.

**A3 · Tách người làm và người kiểm.** Mốc 1–2 và 4: Astra Codex. Mốc 3 (xác nhận bắt đầu) và mốc 5–6: một phiên AI khác, chỉ đọc README + hồ sơ, không chat với Host. Nếu phiên đó phải hỏi → ghi câu hỏi vào 003 = bằng chứng hướng dẫn thiếu. Đây chính là phép thử của ô 2.

**A4 · Một bảng ánh xạ duy nhất** mốc → MOT → trạng thái vào/ra → nhóm ghi → bảng PG → bộ kiểm. 7 dòng. Mọi bảng khác (13 trường, 34 nghĩa vụ) sinh từ bảng này, không duy trì tay.

**A5 · Over view đảo thứ tự và rút chữ.**
- Dòng 1: **mỗi ca một dòng**: tên việc · thanh 7 ô (■ đang · 🟢 đạt · 🔴 tắc · ⬜ chưa) · ai làm tiếp · tắc vì gì. Hiện nay 1 dòng (MOW001).
- Dòng 2: công thức `⑤ = Khai → Chuẩn bị → Xác nhận → Làm → Kiểm → Duyệt → Bàn giao`.
- Hai bảng 11 hàng chuyển xuống mục xổ "Cho AI". Mã CAT-xxx chỉ hiện khi xổ.
- Màu đúng luật Owner: xanh = ok · vàng = cảnh báo · đỏ = tắc · xám = chưa làm.

---

## 4. Đường đi đề xuất · thứ tự bắt buộc

```
B1  Ánh xạ 11 RG → bảng PG (A1) · chốt mã thật thay ?/*            🤖 Codex      1 lượt
B2  Ghi bản ghi đầu tiên: checkpoint_instances mốc 1 của MOW001     🤖 Codex/DOT  1 lượt
B3  Mốc 2–3: chuẩn bị + xác nhận bắt đầu bởi phiên AI khác           🤖 AI mới     1 lượt
B4  Mốc 4: 3 MOT của G1, mỗi MOT 1 dòng lifecycle_log                🤖 Codex      2–3 lượt
B5  Mốc 5–7: kiểm, duyệt (approval_requests), bàn giao Owner          🤖 AI mới + 😊 Owner gật
B6  Gom mọi "thiếu" từ B1–B5 trong 002 → sửa ⑤/Master (003)          🤖 Codex      1 lượt
B7  Ca 2 · R04: Owner cho 1 ý tưởng nhỏ → ⑤ → 003 dựng quy trình     😊 Owner 1 câu · 🤖 AI
    → chạy được, dùng đúng bảng B1. Chứng minh mục tiêu 1.
```
Hạ tầng (Node trên VPS) chạy song song theo quy trình VPS, không chặn B1–B5.

---

## 5. Việc cho Host Codex xét ngay
1. ACCEPT/REJECT A1–A5; nếu ACCEPT thì ghi D27 và đổi ➡ Kế tiếp sang B1.
2. Kiểm cột thật 4 bảng PG ở A1 (Claude chỉ đọc schema + count, chưa đọc nội dung dòng).
3. Chốt mã thật cho CAT-227*/CAT-069?/CAT-003?/CAT-009? trong Master of Master (F08).
4. Chỉ định phiên AI mới cho B3 (F04); ghi vào phiếu MOW001.reviewer.
5. Over view theo A5; hai bảng hiện tại giữ nguyên dữ liệu, chỉ chuyển xuống mục xổ.

---

## 6. Rà 2 vòng
- Vòng 1 (hiện trạng): chạy lại 5 suite + runner, đọc phiếu, render trang, đếm commit/lời gọi, đọc schema PG. Mọi số trong file này lấy từ nguồn, không từ báo cáo.
- Vòng 2 (gốc rễ): hỏi vì sao 2 ngày không đi được một mốc → vì không có chỗ ghi → vì đang thiết kế chỗ ghi mới trong khi PG đã có. JEV xác nhận gốc rễ no_store/scope và hướng B. Rủi ro của đề xuất: bảng PG có sẵn có thể không đúng nghĩa 100% với 7 mốc → chấp nhận 🟡 cho ca đầu, ghi lệch vào 002, không vẽ bảng mới trước khi chạy.
