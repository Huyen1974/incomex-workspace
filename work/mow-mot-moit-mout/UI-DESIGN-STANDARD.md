# Quy chuẩn UI cha — cửa vào cho người và AI

**SSOT nội dung: [★ UI cha](https://vps.incomexsaigoncorp.vn/knowledge/modules?task=mow-mot-moit-mout&view=content&section=matrix-view-process)**, nguồn `ban-duyet.html#parent-ui-standards`. Owner 08/10/2026 yêu cầu đặt quy chuẩn đúng từng UI; tệp này chỉ dẫn đường, không giữ bản sao quy chuẩn.

| UI | Quy chuẩn và nguồn mẫu |
|---|---|
| UI.MASTER | [Mở đúng mục](https://vps.incomexsaigoncorp.vn/knowledge/modules?task=mow-mot-moit-mout&view=content&section=standard-UI.MASTER) |
| UI.CANVAS | [Mở đúng mục](https://vps.incomexsaigoncorp.vn/knowledge/modules?task=mow-mot-moit-mout&view=content&section=standard-UI.CANVAS) |
| UI.CONFIG | [Mở đúng mục](https://vps.incomexsaigoncorp.vn/knowledge/modules?task=mow-mot-moit-mout&view=content&section=standard-UI.CONFIG) |
| UI.STUDIO | [Mở đúng mục](https://vps.incomexsaigoncorp.vn/knowledge/modules?task=mow-mot-moit-mout&view=content&section=standard-UI.STUDIO) |
| UI.REVIEW | [Mở đúng mục](https://vps.incomexsaigoncorp.vn/knowledge/modules?task=mow-mot-moit-mout&view=content&section=standard-UI.REVIEW) |
| UI.WORKSPACE | [Mở đúng mục](https://vps.incomexsaigoncorp.vn/knowledge/modules?task=mow-mot-moit-mout&view=content&section=standard-UI.WORKSPACE) |
| UI-029 · Tìm kiếm chung | [Mở đúng mục](https://vps.incomexsaigoncorp.vn/knowledge/modules?task=mow-mot-moit-mout&view=content&section=standard-UI-029) |
| UI-008 · MOUT Builder | [Mở đúng mục](https://vps.incomexsaigoncorp.vn/knowledge/modules?task=mow-mot-moit-mout&view=content&section=standard-UI-008) |

- [Quy tắc dùng chung](https://vps.incomexsaigoncorp.vn/knowledge/modules?task=mow-mot-moit-mout&view=content&section=parent-ui-common).
- [Cổng kiểm trước bàn giao](https://vps.incomexsaigoncorp.vn/knowledge/modules?task=mow-mot-moit-mout&view=content&section=parent-ui-review-gate); phiếu [UI-REVIEW-CONTRACT.json](UI-REVIEW-CONTRACT.json), chạy `python3 work/mow-mot-moit-mout/check-ui-review.py <receipt.json>`.
- [Rules](https://vps.incomexsaigoncorp.vn/knowledge/modules?task=mow-mot-moit-mout&view=content&section=matrix-view-uis) giữ nguyên tắc hệ thống. Chi tiết từng khuôn UI cập nhật tại UI cha.
- [Danh mục UI con](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/danh-muc-ui-con-v1.html) đọc `ui/child-ui-registry.json`. Khối 4 Mẹ trong UI cha đọc cùng registry, không có danh sách URL thứ hai.
- Source/renderer trên VPS là UI thực thi; tài liệu không tự chứng minh đã nối PG hoặc nghiệm thu chức năng.
- [Kết quả rà trước đây](UI-AUDIT-20261007.md) và các phiếu cũ giữ để truy nguồn. Phiếu hiện hành cho mục UI cha: [UI-REVIEW-PARENT-GALLERY.json](UI-REVIEW-PARENT-GALLERY.json).

CE-20261008-PARENT-SSOT · Owner giao trực tiếp: đường mở UI đang có + quy chuẩn tại từng UI cha. Chuyển nội dung từ bản quy chuẩn trước và phần UI.MASTER trong FORMULA-AI-README; giữ mã neo, giữ lịch sử Git. Thư mục Desktop/quy trình chỉ được đối chiếu, không sửa bản lịch sử.
