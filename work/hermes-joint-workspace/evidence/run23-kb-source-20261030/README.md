# RUN23 — primary KB source candidate

Result: G8_AD_KB_PRIMARY_SOURCE_CI_PASS. Overall KB coverage remains PARTIAL (admin maintenance routes below). Source/fixture/CI only; not G8_SYSTEM, KST acceptance, deployed enforcement or live-client C1/C2.

READY 01e3e0d06a8db177d28e55114a2c618324cec7d1; PROMPT SHA256 f541e690d08f3ffafc5187b347ca224053c35e41aeb8d7b3e6894154c7b922c4.
PR358 HEAD 2d966640a0ccdf22fec50ee45a725fdfb41bfe48; prior 833bbc183494166496ffbaad0ba3933ea23d3fb4; main 6160f9ad6e5d16012dfe20bb59949abf5ffadad2. Non-force push to existing dev branch; still DRAFT.
PR357 unchanged 36c682914c9f412078113b6d85319f11356d1130. No VPS, production, live KB, permissions or credentials changed.

## Coverage and provenance
| Ingress | Covered existing writers | Authentication and facts |
|---|---|---|
| MCP server direct Python dispatch | upload/update/patch/delete/ingest_document | Existing master/agent auth and ACL retained. Handler-level guard also covers calls bypassing FastAPI Depends. |
| REST | POST /documents; PUT/PATCH/DELETE /documents/{id}; POST /ingest | Same API key dependency; shared-rest identity proves credential only, not AI or origin. Optional X-Write-Declaration JSON max8192 bytes remains untrusted. |
| stdio client | upload/update/patch/delete/ingest_document | Existing key; forwards public facts to REST and returns receipt. |
| hybrid client | upload/update/delete/ingest_document | All four existing writers forwarded. Hybrid did not expose patch; no new tool added. |
| Verified profile mapping | Operator-owned master_profiles[id].declaration_facts bound to authenticated profile | Only explicit mapping can auto-fill. Invalid/conflicting facts rejected; fixture-proven support, no live mapping/config created. |
| Shared credential / absent mapping | AI product, origin, task, command_ref remain self_declared | No inference from host/IP/User-Agent/clientInfo. Raw/canonical/provenance/auth identity recorded by existing contract. Declaration does not grant ACL. |

Enforce refusal occurs before PG/Qdrant/business events. Advertise old calls retain original result/error semantics. Existing revision/CAS, exact patch, soft-delete/upsert retained. Declared partial store failures retain receipt and partial/unconfirmed outcome, not atomic success. Generic transport auditing is not asserted to be zero. No general KB replay/idempotency service introduced; existing duplicate-create/CAS/patch protections remain. Existing documents are not relabelled.

## Verification
Mac existing CI list: 271 passed in 2.44s (238 HJW including 69 new +33 others). Real contract with actual source handler/client bodies and fake storage adapters; not full production application startup.
Mac FastAPI HTTP fixture: 30 passed across five routes (wrong key, missing facts, forged header/private body, valid receipt, advertise legacy); rejected writes have zero storage/event trace. Reproduce from checkout: PYTHONPATH=. <isolated-python> <evidence-dir>/rest_lab.py. Requires pytest, fastapi==0.115.6, httpx. Local test venv has unrelated sse-starlette dependency incompatibility; full app/SDK startup was not tested or claimed.
GitHub run41075696274 SUCCESS: preflight/scan/actionlint/policy/policy regressions/Unit/gate all success. Unit actual271 passed in17.16s; mandatory TESTS includes test_hjw_four_facts.py. Exact head/base above; merge-test6e6289a9a6c51ec08cedeb3c8cb70a2a6d20cc88. Existing ci_change_kst_review=true; no merge authorization. Workflow unchanged in RUN23.
https://github.com/Huyen1974/agent-data-test/actions/runs/41075696274

## Remaining coverage / NEXT_TRIGGER
- /kb/reindex: PG vector_status and Qdrant writes; not guarded by new declaration adapter.
- /kb/cleanup-orphans: Qdrant deletes; not guarded.
- /kb/reindex-missing: Qdrant plus PG markers; not guarded.
- /kb/audit-sync: conditional auto_heal invokes reindex/cleanup; not guarded.
- /documents/{id}/move is deprecated501, not active writer; /documents/batch reads; /api/docs GitHub read proxy/cache is not KB writer. Chat/session/webhook/presence persistence is outside primary KB scope.
NEXT_TRIGGER: GPT Host reviews P486 and decides admin coverage/verified mapping follow-up. PR357 integration, Linux image/rebuild/rollback and real C1/C2 remain later gates. No automatic RUN, merge, deploy or additional Claude round.

## Evidence index
manifest.json: five-path delta and unchanged auth/ACL AST + queue/execution/workflow blobs.
source-diff.patch: exact RUN23 committed delta.
unit.txt: Mac exact CI list results. collection.txt: HJW current case count.
rest_lab.py / rest-lab.json: reproducible isolated HTTP fixture and outcomes.
ci-run.json / ci-evidence.txt: GitHub jobs and actual test/head/base output.
pr358.json / pr357-final.json: GitHub PR readbacks.
