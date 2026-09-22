# YÊU CẦU CHO CODEX — Gắn data-region cho MODUT (modut-builder-v1) — biến MOUT chạy được

**File cần sửa (VPS):** `/opt/incomex/docs/mcp-writes/ui-preview/modut-builder-v1.html`
**UI:** MODUT — lắp ráp để một báo cáo MOUT tự chạy (chọn báo cáo nguồn + miền dữ liệu/nguồn DB + hàm DOT + kỳ/lịch + trigger + người nhận + neo 7 tầng + xuất → đúc & lên lịch).
**Vai:** Codex = NGƯỜI-SỬA. CW = NGƯỜI-KIỂM (verify 3-tập + điền Excel). Tách vai.

---

## 1. NGUYÊN TẮC
- `data-region` = ĐỊA CHỈ khu UI, tầng GIAO DIỆN, không gánh khái niệm.
- **KHÔNG bump `?v=`** (mot-theme?v=17… giữ nguyên).
- **KHÔNG sửa Excel.** **CHỈ THÊM thuộc tính** — chứng minh bằng phép thay ngược (gỡ ra = đúng byte + SHA gốc).
- Chỉ sửa 1 file: `modut-builder-v1.html`.

## 2. RANH GIỚI — file TỰ CHỨA (khác MODIT!)
Toàn bộ JS chức năng (`el`, `UI`, `App`, `TREE`, `PEOPLE`, `REPORTS`, `DOTFN`, `M`…) nằm INLINE. **Không append engine chung** — KHÁC MODIT (MODIT có `entry-engine.js`); MODUT **không có** `entry-engine`/`modit-entry-enhance`/`entry-savemode`.
- **LOẠI TRỪ**: `eco-nav.js` (dock, `?ts=`) + `guide-dock.js` (dock/guide, `?ts=`) + `mot-theme-v1.css`. Không gắn.
- Mọi khu đều RIÊNG của trang. Không có nhánh `modut.entry.*`.

## 3. PREFIX & CHỐNG NHIỄM CHÉO
- **Prefix: `modut.`** (song song `modit.*`/`modt.*`/`modw.*` — đều là builder MOD*). Thuộc Mẹ MOUT.
- **Khớp ranh giới token** `modut\.`. Kiểm sau khi gắn: **0 mã lọt sang `mout.`, `mouthome.`, `mot.`, `modt.`, `moit.`, `modit.`, `motstudio.`** (chú ý `modut` ≠ `mout` ≠ `modt`).

## 4. KHUNG KHU VỰC CẦN GẮN (khung định hướng — Codex enumerate lá theo 5 luật + đối chiếu DOM thật)
Đặt tên `modut.<khu>.<phần>`. D=DỮ LIỆU · H=HÀNH VI · G=GIAO DIỆN.

**Vỏ**: `modut.app`(body)G · `modut.content`(.stu-wrap)G · `modut.intro`(heading+.lead)G · `modut.topbar`G + `.topbar.brand`/`.topbar.badge`/`.topbar.mout`(link→mout-builder)/`.topbar.list`(link→mout-home) G

**Trái — bảng lắp ráp (7 mục):**
- ① `modut.source`(psec "Báo cáo nguồn")G · `.source.select`(#rSel)**H** · `.source.cols`(#rCols)D
- ◆ `modut.scope`(psec "Miền dữ liệu")G · `.scope.text`(#dsText)**D** · `.scope.code`(#dsCode)**D** · `.scope.source`(#dsSrc, nguồn collection DB)**H** · `.scope.note`G
- ② `modut.fn`(psec "Hàm số liệu DOT")G · `.fn.select`(#fnSel)**H** · `.fn.note`G
- ③ `modut.timing`(psec "Kỳ & Lịch chạy")G · `.timing.period`(#perSel)**H** · `.timing.schedule`(#schSel)**H** · `.timing.resolved`(#schTxt)D
- ④ `modut.triggers`(psec "Trigger sự kiện")G · `.triggers.list`(#trigList)G · `.triggers.add`(nút + Thêm trigger)**H**
  - `.triggers.item`(mỗi `.trg` **REP**)G + lá: `.item.trigger`(select mã trigger)**H** · `.item.condition`(select điều kiện)**H** · `.item.remove`(✕)**H** · `.item.desc`(textarea)**D**
- ⑤ `modut.recipients`(psec "Người nhận")G · `.recipients.list`(#recipChips)G · `.recipients.add`(nút + Thêm người nhận)**H**
  - `.recipients.item`(mỗi `.chip` **REP**)G + lá: `.item.name`(who)**D** · `.item.dept`**D** · `.item.remove`(rmc)**H**
- ⑥ `modut.anchor`(psec "Neo 7 tầng + Xuất")G · `.anchor.field`(#anchorTxt pickfld, mở modal)**H** · `.anchor.export`(cụm xuất)G + `.export.xlsx`(#exX)**H** · `.export.csv`(#exC)**H**

**Phải — bản đúc chạy được:**
- `modut.run`(cột phải)G · `.run.top`(rtop)G · `.run.title`(rtitle)G · `.run.cast`(⚡ Đúc & lên lịch)**H**
- `.run.card`(.runcard)G · `.card.header`(rc-hd)G + `.header.tier`(#cTier)D · `.header.name`(#cName)**D** · `.header.bread`(#cBread, đường 7 tầng)D
- `.card.body`(#cBody)G — các dòng render: `.body.scope`(miền dữ liệu)D · `.body.fn`D · `.body.timing`D · `.body.trigger`D · `.body.recipients`D · `.body.output`(đường dẫn + xuất)D (Codex quyết độ sâu; các giá trị = D)
- `.run.json`(#moldJson)**D**

**Modal Neo 7 tầng** (#catBg): `modut.cat`G · `.cat.title`G · `.cat.close`H · `.cat.tiers`(#tierSelects)G + `.cat.tiers.item`(mỗi select **REP7**)H · `.cat.search`(#catSearch)H · `.cat.list`(#catList)G · `.cat.item`(mỗi node **REP**)H + `.item.name`D · `.item.tier`D

**Modal Người nhận** (#pBg): `modut.people`G · `.people.title`G · `.people.close`H · `.people.search`(#pSearch)H · `.people.list`(#pList)G · `.people.item`(mỗi người **REP**)H + `.item.name`D · `.item.dept`D · `.item.role`D

> Phân nhóm: builder nhiều H (chọn báo cáo/nguồn/hàm/kỳ/lịch, thêm-xoá trigger, thêm-xoá người nhận, chọn export, mở modal, chọn neo/người, đúc) + D (miền dữ liệu, mã, giá trị trigger/desc, tên-bộ phận người nhận, neo, đường dẫn, JSON, các dòng bản đúc) + G (container/khu/nhãn/card).

## 5. TRẠNG THÁI QUÉT (DOM union)
base · đổi báo cáo nguồn (#rSel) · mở modal Neo 7 tầng · mở modal Người nhận · thêm/xoá trigger · thêm/xoá người nhận · đổi kỳ/lịch · bật/tắt export xlsx/csv · bấm **Đúc & lên lịch** (nếu có đổi DOM). Union tất cả state (bảo đảm trigger.item, recipients.item, cat.item, people.item đều render trong ít nhất 1 state).

## 6. SẢN PHẨM GIAO CW
1. `modut-builder-data-region-manifest.csv` — cột `ma,pham_vi,nhom,mo_ta,vi_tri_source,occurrence,trang_thai`. `pham_vi=RIENG_MODUT`, `trang_thai=BUILT`, `vi_tri_source=modut-builder-v1.html:<dòng>`.
   - **QUAN TRỌNG (đọc được):** ghi manifest **UTF-8 thuần**, trong `mo_ta` **ĐỪNG dùng ký tự "›"** (dùng ">" / "/" / " - "). (Manifest MODIT dùng "›" bị connector chặn nhầm là binary — lần MOUT đã bỏ "›" và đọc sạch.)
2. `modut-builder-runtime-audit.json` — `source==runtime` (0 thiếu/thừa); `boundary`: `pagePrefix="modut."`, `excluded=["eco-nav.js","guide-dock.js","shell.*"]`, `edited=["modut-builder-v1.html"]` (chỉ 1 file); states; occurrence min/max. **Giữ file < 50KB nếu được** (audit lớn bị cắt khi CW đọc).
3. `modut-builder-data-region-handoff.md` — số mã theo D/H/G; xác nhận 0 mã lọt sang `mout./mouthome./mot./modt./moit./modit.`; không bump `?v=`; snapshot/commit id; phép thay-ngược; **ghi rõ hành vi DEMO** (nút "Đúc & lên lịch" = alert demo? / còn gì demo) để CW ghi chú vào sổ.

## 7. NGHIỆM THU (Codex tự kiểm)
- [ ] source = DOM union (mọi state), thiếu 0/thừa 0.
- [ ] 0 mã lọt sang `mout.*`/`mouthome.*`/`mot.*`/`modt.*`/`moit.*`/`modit.*`/`motstudio.*`; mọi mã bắt đầu `modut.`.
- [ ] `eco-nav.js` + `guide-dock.js` loại trừ; không bump `?v=`; thay-ngược đúng SHA gốc.
- [ ] manifest UTF-8, mô tả không có "›".

---
**Sau khi giao 3 file:** CW verify độc lập 3-tập (parse `modut-builder-v1.html` → mọi `modut.*`; đối chiếu DOM; xác nhận không lẫn `mout./mouthome./modit.`) → điền `SO_HOP_DONG` **vùng Mẹ MOUT** (`me=MOUT`, sau `mout.*`, sort theo (me, sub-UI)). Codex KHÔNG động Excel.
