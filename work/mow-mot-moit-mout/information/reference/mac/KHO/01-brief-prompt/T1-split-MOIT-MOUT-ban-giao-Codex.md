# T1 SPLIT ①/② (MOIT/MOUT) — BÀN GIAO CODEX

> Mục tiêu: **Công việc (T1) tách 2 phần: ① Nhập liệu — MOIT · ② Tham khảo — MOUT**, ĐỒNG BỘ ở CẢ 3 NƠI. Làm 1 nơi mà nơi khác lệch = hỏng. Chỉ đụng T1; T2 (bảng thời gian) và T3–T7 giữ nguyên.
>
> Chia việc: **Claude đã xong phần `mvx-v3.js` (đề xuất nâng cao)** và định nghĩa HỢP ĐỒNG dữ liệu. **Codex làm phần còn lại trong canvas HTML** (Claude không đọc/ghi an toàn được file 116KB > giới hạn 50KB).

---

## 0. HỢP ĐỒNG DỮ LIỆU (SSOT — mọi nơi bám theo)

Mỗi **con của T1** mang thêm một trường:

```
_kind: 'in' | 'ref'      // mặc định 'in' nếu thiếu
```

- `'in'`  → thuộc **① Nhập liệu — MOIT** (trường phải nhập, việc cần làm).
- `'ref'` → thuộc **② Tham khảo — MOUT** (trường chỉ để xem).

Quy tắc đọc an toàn ở mọi chỗ: `var kind = (c._kind==='ref' ? 'ref' : 'in');`

`_kind` phải **đi xuyên suốt**: D (node T1) → `startEdit` → `editSt.children` → `submitEdit`/proposal → và ngược lại. Nếu mất `_kind` ở bất kỳ khâu nào thì 3 nơi sẽ lệch.

---

## 1. CLAUDE ĐÃ LÀM (tham chiếu để khớp) — file `mvx-v3.js`

Build tag mới: `window.MVX_BUILD = 'mvx-v3.3-t1split-20260723'`. Chỉ nhánh **T1** đổi; T2/T37 nguyên.

- `buildDraft`: mỗi row đọc `kind:(c._kind==='ref'?'ref':'in')`.
- `renderForm`: T1 → `bodyT1()` + `drawT1()` (T2 vẫn `bodyT2/drawRows`, T37 vẫn `bodyT37/drawSimple`).
- `bodyT1()`: 2 khối có nhãn ①/② + badge đếm + nút thêm riêng mỗi khối; danh sách dài cuộn trong khung.
- `drawT1()`: lọc `d.rows` theo `kind`, đổ vào `#mvx-rows-in` / `#mvx-rows-ref`, cập nhật badge `#mvx-cnt-in` / `#mvx-cnt-ref`.
- Mỗi trường có nút chuyển khối `mvx.toggleKind(id)` (nhãn `→ tham khảo` / `→ nhập`); thêm trường `mvx.addFieldT1('in'|'ref')`.
- `childrenForSave`: ghi `_kind:(r.kind==='ref'?'ref':'in')` → **đây là chỗ `_kind` được đẩy ra**. Canvas cần GIỮ trường này khi nhận proposal.
- `buildRecord` (T1): thêm `rec.moit=[...]`, `rec.mout=[...]`; màn "Xem lại" nhóm ①/②.

**Đã verify trực quan:** render ①/②, toggle qua lại, badge đếm, 13 trường cuộn trong khung không vỡ layout, Gửi đề xuất + màn cảm ơn + recap OK; T2 nguyên vẹn.

---

## 2. CODEX LÀM — trong `mow-unified-canvas-v2.html` (CHỈ T1)

### 2A. Mô hình dữ liệu `_kind`
- Node T1 trong `D`: mỗi con thêm `_kind` (mock hiện tại đặt mặc định 'in'; có thể set vài con demo = 'ref' để thấy khối ②).
- `startEdit(node)` khi tier T1: copy `_kind` vào `editSt.children[i]` (đừng rơi trường này).
- `submitEdit` / nơi dựng proposal: **giữ nguyên `_kind`** của từng con khi ghi ra (đừng chỉ pick `code/title/tl`). Nhờ vậy khi mở lại đề xuất nâng cao, `mvx.buildDraft` đọc đúng khối.

### 2B. Thẻ READ-MODE ("ở ngoài") — T1
Khi render `.child-list` của một thẻ **T1** (read mode, con là `.ci`): chia 2 nhóm, mỗi nhóm có tiêu đề + badge đếm:
- **① Nhập liệu — MOIT**  `<badge = số con kind!=='ref'>`
- **② Tham khảo — MOUT**  `<badge = số con kind==='ref'>`
- Nhóm rỗng: hiện dòng mờ "— chưa có —".
- Danh sách dài: mỗi nhóm bọc khung cuộn (`max-height:240px; overflow:auto`) để trang không tràn.
- T2/T3–T7: render như cũ (KHÔNG chia).

### 2C. Thẻ INLINE "đề xuất cải tiến" (`.card.editing`) — T1
Cấu trúc hiện có (đã soi): `.card.editing[data-region="mow.propose.improve"]` › `input.edit-title` › `.child-list` › nhiều `.edit-row[draggable][data-vi=N]` (mỗi row có `.drag-handle` + input tên + nút ✕) › nút "Thêm mục" › "Huỷ" / "Gửi đề xuất". (Các nút này dùng listener ủy quyền, không phải onclick.)

Đổi cho T1:
- Chia `.child-list` thành 2 khối ①/② y như 2B (tiêu đề + badge + khung cuộn).
- Mỗi `.edit-row` thêm 1 nút nhỏ chuyển khối: nhãn `→ tham khảo` (khi đang 'in') / `→ nhập` (khi đang 'ref'); bấm → đổi `_kind` con đó → re-render.
- Mỗi khối có nút thêm riêng: **＋ Thêm trường nhập** (tạo con `_kind:'in'`) và **＋ Thêm trường tham khảo** (tạo con `_kind:'ref'`) — thay cho nút "Thêm mục" chung ở T1.
- Kéo thả (drag) trong T1: có thể tắt cho gọn (bản modal đã bỏ drag ở T1). Nếu giữ, chỉ cho kéo trong cùng khối.
- Giữ ✕ xoá, input tên như cũ.

### 2D. Đồng bộ hình thức (khớp modal — dùng đúng bộ màu/format sau)
Nhãn khối, badge, khung cuộn theo đúng bản modal để 3 nơi nhìn như một:

```css
/* nhãn khối */
.t1-lbl{display:flex;align-items:center;gap:7px;font-size:12.5px;font-weight:700;color:#1d1d1f;margin:0 0 8px}
.t1-lbl .h{font-weight:400;font-size:10.5px;color:#86868b}      /* phụ đề mờ */
.t1-lbl.in  .t1-no{color:#3b6d11}   /* ① xanh */
.t1-lbl.ref .t1-no{color:#8a6d00}   /* ② vàng nâu */
.t1-no{font-weight:800}
.t1-cnt{font-size:10px;font-weight:700;color:#86868b;background:#f0f0f2;border-radius:99px;padding:1px 8px}  /* badge đếm */
/* khung cuộn danh sách dài */
.t1-rows{max-height:240px;overflow:auto;border:1px solid #ececf0;border-radius:9px;padding:6px;background:#fafafa}
.t1-empty{font-size:11.5px;color:#a1a1a6;padding:8px 6px}
/* nút chuyển khối */
.t1-kind{font-size:10.5px;font-weight:600;color:#6e6e73;background:#fff;border:1px solid rgba(0,0,0,.12);border-radius:7px;padding:4px 8px;cursor:pointer;white-space:nowrap}
.t1-kind:hover{border-color:#639922;color:#3f7d12;background:#f3f8ea}
```

Nhãn chuẩn: `① Nhập liệu — MOIT` (phụ đề: `· việc cần làm: các trường phải nhập`) · `② Tham khảo — MOUT` (phụ đề: `· thông tin tham khảo: các trường chỉ để xem`).

### 2E. CACHE — bump version
Trong canvas HTML đổi:
```
<script src="./mvx-v3.js?v=5"></script>   →   <script src="./mvx-v3.js?v=6"></script>
```
Để reload thường nạp `mvx-v3.js` mới (bản có split modal). (Claude đã lưu file mới ở `?v=5` trên server; chỉ cần đổi số version để phá cache.)

---

## 3. NGHIỆM THU (cả 3 nơi phải khớp)
1. Thẻ read-mode T1: thấy ① MOIT / ② MOUT + badge đúng số.
2. Thẻ inline cải tiến T1: chia ①/②, chuyển trường qua lại, thêm trường đúng khối, danh sách dài cuộn không vỡ.
3. Đề xuất nâng cao T1 (modal): đã xong — mở lại phải khớp hệt (cùng con, cùng khối).
4. Con để 'ref' ở nơi này, mở nơi kia vẫn nằm khối ② (nhờ `_kind` xuyên suốt).
5. T2/T3–T7: không đổi.

---
*Hợp đồng chốt: `_kind ∈ {in,ref}` mặc định `in`. Mọi nơi đọc/ghi giữ nguyên trường này.*
