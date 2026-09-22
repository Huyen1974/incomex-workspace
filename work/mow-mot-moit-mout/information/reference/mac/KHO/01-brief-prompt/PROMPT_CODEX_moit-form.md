# YÊU CẦU CHO CODEX — Gắn data-region cho MOIT-form (UI #1 của Mẹ MOIT)

**File cần sửa (VPS):** `/opt/incomex/docs/mcp-writes/ui-preview/moit-form-v1.html`
**UI:** MOIT — tạo form nhập liệu (giao diện để xem & thao tác). Là phần UI/sản phẩm cuối; muốn chạy thật thì sang MODIT (moit-builder).
**Vai:** Codex = NGƯỜI-SỬA (gắn mã trên VPS). CW = NGƯỜI-KIỂM (verify độc lập 3-tập + điền Excel). Hai vai tách nhau.

---

## 1. NGUYÊN TẮC (bắt buộc)
- `data-region` = ĐỊA CHỈ/mỏ neo một khu trên UI, tầng GIAO DIỆN. **Không gánh khái niệm nghiệp vụ.**
- **KHÔNG bump `?v=`** của file nào (mot-theme?v=17… giữ nguyên).
- **KHÔNG sửa Excel** (CW làm). **KHÔNG đổi hành vi/CSS/logic** — chỉ THÊM thuộc tính `data-region`. Chứng minh bằng phép thay ngược (gỡ thuộc tính ra thì tái tạo đúng byte gốc).
- Chỉ sửa đúng 1 file HTML nêu trên.

## 2. RANH GIỚI — file này TỰ CHỨA
Toàn bộ JS chức năng (`el`, `UI`, `App`, `KIT`, `KITMAP`, `M`, `widget`) nằm NGAY trong `moit-form-v1.html`. **Không mượn engine dùng chung** (không master-list.js, không entry-engine.js). Vì vậy:
- **LOẠI TRỪ**: `eco-nav.js` (dock, nạp bằng `?ts=`), `guide-dock.js` (dock/guide, nạp bằng `?ts=`), `mot-theme-v1.css` (theme). Không gắn.
- Không có phần "borrow" — mọi khu đều là RIÊNG của trang này.

## 3. PREFIX & CHỐNG NHIỄM CHÉO
- **Đề xuất prefix: `moit.form.`** (tất cả khu của UI này). Lý do: giữ Mẹ MOIT dưới một prefix `moit.` (đồng bộ với 5 mã `moit.proposal.*` đã có trong sổ), sub-namespace `.form.` để phân biệt.
- **Nếu Codex đã có sơ đồ prefix riêng cho 4 UI Mẹ MOIT** (vd mỗi UI 1 prefix như modt/motstudio), cứ chỉnh theo scheme đó và **ghi rõ trong handoff** — miễn thỏa: (a) thuộc Mẹ MOIT, (b) KHÔNG đụng `moit.proposal.*` đang tồn tại (5 mã, NOT_BUILT), (c) token-boundary rõ ràng.
- **Khớp ranh giới token** `moit\.form\.` (không `startswith("moit")` — sẽ nuốt `moit.proposal.`). Kiểm sau khi gắn: 0 mã lọt sang `moit.proposal.*`, `modit.*`, hay `mot.*` (chú ý `moit` ≠ `mot`, đừng để lẫn).

## 4. KHUNG KHU VỰC CẦN GẮN (khung định hướng — Codex enumerate lá theo 5 luật, thêm/bớt cho khớp DOM thật)
Đặt tên `moit.form.<khu>.<phần>`. Gợi ý nhóm ghi kèm (D=DỮ LIỆU, H=HÀNH VI, G=GIAO DIỆN).

**Vỏ trang**
- `moit.form.app` (body.mot) G · `moit.form.content` (.stu-wrap) G · `moit.form.intro` (.lead) G
- `moit.form.topbar` G · `.topbar.brand` (.logo) G · `.topbar.badge` (.vbadge) G · `.topbar.modit` (link MODIT) G · `.topbar.mottools` (link Bộ công cụ MOT) G

**Cột trái — bộ dựng (`.build` trái)**
- `moit.form.fields` (psec "Trường nhập") G · `.fields.list` (#inpList) G · `.fields.add` (nút + Thêm trường) **H**
- `moit.form.fields.item` (mỗi `.ifield`) **REPEATABLE(7 mặc định)** G, kèm lá:
  - `.item.drag` (⠿ kéo đổi thứ tự) H · `.item.editlabel` (✎) H · `.item.label` (input nhãn) **D** · `.item.kit` (mã F01…) **D** · `.item.required` (BB) **H** · `.item.fullwidth` (↔) **H** · `.item.remove` (✕) **H**
- `moit.form.layout` (psec "Khung sắp xếp") G · `.layout.switch` (#laySw) G · `.layout.switch.item` (mỗi nút L1–L4) **REPEATABLE(4) H**
- `moit.form.next` (psec "Bước tiếp") G · `.next.modit` (link sang MODIT) G

**Cột phải — xem trước / kết quả (`.build` phải)**
- `moit.form.preview` (cả cột phải) G
- `.preview.title` (#fTitle) **D** · `.preview.title.edit` (✎ pen) H · `.preview.save` (⚡ Lưu form) **H**
- `.preview.header` (.formhd) G · `.preview.code` (#fCode MOIT-FORM-0001) **D** · `.preview.layouttext` (#fLayTxt) G · `.preview.count` (#fCnt) **D**
- `.preview.card` (.formcard) G · `.preview.zonelabel` (.zlbl) G · `.preview.zone` (#formZone) G
  - `.preview.zone.cell` (mỗi `.cell` render ra) **REPEATABLE(7)** G — (widget bên trong là ô nhập của form; Codex quyết độ sâu, tối thiểu tới cell)
- `.preview.footer` (.z-ft) G · `.preview.footer.done` (nút Hoàn thành) **H**
- `.preview.json` (#moldJson — form_schema xuất ra) **D**

**Modal bộ công cụ KIT (`#kitBg`)**
- `moit.form.kit` (modal) G · `.kit.title` (h3) G · `.kit.close` (×) H · `.kit.grid` (#kitGrid) G
- `.kit.item` (mỗi `.kit-card`) **REPEATABLE(12: F01–F10 + E01/E02) H** (bấm = thêm trường), kèm lá: `.item.code` (.kc) D · `.item.name` (.kn) D · `.item.type` (.kt) G

> Lưu ý phân nhóm: đây là UI dựng-form (builder), nên vừa có nút thao tác (H: add/remove/toggle/layout/drag/save/done/open-close kit) vừa có dữ liệu (D: nhãn trường, mã KIT, mã form, số đếm, JSON schema). Container/khu/nhãn = G.

## 5. TRẠNG THÁI CẦN QUÉT (DOM union cho runtime-audit)
base (7 trường, L2) · mở modal KIT · đổi layout L1/L3/L4 · form RỖNG (xoá hết trường → `.empty-f`) · một trường bật full-width + required. Union tất cả state.

## 6. SẢN PHẨM GIAO CW (đặt cùng thư mục ui-preview/, tên song song các vòng trước)
1. **`moit-form-data-region-manifest.csv`** — cột: `ma,pham_vi,nhom,mo_ta,vi_tri_source,occurrence,trang_thai`. `pham_vi=RIENG_MOIT_FORM` (không có phần dùng chung), `trang_thai=BUILT`, `vi_tri_source=moit-form-v1.html:<dòng>`.
2. **`moit-form-runtime-audit.json`** — `source.count == runtime.count` (thiếu 0/thừa 0); `boundary`: `pagePrefix="moit.form."`, `excluded=["eco-nav.js","guide-dock.js","shell.*"]`, `edited=["moit-form-v1.html"]` (chỉ 1 file); liệt kê states đã quét; occurrence min/max mỗi mã.
3. **`moit-form-data-region-handoff.md`** — tóm tắt: số mã đã gắn theo nhóm D/H/G, prefix dùng (xác nhận/điều chỉnh so với đề xuất `moit.form.`), xác nhận 0 mã lọt sang `moit.proposal./modit./mot.`, không bump `?v=`, snapshot/commit id, và phép thay-ngược (chỉ-thêm-thuộc-tính).

## 7. NGHIỆM THU (Codex tự kiểm trước khi giao — CW kiểm lại độc lập)
- [ ] source (mọi `data-region` gắn) = DOM union (mọi state), thiếu 0/thừa 0.
- [ ] 0 mã lọt sang `moit.proposal.*` / `modit.*` / `mot.*`; mọi mã mới bắt đầu đúng `moit.form.`.
- [ ] `eco-nav.js` + `guide-dock.js` loại trừ (0 mã dock).
- [ ] Không bump `?v=`; chỉ-thêm-thuộc-tính (thay ngược ra đúng byte gốc).
- [ ] occurrence khớp: fields.item ≈7, layout.switch.item=4, kit.item=12, zone.cell theo số trường.

---
**Sau khi Codex giao 3 file:** CW verify độc lập 3-tập (parse `moit-form-v1.html` → mọi `moit.form.*`; đối chiếu DOM union; xác nhận không lẫn `moit.proposal./modit./mot.`) → rồi **điền vào `SO_HOP_DONG` ở vùng Mẹ MOIT** (cột `me=MOIT`, sau `moit.proposal.*`, sort theo (me, sub-UI)). Codex KHÔNG động Excel.
