# COLLAB — mbm-qtth-07-ve-ui-mow
Tên việc: MMOW 07 — vẽ UI cho các MOW trong Master MOW, làm bằng công thức MBM

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
Xác nhận User: ĐÃ XÁC NHẬN — Owner 19/10/2026 18:28: MMOW 07 chỉ Vẽ UI (thay bản 18/10 21:25 gồm 3 mục tiêu; Chốt Info contract → MMOW 08, Config → MMOW 09).
Host: Claude Chat · Owner giao trực tiếp 16/10 16:29–17:05.

### ⇢ HANDOFF CHO PHIÊN SAU · 21/10/2026 14:25 +07 · Claude · P67 · cập nhật 14:50 P68
> Phiên mới: đọc hết mục này → mở 3 trang ở H2 → làm việc đầu tiên chưa ✅ ở H4 (hiện: H4.4a). Không bàn lại những gì ở H3.

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
- ✅ **H4.3b** (P70) Sửa CT-000.1, CT-000.2, CT-000.4 theo phản biện vòng 3 GPT Pro (H5 · Vòng 3): 3 lưới khép kín, Bảng Trạng thái, 4 giới hạn, 8 kết quả. Commit `8d1479e2` + `a4648ef4`.
- ✅ **H4.3c** (P71) Đổi cách làm theo Owner 16:24 «cơ chế, không phải nguyên tắc»: logic chạy viết 1 chỗ = Bảng Chuyển trạng thái (92 dòng) + Bảng Trạng thái (32 trạng thái) + Bảng Giá trị; bỏ Bảng Kết quả lượt; bảng khác chỉ trỏ mã T. Máy kiểm 6 điều: 0 lỗi; 14 ca thử: 14/14. Commit `da9609f9` · `7cc4ecec` · `e14ad530`.
- ➡ **H4.4a** Gửi GPT Pro rà vòng 5 trên Bảng Chuyển trạng thái. Mỗi ca GPT Pro nêu thêm ⇒ thêm vào danh sách ca thử của máy (H7) rồi chạy, không tranh luận bằng lời. Sau đó gắn 1 việc sửa UI thật.
- **H4.4b** Thử thật trên PG + Flow (hàm X1, nhận việc, thu hồi, quét mồ côi): ghi bằng chứng riêng với H4.4a; chưa có H4.4b thì không ghi «đã chạy được».
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
> Không làm theo nguyên văn (P69, để GPT Pro rà): (a) 4 chỗ GPT Pro đưa 2 cách, Host chọn 1 — tái phát ⇒ mở lại cùng sự cố; từ chối ⇒ về G3, quá N ⇒ X9; đạt một phần ⇒ làm tiếp phần còn lại, bù chỉ khi huỷ; Owner chưa trả lời ⇒ chờ + nhắc, không có người thay Owner. (b) Chưa chỉ ra công cụ hiện có cho từng thao tác: theo H6.12 ghi yêu cầu + nợ 🔴 ở H8. (c) ĐÍNH CHÍNH P70: GPT Pro đúng — PG 18 §13.3.4 Deadlocks có câu «giữ giao dịch mở lâu, vd chờ người nhập, là cách làm không tốt»; Host đã tra sai trang. Nguồn đã gắn vào Yêu cầu PG 4. (d) Ánh xạ CAT-069 ↔ `feedbacks`: để VD-029.

#### H5 · Vòng 3 GPT Pro (21/10 15:35) — 15 điểm, P70 nhận cả 15
1. Cổng G2, G4, G5 phải khớp cột Đạt khi (G2 gồm G4.7; G4 gồm G4.4–G4.5; G5 là Đúng, không chỉ «có giá trị»).
2. G1: G1.9 Chưa biết chưa có đường; G1.9 Sai cùng câu khác Sai khớp 2 đường; thiếu hạn mặc định khi G1.7 chưa Đúng.
3. G2 phân tuyến theo lý do (chờ / lỗi), không theo trạng thái; X6 thiếu nhánh Chưa biết.
4. Thu hồi lượt hết hạn có thể chạy lại tác động đã làm ⇒ phải đối soát; ghi kết quả kiểm đúng việc + thế hệ + trạng thái.
5. M phải đếm lúc nhận, không chờ máy báo; kiểm trần và hạn trước khi nhận lại.
6. Quá hạn chặn tác động mới nhưng vẫn đối soát, bù; Huỷ ở X9 phải bù trước khi kết thúc.
7. Chưa biết: đối soát xong phải chấm theo điều kiện lượt; «không thấy» không đồng nghĩa «chưa làm».
8. 1 sự cố gắn nhiều việc gốc: X6 chấm riêng từng việc; bộ đếm, hạn theo từng việc.
9. X9: ngoại lệ phải ghi câu, phạm vi, hiệu lực, bước trở lại (cổng phải nhận «Được miễn»); làm tiếp sau khi hết trần phải ghi trần mới.
10. CAT-228*: mã việc ổn định qua các lần thử; lịch sử lần thử ghi ở đâu.
11. Từ chối ⇒ sửa là thao tác mới, không gửi lại mã cũ với nội dung khác.
12. «100% PG + Directus, không cài thêm» quá mạnh ⇒ «ưu tiên…; xác minh ở bước ghép công cụ».
13. «Tắt tầng trên chỉ chậm» ⇒ «có thể tạm dừng, không mất trạng thái»; PG gốc giữ gì phải nói rõ.
14. Nguồn: PG §13.3.4 (Host sai); DMN Unique chưa đủ để không sót; gRPC UNAVAILABLE, ABORTED cần điều kiện; RFC 2119 có cả SHOULD, MAY.
15. Phép thử PG 1, 6, 8 phải sửa; H4.4 tách thử giấy và thử thật.
> P70 thêm theo Owner 15:35 «không mồ côi»: luật 9 Không mồ côi + Flow quét (PG 14) + giới hạn D độ sâu chuỗi sự cố + ghi ý định trước khi làm (G3) + Bảng Trạng thái 10 trạng thái.

#### H5 · Vòng 4 GPT Pro (21/10 16:24) — 11 điểm, P71 nhận cả 11
Gốc rễ: logic viết bằng lời rải 6 bảng ⇒ hở chỗ nối; phép kiểm cũ chỉ xem tên đích có tồn tại. P71 đổi sang cơ chế: 1 bảng chuyển trạng thái + máy kiểm + ca thử.
1. G5 đủ ⇒ đóng hồ sơ (T41) · Config chung khi chưa có Loại việc · nguồn «một trong» còn nguồn khác ⇒ tiếp tục chờ · chờ nghiệm thu ⇒ Chờ người·G4 (T36) · G5 lỗi trước, chờ nhận sau · Chờ người ghi chờ ai, trả lời gì, bước trở lại.
2. M xét TRƯỚC khi tăng, lượt thứ M vẫn chạy (ca 2) · trần song song khoá phạm vi (PG 3) · gia hạn kiểm còn hạn, thu hồi cùng 1 lệnh (PG 5) · số lần nhận tách khỏi thế hệ (G3.4).
3. CAT-238*: 1 dòng = 1 biên nhận; nhiều biên nhận cùng trỏ 1 mã thao tác.
4. «Chưa thấy» không phải «chưa làm»; không chống trùng ⇒ người đối soát, không quay vòng (ca 7) · biên nhận muộn vẫn ghi (X5, PG 8).
5. Huỷ ⇒ Xét huỷ ⇒ đối soát ⇒ bù ⇒ đóng, không quay về G4 (ca 8) · huỷ sau hạn dùng hạn phục hồi (ca 9, 13) · Đạt muộn: G5 «dừng hạn» nếu còn tác động.
6. Đến giờ kiểm không phải mồ côi (PG 14; ca 10) · 3 loại hạn (Bảng Giá trị).
7. Tự chờ sự cố của chính mình ⇒ X7 (X1 ②); độ sâu theo đường xử lý.
8. Nhiều gốc khác hạn: lượt sửa dùng hạn muộn nhất còn hiệu lực; gỡ chặn ⇒ kiểm lại hạn, huỷ, Owner (T57).
9. Ngoại lệ chấm lại cả cổng (T87; ca 11); Làm tiếp về đúng bước trở lại (T85).
10. Tái phát sau kết thúc: không tự mở lại việc đã kết thúc; không còn gốc mở ⇒ X9 (X1 ⑥).
11. X1 tự lỗi: cờ «chưa chuyển sự cố» + Uptime Kuma kiểm lần quét hoàn tất (PG 12, 15).
> Tự phát hiện thêm khi rà P71: G4.6 còn ghi bộ kết quả cũ ⇒ đã sửa khớp từng chữ; máy kiểm có bước đối chiếu chéo.

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
13. PG là tầng gốc giữ sự thật, khai thác tối đa PG trước; dịch vụ như Kubernetes chỉ là lớp trên cho bài toán chuyên biệt (Owner 21/10 15:15 → CT-000.2 luật 7–8).
14. Khép kín mọi trường hợp, đi đến cùng mọi nhánh; tệ nhất là vào hàng đợi; không để tình trạng mồ côi (Owner 21/10 15:35 → CT-000.2 luật 9–10, CT-000.4 3 lưới).
15. Viết nguyên tắc không có nghĩa gì; quan trọng là hành động, cơ chế để không hiểu sai, không thể làm sai (Owner 21/10 16:24 → Bảng Chuyển trạng thái + máy kiểm H7 + PG 16: hàm chỉ chuyển theo dòng có trong bảng).

#### H7. Mẹo kỹ thuật
- Sửa trang: `fs_edit` root gh; tệp ~760KB, luôn dùng old_str nguyên văn; báo «không khớp» thì `fs_search` lấy nguyên văn; push bị từ chối (phiên khác vừa đẩy) thì gửi lại cùng expected_version.
- Trang xem giữ bản cũ: mở `ui-preview/hpml-view-for-user/view.html?task=mow-mot-moit-mout`, bấm `header button`, đợi ~18 giây, rồi chụp `knowledge/modules?…&section=<id>`.
- Công cụ chụp không mở được «Chi tiết» trong khung trang → kiểm bằng đếm mã (`fs_search` count) và nói rõ giới hạn.
- Đọc PG: `query_pg` database `directus` (chỉ đọc). `directus_read` đang lỗi phân giải tên miền.
- Neo trang: `formula-ct-000-1` … `formula-ct-000-4` · `formula-ct-001` … · `kn-cat-000-5`.
- Mỗi lượt sửa: cập nhật Bảng điều khiển + Nhật ký (P tăng dần) trong COLLAB này.
- Mọi mục chèn vào §0 dùng cấp `###` trở xuống. Cấp `##` cắt §0 ⇒ trang Task mất Bảng điều khiển (bộ đọc `hvu-b2/sync.py` lấy §0 tới dòng `##` kế). Lỗi P67, sửa P68.

- **Máy kiểm Bảng Chuyển trạng thái (P71).** Mỗi lần sửa Bảng Trạng thái, Bảng Chuyển trạng thái hoặc câu G4.6 PHẢI chạy khối dưới (workspace_exec, root workspace, `python3 -c`). Đạt = «LỖI 0» và «CA THỬ ĐẠT n / n». Ca mới: thêm 1 dòng vào `TR` (tên, trạng thái đầu, các bước sự kiện–giá trị, trạng thái cuối mong đợi, biến, trạng thái phải qua / `!` không được qua).
<details><summary>Lệnh máy kiểm (6 điều + 14 ca)</summary>

```python
import re,html,collections,sys
sys.setrecursionlimit(10000)
h=open('work/mow-mot-moit-mout/ban-duyet.html',encoding='utf-8').read()
a=h.index('id="formula-ct-000-4"'); s=h[a:h.index('</section>',a)]
def table(name):
  i=s.index('head-label">'+name+'<'); t=s[i:s.index('</table>',i)]
  body=re.search(r'<tbody>(.*?)</tbody>',t,re.S).group(1)
  return [[html.unescape(re.sub('<[^>]+>','',c)).strip() for c in re.findall(r'<td[^>]*>(.*?)</td>',r,re.S)] for r in re.findall(r'<tr>(.*?)</tr>',body,re.S)]
def expand(cell):
  out=[]
  for part in cell.split(' + '):
    m=re.match(r'(.*?)\s*\[(\w): ([^\]]+)\]$',part.strip())
    if m:
      base,var,vals=m.groups()
      for v in [x.strip() for x in vals.split(',')]: out.append((base.replace('{'+var+'}',v),{var:v}))
    else: out.append((part.strip(),{}))
  return out
ST={}
for c in table('Bảng Trạng thái'):
  dom={}
  if c[4] not in ('—',''):
    for seg in c[4].split(' ; '):
      ev,vals=seg.split(': ',1); dom[ev.strip()]=[v.strip() for v in vals.split(' / ')]
  for name,b in expand(c[0]): ST[name]=dict(kind=c[1],holder=c[2],check=c[3],dom=dom)
term={n for n,v in ST.items() if v['kind']=='kết thúc'}; nonterm=[n for n in ST if n not in term]
TT=table('Bảng Chuyển trạng thái'); ROWS=[]
for tid,frm,ev,vals,act,to in TT:
  if frm.startswith('*'):
    exc=[x.strip() for x in frm.split('trừ',1)[1].split(',')] if 'trừ' in frm else []
    froms=[(n,{}) for n in nonterm if n not in exc]
  else: froms=expand(frm)
  for f,b in froms:
    for v in [x.strip() for x in vals.split(' / ')]:
      t=to
      for k,val in b.items(): t=t.replace('{'+k+'}',val)
      tg=[f] if t=='(giữ nguyên)' else (['Chấm G1','Chấm G2','Chấm G4','Chấm G5'] if '[bước trở lại]' in t else [t])
      ROWS.append(dict(id=tid,frm=f,ev=ev,val=v,act=act,to=tg,bound=bool(re.search(r'(lần nhận|vòng) \+1|trần',act))))
glob=set(c[2] for c in TT if c[1].startswith('*')); HUMAN={'yêu cầu huỷ','trả lời','quyết định'}
err=[]; idx=collections.defaultdict(list)
for r in ROWS: idx[(r['frm'],r['ev'],r['val'])].append(r['id'])
def evs(n):
  e=dict(ST[n]['dom'])
  for g in glob: e.setdefault(g,['ok'])
  return e
for n in nonterm:
  for ev,vals in evs(n).items():
    for v in vals:
      if len(idx[(n,ev,v)])!=1: err.append(('1',n,ev,v,idx[(n,ev,v)]))
for (n,ev,v),ids in list(idx.items()):
  if ids and (n not in ST or n in term or ev not in evs(n) or v not in evs(n)[ev]): err.append(('1b',n,ev,v,ids))
E=[]
for r in ROWS:
  for t in r['to']:
    if t not in ST: err.append(('2',r['id'],t))
    else: E.append((r['frm'],t,r['bound'],r['id'],r['ev']))
G=collections.defaultdict(set); R=collections.defaultdict(set)
for e in E: G[e[0]].add(e[1]); R[e[1]].add(e[0])
seen={'Mới'}; st=['Mới']
while st:
  x=st.pop()
  for y in G[x]:
    if y not in seen: seen.add(y); st.append(y)
err+=[('3',n) for n in ST if n not in seen]
ok=set(term); st=list(term)
while st:
  x=st.pop()
  for y in R[x]:
    if y not in ok: ok.add(y); st.append(y)
err+=[('4',n) for n in nonterm if n not in ok]
def sccs(nodes,edges):
  adj=collections.defaultdict(list)
  for e in edges: adj[e[0]].append(e[1])
  index={};low={};stack=[];on=set();res=[];i=[0]
  def sc(v):
    index[v]=low[v]=i[0]; i[0]+=1; stack.append(v); on.add(v)
    for w in adj[v]:
      if w not in index: sc(w); low[v]=min(low[v],low[w])
      elif w in on: low[v]=min(low[v],index[w])
    if low[v]==index[v]:
      comp=set()
      while True:
        w=stack.pop(); on.discard(w); comp.add(w)
        if w==v: break
      res.append(comp)
  for v in nodes:
    if v not in index: sc(v)
  return res
mach={n for n in ST if ST[n]['kind'] in ('tạm','máy')}
unb=[e for e in E if e[0] in mach and e[1] in mach and not e[2] and e[4] not in HUMAN]
for comp in sccs(mach,unb):
  inner=[e[3] for e in unb if e[0] in comp and e[1] in comp]
  if inner: err.append(('5',sorted(comp),sorted(set(inner))))
for n in nonterm:
  if ST[n]['holder'] in ('','—') or ST[n]['check'] in ('','—'): err.append(('6',n))
  if ST[n]['kind']=='chờ' and not any(e in ST[n]['dom'] for e in ('đến lúc kiểm','kiểm lại','quyết định')): err.append(('6b',n))
print('TRẠNG THÁI',len(ST),'· DÒNG',len(TT),'· LỖI',len(err))
for e in err: print('  ',e)
def run(stt,steps,ctx):
  path=[stt]
  for ev,val in steps:
    if ev=='xin nhận' and val is None: val='hết M' if ctx['lan']>=ctx['M'] else 'được'
    ids=idx.get((stt,ev,val),[])
    if len(ids)!=1: return None,path+['KẸT %s|%s=%s'%(stt,ev,val)]
    r=[x for x in ROWS if x['id']==ids[0] and x['frm']==stt and x['ev']==ev and x['val']==val][0]
    if 'lần nhận +1' in r['act']: ctx['lan']+=1
    stt=r['to'][0] if len(r['to'])==1 else ctx['trolai']; path.append(r['id']+'→'+stt)
  return stt,path
TR=[
('1 bình thường','Mới',[('khai xong','ok'),('chấm','đủ'),('chấm','đủ'),('xin nhận',None),('kết quả','Đạt'),('chấm','đủ'),('chấm','đủ')],'Kết thúc·Đạt',{},None),
('2 M=1','Chờ',[('xin nhận',None),('kết quả','Lỗi tạm an toàn'),('xin nhận',None)],'Chờ ĐK·G2',{'M':1},'Đang chạy'),
('3 B hoặc C','Chờ ĐK·G2',[('kiểm lại','còn chờ'),('kiểm lại','thoả'),('chấm','đủ')],'Chờ',{},None),
('4 chờ nghiệm thu','Chấm G4',[('chấm','chờ người'),('đến lúc kiểm','chưa quá'),('trả lời','có'),('chấm','đủ')],'Chấm G5',{},None),
('5 G5 lỗi trước','Chấm G5',[('chấm','lỗi')],'Chờ ĐK·G5',{},None),
('6 gửi rồi chết','Đang chạy',[('hết hạn giữ','có dở'),('đối soát','không kết luận'),('trả lời','có'),('đối soát','đủ')],'Chấm G4',{},None),
('7 chưa thấy','Đang chạy',[('kết quả','Lỗi tạm không an toàn'),('đối soát','không kết luận'),('đến lúc kiểm','quá hạn PH')],'Chờ ĐK·ĐS·TT',{},None),
('8 huỷ khi lệnh chưa rõ','Đang chạy',[('yêu cầu huỷ','ok'),('xét','có dở'),('đối soát','đủ'),('bù','xong')],'Kết thúc·Huỷ',{},'!Chấm G4'),
('9 huỷ sau hạn','Chờ',[('đến lúc kiểm','quá hạn gốc'),('quá hạn','không dở'),('quyết định','huỷ'),('xét','có tác động'),('bù','xong')],'Kết thúc·Huỷ',{},None),
('10 đến giờ không mồ côi','Chờ ĐK·G2',[('kiểm lại','còn chờ'),('kiểm lại','còn chờ')],'Chờ ĐK·G2',{},None),
('11 miễn 1 câu','Chấm G4',[('chấm','sai, hết vòng'),('quyết định','ngoại lệ'),('chấm','sai, hết vòng')],'Chờ Owner',{'trolai':'Chấm G4'},'!Chấm G5'),
('12 lỗi điều kiện','Đang chạy',[('kết quả','Lỗi điều kiện'),('kiểm lại','thoả'),('chấm','đủ')],'Chờ',{},None),
('13 quá hạn rồi huỷ','Quá hạn',[('quá hạn','có dở'),('đối soát','không kết luận'),('yêu cầu huỷ','ok'),('xét','có dở'),('đối soát','đủ'),('bù','xong')],'Kết thúc·Huỷ',{},None),
('14 chết 2 lần, M=2','Chờ',[('xin nhận',None),('hết hạn giữ','không dở'),('xin nhận',None),('hết hạn giữ','không dở'),('xin nhận',None)],'Chờ ĐK·G2',{'M':2},None),
]
np=0
for name,start,steps,exp,ctx,need in TR:
  c=dict(lan=0,M=99); c.update(ctx); end,path=run(start,steps,c); okk=(end==exp)
  if need and need.startswith('!'): okk=okk and not any(p.endswith('→'+need[1:]) for p in path)
  elif need: okk=okk and any(p.endswith('→'+need) for p in path)
  np+=okk; print(('ĐẠT ' if okk else 'TRƯỢT ')+name+' :: '+' · '.join(path))
print('CA THỬ ĐẠT',np,'/',len(TR))
```

</details>

#### H8. Nợ đang treo — không làm xen
- VD-029 ghi CAT-000.5 vào PG (2 cột Quản lý tại · Lớp; ~65 loài mới; 4 bảng vô chủ; mã mồ côi audit_log; 6 loài lệch tiền tố).
- L0–L6 → đề xuất thay bằng FAC-02 «Vai trò hệ thống» (5 giá trị có sẵn). **Chưa áp lên trang, chờ Owner.**
- ĐL1–ĐL6 → đề xuất chuyển thành dòng Điều luật (CAT-140). Chờ Owner.
- CAT-201* giá trị cố định (Cấp ghép, Lớp, Bước, Tầng, Mốc, Câu hỏi) chưa lập · CAT-250* Miền CV chưa lập.
- MBM M2–M6 · VD-028 · lỗi DNS Directus.
- (P68) CAT-000.5 dòng SPE-QUE* «⚠ thiết kế lệch (CAT-228*)» đã giải ở Bảng Sổ CT-000.4: dòng chờ = CAT-228*, CAT-230* = danh mục hàng đợi (định nghĩa). Sửa dòng loài khi làm VD-029.
- (P68) 🔴 Bảng nối Sự cố ↔ Việc gốc (1 dòng = 1 lần phát sinh, khoá = mã sự kiện) chưa có sổ, chưa có mã CAT — lập khi lên collection.
- (P68) Các «1 hàm PG», «Directus Flow lịch» trong 13 yêu cầu PG là yêu cầu thiết kế, chưa có công cụ thật — dựng khi lên PG (thiết kế từ yêu cầu, H6.12).

### BẢNG ĐIỀU KHIỂN · cập nhật 2026-10-21 16:25 +07 · Claude · P71

> **⏳ Chờ hội đồng rà rồi Owner duyệt từng dòng:** CT-000.1 + CT-000.4 bản luật yes/no (P68, trang Công thức, Chi tiết của 2 thẻ), đã sửa theo vòng 3 GPT Pro (P70), rồi đổi sang cơ chế theo vòng 4 (P71): Bảng Chuyển trạng thái 92 dòng là nơi duy nhất giữ đường đi; máy kiểm 6 điều 0 lỗi; 14/14 ca thử đạt. Phản biện vòng 2 GPT Pro (21/10 14:19) = 29 điểm ở H5 + 3 ý thêm (30–32); P68 giải 1–31: **Luật cổng** Đúng · Sai · Chưa biết (chỉ Đúng qua; Không áp dụng chỉ theo Loại việc + lý do) · **cột Đạt khi** cho 43 câu · cổng 1 đường (bảng quyết định DMN Unique) · **X1–X9** thành hàng thao tác Đọc · Làm · Ghi · Kết quả · **Bảng Kết quả lượt** 7 kết quả, mỗi kết quả 1 đường (chia lỗi theo gRPC) · **Bảng Sổ** (hàng đợi = dòng chờ CAT-228*, khớp CT-007; CAT-206* = khuôn) · **13 yêu cầu PG** có phép thử yes/no · **2 Bảng Chuẩn ngành** (32 chuẩn có nguồn) · khuôn viết luật EARS + RFC 2119 ở CT-000.2. Kế tiếp H4.4a: GPT Pro rà vòng 5 trên Bảng Chuyển trạng thái, ca mới thêm vào máy kiểm → H4.4b thử thật.
- ⚠ Mỗi lượt sửa task: sửa luôn các dòng tổng — giờ cập nhật · ✅ · ⬜ · ➡ · tên việc (nếu mục tiêu đổi).
- 🎯 Mục tiêu: ô 1. Vì sao: bài thử MBM — lần 2 không có Owner, AI vẫn tự chạy.
- 🏁 Xong khi: ô 2.
- 📍 Tiến độ (MBM 6.x): [✓ 6.1 Nhận yêu cầu] → [✓ 6.2 Tạo task] → [✓ 6.3 Chốt mục tiêu] → [◐ 6.4 Liệt kê bước — bản thử] → [◐ 6.5 Bộ câu hỏi] → [■ 6.6 Check Master list] → [□ 6.7 Ký] → [□ 6.8 Chạy]
- ✅ Đã xong: ô 1–2 (18/10 21:25) · rà tới hết mục 4 theo MBM r5.34: 8 bước (5 cố định + 3 chuyên môn) · bảng câu hỏi H1–H7 + Đ1, Đ2 · K1, K2 đã gỡ — xem tab «Nội dung công việc» (`view.html`) · 19/10: Info contract chuẩn ngành, Config + Saga, ý kiến Astra ngoài MBM · M1: QTTH đổi tên MMOW, 4 tầng MBM → MMOW → MOW → Hồ sơ (MBM r5.35) · tên hiển thị «Master MMOW», «MMOW 05/06» trên các trang (mã khoá ML-MOW-TH-001 / MOW-TH-xxx giữ tới khi lên collection — nợ 🔴 VD-027) · Master MMOW có dòng MMOW-007 (việc này), trang hiện mã MMOW-xxx · 18:28: MMOW 07 chỉ Vẽ UI; Master MMOW thêm MMOW-008 (Info contract), MMOW-009 (Config) · 22:26: Master MOW có 3 cột tích Vẽ UI · Info contract · Config (35/35 ☐; tích trên giao diện = nợ VD-028) · 20/10: trang Công thức có khối KHÁI NIỆM · CAT-000.5 (54 loài, 5 định luật ĐL1–ĐL5, ký hiệu tạm chờ vector); MMOW mã OBJ-MMOW · 14:18: CAT-000.5 hợp nhất 107 loài mã SPE (gộp entity_species + khái niệm nháp + CAT-237*; quét máy Q1–Q6: 4 bảng vô chủ, mã mồ côi audit_log, 6 loài lệch tiền tố, 10 sổ 2 mã) · Master Duyệt thiết kế có CAT-000.5 + cột Duyệt TK (xanh = User đã duyệt; CAT-000.5 tạm duyệt 20/10) · nợ VD-029 (ghi PG) · 15:08: chuẩn «?» cho mọi bảng mới (ĐL6), CAT-000.5 đã có «?» ở tiêu đề, ma trận, 8 cột · 17:32: trang Công thức có 2 thanh thu/mở «Công thức gốc» (CT-000.2 Cấp ghép 1–4) + «Công thức chuyên môn» (CT-001→008); 14 thẻ có dòng mờ loài + sổ · 20–21/10: Công thức gốc (21/10 09:51): CT-000.1 Bộ câu hỏi chuẩn (43 câu Trư