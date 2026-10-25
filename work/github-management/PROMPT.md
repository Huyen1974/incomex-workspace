# PROMPT — GHM G0 · KIỂM CHỨNG KÊNH CI/CD ĐÃ CHỦ ĐỘNG NGẮT (CHỈ ĐỌC)
RUN_ID: GHM-G0-CICD-VERIFY-20261025-01
STATUS: DRAFT_NOT_READY — KHÔNG TỰ RUN. Claude ACCEPT SHA PROMPT, GPT Host READY cùng SHA, Owner phát RUN mới cho Codex.
Executor: Codex CLI/Desktop · quyền chỉ đọc 2 GitHub repo hiện có và trạng thái VPS; chỉ được ghi STARTED/KQ/Bảng trong task khi có RUN. Không lấy key, không sudo, không sửa source/runtime hoặc tạo repo.

S0 — ĐỌC QUYẾT ĐỊNH CŨ (KHÔNG LẶP ĐO 33 WORKFLOW)
- Root AGENTS.md DROOT56; root COLLAB PROOT08 + PROOT09 ngày 16/10; work/github-management P12/P17/P20/P21; ROADMAP/KE-HOACH. Sử dụng báo cáo P12 root-only nếu quyền sẵn có, không nâng quyền.
- Điều cần xác nhận: cả hai phía GitHub và VPS đã cố ý khóa đường triển khai, riêng sao lưu VPS→GitHub vẫn tiếp tục. KQ lịch sử không được coi là bằng chứng trạng thái live mới.

S1 — BẢN ĐỒ BA TUYẾN VỚI BẰNG CHỨNG READ-ONLY
A. Dev→GitHub: 2 repo mã còn private, main protection/actor rights hiện có, agent surfaces/credentials độc lập, nhánh/PR và CI PR code/test có đường thật hay chưa; phân biệt 3 workflow audit nghiệp vụ với CI kiểm merge; chưa gọi API ghi.
B. VPS→GitHub: lịch backup daily và refs/HEAD của 2 kho nguồn, chênh mã Web/Agent Data; xác định phương thức này không dùng remote origin và không ảnh hưởng Guard (đọc chứng cứ, không chạy job).
C. GitHub→VPS: trạng thái từng job deploy cũ, secret kết nối chỉ kiểm hiện diện/thiếu (không đọc giá trị), đường SSH/webhook, remote origin top-level và Guard pin DROOT56; source SHA image đang phục vụ; đường nào còn bị khóa hoặc UNKNOWN. **Không thực hiện git fetch/pull/ls-remote origin từ VPS; không trigger deploy để “kiểm”.**
- Quan sát Web source/runtime SHA còn UNKNOWN, submodule dirty và Agent Data image/HEAD khác nhau: ghi rõ rủi ro trước mọi đồng bộ.
- Ghi trạng thái mỗi chặng VERIFIED_OPEN / VERIFIED_BLOCKED / UNKNOWN với bằng chứng, thời điểm mẫu và điều kiện an toàn. Không đăng actor/key/network path nhạy cảm lên repo PUBLIC.

S2 — ĐỀ XUẤT THỨ TỰ CHUẨN ĐỂ HOST/OWNER CHỐT
1. Muốn chứng minh *song song code*: kiểm ba agent có môi trường riêng/credential hạn chế/receipt, Free sandbox sạch nếu cần; test branch/PR/Chief/CI độc lập, **không** cần mở GitHub→VPS và không tự nhận CD đạt.
2. Muốn thử *CD thật*: trước hết Owner GO riêng theo DROOT56; main có cơ chế chỉ Chief merge; nguồn GitHub và image/runtime VPS khớp/pin đúng SHA; thiết kế đường deploy quyền thấp có PRE backup/DRY-RUN/staging/Guard POST/smoke/rollback thật, không đơn giản khôi phục workflow và secret cũ.
3. Chỉ sau các cổng này mới đề xuất RUN khác để kết nối thử, không lấy phép READ-ONLY này làm giấy phép triển khai.

S3 — KQ NGẮN/ĐIỀU KIỆN CHẶN
- Bảng một dòng/đường A–C: tình trạng, số điểm đã VERIFY/chưa VERIFY, rủi ro, chứng cứ (không secret), bước Owner phải quyết; vẽ chuỗi S0→CI→Chief→CD với từng cổng STOP.
- `KQ@GHM-G0-CICD-VERIFY-20261025-01 XONG|DỪNG` + Bảng trong COLLAB; XONG chỉ là kết luận khảo sát có đủ chứng cứ, không có nghĩa CI/CD đã nối. Nếu thiếu tài liệu/không có quyền đọc ⇒ UNKNOWN/NEXT_TRIGGER, không giả PASS.
- CẤM: GitHub repo/branch/settings/actions/billing mutation, tạo repo thử, mở lại secret/SSH/webhook, sửa Guard/origin, fetch/pull/push/deploy, restart/container/DB/GSM, mua Pro, tự phát RUN mới. Không giữ terminal/VPS-GHI chờ.
