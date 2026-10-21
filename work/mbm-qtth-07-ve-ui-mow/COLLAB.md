# COLLAB — mbm-qtth-07-ve-ui-mow
Tên việc: MMOW 07 — vẽ UI cho các MOW trong Master MOW, làm bằng công thức MBM

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
Xác nhận User: ĐÃ XÁC NHẬN — Owner 19/10/2026 18:28: MMOW 07 chỉ Vẽ UI (thay bản 18/10 21:25 gồm 3 mục tiêu; Chốt Info contract → MMOW 08, Config → MMOW 09).
Host: Claude Chat · Owner giao trực tiếp 16/10 16:29–17:05.

### ⇢ HANDOFF CHO PHIÊN SAU · 21/10/2026 14:25 +07 · Claude · P67 · cập nhật 14:50 P68
> Phiên mới: đọc hết mục này → mở 3 trang ở H2 → làm việc đầu tiên chưa ✅ ở H4 (hiện: H4.4). Không bàn lại những gì ở H3.

#### H1. Đang ở đâu
Đang thiết kế **4 Công thức gốc** (khung chung cho MỌI việc) trên trang Công thức. Vừa nhận **phản biện vòng 2 của GPT Pro** (Owner dán 21/10 14:19) cho Bộ câu hỏi chuẩn v2 + Xử lý lỗi. Owner yêu cầu: **áp sát chuẩn ngành IT tốt nhất**, mỗi luật viết **yes/no rõ ràng, chỉ 1 cách làm**, không nói định hướng chung chung. Việc kế tiếp = H4.1.

#### H2. Mở đâu
| Gì | Địa chỉ |
|---|---|
| Khối Công thức gốc (CT-000.1…000.4) | https://vps.incomexsaigoncorp.vn/knowledge/modules?task=mow-mot-moit-mout&view=content&section=formula-ct-000-1 |
| CAT-000.5 Khái niệm | cùng trang, `section=kn-cat-000-5` |
| Master Duyệt thiết kế | https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/master-design-review-v1.html |
| Nguồn trang (SSOT) | gh `work/mow-mot-moit-mout/ban-duyet.html` · `FORMULA-AI-README.md` · ui `definition-master-data-v1.js` (sổ ML-DEF-021 = Master Công thức) · ui `definition-master-registry-v1.js` |

#### H3. Đã chốt — không bàn lại
1. **CAT-000.5 Master Khái niệm** (tạm ở trang Công thức, sau lên collection): gộp entity_species (CAT-020) + sua_re_khai_niem_nhap + CAT-237*; mã loài chuẩn **SPE-xxx** (* = đề xuất); 7 cột + Tình trạng; 107 loài; ĐL1–ĐL6 (ĐL6 = mọi bảng có «?»). Master Duyệt thiết kế có cột **Duyệt TK** (xanh = User đã duyệt; CAT-000.5 tạm duyệt 20/10).
2. **Khối «Công thức gốc»** (thu/mở) trên khối «Công thức chuyên môn» (CT-001→008):
   - **CT-000.1 Bộ câu hỏi chuẩn** (= Info contract law) v2: Việc = Muốn gì + Đang thế nào · 5 giai đoạn có cổng G1 Khai báo (Definition of Ready) · G2 Chuẩn bị · G3 Thực hiện · G4 Nghiệm thu (Definition of Done) · G5 Bàn giao · 7 nhóm công cụ CC1–CC7 · 43 câu G1.1–G5.5, cột Ai trả lời · Nhóm · Master List (mã · 🟡 thiếu ô · 🔴 chưa có sổ · ⚪ không cần) · 4 trạng thái trả lời Có · Không áp dụng · Chưa biết · Sai.
   - **CT-000.2 Điều luật** = Khi nào + Làm gì + Kiểm bằng + Xử lý bằng; sổ CAT-140 (normative_registry, đã có NRM-LAW-02 Registry, NRM-LAW-07 Tận dụng…).
   - **CT-000.3 Cấp ghép** = cấp ghép lớn nhất của thành tố + 1 (Cấp ghép 1 ~ nguyên tử → 4).
   - **CT-000.4 Xử lý lỗi** = 9 bước X1–X9 (Ghi sự cố → Xếp hàng → Tra quy trình → Chạy → Kết quả → Kiểm lại · Vấn đề → MMOW → Owner); Sự cố = ITIL Incident (CAT-017), Vấn đề = ITIL Problem (CAT-069).
3. **Logic gốc:** không đạt ⇒ vào hàng đợi. Không viết «thiếu ⇒ tạo mới» (đó là khái niệm, không phải bước làm). Gọi quy trình nào là việc của hàng đợi.
4. **Ký hiệu:** G = giai đoạn · G1.4 = câu · CC = nhóm công cụ · X = bước xử lý lỗi. Không dùng B (trùng Bước B1–B7).

#### H4. Việc kế tiếp — đúng thứ tự, mỗi lần 1 việc
- ✅ **H4.1** Ghi tóm tắt phản biện vòng 2 (H5) vào mục «Chờ hội đồng» của Bảng điều khiển. (P68)
- ✅ **H4.2** (P68: 2 Bảng Chuẩn ngành, 32 chuẩn có nguồn, đặt trong Chi tiết thẻ CT-000.1 và CT-000.4) Lập **Bảng chuẩn ngành** (Owner 14:19: «chuẩn ngành IT đâu, mang ra áp sát, kiếm chuẩn tốt nhất»): mỗi điểm H5 → chuẩn cụ thể (tên, mục, nguồn) → luật yes/no. Chuẩn đã khớp, cần tìm và dẫn nguồn: Scrum Guide (Definition of Ready/Done) · ISO/IEC/IEEE 29148 (yêu cầu kiểm chứng được) · RFC 2119 (PHẢI/KHÔNG ĐƯỢC) · BPMN 2.0 (error/boundary event, compensation) · CMMN 1.1 (sentry = cổng) · DMN (bảng quyết định) · Kubernetes conditions (True/False/Unknown + reason) · ITIL 4 (Incident/Problem) · Transactional outbox + idempotency key · lease + fencing token · PostgreSQL 18 (SKIP LOCKED, UPDATE 0 dòng, LISTEN/NOTIFY + quét bù, transaction) · Directus Flow (Filter chặn cùng giao dịch / Action sau giao dịch). Không tự sáng tạo.
- ✅ **H4.3** Sửa CT-000.1 + CT-000.4 trên trang theo H5, mỗi luật dạng yes/no. (P68 · commit `9275bd59` + `d4d38d27` · Master Công thức ui `9bd5a22`)
- ➡ **H4.4** Thử 1 việc thật nhỏ (sửa 1 UI có sẵn) qua 10 tình huống GPT Pro nêu.
- **H4.5** Hội đồng thống nhất → Owner duyệt từng dòng.
- Chưa mở (sau H4.5): ghép 7 nhóm CC × Master List (rà mức ô cho 39 câu còn lại) · skill tự kiểm 43 câu cho agent · thanh lọc 45 luật cũ CAT-140.

#### H5. Phản biện vòng 2 GPT Pro — 29 điểm phải sửa
1. Cổng: «có câu trả lời» ≠ «điều kiện đạt»; Sai hoặc Chưa biết ở điều kiện bắt buộc đều chặn cổng; Không áp dụng chỉ theo Loại việc + lý do; câu của giai đoạn chưa tới không phải sự cố.
2. G4.1 = «mọi tiêu chí bắt buộc Đúng»; G4.2 đổi thành «thứ phải giữ ở G1.5 còn đúng không».
3. G1.9 chưa có Loại việc ⇒ dừng ở G1, giao người bổ sung quy trình, có hạn.
4. Đưa xác nhận song song · giữ việc · chống trùng · nơi ghi · gửi ngoài · bù lên cổng G2 (trước lần ghi đầu tiên).
5. G2.4–G2.6: số bản ghi mong đợi 0/1/n + nhánh khi lệch; dữ liệu đã dùng phải tái hiện được.
6. G2.8 phụ thuộc: mã không tồn tại · tự chờ mình · vòng A↔B · việc trước huỷ ⇒ trả về người sửa, không chờ vô hạn.
7. G2.9–G2.10: sau khi chờ phải kiểm lại quyền và phiên bản; đổi phiên bản phải có quyết định.
8. G2.11 trỏ công cụ có thật + thao tác + tham số + quyền.
9. G3.3–G3.4: phạm vi song song (hệ thống / loại / đối tượng); giữ việc: ai · lượt · hạn · gia hạn · thu hồi.
10. G3.5: Loại việc cho cách tạo mã thao tác, không cho mã cố định.
11. G3.6–G3.7: tạo khác sửa; tạo/sửa/xoá gì, bản ghi nào, trường nào, giá trị từ đâu.
12. G3.8, G3.11: đối soát và bù trỏ thao tác thật; không kiểm được ⇒ chờ người.
13. G3.9 trạng thái: bước hiện tại · đang chạy/chờ · chờ ai/gì · việc tiếp · hạn.
14. G4.7: M, N lấy ở cấu hình nào.
15. G4.3: số mong đợi · thực tế · chênh; G5.2: tổng xem ở đâu, tính bằng gì.
16. Vai phải ra người/agent cụ thể; hạn chờ thành thời điểm; gửi thông báo ≠ đã xác nhận nhận.
17. G1.1 mã Việc do máy cấp; G1.7 hạn có múi giờ; G5.4 cho phép «không có».
18. X1 phân 3 ca: gửi lại · phát sinh khi đang mở · tái phát sau đóng (mở lại + xếp hàng); giữ liên kết việc gốc.
19. X2: điều kiện được lấy việc (đến giờ, đủ điều kiện, chưa huỷ, không ai giữ, có người làm) + chống đói việc ưu tiên thấp.
20. X3: quy trình đã duyệt, còn dùng, đủ tham số và công cụ.
21. X4: nhận việc bằng 1 thao tác nguyên tử, có bằng chứng; chờ người = trạng thái chờ, không giữ lượt vô hạn.
22. X5 xử lý đủ 6 kết quả G4.6 + hết lượt; thử lại quay về X2 (không X4); thiếu quyền/dữ liệu sai không tự thử lại.
23. X6 kiểm lại MỌI điểm chặn của việc gốc trước khi cho chạy tiếp.
24. X7: Vấn đề ghi đâu, việc MMOW nào nhận, gộp trùng nguyên nhân; không có MMOW ⇒ X9.
25. X8: quy trình mới qua thử + duyệt (CT-001); chỉ xếp lại việc còn mở; giới hạn vòng tính theo việc gốc.
26. X9: 4 lựa chọn tiếp tục · giao lại · huỷ/kết thúc · ngoại lệ có phạm vi; chờ Owner có hạn + người thay; không tự cho qua.
27. PG: «ghi sự cố + xếp hàng» trong cùng 1 giao dịch thật; rollback không huỷ tác động bên ngoài; không giữ transaction lâu; UPDATE 0 dòng phải có nhánh; NOTIFY + quét bù khi kết nối lại; PG chết ⇒ giám sát ngoài PG; CHECK không thay kiểm quy trình; Directus Flow phân biệt Filter / Action.
28. Sổ chưa chốt vai: CAT-206* (định nghĩa hay trả lời?) · CAT-228* · CAT-230* (định nghĩa hàng đợi hay dòng việc?) · CAT-238* (3 ứng viên) · CAT-069 (đang trỏ feedbacks).
29. Mỗi bước có 1 hàng thao tác: Đọc ở đâu · Làm bằng gì · Ghi vào đâu · Hoàn thành · Không hoàn thành.
30. (mục 3 bản GPT Pro) 1 hay nhiều hàng đợi: 1 nơi ghi việc chờ + màn lọc; tách hàng chỉ khi khác quyền, khác công cụ, cần cách ly tải.
31. (mục 3) Từ 1 việc đang mở phải thấy: việc + việc gốc · bước · trạng thái + lý do · ai chịu trách nhiệm · lượt + hạn giữ · kết quả gần nhất + lần thử/giới hạn · việc kế + khi nào · điểm chặn + bằng chứng.
32. (mục 6) 10 tình huống thử → H4.4.
> P68 đã giải 1–31 trên trang. Điểm 28: vai các sổ chốt ở «Bảng Sổ của vòng xử lý» (CT-000.4); riêng ánh xạ CAT-069 ↔ bảng PG `feedbacks` làm lúc ghi PG (VD-029). Điểm 30: 1 bảng việc CAT-228* (chuẩn River/Oban), khớp CT-007 đã chốt. Điểm 31: câu G3.9.

#### H6. Nguyên tắc Owner đã nhắc trong phiên — không để nhắc lại
1. Không tạo khái niệm, kiểu trình bày mới: dùng lại cái có sẵn (nút số `cf-root-no` của thẻ Bước, khuôn «?» `t1-mapping-table__help`). Tra PG/repo trước khi đặt tên.
2. Tên ngắn nói bản chất; mã chỉ cho máy; dòng mã phụ chữ nhỏ mờ nhưng có nhãn («mã loài: …», «mã master list: …»).
3. Mỗi loại số 1 chữ đầu (G / CC / X); không để nhiều «số 1» khác nghĩa.
4. Mọi bảng có tên bảng + «?» ở tên và từng cột; chấm trong bảng nhạt hơn chấm trên thẻ.
5. Không để ô trống: mã · 🟡 có sổ thiếu ô · 🔴 chưa có · ⚪ không cần.
6. Ít chữ trên mặt; giải thích giấu vào «?», «Chi tiết», chữ hiện khi rê chuột.
7. Thiết kế phải duyệt được từng dòng; hội đồng (GPT Pro phản biện) thống nhất trước, ghi vào repo.
8. Chuẩn ngành IT, không hùa Owner, không tự sáng tạo; tìm chuẩn tốt nhất và dẫn nguồn.
9. Không nói chung chung: mỗi luật yes/no, 1 cách làm; tư duy tận cùng, không để nhánh lửng lơ.
10. Đi từng bước, mỗi lần 1 việc; không tự sửa MBM (CT-008) khi chưa được yêu cầu.
11. Đề xuất kèm sẵn 1 phương án, Owner chỉ gật/lắc.
12. Thiết kế PG từ yêu cầu, không đi khảo sát PG đang có gì (Owner 21/10 09:33); PG chỉ cần «có hỗ trợ».

#### H7. Mẹo kỹ thuật
- Sửa trang: `fs_edit` root gh; tệp ~760KB, luôn dùng old_str nguyên văn; báo «không khớp» thì `fs_search` lấy nguyên văn; push bị từ chối (phiên khác vừa đẩy) thì gửi lại cùng expected_version.
- Trang xem giữ bản cũ: mở `ui-preview/hpml-view-for-user/view.html?task=mow-mot-moit-mout`, bấm `header button`, đợi ~18 giây, rồi chụp `knowledge/modules?…&section=<id>`.
- Công cụ chụp không mở được «Chi tiết» trong khung trang → kiểm bằng đếm mã (`fs_search` count) và nói rõ giới hạn.
- Đọc PG: `query_pg` database `directus` (chỉ đọc). `directus_read` đang lỗi phân giải tên miền.
- Neo trang: `formula-ct-000-1` … `formula-ct-000-4` · `formula-ct-001` … · `kn-cat-000-5`.
- Mỗi lượt sửa: cập nhật Bảng điều khiển + Nhật ký (P tăng dần) trong COLLAB này.

#### H8. Nợ đang treo — không làm xen
- VD-029 ghi CAT-000.5 vào PG (2 cột Quản lý tại · Lớp; ~65 loài mới; 4 bảng vô chủ; mã mồ côi audit_log; 6 loài lệch tiền tố).
- L0–L6 → đề xuất thay bằng FAC-02 «Vai trò hệ thống» (5 giá trị có sẵn). **Chưa áp lên trang, chờ Owner.**
- ĐL1–ĐL6 → đề xuất chuyển thành dòng Điều luật (CAT-140). Chờ Owner.
- CAT-201* giá trị cố định (Cấp ghép, Lớp, Bước, Tầng, Mốc, Câu hỏi) chưa lập · CAT-250* Miền CV chưa lập.
- MBM M2–M6 · VD-028 · lỗi DNS Directus.
- (P68) CAT-000.5 dòng SPE-QUE* «⚠ thiết kế lệch (CAT-228*)» đã giải ở Bảng Sổ CT-000.4: dòng chờ = CAT-228*, CAT-230* = danh mục hàng đợi (định nghĩa). Sửa dòng loài khi làm VD-029.
- (P68) 🔴 Bảng nối Sự cố ↔ Việc gốc (1 dòng = 1 lần phát sinh, khoá = mã sự kiện) chưa có sổ, chưa có mã CAT — lập khi lên collection.
- (P68) Các «1 hàm PG», «Directus Flow lịch» trong 13 yêu cầu PG là yêu cầu thiết kế, chưa có công cụ thật — dựng khi lên PG (thiết kế từ yêu cầu, H6.12).

### BẢNG ĐIỀU KHIỂN · cập nhật 2026-10-21 14:50 +07 · Claude · P68

> **⏳ Chờ hội đồng rà rồi Owner duyệt từng dòng:** CT-000.1 + CT-000.4 bản luật yes/no (P68, trang Công thức, Chi tiết của 2 thẻ). Phản biện vòng 2 GPT Pro (21/10 14:19) = 29 điểm ở H5 + 3 ý thêm (30–32); P68 giải 1–31: **Luật cổng** Đúng · Sai · Chưa biết (chỉ Đúng qua; Không áp dụng chỉ theo Loại việc + lý do) · **cột Đạt khi** cho 43 câu · cổng 1 đường (bảng quyết định DMN Unique) · **X1–X9** thành hàng thao tác Đọc · Làm · Ghi · Kết quả · **Bảng Kết quả lượt** 7 kết quả, mỗi kết quả 1 đường (chia lỗi theo gRPC) · **Bảng Sổ** (hàng đợi = dòng chờ CAT-228*, khớp CT-007; CAT-206* = khuôn) · **13 yêu cầu PG** có phép thử yes/no · **2 Bảng Chuẩn ngành** (32 chuẩn có nguồn) · khuôn viết luật EARS + RFC 2119 ở CT-000.2. Kế tiếp H4.4 (thử 1 việc thật qua 10 tình huống), rồi gửi GPT Pro rà 1 vòng gồm cả kết quả thử.
- ⚠ Mỗi lượt sửa task: sửa luôn các dòng tổng — giờ cập nhật · ✅ · ⬜ · ➡ · tên việc (nếu mục tiêu đổi).
- 🎯 Mục tiêu: ô 1. Vì sao: bài thử MBM — lần 2 không có Owner, AI vẫn tự chạy.
- 🏁 Xong khi: ô 2.
- 📍 Tiến độ (MBM 6.x): [✓ 6.1 Nhận yêu cầu] → [✓ 6.2 Tạo task] → [✓ 6.3 Chốt mục tiêu] → [◐ 6.4 Liệt kê bước — bản thử] → [◐ 6.5 Bộ câu hỏi] → [■ 6.6 Check Master list] → [□ 6.7 Ký] → [□ 6.8 Chạy]
- ✅ Đã xong: ô 1–2 (18/10 21:25) · rà tới hết mục 4 theo MBM r5.34: 8 bước (5 cố định + 3 chuyên môn) · bảng câu hỏi H1–H7 + Đ1, Đ2 · K1, K2 đã gỡ — xem tab «Nội dung công việc» (`view.html`) · 19/10: Info contract chuẩn ngành, Config + Saga, ý kiến Astra ngoài MBM · M1: QTTH đổi tên MMOW, 4 tầng MBM → MMOW → MOW → Hồ sơ (MBM r5.35) · tên hiển thị «Master MMOW», «MMOW 05/06» trên các trang (mã khoá ML-MOW-TH-001 / MOW-TH-xxx giữ tới khi lên collection — nợ 🔴 VD-027) · Master MMOW có dòng MMOW-007 (việc này), trang hiện mã MMOW-xxx · 18:28: MMOW 07 chỉ Vẽ UI; Master MMOW thêm MMOW-008 (Info contract), MMOW-009 (Config) · 22:26: Master MOW có 3 cột tích Vẽ UI · Info contract · Config (35/35 ☐; tích trên giao diện = nợ VD-028) · 20/10: trang Công thức có khối KHÁI NIỆM · CAT-000.5 (54 loài, 5 định luật ĐL1–ĐL5, ký hiệu tạm chờ vector); MMOW mã OBJ-MMOW · 14:18: CAT-000.5 hợp nhất 107 loài mã SPE (gộp entity_species + khái niệm nháp + CAT-237*; quét máy Q1–Q6: 4 bảng vô chủ, mã mồ côi audit_log, 6 loài lệch tiền tố, 10 sổ 2 mã) · Master Duyệt thiết kế có CAT-000.5 + cột Duyệt TK (xanh = User đã duyệt; CAT-000.5 tạm duyệt 20/10) · nợ VD-029 (ghi PG) · 15:08: chuẩn «?» cho mọi bảng mới (ĐL6), CAT-000.5 đã có «?» ở tiêu đề, ma trận, 8 cột · 17:32: trang Công thức có 2 thanh thu/mở «Công thức gốc» (CT-000.2 Cấp ghép 1–4) + «Công thức chuyên môn» (CT-001→008); 14 thẻ có dòng mờ loài + sổ · 20–21/10: Công thức gốc (21/10 09:51): CT-000.1 Bộ câu hỏi chuẩn (43 câu Trước · Trong · Sau + 1 luật rẽ nhánh; gộp Info contract law) · CT-000.2 Điều luật (+ Xử lý bằng) · CT-000.3 Cấp ghép · CT-000.4 Xử lý lỗi = quy trình 9 bước (Ghi sự cố → Xếp hàng → Tra quy trình → Chạy → Kết quả → Kiểm lại · Vấn đề → MMOW → Owner). 10:02: CT-000.1 không đạt ⇒ chỉ vào hàng đợi (bỏ «Thiếu ⇒ Tạo mới»: khái niệm, không phải bước làm). Kế tiếp: skill tự kiểm 43 câu cho agent (chờ Owner). · 21/10 P68: CT-000.1 + CT-000.4 thành luật yes/no theo chuẩn ngành (commit 9275bd59, d4d38d27; Master Công thức ui 9bd5a22).
- ■ Đang làm: — · 0 RUN active
- ⬜ Còn lại: chốt 6.4 → đạt 6.5 → 6.6 → 6.7 → 6.8.
- ➡ Kế tiếp: H4.4 thử 1 việc thật (sửa 1 UI có sẵn) qua 10 tình huống GPT Pro → GPT Pro rà 1 vòng → Owner duyệt từng dòng (H4.5). Sau đó: Owner duyệt Miền CV (CAT-250*) + nháp MBM 3.3 viết theo luật CAT-000.5 (Bước làm = Mục tiêu + Miền CV + Công thức) → sửa MBM M2–M6 (ô 3, «Chờ bàn khi sửa MBM») → viết lại bước chuyên môn MMOW 07 (chỉ Vẽ UI; bước 3.2, 3.3 cũ chuyển sang MMOW 08, 09) → hoàn thiện MMOW 07.
- ⛔ Không làm: G2/PG production · dựng collection trước khi ma trận được ký · gõ tay vào Directus.

### 1. Mục tiêu
Tình trạng: User chốt (Owner 19/10 18:28).
Owner 19/10/2026 18:28 (thay bản 18/10 21:25): mỗi MMOW chỉ giải quyết 1 việc.
1. Vẽ UI (gồm tất cả bước con) cho các MOW trong Master MOW — sẽ vẽ hàng ngàn UI. Trước mắt gắn theo list MOW; sau này gắn thêm list Task, MOIT, MOUT.
Đã tách: Chốt Info contract → MMOW 08 · Config → MMOW 09 (Master MMOW).
Owner 16/10 16:29: đây là bài test MBM — vừa làm vừa sửa MBM để lần 2 không có Owner, AI vẫn chạy được.

### 2. Thế nào là hoàn thành
Owner 18/10/2026 21:25, ý 1 (giữ cho MMOW 07):
1. Vẽ đủ UI theo các bước con (kể cả tách hoặc gộp theo bước con nếu có). → bước con thiếu UI = 0.
Ý 2 (đầu mối Info contract) → MMOW 08 · ý 3 (sẵn sàng Config) → MMOW 09.
D1, D2 (MBM 2.5, không chặn): đã rà — xem tab Nội dung công việc, mục 2.

### 3. Chi tiết cần đạt (AI ghi, Host kiểm)

Kết quả bước 3, bước 4 và vấn đề lộ ra: tab «Nội dung công việc» trên trang Task (tệp `view.html` của việc này) — 1 nơi, không chép lại ở đây. Vấn đề và nợ kỹ thuật (mẫu CAT-069, mã VD-…): cũng ở đó — không dựng hệ phức tạp, xong MMOW 07 thì lên collection + DOT.

#### 📏 Chuẩn chung (Owner 20/10 15:08)
- Mọi bảng mới có «?» ở tiêu đề bảng và từng cột, giải thích cái gì + hướng dẫn cho người mới. Lên collection vẫn giữ: «?» = ghi chú (note) của bảng và của từng trường. (CAT-000.5 ĐL6)
- CAT-000.5 tạm đặt trên trang Công thức; sau chuyển sang collection (nợ VD-029).

#### ⏳ Chờ bàn khi sửa MBM (Owner 19/10 17:36)
| Mã | Việc | Nguồn |
|---|---|---|
| M1 ✅ | Đầu MBM nói rõ 4 tầng MBM → MMOW → MOW → Hồ sơ; QTTH đổi tên MMOW (Mother of MOW) — MBM r5.35 | Astra hiểu nhầm; Owner 19/10 17:46 |
| M2 | Định nghĩa bước chuyên môn (đề xuất: mục tiêu = mục con 3A, bước = việc làm) + hướng Owner: mỗi MMOW chỉ làm đúng 1 việc | Owner 18/10 21:47, 19/10 17:00 |
| M3 | 1 bước chuyên môn × 1 đối tượng = 1 việc con ở CAT-227 (mã việc cha); bước cha xong khi mọi việc con 🟢 | Astra mục 1 |
| M4 | Tên mục tiêu = trạng thái cuối; MMOW 07 «Config thành công» → «Sẵn sàng Config» (Owner gật); mỗi bước chuyên môn có 1 lần thử thật (nghiệm thu) | Astra mục 4 |
| M6 | Ví dụ MMOW 07 trong MBM (3.3.3 ba dòng, 4.2 «bước Config thành công», 9.6) đổi theo MMOW 07 chỉ Vẽ UI | Owner 19/10 18:28 |
| M5 | Bước «Chốt hợp đồng thông tin» của MMOW 07 dùng Info contract chuẩn mới (CT-006.2, 8 thành tố) làm tiêu chí xong | CT-006.2 19/10 17:25 |

#### ☑ Việc cần làm — đọc lại mỗi lượt, xong tích kèm commit
| MBM | Việc | Ai | Xong khi | |
|---|---|---|---|---|
| 6.1 | Nhận yêu cầu | 🤖 | lời Owner ở Nhật ký | ☑ |
| 6.2 | Tạo task + tên + view.html | 🤖 | đúng khuôn, tên `mbm-`, có `view.html` | ☑ `579bec00` |
| 6.3 | Chốt mục tiêu | 😊 | Owner viết ô 1–2 | ☑ 18/10 21:25 |
| 6.4 | Liệt kê Mốc · Mục con · Bước | 🤖 | 3 bảng 3.1–3.3 đủ dòng, mỗi dòng có Câu hỏi + Hoàn thành, 0 ô ❓ | ◐ bản thử 18/10 21:40 theo MBM r5.34 (8 bước: 5 cố định + 3 chuyên môn; Mốc 4 = tích 🟢/🔴) ở view.html |
| 6.5 | Bộ câu hỏi | 🤖 | mọi bước đủ ô | ◐ bảng câu hỏi MMOW 07 = H1–H7 + Đ1, Đ2 · 8 bước · 0 ô trống |
| 6.6 | Check Master list | 🤖 → 😊 | bảng kiểm kê đủ mọi sổ, DOT, Tool; Tình trạng = «có» hết | ■ bảng ở view.html · Master list 6/19 «có» · DOT, Tool chưa điểm danh |
| 6.7 | Ký | 🤖 Hermes kiểm · ✍️ GPT, Gemini · 😊 Owner | 0 ô trống, 0 phản đối (User quyết ký hay bỏ qua) | ☐ |
| 6.8 | Chạy | 🤖 | đạt ô 2 | ☐ |

#### HỘI ĐỒNG — COUNCIL_BOOTSTRAP_V1
| Ghế | Hãng | Bề mặt | Vai | Gọi bằng |
|---|---|---|---|---|
| Claude | Anthropic | Claude Chat (`[auth:claude-chat]`) | Host | Owner làm việc trực tiếp |
| GPT Chat | OpenAI | GPT Chat (`openai-mcp`) | Council · ghế ký | Owner chuyển tay |
| Hermes | Hermes VPS (DeepSeek) | `agent-gw/hermes` | Council · ghế ký · việc thường | Owner chuyển tay |
| Gemini | Google | `gemini-agy` | Council · ghế ký | Owner chuyển tay |
Mode=COUNCIL · Automation_Level=AUTO0 · Khác mặc định: luật quyết = luật ký MBM (CT-008)

#### Sổ vấp MBM — lịch sử V1–V19 (từ 18/10 vấp ghi ở bảng vấn đề mẫu CAT-069 trong view.html)
| # | Vấp | Đã sửa ở CT-008 |
|---|---|---|
| V1 | thiếu bước tạo task | r4.3 |
| V2 | chưa có khuôn tên task | r4.3 |
| V3 | sai thứ tự; task chưa có danh sách việc | r4.4 |
| V4 | tên task chưa cho biết nguồn gốc | r4.5 (`mbm-`) |
| V5 | ma trận đủ A1–C4 từng dòng quá dài | chưa sửa — đổi bộ câu hỏi cần hội đồng |
| V6 | Host bỏ qua bản 25 bước đã gật, tự viết mới (17:25) | r4.6: có bản cũ thì bắt đầu từ bản cũ |
| V7 | bước trỏ tới sổ và lệnh chưa có — AI thường không làm được (18:01) | r5: thêm bước Check Master list |
| V8 | mục «Chia mục và đặt mã» dài, làm không được (20:41) | r5: bảng mẫu |
| V9 | Check Master list đặt trước khi có bước là ngược (21:12) | r5.1: Bước → Check Master list → Bộ câu hỏi |
| V10 | tên bước ngắn, mỗi AI hiểu một kiểu (21:12) | r5.8: thêm cột Câu hỏi cần trả lời + Thế nào là hoàn thành (Owner 22:57) — thay đề xuất «Ra cái gì» |
| V11 | mục 4 không nói tra số lượng ở đâu; Sổ của các sổ rỗng (22:15) | chưa sửa — đề xuất ghi nguồn kiểm kê chuẩn vào mục 4 |
| V12 | bộ tình trạng mục 4 thiếu «rỗng», «dùng lại» (22:15) | chưa sửa — chờ Owner |
| V13 | mã sổ trong bước và tên sổ thật lệch nghĩa (CAT-227/228/239) (22:15) | chưa sửa — đề xuất thêm ô «nghĩa khớp?» vào bảng kiểm kê |
| V14 | kết quả bước 3–4 đặt ngoài ô 3 nên trang Task không hiện; «repo» và «workspace» mỗi bên hiểu một kiểu (Owner 22:07) | r5.6 mục 6: «làm ở workspace» |
| V19 | D1/D2 ghi «trả lời ở dòng MOW» + mục 6 bước 7 bắt trả lời trước khi ký → AI hiểu là việc phải giải xong trong quy trình và biến thành chỗ chặn (Owner 17/10 05:46) | r5.11: D1, D2 là câu hỏi mở, không chặn; ghi chú ẩn giải thích bản chất |
| V18 | Thử như AI mới mục 2: luật «mỗi gạch có số» mâu thuẫn lời User; hoàn thành 1–3 gạch quá ít; chưa rõ hội đồng có phải ký mục tiêu User tự viết (17/10 05:28) | r5.10 (Owner 05:36): AI viết số theo chuẩn, bám nội dung User · hoàn thành 3–5 gạch · User quyết ký/bỏ qua, User duyệt bắt buộc |
| V17 | Host tự đặt bước UI («hành động», «màn») thay vì dùng CT-004/CT-006 có sẵn; rà xuống dữ liệu MOW-001 (con) khi QTTH 07 (mẹ) chưa xong (Owner 17/10 05:15) | r5.9 (Owner 05:22): tiêu đề «3.3 Bước (nền tảng = nhóm con, có thể điều chỉnh cho sát thực tế)»; gỡ ghi chú Host tự thêm |
| V16 | mục 3 chỉ có 1 bảng bước, thiếu tầng Mốc và Mục con có câu hỏi + hoàn thành (Owner 22:57) | r5.8: mục 3 = 3.1 Mốc · 3.2 Mục con · 3.3 Bước |
| V15 | chuyển vào ô 3 vẫn không đọc được: tab Kiểm soát in thô bảng và ô 3 mặc định gập; tab Nội dung báo «Chưa có view» (Owner 22:19) | r5.7: bảng kết quả ghi vào `view.html` của task → tab Nội dung công việc; tạo task kèm `view.html` |

### Vòng trước
- 16/10 17:05 (Owner, 5 mục tiêu): nay thay bằng bản 18/10 21:25 (3 mục tiêu: Vẽ UI · Chốt hợp đồng thông tin · Config thành công).
- 16/10 15:19 (Owner, nay gộp vào ô 1 bản 17:05): vẽ UI theo Master MOW · hoàn thiện Master list, điền đủ SSOT · đủ trường để Config · dùng DOT tạo collection.
- 15/10 (Owner, G1): vẽ UI, liệt kê trường còn thiếu để chốt hợp đồng thông tin, đủ trường để Config · 17:40: cái gì phát sinh cũng ghi vào Master list và kiểm đã ghi đủ.

## Nhật ký (nguyên văn Owner, giữ lỗi gõ)
- P68 · 21/10 14:30 · «Chúng ta chuyển phiên… Bạn đọc ký HO và tài liệu, tiếp tục chỉnh sửa nhé.» — «ý kiến phản biện của GPT. Nguyên tắc là không nói định hướng, khôgn nói chung chung (nguyên tắc) chúng ta phải thiết kế để thế nào là yes thế nào là no rõ ràng, chỉ có làm theo 1 cách thôi mới được nhé. Chuẩn của ngành IT đâu? mang ra đây áp sát vào? Kiếm những chuẩn tốt nhất ra giúp tôi xem nào?» → H4.1–H4.3: CT-000.1 + CT-000.4 luật yes/no, 2 Bảng Chuẩn ngành.
- P67 · 21/10 11:16–14:22 · «…chấm trong G, CC nhạt hẳn xuống… nên có tên bảng… bổ sung 1 cột master list…» — «…chưa có thì ghi chưa có màu đỏ… bạn để trống thì hiểu thế nào?…» — [GPT Pro phản biện vòng 2] — «…thiết kế để thế nào là yes thế nào là no rõ ràng… Chuẩn của ngành IT đâu? mang ra đây áp sát vào?…» — «Viết cho tôi 1 Hand off để chuyển phiên mới…» → HANDOFF P67.
- P66 · 21/10 10:39–10:46 · «Đây là ý kiến đầu tiên của GPT pro… phải tìm ra 1 công thức vạn năng… vẽ cho tôi bức tranh về các nhóm công cụ… không phải việc gì cũng cần trả lời hết…» — «…ngay từ ông yêu cầu cũng phải chuẩn… khai báo chưa chuẩn thì dừng ở chỗ khai báo… đầu ra trước mắt là 1 Công thức 2 Chia giai đoạn 3 Danh sách các công cụ cần… cả hội đồng thống nhất trước khi tôi duyệt… Bạn tiếp tục điều chỉnh bộ câu hỏi chuẩn» → CT-000.1 v2.
- P65 · 21/10 10:02 · «Thiếu => tạo mới chưa đúng => logic gốc mà bị sai… Nguyên tắc là thiếu => đưa vào hàng đợi + quản lý vòng đời… work Flow chúng ta phải đi bộ từng bước… đây là làm cơ mà?» → CT-000.1 không đạt ⇒ hàng đợi; CT-000.4 = 9 bước.
- P64 · 21/10 09:29–09:51 · «…sai thiếu ở bất cứ khâu nào… phải ghi vào 1 nơi để quản lý hàng đợi… gọi các quy trình liên quan… không có thì quay lại hàng đợi…» — «PG bạn không phải kiểm tra… thiết kế từ yêu cầu…» — «…cần đẩy các số thứ tự lên để dành cho Công thức đầu tiên: BỘ CÂU HỎI CHUẨN CT-000.1… Mọi việc dù lớn nhỏ chỉ cần 1 bộ câu hỏi chuẩn… trước, trong, sau… không quá 50 câu… nếu thiếu thì làm gì… nếu được thì sao? Nếu không được thì sao?… chuẩn ngành IT…» → CT-000.1…000.4.
- P63 · 20/10 20:15 – 21/10 08:08 · «…Không tạo ra các concept mới. Dùng lại…» — «…sổ điều luật… Không có số quản lý…» — «…Điều luật… STT… nhóm nằm ngang… ‘?’… mã cũ còn trống thì dùng…» — «…Ai làm? Đầu vào cần gì? Thế nào là hoàn thành?… tư duy theo chuẩn ngành IT…» — «…Infor contract law… giống như skill để cả agent code tự kiểm tra…» — «…Thiếu thì sao? Sai thì sao?… Mục tiêu là xong việc chứ không phải là dừng… gọi 1 trong những quy trình có sẵn… Luật đâu? Bảng nào? Công thức gốc gì nữa?» → CT-000.1 + CT-000.1.1.
- P62 · 20/10 15:26–17:32 · «…Nguyên tử… gọi là khái niệm gì? Có mã gốc không?…» — «…Các công thức CT… đưa vào loại gì?… Hãy nhìn vào bản chất, đừng nhìn vào tên…» — «…Bắt đầu từ việc nhỏ. 1 cái tên ngắn gọn…» — «Cấp thì sao?… Cấp ghép…» — «…Có nên đưa cấp ghép vào nhóm hiện tại không? Hay nên lập ra 1 loại công thức riêng?…» — «…thanh thu ra thu vào ‘Công thức chuyên môn’: CT đầu tiên: Cấp ghép 000.2… Cấp ghép 1 (~ nguyên tử) => 2 => 3 => 4… mã loài công thức… mã master list… mờ thôi» → CT-000.2 + 2 thanh + dòng mờ.
- P61 · 20/10 15:08 · «Được rồi sẽ tạm 000.5 vào đây => sau này chúng ta chuyển sang collection cho nhanh. Mặc định các bảng mới tạo dùng "?" để giải thích nó là cái gì cũng như hướng dẫn… Sau này chuyển vào collection cũng duy trì cơ chế "?".» → ĐL6 + «?» cho CAT-000.5 + chuẩn chung trong task.
- P60 · 20/10 11:20–14:5x · «L0 L1, L2… chấm to chấm nhỏ… cái mẹ thì to hơn cái con…» — «…những gì có từ 2 đối tượng cùng loại => phải có Master list… còn có loài nào đang mô côi…» — «Đồng ý ghép 3 cái này thành 1… trong 000.5 tối thiểu: Mã loài · Tên · Quản lý tại · Mô tả · thuộc khái niệm nào · L0–L6 · ĐL1–ĐL5…» — «Bạn dựng đi… quét lại bằng máy…» — «…master of master là danh sách tổng… Những master list mới bổ sung + 000.5 cần phải được hiện ở bên này… Chuyển màu xanh với những phần đã duyệt thiết kế…» → CAT-000.5 hợp nhất; cột Duyệt TK.
- P59 · 20/10 10:02–11:11 · «Phải có định nghĩa miền là gì?… Miền CV… cần phải có 1 bảng master list Miền CV…» — «chúng ta thiếu 1 master list mà lẽ ra chúng ta phải làm đầu tiên: Master of concept (khái niệm)… CAT - 000.5… Nguyên tử = 1 chấm, phân tử bằng 2 hoặc 3 chấm… Hợp chất… Vật liệu… mã loài… Toàn bộ tôi chỉ cần ở trang Công thức… nguyên tắc chỉ là công thức và định luật.» → khối CAT-000.5 trên trang Công thức.
- P58 · 19/10 22:11–22:26 · «Bước trong MBM: Mục tiêu chuyên môn của MMOW + Phạm vi công việc + 1 công thức (CT001–CT007)… 35 chỉ là ví dụ… đó là miền nhiệm vụ… Ta ghép từng bước… Mỗi lần chúng ta chỉ ghép 1 bước… Trong ML-DEF-004 · Master MOW chúng ta cần thêm 3 cột check box: Vẽ UI, Infor contract, config…» → 3 cột tích; nháp MBM 3.3 gửi Owner duyệt.
- P57 · 19/10 18:28 · «Như tinh thần chúng ta nói là để bớt phức tạp hóa cho MMOW => mỗi MMOW sẽ chỉ giải quyết 1 việc để cho dễ. => MMOW 007 chỉ là vẽ UI. Nó sẽ vẽ hàng ngàn cái UI. chúng ta sẽ có: MMOW 008 là chôt contract infor, MMOW 009 là config… nguyên tắc là chỉ làm 1 việc duy nhất… Danh sách thiết kế UI thì trước mắt gắn theo list mow, sau này có thể gắn thêm vơi list Task, list MOIT/MOUT... nhưng trước mắt hoàn thiện được MMOW 007 đã.» → Master MMOW: 007 chỉ Vẽ UI, thêm 008, 009; ô 1–2 theo Owner; M6.
- P56 · 19/10 18:14–18:18 · thanh Master MMOW trên Master Home; «Mã bạn vãn đang để: MOW-TH-001 chứ không phải MMOW à? Chúng ta đang chốt làm thử QTTH 007 để thử MBM sao không thấy có trong này??» → thêm dòng MMOW-007 (khoá MOW-TH-007); trang hiển thị mã MMOW-xxx, mã cũ ở «Tên/mã cũ».
- P55 · 19/10 18:04 · «Như vậy là do cơ cấu bảng phức tạp, chúng ta chưa thể tạo ra được bảng master view như các bảng khác cho MMOW đúng không? Nếu phức tạp quá thì ghi nợ vào MBM cũng được.» → master view MMOW đã có (UI.MASTER); nợ là chưa collection + mã khoá cũ → VD-027 🔴 ở CAT-069 (Ô bước MBM 6.2).
- P54 · 19/10 17:56 · «Đồng ý nếu sửa không mất quá nhiều thời gian thì bạn sửa luôn giúp tôi.» → đổi tên hiển thị 10 tệp trang + catalog TQT; mã khoá (ghim trong code, >100 chỗ) giữ tới khi lên collection.
- P53 · 19/10 17:40–17:46 · «Bây giờ quay trở lại chúng ta sửa MBM… AI thông minh nhất hiện nay vẫn hiểu => thì ghi chép chả có nghĩa…» — «MOW là mow. Mow là các quy trình đích đến. Còn QTTH là để sinh ra các quy trình trình đó…» — «Giờ tốt nhất đổi QTTH thành MMow (mother of mow) ghi rõ như thế để đỡ nhầm lẫn khái niệm…» → MBM r5.35: 4 tầng MBM → MMOW → MOW → Hồ sơ; task đổi tên MMOW 07 (nhật ký cũ giữ nguyên chữ QTTH).
- P52 · 19/10 17:36 · «Tất cả những gì liên quan đến MBM bạn tổng hợp lại, chúng ta sẽ bàn khi sửa đến MBM. Còn vấn đề gì astra có ý kiến ngoài MBM nữa không?» → danh sách M1–M5.
- P51 · 19/10 17:31 · «Đồng ý nếu mà ngành IT đã giải câu đấy chuẩn rồi thì bạn làm theo ngành IT đi… các bạn mới là người biến nó khả thi và các bạn phải tận dụng tất cả những kiến thức của ngành IT để đưa vào đây… Phần này bạn sửa đi và chúng ta sẽ đi tiếp phần tiếp theo của astra trước khi chúng ta quay lại sửa MBM» → Config 3 ô Song song · Chạy lại · Hết giờ; LC theo Saga.
- P50 · 19/10 17:15–17:25 · Info contract: «…Bắt buộc trong công thức 006.2 là cái gì vậy?… hợp đồng thông tin nhiều khi còn phải đầy đủ hơn cả config…» — «Bạn phải rà soát tổng xem nó là cái gì và thực tế ngành IT làm thế nào??? chứ tôi nói gì bạn làm cái đấy…» — «Rồi bạn tạm ghi vào đi và bạn phải lưu ý là quét đầy đủ thông tin trước khi trả lời…» → CT-006.2 theo chuẩn ngành; bỏ ô Bắt buộc; Config nhận định tuyến kết quả.
- P49 · 19/10 17:00–17:08 · ý kiến Astra: «…Astra chưa hiểu được là quy trình tổng hợp là quy trình trung gian chứ không phải quy trình sản phẩm… Mục 2… tôi đồng ý là vấn đề cần phải sửa… Đi từng việc 1» — «Chúng ta đang bàn về công thức. Tư duy đơn giản là chỗ nào có thể nhầm chúng ta phải đưa thành phần bản ghi vào đó. Thế còn bản khi nào, thì vào chi tiết… Đây là công thức tổng mà?» → Info contract thêm ô Bản ghi; Chi tiết: cùng mã hồ sơ, LC-8. Ghi nhớ cho MBM: câu đầu phải nói QTTH là quy trình trung gian làm ra quy trình sản phẩm.
- P48 · 19/10 16:55 · «Phần đề xuất của bạn: cái đó bạn ghi ghi chú tạm vào chi tiết, tôi chỉ nhìn vào những cái thứ đơn giản tôi mới tư duy được. Còn chi tiết là việc của các bạn… Miễn là chạy được là ok… trừ MBM là cái đầu tiên cho nên phải thiết kế cho đúng logic để nó chạy.» → LC-1…LC-7 + nơi lưu khi chạy ghi 1 lần ở Chi tiết UI Con; Info contract, Config chỉ trỏ về.
- P47 · 19/10 16:39–16:46 · «hàng đợi, lượt chạy chưa thấy có trong công thức thì điều phối kiểu gì?» — «đưa thành công thức con của config có hợp lý không nhỉ?… nó có 1 thành tố trong 1 ô +… Phải đi từ cái đơn giản đến cái phức tạp. Tạo ra công thức là để xử lý các vấn đề phức tạp trở thành những lựa chọn đơn giản và ghép lại…» — «Mục 1 và 2 chị đồng ý» → Config thêm ô Hàng đợi + Lượt chạy; không tạo CT-007.1/007.2; điểm 3 (7 luật PG) chờ giải thích.
- P46 · 19/10 16:31 · «1. Dùng info contract cho nó ngắn. Tôi đã chỉ thị như thế rồi là có Ý của nó. 2. Cái này nó phải là con của UI con cùng hàng với config và cũng cho mờ đi 1 chút như config. 3. Những hệ thống như, hàng đợi, bảng chạy, lượt chạy..... chưa thấy bạn đưa vào đây… bảng lưu nơi lưu (tóm lại là thông tin vào ở đâu và ra ở đâu)… chi tiết kỹ thuật bạn phải tính kỹ chứ» (kèm 16:16: CT-006.1 để trống chừa chỗ chèn giữa) → Info contract · depth 2 · Vào/Lưu/Ra + khi chạy dùng sổ có sẵn (CAT-206*, CAT-248*, CAT-228*, MOIT, MOUT, CAT-069).
- P45 · 19/10 16:12 · «Vậy chị bổ sung thêm CT 006.2 info contract. Ít nhất chỗ này nó cũng giống như config, nhưng chỗ này bạn phải xét tới, cả các yếu tố của lượt chạy, hàng đợi.... nói chung cả config và inforcontract.... cần phải xét đến cái này (về câu chuyện này mà thiết kế theo kiểu PG chứ tôi không rành lắm => bạn phải rà soát để làm sao chạy đúng chuẩn là được.» → CT-006.2 + 7 luật khi chạy dùng chung với CT-007.
- P44 · 19/10 16:03 · «1. Trước hết cần cho sửa công thức CT 007, đổi Nhóm => nhóm con… 2. Bên trên Config, vẫn nằm trong UI con => chúng ta làm hợp đồng thông tin (info contract). => chúng ta cần lấy 1 đối tượng để làm cha của info contract và tôi nghĩ là UI con (Bản chất gần như task) sẽ là hợp lý. Cái này phải áp vào nhiều trường hợp thực tế khác nhau thì mới nhìn ra được hết tất cả các góc cạnh… Cứ thử xây rồi tính. bạn sửa luôn điều 1, điều 2 tôi muốn nghe ý kiến bạn trước khi quyết định sửa thẳng vào Repo.» (chèn P43b: 18/10 21:47 «khoan hẵy sờ đến 007, quay lại MBM») → CT-007 đã đổi; điều 2 chờ Owner quyết.
- P43 · 18/10 21:31 · «Tôi thấy thông tin có vẻ không cập nhật ở đây. Bạn chú ý, việc này bạn đẻ lỗi nhiều lần rồi đó.» → sửa dòng tổng (tên việc, xác nhận User, giờ cập nhật, Đã xong, Kế tiếp, 6.3, 6.4) + dòng nhắc ở đầu Bảng điều khiển.
- P42 · 18/10 21:25 · 3 mục tiêu: «Mục tiêu của chúng ta chỉ có 3. vẽ UI · Chốt hợp đồng thông tin · Config thành công. Thế nào là hoàn thành: 1. vẽ đủ UI theo các bước con (bao gồm tách ra hoặc gộp theo bước con nếu có) 2. Đảm bảo các UI đó ghi đủ đầu mối hợp đồng thông tin (có phương pháp test, đếm phù hợp) 3. Đảm bảo kiểm đủ đầu vào và xác nhận sẵn sàng cho config (không thiếu thông tin). Đơn giản có thế này thôi mà?» → ô 1–2 thay bản 16/10; 3 bước chuyên môn; 8 bước.
- P41 · 18/10 21:18 · «1. K1: Kiểm tra thì chỉ tích xanh hoặc đỏ vào tất cả các các bước trong báo cáo. Vì chưa đến phần báo cáo => bạn cứ hướng dẫn như vậy là ok. 2. K2: Bạn giải thích thêm giúp tôi vấn đề là gì?» → MBM r5.33 (3.1 dòng 4 + 3.3.6).
- P40 · 18/10 21:05 · «Giờ bạn rà soát lại QTTH 007 để làm đến hết mục 4 theo MBM xem có khúc mắc những gì nữa? rồi tôi nhìn vào QTTH 007 sẽ cho ý kiến tiếp» → 9 bước + bảng câu hỏi; K1 (Mốc 4, 5 chưa có bước), K2 (mục tiêu trùng bước cố định).
- P39 · 18/10 20:57–21:01 · câu đặc thù: «Bản chất là: trong QTTH nếu nhiệm vụ của QTTH có những câu hỏi đặc thù riêng cần bổ sung thì thêm vào bảng câu hỏi chuẩn từ MBM cho riêng QTTH đó. viết cho rõ ràng» → MBM r5.32 (mã Đ1, Đ2…).
- P38 · 18/10 20:44–20:46 · H2: «H2 Lấy ở đâu? mã sổ nguồn CAT-206 · ML-DEF-008 — Câu này nghĩa là gì?… đừng ghi lung tung!!!» — «Bạn ghi rõ ràng như vậy. CAT-206 có đúng tên đính đặt không? trong danh sách này (master-design-review-v1.html) tôi chưa thấy có đâu đấy. Viết làm sao để dễ hiểu, tránh hiểu nhầm tối đa» → MBM r5.30: mã đúng là CAT-206* (có dấu *), sổ ghi mã + tên.
- P37 · 18/10 20:37 · sửa hướng dẫn 3.3.3: «1. Mục tiêu chuyên môn là ghi các yêu cầu cần hoàn thành do User chốt (ở phần mục tiêu) 2. Thế nào là hoàn thành?: Định nghĩa rõ từng mục tiêu chuyên môn hoàn thành là tình trạng thế nào? đó đếm nếu có? 3. Câu hỏi đặc thu: Ngoài các câu hỏi tiếu chuẩn (chuẩn H1–H7) thì mỗi QTTH có thể có thêm các câu hỏi riêng về chuyên môn đặc thù cần trả lời. Việc tôi liệt kê ngắn nhưng không phải là UI… bản chất là thiết kế UI (gồm tất cả các bước con) của các quy trình nằm trong master list mow. Ví dụ thì phải ghi như vậy. Ngắn gọn nhưng cần hiểu rõ, hiếu đúng và không thể hiểu nhầm!!!!!» → MBM r5.28.
- P36 · 18/10 20:17 · «1. Mục 3.3.3 cần có hướng dẫn dùng "?" như bảng của 3.1. Đây là hướng dẫn chuẩn nên cần viết rõ để tất cả hiểu thống nhất. 2. Phần câu hỏi nên đưa thành mục 4 vì dùng cho mục 3 => cấu trúc lại và hiệu chỉnh ở các nơi liên quan.» → MBM r5.27 + đồng bộ task.
- P35 · 18/10 18:25 · làm từng phần: «Tôi thấy bạn lại đang làm rối, làm từng phần nhỏ nhé. Trước tiên là MBM mục 3. Tôi chưa thấy sửa gì? Phải bắt đầu từ đó đã. làm từng bước, đừng rối tinh lên.» → MBM r5.26: chỉ viết lại 3.3 theo khuôn mục tiêu chuyên môn; QTTH 07 để lượt sau.
- P34 · 18/10 16:36–18:07 · bộ câu hỏi: «Câu hỏi cần cụ thể hơn kiểu: Cần cái gì? ghi cái cần ở đâu? đã ghi chưa? đã kiểm lại chưa??… Nguyên tắc là những cái gì lập đi lập lại thì đưa thành bộ công thức chuẩn» — «Đồng ý, bạn sửa vào MBM, làm thử quả QTHT 007 xem có vướng gì không? xác nhận đã, nếu không vướng, lượt sau chúng ta sẽ áp xuống QT 001» → MBM r5.25 (H1–H7 + đặc thù + ➖/🟡/🔴) + điền thử 19 dòng.
- P33 · 18/10 07:39–09:00 · định nghĩa Bước: «… Ý tôi là trong MBM phải định nghĩa bước là gì? nguyên tắc 6W thì đầu tiên what mà chúng ta toàn quên» — «Đồng ý. bạn sửa đi, và đưa thử vào QTTH 007, cuối cùng bước là những gì?» → MBM r5.24 + QTTH 07 còn 18 + N bước.
- P32 · 18/10 05:51 + 07:06 · CAT-069: «Đúng, Quy định đơn giản. Mọi nợ đều nằm trong CAT 068, có cột mã của 227. 227 và 069 (và có thể 1 số master list khác là sổ tông hợp của mọi con MBM. Làm như vậy thì sẽ hiểu được nhất quán. bạn sửa thật gọn. Cố gằng logic để ít chữ nhé. … Con người cần biểu tượng, suy luận logic, màu sắc để dễ nhận ra vấn đề.» («CAT 068» = CAT-069) → MBM r5.23 + CAT-069 đổi nhãn + bảng vấn đề VD-001…019.
- P31 · 18/10 05:30 · CT-006: «Trong phần côg thức: UI Con CT-006 Chuỗi+Bước+Tầng+Nhóm+UI cha⇒UI Con. Bạn đổi giúp tôi đây là Nhóm con (bản chất UI con chính là bước con, hay nhóm con (xét về số lượng và thứ tự)).» → CT-006 = Chuỗi + Bước + Tầng + Nhóm con + UI cha ⇒ UI Con.
- P30 · 17/10 21:33 · nợ kỹ thuật: «Cái gì chưa làm được do công cụ thì ghi chú nợ kỹ thuật QTTH 007 (chúng ta không cố build hệ thống phức tạp như codex đã làm mà sẽ đưa lên collection sau khi hoàn thành QTTH 007. DOT trên collection sẽ rất nhanh, giờ chỉ cần ghi chú danh sách là được, có một ít thông tin không đáng ngại.» → N01–N08 ở view.html.
- P29 · 17/10 21:18 + 21:26 · rà tới 3.2: «đồng ý, bạn sửa tiếp đi, làm sao để chạy không vướng. AI biết phải làm gì? hiểu ngay và không hiểu sai» → MBM r5.22 · mục tiêu + hoàn thành có số · rà D1/D2 · CAT-249 chưa có đường nạp dòng nên bảng 8 MBM là dữ liệu đầu tạm thời.
- P28 · 17/10 19:43 · đánh mã xong: MBM r5.21 (mục 1–9 đánh mã; 6.0 luật chung, bước 6.1–6.8) → danh sách việc của task dùng mã 6.1–6.8.
- P27 · 17/10 18:45 + 19:43 · đánh mã nhất quán: «Bạn rà lại, nên đánh số nhất quán thống nhất tuyệt đối từ MBM công thức => hướng dẫn => QTTH 07 và các quy trình sau này. Ví dụ hướng dẫn không nên để chấm/gjach đầu dòng mà đển 1.1, 1.2... Nguyên tắc mỗi thứ có tên riêng, duy nhất để dễ gọi tên, dễ định nghĩa. 2.1 đến 2.4 là cùng bước. Nên có cách ghi THẬT NGHẮN GỌN để cả con người và AI cùng hiểu là cùng bước hoặc khác bước. Những thứ như thế này nên nhất quán tuyệt đối» — «Miễn là nhất quán, nhìn ngắn gọn và nguyên tắc đơn giản nhất có thể. Bạn đánh mã đi» → MBM r5.20 (mục 1–4) + QTTH 07 đổi theo; mục 5–9 làm tiếp.
- P26 · 17/10 17:14 · sửa format trước: «Ok. Những thứ thuộc về chính tả, format bạn sửa trước đi.» → MBM r5.19 (3A/3B, mã 3A.1, bỏ câu trái nhau); vướng 3, 5, 6, 7 (thiết kế) chưa đụng.
- P25 · 17/10 17:07 · sửa MBM + rà lại mục 3: «OK. bạn sửa, sau đó lại thử rà lại QTTH 007 đến hết mục 3 xem còn thấy vướng gì không? Như AI lần đầu làm? (bối cảnh sau việc này, chúng ta sẽ cố định các master list trên VPS làm 1 trang chủ để treeview và các thao tác thì giao DOT. Nhưng giờ cái đó chưa chạy => ko nên coi đó là mắc nhé» → MBM r5.18 + bản thử mục 3 (5 mốc, 26 bước), 7 chỗ vướng ở view.html.
- P24 · 17/10 14:29 · Mốc 2 cụ thể: «2 Rà soát chuẩn bị (Master list, DOT, Tool) Đủ Master list, DOT, Tool để làm chưa? mục con 2.1–2.4 xong; thiếu = 0. Mục này vẫn mơ hồ. Nên liệt kê cụ thể từng dòng, có thì là có, không ghi không cần. Như vậy mới không cần gỉai thích nhiều» → MBM r5.17.
- P23 · 17/10 14:17 · chốt 5 mốc + mục con: «Vẫn mơ hồ (ý tôi là chưa thật cụ thể) và mỗi Ai có thể làm 1 kiểu. … Mốc gồm: 1. Khai việc 2. Rà soát chuẩn bị (master list, DOT, tool) 3. Triển khai (nếu Dài AI tự chia bước) 4. Kiểm tra: 5. Báo cáo. Mục con: Trong mục 2 (rà soát), mục 3 triển khai có thể chia nhỏ hơn thành mục con) Tuỳ AI cân đối 1. Lập danh sách DOT đã có, DOT cần thêm và DOT sửa lại (nếu có) 2. Lập danh sách Master list đã có/cần user phê duyệt UI/ Cần làm mới (nếu cần) 3. Tạo mới/nâng cấp các danh sách DOT cần làm nếu có 4. Tạo mới/nâng cấp các danh sách master list cần làm nếu có 5. (Option) AI chia nhỏ triển khai thành nhiều phần nếu cần. => Viết 1 định nghĩa rất ngắn và chốt bảng mốc và mục con luôn. => Bước thực sự phải triển khai theo cả mốc và mục con + Nhóm con đấy (việc này phải nghĩ thêm chút). … Bạn sửa thêm rồi tôi nhìn vào đó bàn tiếp (Sửa MBM trước), chúng xem đưa thẳng vào MBM khoá cứng ổn không?»
- P22 · 17/10 13:54 · định nghĩa Mốc/Mục con: «… Tư duy đơn giản là: cứ có chỗ để điền, AI sẽ biết cách điền thông tin. => Vấn đề là quy định về form mẫu chuẩn. Đọc có thể hiểu. Giờ nhìn vào bạn làm thử: tôi thấy khái niệm: Mốc là gì chưa rõ (AI - Bạn) đang tự làm theo ý. Mục con cũng tương tự. Cái này phải định nghĩa rõ từ MBM. Mốc phải > mục con, mốc chứa nhiều mục con mới đúng (và mục con là nếu có) tức là quá dài thì mới cần mục con để chia nhỏ mốc => Bạn rà soát cái này.»
- P21 · 17/10 12:25 · nhật ký = CAT-227 + CAT-069: «Đây lại là vấn đề thiết kế chưa rõ rõ ràng. MBM có lẽ lần đầu phải mang trọng trách để hướng dẫn hệ thống. Thực sự thì chưa ai, kể cả bạn đang hình dung được Hệ thống gồm những master list nào. Đó là vấn đề cần giải quyết. Tôi thì hình dung ra 1 số nhưng không thể đủ? Phần nhật ký này thực ra về bản chất chúng ta có 2 bảng: 1. Thứ nhất là tiến trình (CAT-227). Chúng ta bắt đầu làm từ việc gì => điền vào đây. Từ việc bé đến việc to (từ sửa 1 cách đến thực hiện 1 quy trình tổng hợp rất lớn, tất cả đều được gọi chung bằng 1 "việc" => có 1 dòng => có 1 mã việc riêng 2. Bảng ghi chép lại công nợ (CAT-069) khi đang làm. Nhưng bảng này chưa điền của mã việc CAT-227. Tức là những khúc mắc của việc 227. Vấn đề là những việc này là hệ thống chung => nên viết từ MBM để các quy trình do MBM sinh ra nhứ QTTH 007 chép lại. Bạn điều chỉnh lại từ MBM và xem 2 việc này còn vướng nữa không? … AI phải tự đọc để xem có hiểu cách làm không? Chứ các bạn cứ góp Ý ào ào, đến lúc làm lại tắc => Vô nghĩa mất thời gian»
- P20 · 17/10 11:59 + 12:04 · tình trạng mục tiêu: «bạn có đang phức tạp hoá lên không. Mục tiêu user tam chốt rồi => đi quay lại 1 vấn đề đã chốt rồi làm gì? Cái chính là hiện nay AI không biết được là User chốt chưa? Thiếu tình trạng. … Cần phải làm kỹ lưỡng từng chút 1. Làm ào là gãy. … Bàn ít một đã» — «Đồng ý thêm tình trạng.»
- P19 · 17/10 11:52 · D1/D2 trỏ CAT-249: «Như vậy cần ghi rõ trên MBM => đọc từ MBM sang QTTH 007 để Ai hiểu là rà soát lại (không chặn) để cập nhật thêm các Tool/giải pháp mới, dùng lại nếu có..... ghi nhắn gọn nhưng mọi người hiểu là có vấn đề D1, D2 và dẫn chiếu đến Cat 249 là ok. Nhìn lại lần nữa xem QTTH 007 làm theo MBM từ 1-4 có còn mắc gì không? Nhìn như AI phải làm việc này lần đầu tiên, để đọc xem còn chỗ nào khó hiểu? Chỗ nào không hiểu?»
- P18 · 17/10 07:13 · Master công cụ giám sát: «Thay vì lý thuyết. Bạn tạo luôn giup tôi 1 master list về: Master công cụ giám sát. Đăt mã, đặt tên, vẽ Ui cho nó và đưa vào thành 48 list. Chỉ cần có list master có chỗ là AI biết điền, giải thích dài dòng làm gì?» → đã tạo CAT-249* · UI.MASTER.TQT.249 · `process-work-master-v1.html?master=CAT-249%2A` · danh sách Master = 48 (commit `65785b73`, `3bd15fae`).
- P17 · 17/10 05:46 · bản chất D1, D2: «D1. D2 bạn cho vào đó là sai => lòi ra. bản chất tôi đã giải thích. 1. Cơ chế này không thể giải quyết hiệu quả trong 1 việc/ trong 1 quy trình cụ thể. Mà phải giải quyết ở tầm MBM hoặc cao hơn. Các giải pháp đưa ra sẽ phức tạp và cần được tích luỹ theo thời gian. Ví dụ cơ chế chốgn lệch của PG giống như các dịch vụ của google về bất đối xứng... các công nghệ chung của Direcutus. Những việc này có thể là tổng hợp của nhiều công nghệ/DOT và giải pháp khác nhau. 2. Tôi muốn viết vào từng việc như QTTH 07 và xét vào từng việc là để 1 lần nhìn lại vấn đề này xem cí làm được gì không? Có cái gì đã bàn , đã làm mà chưa áp dụng không? Có áp dụng được cái mới gì không?.... 3. D1, D2 nó giống như câu hỏi mở, có quy trình để xem, có nơi (sổ /master list) để ghi các phương án đã áp dụng... để trả lời những câu hỏi ở mục 2. Cái này làm rõ và nên ghi chú ẩn được về D1, D2. Không làm thì kết quả tệ,. không ghi thì mai quên lãng không ai nhớ, chẳng ai bàn và viẹc này quên lãng + kết quả tệ. Nhưng ghi ra không được biến thành block»
- P16 · 17/10 05:36 · mục 2 MBM: «2.1 thì thống nhất các bạn viết số vào. Bám vào nội dung của tôi, còn số là phần trình bày, làm thế nào (viết ngắn để AI hiểu là có format chủ động theo chuẩn) 2.2 chuyển luôn thành 3-5 gjach đi 2.3. (User quyết hội đồng ký/bỏ qua bước này), tức là User duyệt vẫn là bắt buộc. 2.4 Tôi chưa hiểu bạn đang vướng gì? Chúng ta làm từng mục cho dễ.»
- P15 · 17/10 05:22 · tiêu đề 3.3 MBM: «3.3 Bước … => đổi thành: 3.3 Bước (nền tảng = nhóm con, có thể điều chỉnh cho sát thực tế). Không tự viết lung tung vào MBM khi tôi chưa yêu cầu!»
- P14 · 17/10 05:08 + 05:15 · bước theo công thức: «Bạn chưa hiểu sâu hết đâu. Mục: 3.3 Bước của QTTH 07 => bạn ghi chú ngay sau "3.3 Bước" là: (Bước tính theo nhóm con, mỗi quy trình có số UI tính theo công thức của UI con) Chúng ta đã có những công thức cho việc này rồi. => bạn thử rà soát lại xem số bước đúng chưa?» — «bạn đang nhầm lẫn: 1. công thức ngay trong này (trên phần MBM một tí ...) 2. Chúng ta đang chế tạo QTTH 07 từ MBM: MBM => QTTH 07 (và các quy trình khác sau này) => QT 01 của master mow. Đừng rà cái con khi cái mẹ còn chưa xong. Các bạn đang phức tạp lên. Nhóm con CT-004 Chuỗi+Bước con+Tầng⇒Nhóm con. UI Con CT-006 Chuỗi+Bước+Tầng+Nhóm+UI cha⇒UI Con. Công thức có vài chữ thôi, nhưng con người nhìn vào đây là hiểu hết. Các bạn chữ nhiều nhưng rối tinh lên»
- P13 · 22:57 · mục 3 thành 3 bảng: «Mục 3 triển khai tôi nhìn thấy phải sửa từ MBM. 1. Thêm mục 3.1. Mốc 3.2 Mục con 3.3 Bước (hiện tại chuyển thành bước) 3.1 Để các cột. STT; Tên Mốc; Câu hỏi cần trả lời; Thế nào là hoàn thành 2. Bảng 3.1 Để các cột. STT; Tên Mốc; Câu hỏi cần trả lời; Thế nào là hoàn thành 3.2 Cột: STT; Tên Mốc; Tên mục con; Câu hỏi cần trả lời; Thế nào là hoàn thành 3.3 Cần thêm 2 cột Câu hỏi cần trả lời; Thế nào là hoàn thành. Sau đó thử làm lại trên Repo xem? Cần hoàn thiện từng bước cho hợp lý.»
- P12 · 22:19 · lỗi hiển thị: «Bạn kiểm tra xem có lỗi gì không? tôi kiểm tra mbm-qtth-07-ve-ui-mow không thấy chuyển về?»
- P11 · 22:07 · làm ở workspace: «Không, bạn đưa lên repo chứ. Đó bạn thấy không? mỗi người vẫn hiểu 1 kiểu, mỗi AI vẫn hiểu 1 kiểu. Và cái đó rõ ràng chưa thể trở thành quy trình được. Ghi thêm vài chữ là làm ở workspace để không hiểu nhầm nữa»
- P10 · 21:57 · làm thử bước 3–4: «Giờ quay lại QTTH 007. bạn làm bước 3,4 trên repo để thử xem còn vấn đề gì nữa chúng ta bàn tiếp.»
- P09 · 21:12 · công thức + 2 vấn đề: «Yêu cầu User+Mục tiêu+Master list+Bước (Mốc · Mục con · Bước)+Bộ câu hỏi⇒MOW đổi thành => Yêu cầu User+ Mục tiêu + Mốc /Mục con/Bước+ Check Master list + Bộ câu hỏi⇒MOW. Tôi thấy bạn làm thực đang có 2 vấn đề: 1. Mục bước ví dụ QTTH 07 đã liệt kê ra, nhưng nhìn vào cột bước (chưa bàn thiếu đủ) thì chắc làm thế nào để hiểu cho nhất quán được. Bạn đang suy diễn theo cách hiểu của bạn để làm. Ai khác có thể sẽ làm theo cách không giống bạn. 2. Việc tiếp theo việc chốt được bước => như bạn vừa làm là kiểm kê lại các danh sách master list rõ ràng là việc cần, nhưng nên đưa vào đâu? Phải làm thực mới rút ra được kinh nghiệm => để ở vị trí đó có hợp lý không?»
- P08 · 20:41 · sửa MBM r5: «rõ ràng là làm thử thấy mắc ngày => cả MBM lẫn quy trình đều không khả thi. Giờ cần sửa lại cả. Chúng ta sẽ vừa sửa MBM vừa làm thử lại. Quy trình mà không thực hiện được hoặc thực hiện không nhất quán, hoặc không thể đạt mục tiêu => chả có nghĩa gì. 1. "② Chia mục và đặt mã" muc hướng dẫn này viết dài rồi cũng không làm được. Quy đinh là liệt kê đầy đủ theo mẫu: # Mốc Mục con Bước / 1 007-1 Khai việc — 1.1 Tra hoặc tạo việc duy nhất / 2 007-1 Khai việc — 1.2 Mở hồ sơ. Như bước bạn vừa làm 2. Trên công thức: Mốc, mục con, bước gồm thành 1 bước. 3. Bước tiếp theo nên là: Rà soát các master list. bạn sửa đi rồi tôi hướng dẫn tiếp. Sửa MBM trước đi»
- P07 · 18:01 · thử hiểu bước 1: «Vấn đề là các bước chúng ta đã bàn. AI bình thường có thực sự biết làm gì không> ví dụ bạn thử mô tả cho tôi mục 1 gồm: 1.1, 1.2 và 1.3 xem bản thân bạn hiểu là bạn cần phải làm gì nếu bạn được giao làm việc này?»
- P06 · 17:25 · dùng lại bản cũ: «Tôi chả hiểu bạn đang viết cái này là cái gì nữa? Bạn kiểm tra xem trước nếu chưa có MBM chúng ta đã bàn thế nào? mấy chục cái bước gồm những bước gì? Việc này mà chúng ta không MBM thì chúng ta cũng làm xong rồi đấy. Kiểm tra lại xem nào? Liệt kê cho tôi các cái bước chi tiết, theo tôi nhớ chúng ta còn làm cả hồ sơ rồi cơ mà? Các bạn cứ viết Tràng giang đại học xong lúc quay lại viết như là người không hiểu gì? Tôi cũng chả hiểu bạn đang viết gì luôn?»
- P05 · 17:05 · chốt ô 1–2: «1. Mục tiêu này 1. vẽ UI theo Master MOW 2. hoàn thiện Master list (đủ các master list có cần dùng và từn master phải được user duyệt lần đầu) 3. Điền đủ (SSOT) ( không có đối tượng liên quan đến quy trình này bị mồi côi (không có "sổ" để ghi, có sổ nhưng chưa được ghi, ghi ở 2 SSOT...) 4. Đủ trường để Config => list được hợp đồng thông tin liên quan 5. Dùng 100% DOT tạo collection, không làm hệ nặng. Bổ sung các DOT cần thiết, để dùng lại lâu dài. Ưu tiên chạy DOT nếu nếu có thể (tức là tự động 2. Thế nào là hoàn thành 1. Vẽ xong UI theo masterlist mow bao gồm hợp nhất các Mow hoặc tách cách mow 2. Xác đinh tin cậy số lượng đối tượng "mồ côi" (dùng dot) => đảm bảo không có đối tượng liên quan mô côi. 3. Các master list điền đầy đủ thông tin, đảm bảo SSOT 4. Xác đinh đủ hợp đồng thông tin để config không lỗi. Theo công thức: Yêu cầu User+Mục tiêu+Mốc+Mục con+Bước+Bộ câu hỏi⇒MOW chúng bạn đưa lên task và hoàn thành mục tiêu. Viết sao cho ngắn gọn nhưng làm được. Kinh nghiệm đau thương của tôi là các bạn viết dài nhưng cuối cùng vẫn sai, con người thì không nhìn được vì nó quá nhiều chữ»
- P04 · 16:50 · viết gọn: «Giờ bạn tạo task trước đi, viết ngắn thôi nhưng đủ. 2 tạo tên 3. chôt mục tiêu + thê nào là hoàn thành => Kiểm tra lại các thông tin tôi đã chỉ đạo trước đây để viết vào. 4. Liệt kê ngắn gọn các đầu việc task (cái này để xem làm thế nào cho gọn). Nhắc lại tổng thể là viết ngắn gọn. Đừng viết dài quá các bạn cũng không đọc được đâu lại làm sai hết.»
- P03 · 16:52 · tên task: «Bạn ghi luôn là tên task mà làm theo MBM thì chữ đầu tiên phải là mbm-.... sau này chúng ta có nhiều công thức, quy định luôn cách đặt tên để còn biết tìm. Nhìn cái là phải hiểu nguồn gốc nó từ đâu.»
- P02 · 16:39 · thứ tự ④ + danh sách việc: «Không tôi nghĩ là nên làm ngược lại: ④ Làm một MOW bằng MBM. Nhận yêu cầu => tạo task Tạo task trên workspace => Chốt mục tiêu (quy trình sẵn cũ). Đưa 1 danh sách list những viẹc cần làm lên Task, cái nào làm xong thì tích. Lý do là các bạn ít đọc công thức, chỉ đọc 1 lần thôi. Còn lại task là cái mà lần nào cũng phải đọc lại, xem lại. Dễ bàn hơn. Sửa lại và làm thử theo xem có hợp lý không. Chưa hợp lý lại tiếp tục sửa. Chỉ có phần quét chi tiết mà hội đồng đã góp Ý nhiều lần => chúng ta nên hạn chế sửa bừa bừa bãi. Bởi vì sửa lại phải kéo cả hội đồng và góp Ý. Còn lại thứ tự quy trình, tôi và bạn làm là đủ rồi. Cho nhanh. Cái gì đúng là nó chạy được thực tế. Còn vào thực tế mà mắc => phải sửa lại hết.»
- P01 · 16:29 · tạo việc: «Thấy bạn lúng túng lắm. Tức là các bạn viết ra đó nhưng các bạn chưa chắc đã làm được 1 quy trình từ MBM đâu. Đây sẽ là bài test thử. Đầu tiên bạn sửa lại việc này. Bổ sung phải taọ task trên workspace nữa. => bạn thấy đấy. Viết không đủ cụ thể, khôgn tính đến khi làm => vào làm là mắc. Chúng ta vừa làm vừa hiệu chỉnh toàn bộ MBM để làm sao các bước thật chi tiết. Lần 2 không có tôi AI thưc sự chạy được. Các bạn viết thì hay, nhưng khi các bạn làm là hỏng ngay. Giờ bổ sung phần đó và việc đầu tiên bạn tạo task trên WP đi. qtth.07-ve-UI-mow»
