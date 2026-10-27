# tools/ramgate — GS-RAM-GATE-C1E-20261027-15 (pha R)

Sao lưu VPS→repo (DROOT56: mã sống ở VPS là SSOT, repo chỉ lưu trữ). Bản sửa `graph-refresh` (đích Config Guard `graph-refresh-cli`)
`e5e0af2f…f23d98ae` → `f9dc3543…a54cd216e45`: cổng nhận lane code trước Enola/Neo4j tạm/Cognee (cần = sàn 3 GiB + trần Cognee 1536 MiB +
trần Neo4j tạm 1024 MiB + đệm 512 MiB), thiếu ⇒ SKIP_RESOURCE vàng có chủ, tụt RAM khi Neo4j tạm đã nhận ⇒ ĐỎ như cũ.

- `graph-refresh.ramgate.diff` — diff GNU tạo trên VPS (`--label`), sha256 `50e37362e78ac796275258efea8b456c7791e5e2fdc1f593cd4375fe5f59d66c`.

Các script khác nằm trong thư mục bằng chứng VPS `evidence/GS-RAM-GATE-C1E-20261027-15/scripts/` (không chép lên repo để giảm tải, băm dưới đây):

| tệp | sha256 | vai trò |
|---|---|---|
| `graph-refresh` | `f9dc3543f2fb57705acf0c1c8578bc7528af282b74a7f18f5a929a54cd216e45` | ứng viên = bản sống sau áp |
| `patch_ramgate.py` | `db964839e02cbadb2975cf9601a486f6e8a26389c6649159378e55f2f8e0c0e6` | vá có neo duy nhất (15 neo), dựng lại ra đúng sha ứng viên |
| `ramgate_fixtures.py` | `158428e2828d8c4e7a9bf39bc7a5f5a423b67137efcc69e7e628eaff91c7f14e` | lỗi giả R4 20 ca (ứng viên 20/20, bản PRE đối chứng 8/20) |
| `ramgate_install.py` | `8842adc61da591824750b0100fccfa0823b0e37e5c49ba9e08cf8e3b021e085a` | check / apply / drill / rollback qua apply-v0 |
| `ramgate_cov.py` | `17c456c9effdf9384b243ba25b8a4f75189d2274f18bccc842fc28d78a44905f` | coverage Guard POST (4 ô/mục) |
| `s0_probe.py` | `46770c3495caadad6ad66eb2b5c5a43630ca5b94f9d5ac3866db26b213c37dbd` | đo S0/POST chỉ đọc |

Màn hình Mac (E3, chỉ trên máy Owner `~/Incomex-Graph-View/tools/build/`): `build_view_c1e.py` sha256 `eac5c80eb530661246d6f0cc9380e01332d6dbe8b477d4b2cff0ca27957a5201`,
`layout_c1e.mjs` sha256 `e32e2feea943cf890f177c229748faffaafaafb2ab46543a235a8b9a00db3614`.
