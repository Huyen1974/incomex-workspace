# Nguồn lắp ráp bản phác thảo Task html view

Trạng thái: UI draft, Owner đang chỉnh; không dùng thư mục này để deploy runtime VPS.

- `app.vue`: bố cục và dữ liệu minh họa; dùng UAccordion/UButton/UInput/UBadge/UAlert của Nuxt UI.
- `app.config.ts`: màu violet/slate theo Agency OS hiện có.
- `nuxt.config.ts`, `package.json`: cấu hình preview tĩnh, không backend.
- `pack.mjs`: đóng output Nuxt thành một HTML tự chứa; chỉ phục vụ tài liệu phác thảo.
- HTML dành cho Owner: `../view.html` (một bản chính).

Tái dùng dependencies của web-test/web (Nuxt 3.20.2, @nuxt/ui 2.x, esbuild); không cài framework mới. Chạy từ thư mục này với các dependencies đó: `nuxt generate`, rồi `node pack.mjs`; output là `.output/public/view.html`. Kiểm tra trình duyệt trước khi cập nhật HTML chính bằng workspace tool có expected version/head. Không commit node_modules/.nuxt/.output.

Chưa nối dữ liệu GitHub, nút Cập nhật hay tín hiệu ai đang làm. Thu gọn mở rộng và tìm/chọn việc đã kiểm; phần còn mở là Owner chỉnh bố cục và Host cập nhật kế hoạch triển khai. Không coi prototype là production PASS.
