# D04 — một đề xuất trách nhiệm để PM trình Owner

**OWNER DECISION REQUIRED.** Chưa quyết thay Owner. Không chặn việc nộp Gate1; chặn việc hiện thực hóa cách giao/bàn giao có nghĩa chưa thống nhất. Không hỏi Owner giữa gói việc.

Cùng vai thứ ba hiện được dùng với ít nhất hai nghĩa khác nhau: C02 list kiểm `forwarder`/người chuyển tiếp, nhưng drawer hiện **Làm thay**; C39 module assignment mô tả người làm thay khi người thực hiện vắng và ủy quyền còn hiệu lực; C12 rule table có người được chuyển tiếp, thiếu chỉ cảnh báo. Đây là khác trách nhiệm, không chỉ khác nhãn.

| Lựa chọn | Cách hiểu | Tác động |
|---|---|---|
| **A — tách nghĩa, dùng refs có sẵn (khuyến nghị)** | Người thực hiện chịu trách nhiệm task hiện tại. Người làm thay thực hiện task đó theo ủy quyền có hiệu lực. Người nhận bước kế là executor do NTGV của MOT đích phân giải. Nếu nghiệp vụ cần đầu mối chuyển giao thì đặt nghĩa riêng, không dùng thay executor. Người nhận báo cáo là notification/report recipient. | Không ngầm chuyển trách nhiệm do đổi nhãn. Có thể vẫn một panel, không đòi thêm màn hoặc bảng; phải map refs/danh tính/ủy quyền sau catalog review Gate3/4. |
| B — giữ một “vai 3” đa nghĩa, phân biệt bằng ngữ cảnh | Cùng ô có thể là người làm thay hoặc người nhận bước kế; phải khai loại và luật ưu tiên cho từng chỗ dùng. | Ít nhãn ban đầu nhưng tăng branch giải thích, dễ cấp sai quyền và bàn giao sai. Chưa có evidence UI hiện tại phân biệt đủ. |

Owner cần quyết **nghĩa trách nhiệm theo A hay B**; PM chịu trách nhiệm chuẩn bị thuật ngữ và mapping cụ thể. Khuyến nghị A không tự cho phép ủy quyền, thêm người, đổi quyền hay thêm schema.

Sau quyết định: Gate2 trình bày kết quả phân giải gồm người/vai, luật NTGV/version, nguồn ủy quyền, thời điểm hiệu lực và lý do thiếu. Gate3/4 xác định identity source, delegation semantics, policy khi vắng/trống và quyền ký; Gate6 kiểm một task được làm thay, một handoff tới task mới, ca hết hạn/thu hồi ủy quyền. HMITL thiếu executor không chạy; AUTO không bắt buộc có executor người. Hành vi BLOCK/WARN hiện trong Help chỉ là đề nghị, D05/policy phải chốt theo loại tác động.

Evidence: [C02 detail](browser/C02-detail-dom.txt), [New MODT source](source/839d16634c-admin-new-modt) lines 991–1032 và 1428–1469; [NTGV table](source/a7f08313d4-ntgv-rule-table-v1.js) line28; [C12 Help](browser/C12-help-dom.txt). Không click duyệt/gửi/Done.
