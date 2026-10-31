# HJW G8 — MỘT VIỆC NHỎ: ghi danh ở cổng hiện hữu và dọn phần thừa
RUN_ID: HJW-G8-MIN-WRITE-ONEPASS-20261031-26
STATUS: DRAFT_FOR_CLAUDE_CHAT_REVIEW_ONCE — NOT READY / NOT STARTED / NO EXECUTION.
Host: GPT Chat. Reviewer: Claude Chat một lần trước READY. Executor sau READY và Owner dispatch: Claude Code CLI Mac, không gọi Codex.
Write_Path nếu RUN được duyệt: HJW COLLAB/Bảng/evidence qua Workspace Gateway; chỉ nhánh DRAFT PR358 nếu thật sự cần sửa tối thiểu mã nguồn. Không quyền VPS/runtime/main.
Read_First: AGENTS A0/A2/A5/A6; root COLLAB/STOP; HJW COLLAB §0/§1–3 và P453/P458/P491/P493/P494/P495/P496; evidence RUN25 writer map + manifest; PR358 HEAD235dc88087257f5163f44201beb9e69c5f738025, PR357 HEAD36c682914c9f412078113b6d85319f11356d1130 (đã nằm trong PR358), PR360 đã merge; các route hiện có workspace_* (AD) và fs_* (helper). Dùng nguồn đã kiểm kê; không đọc lại toàn bộ VPS.

## 1. Đích duy nhất — không xây “vé”
Owner muốn biết AI nào, làm việc gì, đã ghi gì. “Vé” chỉ là NHÃN công việc mang theo lệnh ghi, không phải thực thể. Không có cấp/phát vé, TTL, revoke, DB, session registry, daemon, service hay Gateway thứ hai.
- AI nào: Gateway lấy authenticated principal từ kết nối thật. Chỉ coi principal chứng minh sản phẩm/môi trường khi credential độc lập và có bằng chứng; shared credential như GPT Chat/Work/Dot, helper, cron chỉ biết kết nối, không thể khẳng định AI cụ thể. AI khai phần tên/môi trường thiếu và receipt phân biệt verified với self_declared. Không cấp thêm quyền A2.
- Việc gì: task_id + command_ref lấy từ assignment/lệnh đã có; cấu hình nhãn một lần ở caller, mỗi lệnh ghi tự đính kèm; không thêm quản lý phiên tại server. operation_id để chống ghi trùng, không thay command_ref khi không có chứng cứ.
- Ghi gì: tool/method, đích/path, nội dung hoặc content hash/commit do thao tác có sẵn cung cấp; dùng receipt/log hiện hữu, không ghi lộ secret/nội dung nhạy cảm.
- P458 vẫn yêu cầu đủ 4 dữ liệu logic sản phẩm AI · môi trường AI Cloud/MacBook/VPS · task · mã lệnh trong dấu vết. Tự lấy tối đa thông tin có chứng cứ, chỉ đòi bổ sung trường không biết. KHÔNG bắt AI nhập 4 ô mỗi lượt, KHÔNG suy môi trường AI từ VPS gateway.
- Đọc không phải khai. Không mở rộng sang SQL/PG, Directus Flow/cron/Graph; đường vòng không qua Gateway = UNKNOWN, không nhận đã bảo vệ.

## 2. Một RUN, hai đầu ra; ưu tiên dùng lại
**A. Ghi danh tối giản**
1) Dựa vào bảng writer P491: với hai họ Gateway hiện có, xác nhận auth thực tế + nơi gắn task/command + receipt hiện có. Phân nhóm AUTH_UNIQUE (đủ bằng chứng ai là AI), AUTH_SHARED (chỉ biết credential, phải khai phần thiếu), BYPASS/UNKNOWN (đường không qua cổng). Dẫn đường code, credential profile và nguồn chứng cứ; không giả định mọi credential là độc lập. Không lập lại toàn bộ inventory SQL/VPS.
2) Nếu đã đủ tính năng => 0 dòng code. Nếu còn thiếu 1 mắt xích => sửa nhỏ nhất trong adapter/cấu hình hiện có, trên ứng viên DEV, không mở Gateway mới, không sửa lõi từng handler, Docker, pg_store, SQLite, Graph, CI workflow, production. PR358 20 tệp chỉ là mã tham khảo, KHÔNG phải gói phải merge/deploy. Nếu muốn làm mà bắt buộc đụng lõi hoặc phát hành toàn AD, KQ=NEEDS_OWNER_CHOICE nêu rõ chỗ nghẽn, không chạy hướng nặng.
3) Chứng minh trên phạm vi được phép: 1 lệnh ghi hợp lệ có receipt authenticated principal + bốn facts (verified/self_declared minh bạch) + task/command + đích/hash; 1 lệnh shared thiếu nhãn cần khai bị từ chối trước ghi và có chỉ dẫn; đọc không bị yêu cầu khai; retry không ghi đôi. Nếu chỉ test fixture/local thì ghi SOURCE_TESTED, không gọi LIVE_PASS. Nếu cần chạm VPS1/production phải có Owner GO riêng; không diễn tập release trong RUN này.

**B. Thu gọn rác của RUN12–25**
1) Tận dụng manifest, evidence, PR đã có; khảo sát đúng các mục đã biết: PR358/357/360 và nhánh liên quan, evidence RUN12–25, candidate code/test/overlay/image, scratch/venv/lab Mac/VPS nếu có nguồn READ; không SSH/quét cả máy. PR357 liên quan VPSC2, PR360 đã merge: không mặc nhiên coi rác HJW.
2) Lập MỘT bảng: đường dẫn/ID · owner/consumer · đang dùng hay không · dung lượng đo được (không bịa) · GIỮ / ĐỀ XUẤT LOẠI / CHỜ OWNER DUYỆT. GIỮ mã/test hữu ích và bằng chứng SSOT. Các module/ticket/alias/guard thừa chỉ đề xuất bỏ khỏi phương án G8; không rewrite Git history, không đóng PR, không xóa branch/evidence/image/data cũ khi Owner chưa duyệt danh sách cụ thể. Đồ nặng độc nhất chỉ đề xuất backup Drive+hash/khôi phục trước xóa khi Owner cho phép; Git đã lưu mã không backup trùng không cần thiết. Không đụng Docker.raw 44 GB, base image đang chạy hay dữ liệu khác task.
3) Tự dọn scratch/cache CHỈ do chính RUN mới tạo khi chắc không chứa dữ liệu người dùng. Rút ngay khỏi roadmap/DoD ghi-danh các việc không liên quan: Docker/image rollback/queue4/Graph/RAM/7 continuation tests/GH→VPS1 full release. Không xóa lịch sử hoặc kết quả cần dự án khác.

## 3. Nghiệm thu và rào an toàn
Một KQ + Bảng + một evidence INDEX đủ 2 bản đồ: (i) Gateway AUTH_UNIQUE/SHARED/UNKNOWN, ca ghi hợp lệ và từ chối, số tệp sửa thực (0 nếu đủ); (ii) bảng rác theo trạng thái và yêu cầu Owner duyệt. Chỉ kết luận DONE_SCOPED khi có bằng chứng trên cổng thật được phép; ngoài cổng = UNKNOWN. Nếu vướng, ghi 1 nguyên nhân chính, không mở chuỗi RUN mới.
CẤM: tự merge/close PR, xóa artefact cũ, deploy GH→VPS1/VPS2, chỉnh VPS/PG/Directus/GSM/nginx/Guard, tạo token/permission/service/Gateway/ticket-system, rebuild AD, thay đổi task khác, mở workflow mới. Nếu cần quyền ghi/cleanup chưa được phê duyệt => giữ nguyên, đưa vào bảng Owner.

## 4. Gate DUY NHẤT trước chạy
Claude Chat REVIEW 1 vòng đúng 3 câu: (1) còn kiến trúc/việc thừa nào cắt được? (2) có bỏ sót 4 facts P458 hoặc nhầm principal xác thực với tên AI tự khai không? (3) việc dọn có nguy cơ xóa tài sản của task khác/PR357/PR360 không?
Trả ACCEPT hoặc FIX_TỐI_ĐA_3_ĐIỂM, viện dẫn đúng dòng cần vá. Không đề xuất ticket/gateway/quy trình mới. GPT Host xử lý một lần rồi ký READY@last-touch PROMPT commit; không tự ký trước REVIEW. Chỉ Owner chuyển lệnh sau READY; executor không tự STARTED từ DRAFT.
