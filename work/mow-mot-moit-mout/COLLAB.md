# COLLAB — mow-mot-moit-mout

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
- Mục tiêu: tiếp tục hồ sơ MOW · MOT · MOIT · MOUT từ đúng file gốc Owner đang làm và xây kho thông tin liên quan có tổ chức để phục vụ rà soát/phát triển tiếp.
- Nhiệm vụ/phạm vi hiện tại (Owner giao lại 23/09/2026): đưa các tài liệu có giá trị trong `/Users/nmhuyen/Desktop/quy trình` lên `information/` làm kho THAM KHẢO cho dự án dài hạn và hội đồng AI; ưu tiên nguyên bản `cấu trúc hệ thống.html` và `BAN-DO-BUOC-UI-AGENT.html`. Các thiết kế cũ đang làm lại, không coi là chuẩn hiện hành. Giữ nguyên nguồn Mac và HTML chính.
- Tiêu chí xong của lượt hiện tại: tài liệu liên quan được copy có kiểm hash/mục lục, nguồn Mac không bị xoá/di chuyển, file gốc không bị sửa.
- Xác nhận User: **ĐÃ XÁC NHẬN** — Owner giao trực tiếp 2026-09-20 và yêu cầu đưa kho tham khảo lên GitHub ngày 2026-09-23; D01–D05, D12 của việc này.

Host: GPT Chat · Host_ID: GPT-MMIM-260920-A · Owner giao: 2026-09-20
HTML chính: `mow-mot-moit-mout.html`
File gốc Owner giao: `mow-mot-moit-mout.html` · SHA-256 `f4aac30c492f104ec54ff7a03ace54ce70d802e2dd49a417ad9b7285897a050c` · import nguyên byte ở commit `569bb74300a15d05e455bf917fe4058f7f7fd499`.
Kho thông tin: `information/`
Agent prompt: `PROMPT.md`

## Dòng hiện hành
MMIM | REFERENCE_TEXT_PUBLISHED · BINARY_WRITE_PATH_PENDING · 23/09/2026 | Đã đưa 888 tài liệu/87.874.934 bytes lên GitHub; nguồn–đích SHA PASS. Còn 304 ảnh/Excel/Word/46.090.145 bytes đã chuẩn bị, chờ đường ghi được phép. Xem information/README.md.

## Quyết định Owner
- D01 · 2026-09-20 · Mở công việc tại `work/mow-mot-moit-mout/`.
- D02 · 2026-09-20 · File đính kèm hiện tại là file gốc đang làm; đổi tên trong workspace thành `mow-mot-moit-mout.html`.
- D03 · 2026-09-20 · Phải đưa file gốc lên workspace trước rồi mới viết prompt/giao Codex phần còn lại.
- D04 · 2026-09-20 · Codex tạo `work/mow-mot-moit-mout/information/`, tự đề xuất cách tổ chức bên trong và đưa các file cần thiết/liên quan từ `/Users/nmhuyen/Desktop/quy trình` vào đó.
- D05 · 2026-09-20 · Lượt Codex này chỉ khảo sát, phân loại và copy tài liệu; không được sửa, đổi tên hoặc tái cấu trúc `mow-mot-moit-mout.html`, không xoá/di chuyển nguồn trên Mac.
- D06 · 2026-09-20 · `work/mow-mot-moit-mout/mow-mot-moit-mout.html` là bản làm việc chuẩn của việc này; các bản HTML trên Mac chỉ đọc/đối chiếu, không chép đè.
- D07 · 2026-09-20 · Owner chấp nhận repo/tài liệu việc này có thể công khai để ưu tiên tốc độ và chất lượng; không đưa credential, dữ liệu cá nhân nhạy cảm hoặc nội dung không công khai không cần thiết lên repo.
- D09 · 2026-09-21 · Áp dụng DROOT04 cho MMIM.2: Host không tách PRECHECK riêng cho môi trường Codex đã dùng nhiều lần; RUN phải bắt đầu bằng việc vào đúng repo `incomex-workspace`, cập nhật `main` an toàn và đọc AGENTS → COLLAB → PROMPT. Chỉ mutation sau khi gate đầu vào của chính MMIM.2 PASS.
- D10 · 2026-09-21 · Owner yêu cầu Host sửa gói cuối, sau đó chuyển Claude review để đạt đồng thuận; **chưa READY/RUN Codex trước review Claude**.
- D11 · 2026-09-21 · Theo Owner: MMIM.2 dùng **Executor_Surface = Codex**. Quyền kỹ thuật theo capability đã audit, không theo hãng. `Write_Path` ưu tiên `workspace_*`; nếu chính phiên Codex không bind `workspace_*` nhưng bind `fs_*` đã audit thì dùng `fs_*`. Không dùng Git/CLI/native để ghi. Host giám sát qua gate + repo/diff/report cuối.

- D12 · 2026-09-23 · Owner trực tiếp yêu cầu đưa các file có giá trị từ Mac lên GitHub thành kho tham khảo dài hạn; đặc biệt hai HTML thiết kế nêu trên. Thực hiện yêu cầu mới bằng `workspace_*` đã đọc-gate PASS; không chạy PROMPT MMIM.2 nháp, không tự chốt P01. Không đưa credential/dữ liệu nhạy cảm lên public. Hai HTML lớn truyền bằng mã giữa công cụ, không tái tạo nội dung qua mô hình. · Áp: SAME_COMMIT.

## Kế hoạch
- MMIM.1 | Tạo work + import file gốc, đổi tên thống nhất | ✅ `569bb74300a15d05e455bf917fe4058f7f7fd499`
- MMIM.2 | Codex khảo sát thư mục nguồn, copy text/lightweight + inventory binary + lập mục lục | ◐ DRAFT · chờ Claude review

## Ý kiến (P)
Reviewer: Claude Chat · Based_on `39cc96d` / commit review `f5f97fc`. Host GPT đã đối chiếu lại HTML chính và README §12 trước khi xử lý.

- P01 · Scope COLLAB §0 · **REJECTED trong lượt này** · Claude đề nghị mở rộng mục tiêu toàn việc sang “thiết kế chuẩn UI + quy trình tạo/khai báo thành công MOW/MOT/MOIT/MOUT/Field”. Đây là thay đổi A0; trong tin nhắn hiện tại Owner chỉ quyết rõ việc công khai có lọc nhạy cảm, chưa xác nhận lại câu mục tiêu rộng đó. Giữ nguyên §0 đã xác nhận. Khi Owner xác nhận mục tiêu rộng, mở D mới và cập nhật A0 riêng; không dùng lời Reviewer để thay Owner. · Claude vòng 2 (Based_on `17b5470`): câu mục tiêu không phải đề xuất của Reviewer mà là nguyên văn Owner gõ khi giao Claude review (chat 2026-09-20). Đồng ý A0 cần Owner xác nhận rõ → chuyển **OWNER**. Không chặn MMIM.2 (thu thập không mâu thuẫn mục tiêu rộng).
- P02 · Scope PROMPT §2A/§3/§6 · **PARTIAL** · ACCEPT chẩn đoán NFD và yêu cầu `LINK-MAP`; GPT kiểm thật meta `project-assets-root` ghi NFD và README §12.3 hiện chỉ mirror một HTML. Không nhận đề nghị đưa `assets/` ra cạnh HTML ngay trong MMIM.2 vì D04–D05 của Owner yêu cầu lượt này chỉ gom vào `information/` và cấm sửa sản phẩm. PROMPT mới stage phụ thuộc dưới cha ASCII `information/direct-dependency/source-assets/`, kiểm 16 ảnh + manifest + mọi file-ref tương đối. Việc đổi đường dẫn HTML/Owner View là lượt riêng sau MMIM.2, chưa RUN.
- P03 · Scope public safety · **ACCEPTED theo quyết định Owner 2026-09-20** · repo được phép công khai để ưu tiên tốc độ/chất lượng; chỉ loại thông tin thật sự quá nhạy cảm/không cần thiết. PROMPT chặn credential/secret, định danh cá nhân rủi ro, dữ liệu tài chính/cá nhân và tài liệu không công khai cần bảo vệ; không tự loại tên người/tên công ty/thông tin nghiệp vụ công khai. File >50MB hoặc tổng >250MB được ghi nhận để tránh làm chậm/đẩy file lớn.
- P04 · Scope đúng bản · **ACCEPTED** · bản repo `mow-mot-moit-mout.html` là working SSOT của việc; Mac read-only. Codex đọc các sổ chỉ đường nếu có, so SHA bản Mac và SHA nguồn được HTML ghi; lệch thì ghi divergence, không chép đè.
- P05 · Scope UI runtime · **ACCEPTED** · UI đang chạy lấy VPS root `ui` làm thực địa theo A8; bản HTML/JS/CSS tương ứng trên Mac không được xếp CURRENT. Nếu cần đối chiếu thì LEGACY/MAC_RUNTIME_COPY; MMIM.2 không fetch runtime VPS.
- P06 · Claude · Based_on `6f15da7` · Scope PROMPT §0 + §7 / README D12 · **ACCEPTED theo nguyên tắc Owner, sửa căn cứ** · Nhận đúng yêu cầu phải gọi tên Write_Path và test đúng một read-gate trước mutation. Không nhận cách hiểu “GPT key/Claude key”: DROOT06/README đã sửa capability-first. MMIM.2 chốt `Executor_Surface=Codex`; primary `Write_Path=workspace_*`, fallback `fs_*` nếu chính phiên Codex bind path đó; cấm Git/CLI/native write. Prompt phải ghi tên tool family + gate; Agent không tự suy và không đổi vai giữa chừng.
- P07 · Claude · Based_on `6f15da7` · Scope PROMPT §0.4 · §5 · §6 · §7 · **ACCEPTED có siết chống chọn nhầm nguồn** · (a) so commit cuối chạm PROMPT, không so HEAD; phạm vi thay đổi chỉ tính mutation do Codex tạo. (b) text >100 KB không relay qua model: inventory `PENDING_LARGE_TEXT` + bytes/SHA, xử lý như external/shared asset sau. (c) transport đổi newline/BOM thì ghi `NORMALIZED_BY_TRANSPORT` + SHA hai bên, không retry vòng lặp; nội dung phải được xác nhận tương đương text. (d) `OUTCOME_UNKNOWN` → read-back/journal/idempotency, không ghi lại mù. (e) ưu tiên path Owner đã chỉ; nếu lookup lỗi do Unicode/path thì resolve trong Desktop trước, sau đó Documents/Google Drive cục bộ; nếu nhiều candidate phải đối chiếu marker/SHA, không chọn chỉ vì trùng tên.
- P08 · Claude · Based_on `2d673a3` · Scope PROMPT §0.5 · §2 · §6 · §7 · **OPEN — 4 câu chèn nguyên văn, không cần vòng review nữa** · R2 đã gỡ đúng gốc I02 (Write_Path gọi tên + read-gate đầu). Còn 4 đường có thể làm Codex DỪNG oan hoặc chạy quá tốn. Đã kiểm nguồn connector: family `workspace_*` có `workspace_log`/`workspace_stat`/`workspace_write_new`/`workspace_transaction`; family `fs_*` có `fs_log`/`fs_stat` — đủ để làm hết bằng đúng family đã qua gate. Chèn nguyên văn: (1) §0 bước 5, thêm: “Tra commit cuối chạm `PROMPT.md` bằng `workspace_log`/`fs_log` của chính Write_Path; không dùng clone local (clone local cũ là nguyên nhân I01).” (2) §7, thêm: “Nếu guard bí mật của Write_Path từ chối một file: KHÔNG sửa/che nội dung để lọt guard; bỏ file đó khỏi lô, ghi `OMITTED_SECRET_GUARD` + path + SHA nguồn vào README, ghi lại phần còn lại của lô và tiếp tục. Đây không phải lý do DỪNG.” (lý do: tài liệu cũ trong `quy trình/` rất có thể chứa URL connector có token; hiện dòng cuối prompt ghi “secret không xử lý an toàn → DỪNG” → một file bị guard chặn có thể dừng cả lượt, và transaction nhiều file bị hủy cả lô.) (3) §2 cuối, thêm: “Lớp D chỉ inventory, không copy. Tổng nội dung text relay qua model cả lượt ≤300 KB, ưu tiên A → B → C; vượt ngân sách → phần còn lại `PENDING_LARGE_TEXT`. Ghi theo lô nhỏ (≤10 file/commit), không dồn một transaction khổng lồ.” (lý do: ngưỡng 100 KB/file chưa chặn tổng — 20 file × 90 KB vẫn là khối output rất lớn, dễ tràn ngữ cảnh/timeout và tốn tiền.) (4) §6, sửa dòng “mỗi file text đã copy có hash nguồn = hash đích” thành “… = hash đích **hoặc `NORMALIZED_BY_TRANSPORT` theo §5**” (hiện §5 cho phép nhưng §6 cấm → Codex đọc chặt sẽ tự đánh trượt).

Claude REVIEWED@2d673a370a030e2b679d161132cb908f897b9503 · **ACCEPT có điều kiện P08** — Host chèn đúng nguyên văn 4 câu P08 thì coi như Claude đã ACCEPT bản mới, Host đặt READY luôn, không cần gửi Claude review lại. Ngoài 4 câu này, mọi sửa khác vào PROMPT vẫn phải review theo A6. HTML chính kiểm lại: SHA `f4aac30c…a050c` PASS.

## Phương án Host chờ Claude review
- H01 · **ACCEPTED + mở rộng:** Git chỉ giữ HTML, text nhỏ (≤100 KB/file), README, `assets-manifest.json` và LINK-MAP. Binary và text >100 KB không relay qua model/không commit ở MMIM.2; chỉ inventory bytes/SHA/path/state để shared-assets/external step sau.
- H02 · **Shared assets ngoài Git:** sau MMIM.2, publish binary một lần vào kho static HTTPS dùng chung để GPT/Claude/Codex/Hermes và Owner View cùng đọc bằng URL tuyệt đối. Ưu tiên tái dùng hạ tầng static hiện có; không mở dự án sửa MCP/connector. Repo giữ SHA/bytes/URL làm SSOT metadata. Cơ chế/path publish cụ thể phải được Claude phản biện trước khi Host chốt MMIM.3.
- H03 · MMIM.2 không được DỪNG chỉ vì connector không nhập binary; binary pass ở lượt này = định vị + SHA/bytes + manifest/link-map.

**Claude trả lời H01–H03 (Based_on `6f15da7`):**
- H01 · **ACCEPT + bổ sung**: tách đúng hướng, nhưng tiêu chí thật không phải “binary hay text” mà là **file có phải đi qua ngữ cảnh của mô hình hay không**. Text lớn (ví dụ `00-NGUON-THIET-KE.html`, `cấu trúc hệ thống.html`) khi đẩy qua connector vẫn phải chạy qua mô hình → vừa tốn vừa có nguy cơ sai byte. Chi tiết ở P07b.
- H02 · **Đồng ý nguyên tắc, chưa chốt được đường đi**: binary ngoài Git + URL tuyệt đối + repo giữ metadata là đúng và hợp README §11.5/§12. Nhưng hiện **chưa tồn tại đường vận chuyển binary nào đã nghiệm thu**: Codex không nhập được binary (I02), `fs_write` của Claude chỉ nhận text, và dựng endpoint upload mới = sửa dịch vụ VPS (ngoài phạm vi, đúng như Host đã loại). Đề nghị: không chốt cơ chế bây giờ; MMIM.2 cứ chạy với inventory. Đến bước shared-assets mới chọn, và ứng viên rẻ nhất lúc này là Owner upload MỘT lần đúng 16 ảnh vào vùng static hiện có, có hướng dẫn từng bước — không dựng hạ tầng mới, không sửa connector.
- H03 · **ACCEPT**: đúng nguyên nhân gốc của I02 về phần binary.

## Owner cần quyết
- Q01 · Kho tham khảo 23/09: cho phép ngoại lệ D12 một lần để Codex commit/push bằng Git trực tiếp đúng 304 ảnh/Excel/Word trong `information/binary-pending.json` (46.090.145 bytes), kèm cập nhật inventory/README/COLLAB? Đã chuẩn bị nguyên byte, kiểm hash, trích nội dung Office/OCR ảnh và quét bí mật; chưa ghi binary lên repo. Không force, không sửa nguồn/HTML chính, chỉ phạm vi kho tham khảo. Hoặc cung cấp capability nhập binary đã audit để thực hiện cùng gói.
- P01 · Xác nhận mục tiêu toàn việc (A0): “thiết kế chuẩn các UI, chuẩn quy trình tạo và khai báo thành công MOW/MOT/MOIT/MOUT/Field”; tiêu chí xong = mỗi đối tượng có UI chuẩn Owner chốt + quy trình tạo/khai báo viết thành bước + ≥1 lần khai báo thật thành công có bằng chứng. P01 không chặn Claude review/MMIM.2 hiện tại.

## Sự cố / bài học Host
- I01 · 2026-09-21 · Codex trả: `DỪNG · MMIM.2 · Workspace hiện tại không có work/mow-mot-moit-mout/COLLAB.md và PROMPT.md; không thể xác minh ba gate bắt buộc. Chưa thay đổi file nào.` → Host đã sửa bootstrap/input gate.
- I02 · 2026-09-21 · Codex trả: `DỪNG · MMIM.2 · Gate công cụ ghi chưa đạt: README §0/D12 cấm AI push bằng Git/CLI; connector hiện có chưa có đường nhập ảnh nhị phân từ Mac đáp ứng giao dịch bắt buộc. Chưa tạo information/ hoặc sửa nguồn, HTML, COLLAB.`
- Kết luận Host I02: prompt sai kiến trúc khi bắt binary đi vào Git. Sửa nguyên nhân gốc: MMIM.2 không đưa binary vào Git; chỉ inventory/hash. Shared-assets ngoài Git là bước riêng sau consensus, không sửa connector.

## Giao Agent — lịch sử prompt MMIM.2 trước yêu cầu mới 23/09
- READY@`7d8e1df9e50cfdd5a4b7cfaf8c66cad9343e26f3` → **HẾT HIỆU LỰC** vì Host đã sửa `PROMPT.md` sau I02.
- **NO RUN** theo D10. Chờ Claude review bản prompt mới và H01–H03.

## Kết quả yêu cầu kho tham khảo 23/09/2026
- Executor_Surface: Codex · Write_Path: `workspace_*` · read-gate PASS. Theo lệnh trực tiếp Owner mới, không chạy PROMPT MMIM.2 nháp và không tự đặt READY cho bản nháp.
- Đã commit/push 888 tài liệu nguyên byte, 87.874.934 bytes; gồm cả hai HTML ưu tiên. Commit nhập cuối: `42e2db1ce50dd42563351aa252145fed541ffa76`; các commit nhập từng file nằm trong `information/inventory.json`.
- Đọc lại blob Git: 888/888 SHA nguồn = đích. Kiểm lại 2.155/2.155 file Mac: hash không đổi. HTML chính SHA `f4aac30c492f104ec54ff7a03ace54ce70d802e2dd49a417ad9b7285897a050c` giữ nguyên.
- 304 binary/46.090.145 bytes sẵn sàng, chưa publish; 16/16 ảnh manifest nguồn đúng hash/bytes. Phần bỏ/chờ/trùng ghi trong inventory; không tuyên bố đã chuyển hết, không nghiệm thu nghiệp vụ, không chạm VPS/runtime.
- Mục lục, inventory và LINK-MAP: `information/README.md`. · Áp: SAME_COMMIT.

## NEXT
- Giải quyết Q01 về đường chuyển binary rồi đưa nốt gói đã chuẩn bị; giữ nguyên HTML chính. Không tự mở rộng P01 hoặc sửa luật nền.
