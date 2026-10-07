# PROMPT — GS-R6D-DOT-SQL-EXPLICIT-20261007-08

## 0. LỆNH / PHẠM VI

RUN_ID: `GS-R6D-DOT-SQL-EXPLICIT-20261007-08`
Executor_Surface: Claude Code CLI
Repo: `Huyen1974/incomex-workspace` · branch `main`
Task: `work/graph-server`
Repo Write_Path: Incomex workspace gateway `workspace_*` · root `workspace`
Runtime Write_Path: terminal/SSH hiện hữu tới VPS1.

Owner D14: GPT + Claude tự quyết trial nhỏ; production/quy mô thật mới xin Owner.

MỤC TIÊU DUY NHẤT:
- chứng minh đường nạp Graph cho **quan hệ tường minh có nguồn xác định**, nơi Enola không parse shell DOT/SQL;
- Họ A: PostgreSQL native catalog trigger → table/function + trạng thái tại snapshot;
- Họ B: lệnh DOT tồn tại trên đĩa ↔ khai báo registry hiện hữu;
- không suy từ thân hàm/script.

KHÔNG:
- parse shell/SQL;
- đọc thân hàm `prosrc` / `pg_get_functiondef`;
- đọc nội dung script DOT;
- LLM/JEV/vector/Cognee;
- sửa PG/Directus/DOT registry;
- tạo registry mới;
- dùng view dò chữ/callgraph để bù UNKNOWN;
- nối Neo4j trực tiếp vào PG.

§0.3: đọc/đối chiếu trước mọi mutation trial.

## 1. READ-GATE

Đọc:
1. `AGENTS.md`
2. BẢNG + §0 + D14/D15 + P45–P48 của `work/graph-server/COLLAB.md`
3. `work/graph-server/PROMPT.md`
4. `work/graph-server/view.html`
5. root `COLLAB.md` dòng Graph.

Xác minh READY full SHA = commit cuối chạm PROMPT; không HOLD/STOP/READY mới; không STARTED cùng RUN chưa có KQ.

PASS → ghi:
`STARTED@GS-R6D-DOT-SQL-EXPLICIT-20261007-08 <UTC> · executor=Claude Code CLI`

FAIL → 0 runtime mutation, KQ DỪNG.

## 2. PG READ-ONLY GATE — BẮT BUỘC

Chỉ được dùng **đường PG read-only hiện hữu** tương đương role mà cổng `query_pg` dùng.
Không dùng owner/superuser.
Không tạo role.
Không in credential.

Trước ba query:
- `BEGIN READ ONLY`
- `SET LOCAL default_transaction_read_only=on`
- ghi evidence:
  - current_user;
  - `rolsuper=false`;
  - `has_table_privilege(current_user,'public.trigger_registry','INSERT')=false`;
  - `has_table_privilege(current_user,'public.dot_tools','INSERT')=false`.

Không chứng minh được read-only path ⇒
`DỪNG · NO_READONLY_PG_PATH`.

PG chỉ SELECT catalog/registry. Không INSERT/UPDATE/DELETE/DDL/CALL.

## 3. BA SELECT DUY NHẤT — CHÉP NGUYÊN

### Q_TRG · PostgreSQL native catalog — SOURCE OF TRUTH
```sql
SELECT n.nspname AS tbl_schema, c.relname AS tbl, t.tgname AS trg,
       pn.nspname AS fn_schema, p.proname AS fn,
       pg_get_function_identity_arguments(p.oid) AS fn_args, t.tgenabled AS enabled_code
FROM pg_trigger t
JOIN pg_class c ON c.oid = t.tgrelid  JOIN pg_namespace n  ON n.oid  = c.relnamespace
JOIN pg_proc  p ON p.oid = t.tgfoid   JOIN pg_namespace pn ON pn.oid = p.pronamespace
WHERE NOT t.tgisinternal ORDER BY 1, 2, 3;
```

### Q_REG · trigger_registry — INDEPENDENT CROSS-CHECK ONLY
```sql
SELECT code, trigger_name, table_name, function_name, enabled FROM trigger_registry ORDER BY code;
```

### Q_DOT · dot_tools — DECLARATION ONLY
```sql
SELECT code, name, file_path, paired_dot, status FROM dot_tools ORDER BY code;
```

CẤM query thêm để cứu kết quả.
Metadata role/read-only ở §2 không tính là source query.

## 4. DOT DISK SOURCE

Source of truth về lệnh DOT đang tồn tại:
- `/opt/incomex/dot/00-SO-DOT.tsv`
- sorted filename list thực tế dưới `/opt/incomex/dot/bin/`.

Không chạy `dot-dot-catalog`.
Không đọc nội dung script.

Freeze:
- SHA256 `00-SO-DOT.tsv`;
- sorted basename list của `dot/bin`;
- hash list.

Nếu TSV lệch directory:
- directory hiện hữu thắng về EXISTENCE;
- ghi exact diff;
- không sửa TSV.

Tên bị surface filter che nếu có: không in tên; vẫn được tính local/count/hash.

## 5. NGUỒN CẤM / CHỈ ĐỐI CHIẾU

KHÔNG dùng làm source truth hoặc graph input:
- `dot_iu_command_catalog`
- `iu_relation`
- `entity_dependencies`
- `universal_edges`
- `_recon_dot_fs_inventory`
- `v_qt001_callgraph_edges_v2`
- `v_qt001_native_dependency_edges_v6`
- `directus_relations`
- `trigger_registry` cho trạng thái truth
- `dot_tools` cho command existence truth.

`trigger_registry` và `dot_tools` chỉ cross-check/DECLARED.

## 6. SNAPSHOT / FREEZE TRƯỚC NẠP

Xuất local dưới:
`/opt/incomex/work/graph-server/runtime/r6d/input/`

Files:
- `q_trg.csv`
- `q_reg.csv`
- `q_dot.csv`
- `dot_disk.tsv`
- `FREEZE.sha256`
- `snapshot-meta.json` timestamp UTC + row counts.

Permissions 700 dir / 600 files.
Hash toàn bộ trước Neo4j load.

Số P47 đo sáng 07/10 chỉ là reference.
**Acceptance tính theo frozen RUN snapshot.**
Nếu khác P47: báo diff; không tự coi là lỗi, không rerun để nâng số.

Cuối RUN chạy lại đúng Q_TRG/Q_REG/Q_DOT read-only:
- hash không đổi ⇒ stable snapshot;
- đổi ⇒ ghi `SOURCE_CHANGED_DURING_RUN` + exact row-key diff.
Không sửa nguồn.

## 7. GRAPH SCHEMA — FRESH NEO4J, KHÔNG COGNEE

Fresh R6D Neo4j:
- Community 5.26.31 local image;
- `--pull never`;
- 0 public port;
- internal/loopback only;
- volume riêng R6D;
- 0 outbound.

Nạp bằng `LOAD CSV` từ file snapshot.
Neo4j **không** có PG credentials/network route.

Unique IDs:

### Họ A · PostgreSQL triggers
- `:PgTable{id = tbl_schema+'.'+tbl}`
- `:PgTrigger{id = tbl_schema+'.'+tbl+'.'+trg}`
- `:PgFunction{id = fn_schema+'.'+fn+'('+fn_args+')'}`

Edges:
- `(:PgTrigger)-[:ON_TABLE]->(:PgTable)`
- `(:PgTrigger)-[:EXECUTES]->(:PgFunction)`

PgTrigger properties:
- `enabled_code`
- `source='pg_catalog'`
- `snapshot_utc`
- `source_file`
- `source_row`.

### Họ B · DOT
- `:DotCommand{id=<basename from disk source>}`
- `:DotRegistryEntry{id=<dot_tools.code>}`

`REGISTERS`:
1. nếu `file_path` có giá trị và basename(file_path) == DotCommand.id ⇒ edge;
2. nếu `file_path` trống và `name` == DotCommand.id ⇒ edge;
3. nếu `file_path` có giá trị nhưng file không còn ⇒ **không edge**, dù name trùng;
4. không fuzzy/normalized-name matching ngoài trim newline của serialization.

`PAIRED_WITH`:
- chỉ tạo khi `paired_dot` bằng **đúng một code** tồn tại;
- multi-code/composite string ⇒ không edge.

DOT edge properties:
- `trust='DECLARED'`
- snapshot/source file/source row.

Không graph hóa status/last_executed/usage_count thành runtime truth.

## 8. TRUST SEMANTICS — KHÓA TRƯỚC LOAD

Nếu PASS, chỉ được đề xuất Host nâng v0.5:

1. `EXACT_AT_SNAPSHOT`
   - PgTrigger existence;
   - ON_TABLE;
   - EXECUTES;
   - enabled_code;
   - DotCommand existence từ disk snapshot.
   - Vắng trigger/DotCommand = không có **tại snapshot source truth tương ứng**.

2. `DECLARED`
   - DotRegistryEntry;
   - REGISTERS;
   - PAIRED_WITH.
   - Không chứng minh command chạy thật hay body gọi gì.

3. `UNKNOWN`
   - function body → table/function;
   - DOT body → table/function;
   - DOT calls DOT ngoài declared paired_dot;
   - scheduling/execution history;
   - Python/TS ↔ DOT/SQL;
   - relation không có explicit source.

Không suy từ text/body/regex để lấp UNKNOWN.

## 9. C1–C6 PASS — TẤT CẢ PHẢI ĐẠT

### C1 · READ-ONLY + SNAPSHOT INTEGRITY
- PG read-only preflight PASS.
- 4 source snapshots frozen+hashed trước load.
- production PRE=POST.
- Q_TRG/Q_REG/Q_DOT post-run:
  - stable ⇒ PASS;
  - nếu source đổi do bên khác, graph vẫn phải khớp frozen snapshot và báo `SOURCE_CHANGED_DURING_RUN`; executor không rerun.

### C2 · IDENTITY EXACT
Graph node unique counts = unique IDs từ frozen input.
Bắt buộc chứng minh:
- `public.unit_version` ≠ `sandbox_tac.unit_version`;
- overload function identity giữ `fn_args`;
- duplicate DOT registry rows không gộp sai command node.
0 key collision ngoài rule.

### C3 · PG LOAD FIDELITY
Tập ON_TABLE + EXECUTES trong graph = exact frozen Q_TRG-derived sets.
0 extra, 0 missing.
Mỗi edge có provenance snapshot/source row.

### C4 · TRIGGER REGISTRY CROSS-CHECK
Từ frozen Q_REG:
- exact MATCH/MISSING/NAME_MISMATCH;
- exact enabled mismatch count so với Q_TRG;
- graph state luôn theo Q_TRG.

PASS = báo cáo cross-check **chính xác 100% theo hai frozen files**.
Không yêu cầu registry phải đầy đủ hay enabled phải đúng.

### C5 · DOT FIDELITY / DRIFT
Từ frozen disk + Q_DOT:
- expected REGISTERS set = graph set;
- expected PAIRED_WITH set = graph set;
- report exact:
  - registry rows không nối được;
  - disk commands không có registry edge;
  - commands có nhiều registry rows;
  - composite paired_dot bị bỏ.
0 extra, 0 missing theo deterministic rule.

PASS không có nghĩa dot_tools đúng; chỉ graph phản ánh disk truth + registry declarations.

### C6 · 8 GRAPH QUESTIONS
Oracle tính từ frozen input **trước** khi hỏi graph:

1. Với `public.dot_tools`: trigger nào chạy, gọi hàm nào, enabled_code nào?
2. `public.dot_domains` có trigger không?
3. Trigger trên `unit_version` — tách schema.
4. `trg_count_dot_tools` enabled/disabled? Nếu Q_REG khác, trả catalog truth + `REGISTRY_MISMATCH`.
5. `public.refresh_registry_count()` đọc/ghi bảng nào? ⇒ `UNKNOWN_FROM_GRAPH`.
6. DOT nào đọc/ghi `dot_tools`? ⇒ `UNKNOWN_FROM_GRAPH`.
7. `dot-dot-catalog`: disk existence? registry edge?
8. `dot-schema-ensure`: một command node; bao nhiêu registry entries trỏ tới nó?

PASS:
- Q1–Q4 exact frozen Q_TRG;
- Q5–Q6 đúng UNKNOWN, không dò body;
- Q7–Q8 exact frozen disk/Q_DOT.

## 10. KHÔNG ĐƯỢC NÓI QUÁ

PASS chỉ chứng minh:
- PostgreSQL trigger catalog relations exact tại snapshot;
- DOT command existence exact theo disk snapshot;
- DOT registry relations graph hóa đúng deterministic DECLARED rule.

PASS KHÔNG chứng minh:
- SQL function/table dependency nói chung;
- script DOT body dependency;
- execution history/schedule;
- DOT calls DOT thật;
- toàn bộ SQL/code relation.

“DOT/SQL” ở R6D = **explicit native/declared metadata coverage**, không phải parser coverage.

## 11. CLEANUP / KQ

Evidence:
`/opt/incomex/work/graph-server/evidence/GS-R6D-DOT-SQL-EXPLICIT-20261007-08/`

Tối thiểu:
- PRE/POST;
- read-only proof;
- frozen hashes/counts;
- expected sets;
- Neo4j counts/diffs;
- C1–C6;
- 8 graph answers;
- 00-KQ.md;
- EVIDENCE.sha256.

Cleanup:
- stop/remove R6D container/network;
- giữ R6D volume + evidence cho Host;
- wipe dry-run only;
- không xoá R6B/R6B0 private copies;
- không xoá R6C runtime.

Repo chỉ update Bảng/KQ trong task COLLAB.
Không sửa PROMPT/view ở executor.

KQ:
`KQ@GS-R6D-DOT-SQL-EXPLICIT-20261007-08 XONG|DỪNG`

Final:
`XONG · GS-R6D-DOT-SQL-EXPLICIT-20261007-08 · <commit>`
hoặc
`DỪNG · GS-R6D-DOT-SQL-EXPLICIT-20261007-08 · <blocker> · <commit>`

## 12. AUTONOMY

Claude tự xử export CSV/local Neo4j/LOAD CSV/scoring trong scope.
Không hỏi Owner.
Không đổi nguồn/query/rules.
Không rerun để nâng số.
Không viết parser.
Không dùng body text.
Không mutation production.

Nếu cần source/query thứ tư, write privilege, parser mới hoặc sửa registry ⇒ DỪNG sạch.
