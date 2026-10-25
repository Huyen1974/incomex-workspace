# HJW P387 · KẾT THÚC NÚT NÂNG HERMES — KHÔNG LÀM LẠI A/B
RUN_ID: HJW-HERMES-UPDATE-CLOSE-20261025-01
STATUS: HOST_DRAFT — chỉ thực thi sau READY theo full SHA cuối chạm PROMPT.
Host: GPT Chat · Reviewer nền: Claude Chat P381/P383 · Executor_Surface: Claude Code CLI do Owner chuyển tay.
Write_Path: MCP workspace_* cho hồ sơ; VPS chỉ qua cơ chế quản trị/Config Apply được duyệt và khóa VPS-GHI. Mac chỉ là màn hình Hermes VPS.

**Mục tiêu duy nhất:** Chốt phần C còn thiếu P386 để lần vá stable kế tiếp Owner chỉ bấm một thẻ Telegram, bộ nâng `hermes-safe-update` thực hiện và báo kết quả. **A token/Kuma và B sudo/GSM/COLLAB đã hoàn thành: không đổi token, không đụng IAM, sudo, write_scope, cron/Guard nghiệp vụ hay chạy lại 69+32 test.** Không nâng Hermes thật khi vẫn đang v0.22.5 stable mới nhất.

**S0 · 0 mutation:** Đọc AGENTS, root/HJW COLLAB, P378–P387, KQ P386, PROMPT; kiểm READY/Owner RUN/lease/Guard và vị trí phiên bản. Dùng P386 làm bằng chứng, không khảo sát lại từ đầu. Dựng bản lùi CHỈ cho file thực sửa. Guard hoặc quyền chặn thì KQ DỪNG, không lách.

**S1 · Thẻ bấm tối thiểu:** Timer stable và nút xác nhận Owner đã tồn tại. Dùng đúng handler `hjw-control` và vòng xử lý root đang chạy; chỉ mở rộng đường này nếu không có cách ít sửa hơn. Thẻ riêng bot Hermes: “Có bản stable X · Nâng / Để sau”. Nhận bấm phải đối chiếu Owner ID + mã dùng một lần, có hạn, chống bấm đôi, gắn đúng bản stable do **root tự xác nhận**; “Để sau” không chạy. Root gọi duy nhất lệnh nâng định sẵn, không nhận tên lệnh hay tham số shell từ callback. Giữ chặn Desktop→VPS, không khôi phục sudo Hermes, không xây plugin/daemon/cron/gateway mới. Nếu cần, chỉnh đúng plugin hiện hữu rồi restart đúng gateway có kiểm và đường lùi; không ảnh hưởng bot cảnh báo P385.

**S2 · Bản vá gọn có đường lùi:** Với bản vá cùng major.minor, ưu tiên quick state snapshot native + bản commit stable trước nâng và đường restore mã/phụ thuộc sẵn có. Trước khi bỏ bản chụp toàn cây ~7 GB phải kiểm được *trên fixture* các file trạng thái quan trọng có trong snapshot và khả năng lùi mã; hãng nói quick snapshot **không** thay dữ liệu DB lớn/migration. Nếu thiếu độ bao phủ hoặc gặp migration, **không bật đường cập nhật gọn cho bản đó** — báo yêu cầu dùng đường thay đổi lớn; tuyệt đối không tắt đường lùi để lấy tốc độ. Đối với bản vá thông thường đã chứng minh an toàn, bỏ upload Google Drive/full fixture trong mỗi lần nâng; giữ mutex tự lấy/trả, kiểm bản phát hành stable, kết quả update, health và một chat/tool nếu có sẵn. KQ nâng VPS KHÔNG chờ Desktop Mac, không ép cùng commit. Desktop chỉ tự cập nhật app theo chức năng app-only của hãng; không bấm nút cập nhật chung có thể nâng nhiều gateway. Không bật tự nâng không hỏi Owner.

**S3 · Kiểm thử ngay, không đợi bản phát hành mới:** Mô phỏng một offer stable mới và callback thật của Owner trên môi trường khô, chứng minh chuỗi nhận thẻ→xác thực→root action cố định→kết quả; tuyệt đối không nâng production vì hiện đang up-to-date. Thử âm: người khác, hết hạn, dùng lại, nhấn đôi, sai target, VPS-GHI bận, Hermes đang chạy model, “Để sau”. Thử `hermes-safe-update check` với bản đang có phải báo “Đã mới nhất”, không thay đổi runtime. Guard PRE/POST + rollback/Đ30–31 CHỈ cho delta nút và bộ nâng, không chạy lại fixture N3 #21 không liên quan. Không được báo đã thử nâng stable thật; ghi `NEXT_REAL_PATCH_UNTESTED` như giới hạn tự nhiên, không mở RUN riêng chỉ để đợi phiên bản.

**S4 · Đóng:** Thay luật P325.7: VPS patch=thẻ bấm + `hermes-safe-update` root, Mac=app-only độc lập; update lớn/migration dùng nhánh thủ công có chứng cứ; không lặp backup 7 GB/Drive/fixture mỗi patch. Ghi KQ cho RUN này, trạng thái C = TESTED_DRY_RUN hoặc DỪNG đúng sự thật; A/B từ P386 giữ nguyên, Guard POST lịch sử của A/B không sửa. Cập nhật roadmap/Bảng/Owner View đúng mức đã đạt, dọn vật tạm, trả VPS-GHI. Không dọn ba báo cáo rời trong RUN này.

STEP_WALK (một RUN, không giữ khóa trong lúc chờ người):
| Pha | Ai/trình tự | Giới hạn | Bằng chứng / điểm dừng |
|---|---|---|---|
| S0 | Claude Code khi Owner giao đúng READY | read-gate đầu lượt | baseline+backup file chạm, kiểm cổng; FAIL→DỪNG |
| S1 | Claude Code sau S0 | một lượt triển khai nhỏ | thẻ/Owner/nonce/root action; thiếu cơ chế sẵn có→DỪNG |
| S2 | Claude Code sau S1 | trong cùng lượt | snapshot gọn + rollback fixture; không chứng minh được→không bật đường gọn |
| S3 | Claude Code sau S2 | trong cùng lượt | pilot/âm+Guard; FAIL→lùi phần chạm |
| S4 | Claude Code cuối lượt | báo ngay | KQ/commit/nhả khóa/0 việc nền |
