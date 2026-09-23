# COLLAB — mow-mot-moit-mout

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
- Mục tiêu: tiếp tục hồ sơ MOW · MOT · MOIT · MOUT từ đúng file gốc Owner đang làm và xây kho thông tin liên quan có tổ chức để phục vụ rà soát/phát triển tiếp.
- Nhiệm vụ/phạm vi hiện tại (Owner 23/09/2026): sau khi đã có vỏ tab Step quy trình, Host phải đề xuất **bản đồ thao tác thật** từ dưới lên Field → Form (MOUT, MOIT) → MOT → MOW: tạo bắt đầu ở đâu, bấm gì, người khai tay gì, máy config gì, phụ thuộc tầng dưới xử lý ra sao, kết quả mong đợi, lỗi quay về đâu, tạo xong quản lý ở UI nào và quản lý thông tin gì. Đồng thời đề xuất deep-link để URL ngoài `/knowledge/modules?task=...` phản ánh tới tab/khu vực/bảng con/bước đang xem. Đây là lượt thiết kế/consensus với Claude; **chưa điền HTML theo đề xuất trước khi hội đồng thống nhất**.
- Tiêu chí xong của lượt thảo luận: COLLAB có schema Step chuẩn + draft bước cho đủ Field/MOUT/MOIT/MOT/MOW + quy tắc nhánh “đã có thì chọn / chưa có thì tạo tầng dưới rồi quay lại” + đối chiếu UI hiện có + yêu cầu URL deep-link có acceptance test; Claude review và Host hòa giải trước khi giao Agent sửa HTML.
- Xác nhận User: **ĐÃ XÁC NHẬN** — Owner giao trực tiếp 2026-09-20 và yêu cầu đưa kho tham khảo lên GitHub ngày 2026-09-23; D01–D05, D12–D16 của việc này. D16 là yêu cầu trực tiếp tạo tab/vỏ bảng của Owner, cho phép sửa HTML chính trong phạm vi này.

Host: GPT Chat · Host_ID: GPT-MMIM-260920-A · Owner giao: 2026-09-20
HTML chính: `mow-mot-moit-mout.html`
File gốc Owner giao: `mow-mot-moit-mout.html` · SHA-256 `f4aac30c492f104ec54ff7a03ace54ce70d802e2dd49a417ad9b7285897a050c` · import nguyên byte ở commit `569bb74300a15d05e455bf917fe4058f7f7fd499`.
Kho thông tin: `information/`
Agent prompt: `PROMPT.md`

## Dòng hiện hành
MMIM | PROCESS_MAP_DESIGN · 23/09/2026 | Vỏ Step quy trình đã có; Host đang đề xuất bản đồ thao tác thật + deep-link URL tới tab/bảng/bước. Chưa sửa nội dung bảng; NEXT: Claude review MAP01–MAP05 + URL01.

## Quyết định Owner
- D01 · 2026-09-20 · Mở công việc tại `work/mow-mot-moit-mout/`.
- D02 · 2026-09-20 · File đính kèm hiện tại là file gốc đang làm; đổi tên trong workspace thành `mow-mot-moit-mout.html`.
- D03 · 2026-09-20 · Phải đưa file gốc lên workspace trước rồi mới viết prompt/giao Codex phần còn lại.
- D04 · 2026-09-20 · Codex tạo `work/mow-mot-moit-mout/information/`, tự đề xuất cách tổ chức bên trong và đưa các file cần thiết/liên quan từ `/Users/nmhuyen/Desktop/quy trình` vào đó.
- D05 · 2026-09-20 · Lượt Codex này chỉ khảo sát, phân loại và copy tài liệu; không được sửa, đổi tên hoặc tái cấu trúc `mow-mot-moit-mout.html`, không xoá/di chuyển nguồn trên Mac.
- D06 · 2026-09-20 · `work/mow-mot-moit-mout/mow-mot-moit-mout.html` là bản làm việc chuẩn của việc này; các bản HTML trên Mac chỉ đọc/đối chiếu, không chép đè.
- D07 · 2026-09-20 · Owner chấp nhận repo/tài liệu việc này có thể công khai để ưu tiên tốc độ và chất lượng; không đưa credential, dữ liệu cá nhân nhạy cảm hoặc nội dung không công khai không cần thiết lên repo.
- D09 · 2026-09-21 · Áp dụng DROOT04 cho MMIM.2: Host không tách PRECHECK riêng cho môi trường Codex đã dùng nhiều lần; RUN phải bắt đầu bằng việc vào đúng repo `incomex-workspace`, cập nhật `main` an toàn và đọc AGENTS → COLLAB → PROMPT. Chỉ mutation sau khi gate đầu vào của chính MMIM.2 PASS.
- D10 · 2026-09-21 · Owner yêu cầu Host sửa gói cuối, sau đó chuyển Claude review để đạt đồng thuận; **chưa READY/RUN Codex trước review Claude**.
- D11 · 2026-09-21 · Theo Owner: MMIM.2 dùng **Executor_Surface = Codex**. Quyền kỹ thuật theo capability đã audit, không theo hãng. `Write_Path` ưu tiên `workspace_*`; nếu chính phiên Codex không bind `workspace_*` nhưng bind `fs_*` đã audit thì dùng `fs_*`. Không dùng Git/CLI/native để ghi. Host giám sát qua gate + repo/diff/report cuối.

- D12 · 2026-09-23 · Owner trực tiếp yêu cầu đưa các file có giá trị từ Mac lên GitHub thành kho tham khảo dài hạn; đặc biệt hai HTML thiết kế nêu trên. Thực hiện yêu cầu mới bằng `workspace_*` đã đọc-gate PASS; không chạy PROMPT MMIM.2 nháp, không tự chốt P01. Không đưa credential/dữ liệu nhạy cảm lên public. Hai HTML lớn truyền bằng mã giữa công cụ, không tái tạo nội dung qua mô hình. · Áp: SAME_COMMIT.

- D13 · 2026-09-23 · Owner: “Ảnh thì không nên chuyển lên Gh vì nó làm nhanh làm đầy repo nhé.” Loại toàn bộ file ảnh khỏi kế hoạch Git; chỉ giữ metadata/hash/nguồn trong inventory và LINK-MAP. Chưa publish ảnh nơi khác, chưa sửa đường dẫn HTML; quyết định này không cấp ngoại lệ Git trực tiếp cho Office. · Áp: SAME_COMMIT.

- D14 · 2026-09-23 · Owner yêu cầu dọn cũ/trùng, không thiếu nguồn nhưng nhẹ nhất và ít tốn token; UI thiết kế đã có trên VPS chỉ giữ link, có thể tham khảo JEV. Hủy đề nghị upload lô 97 Office ở Q01. Bản nguyên gốc được tra qua commit cố định, không gom vào archive khác trong repo. Không đổi HTML chính/Mac/VPS hoặc rewrite lịch sử. · Áp: SAME_COMMIT.

- D15 · 2026-09-23 · Owner: “Đồng ý cho ngoại lệ. Làm cho gọn trên Git nhưng không miss thông tin quan trọng đã làm là được”. Chấp thuận Q02: dùng Git trực tiếp một lần để xóa đúng 888 file `information/reference/**`, cập nhật mục lục/COLLAB, commit/push thường; giữ HTML chính, nguồn Mac, VPS và lịch sử Git. · Áp: SAME_COMMIT.

- D16 · 2026-09-23 · Owner yêu cầu thêm tab “List quy trình” và vỏ bảng, đi từ Field → Form (MOUT, MOIT) → MOT → MOW, đủ bảy cột đã nêu ở A0. Đây là lượt sửa HTML mới sau thu thập/dọn kho, không còn áp dụng yêu cầu giữ nguyên hash HTML của lượt MMIM.2 cho thay đổi được giao này. Không điền sẵn quy trình; không sửa Mac hoặc runtime. Executor_Surface=Codex; Write_Path=workspace_transaction, read-gate workspace_stat PASS. · Áp: SAME_COMMIT.

- D17 · 2026-09-23 · Theo yêu cầu trực tiếp Owner: đổi tên List quy trình thành Step quy trình; đưa tab ngay sau UI Master và trước Quy trình. Giữ nguyên các bảng và ID liên kết. · Áp: SAME_COMMIT.

- D18 · 2026-09-23 · Owner yêu cầu giải thích thống nhất hai cột tổng ở Step quy trình: bảng tổng hợp chỉ hiện số tổng; danh sách trường nằm ở bảng chi tiết, mỗi bảng có mã riêng để quản lý/khai báo. Quy ước chuẩn đặt tại HTML chính `#step-quy-trinh-quy-uoc`; AI đọc mục này trước khi điền. Đổi nhãn thành “Tổng số trường cần config”; chưa tạo bảng chi tiết/cấp mã/điền số. · Áp: SAME_COMMIT.

- D19 · 2026-09-23 · Owner yêu cầu Host **chưa cho Agent tự mò tiếp** mà phải định nghĩa bản đồ quy trình chi tiết trước: đi từ Field → Form/MOUT/MOIT → MOT → MOW; mỗi quy trình phải nêu bước thao tác, UI, hành động, input tay, config máy, kết quả, nhánh lỗi/phụ thuộc và nơi quản lý sau tạo. MOW bắt buộc có nhánh “MOT đã có → chọn/gắn; chưa có → chạy quy trình tạo MOT → quay lại đúng bước MOW”. Owner đồng thời yêu cầu URL ngoài thay đổi theo tab/khu vực/bảng con để trao đổi chính xác. Lượt này Host đề xuất → Claude review → Owner chốt; chưa sửa bảng Step theo đề xuất.

## Đề xuất Host · MAP01–MAP05 + URL01 · chờ Claude review

### MAP01 · Step quy trình là bản đồ **tạo/khai thật**, không lặp tab Vòng đời
- Tab Vòng đời hiện đã có khung 8 trạng thái `Tìm → Tạo → Master → Config → Test → Dùng → Chạy → Ngừng`; giữ nguyên để quản lý vòng đời.
- Tab **Step quy trình** trả lời câu hỏi khác: “Từ lúc cần tạo một đối tượng cho tới lúc nó được lưu, quản lý và trả về nơi gọi thì người/máy thực sự làm những thao tác nào?”.
- Giữ bảy cột tổng hiện tại để nhìn nhanh. Mỗi `Mã Bước` phải mở một **bảng chi tiết có mã ổn định** với các trường bắt buộc:
  `Điểm vào/UI · Bấm/Hành động · Khai tay · Config máy · Phụ thuộc/nhánh · Kết quả mong đợi · Lỗi/quay về · Nơi quản lý sau tạo · Thông tin quản lý · Bằng chứng UI`.
- Cột “Tổng số trường cần khai/config” chỉ lấy số đếm từ bảng chi tiết; không nhập số bằng suy đoán.

### MAP02 · Một quy tắc nhánh dùng chung cho mọi tầng
Khi đối tượng X cần đối tượng tầng dưới Y:
`đến bước cần Y → Tìm Y → [đã có: chọn/gắn Y] | [chưa có: gọi PROCESS(Y).CREATE → Y PASS → quay lại đúng bước đang chờ của X → gắn Y] → test chỗ nối → đi tiếp`.
- Không “nhảy tiếp” nếu Y chưa PASS.
- Phải lưu `return_to_step`/mã bước gọi để agent và UI biết quay về đâu.
- Áp dự kiến: MOIT/MOUT cần Field; MOT có thể cần MOIT/MOUT; MOW cần MOT. Claude cần rà phạm vi bắt buộc/tuỳ chọn của từng phụ thuộc.

### MAP03 · Draft số bước thao tác V1 — để cùng rà, **chưa phải nghiệm thu**
**FIELD · đề xuất 6 bước**
1. `FIELD.S01` Tìm Field hiện có.
2. `FIELD.S02` Có → chọn/dùng lại; chưa có → bấm `+` tạo Field.
3. `FIELD.S03` Khai tay phần định danh/nghĩa nghiệp vụ. Nguồn UI hiện cho thấy ít nhất: **tên, định dạng, mô tả, nhóm quản lý**; chỉ chốt trường sau khi rà UI-018.
4. `FIELD.S04` Máy tạo/cấu hình phần kỹ thuật cần thiết; danh sách config phải lấy từ UI/contract, không tự đoán.
5. `FIELD.S05` Test/validate Field và chỗ dùng.
6. `FIELD.S06` Lưu/đăng ký → quản lý ở Master Field → trả `field_id/version` về nơi gọi.
UI nguồn hiện thấy: UI-018 “Field · khai báo trường”; UI-022 “Master Field”; UI-021 Kanban FIELD. **Có mâu thuẫn nguồn cũ “chưa có UI quản lý Field theo Owner” với catalogue UI con “đã có”; cần tách `UI tồn tại` và `Owner đã chốt cho bước`.**

**MOUT · đề xuất 7 bước**
1. `MOUT.S01` Tìm MOUT hiện có trong Master.
2. `MOUT.S02` Có → chọn; chưa có → mở Builder tạo MOUT.
3. `MOUT.S03` Khai tay ý nghĩa báo cáo/khuôn: miền dữ liệu, cột, filter, thời gian, tổng, phân phối theo nhu cầu nghiệp vụ.
4. `MOUT.S04` Với Field cần dùng: đã có → chọn từ kho Field; thiếu → gọi PROCESS(FIELD).CREATE rồi quay lại.
5. `MOUT.S05` Máy sinh/hoàn thiện config kỹ thuật/JSON/output từ khai báo.
6. `MOUT.S06` Preview/“đúc”/test báo cáo.
7. `MOUT.S07` Lưu/đăng ký Master MOUT → trả `mout_id/version` về nơi gọi.
UI nguồn hiện thấy: Builder v3, Master MOUT UI-014, Studio MOUT UI-016, Kanban UI-020.

**MOIT · đề xuất 8 bước**
1. `MOIT.S01` Tìm MOIT hiện có trong Master.
2. `MOIT.S02` Có → chọn; chưa có → tạo draft MOIT.
3. `MOIT.S03` Khai tay mục đích/form nhận dữ liệu và danh sách thông tin cần nhập/đọc.
4. `MOIT.S04` Mỗi Field: có → chọn; thiếu → PROCESS(FIELD).CREATE → quay lại.
5. `MOIT.S05` Khai tay các quyết định nghiệp vụ: nguyên tắc nhập, ai nhập/ai nhận, chạy/kết thúc.
6. `MOIT.S06` Máy config binding kỹ thuật. UI-017 hiện có các cột: Collection, Field, Check tương tự, địa chỉ dữ liệu, kiểu dữ liệu, hợp đồng JSON, Test, tình trạng, ghi chú; cần rà cái nào máy tự làm/cái nào người duyệt.
7. `MOIT.S07` Test form/input end-to-end.
8. `MOIT.S08` Lưu/đăng ký Master MOIT → trả `moit_id/version` về MOT/nơi gọi.
UI nguồn hiện thấy: Master UI-013, Studio UI-015, Config UI-017, Kanban UI-019.

**MOT · đề xuất 8 bước**
1. `MOT.S01` Tìm MOT hiện có trong Master.
2. `MOT.S02` Có → chọn; chưa có → tạo khung công việc MOT/T1.
3. `MOT.S03` Khai tay định danh/mục đích công việc.
4. `MOT.S04` Gắn MOIT đầu vào khi cần: có → chọn; thiếu → PROCESS(MOIT).CREATE → quay lại.
5. `MOT.S05` Gắn MOUT tham khảo/đầu ra khi cần: có → chọn; thiếu → PROCESS(MOUT).CREATE → quay lại.
6. `MOT.S06` Khai nghiệp vụ + máy config: nguyên tắc giao việc, ai làm/ai nhận, chạy/kết thúc; mapping GHI VÀO/ĐỌC RA và binding kỹ thuật theo UI.
7. `MOT.S07` Test công việc end-to-end và các nối MOIT/MOUT.
8. `MOT.S08` Lưu/đăng ký Master MOT → trả `mot_id/version` về MOW. Sau tạo vận hành ở Bàn làm việc/Kanban.
UI nguồn hiện thấy: Master MOT, Config UI-006, Studio UI-007, Bàn làm việc UI-010, Kanban UI-028.

**MOW · đề xuất 9 bước**
1. `MOW.S01` Tìm MOW hiện có trong Master.
2. `MOW.S02` Có → mở/sửa đúng bản; chưa có → `+ Tạo quy trình (MOW)`.
3. `MOW.S03` Khai tay định danh + neo cây/tầng/phạm vi của quy trình.
4. `MOW.S04` Khai từng bước quy trình và **chọn MOT** cho bước.
5. `MOW.S05` Nhánh bắt buộc: MOT có → gắn; MOT chưa có → PROCESS(MOT).CREATE → nhận `mot_id/version` → quay lại đúng `MOW.S04`.
6. `MOW.S06` Sắp thứ tự/nhánh/handoff/hội tụ giữa các MOT.
7. `MOW.S07` Khai quyết định nghiệp vụ + máy config event/checkpoint/data/role/điều kiện theo thiết kế đã chốt.
8. `MOW.S08` Test end-to-end toàn MOW, gồm chỗ nối MOT.
9. `MOW.S09` Lưu/đăng ký Master MOW và đưa vào quản lý/vận hành.
UI nguồn hiện thấy: Master MOW UI-001, Kanban MOW, chi tiết MOW, checkpoint, data-events. Master hiện đã có nút `+ Tạo quy trình (MOW)`.

### MAP04 · “Khai tay” và “Config máy” phải tách bằng trách nhiệm, không chỉ bằng cột
- **Người khai:** nghĩa nghiệp vụ, lựa chọn thành phần đã có, tên/mục đích, điều kiện/quy tắc mà Owner/nghiệp vụ phải quyết.
- **Máy config:** tạo mã/khoá/binding kỹ thuật, materialize JSON/địa chỉ dữ liệu/contract/event/checkpoint từ quyết định đã khai, chạy validation/test tự động.
- Mọi trường config máy vẫn phải hiện trong bảng chi tiết với nguồn và trạng thái; “máy làm” không có nghĩa “không quản lý”.
- Mỗi step phải có `manual_count`, `config_count`, và danh sách chi tiết tương ứng trước khi số tổng xuất hiện ở bảng Step.

### MAP05 · Sau khi tạo, phải chốt “quản lý ở đâu / quản lý gì”
Mỗi đối tượng có hai câu riêng:
1. **Registry/Master ở đâu?** nơi tìm, version, trạng thái, ngừng/lưu trữ.
2. **Workspace/Canvas ở đâu?** nơi dùng/vận hành/chỉnh config nếu có.
Tối thiểu quản lý: `ID/code · tên · version · trạng thái · nơi dùng/parent refs · người/quyền · config status · test status · updated_at/source`. Bộ trường cuối phải rà từng UI, không lấy danh sách này làm schema thật nếu UI/contract chưa xác nhận.

### URL01 · Deep-link tới đúng tab → bảng → bước → bảng chi tiết
**Hiện trạng:** HTML con đã đổi hash nội bộ như `#matrix-view-process-list`, nhưng URL ngoài vẫn chỉ là `/knowledge/modules?task=mow-mot-moit-mout`; khi dùng iframe/view wrapper thì hash của HTML con không phản ánh ra URL ngoài, nên gửi link không chỉ đúng chỗ đang nói.

**Đề xuất URL chuẩn ở viewer ngoài:**
`/knowledge/modules?task=mow-mot-moit-mout&view=process-list&section=field&step=FIELD.S03&detail=FIELD.S03.INPUT`
- `view`: tab lớn, dùng key hiện có `master | process-list | process | blockers | ui | uses | lifecycle | all | reference`.
- `section`: bảng/khu vực ổn định, ví dụ `field | mout | moit | mot | mow`.
- `step`: mã bước ổn định.
- `detail`: bảng con/record cụ thể nếu đang mở.
- Click tab/bảng/row/detail → parent URL `history.replaceState/pushState` cập nhật ngay, không reload.
- Mở URL trực tiếp/reload/back/forward → viewer khôi phục đúng tab, mở đúng bảng/detail và scroll/focus đúng mục.
- Nếu HTML chạy trong iframe: child gửi state bằng `postMessage` cùng-origin/whitelist; parent cập nhật URL và khi load gửi route xuống child. Không cho arbitrary selector/code qua message.
- Giữ tương thích hash cũ: `#matrix-view-...` vẫn route được và được chuẩn hoá sang query khi mở qua viewer.

**Acceptance URL01**
1. Copy link ở Step→MOT→`MOT.S04`, dán tab mới → mở đúng vị trí.
2. Click UI Master ↔ Step quy trình → URL `view=` thay đổi.
3. Click Field/MOUT/MOIT/MOT/MOW → `section=` thay đổi.
4. Mở step/detail → `step/detail` thay đổi.
5. Back/Forward khôi phục UI đúng trạng thái.
6. URL không hợp lệ → fallback về tab hợp lệ gần nhất, không blank/crash.
7. Không làm mất `task=mow-mot-moit-mout`.

### Câu hỏi Host gửi Claude
- C01 · Có đồng ý **Step quy trình = bản đồ thao tác tạo/khai**, không lặp 8 trạng thái Vòng đời?
- C02 · Các số bước V1 (Field 6 · MOUT 7 · MOIT 8 · MOT 8 · MOW 9) có chỗ nào nên gộp/tách trước khi điền UI?
- C03 · Phụ thuộc tầng dưới nào là bắt buộc/tuỳ chọn: MOIT↔Field, MOUT↔Field, MOT↔MOIT/MOUT, MOW↔MOT?
- C04 · Có đồng ý tách trạng thái UI thành `EXISTS` / `OWNER_APPROVED_FOR_STEP` / `NEEDS_FIX` thay vì một ô Check UI nhị phân?
- C05 · URL01 dùng query state ở parent + postMessage khi iframe có phải giải pháp ít sửa và bền nhất với viewer hiện tại không?

## Kế hoạch
- MMIM.1 | Tạo work + import file gốc, đổi tên thống nhất | ✅ `569bb74300a15d05e455bf917fe4058f7f7fd499`
- MMIM.2 | Codex khảo sát thư mục nguồn, copy text/lightweight + inventory binary + lập mục lục | ◐ DRAFT · chờ Claude review

## Ý kiến (P)
Reviewer: Claude Chat · Based_on `39cc96d` / commit review `f5f97fc`. Host GPT đã đối chiếu lại HTML chính và README §12 trước khi xử lý.

- P01 · Scope COLLAB §0 · **REJECTED trong lượt này** · Claude đề nghị mở rộng mục tiêu toàn việc sang “thiết kế chuẩn UI + quy trình tạo/khai báo thành công MOW/MOT/MOIT/MOUT/Field”. Đây là thay đổi A0; trong tin nhắn hiện tại Owner chỉ quyết rõ việc công khai có lọc nhạy cảm, chưa xác nhận lại câu mục tiêu rộng đó. Giữ nguyên §0 đã xác nhận. Khi Owner xác nhận mục tiêu rộng, mở D mới và cập nhật A0 riêng; không dùng lời Reviewer để thay Owner. · Claude vòng 2 (Based_on `17b5470`): câu mục tiêu không phải đề xuất của Reviewer mà là nguyên văn Owner gõ khi giao Claude review (chat 2026-09-20). Đồng ý A0 cần Owner xác nhận rõ → chuyển **OWNER**. Không chặn MMIM.2 (thu thập không mâu thuẫn mục tiêu rộng).
- P02 · Scope PROMPT §2A/§3/§6 · **PARTIAL** · ACCEPT chẩn đoán NFD và yêu cầu `LINK-MAP`; GPT kiểm thật meta `project-assets-root` ghi NFD và README §12.3 hiện chỉ mirror một HTML. Không nhận đề nghị đưa `assets/` ra cạnh HTML ngay trong MMIM.2 vì D04–D05 của Owner yêu cầu lượt này chỉ gom vào `information/` và cấm sửa sản phẩm. PROMPT mới stage phụ thuộc dưới cha ASCII `information/direct-dependency/source-assets/`, kiểm 16 ảnh + manifest + mọi file-ref tương đối. Việc đổi đường dẫn HTML/Owner View là lượt riêng sau MMIM.2, chưa RUN.
- P03 · Scope public safety · **ACCEPTED theo quyết định Owner 2026-09-20** · repo được phép công khai để ưu tiên tốc độ/chất lượng; chỉ loại thông tin thật sự quá nhạy cảm/không cần thiết. PROMPT chặn credential/secret, định danh cá nhân rủi ro, dữ liệu tài chính/cá nhân và tài liệu không công khai cần bảo vệ; không tự loại tên người/tên công ty/thông tin nghiệp vụ công khai. File >50MB hoặc tổng >250MB được ghi nhận để tránh làm chậm/đẩy file lớn.
- P04 · Scope đúng bản · **ACCEPTED** · bản repo `mow-mot-moit-mout.html` là working SSOT của việc; Mac read-only. Codex đọc các sổ chỉ đường nếu có, so SHA bản Mac và SHA nguồn được HTML ghi; lệch thì ghi divergence, không chép đè.
- P05 · Scope UI runtime · **ACCEPTED** · UI đang chạy lấy VPS root `ui` làm thực địa theo A8; bản HTML/JS/CSS tương ứng trên Mac không được xếp CURRENT. Nếu cần đối chiếu thì LEGACY/MAC_RUNTIME_COPY; MMIM.2 không fetch runtime VPS.
- P06 · Claude · Based_on `6f15da7` · Scope PROMPT §0 + §7 / README D12 · **ACCEPTED theo nguyên tắc Owner, sửa căn cứ** · Nhận đúng yêu cầu phải gọi tên Write_Path và test đúng một read-gate trước mutation. Không nhận cách hiểu “GPT key/Claude key”: DROOT06/README đã sửa capability-first. MMIM.2 chốt `Executor_Surface=Codex`; primary `Write_Path=workspace_*`, fallback `fs_*` nếu chính phiên Codex bind path đó; cấm Git/CLI/native write. Prompt phải ghi tên tool family + gate; Agent không tự suy và không đổi vai giữa chừng.
- P07 · Claude · Based_on `6f15da7` · Scope PROMPT §0.4 · §5 · §6 · §7 · **ACCEPTED có siết chống chọn nhầm nguồn** · (a) so commit cuối chạm PROMPT, không so HEAD; phạm vi thay đổi chỉ tính mutation do Codex tạo. (b) text >100 KB không relay qua model: inventory `PENDING_LARGE_TEXT` + bytes/SHA, xử lý như external/shared asset sau. (c) transport đổi newline/BOM thì ghi `NORMALIZED_BY_TRANSPORT` + SHA hai bên, không retry vòng lặp; nội dung phải được xác nhận tương đương text. (d) `OUTCOME_UNKNOWN` → read-back/journal/idempotency, không ghi lại mù. (e) ưu tiên path Owner đã chỉ; nếu lookup lỗi do Unicode/path thì resolve trong Desktop trước, sau đó Documents/Google Drive cục bộ; nếu nhiều candidate phải đối chiếu marker/SHA, không chọn chỉ vì trùng tên.
- P08 · Claude · Based_on `2d673a3` · Scope PROMPT §0.5 · §2 · §6 · §7 · **OPEN — 4 câu chèn nguyên văn, không cần vòng review nữa** · R2 đã gỡ đúng gốc I02 (Write_Path gọi tên + read-gate đầu). Còn 4 đường có thể làm Codex DỪNG oan hoặc chạy quá tốn. Đã kiểm nguồn connector: family `workspace_*` có `workspace_log`/`workspace_stat`/`workspace_write_new`/`workspace_transaction`; family `fs_*` có `fs_log`/`fs_stat` — đủ để làm hết bằng đúng family đã qua gate. Chèn nguyên văn: (1) §0 bước 5, thêm: “Tra commit cuối chạm `PROMPT.md` bằng `workspace_log`/`fs_log` của chính Write_Path; không dùng clone local (clone local cũ là nguyên nhân I01).” (2) §7, thêm: “Nếu guard bí mật của Write_Path từ chối một file: KHÔNG sửa/che nội dung để lọt guard; bỏ file đó khỏi lô, ghi `OMITTED_SECRET_GUARD` + path + SHA nguồn vào README, ghi lại phần còn lại của lô và tiếp tục. Đây không phải lý do DỪNG.” (lý do: tài liệu cũ trong `quy trình/` rất có thể chứa URL connector có token; hiện dòng cuối prompt ghi “secret không xử lý an toàn → DỪNG” → một file bị guard chặn có thể dừng cả lượt, và transaction nhiều file bị hủy cả lô.) (3) §2 cuối, thêm: “Lớp D chỉ inventory, không copy. Tổng nội dung text relay qua model cả lượt ≤300 KB, ưu tiên A → B → C; vượt ngân sách → phần còn lại `PENDING_LARGE_TEXT`. Ghi theo lô nhỏ (≤10 file/commit), không dồn một transaction khổng lồ.” (lý do: ngưỡng 100 KB/file chưa chặn tổng — 20 file × 90 KB vẫn là khối output rất lớn, dễ tràn ngữ cảnh/timeout và tốn tiền.) (4) §6, sửa dòng “mỗi file text đã copy có hash nguồn = hash đích” thành “… = hash đích **hoặc `NORMALIZED_BY_TRANSPORT` theo §5**” (hiện §5 cho phép nhưng §6 cấm → Codex đọc chặt sẽ tự đánh trượt).

Claude REVIEWED@2d673a370a030e2b679d161132cb908f897b9503 · **ACCEPT có điều kiện P08** — Host chèn đúng nguyên văn 4 câu P08 thì coi như Claude đã ACCEPT bản mới, Host đặt READY luôn, không cần gửi Claude review lại. Ngoài 4 câu này, mọi sửa khác vào PROMPT vẫn phải review theo A6. HTML chính kiểm lại: SHA `f4aac30c…a050c` PASS.

## Phương án Host chờ Claude review
- H01 · **ACCEPTED + mở rộng:** Git chỉ giữ HTML, text nhỏ (≤100 KB/file), README, `assets-manifest.json` và LINK-MAP. Binary và text >100 KB không relay qua model/không commit ở MMIM.2; chỉ inventory bytes/SHA/path/state để shared-assets/external step sau.
- H02 · **Shared assets ngoài Git:** sau MMIM.2, publish binary một lần vào kho static HTTPS dùng chung để GPT/Claude/Codex/Hermes và Owner View cùng đọc bằng URL tuyệt đối. Ưu tiên tái dùng hạ tầng static hiện có; không mở dự án sửa MCP/connector. Repo giữ SHA/bytes/URL làm SSOT metadata. Cơ chế/path publish cụ thể phải được Claude phản biện trước khi Host chốt MMIM.3.
- H03 · MMIM.2 không được DỪNG chỉ vì connector không nhập binary; binary pass ở lượt này = định vị + SHA/bytes + manifest/link-map.

**Claude trả lời H01–H03 (Based_on `6f15da7`):**
- H01 · **ACCEPT + bổ sung**: tách đúng hướng, nhưng tiêu chí thật không phải “binary hay text” mà là **file có phải đi qua ngữ cảnh của mô hình hay không**. Text lớn (ví dụ `00-NGUON-THIET-KE.html`, `cấu trúc hệ thống.html`) khi đẩy qua connector vẫn phải chạy qua mô hình → vừa tốn vừa có nguy cơ sai byte. Chi tiết ở P07b.
- H02 · **Đồng ý nguyên tắc, chưa chốt được đường đi**: binary ngoài Git + URL tuyệt đối + repo giữ metadata là đúng và hợp README §11.5/§12. Nhưng hiện **chưa tồn tại đường vận chuyển binary nào đã nghiệm thu**: Codex không nhập được binary (I02), `fs_write` của Claude chỉ nhận text, và dựng endpoint upload mới = sửa dịch vụ VPS (ngoài phạm vi, đúng như Host đã loại). Đề nghị: không chốt cơ chế bây giờ; MMIM.2 cứ chạy với inventory. Đến bước shared-assets mới chọn, và ứng viên rẻ nhất lúc này là Owner upload MỘT lần đúng 16 ảnh vào vùng static hiện có, có hướng dẫn từng bước — không dựng hạ tầng mới, không sửa connector.
- H03 · **ACCEPT**: đúng nguyên nhân gốc của I02 về phần binary.

## Owner cần quyết
- P01 · Xác nhận mục tiêu toàn việc (A0): “thiết kế chuẩn các UI, chuẩn quy trình tạo và khai báo thành công MOW/MOT/MOIT/MOUT/Field”; tiêu chí xong = mỗi đối tượng có UI chuẩn Owner chốt + quy trình tạo/khai báo viết thành bước + ≥1 lần khai báo thật thành công có bằng chứng. P01 không chặn Claude review/MMIM.2 hiện tại.

## Sự cố / bài học Host
- I01 · 2026-09-21 · Codex trả: `DỪNG · MMIM.2 · Workspace hiện tại không có work/mow-mot-moit-mout/COLLAB.md và PROMPT.md; không thể xác minh ba gate bắt buộc. Chưa thay đổi file nào.` → Host đã sửa bootstrap/input gate.
- I02 · 2026-09-21 · Codex trả: `DỪNG · MMIM.2 · Gate công cụ ghi chưa đạt: README §0/D12 cấm AI push bằng Git/CLI; connector hiện có chưa có đường nhập ảnh nhị phân từ Mac đáp ứng giao dịch bắt buộc. Chưa tạo information/ hoặc sửa nguồn, HTML, COLLAB.`
- Kết luận Host I02: prompt sai kiến trúc khi bắt binary đi vào Git. Sửa nguyên nhân gốc: MMIM.2 không đưa binary vào Git; chỉ inventory/hash. Shared-assets ngoài Git là bước riêng sau consensus, không sửa connector.

## Giao Agent — lịch sử prompt MMIM.2 trước yêu cầu mới 23/09
- READY@`7d8e1df9e50cfdd5a4b7cfaf8c66cad9343e26f3` → **HẾT HIỆU LỰC** vì Host đã sửa `PROMPT.md` sau I02.
- **NO RUN** theo D10. Chờ Claude review bản prompt mới và H01–H03.

## Lịch sử nhập kho trước D14 (không phải chỉ dẫn đọc hiện hành)
- Executor_Surface: Codex · Write_Path: `workspace_*` · read-gate PASS. Theo lệnh trực tiếp Owner mới, không chạy PROMPT MMIM.2 nháp và không tự đặt READY cho bản nháp.
- Đã commit/push 888 tài liệu nguyên byte, 87.874.934 bytes; gồm cả hai HTML ưu tiên. Commit nhập cuối: `42e2db1ce50dd42563351aa252145fed541ffa76`; các commit nhập từng file nằm trong inventory lịch sử tại `b2666914babf884670d80597d639609681f9d3ea` (link ở README).
- Đọc lại blob Git: 888/888 SHA nguồn = đích. Kiểm lại 2.155/2.155 file Mac: hash không đổi. HTML chính SHA `f4aac30c492f104ec54ff7a03ace54ce70d802e2dd49a417ad9b7285897a050c` giữ nguyên.
- Sau D13: 97 Excel/Word/10.507.371 bytes chưa publish; 207 ảnh khác nhau/35.582.774 bytes không đưa lên Git. 16/16 ảnh manifest nguồn đúng hash/bytes; chỉ giữ metadata. Phần bỏ/chờ/trùng ghi trong inventory; không tuyên bố đã chuyển hết, không nghiệm thu nghiệp vụ, không chạm VPS/runtime.
- Mục lục, inventory và LINK-MAP: `information/README.md`. · Áp: SAME_COMMIT.

- Ghi nhận dung lượng: 3 HTML tham khảo đã lưu nguyên bản chứa khoảng 12,22 MB chuỗi ảnh nhúng. Đã loại ba bản chép đó cùng lô 888 khỏi cây hiện tại theo D15; bản lưu lịch sử không sửa.

## Kết quả rà dọn D14
- JEV: `gen-dec-1790115453-3T8Uh0LawUeGYjT756bc`, model do gateway trả `typesafe/jev-1.13-20260917`; năm nhóm đều ưu tiên link lịch sử hoặc VPS, không giữ toàn bộ bản chép trong phần đọc hằng ngày.
- 15 URL kiểm GET TLS, HTTP 200; mục lục giữ 14 link không trùng (URL Kanban trơn gộp vào URL Owner có query). Đây không phải nghiệm thu chức năng/UI/PG. Web reader và browser connector không dùng được; curl kiểm đọc thành công, không ghi VPS.
- Link tài liệu gốc cố định tại `b2666914babf884670d80597d639609681f9d3ea`; hai tài liệu thiết kế quan trọng vẫn truy nguyên byte. Không giả định URL UI là bản thay thế cho tài liệu.
- Đã xóa chính xác: 888 file/87.874.934 bytes dưới `information/reference/`. Xóa cây không thu hồi lịch sử Git; không hứa giảm dung lượng lưu GitHub tương ứng. Ở thời điểm rà, clone local báo object rời 4,49 MiB + pack 10,71 MiB; API GitHub trả size 1.824 KiB có thể cập nhật chậm, không dùng làm số tiết kiệm.
- Bốn file chỉ dẫn/metadata đã thay bằng bản gọn; hoàn tất xóa theo D15. Kiểm trước xóa: 888/888 file khớp manifest SHA-256, blob hiện tại bằng blob lịch sử; 11/11 nguồn Mac được chọn khớp SHA. HTML chính khớp SHA đầy đủ ghi ở đầu hồ sơ. Không chuyển rác sang archive trong repo. · Áp: SAME_COMMIT.

## Kiểm tra tab List quy trình
- Bản xem thử trên trình duyệt: mở đúng tab bằng hash và nút; đủ Field, Form/MOUT, Form/MOIT, MOT, MOW, bảy cột và ba hàng trống mỗi bảng. Chuyển sang Quy trình và UI Master hiển thị đúng nội dung cũ. Bảng cuộn ngang trên màn hình hẹp. Chưa có dữ liệu để đánh Check UI; không thêm lưu dữ liệu hoặc bảng con. · Áp: SAME_COMMIT.

## NEXT
- Cùng Owner đi từng bước để điền Step quy trình; chưa tự khai bước, số trường hoặc đánh Check UI. P01 vẫn chờ Owner, không tự chốt mục tiêu rộng.
