# T0 lab tool contract

You operate only through `python3 tool.py`, with one JSON request on standard input. It authenticates your current synthetic identity; no caller-supplied identity or PG access. `work.json` identifies your work entry. Scope is pilot. Do not read any other project, history, SSOT, setup source, transcripts, or credentials. You may use local scratch files inside this work directory. Do not change the transport, profile, permissions, or catalog. Never publish materials or substitute a guessed approved ID.

Read: `{op:"read", collection:string, id?:string, query?:object}`. Query is native Directus: filter/search/fields/limit/sort. Collections: lab_intents, lab_drafts, lab_missing, lab_definitions, lab_versions, lab_profiles, forms. Results include server versions/revisions. Published lab_versions are approved TEST resources, not production acceptance. Exact resource identity is its UUID + version + digest; resolve meaning/compatibility from record contents. `lab_definitions` holds family meaning/owner; `lab_versions` holds immutable selected semantics/parameters/refs. Do not duplicate compatible materials.

Write: `{op:"write", action:string, id:UUID, request_id:UUID, expected_revision:integer, data:object}`. New items use revision0. Retry same logical write with same request_id and identical data. A revised write must read current revision first and use a new request_id. Native system actor/date/revision are server-owned. Error means inspect authoritative state, not bypass.

Actions and input fields:

- `draft` → lab_drafts: intent_id UUID; title; family; version integer; status draft/waiting; content object; search_brief object; source_version optional published UUID; feedback_id optional UUID; reason optional text. Scope fixed pilot.
- `missing` → lab_missing: parent_id UUID; parent_revision integer; slot string; search_brief object; owner_role string; status waiting/resolved/cancelled; result_ref optional published UUID; checkpoint object. Use owning role of required resource or synthetic-material-owner if unresolved. Preserve the exact parent/slot/revision you read; a result for stale/cancelled context may not be applied.
- `intent` → lab_intents: sentence; status. Already assigned intents live in PG; do not recreate them.

Draft content contract (generic, not a complete declaration): `steps` array, each with `id` locally unique, `order` positive integer, `mot_ref` exact published UUID, `start` object (`trigger_ref` for an entry; `previous_step` plus output/completion dependency and condition/join for a later step), and optional `condition_ref` UUID or null when unresolved. `refs` contains the exact published UUIDs used transitively; `missing_slots` lists unresolved content paths. Keep family semantics in referenced materials; don't copy their full bodies as a second writable truth. A MOW draft can reuse MOT/MOIT/MOUT as exact refs rather than duplicating their Drafts. No release/activation in this work.

Search Brief records requirements, candidate comparison, reuse decision and provenance from PG catalog. Distinguish requested vs reused vs new vs unresolved. Unknown or absent compatible resource requires a structured missing record and a durable WAIT checkpoint. Checkpoint must tell a fresh session what remains without relying on chat. On resume re-read parent, request, and published result; material changes require readiness again.

Return a concise report containing persisted IDs/revisions, reused UUID set, missing requirements, and actual tool-call count. Report a limitation honestly. The tool does not construct Drafts or pick materials for you.
