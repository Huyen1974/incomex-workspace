# YÊU CẦU CHO CODEX — Gắn data-region cho MOIT-builder / MODIT (UI #2 của Mẹ MOIT)

**File cần sửa (VPS):** `/opt/incomex/docs/mcp-writes/ui-preview/moit-builder-v1.html`
**UI:** MOIT Builder (MODIT) — biến 1 MOIT thành chạy được: khai form + điều kiện + trigger + gắn bản ghi/người thực hiện.
**Vai:** Codex = NGƯỜI-SỬA. CW = NGƯỜI-KIỂM (verify 3-tập + điền Excel). Tách vai.

---

## 1. NGUYÊN TẮC
- `data-region` = ĐỊA CHỈ khu UI, tầng GIAO DIỆN, không gánh khái niệm.
- **KHÔNG bump `?v=`** (mot-theme?v=17, entry-engine.js?v=1, modit-entry-enhance.js?v=1, entry-savemode.js?v=1 … giữ nguyên).
- **KHÔNG sửa Excel.** **CHỈ THÊM thuộc tính** — chứng minh bằng phép thay ngược (gỡ ra = đúng byte + SHA gốc).
- Chỉ sửa 1 file: `moit-builder-v1.html`.

## 2. RANH GIỚI — QUAN TRỌNG NHẤT (giống hệt MODT đã làm)
Trang có phần dựng UI **INLINE** trong `<script>` của chính file, và cuối file **append 3 script DÙNG CHUNG**: `entry-engine.js`, `modit-entry-enhance.js`, `entry-savemode.js`.
- **3 file JS chung KHÔNG mang data-region** (chỉ `data-ee`/`data-sm`/id/class). **TUYỆT ĐỐI KHÔNG sửa 3 file này.**
- Nhưng 3 file này **tiêm DOM lúc chạy** vào trang: khu **◈ Nhập khóa ngoại (reference/FK)**, **▤ Bảng đích (target)**, **cảnh báo trùng (duplicate)**, và **chọn nơi lưu (save-mode: commit/staging)**.
- **Cách xử lý = y hệt MODT:** tag các khu engine-tiêm đó bằng họ **`modit.entry.*`**, GẮN **INLINE trong `moit-builder-v1.html`** (script nhỏ trong chính file, set `data-region` lên phần tử engine-tiêm theo id của chúng — `refSec`/`eeRefZone`/`targetCollSec`/`saveModeSec`/`ee-dup-banner`… — SAU khi engine tiêm), KHÔNG chạm vào file JS chung.
- **Đối chiếu trực tiếp `modt-builder-v1.html` (họ `modt.entry.*`: reference.design/runtime · target · save_mode · duplicate_warning)** rồi làm bản MODIT tương ứng.
- **LOẠI TRỪ**: `eco-nav.js` (dock; nạp nhiều kiểu ?v=3/?v=6/ts) + theme. Không gắn.

## 3. PREFIX & CHỐNG NHIỄM CHÉO
- **`modit.*`** cho vỏ trang (song song `modt.*` của MODT). **`modit.entry.*`** cho khu engine-tiêm (song song `modt.entry.*`).
- (Nếu ecosystem muốn `moit.builder.*` cho đồng bộ với `moit.form.*`, Codex được quyền đổi và ghi rõ trong handoff — nhưng khuyến nghị `modit.*` để song song với `modt.*` — cùng là builder MOD*.)
- Khớp ranh giới token: `modit\.`. Kiểm sau khi gắn: **0 mã lọt sang `modt.*`, `moit.form.*`, `moit.proposal.*`, `mot.*`** (chú ý `modit` ≠ `modt` ≠ `moit`).

## 4. KHUNG KHU VỰC (định hướng — Codex enumerate lá theo 5 luật + đối chiếu DOM thật)
Đặt tên `modit.<khu>.<phần>`. D=DỮ LIỆU · H=HÀNH VI · G=GIAO DIỆN.

**Vỏ**: `modit.app` (body) G · `modit.content` (.stu-wrap) G · `modit.intro` (heading+.lead) G · `modit.topbar` G + `.topbar.brand`/`.badge`/`.arch`(link Kiến trúc→moit-dataflow)/`.mottools`(link Bộ công cụ MOT) G

**Trái — Panel 1 "Nhập gì?"**: `modit.inputs` G · `.inputs.list`(#inpList) G · `.inputs.add` H · `.inputs.item`(.ifield **REP≈3**) G + lá `.item.drag`H `.item.editlabel`H `.item.label`D `.item.kit`D `.item.required`H `.item.remove`H

**Trái — Panel 2 "Gắn với gì?" (điều kiện)**: `modit.conditions` G · `.conditions.tabs`(.tabs) G + `.tabs.simple`(tbS)H `.tabs.complex`(tbC)H
- Đơn giản (#cSimple): `.conditions.simple` G · `.simple.connector`(seg2)G + `.connector.and`H `.connector.or`H · `.simple.list`(#condList)G · `.simple.item`(.crow **REP5**)G + `.item.field`(pickfld)H `.item.remove`(xr)H `.item.op`(select)H `.item.value`(input)D
- Phức tạp (#cComplex): `.conditions.complex` G · `.complex.list`(#complexBoxes)G · `.complex.item`(.tbox **REP5**)G + `.item.text`(textarea)D

**Trái — Panel 3 "Trigger?"**: `modit.trigger` G · `.trigger.list`(#trigBoxes)G · `.trigger.item`(.tbox **REP3**)G + `.item.text`(textarea)D

**Trái — Panel 4 "Gắn bản ghi"**: `modit.binding` G · `.binding.executor`(#bPic)D · `.binding.when`(#bWhen)D · `.binding.anchor`(#bAnchor pickfld, mở modal cây)H · `.binding.note`(.bind)G

**Phải — xem trước/kết quả**: `modit.preview` G · `.preview.top`(rtop)G · `.preview.title`(#fTitle)D · `.preview.title.edit`H · `.preview.cast`(⚡ Đúc biểu mẫu)**H** · `.preview.header`(.formhd)G · `.preview.code`(#fCode)D · `.preview.tier`(tchip)G · `.preview.anchor`(#fAnchorTxt)D · `.preview.executor`(#fPicTxt)D · `.preview.card`G · `.preview.zonelabel`G · `.preview.zone`(#formZone)G + `.preview.zone.cell`(.frow **REP**)G · `.preview.gate`(#gateTxt: điều kiện+trigger)G · `.preview.json`(#moldJson)D

**Modal KIT** (#kitBg): `modit.kit` G · `.kit.title`G `.kit.close`H `.kit.grid`G · `.kit.item`(.kit-card **REP12**)H + `.item.code`D `.item.name`D `.item.type`G

**Modal Kho trường/Neo 7 tầng** (#catBg): `modit.cat` G · `.cat.title`(#catTitle)G `.cat.close`H · `.cat.tiers`(#tierSelects)G + `.cat.tiers.item`(mỗi select **REP7**)H · `.cat.search`(#catSearch)H · `.cat.count`(#catCount)D · `.cat.list`(#catList)G · `.cat.item`(.fitem **REP** biến thiên)H + `.item.name`D `.item.path`D `.item.type`G

**Khu ENGINE-TIÊM (họ `modit.entry.*`, tag INLINE — mirror `modt.entry.*`)**: reference (◈ khóa ngoại) design+runtime · target (▤ bảng đích) · save_mode (commit/staging + toggle + note) · duplicate_warning. Enumerate lá theo đúng bản MODT.

## 5. TRẠNG THÁI QUÉT (DOM union)
base · mở modal KIT · mở modal cây (cả 'anchor' lẫn 'cond') · tab điều kiện Đơn-giản ↔ Phức-tạp · connector và↔hoặc · inputs rỗng · **và các state làm hiện khu `modit.entry.*`** (chọn bảng đích → reference/target hiện; bật save-mode commit/staging; duplicate warning). Bảo đảm mọi `modit.entry.*` render trong ít nhất 1 state.

## 6. SẢN PHẨM GIAO CW
1. `moit-builder-data-region-manifest.csv` — cột `ma,pham_vi,nhom,mo_ta,vi_tri_source,occurrence,trang_thai`. `pham_vi=RIENG_MODIT` (cả `modit.*` lẫn `modit.entry.*` đều tag inline trong moit-builder-v1.html). `vi_tri_source=moit-builder-v1.html:<dòng>`.
2. `moit-builder-runtime-audit.json` — `source==runtime` (0 thiếu/thừa); `boundary`: `pagePrefix="modit."`, `entryPrefix="modit.entry."`, `excluded=["eco-nav.js","shell.*"]`, `notEdited=["entry-engine.js","modit-entry-enhance.js","entry-savemode.js"]`, `edited=["moit-builder-v1.html"]` (CHỈ 1 file); states; occurrence min/max.
3. `moit-builder-data-region-handoff.md` — số mã theo D/H/G; xác nhận 3 file JS chung **sha256 KHÔNG đổi** (kèm hash trước/sau); 0 mã lọt sang `modt./moit./mot.`; không bump `?v=`; **ghi rõ hành vi nào là DEMO** (nút "Đúc biểu mẫu" = alert demo?) vs đã wire (save-mode commit/staging của entry-savemode) — để CW ghi chú vào sổ.

## 7. NGHIỆM THU (Codex tự kiểm)
- [ ] source = DOM union (mọi state, gồm các state hiện `modit.entry.*`), thiếu 0/thừa 0.
- [ ] 3 file JS chung sha256 KHÔNG đổi (chứng minh không đụng); `edited` chỉ `moit-builder-v1.html`.
- [ ] 0 mã lọt sang `modt.*`/`moit.form.*`/`moit.proposal.*`/`mot.*`; mọi mã bắt đầu `modit.`.
- [ ] eco-nav loại trừ; không bump `?v=`; thay-ngược đúng SHA gốc.

---
**Sau khi giao 3 file:** CW verify độc lập 3-tập (parse `moit-builder-v1.html` → mọi `modit.*`/`modit.entry.*`; đối chiếu DOM; xác nhận 3 JS chung y nguyên; 0 lẫn `modt./moit.`) → điền `SO_HOP_DONG` vùng Mẹ MOIT (`me=MOIT`, sau `moit.form.*`/`moit.proposal.*`, sort theo (me, sub-UI)). Codex KHÔNG động Excel.
