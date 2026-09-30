# COLLAB — MMIM Lane A · Gate / Catalog Law / Tool

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
Xác nhận User: **ĐÃ XÁC NHẬN** — Owner 28/09/2026 yêu cầu Lane A/B/C bền qua phiên; Lane A phụ trách nền tích lũy, gate, tool và luật catalog.

### 1. Mục tiêu
Biến Process/Tool đã chốt thành dữ liệu có thể kiểm bằng máy; không phụ thuộc trí nhớ phiên.

### 2. Thế nào là hoàn thành
A02 nâng process-gate để kiểm được contract metadata của Human Step mà B02 chuẩn hóa, nhưng không phá E1 và không sửa canonical Process.

### 3. Chi tiết cần đạt (AI ghi, Host kiểm)
- Canonical Process: `../ban-duyet.html#ml5-cho-ai`.
- Tool source: `../cong-cu/dot-process-gate.py`.
- A02 chỉ sửa tool + COLLAB lane A.
- KQ mới nhất: **A03 XONG · B02R1 đã XONG; Host mở A04 chỉ để dứt điểm 5 List Master.**
- A04 verdict Host: MOW✓ · MOT✓ · MOIT✓ baseline · MOUT✓ baseline · FIELD◐; phải đưa row/detail schema + evidence vào Master of Master, không chỉ tên/link.
- A04 HOST GATE · PASS · PROCESS=`VEUI.MOW` · catalog=`78b4a6879e8881bb26d67dcf3af6ec29e49abbc6c2032ec3b097105b1ae7e868` · prompt=`056ba8b08ac4a041d121768dbb451fae77785dd09e4bd90a0ce021686f9c9902`.
- READY@b68e2a59562b9931d89b88df4426f10871ce8ed5 · RUN_ID `MMIM-LANE-A04-20260928-01`.
- RUN ISSUED · chỉ List Master; B/C giữ chờ; XONG/DỪNG rồi dừng.
- A05 HOST GATE · PASS · PROCESS=`VEUI.MOW` · prompt=`5a519ab4e050a623bc10c2527a9c4e28f57af7b6b5524af4298fdcd989acce5e`.
- READY@f95b2211777c56bc9a288ae1e302ac76a35fdb49 · RUN_ID `MMIM-LANE-A05-20260928-01`.
- RUN ISSUED · song song B03/C02; chỉ root ui + lane-a/COLLAB theo PROMPT.
- A05 D74 RE-GATE · PASS · prompt=`bfe603411d82391a32daa3987b6f124436641e969c623249b5441f8c1c412658`.
- READY@1bd42c508d18fb747a0aeeb16f16886d18edec9a · RUN_ID `MMIM-LANE-A05-20260928-01` · **SUPERSEDES READY f95b...**.
- A03: sửa duy nhất `dot-walk-check` để chấp nhận process attrs trên `p`; canonical READ-ONLY.
- HOST GATE · PASS · PROCESS=`CHUNG.APQUYTRINH` · catalog=`ba8096abf853e721f460c990667a59db379ccc9aca8347aa16dade4f1601a4a7` · prompt=`7e2a3446298e206c2e649445d2fe5cd30d22737e8cf5dac55b2c79e16ce9ad53`.
- READY@f69af7bbacd92b3c46bbcb873059054a83ab655a · RUN_ID `MMIM-LANE-A03-20260928-01`.
- RUN ISSUED · chỉ sửa dot-walk-check + lane-a/COLLAB; B/C chờ; XONG/DỪNG rồi dừng.
- HOST GATE · PASS · PROCESS=`CHUNG.APQUYTRINH` · catalog=`ba8096abf853e721f460c990667a59db379ccc9aca8347aa16dade4f1601a4a7` · prompt=`af0cd3aa4b889507becb0334c6a2ad2bff090da202f0bf751b03c7a7dbc7b14e`.
- READY@f39ca2ded193af84048937452c937923348ec6b1 · RUN_ID `MMIM-LANE-A02-20260928-01`.
- RUN ISSUED · chỉ gate tool + lane-a/COLLAB; canonical ban-duyet READ-ONLY; XONG/DỪNG rồi dừng.

### Vòng trước
A01 đã PASS: process=39 · shared=8 · scopes=18 · E1 gate PASS.

### A02 · KQ · 2026-09-28
KQ@MMIM-LANE-A02-20260928-01 XONG
KQ@LANE-A A02 · PROCESS=CHUNG.APQUYTRINH · PROCESS_GATE=PASS · contract_gate=PASS · NEXT=Host nghiệm thu A02 cùng B02, rồi mới xét C02.

- Áp: `8fc042022fa93deedfa3e37e8973f02f1e6d9fda` (lượt đầu) + SAME_COMMIT (đính chính); chỉ sửa `../cong-cu/dot-process-gate.py` và COLLAB Lane A; `../ban-duyet.html` read-only.
- Gate trước ghi: `CHUNG.APQUYTRINH` PASS · process_count=39 · step_count=6 · catalog `ba8096abf853e721f460c990667a59db379ccc9aca8347aa16dade4f1601a4a7` · PROMPT `af0cd3aa4b889507becb0334c6a2ad2bff090da202f0bf751b03c7a7dbc7b14e`.
- Công cụ v2: chỉ process `data-contract-v="1"` mới bị kiểm 5 thuộc tính process, 6 thuộc tính cho từng Human Step trực tiếp, mã bước duy nhất toàn catalog, quyền/UI-intent theo bộ giá trị; `--audit-contracts` chỉ đọc và xuất coverage/lỗi.
- Thử thật trên bản nguồn trước ghi: E1 v1/v2 cho catalog hiện hành **trùng kết quả JSON và exit 0**; 13/13 fixture PASS (đủ metadata, thiếu từng loại, trùng mã bước, quyền/UI-intent sai, machine-only, old process, audit coverage/lỗi); ca máy→người→máy PASS 3 bước/1 Human Step; `py_compile` PASS.
- Audit catalog hiện hành: process=39 · opt-in=0 · Human Step opt-in=0 · errors=0 · unversioned=39. Đây là kiểm tương thích; contract thật do B02 gắn vào canonical và Host nghiệm thu sau.
- Giới hạn: kiểm **sự có mặt/hình thức**, chưa xác nhận đúng nghĩa quyền/state/đường quay về; không E3 hard block. Không ghi PG/VPS.
- Đính chính sau đọc lại: lượt đầu lưu thiếu 2 chỉnh sửa cuối; bản đính chính giữ JSON E1 v1 nguyên dạng và trả `contract_errors` khi opt-in BLOCK. Đã kiểm lại SHA source và chạy gate sau lưu.

### A03 · KQ · 2026-09-28
KQ@MMIM-LANE-A03-20260928-01 XONG
KQ@LANE-A A03 · PROCESS=CHUNG.APQUYTRINH · PROCESS_GATE=PASS · walk_attrs=PASS · NEXT=B02R1

- Áp: SAME_COMMIT. Chỉ sửa `../cong-cu/dot-walk-check.py` và COLLAB Lane A; canonical và A02 gate read-only.
- Gate trước ghi: PASS `CHUNG.APQUYTRINH` · process=39 · step=6 · catalog `ba8096abf853e721f460c990667a59db379ccc9aca8347aa16dade4f1601a4a7` · PROMPT `7e2a3446298e206c2e649445d2fe5cd30d22737e8cf5dac55b2c79e16ce9ad53`.
- Walk trước/sau trên catalog thật: 84 Master · 39 Process · 👤62 · 🤖66 · Thuộc 🔁8/⚙️22/🏗9 · 80 calls · orphan 77–82 · 0 lỗi · exit 0.
- Ca tạm: 12 process có attrs trên `p` → walk 39; thêm 15 span contract rỗng → walk 39; whitespace giữa `p`/`b`, `p` ngoài canonical và mã lỗi đều không làm lệch 39. A02 audit bản đủ contract PASS 12/15/0 lỗi; A02 audit catalog thật PASS 0/39 opt-in. `py_compile` PASS.
- Giới hạn: walk chỉ bỏ markup để kiểm bước; không đọc/nghiệm thu đúng nghĩa contract. B02R1 mới ghi contract vào canonical; không mở C hay RUN tiếp.

### A04 · KQ · 2026-09-28
KQ@MMIM-LANE-A04-20260928-01 XONG
KQ@LANE-A A04 · PROCESS=VEUI.MOW · PROCESS_GATE=PASS · list_checked=5/5 · list_green=4 · list_warn=1 · false_green=0 · HUMAN_CHECK=WAIT_OWNER · NEXT=OWNER_LOOK

- Gate trước ghi: READY b68e2a59562b9931d89b88df4426f10871ce8ed5 = commit cuối chạm PROMPT; dot-process-gate exit 0, VEUI.MOW PASS, process=39, step=8, catalog SHA 78b4a6879e8881bb26d67dcf3af6ec29e49abbc6c2032ec3b097105b1ae7e868, prompt SHA 056ba8b08ac4a041d121768dbb451fae77785dd09e4bd90a0ce021686f9c9902.
- Chỉ sửa VPS root ui: master-of-master-v1.html SHA f25a942f25bd4429ceca7f3aafe8f87e26214636416aa24ffd629a24b397237c; master-home-v1.html SHA cc671b637f0ed15cda3ca8c8553b17ad8f65491210125091c8113e8283eb3a1e; ui-child-content-v1.js SHA 337f6d9a8e21f0fa31ce429f0d2e5a83bd3223d1af098ecb20c6f272d3fcbdfb. Ghi KQ riêng ở root workspace theo PROMPT; không có same-commit xuyên hai root.
- Master of Master: 84/84 mã đúng thứ tự trước RUN; 79 record ngoài pilot trùng nguyên nội dung; chỉ 5 pilot có listBaseline, sourceFiles SHA khớp file thật. Badge QL: MOW✓7, MOT✓7, MOIT✓6, MOUT✓6, FIELD◐3; tooltip đọc được. Home List có rowFields, detailSections, URL nguồn + SHA, gap, Mở List và Detail mẫu.
- Checkpoint UI: Home MOW → List → row WF-0001 → Detail đọc bảng bước + 3 câu hỏi + checkpoint/data links; MOT 7/TSK-0001 đọc MOIT+MOUT/trigger/3 vai/PG; MOIT 6/MOIT-F-0001 đọc schema/form/7 tầng/PG/Config; MOUT 6/RPT-0010 đọc report/7 tầng/PG/Builder; Field 3/full_name Detail generic, thiếu type/unit/required/placeholder/help/format/validation/mapping nên giữ ◐. Deep links chi-tiet mở đúng cả 5. MOIT/MOUT ghi rõ dữ liệu minh họa, chưa nối nguồn thật/PG.
- Màn 390 và 1280: Home + Master of Master không tràn trang ngang; Home console 0 lỗi; List cha chỉ có CSP Google Fonts cũ. Parent hashes không đổi: master-list.js a92524f5…, mot-theme-v1.css 81cc5a69…, mot-master-v1.html 85da2f85…. Không tạo dataset nghiệp vụ, không ghi PG/Directus, không mở Step/UI/Tool/Process.
- Giới hạn công cụ bấm: CUA click chuột trên tab/nav và row-link không đổi trạng thái; Enter trên cùng control mở đúng route/Detail. Owner kiểm thao tác chuột khi xem; HUMAN_CHECK vẫn WAIT_OWNER. NODE không có trong snapshot root ui, kiểm JS bằng trang thật/console.

### A05 · KQ · 2026-09-28
KQ@MMIM-LANE-A05-20260928-01 XONG
KQ@LANE-A A05 · PROCESS=VEUI.MOW · PROCESS_GATE=PASS · lists=5/5 · FIELD=◐ · click_path=PASS · HUMAN_CHECK=WAIT_OWNER · NEXT=Host nghiệm thu A05.
COORD · NOW=XONG · NEXT=Host nghiệm thu A05 · BLOCKED_BY=FIELD_✓: thiếu nguồn thông số Field theo từng bản ghi · RESERVED_TARGETS=ui/master-of-master-v1.html,ui/master-home-v1.html,ui/ui-child-content-v1.js (đọc, không sửa); lane-a/COLLAB.md (ghi KQ) · LAST_SYNC=D72-D73/A05
- A06 HOST GATE · PASS · PROCESS=`VEUI.MOW` · prompt=`35b2e59d549be357e5b78081001b37fb7dc89421f3129496a64992e54ac08434`.
- READY@903b34c4dc7103a7dc88a84d3f59d4ac5d6b3aee · RUN_ID `MMIM-LANE-A06-20260928-01`.
- A06 D79 RE-GATE · PASS · prompt=`602abe3698fdef2da3274c4bb00518e3f35cb2ed843c2aa183eb69d7f344218f`.
- READY@c48c877992fea2ec0acd26f7f02a20c6c9ca9ab6 · RUN_ID `MMIM-LANE-A06-20260928-01` · supersedes READY 903b...

- READY `1bd42c508d18fb747a0aeeb16f16886d18edec9a` khớp commit cuối chạm PROMPT; process gate exit 0, VEUI.MOW PASS, catalog SHA `78b4a6879e8881bb26d67dcf3af6ec29e49abbc6c2032ec3b097105b1ae7e868`, prompt SHA `bfe603411d82391a32daa3987b6f124436641e969c623249b5441f8c1c412658`. Registry giữ target A riêng, không trùng B/C.
- Đi thử trên UI thật: Home → List → hàng → Detail bằng chuột 5/5; bàn phím 5/5. List và Detail ở 1280/390: MOW 7/WF-0001, MOT 7/TSK-0001, MOIT 6/MOIT-F-0001, MOUT 6/RPT-0010, FIELD 3/full_name; nội dung/nguồn/gap đọc được, không tràn trang ngang. MOW/MOT/MOIT/MOUT giữ ✓ theo evidence A04; FIELD giữ ◐.
- Field: UI-018 là mẫu khai minh họa, định dạng chưa chọn và lưu trong trình duyệt; UI-022 có 3 dòng mẫu mã/tên/tầng, không có kiểu dữ liệu, đơn vị, required, placeholder/help, format/validation/mapping hoặc nơi lưu theo từng dòng. PG Field nghiệp vụ chưa nối. Home và Master of Master đã chỉ rõ gap này; không suy ra thông số từ mẫu để nâng ✓.
- Ba file UI Reserved_Targets vẫn đúng SHA A04; không sửa UI, Step, Process, Tool, PG/Directus hay target B/C. Bấm chuột và bàn phím qua công cụ PASS; HUMAN_CHECK=WAIT_OWNER là lượt Owner tự xem/nghiệm thu.


### A07 · 2026-09-30
STARTED@MMIM-LANE-A07-20260930-01 2026-09-30T07:10:33Z · executor=Codex

KQ@MMIM-LANE-A07-20260930-01 XONG
- 1 · PROVEN: poll revision chung dựng lại iframe dù HTML MOW không đổi; trạng thái xổ xuống bị mất.
- 2 · SUSPECT: HTML ~551 KB / ~12,3k DOM + iframe ẩn có 11 JS ngoài làm tải đầu nặng; chưa đo phần thời gian riêng.
- 3 · SUSPECT: popstate + hashchange cùng restore/cuộn; có đường xử lý lặp, chưa chứng minh là nguyên nhân chậm chính.
- Patch nhỏ: giữ iframe khi nội dung không đổi; nạp srcdoc một lần khi vào tab; gộp restore/cuộn.
- Rủi ro: giữ nhầm bản cũ hoặc mất deep-link/trạng thái; phải kiểm cả nội dung đổi và không đổi.
KQ@LANE-A A07 · PROCESS=VEUI.MOW · PROCESS_GATE=PASS · causes=3 · proven=1 · suspect=2 · NEXT=A08_PATCH_AFTER_B05
COORD · NOW=XONG · NEXT=A08_PATCH_AFTER_B05 · BLOCKED_BY=none · RESERVED_TARGETS=lane-a/COLLAB.md · LAST_SYNC=FORMULA-01/A07

#### Evidence / before metrics

- Gate: READY `626769a87a786abfeb410ea3e85b8a48d9ff8846` vẫn là commit cuối chạm PROMPT; Registry đúng A07, không STOP. Gate exit 0: `{"status":"PASS","process":"VEUI.MOW","catalog_sha256":"e0e533ab98b80ec80bc51cd616cce07aaa2d53f343099e1aedf664c441ff3bd5","prompt_sha256":"eda0373320a09b1e732393c6613324bf95d8702a06f6adcfc7d5facc03aac37d","reason":"OK","process_count":39,"step_count":8}`.
- Snapshot đầu `e0e533ab…ff3bd5`: 546.642 bytes, 12.261 thẻ nguồn / 12.268 phần tử DOM trên bản mở trực tiếp, 296 details. B05 cập nhật hợp lệ trong lúc A07 đọc: snapshot `ccf4e77b83b48d6691078dfc72f88de8a999a914bff836e3f84a4575abee8d4f` = 550.846 bytes, 12.307 thẻ nguồn / 12.313 phần tử trong html của iframe xuất bản, 297 details. Cả hai: 1 iframe, 1 srcdoc; source của phần này ở `matrix-view-process-list-2`.
- Hai panel cũ Step quy trình + Master list chứa 3.529 + 5.542 phần tử (khoảng 74% DOM snapshot đầu), kể cả lúc ẩn. Iframe Step 2 có srcdoc ngay trong HTML, không có loading/lazy gate: 3.433 ký tự / 3.528 bytes, 11 JS ngoài, 2 stylesheet, 2 script inline. Khi mở Step 2 thấy đủ bảng 7 dòng. Chưa tách được thời gian parse, chạy script và request của iframe ẩn; cấu hình eager là fact nguồn, mức ảnh hưởng là SUSPECT.
- Core listener: 10 tab click, 19 child-UI click, 296→297 details toggle; 1 delegated hash-link click; 2 hashchange + 2 popstate (restore và hdReveal). `show` chỉ đổi hidden/ARIA; `write` push/replaceState và bỏ hash trùng; `restore` mở ancestors + scrollIntoView. Mở một details viết đúng hash của mục; không thấy vòng history vô hạn. Hai handler restore có thể cùng cuộn khi history traversal phát cả hai event; chưa đếm invocation runtime.
- Script tab không đổi sau B05: so sánh nguyên tail trả `unchanged_from_A07_initial_script=true`, SHA `1f00108af2f9f4cec6cd8fb0b33e58b1e897f9b17e68d1276a4277ca57a14ef9`, 5.353 ký tự. Vùng hiện hành bắt đầu dòng 744; iframe ở dòng 113.

#### Reload thật / đổi DOM

- Click tab trực tiếp: Master details vẫn mở khi sang Công thức; Back/Forward khôi phục đúng Master/Công thức và giữ details. Reload chủ động tại cùng hash Công thức đóng details Master. Lọc Tạm dừng trong iframe Step 2 vẫn giữ sau Step 2 → Công thức → Step 2; đã trả lọc về Mọi trạng thái.
- Qua đúng Owner View: click tab đổi URL portal `section=matrix-view-master` và tab con được chọn, nhưng attr src của iframe tài liệu vẫn là bản c51fe1…#matrix-view-formula. Bridge chỉ postMessage section; bộ nạp cập nhật URL bằng replaceState. Đây là đổi DOM/hash/cuộn, không dựng lại document trong ca bấm tab.
- Reload thừa đã tái hiện tự nhiên: 07:30:11Z iframe đang ở revision `4e8cf8d4dacef4752a78538de07aaf85858f6379`, details Master mở. 07:31:39Z iframe đổi sang `06e08d20d2438e0f97fc43e3e8e5d4af3cbdd83d`, cùng tab Công thức, details Master đóng. SHA HTML ở hai revision giữ nguyên ccf4e77b…; Git log cho thấy 06e08d… chỉ cập nhật `work/hermes-joint-workspace/COLLAB.md`.
- Source live HPML: `ie()` poll sync-status mỗi 60s; publishedRevision đổi → lấy tasks mới. `Y=computed(documentPath)`, `H=Y+section`; iframe dùng `key=Y, src=H`. Đường revision đổi làm remount ngay cả khi bytes tài liệu không đổi. Presence poll 15s riêng không phải bằng chứng document reload.
- Giới hạn: capability đọc DOM không cung cấp Performance/Network timeline; không báo số request, long-task hay ms parse. Thời gian gọi tool không được dùng làm độ trễ UI. Lượt mở portal đầu có trạng thái chưa snapshot rồi tự chuyển fresh; chưa xác định nguyên nhân độ trễ fetch ban đầu.

#### Patch plan cho Host / A08 — chưa áp

1. **Bộ nạp HPML · ie / Y / H / watcher Y / iframe key:** tách snapshot metadata đang poll khỏi loaded document. Dùng fingerprint nội dung từng tài liệu để quyết định đổi loaded src/key; revision chỉ đổi metadata và nội dung giữ nguyên thì giữ document cùng trạng thái. Nội dung thực sự đổi thì thay document một lần, dùng section hiện hành. Nếu snapshot chưa có fingerprint đáng tin thì giữ hành vi an toàn hiện có, Host chốt đường fingerprint trước; không chỉ bỏ key trong khi vẫn đổi src.
2. **ban-duyet.html · iframe Step 2 + show:** giữ nguyên srcdoc/asset/UI-001 đã chốt, chuyển payload sang thuộc tính không kích hoạt frame; gán srcdoc đúng một lần khi panel lần đầu được mở, kể cả mở qua deep-link. Không gán lại khi chuyển tab; giữ filter/drawer. Không tách file, không dựng UI con mới.
3. **ban-duyet.html · restore + hai listener + toggle:** dùng một scheduler restore cho hashchange/popstate, gộp cùng URL/target và chỉ scroll một lần; toggle do restore mở ancestors không tạo history mới. Giữ `target()` cùng alias cũ, `write()` de-dup, user details deep-link, ARIA và bridge. Chưa cần chia/cắt kho DOM dài trong patch nhỏ.
4. **Kiểm sau patch:** Owner route + URL tài liệu trực tiếp; tab/summary/anchor, Back/Forward, reload tại deep-link, alias wf4/wf5, iframe lọc/drawer; một commit metadata khác không thay loaded document; thay nội dung thật phải hiện bản mới và giữ section. Đo request/navigation/restore và thời gian bằng capability được Host cấp, tách khỏi thời gian tool.
5. **Đích an toàn:** phần HPML nằm ở runtime `/ui-preview/hpml-view-for-user/view.html`; A07 chỉ đọc source live. Đường `root=docs hpml-view-for-user/view.html` trả PATH_UNAVAILABLE. Host cần xác định/reserve SSOT bộ nạp trước khi giao patch; không vá mù bundle đang xuất bản. B05 vẫn là writer canonical của batch này.

A07 chỉ append STARTED/KQ/COORD vào ledger Lane A; canonical/root ui/PG/Directus và Registry không bị A07 sửa. Trình duyệt đã trả về Master Home. Dừng.
- A08 HOST GATE · PASS · PROCESS=`CHUNG.TIM` · prompt=`382d5e559ada90c1ac43dbf81f0dce4a7d26628df8289a7513264b96ec7ac048`.
- READY@ab7df4bff37aafc8c0bfe919719fd5514b38fe70 · RUN_ID `MMIM-LANE-A08-20260930-01`.

STARTED@MMIM-LANE-A08-20260930-01 2026-09-30T08:06:36Z · executor=Codex

### A08 · 2026-09-30 · BLOCKED_SOURCE_UNAVAILABLE
KQ@MMIM-LANE-A08-20260930-01 DỪNG
KQ@LANE-A A08 · PROCESS=CHUNG.TIM · PROCESS_GATE=PASS · source=BLOCKED · runtime=/ui-preview/hpml-view-for-user/view.html · NEXT=HOST_EXPOSE_SOURCE
COORD · NOW=DỪNG · NEXT=HOST_EXPOSE_SOURCE · BLOCKED_BY=chưa đọc được SSOT runtime VPS/hash hiện hành và quyền deploy · RESERVED_TARGETS=lane-a/COLLAB.md · LAST_SYNC=PRESERVE-01/A08

- Gate PASS, exit 0: `{"status":"PASS","process":"CHUNG.TIM","catalog_sha256":"ccf4e77b83b48d6691078dfc72f88de8a999a914bff836e3f84a4575abee8d4f","prompt_sha256":"382d5e559ada90c1ac43dbf81f0dce4a7d26628df8289a7513264b96ec7ac048","reason":"OK","process_count":39,"step_count":1}`. READY `ab7df4bff37aafc8c0bfe919719fd5514b38fe70` vẫn là last-touch PROMPT; freshness gate trước KQ tại HEAD `349b1eb6648e787dc18c34714102eead524b9bbd` đúng PROMPT/Registry, không STOP.
- **Con trỏ nguồn đã tìm được, chưa đủ FOUND_SOURCE:** `work/hpml-view-for-user/ui-assembly/README.md:3` chỉ đích danh VPS `/opt/incomex/docker/nuxt-repo/scripts/hvu-b2/ui/` là runtime source; ứng viên cần đọc là `app.vue`, cấu hình/build `nuxt.config.ts`, `pack.mjs`, cùng `../README.md` của runtime. COLLAB HPML dòng 139–140, 447, 654 xác nhận lịch sử `ui/app.vue → view.html`, sync riêng ở `scripts/hvu-b2/sync.py`. Các commit runtime được tài liệu nhắc là evidence lịch sử, **không phải hash hiện hành**.
- **Đường dựng được tài liệu mô tả:** tại VPS dùng `nuxt generate → node pack.mjs → .output/public/view.html → bản tĩnh phục vụ /ui-preview/hpml-view-for-user/view.html`; COLLAB HPML dòng 269 trỏ vị trí lịch sử `docker/nginx/static/ui-preview/hpml-view-for-user/`. Chưa đọc được README/manifest/copy route đang dùng trên VPS, nên chưa xác nhận lệnh deploy, hash source↔artifact hay write authority hiện hành. Webhook/backstop chỉ sinh snapshot dữ liệu, không deploy app; README gốc §11–§12 cấm dùng mirror Git làm đầu vào deploy runtime.
- **Mirror không thay được nguồn:** `workspace:work/hpml-view-for-user/ui-assembly/app.vue` SHA `1584e25ba41fbc393b3406859c99f1c53664f868cc21eaf814fad0b23411087c`; README SHA `7eecf511a1c6f5774490a21dfa4bbf48d82373407c9915b2a7a0307060f6b211`; pack SHA `84f11790a4e6fbf83446f182e770acd5df35892cd4b1f1bd6509c219d2dcb22f`. README nói rõ chỉ tham khảo, không deploy. Source mirror còn bảng sáu thành viên và iframe không có `hvu-task-document`, trong khi live đã có bảng Master/bridge/presence mới; không chứng minh mirror sinh bản đang phục vụ.
- **Runtime đọc thật:** browser mở trực tiếp URL HPML, DOM fresh tại revision `5dbb6d850f79bcb0d8d91df0898b5c384ed602db`; buildId `e8931c45-39dc-4dad-a3d2-f9a17a764c81`. Script live vẫn có `ie()` poll 60s; `Y=computed(documentPath)`, `H=Y+section`, iframe `key=Y,src=H`. Đây xác nhận điểm reload A07; không dùng minified bundle làm SSOT được phép sửa. Chưa có SHA nguồn VPS hiện hành.
- **Phạm vi đã tìm:** workspace README §11–§12, HPML COLLAB/PROMPT/ui-assembly README/app.vue/pack, các tham chiếu deploy trong work/*.md; root ui tìm 195 tệp Markdown và 137 tệp JS/MJS/Vue/JSON/shell không có marker HPML. `ui:hpml-view-for-user`, `docs:hpml-view-for-user`, `agent-data:scripts/hvu-b2/ui/app.vue` đều trả `PATH_UNAVAILABLE`; local web-test cũng không có `scripts/hvu-b2`. Discovery chỉ expose ui/docs/workspace/agent-data; vps_status git mẫu fresh chỉ có agent-data/ui/workspace, không có nuxt-repo. Không dò root hay vượt biên để đọc runtime.
- **Host cần nối đúng nguồn:** expose đường đọc đã duyệt tới `/opt/incomex/docker/nuxt-repo/scripts/hvu-b2/` và bản đang phục vụ/nginx mapping, hoặc giao executor có đường VPS đã audit đọc tại chỗ. Lấy SHA hiện hành từng input, runtime Git/dirty state, README build/copy và hash artifact để chứng minh quan hệ nguồn→live; ghi authority và reserve đúng target trước RUN sửa. Điểm kiểm tối thiểu khi nguồn đã nối: hàm refresh/documentPath, loaded src/key + section, fingerprint từng tài liệu. Không chỉ bỏ key khi src còn đổi.

A08 chỉ append STARTED/KQ/COORD vào lane-a/COLLAB; không patch runtime, không sửa ban-duyet.html, không tạo file hoặc RUN mới. Trình duyệt đã trả về Master Home; dừng chờ Host/Owner. Áp: SAME_COMMIT.
