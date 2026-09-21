# Nguồn lắp ráp Task html view

UI03, 21/09/2026. Owner chỉnh trực tiếp tại https://vps.incomexsaigoncorp.vn/knowledge/modules. Nguồn tài liệu: GitHub incomex-workspace. Mirror: /ui-preview/hpml-view-for-user/view.html. Không dùng thư mục này deploy runtime VPS.

## Danh mục và cách dùng
- app.vue: renderer/phác thảo, UAccordion, UTabs, UTooltip, UButton, UInput, UBadge, UAlert của Nuxt UI 2 hiện hữu. Hai tab; sidebar UI02 × 0.8; fixture ghi nhãn rõ.
- app.config.ts: màu điều khiển theo Agency OS; tín hiệu dùng màu kiểu Apple, thanh 6px bo tròn, chấm 9px. Tooltip/focus và nhãn hỗ trợ đọc không chỉ dựa màu.
- nuxt.config.ts, package.json: preview tĩnh, colorMode storageKey riêng.
- pack.mjs: đóng một HTML tự chứa; HTML chính là ../view.html.
- MOT lấy nguyên work/mow-mot-moit-mout/mow-mot-moit-mout.html; mirror dẫn xuất ở /ui-preview/hpml-view-for-user/documents/mow-mot-moit-mout.html. Không copy source vào thư mục task này. Iframe tách CSS/JS, có nút mở rộng; các liên kết/asset trong tài liệu gốc giữ nguyên, không tự công khai file phụ.

Tái dùng dependencies web-test/web: Nuxt 3.20.2, Nuxt UI 2, esbuild. `nuxt generate` rồi `node pack.mjs`. Kiểm tra browser; ghi source + HTML qua workspace tools expected version/head. Không commit node_modules/.nuxt/.output. Runtime shell VPS giữ nguyên; mirror HTML nguyên tử, đối chiếu hash.

## Contract đấu nối — HVU-DATA01/B2
GitHub `main` là SSOT dữ liệu. UI03 là khung đã có; B2 chỉ thay fixture bằng snapshot sống.
- Tự phát hiện task từ mọi `work/*/COLLAB.md`; root `## Đã xong` chỉ đánh dấu Done.
- Scheduler kiểm remote HEAD mỗi 60 giây. HEAD không đổi → thoát; HEAD đổi → đọc một revision nhất quán, dựng snapshot rồi publish nguyên tử. Webhook chưa cần; chỉ xét nếu sau dùng thật thấy 60 giây quá chậm.
- Snapshot tối thiểu: `sourceRevision`, `generatedAt/receivedAt`, `syncStatus`, goal A0 nguyên văn, 4 stage theo AGENTS A9, currentStage, lastActors/activeActors, documentPath + documentRevision. Thiếu tín hiệu → unknown/null, không đoán.
- `lastActors`: B2 chỉ dùng bằng chứng surface rõ ràng đã tồn tại; không suy từ Git author/pusher dùng chung. `activeActors` để null khi chưa có nguồn đáng tin. B3 mới chuẩn hoá dấu `Surface:` tại cổng ghi.
- HTML chính của công việc được mirror như **dữ liệu**, không chạy/build app từ repo. `view.html` của Task html view là app/runtime và vẫn deploy có kiểm soát theo README §11.
- Last-good bắt buộc: lock, không hạ revision, validate trước publish. Fetch/parse/copy lỗi → giữ snapshot tốt cuối, cập nhật health `error/stale`, tự retry lượt sau. Một task lỗi hiện warning/unknown nếu có thể; không làm trắng toàn dashboard.
- UI đang mở đọc lại snapshot/health mỗi khoảng 60 giây; khi `sourceRevision` đổi thì thay toàn snapshot của task, không cộng dồn chấm xanh.

B2 là đường ống tự đổ. B3 actor-surface và B4 webhook/active actor chỉ mở sau khi B2 chạy ổn.

Tham chiếu: https://developer.apple.com/design/human-interface-guidelines/color ; https://docs.github.com/en/webhooks/using-webhooks/best-practices-for-using-webhooks
