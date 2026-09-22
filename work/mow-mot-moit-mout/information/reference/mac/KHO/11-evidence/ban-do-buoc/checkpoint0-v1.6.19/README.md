# Checkpoint0 — bản đồ bước · v1.6.19 ·12/09/2026

Entry duy nhất cho Owner/Agent: [HTML hiện hành](../../../../BAN-DO-BUOC-UI-AGENT.html). Đang CHỜ XÁC NHẬN PHẠM VI. Chưa Owner freeze, chưa independent review, chưa Pha B. D04 nghĩa đã Owner ACCEPT11/09 theo PM; Gate1 completeness DOING, Gate2 PARTIAL, Gate3/4 PARTIAL tạm dừng khóa cuối.

## Tiếp tục đúng chỗ

1. Đọc bản duyệt 2 phần ở đầu HTML; mở chi tiết đúng family/luồng/source khi cần.
2. Chờ Owner phản hồi phạm vi. Ghi nguyên văn phản hồi, delta yêu cầu và nguồn; chỉ freeze sau xác nhận thật.
3. PM/supervisor kiểm lệch nguồn23↔14: nguyên văn9 bước lịch sử chưa có, không giả crosswalk đầy đủ. Tám đường logic đã có; chưa được dùng làm UI/runtime PASS.
4. Sau xác nhận, làm toàn Pha B theo pm-command: bảng tool thực có trước, rồi thông tin/control/candidate/gap/contract/data, reverse Gate0. Không chạy lab/product code trong gói này.
5. Cập nhật cùng lượt HTML/dataset/evidence/tổng heatmap và SSOT; ma trận chi tiết chỉ ở HTML. Mỗi work ảnh hưởng phải ghi Step/UI refs hoặc N/A có lý do.

## Chọn đúng nguồn

Dataset nhúng trong HTML hiện hành là dữ liệu của bản đồ. dataset.json ở đây là bản evidence chính xác của checkpoint này, không phải nguồn current thứ hai. 87 định nghĩa:38chung+47đặc thù+2ngoài12;987 lượt gắn family/flow (có chồng giữa các phạm vi);248dòng trace. Không tính tỷ lệ UI/tool ở Pha A. Các test render dùng VM/DOM stub offline, không browser/visual QA; CUA đã từ chối file URL và không đi vòng bằng server/browser khác.

Code tài liệu lưu trong document-harness.zip để truy nguồn. Đây là snapshot quá trình tạo/check/stage, không entry để Agent sau chạy mù: đường staging lịch sử đã dọn; handoff.py cố ý chặn ghi lại khi current hash thay hoặc map tồn tại. Muốn tái tạo hãy dùng sandbox tài liệu và inputs đã niêm phong, không chạy đè main. Không code sản phẩm/DDL/DML/runtime/deploy mới.

## Danh mục đầy đủ

- `BAN-DO-BUOC-UI-AGENT.html` — Snapshot HTML checkpoint; mở bản root để relative assets đúng.
- `README.md` — Điểm phục hồi phiên và danh mục này.
- `check-results.json` — Tự QA, giới hạn và các phần chưa làm.
- `dataset.json` — Exact dataset checkpoint; chưa Owner freeze.
- `discussion.md` — Trao đổi Owner/PM giải thích tinh thần; v2 là lệnh hiện hành.
- `document-function-check.json` — Offline rendering/filter checks; không browser QA.
- `document-harness.zip` — Code tài liệu/QA/staging, không production code.
- `manifest.json` — Hash các files evidence, không tự hash chính manifest.
- `pm-command.md` — Lệnh hiện hành đầy đủ, có checkpoint bắt buộc.
- `protected-check.json` — INV/Factory/ownership preservation checks.
- `source-design-v2.9.html` — Nguồn thiết kế cũ raw; không authority current.
- `source-manifest.json` — Nguồn yêu cầu và hash/scope.
- `ssot-result-v1.6.19.html` — Snapshot kết quả; raw links theo vị trí root.
- `ssot-source-v1.6.18.html` — Snapshot trước; raw relative links theo vị trí gốc.
- `ssot.diff` — Diff duy nhất của main.
- `workbook-source.json` — Hàng Excel đọc có sheet/row, không chỉnh workbook.
- `write-receipt.json` — One-write receipt, backup/hash, preserved proof/workshop.
