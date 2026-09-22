# HANDOFF — PHIÊN MỚI: test connector → triển khai MODW

> Đọc hết file này TRƯỚC khi làm. Phiên trước quá dài nên chuyển phiên. Mọi số trong đây đã xác minh từ file sống (2026-07-14), nhưng **luật vàng: đọc lại file sống, cấm trích số nhớ.**

---

## 0. MỤC ĐÍCH PHIÊN MỚI (đúng thứ tự)
1. **TEST kết nối lại** — connector đọc-file VPS vừa được Owner fix; xác nhận nó đã nạp tool trong phiên mới chưa.
2. **Triển khai MODW** — gắn `data-region` cho MODW (UI thứ 2), theo KHUÔN NGHIỆM THU đã chốt ở MOW.

---

## 1. DỰ ÁN LÀ GÌ (1 đoạn)
Xây "hợp đồng thông tin sửa rẻ" cho hệ UI Incomex: nhúng mã bền `data-region` vào từng phần tử HTML = **cột C** trong Excel. Mỗi lần UI đổi → `grep data-region` trong code ↔ cột C (gọi là **TRỌNG TÀI**) tự lộ thiếu/thừa, khỏi rà tay. Đích sâu hơn = **"linh hồn sửa rẻ": không phải vẽ đúng hôm nay, mà làm cho SỬA NGÀY MAI rẻ.** Cố enumerate hoàn hảo = phản linh hồn.

## 2. VAI TRÒ (hội đồng — giữ đúng "người-sửa ≠ người-kiểm")
- **CW (Cowork, bạn):** soạn spec · quản Excel · nghiệm thu (trọng tài). Có: Excel (Read/Write/Edit), bash sandbox, Chrome MCP (hay chết), Directus MCP, web_fetch. **KHÔNG:** sửa code VPS, lưu ảnh chụp màn.
- **Desktop (DT):** phản biện + chuyển ý Owner. Soi rất kỹ, hay verify bản sống.
- **Owner (Huyen):** quyết nghiệp vụ thật, chốt cuối.
- **Claude Code:** sửa/commit code VPS (có shell VPS trực tiếp). Là "người-sửa".
- **Codex:** điều khiển máy Mac, **lưu ảnh chụp màn** (CW không lưu được).

## 3. FILE & CÁC SHEET
File: `/Users/nmhuyen/Desktop/quy trình/hop-dong-thong-tin-sua-re.xlsx` (13 sheet). **Backup trước MỖI lần ghi** (cp sang `_BACKUP_<ngày>.xlsx`).

| Sheet | Vai trò |
|---|---|
| `BAT_DAU` | Cửa vào — Owner nhìn 3 sheet: ui_cay / man_hinh / phieu_trinh |
| `ui_cay_ma_khu_vuc` | **BẢN ĐỒ CHÍNH** — 169 dòng, 16 cột (xem §4) |
| `man_hinh` | Sổ màn: 10 ảnh MOW (`anh-man-hinh-ui/mow-01..10.png`) + màn 11,12 MODW = "CHỜ" |
| `phieu_trinh` | Việc chờ Owner (hiện 0) |
| `dinh_nghia_khai_niem` | **SỔ KHÁI NIỆM (bản NHÁP)** — 45 concept. Cột: concept_key·ten·concept_kind·mo_ta·ranh_gioi·aliases·match_policy·status·note·lien_quan |
| `tu_dien` | Giá trị cho phép mỗi cột (dropdown) |
| `quy_trinh` | **QUY TRÌNH CHUẨN** (HOW là SSOT ở đây) — Loại A/B, 5 luật, khuôn nghiệm thu NT1–6, quy trình sửa rẻ, 4 luật vệ sinh, Luật 5 HOW-SSOT |
| `huong_dan` | **VÌ SAO** (nguyên tắc/triết lý/bài học) — 265 dòng. NỢ: còn HOW-chi-tiết + lịch sử cần dời (xem §8) |
| `sua_re_khai_niem_nhap` + `sua_re_ui_khai_niem_nhap` | **GƯƠNG 2 TABLE PG** — GIỮ TRỐNG tới khi CHUẨN HOÁ CUỐI. ĐỪNG đổ dữ liệu vào lúc nháp! |
| `CONG_CU`, `biz_flow_nhap` | phụ |
| `Plan_luu_tru` | Kho lưu trữ (lịch sử/legacy đã dời) |

## 4. CỘT của `ui_cay_ma_khu_vuc` (16 cột — legacy đã nghỉ hưu)
`stt · ui_cay_theo_ten_hien_thi · ui_cay_ma_khu_vuc(=data-region=ANCHOR) · id · mo_ta_thuc_te(tiếng người, cứu-Owner) · man_hinh_so · ban_chat(nghĩa đầy đủ) · khai_niem_chung(→concept_key) · trang_thai · note · ban_chat_khu · doi_tuong · vai_tro · hanh_dong · pham_vi_hop_dong(IN/OUT/REVIEW) · anchor_scope(DOM/PLANNED/NA)`
Bộ giá trị mỗi cột enum có dropdown; danh sách ở `tu_dien`.

## 5. TRẠNG THÁI: MOW ĐÃ KHÉP HOÀN TOÀN
- `data-region` MOW: **khép 100%** (trọng tài 0 thiếu; code không đổi từ phiên gắn mã).
- Sổ khái niệm: **45 concept** (concept_kind: người 4 · thời gian 7 · quy trình 18 · đề xuất 15 · tổ chức 1). Đủ 5 nhóm MOW, hội tụ (nhóm sau lộ ít hơn).
- Bản đồ: **169 dòng**, mọi cột chính đầy, cột legacy nghỉ hưu (lưu ở Plan_luu_tru).
- **Khuôn nghiệm thu NT1–6 đã self-test trên MOW** (PASS substance; đã siết chặt NT1 + NT6).

---

## 6. VIỆC 1 — TEST KẾT NỐI LẠI (làm đầu tiên)
Phiên trước: connector đọc-file VPS **rớt giữa chừng** (Directus/DB vẫn ok). Owner đã fix. Trong phiên mới, kiểm:
1. `ToolSearch` các tool đặc trưng: `read_file`, `write_file`, `query_pg`, `pg_schema`, `docker_logs`. Nếu 1 connector (UUID bất kỳ) hiện ra với các tool này → **đã về**.
2. Xác nhận DB: `mcp__directus__directus_health` (kỳ vọng `ok`, URL `directus.incomexsaigoncorp.vn`).
3. **Nếu file-read connector đã về** → đọc thẳng raw `modw-builder-v1.html` (đường dẫn VPS: `/opt/incomex/docs/mcp-writes/modw-builder-v1.html`).
4. **Nếu VẪN chưa về** → dùng Claude Code (có shell VPS) `cat` file — prompt ở §7.4.
> ⚠️ Bẫy phiên trước: `web_fetch` chuyển HTML→markdown (mất thẻ/class, KHÔNG dùng để đếm MATCHES). Chrome `javascript_tool` bị **privacy-guard khoá** sau khi trích `outerHTML` (mọi page-data return thành `[BLOCKED]`); Chrome tab hay chết. `read_page` (accessibility tree) thì CHẠY được — dùng nó để đọc cấu trúc live nếu cần.

---

## 7. VIỆC 2 — TRIỂN KHAI MODW

### 7.1 Đã biết từ đọc code LIVE phiên trước (Chrome read_page) — TIN được, nhưng nên đọc lại raw để chốt chuỗi FIND
- **URL:** `https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/modw-builder-v1.html` (file 1, self-contained, ~29.7KB, inline JS).
- **6 `data-region` SẴN = toàn `shell.dock.*`** (dock dùng chung do eco-nav.js inject) → **KHÔNG phải nội dung MODW**. Nội dung builder = **0 mã**. ⚠️ Chạy trọng tài MODW phải **TRỪ 6 dock** ra, không thì báo thừa oan.
- **Excel có 31 mã `modw.*`** (3 NA gốc-cây: `modw`, `modw.build`, `modw.picker`; 28 PLANNED). Trong 28 PLANNED có **3 CHƯA DỰNG thật** (không có element): `modw.build.approver`, `modw.build.delegate`, `modw.build.variant` (là khái niệm khuôn-đúc thêm ở phiên trước) → **bỏ qua khi gắn, không có element**.
- ⇒ **~24–25 element THẬT cần gắn.**

### 7.2 Bản đồ element live → mã modw.* (để soạn spec)
- Topbar: link "MOW canvas" → `modw.shell.link.canvas`; link "Danh sách MOW" → `modw.shell.link.list`.
- Mục 1 Node&tầng: `input#nNode` → `modw.build.node.name`; `select#nTier` → `modw.build.node.tier`.
- Mục 2 Bố: select/khối "Bố (Tx)" → `modw.build.parent`.
- Mục 3 Người thực hiện: khung → `modw.build.exec`; **chip người (template, N instance)** → `modw.build.exec.chip` (**OCC:all / gắn trong hàm render — bẫy 'helper 1 chuỗi render N'**); nút "＋ Thêm người thực hiện" → `modw.build.exec.add`.
- Mục 4 Người nhận: khung → `modw.build.recipient`; **chip (template)** → `modw.build.recipient.chip` (OCC:all); nút "＋ Thêm người nhận" → `modw.build.recipient.add`.
- Mục 5 Kho: khung → `modw.build.store`; **6 checkbox item (template)** → `modw.build.store.item` (OCC:all).
- Mục 6 Thời gian: textbox "Khi nào" → `modw.build.time`.
- Bản đúc: nút "⚡ Đúc node" → `modw.preview.cast`; preview: tier→`modw.preview.tier`, tên→`modw.preview.name`, đường tổ tiên→`modw.preview.bread`, thân→`modw.preview.body`, JSON→`modw.preview.json` (tên hiển thị "Khuôn đúc").
- Modal "Chọn": tiêu đề→`modw.picker.title`; nút ✕→`modw.picker.close` (⚠️ nhiều nút ✕ trên trang, cần đếm MATCHES kỹ); ô "Tìm…" + **dòng item (template)** → `modw.picker.item` (OCC:all).

### 7.3 ⚠️ LỖ HỔNG đã phát hiện (đọc code live mới thấy)
Mục 6 trong code SỐNG còn cả **khối "Hướng dẫn" đa phương tiện** (Văn bản · Sơ đồ/Ảnh · Audio · Video · Các bước + nút xem trước) mà **31 mã Excel KHÔNG có**. → Khi siết concept MODW sẽ **lộ concept mới** (hướng dẫn đa phương tiện). Phải lật-gần-giống trước khi tạo (có thể gộp vào `noi_dung_de_xuat`/`huong_dan` hay tách mới — Owner quyết TRÊN ẢNH).

### 7.4 CÁC BƯỚC MODW (theo khuôn, KHÔNG đẻ luật mới)
1. **Đọc raw** `modw-builder-v1.html` (connector đã về, hoặc Claude Code cat). Prompt Claude Code nếu cần:
   ```
   CLAUDE CODE — chỉ ĐỌC, không sửa:
   1. ls -la /opt/incomex/docs/mcp-writes/modw-builder-v1.html
   2. grep -o 'data-region="[^"]*"' <file> | sort | uniq -c   (kỳ vọng 6 shell.dock.*)
   3. Dán raw: HTML 6 mục .psec + khối Hướng dẫn + nút Đúc + preview + modal Chọn;
      và phần <script> render chips người / item kho / item picker (để xác định template→OCC:all).
   4. KHÔNG gắn. Đưa raw về CW soạn spec → Desktop soi → rồi Claude Code mới gắn.
   ```
2. **CW soạn spec:** map ~24 mã → **chuỗi FIND thật + đếm MATCHES + OCC:first/all** (đọc raw, KHÔNG đoán — bẫy lớn nhất: FIND khớp >1 mà OCC:first = gắn nhầm). Theo **5 LUẬT** (§8) + khuôn NT1–6. Template (chip/item) → gắn trong hàm render 1 chỗ (setAttribute), hiện N instance.
3. **Desktop SOI spec** → **Claude Code GẮN** (người-sửa ≠ người-kiểm).
4. **CW nghiệm thu:** trọng tài `grep data-region` (TRỪ 6 dock) ↔ cột C = 0 thiếu; byte-check; UI không vỡ. Chỉnh `anchor_scope` PLANNED→DOM cho mã đã gắn PASS.
5. **Codex chụp màn 11,12** → cập nhật `man_hinh`.
6. **Siết concept MODW KÈM ẢNH khoanh vùng** — phần lớn đã khớp MOW sẵn qua aliases (`don_vi_to_chuc`, `quy_trinh`, `cong_viec`, `nguoi_thuc_hien`, `nguoi_nhan_bao_cao`, `duc_node`, `khuon`, `muc_con`, `vi_tri_de_xuat`…). Lật-gần-giống TRƯỚC khi tạo mới. Xử lý lỗ hổng "Hướng dẫn" (§7.3).
7. **Nghiệm thu MODW theo KHUÔN NT1–6** (§8).

---

## 8. LUẬT & RÀNG BUỘC (bắt buộc giữ)
**5 LUẬT gắn mã:** L1 template khác DỮ LIỆU→gộp 1 mã; L2 widget chung khác Ý NGHĨA→truyền tham số; L3 tĩnh→FIND→REPL; L4 DOM→setAttribute ngay sau dòng tạo; L5 nút cây→không gắn. Ranh giới L1/L2 = "khác DỮ LIỆU hay Ý NGHĨA?".

**KHUÔN NGHIỆM THU 1 UI (NT1–6)** — 1 UI "chuẩn xong" khi:
- NT1 trọng tài grep code SỐNG ↔ cột C = 0 thiếu (⚠️ phải grep code sống; không được thì ghi "dựa lần sạch gần nhất", KHÔNG tính đã tái kiểm).
- NT2 mọi khu có concept HOẶC OUT (0 khu chưa phân loại).
- NT3 cột chính đầy (ban_chat_khu·doi_tuong[/OUT]·mo_ta·pham_vi·anchor·trang_thai: 0 ô cứu-người trống).
- NT4 mọi màn/state có ảnh trong man_hinh.
- NT5 3 loại tài liệu tách bạch (định nghĩa/quy trình/vì sao). **HOW-SSOT = quy_trinh** (lệch → tin quy_trinh).
- NT6 concept mới qua lật-gần-giống; **quyết TRÙNG bằng RANH GIỚI (bản chất), KHÔNG bằng tên chung** (anh em cùng họ chung từ nhưng khác ranh giới → KHÔNG trùng).

**Nguyên tắc gốc:**
- **Địa chỉ vs Khái niệm:** `data-region` = địa chỉ (nhiều cửa nhiều mã, giữ riêng); `concept` = khái niệm (nhiều cửa → 1). **Gom KHÁI NIỆM, không gom MÃ** (chống double).
- **Concept = ĐỐI TƯỢNG, thao tác ở cột `hanh_dong`** (không đẻ concept cho mỗi nút bấm).
- **Lật-gần-giống** TRƯỚC khi tạo concept (quét sổ + bản đồ + sổ cũ `sua_re_ui_khai_niem_nhap` có tên dạng `tier.*`/`action.*`). Chống "tên thứ 3".
- **Đọc FILE SỐNG, cấm trích số nhớ** (bài học: Desktop từng trích "HELP 214" từ bản cũ — sai, vì HELP đã đổi tên `huong_dan`).
- **Khuôn–đúc:** quy trình = khuôn SỐNG; mỗi đơn vị = bản đúc TRỎ VỀ (không copy chết); sửa khuôn → mọi bản theo. Biến thể A/A' = 2 bản độc lập cùng giống loài + nút "ai dùng khuôn nào". Khác "nhiều-cha thảm hoạ".
- **4 luật vệ sinh file:** 1 chỗ ở · ghi đè không ghi chồng · tách lịch sử → Plan_luu_tru · liếc mỗi lần mở.

**KHÔNG động (phiên khác):** thiết kế PG · 4 lỗ hổng data (id mục con/parent_id/order) · 2 nút chết (`view.template`/`view.ops`) + `shell.dot` · dọn lớn `huong_dan` (chờ Owner).

**Kỹ thuật:** VPS = SSOT (không CI/push). NEVER bump `?v=`. `data-region` không đổi tùy tiện (Luật D). Backup Excel trước mỗi lần ghi. Sau khi lưu Excel: giữ comment B1/C1 nếu có.

**NỢ ĐÃ GHI (quy_trinh):** dọn `huong_dan` — dời HOW-trùng (→quy_trinh) + lịch sử đã xong (→Plan_luu_tru), giữ chỉ VÌ SAO. Làm khi Owner gật reorg.

---

## 9. ẢNH KHOANH VÙNG (khi siết concept — luật mới của Owner)
"Nhìn ảnh hiểu ngay, nhìn mô tả không hiểu" → **mọi lần trình Owner siết concept phải KÈM ẢNH khoanh vùng.** Cách làm (đã chạy được): PIL vẽ box đỏ + số lên `anh-man-hinh-ui/mow-XX.png` (bash sandbox, tìm path bằng `find`), lưu ra outputs, rồi `Read` bằng **host path** (`/Users/nmhuyen/Library/.../outputs/...png`) để tự kiểm placement, rồi `present_files`. MODW dùng ảnh màn 11,12 (Codex chụp sau khi gắn mã).

---
*Hết handoff. Bắt đầu phiên mới bằng VIỆC 1 (test connector), rồi VIỆC 2 (MODW).*
