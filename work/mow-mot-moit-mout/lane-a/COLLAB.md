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

