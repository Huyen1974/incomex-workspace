# PROMPT — GS-R6B0-SOURCE-MEASURE-20261007-06

## 0. LỆNH / PHẠM VI

RUN_ID: `GS-R6B0-SOURCE-MEASURE-20261007-06`
Executor_Surface: Claude Code CLI
Repo: `Huyen1974/incomex-workspace` · branch `main`
Task: `work/graph-server`
Repo Write_Path: Incomex workspace gateway `workspace_*` · root `workspace`
Runtime Write_Path: terminal/SSH hiện hữu tới VPS1 + đường đọc Lark hiện hữu.

Owner D14: GPT + Claude tự quyết trial nhỏ; production/quy mô thật mới xin Owner.

ĐÂY LÀ R6B0 — ĐÚNG MỘT LƯỢT ĐO SỐ:
- chỉ đo hai candidate đã khóa ở P39, thứ tự C3 → C1;
- không model/LLM/JEV;
- không Cognee/Neo4j/PGVector;
- không cài Presidio/Stanza hay package nào;
- không đọc thêm base/table/surface;
- không đọc raw text bằng mắt;
- raw text không được in ra terminal/Claude/repo/evidence.

Mục tiêu: quyết định có đủ **trao đổi công việc nội bộ** để mở R6B1 hay không.

§0.3: đọc/đối chiếu trước mutation.

## 1. READ-GATE

Đọc:
1. `AGENTS.md`
2. BẢNG + §0 + D14/D15 + P37–P40 của `work/graph-server/COLLAB.md`
3. `work/graph-server/PROMPT.md`
4. roadmap hiện hành trong `work/graph-server/view.html`
5. root `COLLAB.md` dòng Graph.

Xác minh READY full SHA = commit cuối chạm PROMPT; không HOLD/STOP/READY mới; không STARTED cùng RUN chưa có KQ.

PASS → ghi:
`STARTED@GS-R6B0-SOURCE-MEASURE-20261007-06 <UTC> · executor=Claude Code CLI`

FAIL → 0 data read beyond gate, KQ DỪNG.

## 2. CHỈ HAI CANDIDATE — CẤM MỞ NGUỒN THỨ BA

### C3 — ưu tiên 1
Base: `07 - Quản lý công việc ưu tiên`
Table: `Cải tiến` · `tbl2MIHGtfYUJxyO`
Text candidate:
- `Nội dung cải tiến` · `fldweh4ncT`
Oracle candidate:
- link `Đầu việc cải tiến` · `flddAwzJ4H`

Không dùng:
- lookup `Nội dung công việc` làm input/model;
- `Đánh giá cải tiến` làm oracle.

Quan hệ tương lai nếu PASS:
`IMPROVEMENT_PROPOSAL_FOR_TASK` (tên canonical có thể Host chốt ở R6B1).

### C1 — ưu tiên 2
Base: `07 - Quản lý công việc ưu tiên`
Table: `Giao việc không tiêu chuẩn` · `tbl5b8o8OFSwrapD`
Text candidate:
- `Nội dung yêu cầu` · `fldIPCO6H7`
Oracle candidate:
- link `ĐH liên quan (nếu cần)` · `fldgsvJsZF`

Không dùng TTS link.
Không dùng `Thực hiện` làm oracle.

Quan hệ tương lai nếu PASS:
`NONSTANDARD_REQUEST_FOR_ORDER`.

CẤM:
- C2/C4;
- 14 base chưa khảo sát;
- PostgreSQL/Directus khác;
- Gmail/chat/KB;
- source mới do executor tự nghĩ.

## 3. RAW-TEXT BOUNDARY

Dùng script cục bộ trên VPS.
Ưu tiên reuse `r6b_read.py` / `r6b_lengths.py` đã có; được chỉnh tham số/path trong runtime, không tạo framework mới.

Raw records:
- private runtime dir mode 700;
- private files mode 600;
- không Git;
- không evidence public;
- không stdout/stderr.

Terminal chỉ được thấy:
- table/candidate id;
- count;
- length metrics;
- ratios;
- hash;
- PASS/FAIL.

Không dùng `cat`, `grep`, debug print hay Python traceback chứa raw value.
Nếu script lỗi có nguy cơ in raw text ⇒ dừng, sửa logging local trước rồi mới rerun cùng measurement.

## 4. ĐO C3 RỒI C1 — MỖI CANDIDATE CÙNG BỘ METRIC

Schema freeze trước read:
- xác nhận field id/name/type;
- ghi schema hash.

Với **mỗi candidate**, script chỉ xuất các số:

1. total records;
2. records có text;
3. records có **text + oracle**;
4. length chars trên records có text+oracle:
   - min
   - median
   - p75
   - count >=80
   - count >=200
   - count có newline;
5. leak/label-overlap ratio:
   - tỉ lệ text trùng nguyên hoặc chứa normalized display value của một field khác trong cùng record, kể cả lookup;
   - normalization rule phải freeze trước khi tính và dùng y hệt cho C3/C1;
6. uniqueness ratio = unique normalized text / nonempty text;
7. oracle coverage ratio;
8. số oracle values khác nhau;
9. qualified_count = records đồng thời:
   - text >=80 chars;
   - oracle có giá trị;
   - không bị exact duplicate text.

Không in raw oracle/display values.

## 5. SOURCE GATE — PHẢI ĐẠT ĐỦ NĂM

Một candidate PASS khi đồng thời:

G1. >=16 records text >=80 chars **và có oracle**.
G2. median text length >=80.
G3. leak/label-overlap ratio <=20%.
G4. uniqueness ratio >=80%.
G5. oracle có >=6 distinct values.

Không hạ ngưỡng.
Không bỏ gate.
Không đổi normalization sau khi thấy số.

## 6. QUY TẮC CHỌN TẤT ĐỊNH

Sau khi đo cả C3 và C1:

1. C3 PASS 5/5 ⇒ SELECT=C3.
2. else C1 PASS 5/5 ⇒ SELECT=C1.
3. else xét COMBINED chỉ khi:
   - C3 qualified_count >=6;
   - C1 qualified_count >=6;
   - total qualified_count >=16.
   Khi đó tính lại G1–G5 trên union bằng cùng normalization.
   COMBINED PASS 5/5 ⇒ SELECT=C3+C1.
4. else ⇒ DỪNG `NO_FREETEXT_SOURCE_GATE_PASS`.

Không chọn source theo “gần đạt”.
Không thêm candidate.

## 7. PRIVACY — R6B0 CHỈ GHI NĂNG LỰC, KHÔNG CÀI

R6B0 không cần PERSON-scan raw corpus vì không có external model call.

Chỉ xác minh read-only:
- `lark_client.pii` hiện có structured-id regex nhưng không PERSON NER;
- chưa có local PERSON scanner đã nghiệm thu.

Ứng viên **cho R6B1 nếu source PASS**, không cài ở R6B0:
- `presidio-analyzer==2.2.364`
- `stanza==1.15.0`
- Stanza Vietnamese VLSP NER.

Nguồn upstream Host đã fresh-check 07/10/2026:
- Presidio/Data Privacy Stack: MIT, maintained, Stanza supported as NLP engine; default config English nên R6B1 phải cấu hình vi explicitly.
- Stanza 1.15.0: Apache-2.0; official Vietnamese VLSP NER exists; official table reports F1 82.44 overall, **không đủ để coi PERSON recall của Incomex đã đạt**.

Không tin benchmark công bố thay cho local gate.

## 8. OUTPUT PASS — KHÔNG CHẠY R6B1 TRONG CÙNG RUN

Nếu SELECT=C3/C1/COMBINED:
- KQ XONG `SOURCE_GATE_PASS:<selection>`;
- ghi đủ metrics nhưng không raw text;
- giữ private sample data local;
- đề xuất R6B1 là RUN riêng.

R6B1 tương lai phải:
1. cài Presidio+Stanza trong vùng trial riêng, exact pinned versions;
2. tải model trước rồi disable auto-download;
3. đo PERSON recall tại chỗ **trước** khi dùng để lọc corpus;
4. chỉ nếu privacy gate PASS mới làm free-text oracle <=16 đoạn.

Không cài gì trong R6B0.

## 9. OUTPUT FAIL — STOP RULE

Nếu không source nào PASS:
- KQ DỪNG `NO_FREETEXT_SOURCE_GATE_PASS`;
- **không đào thêm nguồn**;
- trong `## Owner cần quyết` ghi đúng một dòng:
  `R6B free-text: hệ thống hiện chưa có nguồn trao đổi đủ chuẩn để thử. Đề xuất dừng free-text ở mức R5 đã chứng minh cơ chế, đi tiếp R6C; việc bắt đầu ghi care/exchange hoặc nối hộp thư/chat để R7 quyết production scope.`
- roadmap chuyển current sang R6C; R6B1 = BLOCKED_BY_SOURCE.
- không chờ Owner để R6C được tiếp tục theo D14.

Đây là stop rule cuối cho discovery hiện tại.
Không có lượt discovery thứ ba.

## 10. KQ / EVIDENCE / CLEANUP

Evidence:
`/opt/incomex/work/graph-server/evidence/GS-R6B0-SOURCE-MEASURE-20261007-06/`

Evidence public chỉ:
- schema ids/types/hash;
- metric JSON;
- gate result;
- script hashes;
- no raw text/oracle values/record ids.

Private:
`/opt/incomex/work/graph-server/runtime/r6b0/private/`
mode 700/600.

Kết thúc:
- không container mới;
- không provider call;
- cost 0;
- production untouched;
- wipe dry-run private path, chưa xoá thật theo preserve-by-default.

Repo chỉ cập nhật `work/graph-server/COLLAB.md` Bảng/KQ.

KQ:
`KQ@GS-R6B0-SOURCE-MEASURE-20261007-06 XONG|DỪNG`

Commit:
`[Claude Code] GS-R6B0-SOURCE-MEASURE-20261007-06 · graph-server · <XONG|DỪNG>`

Final:
`XONG · GS-R6B0-SOURCE-MEASURE-20261007-06 · <selection> · <commit>`
hoặc
`DỪNG · GS-R6B0-SOURCE-MEASURE-20261007-06 · NO_FREETEXT_SOURCE_GATE_PASS · <commit>`

## 11. AUTONOMY

Claude tự xử read-only schema/fetch/script mechanics trong đúng C3/C1.
Không hỏi Owner.
Không mở source thứ ba.
Không cài package.
Không model call.
Không production mutation.

Bất kỳ nhu cầu vượt phạm vi ⇒ DỪNG.
