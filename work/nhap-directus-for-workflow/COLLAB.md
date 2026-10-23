# COLLAB — nhap-directus-for-workflow
Tên việc: Sổ + trang chủ cho cỗ máy sản xuất quy trình — làm trên vùng nháp Directus, phần đã chốt lên PG thật y như nháp

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
Xác nhận User: CHƯA XÁC NHẬN — ô 1 = lời Owner 23/10/2026 14:37 + 15:02 (chỉ sửa chính tả); chờ Owner gật ô 2 và 3.0.
Host: Claude Chat · Owner chỉ định 23/10/2026 14:37 («bạn tiếp tục làm host»).

### BẢNG ĐIỀU KHIỂN · cập nhật 2026-10-23 15:25 · Claude Host · P02
- ⚠ Mỗi lượt sửa task: sửa luôn các dòng tổng — giờ cập nhật · ✅ · ■ · ⬜ · ➡.
- 🎯 Mục tiêu: ô 1. Vì sao: mọi thứ có sổ, mỗi thông tin 1 nhà ⇒ người và máy nhìn cùng một thứ; chỉnh trên nháp cho nhanh, chốt phần nào lên thật phần đó.
- 🏁 Xong khi: ô 2 (đề xuất — chờ Owner gật).
- 📍 Tiến độ: [■ L0 Chốt khung] → [□ L1 Kiểm kê sổ + DOT] → [□ L2 Máy dựng vùng] → [□ L3 Nạp sổ nháp] → [□ L4 Trang chủ] → [□ L5 Đưa phần đã chốt lên sổ] → [□ L6 Chạy thử 3 nhóm] → [□ L7 Lên thật từng sổ]
- ✅ Đã xong: P01 tạo task · P02 ô 1 thêm mục 5–7 · lộ trình (3.1) · trang chủ (3.2) · sổ (3.3) · quy chuẩn vùng nháp (3.4) · cơ chế Một nhà (3.5).
- ■ Đang làm: L0 · chờ GPT rà P02 (1 vòng) + Owner gật 3.0 · 0 RUN active
- ⬜ Còn lại: L1 → L2 → L3 → L4 → L5 → L6 → L7 (L5–L7 lặp theo từng sổ).
- ➡ Kế tiếp: 🤖 GPT rà 3.0–3.6, ghi P03 → Host chốt → 😊 Owner gật 3.0 → 1 lệnh Claude Code cho L1 (chỉ đọc, qua DOT). NEXT_TRIGGER=GPT_RA_P02
- ⛔ Không làm: AI chạm thẳng Directus/PG (kể cả đọc) · gõ tay vào Directus (kể cả Owner) · ghi vào production khi sổ chưa chốt hoặc phần chênh chưa duyệt · trang viết riêng cho từng bảng · sửa MBM khi chưa xin phép · tạo tệp ngoài COLLAB khi Owner chưa gật.

### 1. Mục tiêu
Tình trạng: Owner viết 23/10/2026 14:37 (mục 1–4, Lưu ý) và 15:02 (mục 5–7). Chỉ sửa chính tả, giữ ý. Chờ Owner xác nhận.
1. Tạo task mới work/nhap-directus-for-workflow, dùng để thiết lập các quy trình: 1. Chế tạo cỗ máy sản xuất quy trình 2. Vận hành cỗ máy sản xuất quy trình 3. Các quy trình do cỗ máy sản xuất quy trình tạo ra.
2. Mục tiêu hoàn thiện quy trình, thiết kế và thiết lập chuẩn các khuôn UI, collection chuẩn để sau này thiết lập chuẩn trên PG => Collections.
3. Những gì làm bây giờ là nháp => cần xoá đi dễ dàng, nhưng thiết lập để dùng lại những thứ nháp này tối đa và nhanh nhất (nháp sau khi ok => đưa ra làm thật đúng như vậy).
4. Dùng DOT 100% với Directus (DOT đã tương đối đầy đủ), thiếu DOT viết thêm. AI tuyệt đối không thao tác trên Directus và PG. Thiết kế để đảm bảo các DOT cũ dùng lại được (hoặc sửa thêm) cho cả nháp và production mà không cần sửa lại DOT.
5. Trọng tâm: mọi thứ có sổ => sẽ đảm bảo được thành công.
6. Nguyên tắc đối tượng là SSOT: mỗi việc kiểm soát 1 nơi ghi gốc, chỉ cho phép ghi ở đó; những nơi khác chỉ được thiết kế đọc lại SSOT (nếu được thì khoá quyền ghi, chỉ cho phép đọc) để 1 thông tin không có 2 nguồn sự thật.
7. Người và máy có cùng tư duy: collection thiết kế thế nào => hiển thị ra đúng như vậy. Kiểm soát độ phức tạp để không trở thành đống rác tiếp theo.
Lưu ý: trong tiến trình có thể vừa tiếp tục nháp để điều chỉnh cho nhanh, vừa triển khai những phần đã chốt lên PG để làm thật (2 quá trình song song).

### 2. Thế nào là hoàn thành
Đề xuất của Host — chờ Owner gật.
1. Mọi sổ của cỗ máy có đúng 1 dòng trong Sổ của các sổ; mỗi sổ là 1 collection có «?» ở bảng và ở từng cột.
2. Vùng nháp theo đúng quy chuẩn 3.4: lọc 1 lần ra hết; xoá cả vùng bằng 1 lệnh DOT rồi dựng lại ra y hệt; production không đổi gì.
3. Trang chủ chạy trên VPS: cây bên trái, bảng bên phải, nút về trang chủ ở mọi trang, mã nào cũng bấm được; thêm 1 sổ mới không phải viết thêm dòng mã giao diện nào.
4. Mỗi thông tin chỉ ghi được ở 1 nhà; ghi vào chỗ khác bị chặn; chỗ khác chỉ hiện lại.
5. Chạy thử trọn 1 vòng trên nháp: MBM sinh MMOW 007, MMOW 007 chạy trên 1 MOW, ra 1 hồ sơ đủ ký.
6. Ít nhất 1 sổ đã chốt được đưa lên production y như nháp: cùng tệp khai báo, cùng DOT, chỉ khác vùng; đã vào lớp bảo vệ Điều 30/31.
7. Mọi thao tác Directus và PG đi qua DOT. AI thao tác trực tiếp: 0 lần.

### 3. Chi tiết cần đạt (AI ghi, Host kiểm)

#### 3.0 Owner cần quyết — đề xuất sẵn, gật hoặc lắc (P02, thay 3.6 của P01)
1. Ô 2 Hoàn thành 7 dòng. Đề xuất: gật.
2. Vùng nháp nằm ngay trong Directus/PG thật, khoanh bằng quy chuẩn 3.4 — **thay đề xuất P01 «Directus + PG riêng»**. Lý do: nháp riêng phải chép bảng thật sang ⇒ 2 nguồn, trái ô 1 mục 6; trong cùng hệ thì nháp trỏ thẳng sang bảng thật bằng mã, không chép. Cách này đã chạy thật ở web công ty (`web_incomex`) và khớp thiết kế Owner gật ở việc TQT 15/10. JEV `gen-dec-1792742987-VzYh7NFAOzmzv3GMs04u`: 1,00. Đề xuất: gật.
3. Trang chủ = 1 trang mới trong cổng Knowledge, `/knowledge/home`, khung giống Task html view (3.2). JEV 0,93. Đề xuất: gật.
4. Sổ của các sổ phía thật = `meta_catalog` đang có (trang Registries); vùng nháp có sổ riêng `nhap_so`; lên thật thì dòng chuyển sang `meta_catalog`. JEV 0,87: phải kiểm trigger, đếm, cột của `meta_catalog` trước ⇒ kiểm ở L1. Đề xuất: gật, có điều kiện L1.
5. Trang chủ công khai trên VPS, chỉ đọc, đọc bằng 1 thẻ máy chỉ-đọc; không mở quyền public của Directus. Đề xuất: gật.
6. Xoá trong vùng nháp: chạy theo kế hoạch đã duyệt, không hỏi từng lần; xoá ở production: luôn hỏi Owner từng lần. Đề xuất: gật.
7. Nguồn nạp MOW = Master MOW 35 dòng (ML-DEF-004), không lấy bảng PG `workflows` 3 dòng. Đề xuất: gật.
8. Hội đồng: Claude Chat Host · GPT Chat rà · Claude Code chạy DOT. Đề xuất: gật.
9. Trang «⌂ Master» cũ (`ui-preview/mcp-writes/master-home-v1.html`) và «Master of Master 86 mục» tĩnh: khi trang mới chạy thì trỏ sang trang mới, giữ làm lịch sử, không xoá. Đề xuất: gật.
10. Trung tâm UI / trang chủ cây (việc TQT, bước 3, Owner 16/10) và DOT `dot-master-apply` (thiết kế TQT R41–R46, chưa viết) chuyển về việc này; việc TQT ghi 1 dòng trỏ sang đây. Đề xuất: gật.

#### 3.1 Lộ trình — trọng tâm «mọi thứ có sổ» (Owner 15:02: «Roadmap thì bạn lập ra để GPT có ý kiến»)
| Bước | Làm gì | Ai | Xong khi |
|---|---|---|---|
| L0 Chốt khung | ô 1–2 · 3.0–3.6 | Host → GPT rà 1 vòng → 😊 gật 3.0 | 3.0 có câu trả lời |
| L1 Kiểm kê (chỉ đọc, qua DOT) | Kê mọi sổ đang có (`meta_catalog` · 86 mục tĩnh · 28 ML-DEF · sổ trên trang Công thức: CT, 43 câu, MMOW, Miền CV…) → bảng ánh xạ mã ↔ bí danh ↔ nơi đang ở ↔ nhà đích. Kê DOT Directus có sẵn (có / thiếu). Kiểm `meta_catalog` (trigger, đếm, cột) và tiền tố `nhap_` chưa ai dùng. Đo độ rộng cột Task html view. | 🤖 Claude Code (1 lệnh) | 2 bảng (sổ, DOT); Host + GPT rà |
| L2 Máy dựng vùng | Viết `dot-master-apply` (ap · kiem · xoa-vung) + 1 thẻ ghi (DOT) + 1 thẻ đọc (trang chủ) + bảo vệ Điều 30/31 | 🤖 Claude Code | áp → xoá vùng → áp lại = y hệt; ghi tay bị chặn; lệnh xoá bảng thật bị từ chối |
| L3 Nạp sổ nháp | Tệp khai báo 8 sổ (3.3) + dữ liệu từ GitHub → DOT áp | Host soạn tệp → 🤖 DOT | 8 sổ có dữ liệu; 0 bảng / cột thiếu «?» |
| L4 Trang chủ | Trang `/knowledge/home` theo 3.2 + nút ⌂ ở mọi trang | 🤖 Claude Code (deploy qua DOT) | mở được trên VPS, có ảnh chụp; thêm 1 sổ thử không phải sửa mã |
| L5 Đưa phần đã chốt lên sổ | Công thức (CT-000.x, CT-001…008), MBM, 43 câu, Master MMOW, Master MOW: mỗi thứ 1 nhà, mã thành link; HTML cũ chỉ hiện lại hoặc trỏ | Host + 🤖 DOT | DOT `kiem`: 0 thông tin có 2 nơi ghi |
| L6 Chạy thử 3 nhóm | 1 AI mới: MBM → MMOW 007 → MOW 001 → hồ sơ đủ ký; thử ghi sai nhà | 🤖 AI mới + GPT kiểm | ô 2 dòng 4–5 đạt |
| L7 Lên thật từng sổ | `ap <SHA> --vung that`; Owner duyệt phần chênh; POST-PROTECT; dòng sổ chuyển `nhap_so` → `meta_catalog` | 🤖 DOT + 😊 duyệt | ô 2 dòng 6 đạt |

L5–L7 lặp theo từng sổ: sổ nào chốt thì lên thật, sổ khác vẫn chỉnh trên nháp (ô 1, Lưu ý). L4 đọc được ngay sổ thật đang có, không phải chờ L3 xong hết.

#### 3.2 Trang chủ (Owner 15:02, điểm 1–3) — đề xuất thiết kế, làm cho production luôn
Owner 15:02: (1) chọn 1 nơi làm trang chủ, thiết kế cho Nháp, sau dùng lại hoặc nhân bản thành trang chủ Production · (2) thiết kế lại phần đã chốt (công thức, MBM, các danh sách) để hyperlink tối đa, luôn có nút home ở mọi chỗ; truy cập chéo phải tiện cho con người để còn chỉ đạo · (3) treeview: xem xét lấy luôn màn `knowledge/modules?task=mow-mot-moit-mout&view=content&section=detail-formula-chi-tiet-3`, cùng độ rộng cột; cột trái treeview, cột phải bảng; bảng kiểu master of master là bảng toàn link.

Đã xem 4 nơi đang có (P02):
| Nơi | Đang làm gì | Kết luận |
|---|---|---|
| `ui-preview/mcp-writes/master-home-v1.html` «⌂ Master» | HTML viết tay; đọc 86 mục chép sẵn trong `master-of-master-v1.html` | Không dùng: dữ liệu nằm trong HTML = bản chép thứ 2 |
| `/knowledge/registries` «Danh mục hệ thống» | Đọc `meta_catalog` thật; có trang chung từng loại, mã tự thành link (`AutoLinkedValue`), quan hệ tự đọc (`/api/discovery/relations`) | Dùng lại đường đọc + linh kiện; không sửa trang này |
| `/knowledge/modules` «Task html view» | Khung cột trái danh sách việc, cột phải nội dung; nội dung là tài liệu repo | Lấy khung và độ rộng cột |
| Directus Studio | Đúng khai báo, nhưng phải đăng nhập, đầu cột không có «?» | Để máy dùng |

Thiết kế:
- T1 Địa chỉ `/knowledge/home`. Nút ⌂ đặt ở 2 chỗ chung: thanh menu Nuxt (mọi trang Nuxt) và `eco-nav.js` (thanh 4 Mẹ của các trang tĩnh) ⇒ trang nào cũng về được trang chủ.
- T2 Khung: giữ thanh menu trên; cột trái rộng bằng cột danh sách việc của Task html view (ảnh 1440px: khoảng 320px, đo đúng ở L1); cột phải là phần còn lại. Nền trắng, chữ tối, chữ to.
- T3 Cột trái — cây: ⌂ Sổ của các sổ → nhóm (3.4 V3 + nhóm của `meta_catalog`) → từng sổ (số dòng, nhãn 🟡 Nháp / 🟢 Thật) → dòng con nếu sổ có quan hệ cha–con.
- T4 Cột phải — bảng: cột lấy đúng khai báo collection (thứ tự · tên hiện · «?» = ghi chú cột); ô mã, ô quan hệ là link; bấm 1 dòng ⇒ chi tiết dòng + «nơi đang dùng». Chọn gốc ⇒ bảng Sổ của các sổ, ô nào cũng là link.
- T5 Địa chỉ giữ chỗ đang xem: `?so=<mã>&dong=<mã>&vung=nhap|that` ⇒ gửi link là mở đúng chỗ. Nháp và thật là cùng 1 trang, khác tham số vùng: không cần nhân bản.
- T6 Chỉ đọc. Sửa = sửa tệp GitHub ⇒ DOT áp. Đọc bằng 1 thẻ máy chỉ-đọc (một thẻ · hai cổng).
- T7 Luật «khai báo = hiển thị» (ô 1 mục 7): 1 bộ hiển thị chung cho mọi sổ, không trang riêng · chữ trên màn chỉ lấy từ khai báo · thiếu gì ⇒ bổ sung khai báo, không viết cứng · trình bày đặc biệt (ma trận màu, thẻ công thức) ⇒ khai thành 1 sổ dạng «khung nhìn», cũng có «?». Màn nào không làm được theo T7 ⇒ ghi nợ, không viết trang riêng.
- T8 Dùng lại cái đã có: đường đọc `$directus` + `/api/discovery/relations` + `AutoLinkedValue` · `SectionFields` · `SectionRelation` (Nuxt Registries). Không thêm gói, không đổi phiên bản.

Ý kiến Host về ô 1 mục 7 (Owner hỏi có khả thi không): khả thi, và đó là chuẩn ngành — giao diện sinh từ khai báo (Directus Studio, Django admin làm như vậy). Lợi lớn nhất: thêm 1 sổ = 0 dòng mã giao diện ⇒ chặn đống rác. Giới hạn nói trước: phần trình bày đặc biệt (ma trận màu, thẻ công thức kiểu CT-000.4) không tự sinh từ bảng thường ⇒ khai thành sổ khung nhìn (T7).

#### 3.3 Các sổ của 3 nhóm quy trình (ô 1 mục 1, mục 5)
| Nhóm | Nghĩa | Sổ nháp (tên máy) | Nhà / nơi đang ở |
|---|---|---|---|
| 0 Sổ | Sổ của các sổ (vùng nháp) | `nhap_so` | thật: `meta_catalog` (CAT-xxx) · tĩnh: master-of-master 86 mục, ML-DEF 28 mục |
| 1 Chế tạo cỗ máy | Dựng MBM: công thức + thừa số chung | `nhap_cong_thuc` · `nhap_cau_hoi` | ML-DEF-021 Master Công thức · CT-000.1 trên `ban-duyet.html` (chưa có sổ) |
| 2 Vận hành cỗ máy | Dùng MBM sinh ra MMOW: Mục tiêu → Miền CV → Bộ câu của MMOW → câu đặc thù → hồ sơ mẫu | `nhap_mmow` · `nhap_khuon` (MMOW × câu) · `nhap_mien_cv` | ML-MOW-TH-001 Master MMOW · CAT-206* · CAT-250* |
| 3 Quy trình do cỗ máy tạo ra | MMOW chạy trên từng dòng Miền CV (MOW / Task / MOIT / MOUT / Field) ⇒ mỗi dòng 1 hồ sơ | `nhap_ho_so` · `nhap_tra_loi` (hồ sơ × câu, Check 1 · Check 2) | việc con CAT-227 · CAT-228* · ký CAT-015 |

\* = chưa có sổ. Cột và quan hệ chi tiết làm ở L1. Bảng đã có ở production (CAT-227, CAT-015, CAT-025, CAT-140): nháp trỏ sang bằng mã, chỉ đọc, không chép (3.4 V6).

#### 3.4 Quy chuẩn vùng nháp (Owner 15:02: «tất cả collection trong vùng này bắt buộc theo 1 quy chuẩn ⇒ lọc 1 cái là ra hết, không lẫn lộn»)
Dùng lại thiết kế Owner đã gật ở việc TQT (R41–R46, 15/10 16:21 + 21:39: «vùng nháp chỉ là cấu hình»), đổi tiền tố thành tiền tố chung.
- V1 Tiền tố: mọi collection vùng nháp có tên bắt đầu `nhap_`. Lọc `nhap_*` = ra hết. L1 kiểm: chưa collection nào đang dùng tiền tố này.
- V2 Phần sau tiền tố = tên thật khi lên production: `nhap_cong_thuc` ⇒ `cong_thuc`. Chữ thường, không dấu, nối `_` (khớp cách TQT đặt `ma`, `ten`).
- V3 Nhóm Directus: thư mục «NHÁP» → «0 Sổ» · «1 Chế tạo cỗ máy» · «2 Vận hành cỗ máy» · «3 Quy trình tạo ra». Cây trang chủ đọc đúng các nhóm này.
- V4 Ghi chú bảng bắt đầu `[NHAP]`, tiếp theo là «?» của bảng. Mỗi cột có ghi chú = «?» của cột.
- V5 Mỗi bảng có cột `ma` (khoá chính, chuỗi, ổn định) và `ten`. Quan hệ nối bằng `ma`.
- V6 Nối sang bảng thật: chỉ bằng mã, chỉ đọc, không khoá ngoại; bảng thật không bao giờ trỏ vào nháp ⇒ xoá vùng không làm gãy bảng thật.
- V7 Người ghi duy nhất: 1 DOT `dot-master-apply` đọc tệp khai báo trên GitHub đúng 1 commit. Vùng khai trong `vung.json` (tiền tố · nhóm · nhãn · xoá được). Nháp ⇒ thật = đổi `--vung`, mã DOT không đổi. Mẫu đã có: DOT nhận `--mode prod --conf …` (`dot-stack-cutover`).
- V8 DOT chỉ xoá được thứ có trong sổ sở hữu của vùng và mang tiền tố nằm trong danh sách viết cứng trong mã (`nhap_`); sửa tệp khai báo không mở được quyền xoá bảng thật.
- V9 `kiem` báo đỏ khi: sai tiền tố / nhóm / nhãn · khoá ngoại ra ngoài vùng · Flow hoặc trigger trên bảng nháp · quyền public · thẻ ghi khác DOT.
- V10 Tệp khai báo đặt ở `work/nhap-directus-for-workflow/khai-bao/` — chỉ tạo ở L2 sau khi Owner gật.

#### 3.5 Cơ chế Một nhà (ô 1 mục 6)
- N1 Nhà: mỗi thông tin (cột) có đúng 1 collection nhà, ghi ở Sổ của các sổ / Master Field, cột «Quản lý tại» (luật CT-000.2 dòng 11, CAT-000.5).
- N2 Cổng ghi: quyền Directus — chỉ thẻ chủ nhà được ghi collection đó; mọi thẻ khác chỉ đọc. Vùng nháp: chỉ thẻ DOT ghi. Mô hình «một thẻ · hai cổng»: mỗi tác nhân 1 thẻ, cổng đặt đúng ở chỗ ghi; không dựng thêm lớp chặn khác.
- N3 Nơi khác chỉ hiện lại qua quan hệ (link, hiển thị liên kết), không có cột chép.
- N4 Bắt lỗi: DOT `kiem` đếm cột cùng nghĩa ở 2 bảng mà không qua quan hệ ⇒ đỏ; L5 xong khi số này = 0.

#### 3.6 Luật đã có — chỉ trỏ, không chép
- Root `COLLAB.md`: DROOT26 (Directus/PG chỉ qua DOT, cả lab lẫn production, kể cả đọc) · DROOT35 (DOT 100%) · DROOT27 (DOT tự mô tả: `--help`, dry-run, rollback, exit code) · DROOT29 (mã/DOT lên production phải vào bảo vệ Điều 30/31 + POST-PROTECT) · DROOT39 (chỉ danh tính máy giữ quyền quản trị).
- Lệnh giao Claude Code đụng máy chủ/production phải nhắc: làm xong kiểm lại, đưa ngay vào bảo vệ Điều 30/31.
- Hành động phá huỷ (xoá/dừng/sửa production): chỉ Owner quyết (AGENTS A2).
- Sửa MBM (CT-008): xin phép Owner trước.
- Đầu vào từ việc MMOW 07 (`work/mbm-qtth-07-ve-ui-mow/COLLAB.md`): P101 (3.3 mục 19) 7 bảng + 4 điều kiện — điều kiện (a) nay theo 3.4 · P100 (3.3 mục 18) phép thử AI mới, vướng lớn nhất = không biết ghi ở đâu · MBM r7.1 ở `work/mow-mot-moit-mout/ban-duyet.html`; M2–M6 vẫn chờ gật ở việc đó · lệch đã biết: Master MOW ML-DEF-004 = 35 dòng, bảng PG `workflows` = 3 dòng.

#### HỘI ĐỒNG — COUNCIL_BOOTSTRAP_V1
| Ghế | Hãng | Bề mặt | Vai | Gọi bằng |
|---|---|---|---|---|
| Claude | Anthropic | Claude Chat (`[auth:claude-chat]`) | Host | Owner làm việc trực tiếp |
| GPT Chat | OpenAI | GPT Chat (`openai-mcp`) | Reviewer | Owner chuyển tay |
| Claude Code | Anthropic | Claude Code CLI | Worker · chạy DOT | Owner dán 1 lệnh |
Mode=COUNCIL · Automation_Level=AUTO0 · Khác mặc định: —

### Vòng trước
- P01 (23/10 14:50): ô 2 bản 5 dòng (chưa gật) — thay bằng 7 dòng ở P02. Đề xuất P01 «nháp = Directus + PG riêng, lên thật bằng schema snapshot → diff → apply» — thay bằng 3.0 câu 2 + 3.4 (lý do ở 3.0 câu 2).

### P03 · 23/10/2026 · GPT Chat Reviewer · L0 · vòng 1/1 · Based_on P02 / commit `1b1920bd`
**Kết luận:** ĐỒNG THUẬN hướng dùng Directus/PG hiện hữu, tiền tố `nhap_`, trang chủ dùng chung `/knowledge/home`, tái sử dụng `meta_catalog` và trang Registries. **Đề nghị Owner gật có điều kiện, chưa READY/RUN** vì mục tiêu/ô 2 và mục 3.0 vẫn CHƯA XÁC NHẬN. Chỉ sửa 5 điểm ngắn trong thiết kế, không lập nhánh việc mới:
1. **L0/SSOT:** nháp là đề xuất chưa ban hành; không phải nguồn thật thứ hai. Một sự thật được xác định theo **đối tượng + thuộc tính**, không căn cứ trùng tên cột (nhiều sổ có `ma`, `ten` hợp lệ). Master Field ghi nhà nguồn; bảng khác trỏ mã/quan hệ và chỉ đọc. L1 chỉ ánh xạ ba danh mục 86 tĩnh/28 ML-DEF/`meta_catalog`, chưa gộp/xóa vì có thể khác chức năng.
2. **Nháp chung DB:** `nhap_` + thư mục NHÁP chỉ để nhận diện, không phải cách ly quyền. DOT của vùng nháp cần thẻ/role chỉ ghi các collection được phép; quyền production chỉ đọc, không sửa schema/bảng/Flow/trigger production. Kiểm cả quyền thực tế, không chỉ so tiền tố. Lên thật từng sổ là thao tác riêng cần Owner duyệt và theo Điều 30/31; không chỉ đổi `--vung` là đủ.
3. **Giảm việc trước mắt:** đưa L4 **bản trang chủ tối thiểu + 1 sổ mẫu** ngay sau L1 và bộ khai báo tối thiểu L2; không chờ nạp đủ 8 sổ mới xem được. Dùng lại `/knowledge/registries`, `AutoLinkedValue`, `/knowledge/modules` và DOT đã có; chỉ bổ sung DOT cần thiết nếu kiểm kê L1 xác nhận thiếu. Không ưu tiên làm `xoa-vung`/rollback tổng quát trước khi có sổ mẫu xem được; xóa vùng chỉ theo danh sách sở hữu và kế hoạch Owner duyệt, mặc định không xóa.
4. **Trang chủ:** một renderer chung đọc metadata Directus và quan hệ; `?` dùng ghi chú cột/bảng; cây trái, bảng phải, các link và nút ⌂. Không hứa màn đặc biệt tự có đủ chức năng chỉ từ bảng; phần đặc biệt xử lý sau khi sổ mẫu chứng minh cần. Trang public chỉ xuất dữ liệu đã cho phép công khai; thẻ đọc phải giữ phía server, không chuyển vào trình duyệt hay mở quyền public Directus.
5. **Quy chuẩn:** `nhap_` giữ làm bộ lọc, nhưng `ma` nên là mã nghiệp vụ ổn định/unique, **không buộc là khóa chính vật lý** nếu collection hiện hữu có `id`/UUID. Trước khi nhân hàng loạt, thử một thao tác thiết kế collection → trang chủ hiển thị đúng cột/ghi chú/link → ghi dữ liệu nháp đúng nhà → kiểm từ chối ghi production bằng quyền nháp.
**Chốt 5.1–5.4:** gật có điều kiện như trên; ưu tiên `/knowledge/home`, giữ URL cũ và sử dụng `meta_catalog` sau L1. Bám L0–L7 nhưng thực hiện theo vòng nhỏ: **kiểm kê → trang chủ + một sổ mẫu → dùng thử → mở rộng sổ → duyệt lên thật**. Không thay mục tiêu Owner, không trực tiếp chạm Directus/PG, không tạo file/schema/DOT ở lượt phản biện này.

## Nhật ký (lời Owner — chỉ sửa chính tả)
- P02 · 23/10 15:02 · «Rồi, cần 1 roadmap cho kế hoạch này. Lưu ý là trọng tâm là mọi thứ có "sổ" => sẽ đảm bảo được thành công. Đưa ra ngoài mục tiêu: Nguyên tắc đối tượng là SSOT. Mỗi việc cần kiểm soát 1 nơi ghi gốc, chỉ cho phép ghi ở đó, những nơi khác chỉ được thiết kế đọc thông tin lại SSOT (nếu được thì khoá quyền ghi lại, chỉ cho phép đọc SSOT) để đảm bảo 1 thông tin không có 2 nguồn sự thật. Để con người và máy móc có cùng tư duy, các collection thiết kế thế nào => hiển thị ra đúng như vậy (bạn có ý kiến thêm xem có khả thi không, nhưng đó là cách nhanh nhất để đồng bộ hoá suy nghĩ giữa người và máy); tôi cần kiểm soát sự phức tạp của các bạn để tránh lại trở thành đống rác tiếp theo. Roadmap thì bạn lập ra để GPT có ý kiến. Tôi đề nghị mấy điểm: 1. Cần chọn 1 nơi làm trang chủ. Thiết kế trang chủ cho Nháp (sau này có thể dùng lại hoặc chỉ cần nhân bản là thành trang chủ Production). 2. Thiết kế lại các phần chúng ta đã chốt: các công thức, MBM, các danh sách để làm sao hyperlink tối đa với nhau và luôn có nút home ở bất kỳ chỗ nào. Việc truy cập chéo đầu tiên cần trở nên tiện lợi với con người để còn chỉ đạo. 3. Thiết kế hệ thống treeview => có thể xem xét lấy luôn màn hình https://vps.incomexsaigoncorp.vn/knowledge/modules?task=mow-mot-moit-mout&view=content&section=detail-formula-chi-tiet-3 với cùng độ rộng của cột. Cột trái làm treeview và cột phải là bảng. Các bảng kiểu master of master nên là một bảng toàn link. Giờ chọn trang chủ và chúng ta bắt đầu thiết kế nhé. Thiết kế để cho production luôn. Một điều quan trọng: bạn chưa quy chuẩn vùng Nháp trong task để cho nhất quán. Tất cả mọi collection trong vùng này bắt buộc phải theo 1 quy chuẩn => để lọc 1 cái là ra hết và không bị lẫn lộn.» → Claude Host: ô 1 thêm mục 5–7; 3.0–3.6 mới (lộ trình L0–L7, trang chủ T1–T8, sổ, quy chuẩn V1–V10, Một nhà N1–N4); đổi đề xuất nháp riêng ⇒ nháp trong hệ thật (JEV `gen-dec-1792742987-VzYh7NFAOzmzv3GMs04u`: nháp trong hệ 1,00 · trang Nuxt chung 0,93 · rủi ro `meta_catalog` 0,87). Đã xem thật: `/knowledge/registries`, `/knowledge/modules`, `master-home-v1.html`, mã Nuxt Registries. Không chạm Directus/PG.
- P01 · 23/10 14:37 · «Bạn ghi những thứ cần thiết và bạn tiếp tục làm host: 1. Tạo task mới: work/nhap-directus-for-workflow. Dùng để thiết lập các quy trình: 1. Chế tạo cỗ máy sản xuất quy trình 2. Vận hành cỗ máy sản xuất quy trình 3. Các quy trình do cỗ máy sản xuất quy trình tạo ra. 2. Mục tiêu hoàn thiện quy trình, thiết kế và thiết lập chuẩn các khuôn UI, collection chuẩn để sau này thiết lập chuẩn trên PG=> Collections. 3. Những gì làm bây giờ là nháp => Cần xoá đi dễ dàng, nhưng thiết lập để dùng lại những thứ nháp này tối đa và nhanh nhất (nháp sau khi ok => đưa ra làm thật đúng như vậy) 4. Dùng DOT 100% với Directus (DOT đã tương đối đầy đủ), thiếu DOT viết thêm. AI tuyệt đối không thao tác trên Directus và PG. Thiết kế để đảm bảo các DOT cũ dùng lại được (hoặc sửa thêm) dùng được cho cả nháp và production mà không cần sửa lại DOT. Lưu ý: 1. Trong tiến trình chúng ta có thể vừa tiếp tục nháp để điều chỉnh cho nhanh và triển khai những phần đã chốt lên PG để làm thật (2 quá trình song song). Làm trước task và mục tiêu => bạn viết các phần liên quan rồi tôi chỉ đạo tiếp.» → Claude Host: tạo task; ô 1; ô 2 + đề xuất. JEV `gen-dec-1792741473-45t55tJ0vzYRd4AsGRg0`. Không chạm Directus/PG.
