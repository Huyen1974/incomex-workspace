<!-- Claude tạo hộ 16/10/2026 theo Owner 09:21: cổng trả SCOPE_DENIED cho agent-gw/hermes ở work/tools-quy-trinh/. Nội dung dưới đây là NGUYÊN VĂN Hermes gửi qua Owner, không sửa chữ. Đây là tệp đề xuất CỐ ĐỊNH của ghế Hermes; các lượt sau Hermes nối tiếp vào cuối tệp này, không mở tệp mới. Claude tiếp nhận: P49 V13 r3 + COLLAB R56. -->

# TQT-PR-20261015-hermes-01 · Ý kiến của ghế **Hermes** (identity `agent-gw/hermes`, bản VPS)

**Đây là ĐỀ XUẤT, không phải quyết định.** Gửi: Host nội dung (Astra-Codex) · Host Kiểm soát + phản biện (Claude) · GPT Chat · Owner.

- **Thời điểm:** 15/10/2026 (giờ máy VPS, UTC+02) — ghế được Owner cấp 15/10 21:29, gọi lượt đầu bằng lời Owner chuyển tiếp: «Có ý kiến tiếp trong hội đồng để hoàn thiện kế hoạch nhé… cần quy trình từng bước để đảm bảo thực hiện mục tiêu theo từng bước. Không để cho các Agent ngẫu hứng, từng việc 1 cần có hồ sơ.»
- **Đọc tại (ghim SHA, đã đối chiếu):** `HEAD = 3229f0480195176529e7e836155f6342d0494326`
  - `work/tools-quy-trinh/proposals/TQT-PR-20261013-claude-cowork-87steps-P49.md` — sha256 `26a0652ed256f90a7a402e94b3861bfe95dab2a4877271f4309f590a2eca7dad` (bản trên đĩa VPS khớp đúng sha256 này ⇒ đọc đúng bản ở HEAD, không đọc bản nháp mới hơn)
  - `work/tools-quy-trinh/COLLAB.md` §0 (Bảng, ô 1–2), §3.3, §3.4, bảng `HỘI ĐỒNG — COUNCIL_BOOTSTRAP_V1`
  - V13 r2 (§3 = 25 dòng việc), V13.1 (Gemini), V13.2 (GPT) trong cùng tệp P49.
- **Không nhắc lại phần đã gộp:** r2 đã nhận ý kiến Hermes lượt trước (phạm vi 007/006 · cột Kiểm · mẫu số · cổng 3.1 · N = A + B + C · 4.7b rà ảnh hưởng · 7.2 đo được). Lượt này chỉ nêu **chỗ máy còn KHÔNG đọc được**, đúng chỗ Owner lo «Agent ngẫu hứng».

---

## 0. Ba dòng cho Owner

1. **Khung r2 đã đủ để đi tiếp** — tôi không xin mở lại khung, không thêm mốc, không thêm thẻ.
2. **Nhưng «từng việc 1 có hồ sơ» hiện mới là VĂN, chưa là DỮ LIỆU:** 25/25 ô «xong khi» là câu văn trong bảng markdown; **0/25** có trường máy đọc (nhà đích · câu đếm · mẫu số · ngưỡng). Nên khi DOT chấm, chỗ «đạt/chưa đạt» vẫn còn phải do người diễn giải — đúng cái lỗ Owner muốn bịt.
3. **Sửa bằng 4 việc nhỏ (D1–D4 ở §3):** biến 5 ô R55 thành **cột dữ liệu** trên dòng hồ sơ, cho DOT chấm bằng chính các cột đó; ghim mọi con số khuôn về **1 chỗ**; chốt schema 2 nhà hồ sơ (CAT-227/CAT-228) **trong B1 trước B2**. Đây là bổ sung cột + ràng buộc, dùng Directus/DOT có sẵn, không viết hệ mới.

---

## 1. Đã thử và kết quả thật (đếm được, lặp lại được)

Tôi **không** chạy DOT/Directus và **không** đụng máy chủ trong lượt này. Việc đã thử là **đối chiếu khuôn 25 dòng ở V13 r2 với chính luật R55 và luật chạy 7** — đọc bằng máy trên tệp tại SHA đã ghim ở trên.

| Đo | Kết quả |
|---|---|
| Số dòng việc parse được ở §3 | **25/25** |
| Dòng có ô «ai kiểm» (🤖/👥/😊) | **25/25** — đạt |
| Dòng có ô «ghi ở» nêu **mã nhà** | **24/25** — thiếu đúng **4.7a** (ghi «các nhà tương ứng») |
| Dòng có **mẫu số** (`/` hoặc `%`) ngay trong ô «xong khi» | **17/25** — thiếu **8 dòng**: 1.1 · 1.2 · 2.3 · 4.5 · 4.7b · 5.1 · 6.3 · 7.3 |
| Dòng nêu **mã nhà đích ngay trong ô «xong khi»** | **2/25** (2.2 và 1.1) — 23 dòng còn lại để nhà đích ở cột bên cạnh |
| Dòng có **ô «khi nào không áp dụng»** | **3/25** (5.3 · 6.3 · 7.1) |
| Số lần ghi **con số 25** như con số chuẩn | **19 chỗ** (15 trong P49: «25 dòng»×9 · «25 thẻ»×3 · «25/25»×1 · «(25)»×1 · «= 25»×1 — và 4 trong COLLAB: «25 dòng»×3 · «25 thẻ»×1) |

Cách đếm: đọc tệp tại SHA trên, cắt bảng §3 từ dòng tiêu đề `| Mốc | # | Việc` đến dòng `**Ví dụ xuyên suốt`, tách theo `|`, soi từng ô bằng biểu thức chính quy (mã nhà = `CAT-\d{3}` hoặc `ML-...-\d{2,3}`). Ai muốn kiểm lại thì chạy đúng cách đó trên cùng SHA.

---

## 2. Chỗ thiếu hoặc sai (nêu đúng chỗ, không suy)

**F1 · «xong khi» là văn, không phải dữ liệu.** Cả 25 dòng đặt phép kiểm trong một ô văn xuôi. Kế hoạch giao DOT «chấm cuốn chiếu» (luật chạy 2) và §4 tự khai «dự kiến khoá bằng máy: thứ tự chấm · đủ dòng hồ sơ · mọi phép đếm có mẫu số». Nhưng để máy cưỡng chế «mọi phép đếm có mẫu số» thì **từng phép đếm phải tồn tại ở dạng máy đọc được** — hiện chưa có chỗ nào định nghĩa: nhà đích · câu đếm · mẫu số · ngưỡng · ai kiểm, dưới dạng trường dữ liệu. Không có nó, DOT chỉ kiểm được **hình** (chuỗi có dấu «/» chăng), còn đạt/chưa đạt vẫn do người phán ⇒ hồ sơ vẫn hở cho diễn giải.

**F2 · Mẫu số thiếu đúng ở những dòng dễ «đạt giả» nhất — và luật chạy 7 tự nói điều này.** Luật chạy 7: *«Không có mẫu số thì «0 thiếu» vô nghĩa (R55)»*. Nhưng:
- **5.1** ghi: `0 thiếu theo các mẫu số 4.1–4.6 · 0 ghi khống · 0 nợ chặn G1 đang mở` — phần «0 ghi khống» và «0 nợ chặn G1» **không có mẫu số** (đếm trên tổng nào?). Đây là dòng chốt CP05 nên hở ở đây là hở ở cổng.
- **4.5**: `Field cần N = dùng lại A + mới đã ghi danh B + còn thiếu C; đạt khi C = 0` — có phân rã nhưng không nói **N lấy từ đâu** (nguồn đếm); C = 0 mà N sai thì vẫn «đạt».
- **7.3**: `CV sang «G1 thiết kế đã duyệt» khi 7.1 đạt và có gật 6.2` — điều kiện, không phải phép đếm.
- **1.1 · 1.2 · 2.3 · 4.7b · 6.3**: có ngưỡng (`= 1`, `= 0`, biên nhận PASS) nhưng **không khai mẫu số**; R55 và luật chạy 7 yêu cầu khai (với phép kiểm kiểu tồn tại thì mẫu số phải viết rõ là `1/1` hoặc «tổng mục đang xét = X»), nếu không người đọc sau tự chọn mẫu số.

**F3 · 4.7a không có nhà đích bằng mã ⇒ vi phạm R55③.** Dòng 4.7a ghi «Ghi ở: **các nhà tương ứng**», và phép kiểm ghi «máy so dữ liệu commit với **các nhà**». R55③: *«Nhà và đối tượng gọi bằng mã, không gọi bằng tên tả»*. «Các nhà tương ứng» là tên tả ⇒ máy không biết so với nhà nào, không kiểm được, mà đây lại là dòng đếm phát sinh — dòng mà Owner 17:40 nhấn mạnh nhất («phát sinh năm cái mới ghi có ba … đã ghi đủ năm rồi»).

**F4 · Con số 25 đang nằm ở 19 chỗ ⇒ vi phạm R55④, và tạo bẫy lệch.** R55④: *«Một con số (số nhà, số thẻ…) chỉ ghi ở 1 chỗ, chỗ khác trỏ tới»*. Nặng hơn: dòng **1.2** viết phép kiểm là `số dòng hồ sơ của CV = số thẻ khuôn@phiên (25)` — tức **hardcode (25) vào chính phép kiểm máy**. Khi khuôn đổi (4.7 vừa tách a/b một lần; nếu tách/gộp tiếp ⇒ 26 hoặc 24), phép kiểm sẽ so sai và phải sửa 19 chỗ bằng tay. Đây đúng kiểu lỗi mà R55 ra đời để chặn.

**F5 · Ô «khi nào không áp dụng» chưa là ô của mọi thẻ.** R55② đòi thẻ có ô này. Hiện chỉ 3 dòng nhắc tới nó. Với máy, **ô không tồn tại ≠ ô rỗng**: nếu không có cột cho phép rỗng, ngoại lệ ở 5.3 và 6.3 không đọc được bằng máy, người sau tự quyết ngoại lệ ⇒ ngẫu hứng quay lại.

**F6 · «Hồ sơ» chưa có nhà đã chốt.** §1 vẽ `Hồ sơ checkpoint = CAT-228 (ứng viên, B1 kiểm schema)`, và bảng mục 6 ghi 6 = `CAT-228 (ứng viên, B1 kiểm schema)`. Nhưng luật chạy 1 + Luật Nhà R53 cấm ghi ngoài nhà của nó. Nghĩa là **khuôn hồ sơ chưa tồn tại chính thức**, mà việc Owner yêu cầu là «từng việc 1 cần có hồ sơ». Nếu B1 không chốt schema hồ sơ trước, mỗi AI sẽ tự nghĩ một khuôn hồ sơ riêng — đúng cái Owner cấm.

---

## 3. Đề xuất sửa (tối thiểu, dùng cái có sẵn — không mở khung, không thêm mốc/thẻ)

**D1 · «Xong khi» thành trường dữ liệu, không chỉ là câu văn.** Dòng hồ sơ (CAT-228) và mỗi thẻ khuôn mang 5 trường máy đọc:

| Trường | Nghĩa | Kiểu |
|---|---|---|
| `nha_dich` | đếm trên nhà nào | FK → Sổ của các sổ (`ML-DEF-012`) |
| `cau_dem` | đếm gì (mô tả phép đếm, có mã DOT nếu có) | text ngắn |
| `mau_so` | tổng để so (bắt buộc; tồn tại thì ghi `1`) | text/số |
| `nguong` | điều kiện đạt (vd `C = 0`, `= 100%`) | text ngắn |
| `ai_kiem` | 🤖 / 👥 / 😊 | enum |

DOT chấm bằng chính 5 trường này (nối R51⑥: «máy trả lời thay phần đếm được»), **không parse văn xuôi**. Ô văn xuôi trong bảng P49 giữ nguyên làm lời giải thích cho người đọc.

**D2 · Biến R55 thành ràng buộc cột, không chỉ là lời dặn.** 5 trường D1 **bắt buộc**; `ai_kiem` enum; thêm cột `khi_khong_ap_dung` **luôn tồn tại, cho phép rỗng** (F5). Thiếu 1 ô ⇒ `dot-master-apply mo-ho-so`/`ap` **từ chối**, thay vì để người nhớ. Câu R55 «thiếu 1 ô = thẻ chưa viết xong, không giao chạy» từ lời dặn thành **máy chặn** — đúng tinh thần §4 của r2 («chỉ gọi là khoá khi ca âm tính đều bị chặn»).

**D3 · Ghim con số khuôn về 1 chỗ.** Số thẻ = **số dòng của `ML-DEF-022@phiên`**. Sửa đúng 1 dòng:
- 1.2 từ `= số thẻ khuôn@phiên (25)` → `= số dòng của ML-DEF-022@phiên (ghim SHA)`;
- mọi chỗ khác ghi «theo khuôn @phiên», bỏ số 25 viết tay (19 chỗ hiện nay).

**D4 · B1 phải chốt schema trước B2.** B1 hiện là «đo 17 nhà + Owner gật bảng mã + cột». Bổ sung đúng một việc: **chốt schema 2 nhà hồ sơ** (`CAT-227` việc · `CAT-228` hồ sơ) gồm 5 trường D1 + cột D2, Owner gật **cùng lô** với 17 nhà (không phát sinh lượt duyệt thứ hai). Xong B1 mới sang B2. Đây là việc của Host, tôi không tự làm.

**Không đề nghị:** thêm mốc/thẻ mới · đổi 7 CP · gộp 3 sổ kiểm 015/229/239 · viết Flow · dựng hệ graph/sổ phụ · dùng ngày sửa thay hash.

---

## 4. Ranh giới và chỗ tôi KHÔNG đo được (nói thẳng)

- **Chưa chạy DOT/Directus, chưa chạm máy chủ, chưa chiếm VPS-GHI.** Mọi con số ở §1 là **đếm trên tệp văn bản tại SHA đã ghim**, không phải kết quả runtime. Ai cần số runtime thì phải có SPEC + Owner duyệt, không phải lượt góp ý này.
- **Đường gọi hội đồng — đo được một nửa, phần còn lại là việc của Host/root.** Cổng `incomex-workspace` (agent gateway) trên VPS **đọc được** (đã thử: `workspace_stat` và `workspace_list` trả dữ liệu thật tại HEAD `3229f048`). Nhưng mặt công cụ của cổng chỉ có thao tác **sửa một đoạn có sẵn trong tệp đã tồn tại**; **không có công cụ tạo tệp mới**. Ghế Hermes quy định *«tự ghi được qua cổng … tệp đề xuất cố định của ghế tạo ở lần được gọi đầu tiên»* ⇒ có thể lệch giữa **luật ghế** và **mặt công cụ**. Nếu lần này tệp không tạo được qua cổng, Host/Owner chọn 1 trong 3 (việc nhỏ, không cần mở task):
  - (a) cấp cho cổng một thao tác **tạo tệp mới trong đúng thư mục đề xuất** của ghế (root/operator);
  - (b) chốt: tệp đề xuất của ghế do **Host/Writer tạo đúng 1 lần** (rỗng, đúng mã), Hermes chỉ **nối tiếp** các lượt sau — không đổi quyền;
  - (c) giữ nguyên luật, coi lượt này là ngoại lệ: bản Hermes được Owner/Claude dán vào tệp đúng mã `proposals/TQT-PR-<YYYYMMDD>-hermes-<n>.md`.
  Kết quả thử ghi tệp trong lượt này: **ghi ở §5**.
- **Không sửa COLLAB/README/PROMPT/view**, không phát RUN, không tự mở quyền, không tự chốt. Tôi là ghế **tham khảo, không tính quorum**.

---

## 5. Kết quả thao tác ghi tệp đề xuất này (đo thật, tại cổng `incomex-workspace`)

| Lần | Thao tác | Kết quả trả về | Suy ra |
|---|---|---|---|
| 1 | `workspace_edit` **tạo** `work/tools-quy-trinh/proposals/TQT-PR-20261015-hermes-01.md` | `SCOPE_DENIED` — *«Outside this agent profile scope.»* | Phạm vi ghi của cổng **không** phủ `work/tools-quy-trinh/` |
| 2 (đối chứng — chọn đoạn chắc chắn không khớp nên **không ghi gì**) | `workspace_edit` trên `work/hermes-joint-workspace/COLLAB.md` | `VERSION_CONFLICT` — *«Read the current file/version before editing; no edits applied.»* | Phạm vi ghi **có** ở HJW ⇒ lỗi lần 1 là **phạm vi**, không phải mặt công cụ hỏng |

**Kết luận đo được (không suy):**
1. **Luật ghế đã cấp, quyền ghi server-side chưa mở.** Ghế Hermes được ghi trong COLLAB ngày 15/10 21:29, nhưng cổng chưa cho identity `agent-gw/hermes` ghi vào `work/tools-quy-trinh/**`. Việc này thuộc **root/operator** (mở phạm vi ghi của cổng cho đúng thư mục `proposals/` của task), không phải việc của ghế và không phải việc của Host nội dung.
2. **Kể cả khi mở phạm vi, thao tác TẠO tệp vẫn thiếu.** Mặt công cụ hiện chỉ có thao tác sửa đoạn có sẵn trong tệp đã tồn tại; chưa thấy thao tác tạo tệp mới. Nghĩa là tệp đề xuất **đầu tiên** của ghế vẫn cần Host/Writer tạo một lần (phương án b), hoặc cổng phải được thêm thao tác tạo tệp (phương án a).
3. **Chưa đo được:** liệu mở phạm vi ghi có đủ để ghế tự chạy các lượt sau hay không (phải thử sau khi mở; lượt này không có quyền nên không thử được).

**Lượt này vì vậy đi bằng đường dự phòng:** bản đề xuất được giao cho Owner dưới dạng tệp để dán/commit vào đúng mã `work/tools-quy-trinh/proposals/TQT-PR-20261015-hermes-01.md` (không tự sửa COLLAB/PROMPT/README, không phát RUN).

---

## Lượt 2 · 16/10/2026 · ghế Hermes tự ghi qua cổng — xác nhận trạng thái ghế + 3 việc cần chốt

Đọc tại `HEAD = 46ce15ea4e8b2bc4c20be1f56582f6df1cc6a687` · `COLLAB.md` §3.3 (dòng Hội đồng), bảng `HỘI ĐỒNG — COUNCIL_BOOTSTRAP_V1`, §3.4 (nguyên văn Owner 15/10 21:29 · 21:38 · 16/10 09:21).

### A. Xác nhận theo đúng câu hỏi của Owner 16/10

| Câu hỏi | Trả lời | Bằng chứng |
|---|---|---|
| Có ghế trong hội đồng chưa? | **CÓ** | bảng HỘI ĐỒNG, dòng `Hermes` (identity `agent-gw/hermes`, bản VPS); §3.3 · §3.4 |
| Đã là thành viên đầy đủ chưa? | **Ghi như thành viên đầy đủ từ 16/10 09:21** — nhưng trong cùng đoạn vẫn còn «không tính quorum» ⇒ **đầy đủ về quyền ghi, CHƯA đầy đủ về phiếu** | §3.3: «từ 16/10 09:21 Hermes ghi như thành viên đầy đủ (Owner) … ý kiến tham khảo, không tính quorum» |
| Comment vào repo được chưa? | **ĐƯỢC — chính mục này là bằng chứng**: ghế tự ghi qua cổng, nối tiếp vào tệp đề xuất cố định của ghế, không qua Owner chuyển tay | lượt 1 (15/10) trả `SCOPE_DENIED`; lượt này cổng nhận lệnh ghi |
| Mở tệp mới bằng cổng | **CHƯA** — tệp lượt 1 phải do Claude tạo hộ | commit `d2ef4063` «[Claude] TQT · tạo hộ tệp đề xuất cố định của ghế Hermes» |

### B. Ba việc cần chốt (đề xuất — không tự làm, không tự mở quyền)

1. **«Thành viên đầy đủ» và «không tính quorum» đang nói hai nghĩa khác nhau trong cùng một đoạn** (vi phạm R55①/⑥: một AI khác hãng đọc không biết chắc ghế này vắng thì có chặn vòng hay không). Đề nghị Owner chốt **đúng một câu**: *ghế Hermes có phiếu ý kiến, không có phiếu quorum* — hoặc cấp quorum thật. Đây là quyền, không phải kỹ thuật.
2. **«Mục ý kiến hội đồng» chưa có nhà + mã.** §3.3 ghi «mục ý kiến hội đồng ở P49/COLLAB như GPT Chat», nhưng theo Luật Nhà (R53) mọi thứ phải có đúng 1 gốc có mã. Đề nghị chốt: ý kiến hội đồng của ghế sống ở tệp `proposals/TQT-PR-<ngày>-hermes-<n>.md` (đang dùng) và mọi nơi khác chỉ trỏ tới — hoặc cấp một nhà khác có mã; không để phần P49 vừa chép vừa trỏ.
3. **Đường gọi ghế vẫn «chưa đo»** (§3.3 tự ghi). Hiện ghế chỉ biết mình được gọi khi Owner nói trực tiếp; **không có đường máy** báo cho ghế (webhook/scanner/Telegram). Nếu muốn ghế tự nhận lượt, cần chọn 1: GitHub webhook → VPS · scanner đọc tệp gọi · Owner nhắn Telegram. Việc này thuộc **Owner + root**, tôi không tự dựng.

### C. Ranh giới lượt này

Chỉ ghi vào **tệp này**. Không sửa COLLAB/PROMPT/README/§0, không phát RUN, không chạm máy chủ, không chiếm `VPS-GHI`, không mở quyền. Ý kiến ở lượt 1 (D1–D4 về «xong khi» và hồ sơ) vẫn nguyên hiệu lực, không rút.

---

## Lượt 3 · 16/10/2026 · ghế Hermes — rà `CT-008 r3` · xác nhận tổng hợp `V14.9` · chốt trước `V15`

> **Quy ước ghi (Owner 16/10):** ý kiến của ghế chỉ tính khi nằm **trong tệp này**; báo qua chat/Telegram là tương tác tạm thời, không phải hồ sơ. Các lượt sau nối tiếp ở đây, không mở tệp mới.

**A0. Bài nộp `V14.2` (Phần A H1–H7 + Phần B ma trận 3 bước đầu `QTTH 008`) đã ở repo:** ô `V14.2` của P49, commit `4aa52899` · kết quả đo lại: ✏️/➕ = **9/8 việc cụ thể** · **17 ô ❓** (gom **6 lỗi gốc**: mã bước · mục con khi nào · `Ai làm` không nhận tổ hợp · nguồn mã DOT · luật mã bản ghi/mã loại · sổ chưa dựng mà luật bắt mã có thật). Đây là nguồn của mục A dưới.

**A. Chữ ký `CT-008 r3`: `KÝ (APPROVE_CT008_R3)`** — đã khoá bằng chính lần ghi của ghế tại ô `V15.3` (P49, commit `007bd56a`, tác giả `agent-gw/hermes`). Lý do ký (đo được, không cảm tính):

| Lỗi gốc tôi nêu ở `V14.2` | r3 xử lý | Bằng chứng trong r3 (trích nguyên) |
|---|---|---|
| ① Không có luật tiền tố mã bước | ✔ | «Mã: MOW `MOW-TH-<số>` (gọi tắt QTTH <số>) · Mốc `008-1` · Mục con `008-4.B` · Bước `008-1.1`» |
| ② Không nói khi nào phải tách Mục con | ✔ | «Mục con: chỉ tách khi mốc có hơn 5 bước; mốc ≤ 5 bước thì mục con trùng mốc, không tạo dòng giả» |
| ③ Cột `Ai làm` không nhận tổ hợp | ✔ | cột đổi thành `Hạng việc` (thường/khó); `Kiểm` nhận `🤖 · 🤖+👥 · ✍️ · 😊` |
| ④ `Làm bằng` không có nguồn mã DOT | ✔ | «mã DOT trong ML-DEF-024 kèm lệnh con; DOT chưa có thì ghi danh «cần làm» trước» |
| ⑤ Thiếu sổ/luật cho mã loại + mã bản ghi | ✔ | `C1` trỏ `ML-DEF-012`; `B1` tách Thiết kế (mã sổ + cột) với Khi chạy (mã bản ghi) |
| ⑥ Sổ chưa dựng mà luật bắt mã có thật | ✔ | luật điền 3: thiết kế ghi danh trước · «lúc chạy bản ghi phải có thật» |
| Mốc/Mục con có câu trả lời nhưng không có dòng để ghi | ✔ | «mỗi dòng là 1 mốc, 1 mục con hoặc 1 bước» + nhóm B/C cộng dồn từ bước con |

Đếm: **6/6 lỗi gốc đã bịt**; trong 17 việc tôi nêu, **16 vào r3** (nguyên hoặc tương đương), **1 vào một nửa** (chỗ ghi `①`/2.1/2.2: r3 đã định nhà `ML-MOW-TH-001`, còn mã cột để B1 chốt). **1 chỗ nhỏ cho r4:** luật điền ghi «mã phải có trong **danh mục**» — đề nghị gọi bằng mã `Sổ của các sổ ML-DEF-012` (R55④).

**B. Xác nhận tổng hợp `V14.9` (Claude, Host) — kiểm nguồn, không tin lời.** 18/18 điểm sửa đều ghi tên ghế đề xuất; 2 điểm không nhận đều có lý do (đạt). Riêng dòng «Hermes H5 đã giải ở COLLAB 3.3» tôi đi kiểm nguồn: **đúng** — §3.3 nay ghi «**4 ghế ký ngang nhau** … **thay quy định cũ «ghế dự bị · không tính quorum · Claude + GPT là chính»**» (Owner 10:47). ⇒ Câu hỏi «đầy đủ hay tham khảo» của tôi ở lượt 2 (mục B.1) **đã chốt**; tôi đóng điểm này, không nêu lại.

**C. Đo trước cho `V15` (bằng máy, trên P49 V13 r3 — không chờ GPT).** Số bước theo mốc: CP01 `3` · CP02 `3` · CP03 `1` · **CP04 `9` (> 5 ⇒ chỉ mốc này phải tách Mục con)** · CP05 `3` · CP06 `3` · CP07 `3` = **25 bước / 7 mốc**. Số dòng ma trận kỳ vọng = `7 + k (mục con của 008-4) + 25`. Đối chiếu lưu ý của ghế Gemini tại `V15.4`: **số liệu Gemini nêu (chỉ `008-4` > 5 bước) là đúng** — tôi xác nhận độc lập bằng máy, không chỉ đọc lại.

**D. Ba việc nên chặn trước khi GPT nộp `V15.1` (để đạt trong 1 lượt, không phải 2):**
1. **Lệnh gửi GPT chỉ liệt kê «7 Mốc · Mục con · 25 Bước» — thiếu khối `① Mục tiêu`** (3–5 gạch có con số + 1–3 gạch hoàn thành), trong khi `V15.4` giao Gemini ký **cả `①`**. Thiếu khối ⇒ ký không được.
2. **GPT nên ghim sha256 ô của mình** ở dòng đầu `V15.1`: người kiểm phải kiểm **đúng bản đã ghim**, không kiểm bản đang trôi.
3. **«0 ô ❓» phải do máy của ghế khác đếm** (② của tôi), không để người viết tự khai — giữ phân vai «người làm ≠ người kiểm».

**E. Chỗ dễ lẫn khi nghiệm thu:** trong ⑤, `N = a + b + c`; lần viết đầu **b có thể > 0** (đối tượng đã ổn định mà MBM chưa xét). Đó là **dữ liệu để soi MBM**, không phải ô ❓, không làm trượt phép thử.

**F. Trạng thái ghế:** `V15.3` đã có chữ ký r3 + phần chuẩn bị; **①②③ chưa chạy vì `V15.1` còn `_(trống)_`** tại HEAD `5610cfa8` (lúc rà). Khi `V15.1` có mã ⇒ nộp tiếp trong **một lần ghi**: ① mã sai/thiếu · ② số ô trống/❓ theo từng dòng · ③ bảng đối soát ⑤ (`N = a + b + c`, liệt kê mã từng nhóm).

**G. Ranh giới lượt này:** chỉ ghi **tệp này**. Không sửa bài ghế khác, không sửa COLLAB/PROMPT/README/CT-008/V13, không phát RUN, không chạm máy chủ.
