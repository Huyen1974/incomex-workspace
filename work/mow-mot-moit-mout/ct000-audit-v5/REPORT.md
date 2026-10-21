# Rà soát CT-000, vòng 5 — Kết quả bằng công cụ

## Kết luận

**CHƯA ĐẠT để coi là quy trình thực thi đã khép kín.** Bảng hiện tại đạt các phép kiểm cấu trúc trên các nhãn đã khai báo. H7 chưa kiểm được đầy đủ cách tính nhãn từ dữ kiện và tác dụng của hành động. Một số chỗ nối giữa các bảng còn mâu thuẫn hoặc thiếu nhánh thực thi.

Phạm vi nguồn: `work/mow-mot-moit-mout/ban-duyet.html` và H7 trong `work/mbm-qtth-07-ve-ui-mow/COLLAB.md`, đọc tại head `4c93ecce01d8889dcc4e7558fc604a526fe2b010`. Các trích đoạn, metadata và hash nằm trong gói. Đây không phải thử nghiệm trên PG hoặc Directus của VPS.

## 1. Kết quả thực chạy

| Phép kiểm | Kết quả | Kết luận được phép rút ra |
|---|---:|---|
| Chạy nguyên H7 | 32 trạng thái, 92 dòng, 0 lỗi, 14/14 | Tái lập đúng số đếm Claude công bố. |
| Parser/đồ thị độc lập | 160 bộ đã khai, không thiếu/trùng, đích hợp lệ | Đúng cấu trúc trên miền nhãn đã kê. |
| Đường thành công và huỷ có đối soát | Đến đúng kết thúc | Hai đường này có tuyến hợp lệ; chưa kiểm hành động thật. |
| Đột biến cố ý làm hỏng an toàn | 11/11 vẫn được H7 chấp nhận | H7 không đủ sức phát hiện các thay đổi này. |
| Đối chứng gây lỗi cấu trúc | 3/3 có báo lỗi, nhưng cả 3 exit 0 | Chương trình gọi H7 có thể coi lần kiểm trượt là thành công. |
| Độ phủ 14 ca gốc | 35/92 mã T; 36/160 bộ mở rộng | 22,5% bộ mở rộng được 14 ca đi qua; không phải tỷ lệ thiết kế đúng. |
| PG/Directus/hiệu ứng bên ngoài | Chưa chạy | Không có bằng chứng triển khai chạy đúng. |

Chi tiết: `evidence/mutations/results.json`, `evidence/mutations/run_probes.json`, `evidence/independent_results.json`, `evidence/semantic_report.json`.

### Vì sao H7 cho qua lỗi?

H7 đọc Bảng Trạng thái và Bảng Chuyển trạng thái nhưng không đọc Bảng Giá trị. Hàm `run()` phần lớn nhận sẵn nhãn như `được`, `Chưa biết`, `có dở`; tác dụng dữ liệu được mô phỏng chỉ là tăng số lần nhận nếu gặp đúng chuỗi `lần nhận +1`. Nó chưa thực hiện điều kiện thời gian, quyền giữ, thế hệ, ghi biên nhận, gửi hoặc bù.

Ví dụ đột biến trong **bản sao**:

| Thay đổi cố ý | Kết quả H7 |
|---|---|
| Xoá toàn bộ Bảng Giá trị | 0 lỗi, 14/14 |
| T24: gửi lại ngay, đổi mã, bỏ đối soát | 0 lỗi, 14/14 |
| T13: bỏ khoá phạm vi và giữ chỗ | 0 lỗi, 14/14 |
| T70: bỏ bằng chứng, không ghi CAT-238* | 0 lỗi, 14/14 |
| T17: “gia hạn vô hạn; không có trần” | 0 lỗi, 14/14 |

Ở ví dụ cuối, H7 tìm từ `trần`, kể cả trong câu phủ định. Đối chứng chỉ ghi “gia hạn vô hạn” thì nó báo lỗi. Không được dùng một từ khoá thay cho phép kiểm giới hạn thực tế.

Các hành động sai trong bảng trên **không phải nội dung đang có trong bản gốc**. Đó là phép thử bộ kiểm. Toàn bộ diff và stdout từng ca đã được giữ lại.

## 2. Điểm gãy và khoảng trống trên bản gốc

### A. Giá trị sinh ra không có dòng nhận — IA-02

**Đường thử:** trạng thái `Chờ` → sự kiện `đến lúc kiểm` → Bảng Giá trị sinh `chưa quá` → tra bảng không có dòng. T16 chỉ nhận `chưa`.

**Đã kiểm:** lookup thực trả `NO_TABLE_ROW`.

**Sửa:** một mã duy nhất phải xuất hiện ở bộ tính giá trị, miền trạng thái và T16. Test nhập giờ hiện tại/hạn thực, để bộ phân loại tự sinh giá trị; không tự đưa nhãn `chưa` vào để làm ca đạt.

### B. “Còn lại” đứng trước các nhánh lỗi cụ thể — IA-01

**Đường thử:** nhận `ABORTED`; áp cách xét First đã ghi. Sau nhánh lỗi tạm an toàn là `Lỗi tạm không an toàn: còn lại`; nhánh này bắt trước `Xung đột: ABORTED`. Kết quả theo nghĩa đen là **T24 → Đối soát**, trong khi nhánh ABORTED phía sau yêu cầu **T25 → G2**. PERMISSION_DENIED tương tự bị T24 nhận thay vì T26.

**Đã kiểm:** sáu mã lỗi được đưa vào bộ phân loại tối thiểu diễn dịch đúng thứ tự câu chữ; bốn mã dẫn khác đường, hai mã khác phân loại nhưng hiện cùng đích.

**Sửa:** viết rõ `còn lại trong nhóm lỗi tạm`, hoặc đặt fallback toàn cục ở cuối. Định nghĩa cách sinh cả `Đạt` và `Một phần`. Nếu tác giả định hiểu “còn lại” chỉ trong một nhóm, phạm vi nhóm ấy phải thành điều kiện cụ thể mà máy đọc được.

### C. Đối soát thường cần hạn chưa được khởi tạo — S1

**Đường thử:** T13 → T27 (`Chưa biết`) → `Đối soát·TT` → T65 → `Chờ người·ĐS·TT`. Việc gốc còn hạn, chưa huỷ. Trạng thái chờ yêu cầu hạn chờ không quá hạn phục hồi (PH), nhưng định nghĩa chỉ tính PH khi vào `Quá hạn` hoặc `Xét huỷ`. Đường này chưa đi qua cả hai.

**Đã kiểm:** đường đi và chỗ khai báo khởi tạo không khớp. Đây là thiếu thao tác khởi tạo trong đặc tả, không phải lỗi PG đã chạy.

**Sửa:** xác định đúng bước tính PH lần đầu khi bắt đầu đối soát, gồm nhánh TT; ghi nơi lưu và không đặt lại qua vòng chờ. Chốt quan hệ PH với hạn gốc ở nhánh thường.

### D. T75/T83 cho phép chờ phục hồi tiếp mà chưa có nhánh hết hạn — IA-04

**Đường thử:** `Đối soát·Huỷ` → T67 → `Chờ người·ĐS·Huỷ` → T71 khi hết PH → `Chờ ĐK·ĐS·Huỷ` → T75 `còn chờ` → T75 → …

Bốn trạng thái `Chờ ĐK·ĐS·TT/Huỷ/QH` và `Chờ ĐK·Bù` chỉ nhận `thoả/còn chờ`. Không có nhánh hết PH hoặc nguồn không thể thoả. H7 loại mọi trạng thái loại `chờ` ra khỏi phép kiểm vòng, dù Flow vẫn phát lần kiểm tự động.

**Đã kiểm:** có đường tự lặp tuỳ ý trong bảng đang được kiểm. Điều này bác bỏ tuyên bố riêng bảng đã chứng minh mọi vòng có giới hạn; chưa chứng minh hệ thống thật chắc chắn treo nếu có quy trình con bên ngoài đưa việc lên Owner.

**Sửa:** thêm nhánh hết PH/không thể thoả, hoặc nối rõ quy trình sự cố con vào phép kiểm và chứng minh sự cố con hết hạn sẽ đưa việc cha đến quyết định cụ thể. Việc “có X1 ở đâu đó” chưa đủ.

### E. Chính thao tác bù mất phản hồi chưa có đường xử lý — S2

**Đường thử:** T90 huỷ → T77 đã có tác động → `Bù`; lệnh bù được gửi, bên ngoài có thể đã làm, nhưng mất phản hồi. Trạng thái Bù chỉ nhận `xong/lỗi/không bù được`. Không có kết quả chưa biết, thu hồi máy bù chết hoặc xử lý hết PH tại đây.

Ép thành `lỗi` sẽ dẫn T80 → T82 → Bù, chưa có quyết định an toàn bắt buộc trước khi thực hiện bù lần nữa. Bù còn được đánh dấu `tạm`, trong khi phần định nghĩa tạm là máy chấm ngay trong cùng giao dịch; chưa chỉ rõ bước nào nhận và chạy tác động bù bên ngoài giao dịch.

**Sửa:** dùng lại cơ chế nhận, giữ lượt, ghi kết quả và đối soát cho **mã thao tác bù**. Phản hồi mất phải đối soát việc bù, giữ mục đích huỷ, không tự quay lại làm. Test phải đặt điểm chết sau khi bù đã được bên ngoài thực hiện nhưng chưa ghi được kết quả.

### F. Giao lại khi bù lỗi mất đường trở lại bước bù — S3

**Đường thử:** T90 → T77 → Bù → T81 không bù được → Chờ Owner → T86 giao lại → Chấm G2 → T09 Chờ. Không có quyết định rút huỷ.

Theo bộ lọc X2, việc còn cờ huỷ không được nhận; theo bộ phân loại nhận trong bảng, chỉ xét M/hạn/sức chứa thì thiếu điều kiện giữ mục đích bù. Hai cách triển khai có thể cho kết quả khác nhau.

**Đã kiểm:** đích trong bảng và sự bất nhất với bộ lọc; không khẳng định hệ thống thật đã chạy lại việc gốc.

**Sửa:** T85/T86 giữ bước trở lại và mục đích xử lý. Giao lại lúc bù là giao người khác làm bước bù đang dở. Rút yêu cầu huỷ, nếu được phép, phải là quyết định riêng có ghi nhận.

### G. Miễn G1 hợp lệ vẫn bị nhánh “không Đúng” chặn — S4

**Đường thử:** mọi câu G1 Đúng, riêng G1.5 được miễn đúng phạm vi/hiệu lực → T87 → G1. Điều kiện đầu `G1.1–G1.8 có câu không Đúng` nhận `Được miễn` → T02 → chờ người.

**Đã kiểm:** áp chính predicate đã viết vào dữ kiện. Nếu có bước chuẩn hoá “miễn hợp lệ cũng đạt”, bước ấy chưa nằm trong phép tính hiện tại.

**Sửa:** tính đạt hiệu lực một lần bằng `Đúng hoặc miễn hợp lệ`, rồi mọi nhánh thiếu/sai/chưa biết dùng cùng kết quả đó. Test cả miễn đúng câu, sai câu, hết hiệu lực và còn câu khác chưa đạt.

### H. Thử lại cùng mã nhưng quy tắc ghi ý định chưa có nhánh dùng lại — S5

**Đường thử:** ý định mã thao tác K đã ghi ở thế hệ 1 → lỗi tạm an toàn → T23 → T13 nhận thế hệ 2, giữ mã K. G3 yêu cầu ghi ý định đúng thế hệ trước tác động; PG2/CAT-238 chỉ cho một ý định cho mỗi mã, trùng thì DO NOTHING. Lần ghi mới không thêm dòng.

**Đã kiểm:** mô phỏng ràng buộc tập hợp một ý định/mã cho kết quả thêm 1 rồi 0. Đây là mâu thuẫn/chỗ chưa định nghĩa giữa thử lại và điều kiện ghi; không phải test SQL thật. Một ý định đã tồn tại hợp lệ có thể được dùng lại, nhưng nguồn phải định nghĩa việc xác nhận ấy.

**Sửa:** thêm kết quả thao tác `đã tồn tại và khớp hợp lệ`: kiểm cùng nội dung, quyền giữ/thế hệ hiện tại, an toàn thử lại; ghi biên nhận lượt mới; dùng lại ý định cũ và giữ mã thao tác. Nội dung khác dưới cùng mã phải bị từ chối, có nơi ghi nhận và đường xử lý.

## 3. Không để phần mô tả còn quyết định đường đi

Host cần thay những câu như `gọi X3`, `ghi biên nhận`, `có trần` bằng tham chiếu đến thao tác và phép kiểm có thể chạy. Mỗi thao tác tối thiểu phải chỉ ra:

| Cần chỉ ra | Bằng chứng kiểm được |
|---|---|
| Đọc ở đâu | Tên bảng/trường/khoá hoặc API; kết quả 0, 1, nhiều dòng đi đâu. |
| Bằng gì | Tên hàm SQL/Flow/công cụ thực, đầu vào và quyền gọi. Chưa có công cụ thì chưa đạt. |
| Ghi vào đâu | Bản ghi thay đổi, điều kiện phiên/thế hệ, ghi biên nhận cùng hay khác giao dịch. |
| Đạt khi nào | Dữ liệu hoặc tác động quan sát được; không chỉ tên trạng thái cuối. |
| Thiếu/sai/chưa biết | Mỗi kết quả thao tác có mã và đường đi; không nén mọi lỗi thành một chữ `lỗi`. |
| Tắc thì ai làm tiếp | Việc đang chờ ai, chờ gì, lúc kiểm tiếp, hạn, đường hết hạn và sự kiện đánh thức. |

Hàm PG chỉ kiểm `(trạng thái,sự kiện,giá trị,đích)` tồn tại chưa chứng minh giá trị do caller gửi là đúng. Phải kiểm quyền và dữ kiện tại thao tác thực thi; chứng minh các ghi bắt buộc xảy ra hoặc cùng bị huỷ khi lỗi.

Điểm cần nối thêm nhưng **chưa tính là lỗi thực thi đã chứng minh**: không ô hành động nào trong 92 dòng gọi rõ X6. X6 đã có ở phần mô tả; cần chỉ ra tác vụ sửa sự cố hoàn thành sẽ gọi X6 ở đâu, đánh giá riêng từng việc gốc và đánh thức chúng thế nào. Test một sự cố chặn hai việc có hạn khác nhau.

## 4. Phép thử PG/Flow còn bắt buộc

Không dùng kết quả trên để ghi H4.4b đã hoàn thành. Khi Host ghép công cụ thật, lưu ít nhất tên phiên PG/Directus, câu lệnh/Flow thực dùng, dữ liệu trước–sau, số dòng tác động, biên nhận và mã thoát cho các ca:

1. Hai bên nhận cùng việc; sức chứa còn một chỗ; chỉ đúng người giữ được tiếp tục.
2. UPDATE trả 0 dòng do thế hệ/trạng thái đã đổi: không ghi thành công giả; có kết quả rõ cho caller.
3. Kết quả chạy đua với huỷ/thu hồi; quyền ghi trạng thái và bằng chứng đến muộn được xử lý đúng.
4. Ý định đã tồn tại: cùng nội dung dùng lại đúng; khác nội dung bị từ chối.
5. Tác động thường và tác động bù mất phản hồi: không gửi mù, có đối soát đúng mã và hạn.
6. Khởi động lại PG/Flow khi đang chờ hoặc đang giữ: việc còn trên sổ, có người/công cụ nhận tiếp theo quy tắc đã chốt.
7. Một sự cố sửa xong: từng việc gốc được chấm lại và đánh thức; việc hết hạn không tự chạy nghiệp vụ lại.

Các ca này là nghĩa vụ kiểm còn lại, không phải kết quả đã chạy. Không có môi trường PG trong lần rà này.

## 5. Quy tắc sử dụng kết quả

- 11 đột biến là phép thử H7, không cộng thành 11 lỗi của bản gốc.
- IA-01 áp nghĩa First theo chữ đã viết; nếu muốn nghĩa khác, phải định nghĩa phạm vi cụ thể và kiểm được.
- IA-04 là phản ví dụ của bảng/đồ thị, không suy diễn thành sự cố vận hành đã xảy ra.
- Các mục NOT_PROVEN giữ nguyên là chưa chứng minh. Không biến đầu vào bị từ chối theo chủ ý thành lỗi.
- Bộ kiểm ngữ nghĩa tự chặn khi nguồn đã đổi ngoài phạm vi hỗ trợ. Không thể dùng nó để chứng nhận mọi sửa đổi lời văn tự động.
- Công cụ không bảo đảm “không còn bất kỳ lỗi nào”. Nó đưa ra ca phản ví dụ có thể chạy lại và cổng từ chối rõ ràng khi còn lỗi hoặc chưa kiểm được.
