# README · MMIM · START HERE

## P38 · Hồ sơ nhẹ, giữ nguyên lịch sử

Kho vật lý dùng `TQT-HISTORY-POOL-1` trong cùng tệp, không mở kho/Master khác. Mỗi khối lặp lưu một lần theo SHA256; CHECK004 kiểm hash và giải mã trước khi đối chiếu. Nội dung G1/18 sự kiện/20lần kiểm/7mốc không đổi. Biên nhận và tiến độ tại aggregate#host_review_P38.

**Cho AI:** Tra Master DOT rồi dùng CHECK004 `--compact-history SOURCE` (dry-run); thêm `--execute --output CANDIDATE` chỉ tạo ứng viên mới. Kiểm `--check-history` và `--validate-transition BEFORE AFTER`; ghi qua upload/transaction có expected_version và cửa ghi hiện hành; đọc lại có chữ ký trước khi chốt. Khi cần bản JSON đầy đủ, dùng `--expand-history SOURCE --execute --output EXPANDED` ở vùng tạm; không nhân thành nguồn chuẩn. Sau sửa nghiệp vụ phải pack lại và vẫn tuân phiên/lịch sử cũ. Trước khi lùi runtime cũ phải expand qua cổng hiện hành, không tráo bộ đọc cũ vào dữ liệu mới. Bộ tổng kho nhẹ đã chạy trong1GiB; không tự tăng ngân sách.

**Cho người dùng:** ô xong có tích xanh, ô chưa xong màu xám; tự tổng hợp từ bằng chứng, không tích tay. Lịch sử vẫn là các sự kiện cũ trong Master lịch sử.


## P37 · Một vòng MOW001 G1 đã duyệt và nhận

**Kiểm cuối P37:** bộ tổng VPS PASS, job `43e4948f9c5c4c27b7b868b47483bcd3`; giữ đầy đủ lịch sử, nguồn sản phẩm `908f9c7f`. Đã kiểm hồ sơ 7/7, 50 câu trả lời và phép chiếu Master. Biên nhận/các lượt lỗi/phục hồi ở aggregate#host_review_P37. Đã trả cả hai nguồn cấu hình tài nguyên về đúng bản gốc; biên nhận tại resource_restoration. Lần kiểm đầy đủ sau cần ngân sách2GiB khai trong DOT; mặc định1GiB sẽ dừng trước kiểm.

Hồ sơ đúng việc: [TQT-VIEC-001 · MOW001](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/process-work-master-v1.html?master=DEF00.1&chi-tiet=TQT-VIEC-001). TQT-VIEC-002 là MOW002 mới ghi danh, chưa mở hồ sơ; không điền dữ liệu MOW001 sang đó.

Owner đã duyệt và xác nhận nhận G1 trực tiếp ngày 12/10/2026. Hồ sơ qua cửa ghi: **7/7 mốc, 31/31 nghĩa vụ phát sinh đã đối chiếu; 3 nhánh điều kiện không phát sinh**. Commit 8ac40578c3bccf9b4b43f6af1e7c5ac0fa91210b; task0a72d0f4bb5342749a88059e9c148bdd; hash908f9c7fbf3eb664ffd88249a1c9d277f90a7d3022e8c01c246af10f3fefd35b. Biên nhận kiểm và giao diện cuối nằm tại UI-REVIEW-AGGREGATE.json#host_review_P37. G1 là thiết kế; G2/PG chưa được nghiệm thu.

### Thực hiện và ghi theo một nguồn

1. Mở DEF00.1, chọn đúng mã việc → hồ sơ/phạm vi/phiên. Chưa có application_id thì khai hồ sơ trước; không lấy hồ sơ tiền nhiệm làm của việc mới.
2. Đọc **50 câu hỏi–đáp án và 13 khai báo**. CHECK004 --read-preparation FILE kiểm số câu, nội dung, nguồn và phiên; thiếu phải ghi thiếu rồi giải quyết. Hồ sơ nguồn là UI-REVIEW-MOW001.json#/application_D24; câu trả lời kế thừa giữ answer_ref, trang Master chiếu ra, không nhập lại.
3. Tra [Master DOT](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/definition-master-v1.html?stt=24) và [Master Tool](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/definition-master-v1.html?stt=23): đọc trạng thái, phiên/hash, phạm vi, cách chạy và bằng chứng trước khi dùng lại. Thiếu mới đề xuất công cụ. Lệnh tạm gắn lượt dùng, ca TEST gắn bộ hiện có; không tạo một DOT cho mỗi lệnh.
4. Mốc 1–3: đúng MOW/MOT → câu hỏi/khai báo → hợp đồng CAT206, kế hoạch CAT228 → quyền kho tệp bằng biên nhận máy chủ đúng nguồn/hash. Quyền này không thay quyền toàn Master/PG.
5. Mốc 4–5: P02/P03 ghi thiết kế → P04 tự mở đúng bản/hash bằng CHECK004 --read-designs FILE, đối chiếu 11 tiêu chí và UI thật. Ghi CAT015 kết quả/người kiểm, CAT229 lượt làm, CAT069 sai/thiếu, CAT016 thay đổi, CAT233 lịch sử.
6. Mốc 6–7: lời duyệt/nhận thật đúng người → CAT025 quyết định, CAT228 kết quả P05, CAT232 nhận → ghi qua cửa máy chủ → đọc lại đúng hash → kiểm tuần tự 6 rồi 7. Không lấy TEST, ACK iframe hoặc chữ ký kỹ thuật thay Owner.
7. **Kiểm đủ nơi ghi:** DEF00.1 tiến độ; CAT012 tiêu chí; CAT015 kết quả; CAT016 thay đổi; CAT025 quyết định; CAT069 vấn đề; CAT228 kế hoạch/kết quả; CAT229 lượt làm; CAT232 giao nhận; CAT233 lịch sử; CAT206 hợp đồng; CAT244 chỉ khi hủy. Mã MOW/MOT và nguồn/đích khác giữ Master gốc. Danh sách 19 Master liên quan, 34 nghĩa vụ và nơi lưu được tổng hợp tại aggregateP37/master_coverage và chính hồ sơ, không nhập bảng độc lập.
8. CHECK005 kiểm đủ câu trả lời/đúng phiên, quyết định/nhận/lịch sử hiện ra ở đúng Master và không nhầm việc chưa mở. CHECK006 chạy tổng/kiểm hash/danh mục khi đổi mã. Đọc lại UI đúng revision và hash tài liệu đã xuất, không chỉ HTTP200. Cập nhật ngay bảng điều khiển cùng biên nhận.

### Dùng lại trước, khôi phục có bằng chứng

CHECK001/002: mô hình/mã/quan hệ. CHECK003/004: hợp đồng/mốc/ghi–đọc. CHECK005: Master/hồ sơ/UI. CHECK006: chạy tổng, kiểm nguồn và kiểm kê. Với mỗi lượt giữ mã việc, công cụ/nhà cung cấp, phiên/hash, thời điểm, mã chạy, kết quả và nguồn bằng chứng. Công cụ ngoài VPS cần biên nhận nền tảng; gateway không tự nhìn thấy. Có hàng trăm tệp tìm thấy không đồng nghĩa hàng trăm công cụ đã kiểm chạy.

Ghi lâu dùng workspace_task_start, expected_version và operation_id. Mất trả lời không suy đã ghi: kiểm task/hash/log trước khi gửi lại. Gặp ROLLBACK_CONFLICT: dừng ghi, kiểm manifest/HEAD/before–after; chỉ phục hồi đúng byte của chính giao dịch dưới khóa, giữ bản lỗi và dấu vết. P37 tái lập bad_alloc ở vùng nhớ1.5GiB, PASS2.5GiB; tạm chạy nối tiếp qua Config Guard, phải trả cấu hình sau ghi. Đây là biện pháp khép G1, chưa phải lời giải nhân rộng. Không bỏ chốt kiểm hoặc xóa lịch sử cho vừa tài nguyên.

**Còn mở:** G2, PG; chuyên môn cha T3 chưa xác minh; AI mới tự lặp một vòng việc thật; tối ưu lịch sử và cải thiện chẩn đoán/hoàn tác khi thiếu tài nguyên. Theo các issue hiện hữu và TQT-P37-F03/F04/F05. Hai chữ ký GPT/Claude vẫn gắn người/phạm vi/phiên; chưa có Claude ghi chưa duyệt, không chặn theo Owner.

## Lịch sử trước P37 — không phải trạng thái hiện hành

## P36 · MOW001/G1 · 12/10/2026

P02/P03 thật đã được ghi và P04 tự mở đúng hash; 11 tiêu chí G1 được Reviewer `/root/review_mow001` chấp nhận kỹ thuật (`e1e753`, `2026-10-12T08:59:31Z`). P04 commit `db0de657082d8f68cd5a03c207785fd4c8e02bbc`, nguồn `88460eee2688ebd8ce4f2c11d94f17887049322c7e44c20e0f2fd463b3b82422`; máy chủ R2 ký biên nhận đọc task `114c0cf2341341c2b7b764a7f737273b`. Có 16 quan sát giao diện đã triển khai, 24 ca model bổ trợ; minh hoạ không thay nguồn nghiệp vụ thật.

**Đã lưu: CHO_DUYET, 5/7 mốc, 28/34 nghĩa vụ.** CP05 qua cửa ghi tại commit `0ea489a366eaa4a230a6a2346987281e8d9c9694`, transaction `0c68b2d7ed5d42a18a13482714235d66`, task `ea88409a8d19423d91b8977ebdce9e3c`; phiếu đúng SHA256 `ec1620205a41c174f98a38b77225a2151811745a65e2c42f11c1d21fd774d6df`. CP06 quyết định Owner và CP07 xác nhận nhận chưa có; không tự điền. Bộ tổng cuối PASS trên VPS1GiB, job `1912451206cb4dd28b30f4447cdfcfc3`, nguồn `276f1ac407e32f1a7821b0d3ed163f5dd50b4f42`; CHECK001–005 và runner006 đều đạt. Đã sửa cách nạp dữ liệu TEST, thời hạn005 và liên kết sổ; giữ toàn lịch sử thật, không nới giới hạn hoặc sửa gate cho vừa TEST. Biên nhận và các lượt lỗi giữ tại tools-quy-trinh/UI-REVIEW-AGGREGATE.json#host_review_P36. Nguồn duy nhất vẫn `UI-REVIEW-MOW001.json#/application_D24`; xem `execution_walk`, `design_artifacts`, `plan_results`, `test_cases`. Hợp đồng v5/schema1.4/plan4; UI build P36.1. G2 nguồn Field/evaluator/consumer còn OPEN; chưa PG. Không dùng TEST, ACK iframe hoặc thiếu duyệt Anthropic thay quyết định Owner.

Điều hành và hướng dẫn ghi–đọc/khôi phục ở [tools-quy-trinh README · P36](../tools-quy-trinh/README.md). Dùng lại CHECK004 đọc chuẩn bị, thiết kế và kiểm model; CHECK006 kiểm tổng. Với lượt ghi lâu dùng hàng đợi hiện có, kiểm hash và trạng thái trước khi thử lại; không bỏ cửa ghi. Master đọc cùng nguồn, không mở thêm sổ/DOT. Các mục P35 và các ngày trước bên dưới giữ lịch sử, không phải trạng thái hiện hành.


> **P35 · MOW001/G1 hiện hành 12/10:** hồ sơ duy nhất `UI-REVIEW-MOW001.json#/application_D24`, phần `execution_walk` và `preparation_review`. CP01/CP02 đạt trên việc thật (2/7),20/34 mục đã đọc lại;50 câu gồm44 rà lại+6 bổ sung. CP03 thiếu đầu vào tin cậy từ adapter cửa ghi, chưa sửa/duyệt UI. Điều hành ở [tools-quy-trinh](../tools-quy-trinh/README.md); các lượt cũ bên dưới giữ nguyên lịch sử. Chưa PG; không dùng TEST thay nghiệm thu sản phẩm.


> **★ UI cha:** [mở mẫu và quy chuẩn](https://vps.incomexsaigoncorp.vn/knowledge/modules?task=mow-mot-moit-mout&view=content&section=matrix-view-process). Khối **4 Mẹ** dùng bản xuất `ML-DEF-018` trong `definition-master-data-v1.js` đã có sẵn trên trang, truy nguồn `ui/child-ui-registry.json`; không duy trì danh sách URL riêng. Bấm tên mở UI gốc ở tab mới. **Đã sửa 08/10:** bấm “Mở mẫu cha để đối chiếu” ngay trong cổng mở đúng mẫu gốc ở tab mới, giữ trang tài liệu. Lỗi nằm ở quyền mở tab của khung ngoài; runtime `b47545bc1edbfb0f3551af2041441480d6859f8f` đồng bộ quyền cho cả lớp cổng còn lưu đệm. Hồ sơ kiểm tra/hoàn tác: `/opt/incomex/work/mow-mot-moit-mout/UI-PARENT-LINKS-20261008/`; quy trình nguồn tại `scripts/hvu-b2/README.md` của runtime Nuxt. Quy chuẩn từng UI nằm ngay bên dưới, gồm giữ nguyên/được thay và thông số; UI-DESIGN-STANDARD và FORMULA-AI-README chỉ dẫn về đây. Không giữ ảnh chụp hay bản sao quy chuẩn. Phiếu kiểm: [UI-REVIEW-PARENT-GALLERY.json](UI-REVIEW-PARENT-GALLERY.json).
>
> **CE-20261008-PARENT-SSOT · APPROVED:** Owner yêu cầu trực tiếp gom đường mở UI và quy chuẩn theo từng UI cha. Đã chuyển nội dung từ UI Master, UI-DESIGN-STANDARD và phần token Master của FORMULA-AI-README; giữ các mã neo cũ. Thư mục Desktop/quy trình được đối chiếu, không sửa bản lịch sử. Menu 4 Mẹ/VPS giữ nguyên; chưa có thay đổi thiết kế, trạng thái duyệt hoặc dữ liệu nghiệp vụ.

> **Rules — đầu mối quy định hiện hành:** [mở tab Rules](https://vps.incomexsaigoncorp.vn/knowledge/modules?task=mow-mot-moit-mout&view=content&section=matrix-view-uis), nguồn `ban-duyet.html#rules-current` (R01–R48). Các mục dưới là hợp đồng triển khai/đối chiếu; khi đổi nguyên tắc sửa Rules trước, không ban hành một bản luật song song. Help và tài liệu cũ giữ làm nguồn, không tự ghi đè hoặc xóa.

> **Mọi thay đổi UI:** đọc [Quy chuẩn UI cha](UI-DESIGN-STANDARD.md) trước; bàn giao phải có phiếu theo [UI-REVIEW-CONTRACT.json](UI-REVIEW-CONTRACT.json) và chạy `check-ui-review.py`. AI chịu trách nhiệm kiểm, không đẩy Owner thành tester. Kết quả rà: [UI-AUDIT-20261007.md](UI-AUDIT-20261007.md).

> **Cửa vào bắt buộc của việc `work/mow-mot-moit-mout`.**
> Nếu một file/quy trình/tool mới không được nối từ README / Bảng điều khiển / Master tương ứng thì coi như **chưa được đăng ký vận hành**.

## Tools · CTCM · Quy trình thiết kế và kiểm UI
**D24 · 10/10/2026:** Hướng dẫn hiện hành ở [tools-quy-trinh](../tools-quy-trinh/README.md); hồ sơ sản phẩm vẫn giữ tại nguồn gốc. Phiếu chuẩn bị lượt mới: [UI-REVIEW-MOW001.json](UI-REVIEW-MOW001.json), mục `application_D24`, chỉ G1 thiết kế 3 MOT. Đang CHUAN_BI, cần xác nhận điều kiện/kế hoạch trước sửa UI; không G2/G3. Các phiếu cũ giữ làm bằng chứng, không tự tính đạt cho lượt mới.
[Master Tool](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/definition-master-v1.html?stt=23) → [Quy trình Tools và áp thử MOW-NHC-001](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/tools-playbook-v1.html). Quy tắc R46–R48.
Nguồn hướng dẫn hiện hành: `work/tools-quy-trinh/view.html`. VPS `definition-master-data-v1.js`/`ML-DEF-023` và `tools-catalog-v1.js` giữ nội dung hướng dẫn lịch sử và sổ sản phẩm gốc; không sửa hướng dẫn song song. Tool008 ghi/đọc lại/bàn giao hồ sơ; MOW-TH-002 giữ vòng xử lý, Tool009 đóng gói DOT. Mỗi quy trình có Bước/Câu hỏi/Việc phải làm. Phiếu kiểm thanh Công thức: `UI-REVIEW-FORMULA-TOOLS.json` (đã kiểm desktop và màn hẹp cho riêng thanh Tools). Hai công thức thao tác CT-TOOLS-UI/CT-TOOLS-CFG ở ML-DEF-021 là đề xuất, không thay công thức sinh đối tượng.
Bộ rà hiện tại: 8 câu/MOT × 3 MOT = 24 ô; 16 nhánh nền. Đã sửa Q2/Q5/Q8 và vòng kiểm hiệu lực: chưa đạt đích → xác định câu/nhánh thiếu → sửa Tool gốc → thêm ca → chạy lại. [Sổ theo dõi](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/tools-playbook-v1.html#issue-register) và [kết quả từng Tool](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/tools-playbook-v1.html#tools-run-register) là SSOT trạng thái; AI đọc đầu/cuối lượt. Chưa đạt production, chưa triển khai DOT mới. Hai đường đi: 1→3 hoặc 1→2→3.
Phiếu kiểm trang hướng dẫn: `UI-REVIEW-TOOLS.json`; không dùng kết quả trang hướng dẫn thay kết quả hành trình tìm Field.

## Rà lại MOW001 · 09/10/2026
Phiếu hiện hành vẫn [UI-REVIEW-MOW001.json](UI-REVIEW-MOW001.json), mục `process_trial_20261009`: đáp án 44 mã câu, hợp đồng thiết kế A/B/C do Host tiếp nhận, 7 Config×3, 24 ô UI cũ và 14 ca Host bấm trình duyệt. Đã xác định thiếu nguồn thật, máy đánh giá và gói kết luận B1; toàn UI còn PARTIAL/FAIL, chưa production. Quy tắc ghép ghi chú riêng ở [tools-quy-trinh README](../tools-quy-trinh/README.md), không tạo phiếu/nguồn quy định song song. Sửa UI001 tiếp theo phải bám đáp án trong phiếu; chưa MOW002.

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
