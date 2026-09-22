# W005 Rev 2 — nguồn proof và kế hoạch trước triển khai

**Đã kết thúc lượt v1.6.18 — BLOCKED BY DATA-AUTHORITY.** Các đoạn dưới lưu lý do I0–I5 trước khi làm, không phải danh sách chưa chạy. Kết quả hiện hành ở ../../README.md và ../../REVIEW.md. Freeze172 +5 bổ sung =177; còn6 gap. Lab đã dọn, không chạy lại setup script trên môi trường có dữ liệu.

Nguồn: `configure-*`, `prepare-*`, `repair-*` khai báo native theo thứ tự evidence; `compile-readiness.py`/`compile-and-test.py`/`provider-smoke.py`/`candidate-release.py` là compiler và runner TEST; `lifecycle-*`, `feedback-*`, `close-declared-data.py`, `current-profile-stale.py` là ca proof, nhiều script không idempotent. `extension/index.js` là guard generic cuối; worker kế thừa ở ../runtime/kernel.mjs. `map-pilot-facts.py` tổng hợp mapping với giới hạn production; `snapshot.py`/`export-final-config.py` đọc lab; `cleanup-lab.py` chỉ dọn đúng label. `archive-evidence.py` không chạy lại mù.

Chỉ `replay-head.py` là lệnh khởi tạo/rerun đầu chuỗi đã kiểm: cần SSH vps2, Docker images đã có, Codex CLI đăng nhập sẵn. Nó dựng lab mới, chạy2 phiên, export và cleanup; chỉ proof PG Intent→Draft/WAIT trên catalog/guard seed ban đầu, không replay lifecycle hay UI phiên cuối. Xem SUPERVISOR-REVIEW-INPUT.

Freeze: `evidence/02-freeze/pilot-critical-set.json`, 172 fact classes, không đổi mẫu số theo kết quả. Lab `proof-g34r2-20260911-01a07f1f`; network internal, không public port, PG16.15/DC11.5.1 image exact đã rehearsal. Không deploy sản phẩm. Không đổi guard/worker trước khi config bị chứng minh thiếu.

I0: giữ cổng ghi v17, Joi, receipt/CAS/current ItemsService; metadata production đọc mới ở `production-authority.jsonl`. workflows/workflow_steps là editable topology, PK-only, không semantic family Definition/Version độc lập. APR có vote/quorum/apply nhưng approver/proposer text, không exact material/release digest/expiry; không copy rồi gọi đủ lifecycle authority. Current UI workflow library (`web/pages/knowledge/workflows/index.vue`) dùng table_registry, DirectusTable; có thể tái dùng nguyên byte với registry lab trỏ Draft source.

I1: PG native UUID/FK/UNIQUE/check/index và immutable storage giữ integrity; JSONB cho family parameters hợp lệ. SQL procedure/trigger mới nếu có vẫn tính code. Không tạo bảng cho từng family hoặc 7 cột readiness.

I2: Directus collection/field/relation/permission/Flow declaration là đường ưu tiên: identity current, system actor/date, filter blocking, conditional operations, native CRUD/audit. Pilot-specific policy nằm trong khai báo synthetic, không engine approval riêng.

I3: tái dùng nguyên byte trang thư viện workflow + DirectusTable trong lab UI existing transport. Không sửa UI/page cho Pilot; chỉ chọn host component có sẵn và registry data. Không dùng bảng lab_contracts sai nghĩa để giả UI Draft.

I4: Joi17.13.3 + Directus native filter/operations, pg-boss12.30.0 đã khóa. Không thêm product dependency/queue/auth engine. Không research platform tiếp.

I5: compose generic routes/profiles/native fields and permissions with existing immutable release/queue. Missing canonical semantic facts được khai báo lab riêng có owner/source/status và đánh dấu NEW_REQUIRED candidate cho PM; không nhận là production authority. Bằng chứng loại reuse sẽ gắn riêng từng fact trong bước9. Nếu composition không bảo vệ atomicity/current policy, đo lỗi trước rồi chỉ mở adapter tối thiểu trong phạm vi được phép; không per-workflow logic.

Hai fresh Agent chỉ đọc TOOL-CONTRACT + PG Intent + catalog/checkpoint, không SSOT/transcript/sample/ID gợi ý. Dùng phiên Codex mới có JSONL tool transcript. Root chuẩn bị môi trường và thu evidence; không chọn bước tool cho Agent. Hai initial runs trước missing-resource publish; fresh resume sau. Input/missing/Draft là PG qua cổng ghi. Code hỗ trợ proof phải ghi riêng khỏi reusable product adapter; không giấu trong SQL/Flow.

Bảy mục readiness được resolve từ refs. Bước đầu nhận Trigger, bước sau nhận previous output + condition/join. Machine compile có evaluator generic và expected độc lập theo contract; material digest pin evidence, chưa gọi O1/2/3 VERIFIED. Lifecycle qua nonadmin policy synthetic; D04 chưa chốt trách nhiệm thật.
