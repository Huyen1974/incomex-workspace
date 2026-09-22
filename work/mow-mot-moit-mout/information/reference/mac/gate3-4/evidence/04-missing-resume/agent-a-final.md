Completed the PG resume work through `python3 tool.py` only.

Persisted state:
- Intent `75691f3d-ff92-46f6-b0ba-085ce66c9aa5`: revision `1`, status `pending`.
- Draft `47775731-9db1-4a91-860d-1b2fcab2a97e`: updated from revision `1` to revision `2`, status `draft`.
- Applied missing slot `content.steps[1].condition_ref` with Condition `c15adbf9-c5d5-4369-b893-f508683481f6`.
- Condition identity verified: version `1`, digest `bc05d25b8feadd0e5c662c46c1e87842f7ae3cc7b6e2dc6ffa3f0afa63bede8a`, status `published`, meaning `duration_minutes > 60`; exactly 60 is not over threshold.
- Missing record `b3f28ca9-3c08-4f43-939f-2ba6a3495600`: revision `6`, status `resolved`, result_ref matches the applied Condition.

Reused UUID set now includes:
`8b3f61fc-1aaa-41f1-b61e-d3fabceea130`, `fff27c3f-c1f2-48c9-85b8-e2d8b23c86f4`, `756a9da6-31bd-45d4-89c7-ada389b51f21`, `27348608-bd97-4cad-bd46-8755fd9493a1`, `72fd9674-f34d-43dd-a7cb-2d2d5371b176`, `a5e7fccf-ffb4-4c7d-82e0-3df6c13a2338`, `487d8c64-c15b-4d89-897c-6c4c258d04ad`, `5539f704-cba3-4c4b-ab88-7741d18314cb`, `59b79193-7978-4e01-99e7-aca8dddf878f`, `d2821a8f-632b-4698-92c7-0ecc7cb1f43c`, `bb6361b9-6caf-455f-87d5-a13292b1fdf2`, `b8756a04-b301-42e4-a791-2e3b98532b6a`, `c15adbf9-c5d5-4369-b893-f508683481f6`.

What I can prove from the contract reads:
- Draft has no remaining `missing_slots`.
- Step 2 now references the exact published Condition.
- Draft remains Draft; nothing was published or activated.

Limitation: the tool contract does not provide machine readiness tests, execution validation, publish checks, or activation checks, so I did not claim those. Actual PG tool-call count: `10`, including one rejected read caused by unsupported sort syntax.