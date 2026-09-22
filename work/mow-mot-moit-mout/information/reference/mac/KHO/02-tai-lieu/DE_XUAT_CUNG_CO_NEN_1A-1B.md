# DE XUAT CUNG CO NEN — HUONG C (v3.2)

Version: v3.2 · 2026-07-16 · CW soan · [DANG BAN — CHUA CHOT · sheet DRAFT]
CANONICAL GOVERNANCE:
- AUTHORITATIVE = VPS /opt/incomex/docs/mcp-writes/DE_XUAT_CUNG_CO_NEN_current.md
- MIRROR (cache) = Mac /quy trinh/DE_XUAT_CUNG_CO_NEN_1A-1B.md
- HASH luu file .sha256 rieng (VPS + local), khong chi trong chat.
- Ban _v3.md cu = SUPERSEDED (tro sang _current.md). KHONG giu ban trung ten khac noi dung.
- SSOT NOI DUNG: Khung object song o SHEET khung_object (Excel), KHONG trong .md nay.

## TRANG THAI ARTIFACT (ghi ro DAT / CHUA)
| Thu | Trang thai |
|---|---|
| Sheet khung_object (13 object) + cot thuoc_object | DA DUNG — DRAFT, cho Codex+Owner duyet |
| trong-tai-3-tap.py + 8 test | CHUA sua/CHUA co |
| Excel noi dung UI (bread, khai_niem_chung, anchor) | CHUA sua (dung — dang ban) |
| 4 ma TO_REMOVE tren VPS source | VAN SONG |
| Schema MODW / PG / pilot | CHUA lam |
=> Moi so "sau sua" = DU KIEN.

## 0. 3 TANG HOP DONG != 3 NHOM BANG PG
DU LIEU (schema object, co the anh xa cot) · HANH VI (command/event, khong mac nhien la bang) · GIAO DIEN (data-region, test manifest, KHONG vao PG). data-region KHONG ganh concept.

## 1A — THUOC UI (ha muc)
3 lop: Static gate (SOURCE<->Excel-KNOWN) · Runtime smoke (DOM union phu ACTIVE) · Component test (fixture). Occurrence: SINGLE default + REPEATABLE nho (khong 4-loai/169). DOM runner: council tu chu.
So MOW (verified): parser 107=DOM 107; grep cu 96 (sot 11 ma-bien); 4 TO_REMOVE song.
SCRIPT: spec DINH NGHIA yeu cau (gate (SOURCE U DOM)-EXCEL_KNOWN={} · Excel reader KNOWN/ACTIVE/FORBIDDEN · 8 test). SCRIPT+TEST **CHUA TRIEN KHAI**. TO_REMOVE: thuoc bat DO truoc, xoa 4 ma o thay doi RIENG.

## 1B — GO concept khoi region. ban_chat_khu = role (CONTENT 72/BEHAVIOR 31/NAV 49/GROUP 13/DECOR 4). NAV/GROUP/DECOR 100% OUT.
NT2: CONTENT khong tu dong IN. binding->schema.field_path · derived->derivation rule · action->command_id · UI-only->no FK. **BINDING = OPTIONAL BRIDGE; SCHEMA la SSOT, region CHI la dia chi.**

### DANH SACH 17 (sua dung tap theo Codex — nen de gan object)
No: 19 HIEN TAI -> 18 (bread->OUT) -> 17 (bo accumulate TO_REMOVE) [du kien].
- UI-only (1): gatenote
- Derived (6): sla_light · unassigned · frozen/truong · total_exec · total_buffer · total_all
- Command (2): addtask · addbuffer
- UI-state/param can quyet (1): inputmode
- Data/object candidate (7): assignee_sla.sla · exectime · buffer · bang_thoi_gian · trang_thai_muc · ghi_chu · ngu_canh_them
=> TONG 17. Chi 7 data-candidate moi la ung vien vao object; derived/command/UI-only KHONG thanh object du lieu.
NGOAI 17 (ghi rieng): bread (->NAV+OUT) · accumulate (TO_REMOVE) · ai_toggle (command, ngoai tap 19 CONTENT+IN).

## KHUNG A -> DA CHUYEN sang SHEET khung_object (SSOT)
Xem sheet khung_object (13 object, DRAFT). 2 CHAN Codex da khac phuc trong sheet:
- process_task_membership (T2<->T1 N:M — T1 dung lai nhieu quy trinh; khong the parent_id don).
- template + variant + template_assignment (khuon/bien-the/gan-khuon — hop dong "vo hinh" da chot).
6 CHINH Codex ap trong sheet: (#1) dung "object/contract ung vien" khong "nhom bang"; (#2) proposal/command/event = 3 dong rieng; (#3) do_chac (identity CHAC) TACH storage_chot (CHUA CHOT); (#4) store_binding N:M + default_store optional; (#5) time_plan chi PLANNED, actual CHO-MOT; (#6) canonical governance o header file nay.
Cot thuoc_object (ui_cay): 57 khu CONTENT+IN -> object_key; de trong derived/command/UI-only (dung Codex triage). 2 khu moit.proposal.* -> event_audit (them khi soi).

## THU TU A->B->C
A. Khung tong the (sheet khung_object) — xong DRAFT. B. Pilot 1 object MODW = THU-DE-HOC roi VUT (trong khung A). C. Chi khi A+B on -> schema that + PG.
=> CHUA dung pilot B cho toi khi Khung A (sheet) duoc Codex phan bien + Owner duyet.

## 2 LOI NGHIA (du kien sua Excel SAU khi chot)
- modw.build.time = trigger/han -> KHONG phai tg_thuc_thi.
- modw.preview.bread -> DIEU_HUONG + OUT (hien THONG_TIN+IN).

## SCHEMA-MAU MODW can du (buoc B — Codex): schema_id/version/kind · required/nullable/default/enum|range|unit · identity+id/parent_id · mutable/read-only/derived + cong thuc field suy ra · validation + invariant lien-truong · canonical concept_key · command: quyen/precondition/idempotency/side-effect/event/loi · compatibility/deprecation · example payload + test fixture. Anh xa PG optional.

## RANG BUOC: CHUA field chi tiet · chua PG · chua pilot · chua nhan UI. CW dung -> Desktop+Codex soi -> Owner duyet -> roi wire (Luat ve sinh #5). Backup Excel truoc moi ghi.
