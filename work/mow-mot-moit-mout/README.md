# README · MMIM · START HERE

> **★ UI cha:** [mở mẫu và quy chuẩn](https://vps.incomexsaigoncorp.vn/knowledge/modules?task=mow-mot-moit-mout&view=content&section=matrix-view-process). Khối **4 Mẹ** dùng bản xuất `ML-DEF-018` trong `definition-master-data-v1.js` đã có sẵn trên trang, truy nguồn `ui/child-ui-registry.json`; không duy trì danh sách URL riêng. Bấm tên mở UI gốc ở tab mới. **Đang chặn:** lớp iframe ngoài của `/knowledge/modules` chưa cho mở tab mới; thao tác mở đã chạy ở bản Mở rộng, chưa nghiệm thu đường bấm ngay trong cổng. Quy chuẩn từng UI nằm ngay bên dưới, gồm giữ nguyên/được thay và thông số; UI-DESIGN-STANDARD và FORMULA-AI-README chỉ dẫn về đây. Không giữ ảnh chụp hay bản sao quy chuẩn. Phiếu kiểm: [UI-REVIEW-PARENT-GALLERY.json](UI-REVIEW-PARENT-GALLERY.json).
>
> **CE-20261008-PARENT-SSOT · APPROVED:** Owner yêu cầu trực tiếp gom đường mở UI và quy chuẩn theo từng UI cha. Đã chuyển nội dung từ UI Master, UI-DESIGN-STANDARD và phần token Master của FORMULA-AI-README; giữ các mã neo cũ. Thư mục Desktop/quy trình được đối chiếu, không sửa bản lịch sử. Menu 4 Mẹ/VPS giữ nguyên; chưa có thay đổi thiết kế, trạng thái duyệt hoặc dữ liệu nghiệp vụ.

> **Rules — đầu mối quy định hiện hành:** [mở tab Rules](https://vps.incomexsaigoncorp.vn/knowledge/modules?task=mow-mot-moit-mout&view=content&section=matrix-view-uis), nguồn `ban-duyet.html#rules-current` (R01–R48). Các mục dưới là hợp đồng triển khai/đối chiếu; khi đổi nguyên tắc sửa Rules trước, không ban hành một bản luật song song. Help và tài liệu cũ giữ làm nguồn, không tự ghi đè hoặc xóa.

> **Mọi thay đổi UI:** đọc [Quy chuẩn UI cha](UI-DESIGN-STANDARD.md) trước; bàn giao phải có phiếu theo [UI-REVIEW-CONTRACT.json](UI-REVIEW-CONTRACT.json) và chạy `check-ui-review.py`. AI chịu trách nhiệm kiểm, không đẩy Owner thành tester. Kết quả rà: [UI-AUDIT-20261007.md](UI-AUDIT-20261007.md).

> **Cửa vào bắt buộc của việc `work/mow-mot-moit-mout`.**
> Nếu một file/quy trình/tool mới không được nối từ README / Bảng điều khiển / Master tương ứng thì coi như **chưa được đăng ký vận hành**.

## Tools · CTCM · Quy trình thiết kế và kiểm UI
[Master Tool](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/definition-master-v1.html?stt=23) → [Quy trình Tools và áp thử MOW-NHC-001](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/tools-playbook-v1.html). Quy tắc R46–R48.
SSOT nội dung: VPS `definition-master-data-v1.js`, `ML-DEF-023`, TOOL-CTCM-001…009; thanh **Quy trình - Tools** ngay trang Công thức (sau D) và trang Tools dùng cùng `tools-catalog-v1.js`, đọc cùng SSOT. Tool008 quản lý UI thiếu/lỗi; Tool009 đóng gói DOT. Mỗi quy trình có Bước/Câu hỏi/Việc phải làm. Phiếu kiểm thanh Công thức: `UI-REVIEW-FORMULA-TOOLS.json` (đã kiểm desktop và màn hẹp cho riêng thanh Tools). Hai công thức thao tác CT-TOOLS-UI/CT-TOOLS-CFG ở ML-DEF-021 là đề xuất, không thay công thức sinh đối tượng.
Bộ rà hiện tại: 8 câu/MOT × 3 MOT = 24 ô; 16 nhánh nền. Đã sửa Q2/Q5/Q8 và vòng kiểm hiệu lực: chưa đạt đích → xác định câu/nhánh thiếu → sửa Tool gốc → thêm ca → chạy lại. [Sổ theo dõi](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/tools-playbook-v1.html#issue-register) và [kết quả từng Tool](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/tools-playbook-v1.html#tools-run-register) là SSOT trạng thái; AI đọc đầu/cuối lượt. Chưa đạt production, chưa triển khai DOT mới. Hai đường đi: 1→3 hoặc 1→2→3.
Phiếu kiểm trang hướng dẫn: `UI-REVIEW-TOOLS.json`; không dùng kết quả trang hướng dẫn thay kết quả hành trình tìm Field.

## Thử thiết kế theo MOW · Owner 07/10/2026
[MOW-NHC-001 · 3 màn hình riêng](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/mow-ui-walkthrough-v1.html?mow=MOW-NHC-001), mở từ số MOT trong Master MOW. Mỗi màn có URL step=1/2/3; trạng thái đầu trống, minh hoạ thu riêng và cùng renderer UI-029 (flow=field). Nguồn dùng chung: tim-kiem-chung-v1.html + field-flow-v1.js/css + field-flow-model-v1.js; walkthrough điều hướng và metadata SSOT. Ba màn ở REVIEW, chưa thêm UI xác nhận vào canonical. [Phiếu kiểm](UI-REVIEW-MOW001.json): 17 model tests từ lượt trước; 08/10 đã truy cập browser và ghi 18 quan sát chọn lọc màn 2/minh hoạ, xem lượt TQT-UI-20261008-MOW001-STEP2 trong phiếu. Toàn hành trình còn PARTIAL: responsive/parity chưa phủ, tìm thật/nơi nhận chưa đủ; không coi là production-ready. Rà UI bằng [hướng dẫn Tools](../tools-quy-trinh/view.html#ra-ui), giữ sổ MOW hiện có. Chuyên môn, dữ liệu thật, JEV và nơi nhận xác nhận còn trong sổ.

## 1. Mỗi phiên phải đọc gì?

1. Root `AGENTS.md`.
2. `COLLAB.md` → đọc **§0 + BẢNG ĐIỀU KHIỂN** để biết việc hiện tại và hành động kế tiếp.
3. README này.
4. Nếu chạm Công thức / Định nghĩa / Master / UI / Coverage → `FORMULA-AI-README.md`.
5. Nếu thay đổi tiêu chí / trạng thái / tên / quan hệ có thể lan nhiều nơi → `CHANGE-PROPAGATION.md` + `CHANGE-IMPACT-MAP.json`.
6. `council/REGISTRY.md` để biết Host/Reviewer/NEXT.
7. Chỉ sau đó mới đọc file chuyên môn cần thiết.

## 2. Luật chống “làm xong rồi quên”

Mọi artifact vận hành mới (quy trình, tool, script, UI, Master, prompt, checklist) phải có **ít nhất một cửa đăng ký bắt buộc**:

- **Quy trình / luật làm việc** → README này + HANDOFF/AGENTS pointer.
- **Công thức / định nghĩa** → FORMULA-AI-README + Master Công thức/Định nghĩa.
- **UI đã duyệt** → Master UI con / UI cha tương ứng.
- **UI chưa duyệt** → review surface; **không** vào Master UI canonical.
- **Prompt/RUN đang chờ** → BẢNG ĐIỀU KHIỂN + council/REGISTRY.
- **Tool/script** → catalog/tool Master hiện hành + tài liệu gọi nó.

**Cấm:** tạo file rồi chỉ ghi tên file trong lịch sử COLLAB. Nếu ngày mai AI không biết *khi nào phải đọc/call nó* thì artifact đó chưa hoàn thành.

## 3. Quy trình thay đổi liên bảng

Khi một tiêu chí thay đổi, **không sửa một chỗ rồi XONG**.

Bắt buộc dùng:
- `CHANGE-PROPAGATION.md` — quy trình 8 bước.
- `CHANGE-IMPACT-MAP.json` — bản đồ machine-readable các bảng/view phải quét.

Chuỗi:
`Change Event → SSOT → quét impact trước → UPDATE/VERIFY/N-A → sửa → quét stale sau → kiểm live → evidence/KQ`.

### Điều hành PENDING · event-driven, không polling
- **Không tạo schedule/automation nền chỉ để nhắc một việc nội bộ repo.** Việc đó tốn quota nhưng không làm hệ thống thông minh hơn.
- PENDING phải nằm trong **BẢNG ĐIỀU KHIỂN + README này + council/REGISTRY**.
- Trigger mặc định là **sự kiện**, không phải thời gian: `mở phiên`, `STARTED@`, `KQ@`, `Owner duyệt`, `status đổi`, `dependency đổi`.
- Khi mở phiên, Host đọc Bảng/NEXT và nêu việc PENDING nếu chưa có KQ; đây là cơ chế “nhớ”.
- Automation chỉ được cân nhắc khi có nhu cầu thời gian/điều kiện bên ngoài thật sự, Owner yêu cầu/duyệt, và cadence được chọn theo chi phí quota.
- Mục tiêu dài hạn: các event/status tự kích hoạt đúng quy trình; **không polling vô thức**.

## 4. Sổ vận hành ngắn

| Artifact | Dùng khi nào | Trạng thái |
|---|---|---|
| `FORMULA-AI-README.md` | Chạm Công thức/Định nghĩa/Master/UI/Coverage | BẮT BUỘC |
| `CHANGE-PROPAGATION.md` | Một thay đổi có thể ảnh hưởng >1 bảng/view | BẮT BUỘC |
| `CHANGE-IMPACT-MAP.json` | Agent cần biết phải quét/cập nhật đâu | BẮT BUỘC cùng Change Propagation |
| `PROMPT-CHANGE-PROPAGATION.md` | Codex audit case đầu tiên của quy trình mới | **PENDING RUN** |
| `HANDOFF-20261001.md` | Phiên Host mới tiếp quản lịch sử/tinh thần | BẮT BUỘC khi handoff |
| `COLLAB.md` | Trạng thái hiện hành + evidence + quyết định | SSOT trạng thái |
| `council/REGISTRY.md` | Ai đang Host/Review/NEXT | SSOT điều phối |

## Master Config · D152 · 06/10/2026
- UI đang rà: [Master Config](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/config-master-v1.html), dòng 28 trong bảng duyệt hiện hành.
- Dùng nguyên UI.MASTER cha `mot-master-v1.html`; schema/nhãn SSOT tại `ui/config-master-data-v1.js#CONFIG_MASTER_SCHEMA`. Không còn renderer bảng riêng.
- Mặt danh sách: **STT · ID · Tên · Loại config · Mục đích · Áp dụng cho · Phạm vi sử dụng · Người phụ trách · Trạng thái**. “Loại config” không gộp Nhóm cha/con; người phụ trách quản lý khác người thực hiện theo NTGV.
- Chi tiết: UI cha, người thực hiện, kích hoạt khi, phiên bản, tham số, bằng chứng áp dụng, nguồn/ghi chú. Thông tin chưa biết hiển thị chưa khai báo/chưa phân công, không tự bịa.
- `CFG-TEST-001` giữ toàn bộ trường gốc và trạng thái nháp/test. Chưa nối DB hoặc có UI CRUD. FC-002 vẫn OPEN; chưa quyết nghĩa canonical của Config hay quan hệ định nghĩa/lần áp dụng.

## D153 · Danh mục Nhóm cha / Nhóm con T0–T2 · 06/10/2026

Đã ghi vào hai Master hiện hữu theo chỉ đạo Owner: **35 Nhóm cha** (B1–B7 × 5 nhánh) và **115 Nhóm con** (23 Bước con × 5 nhánh). Nguồn Bước/Bước con: CT-001 trong `ML-DEF-021`; đối tượng/tầng: CT-002. MOIT và MOUT cùng T0.5 nhưng là hai nhánh riêng.

| Tầng / đối tượng | Nhóm cha | Nhóm con |
|---|---:|---:|
| T0 · Field | 7 | 23 |
| T0.5 · MOIT | 7 | 23 |
| T0.5 · MOUT | 7 | 23 |
| T1 · MOT | 7 | 23 |
| T2 · MOW | 7 | 23 |
| Tổng | 35 | 115 |

- [Master Nhóm cha](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/definition-master-v1.html?stt=1): `NHC-001…035`; thêm 28, giữ nguyên 7 dòng cũ.
- [Master Nhóm con](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/definition-master-v1.html?stt=2): `NHCN-001…115`; thêm 112, giữ nguyên 3 dòng cũ.
- Số Bước con B1→B7: **3, 2, 4, 4, 3, 3, 4 = 23**. Không tạo B8/B9 hoặc bước con chưa có nguồn.
- Khóa chống trùng: `stepRef + tierRef`; mỗi Nhóm con có `parentGroupId` cùng đối tượng/tầng, đúng Bước gốc. `tierRef` phân biệt MOIT/MOUT tại T0.5.
- **Độ phủ danh mục: FULL cho phạm vi Owner giao.** Rule/config/bộ trường bắt buộc chưa hoàn thiện vẫn hiển thị thiếu; Chuyên môn Nhóm con giữ OPEN. Đây không phải kết luận các nhóm đã được duyệt để vận hành. Không đổi công thức/khái niệm hoặc canonical UI.

## D155 · Total của các Master

[Bảng 28 Master](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/definition-master-index-v1.html) có cột **Total ngay sau Tên**, đếm từ nguồn đang dùng ở list con. Tự nạp lại nguồn khi mở/tải lại bảng; không sửa total tay. Công thức chỉ đếm dòng gốc; MOIT/MOUT theo mã duy nhất; thiếu nguồn hiển thị —, mảng rỗng hiển thị 0. Logic ở `ui/ui-child-content-v1.js`, nạp nguồn ở `ui/ui-child-from-parent-v1.js`; dữ liệu không đổi. Xem KQ D155 trong COLLAB.

## D156 · Công thức và ngoại lệ Gộp/Tách

CT-005 dùng **Nhóm cha**; **CT-005.1 · Bước con + Tầng ⇒ Task** đứng ngay sau 005, tổng 8 công thức. Master Nhóm con và MOT/Task có **Gộp / Tách** với ? theo UI cha, tham chiếu mã hồ sơ riêng. Dữ liệu chuẩn giữ nguyên; chưa có hồ sơ thật hoặc backend CRUD. Trước khi lập hồ sơ ngoại lệ, đọc hợp đồng ở `FORMULA-AI-README.md` D156; mỗi hồ sơ giữ nguồn/kết quả/lý do/quyết định/bằng chứng. Chưa sinh Task mới trong lượt này.

## 5. VIỆC ĐANG CHỜ — KHÔNG ĐƯỢC QUÊN

**PENDING:** giao Codex chạy audit Change Propagation đầu tiên.

- Based on commit: `61b691dfc7457b17467f5eff8d5a1f19da411e4d`
- Prompt: `work/mow-mot-moit-mout/PROMPT-CHANGE-PROPAGATION.md`
- RUN_ID: `MMIM-CHANGE-PROP-20261006-01`
- Mục tiêu: quét repo/current-live cho case UI con D144, sửa stale reference, bổ sung impact map nếu còn thiếu.
- Chỉ hết PENDING khi có:
  `KQ@MMIM-CHANGE-PROP-20261006-01 XONG`
  và Host nghiệm thu.

**Quy tắc Host:** nếu mở phiên mới mà PENDING này chưa có KQ XONG, phải nêu ngay trong phần “Kế tiếp”; không được âm thầm đi sang việc khác. **Không dùng reminder automation mặc định để làm việc này.**

## 6. Câu giao Codex

> Đọc `work/mow-mot-moit-mout/PROMPT-CHANGE-PROPAGATION.md`, bám commit `61b691dfc7457b17467f5eff8d5a1f19da411e4d`, chạy đúng RUN_ID `MMIM-CHANGE-PROP-20261006-01`. Không đổi concept; audit/fix current-live theo Change Propagation và ghi KQ vào COLLAB.
