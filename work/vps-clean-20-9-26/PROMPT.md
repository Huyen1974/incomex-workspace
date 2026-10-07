# PROMPT — VPSC R7 · CHUÔNG NÓI THẬT · Ổ ĐĨA CÓ TÊN CÓ TRẦN · MÃ CÓ KHOÁ · 07/10/2026

STATUS: chỉ được chạy khi `COLLAB.md` của việc có ĐỦ hai dòng mang cùng SHA last-touch của tệp này: `READY@<sha>` (Host Claude Chat) và `CODEX ACCEPT@<sha>` (Reviewer Codex). Thiếu một ⇒ DỪNG trước mọi thay đổi.
RUN_ID: VPSC-R7-TRUTH-20261007-01
Executor_Surface: Claude Code CLI trên Mac → VPS1 (`vmi3080463`) qua đường SSH/DOT hiện hữu
Write_Path: tài liệu = repo qua `workspace_*`/`fs_*` · runtime = DOT/script-wrapper + Config Guard (`incomex-config-apply-v0`) + git cục bộ `/opt/incomex`
Evidence_Dir: `/opt/incomex/work/vps-clean-20-9-26/R7-20261007/` (tạo bằng `mkdir`)
Báo cáo: thêm mục `## R7` vào `work/vps-clean-20-9-26/BAO-CAO.md` — không tạo tệp báo cáo mới.

## 0 · Vì sao có lượt này (đọc trước — bạn không có ký ức phiên trước)
Owner 07/10: chuông Telegram DOWN/UP quá nhiều; ổ đĩa vẫn đầy nhanh, mỗi lần kiểm lại lòi lỗi mới; hỏi Điều 30/31 đã bảo vệ đủ chưa. Codex khảo sát chỉ đọc (root `COLLAB.md`, dòng **PROOT01**); Host tự kiểm lại và bổ sung (`COLLAB.md` việc này, **P51**). Bốn gốc, mỗi gốc một gói:

| Gói | Gốc đã đo (07/10) |
|---|---|
| **A · chuông giả** | `dot/bin/dot-directus-license-watch` 1.0.0 đẩy `status=down` ngay lần trượt đầu, trông vào Kuma `maxretries=1`. Đèn push của Kuma không giữ được luật đó: nhịp PENDING bị chính Kuma đổi thành DOWN “No heartbeat in the time window” sau ~62 s (`/app/server/model/monitor.js` ~739–746; `routers/api-router.js` ~582–587) ⇒ 5 cặp DOWN/UP ngày 06/10, lý do thật (Directus trả 503) bị che. OPS Proxy: hai lần 503 đơn lẻ ⇒ hai cặp DOWN/UP. |
| **B · ổ đĩa** | Trống theo giờ (`/opt/incomex/logs/disk-monitor.log`): 48,44 GiB (06/10 02:00) → 40,95 GiB (07/10 10:00) = **một bậc −5,08 GiB** lúc 03–04h 06/10 (trùng Graph RUN-1 kéo image ~5 GB; footprint trial đã duyệt ≤ 10 GB) + **ba bậc −0,5…0,65 GiB** (15h và 18h 06/10; 09h 07/10 — lượt r6c 08:31 khớp bậc cuối) + **trôi nền ≈ −0,4…0,5 GiB/ngày chưa có tên**. `scripts/storage-watch.py`: gốc đo chỉ có `/opt/incomex`, `/opt/workflow` ⇒ không thấy `/var/lib/docker`, `/var/lib/containerd`, `/var/log`…; gốc không đọc được bị bỏ qua (dòng 72–73), `du` lỗi bị bỏ qua (137–138) mà vẫn `green`, rc 0; chuông SLOPE24 −6,92 GiB lúc 02:00 07/10 **tự xanh** lúc 04:00 khi cửa sổ 24h trượt qua, chưa ai gọi tên 5 GiB. |
| **C · bảo vệ** | `scripts/mcpw-protection-guard`, `mode_pre_post` (~2817–2855) chỉ so một `snapshot()` cố định PRE↔POST. Tệp ngoài tập đó đổi thì POST vẫn PASS và biên nhận vẫn ghi “bảo vệ đủ”. Ví dụ thật: `docker/agent-data-repo/scripts/workspace-exec-worker.py` (R6W vừa sửa) và unit `incomex-workspace-exec.service` không nằm trong Config Guard. Trái AGENTS A10-R4. |
| **D · 502/503** | `incomex-agent-data` chạy `uvicorn … --workers 2`; `requirements.txt` ghim `uvicorn[standard]==0.35.0`. Log container 37 giờ: 7 dòng `Child process [pid] died`, mỗi lần 18–44 s mới có tiến trình thay; Docker restart=0, healthy; nginx cùng giây ghi `upstream prematurely closed` ⇒ MCP 502. Máy 6 CPU / 12 GB; swap gần đầy từ sau Graph RUN-1 (sổ graph-server: “phần bị đẩy ra là uvicorn/hermes production”); Chrome bị kernel OOM 3 lần chiều 06/10 trong cgroup 6 GiB. **Nguyên nhân CHƯA chứng minh.** Giả thuyết phải kiểm: supervisor của uvicorn ping tiến trình con, quá 5 s không trả lời thì kill và thay (0.35.0 không chỉnh được; cờ `--timeout-worker-healthcheck` chỉ có từ 0.37.0). Directus 503 nghiêng về pressure limiter, chưa có body. |

## 1 · Hộp xanh / hộp đỏ (ngân sách cứng của cả lượt)
- **ĐƯỢC:** sửa script/DOT/cron/registry/Guard do Incomex viết · đổi cấu hình đèn Kuma qua đường ensure/DOT hiện hữu (socket chính thức) · đăng ký Config Guard · ghi sổ đo.
- **CẤM (gặp nhu cầu ⇒ ghi đề xuất ở D6, không làm):** restart/recreate/rebuild `postgres`, `incomex-directus`, `incomex-nuxt`, `incomex-qdrant`, `incomex-agent-data`, `incomex-nginx` · đổi phiên bản bất kỳ thành phần nào · docker prune/build · xoá dữ liệu/volume/image/hồ sơ/trial · đổi khoá hay xác thực · swapoff/sysctl · Directus/PG ngoài DOT · tắt, tạm dừng đèn hoặc hạ ngưỡng để lấy xanh · sửa trực tiếp `kuma.db`.
- **Bí mật:** không `cat`/in tệp `.env`, compose, nginx conf hay bất kỳ tệp nào có khoá; cần xem cấu hình thì chỉ in TÊN biến hoặc giá trị đã che. (PROOT01: một khoá dùng chung đã lọt ra đầu ra công cụ vì đọc nguyên tệp.)
- **Telegram tới Owner:** tối đa 1 cặp tin thử gắn nhãn 🧪 + 1 biên nhận cuối.
- **Không điểm chờ duyệt, không giữ terminal chờ** (DROOT43, D16). Hết phạm vi ⇒ KQ DỪNG sạch.
- **Bảo vệ đến đâu chắc đến đó:** mỗi gói kết thúc bằng test PASS + đăng ký Config Guard (hash cũ→mới + lý do, DROOT29) + commit git cục bộ + ghi BAO-CAO. Gói sau hỏng không kéo lùi gói trước.

## 2 · PRE
1. Read-gate Write_Path; đọc `AGENTS.md` → root `COLLAB.md` (PROOT01) → `work/vps-clean-20-9-26/COLLAB.md` (Bảng + §0.3 vòng 4 + P51) → tệp này. Kiểm hai dòng `READY@` và `CODEX ACCEPT@` cùng SHA.
2. Ghi `STARTED@VPSC-R7-TRUTH-20261007-01 <UTC> · executor=Claude Code CLI` + sửa dòng ■/➡ của Bảng (cùng commit).
3. NO_CONCURRENT: `COLLAB.md` việc khác có `STARTED@` chưa `KQ@` kèm server mutation, hoặc hàng đợi agent-data có job đang chạy của phiên khác ⇒ chờ tối đa 10 phút; còn ⇒ `DỪNG · CONCURRENCY`, 0 mutation. Kiểm lại trước mỗi gói.
4. Guard `pre` (lưu vào Evidence_Dir) + chạy bộ selftest sẵn có của Guard (biển tại chỗ) + chụp: bảng 22 đèn, `storage-watch.py check`, `df -B1 /`, trạng thái Config Guard.

## 3 · Gói A — đèn chỉ đỏ khi hỏng thật
**A1 · `dot-directus-license-watch` 1.0.0 → 1.1.0.** Luật “2 lượt trượt liên tiếp mới DOWN” do **chính DOT** giữ (đếm trượt liên tiếp trong tệp trạng thái của DOT dưới `/var/lib/incomex/`); Kuma #23 đặt `maxretries=0` qua `install --execute` của chính DOT. Lý do đẩy đi là lý do thật, phân loại: `license=<status>` · `directus <http> <≤60 ký tự body>` (503 = Directus bận, không phải mất giấy phép) · `licensing net <mã>`. Hợp đồng — thử bằng fixture (ép kết quả phép thử qua biến môi trường, hứng lệnh đẩy bằng endpoint giả; không đụng #23 thật):
- c1 trượt 1 lượt rồi đạt ⇒ không có lệnh đẩy `down`; log DOT có lý do thật.
- c2 trượt 2 lượt liền ⇒ đúng một lệnh đẩy `down`, msg = lý do thật.
- c3 đạt lại ⇒ đẩy `up`, bộ đếm về 0.
- c4 tệp trạng thái hỏng/không ghi được ⇒ fail-closed: coi là trượt, lý do `STATE_UNWRITABLE`, không im.
- c5 nhịp tim: giữa hai lượt đạt cách nhau một lượt trượt, Kuma không tự báo “No heartbeat” (chọn cách đẩy/khoảng `interval` cho khớp, ghi rõ số); cron/DOT chết hẳn ⇒ #23 DOWN trong ≤ 20 phút.

E2E đúng kênh, một lần trên chính #23: ép 2 lượt trượt có nhãn `🧪 THỬ R7` ⇒ Telegram nhận đúng 1 DOWN mang lý do thử, không phải “No heartbeat”; bỏ ép ⇒ đúng 1 UP. Lưu message_id.

**A2 · luật 2-lần-trượt trên cả 22 đèn.** Kiểm kê chỉ đọc `kuma.db`: id · tên · type · interval · retryInterval · maxretries · resend. Áp:
- đèn chủ động (http/keyword/port…): `maxretries=2`, `retryInterval=60` ⇒ chỉ đỏ khi hỏng liên tục ~2–3 phút;
- đèn push: Kuma `maxretries=0`; bộ đẩy nào đẩy `down` ngay lần trượt đầu vì một phép thử mạng/HTTP thoáng qua ⇒ sửa như A1; bộ đẩy báo trạng thái tất định (lệch hash, sổ dung lượng, invariant đã tự “fail x2”) giữ nguyên.

Nộp bảng trước/sau cho đủ 22 đèn.

**A3 · lọc nhiễu không được che suy giảm.** Bản tin 08:00 (sender hiện hữu, vẫn ≤ 3 dòng) thêm: `thoáng qua 24h: N` (số lượt trượt không thành DOWN, kèm tên đèn nhiều nhất) và `agent-data con chết: N`.

## 4 · Gói B — mỗi GiB có tên, có trần; không đo được = đỏ
**B1 · fail-closed** trong `storage-watch.py`: gốc không liệt kê được · `du` lỗi/hết giờ · registry hỏng · chuỗi mẫu thủng làm mất mốc 24h dù chuỗi đã dài > 27 h ⇒ `status=red`, lý do `MEASURE_FAIL <đường dẫn/nguyên nhân>`, rc ≠ 0; `taxonomy_ts` không được tiến khi phép đo thiếu.

**B2 · sổ phủ cả filesystem `/`.** Thêm gốc/dòng vào `storage-registry.tsv` để mọi byte thuộc đúng một dòng: tối thiểu `/var/lib/docker` (tách volume theo tên · image/overlay · log container), `/var/lib/containerd`, `/var/lib/incomex*`, `/var/log`, phần còn lại của `/var`, `/home`, `/root`, `/tmp`, `/usr`, phần còn lại của `/opt`, swapfile, và dòng `DELETED_OPEN` (tệp đã xoá còn bị tiến trình giữ). Mỗi lượt taxonomy tính `UNEXPLAINED = df_used − Σ dòng`; |UNEXPLAINED| > 1 GiB ⇒ đỏ.
Trần dòng mới = max(đo × 1,25 ; đo + 0,5 GiB), làm tròn lên 0,25 GiB, ghi số đo gốc; dữ liệu nghiệp vụ (PG18, Qdrant, tệp Directus) = `-` kèm dự kiến tăng. **Nhóm Graph trial** (image neo4j/cognee/pgvector + volume + runtime trial + `/opt/incomex/work/graph-server`): **trần nhóm 10 GiB**, owner `GS` (quyết định graph-server: “Image + volume + build cache + log của trial ≤ 10 GB”). Không xoá gì.

**B3 · chuông tự gọi tên.** Khi SLOPE24/SLOPE7D/UNEXPLAINED/CAP kích hoạt: đo taxonomy ngay trong lượt đó, so từng dòng với lượt taxonomy gần nhất cách ≥ 20 h, đưa 3 dòng tăng nhiều nhất (tên ngắn +GiB) vào lý do gửi #11 (≤ 180 ký tự).

**B4 · chuông không tự lành.** SLOPE chỉ đỏ khi phần giảm KHÔNG quy được ≥ 90% về các dòng có trần và còn dưới trần; phần quy được ⇒ không đỏ, lên bản tin 08:00. Vượt trần / vô danh là điều kiện theo MỨC ⇒ đỏ tới khi dọn hoặc trần được sửa qua Config Guard; không xanh lại chỉ vì 24h trôi qua. Chưa đủ hai lượt taxonomy để quy ⇒ giữ hành vi cũ (đỏ).

**B5 · bản tin 08:00** (vẫn trong 3 dòng): `💽 trống X GiB · 24h −Y · lớn nhất: <tên> +Z`.

Thử (fixture qua các biến `SW_*`, không đụng dữ liệu thật): t1 mục lạ ngoài `/opt` +2,1 GiB ⇒ đỏ đúng tên · t2 nhóm Graph tăng trong trần ⇒ không đỏ, có dòng bản tin · t3 nhóm vượt trần ⇒ đỏ và còn đỏ sau khi mốc 24h trượt qua · t4 UNEXPLAINED 1,5 GiB ⇒ đỏ · t5–t8 bốn ca B1 đều đỏ, rc ≠ 0.
Chạy thật một lượt `daily`: nộp bảng đối soát `df` ↔ Σ dòng (UNEXPLAINED ≤ 1 GiB; lớn hơn ⇒ tách tiếp; không tách được ⇒ nêu rõ phần còn lại) + 10 dòng lớn nhất. Sau gói B đèn #11 phải phản ánh ĐÚNG thực tế: xanh nếu mọi phần tăng có tên và dưới trần; còn đỏ thì lý do nêu tên thủ phạm — không ép xanh.

## 5 · Gói C — mã có khoá thật (Điều 30/31)
**C1 · đăng ký ngay** `docker/agent-data-repo/scripts/workspace-exec-worker.py` + unit `incomex-workspace-exec.service` (tệp nguồn và bản cài trong systemd) vào Config Guard. Trước khi đăng ký, đối chiếu hash với bản v2 đã nghiệm thu R6W (BAO-CAO R6W, P47); lệch ⇒ không bless, ghi DỪNG riêng C1.

**C2 · “sổ mã đang chạy”.** Liệt kê tất định mọi tệp mã/cấu hình do Incomex viết mà production thực thi: ExecStart/EnvironmentFile của unit systemd ngoài distro · mọi lệnh trong crontab root và `/etc/cron.d/*` · compose + tệp mount vào container + image ID đang chạy của từng dịch vụ · `dot/bin/*` · `scripts/*` được gọi · cấu hình nginx/logrotate của Incomex. Không gồm thư viện bên thứ ba. Đối chiếu Config Guard ⇒ nộp `N đang chạy · M có khoá · K hở` + danh sách K. Đăng ký K (hash hiện hành, lý do “đăng ký lần đầu R7”; được khoá theo cây cho thư mục mã). Thêm một invariant vào Guard theo khung INV sẵn có: tệp thực thi mới ngoài sổ ⇒ đỏ (fail x2) kèm tên; vùng không quét được ⇒ `UNKNOWN`, không tuyên bố đủ.

**C3 · cổng POST-PROTECT trên footprint thật.** Sửa `mode_pre_post`: PRE lưu manifest (đường dẫn → sha256) của toàn bộ bề mặt C2; POST lấy footprint thật = mọi đường dẫn thêm/đổi/xoá. Với TỪNG đường dẫn, bảng coverage do RUN nộp (`--coverage <tệp>`) phải đủ 4 ô: **Đ31** (đã ở Config Guard với hash mới) · **Đ30** (tên test + PASS + đường dẫn bằng chứng) · **watchdog** (đèn/invariant nào canh) · **rollback** (bản known-good tồn tại + hash). Thiếu một ô ⇒ POST FAIL, in `THIẾU <đường dẫn>:<ô>`; footprint ≠ rỗng thì `--receipt` bắt buộc; chữ “bảo vệ đủ” chỉ được sinh khi bảng đủ. Máy chỉ kiểm ĐỦ LỚP, không tự sinh test. PRE cũ không có manifest ⇒ chạy luật cũ + cảnh báo (không hồi tố lượt đang chạy).
Thử âm: n1 đổi một tệp ngoài bảng ⇒ FAIL · n2 thiếu rollback ⇒ FAIL · n3 bảng đủ ⇒ PASS + biên nhận (chế độ thử, không gửi Owner) · n4 footprint ≠ rỗng mà không có `--coverage` ⇒ FAIL.
Selftest Guard PASS trước/sau; hai nhịp periodic liền sau khi sửa phản ánh đúng thực tế.

## 6 · Gói D — 502/503: chứng minh nguyên nhân, không đụng lõi
**D1 · sổ áp lực** (không thêm cron/timer): ghép vào nhịp periodic 5′ của Guard, bọc lỗi riêng để không bao giờ làm Guard đỏ; mỗi nhịp một dòng: PSI cpu/memory/io (`/proc/pressure/*`, gồm `total`) · MemAvailable · swap dùng · với từng container và 5 cgroup ngoài container có RSS lớn nhất: `memory.current`, `memory.swap.current`, `memory.events`, `memory.pressure`, `cpu.stat` (throttled). Tệp vòng ≤ 20 MiB, giữ 14 ngày, có dòng ở storage-registry + Config Guard. Không có PSI ⇒ ghi loadavg + top RSS và nêu rõ.

**D2 · bảy lần `Child process died`** (docker logs có giờ): mỗi lần ghi giờ chính xác · pid · thời gian tới khi có tiến trình thay · request cuối của pid · kernel log ±60 s · `memory.events`/swap của cgroup agent-data. Xác nhận phiên bản uvicorn thật trong image đang chạy (chỉ đọc) và đoạn mã supervisor tương ứng. Phân loại từng lần: `SUPERVISOR_PING_TIMEOUT` · `CRASH` (có traceback) · `OOM_KILL` · `KHÔNG ĐỦ BẰNG CHỨNG`. Không thử tải, không giả lập trên production.

**D3 · Directus 503:** lấy body/headers thật (log A1 mới, hoặc `upstream_status` của nginx) ⇒ xác nhận hay bác “pressure limiter”; đọc tên + giá trị không bí mật của `PRESSURE_LIMITER_*` đang hiệu lực.

**D4 · trình duyệt headless:** tiến trình/unit nào sở hữu cgroup 6 GiB bị OOM 06/10 14:24, 14:26, 15:48 (+07); ai gọi; trần đặt ở đâu. Được hạ trần xuống **2 GiB** + tối đa **1 phiên đồng thời** CHỈ KHI đó là giá trị trong unit/cấu hình do Incomex quản, đổi không cần restart 6 container lõi, và bộ test UI/chụp màn hình hiện hữu chạy lại PASS; không đủ điều kiện ⇒ chỉ đề xuất.

**D5 · dồn cron:** liệt kê mọi job nổ cùng phút chia hết cho 5 (kèm thời lượng chạy); chỉ đề xuất phương án dàn lệch, không đổi lịch trong lượt này.

**D6 · phiếu đề xuất N2 cho Owner** (≤ 12 dòng; mỗi dòng: việc · số cụ thể · gián đoạn · đường lùi · bằng chứng). Số Host đã chốt sẵn để điền nếu bằng chứng khớp — agent không tự chọn số khác, thấy cần khác thì nêu lý do: nếu D2 = `SUPERVISOR_PING_TIMEOUT` ⇒ uvicorn 0.35.0 → **0.37.0** + cờ `--timeout-worker-healthcheck 30` (rebuild + recreate agent-data, gián đoạn MCP ~1 phút), kèm việc gỡ tận gốc chỗ chặn/thiếu RAM đã đo được; trần RAM cho tải thử (trình duyệt, Graph trial) để production không bị đẩy ra swap; xả swap có kiểm soát; ngưỡng pressure limiter của Directus.

## 7 · POST-PROTECT
Chạy Guard `post` bằng **cổng mới C3** với `--coverage` phủ footprint thật của chính R7 (A+B+C+D) + `--receipt` (≤ 3 dòng tiếng Việt, có màu; lưu message_id). Config Guard CLEAN. Còn một ô `THIẾU` ⇒ KQ không được là XONG.

## 8 · KQ và báo cáo
- `## R7` trong BAO-CAO: bảng A/B/C/D (đạt · chưa đạt · bằng chứng), bảng 22 đèn trước/sau, bảng đối soát ổ đĩa, `N/M/K` sổ mã, bảng 7 lần chết + phân loại, phiếu D6.
- **Sổ tồn đọng — chỉ ghi, không sửa; mỗi dòng: gì · bằng chứng · chủ:** AD1 p95 348 s > 300 và “lệch phụ p02” thường trực (HJW) · đèn #22 đỏ lặp theo #11 làm một nguyên nhân thành hai cặp tin (HJW) · hai mục “chưa xác định” VPS2 + Directus Flows/PG trong bản tin 08:00 (GPT root) · worker ghi rỗi 481/168 + transactions GC (chủ agent-data) · Nuxt #6 404, presence 502 (chủ đã ghi ở root) · giữ/xoá dữ liệu Graph trial (GS) · khoá dùng chung đã lộ (N2, chờ Owner).
- Ghi một dòng, cùng lượt cập nhật Bảng: `KQ@VPSC-R7-TRUTH-20261007-01 XONG · A=… · B=… · C=… · D=…` hoặc `KQ@VPSC-R7-TRUTH-20261007-01 DỪNG · <gói> · <lý do chính xác> · đã giữ: <gói PASS>`.
- Trả Owner đúng một dòng XONG/DỪNG. Nghiệm thu là việc của Codex (độc lập, chỉ đọc + thử âm) và Host — agent không tự nghiệm thu.
