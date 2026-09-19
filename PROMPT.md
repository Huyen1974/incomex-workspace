# PROMPT — R03 · Hoàn tất vòng đời tệp cho hai đầu nối (không đổi schema)

RUN_ID: R03-FILE-LIFECYCLE-20260919-01
Soạn: Claude Chat. Trạng thái KHÔNG ghi ở file này: chỉ tin `READY@<full-sha>` trong COLLAB.md.
Chỉ chạy khi: COLLAB P12 có Host ACCEPTED (D09–D11) + `REVIEWED@` của Founder không soạn + `READY@` đúng commit cuối chạm file này + lệnh RUN hợp lệ.

## 0. Trước khi làm
1. Kiểm READY trên bản sao riêng dưới /tmp (git clone repo công khai), so đủ 40 ký tự; lệch → DỪNG.
2. Đọc AGENTS.md, COLLAB.md (R03, P12, D09–D11) và KB §13.11 (báo cáo 15:20 nguyên văn + đính chính).
3. Áp PL1–PL3 của P10 theo đính chính 7159559: không fetch/pull/checkout/commit trên 2 clone làm việc; repo mã VPS commit cục bộ theo path, không push/force-push; chỉ restart 4 dịch vụ của PL2 với đúng điều kiện; hỏng → quay về tag rollback.
4. Mỗi việc: test đỏ trước, sửa, test xanh.

## 1. Phạm vi cố định (không mở rộng ngoài 29 năng lực; không mở bề mặt HTTP mới)
Schema/tool chỉ được đổi nếu thực sự cần để đóng #7 (so hai phiên bản), #9 (sửa mọi chỗ khớp), #14/#20 (khoá cây cho move, cả gốc ui) và #28 RESTORE; nếu đổi phải gộp toàn bộ trong **một lần cuối**, báo đủ tool/schema/metadata diff và `CLIENT_REFRESH_REQUIRED=YES`. Không đổi vì lý do khác.
GPT (đã code + test, chưa deploy — §13.11): G1, G2 (+G8 tree token), G3, G4, G7, G11/G15. Làm thêm:
- D09 chặn sinh đôi NFC (xem dưới).
- G5 guarded replace cho upload/import nếu làm được bằng backend; cần đổi schema → ghi BLOCKED + lý do, không đổi.
- G6 kiểm resume sau restart (test, không restart production).
Claude (claude-mcp/app/fsroots.py + helper):
- C3 fs_copy nhận thư mục: đệ quy, đích chưa tồn tại, all-or-nothing, 1 commit, không theo symlink, quét bí mật từng tệp như copy tệp, có trần số tệp/dung lượng; op `copy` trong fs_transaction cũng nhận thư mục.
- C4/C8 fs_stat(thư mục) trả tree token xác định (Git tree SHA hoặc tương đương), đổi khi bất kỳ tệp con đổi; fs_copy và op transaction nhận token làm expected_version; fs_move trên gh dùng expected_head; gốc ui: fs_move nhận tree token (expected_version) trong cùng đợt đổi schema duy nhất.
- C7 copy/move thư mục vào chính con/cha của nó → reject trước khi đổi gì.
- C11/C15 sau move/transaction/rollback: prune thư mục rỗng trong phạm vi thao tác, xoá cha tự sinh khi rollback; fs_list chỉ hiện cái Git có. Thư mục ma hiện có `_thu-nghiem/audit-claude-20260919/a/b/c` phải biến mất nhờ chính cơ chế mới, không dọn tay.
- C16 fs_write thay tệp đã tồn tại ở mọi kích thước, mọi gốc ghi → bắt buộc expected_version; lỗi chỉ cách lấy version. Tạo mới giữ nguyên.
D09 (cả hai phía): không đổi byte, không rename tên có sẵn; tạo tên mới mà NFC trùng tên đã có khác byte → reject, chỉ ra tên có sẵn; đọc/stat theo byte, không có thì tra tương đương NFC duy nhất.
N/A theo quyết định (ghi rõ trong ma trận, không để trống): C1, C6, C13, G13 (D10); C2 và phần gh-binary của G9/C9 (D11) — G9/C9 thu về "SHA binary giữ nguyên trên ui"; C10 không có bề mặt mới nhưng C3 phải qua secret scan; G16 không tồn tại (C16 chỉ phía Claude); C5 = C16 phía Claude; G12/C12 = mục 4.

## 2. Cổng năng lực chuẩn — 29 dòng, điều kiện trước deploy
Đây là danh mục **cố định theo nhu cầu người dùng**, không sinh từ lỗi đang gặp. Một bảng `# | Năng lực | GPT | Claude | Bằng chứng | PASS/FAIL/N/A(Dxx)` phải có đủ 29 dòng dưới đây, không ô trống. Còn FAIL (trừ N/A có Dxx) → không deploy.

1. LIST/ROOT DISCOVERY — gọi không root phải thấy toàn bộ root + writable/read-only/mode; list path có pagination + Unicode; root không được cấp quyền phải reject.
2. READ/TEXT FIDELITY — cửa sổ nhỏ, dòng rất dài, tệp text vài MB; bảo toàn UTF-8 BOM nếu có, CRLF/LF và trailing spaces, không tự normalize newline.
3. SEARCH — literal + regex + context/pagination.
4. STAT FILE — bytes/hash/version/head/freshness.
5. STAT DIRECTORY — deterministic tree token; descendant đổi → token đổi.
6. LOG — lịch sử fresh, không bỏ commit mới; lọc theo path và đi theo tệp khi dời/đổi tên (follow), cả hai phía.
7. DIFF — đúng path/version và fresh; THÊM so một path giữa hai phiên bản bất kỳ (from=commit/version, to=commit hoặc HEAD) ở server, có phân trang, không relay cả tệp. Đây là thao tác Reviewer dùng hằng ngày (AGENTS A3: đọc thay đổi từ Based_on tới HEAD); hiện Claude chỉ xem từng commit, GPT chỉ so từ bản sao lưu sau sửa.
8. CREATE — tạo tệp ở nested path khi mọi parent chưa tồn tại; rollback dọn parent tự sinh.
9. EDIT — expected_version bắt buộc khi thay tệp; giữ byte ngoài vùng sửa, BOM/CRLF/LF/trailing spaces; warning không biến thành block sai. THÊM sửa mọi chỗ khớp (replace_all) trả về số chỗ đã thay và từ chối nếu khác expected_count khi có truyền; cả hai phía (đổi một thuật ngữ trong HTML lớn).
10. GUARDED REPLACE — thay toàn bộ tệp hiện hữu bằng expected_version, cả tệp nhỏ và HTML lớn; stale → reject, bản cũ nguyên; fidelity của bytes text theo #2.
11. COPY FILE — nested destination, no overwrite, version/head guard, one commit.
12. COPY DIRECTORY — recursive, one commit, no overlap, no symlink-follow, secret/policy scan từng tệp, cap file-count + total-bytes.
13. MOVE FILE — nested destination, no overwrite, guard, source/dest đúng sau commit.
14. MOVE DIRECTORY — recursive, one commit, overlap/self-descendant reject, guard, prune thư mục rỗng do thao tác tạo ra.
15. TRANSACTION FILE+TREE — create/edit + copy/move file + copy/move directory; validate trước, đúng 1 commit, all-or-nothing; chỉ stage đúng file của thao tác, không cuốn file bẩn/không liên quan.
16. DELETE — N/A theo luật Owner; connector không có delete, dùng move lưu trữ.
17. IMPORT ATTACHMENT — GPT import_file: request identity/idempotency, guarded create/replace, backend fixture UTF-8 HTML 2–3 MB; Claude direct sandbox import = N/A(D10).
18. LARGE/RESUMABLE UPLOAD — GPT begin/append/status/commit: chunk retry, lost response begin/commit, resume sau process/service-test restart, expiry/GC bằng TTL test; Claude direct upload = N/A(D10).
19. EXPORT/DOWNLOAD — N/A(D10) trong R03; không mở HTTP surface mới.
20. CONCURRENCY/LOCK — expected_head/version/tree-token; client khác sửa descendant → stale token reject, không mất thay đổi.
21. IDEMPOTENCY/LOST RESPONSE — mọi mutation liên quan write/edit/import/upload/copy/move/transaction: same request replay; same id khác payload reject; không duplicate commit/job/write.
22. FAILURE/RECOVERY HYGIENE — push/conflict/failure rollback sạch; không ghost parent, temp, orphan session; session hết hạn được GC.
23. DANGEROUS PATHS — `..`, absolute path, symlink escape, `.git/**` và state/temp nội bộ của connector bị chặn; destination tồn tại không overwrite.
24. UNICODE/NFC/PORTABILITY — giữ byte tên hiện hữu; D09 chặn tên mới NFC-equivalent khác byte; tên/path tiếng Việt thật PASS. Test thêm case-only collision (`A`/`a`): phải có chính sách rõ PASS hoặc BY-DESIGN, không để hành vi ngầm gây lỗi khi clone sang Mac.
25. POLICY/GIT SAFETY — gh chỉ UTF-8 text/HTML theo D11; binary gh N/A; secret scan không bị bypass; caps cỡ/path-segment/tổng tài nguyên rõ; main chỉ fast-forward, không force-push, không stage file ngoài thao tác. Đường ghi thứ ba (GitHub native của ChatGPT: không khoá, không quét bí mật) phải là CHỈ ĐỌC với repo này (D12) — Agent kiểm và ghi rõ cách Owner đặt quyền, không tự đổi. Text không phải UTF-8 (UTF-16/Windows-1258 xuất từ Excel) → từ chối rõ ràng, không thành chữ lỗi.
26. FRESHNESS/CROSS-CLIENT — GPT↔Claude thấy commit/path mới ngay; sửa chéo làm stale guard hoạt động đúng; không cần chạy lại toàn K1–K10.
27. CLIENT BINDING CONTRACT — chat thật thấy đúng tool count + input schema/required fields + description/annotations/fingerprint/build-id cần thiết. Báo riêng `TOOL_LIST_CHANGED`, `TOOL_INPUT_SCHEMA_CHANGED`, `TOOL_METADATA_CHANGED`; description/annotations đổi cũng tính là metadata đổi. Bất kỳ YES → `CLIENT_REFRESH_REQUIRED=YES` và client smoke chỉ sau đúng một refresh/recreate cuối cùng.
28. HISTORICAL READ / SAFE RESTORE — phải lấy được một tệp text/HTML ở commit/version cũ và khôi phục **tệp hiện hữu** về bản đó bằng một forward commit mới, có expected current head/version, không reset/force, không relay tệp lớn qua model. Không được dùng restore để xoá tệp mới (quyền delete vẫn N/A). THÊM: đích là path chưa tồn tại → tạo lại (create-only) để lấy lại tệp đã dời/đổi tên; restore dùng được như op trong transaction để hoàn tác nhiều tệp của một lần sửa bằng đúng 1 forward commit. Cả GPT và Claude phải PASS; nếu cần đổi schema/tool thì dùng quyền đổi-một-lần của mục 1.
29. OWNER-VIEW PUBLISH BOUNDARY — hiện connector không có cross-root copy `workspace/gh → ui`; ghi **N/A(R04/D08)** trong R03, không coi PASS giả. R04 Owner View phải cung cấp đường server-side pull/copy đúng một HTML chính từ GitHub SSOT sang `ui` mirror, kiểm hash/size và không relay 2–3 MB qua model.

Ma trận G1–G16/C1–C16 của §13.11 vẫn phải xuất đầy đủ như evidence chi tiết; G16=N/A, không bỏ hàng. 29 dòng trên là **cổng cấp người dùng** để không còn phát hiện thiếu theo từng việc.
Số thứ tự 29 dòng ở đây là SỐ CHUẨN; DANH-MUC-CONG-CU.md §2 dùng đúng số này và là nơi lưu lâu dài (PROMPT.md sẽ bị ghi đè ở việc sau).

Các tool KB/UI/exec/task không đổi trong R03: không thêm dòng capability mới, nhưng full `run_acceptance.py` phải xác nhận không regression và tool count/build/fingerprint đúng.

## 3. Deploy — một lần cho cả hai
Chỉ khi 29/29 dòng PASS hoặc N/A có Dxx/Rxx và G1–G16/C1–C16 không còn FAIL: gắn tag rollback cho image đang chạy mỗi bên; deploy agent-data + claude-mcp (+ helper nếu đổi); healthy trong 2 phút, không thì hoàn nguyên và DỪNG. Chạy lại `run_acceptance.py` hai bên → PASS. Không deploy lần hai trong R03 ngoài rollback.

## 4. Client + cross smoke — R03 chưa đóng nếu chưa qua
Agent chỉ hoàn tất **tầng máy**, không được tự tuyên bố R03 CLOSED.
- Claude Code/Agent: smoke public/backend route mà nó thực sự điều khiển được; không gọi đó là Claude Chat PASS.
- Claude Chat thật sau deploy/reconnect: copy dir 2 cấp = 1 commit; stat dir lấy token, sửa descendant rồi dùng token cũ → reject; ghi đè không version → reject; NFD collision → reject; move không ghost.
- GPT Chat thật ở chat mới dùng Full All: nested create; recursive dir copy; stale tree-token reject; NFD collision reject; gọi `workspace_import_file` thật từ một attachment. Backend phải chứng minh HTML 2–3 MB; client ít nhất chứng minh attachment bind/call thật.
- CROSS: GPT tạo nested tree → Claude cold-read thấy ngay; Claude sửa descendant → GPT dùng tree-token cũ reject; Claude move tree → GPT stat thấy path mới.
- Nếu `CLIENT_REFRESH_REQUIRED=YES`, chỉ nghiệm thu sau một lần refresh/recreate cuối cùng GPT plugin + reconnect Claude; ghi tool count/build/fingerprint và metadata mới.

## 5. Báo cáo — bắt buộc TRƯỚC khi trả lời Owner
Ghi nối tiếp KB §13.11: ma trận G1–G16/C1–C16, bảng 29 năng lực, deploy, flags client-contract, smoke mà Agent thực sự làm được. Chưa ghi KB thì không trả Owner.
Agent chỉ trả một dòng: `R03-FILE-LIFECYCLE-20260919-01: MACHINE_DONE — client/cross còn mục 4 · KB §13.11` hoặc `...: DỪNG ở <ID/#> — lý do ở KB §13.11`. Chỉ Host sau client/cross thật mới được ghi R03 CLOSED.

## 6. Cấm / BY-DESIGN
Không tự đổi schema/tên tool, không thêm tool, không mở route/nginx mới; không connector-delete/host-shell/chmod/symlink-creation; không sửa AGENTS/README/COLLAB/PROMPT; không xoá dữ liệu/nhánh/image; không dọn repo trong R03. Git không lưu empty directory nên mkdir rỗng không phải capability; nested create phải tự tạo parent. Binary gh, Claude direct attachment và export HTTP là N/A theo D10/D11, không phải lỗi bị bỏ quên. Gặp gì ngoài dự kiến → DỪNG, ghi KB.
