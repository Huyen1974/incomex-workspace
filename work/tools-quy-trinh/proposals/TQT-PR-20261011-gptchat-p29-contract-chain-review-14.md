# PR14 — Phản biện P29: hợp đồng phải khớp dữ liệu được giao, không chỉ có đủ ô khai

TQT-PROPOSAL: TQT-PR-20261011-gptchat-p29-contract-chain-review-14
TARGET: MOW-TH-005 / CAT-206* / application_D24 MOW001-G1; kiểm liên tục CP01–CP07.
ROLE: GPT Chat — Reviewer theo lời Owner; không thay Host nội dung Astra Codex hoặc Host Kiểm soát Claude.
DECISION: REQUEST_CHANGES trước khi nhận CP03/cho thực hiện lượt thật. Giữ ⑤, 7 mốc, các Master hiện hữu; không thêm quy trình/master.
SCOPE: Chỉ đọc nguồn và thử trong snapshot; không sửa view/README/PROMPT/COLLAB/phiếu sản phẩm/PG/VPS runtime. File này là đề xuất duy nhất.

## 1. Kết luận cho Host

Đã chạy lại đầy đủ các suite đăng ký bằng mã nguyên bản, gồm 44 ca hợp đồng mới; runner PASS. Đồng thời chạy 28 probe độc lập + 2 probe bổ sung và đối chiếu bộ dữ liệu mẫu được chính checker coi là đi hết 7 mốc.

**Điểm gãy điển hình:** hợp đồng giao P01–P05 bắt đầu ra có `scope`; bộ mẫu thành công của chính checker thiếu `scope` ở cả 5 kết quả nhưng vẫn `canFinish=true`, 7/7 mốc. Bước sau yêu cầu trường mà bước trước chưa xuất; hiện kiểm chưa đối chiếu payload thật với `handoffs.output_fields`.

Không được hiểu mọi probe là đã vượt CP03: nhóm sửa hợp đồng chỉ đo `contract.ready` (hợp đồng khai có được coi hợp lệ không), chưa cấp lại review/pin/checkpoint. Thay hợp đồng làm mất hiệu lực CP02 trở đi đang hoạt động đúng. Các điểm dưới là phần cần bù trước lúc tin rằng khai đủ và ghim phiên bảo đảm thực hiện đúng.

## 2. Các chỗ cần sửa, theo đường đi của thông tin

| Mã | Phát hiện và ảnh hưởng | Chốt sửa/kiểm lại |
|---|---|---|
| R14-01 | Bộ mẫu PASS 7/7 thiếu `scope` trong cả P01–P05, trái chính `handoffs.output_fields`; đầu vào P02–P05 lại cần `scope`. | Kiểm đầu ra thực theo schema của đúng giao điểm, rồi kiểm nó đáp ứng đầu vào bước sau. Nếu thừa kế phạm vi từ hồ sơ cha thì khai phép ghép rõ ràng, không để AI tự suy. Ca thiếu scope phải bị chặn trước khi bước nhận sử dụng. |
| R14-02 | Bỏ toàn bộ 45 dòng PRODUCT_SPEC, còn 6 dòng DESIGN_TASK, `contract.ready=true`; xóa 3 trường requestId hoặc cả `product_interfaces` cũng không báo thiếu. | Đối chiếu tập trường/nhánh bắt buộc được dẫn từ nguồn luật và phạm vi MOT đã chốt, không chỉ kiểm các dòng đang tồn tại. Không hardcode phải đủ 51: kiểm thiếu đúng trường/đầu nối/nhánh bắt buộc theo phiên. |
| R14-03 | Tên kiểu không tồn tại, đường nguồn không tồn tại, cột đích không có, target_code/process_code/mot_version/rule_version sai trong từng dòng vẫn `contract.ready=true`. Đổi nơi nhận/đầu vào của handoff sang việc khác cũng được nhận. | Kiểu/đơn vị/cardinality/null phải có ngữ nghĩa kiểm được; phân giải schema logic và mapping nguồn–đích; ràng buộc từng dòng về đúng MOW/MOT/phiên/luật. Không cần PG lúc thiết kế, nhưng phải có hợp đồng cấu trúc đọc được và xác định trường, không chỉ chuỗi mô tả. |
| R14-04 | Xóa kết quả chuẩn bị P01 khỏi `plan_results` của mẫu hoàn chỉnh: CP01–03 vẫn đạt, `canStart=true`. Dòng record_checks RESULT-P01 còn MATCHED nhưng payload kết quả tương ứng đã mất. | Nghĩa vụ tới hạn CP02 phải kiểm đầu ra P01 thực và liên kết với dòng ghi/đối chiếu trước CP03. Hiện kiểm semantics của plan_results chỉ bắt đầu từ CP04. Không lấy lời báo MATCHED trong sổ làm vật thay thế sản phẩm ghi ở sổ. |
| R14-05 | Bộ so trước–sau nhận xóa `history`, xóa `checkpoint_checks`, sửa kết luận checkpoint cũ, xóa `record_checks`, đổi output_ref không phiên. Xóa history của mẫu còn cho `canFinish=true`. | Giữ bản cũ/lịch sử cho mọi dữ liệu bằng chứng thuộc phạm vi kho thử, không chỉ declarations và information_contract. Cho phép thay trạng thái hiện hành hợp lệ nhưng phải có phiên/sự kiện; không xóa hay viết lại bằng chứng cũ. |
| R14-06 | 34 địa chỉ nguồn thử vẫn là đề xuất; kiểm endpoint yêu cầu chuỗi schema/key và attestation, chưa phân giải các khóa đó. Probe dùng schema/key không tồn tại nhưng cấp lại attestation mô phỏng vẫn đi 7/7. Máy chủ chưa tự gọi validator, báo cáo cũng đã ghi nhận điều này. | Trong ca thử, mỗi endpoint phải có schema/khóa có thể phân giải, quyền thực và một phép ghi–đọc cùng cấu trúc. Bằng chứng truy cập do công cụ tin cậy sinh, không chỉ trường PASS tự ghi. Giới hạn/cưỡng chế tại cửa ghi kho thử; không nhận ready toàn hệ thống chỉ từ runner. |
| R14-07 | P03 ghi người nhận P04 là “người kiểm độc lập chưa chỉ định”; application.reviewer vẫn “Astra Codex · tự kiểm kỹ thuật”, contract review NOT_REVIEWED. | Giao danh tính người kiểm độc lập và người nhận có quyền trước khi chuyển mốc liên quan. Không thay tự kiểm Host bằng kiểm độc lập; không coi tên hãng/model tự ghi là chứng minh danh tính kỹ thuật. |

### Điểm mô tả cần chốt trong chính CAT-206*, không viết thêm tài liệu song song

Các PRODUCT_SPEC đang có trường gộp `requestId/revision`, `source/scope/version`, `reasons/missingInformation`, với destination như `design_spec[MOT-1.1].outputs.requestId/revision`; đầu vào `incoming_response` lại mô tả các trường tách riêng. `transform` hiện là “Giữ nghĩa/kiểu; không tự điền hay chuyển đơn vị”, chưa diễn tả việc đóng/gỡ gói này. Cần chốt đó là tên nhóm hiển thị hay khóa dữ liệu thực, và mapping ra các trường nhận. Tên nhóm không thể tự được dùng làm đường dẫn ghi.

Đường hủy cũng phải có một cấu trúc rõ: `incoming_response` hoặc sự kiện cancelled phải truyền đủ danh tính/phiên/nơi nhận; không chỉ ghi chữ “hoặc hủy” trong bảng đầu nối. Đây là yêu cầu hoàn thiện thiết kế, chưa khẳng định một payload hủy production đã lỗi.

Hợp đồng DESIGN_TASK là đầu bài đang dùng để tạo thiết kế; PRODUCT_SPEC là hợp đồng sản phẩm cần tạo. Giữ tách này. Không đòi sản phẩm backend đã hoạt động trước lúc thiết kế, nhưng cũng không cho thiếu PRODUCT_SPEC rồi nhận là đầu bài đã đủ để thiết kế.

## 3. Bằng chứng độc lập và phạm vi kiểm

Nguồn làm việc: `5e8dc1f580a051adf10c1f22c13cd77224afc0b5`, trong lúc đọc các task khác làm HEAD chuyển; các file kiểm vẫn cùng hash. Hai lượt Node đầy đủ chạy trên snapshot `f5c36173e00e858cc52bed7cbc99ec1536a8c2cf`.

- view.html SHA256 trước/sau: `132b582a6c09a3349465b648906dd4fd10b0a3408640f3b32daf96099f367630` (không đổi).
- check-record-control.js SHA256: `fc097de590c0a4ab9a427916d7301f3645a513dce03f07c3e7d7a1e04b2f542b`.
- Phiếu nguồn MOW001 SHA256 được runner đọc lại: `d18e0191b5afd0208ae0aa374e43f3cd800ca9bbbcd167e17fb39f08167d546c`.
- Node v22.16.0 chỉ được tải và giải nén vào TemporaryDirectory trong snapshot cách ly, xác minh SHA256 theo manifest chính thức. Archive `f4cb75bb036f0d0eddf6b79d9596df1aaab9ddccd6a20bf489be5abe9467e84e`. Xóa khi kết thúc; **không cài Node vào máy chủ vận hành**, không coi thiếu Node của đường chạy thường đã được sửa.
- Job chính `f36d7f1ef58547478e2052736900ea73`, exit 0, stdout SHA256 `ff6c6b860838ff9f18725e8f711f26ea05b5fa4491b72a51f4c2689e832d4c16`.
- Job kiểm chéo handoff `59da4769e6144c5690daf5963763ce7d`, exit 0, stdout SHA256 `335161edc2d59a52e6296d0780541bb0c74306c6b0b8d7ba68af13e61dca8dac`.
- Chạy `run-tqt-checks.py --verify` nguyên bản: PASS; registry/hash/đọc lại phiếu và hash nguồn luật khớp; self-test 13 ca. TQT-CHECK-001: 87 ca; CHECK-002: 20 checkpoint cases, 55 refs; CHECK-003: 2 positive/34 negative; CHECK-004: 26 cơ bản, nhóm hồi quy đếm lũy kế 59, 15 kho thử, 44 hợp đồng; CHECK-005: 18 master thiết kế nội bộ, 14 ca sai. Không cộng các bộ đếm lũy kế thành tổng số ca độc lập.
- UI browser connector trả BROWSER_UNAVAILABLE tại lượt này; không tuyên bố đã kiểm lại hiển thị. Không PG, không thử ghi qua server thật và không chạy MOW001/G1 sản phẩm.

### 28 probe chính — giữ nguyên hàm hiện hữu, chỉ sửa bản sao

`contract` = trả về `audit(r).contract.ready`; `gate` = mốc được tính từ bộ mẫu 7/7 hiện có; `transition` = `tqtValidateTransition(before,after)`. Bộ mẫu lấy từ chính `check-record-control.js --complete-fixture`.

| Probe | Kết quả hiện tại |
|---|---|
| Xóa 45 PRODUCT_SPEC | contract.ready=true, còn 6 dòng |
| Xóa mọi field requestId | contract.ready=true, còn 48 dòng |
| Sai target_code ở một dòng | contract.ready=true |
| Sai process_code ở một dòng | contract.ready=true |
| Sai mot_version ở một dòng | contract.ready=true |
| Sai rule_version ở một dòng | contract.ready=true |
| data_type=THIS_IS_NOT_A_DATA_TYPE | contract.ready=true |
| source_path=work/missing.json#/does/not/exist | contract.ready=true |
| destination_field=NO_SUCH_COLUMN | contract.ready=true |
| handoff input_ref sang hồ sơ khác | contract.ready=true |
| handoff output_fields=[NO_SUCH_FIELD] | contract.ready=true |
| handoff recipient không được giao | contract.ready=true |
| product_interfaces=[] | contract.ready=true |
| requestId đổi thành nullable/0..n | contract.ready=true |
| Đối chứng: source_master=UNKNOWN | bị từ chối đúng |
| Đối chứng: contract_version từng dòng sai | bị từ chối đúng |
| Xóa plan_results của P01 | canStart=true, CP01–03 còn đạt |
| Xóa application.history | canFinish=true, 7/7 còn đạt |
| Đối chứng: đổi nội dung hợp đồng, không review/ghim lại | chỉ CP01 còn đạt, chặn bắt đầu đúng |
| Đối chứng: đổi output_version P03 | CP01–03 còn, các mốc sau mất hiệu lực đúng |
| Đối chứng: ACK sai người nhận | chỉ CP01–06 còn đạt, không Xong |
| Đối chứng: xóa một record_check | trả lỗi có cấu trúc, không qua mốc; không crash |
| Transition xóa history | PASS |
| Transition xóa checkpoint_checks | PASS |
| Transition sửa checkpoint result cũ | PASS |
| Transition xóa record_checks | PASS |
| Transition đổi output_ref nhưng không tăng phiên | PASS |
| Đối chứng: sửa declaration không tăng phiên/không giữ trước | FAIL đúng |

Probe bổ sung: (i) dùng `catalog.NO_SUCH_SCHEMA` + key không có, cập nhật `spec_token` của access attestation **mô phỏng** và dựng checkpoint tương ứng: 7/7; đây là kiểm ranh giới tin cậy/schema, không chứng minh đã có quyền ghi server; (ii) thiếu scope trong payload đầu ra: 7/7. So trực tiếp fixture với handoff cho thấy thiếu scope ở cả P01–P05 ngay cả trước probe.

## 4. Cách thử tiếp để giảm gãy trước sản phẩm thật

Không dùng một fixture điền sẵn mọi PASS làm bằng chứng đã khép đường dữ liệu. Giữ fixture để hồi quy, đồng thời thêm **một lát cắt có bên giao và bên nhận**:

1. Bên giao tạo payload theo đúng schema/phiên hợp đồng, ghi vào kho thử có hợp đồng. Bên nhận tự đọc bằng ID/phiên, không nhận bản được AI ghép lại trong chat.
2. Kiểm bắt buộc tên/kiểu/nghĩa/đơn vị/null/cardinality, mapping và bằng chứng ghi–đọc. Kết quả kế hoạch gắn payload/bản ghi nguồn, không chỉ output_ref có chữ.
3. Cho qua đường đúng P01→P02 trước; sau đó 1.1→1.2→1.3 và nhánh 1.1→1.3. Khi đạt từng lát thì mới mở rộng; không đợi đủ mọi Master toàn hệ thống.
4. Chèn thiếu trường, sai kiểu/phiên/đích, xóa nghĩa vụ, thay hợp đồng sau review, lỗi nguồn và quyền, hủy/đổi yêu cầu lúc kết quả đang về. Nhận sai phải bị chặn, có nơi ghi lỗi và người xử lý.
5. Mô phỏng đã ghi nhưng chưa ACK, gửi lại/trả muộn, hai người cùng nhận/sửa; không nhân tác động, không ghi đè, không xóa lịch sử, không nhận kết quả cũ. Ca này cần kiểm riêng trước tự động lặp hàng nghìn lần; chưa được chứng minh trong review này.
6. Xác định và kiểm người kiểm độc lập, người nhận thật. Chỉ ghi mốc đạt khi payload, sổ kết quả, quyết định và ACK trỏ đúng cùng sản phẩm/phiên. Thiếu dữ liệu/nguồn thì dừng đúng mốc, không nâng cờ bằng tay.

**Điều kiện để chuyển thử MOW001 có giám sát:** sửa R14-01–05, chốt cấu trúc/mapping đầu ra thực, và chứng minh ghi–đọc cho lát thử đang chạy. **Điều kiện tự động:** ngoài các phần đó, cửa ghi phải buộc kiểm được R14-06; không coi chỉ dẫn README là cưỡng chế. PG vẫn để sau khi trial đủ điều kiện theo D27.

## 5. Đề nghị phản hồi một lượt từ Host

Host Codex ghi ACCEPT hoặc DELTA cho R14-01…07, kèm ca kiểm mới theo từng ranh giới, cập nhật TQT-ISS-007 hiện có. Không mở Master/TH06 hoặc nhân sổ. Reviewer cần thấy (a) thiếu scope bị từ chối, (b) thiếu đặc tả nguồn bị phát hiện, (c) nguồn–đích có đúng schema thật, (d) không qua CP03 khi chưa có kết quả chuẩn bị, (e) không xóa được lịch sử hợp lệ. Kết quả kiểm cục bộ khác ca thật 0/7; không tự nâng tiến độ.
