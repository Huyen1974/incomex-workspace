# TEST Gate3–4 — kế hoạch trước code

Ngày 11/09/2026. PM cho phép lab synthetic riêng trên VPS2. Tái dùng harness Gate0/Gate2, nhãn proof-g34-20260911-01a07f1f, network internal, PG512MiB/DC1024MiB/worker512MiB, 0.5CPU mỗi container, không public port, không production write. Chụp 5demo process và 2safeGET trước/sau; cleanup theo ownership.

I0: cổng ghi + native ItemsService/transactions/revisions/idempotency có sẵn; lỗi đã biết là runtime đọc forms.main. I1: PG FK/UNIQUE/immutable-release/transaction giải quyết integrity; không tự xây queue. I2: Directus native content version là delta còn editable, không tự chứng minh immutable transitive semantic closure; ItemsService vẫn là cửa quyền hiện thời. I3: Nuxt chỉ đọc/transport, không quyết quyền/nghĩa. I4: Joi17.13.3 build mô tả + pg-boss12.30.0 retry/queue/ACK sẵn có. I5: compose các vật trên. I6: chỉ sửa adapter cũ để resolve release từ instance (không tin release caller), lấy profile/form/capability exact từ closure, không đọc nghĩa main; phân loại lỗi trước giao native queue retry. Không I7/framework mới.

Tách pin semantics (form/field/unit/profile/Joi engine/action implementation/binding) và quyền current (native identity/status/permission/scope). Receipt + output cùng transaction, key occurrence/instance/effect riêng; unknown-effect phải reconcile receipt trước retry. Immutable là DB constraint + privilege, không chỉ hash tự khai.

P1 queuedV1→editmain/publishV2→runV1/newV2; P2 revoke livepermission; P3 transient/permanent/unknown/auth; P4 currentprofile drift; P5 stale parent/slot/cancel; P6 boundary writes. Mỗi bước lưu actual result, không thay fixture-pass bằng runtime-pass.

Hai mũ tự rà trước chạy: (thiết kế) dùng cơ chế có sẵn; (phản biện) release không đủ nếu worker/server còn đọc main; DB immutable phải chặn sửa; native permission phải tái kiểm ngay khi ghi; unknown-effect không tự retry; producer không tự chọn target/release; mapping candidate không bằng authoritative. Review này do cùng agent thực hiện, không nhận là independent review.
