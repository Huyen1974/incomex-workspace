# tools/ramk4 — GS-RAM-K4-PREFLIGHT-READONLY-20261029-22

Bộ đo CHỈ ĐỌC dùng ở P301 (graph-server). Gom các lệnh đã chạy trong lượt thành một tệp để lần sau đo lại đúng cách.

- Chạy: `ssh contabo 'bash -s' < ramk4_probe.sh > out.txt` (đầu ra để ở Mac, quyền 0600; không đưa lên repo).
- Đọc: /proc/meminfo, /proc/pressure/memory, vmstat, cgroup v2 `memory.current/stat/swap.current/peak` theo container và unit, PSS worker agent-data qua `smaps_rollup`, `docker inspect` tên, journal `incomex-graph-refresh`, `last.json`/`cert/current.json`/`refresh-sources.json`, băm nitro.json Nuxt, registry + baseline Config Guard.
- Không ghi tệp trên VPS, không restart/kill, không drop cache, không in biến môi trường hay argv đầy đủ.
- Bài học: không dùng `find /` để tìm thư mục trên VPS (IO, quá 120 s); đường Graph là `/opt/incomex/graph-server/prod-v1`.
- sha256 `ramk4_probe.sh`: 103a5c0eed79e611ede93737319655606b58cf1c8eda4ea261b8b7e8f3fbcae5
