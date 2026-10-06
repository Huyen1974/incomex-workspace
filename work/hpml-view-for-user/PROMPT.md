# PROMPT — HVU-OWNERVIEW02 · Viết gì trên repo thì chảy xuống trang Owner; hỏng thì có đèn báo

RUN_ID: HVU-OWNERVIEW02-20261006-01

**Trạng thái: NHÁP — CHƯA READY.** Claude Chat soạn 06/10/2026 theo lời Owner 14:59 (COLLAB P36). Chỉ được chạy khi `COLLAB.md` của việc này có dòng READY trỏ đúng commit cuối chạm file này và không có HOLD/STOP/cờ bận.

## 0. Cổng đọc và ranh giới
- Executor: **Claude Code CLI, phiên mới.** Đọc theo thứ tự: `AGENTS.md` → root `COLLAB.md` (DROOT16/17, 26, 29, 30, 31, 32, 35, 36, 42, 43) → `work/hpml-view-for-user/COLLAB.md` (§0, Bảng điều khiển, P36) → file này → trên VPS: `docker/nuxt-repo/scripts/hvu-b2/README.md` và `00-NHAN-THU-MUC.md`.
- Sau khi qua cổng đọc: ghi `STARTED@<RUN_ID> <giờ UTC> · executor=Claude Code CLI` vào COLLAB, sửa dòng ■ / ➡ / `cập nhật` của Bảng trong cùng commit (MT4). Kết thúc bằng một dòng KQ (mục 6).
- **Mã chạy trên VPS là nguồn chuẩn. Cấm GitHub → VPS** cho mã dưới mọi hình thức. Trang chỉ được build trên VPS.
- Repo công khai: không ghi bí mật, token, địa chỉ đầy đủ của đầu nối, IP vào repo, vào `tasks.json` hay vào báo cáo; log chỉ in tên và số đếm.
- Lượt này **không đọc, không ghi Directus/PostgreSQL** (không cần).
- Không dựng dịch vụ, timer, trang, URL hay đường xem mới. Không đụng: cổng ghi (agent-data, claude-mcp), webhook, nginx, compose, các unit systemd, `presence.py`, tài liệu của việc khác.
- Một lượt liền, **không có điểm chờ Owner**. Gặp điều kiện DỪNG: ghi KQ DỪNG kèm nguyên nhân rồi kết thúc phiên; không giữ tiến trình nền, không vòng chờ.

## 1. Mục tiêu (Owner 06/10/2026 14:59)
> “các bạn cứ bàn trên repo, viết cái gì ra thì chayn xuống VPS. VPS đơn giản chỉ là cái kênh để cho user có thể xem trực tiếp và dễ nhìn. Đặc biệt là thông tin tiến độ theo thời gian thực (ai đang làm? ai vừa làm) … Còn gì lỗi của việc này dẫn đến lỗi ngớ ngẩn đó => bạn có thể sửa, bảo vệ để khỏi hỏng”

Lỗi cần trị tận gốc (COLLAB P36): máy đồng bộ so đúng từng chữ một dòng tiêu đề nên một lần đổi chữ làm trang trắng mục tiêu mà không ai được báo; Bảng điều khiển không được rút xuống trang; tài liệu cũ không ghi ngày.

## 2. Đọc trước — chỉ đọc, trong cùng lượt
- **P1.** Ghi số đèn và sổ tin báo hiện tại (bao nhiêu xanh/đỏ; bao nhiêu loại · chạy · hỏng). Có đèn đỏ liên quan Owner View ⇒ DỪNG.
- **P2.** Trong `docker/nuxt-repo`: trạng thái Git của đúng các file sẽ chạm — `scripts/hvu-b2/sync.py`, `test_sync.py`, `ui/app.vue`, `README.md`, `00-NHAN-THU-MUC.md`, `web/tests/e2e/owner-view-lifecycle.spec.ts`. Có thay đổi chưa commit không phải của lượt này trên các file đó ⇒ DỪNG, nêu tên file.
- **P3.** Chạy bộ thử đang có trước khi sửa để lấy mốc: `python3 -m unittest -v test_sync test_b3 test_lifecycle_r6`, `node test_webhook.mjs`, và phép thử trình duyệt theo đúng lệnh ghi ở `00-NHAN-THU-MUC.md` (fixture). Không xanh ⇒ DỪNG.
- **P4.** Cờ bận: đọc root `## Đang làm` và Bảng các việc đang làm. Có RUN đang STARTED chưa KQ mà chạm `scripts/hvu-b2`, `mcpw-protection-guard` hoặc baseline Config Guard ⇒ DỪNG, nêu tên RUN.
- **P5.** Xác định bằng đọc: (a) Guard `mcpw-protection-guard` đang có phép nào canh Owner View (đã biết INV12, INV13); đã có phép nào canh `sync-status.json` báo lỗi hoặc quá hạn chưa; số INV kế tiếp còn trống; (b) mục Config Guard nào đang giữ hash của `sync.py`, của `view.html` đang phục vụ và của chính guard; đường áp chuẩn `incomex-config-apply-v0` mà lượt R6 (02/10) và A09R1 (01/10) đã dùng cho chính các file này; (c) cách thêm một dòng sổ tin báo (mẫu: dòng `B-N1CS01` của HJW N1).
- **P6.** Tồn dư “presence 502” (root `COLLAB.md`, dòng VPSC residual): đếm số lần 502 của `data/presence.json` và `data/sync-status.json` trong log nginx 24 giờ gần nhất. **Chỉ ghi con số vào KQ, không sửa trong lượt này.**

Ghi kết quả đọc trước thành một đoạn ngắn trong mục P của lượt rồi làm tiếp ngay.

## 3. Việc sửa — đúng sáu việc, không thêm

### F1 · `sync.py` — rút Bảng điều khiển
- Trong phần §0 hiện hành (trước `### Vòng trước` đầu tiên): lấy dòng tiêu đề bắt đầu bằng `### BẢNG ĐIỀU KHIỂN`; thân là các dòng tới tiêu đề `### ` kế tiếp. Bảng nằm sau `### Vòng trước` là của vòng cũ, không nhận.
- Thêm vào mỗi việc trong `tasks.json` trường `board`: `{title, updated, lines}` — `title` = dòng tiêu đề bỏ `### `; `updated` = đoạn sau chữ `cập nhật ` tới dấu ` · ` kế tiếp (không có thì rỗng); `lines` = các dòng không rỗng của thân, đã qua `clean_line` sẵn có. Không có Bảng ⇒ `board` = null.
- Thêm trường `goalWarnings` (danh sách chuỗi) chứa riêng các lời nhắc về §0 và Bảng (cả lời nhắc cũ `§0 chưa chuẩn`, `A0 thiếu hoặc sai dấu Xác nhận User` lẫn lời nhắc mới ở F1/F2); các lời nhắc này vẫn có mặt trong `warnings` như cũ.
- Việc đang làm (bucket Now) mà không có Bảng ⇒ thêm lời nhắc `Chưa có Bảng điều khiển (AGENTS MT4)`. Việc đã xong thì không nhắc.
- **Chỉ thêm trường; không đổi tên, không đổi nghĩa trường cũ** (`presence.py`, cổng Hermes và bản trang cũ phải đọc được như trước).

### F2 · `sync.py` — đọc §0 dung thứ, không im lặng
- Tiêu đề §0: so đúng chữ như hiện nay trước. Không thấy ⇒ nhận dòng `## ` đầu tiên bắt đầu bằng `## 0.` làm §0 và thêm lời nhắc `Tiêu đề §0 lệch chuẩn: <tiêu đề thật>`.
- Bốn tiêu đề con: so đúng chữ trước. Không đủ ⇒ nhận theo đầu dòng `### 1.`, `### 2.`, `### 3.` (mỗi cái đúng một lần, đúng thứ tự, trước `### Vòng trước` đầu tiên) và thêm lời nhắc `Tiêu đề con §0 lệch chuẩn`. Thiếu hẳn `### Vòng trước` ⇒ coi phần còn lại của §0 là vòng hiện hành và thêm lời nhắc `§0 thiếu mục Vòng trước`.
- Đọc được theo cách dung thứ ⇒ `goalStructured` = true, các ô hiện bình thường, kèm lời nhắc. Vẫn không đọc được ⇒ giữ nguyên hành vi cũ (`goalStructured` = false, `§0 chưa chuẩn`).

### F3 · `ui/app.vue` — trang hiện Bảng trên cùng, chữ sạch
- Tab `Kiểm soát`: thêm **đúng một** mục đầu tiên `Bảng điều khiển`, mở sẵn, hiện `board.lines` mỗi dòng một đoạn, không cuộn trong ô; phía trên có dòng nhỏ `cập nhật <board.updated>`. Việc đang làm mà `board` = null ⇒ nhãn `Bảng điều khiển · chưa có` chữ vàng cam và một câu giải thích. Việc đã xong không có Bảng ⇒ không hiện mục này.
- `goalWarnings` không rỗng ⇒ hiện thành một dòng vàng cam ngay đầu tab `Kiểm soát` (hiện nay lời nhắc chỉ nằm trong mục gập cuối trang).
- Các ô Mục tiêu, Thế nào là hoàn thành, Chi tiết cần đạt, Vòng trước: hiện chữ đã bỏ ký hiệu định dạng (`**`, dấu backtick, `> ` đầu dòng, `~~…~~`) qua một hàm thuần chữ. **Vẫn dùng nội suy chữ `{{ }}`; cấm `v-html`.** Bỏ giới hạn chiều cao và cuộn trong của hai ô Mục tiêu và Thế nào là hoàn thành; hai ô còn lại giữ nguyên.
- Sửa hai câu chú thích đã cũ trong chính file này: `Vừa làm 2: lần trước đó` → `Vừa làm 2: AI khác gần nhất` (HVU P35, Owner 24/09); `backstop kiểm mỗi 15 phút` → `4 phút`.
- **Không đổi gì khác:** thứ tự tab, thứ tự các mục còn lại, Master list, cột, sao, deep-link, nút Cập nhật, cách lấy người làm.

### F4 · `sync.py` + `ui/app.vue` — ngày của tài liệu
- `sync.py`: thêm trường `documentCommit` = `[sha, giờ ISO, tiêu đề commit]` của commit cuối chạm đúng file HTML chính của việc (dùng hàm `log` sẵn có); không có tài liệu ⇒ null.
- `ui/app.vue`, tab `Nội dung công việc`, ngay cạnh chữ `HTML nguyên bản từ GitHub`: thêm `sửa lần cuối HH:mm dd/MM/yy · <bao lâu trước>` bằng đúng hàm thời gian trang đang dùng. Chữ trung tính, không tô màu, không suy diễn “cũ hay mới”.

### F5 · Guard — đèn báo khi Owner không đọc được
- Thêm **một** phép canh vào `mcpw-protection-guard` (đèn gộp #22), tên `owner_view_goal_flow`, dùng số INV kế tiếp còn trống. ĐỎ khi: (a) trong `tasks.json` đang phục vụ có việc bucket Now mà `goalStructured` = false hoặc `objective` rỗng — thông báo nêu tên việc; (b) `sync-status.json` có `status` = error hoặc `lastSuccessAt` cũ hơn 35 phút — **chỉ thêm (b) nếu P5 cho thấy chưa có phép nào canh điều này**. Không đọc được `tasks.json` ⇒ đỏ.
- Thiếu Bảng **không** làm đỏ (chỉ vàng trên trang).
- Thêm một dòng sổ tin báo cho phép canh này trong cùng lượt (DROOT36); số loại tăng đúng 1.
- Mọi thay đổi guard và baseline đi qua `incomex-config-apply-v0`. Không sửa tay file đang được Config Guard giữ hash. Không rebaseline bất cứ thứ gì ngoài dấu chân của lượt này.

### F6 · Thử, bảo vệ, quay lui (Điều 30/31, DROOT29)
- `test_sync.py` thêm ca: (1) tiêu đề §0 bị thêm chữ nhưng còn `## 0.` ⇒ `objective` vẫn ra, có lời nhắc; (2) tiêu đề con lệch kiểu `### 1. Mục tiêu (…)` ⇒ vẫn ra, có lời nhắc; (3) thiếu `### Vòng trước` ⇒ vẫn ra, có lời nhắc; (4) không có §0 ⇒ `goalStructured` = false; (5) có Bảng ⇒ `board.lines` đúng số dòng, `updated` đúng; (6) không có Bảng ⇒ `board` = null, có lời nhắc ở việc đang làm, không có ở việc đã xong; (7) Bảng nằm sau `### Vòng trước` không được nhận; (8) `documentCommit` trỏ đúng commit của file HTML; (9) mọi trường cũ của một việc mẫu giữ nguyên giá trị so với trước khi sửa.
- `owner-view-lifecycle.spec.ts` (fixture) thêm: mục `Bảng điều khiển` đứng đầu và hiện đúng dòng; ô Mục tiêu không còn `**`; nhãn ngày tài liệu có mặt; dòng vàng hiện khi có `goalWarnings`. Các phép cũ (Sổ phiên, Ngoài việc, 2 PHIÊN) phải vẫn xanh. Thử bản build mới bằng `OWNER_VIEW_HTML=<file>` **trước** khi đưa lên; sau khi đưa lên chạy thêm `OWNER_VIEW_LIVE=1`.
- Phép âm cho guard: trên bản sao/fixture (không sửa repo thật, không sửa dữ liệu đang phục vụ) cho một việc Now có `goalStructured` = false ⇒ phép canh phải đỏ và nêu đúng tên; trả lại ⇒ xanh.
- Trước khi đổi: sao lưu `sync.py`, `test_sync.py`, `ui/app.vue`, `view.html` đang phục vụ và guard vào `/opt/incomex/work/hpml-view-for-user/HVU-OWNERVIEW02-20261006/before/`, kèm `rollback.sh` (`--check` / `--apply`) trả đúng các file đó qua đường áp chuẩn. Chạy `rollback.sh --check`.
- Cập nhật `README.md` và `00-NHAN-THU-MUC.md` của `scripts/hvu-b2` bằng một đoạn ngắn: trường mới, phép canh mới, cách quay lui. Commit mã chạy theo README §11 của workspace.
- POST-PROTECT: lập bảng `thành phần → Điều 30 → Điều 31 → watchdog → rollback → ĐỦ|THIẾU`. Còn một dòng THIẾU ⇒ không được ghi XONG.

## 4. Thứ tự làm
1. `sync.py` + ca thử (F1, F2, phần máy của F4) → thử đơn vị xanh → áp. Chờ **một** lần đồng bộ thật do chính commit checkpoint của lượt này kích (không ép build tay, không sửa tay `tasks.json`). Đọc `tasks.json` đang phục vụ: trường mới có, trường cũ không đổi, `presence.json` vẫn mới.
2. `ui/app.vue` (F3, phần trang của F4) → build chỉ trên VPS theo README (`ui/`: `nuxt generate` rồi `node pack.mjs`) → thử trình duyệt trên file vừa build → thay nguyên tử `view.html` đang phục vụ → thử LIVE.
3. Guard (F5) → selftest + phép âm → chạy thật PASS → sổ tin báo.
4. Phần còn lại của F6 → KQ.

Ngay trước mỗi bước 1, 2, 3: đọc lại `COLLAB.md` và `PROMPT.md` của việc này (DROOT30). Thấy HOLD, STOP hoặc READY mới ⇒ DỪNG. Bước nào hỏng: quay lui đúng bước đó bằng `rollback.sh`, ghi KQ DỪNG kèm nguyên nhân; không vá vòng, không thử cách khác ngoài đề bài.

## 5. Chỉ ghi XONG khi đủ cả mười điều
1. Cả năm việc đang làm (`graph-server`, `hermes-joint-workspace`, `hpml-view-for-user`, `mow-mot-moit-mout`, `pg-nhan-balo`) có `goalStructured` = true và `board` khác null trong `tasks.json` đang phục vụ; mục `Bảng điều khiển` đứng đầu tab Kiểm soát; số dòng và dòng `cập nhật` trùng Bảng trong COLLAB ở đúng revision đang publish.
2. Thử sống một vòng: chính commit KQ/checkpoint của lượt này sửa dòng `cập nhật` của Bảng việc này ⇒ trong vòng 5 phút trang hiện dòng mới mà không ai chép tay. Ghi hai mốc giờ.
3. Ô Mục tiêu và Thế nào là hoàn thành không còn ký hiệu định dạng thô; trong `app.vue` không có `v-html`.
4. Ca đổi tiêu đề (fixture): mục tiêu vẫn hiện, có dòng vàng. Ca không đọc được: phép canh đỏ, nêu tên việc.
5. “Vừa làm 1/2”, “Đang làm”, Master list, deep-link, nút Cập nhật không đổi: phép thử cũ xanh; INV12, INV13 xanh.
6. Bộ thử: unittest cũ + mới xanh; `node test_webhook.mjs` xanh; thử trình duyệt fixture + LIVE xanh.
7. Đèn: tổng số không giảm, 0 đỏ. Sổ tin báo: 0 hỏng, số loại tăng đúng 1. Config Guard sạch sau khi áp.
8. `rollback.sh --check` PASS; biên nhận POST-PROTECT đủ, 0 THIẾU.
9. Không có bí mật hay địa chỉ đầu nối trong repo, trong `tasks.json`, trong báo cáo của lượt.
10. KQ ghi ở COLLAB, Bảng sửa cùng commit, kèm link: `https://vps.incomexsaigoncorp.vn/knowledge/modules?task=hpml-view-for-user`.

## 6. Báo cáo
- Xong: `KQ@HVU-OWNERVIEW02-20261006-01 XONG · board=5/5 · live_roundtrip=<giây> · inv=<số INV mới> PASS · den=<xanh>/<tổng> · so_tin_bao=<N loại · M chạy · 0 hỏng> · presence_502_24h=<số>`
- Dừng: `KQ@HVU-OWNERVIEW02-20261006-01 DỪNG · <lý do cụ thể> · rollback=<đã làm|không cần>`
- Phần cho Owner: tối đa năm dòng tiếng Việt thường, không thuật ngữ — trang giờ có gì mới, hỏng thì ai được báo, và link ở trên.
- Ghi KQ xong thì kết thúc phiên; không để lại tiến trình nền.
