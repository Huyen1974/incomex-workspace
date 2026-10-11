# PROMPT — HJW N3 · KHÓA OPENROUTER RIÊNG + PHIÊN HERMES DESKTOP LOCAL
RUN_ID: HJW-N3-MAC-KEY-20261012-01
STATUS: DRAFT_HOST_P292 · CHƯA REVIEW/READY/RUN
Host: GPT Chat; Reviewer: Claude Chat (phiên độc lập với Claude Code worker P291; một review exact SHA theo A6/DROOT53)
Executor_Surface: Claude Code CLI trên MacBook Owner, Owner tự dán câu DROOT38(c) khi Host READY
Write_Path: Mac local; báo KQ qua Incomex workspace_* CAS vào HJW COLLAB, không ghi VPS
Node: N3/K3 tiếp tục, không tạo task mới.

## 0. MỤC TIÊU VÀ NHỮNG GÌ ĐÃ XONG
Owner cần một Hermes Desktop làm Remote màn hình cho Hermes VPS đang chạy và một Hermes Local độc lập trên MacBook dùng OpenRouter API **khóa riêng**. Sau MAC_PASS mới tới Hermes Mac nhắc GPT/Claude một câu vào repo (T9), N4–N6 như roadmap. Không tự động gọi API vào tài khoản thuê bao GPT/Claude.
P291: Local CLI trả PONG, Local backend hoạt động, Remote VPS qua tunnel 3/3 PASS, launcher Hermes Mac đã sửa, rollback có sẵn. UPDATE_PREVIEW_PASS qua hermes-sync, UPDATE_LIVE=NOT_RUN. **MAC_NOT_PASS** duy nhất do Mac dùng chung key với VPS và thiếu phiên Desktop "This device" xác thực. KHÔNG cài lại hoặc làm lại phần đã PASS.
**Owner đã cung cấp tệp chứa key mới trên Mac:** `$HOME/Desktop/it/openrouter_key_for_hermes_macbook.txt` (Mac user /Users/nmhuyen). Chỉ dùng key này cho Local Mac; nếu đã có key hợp lệ trong tệp thì KHÔNG gọi OpenRouter tạo key khác. Tuyệt đối không đưa nội dung key ra GPT/Claude context, chat, terminal output, repo, log, VPS, Drive hoặc shell arguments.

## 1. CỔNG AN TOÀN — CHỈ MAC-ONLY, GRAPH ĐƯỢC CHẠY SONG SONG
- Đọc AGENTS A0/A6/A9/A10, root COLLAB, HJW A0/Bảng/P289–P292 và PROMPT này. P291 đã terminal DỪNG, nhả busy; kiểm không STOP/alert/STARTED trùng. Một RUN nhỏ; không cần lặp lại audit 02/10.
- Mac tree `~/.hermes/hermes-agent` và hook mac-lock giữ nguyên SHA VPS `749220ef`; không checkout/merge/reset hay thêm upstream vào tree đó (INV14 Guard của Graph). Trên VPS chỉ được đọc/status nếu thật sự cần; KHÔNG `hermes-safe-update check/health/apply`, update, restart, SSH write hay change service. Không đụng Graph/VPSC.
- Không bấm Update/Update all instances trên Hermes Desktop; không tải/chạy bản v0.21.6 hay sửa hermes-sync. Model Local mặc định hiện đang là Opus đắt: không thay mặc định không xin phép; lần xác minh dùng model rẻ từng thử P291 với một prompt ngắn và giới hạn token hợp lệ.

## 2. THỰC HIỆN (MỘT LƯỢT / MỘT KQ)
| Bước | Người thực hiện / trigger | Bằng chứng | Lỗi thì làm gì |
|---|---|---|---|
| 1. Nguồn key | Claude Code sau Owner paste READY | Kiểm file cục bộ là regular file; quyền chỉ Owner; nội dung đọc **trong process kín**, không in/echo/cat, không đưa key thành đối số, không `set -x`; chấp nhận raw token hoặc dòng `OPENROUTER_API_KEY=...`, không source/exec nội dung tệp | Tệp rỗng/sai/mất ⇒ một hành động Owner, KQ DỪNG; không dùng lại key VPS |
| 2. Cấu hình Local | Claude Code | Sao lưu cấu hình Mac riêng với mode 0600; cập nhật **đúng** OpenRouter credential Local hiện hữu (ví dụ `~/.hermes/.env` nếu đúng backend), ghi atomically mode 0600, giữ nguyên các trường khác; không động credential Remote hay VPS. Kiểm boolean key mới khác key Mac cũ P291; không in một phần/hash/key | Khác key chưa chứng minh được ⇒ DỪNG/rollback |
| 3. Xác thực | Claude Code | Một request OpenRouter `GET /api/v1/key` từ local process kín trả HTTP 200 + có limit/budget hợp lệ, không log response chi tiết; một Local test PONG chi phí thấp với key vừa thay, tối đa một lần. Không dùng model Opus mặc định cho canary | 401/402/limit hết/chưa đặt hạn mức ⇒ hướng dẫn Owner đúng một lần; DỪNG sạch |
| 4. Bằng chứng Desktop | Claude Code hướng dẫn Owner 1 lượt | Owner mở Hermes Desktop, chuyển thật sang **This device**, mở phiên mới gửi `LOCAL_MAC_PONG`; Claude xác minh local backend log/state DB có **phiên Desktop mới** và lastUsed Local, không chỉ tin câu “đã xong”. Sau đó quay về Remote `127.0.0.1:9119`, lịch sử VPS còn, key Remote không đổi. Không buộc Owner dán key bằng tay nữa | Thiếu session/không đúng connection ⇒ MAC_NOT_PASS, mô tả chính xác một blocker |
| 5. Kết thúc | Claude Code | KQ XONG/DỪNG và 1 P ngắn tại HJW COLLAB, cập nhật Bảng: LOCAL_KEY_DISTINCT, LOCAL_AUTH, DESKTOP_LOCAL_SESSION, REMOTE_VPS, MAC_PASS; `UPDATE_PREVIEW_PASS=P291`, `UPDATE_LIVE=NOT_RUN`; file/path đổi (không secret), rollback, 0 VPS writes, release busy; đúng một NEXT_TRIGGER | Không đủ bằng chứng không giả PASS |

## 3. TIÊU CHÍ VÀ RANH GIỚI
**MAC_PASS** chỉ khi khóa Local thực sự riêng và hợp lệ, Local Desktop có phiên mới chạy bằng khóa đó, Remote VPS vẫn dùng được và không thay đổi; Local tắt không ảnh hưởng VPS. PONG CLI từ P291 không thay Desktop proof.
Tệp khóa gốc trên Desktop không tự xóa, không tự upload/copy đi đâu. Nếu cần Owner tạo key qua website do tệp không có key hợp lệ thì một việc cho Owner, không tự tạo API credentials trên tài khoản.
Không mở RUN nâng cấp VPS trong lượt này. Theo release hãng 08/10, v0.21.6 commit `818c13be...` là candidate cho Docker/Cloud, Desktop bundled **chưa nâng trong cùng đợt**, schema/compat chưa nghiệm thu ⇒ **chưa APPROVE TARGET_SHA**. Bước update đồng bộ tiếp tục trong N3 sau khi đủ Guard/#11/Graph slot/rollback; sau MAC_PASS mới courier nhắc GPT/Claude và T9, rồi N4–N6.
