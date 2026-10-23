# COLLAB — nhap-directus-for-workflow
Tên việc: Vùng nháp Directus cho cỗ máy sản xuất quy trình — chỉnh nhanh trên nháp, phần đã chốt lên PG thật y như nháp

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
Xác nhận User: CHƯA XÁC NHẬN — ô 1 chép nguyên văn Owner 23/10/2026 14:37; chờ Owner gật ô 2 (đề xuất) và 6 câu ở 3.6.
Host: Claude Chat · Owner chỉ định 23/10/2026 14:37 («bạn tiếp tục làm host»).

### BẢNG ĐIỀU KHIỂN · cập nhật 2026-10-23 14:50 · Claude Host · P01
- ⚠ Mỗi lượt sửa task: sửa luôn các dòng tổng — giờ cập nhật · ✅ · ■ · ⬜ · ➡.
- 🎯 Mục tiêu: ô 1. Vì sao: chỉnh trên nháp cho nhanh; phần nào chốt thì đưa lên PG thật y như nháp, không làm lại.
- 🏁 Xong khi: ô 2 (đề xuất — chờ Owner gật).
- 📍 Tiến độ: [■ B0 Chốt mục tiêu] → [□ B1 Kiểm kê DOT + thiết kế 7 bảng] → [□ B2 Dựng nháp] → [□ B3 Nạp + chạy thử 3 nhóm] → [□ B4 Đưa phần đã chốt lên thật] (B2–B4 lặp theo từng bảng)
- ✅ Đã xong: tạo task · ô 1 nguyên văn · ô 2 + 3.1–3.6 đề xuất (P01).
- ■ Đang làm: B0 · chờ Owner gật ô 2 + 6 câu ở 3.6 · 0 RUN active
- ⬜ Còn lại: B1 → B2 → B3 → B4 (lặp).
- ➡ Kế tiếp: 😊 Owner gật/sửa ô 2 + 3.6 → Host viết kế hoạch B1 → GPT rà 1 vòng → 1 lệnh Claude Code kiểm kê (chỉ đọc, qua DOT). NEXT_TRIGGER=OWNER_GAT_O2_VA_3_6
- ⛔ Không làm: AI chạm thẳng Directus/PG (kể cả đọc) · gõ tay vào Directus · ghi vào production khi bảng chưa chốt hoặc diff chưa được duyệt · sửa MBM khi chưa xin phép · tạo tệp mới ngoài COLLAB khi Owner chưa gật.

### 1. Mục tiêu
Tình trạng: Owner viết 23/10/2026 14:37, nguyên văn, giữ lỗi gõ. Chờ Owner xác nhận.
1. Tạo task mới: work/nhap-directus-for-workflow. Dùng để thiết lập các quy trình: 1. Chế tạo cỗ máy sản xuất quy trình 2. Vận hành cỗ máy sản xuất quy trình 3. Các quy trình do cỗ máy sản xuất quy trình tạo ra.
2. Mục tiêu hoàn thiện quy trình, thiết kế và thiết lập chuẩn các khuôn UI, collection chuẩn để sau này thiết lập chuẩn trên PG=> Collections.
3. Những gì làm bây giờ là nháp => Cần xoá đi dễ dàng, nhưng thiết lập để dùng lại những thứ nháp này tối đa và nhanh nhất (nháp sau khi ok => đưa ra làm thật đúng như vậy)
4. Dùng DOT 100% với Directus (Dot đã tương đối đẩy đủ), thiếu DOT viết thêm. AI tuyệt đối không thao tác trên Directus và PG. Thiết kế để đảm bảo các DOT cũ dùng lại được (hoặc sửa thêm) dùng được cho cả nháp và production mà không cần sửa lain DOT.
Lưu ý: 1. Trong tiến trình chúng ta có thể vừa tiếp tục nháp để điều chình cho nhanh và triển khai những phần đã chốt lên PG để làm thật (2 quá trình song song).

### 2. Thế nào là hoàn thành
Đề xuất của Host — chờ Owner gật.
1. Có vùng nháp Directus chạy được, tách hẳn production. Xoá cả vùng nháp bằng 1 lệnh DOT, rồi dựng lại ra y hệt; production không đổi gì.
2. Đủ collection và khuôn UI cho 3 nhóm quy trình ở ô 1. Mỗi bảng, mỗi cột có «?». Dữ liệu nạp bằng DOT từ nguồn trên GitHub, không gõ tay.
3. Chạy thử trọn 1 vòng trên nháp: MBM sinh MMOW 007, MMOW 007 chạy trên 1 MOW, ra 1 hồ sơ đủ ký. Mỗi thông tin chỉ ghi ở 1 nhà, chỗ khác chỉ hiện lại; ghi vào chỗ không phải nhà thì bị chặn.
4. Ít nhất 1 collection đã chốt được đưa lên production y như nháp: cùng tệp khai báo, cùng DOT, chỉ khác tệp đích. Có bằng chứng nháp khớp thật và đã vào lớp bảo vệ Điều 30/31.
5. Mọi thao tác Directus và PG đi qua DOT. DOT mới hoặc sửa có hướng dẫn tại chỗ và có trong Master DOT. AI thao tác trực tiếp: 0 lần.

### 3. Chi tiết cần đạt (AI ghi, Host kiểm)

#### 3.1 Ba nhóm quy trình (ô 1 mục 1) — đề xuất, chờ Owner gật
| Nhóm | Nghĩa | Bảng nháp (7 bảng — P101 việc MMOW 07) | Sổ / nhà hiện tại |
|---|---|---|---|
| 1 Chế tạo cỗ máy | Dựng MBM: công thức + thừa số chung | Công thức · Câu hỏi (43 câu + câu riêng) | ML-DEF-021 Master Công thức · CT-000.1 trên trang `ban-duyet.html` (chưa có sổ) |
| 2 Vận hành cỗ máy | Dùng MBM sinh ra MMOW: Mục tiêu → Miền CV → Bộ câu của MMOW → câu đặc thù → hồ sơ mẫu | MMOW · Khuôn (MMOW × Câu hỏi) · Miền CV | ML-MOW-TH-001 Master MMOW · CAT-206* · CAT-250* |
| 3 Quy trình do cỗ máy tạo ra | MMOW chạy trên từng dòng của Miền CV (MOW / Task / MOIT / MOUT / Field) ⇒ mỗi dòng 1 hồ sơ | Hồ sơ · Trả lời (Hồ sơ × Câu hỏi, Check 1 · Check 2) | việc con CAT-227 · CAT-228* · ký CAT-015 |

\* = sổ chưa dựng. Cột, quan hệ, «?» của từng bảng thiết kế ở B1.
Nhà khi có 2 nơi: bảng đã có ở production (CAT-227, CAT-015, CAT-025, CAT-140) ⇒ nháp chỉ giữ bản chụp chỉ đọc do DOT chép, nhà vẫn ở production. Bảng chưa có (\*) ⇒ nháp là nhà tạm; lên thật thì thành nhà thật, HTML chỉ hiện lại.

#### 3.2 Cách dựng để «nháp ok ⇒ làm thật y như vậy» (ô 1 mục 3–4 + Lưu ý 1) — đề xuất
1. **Khai báo = dữ liệu.** Mỗi collection ghi trong 1 tệp khai báo ở thư mục task: cột · quan hệ · ô bắt buộc · «?» (= note của bảng/cột trong Directus) · khuôn UI (interface · display · layout). Tệp khai báo là nhà của thiết kế. Khớp cách dựng sổ Owner đã xác nhận 16/10 16:13 (`work/tools-quy-trinh/COLLAB.md`): thiết kế → DOT tạo collection → DOT nạp dữ liệu từ gốc GitHub → sửa gốc rồi DOT áp lại.
2. **1 DOT, 2 đích.** DOT đọc tệp khai báo + tệp đích (`--conf`). Nháp hay thật chỉ khác tệp đích; mã DOT không đổi. Mẫu đã có: `dot-stack-cutover … --mode prod --conf /opt/incomex/dot/config/stack-cutover.prod-vps1.conf`. Đích thật thêm cổng: Owner duyệt diff + POST-PROTECT (DROOT29).
3. **Nháp tách hẳn.** Directus nháp + PG nháp riêng (đúng D20 việc Graph Server: «Directus sandbox với PG riêng»), cùng phiên bản và cùng tên collection với thật ⇒ lên thật không phải đổi tên. Xoá nháp = 1 lệnh DOT; DOT từ chối lệnh xoá khi tệp đích là production.
4. **Lên thật bằng công cụ chuẩn của Directus:** schema snapshot (nháp) → diff với thật → Owner duyệt diff → apply qua DOT. Chỉ lấy bảng đã chốt (`includeCollections`), chế độ chỉ thêm (`merge`). Diff mang hash của đích: đích đổi sau khi diff ⇒ diff lại. Khác phiên bản Directus ⇒ diff từ chối; không dùng `force`. Dữ liệu: DOT nạp lại từ cùng nguồn GitHub.
5. **Song song.** Mỗi collection có 1 trạng thái trong tệp khai báo: nháp → đã chốt → đã lên thật. Bảng chưa chốt chỉnh tiếp trên nháp. Bảng đã lên thật muốn sửa thì đi lại vòng diff → duyệt → apply.
6. **Thứ snapshot không mang theo** (quyền, flow, preset/bookmark, dữ liệu): khai báo riêng trong tệp, DOT áp. Phạm vi thật đo ở B1 — CHƯA ĐO.

#### 3.3 Luật đã có — chỉ trỏ, không chép
- Root `COLLAB.md`: DROOT26 (Directus/PG chỉ qua DOT, cả lab lẫn production, kể cả đọc) · DROOT35 (DOT 100%) · DROOT27 (DOT tự mô tả: `--help`, dry-run, rollback, exit code) · DROOT29 (mã/DOT lên production phải vào bảo vệ Điều 30/31 + POST-PROTECT) · DROOT39 (chỉ danh tính máy giữ quyền quản trị).
- Lệnh giao Claude Code đụng máy chủ/production phải nhắc: làm xong kiểm lại, đưa ngay vào bảo vệ Điều 30/31.
- Hành động phá huỷ (xoá/dừng/sửa production): chỉ Owner quyết (AGENTS A2).
- Sửa MBM (CT-008): xin phép Owner trước.
- Luật «Một nhà»: CT-000.2 dòng 11 + CAT-000.5 cột «Quản lý tại».

#### 3.4 Thứ tự làm — đề xuất
- **B1 Kiểm kê + thiết kế** (chỉ đọc, qua DOT): DOT Directus/PG nào đã có, cái nào nhận `--conf` · RAM/đĩa cho Directus nháp, đặt ở VPS nào · giấy phép Directus 12 cho bản thứ 2 · snapshot/diff/apply của Directus 12.4.1 mang theo gì. Ra: bảng DOT có/thiếu + thiết kế 7 bảng (cột · quan hệ · «?»). GPT rà 1 vòng.
- **B2 Dựng nháp** (1 lệnh Claude Code): viết/nâng DOT còn thiếu → dựng Directus + PG nháp → áp tệp khai báo → thử xoá rồi dựng lại ra y hệt.
- **B3 Nạp + chạy thử:** DOT nạp từ GitHub (MBM r7.1, 43 câu, Master MMOW, Master MOW…) → 1 AI mới thiết kế MMOW 007 trên nháp → chạy trên MOW 001 → ra hồ sơ; thử chặn ghi sai nhà.
- **B4 Lên thật:** diff → Owner duyệt → apply qua DOT + POST-PROTECT → so khớp nháp = thật.
- B2–B4 lặp theo từng bảng.

#### 3.5 Đầu vào từ việc MMOW 07 (`work/mbm-qtth-07-ve-ui-mow/COLLAB.md`) — chỉ trỏ
- P101 (3.3 mục 19): 7 bảng + 4 điều kiện (a)–(d). Điều kiện (a) «tiền tố / schema riêng» nay đề xuất thay bằng Directus + PG riêng (3.2 mục 3).
- P100 (3.3 mục 18): phép thử AI mới; vướng lớn nhất = không biết ghi ở đâu.
- MBM r7.1: `work/mow-mot-moit-mout/ban-duyet.html` (CT-008). M2–M6 sửa MBM vẫn chờ gật ở việc MMOW 07.
- Lệch đã biết: Master MOW ML-DEF-004 = 35 dòng, bảng PG `workflows` = 3 dòng (3.6 câu 6).

#### 3.6 Owner cần quyết — đề xuất sẵn, gật hoặc lắc
1. Ô 2 Hoàn thành 5 dòng như trên. Đề xuất: gật.
2. Vùng nháp = Directus + PG riêng, cùng phiên bản, cùng tên collection với thật (D20). Đề xuất: gật. JEV chọn phương án này 0,95; JEV cũng báo 0,86 cần đo RAM và giấy phép trước ⇒ đo ở B1. Không đủ tài nguyên thì dự phòng: nháp nằm trong Directus thật, tên có tiền tố `nhap_`.
3. Lên thật bằng snapshot → diff → Owner duyệt diff → apply; chỉ thêm, chỉ bảng đã chốt. Đề xuất: gật.
4. Xoá trong vùng nháp: Host cho chạy theo kế hoạch đã duyệt, không hỏi từng lần; xoá ở production luôn hỏi Owner từng lần. Đề xuất: gật.
5. Hội đồng: Claude Chat Host · GPT Chat Reviewer · Claude Code CLI thợ chạy DOT. Đề xuất: gật.
6. Nguồn nạp MOW = Master MOW 35 dòng (ML-DEF-004), không lấy bảng PG `workflows` 3 dòng. Đề xuất: gật.

#### HỘI ĐỒNG — COUNCIL_BOOTSTRAP_V1
| Ghế | Hãng | Bề mặt | Vai | Gọi bằng |
|---|---|---|---|---|
| Claude | Anthropic | Claude Chat (`[auth:claude-chat]`) | Host | Owner làm việc trực tiếp |
| GPT Chat | OpenAI | GPT Chat (`openai-mcp`) | Reviewer | Owner chuyển tay |
| Claude Code | Anthropic | Claude Code CLI | Worker · chạy DOT | Owner dán 1 lệnh |
Mode=COUNCIL · Automation_Level=AUTO0 · Khác mặc định: —

### Vòng trước
- Chưa có (việc mở 23/10/2026).

## Nhật ký (nguyên văn Owner, giữ lỗi gõ)
- P01 · 23/10 14:37 · «Bạn ghi những thứ cần thiết và bạn tiếp tục làm host: 1. Tạo task mới: work/nhap-directus-for-workflow. Dùng để thiết lập các quy trình: 1. Chế tạo cỗ máy sản xuất quy trình 2. Vận hành cỗ máy sản xuất quy trình 3. Các quy trình do cỗ máy sản xuất quy trình tạo ra. 2. Mục tiêu hoàn thiện quy trình, thiết kế và thiết lập chuẩn các khuôn UI, collection chuẩn để sau này thiết lập chuẩn trên PG=> Collections. 3. Những gì làm bây giờ là nháp => Cần xoá đi dễ dàng, nhưng thiết lập để dùng lại những thứ nháp này tối đa và nhanh nhất (nháp sau khi ok => đưa ra làm thật đúng như vậy) 4. Dùng DOT 100% với Directus (Dot đã tương đối đẩy đủ), thiếu DOT viết thêm. AI tuyệt đối không thao tác trên Directus và PG. Thiết kế để đảm bảo các DOT cũ dùng lại được (hoặc sửa thêm) dùng được cho cả nháp và production mà không cần sửa lain DOT. Lưu ý: 1. Trong tiến trình chúng ta có thể vừa tiếp tục nháp để điều chình cho nhanh và triển khai những phần đã chốt lên PG để làm thật (2 quá trình song song). Làm trước task và mục tiêu => bạn viết các phần liên quan rồi tôi chỉ đạo tiếp.» → Claude Host: tạo task; ô 1 nguyên văn; ô 2 + 3.1–3.6 đề xuất. Bối cảnh: Owner 14:17 ở việc MMOW 07 (Nhật ký P101). JEV `gen-dec-1792741473-45t55tJ0vzYRd4AsGRg0` (nháp riêng 0,95 · cần đo trước 0,86). Nguồn Directus: https://directus.com/docs/tutorials/migration/promoting-changes-between-environments-in-directus. Không chạm Directus/PG.
