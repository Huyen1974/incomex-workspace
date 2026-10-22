# CT-000 — phản biện vòng 7 bằng công cụ

Ngày: 22/10/2026. Ghế: GPT Reviewer. Host quy trình vẫn là Claude.

## Kết luận

**Đồng thuận hướng kiến trúc; chưa thông qua H4.4a, chưa mở triển khai PG/Flow.** Không yêu cầu thay kiến trúc hoặc xây framework mới. Giữ bảng chuyển trạng thái, PG làm tầng lưu trạng thái, Directus và hai công cụ đã đăng ký. Phải sửa các lỗi/thiếu hợp đồng dưới đây trước khi dùng kết quả kiểm để ký.

Đã chạy lại trên bản sao cách ly: kiểm tĩnh, cấu trúc, tranh chỗ và **29/29 ca cũ đạt**. Bộ phản biện mới tái hiện **9 phát hiện, gom thành 6 nhóm**. Đây là các phản ví dụ của mô hình, khoảng trống hợp đồng đầu vào và phép thử máy kiểm; không phải báo cáo 9 lỗi đã xảy ra trên production.

Nguồn được ghim:
- HTML: `5948c52fc293b666c550148b648fb3fc10a52d4e2ac303d19329d20bd3107a93`.
- Máy kiểm Claude: `dbcf08b725c679fa1c8b4205cd3f2a3cd30bff0038c8392578bb25640702bf6a`.
- Công cụ phản biện `review_v7.py`: `2d1459f4c67433845e8b4fd81deeeff4321fee1eca16aab10e5094c415175655`.
- Snapshot thực thi: commit `f34d15136e6cbe6630b0730d94a807f1453d904a`.
- Biên nhận thực thi: job `84da8b982ba54efba100414cff673ce7`, exit **1**, không timeout, stderr rỗng. Không chạy duyệt lớn, không truy cập PG/Flow.
- Bằng chứng nguyên trạng: `evidence/v7-results.json`, SHA256 `65ca792fa93a9de5253973542812f7ea294d159058deef487c412dd94dc364ea`.

## Sáu nhóm phải đóng

### 1. Kết quả và gia hạn của lượt cũ lọt vào lượt mới — V7-01, V7-02

Vết V7-01: nhận lượt thế hệ 1 → hết hạn, thu hồi → nhận lượt mới thế hệ 3 → lượt mới thực hiện tác động → lượt cũ gửi `FAILED_PRECONDITION`, mang `tác_nhân=1` → bảng vẫn chạy **T26**, chuyển lượt mới sang `Chờ ĐK·G2`, nhả chỗ của thế hệ 3. B1–B13 không báo lỗi.

Vết V7-02: sau khi nhận thế hệ 3, gửi `gia hạn` mang thế hệ 1 → bảng vẫn chạy **T17**, tăng bộ đếm gia hạn của lượt mới. Bất biến cũng không báo.

Cổng `làm thao tác` có kiểm thế hệ, nhưng công thức `kết quả` và `gia hạn` chưa có kiểm tương ứng. Đây là bất nhất với yêu cầu PG 5/X5 trên chính trang.

**Sửa và kiểm:** định danh sự kiện phải gắn đúng việc, lượt/thế hệ, thao tác và trạng thái cho phép. Kết quả cũ được lưu làm bằng chứng nhưng không đổi trạng thái/nhả chỗ lượt hiện hành. Gia hạn cũ bị từ chối, không thay hạn hoặc bộ đếm. Thêm cả ca cùng thế hệ được phép và khác thế hệ bị chặn; thử lại khi lên PG.

### 2. Phản hồi người chưa được kiểm nội dung — V7-03, V7-04, V7-05

- V7-03: G1 thiếu → `trả lời {}` → T42 gán `g1='đủ'` → qua G1.
- V7-04: chờ duyệt G4 → `trả lời {}` → T45 bỏ cờ chờ → T37/T41 → `Kết thúc·Đạt`.
- V7-05: chờ xác nhận bàn giao G5 → `trả lời {}` → T45 bỏ cờ chờ nhận → T41 → `Kết thúc·Đạt`.

Cả ba đường không bị B1–B13 bắt. Có thể thiết kế một lớp xác thực sự kiện bên ngoài, nhưng hiện mô hình không chạy lớp đó; không được lấy việc phát ra sự kiện `trả lời` làm bằng chứng nội dung đã đạt.

**Sửa và kiểm:** sự kiện có nội dung/định danh người/phạm vi/phiên bản. Phân biệt thiếu, sai, từ chối, chưa biết và đồng ý hợp lệ. G1 phải tính lại từ dữ kiện, G4 phải có quyết định hợp lệ, G5 phải có xác nhận nhận đúng hồ sơ. Ca trả lời rỗng/sai người/sai phiên không được mở cổng; ca đúng phải đi tiếp. Liên kết việc tính các giá trị gộp với 43 câu, không chỉ mặc định chúng đã được chấm đúng.

### 3. Miền mã kết quả ngoài chưa khép kín — V7-06

Đưa lần lượt `CANCELLED`, `NOT_FOUND`, `ALREADY_EXISTS`, `OUT_OF_RANGE`, `UNIMPLEMENTED`, `INTERNAL`, `DATA_LOSS`, `UNAUTHENTICATED` vào sự kiện kết quả. Cả 8 trả `L1 công thức không ra giá trị`, thay vì có đường xử lý đã định. Đây đều là mã trong danh sách gRPC chính thức [1].

**Sửa và kiểm:** thêm/buộc chạy bộ chuẩn hóa mã ngoài vào miền đóng, có nhánh cho mã lạ và dữ liệu thiếu. Mỗi mã ngoài phải có đúng một kết quả chuẩn hóa và đường tiếp theo. Không gom mọi lỗi thành thử lại; kết quả chưa rõ tác động phải đối soát. Thiếu lớp chuẩn hóa hoặc không kiểm được lớp đó thì không được ký phạm vi đầu-cuối.

### 4. Lỗi máy kiểm vẫn có thể bị tính là bắt đột biến — V7-07

Thử **giữ nguyên mô hình**, chỉ gây `RuntimeError('V7_INJECTED_CHECKER_FAILURE')` khi bộ tính bất biến B1 chạy trong lượt đột biến. Chạy chính `main()` của máy kiểm: `vi_pham()` bắt exception rồi biến thành một lỗi bất biến; bộ phân loại ghi **KILLED** cho mô hình không hề bị sửa.

Lượt thử dùng `--kb -` để giới hạn tài nguyên, vì vậy exit chung vẫn là **2**, không phải 0. Phát hiện ở đây là phân loại KILLED sai, không phải tuyên bố máy đã báo PASS toàn phần.

**Sửa và kiểm:** tách lỗi tính/checker error khỏi predicate trả False. Đột biến không được tính KILLED chỉ vì máy kiểm lỗi. Thêm tự kiểm: mô hình nguyên + checker lỗi phải ra CHECKER_ERROR; mô hình hỏng thật + vết vi phạm hợp lệ mới KILLED. Phân biệt đột biến tương đương/vô nghĩa với bỏ lọt lỗi; không sửa nghĩa luật chỉ để đạt điểm đột biến.

### 5. Phép kiểm tính sống đang yếu hơn tên gọi — V7-08

Cho hàm `song()` đồ thị nhỏ: trạng thái tạm `Chấm G2` có cạnh máy tự quay về chính nó và một cạnh đi kết thúc. Hàm trả **không lỗi**, vì loại mọi cạnh `u == v` trước khi kiểm vòng và dùng phép tìm đường ngược để xác nhận có đường ra.

Đây là phép thử thuộc tính của máy kiểm, **không phải vết chứng minh bản workflow hiện tại đã kẹt**. Tuy nhiên, có một đường ra không đồng nghĩa mọi lần thực thi hợp lệ cuối cùng đều đi ra. Điều kiện bộ lập lịch tiếp tục cho các hành động được phép chạy (fairness) phải được khai rõ khi kiểm tính sống [2].

**Sửa và kiểm:** phân biệt lặp chờ hợp lệ với lặp xử lý tức thời không tiến triển; kiểm theo giả định thời gian/bộ quét đã khai. Không cấm mọi vòng tự lặp, cũng không bỏ mọi vòng tự lặp. Chứng minh hoặc giới hạn lại phát biểu L2–L4 đúng bằng điều máy kiểm thực sự kiểm.

### 6. Kiểm kê có thể nhận nhầm lịch sử là đăng ký thật — V7-09

Tạo fixture trong thư mục tạm: `catalog.tool_registry.provider_tools=[]`, `memory=[]`; chỉ đặt chuỗi `id/path/sha256/tool_id` hợp lệ trong `archive`. Hàm `kiem_ke()` vẫn trả danh sách lỗi rỗng và báo hai công cụ đủ. Nguyên nhân là tìm chuỗi trên toàn HTML thay vì đọc đúng bản ghi JSON đang hoạt động.

**Sửa và kiểm:** parse đúng script `tqt-composite-processes` → `catalog.tool_registry`; kiểm ID duy nhất, đường dẫn đầy đủ, tệp thật, hash, manifest và memory đúng ID. Tên có trong lịch sử hoặc tệp trùng tên ở thư mục khác không được tính. Phạm vi “hai công cụ CT-000” khác với “toàn bộ script của việc”; các script ngoài Master không thể chỉ cảnh báo rồi dùng exit 0 làm bằng chứng kiểm kê toàn bộ.

## Phần đã kiểm kê thật trước cập nhật đăng ký

Đọc JSON thực thay vì chỉ tìm chuỗi: 28 mục `provider_tools`, không trùng ID. Hai công cụ CT-000 mỗi công cụ đúng một mục, đường dẫn và hash khớp; manifest bộ GPT có **20/20 tệp khớp**, không lệch. Con số 37 trên giao diện do báo cáo trước nêu gồm cả 9 phương pháp; 28 mục provider không phủ định con số giao diện đó.

Sáu script chưa nằm trong provider registry tại thời điểm đo: `cong-cu/dot-walk-check.py`, `dot-edit-simulate.py`, `dot-push-verify.py`, `dot-page-shot.py`, `dot-process-gate.py`, và `check-ui-review.py`. Đăng ký bổ sung chỉ là ghi danh artifact để tìm lại; không chứng nhận chức năng, không đưa vào bộ chạy tự động của Master DOT.

## Khoảng trống cần gắn vào điều kiện thông qua, không gọi là lỗi production đã tái hiện

1. **Phạm vi mô hình:** 43 câu chưa được tính đầy đủ từ đầu vào thật; giới hạn D/đồ thị phụ thuộc/nhiều gốc chung một sự cố và nhiều thao tác ngoài không được chứng minh chỉ bằng một biến kết quả gộp. Phải chỉ rõ phần được mô hình hóa, phần giả định và ca kiểm từng phần. 21 cấu hình không tự động bằng mọi tổ hợp của các biến.
2. **X1 và mất sự cố:** yêu cầu PG 15 ghi cờ bằng lệnh riêng sau khi X1 rollback còn cửa sổ tiến trình chết trước khi cờ được ghi. Thiết kế phải có dấu tiếp nhận bền vững trước bước có thể mất hoặc cơ chế quét tái dựng được; thử crash đúng tại ranh giới rollback/ghi cờ. Không chỉ thêm câu “máy sẽ quét”.
3. **Ý định và gửi ngoài:** mô hình gộp “ghi ý định rồi gửi” thành một bước; PG commit và gửi mạng không phải một giao dịch chung. Cần ca chết sau commit/trước gửi, sau gửi/trước ghi kết quả; phiên cũ tỉnh lại sau kiểm quyền; từng mã thao tác/bù và thời hạn chống trùng. Outbox có thể phát lại thông điệp; không tự đảm bảo gửi đúng một lần [3].
4. **H4.4a/H4.4b:** báo cáo Claude mới có 13/21 kịch bản duyệt hết, 8 còn lại và đột biến chưa xong. Lượt GPT này không chạy lại duyệt lớn để tránh tiêu tốn tài nguyên; không nâng số đạt đó. PG/Flow thật chưa được kiểm: nhận việc đồng thời, thu hồi/gia hạn đua nhau, biên nhận đến muộn, rollback/X1, khởi động lại bộ quét. Có tên “khóa phạm vi” trong mô hình chưa thay bằng chứng giao dịch PG thật [4].

## Việc tiếp theo cho Claude Host

Giữ nguyên kiến trúc. Xử lý 6 nhóm trên trong chính bảng/công cụ hiện có; thêm ca cấm và ca được phép tương ứng, kết quả chạy tách theo mã V7. Chốt phạm vi và giả định trước khi duyệt hết đồ thị; không tăng trần bộ nhớ hoặc chạy nhiều lượt nặng trên VPS để thay việc sửa mô hình. Khi nguồn đổi, GPT cập nhật probe theo nghĩa rồi ghim nguồn mới; không chỉ thay hash cho xanh. Sau kiểm mô hình và kiểm chéo mới mở H4.4b bằng lượt riêng được duyệt. Không có READY/RUN triển khai trong phản biện này.

Tái chạy:
```bash
python3 work/mow-mot-moit-mout/audit-ct000/run.py --v7 --out /tmp/ct000-audit-v7-results
```
Nguồn ghim hiện tại phải trả **exit 1 / FINDINGS_REMAIN**. Exit 0 chỉ có nghĩa các probe trong phạm vi đạt; không thay kiểm đầy đủ hoặc phê duyệt của Owner.

## Nguồn đối chiếu kỹ thuật

[1] gRPC, Status Codes: https://grpc.io/docs/guides/status-codes/

[2] Leslie Lamport, PlusCal Tutorial — Session 9, Liveness: https://lamport.azurewebsites.net/tla/tutorial/session9.html

[3] AWS Prescriptive Guidance, Transactional outbox pattern: https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html

[4] PostgreSQL 18, Explicit Locking: https://www.postgresql.org/docs/18/explicit-locking.html
