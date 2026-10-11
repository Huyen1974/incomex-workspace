# TQT-PR-20261011-claude-feasibility-qtth05-12
## BẢN v2 · HIỆN HÀNH · 11/10/2026 18:15 · gộp 3 lần rà (PR-07 09/10 · v1 17:55 · rà lại theo cách đi của Owner)

TQT-PROPOSAL: TQT-PR-20261011-claude-feasibility-qtth05-12 (v2)
TARGET: MOW-TH-005@1.1 · 7 mốc · record_control · 18 Master thiết kế · TQT-MODEL-001 · phiếu MOW-NHC-001-G1-20261010-01 · Over view.
TESTED: Đọc nguồn @dfaa160; tự chạy run-tqt-checks --verify (PASS cục bộ, pg NOT_RUN); đọc phiếu MOW001; đối chiếu 18 Master thiết kế với MODEL-001 và pg_design của record_control bằng script; chỉ SELECT schema/đếm dòng PG. JEV: gen-dec-1791715670, gen-dec-1791716688, gen-dec-1791717154.
BLOCKER_TYPE: LOI_QUY_TRINH (luật ghi tự khoá ca thử) · THIEU_HUONG_DAN (chưa có tiêu chí qua bước)
OBSERVED: Ca thử duy nhất MOW001/G1 đứng ở mốc 2 hai ngày, 0/34 đã ghi. Nguyên nhân gốc: luật thiết kế đòi "Đã ghi" phải có bản ghi ở nơi lưu thật và mốc 3 phải kiểm nơi lưu/quyền, trong khi nơi lưu thật (PG) theo đúng cách đi của Owner chỉ có ở bước 3. Ngoài ra có 3 bản thiết kế dữ liệu chưa nối với nhau.
PROPOSED_CHANGE: Giữ nguyên cách đi của Owner. Bổ sung 8 việc ở Bước 1, 5 việc ở Bước 2, 4 việc ở Bước 3 (mục 2). Việc làm ngay: C1 khai kho thử ngoài PG.

**Cách đi của Owner (11/10 18:02, nguyên văn ở COLLAB ô 3 mục 3.4):** ① thiết kế hệ thống đúng → ② chạy thử một số ca để hiệu chỉnh thiết kế, bổ sung cột, làm tay cũng được → ③ chạy ổn mới rà và đưa vào PG một lần.
**Bản v1 lúc 17:55 đề xuất "dùng bảng PG ngay làm nơi ghi" (A1) — SAI với cách đi này và với chỉ đạo 09/10 "xử lý chuẩn bên ngoài rồi bê nguyên khối vào PG". Bỏ A1.** Các bảng PG đang chạy chỉ dùng để chọn đích ở Bước 3 (T4).

---

## 1. Nhìn 30 giây

| Bước | Trạng thái | Đang vướng |
|---|---|---|
| ① Thiết kế | 🟡 rất nhiều, chưa gộp | 3 bản thiết kế dữ liệu cho cùng khái niệm; mã chưa chốt; chưa có tiêu chí "đủ để thử" |
| ② Chạy thử ngoài PG | 🔴 kẹt ở mốc 2 | Luật ghi đòi nơi lưu thật, chưa có kho thử → ca không thể qua mốc 3 |
| ③ Đưa vào PG một lần | ⬜ chưa tới | Chưa ghi đích PG dự kiến; chưa có kịch bản nạp/đường lui |

Ví dụ đời thường: bản vẽ nhà đã chi tiết tới từng ổ điện, nhưng luật công trường lại ghi "chỉ được đặt gạch lên móng bê tông" — mà móng bê tông thì để đổ sau cùng. Thợ đứng chờ. Cần cho phép **móng tạm** (kho thử) để xây thử, đúng kích thước móng thật, xây ổn rồi mới đổ bê tông một lần.

---

## 2. Danh sách bổ sung theo 3 bước

### ① Thiết kế đúng — còn thiếu
| # | Việc | Vì sao | Mức |
|---|---|---|---|
| T1 | **Gộp 3 bản thiết kế dữ liệu thành 1.** Đang có: TQT-MODEL-001 (18 bảng, 09/10) · pg_design của record_control (4 bảng, dùng lại MODEL-001) · 18 Master thiết kế (12–36 cột mỗi Master, 11/10, `pg = null`). Chưa có bảng nối. Cặp cùng nghĩa: issue ↔ CAT-069?/CAT-017 · event ↔ CAT-233* · assessment ↔ CAT-015 · run ↔ CAT-227*/CAT-229* · outbox/call ↔ CAT-238*. | Để tới Bước 3 mới chọn thì phải sửa PG nhiều lần — đúng điều Owner muốn tránh. JEV: rủi ro "likely" 0,97. | 🔴 |
| T2 | **Chốt mã thật** thay CAT-227*, CAT-069?, CAT-003?, CAT-009?… trước bản ghi thử đầu tiên. | Mã là khoá chính; đổi sau = sửa mọi bản ghi thử. | 🔴 |
| T3 | **Mỗi Master có phiên bản cấu trúc** (hiện `version = None` cả 18). | Bước 2 sẽ thêm cột; phải biết bản ghi thử nào theo phiên nào để nạp PG đúng. | 🟡 |
| T4 | **Ghi "đích PG dự kiến" cho từng Master** (một dòng thiết kế, không chạm PG): dùng lại bảng đang chạy (`checkpoint_instances` 121 dòng · `approval_requests` 232 · `lifecycle_log` 851 · `dot_tools` 314) hay tạo mới. | Để Bước 3 thật sự "một lần", không vướng bảng cũ trùng nghĩa. | 🟡 |
| T5 | **Một bảng gốc 7 dòng** mốc → MOT → trạng thái → nhóm ghi → Master. 13 câu khai, 11 trạng thái, 11 nhóm ghi, 34 nghĩa vụ sinh ra từ bảng này. | Hiện 6 cách đếm cho một quy trình; AI dễ sót, người khó nhớ. | 🟡 |
| T6 | **Thiết kế đường "ý tưởng → quy trình chạy được"** (ô 3 R04): Owner đưa ý tưởng → ⑤ khai việc → ③ dựng quy trình → ① khi cần config/DOT. | Đây là mục tiêu số 1; hiện chưa có. | 🟡 |
| T7 | **Over view nhìn là hiểu:** dòng đầu mỗi việc một dòng (tên · thanh 7 ô màu · ai làm tiếp · tắc vì gì); hai bảng 11 hàng đưa xuống mục "Cho AI". | Trang đang cao ~4.900 px, mã đứng trước tình trạng. | 🟡 |
| T8 | **Tiêu chí "thiết kế đủ để chạy thử":** T1, T2, C1 xong + có ca thử đã khai. Đủ thì dừng thêm Master/UI, chuyển sang thử. | 11/10 thêm 8 Master trong khi ca thử chưa đi bước nào; không có điểm dừng thì Bước 1 kéo dài mãi. | 🟡 |

### ② Chạy thử ngoài PG — còn thiếu
| # | Việc | Vì sao | Mức |
|---|---|---|---|
| **C1** | **Khai "kho thử ngoài PG" — làm ngay.** Một file trong repo (vd `work/tools-quy-trinh/trial-store.json`), mỗi Master một khối: mã Master · phiên cấu trúc · danh sách cột và khoá đúng như PG dự kiến · các dòng. Trong Bước ②: "Đã ghi" = có dòng trong kho thử; phiếu ghi `store_state = TRIAL`, `record_ref` trỏ vào dòng đó, `record_version` = phiên Master; "đọc lại" = bộ kiểm record_control đọc file và đối chiếu (máy kiểm, không tin lời AI). Mốc 3 kiểm kho thử, **không đòi PG**. Host sửa câu luật ghi cho rõ: ở bước ②, nơi lưu đích = kho thử đã khai (cột/khoá cố định, có phiên, máy đọc lại); file nháp khác vẫn không tính — tránh hai AI hiểu khác nhau (JEV 0,46: chưa sửa câu thì dễ cãi). **Cùng một hợp đồng cột/khoá và cùng bộ kiểm cho kho thử và PG**: qua kiểm ở kho thử thì nạp PG cũng qua (JEV 0,86). Một file, không tách 18 file (JEV chọn 1,0). AI ghi tay được ngay, đúng câu Owner "giờ ghi tay trên repo/VPS cho nhanh" (R09). | Luật hiện tại ("Đã ghi chỉ khi có bản ghi ở nơi lưu thật"; "trước mốc 3 kiểm nơi lưu/quyền") + chưa có nơi lưu = ca thử **không bao giờ qua được mốc 3**. Đây là lý do MOW001 đứng 2 ngày (34/34 `record_ref = null`). JEV: tự khoá 0,88; là việc gỡ bế tắc số 1 (0,86); hợp cách đi của Owner 0,90. | 🔴 |
| C2 | **Bộ ca thử khác loại:** MOW001/G1 (thiết kế UI) · 1 ca sai/thiếu đi qua ② · 1 ca "ý tưởng → quy trình" (T6). Mỗi nhóm ghi có ít nhất 1 bản ghi thật trong kho thử. | Một ca UI không phủ được các nhánh và không chứng minh mục tiêu 1. | 🟡 |
| C3 | **Người làm ≠ người kiểm:** mốc 3, 5, 6 do một phiên AI khác, chỉ đọc README + hồ sơ. Phải hỏi = hướng dẫn thiếu → ghi vào ③. | Hiện Codex tự làm, tự kiểm, tự duyệt; ô 2 đòi "AI mới làm theo không hỏi". | 🟡 |
| C4 | **Mỗi lần thêm/sửa cột** → ghi sổ đổi định nghĩa (CAT-016) + tăng phiên Master (T3). | Đây chính là "hiệu chỉnh thiết kế" của Bước 2, có dấu vết để Bước 3 chuyển đổi đúng. | 🟡 |
| C5 | **Tiêu chí xong Bước 2:** 3 ca đi hết 7 mốc · ca cuối không phải thêm cột nào · AI mới đi hết không hỏi · mọi nhóm ghi có bản ghi. | Không có tiêu chí thì không biết khi nào "ổn" để đưa vào PG. | 🟡 |
| C6 | Node.js trên VPS để bộ kiểm chạy ở nơi hệ thống sống. | Không chặn Bước 2 (chạy ở máy Host được). | ⬜ |

### ③ Đưa vào PG một lần — chuẩn bị sẵn
| # | Việc |
|---|---|
| P1 | Bảng ánh xạ cuối: Master (phiên cuối) → bảng PG (dùng lại/tạo mới, theo T4) · cột → cột. |
| P2 | Kịch bản nạp bằng DOT: chạy trên staging, nạp toàn bộ kho thử, đọc lại so số dòng + hash, chạy lại đúng bộ kiểm đã dùng ở bước ②. |
| P3 | Đường lui (rollback) kiểm trước khi chạy thật. |
| P4 | Nạp xong: kho thử chuyển lưu trữ, chỉ còn PG là nguồn (một SSOT). |

---

## 3. Đã xong từ 2 lần rà trước — không làm lại
- PR-07 (09/10): mục tiêu ngắn 3 ý (D25) · Bảng đúng khuôn MT4 · bảng "Ý kiến hội đồng · Host kết luận" ở README · TH-001 gọi quy trình con bằng mã (20/20) · gộp 2 đường sai/thiếu về ② · công thức khép kín đưa lên đầu (P16).
- Vẫn mở từ PR-07: khoá kỹ thuật chỉ Host được ghi (TQT-ISS-006).

## 4. Từ v1 (17:55) — giữ / sửa / bỏ
| v1 | Xử lý trong v2 |
|---|---|
| F01 không có nơi ghi thật | **Sửa** → C1 kho thử ngoài PG |
| F02 PG đã có bảng tương đương | **Sửa** → T4 chỉ ghi đích dự kiến, dùng ở Bước 3 |
| F03 thiết kế nở ra | **Sửa** → T8 tiêu chí đủ để thử |
| F04 tự kiểm | Giữ → C3 |
| F05 Node VPS | Giữ → C6 |
| F06 ⑤ tựa cổng chưa nghiệm thu | Giữ: ca thử làm S1 thủ công theo phiếu 13 câu, ghi rõ "thủ công" |
| F07 nhiều cách đếm | Giữ → T5 |
| F08 mã ?/\* | Giữ → T2 |
| F09 thiếu ca ý tưởng | Giữ → T6 + C2 |
| F10 Over view | Giữ → T7 |
| A1 dùng bảng PG ngay | **Bỏ** — trái cách đi của Owner |
| A2 đóng băng tới mốc 4 | **Sửa** → T8 (đủ để thử thì dừng mở rộng) |
| A3–A5 | Giữ → C3, T5, T7 |

## 5. Thứ tự đề xuất cho Host nội dung
1. **C1** khai kho thử → **T2** chốt mã → **T1** gộp thiết kế dữ liệu (cùng lúc với C1 vì kho thử lấy cột từ bản gộp).
2. Cho MOW001/G1 đi tiếp mốc 3 với kho thử; mốc 3 do phiên AI khác xác nhận (C3).
3. Song song khi chờ người kiểm: T3, T4, T5, T7.
4. Sau MOW001: ca sai/thiếu, rồi ca "ý tưởng → quy trình" (C2, T6). Đạt C5 → Bước 3 (P1–P4).

## 6. Rà 2 vòng
- Vòng 1: chạy lại bộ kiểm, đọc phiếu MOW001, dò bằng script 18 Master (đều `version = None`, `pg = null`), so với 18 bảng MODEL-001 và 4 bảng record_control; đọc luật ghi và luật mốc 3.
- Vòng 2: truy vì sao ca thử đứng 2 ngày → luật ghi + chưa có nơi lưu = tự khoá. Đối chiếu cách đi 3 bước của Owner: kho thử ngoài PG gỡ được khoá mà không vi phạm "chỉ vào PG một lần". JEV xác nhận thứ tự và mức rủi ro.

---

# Bản v1 · 11/10 17:55 — ĐÃ THAY bằng bản v2 ở trên (A1 "dùng bảng PG ngay" bị Owner bác 18:02). Giữ để đối chiếu.
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
