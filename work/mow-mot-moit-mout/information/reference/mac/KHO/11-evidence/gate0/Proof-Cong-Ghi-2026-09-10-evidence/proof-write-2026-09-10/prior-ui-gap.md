# UI — source gap, chưa đạt kiểm tích hợp

**NOT RUN integrated UI / NOT COMPLETED user submit→canonical record→reopen.** Không lấy Directus API 200 làm UI PASS. Không dựng trang, renderer hoặc ảnh mock thay bằng chứng.

Đã đọc đúng build được bind vào Nuxt đang chạy: `/opt/incomex/deploys/nuxt-output`, `nitro.json` ghi build 2026-09-04T12:03:39.211Z, Nuxt3.20.2/Nitro2.12.8. Runtime Node20.20.0; image digest trong `source-current.json`. Thư mục checkout trên VPS chỉ có scripts/sql/tests; git HEAD tra từ thư mục cha không được coi commit của build. Source local cũ chỉ hỗ trợ truy đường; kết luận dựa compiled module current có hash.

**Đường đã có:** block Form → UForm → FormCustom; `form.schema` được map thành input/textarea/checkbox/file/signature. Module current `server/chunks/build/UForm-0Pia6Vp9.mjs`, SHA256 `ecf89012e63e357d612dfde8910b40ca58a5944383038bb0a5492bfbe421a67c`.

| Vị trí compiled source | Actual behavior | Phần thiếu cho lát cắt |
|---|---|---|
| 704–712 | Tạo groups từ schema trong setup; renderInput dùng name/type/placeholder/modelValue | Không resolve contract_ref/version/subject/unit hoặc system-created write policy |
| 725–728 | Click submit gọi trực tiếp props.onSubmit sau preventDefault | Không được coi client validation là quyền server; chưa kiểm behavior trình duyệt |
| 750–753 | Validator trong UForm yêu cầu email cố định | Không phải validator contract thời lượng/ghi chú của lát cắt; đường click trực tiếp còn cần kiểm riêng, không suy mọi submit đều bị email chặn |
| 755–762 | `createItem("inbox", {data:formData, form:props.form.id})` | Write target inbox, không lab_task_records/canonical runtime record; không form_version trong payload, không stale/idempotency context |
| 764–767 | Success message/redirect | Không có readback/edit saved record trong component này |
| props form + type Form | Nhận object form; schema có trường tùy ý nhưng logic chỉ đọc các props nêu trên | Không có chứng cứ binding chọn đúng version và server dùng cùng contract |

**Điểm dừng:** dùng lại được khả năng vẽ input từ khai báo, nhưng đường submit/version/readback đúng yêu cầu chưa có mapping đã được kiểm. Không dựng đầy đủ clone Nuxt hoặc tự thêm inbox adapter để vượt gap. Nuxt lab không boot, UI before/after và browser identity = NOT RUN. Directus native content version được đo độc lập, không thay kết quả UI.

**Phần nối tối thiểu cần PM giao kiểm tiếp:** renderer hiện hữu lấy đúng form ID + version từ binding, cổng ghi dùng cùng contract/profile và write target có quyền; UI mở lại bản ghi đúng identity. Xét khả năng cấu hình existing data/form path trước; chỉ nếu source/API chứng minh không đủ mới nộp adapter candidate. Không kết luận đã cần một renderer mới.

Evidence: [current-build-source.json](./current-build-source.json), [source-database.json](./source-database.json), [execution-map.md](./execution-map.md). Đây là giới hạn của đường UForm/blocks đã truy, không khẳng định không có renderer phù hợp ở mọi module chưa đọc.
