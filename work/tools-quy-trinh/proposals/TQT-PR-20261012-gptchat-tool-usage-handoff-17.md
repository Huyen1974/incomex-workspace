# PR17 — Rà DOT/Tool: báo cáo đã trao đổi và phần Host cần tiếp nhận

TQT-PROPOSAL: TQT-PR-20261012-gptchat-tool-usage-handoff-17
Ngày lưu: 12/10/2026. Owner yêu cầu lưu các báo cáo để AI/Agent sau tìm được vấn đề.
Vai: GPT Chat lưu báo cáo; Astra Codex giữ Host nội dung, Claude giữ Host Kiểm soát. Không sửa Master, phiếu công việc, quyền hay tiến độ.

## 1. Kết luận và thời điểm áp dụng

Báo cáo gốc trong chat được lập trước P33: **quét file task chưa đủ kiểm kê mọi công cụ AI đã dùng**. Phải theo dõi cả lần gọi, lệnh tạm, công cụ nhà cung cấp và ca thử. Đây không còn là kết luận rằng hiện hệ thống chỉ có sáu DOT hoặc chưa thu thập lần gọi: Codex đã bổ sung ở P33–P36.

Trạng thái mới nhất phải đọc `../README.md` P33/P34/P36, `../COLLAB.md`, `../view.html → catalog.tool_registry` và bằng chứng `../UI-REVIEW-AGGREGATE.json#host_review_P33`, `#host_review_P36`. Lúc lưu đã đối chiếu README SHA256 `2b3d0b642120deed46ec151150a008b0e3e42e4a40dc5ed15da341f01e2cbf5a` tại HEAD `86d1c2ca8c1d5f52b0eb8502d959a8efc4033d21`. Không giao làm lại phần Codex đã hoàn thiện.

## 2. Công cụ đã dùng và nơi tìm lại

Sáu bộ kiểm ở `work/tools-quy-trinh/`, đăng ký trong `view.html → catalog.tool_registry.records`. Master DOT chuẩn là `ML-DEF-024`; `CAT-006` là alias, không tạo Master thứ hai.

| Mã | File nguồn | Chức năng |
|---|---|---|
| TQT-CHECK-001 | check-process-model.py | Mô hình/hợp đồng/mô phỏng |
| TQT-CHECK-002 | check-process-catalog.py | Mã và tham chiếu quy trình |
| TQT-CHECK-003 | check-overview-consistency.py | Phiếu nguồn, điều kiện chuyển mốc |
| TQT-CHECK-004 | check-record-control.js | Hợp đồng, sổ, checkpoint, giao nhận và lịch sử; các mode đọc chuẩn bị/thiết kế/cửa ghi |
| TQT-CHECK-005 | check-work-masters.js | Master, UI, ánh xạ, kiểm trạng thái dùng lại |
| TQT-CHECK-006 | run-tqt-checks.py | Chạy bộ kiểm, kiểm kê, hash và biên nhận |

Lượt kiểm kê trước P33 xác minh 6/6 file khớp hash, không thiếu đăng ký `.py/.js` trong riêng task. Job `ae62152d094e40d3b60194265e0aa2a7` kiểm danh mục/file/hash; job `5f45205b8e134a62826f0efb72034a55` đọc runtime/công cụ phụ; snapshot `b2425aefe028d3f4d10865b12184a82edf9e6539`. Đây là bằng chứng lịch sử, không thay kiểm phiên công cụ hiện hành.

Các công cụ ngoài sáu file đã dùng:
- **MCP/connector:** workspace_read/search/stat/list/exec/exec_status, ui_inspect/ui_screenshot và các thao tác ghi được Owner cho phép. GitHub fetch_file dùng trong các lượt trước; từ khi VPS là nguồn chuẩn không dùng GitHub cũ để suy trạng thái mới.
- **JEV Reference:** đã dùng theo bằng chứng COLLAB P28–P31. Lượt phân loại trong báo cáo gốc có receipt `gen-dec-1791753545-2Mqkr6NUNDpc1BDlJzqy`, model `typesafe/jev-1.13-20260917`; chỉ là tham khảo, không thay kiểm thực tế hay quyền duyệt. Lượt P36 và lần lưu này không gọi JEV.
- **Python/Node kiểm một lần:** lệnh đọc, so nguồn/hash và tiêm lỗi trong snapshot. PR14/PR15/PR16 giữ job/bằng chứng. Không khẳng định đã lưu được mọi mã lệnh tạm nếu chỉ còn kết quả; cần đối chiếu chỗ đã được nhập vào CHECK004.
- **Script triển khai P32:** `prepare.py`, `activate.py`, `activate-r2.py`, `probe.py` đã có tên/hash trong CHECK004.runtime_binding, từng ở `/opt/incomex/staging/tqt-p32`. P36 có runtime mới; không chạy lại các script cũ theo báo cáo này.
- **Mã nhúng/library/ca thử:** engine trong view.html, adapter, helper và case trong bộ kiểm không mặc nhiên là DOT độc lập. Ca thử đi CAT-012; kết quả đi CAT-015; dùng lại tool cha khi phù hợp.

## 3. Phần Codex đã tiếp nhận — tránh chồng chéo

| Yêu cầu gốc | Nơi đã triển khai/thiết kế tiếp |
|---|---|
| Một Master DOT, không trùng CAT-006 | P30, master_identity và alias |
| Kiểm kê rộng hơn file task, theo lần gọi | P33, CHECK006 --audit-vps, nguồn nhật ký được cấp quyền |
| JEV/MCP/công cụ ngoài VPS | provider_tools, external_receipts; thiếu dữ kiện ghi UNKNOWN |
| Ma trận dùng lại không nhập tay hai nơi | reuse_needs và audit_projection từ biên nhận |
| Nhớ phiên, nâng cấp, người kiểm, dùng được/chưa đủ | P34: lifecycle_policy, memory, reviews, changes |
| Dùng lại trên việc thật | P36 và PR16: CHECK004 đọc P02/P03, chữ ký và trạng thái thật |

Tra Master theo mục đích trước khi viết mới. Không chạy hàng loạt file vừa tìm thấy. RETURNED/QUEUED/ERROR không tự là PASS; có công cụ trong danh sách không có nghĩa đã nghiệm thu.

## 4. Việc còn phải quản và nơi giao

| Vấn đề | Tiếp nhận | Căn cứ đóng |
|---|---|---|
| Ca/lệnh tạm của reviewer chưa nối đủ về danh mục và kết quả | Host Codex | Đối chiếu PR14–PR16; ca đã nhập CHECK004 chỉ dẫn lại, ca còn hữu ích bổ sung vào bộ hiện có; job/phiên/kết quả gắn đúng việc |
| Lịch sử ngoài VPS hoặc đã mất dấu | Host Codex, chủ adapter | Phạm vi thu rõ ràng; phần không chứng minh được giữ UNKNOWN; lần mới có biên nhận đúng nền tảng |
| Công cụ tìm thấy chưa chắc dùng được | Chủ công cụ | Nguồn/phiên, hợp đồng, quyền, thử và bằng chứng đúng phạm vi |
| Lần thứ hai phải nhanh và chính xác hơn | Host Codex sau nhận G1 | AI/Agent mới dùng tài liệu và công cụ đã chốt; ghi thời gian/vướng/kết quả, không phải hỏi tác giả |
| Hồ sơ lớn làm chậm kiểm/ghi/đọc | Host Codex | Theo PR16 §4.B: giữ lịch sử, quản lý phiên, đo cải thiện trước khi nhân rộng |

Đây là bảng tiếp nhận của báo cáo, **không là sổ lỗi cạnh tranh**. Host gắn các mục còn mở vào sổ hiện hữu đúng loại (CAT-069/TQT-ISS-007 hoặc nguồn phù hợp), trỏ về mã báo cáo/mục; không mở task/sổ trùng. Không coi các thiếu hụt toàn hệ thống là lý do làm lại sản phẩm G1 đã có bằng chứng.

## 5. Báo cáo liên quan

- [PR14 — hợp đồng/giao nhận P29](TQT-PR-20261011-gptchat-p29-contract-chain-review-14.md): lịch sử để kiểm cách sửa P31.
- [PR15 — các ranh giới sau P31](TQT-PR-20261012-gptchat-p31-final-boundaries-15.md): lịch sử để kiểm cách sửa P32.
- [PR16 — P36, năm mục tiêu và điều kiện nhận G1](TQT-PR-20261012-gptchat-p36-five-objectives-16.md): bằng chứng thật, các phần còn lại và giới hạn nghiệm thu.

Lưu báo cáo không phải chạy lại test, không phải Owner duyệt/ACK và không cho phép chuyển PG. Trạng thái đóng từng vấn đề phải dựa trên bằng chứng mới, không sửa ngược báo cáo lịch sử.
