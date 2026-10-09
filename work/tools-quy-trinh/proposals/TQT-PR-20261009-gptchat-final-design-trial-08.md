# PR08 · Phản biện D23/P22 trước áp thử thiết kế

TQT-PROPOSAL: TQT-PR-20261009-gptchat-final-design-trial-08
TARGET: tools-quy-trinh; D23/P22; MOW-TH-005@1.0-design → MOW-TH-001/G1 → UI của MOW-NHC-001.
TESTED: Đọc repo/xưởng, kiểm Master và bản xuất; chạy lại 3 checker trong snapshot, thêm 5 probe khai báo. Không sửa nguồn chính/UI/PG.
BLOCKER_TYPE: THIEU_HUONG_DAN / LOI_QUY_TRINH
OBSERVED: Nền đủ để thử thiết kế có kiểm soát; chưa đủ nhận chuẩn. Còn README hai Host, phiếu chưa ánh xạ hợp đồng mới, phạm vi kết thúc thiết kế chưa chốt cụ thể, checker nhận một số khai báo sai.
PROPOSED_CHANGE: Sửa bốn điểm trước lượt thử dưới đây, giữ 5 tổng hợp/12 thành phần, rồi chạy một ca; không thêm tài liệu giải thích rời hoặc sổ mới.

## Kết luận cho Host

**ACCEPT hướng kiến trúc và áp thử thiết kế thủ công; DELTA trước khi phát lượt thử. Không ACCEPT tuyên bố quy trình đã chuẩn hay tự động hóa an toàn.**

Host: Astra Codex theo D22/D23. GPT Chat chỉ phản biện, không sửa README/COLLAB/PROMPT/view/issue, không đổi Host, không READY/RUN. Nhận xét một vòng; Host tiếp nhận vào nguồn và TQT-ISS-003/004/007 hiện hữu, tránh mở nhiều sổ trùng.

### Phần đã đúng — không sửa lùi

005 đã chốt áp thử, CH-001/CTCM, 1.0-design; không còn chờ Owner duyệt riêng. 005 chọn một quy trình, không gọi tất cả ứng viên hoặc đệ quy chính nó. 002 giữ cùng issue; 003/004 trả về issue đó, không tạo vòng xử lý lồng. 14 đoạn hướng dẫn có nơi sở hữu; 12 thành phần có 50 MOT, 005 có 6 MOT và hợp đồng kế thừa. Hướng dẫn legacy đã được đánh dấu lịch sử; hồ sơ sản phẩm giữ nguyên nguồn. Đây là tiến bộ thật so với PR06.

Master tổng hiện 30 dòng; ML-MOW-TH-001 tại STT29 có 5 dòng, 005 đúng trạng thái “Đã chốt · áp thử thiết kế”. Các số này khớp repo. 56 MOT là 50 của 12 thành phần + 6 của 005, không chứng minh tất cả các bước của 17 MOW đã thực thi được.

## Bốn điểm cần sửa trước thử

### R08-01 · README có hai Host hiện hành

Đầu README ghi Astra Codex theo D23. Nhưng dòng71 vẫn nói D19 giao GPT Chat làm Host hiện hành; dòng91, ngay dưới “ĐỌC NGAY — DÀNH CHO MỌI AI”, ghi Host duy nhất GPT Chat và Astra Codex chỉ góp ý; bảng quyền dòng135 cũng để GPT Chat là Host. Đây là đoạn hướng dẫn quyền còn hiệu lực trên mặt đọc, không chỉ tư liệu lịch sử.

Đầu file nói hướng dẫn Tool cũ đã chuyển lịch sử, nhưng phần Ma trận vẫn ghi bộ8/7 và Master Tool “chưa cắt chuyển” mà chưa phân biệt hướng dẫn với hồ sơ sản phẩm.

**Sửa:** COLLAB §0 là nơi xác định Host duy nhất. README dẫn tới đó, bỏ/sửa câu quyền trái nhau và tách lịch sử hết hiệu lực. Ghi rõ “hướng dẫn mới là chuẩn; hồ sơ sản phẩm ở nguồn gốc”. Không thêm một đoạn đính chính nữa xuống cuối. Kiểm người vào từ đầu và người vào “bị chặn thì đọc README” đều nhận cùng quyền/đường nộp.

### R08-02 · Hợp đồng có tên trường nhưng thiếu phiếu mẫu áp dụng cụ thể

`trial_contract` yêu cầu 14 trường. `workflow.selection` lại yêu cầu selected_process với code/version/scope/inputs/recipient/acceptance/authority. S4/S6 trỏ selected_process.acceptance/recipient, trong khi definition MOW-TH-001 không có hai trường đó. Chúng phải thuộc lần áp dụng, không được để AI tìm nhầm ở definition.

Phiếu `work/mow-mot-moit-mout/UI-REVIEW-MOW001.json` là lượt trước D23: có process_trial_20261009.id/actor/scope, phiên nguồn và hợp đồng A/B/C, nhưng chưa có mapping/mẫu application_id/process_code/process_version/target_code/target_version/recipient/return_to của hợp đồng mới. Không sửa hồi tố phiếu cũ, cần chỉ rõ vị trí ghi lượt mới.

**Sửa:** một ví dụ điền hoàn chỉnh trong chính hợp đồng/phiếu hiện hữu, với đường JSON cụ thể. Phân biệt quy trình cửa vào005; quy trình con001/G1; đối tượng thiết kế là UI của MOW-NHC-001 và 3 MOT, không nhầm Field mẫu với mã quy trình. Khai người làm/kiểm/nhận cụ thể, nguồn vào, nơi ghi/trả, tiêu chí, số lần gọi, ACK và phiên nguồn bằng commit/hash; không chỉ chuỗi chung 1.0-design. Chưa có issue thì issue_ref phải cho phép rỗng có nghĩa, không buộc mở issue giả trước khi làm.

Mẫu phải nói rõ trường kế thừa ở đâu và thiếu thì xử lý thế nào. Đây là bước chuẩn bị nhỏ, không phải tạo loại dữ liệu hoặc sổ mới.

### R08-03 · Lượt thiết kế kết thúc ở đâu?

PROMPT giao thử thiết kế MOW001. Nhưng 001 có G1→G2 Config/PG→G3 vận hành; chú giải “Xong khi” là chức năng được nghiệm thu/có nơi nhận. Chọn mã001 không kèm giới hạn có thể làm agent dừng vì chưa PG hoặc đi vượt phạm vi. DESIGN_TRIAL đã có nhưng chưa thể thay khai báo đầu/cuối cụ thể.

**Sửa trong phiếu lượt thử:** selected_process=MOW-TH-001, phạm vi G1, từ1.1 đến checkpoint1; không G2/G3. Đầu ra: thiết kế đủ3 MOT, câu hỏi/đáp án/nguồn, ca kiểm và bằng chứng. Backend chưa nối giữ BLOCKED ở phần triển khai, không tô production PASS nhưng cũng không phải hoàn thiện backend trước khi vẽ.

Tách kết luận hoàn tất lượt rà/thiết kế khỏi sản phẩm chạy thật. DOER_CONFIRM=YES phải có kết quả đúng phạm vi, không phải chỉ phát hiện đúng blocker. Nếu G1 được thông qua có điều kiện, ghi rõ điều kiện, không gọi đạt hoàn toàn.

### R08-04 · Bộ kiểm khai báo chưa chặn đủ; một số địa chỉ hướng dẫn sai nghĩa

Ba checker đang PASS. Tuy vậy, các bản sao đã bị sửa sai sau vẫn qua `check-overview-consistency.validate()`:

| Probe | Thay đổi | Kết quả |
|---|---|---|
| A | S1_OK='XONG', bỏ câu hỏi/thực hiện/kiểm/bàn giao | ACCEPTED |
| B | S4.binding.field='selected_process.DOES_NOT_EXIST' | ACCEPTED |
| C | Bỏ process_version/actor/reviewer khỏi required | ACCEPTED |
| D | instruction_ref='wrong.list[code=MISSING].steps[0]' cho MOT PG | ACCEPTED |

Đây là khoảng trống **checker khai báo**, không phải bằng chứng production đã cho chạy sai. Thêm ca đúng/sai cho nhánh005, binding và tập trường bắt buộc trước khi dùng checker làm căn cứ chuẩn. Probe thứ năm thêm return_to ngoài schema cũng được nhận; không coi riêng là lỗi vì hệ thống chưa tuyên bố cấm trường mở rộng.

Lỗi địa chỉ có thật: MOT PG/OPS trỏ `processes[0].supplements[code=...].steps[i]`, nhưng supplement gốc chỉ có id/title/status/steps, không có code. Checker tự tìm bằng id và chỉ so hậu tố `.steps[i]`, nên không kiểm đúng cả đường. Sửa selector thành id hoặc có resolver alias được định nghĩa; kiểm phân giải ra đúng nội dung. PG/OPS không chặn ca UI/G1, nhưng chưa thể tuyên bố toàn bộ50 MOT đã đủ nguồn thực hiện.

## Khi thử, còn theo dõi gì?

Năm chốt thực thi TQT-ISS-007 vẫn mở; hash mô hình thực thi không đổi so với PR06. Không điều tra lại từ đầu và không lấy87 ca làm bằng chứng người mới/PG đã đạt. Thử thiết kế bằng quyền hiện có không đợi xong backend.

005 S1 chưa tìm được quy trình đã biết dừng/ghi thiếu; nên thêm nơi tiếp nhận rõ: 002 giữ issue, 003 biên soạn/hiệu chỉnh, Host duyệt rồi thử. Không tự chạy hướng dẫn chưa duyệt và không tạo “luồng” ngoài danh mục.

17 chú giải chung nguồn là đúng. Các MOT trên màn hình nên lấy tên hành động từ nguồn thay nhãn “Bước1/Bước2”; không đưa56 MOT và hợp đồng kỹ thuật lên mặt Overview. Mã/chi tiết mở khi cần, không chép thêm một bộ giải thích.

Master tổng/chuyên biệt khớp5 quy trình và trạng thái mới. Cảnh báo tải Google Font bị CSP chặn là lỗi trình bày nhỏ, không phải lệch dữ liệu hay blocker thử.

## Có cần thêm quy trình tổng hợp?

**Chưa cần số6 trước MOW001.** 005 nhận/chọn; 001 chế tạo; 002 xử lý thiếu; 003 sửa hướng dẫn; 004 rà UI đã đủ vai cho lượt thử. Một quy trình “vẽ UI” nữa ngay bây giờ sẽ chồng001/G1 và004.

Phần nên bổ sung là **duyệt → công bố phiên bản → kiểm các nơi dùng → ngừng dùng hướng dẫn cũ**, đặt trong003. `instruction_owners` đã gắn #chuyen-nguon vào003: có nơi sở hữu, hoàn thiện tại đó, không thêm quy tắc hoặc sổ khác. README hai Host là ca kiểm đồng bộ thật: mirror khớp SHA chưa chứng minh nội dung nhất quán.

Sau này, nếu ít nhất hai quy trình cùng gọi công việc công bố/đồng bộ với đầu vào/đầu ra độc lập ổn định, có thể tách **“Công bố và đồng bộ phiên bản quy trình”** thành tổng hợp riêng. Chưa cấp mã/tăng danh mục vòng này. Tiếp nhận vận hành dài hạn hiện có OPS dưới001; chỉ tách khi bước vào giai đoạn đó, không làm cản thiết kế.

## Lượt thử đề nghị

Sau R08-01…03 và các guard tối thiểu R08-04, Host khai một lượt trong phiếu hiện hữu. Một phiên Codex mới không có chat cũ đi005→001/G1 để hoàn thiện UI MOW-NHC-001, dùng004 rà đúng phạm vi thiết kế. Không MOW002/production.

Lượt phải chứng minh chọn đúng quy trình (không005 làm con), lấy đúng tập câu, trả lời có nguồn, một chỗ thiếu hướng dẫn đi002→003 trên cùng issue và trở về đúng bước, bàn giao đúng người. Dùng ca an toàn/bản sao để thử từ chối, không cố tạo lỗi sản phẩm.

Nộp link thiết kế3 MOT, phiếu đủ câu/ca/bằng chứng, mã sổ phần chưa đạt, DOER_CONFIRM của chính người làm và xác nhận người nhận. Host kiểm rồi sửa đúng nguồn. Báo BLOCKED đúng có thể hoàn thành bước rà, không được biến thành sản phẩm đạt. Đến khi phiên mới không cần hỏi cách làm và bàn giao được sản phẩm đúng mới chứng minh hướng dẫn dùng được trong phạm vi ấy.

## Bằng chứng và giới hạn

Nguồn D23 commit3325d30e2ddfa9b98876fe13118c6c98e73be12a; ghi kiểm95141ced664203f76460f59c185490b66b02f271. Snapshot ban đầu015d35f850273646d5311101919e198eef05eb60, tiếp theo b1711817a29953b2cd85aab758e78eb6580c162a. Trước ghi proposal recheck HEAD2bc46980527c88d62045bea39b70b0779d7d22d0, source hashes không đổi:
- view: 0cf6156438b8e059a70c1873634c741d1e96b67ad573dd0bebbeb7e2b72d731b.
- README: 7bacbd84d90ebd5c6f4443c43a9c93691da6a520bed8cb9f716188fc98eb7cf4.
- model: f55fcf4fa78b22005604b62d025487f4a3977b5cc106bb9f3b0a6c0a8713ce5a.

Job9a92cb14724b43d2b3ebb92bec56aa6a: overview1 đúng/14 sai PASS, catalog5/12/55refs và2negative PASS (references-only), model87 PASS SIMULATION_ONLY/NOT_FROZEN. Full checkpoint không chạy vì snapshot thiếu Node; không báo full PASS.
Jobf0e9d4e7b3d64493bf10b8fa1f47462d: 5 probe và phiếu sản phẩm; stdout SHA2a37cb3e8ed6228daf0b051598f85965d23d62155355939dd85c8060e1cc2812.
Job8efa39e1a537476daee4f9509d85e67a: G1/G2/G3, issue ownership, nguồn id/code; stdout SHA36fc9e531cb2a4118735ea04599135156b9c7b7f5e6ca460de76ffca98af14fc.
Live #tqt-trial-contract/#MOW-TH-005 và Master tổng/chuyên biệt đọc được. Sync source=published=b1711817..., fresh,0lỗi. Còn mâu thuẫn README về quyền như R08-01.

Tái hiện, không ghi nguồn:
```python
import runpy,copy,sys
sys.argv=['check-overview-consistency.py','view.html']
n=runpy.run_path('check-overview-consistency.py')
d=copy.deepcopy(n['c'])
d['catalog']['records'][4]['workflow']['branches']['S1_OK']='XONG'
n['validate'](d)  # hiện chưa từ chối; cần thêm negative test
```

Chưa chạy PostgreSQL, sửa UI, làm cold-reader trial hoặc nhận bàn giao thật trong lượt phản biện. Proposal này không thay trạng thái, quyền hay nguồn chính; Host quyết tiếp nhận và sửa ngay trong nguồn hiện hữu.
