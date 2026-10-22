# COLLAB — mbm-qtth-07-ve-ui-mow
Tên việc: MMOW 07 — vẽ UI cho các MOW trong Master MOW, làm bằng công thức MBM

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
Xác nhận User: ĐÃ XÁC NHẬN — Owner 19/10/2026 18:28: MMOW 07 chỉ Vẽ UI (thay bản 18/10 21:25 gồm 3 mục tiêu; Chốt Info contract → MMOW 08, Config → MMOW 09).
Host: Claude Chat · Owner giao trực tiếp 16/10 16:29–17:05.

### ⇢ HANDOFF CHO PHIÊN SAU · 21/10/2026 14:25 +07 · Claude · P67 · cập nhật 22/10 15:30 P82
> Phiên mới: đọc hết mục này → mở 3 trang ở H2 → làm việc đầu tiên chưa ✅ ở H4 (hiện: H4.4c1 — MBM r6.0 + bộ câu cố định MMOW 07, mục 3.1). Không bàn lại những gì ở H3. **Mỗi lượt trả lời ≤ 15 phút; quá thì dừng, báo, chia nhỏ.**

#### H1. Đang ở đâu
**P78 · Claude Host · 22/10 11:10 — ĐỔI CÁCH LÀM (Owner 11:00 + GPT đồng thuận).** Owner: kiểm mãi máy kiểm, mỗi lượt hàng giờ ⇒ «chỉ dẫn ra nghĩa trang»; phức tạp lên là ngớ ngẩn. GPT đề nghị, Claude đồng ý: **DỪNG kiểm vét cạn H4.4a**, giữ nguyên thành quả. Cách làm mới 3 lớp: (1) 43 câu = hợp đồng thông tin dùng chung, không biến thành bước thực thi · (2) quy trình ngắn theo việc thật, mỗi bước: đọc gì → làm bằng gì → ghi ở đâu → đạt đi đâu → sai xử lý thế nào · (3) CT-000.4 chỉ gọi khi có lỗi. Tiêu chí xong đổi từ «duyệt hết + bắt mọi đột biến» sang **1 MOW thật chạy từ khai báo tới nghiệm thu** (H4.4c). Thành quả giữ: máy kiểm `b567b8b1` (P78: `--kb` nhận tên có dấu phẩy; tiết kiệm bộ nhớ 1,7 → 0,8 GB, mỗi kịch bản 1 tiến trình con) · VPS job `cb4a7759`: **21/21 kịch bản 0 lỗi, mã 0** (chưa gồm đột biến; job đột biến `105df51c` đã huỷ).

**P76 · GPT Reviewer · 22/10/2026: đồng thuận hướng kiến trúc, CHƯA THÔNG QUA H4.4a.** Chạy lại 29/29 ca cũ đạt nhưng 9 phép phản biện tái hiện 6 nhóm cần đóng; báo cáo `work/mow-mot-moit-mout/audit-ct000/REPORT-V7.md`, vết `evidence/v7-results.json`. Đã cập nhật cùng mã `python:ct000-audit` qua `run.py --v7`, giữ v5/v6; đã ghi danh thêm 6 script hiện hữu vào Master Tool, chưa nghiệm thu chức năng và không thêm vào runner DOT. Kiểm lại JSON thật: 34 provider, ID trùng = 0, manifest GPT 23/23 khớp, script còn ngoài Master trong danh sách 6 = 0. Chưa chạy duyệt lớn hoặc PG/Flow; Claude vẫn Host.

**P77 · Claude Host · 22/10 09:50: đã sửa đủ 6 nhóm P76 bằng cơ chế** (trang `d9ef7e5e`, máy kiểm `55c68218`, Master `d6b7b1d1`): (1) T20b «lượt cũ» chỉ ghi biên nhận, gia hạn phải đúng thế hệ, B14 máy ghi ở mọi bước chuyển · (2) trả lời mang ý/đúng người/đúng phiên ⇒ không hợp lệ (giữ chờ, nhắc) · từ chối (X9 → Owner) · hợp lệ; G1 tính lại từ `g1_mới` · (3) 17 mã gRPC; mã lạ/thiếu ⇒ Chưa biết → đối soát, không thử lại · (4) lỗi máy kiểm ⇒ CHECKER_ERROR, `--tu-kiem` tự chứng minh 3 điều · (5) L2 cấm tự lặp ở trạng thái tạm + giả định công bằng ghi trên trang (L2, L3) · (6) `--kiem-ke` đọc JSON `catalog.tool_registry`, ID duy nhất, đường dẫn đầy đủ, script chưa đăng ký = lỗi. Kết quả: ca 30–46 mới (cấm + được phép) → **46/46 ca đạt** · `--tu-kiem` đạt · `--kiem-ke`: GPT 23/23 tệp, 6 script đã đăng ký nhận đúng · bảng mới duyệt **3/21** kịch bản 0 lỗi (hết chỗ · M=1 · không có cách bù 129.008 trạng thái); số 13/21 cũ hết hiệu lực vì bảng đổi. **Kế tiếp:** duyệt 18/21 còn lại từng 1–3 cái → `--dot-bien` → GPT cập nhật probe v7 theo nghĩa bảng mới.

Báo cáo Host trước P76 — đang ở **H4.4a**: chạy máy kiểm `kiem-ct000-4.py` cho 6 bảng CT-000.4 tới thoát 0. P74 đã sửa đủ 6 điểm GPT Pro v6; 29/29 ca đạt; **13/21 kịch bản duyệt hết 0 lỗi**; còn 8 kịch bản + đột biến. P75 kiểm kê công cụ: 2 công cụ CT-000 đúng trong Master Tool ML-DEF-023 (giao diện stt 23, dòng 10–11), bộ tệp GPT Pro 20/20 khớp manifest, `--kiem-ke` thoát 0. Việc kế tiếp theo P76: đóng 6 nhóm phản biện và chốt phạm vi/giả định trước, rồi mới hoàn tất duyệt kịch bản và đột biến có giới hạn tài nguyên.

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
- ✅ **H4.3d** (P72) Vòng 5 GPT Pro chứng minh máy kiểm P71 bỏ lọt 11/11 bản làm hỏng. Đã bỏ kiểm bằng tên: CT-000.4 thành 6 bảng máy chạy được (Trạng thái · Biến · Giá trị = công thức · Thao tác = phép gán · Bất biến B1–B11, L1–L4 · Chuyển trạng thái 107 dòng) + máy kiểm dùng chung `work/mow-mot-moit-mout/kiem-ct000-4.py` (duyệt hết trạng thái, in vết chạy, đột biến, mã thoát 0/1/2). Máy bắt và đã sửa 8 lỗi thật (H5 · Vòng 5). Commit trang `32f1c61f` … `8bac5f76`; máy kiểm `a5a95af9` … `f8a7f8f5`.
- ⏸ **H4.4a** (DỪNG P78 theo Owner + GPT; giữ công cụ, ca, bằng chứng; kết quả cuối: VPS 21/21 kịch bản 0 lỗi, đột biến không chạy tiếp) Chạy đủ `python3 work/mow-mot-moit-mout/kiem-ct000-4.py --dot-bien` tới khi thoát 0: mọi kịch bản duyệt hết không vượt trần, 0 lỗi, mọi đột biến KILLED. **P73:** GPT Pro v6 tái hiện 3 đường sai (gửi sau hạn gốc · bù vượt MB lệch 1 · bù sau hạn PH) + 3 lỗ máy kiểm (dữ liệu thiếu/sai vẫn Đạt · tranh chỗ không chạy công thức thật · quá trần/máy lỗi bị tính là bắt đột biến); đăng ký 2 công cụ vào Master (`edcb28fa`). **P74 đã sửa cả 6** (trang `2cfb9eb6` `4db2b485`; máy kiểm `48be67a3` `b765e41b` `3508f42f`): 1 cửa «Bắt đầu bù» (kiểm PH + trần MB trước khi tăng; bỏ T88b/T90b, thêm T95b/T95c), chặn gửi mới sau hạn gốc, chấm G1/G2/G4/G5 bỏ «đủ ← True» + nhánh «dữ liệu sai» → X1, G5 «chưa biết», B12–B13; máy bắt thêm lỗi 9 (thiếu G4 bị coi là «sai» → làm lại) đã sửa. 29/29 ca đạt. **P75: 13/21 kịch bản duyệt hết 0 lỗi** (thường · chống trùng · M=1 · không tra được · xác nhận vắng · G1 thiếu 533.039 trạng thái · G1 chưa có Loại việc · G2 chờ · G2 lỗi · không có cách bù · hết chỗ · G2 thiếu dữ liệu · MB=1); lượt chạy chung hết bộ nhớ (mã 137) ở kịch bản 14 ⇒ chạy từng kịch bản `--kb TÊN`. **P77:** bảng đổi theo GPT v7 ⇒ duyệt lại từ đầu; đã xong 3/21 (0 lỗi), 46/46 ca, `--tu-kiem` đạt. Còn: 18/21 kịch bản → `--dot-bien` thoát 0. **Phạm vi mô hình phải ghi rõ khi xin ký (GPT v7):** g1/g2/g5 là giá trị gộp — 43 câu chưa tính từ dữ kiện thật; 21 cấu hình ≠ mọi tổ hợp biến; D / nhiều gốc chung một sự cố / nhiều thao tác ngoài chưa được chứng minh; GPT Pro rà nghĩa và cập nhật ca `python:ct000-audit` cho bản mới (bản ghim trả exit 2 đúng thiết kế). Sau đó gắn 1 việc sửa UI thật.
- ✅ **H4.4c0** (P79–P81) «Cách dùng 43 câu»: GPT đồng ý P80, Host sửa 3 điểm P81.
- ➡ **H4.4c1** (P82) MBM r6.0 (Bước = Việc + Miền CV + Công thức; MMOW chốt bộ câu cố định + hướng dẫn bổ sung) + bộ câu cố định MMOW 07 (mục 3.1) → GPT rà P83, 1 vòng → trả lời 22 câu 📋 một lần → H4.4c.
- **H4.4c** (P78) **1 MOW thật: MOW 001 vẽ UI**, dùng công cụ đã có, chạy từ khai báo tới nghiệm thu. Nhánh thử (chỉ cái thực sự gặp): đủ thông tin → vẽ · thiếu → hỏi bổ sung · người duyệt từ chối → sửa. Kiểm an toàn bắt buộc: đúng quyền, không chạy trùng, không tự cho qua khi thiếu kết quả, việc dở có người nhận. **Xong khi:** UI hiện đúng trên VPS + ảnh chụp + người duyệt xác nhận + việc đóng đúng trạng thái; phần chưa kiểm ghi rõ. Không dựng máy/bảng mới.
- **H4.4b** (sau H4.4c, chỉ khi cần) Thử thật trên PG + Flow (hàm X1, nhận việc, thu hồi, quét mồ côi): ghi bằng chứng riêng với H4.4a; chưa có H4.4b thì không ghi «đã chạy được». **Điều kiện thêm từ GPT v7 (khoảng trống, chưa phải lỗi đã tái hiện):** (a) X1 rollback rồi chết trước khi ghi cờ (PG 15) ⇒ cần dấu tiếp nhận bền trước bước có thể mất hoặc bộ quét tái dựng được, thử crash đúng ranh giới; (b) ghi ý định và gửi mạng không cùng giao dịch: thử chết sau commit/trước gửi, sau gửi/trước ghi kết quả, outbox phát lại (không đảm bảo đúng 1 lần), phiên cũ tỉnh lại sau kiểm quyền; (c) khoá phạm vi = khoá PG thật; nhận việc đồng thời, thu hồi/gia hạn đua nhau, biên nhận muộn, khởi động lại bộ quét.
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

#### H5 · Vòng 5 GPT Pro (21/10 17:47) — máy kiểm P71 bỏ lọt 11/11 đột biến + 8 điểm
Gốc: máy kiểm P71 đọc tên, không chạy thao tác; ca thử nhận sẵn nhãn. P72 đổi cách: bảng chạy được + duyệt hết trạng thái + đột biến.
8 điểm GPT Pro, đã sửa trong bảng: mã «chưa quá» thống nhất · kết quả phủ mọi mã, bỏ «còn lại» · đặt hạn PH khi vào đối soát thường · chờ phục hồi có lối quá hạn PH · bù có đối soát lần bù · giao lại lúc bù về bước bù, rút huỷ là quyết định riêng · miễn G1 tính đúng · dùng lại ý định khi thử cùng mã.
Máy kiểm P72 bắt thêm 8 lỗi thật (có vết chạy), đã sửa: ① gửi lại khi lệnh cũ còn bay (rút huỷ rồi chạy lại) ② Owner huỷ lại khi đang huỷ ⇒ bù 2 lần ③ Xét huỷ bỏ qua lệnh bù đang bay ④ rút huỷ khi lệnh bù đang bay ⑤ vòng gửi bù lại không trần (thứ tự công thức) ⑥ máy bù chết lặp không trần ⑦ đối soát bù «chưa thấy» gửi lại ngay ⑧ đóng Đạt sau vòng sửa chưa chạy (biến bước).

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
16. Đừng viết văn, phải học toán: rà soát bằng công cụ; các AI dùng chung công cụ để kiểm tra chéo nhau (Owner 21/10 17:47 → kiem-ct000-4.py trong kho, GPT Pro chạy cùng tệp).
17. Lưu lại mọi công cụ/script đã dùng vào kho + đăng ký Master Tool/DOT để lần sau chỉ dùng lại hoặc điều chỉnh; kiểm tra đăng ký đúng và kiểm kê lại (Owner 21/10 20:37 + 21:33 → H7 «Luật lưu công cụ» + `kiem-ct000-4.py --kiem-ke`).
15. Viết nguyên tắc không có nghĩa gì; quan trọng là hành động, cơ chế để không hiểu sai, không thể làm sai (Owner 21/10 16:24 → Bảng Chuyển trạng thái + máy kiểm H7 + PG 16: hàm chỉ chuyển theo dòng có trong bảng).

#### H7. Mẹo kỹ thuật
- Sửa trang: `fs_edit` root gh; tệp ~760KB, luôn dùng old_str nguyên văn; báo «không khớp» thì `fs_search` lấy nguyên văn; push bị từ chối (phiên khác vừa đẩy) thì gửi lại cùng expected_version.
- Trang xem giữ bản cũ: mở `ui-preview/hpml-view-for-user/view.html?task=mow-mot-moit-mout`, bấm `header button`, đợi ~18 giây, rồi chụp `knowledge/modules?…&section=<id>`.
- Công cụ chụp không mở được «Chi tiết» trong khung trang → kiểm bằng đếm mã (`fs_search` count) và nói rõ giới hạn.
- Đọc PG: `query_pg` database `directus` (chỉ đọc). `directus_read` đang lỗi phân giải tên miền.
- Neo trang: `formula-ct-000-1` … `formula-ct-000-4` · `formula-ct-001` … · `kn-cat-000-5`.
- Mỗi lượt sửa: cập nhật Bảng điều khiển + Nhật ký (P tăng dần) trong COLLAB này.
- Mọi mục chèn vào §0 dùng cấp `###` trở xuống. Cấp `##` cắt §0 ⇒ trang Task mất Bảng điều khiển (bộ đọc `hvu-b2/sync.py` lấy §0 tới dòng `##` kế). Lỗi P67, sửa P68.

- **Máy kiểm CT-000.4: tệp `work/mow-mot-moit-mout/kiem-ct000-4.py` · Master Công cụ ML-DEF-023 mã `python:kiem-ct000-4`.** Chạy: `python3 work/mow-mot-moit-mout/kiem-ct000-4.py --dot-bien` (workspace_exec, root workspace). `--kb A,B` chỉ xét một phần kịch bản (mã tối đa 2); `--kb -` = chỉ kiểm tĩnh + cấu trúc + tranh chỗ + ca (nhanh, ~15 giây); `--json ĐƯỜNG_DẪN` ghi bằng chứng; `--tu-kiem` máy kiểm tự chứng minh phân loại (lỗi máy ⇒ CHECKER_ERROR · đột biến thật ⇒ KILLED · tự lặp ở trạng thái tạm bị bắt), tự chạy trước `--dot-bien`; duyệt lớn chạy từng 1–3 kịch bản (lượt chung 21 kịch bản hết bộ nhớ). Mã thoát: 0 đạt · 1 còn lỗi (có vết) · 2 chưa kết luận (quá trần, máy kiểm lỗi, xét một phần) — **2 KHÔNG phải đạt**. Đột biến: KILLED / SURVIVED / INCONCLUSIVE / CHECKER_ERROR, chỉ KILLED tính là bắt; đột biến chỉ chạy khi bản gốc sạch. Mỗi lần sửa 6 bảng của CT-000.4 PHẢI chạy. Ca mới: thêm vào `CA` (phần tử thứ 7 `kiem` = giá trị biến mong đợi cuối); mỗi ca cấm nên có ca được phép đối ứng.
- **Luật lưu công cụ (Owner 21/10 20:37: «lưu lại tất cả các công cụ đã dùng để sau này không phải làm lại»).** Mọi phép kiểm/script đã dùng để ra kết luận phải: (1) nằm trong tệp công cụ trong kho — cùng việc thì gộp vào công cụ sẵn có (P74: kiểm cấu trúc bảng từng làm tay đã gộp thành S8), không để `python3 -c` rời; (2) có mục trong Master Công cụ ML-DEF-023 = `work/tools-quy-trinh/view.html`: mục `provider_tools` (id ổn định, path, sha256, verify, input/output, limitations, evidence_state) + mục `memory` (owner, acceptance_scope, blocker, next_action); (3) mỗi lần sửa tệp → cập nhật sha256 + trạng thái Master trong cùng phiên, rồi chạy `python3 work/mow-mot-moit-mout/kiem-ct000-4.py --kiem-ke` phải thoát 0 (kiểm đường dẫn, sha256, manifest từng tệp, mục ghi nhớ; ⚠ liệt kê script trong thư mục việc chưa vào Master). Ghi chú nơi ghi: Master Tool ML-DEF-023 (giao diện stt 23) = 9 phương pháp trong `ui/definition-master-data-v1.js` + `view.html → catalog.tool_registry.provider_tools`; `records` cùng khối là Master DOT ML-DEF-024 (6 bộ kiểm TQT, bộ chạy tổng chạy theo đó — không thêm script dài vào đây); (4) công cụ của AI khác ghim hash (`python:ct000-audit` của GPT) → không tự sửa hash/ca, báo AI chủ quản rà nghĩa; (5) trước khi viết công cụ mới, tra Master trước — có rồi thì dùng/điều chỉnh.
- ~~Máy kiểm P71~~ CŨ, KHÔNG DÙNG (GPT Pro chứng minh bỏ lọt 11/11 đột biến). Mỗi lần sửa Bảng Trạng thái, Bảng Chuyển trạng thái hoặc câu G4.6 PHẢI chạy khối dưới (workspace_exec, root workspace, `python3 -c`). Đạt = «LỖI 0» và «CA THỬ ĐẠT n / n». Ca mới: thêm 1 dòng vào `TR` (tên, trạng thái đầu, các bước sự kiện–giá trị, trạng thái cuối mong đợi, biến, trạng thái phải qua / `!` không được qua).
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
- (P75 → P76) ĐÃ GHI DANH 6 script hiện hữu của mow-mot-moit-mout vào Master Tool ML-DEF-023: `python:dot-walk-check`, `python:dot-edit-simulate`, `python:dot-push-verify`, `python:dot-page-shot`, `python:dot-process-gate`, `python:check-ui-review`; path + sha256 + memory. Kiểm JSON thật sau cập nhật: không còn script nào trong danh sách 6 nằm ngoài Master. Chỉ ghi danh artifact để dùng lại; chức năng/hợp đồng thực thi chưa nghiệm thu trong lượt này, thuộc Host mow-mot-moit-mout. Không sửa 6 tệp, không đưa vào runner DOT.
- (P68) Các «1 hàm PG», «Directus Flow lịch» trong 13 yêu cầu PG là yêu cầu thiết kế, chưa có công cụ thật — dựng khi lên PG (thiết kế từ yêu cầu, H6.12).

### BẢNG ĐIỀU KHIỂN · cập nhật 2026-10-22 17:50 · Claude Host · P91

> **P91: MBM r6.7 — mục 4 = Hồ sơ** (`22185f1f`, Owner 17:34): bảng ghi sẵn 3 phần — I Thông tin chung (8 ô, máy điền) · II Mốc / Bước làm (5 Mốc, mỗi câu 1 dòng) · III Bộ câu của MMOW; mỗi dòng có Check 1 (AI làm) + Check 2 (AI khác hãng) ký tên. Luật điền thu vào «Chi tiết». Chờ Owner gật 1 điểm: 3.1 Mốc 1 còn ghi mã việc ở CAT-227, hồ sơ lấy mã từ Master MOW.

> **P90: MBM r6.6 — 3.2 đã xong** (Owner 16:54). 3.2 Bước làm chỉ hiện công thức **Dòng Miền CV + Bộ câu của MMOW ⇒ Hồ sơ**; 3 dòng giải thích thu vào «Chi tiết». Mục tiêu, Công thức không ở 3.2 vì đã có trong bộ câu (G1.2 · G1.4 · G2.11 · G3.7). Chờ GPT rà P83 trên bản r6.6.

> **P82: MBM r6.0.** Bước = Việc + Miền CV + Công thức; bộ câu = 43 câu, mỗi MMOW chốt phần cố định + hướng dẫn bổ sung; MMOW 07 cố định 39 câu + Đ1, Đ2 (mục 3.1). Chờ GPT rà P83.

> **P79: CÁCH DÙNG 43 CÂU** (mục 3): mỗi việc chỉ trả lời câu áp dụng — bảng quyết định + máy tra + JEV, học dần từ việc thật, dùng ngay. Chờ GPT đồng thuận (P80) + Owner hướng dẫn MMOW.

> **P78: ĐỔI CÁCH LÀM.** Dừng kiểm vét cạn H4.4a (giữ thành quả: 21/21 kịch bản 0 lỗi trên VPS). Việc kế tiếp = 1 MOW thật (MOW 001 vẽ UI) từ khai báo tới nghiệm thu. Mỗi lượt ≤ 15 phút.

> **GPT phản biện P76: CHƯA THÔNG QUA H4.4a.** Đồng thuận hướng bảng chạy được + ưu tiên PG/Directus, không yêu cầu thay kiến trúc. Nguồn HTML `5948c52f…`, checker `dbcf08b7…`: 29/29 ca cũ đạt; 9 phát hiện gom 6 nhóm: kết quả/gia hạn lượt cũ; phản hồi người rỗng tự mở cổng; 8 mã gRPC thiếu đường; checker lỗi vẫn bị tính KILLED; phép kiểm tính sống yếu hơn phát biểu; kiểm kê nhận nhầm chuỗi lịch sử. Phân biệt phản ví dụ mô hình, thiếu hợp đồng đầu vào và phép tự kiểm checker trong `audit-ct000/REPORT-V7.md`; không gọi là lỗi production đã xảy ra. Bộ GPT đã nâng cùng mã, `run.py --v7`, manifest 23 tệp; 6 script còn thiếu đã ghi danh, chưa nghiệm thu chức năng, không đổi Master DOT. Claude vẫn Host; chưa PG/Flow và không có READY/RUN triển khai.
- ⚠ Mỗi lượt sửa task: sửa luôn các dòng tổng — giờ cập nhật · ✅ · ⬜ · ➡ · tên việc (nếu mục tiêu đổi).
- 🎯 Mục tiêu: ô 1. Vì sao: bài thử MBM — lần 2 không có Owner, AI vẫn tự chạy.
- 🏁 Xong khi: ô 2.
- 📍 Tiến độ (MBM 6.x): [✓ 6.1 Nhận yêu cầu] → [✓ 6.2 Tạo task] → [✓ 6.3 Chốt mục tiêu] → [◐ 6.4 Liệt kê bước — bản thử] → [◐ 6.5 Bộ câu hỏi] → [■ 6.6 Check Master list] → [□ 6.7 Ký] → [□ 6.8 Chạy]
- ✅ Đã xong: ô 1–2 (18/10 21:25) · rà tới hết mục 4 theo MBM r5.34: 8 bước (5 cố định + 3 chuyên môn) · bảng câu hỏi H1–H7 + Đ1, Đ2 · K1, K2 đã gỡ — xem tab «Nội dung công việc» (`view.html`) · 19/10: Info contract chuẩn ngành, Config + Saga, ý kiến Astra ngoài MBM · M1: QTTH đổi tên MMOW, 4 tầng MBM → MMOW → MOW → Hồ sơ (MBM r5.35) · tên hiển thị «Master MMOW», «MMOW 05/06» trên các trang (mã khoá ML-MOW-TH-001 / MOW-TH-xxx giữ tới khi lên collection — nợ 🔴 VD-027) · Master MMOW có dòng MMOW-007 (việc này), trang hiện mã MMOW-xxx · 18:28: MMOW 07 chỉ Vẽ UI; Master MMOW thêm MMOW-008 (Info contract), MMOW-009 (Config) · 22:26: Master MOW có 3 cột tích Vẽ UI · Info contract · Config (35/35 ☐; tích trên giao diện = nợ VD-028) · 20/10: trang Công thức có khối KHÁI NIỆM · CAT-000.5 (54 loài, 5 định luật ĐL1–ĐL5, ký hiệu tạm chờ vector); MMOW mã OBJ-MMOW · 14:18: CAT-000.5 hợp nhất 107 loài mã SPE (gộp entity_species + khái niệm nháp + CAT-237*; quét máy Q1–Q6: 4 bảng vô chủ, mã mồ côi audit_log, 6 loài lệch tiền tố, 10 sổ 2 mã) · Master Duyệt thiết kế có CAT-000.5 + cột Duyệt TK (xanh = User đã duyệt; CAT-000.5 tạm duyệt 20/10) · nợ VD-029 (ghi PG) · 15:08: chuẩn «?» cho mọi bảng mới (ĐL6), CAT-000.5 đã có «?» ở tiêu đề, ma trận, 8 cột · 17:32: trang Công thức có 2 thanh thu/mở «Công thức gốc» (CT-000.2 Cấp ghép 1–4) + «Công thức chuyên môn» (CT-001→008); 14 thẻ có dòng mờ loài + sổ · 20–21/10: Công thức gốc (21/10 09:51): CT-000.1 Bộ câu hỏi chuẩn (43 câu Trước · Trong · Sau + 1 luật rẽ nhánh; gộp Info contract law) · CT-000.2 Điều luật (+ Xử lý bằng) · CT-000.3 Cấp ghép · CT-000.4 Xử lý lỗi = quy trình 9 bước (Ghi sự cố → Xếp hàng → Tra quy trình → Chạy → Kết quả → Kiểm lại · Vấn đề → MMOW → Owner). 10:02: CT-000.1 không đạt ⇒ chỉ vào hàng đợi (bỏ «Thiếu ⇒ Tạo mới»: khái niệm, không phải bước làm). Kế tiếp: skill tự kiểm 43 câu cho agent (chờ Owner). · 21/10 P68: CT-000.1 + CT-000.4 thành luật yes/no theo chuẩn ngành (commit 9275bd59, d4d38d27; Master Công thức ui 9bd5a22). · 15:30 P69: luật Kiến trúc — PG gốc + Lớp trên (CT-000.2 dòng 7–8); 2 Bảng Chuẩn ngành ghi rõ «chỉ mượn cách làm, không cài, không trả phí» (commit b6bc677d). · 16:15 P70: sửa theo vòng 3 GPT Pro + luật Không mồ côi (commit 8d1479e2, a4648ef4; ui 19d9d4a). · 16:25 P71: Bảng Chuyển trạng thái + máy kiểm 0 lỗi, 14/14 ca (commit da9609f9, 7cc4ecec, e14ad530). · 18:35 P72: bảng máy chạy được + kiem-ct000-4.py, 8 lỗi thật đã sửa (commit 32f1c61f … 8bac5f76). · P73: GPT rà v6 bằng công cụ; lưu v5/v6 và bằng chứng vào kho chung; đăng ký 2 mã Master Công cụ (ghi danh để dùng lại, chưa nghiệm thu quy trình).
- ■ Đang làm: H4.4c1 — MBM r6.7 (3.2 xong · mục 4 = Hồ sơ 3 phần) + bộ câu cố định MMOW 07, chờ GPT rà P83 · 0 RUN active
- ⬜ Còn lại: chốt 6.4 → đạt 6.5 → 6.6 → 6.7 → 6.8.
- ➡ Kế tiếp: GPT rà MBM r6.7 + bộ câu MMOW 07 (P83, 1 vòng) → lập sổ CAT-250* Master Miền CV + dòng MCV-001 (35 MOW) → trả lời 22 câu 📋 mẫu MMOW 07 một lần → MMOW 07 chạy trên MOW 001 (UI + hồ sơ đầu tiên) tới nghiệm thu → Owner xác nhận UI. Mỗi lượt ≤ 15 phút. (P78 dừng H4.4a, giữ thành quả; H4.4b PG + Flow chỉ khi cần.)
- ⛔ Không làm: G2/PG production · dựng collection trước khi ma trận được ký · gõ tay vào Directus.

### 1. Mục tiêu
Tình trạng: User chốt (Owner 19/10 18:28).
Owner 19/10/2026 18:28 (thay bản 18/10 21:25): mỗi MMOW chỉ giải quyết 1 việc.
1. Vẽ UI (gồm tất cả bước con) cho các MOW trong Master MOW — sẽ vẽ hàng ngàn UI. Trước mắt gắn theo list MOW; sau này gắn thêm list Task, MOIT, MOUT.
Đã tách: Chốt Info contract → MMOW 08 · Config → MMOW 09 (Master MMOW).
Theo MBM r6.4 (P87): phạm vi tách sang Miền CV — đợt 1 MCV-001 = 35 MOW (Master MOW); list Task, MOIT, MOUT = các đợt sau. Mục tiêu MMOW 07 chỉ còn: Vẽ UI (gồm tất cả bước con).
Owner 16/10 16:29: đây là bài test MBM — vừa làm vừa sửa MBM để lần 2 không có Owner, AI vẫn chạy được.

### 2. Thế nào là hoàn thành
Owner 18/10/2026 21:25, ý 1 (giữ cho MMOW 07):
1. Vẽ đủ UI theo các bước con (kể cả tách hoặc gộp theo bước con nếu có). → bước con thiếu UI = 0.
Ý 2 (đầu mối Info contract) → MMOW 08 · ý 3 (sẵn sàng Config) → MMOW 09.
D1, D2 (MBM 2.5, không chặn): đã rà — xem tab Nội dung công việc, mục 2.

### 3. Chi tiết cần đạt (AI ghi, Host kiểm)

#### 3.0 Cách dùng 43 câu (P79 · Owner 22/10 11:05–11:45 · GPT đồng ý P80, đã sửa 3 điểm P81)
1. **Nguyên tắc.** Thứ hữu hạn thật sự là thời gian ⇒ không tuyệt đối hoá. Mỗi việc chỉ trả lời đúng câu áp dụng: không thừa, không thiếu. Việc 5 phút không được thành nửa giờ kiểm.
2. **Thành phần.**
   2.1 Bộ 43 câu (đã có) = hợp đồng thông tin dùng chung.
   2.2 Bảng quyết định (chuẩn DMN): 43 câu thêm 2 cột «Hỏi khi» (luôn · khi có đặc điểm X) và «Tự điền từ đâu» (sổ · mẫu Loại việc · máy cấp · không). Không ô trống; chỉ kiểm 1 lần khi soạn bảng.
   2.3 Đặc điểm việc (~6 câu có/không): ghi dữ liệu thật · gửi ra ngoài hoặc không hoàn tác · có người duyệt · tạo mới · làm song song · hạn cứng.
   2.4 Máy tra: Loại việc ⇒ kế thừa đặc điểm + danh sách câu đã lưu · đặc điểm còn thiếu ⇒ JEV **chỉ gợi ý** kèm xác suất, không tự xác nhận: dữ kiện chỉ được nhận khi có bằng chứng trong sổ hoặc người có thẩm quyền xác nhận · bảng ra danh sách câu · tự điền phần có trong sổ.
   2.5 Thiếu thông tin ⇒ hỏi đúng người. Câu không áp dụng thì bỏ qua (➖ + lý do); câu cần mà chưa có dữ liệu ghi «Chưa biết», không bao giờ tự coi là đạt.
3. **Học từ việc thật.** Câu nào phải hỏi người ⇒ đề xuất thành luật; kiểm (Host + 1 ghế khác hãng) rồi mới đưa vào bảng dùng chung, không tự biến câu trả lời thành luật. Loại việc chạy xong 1 lần ⇒ lưu danh sách câu của loại đó.
4. **Thứ tự.** Bản 0 bảng quyết định (trang Công thức, dưới CT-000.1) → dùng ngay cho MOW 001 vẽ UI → sửa bảng theo chỗ thiếu → bảng ổn mới viết script, rồi PG/Directus. Không chờ tự động hoá xong mới dùng.
5. **Xử lý lỗi.** CT-000.4 chỉ gọi khi gặp lỗi thật; không kiểm vét cạn trước.
6. **Nhịp làm.** Mỗi lượt ≤ 15 phút và phải có kết quả hoặc điểm tiếp tục rõ ràng; quá thì dừng, báo, chia nhỏ.
7. **Chuẩn ngành mượn cách làm:** câu hỏi có điều kiện (skip logic) · bảng quyết định DMN · ITIL 4 «standard change» (việc có mẫu sẵn thì theo mẫu, không đánh giá lại từ đầu).
8. **Danh sách câu chốt ở MMOW (Owner 22/10 15:11).** Mỗi MMOW chốt cố định câu phải trả lời (MBM r6.0 mục 4.2), không để mỗi AI tự lọc ⇒ kết quả đồng nhất; câu ngoài danh sách ghi ở mục «Câu hỏi bổ sung (nếu có)» của hồ sơ (4.3). Bảng quyết định (2.2) chỉ dùng khi soạn danh sách cho MMOW mới.

#### 3.1 Bộ câu cố định MMOW 07 · Vẽ UI (P82–P87 · bản thử, kiểm bằng hồ sơ MOW 001 · theo MBM r6.4 mục 3.2 + 4)
3 tầng (Owner 15:35): MBM (công thức gốc) ⇒ MMOW 07 (Vẽ UI) ⇒ MOW 001, MOW 002… trong Master MOW. Mỗi lần MMOW 07 chạy trên 1 MOW để lại **1 hồ sơ = danh sách câu dưới đây + câu trả lời**, gắn mã MOW, đi cùng MOW đó mãi mãi.
Bước làm (MBM r6.5 mục 3.2): MCV-001 (35 MOW · Master MOW) + Bộ câu của MMOW 07 (bảng dưới) ⇒ 35 hồ sơ · Xong khi: bước con thiếu UI = 0 · Thao tác: đọc yêu cầu → dựng giao diện → chụp ảnh kiểm → gửi duyệt.

| Nguồn trả lời | Số | Câu |
|---|---|---|
| 📋 Mẫu MMOW — trả lời 1 lần, khi chạy chép vào từng hồ sơ kèm phiên bản | 22 | G1.2 · G1.3 · G1.4 · G1.8 · G1.9 · G2.2 · G2.4 · G2.5 · G2.7 · G2.11 · G3.1 · G3.2 · G3.3 · G3.4 · G3.5 · G3.7 · G3.10 · G4.4 · G4.7 · G5.1 · G5.2 · G5.3 |
| 🤖 Máy điền khi chạy | 12 | G1.1 · G1.6 (lấy dòng từ Miền CV — P87) · G1.7 · G2.1 · G2.6 · G2.9 · G2.10 · G3.6 · G3.9 · G4.3 · G4.5 · G4.6 |
| ✍ Riêng từng hồ sơ (người làm điền) | 5 + 2 | G1.5 · G4.1 · G4.2 · G5.4 · G5.5 · Đ1 Dùng lại UI nào, vẽ mới UI nào? · Đ2 Bước con nào cần tách hoặc gộp? |
| ➕ Chỉ thêm khi gặp (mục «Câu hỏi bổ sung» của hồ sơ) | 4 | G2.3 · G2.8 · G3.8 · G3.11 |

Luật kèm (GPT P80): G1.7, G1.8 máy chỉ điền khi có mặc định đã duyệt · vai ở G2.2, G4.4, G5.1 phải ra người cụ thể khi chạy · G1.5, G4.2 không mặc định «không áp dụng»: vẽ mới ghi «không có», sửa UI cũ ghi thứ phải giữ · G3.3–G3.5 dùng mặc định đơn giản (1 việc / MOW).

#### 3.2 Định nghĩa Bước làm (Owner 22/10 16:04 · MBM r6.4 Bảng 3.2)
1. Yêu cầu: mọi người đọc hiểu **đúng và nhất quán, không thể hiểu sai** — Mục tiêu của tầng nào (MBM · MMOW · MOW), Miền CV, Công thức nào đều phải định nghĩa rõ.
2. Miền CV cần 1 master list mới: mỗi đợt triển khai có mã, tên, master list nào, số lượng… để truy vấn dễ, quản lý vòng đời tốt. 1 master list (MOW, Task, MOIT, MOUT, Field…) có nhiều đợt. Định nghĩa ngắn nhưng rõ để AI sau đọc hiểu.
3. Owner 16:25: Công thức đã dùng để tạo master list, Miền CV là 1 phần trong đó ⇒ không đưa ra lại. Mục tiêu để AI hiểu việc và tự đánh giá sau khi làm, không phải chỗ máy hành động. Giải thích phải ngắn — nhiều chữ là rối.
4. Đã chốt (r6.5–r6.6, Owner 16:43–16:54 · 3.2 kết thúc): **Dòng Miền CV + Bộ câu của MMOW ⇒ Hồ sơ**; trên MBM chỉ hiện công thức, giải thích ở «Chi tiết» (cho người đọc lần đầu hoặc lúc quên). Bộ câu của MMOW = các câu trích từ bộ câu chuẩn, chốt riêng cho từng MMOW; MMOW đặc thù có thể có câu riêng ngoài bộ chuẩn. Miền CV: 1 đợt = 1 MMOW + 1 master list, danh sách chốt khi bắt đầu chạy (JEV: A 0,58 · chốt danh sách 0,83) — chi tiết cột ghi ở sổ CAT-250* khi lập, không ghi trong MBM.

#### 3.3 Hồ sơ (Owner 22/10 17:34 · MBM r6.7 mục 4)
1. Mục 4 MBM = Hồ sơ: bản chất là 1 bảng ghi sẵn + hướng dẫn làm. Thiết kế MMOW thì mọi câu hỏi soạn sẵn; lúc làm chỉ điền đủ trả lời là xong.
2. 3 phần: I Thông tin chung (MMOW · MOW · Miền CV · Mã việc / Tên việc lấy từ Master MOW · Hạn hoàn thành · thêm nếu cần) · II Mốc / Bước làm (STT · Tên Mốc · Câu hỏi, mỗi câu 1 dòng · Thông tin đã làm · Thế nào là hoàn thành · Check 1 · Check 2) · III Bước làm — Bộ câu của MMOW (STT · Câu hỏi · Trả lời · Check 1 · Check 2).
3. Check 1 = chữ ký AI thứ nhất, Check 2 = chữ ký AI thứ hai — ghi tên mình (vd Claude, GPT).
4. Host thêm vào phần I (lý do: thiếu thì không truy được, không quản vòng đời): Mã hồ sơ · Phiên bản mẫu · Tình trạng. Check 2 phải khác hãng với Check 1 (theo luật G4.4 + hội đồng).

Kết quả bước 3, bước 4 và vấn đề lộ ra: tab «Nội dung công việc» trên trang Task (tệp `view.html` của việc này) — 1 nơi, không chép lại ở đây. Vấn đề và nợ kỹ thuật (mẫu CAT-069, mã VD-…): cũng ở đó — không dựng hệ phức tạp, xong MMOW 07 thì lên collection + DOT.

#### 📏 Chuẩn chung (Owner 20/10 15:08)
- Mọi bảng mới có «?» ở tiêu đề bảng và từng cột, giải thích cái gì + hướng dẫn cho người mới. Lên collection vẫn giữ: «?» = ghi chú (note) của bảng và của từng trường. (CAT-000.5 ĐL6)
- CAT-000.5 tạm đặt trên trang Công thức; sau chuyển sang collection (nợ VD-029).
- Kiến trúc (Owner 21/10 15:15): PG là tầng gốc giữ sự thật — dữ liệu, hàng đợi, trạng thái, khoá; khai thác tối đa PG trước cho đơn giản, tin cậy. Dịch vụ như Kubernetes chỉ là lớp trên cho bài toán chuyên biệt, không giữ dữ liệu gốc, tắt đi chỉ chậm hơn. Chuẩn ngành = mượn cách làm, không mua dịch vụ. Luật: CT-000.2 dòng 7 «PG gốc», 8 «Lớp trên».
- Khép kín (Owner 21/10 15:35): mọi điểm có thể gãy phải đi đến cùng mọi nhánh, mọi trường hợp; tệ nhất là vào hàng đợi (quản lý được); không để tình trạng mồ côi. Luật: CT-000.2 dòng 9 «Không mồ côi», 10 «Còn lại»; CT-000.4 Bảng Trạng thái + Yêu cầu PG 14.
- Cơ chế thay nguyên tắc (Owner 21/10 16:24): viết nguyên tắc không có nghĩa gì; phải có cơ chế để không hiểu sai, không thể làm sai. Áp dụng: đường đi của việc chỉ viết 1 chỗ (Bảng Chuyển trạng thái); máy kiểm (H7) phải ra 0 lỗi trước khi đưa duyệt; lên PG thì hàm chuyển trạng thái chỉ đi theo dòng có trong bảng (PG 16).

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
- P91 · 22/10 17:34 · «Mục 4 giờ nên đưa thành Hồ sơ: (bản chất ở đây là hướng dẫn cách tạo hồ sơ trong MMOW) Hồ sơ đơn giản gồm 3 phần: I. Thông tin chung: 1. MMOW 2. Mow 3. Miền CV 4. Mã việc/Tên việc (lấy từ list mow) 5. Time hoàn thành 6. … khác bổ sung nếu bạn thấy cần · II. Mốc / Bước làm: 1. STT 2. Tên Mốc 3. Câu hỏi (nên tách ra từng câu: Ví dụ việc gì, 1 dòng, đã có mã việc chưa 1 dòng...) 4. Thông tin đã làm 5. Thế nào là hoàn thành?: Định nghĩa từng việc 6. Check 1: Chữ ký của AI thứ nhất, điền tên mình vào luôn VD: Claude 7. Check 2: Chữ của AI thứ hai điền tên mình vào luôn VD: GPT · III. Bước làm - Bộ câu của MMOW: 1. STT 2. Câu hỏi 3. Trả lời 4. Check 1 5. Check 2. Bản chất hồ sơ là 1 bảng ghi sẵn và hướng dẫn làm. Đến khi thiết kế MMOW => Tất cả câu hỏi này thiết kế sẵn, lúc làm chỉ cần điền đủ số câu trả lời là xong.» → MBM r6.7 (`22185f1f`): mục 4 = Hồ sơ, 3 bảng ghi sẵn có «?»; phần I thêm Mã hồ sơ · Phiên bản mẫu · Tình trạng; luật điền (bộ câu · nguồn trả lời 📋🤖✍ · ➖🟡🔴 · câu bổ sung · Check · ký hồ sơ mẫu) thu vào «Chi tiết»; bỏ 4.5 Mở khi / Dòng Mốc không lưu riêng (trái với phần II); công thức đầu MBM 4 = Hồ sơ; 6.0, 6.5, 9.5, SPE-CHO* sửa cho khớp.
- P90 · 22/10 16:54 · «1. Cho mục 3.2.1 -> 3.2.3 vào Chi tiết để thu lại cho ít chữ. Quá trình làm nhiều tôi chỉ cần nhìn công thức, giải thích thì đúng lúc nào quên hoặc những ai đọc lần đầu. 2. Bộ câu MMOW => Bộ câu thuộc MMOW (bổ sung thêm chữ "thuộc", hoặc chữ "của" nhìn sẽ dễ liên tưởng hơn. Hạn chế và đọc giải thích. Sửa xong phần này là kết thúc 3.2.» → MBM r6.6: 3.2.1–3.2.3 vào «Chi tiết»; «Bộ câu của MMOW» (JEV: của 0,63) ở công thức, 3.2.2, 4.2, 6.4, 9.1. 3.2 kết thúc.
- P89 · 22/10 16:43 · «Đồng ý, thấy nó dễ hiểu hơn. Thêm định nghĩa: Bộ câu MMOW: Là các câu hỏi trích từ bộ câu hỏi chuẩn cho từng MMOW cụ thể. Bộ câu hỏi này được chốt theo từng MMOW. Note: các MMOW đặc thù, có thể có những câu hỏi riêng ngoài bộ câu hỏi chuẩn. Mục 3.2 bạn lại làm 1 cái chi tiết của riêng công thức mục 3.2 nữa. Giải thích ngắn gọn và cho nó gọn lại. Con người nhìn nhiều chữ sẽ bị rối.» → MBM r6.5 (`575531f8`): 3.2 còn công thức + 3 dòng (Miền CV · Bộ câu MMOW · Hồ sơ); bỏ bảng 4 dòng và dòng cột sổ Miền CV; 4.2, 6.4, 9.1, Master Khái niệm sửa cho khớp.
- P88 · 22/10 16:25 · «Bạn đang cố ghép các dữ liệu với nhau, nhìn thực tế từ 1 người phải làm tôi thấy mơ hồ hết sức. Không khả thi. 1. Công thức đã được dùng để tạo ra master list và miền công việc là 1 phần trong đó rồi. Đưa ra sẽ bị rối? Bạn phải đọc toàn cảnh bởi vì phần này nó liên quan đến những phần khác. 2. Mục tiêu cho vào đây: kể cả đo đếm được cũng vô nghĩa. Máy không biết làm gì với mục tiêu đó. Mục tiêu là để AI hiểu việc phải làm và tự đánh giá lại sau khi làm xong. Chứ mục tiêu không thể là chỗ để cho máy hành động được. Phần giải thích cũng dài và mơ hồ. Bạn có ý kiến ra chat trước, ok hãy sửa cho đỡ mất thời gian.» → Host: đọc lại 43 câu — làm gì (G1.2, loài đã gắn công thức), bằng gì (G2.11), ghi ra đâu (G3.7), xong khi (G1.4 → AI tự chấm G4.1) đều đã có ⇒ đề xuất 3.2 = «Dòng Miền CV + Bộ câu MMOW ⇒ Hồ sơ», 3 dòng; rút đề xuất cột «Công thức» ở Master MMOW. Luật cho Host: trước khi thêm gì vào MBM, tra 43 câu trước — có rồi thì không thêm.
- P87 · 22/10 16:04 · «Giờ bàn về công thức này: 3.2 Bước làm Mục tiêu+Miền CV+Công thức⇒Bước làm. 1. Mục tiêu là gì? Mục tiêu ở đây có trùng với phần mục tiêu 2 không? Mục tiêu của MBM hay của MMOW, hay của MOW chúng ta không làm rõ thì làm sao mà đảm bảo tất cả mọi người đọc hiểu đúng được (đúng và nhất quán, không thể hiểu sai => đấy mới là yêu cầu) 2. Miền công việc: đúng là chỗ này cần phải 1 bảng master list mới nữa thật… Miền công việc, bản chất là 1 phần (1 danh sách ngắn) trong đó… (hiểu nôm na là 1 đợt triển khai)… mỗi bảng này lại có thể có nhiều miền công việc khác nhau… có mã của miền công việc, có tên miền công việc và các thông tin kèm theo như master list nào? Số lượng… => đừng định nghĩa dài nhưng phải định nghĩa rõ ràng để các AI sau đọc còn hiểu. 3. Công thức: là công thức nào phải định nghĩa rõ? Giải quyết 3 việc này trước.» → MBM r6.4 (`8b21c5d6`): Bảng 3.2 (Thành phần · Là gì · Ghi ở · Luật · Ví dụ MMOW 07) + 3.2.1 sổ Miền CV 8 cột; Master Khái niệm SPE-MCV*, SPE-BLM* sửa cho khớp; COLLAB 3.2; G1.6 chuyển 🤖.
- P85–P86 · 22/10 15:40–15:46 · «1. Việc là việc gì? lấy từ đâu? 2. Công thức là công thức gì? Lấy từ đâu?» — «Bạn đang làm rối tinh lên… giờ chúng ta đã có bộ câu hỏi chuẩn => MBM nên đơn giản nhất có thể… rút được thành phần phức tạp nhất là: bộ câu hỏi chuẩn ra làm "thửa số chung" phần còn lại đơn giản nhất có thể để ghép. Nếu bạn thấy hợp lý thì bỏ mục này đi đã: 3.2 Mục con» → MBM r6.2 («Việc» trùng SPE-VIC* → Mục tiêu) · r6.3 bỏ Mục con, mục 3 = Mốc + Bước làm (3 dòng + bảng ví dụ).
- P84 · 22/10 15:35 · «MBM là công thức gốc => MBM để ra MMOW (trước kia đặt là quy trình tổng hợp) MMOW (VD MMOW 007 vẽ UI => sinh ra MOW 001 (trong master mow list. Mỗi lần MMOW 007 chạy ra quy trình vẽ UI MOW 001, MOW 002... (Có hàng chục ngàn MOW kiểu này) thì sẽ để lại 1 hồ sơ. Chính là danh sách câu hỏi và kết quả trả lời cho các câu hỏi đó. Hồ sơ này đi cùng MOW mãi mãi. Rà soát lại xem bạn có đang hiểu đúng chưa?» → MBM r6.1 3.3.3 + 4.2; COLLAB 3.1.
- P82 · 22/10 14:37–15:11 · «Chúng ta quay trở lại hoàn thành MBM… Việc trước đây đang bị tắc là phần Bước trong MBM… Thay vì phải liệt kê nhiêu câu hỏi trong MBM => MMOW chúng ta chỉ áp đầu việc vào bộ câu hỏi chuẩn được không?… Các phần khác của MBM giờ có nên đơn giản hơn không?… Bàn trước đã» — «…phức tạp không phải là để giải quyết MMOW 007 mà khó khăn là tôi muốn tìm ra 1 công thức tổng quát => để ghép… trả lời câu nào nếu không chỉ định rõ => các AI khác nhau => có thể đưa ra các quyết định khác nhau… Chốt cố định câu hỏi vào MMOW… làm thử với MMOW 007 thử trước… Các câu hỏi cố đinh trong 43 câu mà MMOW… phải trả lời… Có 1 hướng dẫn bên dưới là có thể có những câu hỏi bổ sung… trong phần hồ sơ sẽ có 1 mục là câu hỏi bổ sung (nếu có)… Bạn nghiên cứu và tổng hợp lại cùng với ý kiến của GPT để sửa nhé.» + [GPT: giữ 5 Mốc/mục con/5/7/8, bỏ H1–H7, 1 MMOW 1 nhiệm vụ nhiều thao tác, mặc định an toàn ≠ không áp dụng] → MBM r6.0 (`0c224182`); mục 3.1; H4.4c1.
- **P80 · 22/10/2026 · GPT Reviewer · H4.4c0 · vòng 1/1 · Based_on P79 / commit `776e8b36`**. **ĐỒNG THUẬN hướng 3.0 «Cách dùng 43 câu»**, không vét cạn, không chờ tự động hóa, dùng ngay trên MOW 001 vẽ UI. Chỉ đề nghị Claude Host chỉnh 3 câu nhỏ trước bản 0: **(1)** JEV ≥85% là mức **gợi ý** đặc điểm để giảm câu hỏi, *không tự xác nhận* dữ kiện, quyền hoặc phê duyệt chưa có bằng chứng; phần quan trọng phải đọc sổ hoặc hỏi người. **(2)** Câu áp dụng mà thiếu dữ kiện thì đánh dấu **Chưa rõ**, hỏi đúng người, không tự cho qua; câu không áp dụng thì bỏ qua có lý do. **(3)** Học từ việc thật nghĩa là ghi **đề xuất** cải tiến và kiểm/chốt rồi mới dùng thành luật chung, tránh học lại câu trả lời sai; quá 15 phút ghi phần đã xong, điểm dừng và bước tiếp theo để nối lượt sau, không bỏ dở. Không mở thêm bảng/công cụ/kiểm vét cạn, không sửa schema PG, không RUN. **Kết luận: ĐỒNG Ý TRIỂN KHAI bản 0 sau khi Host sửa đúng 3 chỗ trên trong mục 3.0.**
- P79 · 22/10 11:05–11:45 · «Tôi thực sự không hiểu các bạn kiểm gì mà chỉu nguyên cái bộ câu hỏi chuẩn mất vài ngày…» — «Mục tiêu không phải là cái đó. Mục tiêu là triển khai việc tiếp. Tuyệt đối hóa quá là 1 sai lầm. Bởi vì thứ hữu hạn thực sự là thời gian… Trước khi bắt tay vào làm để tránh những việc ngớ ngẩn kiểu này thì chúng ta có phương pháp nào không?» — «…việc này tôi cần phải trả lời bao nhiêu câu hỏi trong 43 câu đó?… Có cách nào để làm việc này không thừa không thiếu không?» — «…làm sao để tự động, ít nhất là như sử dụng Jev…» — «Việc này làm sao để tự động… phải hoàn thành nốt mục 2 rồi mới ứng dụng được đúng không?» — «Vậy thì nên ghi vào phần chi tiết quy trình này vừa làm, gửi cho GPT thống nhất cách làm để coi như chúng ta thống nhất bộ câu phải chuẩn. Tôi hướng dẫn thêm vài thứ về MMOW trước khi triển khai.» → mục 3.0 Cách dùng 43 câu; H4.4c0.
- P78 · 22/10 09:42–11:00 · «Chúng ta đang làm dở phiên này và đổi phiên… trước tiên bạn chỉ cần đọc lại phần cuối của phiên cũ để hiểu chúng ta đang làm gì? Giúp tiếp tục cho liền mạch.» — «Bạn chỉ xem cái cũ mà mất hơn 1 giờ => Cách làm viêc này chỉ dẫn chúng ta ra nghĩa trang, không bao giờ chúng ta có được cỗ máy. Chỉ là vài cái quy trình vẽ UI. => Config, liệt kê hợp đồng thông tin mà mỗi lần trả lời hàng tiếng thế này thì làm sao chế tạo được cỗ máy. Cần suy nghĩ lại cách làm. Phức tạp lên là ngớ ngẩn!!! Bạn tham khảo ý kiến của GPT. Việc không làm được và không đủ thời gian để làm thì cũng ngớ ngẩn giống nhau thôi mà. Kết quả chung vẫn là: Thất bại!» + [GPT đề nghị dừng vét cạn, 3 lớp, 1 MOW thật] → H4.4a dừng; H4.4c mới; luật lượt ≤ 15 phút.
- P76 · 22/10/2026 · Ghế: GPT Reviewer · Bước/vòng: H4.4a/v7 · 1/1 (Owner yêu cầu tiếp tục). Owner: «bạn tiêp tục việc đang làm dở xem nào?». Based_on snapshot `f34d15136e6cbe6630b0730d94a807f1453d904a`, HTML `5948c52f…`, checker `dbcf08b7…`. Scope: phản biện bằng công cụ, lưu và đăng ký artifact; không sửa bảng chính/máy kiểm Claude, không PG/Flow. KQ: 29/29 ca cũ đạt; V7-01..09 tái hiện 6 nhóm cần đóng; giữ H4.4a CHƯA THÔNG QUA, đồng thuận kiến trúc. Báo cáo chuẩn: `work/mow-mot-moit-mout/audit-ct000/REPORT-V7.md`; bằng chứng nguyên trạng `evidence/v7-results.json` SHA256 `65ca792fa93a9de5253973542812f7ea294d159058deef487c412dd94dc364ea`. Cùng mã Master `python:ct000-audit`, lệnh `python3 work/mow-mot-moit-mout/audit-ct000/run.py --v7`. Đã đăng ký 6 script còn thiếu ở Master Tool, trạng thái chỉ ghi danh/chưa nghiệm thu. Kiểm cuối job `f7ac3b6a47934ed5a3bb8ad25995b8ce`, snapshot `b07843d12482339157c51c82df42c23bfd532f48`: exit 1 do phát hiện mô hình/checker, stderr rỗng, 34 provider, ID trùng 0, 2 mục CT-000 đúng path/hash, manifest GPT 23/23 khớp, script còn ngoài Master trong danh sách 6 = 0. Next: Claude xử lý 6 nhóm theo ca đóng lỗi, không tăng tài nguyên duyệt lớn thay cho sửa mô hình; GPT rà lại nghĩa trước ghim nguồn mới. Claude vẫn Host; không READY/RUN triển khai.
- P73 · 21/10 20:27 +07 · GPT Reviewer, H4.4a/v6, Based_on `250792dce8380e94aa5fe85ce22477925150e6b8`. Owner: «Đây là phần sửa tiếp theo của Cloud Code bản rà soát giúp tôi xem còn vấn đề gì nữa không. Tôi muốn các công cụ các bạn đưa ra dùng nên cho vào list master công cụ để sau này xem xét có thể dùng lại những cái artifact đó, tránh việc bây giờ các bạn đã tạo ra các công cụ nhưng sau rồi lại bỏ đi, đến lúc cần lại viết lại rất lãng phí.» → **CHƯA ĐẠT**. Đã chạy lại baseline 35 trạng thái/107 dòng/226 bộ/49 thao tác, tĩnh 0, 16/16. Probe tái hiện T15 gửi sau hạn; T88 bù lần 2 khi MB=1; T88 bù sau hạn PH; B1–B11 im lặng. Đột biến công thức hết chỗ=False vẫn tĩnh 0/16 ca/PASS đồng thời; 17 khởi tạo không có còn_chỗ=False. Unit probe vào nhánh tổng kết chứng minh vượt trần hoặc RuntimeError bị đếm là bắt đột biến rồi exit 0; không phải đã chạy đủ 17 đồ thị ra 0. g2/g5 thiếu hoặc sai vẫn đóng Đạt trong mô hình; cần chốt kiểm dữ liệu trước default đủ. Chi tiết/sửa tối thiểu/trace: `work/mow-mot-moit-mout/audit-ct000/REPORT.md`, `evidence/`. Nguồn HTML full SHA256 `b94a70383f2e44ffadd9fa6c3e60868152eb0027c53cbb82e9ea8e1184625999`, máy kiểm `9e9436cdc058cb480e08ed6dc7062e0d74b18aae43ccbd1e632342939e4ecbd2`; manifest ghim nguồn trích và các file. Theo yêu cầu Owner, giữ nguyên 53 file v5 trong `work/mow-mot-moit-mout/ct000-audit-v5/`, v6 trong `audit-ct000/`, ghi đúng Master Công cụ ML-DEF-023 qua catalog có sẵn `work/tools-quy-trinh/view.html`: mã `python:kiem-ct000-4` + `python:ct000-audit`, có chủ quản, nguồn/hash, lệnh, đầu vào/ra, phạm vi, hạn chế và việc kế tiếp. Lệnh tái hiện v6: `python3 work/mow-mot-moit-mout/audit-ct000/run.py --snapshot --out /tmp/ct000-audit-v6-results` → exit 1 FINDINGS_REMAIN. Nguồn đổi ngoài phiên hỗ trợ trả exit 2, không đổi hash để bỏ qua. Không sửa logic của Host, chưa chạy hết 17 đồ thị/242 đột biến, chưa thử PG/Flow; Claude vẫn Host, không ghi READY/RUN. Xác minh sau ghi lúc 20:30 +07: commit chia sẻ `edcb28fa09ee35d762ea7b93d1f3b8dd0ea10d3d` đã push; Master ML-DEF-023 mở thật HTTP 200, 37 mục (9 phương pháp + 28 công cụ), thấy đủ hai mã mới, GPT/Claude đều Chưa duyệt. Chạy lại từ bản sao cách ly của kho chung qua workspace_exec job `18cab3116598424e8949273418c4fbc8` (source_head edcb28fa, completed, không timeout): exit 1 FINDINGS_REMAIN, flow/checker/data đều có finding, input không đổi, stderr rỗng; chưa thử PG/Flow.
- P72 · 21/10 17:47 · [GPT Pro vòng 5: máy kiểm bỏ lọt 11/11] — «Bạn đừng viết văn (phải học toán) GPT chạy bằng công cụ được tại sao bạn lại không? Thậm chí các bạn còn phải chung nhau dùng các công cụ để kiểm tra chéo lẫn nhau… Rà soát mãi mà vẫn đẻ ra 1 đống lỗi là sao?» → H4.3d: bảng chạy được + kiem-ct000-4.py, 8 lỗi thật máy bắt đã sửa.
- P71 · 21/10 16:24 · [GPT Pro phản biện vòng 4] — «Sao GPT vẫn còn nhiều ý kiến thế nhỉ? Ngoài ra tôi vẫn phải nhấn mạnh: Viết nguyên tắc không có nghĩa gì. Quan trọng là hanh động, cơ chế để không hiểu sai, không thể làm sai. Bạn rà soát chặt chẽ từng bước giúp tôi.» → H4.3c: Bảng Chuyển trạng thái + máy kiểm, 0 lỗi, 14/14 ca.
- P70 · 21/10 15:35 · [GPT Pro phản biện vòng 3] — «Bạn rà soát lại tất cả các ý kiến đó, với những điểm tiềm năng được gọi là gãy, phải đi đến cùng theo tất cả các nhánh theo tất cả các trường hợp. Phải khép kín mọi trường hợp, tệ nhất là tình trạng chui vào hàng đợi… không được để tình trạng nào kiểu mồ côi.» → H4.3b: 15/15 điểm, 3 lưới khép kín, luật 9–10.
- P69 · 21/10 15:15 · «Tóm lại GPT pro góp ý dài như vậy thì gồm những ý lớn gì? Đã được sửa thế nào? Những cái gì bạn chấp nhận và những cái gì không chấp nhận?» — «…Ưu tiên của mình là chạy trong các dịch vụ của PG trước (khai thác tối đa) để đơn giản và đáng tin cậy, sau đó có thể trồng lên 1 lớp các dịch vụ như Kubernetes… là lớp bên trên để giải quyết những bài toán chuyên biệt. Trong khi mức độ tin cậy và ổn định chính vẫn dựa vào PG. Nếu được thì hãy hướng theo kiến trúc đấy giúp tôi.» → CT-000.2 luật 7 PG gốc, 8 Lớp trên; H6.13; Chi tiết cần đạt.
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
