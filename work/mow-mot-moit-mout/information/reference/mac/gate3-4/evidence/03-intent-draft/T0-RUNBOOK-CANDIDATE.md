# Runbook ứng viên T0 — rút từ hai transcript thật

Đây là ứng viên orchestration, chưa cài thành T0 production hoặc chứng minh độ ổn định toàn catalog.

1. Đọc work entry; xác thực transport hiện thời; đọc Intent từ PG.
2. Tìm candidate theo nghĩa/family và đọc các published versions; khi lexical search không trúng, đọc bounded catalog qua native pagination. So sánh type/unit/operation/completion và where-used refs.
3. Resolve transitive reused UUID set; giữ nguyên owner semantics trong catalog. Tạo Search Brief có candidate comparison/provenance.
4. Ghi Draft Package qua cổng ghi, expected revision0; không tạo lại MOT/MOIT/Field đã có.
5. Khi Condition tương thích chưa có, ghi missing request gắn parent UUID/revision/slot + owner + checkpoint và dừng WAIT.
6. Fresh resume phải đọc lại request/parent/result; dùng CAS cho parent và tính lại readiness. Bước này được kiểm riêng ở 04-missing-resume.

Không có danh sách ID hoặc declaration hoàn chỉnh trong prompt. `tool-sequence.json` giữ lệnh thật; transcript JSONL giữ toàn bộ input/output. Các ID bước và cách biểu diễn slot khác nhau giữa hai lượt, nhưng cùng trỏ condition của MOT AUTO sau một HMITL. Chưa khẳng định runbook là máy deterministic hoặc đã kiểm nhiều family. Không suy tỷ lệ reuse hệ thống từ hai lượt cùng một fixture.
