# W005 Revision 2 — Phiếu A Contract/Data · v1.6.18

**BLOCKED BY DATA-AUTHORITY.** Không xin Gate3/4 exit hoặc Gate5 entry. Gate3/4 DOING/PARTIAL; Gate5–7 NOT STARTED; O1–O3 NOT VERIFIED. D04 WAITING OWNER; quyết định D04 riêng cũng chưa xóa được khoảng trống kỹ thuật dưới đây.

## Đã có bằng chứng mới

Hai fresh sessions đọc Intent từ PG, tự reuse12 Version và tạo Draft/WAIT; hai fresh resume gắn Condition đúng parent/revision. Lệnh replay đã chạy lại ở một lab mới bằng hai sessions nữa, đạt cùng tập reuse/topology/missing meaning. Đây là Agent thật với tool transcript, không phải hàm tạo Draft viết sẵn. Catalog TEST/policy/tool contract được chuẩn bị trước; join/slot của đầu ra còn biến thể; chưa phải dispatcher hoặc compiler tự chạy toàn chuỗi trên production.

Readiness14 dòng được đọc trên generic report sẵn có, không page/UI code mới. Draft xuất hiện P01 sau nút Làm mới. Bản kiểm lấy completion/output từ MOT; MOUT chỉ đọc/tham khảo. Không chứng minh live push, P02 editing hay automatic resume scheduler.

Native Joi40 profiles /11 family đạt116/116 ca cấu trúc. Compile/test cuối đạt17/17, gồm kiểm parameter thật của13 nguyên liệu + MOW candidate + C04 Search, ranh giới89/90/91, lỗi output không ACK và các ca ghi sai/lặp/stale. V1 có bộ59/60/61 riêng. Guard chỉ được sửa chung, worker giữ nguyên; frozen runtime17/17 sau thay guard. Xem manifest/source để phân biệt phiên bản harness trước/sau.

Lifecycle:32/32 ca quyền/runtime, có current grant, expiry, revoke, SoD với author thực sự được gán grant approver, atomic child rollback, exact release, replay, deactivate. Một kiểm source riêng xác nhận publish Flow chỉ ghi Version/Release; publish và activate có receipts riêng. Thêm2 ca profile IO/C04 drift chặn publish ở cuối. Không gọi kiểm source là một lần đo snapshot giữa hai action. Native Flow9 cho lifecycle/feedback, không approval engine mới; số tổng actual Flow/operations ở export cuối.

Feedback có integer ID theo schema `feedbacks` đã kiểm trên production. Cổng UUID ghi action receipt; native Flow tạo feedback integer trong cùng transaction, vì vậy không cần đổi guard để hỗ trợ integer key. Feedback1 → MOW DraftV2, ngưỡng90, reuse12 Version +1 Condition variant; V1 giữ nguyên;6/6 negative/replay. Sau đó sửa C04 Search và exact IO refs bằng khai báo, DraftV2 revision2, compile17/17. Hai Version Capability/MOT mới thuộc sửa hợp đồng, không phải fresh Agent tự tạo. Approval mới dùng riêng cho ca drift đã bị revoke. V2 vẫn Draft; NOT MEASURABLE YET về hiệu quả kinh doanh.

## Gate4: mẫu số và sáu fact còn thiếu

[Matrix177 fact](data/pilot-critical-matrix.json) giữ nguyên172 fact frozen và5 bổ sung ownership ở bước5; không xóa fact để tăng tỷ lệ.171 có mapping tới nguồn/primitive **trong lab**,6 UNKNOWN trong phạm vi đầy đủ một HMITL → AUTO. Đây không phải171 mapping production đã được nghiệm thu. Mỗi dòng giữ kiểu, nguồn, quyền, đường đọc/ghi, phiên bản, quan hệ, provenance, I0–I5 và giới hạn. Matrix385 vị trí của Rev1 là lịch sử/outside Pilot; không giải311 UNKNOWN toàn hệ trong lượt này.

| Fact | Quan sát thực tế / còn thiếu |
|---|---|
| Runtime.task_instance_id | Chỉ có Instance của lát cắt một AUTO. Không có thực thể Task Instance riêng để phân biệt từng việc trong cùng MOW. |
| Runtime.executor | AUTO có service ID; người ghi record không tự trở thành người chịu trách nhiệm Task. Chưa có resolved HMITL executor gắn Task/current authority. |
| Runtime.input | Release hiện giữ literal input. Đổi một giá trị ở đúng Instance bị403 PIN_CONTEXT_MISMATCH, record giữ nguyên. Đây là ranh giới an toàn hiện hành, chưa phải đường nhập HMITL động. |
| Runtime.handoff |14 record người ghi có0 liên kết tới Runtime Instance. Chưa có quan hệ receipt/output của việc trước → input việc kế trong PG. |
| MOUT.context | Đã khai báo mô tả record/context; chưa resolve được từ Task Context có quyền đọc tương ứng. |
| MOUT.consumer_ref | Giá trị hiện tại là mô tả “human reference/result view”, chưa phải ref tới consumer đã bind. Registry lab chỉ có thư viện Draft và bảng readiness; không đổi nhãn này thành một exact ref giả. |

[Schema + counterexample](evidence/09-data-lock/pilot-data-gap.json), [registry/Versions hiện hành](evidence/09-data-lock/pg-final.json). Bốn fact đầu của probe được mở rộng thành sáu sau đối chiếu executor và consumer; phần tăng được ghi rõ trong matrix, không thay số frozen.

## Đề xuất giới hạn cho lần khép khoảng trống

Ưu tiên thẩm định nguồn `tasks`/Instance và backend `information_unit`/`unit_version` hiện có; không tạo bảng production theo tên các bảng lab. Các bảng lab là prototype contract. `unit_version.body/content_hash` là cơ chế version nội dung đã có; chưa tự coi nó là typed semantic Version có scope/owner/ref policy. `tasks.assigned_to` là text, `task_checkpoints` không thay Task Instance. Metadata/fn source thật nằm trong [đối chiếu nguồn](evidence/09-data-lock/production-candidate-sources.jsonl).

Model tối thiểu để PM xét: Task giữ ref tới Instance, MOT Version và step key; resolved executor từ People/Role/Delegation; input-context/output-receipt refs có FK hoặc equivalent được kiểm; MOUT bind consumer và record context từ Task. Dùng native columns/FK/policy/Flow trước. Không copy7 trường readiness thành nguồn mới.

I0–I5 của khoảng trống đã đối chiếu theo nguồn. PG columns và native policy có thể lưu/bảo vệ context nhưng chưa tự sửa được phép so sánh literal input hiện tại trong guard; Flow chạy sau kiểm đó. UI không được trở thành authority. pg-boss chỉ giữ delivery/ACK. Chưa kết luận mọi composition native đều bất khả thi. Nếu cần adapter input-binding, phải chứng minh một sửa generic giữ current authority, exact released profiles và thực thi được cả release cũ; không dùng một cờ bỏ kiểm pin, không per-workflow code, không page mới. Lượt này không viết thêm engine hoặc tự nhận một nguồn chưa được chứng minh chỉ để có UNKNOWN=0.

Phiếu B Platform: **ACCEPT WITH FOLLOW-UP**, không discovery lại. D08 DECIDED PM: “Ghi nhận thời lượng xử lý”. Formal Gate5 chỉ chạy sau PM chấp nhận exit và D04 khi cần; xem [plan](GATE5-PLAN.md).
