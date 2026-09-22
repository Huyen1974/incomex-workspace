# Lệnh giao Codex — cưỡng chế cổng ghi trên lát cắt A/B hiện có

**PM: GPT Chat · 09/09/2026. Đây là lệnh thực thi proof trong lab, không phải vòng thiết kế mới.**

## 1. Nguồn và quyết định PM

Đọc SSOT thực tế tại `/Users/nmhuyen/Desktop/quy trình/cấu trúc hệ thống.html` và gói `Proof-AB-2026-09-09-evidence.zip`. Snapshot `ssot-v1.6.11-read-only.html` trong ZIP là bằng chứng, không phải SSOT thứ hai để sửa.

PM đã kiểm offline toàn bộ manifest: **93 tệp khớp kích thước/hash**, HTML snapshot khớp hash sau sửa `9330b93b4b8965a2a3015d8d28bdce66034b332dbc3a934d463c75f555c118b9`. Đã đối chiếu raw HTTP/PG, seed, validator, native version source, checkpoint, UI gap và runtime triage. PM không chạy lại VPS/Directus/PostgreSQL trong lần review này.

**Nhận bằng chứng A/B với kết luận PARTIAL; không nghiệm thu cổng ghi an toàn hoặc toàn bộ authoring.** Retrieval đã ACCEPT/DONE, không đo hoặc tune lại. Factory architecture DONE; FEAS PARTIAL; Gate 0 DOING; O1–O3 NOT VERIFIED; R1 chưa mở.

Đã có bằng chứng: ba Field được dùng lại trong fixture, tạo Draft qua API với test identities, Joi kiểm ngoài API, native content version cuối lưu được, phiên Agent độc lập đọc lại checkpoint. Chưa có bằng chứng full resume có thực hiện hành động tiếp, release bất biến, UI tích hợp hoặc runtime.

**Mục tiêu duy nhất lượt này:** tìm và chạy được một đường ghi dùng chung mà Agent/UI không thể bỏ qua kiểm hợp đồng hoặc ghi đè từ revision cũ. Không mở rộng bộ MOW/MOT/MOIT, không chữa bằng cách bắt Agent tự nhớ chạy validator.

## 2. Phạm vi được phép và giới hạn

Dùng lại harness, fixture, dữ liệu test và sơ đồ hiện có: **1 MOW nháp, 1 MOT, 1 form family, 3 Field** (thời lượng phút, ngày tạo hệ thống, ghi chú). Cho phép thêm các request/fixture âm tính tối thiểu để kiểm sai tham chiếu, sai quyền và ghi đồng thời. Không chuẩn hóa toàn kho.

Chỉ dựng tài nguyên lab mới có nhãn, database/network/volume/credential riêng và resource limits; kiểm lại tài nguyên trước chạy. VPS2 chỉ có demo theo xác nhận Owner, nhưng **phải bảo toàn demo**: không restart/replace/kill container demo, không dùng volume hoặc credential của demo, không public cổng DB. Không clone dữ liệu nghiệp vụ, không nâng cấp stack, không sửa production. Chạy trên exact image/digest đã đo ở proof trước; ghi lại actual versions, không suy từ tag.

Được phép cấu hình collection, quan hệ, validation, quyền và constraints cần cho chính lát cắt trong lab. Đây là schema thử nghiệm, không chốt số bảng/schema production.

**PM cho phép thử tối đa một thành phần bảo vệ ghi dùng chung trong lab nếu bằng chứng cho thấy cấu hình/native hiện có không đủ.** Thành phần này chỉ được dùng cơ chế mở rộng chuẩn của Directus hoặc primitive PG thích hợp; không fork Directus, không xây API platform/validator/engine mới, không tạo code riêng theo MOW hoặc Field. Phải dùng lại validator/service/transaction hiện có và ghi trung thực mọi dòng code mới, kể cả SQL/hook. Không gọi custom code là cấu hình để làm đẹp I-level.

Không cần quay lại xin quyết định chỉ vì một cấu hình native không đáp ứng. Thử đường đơn giản nhất trong giới hạn trên; chỉ dừng nhánh khi cần engine mới, thay đổi lớn, phụ thuộc mới không kiểm soát hoặc phạm vi ngoài lab.

## 3. Tìm nguyên nhân và chọn một đường triển khai

Không xây hai phương án hoàn chỉnh. Trước sửa, lập bảng nhỏ cho các đường ghi mà test identities thực sự có quyền gọi: item create/update, native version create/save/promote nếu mở, và bulk nếu đang mở. Với mỗi đường: ai kiểm quyền, ai kiểm hợp đồng, revision nào được so, mutation xảy ra ở đâu. Đường không cần cho pilot thì đóng bằng quyền và kiểm rằng gọi trực tiếp bị từ chối.

Hai FAIL cũ là expected baseline phải tái hiện trong lab trước khi vá:

- `forms.schema[].contract_ref = nonexistent-contract` vẫn được lưu dù Joi ngoài API từ chối.
- Item PATCH với `If-Match` giả vẫn HTTP 200 và đổi title.

Đây là lỗi của **đường tích hợp đang thử so với yêu cầu sản phẩm**, không phải bằng chứng mọi cấu hình/phiên bản Directus đều không hỗ trợ giải pháp. Không ép giữ header `If-Match` nếu exact API không hỗ trợ; cần expected revision được cưỡng chế thực tế.

Ưu tiên theo thứ tự:

1. Dùng các quan hệ thật/constraints và quyền/validation sẵn có để loại bỏ nơi buộc phải tự kiểm lặp.
2. Tận dụng API/native operation có semantics phù hợp nếu source và thử nghiệm chứng minh được.
3. Nếu còn thiếu, một guard/gateway dùng chung có validator và transaction; bảo vệ hoặc khóa các đường ghi vòng ngoài. Dùng cơ chế extension chuẩn, không chép lại cả CRUD/auth/versioning.

**Không bắt buộc cứu native `/versions/:id/save`.** Nếu không bảo vệ được sạch trên stack hiện tại, khóa nó đối với business identities của pilot và chọn đường version phù hợp khác trong lab. Kết luận rõ native content version còn được dùng cho việc gì. Không giữ cửa phụ không an toàn chỉ để nói “dùng lại native”.

## 4. Hợp đồng phải được kiểm tại nơi ghi

Nguồn có thẩm quyền là catalog/profile được quản trị trong PG, không phải nội dung `contract_ref`, datatype/unit/target do caller tự khai.

- Resolve được Field, exact contract version, profile và quyền sử dụng; không chỉ kiểm chuỗi có tên giống ID.
- Có ID thật nhưng sai Field/contract, sai unit/operation, sai version hoặc sai scope cũng phải bị chặn.
- Thiếu/null/unknown material không mặc nhiên PASS.
- Caller không được chọn một profile “dễ hơn” để né hợp đồng của object.
- Cập nhật từng phần phải kiểm **trạng thái hợp nhất sẽ được lưu**, không chỉ fragment nhận được.
- Kiểm lại profile mẫu: `min(1)` và cho phép duration/note chưa đủ chứng minh duration bắt buộc luôn hiện diện. Thêm ca form chỉ có note nhưng thiếu duration theo đúng intent fixture; expected phải được ghi trước thử. Không coi 11 ca cũ là toàn bộ bộ kiểm.

**PG-first thực chất:** nếu một tham chiếu material có thể được biểu diễn bằng FK/link record phù hợp, ưu tiên cách đó thay vì chôn ID tự do trong JSON rồi viết nhiều vòng kiểm. JSON hiển thị/snapshot được phép tồn tại nhưng phải là dữ liệu dẫn xuất hoặc được cưỡng chế đồng bộ từ một nguồn ghi có thẩm quyền. Không dựng hai bản quan hệ cùng writable. Không dùng CHECK truy bảng khác thay cho FK.

Chỉ chuẩn hóa phần cần thiết của fixture; không thiết kế lại catalog toàn hệ. Joi vẫn được dùng nếu phù hợp, nhưng schema thực thi phải lấy từ profile quản trị, không chứa nhánh hard-code theo tên/ID các ca thử. Không nhận profile tùy ý do Agent gửi như một mã luật được phép chạy.

## 5. Revision phải được kiểm nguyên tử

Tách rõ: business version; revision của Draft đang sửa; và ID lịch sử Directus. Không mặc nhiên coi chúng là một.

Server phải cấp/read-back revision của tài nguyên thực sự được cập nhật. Khi ghi: kiểm expected revision và thay đổi dữ liệu trong **cùng một atomic operation/transaction**. Có thể dùng conditional update/locking phù hợp của PG và service hiện có; không SELECT-so sánh xong rồi UPDATE ngoài transaction. Không tự thay expected revision của caller bằng “current” để request luôn thành công.

Bắt buộc thử hai tình huống khác nhau:

- Hai phiên đọc cùng revision thật; phiên A ghi thành công, phiên B dùng revision cũ phải bị từ chối.
- Hai request đồng thời cùng expected revision, thay đổi nội dung khác nhau; chỉ một được commit, request còn lại báo conflict rõ, không last-write-wins âm thầm.

Nếu dùng native version save, phải kiểm revision của **nội dung Draft version đó**, không lấy `mainHash` lúc promote rồi suy rằng save đã an toàn. Kiểm đường ghi item, version save và mọi đường còn được mở cho caller. Đường không bảo vệ được phải đóng và test deny.

Một request bị từ chối không được để lại canonical object/ref/version delta bị thay đổi một phần. Error/security log riêng được phép, nhưng không ghi audit thành một successful business change.

## 6. Không nhầm native content version với phiên bản chạy bất biến

Nguồn service trong ZIP lưu version delta rồi ghép lên main; binding của MOT hiện vẫn là chuỗi `main`. Kết quả r4 chỉ chứng minh main không đổi trong lần save đã đo, **không chứng minh bản cũ sẽ bất biến khi main thay đổi sau đó**.

Lượt này không dựng full release engine. Nhưng phải ghi rõ disposition của đường version được chọn:

- Native content version là nháp biên tập, hoặc
- Tham chiếu exact version có semantics bất biến đã được chứng minh trong lab.

Không đánh publish/activation/pinning PASS khi chỉ có Draft. Không bắt buộc dùng native content versions làm kho bản phát hành nếu semantics không khớp. Một version record bất biến có FK rõ là ứng viên được phép xét trong model thử, không phải yêu cầu mở một hệ version mới.

## 7. Bộ thử hữu hạn và điều kiện kết thúc

Đóng băng payload, expected và script trước lượt đo của từng phương án. Giữ kết quả trước/sau và mọi correction. Không sửa nhãn để làm PASS.

| Nhóm | Expected tối thiểu |
|---|---|
| Ghi hợp lệ | V1 và thay đổi thêm note được lưu/đọc lại đúng; Field dùng chung không nhân bản |
| Tham chiếu/hợp đồng | Fake/null/missing; ID thật nhưng sai hợp đồng/version/unit/target; profile không được phép; trạng thái hợp nhất sai → không commit |
| Field bắt buộc | Note-only thiếu duration theo fixture phải được phát hiện, không lọt nhờ array min(1) |
| Bypass | Bỏ hoàn toàn validator client; gọi trực tiếp các API còn mở → vẫn được bảo vệ. Đường đã đóng → deny |
| Revision | Revision đúng ghi được; missing hoặc stale bị xử lý theo rule đã chốt; hai writer đồng thời chỉ một commit |
| Quyền | Human/service hợp lệ ghi được; outsider, ngoài scope, giả actor/approver và tự đặt ngày tạo bị chặn trên các đường được dùng |
| Retry | Cùng logical request không tạo thêm object/effect; đọc lại được kết quả trước. Cùng key khác payload không ghi đè. Nếu chỉ có lỗi trùng PK, báo còn PARTIAL về idempotency, không gọi hoàn tất |
| Dấu vết/rollback | Đối chiếu actor, resource/version, request/correlation có nguồn server và dữ liệu trước/sau. Rejected write không có partial business mutation |
| Phiên mới | Agent mới đọc checkpoint và ref/version thật; không chỉ tin câu “PASS” lưu trong checkpoint. Sau khi cổng an toàn, thực hiện một hành động test tiếp hợp lệ mà không tạo lại object |

Đây là bộ thử cổng ghi của lát cắt hiện tại, không full security audit hoặc load test. Các biến thể dùng cùng harness; không phát sinh hàng loạt work mã mới.

Một candidate được nhận ở phạm vi proof nếu request hợp lệ chạy được **và** tất cả đường được cấp quyền trong scope đều không cho qua contract/revision sai. Đóng hết mọi write để có 100% deny không là PASS.

Nếu không đáp ứng được trong phạm vi một giải pháp dùng chung đã cho phép, nộp FAIL/PARTIAL cùng request/source gây chặn và lượng thay đổi tối thiểu còn cần. Không viết thêm tài liệu để thay phép thử, không vá engine vô hạn.

## 8. Giữ đường tới UI và runtime, không lạc vào cổng ghi

**UI:** giữ `ui-gap.md` là issue thật: UForm hiện gửi inbox và chưa có binding/version/write-target/readback phù hợp. Không lấy API PASS thay UI PASS. Lượt này không xây renderer hoặc trang mới. Đầu ra cổng ghi phải kèm đúng request/response mẫu mà renderer hiện hữu cần: form ID + version/revision, dữ liệu được phép nhập, submit action qua cổng, record ID và read-back. Không cho UI tùy chọn tên bảng đích ngoài policy.

Nếu một đường nối renderer đã có, hoàn toàn cấu hình được và không làm tăng scope code, cho phép một smoke tích hợp sau khi cổng PASS; nếu không, báo NOT RUN và **chỉ rõ phần nối tối thiểu**, không lặp khảo sát toàn UI. Việc AI khai báo → UI đổi mà không sửa `.vue` vẫn là điều kiện sản phẩm chưa được nghiệm thu.

**Runtime:** pg-boss mới là ứng viên theo `runtime-triage.md`, chưa cài/chạy. Không triển khai queue/runner trong lượt này. Một thư viện job queue không tự chứng minh toàn bộ MOW chạy được. Giữ Proof C độc lập và chưa hoàn thành; không nâng cấp stack để né lỗi cổng ghi.

## 9. Evidence, công thực hiện và SSOT

Dùng lại scripts lab và cleanup có kiểm ownership. Ghi actual config/native features đã tận dụng, code generic mới nếu có, file/LOC/chức năng, phụ thuộc và phần phải bảo trì. Không tối ưu số LOC bằng nén code. Không gọi harness/config công chuẩn bị là miễn phí.

Đo riêng: dựng môi trường; chuẩn bị profile; các request/runtime test; lỗi/debug; số lần Agent cần phán đoán và hỏi người. Không có telemetry thì ghi NOT MEASURED, không ghi 0. Không suy tỷ lệ 98% khai báo từ ba POST đã được chuẩn bị sẵn.

Nộp cùng bộ bằng chứng: README ngắn, source/config exact có hash, kết quả từng ca, HTTP và PG before/after, transaction/concurrency trace, quyền caller, audit, error logs đã khử secret, replay và cleanup. Snapshot HTML mới phải đúng hash SSOT sau cập nhật.

Chỉ cập nhật SSOT **một lần sau actual evidence**, có backup đúng quy định hiện hành. Không ghi đè một SSOT mới hơn từ snapshot v1.6.11. Không mặc định đánh DONE A/B, Gate0 hay O1–O3.

Sửa tại chỗ các câu current đã stale: Owner card còn “B/C chưa chạy” phải thành “B đã thử một phần, còn lỗi cổng; C mới triage”; checkpoint đọc lại không được gọi full execution resume; giữ raw lịch sử nguyên vẹn. Không thêm framework/checklist song song.

**Báo Owner tối đa một màn:** chọn đường ghi nào; dùng lại những gì; thêm code gì và vì sao; ca hợp lệ/ca âm tính/đồng thời đạt hay không; UI/runtime đang ở đâu; còn đúng blocker nào. Đừng chỉ báo “đã thêm validator/expected_revision”.

## 10. Tài liệu kỹ thuật tham chiếu — không thay bằng chứng exact image

Các cơ chế dưới đây là căn cứ thiết kế chuẩn, không chứng minh đã được tích hợp trong hệ này:

- PostgreSQL 16 constraints: https://www.postgresql.org/docs/16/ddl-constraints.html
- PostgreSQL 16 transaction isolation/conditional UPDATE: https://www.postgresql.org/docs/16/transaction-iso.html
- Directus filter hooks, transaction context và accountability: https://docs.directus.io/extensions/hooks
- Directus API endpoints/extensions: https://directus.com/docs/guides/extensions/api-extensions/endpoints
- Directus content-version delta và promote: https://docs.directus.io/reference/system/versions

Kiểm source/API exact image đang chạy trước khi dùng. Filter trước commit khác action sau commit. Khi gọi internal services phải truyền đúng accountability/transaction; không bỏ accountability rồi vô tình chạy quyền cao. Không coi hook vào `forms.items.update` mặc nhiên chặn mọi native version save.

**Kết quả PM cần:** một cổng dùng chung có bằng chứng chặn lỗi thật với ít code nhất hợp lý; hoặc một thất bại xác định chính xác phạm vi còn thiếu. Không cần thêm một bản kiến trúc hay hơn. 
