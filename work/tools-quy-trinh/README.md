# tools-quy-trinh · Cửa vào

## Bắt đầu tại đây · P60
1. Đọc COLLAB mục tiêu/phạm vi và cờ phối hợp. Luật chuẩn: MOW-TH-006.md phiên 1.0, 71 bước / 7 mốc; bản trên Overview dùng cùng nguồn.
2. Tra mã CAT-227 → chọn CV-001/CV-002. Mã TQT-VIEC-… và DEF00.1/CAT-227* còn là bí danh lịch sử; không mở mã trùng. Mã Field FLD-0001…; tên cột DB là thuộc tính riêng, không phải ID.
3. Năm ô mục tiêu của CV-001 là dự thảo, chưa Owner duyệt. Duyệt G1 cũ không thay duyệt lượt mới. Thẻ 3 dòng tự tính; chưa đủ thì không xanh.
4. Kết quả thực tế chỉ ghi ở hồ sơ chuẩn và Master liên quan. CAT-069 là việc tiếp; CAT-016 là hồ sơ sửa; CAT-025 là nơi ký. Không dùng báo cáo chat hoặc trang local thay bản ghi.
5. Ký P60: mở hồ sơ CV-001 → Xác nhận hai bên → phiếu TQT-P60-CORRECTIONS → đọc đúng scope/manifest/binding → tự ghi review → đọc lại ô của mình. Báo cáo P49 chỉ là giải thích; chưa có review trong phiếu thì chưa ký. Phiếu này duyệt quy định/bộ kiểm, không nghiệm thu sản phẩm QT001.

## Ghi và kiểm ngoài PG
- Nguồn 5 ô/kết quả thiết kế: catalog.work_schedule.records[].control; nhật ký bước vẫn ở detail_tracking.events. Quy định bước: catalog.detailed_workflow.step_cards. Không chép bộ luật vào kết quả thực tế.
- CHECK005 --validate-control INPUT.json kiểm hợp đồng/tiêu chí/chữ ký/thứ tự trong bản kê đầu vào. INPUT gồm work và options (start/prepared/complete); before dùng kiểm thay đổi mục tiêu đã duyệt. Chỉ HOST_CHECK, không chứng thực quyền trên mọi endpoint.
- CHECK005 --validate-dossier INPUT.json tiếp tục kiểm sự kiện/giờ commit/biên nhận/nhánh. Hồ sơ mới bắt phiên hiện hành. CHECK005 --milestone-report INPUT.json sinh bốn dòng báo cáo từ work và milestone; không nhập báo cáo đạt giả.
- CHECK005 --validate-governance-before BEFORE.html kiểm thay phiên quy trình/Field/DOT có CAT-016. Trước ghi dùng bộ kiểm, CAS qua gateway, đọc lại, kiểm trang Owner. Máy hiện chưa chặn mọi đường ghi; Host không bỏ bước này.
- Field hiện ở DESIGN: đếm định nghĩa mới dự kiến khi đủ kiểm kê; PG vẫn chưa xác minh. CREATED/REUSED/ACCEPTED phải có biên nhận PG ở lượt triển khai sau. Lượt này không đọc/ghi PG.

## Rà độc lập bằng CHECK006
Trên bản sao repo, giữ đúng cấu trúc work/tools-quy-trinh và work/mow-mot-moit-mout/UI-REVIEW-MOW001.json. Giữ UI-REVIEW-AGGREGATE.json là bằng chứng nguồn đã đăng ký. Lấy đúng năm tệp UI theo ui_inputs của TQT-CHECK-005: process-work-master-v1.js, definition-master-registry-v1.js, qtth006-overview-v1.js, ui-child-content-v1.js, ui-child-from-parent-v1.js, cùng một thư mục.
Chạy `python3 work/tools-quy-trinh/run-tqt-checks.py --verify --ui-snapshot /đường/tới/5-tệp --report /đường/kết-quả.json`.
Bộ chạy kiểm hash trước khi thử; thiếu/sai tệp phải báo lỗi, không dùng kết quả cũ. Không cần truy cập VPS khi chạy snapshot. Giữ giới hạn bộ nhớ/thời gian trong Master DOT; không tự nới để vượt kiểm. TEST không nghiệm thu việc thật.

## Mã và duyệt lần đầu
Loại + số, ngắn và ổn định. Không lặp tên task/ngày/phiên/trạng thái trong mã. Master/bản ghi có mã riêng; bí danh cũ giữ truy nguồn, không cấp lại. User duyệt lần đầu cần đúng mã/phiên/phạm vi và bằng chứng; AI chỉ ghi quyết định có thật. Chưa có bằng chứng hiện chưa xác minh, không tự tích. Duyệt không đóng băng thiết kế; sửa phải ghi CAT-016 và rà ảnh hưởng chữ ký.

## Phần còn mở
Chưa nghiệm thu QT001, chưa chạy QT002; chưa đủ chữ ký P60/Owner duyệt 5 ô. Lịch sử sửa truy hồi thiếu bằng chứng vẫn chưa xác minh. 16 mục cũ CAT-069 chưa có liên kết mã việc. 10 bước dự kiến tự động hóa ở governance.automation_plan trỏ nợ TQT-P53-AUTOMATION, chưa có lệnh trọn bước. Chưa cưỡng chế mọi endpoint/định danh chữ ký bằng server. Tách tệp lớn ở lượt sau.

## Tra lịch sử
Các mục P58 trở về trước dưới đây chỉ dùng truy nguồn; quy định hiện hành ở trên và MOW-TH-006.md. Không lấy phiên cũ làm luật cho việc mới.


## Mã danh sách và duyệt sử dụng lần đầu · Owner 14/10/2026
- Từ hai mục trở lên phải có danh sách quản lý. Mỗi Master phải có mã riêng duy nhất; mỗi bản ghi phải có mã riêng ổn định, không dùng số thứ tự hiển thị thay mã. Tra mã hiện có trước khi tạo; không đổi mã theo tên hoặc trạng thái.
- Liên kết giữa các sổ dùng mã bản ghi nguồn. DEF00.1 dùng record_id (TQT-VIEC-…); CAT-069 dùng work_id trỏ về mã đó. Chưa biết liên kết thì để trống và ghi thiếu, không suy đoán hoặc gán chung cho một việc.
- Đưa một Master vào sử dụng lần đầu bắt buộc có quyết định trực tiếp của User, gắn đúng mã Master, phiên/phạm vi và bằng chứng. GPT/Claude ký rà không thay User duyệt. AI chỉ ghi lại quyết định đã có, không tự tích hoặc suy diễn đã duyệt từ việc trang đang hoạt động.
- User duyệt lần đầu không khóa thiết kế vĩnh viễn: thay đổi sau đó giữ lịch sử và đi theo quy trình hiệu chỉnh. Master cũ chưa có bằng chứng duyệt vẫn là chưa xác minh duyệt lần đầu, không tự hợp thức hóa.
- Lượt P59 chỉ sửa hai cột mã và luật này. Cơ chế nút User duyệt/bằng chứng áp dụng mọi Master chưa triển khai, phải xử lý trong lượt rà tiếp; chưa được báo đã có cổng máy cưỡng chế.

## P58 · Sổ việc cần xử lý tiếp
[CAT-069 · Việc cần xử lý tiếp](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/process-work-master-v1.html?master=CAT-069%3F) có lối vào ngay dưới Master Field, cùng cột. Không mở Master mới.
- Nguồn hiện hành: cycle.issues của từng hồ sơ, tool_registry.walkthrough.findings, walkthrough_runs[].findings và application_preview.record.execution_walk.findings. UI tự đọc nguồn, không nhập lại bản sao CAT069; bản sao cũ giữ lịch sử, không dùng đè trạng thái mới.
- P58 đối chiếu76 dòng/76 mã:57phát hiện đã có +17 việc đối chiếu hồ sơ cũ (7TQT,10MOW/Tools) +2 phát hiện bổ sung. 17tham chiếu không phải đã cắt chuyển hoặc đã kiểm trạng thái hiện hành; việc kiểm nguồn đó vẫn OPEN. Không tuyên bố đủ mọi nợ toàn server.
- Mọi mục phát sinh phải ghi vào nguồn của đúng hồ sơ, có mã/nội dung/người giữ/trạng thái/việc tiếp/bằng chứng; dùng lại mã trước khi thêm. CLOSED cần bằng chứng kiểm độc lập. OPEN không có nghĩa đã được phép hoãn.
- Tái sử dụng CHECK005: đối chiếu mỗi issue đúng1dòng, đúng nội dung/trạng thái/việc tiếp; đổi nguồn và thêm việc mới phải hiện ngay. Bộ kiểm lưu trong MasterDOT; không tạoDOT mới.
- Hai ô cuối là chữ ký rà SỔ đúng phiênP58, không nghiệm thu từng việc. PhiếuCAT025 TQT-P58-DEBTS trong hồ sơQT001. OpenAI đã rà; Claude tự kiểm và ký. PhiếuP53 giữ nguyên lịch sử.

## Thanh điều hướng chung · Owner 14/10/2026
Mọi UI đang dùng phải giữ thanh **4 Mẹ + Master** ở đáy. Mẫu `master-list.js` và `design-navigation-v1.js` tự nạp thanh mặc định; không được ẩn `.eco-bar` trong chế độ nhúng. Master mới kế thừa mẫu này, không cần nhớ gắn thanh riêng. Nạp `/ui-preview/mcp-writes/eco-nav.js`; không chép menu sang từng trang. Trang con tiếp tục kế thừa thanh từ mẫu cha. Khi kiểm UI bằng `ui_inspect`, kiểm thêm `.eco-bar`: đủ MOW/MOT/MOIT/MOUT/Master, nằm trong viewport, menu trỏ đúng `/ui-preview/mcp-writes/` và thoát khung nhúng khi mở trang khác. Kiểm lại sau khi chuyển tab/mở hồ sơ; thiếu thanh là chưa đạt UI. Không sửa phiếu nghiệm thu hoặc dữ liệu hồ sơ vì thay đổi điều hướng.


## P54 · Sửa hai điểm Claude VÒNG6 còn yêu cầu

**006@0.9 giữ nguyên71 bước và bảng87 nghĩa vụ.** Chuẩn tại [MOW-TH-006 §11](MOW-TH-006.md); hồ sơ duy nhất tại [DEF00.1 / TQT-VIEC-001](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/process-work-master-v1.html?master=DEF00.1&chi-tiet=TQT-VIEC-001).

- Chưa có lệnh đánh giá điều kiện: AI ghi `MANUAL_ASSISTED`, bằng chứng, người/hãng và phiên. Chưa rà giữUNKNOWN. Reviewer khác hãng tự ghi phiếu CAT015 tạiCP05.03, gắn đúng đánh giá; sau đó mớiNOT_APPLICABLE và được thu gọn. Đổi đánh giá phải rà lại. Có lệnh thì bắt buộc biên nhận máy. Không dùng NA cho nghĩa vụ LUÔN.
- Tái sử dụng CHECK005: `--assessment-binding input.json` tạo nội dung ràng buộc để Reviewer ký; `--validate-dossier` kiểm trước ghi và trả số đánh giá tay. Chỉ kiểm hợp đồng ngoàiPG/HOST_CHECK, không cấp quyền hoặc thay kết luận chuyên môn. CHECK006 chạy tổng với5 đầu vàoUI đúnghash; không tạoDOT mới.
- MasterField: quyết định đủ24 nhóm,12gộp/12giữ riêng. 253−18+4trường quản lý mới=239định nghĩa/361lượt dùng. Giữ327lượt thiết kế gốc. Quyết định/lý do hiện tại từngField, nhãn vẫn tại nơi dùng; nhóm trùng chưa quyết hoặc thêmID ngoài quyết định bị chặn. Bốn trường đăng ký mới: review_ref, assessment_binding, collision_decisions, manual_assessments. Chưa biết sốcộtPG cần tạo; chưaPG.
- P53DEBTS giữ nguyên danh sách24mục và cảhai chữký. Bộđánhgiáđiềukiện thuộc nợAUTOMATION hiện có; không mở nợ trùng. Hai phiếuP54 CORRECTIONS/FIELDS thay hai phạmvi cần sửa, không ký thayClaude; lịch sửP53 giữ nguyên.
- Tiêu đề/chipOverview lấy sốbước từnguồn chung. Trangpreview cũ chỉ dẫn vềOverview, không giữ bảng100bước hỏng.
- Handoff: Claude đọcP54 và P49VÒNG6, kiểmC1/F4/UI rồi ký hai phiếuP54. Không rà lại cấu trúc71bước/danh sáchnợ đã đồng thuận; chưa nghiệmthuQT001/P46, chưa chạyQT002.

### Lịch sử P53
## P53 · Quy định và hồ sơ sau rút gọn

- [Quy định chuẩn006](MOW-TH-006.md): **71 bước / 7 mốc**, bảng ánh xạ đủ **87/87 nghĩa vụ cũ**. 11 nhóm gộp giảm17 dòng, thêm bước tiếp tục sau DỪNG. Số bước là kết quả rà, không là chỉ tiêu. Overview dùng cùng nguồn; dấu ? ngay tại cột/bước.
- [Hồ sơ001 tại DEF00.1](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/process-work-master-v1.html?master=DEF00.1&chi-tiet=TQT-VIEC-001): xem gộp71 bước, mở được87 dòng gốc. Không đổi143events P46/G1, không giả đã chạy bản006 mới. Việc mới để trống dữ kiện thực tế.
- Vai thực hiện, khả năng tự động hiện tại và điều kiện áp dụng là ba thông tin riêng. `NO_COMMAND` phải làm tay có ghi nhận `MANUAL_ASSISTED`; không tự nhận đã tự động26 bước hoặc chỉ cần29 dòng. Nhánh chưa rõ vẫn hiện; nhánh không áp dụng chỉ thu khi máy có căn cứ/biên nhận đúng việc. Các nghĩa vụ trong bước gộp đều phải có kết quả kiểm.
- [Master Field](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/definition-master-v1.html?stt=8): 242−11 trùng nghĩa =231; tách1 miền trạng thái vấn đề + đăng ký21 trường hợp đồng/metadata = **253 định nghĩa,357 lượt dùng**. Giữ327 lượt thiết kế gốc và9 lượtP52. Đây không phải số field cần thêm trongPG; con số đó chưa xác minh. Nhãn nằm tại từng nơi dùng; cùng tên khác nghĩa/miền không gộp.
- Dùng lại CHECK005/006, không tạoDOT/Master mới. CHECK006 ghim5 đầu vàoUI, gồm Overview. Nhật ký nâng cấp/caTEST/kết quả tại MasterDOT/CAT015; nợ tại CAT069. Hai chữ ký tại ba phiếu P53 trong CAT025 phải đúngbinding. ClaudeP52 đãOK phầnD1/D2; không chuyển chữ ký đó sang bảnP53.
- Chưa nghiệm thu QT001/P46 và chưa chạyQT002/PG. Claude rà deltaP53 rồi ký từng phiếu; cả haiOK mới trìnhOwner quyết ca thật. Không giữRUN/lease để chờ.

### Lịch sử P52 (số lượng tại thời điểm đó)


Luật chuẩn: [MOW-TH-006 §9](MOW-TH-006.md#9-hoàn-thành-một-việc-qt001--hợp-đồng-nghiệm-thu-p52). Phân biệt khép RUN, duyệt thiết kế G1 và nghiệm thu việc thật/G2/G3. Ba phiếu bộ sửa/nợ/field ở CAT-025 trong cùng hồ sơ DEF00.1; không dùng ký bộ sửa để nghiệm thu P46. Claude tự ký sau rà; Host không ký thay.

[Master Field hiện hữu](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/definition-master-v1.html?stt=8) đọc catalog.field_registry, bao gồm 327 lượt dùng từ 18 thiết kế Master, gom còn 233 định nghĩa + 2 field hãng + 7 field quản lý. Đây là kiểm kê nguồn đã nêu, không phải chứng nhận đầy đủ runtime G1 hay schema PG; xem nợ TQT-P52-FIELD-COVERAGE. Số cần tạo trong PG chưa xác định. Tra mã/nguồn trước khi thêm, ký đúng phiên ở CAT-025.

Dùng lại CHECK005/006. CHECK005 tự tìm Git của tệp nguồn: có Git thì xác minh commit/sự kiện/thời điểm; giả thì FAIL. Không Git báo UNVERIFIED; không dùng snapshot đó để nghiệm thu. Hai hãng khác nhau mới đạt bước rà độc lập. Các ca kiểm nằm ngay CHECK005, không thêm DOT. Sổ dùng tool và kết quả P52: COLLAB P52 / CAT-015. Lịch sử P51 dưới đây để truy nguồn, không là trạng thái hiện hành.


## P51 · Trước khi thử việc mới

Đọc COLLAB P51 và MOW-TH-006 §8. Luật006 hiện0.6; hồ sơP46 giữ0.5 qua bản định nghĩa lịch sử. CHECK005 dùng lại hai chế độ `--validate-dossier` và `--commit-receipt`, không tạo DOT mới. Chỉ HOST_CHECK ngoài PG, không tự coi gateway đã bảo vệ việc mới. Đo 7 mốc từ giờ commit VPS, giữ số đo tool thật; hồ sơ có manifest cho bước lặp. QT002@1.1 có 6 bước và vòng đời issue; mới đủ để rà, chưa chạy.

Hai bên ký tại CAT025 → TQT-P51-CONSENSUS, hiển thị ngay hồ sơ001: GPT duyệt / Claude duyệt. Trống là chưa ký. Hai hãng cùng binding/phạm vi mới trình Owner; không suy thành duyệt ca thử. Claude đọc đề bài P51, nối báo cáo P49 và tự ký phiếu, không sửa nguồn chính. Nơi này chỉ hướng dẫn; không chép trạng thái ký.

## P50 · Đính chính sau review Claude

[P50: phản hồi và đề bài kiểm lại](proposals/TQT-PR-20261013-host-response-P50.md); [P49: review độc lập](proposals/TQT-PR-20261013-claude-cowork-87steps-P49.md). P46 là chẩn đoán/đóng gói lại G1, chưa là AI mới làm sản phẩm mới. Hồ sơ001 giữ91sự kiện cũ, thêm45revision; giờ ghi không là giờ hoàn thành. Tổng32m25s chỉ tới khép RUN, không phải toàn việc. Không cập nhật trạng thái hiện hành ở aggregate lịch sử.

Trước lượt mới: tra DOT/Tool hiện có; chạy CHECK006 từ cây snapshot đủ định nghĩa và UI, không tự lắp lệnh thiếu nguồn. Vấn đề P50 ở CAT069 trong cùng hồ sơ: mỗi vấn đề có người xử lý, nơi quay lại, điều kiện tiếp và quy trình002/003 tương ứng. Chỉ chặn phần phụ thuộc; không biến ghi issue thành đã hoàn thành nghĩa vụ. Chưa có timer/adapter006 tự cưỡng chế toàn đường. Không bịa thời gian hoặc50/66item hồi tố. Claude chưa rà bản sửa; đọc P50 trước khi tiếp tục.

## P47 · Một nơi xem hồ sơ

Hồ sơ thực hiện P46 nằm tại **DEF00.1 → TQT-VIEC-001 → QTTH06**, nguồn `catalog.work_schedule.records[].detail_tracking`. 87 dòng, giờ hoàn thành, thời lượng đo được, công cụ, kết quả và lý do bị chặn đều ở đây. Các Master liên quan chiếu từ cùng nguồn; không nhập lại. Tệp local chỉ là tệp tạm, không là nơi bàn giao. Tổng P46 đến khép RUN:32phút25giây, chưa hoàn tất nhánh tìm thành công. G1 cũ được giữ lịch sử riêng.

**Host trước khi báo đã cập nhật hồ sơ:** kiểm đúng mã việc/nguồn → ghi qua gateway có phiên → đọc lại so dữ liệu → mở đúng hồ sơ trên UI thấy bản mới. Thiếu thì báo chưa ghi, không thay bằng một trang local. CHECK005 kiểm cấu trúc/nội dung; đọc lại và UI vẫn do Host xác minh, chưa có chốt tự động đủ cả ba tại gateway.


## P39 · RUN P36 đã khép, không giữ cờ bận

`MOW001-P36-REAL` có KQ DỪNG sạch; giữ STARTED lịch sử và G1 đã nhận7/7. Nguồn trạng thái duy nhất: Bảng + P39 trong [COLLAB.md](COLLAB.md). Đề bài Claude review6Config Guard targets, hash live/baseline, imageP38 và đường protected apply có điều kiện đều ở P39; chưa READY hay quyền sửa production.

**Khi kết thúc một RUN:** executor xác minh process/lease và kết quả → ghi KQ đúng RUN_ID XONG/DỪNG (không xóa STARTED) → cập nhật Bảng/root cùng transaction → đọc lại cặp STARTED/KQ và bản Owner View. Không lấy hoàn thành sản phẩm thay KQ của RUN hoặc lấy MATCH thay duyệt mã. Dùng lại gateway/status/Config Guard hiện hữu; không cần DOT mới.

## Lịch sử QTTH006 P40–P48 — bản hiện hành xem mục P53

[MOW-TH-006.md](MOW-TH-006.md) là nguồn định nghĩa duy nhất. P40 bổ sung kiểm quyền trước ghi và khép RUN; chuyển bộ kiểm tổng lên CP05 trước duyệt/ACK. QTTH05 giữ khung 7 mốc. Catalog đăng ký 006 là chi tiết hóa 005, không thêm vào selected_process gây vòng gọi.

[Hồ sơ MOW001](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/process-work-master-v1.html?master=DEF00.1&chi-tiet=TQT-VIEC-001): 11 mục phải ghi thu/mở; QTTH06 ngay dưới, 7 nhóm thu/mở. G1 7/7 giữ nguyên; lượt P46 có 87 dòng ghi nhận thực tế trong cùng hồ sơ, không phải 87 bước đã nghiệm thu. Không dùng TEST hoặc G1 để tự tô 87/87. Việc MOW002 chưa mở chỉ xem mẫu.

AI đọc định nghĩa §5 trước khi ghi `DEF00.1 → work_schedule.records[].detail_tracking`. Trạng thái và sự kiện thuộc cùng hồ sơ, bằng chứng ở Master gốc. P40 **chưa cưỡng chế ghi bước006 ở gateway**, chưa thử AI mới tự đi trọn vòng. Đây là giới hạn cần xử lý trong lượt Owner giao tiếp, không tự mở RUN/PG. Bước bổ sung dùng BS-001…; trạng thái thực tế trống/DONE/NOT_DONE/BLOCKED theo §6. Chưa có adapter cấp quyền hoặc tích đạt bằng tay.

Dùng lại **CHECK005** kiểm nguồn/hash/số dòng theo phiên, mã Master, thứ tự và UI; **CHECK006** chạy tổng. Không tạo DOT hoặc Master mới. PR20 giữ đối chiếu 100→85, P40/định nghĩa §Rà thứ tự giữ 85→87; các bản PR18–21 là lịch sử góp ý.

## P38 · Hồ sơ nhẹ, giữ nguyên lịch sử

Kho vật lý dùng `TQT-HISTORY-POOL-1` trong cùng tệp, không mở kho/Master khác. Mỗi khối lặp lưu một lần theo SHA256; CHECK004 kiểm hash và giải mã trước khi đối chiếu. Nội dung G1/18 sự kiện/20lần kiểm/7mốc không đổi. Đã ghi thật và đọc lại có chữ ký; bộ tổng native PASS trong1GiB, task budget đã trả. Biên nhận tại aggregate#host_review_P38.

**Cho AI:** Tra Master DOT rồi dùng CHECK004 `--compact-history SOURCE` (dry-run); thêm `--execute --output CANDIDATE` chỉ tạo ứng viên mới. Kiểm `--check-history` và `--validate-transition BEFORE AFTER`; ghi qua upload/transaction có expected_version và cửa ghi hiện hành; đọc lại có chữ ký trước khi chốt. Khi cần bản JSON đầy đủ, dùng `--expand-history SOURCE --execute --output EXPANDED` ở vùng tạm; không nhân thành nguồn chuẩn. Sau sửa nghiệp vụ phải pack lại và vẫn tuân phiên/lịch sử cũ. Trước khi lùi runtime cũ phải expand qua cổng hiện hành, không tráo bộ đọc cũ vào dữ liệu mới. Bộ tổng kho nhẹ đã chạy trong1GiB; không tự tăng ngân sách. Dùng tác vụ bền vững cho thao tác dài; tệp vận chuyển nằm trong thư mục con riêng, không lẫn thư mục nhật ký phục hồi. Ghép đủ các trang JSON rồi mới giải mã một lần.

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

## Báo cáo phản biện để AI/Agent đọc tiếp · lưu theo Owner 12/10/2026
- [PR16 — P36: năm mục tiêu, bằng chứng thật, điều kiện mốc 6–7 và việc còn lại](proposals/TQT-PR-20261012-gptchat-p36-five-objectives-16.md). §4 chỉ rõ lệch trạng thái/nhãn nguồn, hồ sơ tăng lớn, giới hạn AI mới và chuyển PG; §1 có job/hash để đọc lại. Bản gốc lưu nguyên văn, các câu “chưa ghi repo” mô tả thời điểm báo cáo trước khi được lưu.
- [PR17 — DOT/Tool: kết quả cũ, phần Codex đã tiếp nhận P33–P36 và phần cần quản tiếp](proposals/TQT-PR-20261012-gptchat-tool-usage-handoff-17.md). Không dùng kết luận “chỉ 6 DOT” của lượt cũ làm hiện trạng toàn hệ thống; không giao lại phần đã làm.
- PR13–PR15 đã có trong `proposals/`, giữ làm lịch sử. **Đọc trạng thái/phiên mới nhất ở P36, COLLAB và hồ sơ; báo cáo không thay quyết định/ACK Owner.** Host Codex tiếp nhận mục còn mở vào sổ hiện hữu, ghi bằng chứng đóng; không mở sổ hoặc task trùng.

## P36 · MOW001 G1 ngoài PG — kết quả kỹ thuật và việc còn lại

**Bằng chứng đã lưu:** P02/P03 thật đã được P04 tự mở đúng hash; 11/11 tiêu chí G1 được Reviewer kiểm lại và chấp nhận kỹ thuật. P04 commit `db0de657082d8f68cd5a03c207785fd4c8e02bbc`, phiếu SHA256 `88460eee2688ebd8ce4f2c11d94f17887049322c7e44c20e0f2fd463b3b82422`; biên nhận đọc có chữ ký R2, task `114c0cf2341341c2b7b764a7f737273b`. Reviewer `/root/review_mow001`, lượt `e1e753`, lúc `2026-10-12T08:59:31Z`: ACCEPT trong G1. Đây là lượt kiểm riêng cùng OpenAI, không phải hai hãng đồng thuận.

**Trạng thái đã lưu: 5/7 mốc, 28/34 nghĩa vụ, CHO_DUYET.** CP05 đã qua cửa ghi tại commit `0ea489a366eaa4a230a6a2346987281e8d9c9694`, transaction `0c68b2d7ed5d42a18a13482714235d66`, task `ea88409a8d19423d91b8977ebdce9e3c`; đúng SHA256 phiếu `ec1620205a41c174f98a38b77225a2151811745a65e2c42f11c1d21fd774d6df`. CP06 quyết định Owner và CP07 xác nhận nhận còn thiếu. Bộ kiểm tổng cuối **PASS** trên VPS1GiB, job `1912451206cb4dd28b30f4447cdfcfc3`; nguồn `276f1ac407e32f1a7821b0d3ed163f5dd50b4f42`. Không giảm assertion/lịch sử, không nới giới hạn bộ nhớ. Lượt worker lỗi trước giữ trong aggregate; lượt này có đủ kết quả.

Nguồn chuẩn: `../mow-mot-moit-mout/UI-REVIEW-MOW001.json#/application_D24`; `execution_walk`, `design_artifacts`, `plan_results`, `test_cases` giữ bước làm, sản phẩm, kết quả và bằng chứng. Hợp đồng v5, schema 1.4, plan 4; UI build `MOW001-G1-UI-P36.1`. Đã quan sát 16 tình huống trên giao diện triển khai; 24 ca model bổ trợ dùng lại CHECK004. Kiểm G1 thiết kế không đồng nghĩa nguồn Field/evaluator/consumer nghiệp vụ đã nối. Minh hoạ giữ nhãn riêng; ACK iframe không thay quyết định/ACK Owner. Chưa PG; không lấy TEST thay việc thật; Anthropic chưa duyệt và không là blocker theo Owner.

**Dùng lại trước:** CHECK004 `--read-preparation`, `--read-designs`, `--check-g1-ui`; CHECK006 `--verify --vps-ui`. Runtime hiện hành `agent-data-hvu:tqt-p36-r2-20261012`, policy `MOW001-G1-P36-2`. Máy chủ ghim schema/mã ngoài vùng ghi và ký biên nhận có nội dung thiết kế; quyền chỉ cho một tệp với 34 collection logic, không phải quyền toàn VPS/PG. CHECK004 có 600 giây cho hồ sơ lớn.

**Ghi–đọc lâu:** dùng `workspace_task_start` → `workspace_task_status`/`workspace_result_read`, giữ expected_version/hash và operation_id. HTTP ngắt không đồng nghĩa đã ghi: kiểm sourcehash, log và trạng thái trước khi gửi lại; chỉ lập mã khôi phục mới sau khi chứng minh chưa ghi. P02/P03 đã phục hồi qua task `7cb813a3e87144fd84f897bf18e000c9`, không bỏ cửa ghi hay ghi trực tiếp bằng SSH. Không kết luận nguyên nhân tiến trình chết khi chưa có bằng chứng đủ.

**Master dùng cùng nguồn:** CAT012 tiêu chí, CAT015 kết quả thực/người kiểm, CAT016 thay đổi, CAT025 quyết định, CAT069 điểm hở, CAT228 đầu ra, CAT229 lượt P36, CAT232 nhận, CAT233 lịch sử, CAT206 hợp đồng. Không nhập kết quả hai nơi, không thêm Master/DOT. CAT229 đọc vòng thật; CAT015 không biến hành động thành kết quả. Giữ hai cột GPT/Claude; thiếu chữ ký ghi chưa duyệt. Việc tiếp: Owner quyết định và xác nhận nhận G1; G2/G3, tối ưu hồ sơ lớn và nhãn ACK lịch sử tiếp tục theo sổ hiện có.

**Bài học P36 khi hồ sơ tăng:** CHECK003/004/005 giữ kiểm toàn lịch sử thật, chỉ tránh bản sao thừa trong TEST; CHECK006 giải phóng dữ liệu đã đối chiếu trước khi chạy bộ con. Không giảm tiến độ thật cho vừa fixture. `record_sha256` là hash nội dung application theo dạng chuẩn; `source_version` là hash byte toàn tệp. Hai loại không thay nhau.

**Giao diện phải đọc đúng phiên:** kiểm `documentStatus` và hash tài liệu trong revision xuất, không chỉ `sync-status` hoặc HTTP200. Công cụ hiện hữu `hvu-sync-py` (Master alias `HVU-SCRIPT.sync.py`) được sửa qua Config Guard để truyền tệp lớn theo luồng; test/README nằm cùng nguồn `scripts/hvu-b2`. Bằng chứng và hoàn tác ở aggregate P36/exporter. Không tạo DOT mới; mở rộng phạm vi kiểm kê hiện hữu để tìm lại thành phần này.

## P35 · MOW001 thật — đọc trước lịch sử P34 trở về trước

Nguồn duy nhất: `../mow-mot-moit-mout/UI-REVIEW-MOW001.json#/application_D24`, mục `execution_walk` giữ bước đã làm, nguồn/hash, điểm tắc và người làm tiếp. CP01 đã đối chiếu Master MOW/3MOT thật; 20/34 mục đã đọc lại. Hai mốc CP01/CP02 có bằng chứng thật: P01 đủ50 câu (rà44, thêm6),13 khai báo và gói chuẩn bị đã được tiến trình khác tự mở/kiểm; đây là chuẩn bị G1, chưa phải sản phẩm đạt. Chưa qua CP03, chưa sửa/duyệt sản phẩm.

CAT012/015/229/069 chiếu thêm hợp đồng mốc, kết quả rà, lượt thực hiện và điểm tắc từ chính phiếu MOW001; không nhập hai nơi. Số 0/7 trong các mục P34 trở về trước là lịch sử. Bộ kiểm không cố định ca thật phải đứng0/7: ca giả tự đặt trạng thái, giao diện kiểm theo bằng chứng.

Cửa ghi một tệp vẫn bắt buộc; không có trust context của adapter thì không nhận quyền endpoint/người kiểm. Host đang xử lý phần này, không dùng cờ tự khai hoặc bản TEST để vượt mốc. Thiếu Claude không tự là điểm dừng theo Owner; phê duyệt và ACK Owner vẫn phải là bằng chứng thật. Chưa PG.

**Đọc lại P01 bằng DOT hiện có:** `node check-record-control.js view.html --read-preparation ../mow-mot-moit-mout/UI-REVIEW-MOW001.json`. Kiểm tập câu hiện hành, con trỏ đáp án, hash kế hoạch/coverage và gói chuẩn bị; chỉ đọc, không tự nâng mốc. Biên nhận ban đầu job37c06c47ab39465ba5a0816163dd6121; DOT đã đăng ký đọc lại đúng phiên cuối ở jobe02137945da649c88074d2ba4398d51f. Trước khi ghi phải kiểm trước–sau đúng hai bản.

**Điểm dừng P35:** đường vật lý một tệp đã ghi/đọc thật; chưa đồng nghĩa34 endpoint đã có bằng chứng tin cậy cho CP03. Máy chủ gọi `--write-gate` không truyền trust context; Master/CAT206 giữ thiếu, không tự sửa dữ liệu thành PASS. P02/P03/P04 và quyết định/nhận còn chưa làm. Thiếu Claude không dùng làm blocker độc lập.

## P34 · Nhớ tiến trình DOT/Tool và đồng thuận

Hai Master dùng cùng cột tiến trình, phiên nguồn, nâng cấp, kiểm gần nhất, việc tiếp, **GPT duyệt · Claude duyệt** ở cuối; giải thích tại dấu **?**. Bấm **Chi tiết** để xem người giữ, phạm vi, lịch sử và biên nhận. Chưa có dữ kiện ghi chưa biết, không khảo sát lại phần đã có bằng chứng đúng phiên. Số lần nâng chỉ tính từ P34, không đoán quá khứ.

**Trước dùng:** tra mục đích → đọc phiên/phạm vi/quyền → kiểm bằng chứng → dùng lại. TEST và biên nhận gọi không thay hai hãng duyệt. `Dùng được` mặc định cần TEST đúng mã và hai phiếu hợp lệ cùng phiên/nội dung hợp đồng, cùng phạm vi nghiệm thu. Owner bổ sung P34: thiếu Anthropic không là blocker; CHECK005/006 được tiếp tục dùng trong phạm vi TEST khi đã kiểm/GPT duyệt. Không gọi trường hợp này là đồng thuận hai hãng. Chưa đủ duyệt vẫn có thể thực hiện kiểm kỹ thuật chỉ đọc trong quyền đã giao để tạo bằng chứng; không suy ra quyền mutation. Thay mã/hợp đồng/phạm vi hoặc thu hồi phiếu thì kiểm và duyệt lại.

**Nơi ghi duy nhất:** `catalog.tool_registry.memory` giữ hợp đồng/người giữ/phạm vi, `changes` giữ sự kiện nâng cấp, `reviews` giữ phiếu duyệt. Phiếu cần vendor OpenAI/Anthropic, người/bề mặt, thời điểm, quyết định, `binding` ghim SHA256 + phiên/nội dung hợp đồng + hash UI phụ thuộc nếu có, phạm vi, bằng chứng gốc, căn cứ quyền và kết quả Host đối chiếu biên nhận. Không điền hộ Claude; JEV không là phiếu duyệt. Giữ phiếu cũ; phiếu cuối mỗi hãng quyết định hiệu lực. Đây chưa phải cưỡng chế chữ ký/ACL ở cửa ghi.

**QT 001 chính là TQT-QT-001 → MOW-TH-003 (hiệu chỉnh hướng dẫn), không phải MOW001.** Lượt thực hành đầu `TQT-QT001-P34-01`: `catalog.tool_registry.walkthrough`; bằng chứng tại `UI-REVIEW-AGGREGATE.json#host_review_P34`. Host đi theo sáu bước hiện có: chọn ca → dùng hướng dẫn → ghi chỗ vướng → hiệu chỉnh → chạy bộ kiểm ở tiến trình khác/đọc lại Master → công bố và bàn giao trong phạm vi áp thử. Claude chưa duyệt ghi riêng, không là điểm dừng theo chỉ đạo mới. Không coi Host đóng hai vai là một AI khác độc lập. Chưa làm nhật ký hàng trăm bước.

**Sổ đã nối trong phạm vi task:** CAT012 đọc sáu bộ kiểm đã đăng ký và năm nhóm ca P34; CAT015 đọc kết quả DOT đã lưu; CAT016 đọc thay đổi; CAT025 đọc phiếu duyệt; CAT229 đọc lượt thử; CAT069 đọc4chỗ vướng P34. Các trang là bản chiếu, không nhập hai nơi; không khẳng định đã thống kê mọi ca/lượt toàn hệ thống. 0 phiếu duyệt nghĩa chưa có phiếu trong nguồn này; không có nghĩa AI hãng đó chưa từng làm việc. Bộ kiểm vẫn CHECK005/006, không có DOT mới.

**Sau cập nhật:** dùng CHECK006 `--verify --vps-ui`; xem kết quả thật và mở lại hai Master. Cập nhật kiểm kê bằng tuyến P33. Còn mở: phiên runtime công cụ ngoài, lịch sử cũ chưa gom, xác thực người ký ở cửa ghi, Claude/agent mới có thể bổ sung phản biện sau; không dùng thiếu này chặn lượt áp thử hiện tại. PG chưa chạy; MOW001 giữ0/7. Lượt áp thử Host P34 đã đi hết đường ghi→kiểm snapshot khác→đọc Master→ghi phiếu→bàn giao. Bộ tổng VPS cuối đạt (job8ea318dd00a14af88252e6a9050a0735,157.370giây); chưa gọi đó là AI mới độc lập nghiệm thu toàn bộ QT001.

## P33 · Tra và dùng lại DOT/Tool trước khi viết mới

Trang chủ → dưới **MASTER TIẾN TRÌNH CÔNG VIỆC** → [Master DOT](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/definition-master-v1.html?stt=24) hoặc [Master Tool](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/definition-master-v1.html?stt=23). Mở **Tra công cụ theo việc cần làm** để xem bản đồ dùng lại và phần còn thiếu.

**Quy tắc cho mọi AI/Agent:** (1) tìm theo việc cần làm trong hai Master; (2) đọc hợp đồng chạy, nguồn/phiên, phạm vi quyền và bằng chứng; (3) dùng lại, thiếu khả năng thì bổ sung công cụ hiện có; (4) chỉ tạo mới khi đã đối chiếu mã, chức năng, đường nguồn và hash; (5) ghi biên nhận theo mã việc. Không tự chạy hàng loạt DOT chỉ vì tìm thấy tệp. Ca thử gắn vào CAT-012/bộ kiểm hiện hữu; kết quả gắn CAT-015/bằng chứng của việc. Script triển khai là bộ phận của DOT nếu chưa có hợp đồng độc lập.

**Một nguồn mỗi loại:** sáu bộ kiểm QTTH ở `view.html → catalog.tool_registry.records`; DOT VPS dùng lại `dot-dot-catalog` và nguồn `/opt/incomex/dot/bin`; công cụ nhà cung cấp ở `catalog.tool_registry.provider_tools` trong Master Tool, giữ nguyên chín phương pháp cũ. Không sao chép mã JEV/MCP. Tên hành động connector phải lấy từ schema công cụ đang kết nối, không đặt theo suy đoán. Nhóm nhà cung cấp như GitHub là nơi tra cứu, không phải tên lệnh để gọi. CAT-006 vẫn là alias ML-DEF-024; không thêm Master. `audit_projection` là bản chiếu sinh từ biên nhận, không sửa tay hai nơi; CHECK-006 chặn lệch bản chiếu.

**Kiểm kê dùng lại CHECK-006**, chạy ở VPS operator có quyền đọc nguồn và nhật ký: `python3 run-tqt-checks.py --audit-vps --work-id tools-quy-trinh --report /tmp/TQT-usage.json`. Lệnh chỉ đọc, không gọi DOT tìm thấy và không truy cập PG. Nguồn quét được pin hash. `--usage-event EVENT_KEY` chọn đúng sự kiện; toàn báo cáo chứa sự kiện, nguồn/hash, kết quả hoặc UNKNOWN, mã lượt chạy và nơi lấy bằng chứng. Lệnh ở snapshot không nhìn thấy nhật ký host sẽ báo BLOCKED, không báo đã kiểm đủ. Cập nhật bản chiếu bằng chính runner: `--audit-patch /tmp/TQT-usage.json --report /tmp/TQT-audit-transaction.json`, rồi chuyển payload cho `workspace_transaction`. Lệnh chỉ chuẩn bị bản vá có kiểm phiên; giao dịch ghi hai nguồn cùng commit, giữ lịch sử Git. Không tự viết một script cập nhật khác. Hồ sơ kết quả task ở `UI-REVIEW-AGGREGATE.json#host_review_P33/audit`; ma trận sinh từ catalog + bản chiếu, không nhập một danh sách công cụ thứ hai.

**Thu thập theo lần gọi:** dùng lại SQLite `queue.sqlite/lc_event` và `jobs`, cùng `audit.jsonl`; không mở hệ thống theo dõi mới. Với lượt đã qua kiểm schema, có ngữ cảnh danh tính và lifecycle đang bật, gateway bổ sung hash nguồn thực thi, hash lời gọi, thời điểm kết thúc, hash kết quả, mã lỗi/tham chiếu; RETURNED chỉ nghĩa công cụ đã trả lời, QUEUED chưa phải hoàn tất, ERROR không phải PASS. Lượt chết trước trả lời giữ STARTED/chưa đủ. Sự kiện gateway và hook không cộng thành số lượt duy nhất. Không lưu nguyên đầu vào/kết quả nhạy cảm.

**Ngoài VPS:** không giả định gateway đã thấy. JEV/GitHub/browser/local cần biên nhận nền tảng tại phần `external_receipts` của bằng chứng công việc: mã việc, nhà cung cấp/hành động, phiên hoặc hash nếu có, thời gian và căn cứ thời gian, mã lượt, kết quả, nguồn bằng chứng. Thiếu gì ghi UNKNOWN; không tự khôi phục lịch sử bằng phỏng đoán. Bản P33 có biên nhận JEV và nhận diện alias các công cụ gateway; kết quả cũ thiếu phiên vẫn chưa đủ bằng chứng.

**Giới hạn còn mở:** danh sách tìm thấy không đồng nghĩa đã chạy tốt; lịch sử hết hạn/không gắn việc và nền tảng ngoài VPS chưa thu đủ; đã quét thêm Agent Data/dot/bin và script .py/.sh ở tầng đầu /opt/incomex/scripts; thư mục con, bản sao lịch sử và các phạm vi khác chưa thu đủ. Chưa có mẫu số công đoạn và bằng chứng đủ để tính tỷ lệ tự động hóa. Chưa nghiệm thu toàn đường, chưa nối PG, **MOW001 vẫn 0/7**. CHECK-004 đọc/kiểm; runtime P32 chỉ cưỡng chế một tệp kho thử, không phải toàn hệ thống.


**Điểm vào: [Danh sách 47 Master đã đưa vào thiết kế](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/master-design-review-v1.html).** Đây là danh sách các Master, giữ nguyên bức tranh toàn cảnh. DEF 00.1 · MASTER TIẾN TRÌNH CÔNG VIỆC là dòng đầu, vị trí 0.1; bấm dòng này mới mở trang tiến trình riêng. Không nhúng bảng công việc lên thay danh sách Master. Danh mục toàn hệ thống gồm cả Master chưa thiết kế được quản lý riêng; làm UI đến đâu thì đưa vào danh sách thiết kế đến đó.

DEF 00.1 dùng lại Master có khóa cũ CAT-227*, không tạo Master thứ hai. Hồ sơ chi tiết, việc con, kết quả kiểm và bàn giao nối về mã việc; vòng nâng cấp giữ lịch sử và gắn hồ sơ mới. Tầng của việc, chuyên môn T3, mốc và vòng đời là các trường riêng. Ngày thực tế tách ngày kế hoạch; chưa có phải hiện Chưa ghi. Nguồn tổng hợp duy nhất: `catalog.work_schedule` trong `view.html`; UI đọc nguồn này, không nhập tiến độ hai nơi. Hiện chỉ có 2 việc ghi danh, chưa chứng minh bao phủ toàn hệ thống. Phép chiếu/khóa/quy tắc PG được thiết kế trong `work_schedule.pg_design`, chưa triển khai PG.

**Hồ sơ ngay trong từng việc:** trang Master có thanh riêng “MASTER TIẾN TRÌNH CÔNG VIỆC” dưới “Master Duyệt thiết kế”. Mở tên việc hoặc Chi tiết để xem cùng khung 7 mốc và 11 mục phải ghi. Mốc hiện tại khác mốc đã kiểm đạt. Mỗi nhóm RG01–RG11 tổng hợp những nghĩa vụ thuộc đúng application_id + quy trình/phiên + đối tượng/phiên; số đã ghi, đã đối chiếu và ô Xong lấy từ `tqt-record-control`, cùng quy tắc với Overview. Không chép trạng thái vào hướng dẫn, không dùng hồ sơ MOW001 cho việc khác. Chưa gắn hồ sơ hiện rõ; ghi một phần không được tính là đủ; nhánh chưa phát sinh không tính là lỗi. Ô Xong chỉ đọc, tự tích khi đủ căn cứ, không ghi giả vào trình duyệt. PG chưa nối.

**Lịch sử rà nơi ghi trước P26 · 11/10:** giữ 39 Master cũ, bổ sung UI cho 8 mã đã có: CAT-206* (hợp đồng vào/ra), CAT-012 (bộ kiểm/ca thử), CAT-229* (lần thử), CAT-238* (lệnh gửi–nhận–trả), CAT-226* (áp dụng vào dùng), CAT-081 (bật/ngừng/cho nghỉ), CAT-239* (tệp/bằng chứng), CAT-017 (sự cố vận hành). Danh sách thiết kế có 47 Master; Master of Master vẫn 86, không sinh mã trùng. Mỗi UI dùng UI.MASTER, có list + mẫu khai báo; nguồn hợp đồng trường tại `catalog.work_master_designs`. Bảng “Qua từng mốc, ghi vào đâu?” trên trang duyệt đọc `coverage` cùng nguồn này. Giữ 11 nhóm trong hồ sơ; các sổ chi tiết nối theo `supplemental_master_bindings`.

**Ranh giới:** CAT-012 định nghĩa ca, CAT-015 ghi kết quả; CAT-229* giữ lần thử, CAT-238* giữ lệnh và chống gửi trùng; CAT-069? giữ sai/thiếu thiết kế, CAT-017 giữ sự cố vận hành và nối về nhu cầu sửa khi cần. Hồ sơ CAT-227* giữ khai báo/đáp án, nghĩa vụ và kiểm mốc theo từng phiên/lần; không đẻ Master cho từng trường. Master Phiên bản hiện có được dùng lại ở lớp thiết kế; chưa khẳng định ánh xạ khóa vật lý với CAT-225*. Đầu ra riêng của nghiệp vụ phải khai Master đích trước CP03, không suy rằng 47 Master đã bao phủ mọi nghiệp vụ.

**Mức hoàn thành:** đủ chỗ khai trong thiết kế cho 7 mốc và các nhánh được rà; chưa có bằng chứng ghi/đọc/quyền của các Master mới. Mô hình trường, khóa, liên kết là thiết kế logic, chưa sinh/nạp PG; TQT-ISS-007 tiếp tục mở. Mẫu rỗng không tính là bản ghi đã tạo, không tăng tiến độ MOW001. Kiểm cấu trúc, các ca sai cũ và mở mẫu qua trình duyệt trước bàn giao.

**Lịch sử trạng thái trước P26 · 11/10:** Hướng dẫn chung tách “Thiết kế UI” và “Nguồn lưu”. 11 mục ghi dẫn tới 19 Master liên quan (11 chính + 8 chi tiết), nằm trong danh sách thiết kế 47 Master. Chưa nối nguồn thì số lượng hiển thị —, không suy là 0 bản ghi thực. Hai số 2 hồ sơ/việc và các dòng kế hoạch là dữ liệu chuẩn bị đã biết, không phải số bản ghi PG. “Đã ghi / Đối chiếu” chỉ thuộc hồ sơ từng việc; không đổi thành Đã ghi chỉ vì tạo UI. Nhãn hiển thị chung ở `record_control.display_labels`; trạng thái nguồn và kiểm mốc giữ nguyên căn cứ. Chưa khai nguồn lưu khác với chưa có thiết kế, và khác với hồ sơ chưa gắn bản ghi.


## P32 / PR15 · hiện hành 12/10/2026

Giữ ⑤, 7 mốc, 47 Master và 6 DOT. CAT-206* schema **1.3-design**, hợp đồng áp dụng **phiên 3**; giữ nguyên các phiên trước. **MOW001 vẫn 0/7**, 13 câu khai chưa đối chiếu; chưa có quyền endpoint hay người kiểm độc lập thật.

- **Trả đúng nơi:** đầu nối MOT1.3 → CALLER kiểm giá trị/kiểu, thời điểm hợp lệ, mã lần gọi, phiên, phạm vi và người nhận; chuyển đủ retrievalStatus/retrievedAt. Kết luận phải khớp bằng chứng hiện hành.
- **Không dùng đánh giá cũ:** bên nhận cung cấp ngữ cảnh hiện hành từ adapter (request/revision/scope, phiên luật, phiên từng nguồn), nằm ngoài gói phản hồi. Kiểm cả đánh giá tổng và từng ứng viên. Thiếu adapter/ngữ cảnh → từ chối, không dùng giá trị tự khai để làm xanh.
- **Mở bản thiết kế:** P02/P03 giao `artifact.path/sha256` trong `design_result`; P04 tự mở, đối chiếu phiên/hash/hợp đồng và trường, kiểu, nút, trạng thái, nhánh, nguồn luật. Các ca TEST dùng bản thiết kế tổng hợp để kiểm cơ chế; chưa nghiệm thu nội dung thiết kế MOW001 thật. Lịch sử endpoint/schema được giữ khi tăng phiên.
- **Phục hồi tệp TEST:** dùng khóa do hệ điều hành giữ, tự nhả khi tiến trình chết. Kết quả/ACK/sự kiện nằm cùng bản ghi trạng thái; nhật ký phụ lỗi thì chạy lại ghi bù trước ACK, không nhân tác động.
- **Thời gian DOT:** ngân sách chạy tại `tool_registry.records[].timeout_seconds`; CHECK003/004 180 giây, các bộ còn lại 60 giây. Báo cáo có thời gian thực tế; hết hạn là lỗi, thiếu runtime là BLOCKED. Không chờ vô hạn.

**Cửa ghi — đã bật trên VPS, phạm vi một tệp kho thử:** CHECK004 `--write-gate` được gọi bắt buộc trước commit. Danh tính do máy chủ xác thực; Codex được ghi, ba tài khoản reviewer đã cấu hình được đọc; thử trực tiếp với Codex/GPT-web/khóa cũ đã đạt 10 ca. Dữ liệu sai qua sửa/giao dịch/upload, xóa lịch sử và di chuyển tệp đều bị chặn. Bộ kiểm/view ghim hash ngoài vùng AI ghi; dùng khóa và rollback hiện có. Phép thử đổi tên phát hiện lỗi bỏ sót nguồn, đã khôi phục nguyên vẹn rồi sửa `--no-renames` và kiểm lại. Biên nhận TEST hợp lệ đã lưu, `application_D24` không thay đổi.

**Chạy lại:** trên workspace VPS dùng `python3 run-tqt-checks.py --verify --vps-ui --report /tmp/TQT-TEST-report.json`. Runtime Node 22.16.0 nằm trong image quản lý; CHECK006 tự lấy đủ bốn tệp UI và đối chiếu hash tại CHECK005 trước khi chạy. Thiếu/đổi đầu vào phải dừng có mã lỗi. Không tạo DOT hay Master mới. Gắn mã gateway, script triển khai/thử quyền và hash tại CHECK004.runtime_binding trong Master DOT hiện có.

**Giới hạn:** quyền tệp đã kiểm không thay quyền nghiệp vụ của 34 endpoint; các access_check vẫn NOT_TESTED. Chưa khóa riêng từng phiên Host, chưa có reviewer thật, chưa nghiệm thu bản thiết kế MOW001. Quản trị SSH và phần trình bày công khai không thuộc ACL workspace. Owner xác nhận GitHub cũ, VPS đang dùng là SSOT; không đẩy mã gateway lên GitHub cũ.

**Bằng chứng chốt:** lượt tổng VPS đạt cả 5 suite, 20 ca tự kiểm runner và kiểm Master trùng; khoảng 145 giây (CHECK004 107/180 giây). 10 ca quyền thật/gate đạt. Chi tiết phiên, hash và biên nhận tại `UI-REVIEW-AGGREGATE.json#host_review_P32`. Bộ CHECK004 tự kiểm logic không tự xác nhận cửa ghi đang bật; trạng thái triển khai lấy từ biên nhận VPS riêng.

**Dùng lại:** TQT-CHECK-004 giữ ca PR15, các lệnh `--test-handoff`, `--test-design`, `--write-gate`; CHECK006 quản hash/thời hạn. Danh tính ứng viên kiểm giả lập không được nhập làm người kiểm thật. Kết luận từng điểm: `catalog.host_review_PR15`; bằng chứng lượt: `UI-REVIEW-AGGREGATE.json#host_review_P32`.

## P31 / PR14 · lịch sử kiểm hợp đồng và giao nhận

**Hiện hành:** CAT-206* schema **1.2-design**, hợp đồng áp dụng **phiên 2**, 66 dòng sau tách trường gộp và khai nhánh hủy. Số dòng chỉ để quan sát, **không là điều kiện đạt**. Nguồn schema logic nằm ngay `catalog.work_master_designs.records[code=CAT-206*].validation`; bản áp dụng ở phiếu MOW001. Profile gắn nguồn luật/phiên, đối tượng/phiên và phạm vi MOT. SHA256 của schema nằm trong hợp đồng: đổi schema làm mất hiệu lực ghim cũ. Giữ 47 Master, 6 DOT và ⑤/7 mốc.

**Bộ kiểm kiểm hai lần:** (1) tập trường/đầu nối bắt buộc theo schema nguồn, đúng kiểu, nguồn–đích và phiên; (2) gói đã ghi–đọc đúng schema bên giao và đủ dữ liệu bên nhận. P01 phải có `scope`, đáp án chuẩn bị và nguồn dẫn; sổ ghi phải trỏ đúng ID/phiên/địa chỉ và nội dung đã đọc. Thiếu P01 chặn từ CP02, không đợi CP04. Tên `requestId/revision`, `source/scope/version`, `reasons/missingInformation` đã tách riêng. Đầu nối ghi rõ trường lấy từ request, response hoặc cancellation; hủy cần mã/phiên/người nhận/phạm vi/lý do/thời điểm, không suy từ một chữ “hủy”.

**Lịch sử:** ngoài phiên câu trả lời/hợp đồng, thay bằng chứng hoặc trạng thái hồ sơ phải tăng `evidence_revision` và nối sự kiện EVIDENCE_REVISION vào `history`, giữ nguyên `previous_evidence` trước sửa. Checkpoint là lịch sử chỉ thêm, không sửa/xóa kết luận cũ; không xóa dòng kết quả/kiểm/duyệt/nhận đã có. Đổi kết quả phải tăng `output_version`; kiểm và nhận cũ mất hiệu lực. Vẫn chạy so trước–sau trước transaction và đọc lại sau ghi; chưa có hook máy chủ cưỡng chế.

**Thử bằng công cụ đang có:** TQT-CHECK-004 đã chứa lát P01→P02: bên giao tạo gói từ các đáp án nguồn, ghi tệp TEST; một tiến trình khác đọc tệp, kiểm và dùng phạm vi/đáp án. Có ca thiếu/sai dữ liệu, gửi trùng, sai phiên/nơi nhận, hủy, mất ACK và hai tiến trình cùng ghi. Cùng khóa/cùng gói trả lại biên nhận cũ, không thêm tác động; cùng khóa/khác nội dung bị chặn. Lỗi TEST ghi sự kiện có nơi xử lý CAT-069?, người giữ và quay P01. Gói PRODUCT_SPEC được thử ghép qua 1.1→1.2→1.3 và nhánh trực tiếp/hủy theo mapping; đây là kiểm cấu trúc gói, chưa chạy backend nghiệp vụ. Tệp thử tự dọn; nguồn bộ kiểm vẫn trong Master DOT hiện hữu.

**Ranh giới tin cậy:** `tqtRecordAudit(R, trust)` chỉ nhận danh tính/quyền/biên nhận do adapter thực thi cấp ngoài hồ sơ. Không đọc trust từ JSON worker nộp; chữ PASS và tên người tự khai không cấp quyền. Bộ mẫu 7/7 chỉ chạy trong ngữ cảnh TEST do bộ kiểm cung cấp; đưa nguyên mẫu sang tiến trình khác không làm nó thành hồ sơ đã nghiệm thu. Schema endpoint/khóa đã phân giải được ở lớp logic; quyền ghi–đọc của các địa chỉ thật, adapter cấp trust và rào ghi máy chủ **chưa hoàn tất**. Người kiểm độc lập vẫn **chưa chỉ định**, các access_check thật giữ NOT_TESTED. MOW001 vẫn **0/7, chưa qua CP03**. TQT-ISS-007 còn mở.

**Bằng chứng:** `UI-REVIEW-AGGREGATE.json#host_review_P31`; phản hồi từng R14-01…07 tại COLLAB/P31. Kết quả local/VPS và phép thử tệp TEST được ghi riêng; không lấy ca TEST hay policy mô phỏng làm quyền endpoint thật.

## Hợp đồng thông tin từng bước · lịch sử P29 / PR-13

**Nguồn chuẩn:** giữ Master **CAT-206\*** (Hợp đồng đầu vào/đầu ra), nâng cấu trúc thiết kế từ 1.0 lên **1.1-design**. Bản áp dụng G1 nằm trong phiếu sản phẩm hiện hữu `../mow-mot-moit-mout/UI-REVIEW-MOW001.json#/application_D24/information_contract`; Overview và UI Master đọc cùng bản chiếu, runner đối chiếu file nguồn. Không tạo Master hoặc quy trình mới.

**Cách đọc:** mở Hồ sơ tiến độ → “Hợp đồng thông tin · từng bước nhận gì, trả gì?”. Bảng đầu đi qua P01–P05; chi tiết có **51 dòng cho 3 MOT**, đầu nối giữa các MOT và **11 ca nghiệm thu khai trước**. Đây là đầu bài **DESIGN_TASK**; các dòng PRODUCT_SPEC mô tả sản phẩm phải thiết kế, không đòi sản phẩm đã hoạt động trước khi thiết kế. Đầu vào MOT1.3 phải có phản hồi đúng phiên hoặc sự kiện hủy, không thể chỉ có câu hỏi/ô tích xác nhận rồi tự kết luận.

**Một dòng CAT-206\* ghi:** mã/phiên hợp đồng, hồ sơ/đối tượng/quy trình/MOT/phiên, giao điểm và hướng vào/ra; mã trường, kiểu, nghĩa, đơn vị, bắt buộc khi nào, có cho trống và số lượng; Master/đường nguồn, Master/cột đích, chuyển đổi và xử lý thiếu; nguồn luật/phiên, mã ca nghiệm thu và trạng thái. Khóa tự nhiên đã gồm MOT/giao điểm/phiên hợp đồng để trường trùng tên ở hai bước không đè nhau. Chi tiết kỹ thuật/đích PG dự kiến nằm trong Master, vẫn là thiết kế chưa migration.

**Qua mốc:** CP01 xác định nguồn/phạm vi → CP02 có hợp đồng áp dụng và ca kiểm, không chỉ boolean → CP03 kiểm độc lập, ghim cả phiên **và nội dung**, xác minh nơi đọc/ghi → CP04 ghi đầu ra có phiên và binding → CP05 kiểm đúng ca đã khai, lưu kỳ vọng/thực tế/người kiểm độc lập → CP06 duyệt đúng phạm vi, sản phẩm và binding → CP07 đúng người nhận, quyết định, sản phẩm và binding. Đổi hợp đồng làm mất hiệu lực từ CP02; lỗi/đổi kết quả muộn chỉ ảnh hưởng các mốc liên quan trở đi. “Đã ghi”, “đúng nghiệp vụ”, “được duyệt” và “đã nhận” là bốn điều khác nhau.

**Trước khi ghi kho thử:** giữ bản nguồn trước sửa có hash → sửa bản ứng viên → chạy công cụ đã đăng ký TQT-CHECK-006 với `--before-product <bản-trước>` → chỉ gửi transaction khi báo PASS, hash trước/sau đúng hai bản sắp ghi, cùng các bộ kiểm đã PASS → dùng `expected_version` của nguồn trước → đọc lại nguồn sau ghi và kiểm lại. Nếu nguồn đổi trong lúc làm, lấy bản mới và kiểm trước–sau lại; không dùng báo cáo cũ. Lệnh kiểm riêng ở TQT-CHECK-004: `node check-record-control.js view.html --validate-transition BEFORE_PRODUCT.json AFTER_PRODUCT.json`. Thay dòng khai phải tăng đúng một phiên và giữ **nguyên bản trước** trong lịch sử; sửa/trộn/thêm lịch sử giả bị từ chối. Hợp đồng thay nội dung cũng phải tăng phiên và giữ bản trước. Không đăng ký script tạm riêng.

**Giới hạn cưỡng chế:** công cụ trước–sau đã chạy trong lượt P29, nhưng máy chủ `workspace_transaction` **chưa tự gọi bộ kiểm này**; AI ghi trực tiếp vẫn có thể bỏ qua. `expected_version` chỉ chống ghi đè đồng thời, không bảo đảm lịch sử đúng. Chưa được coi C13-03 đã cưỡng chế toàn hệ thống. C13-04 mới có danh sách **34 địa chỉ nơi ghi** theo đường MOW001, còn phải hoàn thiện ánh xạ từng schema và thử ghi/đọc; mọi `access_check` giữ NOT_TESTED. Không lập sẵn kết quả/duyệt/ACK thành công để làm xanh mốc 3.

**Trạng thái:** 51 dòng đặc tả là bản nháp chưa kiểm độc lập; 13 câu khai vẫn NOT_TESTED; ca thật **0/7**. Còn 7 nghĩa vụ đến hạn chưa có bản ghi (MOW, ba MOT, PLAN, COVERAGE, RESULT-P01), không phải 7 Master khác nhau. Các ca phá lỗi được giữ trong TQT-CHECK-004; TQT-CHECK-005 kiểm danh sách hợp đồng hiển thị; TQT-CHECK-006 quản hash và báo cáo trước–sau. Bằng chứng tại `UI-REVIEW-AGGREGATE.json#host_review_P29`; kết luận từng C13 tại `catalog.host_review_PR13`. VPS snapshot thiếu Node vẫn báo BLOCKED, không lấy PASS cục bộ thay PASS trên VPS.

## Kho thử ngoài PG · P28 / PR-12 v2

**Dùng lại một nguồn:** `../mow-mot-moit-mout/UI-REVIEW-MOW001.json#/application_D24`, được khai làm kho thử cho **13 câu trả lời của MOW001/G1 trong DEF 00.1**. Không tạo file sao chép. `catalog.trial_storage_contract` là hợp đồng; Overview chỉ chiếu dữ liệu nguồn và kiểm khớp file. File nháp khác không được tính Đã ghi. Phạm vi này chưa thay kho của MOW/MOT, kế hoạch, kết quả kiểm, quyết định hay bàn giao.

**Làm tay theo đúng đường:** đọc hợp đồng → sửa dòng nguồn bằng giao dịch có `expected_version` → nội dung đổi tăng `record_version` và giữ bản cũ trong `declaration_history` → cấu trúc đổi tăng `schema_version` và ghi CAT-016 → sinh lại `application_preview` cùng SHA → chạy runner từ CAT-006 → đọc lại bản đã lưu qua MCP và đối chiếu. Giữ dấu NOT_TESTED cho nội dung chưa kiểm. Đọc được bản ghi ≠ câu trả lời đạt ≠ mốc được duyệt. Mốc 3 kiểm nguồn thử trong phạm vi đã khai, không bắt buộc PG; các đích còn lại vẫn phải có hợp đồng và quyền được xác minh.

**Hai phiên riêng:** `schema_version` là phiên cấu trúc, `record_version` là phiên nội dung. Mã CAT-227* là khóa đang có trong Master of Master (mã hiển thị DEF 00.1); không tự xóa dấu để tạo khóa mới. Việc chuẩn hóa mã toàn hệ thống còn cần xác nhận nguồn và bảng chuyển mã.

**Nối thiết kế:** `catalog.data_contract_index` là một chỉ mục 20 Master → nguồn trường UI → khái niệm mô hình → hợp đồng kho thử/đích PG. Chưa coi các Master, 18 bảng mô hình và 4 bảng checkpoint là ba mô hình thay thế nhau; quan hệ có thể 1:n. Đối chiếu từng cột và đích vật lý còn mở. Phiên cấu trúc 1.0-design không có nghĩa đã duyệt chuyển PG.

**Qua bước:** được thử lát dữ liệu đã đủ hợp đồng, không phải chờ mọi Master toàn hệ thống. Trước PG cần tối thiểu ba ca khác loại, kiểm các nhánh lỗi, không còn lỗi chặn, kiểm độc lập và thử staging/rollback. Ca cuối không thêm cột chỉ là một tín hiệu ổn định; kiểm đạt trên file chưa chứng minh quyền, khóa ngoại, giao dịch và đồng thời của PG. “Vào PG một lần” là một đợt cắt chuyển được kiểm soát, không cam kết vĩnh viễn không cần migration.

Kết luận từng mục T1–T8, C1–C6, P1–P4: `catalog.host_review_PR12`; bằng chứng tại `UI-REVIEW-AGGREGATE.json#host_review_P28`. Việc kế: nối các Master còn thiếu → kiểm nội dung đầu vào → người/phiên độc lập kiểm mốc 3. TQT-ISS-007 còn mở; không tự duyệt mốc bằng tên người kiểm khác.

## DOT / Script / Bộ kiểm · dùng lại trước khi viết mới

[Master DOT · ML-DEF-024](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/definition-master-v1.html?stt=24) là Master hiện hữu được dùng lại; **CAT-006 là mã tham chiếu cũ**, không phải Master thứ hai. Sáu bộ kiểm QTTH ở `view.html → catalog.tool_registry.records`; P33 nối bản kiểm kê DOT VPS và biên nhận theo nguồn, không cấp lại mã. Liên kết CAT-006 chuyển về Master này và giữ tham số chi tiết/mẫu. Danh sách thiết kế hiện có **47 Master** sau khi hợp nhất hai dòng DOT. CAT-012 giữ định nghĩa ca, CAT-015 giữ kết quả. Chưa nhập PG; số 314 trong Master of Master cũ chưa phải kiểm kê live.

**Trước khi thêm:** đọc danh sách đã ghép từ registry định nghĩa + thiết kế QTTH + Config; tìm mã, tên, nguồn dữ liệu và đối tượng/chức năng. Nếu đã có thì dùng lại; thiếu khả năng thì bổ sung công cụ hiện hữu. Khai `source_key`, `entity_key`, phạm vi nếu khác toàn cục; DOT/script khai `operation_key` (chức năng ổn định), đường tệp, SHA256 và hợp đồng chạy. Trùng phải giải quyết trước khi ghi. Khác mã nhưng cùng đối tượng chỉ được hợp nhất qua `catalog.master_identity.bindings` có mã chuẩn, mã cũ, quyết định và căn cứ. Không tự bỏ dòng trùng; không dùng thêm phạm vi để lách kiểm.

**Chạy kiểm:** lấy mới `definition-master-registry-v1.js` từ UI VPS và bản ứng viên `view.html`. Chạy runner hiện hữu:
`python3 run-tqt-checks.py --verify --master-registry <registry-vừa-đọc.js> --ui-adapter <process-work-master-v1.js> --report <bằng-chứng.json>`.
Khi kiểm UI, đặt các bản nguồn `ui-child-content-v1.js`, `ui-child-from-parent-v1.js` cùng thư mục adapter để bộ kiểm chạy cả phần ghép danh sách và chuyển liên kết thật. Không lưu thêm một bản registry chuẩn. Trên VPS chưa có Node, dùng `--identity-only --master-registry-json <JSON-registry-vừa-đọc>` để kiểm danh tính bằng Python; đây chỉ là kiểm danh tính, không thay toàn bộ suite. Thiếu registry ⇒ BLOCKED. Mặc định/dry-run không thực thi suite. Sau sửa script phải cập nhật hash trong danh mục cùng lượt.

**Máy kiểm:** mã trùng; tên sau chuẩn hóa hoa/thường, dấu và tiền tố Master/Danh mục; URL, `source_key`, `entity_key` trùng trong cùng phạm vi; alias thiếu/đa nghĩa. DOT còn kiểm trùng đường, `operation_key`, SHA256, tệp chưa đăng ký/mất/lệch và thiếu hợp đồng. Không bỏ từ “List”, để Master View và Master List View vẫn khác nhau. So bằng chỉ mục khóa, không yêu cầu người rà từng cặp. UI chạy cùng nguyên tắc trên danh sách đã ghép: xung đột chưa giải quyết ⇒ dừng hiển thị danh sách và báo mã lỗi. Tên khác hẳn và chưa khai nguồn/chức năng vẫn có thể lọt: phải hoàn thiện metadata; không coi máy đã hiểu mọi từ đồng nghĩa.

**Bằng chứng và giới hạn:** P30 nằm tại `UI-REVIEW-AGGREGATE.json#host_review_P30`. Báo cáo giữ hash nguồn, đầu vào, công cụ và kết quả. Các ca gồm lỗi DOT gốc, đổi tên/cùng nguồn, thiếu mã chuẩn, alias mâu thuẫn, phân biệt View/List View và 10.000 dòng. Kiểm Python/JS quét tệp task, chưa bao phủ toàn VPS/PG. Runtime VPS còn thiếu Node nên toàn bộ suite BLOCKED; kiểm danh tính Python chạy riêng được. Máy chủ ghi chưa tự gọi runner: Host bắt buộc kiểm bản ứng viên trước transaction, dùng phiên nguồn chống ghi đè, đọc lại sau ghi; UI đã chặn danh sách xung đột nhưng chưa là rào ghi toàn hệ thống.

**7 mốc dùng một bộ tính:** `tqt-record-control` trong view.html. Overview, Master và bộ kiểm Python đều gọi nguồn này. Nghĩa vụ bắt buộc lấy từ hợp đồng quy trình + trường khai + phạm vi MOT + kế hoạch; xóa dòng không làm đủ. Đối chiếu cần đúng quy trình/phiên, đối tượng/phiên, đọc lại PASS và phiên bản ghi. Quyết định/biên nhận phải khớp người, phạm vi, phiên và nhau. Mỗi kết quả mốc có revision + căn cứ phụ thuộc; giữ lịch sử khi kiểm lại. Lỗi mốc sau không xóa mốc trước. Nguồn của nhánh chưa phát sinh chỉ trở thành điều kiện khi nhánh phát sinh; đầu ra ALWAYS vẫn phải khai nơi ghi trước CP03.

**Đường ghi–đọc thử:** runner tạo file JSON tại thư mục TEST tạm trong snapshot thực thi của VPS, ghi bản ghi có mã CAT-015 + application_id TEST + revision, đọc đối chiếu rồi khôi phục. Đây là kiểm ghi/đọc/restore thật trên file TEST, không phải bản ghi Master vận hành của MOW001. Bằng chứng nhận lại qua `workspace_exec_status`, lưu ở `UI-REVIEW-AGGREGATE.json#host_review_P26`. Không giữ file tạm thành nguồn chuẩn. MOW001 còn phải khai mapping từng Master và xác minh quyền/ghi–đọc bằng adapter được quản lý trước CP03; không giả đủ vì kiểm TEST đạt.

**Phần còn mở — TQT-ISS-007:** mapping Master thật của MOW001, PG/quyền/đồng thời, danh mục DOT toàn VPS và kiểm AI mới đi hết sản phẩm. Giữ ⑤ và 7 mốc, chưa mở ⑥. Kết quả rà kỹ thuật không thay Reviewer độc lập hay nghiệm thu sản phẩm.

## Over view · đúng hai câu hỏi

**[1. Việc phải qua mốc nào, đang ở đâu?](https://vps.incomexsaigoncorp.vn/knowledge/modules?task=tools-quy-trinh&view=content&section=tqt-checkpoint-list)**
**Kiểm đầu vào (1–3) → làm theo quy trình (4) → kiểm đầu ra, duyệt và bàn giao (5–7).** Bảy mốc thuộc quy trình ⑤, chiếu từ 6 MOT; chưa thêm quy trình/tầng. Mốc đang chuẩn bị khác mốc đã kiểm đạt. Bộ 7 mốc đang áp thử, còn chờ hội đồng thống nhất.

**[2. Phải ghi gì, vào Master nào, từng việc đã ghi và đối chiếu chưa?](https://vps.incomexsaigoncorp.vn/knowledge/modules?task=tools-quy-trinh&view=content&section=tqt-recording-guide)**

Tách hai bảng, cùng dùng quy trình ⑤:

- **Hướng dẫn chung:** phải ghi gì → tên/mã Master → còn thiếu nơi lưu/UI gì → cách ghi. Dấu **?** giải thích từng cột. Không ghi tiến độ của một việc vào đây.
- **Hồ sơ tiến độ từng việc:** một mã hồ sơ cho mỗi lần làm; từng dòng nối về Master đích và bản ghi cụ thể. **Đã ghi chưa:** Chưa ghi / Đã ghi. **Đối chiếu:** Chưa đối chiếu (xám) / Đã đối chiếu (xanh) / Cần sửa lại (đỏ). Hai cột độc lập; đã ghi vẫn có thể cần sửa.

**Mọi sổ đều là Master List có mã.** Chưa có Master → ghi “Chưa có”, bổ sung Master of Master và thiết kế UI theo UI.MASTER. Có mã nhưng thiếu nơi lưu hoặc UI → hiện đúng phần thiếu. Tài liệu chuẩn bị, phiếu JSON hay liên kết mở được không tự chứng minh đã có bản ghi trong Master. Ngoại lệ có hợp đồng: phần kho thử được khai tại P28 bên trên và máy tìm được đúng bản ghi; không suy rộng cho cả file.

**Ca MOW001/G1:** đang chuẩn bị mốc 2, **0/7 mốc đã kiểm đạt**. Có 34 nghĩa vụ: 13 câu khai đã vào kho thử đúng hợp đồng, 21 mục còn lại chưa gắn bản ghi; không kết luận dữ liệu ngoài hồ sơ không tồn tại. Dữ liệu chuẩn bị vẫn giữ nguyên. Số dòng theo phạm vi từng việc, không cố định 34. Chưa đến mốc/nhánh được chú thích riêng, không coi là lỗi. P01 chuẩn bị được làm ngay; chưa sửa sản phẩm trước xác nhận mốc 3.

**Rà Master ngày 11/10:** dùng lại 11 mã trong **[Master of Master — 86 mục](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/master-of-master-v1.html)**. Trong phạm vi này: 3 Master chưa khai nơi lưu, 4 nguồn khác chưa xác minh. UI thiếu đã có bản thiết kế list + mẫu khai báo, chưa nghiệm thu. Các nhóm có thể trùng nhau. Đã ghi thiếu và yêu cầu thiết kế vào từng Master cùng `TQT-ISS-007`; ánh xạ đang ở mức thiết kế, chưa chứng minh các Master vận hành được. Danh mục 30 Master định nghĩa là một phạm vi khác, không dùng để đếm toàn hệ thống.

**Cách làm:** đọc mục tiêu → khai đúng việc/phạm vi → lấy quy trình/câu hỏi → liệt kê mọi nơi phải ghi từ đầu vào, đầu ra, kế hoạch và nhánh → kiểm Master và quyền → xác nhận đủ → làm → kiểm → duyệt/bàn giao. Rà từ danh sách phải ghi, không chỉ từ những bản ghi đang có. Thiếu nơi ghi thì giữ người xử lý, quay S5 của ⑤, dùng ②/③; không mở sổ không mã.

**Nguồn:** luật/mốc và hướng dẫn chung ở `view.html → catalog.work_form.record_control`; nghĩa vụ và tiến độ từng việc ở `../mow-mot-moit-mout/UI-REVIEW-MOW001.json#/application_D24` (`record_requirements`, `record_checks`). Đây là dữ liệu chuẩn bị cho hồ sơ CAT-227*, chưa ghi vào Master vận hành. Overview đọc bản chiếu có kiểm hash; tên/mã Master là snapshot từ Master of Master, phải sinh lại khi nguồn đổi. Không sửa hai nơi hay đổi trạng thái giả trên trình duyệt.

**Hướng PG:** tách quy định theo phiên quy trình; hồ sơ theo lần làm; dòng ghi/đối chiếu theo mã nghĩa vụ; đích bằng mã Master + mã bản ghi + phiên. Đối chiếu đạt cần căn cứ/người/thời điểm; đổi nguồn thì kiểm lại, giữ lịch sử. Các option hiện chỉ đọc từ nguồn, **chưa có API lưu PG**. Bảng/khóa, ánh xạ toàn phiếu, quyền và kiểm đồng thời còn mở tại `TQT-ISS-007`.

**Kiểm Host:** `node check-record-control.js view.html` kiểm 59 ca về tách hướng dẫn/hồ sơ, sai lần/phiên/Master, thiếu dòng, bằng chứng và trạng thái; `python3 check-overview-consistency.py view.html` đối chiếu phiếu nguồn. Các kiểm thiết kế không thay kiểm PG thực tế hay nghiệm thu sản phẩm. PR11 giữ các điểm chưa đủ ở `TQT-ISS-007`.

## MASTER TIẾN TRÌNH CÔNG VIỆC · DEF 00.1

**[Mở tiến trình các việc theo QTTH 05](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/process-work-master-v1.html?master=DEF00.1)**: mỗi dòng là một việc dự kiến, có thứ tự, việc phải xong trước, hồ sơ, mốc hiện tại, chỗ mắc và người tiếp. Dùng lại CAT-227*, không mở Master trùng với sổ hồ sơ. CAT-228* giữ các việc con; CAT-230* là hàng đợi kỹ thuật, không thay lịch trình người dùng.

- MOW001: đã gắn hồ sơ chuẩn bị; mốc/tình trạng lấy từ hồ sơ hiện hữu, không nhập lại.
- MOW002: đứng sau MOW001; chưa triển khai, chưa gắn hồ sơ. Chỉ mở khi MOW001 đạt nghiệm thu thiết kế và có bàn giao, Host xác nhận tiếp tục. Đóng bằng hủy/từ chối không tự mở việc sau.
- Ngày chưa chốt hiện Chưa khai. Làm lại giữ lịch sử hồ sơ; không lấy mã MOW làm thứ tự, không tạo dòng trùng cho mỗi lần thử kỹ thuật.

Nguồn thiết kế: `catalog.work_schedule` (CAT-227*); luật/mẫu UI: `catalog.work_master_designs`. Khóa và phụ thuộc theo mã, không theo tên; kiểm thiếu hồ sơ, sai phiên, trùng mã/thứ tự và vòng phụ thuộc. Dữ liệu này chưa ghi vào PG; ánh xạ bảng/khóa/quyền vẫn thuộc TQT-ISS-007.

**Lịch sử trước lượt bổ sung 11/10 — [Khu Master đang rà](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/master-design-review-v1.html)** bổ sung 9 Master đã có mã, khi đó có 39 mục chọn thiết kế (30 cũ + 9); hiện hành 48 (47 trước + CAT-006). Master of Master vẫn 86 mục. Mỗi UI mới dùng nguyên UI.MASTER cha, có list và nút Xem mẫu khai báo; mẫu không phải bản ghi đã thực hiện. Không nhập các UI nháp vào danh mục UI con đã duyệt. Kiểm cấu trúc: `node check-work-masters.js view.html` (mã/phiên/hồ sơ/phụ thuộc; 10 ca sai bị chặn). Khi rà UI, chạy thêm với đường dẫn nguồn `process-work-master-v1.js` để kiểm toàn bộ cấu hình list/mẫu khai báo hiện hành.

## Hiện hành · D24/P23 · Host đọc tại COLLAB §0
**5 quy trình tổng hợp + 12 quy trình thành phần.** Host đã chốt **MOW-TH-005 · Từ mục tiêu đến kết quả được nghiệm thu**, phiên `1.1-design`, Chuỗi CTCM `CH-001`, để áp thử thiết kế. Owner giao Host tự quyết; không còn chờ phê duyệt riêng ⑤. Chưa nghiệm thu PG hay tự động hóa.

**Một đường làm:** ⑤ khai việc và hai đầu nối → chuẩn bị/khai nơi ghi/lập kế hoạch → xác nhận đủ điều kiện → làm từng MOT → kiểm sản phẩm và kết nối → duyệt, bàn giao có xác nhận. QT-CTCM-012 lấy/kiểm bộ câu hỏi trong phần chuẩn bị. Sai/thiếu: Tool 008 ghi cùng hồ sơ → ② nhận xử lý → cần sửa hướng dẫn thì ③ → kiểm lại đúng nơi phát hiện. Chưa có người nhận thì người giao vẫn giữ.

[Mở Over view](https://vps.incomexsaigoncorp.vn/knowledge/modules?task=tools-quy-trinh&view=content&section=over-view) · [Master Quy trình tổng hợp](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/quy-trinh-tong-hop-master-v1.html) · [Master of Master (86 mục)](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/master-of-master-v1.html).

**Nguồn duy nhất:** `view.html#tqt-composite-processes.catalog`. 17 MOW có chú giải; 12 thành phần có 50 MOT trỏ về từng hướng dẫn gốc; ⑤ có 6 MOT. Các bước này dùng chung `catalog.trial_contract` (hiển thị tại `#tqt-trial-contract`), không nhân bản câu hỏi hay sổ. Mỗi MOT kế thừa đúng lần làm, đối tượng/phiên, người làm/kiểm/nhận, nơi đọc/ghi, tiêu chí và đích trả. Đây là mã thiết kế, chưa là đăng ký runtime.

⑤ chọn **một** quy trình phù hợp, không chạy tất cả; chỉ dùng tại cửa nhận việc, không gọi đệ quy trong quy trình con. Hướng dẫn từng phần có MOW sở hữu tại `instruction_owners`. Kho câu hỏi, tiêu chí và bằng chứng là nội dung dùng trong quy trình; không tạo loại đối tượng quản lý mới. Không thêm T2.5 hay đổi công thức.

**Nguồn Tool cũ:** hướng dẫn trên `tools-playbook-v1.html` chuyển thành tham chiếu lịch sử; đọc hướng dẫn hiện hành từ Master → Overview. Sổ vấn đề/kết quả sản phẩm vẫn ở nguồn gốc; chưa dời dữ liệu. TQT-ISS-004 theo dõi phần dữ liệu còn lại.

**Phiếu áp dụng:** `../mow-mot-moit-mout/UI-REVIEW-MOW001.json#/application_D24` đã khai 13 mục và kế hoạch cho MOW001/G1. Overview chỉ là bản xem sinh lại từ phiếu, kiểm hash và đối chiếu nội dung; không sửa hai nơi. Mẫu/luật chung thuộc `catalog.work_form` của ⑤. **Bước tiếp:** kiểm điều kiện và đáp án G1, ghi `start_confirmation` trước sửa UI. Chỉ G1 tới nghiệm thu thiết kế, không G2/G3. `issue_register_ref` là nơi ghi bắt buộc; `issue_ref` có thể null nếu không có lỗi mới. Ghi vướng đúng sổ, Host hiệu chỉnh đúng nguồn. Không đợi hoàn thành backend mới thử thiết kế; chưa làm MOW002.

**Giới hạn:** 5 chốt cưỡng chế TQT-ISS-007 và nghiệm thu PG/DOT/quyền/đồng thời/khôi phục vẫn mở. Kết quả kiểm danh mục và mô phỏng không thay nghiệm thu chạy thật.

Kiểm nguồn: `python3 check-overview-consistency.py view.html` → `python3 check-process-catalog.py view.html`; mô hình: `python3 check-process-model.py view.html`. Giữ phiếu/sổ hiện hữu; không mở sổ song song.

## Ý kiến hội đồng · Host kết luận
| Ý kiến | Kết luận hiện hành | Nguồn |
|---|---|---|
| PR-01/02 | Đã tiếp nhận phần câu hỏi/ghép, nguồn hiện có ở ma trận và rules | proposals/ · lịch sử ô3 |
| PR-03 | Đã áp phiếu thử MOW001, chưa nghiệm thu sản phẩm | UI-REVIEW-MOW001.json của task sản phẩm |
| PR-04/05 | Đã tiếp nhận mô hình/khép kín; các chốt còn thiếu giữ TQT-ISS-007 | closure_review / tqt-process-model |
| PR-06 | Sửa retry/schema, còn5 chốt mở | host_review_06 · commit3bc305d |
| PR-12 v2 | Nhận hướng ngoài PG; hiệu chỉnh phiên, mã, ánh xạ và tiêu chí chuyển PG. C1 triển khai lát 13 câu khai trên nguồn hiện hữu; phần còn lại giữ mở | P28 · catalog.host_review_PR12 |
| PR-07 | C1/C2/C4 tiếp nhận; C3 giữ mức0–4 và thêm điều kiện từng mốc. Mục tiêu2–3 chưa áp | review_07 / checkpoint_policy · P16 |

## Một đường vào cho người/AI mới
Đọc AGENTS.md → COLLAB.md mục tiêu và kiểm soát → [chọn quy trình hiện có](view.html#tqt-process-inventory) → khai MOW/MOT đang làm, đúng đối tượng/phiên và nghiệp vụ → lấy bộ câu hỏi/ghi chú tương ứng → làm từng bước → nộp kết quả, bằng chứng hoặc chỗ thiếu.
Host ghi vào phiếu/sổ hiện hữu của công việc; AI góp ý chỉ tạo proposal theo hướng dẫn bên dưới. Chưa đủ câu/căn cứ hoặc chưa có nơi nhận thì ghi rõ điểm dừng; không tự xác nhận đủ.

## Rà vòng 6 · lịch sử trước khi lập Master riêng
Nguồn quyết định: `tqt-process-model.host_review_06`; theo dõi cùng TQT-ISS-007. **87 ca hiện có đạt nhưng còn 5 chốt chưa kín**: kết thúc đúng đường thực thi; nhận bàn giao cuối; đúng đối tượng và tập câu bắt buộc; quyền tại thời điểm hành động; đường nhận kết quả hợp lệ. Đã sửa retry khác nội dung/đích trong mô phỏng và cố định search_path cho 8 hàm SQL sinh ra; chưa nghiệm thu PG.
Kiểm kê tại `tqt-composite-processes.inventory`: hai bản phác thảo tổng hợp, hai hướng dẫn điều phối cần chốt cách xếp, 9 Tool và 2 khung con. Mã tài liệu/nháp/Tool chưa thay mã Master. Đây là danh mục nguồn, không phải đăng ký mới.
**Ý mục 3 của Owner vẫn là đề xuất:** quy trình/bước tham chiếu câu hỏi dùng chung và chịu trách nhiệm trả lời/kiểm/ghi/đi tiếp; chưa áp quy tắc mỗi nhóm câu phải thành MOW riêng. Sáu vùng chưa nối và ba vùng giao nhau đã ghi tại danh mục; không mở sổ khác.

## Đọc đích trước khi làm
Mục tiêu chuẩn và tiêu chí hoàn thành ở [COLLAB.md §0, ô 1–2](COLLAB.md); trạng thái hiện tại ở Bảng điều khiển cùng file. Đọc mục tiêu Owner hiện hành D25 ngày 10/10 tại đó (thay bản 15 ý cũ): phải có quy trình khép kín, đủ câu hỏi/đáp án và bằng chứng làm theo ra đúng sản phẩm. Ma trận, UI và mô hình dữ liệu là các phần phục vụ mục tiêu này. Chi tiết dưới đây là cách thực hiện và lịch sử; không thay tiêu chí nghiệm thu.

## Mô hình hướng PG · v2 · đang kiểm ngoài PG
[Mặt người vẫn sáu ô](view.html#tqt-mo-hinh-pg). SSOT: JSON `view.html#tqt-process-model` (`TQT-MODEL-001`). Giữ 159 câu/53 nhóm; không thêm tầng nghiệp vụ.

- **Tiếp nhận proposal05:** sửa hợp đồng đầu vào/ra và nguồn cấp từng trường; khóa ghép/đúng loại tham chiếu; kiểm sự kiện nhận/trả, quyền đóng, bằng chứng từng nơi; giữ lịch sử. Luật ở `enforcement` / `contract_enforcement`, cách ghi nguyên tử ở `transaction_protocol`.
- **Lưu và đọc lại:** thêm ba bảng hỗ trợ `declaration`, `grant_scope`, `outbox` vào nền 15 bảng. Phiếu đủ bốn phạm vi, 70 lượt đáp án mẫu; TARGET trỏ Field, PROCESS/TASK trỏ MOW/MOT. Khóa đáp án theo phiếu/câu/đối tượng/phạm vi/phiên trả lời; không dùng mã tự đặt để né trùng. UI xuất phiếu vẫn là nháp, chưa nối thao tác lưu thật.
- **Bằng chứng v2 trước rà vòng 6:** 83 ca nền đạt, gồm lưu–đọc lại 70 đáp án và trace sáu ô. Vòng này thêm 4 ca chặn retry/schema, tổng 87. Những ca này không kiểm đủ 5 chốt đang mở; 70 chỉ là dữ liệu thử lưu, không phải số câu bắt buộc hay đáp án nghiệp vụ đã duyệt.
- **Xuất gói:** `python3 check-process-model.py view.html --emit-pg /tmp/tqt-schema.sql --report /tmp/tqt-report.json --trace /tmp/tqt-trace.json`. Mặc định SQL chỉ có schema, FK/CHECK/UNIQUE, hàm/trigger và view; thêm `--include-simulation` mới có DRAFT/SIM. Report chứa mã ca/hash mô hình/hash SQL; trace chứa các bản ghi vòng thử. SQL sinh ra không là SSOT thứ hai.
- **Cơ chế cưỡng chế dự kiến:** FK ghép cho cùng phiên/lần/vòng và đúng loại; deferred trigger cho luật nhiều hàng; immutable trigger giữ bằng chứng; transaction SERIALIZABLE + state/event/outbox; retry cùng khóa và fingerprint. SQL/8 hàm PL/pgSQL đã kiểm cú pháp bằng pglast 8.5. Chưa chạy SQL này trên PostgreSQL.
- **Gói vẫn NOT_FROZEN:** chưa chốt mã Master/nhóm, phiên PG, vai DOT và ánh xạ actor tin cậy; chưa có adapter DOT/dispatcher/inbox được kiểm. Không cấp quyền worker ghi bảng trực tiếp. DRAFT/SIM không phải mã Master, không được gọi production.
- **Điều kiện kiểm PG:** cùng ca đúng/sai, hai phiên nhận việc đồng thời, đóng so với thêm nơi ảnh hưởng, retry sau mất kết nối, cha hủy/con trả muộn, hash Python–PG và restore nguyên gói. Guard quét toàn mô hình và khóa thô hiện chỉ cho staging nhỏ; trước production phải giới hạn truy vấn/khóa theo issue/run, đo tải/index/retention. Không lấy SQLite hoặc kiểm cú pháp làm bằng chứng PG/concurrency/scale.
- **Việc còn mở:** `package.freeze_requires`, `pg.open` và [TQT-ISS-007](view.html#TQT-ISS-007); chưa đóng ca B3–B7/Field thật. Một lần chế tạo phải bàn giao có nhận cho VHCM để kết thúc; việc thuần tài liệu không cần PG thì khai N/A có căn cứ.

## Khép kín MOW/MOT · bản thiết kế 09/10/2026
- Đọc [bốn chỗ hở và đường thiếu Field](view.html#tqt-khep-kin). Nguồn: `tqt-composite-processes.closure_review`; renderer đọc câu hỏi từ `tqt-question-matrix`, không chép bộ thứ hai.
- **Lịch sử trước Master tổng hợp:** TQT-TH-001 là mã tài liệu. Hiện dùng MOW-TH-001 trong ML-MOW-TH-001; không dùng đoạn lịch sử này để phủ nhận mã thiết kế. Quyền runtime/PG vẫn chưa nghiệm thu; chưa thêm T2.5.
- Ma trận có 159 câu/53 nhóm; thêm 19 câu tại đúng Tầng/MOW/MOT/UI/Test/NTGV. Đây là câu hỏi đang hiệu chỉnh, không phải 159 câu đều áp dụng cho mọi việc hay đã được trả lời.
- Khai báo theo thứ tự, xem quan hệ ra→vào, nguồn đọc/nơi ghi, người nhận và điều kiện đóng. Ghép câu hỏi thành việc con theo đầu vào/ra/trách nhiệm; không sinh một Task cho mỗi câu.
- Phân biệt mức bằng chứng với hiệu lực kết quả, vòng đời định nghĩa với lần áp dụng. Cơ chế chọn phần cần kiểm lại/PG/DOT/JEV mới là thiết kế; chưa có lưu tự động hay chạy nền.
- Hồ sơ theo dõi duy nhất: [TQT-ISS-007](view.html#TQT-ISS-007). Nội dung hồ sơ đọc từ cùng JSON; không đóng chỉ vì hoàn thiện tài liệu. OPEN-10 vẫn thuộc sổ sản phẩm hiện hành.

## List quy trình tổng hợp · xem chi tiết
- [Mở trên hệ thống](https://vps.incomexsaigoncorp.vn/knowledge/modules?task=tools-quy-trinh&view=content&section=list-quy-trinh-tong-hop). Thu/xổ theo quy trình → giai đoạn → bước.
- Quy trình đầu: **TQT-TH-001 · Thiết kế - xây dựng một chi tiết/chức năng trong chế tạo cỗ máy**. Nguồn duy nhất là JSON `tqt-composite-processes` trong `view.html`; giao diện và vùng AI đọc cùng dữ liệu.
- Bắt đầu ở quy trình tổng hợp để biết thứ tự, checkpoint và đường quay lại; sau đó mở quy trình con/câu hỏi/ghi chú theo liên kết. Không nhầm 9 bước phối hợp ở đây với B1–B9 của Công thức.
- Mỗi lượt áp dụng lưu bằng chứng/checkpoint trong phiếu sản phẩm hiện có; vấn đề ở sổ của nguồn cần sửa. Phần tổng hợp chỉ dẫn nguồn, không mở sổ mới. Hướng dẫn con mới còn trạng thái cần áp thử.
- Host sửa nguồn sau khi tiếp nhận; người góp ý chỉ nộp riêng. Thêm quy trình tổng hợp sau này vào cùng danh sách, không tạo các bản chuẩn rải rác.

## Ma trận câu hỏi · hiệu lực 08/10/2026
- Host/roster hiện hành chỉ xác định tại [COLLAB.md §0](COLLAB.md); thành viên ngoài Host nộp đề xuất riêng. Không suy ra quyền hiện hành từ quyết định lịch sử.
- Mở trực tiếp [Câu hỏi cơ bản trên hệ thống](https://vps.incomexsaigoncorp.vn/knowledge/modules?task=tools-quy-trinh&view=content&section=cau-hoi-co-ban). URL ghi nhớ tab/mục; bước 1.2 dùng section=q-B1-2, mã câu vẫn Q-B1.2-01. Renderer chỉ nhận từ đúng iframe; xem bằng chứng ở COLLAB §0 ô 3.
- Đọc [Câu hỏi cơ bản](view.html#cau-hoi-co-ban) → [Câu hỏi nghiệp vụ](view.html#cau-hoi-nghiep-vu); đọc hàng loạt tại [Ma trận câu hỏi](view.html#ma-tran-cau-hoi).
- **SSOT của bộ câu hỏi mới:** JSON trong `view.html`, script `id="tqt-question-matrix"`. `groups` chứa mã/loại/cha/nguồn; `questions` chứa mã câu, nhóm sở hữu, câu hỏi, trạng thái; `groups[].required_reference` nối câu nguồn bắt buộc ngoài ma trận (Config); ứng viên dùng lại đáp án phải kiểm đúng phạm vi, không tự đánh dấu đủ. `inheritance` quy định câu chung; `rules` giữ quy tắc dùng, tách, kế thừa, ghép và kiểm chứng (hiển thị tại “Cách dùng”/“Cách kiểm sau khi ghép”). AI đọc trực tiếp JSON này; bảng, sơ đồ, bộ ghép và vùng JSON để sao chép đều đọc cùng dữ liệu.
- Host sửa câu hỏi trong JSON, giữ nguyên mã; không sửa chữ tại bản render, không nhân câu hỏi vào từng MOW/MOT. Bước con kế thừa bước lớn và câu chung; thêm câu riêng khi có khác biệt cần kiểm. Thêm nhóm/câu phải kiểm mã duy nhất, cha tồn tại, có câu hỏi, mọi cách xem cùng kết quả.
- Thuật ngữ theo chỉ đạo mới: **chuyên môn = Bước/Tầng/Chuỗi**; **nghiệp vụ = UI/Test/Config…**. Các cách gọi khác ở hồ sơ cũ được giữ để truy nguồn.
- Các nhóm nghiệp vụ khởi đầu: UI, Test/rà UI, Config, Nguyên tắc giao việc (đã được nêu trong mục tiêu Owner); thêm nhóm trong ma trận thì thẻ và bộ ghép tự nhận. Câu hỏi của các nhóm này vẫn là bản khởi tạo.
- Bộ câu hỏi mới là **bản đầu đang hiệu chỉnh**, không phải kết luận đã đủ hoặc đã qua hội đồng. Thành phần Công thức được đối chiếu nguồn; không đồng nghĩa các câu hỏi mới đã được Owner duyệt. Tầng bối cảnh T3–T7 thu gọn; B8/B9 chưa có bước con.
- Nội dung cũ giữ nguyên trong [Quy trình hiện có](view.html#tqt-legacy), liên kết cũ vẫn mở đúng mục. Hướng dẫn hiện hành ở tools-quy-trinh; hồ sơ sản phẩm vẫn giữ tại nguồn gốc. TQT-ISS-004 còn phần kiểm/cắt chuyển dữ liệu sản phẩm.
- Góp ý: file riêng theo mẫu bên dưới, trỏ mã Q/nhóm, nêu chỗ vướng khi làm và câu đề nghị sửa. Chỉ Host quyết định tiếp nhận rồi cập nhật nguồn; không sửa thẳng bốn file chính. Chưa gọi hội đồng trong lượt dựng bản đầu này.


## Ghi chú riêng · đọc trước khi ghép
- Cùng JSON `view.html#tqt-question-matrix` có `note_policy` và `notes`; đây là nguồn duy nhất của quy tắc đặt/ghép ghi chú. Mỗi ghi chú có mã, nơi sở hữu, phạm vi áp dụng, nội dung, nguồn và trạng thái. Host tiếp nhận trước khi dùng như quy định.
- Bấm Bước/Tầng để xem “Ghi chú riêng”; bộ ghép tự lấy mục khớp đúng lựa chọn. Xem toàn bộ dưới Ma trận câu hỏi. MOIT/MOUT cùng T0.5 nhưng không tự dùng chung ghi chú.
- Nội dung chỉ đúng với một MOW/MOT ghi ở phiếu sản phẩm, không biến thành luật chung. Lượt áp dụng hiện hành: [MOW001 · phiếu đáp án, hợp đồng A/B/C và bằng chứng](../mow-mot-moit-mout/UI-REVIEW-MOW001.json), mục hiện hành `application_D24`; `process_trial_20261009` là căn cứ lượt cũ, cần kiểm hiệu lực trước dùng lại. Thứ tự thực hành UI/Config nằm ở notes của nhóm nghiệp vụ.
- Khi thêm ghi chú: kiểm mã/owner/phạm vi tồn tại; kiểm cả ca khớp và ca không khớp; không có ghi chú không đồng nghĩa đã rà đủ. Thay nguồn vẫn phải cập nhật bằng chứng tại phiếu áp dụng.

## 0. ĐỌC NGAY — DÀNH CHO MỌI AI (kể cả khi vừa bị từ chối ghi)

**Host duy nhất của task hiện hành:** đọc `Host/Host_ID/Host_Surface` tại [COLLAB.md §0](COLLAB.md). README chỉ dẫn nguồn quyền, không duy trì danh tính Host thứ hai. Mục tiêu và tiêu chí xong chỉ ở [COLLAB.md §0](COLLAB.md); phải đọc `../../AGENTS.md` và §0 trước khi thực thi.

**Chọn đúng tình huống:**

1. **Muốn dùng quy trình để làm thật:** đọc [Quy trình hiệu chỉnh hướng dẫn và quy trình](view.html#quy-trinh-hieu-chinh) nếu đang xây/sửa quy trình; nếu đang rà UI, đọc [Rà một UI · 6 bước](view.html#ra-ui). Thực hiện theo bước, lưu **sản phẩm/bằng chứng thực tế** tại task sản phẩm được phép ghi. Không đạt → ghi đúng chỗ thiếu, không tự tô PASS.
2. **Thành viên ngoài Host muốn sửa quy trình hoặc sổ TQT:** **KHÔNG** sửa trực tiếp `view.html`, `COLLAB.md`, `README.md` hay hồ sơ trên trang. Tạo **một file đề xuất riêng** `work/tools-quy-trinh/proposals/TQT-PR-YYYYMMDD-<seat>-<so>.md`, tên không trùng; Host đọc → duyệt → chỉ Host nhập vào nguồn chính rồi kiểm lại.
3. **Bị từ chối ghi, VERSION_CONFLICT hoặc không rõ quyền:** **DỪNG sửa nguồn đích**; đọc lại file README **`work/tools-quy-trinh/README.md`**, đối chiếu quyền và mẫu bên dưới; chuyển sang nộp đề xuất riêng, không retry cùng lệnh/bypass/ép push. Nếu ngay cả đường tạo đề xuất bị chặn, báo Host mã lỗi + đường dẫn + thời điểm; không tự mở đường khác.

### Xác nhận của người thực hiện — bắt buộc trước khi Host công nhận quy trình đạt

Bộ 8 câu/MOT và 7 câu Config **đã nằm ở** [“Rà một UI”](view.html#ra-ui); không viết lại bộ câu ở đây. Mỗi lần rà một UI, Codex/agent phải có câu trả lời + bằng chứng hoặc ghi rõ BLOCKED/NOT_TESTED/N-A kèm lý do cho **mọi câu áp dụng**, mọi nhánh bắt buộc và việc bàn giao.

Cuối lượt, **chính AI đã làm** ghi xác nhận tại phiếu được giao; thành viên ngoài Host nộp góp ý quy trình qua proposal, không sửa nguồn chuẩn. Host theo quyền tại COLLAB §0.

```text
DOER_CONFIRM: YES | NO | PARTIAL     # Tôi đọc từ đầu, không được giải thích thêm, có hoàn tất quy trình RÀ SOÁT trong phạm vi giao không?
READ_VERSION: <commit/phiên bản README + #ra-ui + URL/phiên bản UI>
SCOPE: <MOT/màn nào, phần nào N-A hoặc chưa được phép thử>
QUESTION_COVERAGE: <Q1-Q8/MOT và 7 Config: đủ câu trả lời + chứng cứ hoặc lý do còn thiếu>
BRANCH_COVERAGE: <nhánh và ca: PASS/FAIL/BLOCKED/NOT_TESTED/N-A + lý do>
DELIVERED_OUTPUT: <đường dẫn phiếu kiểm, số ca, mã sổ, bằng chứng đọc lại; thiếu thì ghi CHƯA CÓ>
MISSING_FROM_PROCEDURE: <đúng câu/bước/đường dẫn/định nghĩa xong cần thêm, hoặc KHÔNG>
UI_PRODUCT_STATUS: <PASS|FAIL|BLOCKED|PARTIAL>  # Kết quả sản phẩm UI, TÁCH với việc làm được quy trình rà
```

**Quy tắc đọc kết luận:** `DOER_CONFIRM=YES` chỉ khi agent tự đi hết hướng dẫn và **bàn giao được phiếu rà soát đầy đủ phạm vi** mà không phải hỏi cách làm; UI đang lỗi vẫn có thể được kết luận `BLOCKED/FAIL` **nếu đã phát hiện, đối chiếu nguồn, ghi bằng chứng và hồ sơ đúng**. Nếu mới thử vài ca, chưa phủ hết câu hỏi/nhánh hoặc không tìm được nơi lưu thì `PARTIAL/NO`, **không** dùng 5 ca đạt để kết luận cả quy trình. Host chỉ công nhận bản hướng dẫn sau xác nhận của người làm **và** kiểm được kết quả thật; khi thiếu câu/bước, ghi vào hồ sơ TQT-ISS-003, sửa theo vòng TQT-QT-001 và cho phiên mới thử lại.

**Khuôn đề xuất 6 dòng (không cần viết báo cáo dài):**

```text
TQT-PROPOSAL: <mã duy nhất / tên file>
TARGET: <TQT-QT-001 hoặc TOOL-CTCM-xxx / mã sổ + bước>
TESTED: <ai đã đọc và làm / phiên nguồn / đầu ra thật / link evidence>
BLOCKER_TYPE: <THIEU_HUONG_DAN | THIEU_SAN_PHAM | THIEU_QUYET_DINH | THIEU_QUYEN | LOI_QUY_TRINH>
OBSERVED: <đọc hướng dẫn nào, làm đến bước nào, kết quả thực tế và đúng ra phải là gì>
PROPOSED_CHANGE: <thêm/sửa đúng câu, bước, nhánh, kiểm chứng lại thế nào>
```

Nếu **thiếu chức năng sản phẩm** (ví dụ chưa có nguồn Field thật/JEV) thì nêu `THIEU_SAN_PHAM` và mã issue sản phẩm, **không** viết hướng dẫn giả rằng đã có. Host phân loại trước khi sửa.

### Quyền ghi & phản hồi khi bị chặn (TQT_GATE_V1)

| Vai trò | Được ghi | Không được ghi |
|---|---|---|
| Host đúng phiên/bề mặt được ghi tại COLLAB §0 | Nội dung chuẩn/sổ/README trong task sau khi duyệt và kiểm bằng version | Không tự sửa runtime MOW/VPS ngoài phạm vi |
| Mọi AI ngoài phiên Host đã chỉ định | File đề xuất **riêng** trong `proposals/`; bằng chứng sản phẩm ở task được giao | 3 file chuẩn và sổ TQT trên trang |
| Owner | Góp ý/đề xuất trực tiếp bằng chat; Host ghi lên repo | Không bị yêu cầu thao tác Git/Markdown |

**Hiệu lực:** quy định vai trò và đường nộp đề xuất **đã áp dụng**; cổng từ chối ghi theo danh tính kỹ thuật **CHƯA ĐƯỢC XÁC MINH** (TQT-ISS-006). Github đang khóa push thường theo ruleset `gateway-only-writes`, nhưng gateway có DeployKey chung: **không có nghĩa** mọi AI khác đã bị chặn path.

**Yêu cầu kỹ thuật để hoàn thiện TQT-ISS-006, chưa giả là máy đã làm:** gateway phải xác thực **đúng phiên/bề mặt được Owner giao làm Host** bằng identity server-side, không tin chuỗi tự khai trong commit và không chỉ so chuỗi Host_ID tự khai (có thể dùng chung nhiều bề mặt). Khi AI khác cố ghi các file chuẩn, trả `HOST_APPROVAL_REQUIRED`, kèm `readme_path=work/tools-quy-trinh/README.md` và `allowed_proposal_path=work/tools-quy-trinh/proposals/TQT-PR-...`; thử được ca từ chối main, cho phép proposal và Host duyệt nhập/kiểm. Nếu lỗi do nguồn bận/xung đột thì trả lỗi thật, không ngụy thành đã bị chặn quyền.

**Không thay luật toàn repo.** Quy ước này chỉ dành cho `work/tools-quy-trinh`. Sổ `OPEN-01…10` ở MOW vẫn sửa tại nguồn MOW tới khi hoàn tất chuyển nguồn TQT-ISS-004.

---
Đọc `../../AGENTS.md` → [§0/Bảng điều khiển](COLLAB.md) trước; lấy mục tiêu, tiêu chí, Host/roster và việc kế tiếp từ đó.

## Mở đúng nội dung

| Cần làm gì | Nguồn phải đọc |
|---|---|
| Owner xem task | [Over view — bức tranh chung](https://vps.incomexsaigoncorp.vn/knowledge/modules?task=tools-quy-trinh&view=content&section=over-view) |
| Nhìn nhanh có gì, thiếu gì, tắc ở đâu | [Phiếu đủ/thiếu trên Overview](view.html#tqt-work-board) |
| Nhận diện phạm vi, lớp và nhóm chuyên môn | [Cách phân loại](view.html#phan-loai) |
| Tổ chức câu hỏi từ gốc, ghép với nghiệp vụ | [Ma trận câu hỏi](view.html#ma-tran-cau-hoi) · [Phạm vi Host hiện hành](PROMPT.md); ý kiến ngoài Host gửi riêng |
| Owner cùng xây dựng quy trình hiệu chỉnh | [Quy trình hiệu chỉnh hướng dẫn và quy trình · TQT-QT-001](view.html#quy-trinh-hieu-chinh) — MOW-TH-003, có bước duyệt/công bố/kiểm nơi dùng/ngừng bản cũ |
| Rà UI đang có, viết ca và lưu kết quả | [Hướng dẫn thực hành](view.html#ra-ui) → 8 câu/MOT, 7 câu Config, khuôn ca, nơi ghi và kiểm lại |
| Đọc đủ 9 Tools, từng bước/câu hỏi | [9 Tool · một khuôn](view.html#tool-9) — hướng dẫn hiện hành; bản cũ tại VPS giữ lịch sử |
| Luật dùng chung: công thức, xong khi, đi tới đích, sửa hay ghi sổ, Tool→DOT | [Dùng chung](view.html#dung-chung) |
| Xem áp thử MOW-NHC-001 và các lượt chạy | [Áp thử](view.html#ap-thu) · [Sổ lượt chạy](view.html#so-luot-chay) |
| Nguồn cũ đã chép, nơi đang gọi, cách cắt chuyển | [Chuyển nguồn](view.html#chuyen-nguon) → mở bản cũ tại VPS |
| Ghi/kiểm vấn đề của tools-quy-trinh | [Sổ vấn đề](view.html#so-van-de) — TQT sửa ở đây; OPEN là bản chép, trạng thái hiện hành ở sổ MOW tới khi cắt chuyển |
| Đọc vấn đề và kết quả MOW đã có | [Sổ MOW / Tools](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/tools-playbook-v1.html#issue-register) · [Kết quả từng lượt](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/tools-playbook-v1.html#tools-run-register) |
| AI ngoài Host gửi đề xuất sửa quy trình/sổ | Tạo file **riêng** `proposals/TQT-PR-YYYYMMDD-<seat>-<so>.md` gồm mã Tool/vấn đề, ca làm thật, câu/bước cần sửa, đề xuất và bằng chứng; **không sửa** `view.html`/`COLLAB.md`/`README.md` |
| Host duyệt và nhập chuẩn | [TQT-HOST-GATE](COLLAB.md) · Host đối chiếu, chấp thuận/từ chối và cập nhật một nguồn, kiểm kết quả; chưa có chốt chặn quyền máy riêng, theo TQT-ISS-006 |
| Đọc cách góp ý / việc bị tắc | [Cách góp ý](view.html#gop-y) · gửi theo file đề xuất nêu trên, không viết trực tiếp vào sổ chuẩn |
| Tiếp nhận thêm nguồn | Đọc TQT-SOURCES và TQT-REQ trong COLLAB; giữ mã/nguồn/hợp đồng hiện hành |

`view.html` là HTML chính duy nhất. Mục tiêu/tiêu chí/trạng thái điều hành nằm trong COLLAB; sổ vấn đề của task nằm trong `view.html#so-van-de`. Mỗi nội dung có đúng một nơi cập nhật.

Artifact/quy trình được bổ sung về sau phải đăng ký tại đây hoặc danh mục chuẩn được công bố trong task, để phiên tiếp theo biết lúc nào đọc và dùng.

Bộ nhớ P34 khi cập nhật tiếp: thêm sự kiện `changes` và phiếu `reviews`, không sửa phiếu cũ; chỉ ký lại công cụ có nguồn/hợp đồng/phạm vi thay đổi. Lần áp thử mới giữ hồ sơ cũ trong bằng chứng hiện hữu, không xoá lịch sử. Tra Master012 gồm bộ kiểm và ca; kết quả CAT015 phải trỏ mã có thật.

P36 · Chốt bằng chứng 2026-10-12T10:30:47.193507+00:00: nativefull1GiB PASS job1912451206cb4dd28b30f4447cdfcfc3 tại nguồn276f1ac4; Master xuất available, hash khớp25f4c02b..., trình duyệt đọc đúng5/7,28/34,CHO_DUYET. Công cụHVU hiện hữu48ca đạt, liên kếtalias khôngDOTtrùng. Giữ biên nhận worker lỗi ca08...; đề xuất chẩn đoán worker và tối ưu độ lớn lịch sử vẫn mở. MOW001 chỉG1 thiết kế, chưa nốiG2/PG; Owner duyệtvàxácnhậnnhận thực tế mới ghiCAT025/CAT232 vàquaCP06/07.

## P42 · Quy định và ghi nhận thực tế
Overview là cửa đọc luật7mốc/11mục/87bước, các phần đều thu/mở. Nguồn006 tại MOW-TH-006.md, bản chiếu kiểm bằng CHECK005. Hồ sơ DEF00.1 chỉ giữ bước chuẩn + ghi nhận thực tế; tool/kết quả/xác nhận trống tới khi có sự kiện đúng phiên. DONE/NOT_DONE là khai báo, không thay bằng chứng đã kiểm; không hồi tố G1. Xem §6 định nghĩa để ghi events vào nơi hiện hữu; chưa có UI ghi trực tiếp hay adapter xác thực bước. Không tạo bản hồ sơ thứ hai ở Overview.

### P43 · Điền hồ sơ ít nhất
Dấu ? tại từng cột và bước giải thích ngay nơi cần dùng. Ô thực tế để trống tới khi có ghi nhận; không điền sẵn trạng thái, tool hay nơi ghi. Tình trạng DONE=Đã làm, BLOCKED=Bị chặn (bắt buộc lý do), NOT_DONE=Không làm (quyết định + lý do), đều không thay bằng chứng đối chiếu. DONE phải có việc đã làm + kết quả/bằng chứng. Tool ghi mã đã dùng; kết quả trỏ bảng/bản ghi thật, nếu dùng nơi khác ghi nơi thực tế và lý do theo quyền hiện hữu. Người/thời điểm lấy từ sự kiện, giữ lịch sử.
Giữ nguyên mã CP chuẩn. Bước riêng khai trong detail_tracking.added_steps với id BS-001… duy nhất trong hồ sơ, after_step=mã CP chuẩn, action, reason bắt buộc, completion nếu có; chèn ngay sau CP đó. Event của BS dùng cùng hợp đồng event tại §6 MOW-TH-006.md. Không gán mã CP mới hoặc sửa 87 bước chuẩn từ hồ sơ; không có adapter ghi/xác thực bước mới trong P43. CHECK005 kiểm mã trùng/sai, neo bước, trạng thái bị chặn và ô trống.

### Quy ước hướng dẫn tại chỗ · Owner P44
Chuẩn hướng dẫn sử dụng là dấu **?** đặt ngay tại cột, mục hoặc thao tác cần giải thích: thao tác ở đâu, hướng dẫn đúng ở đó, không cần nhớ hay hỏi. Dùng cùng cơ chế mở/thu bằng chuột hoặc bàn phím; không chỉ dựa vào rê chuột. Hướng dẫn lấy từ nguồn quy định hiện hữu, không chép vào ô kết quả thực tế. Áp dụng hiện tại: 11 mục hồ sơ và 87 bước dùng chung dossierHelp; từng RG lấy instruction/checkpoint từ catalog.work_form.record_control.guidance. Khi sửa/thêm UI TQT, áp dụng cùng quy ước tại nơi dùng. Bản ghi, bằng chứng và lịch sử vẫn là dữ liệu thực tế để mở xem; dấu ? không thay bằng chứng hay dấu đạt.

## P45 · AI mới đi lại từ cửa vào
Lượt thật MOW001-QT006-P45-REAL ở CAT229, nối từ DEF00.1/TQT-VIEC-001. Host đã đọc/đối chiếu CP01.01–03; DỪNG tại CP01.04, chưa mở hồ sơ vòng mới. CAT069 có TQT-P45-F01/F02 (đã sửa luật/bộ kiểm) và F03 (chốt quyền/hợp đồng vòng mới chưa xác minh). Policy live chỉ ghim G1 cũ; không dùng quyền ghi tệp chung để coi vòng mới đã qua gate. Không đụng G1, MOW002, PG hoặc runtime. Nguồn lượt/bước thực tế: catalog.tool_registry.walkthrough_runs; đây là phần nhiều lượt của CAT229 hiện hữu, không Master mới. CHECK005 đã hỗ trợ kiểm pool hồ sơ đúng ID/nguồn/phiên; phép thử không thay việc thật.
Bằng chứng P60: [bộ kiểm và đọc lại UI](evidence/TQT-P60-checks.json). Ký đúng phiếu `TQT-P60-CORRECTIONS` trong hồ sơ CV-001, không ký bằng chat. Nguồn/phiên ghi trong manifest của phiếu.
