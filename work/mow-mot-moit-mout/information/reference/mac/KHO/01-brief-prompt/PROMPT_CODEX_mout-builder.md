# YÊU CẦU CHO CODEX — Gắn data-region cho MOUT Builder (mout-builder-v3)

**File cần sửa (VPS):** `/opt/incomex/docs/mcp-writes/ui-preview/mout-builder-v3.html`
**UI:** MOUT Builder — quét điều kiện → đúc ra báo cáo dùng được ngay (chọn cột, lọc, thời gian, tổng → đúc báo cáo, tải CSV/Excel, lưu hệ thống + phân phối).
**Vai:** Codex = NGƯỜI-SỬA. CW = NGƯỜI-KIỂM (verify 3-tập + điền Excel). Tách vai.

---

## 1. NGUYÊN TẮC
- `data-region` = ĐỊA CHỈ khu UI, tầng GIAO DIỆN, không gánh khái niệm.
- **KHÔNG bump `?v=`** (mot-theme?v=17… giữ nguyên).
- **KHÔNG sửa Excel.** **CHỈ THÊM thuộc tính** — chứng minh bằng phép thay ngược (gỡ ra = đúng byte + SHA gốc).
- Chỉ sửa 1 file: `mout-builder-v3.html`.

## 2. RANH GIỚI — file TỰ CHỨA
Toàn bộ JS chức năng (`el`, `UI`, `App`, `FIELDS`, `ENT`, `M`, `resolvePeriod`…) nằm INLINE trong chính file. **Không mượn engine chung** (không master-list.js, không entry-engine.js, không mout-render).
- **LOẠI TRỪ**: `eco-nav.js` (dock, `?ts=`) + `mot-theme-v1.css` (theme). Không gắn.
- Mọi khu đều là RIÊNG của trang.

## 3. PREFIX & CHỐNG NHIỄM CHÉO
- **Đề xuất prefix: `mout.`** (trang này = công cụ MOUT chính, tự chứa — song song `mot.*` của MOT dashboard).
- (Trang chị em `mout-home` sau sẽ là `mouthome.*` — mượn `master.*`. Nếu Codex đã có scheme khác cho họ MOUT thì chỉnh và ghi rõ trong handoff.)
- **Khớp ranh giới token** `mout\.` — KHÔNG `startswith("mout")` (sẽ nuốt nhầm `mouthome.*`). Kiểm sau khi gắn: **0 mã lọt sang `mot.`, `modt.`, `motstudio.`, `motmaster.`, `moit.`, `modit.`, `mouthome.`** (chú ý `mout` ≠ `mot`).

## 4. KHUNG KHU VỰC CẦN GẮN (khung định hướng — Codex enumerate lá theo 5 luật + đối chiếu DOM thật)
Đặt tên `mout.<khu>.<phần>`. D=DỮ LIỆU · H=HÀNH VI · G=GIAO DIỆN.

**Vỏ**: `mout.app` (body) G · `mout.content` (.stu-wrap) G · `mout.intro` (heading+.lead) G · `mout.topbar` G + `.topbar.brand`(logo)/`.topbar.badge`/`.topbar.master`(link ▤ Danh sách master→mout-home)/`.topbar.mow`/`.topbar.mot` G

**Trái — khuôn báo cáo:**
- `mout.scope` (psec "Miền dữ liệu") G · `.scope.text`(#dsText)**D** · `.scope.code`(#dsCode)**D** · `.scope.hint`(.wild) G
- `mout.columns` (psec "Cột báo cáo") G · `.columns.count`(#colCnt)D · `.columns.list`(#colList)G · `.columns.add`(nút + Thêm cột)**H** · `.columns.hint` G
  - `.columns.item` (mỗi `.colchip` **REP≈6**) G + lá: `.item.drag`H · `.item.visibility`(hiện/ẩn)H · `.item.name`(.nm)**D** · `.item.type`(.ty)G · `.item.sum`(Σ)H · `.item.remove`(✕)H
- `mout.filters` (psec "Điều kiện lọc") G · `.filters.count`(#filtCnt)D · `.filters.list`(#filtList)G · `.filters.hint` G
  - `.filters.item` (mỗi `.frule` **REP5**) G + lá: `.item.field`(pickfld)H · `.item.remove`(xr)H · `.item.op`(select)H · `.item.value`(input)**D**
- `mout.time` (psec "Thời gian") G · `.time.mode`(.tmode)G + `.mode.once`(tmCu)H · `.mode.recurring`(tmDk)H
  - `.time.once`(#tCu)G: `.once.field`(#timeFldCu, mở modal)H · `.once.from`(#tFrom)**D** · `.once.to`(#tTo)**D**
  - `.time.recurring`(#tDk)G: `.recurring.field`(#timeFldDk)H · `.recurring.period`(#tPreset)H · `.recurring.dayrange`(#dayRangeRow: dr1/dr2)**D** · `.recurring.schedule`(#tSched)H · `.recurring.resolved`(#tResolved)D
- `mout.totals` (psec "Tổng") G · `.totals.rowtotal`(#rowTotTog)H · `.totals.hint` G
- `mout.note`(.callout) G

**Phải — bản đúc / kết quả:**
- `mout.report` (cột phải) G · `.report.top`(rtop)G · `.report.title`(#rTitle)**D** · `.report.title.edit`(✎)H · `.report.cast`(⚡ Đúc báo cáo)**H** · `.report.titlehint` G
- `.report.scope`(#rScope, banner miền dữ liệu trên báo cáo)D
- `.report.export`(rtop tải)G + `.export.csv`(nút CSV)**H** · `.export.xls`(nút Excel)**H** · `.export.meta`(#metaInfo)D
- `.report.table`(#rptTbl bảng số liệu)G + lá render: `.table.header`G · `.table.row`(**REP** theo dòng)G · `.table.cell`(D các ô số liệu) · `.table.total`(dòng Σ)G — (Codex quyết độ sâu, tối thiểu tới row/total)
- `.report.castbox`(#castBox, hiện sau khi đúc)G + `.castbox.url`(#castUrl)**D** · `.castbox.scope`(#castScope)D · `.castbox.schedule`(#castSched)D · `.castbox.distribute`(#castDist)D
- `.report.json`(#moldJson khuôn JSON)**D**

**Modal Kho trường / 7 tầng** (#catBg): `mout.cat` G · `.cat.title`(#catTitle)G · `.cat.close`H · `.cat.tiers`(#tierSelects)G + `.cat.tiers.item`(mỗi select **REP7**)H · `.cat.search`(#catSearch)H · `.cat.count`(#catCount)D · `.cat.list`(#catList)G · `.cat.item`(mỗi `.fitem` **REP** biến thiên)H + `.item.name`D · `.item.path`D · `.item.type`G

> Phân nhóm: builder nên nhiều H (add/remove/toggle-visibility/Σ/drag/cast/download/mode/period/schedule/pick) + D (miền dữ liệu, giá trị cột/lọc/ngày, ô bảng, URL đúc, JSON, đếm) + G (container/khu/nhãn/bảng-khung).

## 5. TRẠNG THÁI QUÉT (DOM union)
base · mở modal kho trường (target col / filter / time) · thời gian Cụ-thể ↔ Định-kỳ (+ chọn kỳ 'dayrange' hiện dr1/dr2) · bật/tắt cột (visibility) · bật Σ cột · bật 'Tổng hàng' · thêm/xoá cột · thêm/xoá điều kiện lọc · bấm **Đúc báo cáo** (hiện castBox) · bảng rỗng (lọc không khớp). Union tất cả state (bảo đảm castBox + dòng Σ + Tổng hàng đều render trong ít nhất 1 state).

## 6. SẢN PHẨM GIAO CW
1. `mout-builder-data-region-manifest.csv` — cột `ma,pham_vi,nhom,mo_ta,vi_tri_source,occurrence,trang_thai`. `pham_vi=RIENG_MOUT`, `trang_thai=BUILT`, `vi_tri_source=mout-builder-v3.html:<dòng>`.
   - **QUAN TRỌNG (đọc được):** ghi manifest **UTF-8 thuần** và trong `mo_ta` **ĐỪNG dùng ký tự "›"** (dùng ">" hoặc "/" hoặc " - "). Manifest MODIT dùng "›" bị connector chặn nhầm là "binary", CW phải moi qua trình duyệt rất mất công.
2. `mout-builder-runtime-audit.json` — `source==runtime` (0 thiếu/thừa); `boundary`: `pagePrefix="mout."`, `excluded=["eco-nav.js","shell.*"]`, `edited=["mout-builder-v3.html"]` (chỉ 1 file); states; occurrence min/max.
3. `mout-builder-data-region-handoff.md` — số mã theo D/H/G; xác nhận 0 mã lọt sang `mot./modt./moit./modit./mouthome.`; không bump `?v=`; snapshot/commit id; phép thay-ngược; **ghi rõ hành vi DEMO** (nút "Đúc báo cáo" chỉ hiện castBox demo, chưa lưu thật? / tải CSV-Excel có chạy thật) để CW ghi chú vào sổ.

## 7. NGHIỆM THU (Codex tự kiểm)
- [ ] source = DOM union (mọi state, gồm castBox + Σ + Tổng hàng), thiếu 0/thừa 0.
- [ ] 0 mã lọt sang `mot.*`/`modt.*`/`motstudio.*`/`motmaster.*`/`moit.*`/`modit.*`/`mouthome.*`; mọi mã bắt đầu `mout.`.
- [ ] `eco-nav.js` loại trừ; không bump `?v=`; thay-ngược đúng SHA gốc.
- [ ] manifest UTF-8, mô tả không có "›".

---
**Sau khi giao 3 file:** CW verify độc lập 3-tập (parse `mout-builder-v3.html` → mọi `mout.*`; đối chiếu DOM; xác nhận không lẫn `mot./moit./mouthome.`) → điền `SO_HOP_DONG` **vùng Mẹ MOUT** (`me=MOUT`, cột mới, sort theo (me, sub-UI)). Codex KHÔNG động Excel.
