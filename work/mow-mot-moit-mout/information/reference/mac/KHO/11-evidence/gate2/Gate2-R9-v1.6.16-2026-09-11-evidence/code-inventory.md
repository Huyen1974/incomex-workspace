# Code và dependency — khai đầy đủ theo phạm vi

Production code/schema/deploy trong lượt này: **0**. Có code mới phục vụ lab và workshop; không gọi chúng là cấu hình/no-code. Bảng kê tính dòng vật lý, kèm bytes/hash/diff để dòng dài không che độ lớn; không dùng LOC suy hiệu suất hoặc chứng minh tối giản.

Guard extension 163+2 dòng và runtime kernel92 dòng giữ nguyên byte accepted Gate0; xem `platform/candidate-source-comparison.json`. Đây vẫn là custom code cần bảo trì nếu được chọn triển khai, không bằng0 vì tái dùng. Form/UForm/useGuardedSubmission giữ candidate trước; adapter87 dòng và integration27 dòng là nợ code đã tồn tại, không phát sinh thêm theo Form trong đợt này. DirectusTable/useDirectusTable/types/useDirectus được đối chiếu CURRENT. Kết quả từng file trong `code-inventory.json`.

## Code mới/thay đổi trong thử nghiệm

| File | Dòng vật lý | Phạm vi |
|---|---:|---|
| `platform/ui-source/app.vue` | 18 | NEW_OR_CHANGED_LAB_CODE |
| `platform/ui-source/composables/useDirectus.ts` | 12 | NEW_OR_CHANGED_LAB_CODE |
| `platform/ui-source/nuxt.config.ts` | 10 | NEW_OR_CHANGED_LAB_CODE |
| `platform/ui-source/plugins/directus.ts` | 8 | NEW_OR_CHANGED_LAB_CODE |
| `platform/ui-source/plugins/presentation.server.ts` | 5 | NEW_OR_CHANGED_LAB_CODE |
| `platform/ui-source/server/api/lab/[...path].ts` | 18 | NEW_OR_CHANGED_LAB_CODE |
| `platform/ui-source/server/api/session.post.ts` | 8 | NEW_OR_CHANGED_LAB_CODE |
| `workshop/index.html` | 10 | NEW_WORKSHOP_PROTOTYPE_CODE |
| `workshop/workshop.js` | 84 | NEW_WORKSHOP_PROTOTYPE_CODE |
| `workshop/workshop.css` | 2 | NEW_WORKSHOP_PROTOTYPE_CODE |

Workshop là một composition HTML/JS/CSS,5 góc nhìn dùng một fixture và một state; CSS Master/Nháp2 tái dùng có provenance. Nó mô phỏng trạng thái/đường tiếp tục và đo thao tác; không có API quyền, queue hay publish thật. Nếu giữ lại sau Gate2 phải thay fixture bằng read/write contract có thẩm quyền, không mang state TEST thành truth.

Lab transport session/proxy/SDK/presentation/bootstrap chỉ nối các component tái dùng tới isolated CMS. Không có page theo từng workflow. Không đưa auth fixture, session endpoint hoặc loopback settings vào production. SSR directives chỉ presentation, không dùng để bỏ validation/scope. Nuxt CSS fallback là native config, Vue alignment theo dependency Nuxt; chi tiết lỗi và audit còn mở trong platform verdict.

Dependency lab: Nuxt4.5.2, Vue3.5.42, @nuxt/ui2.22.3, @nuxt/image1.11.0, @directus/sdk19.1.0, @vueuse/shared13.9.0, auto-animate0.8.4, vue-dompurify-html5.3.0, v-perfect-signature1.4.0. Worker pg-boss12.30.0/pg8.23.0 tái dùng. Không ép nâng UI4/Image2 trong gói này; audit/module proof còn PARTIAL. Exact package-lock được giữ.

`harness/` là script dựng lab, chạy test, xuất dữ liệu, thu hồi và soạn/kiểm artifact; mọi SQL/function/Flow logic trong đó cũng là code TEST. File nguồn trong remote-target/remote-bridge giữ đúng bản thực chạy; không cộng trùng các bản copy vào production LOC. Manifest ghi từng file/bytes/hash. Khi tái chạy phải đọc ownership/scope, tạo credential mới và lab riêng; không chạy mù vào production.
