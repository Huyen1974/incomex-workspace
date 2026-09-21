# Nguồn lắp ráp Task html view

UI03, 21/09/2026. Owner chỉnh trực tiếp tại https://vps.incomexsaigoncorp.vn/knowledge/modules. Nguồn tài liệu: GitHub incomex-workspace. Mirror: /ui-preview/hpml-view-for-user/view.html. Không dùng thư mục này deploy runtime VPS.

## Danh mục và cách dùng
- app.vue: renderer/phác thảo, UAccordion, UTabs, UTooltip, UButton, UInput, UBadge, UAlert của Nuxt UI 2 hiện hữu. Hai tab; sidebar UI02 × 0.8; fixture ghi nhãn rõ.
- app.config.ts: màu điều khiển theo Agency OS; tín hiệu dùng màu kiểu Apple, thanh 6px bo tròn, chấm 9px. Tooltip/focus và nhãn hỗ trợ đọc không chỉ dựa màu.
- nuxt.config.ts, package.json: preview tĩnh, colorMode storageKey riêng.
- pack.mjs: đóng một HTML tự chứa; HTML chính là ../view.html.
- MOT lấy nguyên work/mow-mot-moit-mout/mow-mot-moit-mout.html; mirror dẫn xuất ở /ui-preview/hpml-view-for-user/documents/mow-mot-moit-mout.html. Không copy source vào thư mục task này. Iframe tách CSS/JS, có nút mở rộng; các liên kết/asset trong tài liệu gốc giữ nguyên, không tự công khai file phụ.

Tái dùng dependencies web-test/web: Nuxt 3.20.2, Nuxt UI 2, esbuild. `nuxt generate` rồi `node pack.mjs`. Kiểm tra browser; ghi source + HTML qua workspace tools expected version/head. Không commit node_modules/.nuxt/.output. Runtime shell VPS giữ nguyên; mirror HTML nguyên tử, đối chiếu hash.

## Contract đấu nối — thiết kế, chưa chạy
GitHub là SSOT. Snapshot cho từng work-id chứa:
- sourceRevision: commit SHA; receivedAt: thời điểm VPS nhận thành công; syncStatus: fresh/stale/error.
- goal: nội dung mục tiêu lấy từ nguồn đã thống nhất, không AI diễn giải lại.
- stages: đúng 4 ID goal/plan/execute/accept, mỗi mục state pending/done/blocked/changing/unknown + note. Trạng thái và giai đoạn hiện tại tách biệt; currentStage xác định đang ở đâu. Unknown không giả làm chưa làm; tooltip ghi rõ. Mẫu hiện tại goal=done, plan=changing, còn lại pending.
- lastActors: danh sách ID vừa có đóng góp được xác nhận trong snapshot mới nhất của công việc; activeActors: null nếu chưa có bằng chứng, [] nếu nguồn xác nhận không ai làm, hoặc danh sách ID đang làm. Không suy đang làm từ một commit.
- actors: gpt-chat = Chat GPT; gpt-work = Codex/GPT Work; claude-chat = Chat Claude; claude-work = Claude Code CLI/Cowork; hermes-chat = Hermes Chat; hermes-code = Hermes Code. Không dùng Git pusher dùng chung để đoán actor. Ưu tiên dấu vết actor/Executor_Surface có sẵn trong COLLAB/tool execution.
- documentPath: HTML chính đã khai báo trong công việc; nội dung và metadata cùng sourceRevision. Assets được khai báo rõ trước khi mirror.

Webhook chỉ là tín hiệu tải lại, không phải nguồn trạng thái nghiệp vụ. Luồng dự kiến: xác thực chữ ký GitHub/repo/branch → chống trùng delivery + lock → đọc HEAD mới nhất, chỉ work-id bị ảnh hưởng → dựng snapshot/HTML cùng revision → đổi bản nguyên tử → trình duyệt nạp snapshot mới. Không chạy mã runtime/build từ repo tài liệu. Webhook trễ/trùng không hạ phiên bản; cập nhật việc A không xóa tín hiệu việc B. Thay nguyên lastActors/activeActors của việc liên quan, không cộng dồn xanh. Không tự tắt màu theo đồng hồ; lỗi nhận giữ bản tốt cuối và hiển thị stale. Kiểm tra định kỳ bù webhook thất lạc; lịch cụ thể chốt khi triển khai qua hạ tầng hiện hữu. Khi tab mở, cần cơ chế nạp snapshot mới để người dùng không phải reload.

Ưu tiên tái dùng receiver/job/kiểm tra hiện có. Chưa tạo webhook, chưa có snapshot backend, chưa tự đồng bộ. UI hiện chỉ có fixture có nhãn và bản HTML MOT đã lấy về. Tình trạng đang làm để xám cho đến khi có nguồn đáng tin. COLLAB ghi phần còn mở, Owner đang chỉnh UI.

Tham chiếu: https://developer.apple.com/design/human-interface-guidelines/color ; https://docs.github.com/en/webhooks/using-webhooks/best-practices-for-using-webhooks
