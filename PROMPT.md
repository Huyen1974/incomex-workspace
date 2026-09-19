# PROMPT — R03 · Hoàn tất vòng đời tệp cho hai đầu nối (không đổi schema)

RUN_ID: R03-FILE-LIFECYCLE-20260919-01
Soạn: Claude Chat. Trạng thái KHÔNG ghi ở file này: chỉ tin `READY@<full-sha>` trong COLLAB.md.
Chỉ chạy khi: COLLAB P12 có Host ACCEPTED (D09–D11) + `REVIEWED@` của Founder không soạn + `READY@` đúng commit cuối chạm file này + lệnh RUN hợp lệ.

## 0. Trước khi làm
1. Kiểm READY trên bản sao riêng dưới /tmp (git clone repo công khai), so đủ 40 ký tự; lệch → DỪNG.
2. Đọc AGENTS.md, COLLAB.md (R03, P12, D09–D11) và KB §13.11 (báo cáo 15:20 nguyên văn + đính chính).
3. Áp PL1–PL3 của P10 theo đính chính 7159559: không fetch/pull/checkout/commit trên 2 clone làm việc; repo mã VPS commit cục bộ theo path, không push/force-push; chỉ restart 4 dịch vụ của PL2 với đúng điều kiện; hỏng → quay về tag rollback.
4. Mỗi việc: test đỏ trước, sửa, test xanh.

## 1. Phạm vi cố định (không mở rộng, không đổi schema, không thêm tool, không mở bề mặt HTTP mới)
GPT (đã code + test, chưa deploy — §13.11): G1, G2 (+G8 tree token), G3, G4, G7, G11/G15. Làm thêm:
- D09 chặn sinh đôi NFC (xem dưới).
- G5 guarded replace cho upload/import nếu làm được bằng backend; cần đổi schema → ghi BLOCKED + lý do, không đổi.
- G6 kiểm resume sau restart (test, không restart production).
Claude (claude-mcp/app/fsroots.py + helper):
- C3 fs_copy nhận thư mục: đệ quy, đích chưa tồn tại, all-or-nothing, 1 commit, không theo symlink, quét bí mật từng tệp như copy tệp, có trần số tệp/dung lượng; op `copy` trong fs_transaction cũng nhận thư mục.
- C4/C8 fs_stat(thư mục) trả tree token xác định (Git tree SHA hoặc tương đương), đổi khi bất kỳ tệp con đổi; fs_copy và op transaction nhận token làm expected_version; fs_move trên gh dùng expected_head; gốc ui ghi nợ.
- C7 copy/move thư mục vào chính con/cha của nó → reject trước khi đổi gì.
- C11/C15 sau move/transaction/rollback: prune thư mục rỗng trong phạm vi thao tác, xoá cha tự sinh khi rollback; fs_list chỉ hiện cái Git có. Thư mục ma hiện có `_thu-nghiem/audit-claude-20260919/a/b/c` phải biến mất nhờ chính cơ chế mới, không dọn tay.
- C16 fs_write thay tệp đã tồn tại ở mọi kích thước, mọi gốc ghi → bắt buộc expected_version; lỗi chỉ cách lấy version. Tạo mới giữ nguyên.
D09 (cả hai phía): không đổi byte, không rename tên có sẵn; tạo tên mới mà NFC trùng tên đã có khác byte → reject, chỉ ra tên có sẵn; đọc/stat theo byte, không có thì tra tương đương NFC duy nhất.
N/A theo quyết định (ghi rõ trong ma trận, không để trống): C1, C6, C13, G13 (D10); C2 và phần gh-binary của G9/C9 (D11) — G9/C9 thu về "SHA binary giữ nguyên trên ui"; C10 không có bề mặt mới nhưng C3 phải qua secret scan; G16 không tồn tại (C16 chỉ phía Claude); C5 = C16 phía Claude; G12/C12 = mục 4.

## 2. Ma trận — điều kiện trước deploy
Một bảng duy nhất `ID | GPT | CLAUDE | TEST (tên test hoặc commit) | PASS/FAIL/N/A(Dxx)` cho G1–G15 và C1–C16. Không ô trống. Còn FAIL (trừ N/A có Dxx) → không deploy.

## 3. Deploy — một lần cho cả hai
Gắn tag rollback cho image đang chạy mỗi bên; deploy agent-data + claude-mcp (+ helper nếu đổi); healthy trong 2 phút, không thì hoàn nguyên và DỪNG. Chạy lại `run_acceptance.py` hai bên → PASS.

## 4. Client smoke
Claude (Agent gọi đầu nối Claude qua đường thật, tệp thử trong `_thu-nghiem/r03/`): copy thư mục 2 cấp = 1 commit; stat thư mục lấy token, sửa 1 tệp con, copy bằng token cũ → reject; ghi đè không version → reject; tên NFD trùng → reject; move tệp không để thư mục ma.
GPT: liệt kê đúng các ca GPT Chat phải tự chạy (tạo a/b/c/file, copy thư mục, token cũ reject, NFD trùng reject) và để PENDING.

## 5. Báo cáo — bắt buộc TRƯỚC khi trả lời Owner
Ghi nối tiếp vào KB §13.11: ma trận mục 2, kết quả deploy, smoke. Chưa ghi KB thì không được trả lời Owner. Trả Owner đúng một dòng: `R03-FILE-LIFECYCLE-20260919-01: XONG — KB §13.11` hoặc `R03-FILE-LIFECYCLE-20260919-01: DỪNG ở <ID> — lý do ở KB §13.11`.

## 6. Cấm
Không đổi schema/tên tool, không thêm tool, không mở route/nginx mới; không delete/shell/chmod/symlink; không sửa AGENTS/README/COLLAB/PROMPT; không xoá dữ liệu/nhánh/image; không dọn repo (việc sau). Gặp gì ngoài dự kiến → DỪNG, ghi KB.
