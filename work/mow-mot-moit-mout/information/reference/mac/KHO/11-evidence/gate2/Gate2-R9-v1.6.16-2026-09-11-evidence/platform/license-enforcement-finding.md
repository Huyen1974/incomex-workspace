# Directus 12: actual resource restriction

12.3.1 API ping 200, isolated synthetic DB boot thành công. Seed same Gate0 fixture dừng ở POST /permissions: HTTP 403 RESOURCE_RESTRICTED, category custom_permission_rules_enabled. Đây là licensing feature enforcement, chưa chứng minh hook/ItemsService/guard thất bại kỹ thuật.

Không chỉnh entitlement/license checks, không ghi permissions trực tiếp SQL để vượt chặn, không dùng admin thay business identities để gọi scoped test PASS. Giữ nguyên evidence request sanitized. No OIG signup/activation/acceptance/egress.

Bounded bridge: lab riêng PG16.15 + accepted Directus11.5.1 dùng cho Nuxt4/Node24 và worker Node22.23.2/pg-boss12.30.0 smoke. Đây là kiểm các thành phần độc lập theo §10, không Directus12 guard PASS, không OLD STACK production adoption. Directus12 full slice cần license key hợp lệ cho custom permissions, sau đó rerun unchanged scope. Design vẫn TARGET-oriented, contracts giữ platform-neutral; deployment license precondition OPEN.
