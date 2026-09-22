# Hiện hành — 16/09/2026

**Master list (List view) = Sổ:** đầu mối tập hợp đối tượng và thông tin đính kèm để tìm, kiểm tra, khai báo, mở Config. Đã có mẫu cha; chưa đủ chi tiết không đồng nghĩa thiếu UI cha.

Chỉ **Kanban view** và **List view (Master)**. MOIT và MOUT có hai màn riêng, cùng T0,5; Field T0. Mẫu nhìn đã có. Nhãn/config/chạy thật rà sau. Các ghi nhận bên dưới là lịch sử theo lượt; phần hiện hành trong HTML và mục này thay nhận định cũ “FIELD chưa có UI”.

# Từ thực tế — bản nhìn theo ma trận

Mở `từ thực tế đã làm.html`. Đây là file Owner chỉ định trong thư mục này.

## Cách dùng
- Mặc định và nút đầu tiên: **Đang tắc ở đâu?** — cây đối tượng → UI → mục kiểm, bảng quan trọng Owner xem mỗi ngày.
- Nút trên đầu: **UI đã có / còn thiếu**, **Mẫu × nơi dùng**, **Đang tắc ở đâu?**, **Vòng đời**.
- **Tất cả các bảng**: danh mục tự lấy từ toàn bộ bảng trong tài liệu, có tìm kiếm theo tên/cột và mở trực tiếp từng bảng; đã kiểm 43/43 đường mở.
- Mỗi lần hiện một bảng. **Chi tiết / nguồn** mở phần tra cứu; bấm ô vẫn dùng hành vi và dữ liệu sẵn có.
- Chữ và ô lớn hơn; bảng rộng cuộn trong khung, giữ tiêu đề hàng/cột. Lý giải dài của mẫu mở theo dòng.

## Danh mục
- HTML: dữ liệu, bảng, ảnh tham chiếu, luật và giao diện hiện hành.
- `backup/từ thực tế đã làm.before-matrix-views.html`: bản nguyên trước chỉnh giao diện ngày 15/09/2026, chỉ để khôi phục.
- Không tạo thêm bộ dữ liệu hoặc nhân bản bảng. Hai khối mới `matrix-views-style` / `matrix-views-script` chỉ điều khiển cách nhìn.

## Kiểm tra và phần còn mở
- PASS: dữ liệu, yêu cầu, sự kiện kiểm, luật chỉ số, script hiện có và các bảng nguyên văn không đổi; thẻ ảnh không đổi.
- PASS qua mô phỏng DOM (không tải tài nguyên mạng): 5 bảng, mỗi lần một bảng; chọn UI con; lọc ma trận; mở nhánh cây; khôi phục vị trí khi in; không lỗi JS trong các thao tác đã thử.
- Chưa kiểm thị giác bằng browser: chính sách công cụ chặn HTML local; không sử dụng cách vòng qua.
- Vấn đề có sẵn trước lượt này: HTML được chuyển sâu hơn và các đường dẫn ảnh hiện không resolve tại đây. Bộ ảnh được tìm thấy trong thư mục anh em `backup từ thực tế đã làm/assets/images/`; lượt này giữ nguyên thẻ ảnh, không chuyển kho ảnh.
- Nút thử cũ “MOT → Sổ” gọi mã mục không còn có hiệu lực trong dữ liệu hiện tại; không thay yêu cầu/luật hoặc hành vi nút cũ trong lượt chỉnh cách nhìn này. Mở nhánh cây thủ công đã kiểm được.

## Sửa lại theo Owner

Lượt trước đặt UI Master làm mặc định khiến bảng theo dõi hằng ngày bị khuất. Đã trả cây 8 bước về nút đầu tiên và mặc định, khôi phục khu Đang tắc bên phải trên màn rộng; thêm danh mục mọi bảng, không bỏ bảng nào.

Bản trước sửa: `backup/từ thực tế đã làm.before-daily-matrix.html`. PASS mô phỏng DOM: mặc định đúng, 43 bảng đều có đường mở và không bị tổ tiên ẩn/đóng, tìm bảng và quay lại cây, không lỗi JS. Chưa kiểm trực quan bằng browser do giới hạn file local đã nêu. Dữ liệu, luật, các bảng gốc nguyên văn giữ nguyên.

Owner xác nhận vai trò: **Đang tắc ở đâu?** là bảng tổng hợp chính của các chỉ số đạt/chưa đạt/chưa rõ, đứng trước UI Master. Những bảng khác là bảng hỗ trợ để đối chiếu và hoàn thiện bảng tổng hợp. Thứ tự được cố định cả trong HTML và lúc dựng thanh nút.

## Rà UI đã duyệt — 15/09/2026

- Cập nhật trực tiếp HTML theo Owner: **85 mục kiểm** (từ 18), **50 ô UI** cập nhật. Đã đọc **12/12 nguồn/vùng UI được chọn** bằng browser.
- Chỉ chấm trục UI. 57 mục có bằng chứng UI, 7 còn một phần, 20 thiếu/lệch đã ghi nhận, 1 chưa đủ căn cứ. Đây là số mục, không phải số màn hay tỷ lệ hoàn thành hệ thống.
- 5 bản Form cũ chưa duyệt được giữ trong `excluded_ui_records`, loại khỏi nguồn chấm. 6 chỗ trống trong cây là nhu cầu còn thiếu, không cộng thành UI đã làm. Ba Studio vẫn là ba bộ riêng, cùng định dạng.
- Nguồn hiện hành: JSON trong HTML và các bảng chiếu từ chính dữ liệu đó. Lịch sử sự kiện cũ được giữ; các trục hợp đồng/kết nối/test không được kiểm mới. Danh mục vẫn mở; không thêm kỳ đo hay sự kiện đóng.
- Cần làm tiếp cùng Owner: các mục đỏ và một phần trong cây; chưa thiết kế UI mới trong lượt này. Các báo cáo ghi 18 mục/72 kết quả trong tài liệu là lịch sử trước cập nhật.
- PASS kiểm cấu trúc/mô phỏng DOM: 12/12 UI chọn có mục, mở cả 85 mục, 43 bảng đều có đường truy cập, tổng không trùng mục dùng chung, giữ mặc định Đang tắc ở đâu, không lỗi JS. Luật tổng hợp/chỉ số và ảnh giữ nguyên.
- Chưa kiểm thị giác local vì chính sách browser chặn file local; vấn đề đường ảnh có sẵn vẫn còn như ghi phía trên.
- Backup nguyên bản trước rà: `backup/từ thực tế đã làm.before-approved-ui-audit.html`.

## Hiệu chỉnh cách hiểu — hai lớp rà soát

Owner yêu cầu (1) có UI hợp lý trước; (2) rà nhãn/mục thông tin để lập hợp đồng, tiếp tục thay đổi từng chi tiết. Bảng lớp 1 nằm trên đầu Đang tắc ở đâu; các bảng cũ vẫn truy cập được.

85 mục/20 thiếu-lệch của báo cáo trước trộn cấp độ, không dùng để đếm UI thiếu. Đã rút 4 kết luận quá sớm về Studio riêng và tạo/config MOIT về cần cùng xem; lịch sử còn nguyên. Studio MOIT/MOUT có mẫu được chọn. Master MOIT/MOUT và quản lý FIELD chưa có theo Owner. Chưa chốt hết khung nhãn/hợp đồng, chưa thiết kế sản phẩm mới.

Backup: `backup/từ thực tế đã làm.before-two-review-layers.html`. Hiện có thêm bảng lớp 1; danh mục mọi bảng tự nhận bảng mới.

Kiểm sau tách lớp: PASS 44/44 bảng truy cập được, 85 mục và hồ sơ mở được, không đếm trùng, không lỗi JS trong mô phỏng DOM. Luật tổng hợp/chỉ số và thẻ ảnh nguyên vẹn. Chưa kiểm thị giác local do giới hạn browser đã ghi.

## Dễ nhìn quan hệ mẹ/con — 16/09/2026

Theo Owner: ưu tiên hình dạng, màu nền và khoảng lùi để nhận biết, không buộc đọc tên để suy quan hệ. Đã sửa CSS bị padding chung ghi đè: hàng mẹ lùi 14px, UI con 42px, mục chi tiết 70px; nền hàng mẹ đậm hơn, tên mẹ đậm, đường nhánh nhẹ nối hàng con. Áp dụng mọi nhóm và hai cách gom cây. Chỉ sửa trình bày; dữ liệu, bảng và luật nguyên vẹn.
Backup: `backup/từ thực tế đã làm.before-hierarchy-indent.html`.

Kiểm: PASS thụt lề 3 cấp ở cả cách gom theo đối tượng và theo mẫu; 44 bảng vẫn truy cập được, không lỗi JS qua mô phỏng DOM. Chưa kiểm thị giác browser local do giới hạn đã ghi.

## Chốt mẫu cha trước — chỉ đạo Owner 16/09/2026

**Bắt đầu tại nút UI Master.** Bảng đầu gán mẫu cho Tìm → Tạo → Sổ → Config → Test → Dùng → Chạy → Ngừng. Các chỗ chưa gán không tự có nghĩa cần thiết kế mới.

Quyết định hiện hành: Sổ dùng một Master list chung, UI con thay label; Kanban view 7 tầng chính là Kanban. Những ghi nhận trước đây “Master MOIT/MOUT chưa có UI” và “Kanban view chưa phải Kanban” đã được thay bằng quyết định này. Mẫu cha đã có không đồng nghĩa UI con/config hoàn tất.

Ba vòng: Owner chốt mẫu cha (rõ màu); AI rà label UI con (phần thu gọn); AI kiểm config và đủ 8 tình trạng (nhạt màu, mở khi cần). Không thay luật tính chỉ số. Có thêm bảng gán mẫu, các bảng cũ vẫn truy cập qua Tất cả các bảng.

Nguồn chuẩn: `du-lieu-kiem-dem-ui.parent_review` trong dữ liệu HTML. Chưa tự chốt các gán mẫu còn mở: các phần chi tiết Test, Dùng, dữ liệu/sự kiện và Ngừng (UI tạo MOUT đã được xác nhận). Không tạo mẫu cha mới trong lượt này.

Backup: `backup/từ thực tế đã làm.before-parent-first-review.html`.

Kiểm: PASS bảng gán mẫu 8 tình trạng, nguyên tắc Master/Kanban view áp dụng, UI con thu gọn và mở được, 45/45 bảng truy cập được, không lỗi JS qua mô phỏng DOM. Chưa kiểm thị giác browser local do giới hạn đã ghi; không truy cập hay sửa sản phẩm trên VPS trong lượt này.

## Kanban view dùng chung — 16/09/2026
Owner chốt UI.CANVAS cho MOW/MOIT/MOUT/FIELD: T2–T7 cùng mẫu; T1 riêng; T0,5 hai ô MOIT/MOUT; T0 Field theo form. Nút UI Master có khối chốt và link trực tiếp. Tầng dưới đã triển khai trên Kanban view VPS, vẫn là dữ liệu minh họa; chưa chốt nhãn/config/PG, không thay Studio/Builder/Master. Các nhận định cũ “FIELD chưa có mẫu nhìn” được thay bởi quyết định này. Không thêm mẫu cha hay đổi luật chỉ số.

Kiểm lượt Kanban view: PASS browser VPS — hai ô T0,5, mở Field MOIT/MOUT, tải lại giữ form, T2 giữ 6 ô, T1 Thường đạt kiểm bố cục và Đề xuất giữ mẫu riêng, không ghi nhận console error. PASS mô phỏng DOM local: 45 bảng tiếp cận được, sáu mẫu cha giữ nguyên. Backup trước sửa: `backup/từ thực tế đã làm.before-shared-canvas.html`.

## Đồng bộ hai view và tách loại T0,5
Dữ liệu nguồn, danh mục UI con, ma trận, trạng thái Field và tên hiển thị đã cập nhật cùng lượt. Có 2 mẫu view; các mẫu phần làm việc không cộng thành view mới. Mã UI.CANVAS và URL cũ được giữ ổn định. Backup: `backup/từ thực tế đã làm.before-kanban-list-sync.html`; bản cấu trúc hệ thống trước đổi tên: `backup/cau-truc-he-thong.before-kanban-list-sync.html`.

Kiểm đồng bộ: PASS 2 loại view; MOIT/MOUT hai URL riêng cùng T0,5; bảng nguồn, 3 UI Kanban, nguồn tham chiếu và trạng thái có mẫu đồng nhất. Đã rút kết luận thiếu toàn bộ Field; chi tiết label/config giữ chưa rõ. PASS 45 bảng đều tiếp cận được, ID duy nhất, hash các khối đúng, không lỗi JS qua mô phỏng DOM. VPS: đã kiểm màn tách loại, menu chọn đúng loại, Field theo form, tải lại giữ URL; T1 `data-t1-audit=ok`, không console error. Browser local vẫn chưa kiểm do giới hạn đã ghi.

## Master list là đầu mối — quyết định hiện hành
Master list (List view), trước đây gọi là Sổ, là một đầu mối tập hợp các đối tượng đã tạo cùng thông tin đính kèm để tìm, kiểm tra, khai báo và mở cấu hình cho chạy.
Đang rà mẫu UI cha. Master list đã có mẫu; chưa đủ label, thông tin đính kèm hoặc đường mở Config là phần UI con/config cần rà, không phải thiếu một mẫu Sổ riêng.
Đã cập nhật định nghĩa, mẫu cha, 8 tình trạng, danh mục/mapping và rút kết luận thiếu UI cha NTGV do cách gọi Sổ. Các lỗi link, nhãn/config và chạy thật chưa được tự chuyển thành đạt. Backup trước lượt: `backup/từ thực tế đã làm.before-master-list-entry.html`.

Kiểm lượt Master list: PASS định nghĩa/nhãn tình trạng 3; mẫu cha và các bảng chiếu đồng nhất; NTGV chuyển về cần rà phạm vi chi tiết; lỗi đường mở Config thực tế vẫn giữ cảnh báo. 45 bảng đều mở được, không lỗi JS qua mô phỏng DOM, hash các khối đúng. Nguồn khai báo VPS đã đồng bộ định nghĩa; lượt này không sửa luồng vận hành UI.

## Hiệu chỉnh trạng thái UI tạo MOUT
Builder v3 đã được Owner xác nhận là UI tạo MOUT: ghi **Đã có UI tạo MOUT**, không còn chờ chốt hoặc chờ mã phân loại. Đồng bộ bảng mẫu cha, dữ liệu nguồn, danh mục UI, bảng ánh xạ và cây/hồ sơ. Lỗi nhãn/config vẫn được giữ riêng. Cách hiểu cũ yêu cầu chốt phần tạo MOUT trong các lượt trước đã bị thay thế.

Kiểm lượt này: PASS trạng thái MOUT thống nhất ở dữ liệu, bảng mẫu cha, danh mục và ma trận; không còn nhãn cũ yêu cầu chốt MOUT trong bản hiện hành. 45 bảng đều mở được qua mô phỏng DOM; giữ nguyên mục kiểm, lịch sử đánh giá, luật và chỉ số. Đã quét file HTML trực tiếp tại thư mục quy trình và nguồn HTML/JS trực tiếp của xưởng VPS: không có nhãn yêu cầu chốt MOUT còn sót. Bản backup giữ nguyên để truy lịch sử; không phải bản hiện hành.

## Đơn giản hóa rà mẫu theo Owner
Kanban thiếu tìm kiếm chung; các mẫu Tạo, Master list, Config, Test, vận hành chính T1/T2 đã có. Ngừng dùng trạng thái + List; thao tác hàng loạt chưa triển khai trong lượt này. “Dùng” cũ là được phép áp dụng/đã duyệt; đề xuất gộp trạng thái, chưa xóa mã bước/điều kiện duyệt trong dữ liệu cũ. Đề xuất tìm kiếm và đánh giá Google nằm ngay trong UI Master. Không dựng sản phẩm tìm kiếm mới ở lượt bàn này.

Kiểm: 45 bảng vẫn truy cập; không lỗi JS qua mô phỏng DOM. Phân biệt List đã có tìm với Kanban thiếu tìm kiếm chung; đề xuất gộp Dùng còn ghi rõ là đề xuất. 85 mục kiểm, lịch sử kết quả, luật/chỉ số giữ nguyên, hash hợp lệ.

## UI con và tìm kiếm · 16/09/2026
Danh mục chuẩn UI-B01 nằm trong file HTML chính (nút **UI con · mã & link**): 29 mã ổn định; registry VPS là bản xuất để gắn mã trên UI. UI-029 là khung tìm kiếm mới, dữ liệu minh họa, chưa nối nguồn/quyền thật; Owner xem rồi rà nhãn/config. Giữ hai view Kanban và Master list.

UI-B02: danh mục UI con nằm **bên dưới mẫu cha trong UI Master**; một bảng 7 cột chia 7 khu vực, số đếm 21 có / 7 cần bản riêng / 1 khung chờ xem. Nút UI con riêng đã bỏ; mã giữ nguyên.

Quy chuẩn mẫu cha: trong UI Master, mục `#parent-ui-standards`, gồm 6 mẫu và ghi chú T1/MOUT Builder. Agent đọc trước khi làm UI con; phân biệt nguyên tắc Owner với thông số hiện trạng. Điểm còn mở nằm ngay cuối mục. Không thêm loại view hay sửa UI nguồn ở lượt này.

UI-B03: UI-013/014/015/016/017 đã có bản riêng, dùng trực tiếp nguồn cha; menu MOIT/MOUT đã gắn link. Tổng danh mục 29 = 26 có + 2 Field chưa có bản riêng + 1 khung tìm chờ xem. UI mẫu, chưa nghiệm thu nhãn/config/PG.

UI-B04: UI-018 có khung khai báo Field riêng (tên, định dạng, mô tả, nhóm quản lý), tái dùng modal/form Kanban. 29 UI = 27 có + 1 Master Field cần bản riêng + 1 tìm kiếm chờ xem. T0,5/T0 đồng bộ đường dẫn các chế độ và danh sách; đề xuất chưa áp dụng vận hành, chưa nối PG.

Kiểm UI-B04: PASS 12 tổ hợp tầng/chế độ, form Field lưu và mở lại, tách đề xuất khỏi Vận hành, tách MOIT/MOUT, T1/T2 không đổi mẫu. Browser kiểm Config → T0,5 MOUT giữ Đề xuất; Master MOIT có tầng form/Field; không lỗi JS. 46 bảng của tài liệu vẫn truy cập được.

UI-B05: 29/29 UI có khung; UI-022 Master Field theo nguồn cha; UI-029 được Owner xác nhận OK. Sửa lỗi bảng HTML tĩnh còn nhãn cũ bằng dựng nhãn trực tiếp từ registry. Xanh chỉ xác nhận có UI, nhãn/config/PG rà riêng.

Kiểm UI-B05: 29/29 URL trả HTTP 200; 29 nhãn có UI màu xanh, không còn nhãn thiếu/chờ trong bảng UI con; bảng tĩnh và bảng hiển thị đồng bộ. Master Field mở đúng Họ và tên trong UI-018; không lỗi JS. 46 bảng vẫn truy cập. Chưa nghiệm thu chức năng/PG toàn bộ 29 UI.

Sửa dòng Tìm trong bảng mẫu cha UI Master: nhãn tĩnh cũ còn vàng dù quyết định đã chốt. Đã chuyển “Đã chốt UI tìm kiếm” sang xanh và đọc lại quyết định từ dữ liệu nguồn khi mở trang. Không đổi trạng thái nhãn/config/PG.

Gate 1 · đường tạo mới: nội dung chuẩn nằm tại `../cấu trúc hệ thống.html#gate1-human-paths`; UI Master chỉ liên kết. 5 đường MOW/MOT/MOIT/MOUT/Field, mỗi đường 6 chặng trình bày để Owner rà; không phải quy trình đã duyệt. Giữ Gate 0 và bằng chứng Gate 3–4. Số form máy chưa xác định.

Owner 16/09: file này là đầu mối người đọc. UI Master đứng đầu/mở mặc định; tab Quy trình đứng thứ hai, trước mắt 8 bước mô tả tạo MOW, đúng 5 cột. Chi tiết cũ chỉ liên kết trong Nguồn đối chiếu, không yêu cầu Owner đọc file khác. 8 bước là bản để cùng chốt, chưa nghiệm thu luồng.

17/09: UI-029 đã thêm nút Quay lại; liên kết tìm kiếm giữ đường dẫn màn nguồn, tầng và chế độ. Đã thử Thường và Đề xuất trên browser.

17/09 · Owner xác nhận T1 Đề xuất phải có toàn bộ Config ngay trong Kanban, gồm MOIT/MOUT, bảng kết nối, Nguyên tắc giao việc, Ai làm & ai nhận, Chạy & kết thúc. Đã thay nhận định một cột trong UI Master và dữ liệu chuẩn. VPS dùng một module chung với New MODT. Backup: `backup/từ thực tế đã làm.before-t1-full-config.html` (trước khôi phục, chỉ để truy nguồn). Bảng MOW 8 bước và các bảng hiện có giữ nguyên. Đây là khôi phục UI, chưa nghiệm thu chạy thật.

17/09 · Bổ sung theo Owner: T1 Đề xuất hiển thị các task theo chiều dọc: thu gọn còn một dòng, mở task hiện toàn bộ Config hai cột. Dấu + trước/giữa/sau dùng lại form thêm mới; tạo task đồng thời có MOIT/MOUT, bảng bên phải và ba nhóm Config. Một task mở tại một thời điểm. Nguồn chuẩn và bảng UI Master cập nhật đồng thời. Backup: `backup/từ thực tế đã làm.before-t1-task-list.html`, chỉ để khôi phục. Không sửa bảng MOW 8 bước hoặc nghiệm thu runtime.
