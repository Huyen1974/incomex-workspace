# INCOMEX — AGENTS.md

## QUY TẮC #1 — ĐỌC SKILL TRƯỚC
Đọc `.claude/skills/incomex-rules.md` (36 mục, 8 bước).
search_knowledge TRỰC TIẾP main process. CẤM background agent.

## QUY TẮC #2 — LÀM THEO SKILL
- Bước 0: nền tảng (3 câu tuyên ngôn + 9 nguyên tắc)
- Bước 1-2: đọc + thiết kế TRƯỚC khi code
- Bước 3: code (rào chắn: DOT 100%, dual-trigger, metadata>code)
- Bước 4-5: 2 mũ + verify production PASTE OUTPUT THẬT
- Bước 6: report gạch từng bước + evidence. Thiếu evidence = FAIL.
- MERGE ≠ DONE. Chỉ DONE khi verify production PASS.

## BẮT BUỘC
1. Đọc OR: search_knowledge("operating rules SSOT")
2. Đọc Hiến pháp: search_knowledge("hiến pháp v4.0 constitution")
3. Đọc luật liên quan đến mission
4. Tuân thủ 36 mục trong .claude/skills/incomex-rules.md
5. Report tại knowledge/current-state/reports/

## QUY TRÌNH
Quy trình 2 mũ (§0-W) = BẮT BUỘC. MERGE ≠ DONE.
Chi tiết 8 bước: xem .claude/skills/incomex-rules.md

## CẤM
- ALTER TABLE trực tiếp
- Code logic trong Nuxt
- INSERT SQL tay (phải qua DOT)
- Viện dẫn DFL v1.1 hoặc Hiến pháp v3.9
- Background agent / Task
- Chỉ ghi "PASS" không paste output (AP-02)

## TECH STACK
- PG 16 DUY NHẤT (MySQL RETIRED)
- Directus CMS + API
- Nuxt 3 (chỉ đọc)
- Agent Data + Qdrant
- VPS Contabo EU, Docker

---

## LAM DEN DAU GHI DEN DO — ghi tai cho, theo mot khuon (DEL-1D, 2026-08-01)

Nguyen tac bat buoc cho moi phien lam viec, uu tien cao hon moi muc khac.

**Phat hien dieu gi moi thi ghi NGAY vao DUNG CHO vua phat hien.**
Khong gom lai cuoi phien. Khong chi ghi vao bao cao.

Muc dich: agent sau mo vat do ra la HIEU NGAY, chi can xac nhan ghi chu da du chua —
khong phai dieu tra lai tu dau.

Cai gia cua viec khong ghi tai cho da tra that: chuyen file `.bak` lan vao lenh song
tung duoc phat hien mot lan, nhung khong ghi tai cho, nen ba luot sau van dem sai
304 thay vi 228.

### Ghi vao dau

| Loai vat | Ghi vao |
|---|---|
| Bang / ham / trigger / view / cot | `COMMENT ON ...`, **cong don** vao nhan co san |
| Database | `COMMENT ON DATABASE` |
| Schema | `COMMENT ON SCHEMA` |
| File, script, DOT | comment o **dau file** |
| Thu muc | `00-NHAN-THU-MUC.md` |
| Cron | comment ngay tren dong job do |

Ghi vao ledger la **THEM**, khong **THAY THE** viec ghi tai cho.

### Khuon ghi chu thong nhat

```
PHAT HIEN: <ngay> · <vong kiem thu may>
LA GI:     <mo ta ngan, mot cau, nguoi khong biet gi cung hieu>
BANG CHUNG:<lenh hoac so lieu de kiem chung lai>
HE QUA:    <neu dong vao thi sao / neu bo qua thi sao>
TRANG THAI:<da xac nhan | con nghi ngo | cho chu he thong quyet>
```

Viet tieng Viet khong dau, ngan gon, tranh thuat ngu khong can thiet.

### Ba dieu de quen

1. **`COMMENT ON` luon GHI DE.** Muon cong don phai doc `obj_description()` truoc roi
   noi chuoi. DEL-1D da vap dung loi nay: mot lenh `COMMENT ON TABLE pivot_results`
   khong cong don da xoa mat nhan `HE-PIVOT` cua vong truoc (phep dem tut 19 → 18).
   Da khoi phuc, nhung dung vap lai.
2. **Ghi ca cai sai cua chinh minh.** Moi lan bao PASS trong khi viec chua xay ra,
   moi lenh tra ket qua sai, deu phai ghi vao muc "BAY DA GAP" cua ho so lien quan.
3. **Ghi ngay khi phat hien.** Neu phien bi ngat giua chung, phan da dieu tra van
   phai con nguyen tai cho — khong nam trong dau, khong nam trong log tam.

---

## NHAN LA BAN GOC, BAO CAO LA MUC LUC (DEL-1E, 2026-08-01)

Ban goc cua moi ket luan nam trong **NHAN tai chinh vat** (`COMMENT ON` cho bang/ham/
trigger/view/cot/database/schema · chu thich dau file cho script/DOT · `00-NHAN-THU-MUC.md`
cho thu muc · chu thich tren dong cron). File bao cao chi la **muc luc**.
**Neu bao cao va nhan lech nhau: TIN NHAN.**

Thuoc do mot nhan dat chuan — mo mot vat bat ky ra, doc nhan cua no, phai tra loi duoc
**5 cau** ma KHONG can mo file nao khac:
1. Vat nay la gi, thuoc bo nao?
2. No con song khong — **so GHI va so DOC**, khong chi mot trong hai?
3. Xoa no thi cai gi chet theo?
4. Da kiem may vong, ket luan gi?
5. Duoc xoa chua, hay con cho gi?

### Ghi HAI DAU — moi quan he deu co hai phia
Phat hien quan he A↔B thi ghi vao **CA A LAN B**, moi ben viet tu goc nhin cua minh.
Ghi mot dau la vo dung: agent sau mo dau kia ra se khong thay gi.

### Ghi NGAY khi tim ra, tung cai mot
Khong gom cuoi phien. Phien dut giua chung thi phan da tim van con nguyen trong he.

---

## BAY DA TRA GIA — doc truoc khi viet lenh (DEL-1C/1D/1E)

### `COMMENT ON` LUON GHI DE, KHONG CONG DON
Da mat nhan `HE-PIVOT` cua `pivot_results` vi loi nay (phep dem 19→18), phai khoi phuc tu file.
**Cach dung:** doc `obj_description()` truoc → noi them chuoi moi → ghi lai TOAN BO:
```sql
DO $$ DECLARE old text; BEGIN
  old := coalesce(obj_description('ten_bang'::regclass,'pg_class'),'');
  IF position('NHAN DOT-NAY' in old) = 0 THEN     -- chan ghi trung khi chay lai
    EXECUTE format('COMMENT ON TABLE ten_bang IS %L', old || E'\n\n-- nhan moi --\n...');
  END IF;
END $$;
```
**Sau moi lo ghi phai dem lai so nhan** de chac khong tut.

### Do luong noi doi — dung tin mot con so
- `n_live_tup` **noi doi**: `event_outbox` bao 4.689, that la **217.998** (sai 46 lan).
  `law_dot_enforcement` bao 0, that la 272. **Luon `COUNT(*)` that.**
- **Bo dem cong don KHONG do duoc hien tai.** `qt001_signoff_plan_binding` co 1.091.413
  luot doc cong don nhung do delta 20 phut ra **dung 1 luot** — trieu luot kia la lich su.
  ⇒ Muon biet mot vat con song khong: **chup 2 lan roi tru**, dung doc so cong don.
- `seq_scan > 0` **khong chung minh co nguoi dung** (`pg_dump` dem cung sinh scan).
- `n_tup_upd = 0` **khong nghia la khong ai ghi** (`UPDATE 0` van la UPDATE that).
- PG **khong dem duoc luot doc view va luot chay ham** (`track_functions=none`,
  `pg_stat_statements` chua nap) ⇒ voi view/ham phai **truy caller**, khong doi bo dem.
- Ten bat dau `v_` **khong bao dam la view** (`v_registry_counts` LA BANG).
- Nhan la **cong don** ⇒ regex lay `HE:` dau tien se ra nhan **CU NHAT**. Lay ban moi nhat.

### Bay bash / shell
- `docker exec -i` **nuot sach stdin con lai cua script** ⇒ chi chay duoc dong dau roi dung
  im lang. Trong script: **bo `-i`**.
- `docker exec postgres psql -f <duong dan HOST>` — psql chay TRONG container, **khong thay**
  file host ⇒ lenh im lang khong chay ma log van in "da xong". Phai **`docker cp` vao container truoc**.
- `echo ... | tee -a "$LOG"` — khi phien SSH dong, stdout thanh ong vo ⇒ **SIGPIPE giet `tee`
  truoc khi kip ghi file** ⇒ script chay toi cung nhung **mat sach bang chung**.
  Ghi thang `>> "$LOG"`; tach han bang `setsid nohup ... </dev/null`.
- `pgrep -c <ten>.sh` **khong khop** khi tien trinh la `bash <ten>.sh`. Dung **`pgrep -f`**.
- Nested quoting qua `ssh` → `docker exec` → `psql -c` **hong im lang**.
  Cach chac: viet file `.sql` → `scp` → `docker cp` → `psql -f`.
- `py_compile` **tu choi `cfile='/dev/null'`** = FAIL GIA.
- `git add` quet ca file chua track ⇒ chi `git add` **duong dan CU THE**.
- Loc theo ten file **luon hong theo huong BO LOT**. Vi du that: bo loc dem lenh DOT bo qua
  duoc `.bak` + gach ngang nhung khong bo qua duoc `.bak` + dau **cham** ⇒ dem thua 1.

### Nap de len ban nap do = NHAN DOI AM THAM
Bang khong khoa, chi `COUNT(*)` toan bo moi bat duoc. Khi dung DB tam de dien tap:
**luon tao moi, khong nap de**.

### Tai lieu KB — noi dung nam o dau
Qua **MCP KB API**: noi dung o `data->'content'->>'body'`, **khong phai** `data->>'content'`
(`content` la object `{body, mime_type}`). Ghi de bang chuoi lam `fn_kb_truncation_guard`
keu `shrunk N->0`. Luon `jsonb_set(data,'{content,body}',...)` va **chup `data::text` ra file
truoc moi UPDATE**.
Qua **bang `knowledge_documents` trong PG**: cot `content` la **TEXT thang**, khong phai jsonb.
Hai duong khac nhau — dung nham la hong.

---

## GOC CHUNG CUA NAM LAN THAT BAI (DEL-1E, 2026-08-01)

Nam vong xay he thong quan tri deu that bai theo **cung mot kieu**:

1. **Xay cong truoc khi co nguoi di qua cong** — dung xong bo may roi moi tim viec cho no.
   Vong 2 de lai 20 bang `qt001_*` voi **permit = 0, done = 0**: bo may day du, chua chay lan nao.
2. **Chi co cua vao, khong co cua ra** — vong 1 registry de lai **khong co gi**;
   `v_registry_summary` xoa-roi-them **87.182 vong cho dung 1 dong**.
3. **Nghiem thu bang "da dung xong" thay vi "co ai dung"** — trang pivot song, HTTP 200,
   nhung trong 118.655 request chi co **2 luot, ca hai deu la bot**. Khong ai kiem dieu do
   truoc khi tuyen bo xong.

**Quy tac rut ra — ap dung cho MOI dot xay moi:**
nghiem thu phai la **"do duoc co nguoi dung that"**, khong phai "da dung xong".
Truoc khi xay them mot bo may quan tri nua, **do xem bo may cu co ai dung khong** —
bang delta 2 lan chup, khong bang bo dem cong don.

---

## 🔑 BÀI HỌC GỐC DEL-1 (ghi 2026-08-01, vòng 6 / DEL-1G) — đọc trước khi dựng thêm bộ máy

**Mục tiêu ban đầu của registry CHỈ LÀ ĐẾM.**

Đếm thì **một câu truy vấn PostgreSQL là xong** — đã chứng minh qua phần report và bảng
`balo_thuc_the`. Cả bộ máy **khai sinh / registry / pivot / governance** là một công trình
dựng lên để làm việc mà **một câu lệnh làm được**.

Số đo (database `directus`, 1722 MB, đo 2026-08-01):

| Bộ | Dung lượng | Vật |
|---|---|---|
| BỘ 1 KHAI SINH — `birth_registry` | **311 MB / 1.217.274 dòng = 18% database** | 155 |
| BỘ 2 REGISTRY | 992 kB / 20 bảng | 286 |
| BỘ 3 PIVOT | 712 kB / 2 bảng | 185 |
| BỘ 4 GOVERNANCE | — | 107 |
| BỘ 5 IU (đóng băng) | 4.744 kB / 32 bảng | 250 |

🔴 **Cái đắt KHÔNG PHẢI ở đĩa** — mà ở **166 trigger bắn trên mỗi lệnh ghi của 148 bảng**.

**Đo delta 70 phút 2026-08-01** trên 352 bảng: **260 CHẾT** · 63 NGỦ · 27 SỐNG · 2 SỐNG MẠNH.
Hai vật SỐNG MẠNH nhất chính là hai vật của bộ máy này, và cả hai đang **ghi đè lên chính mình**:
`v_registry_counts` nạp lại 169 dòng ~26 lần/phút; `pivot_results` sửa ~15 lần/phút cho 150 dòng
cố định. Trang đọc kết quả pivot sống (HTTP 200) nhưng trong 118.655 request chỉ có **2 lượt, cả
hai đều là bot**.

### Ba điều đã chứng minh bằng diễn tập, không phải suy luận

1. **Vô hiệu hoá không làm hỏng gì.** Tắt 262 trigger qua 6 đợt: ghi thử 12/12 OK · 510/510 view
   vẫn phân giải · 8/8 hàm pivot vẫn gọi được · khoá ngoại RESTRICT vẫn chặn.
2. **Cái ngừng là việc âm thầm.** 12 lệnh ghi sinh **12 dòng** `birth_registry` khi trigger bật,
   **0 dòng** khi tắt. Câu hỏi đúng không phải *"có hỏng không"* mà *"có ai cần những dòng đó không"*.
3. **Vô hiệu hoá là hoàn tác được.** Bật lại 262 trigger → dấu vân tay hệ sống **107/107 dòng
   trùng khớp**, danh sách 383 trigger trùng khớp.

### Quy ước bắt buộc từ nay

* **Đích là VÔ HIỆU HOÁ rồi để nguyên tại chỗ**, dán nhãn, theo dõi dài hạn — không `DROP`.
* Mọi vật phải có **`DIA CHI`** — mã định danh ổn định, một vật một mã:
  `PG.<db>.<schema>.<ten>` · `…fn.<ten>` · `…trg.<bang>.<ten>` · `…fk.<bang>.<ten>` ·
  `…idx.<ten>` · `DOT.<ten-lenh>` · `FILE.<duong-dan>` · `CRON.<file>.<job>` ·
  `DIRECTUS.<loai>.<ten>` · `QDRANT.<collection>`.
  ⚠️ Hàm **nạp chồng** phải mang cả chữ ký đối số, nếu không hai hàm trùng một mã.
* Mọi vật phải có **`SU KIEN`** — dòng lịch sử **cộng dồn, không ghi đè**:
  `SU KIEN: <ngay> · <viec> · <ket qua> · <ai lam>`.
* **Muốn biết một vật còn sống không: CHỤP HAI LẦN RỒI TRỪ.** `pg_stat` cộng dồn từ 2026-04-17,
  chưa từng reset — nó nói *"cả đời đã dùng bao nhiêu"*, không nói *"bây giờ còn dùng không"*.
* **Trừ phần của chính phép đo.** 14 "phiên" đo được ở `directus_gov_test_20260602` chính là
  15 lần chụp ảnh của công cụ đo.

Chi tiết đầy đủ: `/opt/incomex/docs/KE-HOACH-XOA-20260801.md` — Phụ lục DEL-1G.
Bằng chứng: `/opt/incomex/evidence/del1g-20260801/`.
**Bản gốc của mọi kết luận nằm trong `COMMENT ON` tại chính vật. File chỉ là mục lục.
Lệch nhau thì TIN NHÃN.**
