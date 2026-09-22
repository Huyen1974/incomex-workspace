# Corrections — giữ actual trước/sau

- Dựng component harness lần đầu thiếu Tailwind tokens của ứng dụng, sau đó thiếu @nuxt/image cho VUpload được import dù fixture không dùng upload. Đã dùng lại tailwind.config và @nuxt/image có sẵn, không sửa renderer/không cài dependency UI mới. Build r2 xong trước UI freeze/V1. Sharp cảnh báo image binaries; fixture không dùng ảnh/file, không claim image renderer PASS.
- CUA fill chuỗi rỗng trên spinbutton không xóa giá trị35 trong lần thao tác đầu; request thực vẫn35 và đã update revision1→2. Không đổi nhãn thành negative PASS. Đã dùng phím Select All/Backspace, kiểm DOM trống rồi mới gửi; raw logs giữ lần trước. Fraction12.5 cũng đã đo server422.
- pg-boss setup lần đầu lỗi PG42501 database CREATE khi thư viện tạo schema. Chưa event/worker nghiệp vụ. R2 chỉ grant CREATE tạm cho role bootstrap rồi revoke finally; worker vẫn không có CREATE hoặc quyền sửa release/business record. Không vá queue/library.

- Runtime emission attempt r1 failed with PG 42501 on binding SELECT FOR SHARE. Transaction rolled back (no event/instance/job/effect). Fixed the unnecessary lock in the generic emitter: a statement reads the binding once and persists its immutable release ID in the same enqueue transaction. Producer retains read-only binding permission. Before proof execution, bootstrap owner resets only the empty runtime mapping and discarded release fixture generation, preserving failed-generation evidence. Runtime kernel r1 source and failure are retained; complete runtime matrix runs again after r3 freeze. UI code/guard unchanged.
- Observation helper typo lab_form_materials corrected to actual lab_material_links; earlier observation stores the error instead of counting it as a table PASS.

- Emission r2 then exposed an incomplete producer ACL: pg-boss sends directly to native job_common for this standard queue. Added INSERT to that native table alongside job, no UPDATE/DELETE/claim authority. Transaction again rolled back before event commit. Kernel r3 and release bytes stay unchanged.

- Read-only restarted-v1 observation overlapped event3: its first collector read tables separately, so it is retained as a timeline sample, not used for cross-table counts. Observer now captures all business/queue/audit tables in one SQL statement (consistent MVCC snapshot). Final assertions use the atomic final snapshot and stable worker-stopped snapshots. No worker/product code changed.

- Read-only final environment collector used lc_collate as a setting, which this PG build rejects. Corrected to pg_database.datcollate. All 10 regression negatives had already passed; only environment collection is rerun, no business test mutation.

- Inventory review makes pg8.23.0 an explicit direct dependency because kernel imports the PG driver. It was already installed and executed at this exact locked version through pg-boss; only root package/lock metadata changes, no installed package, kernel bytes, release or worker code changes. Count is 2 direct packages / 21 total, not 1 direct.
