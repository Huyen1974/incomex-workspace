# Rà soát P36 — năm mục tiêu và điều kiện duyệt G1

Ngày rà: 12/10/2026. Vai: phản biện kỹ thuật; không sửa nguồn, Master, dữ liệu công việc, tiến độ hoặc PostgreSQL.

## Kết luận

Báo cáo của Codex có căn cứ đối với **ca thiết kế MOW001/G1**: năm checkpoint được kiểm đạt, 28/34 nghĩa vụ đã ghi và đối chiếu; bản thiết kế P02/P03 có thật và đọc lại được. Có thể trình Owner duyệt và xác nhận nhận G1 ở mốc 6–7. Không dùng kết luận này để nghiệm thu cả cỗ máy, khẳng định mọi công việc đã tự chạy, hoặc xác nhận chuyển PG đã sẵn sàng.

Không phát hiện chốt hỏng mới buộc làm lại G1 trong các phép kiểm của lượt này. Đây là kiểm có phạm vi, không bảo đảm tuyệt đối không còn lỗi.

## 1. Nguồn và bằng chứng

Nguồn được kiểm trong snapshot VPS tại `86929860b305f90cc9ae6c763079a4ae3c9ab8df`.

| Nguồn | Dấu vết |
|---|---|
| Phiếu `work/mow-mot-moit-mout/UI-REVIEW-MOW001.json` | SHA256 `ec1620205a41c174f98a38b77225a2151811745a65e2c42f11c1d21fd774d6df` |
| `work/tools-quy-trinh/view.html` | SHA256 `3157934bb4ba145baf07e82a75b38f875cc5665165a0b779c8fbf8361fc13dbc` |
| Bộ kiểm `check-record-control.js` | SHA256 `d0082b51b9c73f23f5f42b87df3794f2f3b8c48a9773ceab781bdc01fb389767` |
| Runner `run-tqt-checks.py` | SHA256 `853277b94ff834e5d2b516c5ee65111f73234f7c5c03721b5356da7a1f9247e6` |
| UI đang triển khai `ui/mow-ui-walkthrough-v1.js` | SHA256 `02230bf383141b41f5d09bb586cc34ab6981777a25ddd805a58bbdc451d132e4`; khớp `target_version` trong phiếu |

Hồ sơ: `MOW-NHC-001-G1-20261010-01`. Quy trình điều phối: `MOW-TH-005@1.1-design`. Sản phẩm: `MOW-NHC-001`. Phạm vi: G1 thiết kế ba MOT 1.1/1.2/1.3; không phải G2/G3. Hợp đồng áp dụng phiên 5, schema 1.4, kế hoạch phiên 4, build `MOW001-G1-UI-P36.1`.

Các lượt đã đọc hoặc tự chạy:

| Lượt | Job ID | Kết quả và giới hạn |
|---|---|---|
| Bộ kiểm tổng Codex đã chạy trên VPS | `1912451206cb4dd28b30f4447cdfcfc3` | Đã mở đầu ra gốc: PASS, exit 0, 354,827 giây; nguồn `276f1ac407e32f1a7821b0d3ed163f5dd50b4f42`. Đọc lại đúng hash phiếu trên. Tôi kiểm chứng biên nhận này, không tuyên bố tự chạy lại cả bộ tổng trong lượt mới. |
| Kiểm hồ sơ, mốc, kết quả, phần còn thiếu | `e1f4d3cf227c4dcb96fa14d2db2accc6` | Chỉ đọc; phiếu 54.718.998 byte; danh sách P01–P04 DONE, P05 TODO; các kết quả và lịch sử hiện hữu. |
| Dùng lại CHECK004 đọc bản thiết kế thật | `6854a4450d65466dad622e1b02493a3d` | Chạy `node --max-old-space-size=512 check-record-control.js view.html --read-designs ../mow-mot-moit-mout/UI-REVIEW-MOW001.json`; exit 0, REAL_DESIGN_READBACK, READ_AND_CHECKED; không dùng fixture TEST. |
| Kiểm chữ ký, trạng thái và hai ca đối chứng trên bộ nhớ | `6c23acfa4b8549d793d42e02494bb3c1` | Dùng nguyên reader/chữ ký/engine CHECK004, không sửa source. Nguồn thật: CP01–05 đạt; tự điền APPROVED/ACK giả không làm CP06/07 đạt; bỏ kết quả P04 làm CP05 mất đạt nhưng giữ CP01–04. Khôi phục bộ nhớ trả đúng 5/7. |
| Rà DOT và thiết kế PG | `85ac80d070534ef4b787736b90885d17` | Sáu file bộ kiểm khớp hash khai trong registry. PG record-control ghi LOGICAL_DESIGN_ONLY, chưa đưa toàn phiếu vào gói SQL hoặc chạy PG. |

Lượt kiểm đầu tiên `df7297a23ce34aa095b0c1ba1564ef84` bị lỗi đường dẫn tương đối trong đoạn đọc của reviewer; không có dữ liệu bị sửa. Đã thay bằng lượt đọc đúng `e1f4d3...`, không coi lượt lỗi là bằng chứng kiểm đạt.

## 2. Đánh giá năm mục tiêu

| Mục tiêu của Owner | Đánh giá trong ca hiện tại | Phần chưa thể kết luận |
|---|---|---|
| Mọi việc có thứ tự | QTTH05 có 7 mốc, kế hoạch có quan hệ trước–sau, bằng chứng chặn mốc; ca này đi qua 1–5 và dừng đúng trước quyết định Owner. | Chưa chứng minh toàn bộ công việc trong hệ thống đều áp dụng cùng kỷ luật. |
| Theo quy trình ra kết quả | Có bản thiết kế G1 P02/P03 thật; bộ đọc độc lập kiểm được nội dung, hash và phiên. Phiếu P04 có 11 tiêu chí G1 PASS. | Chưa hết 7/7, chưa chạy nguồn Field/evaluator/consumer nghiệp vụ G2; chưa chứng minh một agent mới có thể lặp lại toàn ca mà không nhờ tác giả can thiệp. |
| Mọi thông tin có sổ | 34 nghĩa vụ đã xác định cho ca này có sổ/collection đích; 28 đã ghi và đối chiếu. Cả dữ liệu sai/thiếu và thay đổi có hồ sơ nối về việc. | Đây là bao phủ của ca đã khai, không phải bằng chứng mọi loại thông tin của toàn hệ thống đã được kiểm kê đầy đủ. Loại mới phải tra Master và khai nơi ghi trước mốc sử dụng. |
| Tương thích PG | Đã thiết kế khóa, phiên, quan hệ, bảng checkpoint và nghĩa vụ ghi; giữ dữ liệu ngoài PG đúng chỉ đạo. | Nguồn tự ghi LOGICAL_DESIGN_ONLY, chưa đưa toàn phiếu vào gói SQL; chưa có vòng chuyển dữ liệu thật sang PG rồi đọc lại và đối chiếu. Không được tuyên bố đã tương thích hoàn toàn. |
| DOT/Tool dùng lại và nhanh hơn | Sáu bộ kiểm đã dùng lại thực tế, có hash, ngân sách chạy, ca hồi quy, biên nhận và công cụ đọc bản thiết kế. Có danh mục công cụ nền/dùng lại, không chỉ sáu file cũ. | Công cụ được tìm thấy không đồng nghĩa đã nghiệm thu chạy tốt. Thu thập mọi bề mặt và hiệu quả một agent mới/lần thứ hai chưa được chứng minh toàn diện. |

## 3. Vì sao 28/34 không phải còn sáu lỗi

Ba nghĩa vụ phải hoàn thành ở mốc cuối:
- `DECISION` → CP06 → CAT-025: quyết định Owner.
- `RESULT-P05` → CP07 → CAT-228*: kết quả hoàn tất việc duyệt/bàn giao.
- `ACK` → CP07 → CAT-232*: xác nhận nhận.

Ba nghĩa vụ có điều kiện, hiện chưa kích hoạt trong hồ sơ: `BLOCKED`, `CANCELLED`, `NA`. Không tạo bản ghi giả cho ba nhánh này để ép tỷ lệ 34/34. Tiêu chí kết thúc là đủ nghĩa vụ áp dụng và đúng mốc, không phải mọi nhánh có dữ liệu.

Mốc đang xét CP06 có đúng một nghĩa vụ đến hạn chưa ghi: quyết định. P05/ACK thuộc CP07. Trạng thái ký thật được bộ tính trả: `canStart=true`, `canFinish=false`, `needsFix=0`.

## 4. Những phần còn phải quản, không biến thành vòng thiết kế mới

### A. Trạng thái hiện hành chưa đồng bộ hết

README P36 và job tổng xác nhận PASS; Bảng điều khiển COLLAB vẫn ghi `PENDING_RECHECK`, còn chờ bộ tổng cuối. Nên cập nhật đúng nguồn này, không thêm một đoạn đính chính ở cuối.

Trang hồ sơ đã hiện 5/7, nhưng RG04/RG09 còn nhãn nguồn chung “Chưa khai nguồn lưu”; trong khi kho tệp thử có cấu trúc và quyền theo biên nhận hiện hành. Nên tách: **kho tệp G1 đã có; bản ghi bàn giao chưa phát sinh; nguồn PG/chức năng toàn Master chưa nghiệm thu**. Không đổi Master toàn hệ thống thành sẵn sàng chỉ vì một tệp đã dùng được.

Trang UI vẫn ghi “Chuyên môn (cha của MOW): Chưa khai báo”. Đây là khoảng trống mô tả/phân loại cần giữ trong sổ; không tự coi đã phân loại toàn hệ thống. Phạm vi G1/MOW001/3 MOT trong hợp đồng hiện tại vẫn được khai rõ.

### B. Hồ sơ tăng quá lớn so với mục tiêu dùng lại nhanh

Một phiếu đã 54.718.998 byte, view.html 56.321.696 byte. Trong cách tuần tự hóa gọn của application: history khoảng 35,57 MB; checkpoint_checks khoảng 12,01 MB; hai bản thiết kế khoảng 0,50 MB. Bộ tổng mất khoảng 355 giây. Có bằng chứng đã từng phải xử lý lỗi worker/đọc–ghi/xuất bản do hồ sơ lớn; không đủ căn cứ kết luận mọi lỗi trước đều do một nguyên nhân.

Không xóa lịch sử hoặc giảm kiểm để làm nhẹ. Trước khi nhân rộng, lưu phiên bất biến một lần và tham chiếu bằng ID/hash thay vì mang toàn nội dung lặp trong mọi bản kiểm. Thực hiện dưới quản lý phiên; không tự đổi mô hình trước lúc duyệt G1 hiện tại. Mốc 6/7 vẫn phải dùng đúng cửa ghi, kiểm trước–sau, theo dõi task và đọc lại; lỗi tài nguyên thì dừng/khôi phục, không bỏ chốt.

### C. Giới hạn của kiểm độc lập và khả thi toàn hệ thống

P04 là lượt reviewer kỹ thuật được giao riêng, cùng OpenAI; nguồn đã nói rõ không phải ghế/quorum khác hãng. Owner đã cho phép thiếu Claude không tự là blocker. Lượt kiểm này dùng reader/cổng hiện hữu trên hồ sơ thật, nhưng không thay việc Owner nhìn và chấp nhận thiết kế.

Đây là lần vừa xây vừa sửa đến kết quả. Cần một lượt AI mới lặp từ tài liệu đã chốt để chứng minh tiêu chí “không hỏi thêm, làm theo ra sản phẩm”; thực hiện sau khi đóng G1, không buộc chứng minh toàn máy trước khi nhận sản phẩm G1 đã làm.

## 5. Cách đi mốc 6–7

1. Owner xác nhận rõ chỉ duyệt và nhận **thiết kế G1 MOW001**, đúng build/phiên trong gói bàn giao. Lệnh “tiếp tục làm” không tự là quyết định nghiệm thu.
2. Host ghi quyết định tại CAT-025, đúng phiên hợp đồng/sản phẩm; kiểm CP06 qua cửa ghi hiện hữu.
3. Hoàn thành P05, ghi kết quả CAT-228* và ACK CAT-232*. ACK iframe minh họa không thay ACK Owner.
4. Chạy kiểm theo đúng phiên sau ghi và đọc lại: CP01–07 đạt, không tăng bằng dữ liệu TEST; không đổi “đã bàn giao G1” thành “G2/G3 đã vận hành”.

Không đề xuất QTTH06, Master mới hoặc chạy PG ở lượt này. Các việc dọn trạng thái, tối ưu hồ sơ, kiểm chuyển PG và kiểm lặp bằng AI mới giữ trong sổ hiện hữu, giao Host xử lý theo đúng giai đoạn.

## 6. Công cụ của lượt rà này

Dùng lại CHECK004 --read-designs; reader chữ ký và tqtRecordAudit nguyên bản; workspace_read/search/stat/exec/exec_status, ui_inspect. Có đoạn Python chỉ đọc để tổng hợp dữ liệu/hash và đoạn Node kiểm hai tình huống trên bộ nhớ; đây là lệnh kiểm một lần, không đăng ký công cụ mới. Các job và SHA đầu ra ở phần 1 đủ để Host gắn vào lịch sử sử dụng công cụ hiện hữu. Không gọi JEV trong lượt này. Không tạo/sửa dữ liệu repo, Master, tiến độ, API ghi hoặc PG; tệp báo cáo này chỉ là bản giao người dùng.

## Liên kết xem

- Hồ sơ: https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/process-work-master-v1.html?master=DEF00.1&chi-tiet=TQT-VIEC-001
- Ba màn G1: https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/mow-ui-walkthrough-v1.html?mow=MOW-NHC-001&step=2
