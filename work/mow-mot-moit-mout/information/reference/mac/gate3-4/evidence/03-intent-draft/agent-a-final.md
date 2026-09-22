Đã xử lý entry PG qua governed lab tool và dừng ở Draft/WAIT.

Persisted outcome:
- Draft: `47775731-9db1-4a91-860d-1b2fcab2a97e`, revision `1`, status `waiting`
- Missing checkpoint: `b3f28ca9-3c08-4f43-939f-2ba6a3495600`, revision `1`, status `waiting`
- Blocked slot: `content.steps[1].condition_ref`

Reused published UUIDs:
`8b3f61fc-1aaa-41f1-b61e-d3fabceea130`, `fff27c3f-c1f2-48c9-85b8-e2d8b23c86f4`, `756a9da6-31bd-45d4-89c7-ada389b51f21`, `27348608-bd97-4cad-bd46-8755fd9493a1`, `72fd9674-f34d-43dd-a7cb-2d2d5371b176`, `a5e7fccf-ffb4-4c7d-82e0-3df6c13a2338`, `487d8c64-c15b-4d89-897c-6c4c258d04ad`, `5539f704-cba3-4c4b-ab88-7741d18314cb`, `59b79193-7978-4e01-99e7-aca8dddf878f`, `d2821a8f-632b-4698-92c7-0ecc7cb1f43c`, `bb6361b9-6caf-455f-87d5-a13292b1fdf2`, `b8756a04-b301-42e4-a791-2e3b98532b6a`.

Limitation: no exact published `Condition` resource for `duration_minutes > 60` was found, so the draft cannot be made ready without that material. I did not publish or activate anything.

Actual governed lab tool calls: `15`.