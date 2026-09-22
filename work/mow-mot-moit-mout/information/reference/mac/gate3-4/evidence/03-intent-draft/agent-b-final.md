Persisted outcome: Draft/WAIT only, no publish or activation.

Draft persisted:
`lab_drafts` `60ec867f-1729-4b67-a074-5caceb691c17`, revision `1`, status `waiting`.

Missing checkpoint persisted:
`lab_missing` `08023199-d531-4f9b-a478-3234d88a533f`, revision `1`, parent revision `1`, status `waiting`.

Reused published UUIDs:
`8b3f61fc-1aaa-41f1-b61e-d3fabceea130`, `fff27c3f-c1f2-48c9-85b8-e2d8b23c86f4`, `d2821a8f-632b-4698-92c7-0ecc7cb1f43c`, `756a9da6-31bd-45d4-89c7-ada389b51f21`, `27348608-bd97-4cad-bd46-8755fd9493a1`, `72fd9674-f34d-43dd-a7cb-2d2d5371b176`, `a5e7fccf-ffb4-4c7d-82e0-3df6c13a2338`, `bb6361b9-6caf-455f-87d5-a13292b1fdf2`, `487d8c64-c15b-4d89-897c-6c4c258d04ad`, `5539f704-cba3-4c4b-ab88-7741d18314cb`, `59b79193-7978-4e01-99e7-aca8dddf878f`, `b8756a04-b301-42e4-a791-2e3b98532b6a`.

Missing requirement:
Exact published `Condition` resource for `duration_minutes > 60`, to bind into step `mark_review_required_when_over_60.condition_ref`.

Actual governed lab tool-call count: `12`. This includes `3` rejected read attempts due field/sort query shape, then successful simpler reads/searches and writes.

Limitation: the draft cannot be made ready because the governed catalog did not contain an exact threshold Condition version. I also observed the native form record is still `draft` and only showed duration/system timestamp fields, while the published MOIT/MOUT refs include the optional note binding.