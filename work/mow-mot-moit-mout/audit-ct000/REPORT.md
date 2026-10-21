# CT-000.4 — rà bản 107 dòng

**Kết luận: CHƯA ĐẠT H4.4a.** Có ba ca phản ví dụ trên bản gốc và các lỗ của máy kiểm. Không dùng riêng mã thoát 0 của `--dot-bien` làm điều kiện khép kín ở phiên hiện tại.

Nguồn ghim: head `250792dce8380e94aa5fe85ce22477925150e6b8`; hash trong README/manifest. Không sửa CT-000.4 hoặc máy kiểm của Host; không chạy PG/Flow.

## Đã xác nhận

35 trạng thái, 107 dòng, 226 bộ trạng thái–sự kiện–giá trị, 49 thao tác, 11 biểu thức B1–B11; L1–L4 do hàm riêng kiểm. Kiểm tĩnh 0 lỗi, 16/16 ca gốc đạt. Hàm đột biến sinh 242 bản. Chưa chạy lại hết 17 đồ thị hoặc toàn bộ 242 đột biến; dùng các probe nhỏ có phản ví dụ cụ thể để không tiêu tốn tài nguyên cho một tiêu chí kết luận còn sai.

## A. Ba đường sai trên bản gốc

| Mã | Dữ kiện và đường đi thực chạy | Quan sát | Sửa tối thiểu |
|---|---|---|---|
| F-DEADLINE | T01 → T05 → T08 → T12; sau nhận, qua hạn gốc; lease còn; T15 | `quá_hạn_gốc=True`, nhưng `đang_bay: 0→1`; B1–B11 không báo. | Kiểm hạn gốc tại chỗ cấp phép tác động mới; hết hạn không gửi. Vẫn cho ghi nhận/đối soát tác động cũ. |
| F-COMPENSATION-BUDGET | MB=1; T81 gửi bù lần 1; `bù mất`; qua hạn giữ; T88 | `lần_bù: 1→2` trong khi MB=1; B1–B11 không báo. Guard dùng `lần_bù > MB` trước khi tăng. | Mọi lần bắt đầu bù phải kiểm số lần trước tăng `< MB`, rồi tăng và ghi lệnh. Kiểm T66/T81/T88/T90/T94. Không chặn ghi kết quả lần cuối đã được cấp phép. |
| F-RECOVERY-DEADLINE | T81; `bù mất`; qua hạn PH; qua hạn giữ; T88, MB còn | Hạn phục hồi đã hết nhưng vẫn phát sinh lệnh bù mới; B1–B11 không báo. | Kiểm PH trước mỗi lần phát sinh tác động phục hồi. Hết PH đi quyết định Owner theo quy trình; ghi nhận/đối soát lệnh cũ tiếp tục. |

Bốn đối chứng đã đạt: đường thường, gửi trước hạn, huỷ chặn lượt cũ và MB còn cho thử lại. Các kết quả trên là hành vi của mô hình, không phải sự cố đã xảy ra trên VPS. Duyệt hết đồ thị vẫn có thể bỏ sót nghĩa vụ nghiệp vụ nếu không có bất biến hoặc probe kiểm nghĩa vụ ấy.

## B. Máy kiểm đang cho phép kết luận quá mức

### E03 — Kiểm đồng thời chưa chạy công thức nhận việc thật

Đột biến trên bản sao: đổi `hết chỗ ← not còn_chỗ` thành `hết chỗ ← False`. Kết quả: kiểm tĩnh 0, 16/16 ca đạt, phép kiểm hai việc tranh một chỗ PASS.

Đưa `còn_chỗ=False`: bản gốc đi T11 về Chờ; bản sửa sai đi T12 vào Đang chạy. Hàm `dong_thoi()` đọc tên có/không của khoá/giữ/nhả rồi chạy chương trình cạnh tranh riêng viết cứng; không chạy bộ phân loại `xin nhận` thật. Cả 17 trạng thái khởi tạo đều có `còn_chỗ=True`, không có phép gán hoặc sự kiện bên ngoài đổi biến đó. Vì vậy tăng RAM để duyệt 17 đồ thị ấy không làm xuất hiện trường hợp hết chỗ này.

**Sửa:** hai việc dùng chung dữ liệu sức chứa và cùng bộ điều kiện/thao tác từ bảng; thử đầy chỗ, hai bên tranh chỗ cuối, nhả rồi nhận lại. Đây chưa phải test khoá PG thực.

### E01/E02 — Chưa duyệt hết hoặc máy kiểm lỗi lại được tính là bắt đột biến

`kham()` khi vượt trần trả `('quá lớn', n)` cùng `graph=None`. `main()` tính mọi danh sách lỗi không rỗng là đột biến đã bị bắt. Nó cũng bắt mọi Exception rồi tính tương tự.

Probe của nhánh báo cáo: giả lập baseline đã đạt để cô lập nhánh đếm; một mutant trả `quá lớn`, hoặc ném RuntimeError. Cả hai đều khiến nguyên `main()` in `bắt được 1 / sống sót 0` và thoát 0. Đây là unit fault injection vào bộ tổng kết, **không phải đã chạy đầy đủ 17 kịch bản ra 0**. Một lần chạy thật `kham()` với trần nhỏ trên dữ liệu gốc đã xác nhận kết quả vượt trần nêu trên.

**Sửa:** kết quả có trạng thái riêng: `KILLED` (lỗi xác định, có bằng chứng), `SURVIVED` (duyệt đủ không bắt), `INCONCLUSIVE` (hết tài nguyên/chưa xong), `CHECKER_ERROR` (máy kiểm lỗi). Hai loại cuối làm chiến dịch chưa đạt, không tăng số đã bắt. Lỗi schema hợp lệ có thể từ chối ngay; lỗi nội bộ không phải bằng chứng phát hiện đúng lỗi của mutant.

## C. Đầu vào thiếu hoặc sai vẫn đóng Đạt trong mô hình

Ca thường là đối chứng PASS. Giữ nguyên mọi dữ kiện khác, lần lượt đặt `g2=None`, `g2='DU'`, `g5=None`, `g5='chưa biết'`; cả bốn vẫn tới `Kết thúc·Đạt`, B1–B11 không báo. Các bộ phân loại mặc định `đủ ← True` chưa có cổng kiểm kiểu/miền/bắt buộc. Trường hợp `g5='chưa biết'` còn cần Host chốt cách gộp Unknown từ các câu hỏi vào g5; không tự giả định miền đã có.

**Sửa:** thiếu/sai/ngoài miền phải bị từ chối hoặc đi nhánh rõ trước phân loại. Chỉ mặc định đủ sau khi xác nhận dữ liệu đầu vào hợp lệ. PG có thể thực hiện NOT NULL/CHECK/enum, nhưng phải chỉ ra schema thực và test; bộ này không thử schema PG. Kết quả mô hình chưa bao trùm việc tính đủ 43 câu từ dữ liệu gốc: g1/g2/g5 vẫn là kết quả gộp được đưa vào.

## D. Việc tiếp theo cho Host

1. Sửa các đường gửi và thu hồi bù đã có phản ví dụ; thêm nghĩa vụ kiểm về hạn gửi, MB và PH. Dùng các trace trong `evidence/flow_results.json` làm ca hồi quy.
2. Sửa bộ tổng kết đột biến và phép kiểm đồng thời; đầu vào thiếu/sai phải có nhánh. Chạy lại probe nhỏ trước khi tăng phạm vi duyệt.
3. Sau đó mới tối ưu không gian trạng thái. Ghi rõ tập dữ liệu khởi tạo, biến thế giới được thay đổi, giới hạn Owner/đếm, số trạng thái đã duyệt và lý do kết thúc; không đồng nhất 17 kịch bản với mọi phối hợp dữ kiện.
4. H4.4b giữ riêng: thử khoá/UPDATE 0/biên nhận/thu hồi/thời gian/X6/khởi động lại bằng đúng công cụ PG/Flow. Không triển khai bằng kết quả mô hình.

## E. Công cụ và ghi danh

Master Công cụ ML-DEF-023 nhận hai mã ổn định: `python:kiem-ct000-4` và `python:ct000-audit`. V5 lưu nguyên phiên trong `../ct000-audit-v5/`; v6 ở thư mục này. README, nguồn/hash, lệnh, phạm vi, hạn chế và bằng chứng đi cùng công cụ. Ghi danh để dùng lại không phải nghiệm thu máy kiểm hoặc quy trình.
