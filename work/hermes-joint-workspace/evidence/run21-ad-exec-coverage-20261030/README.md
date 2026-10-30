# RUN21 — workspace_exec four facts + P480 notes + KB inventory

**KQ PARTIAL. Source/local tests complete; GitHub CI blocked at preflight, Unit tests SKIPPED. NOT G8_AD_WORKSPACE_EXEC_CANDIDATE_PASS, NOT G8_SYSTEM.**

RUN HJW-G8-AD-WEXEC-COVERAGE-20261030-21. Codex Desktop/MacBook Worker; GPT Chat Host.
READY 504ded5e1d5f2d44801b8802824ad778ffa46559. PROMPT SHA256 d161958b43a7375a2485d3a16fcadb169bdf6c7f27b0262bdd735c253449bd0d. STARTED c230ef0f3a8399040a105595e1fd521a2aa345e0.
PR https://github.com/Huyen1974/agent-data-test/pull/358 OPEN/DRAFT. Before 58a44c0559bfd42e7e62f5faf8df49ebd2259e78; commits 760ee56adc74d0f4b449467e495546882973d2be then 53c34ec745c6980a23996273e94b12fdd129b06a. Non-force push, no merge/rebase/main write.
PR357 remains OPEN/DRAFT 36c682914c9f412078113b6d85319f11356d1130. Queue implementation, enqueue_once, supervisor logic and Hermes ACL unchanged.

## Implemented
Exactly five allowed files (source-diff.patch): declaration adapter classifies workspace_exec as a writer and advertises four-fact schema; execution binds original facts/auth to request hash and carries server-owned _declaration; worker copies receipt into terminal result before Queue.finish erases request; contract normalizes done-tasks aliases and derives exact task from explicit cwd; existing test file gains unit marker and focused cases. No workflow, server.py, mcp_server, Queue or PR357 edits.
Missing/invalid declaration and forged hidden fields are refused before original call/state; Hermes ACL precedes declaration. Status remains a read, never mints a declaration from its caller. Receipt records original raw/canonical/provenance/authenticated label; no credentials are relayed. Advertise legacy calls remain undeclared and executable.

## Validation
- 169 focused tests PASS with -m unit; all 169 collected (focused.txt / marker.txt). Original 118 regression cases retained; parameter expansion adds coverage.
- Exact existing CI Unit tests list on Mac: 202 PASS (unit.txt), 33 existing other tests + 169 four-facts tests.
- Isolated Mac runtime/PR357 overlay: 262 PASS (overlay.txt): 169 new suite + RUN17 expanded 93 regressions. Queue code unchanged. Overlay adds terminal retry assertions: original operation replays same job after request=NULL; changed actor refused. Local host-diagnostic subprocess prints CANARY; real SQLite and retained stream files/status; Docker cleanup mocked. This is not Docker/live acceptance.
- Main-only legacy Queue lacks durable operation columns; completed retry guarantee depends on PR357 integration, already pinned. RUN21 does not replace that queue with a second journal or modify its algorithm. Queue cancellation/expiry and supervisor-crash paths are unchanged; this test evidence covers ordinary completed/failed worker outcomes, not all exceptional recovery paths.
- IMAGE_REBUILD_NOT_TESTED, C1/C2_NOT_TESTED. No VPS calls/mutations, no KB network test, no secrets printed.

## CI blocker (not a test failure)
Run https://github.com/Huyen1974/agent-data-test/actions/runs/41041965184 at exact HEAD 53c34ec745c6980a23996273e94b12fdd129b06a failed preflight: BASE_MOVED_REBASE_REQUIRED. Unit tests/scan/policy SKIPPED. Earlier run41041876241 at 760ee56 failed identically. ci-run.json and ci-evidence.txt retain proof. Cannot claim new tests executed on GitHub.
PR baseRefOid remains b4c9ea19cf2e57594a231c2819e098fe0002c99a; actual main now 6160f9ad6e5d16012dfe20bb59949abf5ffadad2 (PR360, 25 source-archive/scripts files; main-drift.json). Read-only comparison shows no RUN21 path overlap. Main was advanced by another run, not this Worker. No workflow bypass, empty-commit retries, force push, rebase or merge performed.

## KB entry → auth → writer → protection → next attachment point (source inventory only)
Inspected at candidate HEAD above; runtime is NOT measured. References below are repository paths and line numbers from this source.

| Entry | Authentication / current protection | Actual writer | Where four facts must attach next |
|---|---|---|---|
| agent_data/server.py /mcp, /mcp/tools/{tool}, /mcp-gpt-full → _dispatch_mcp_tool:3352 | require_mcp_master:708; profile allowlists and _legacy_write_gate; credential-bound master identity via _master_identity. /mcp-agent:3969 uses require_mcp_agent + profile; cannot assume its ACL protects other routes | upload/update/delete/patch/ingest dispatch calls Python handlers directly; FastAPI dependency defaults are not re-executed during Python calls | Preserve authenticated transport identity, validate common contract before any KB side effect; carry trusted envelope to common writer, not merely workspace_tools.call |
| mcp_server/stdio_server.py call_tool upload:528/update/delete:608/ingest:656/patch:711 | _request_with_fallback:85 uses configured X-API-Key, optional cloud IAM header; session-ready gate. Live discovery does not mean four facts are forwarded by these branches | Direct HTTP POST/PUT/DELETE/PATCH /documents and POST /ingest | Add schema/context forwarding and server validation on direct REST path; changing only MCP dispatcher leaves this bypass |
| mcp_server/server.py upload:276/update:303/delete:330/move:342/ingest:358 → _hybrid_request:251 | Configured endpoint X-API-Key; local→cloud connection fallback; no verified product/environment derived here | Direct REST handlers, same PG/Qdrant backend. move remains callable in client but server:1755 returns 501; not an active writer | Same REST contract/carrier, distinguish gateway credential from self-declared client; verify any client-facing wrapper auth separately |
| Direct REST create POST /documents server.py:1498 | require_api_key:675; _ogv2c_validate_write:1226/1507 prefix/body gate; duplicate/upsert checks | pg_store.set_doc/update_doc KB_COLLECTION (kb_documents) then _sync_vector_entry / Qdrant; event bus DOCUMENT_CREATED | Validate once before PG/write and carry to vector/event/result; don't attach only after mutation |
| Direct REST update PUT /documents/{id}:1611 | require_api_key; existence/update-mask validation; optional last_known_revision optimistic check:1669. OGV create gate is not called here | pg_store.update_doc → delete old vectors/sync; event/revision | Same logical-write context before update; preserve revision guard and map partial vector failure |
| Direct REST patch PATCH /documents/{id}:2008 | require_api_key; existing live doc; exact one old_str occurrence (409 for missing/ambiguous); not equivalent to general CAS | pg_store.update_doc:2064 → vector delete/re-embed | Common contract before PG mutation; retained receipt and original auth, no owner attribution guessed |
| Direct REST delete DELETE /documents/{id}:1826 | require_api_key; existence/revision handling; soft-delete metadata | vector delete then pg_store.update_doc deleted_at/vector_status; event | Gate before first vector delete, not only before PG write; record partial outcome |
| Direct REST ingest POST /ingest:869 | require_api_key; inline nonempty; gs:// disabled | optional PG set_doc:909, Qdrant upsert:916; errors can be caught while returning accepted | Gate before agent.last_ingested_text/PG/vector; receipt must describe actual effects, not equate Accepted with all stores committed |

PG sink: agent_data/pg_store.py set_doc:172 INSERT/ON CONFLICT, update_doc:186/191 conditional revision or plain UPDATE; table kb_documents. Qdrant sink is vector_store via _sync_vector_entry/_delete_vector_entry. Stored document revision/event metadata is not the four-facts receipt. Additional admin mutations (/kb/reindex:2303, cleanup-orphans:2391, audit-sync:2626, reindex-missing:2714) exist: include an explicit classification in next scope; inventory here is not exhaustive VPS-wide writer coverage. No KB code/config/data changed.

## Next trigger and cleanup
GPT Host accept P482 partial and decide a scoped PR358 base synchronization/CI retry preserving PR357 and five-file delta. Need valid actual CI before source candidate PASS; no automatic continuation. Then Host can issue RUN22 KB + trusted auto-fill; combined KST only when coverage sufficient. Remaining G8_SYSTEM: full KB/auto-fill, PR357 bootstrap debt, Linux rebuild/rollback, C1/C2 and release gates. Owner need not validate individual commands.
Mac overlay/caches removed after evidence retained; existing clone and exact patch/logs retained, no running test or waiting terminal. No VPS-GHI acquired.

Files: README.md (result + KB map); source-diff.patch; focused.txt, marker.txt, unit.txt, overlay.txt; ci-run.json, ci-evidence.txt; main-drift.json; pr358.json, pr357.json. Source commit and GitHub logs are authoritative for code/CI; this inventory is source-only.
