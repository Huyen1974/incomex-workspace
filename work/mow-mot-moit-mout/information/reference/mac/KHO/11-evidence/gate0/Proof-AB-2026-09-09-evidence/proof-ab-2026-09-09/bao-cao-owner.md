# Báo cáo gửi GPT Chat · 09/09/2026

**Đã thực thi; A/B nộp PM REVIEW / PARTIAL.** Retrieval cũ giữ PM ACCEPT/DONE. Factory DONE; FEAS PARTIAL; Gate0 DOING; O1–O3 NOT VERIFIED; R1 chưa mở.

- **AI khai và ghi được:** 1 MOW nháp, 1 MOT, 1 form; 6 yêu cầu nguyên liệu → 4 reuse, 2 needs_decision, dùng 3 Field có sẵn. Thêm ghi chú bằng native content version, không tạo Field trùng hoặc chuyển binding cũ. False-reuse 0/4 trong quyết định Agent theo contract TEST ONLY; false-new N/A. Agent độc lập đọc lại checkpoint thành công, dữ liệu nghiệp vụ không đổi.
- **Cổng ghi mới bảo vệ được một phần:** các ca ngoài quyền, giả actor, tự ghi ngày tạo, giá trị/FK sai bị chặn. Joi nhận 2 khai báo đúng, chặn 11 biến thể sai, nhưng chưa nối vào cổng. **FAIL:** contract_ref giả bên trong JSON và revision cũ vẫn được API lưu. Retry chỉ chặn trùng khóa, chưa chứng minh idempotency đầy đủ.
- **UI chưa được chứng minh:** source renderer hiện submit vào inbox, thiếu mapping contract/version/đích ghi/đọc lại. Không tạo renderer mới; UI tích hợp NOT RUN, publish NOT COMPLETED, runtime NOT RUN. C chỉ đọc source và so 2 thư viện; pg-boss là ứng viên thử sau, chưa cài/chạy.
- **Dùng lại / code:** PG lexical, Directus CRUD/policy/validation/audit/version, Joi có sẵn. Code sản phẩm/adapter/runner/.vue mới: 0. Có 14 file harness, 504 dòng và 8 collection TEST ONLY; không gọi đây là zero-code. Token/công người tổng: NOT MEASURED.
- **Bàn giao:** lab và credential đã dọn; trạng thái 5 container demo và hai HTTP smoke không đổi (chưa full regression). SSOT cập nhật một lần **v1.6.11**, có backup v1.6.10; archive chứa snapshot HTML đúng bytes sau sửa.

**Đúng một việc PM cần quyết:** giao phép thử trên cùng lát cắt để cổng ghi cưỡng chế contract và expected revision, gồm cả native version save; ưu tiên cấu hình/quan hệ/validation/quyền hiện có trước khi xét adapter.

[Chi tiết và tái chạy](./README.md) · [Kết quả từng chặng](./summary.json) · [HTML để PM đọc trực tiếp — read-only evidence](./ssot-v1.6.11-read-only.html).
