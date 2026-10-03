# PROMPT — HJW · ASSIGNMENT CONTRACT V1 + HERMES READINESS CANONICAL

RUN_ID: HJW-ASSIGN-CONTRACT-READINESS-20261003-05
STATUS: DRAFT — chờ Claude Founder/Reviewer ACCEPT P95 rồi Host READY
Host: GPT Chat · GPT-HJW-260922-A
Executor_Surface: Claude Code CLI phiên mới
Write_Path: DOT/script-wrapper hiện hữu; repo qua workspace_*; runtime mutation chỉ qua wrapper quản lý
Owner_authorization: 03/10/2026 — chuẩn hóa giao việc chung, Hermes phải tự readiness rồi Host tổng hợp lỗi trước lượt sửa cuối.

## 0. Mục tiêu duy nhất của RUN này
1. Cưỡng chế Assignment Contract V1 để mọi AI/Agent/dispatcher dùng cùng một ngôn ngữ.
2. Sau khi contract + tests PASS, tạo **một assignment canonical** cho Hermes tự kiểm readiness.
3. Nhận báo cáo Hermes trên repo và KQ; **không sửa D30/D31 trong RUN này**. Host sẽ đọc report rồi gom lỗi vào lượt sửa cuối.

## 1. PRE / khám phá mã thật
- Đọc AGENTS → root COLLAB DROOT37–39 → HJW Bảng + P94–P95 → prompt này.
- Xác nhận RUN cũ chưa STARTED; READY cũ hết hiệu lực do prompt này là last-touch mới.
- Tìm đúng runtime hiện hữu đang: parse assignment → tạo card → xử lý callback approval → queue/claim → wake Hermes → gửi START/RESULT.
- Ghi đường file/config/job thật + hash trước sửa. Không suy từ tài liệu.
- Không tạo service/DB/bot/token/route mới; reuse đường HJW hiện hữu.
- Legacy -01/-02 nếu đang có chỉ là evidence; không dùng làm acceptance canonical.

## 2. Assignment Contract V1 — parser bắt buộc
Trong COLLAB HJW dùng đúng machine-zone:
`<!-- MACHINE_ASSIGNMENTS_V1:BEGIN -->`
`ASSIGN_V1 {"id":"...","to":"Hermes","role":"Reviewer|Agent","generation":1,"state":"open|claimed|done|blocked","approval":"owner","task":"...","output":"...","read":["..."],"write":["..."],"spec_ref":"...","run":"... optional"}`
`<!-- MACHINE_ASSIGNMENTS_V1:END -->`

Luật:
- Chỉ dòng bắt đầu **cột 1** bằng `ASSIGN_V1 ` và nằm giữa đúng hai marker mới được parse.
- Mọi legacy `ASSIGN@`, prose, quote, backtick, code sample, lịch sử ngoài zone = inert.
- Required: id,to,role,generation,state,approval,task,output,read,write,spec_ref. task/output rỗng hoặc "." = invalid.
- Identity người giao lấy từ gateway/Git author server-side, không từ field JSON.
- role=Agent có mutation phải thêm `run=<RUN_ID hiện hành>` và vẫn qua A6 READY/RUN/HOLD; Reviewer không được tự mutation production.
- `spec_ref` phải unique trong cùng task; dispatcher hash canonical JSON + bytes spec để bind approval.

## 3. Approval / claim / queue
- Record valid + state=open ⇒ gửi đúng 1 card PENDING APPROVAL; 0 model.
- Owner bấm Cho chạy ⇒ tạo ticket bền: assignment id + generation + content/spec hash + approved_at + Owner identity. AI không bấm thay.
- Record/spec đổi sau duyệt ⇒ ticket invalid, không claim; muốn đổi phải generation+1 và duyệt lại.
- Approval không đồng nghĩa START. Với `cron.max_parallel_jobs=1`: nếu slot bận, card chuyển `ĐÃ DUYỆT · XẾP HÀNG`; queue order approved_at rồi id.
- Khi slot rảnh: deterministic gate → expected_version claim open→claimed → gửi BẮT ĐẦU thành công → mới wake model.
- Telegram lỗi trước BẮT ĐẦU ⇒ không wake.
- Hai record cùng id+generation: exact replay idempotent; khác nội dung = invalid/conflict, không chọn đại.

## 4. Kết quả chuẩn
Hermes hoàn tất phải trong cùng commit:
- đổi canonical record claimed→done|blocked;
- ghi detailed report tại report_ref;
- ghi `RESULT_V1 {"id":"...","generation":1,"status":"done|blocked","summary":"...","commit":"<40hex>","next":"...","report_ref":"..."}`.
Telegram KẾT QUẢ lấy từ RESULT_V1/structured state; không suy prose.
Blocked phải nêu blocker + ai/việc nào nhận tiếp. Không tự mở quyền.

## 5. Test cưỡng chế trước khi giao Hermes
Bắt buộc PASS:
A. prose chứa nguyên legacy marker + state=open ⇒ 0 card.
B. code/backtick/example ⇒ 0 card.
C. canonical valid ⇒ đúng 1 card.
D. task="." / thiếu output / spec_ref không tồn tại ⇒ 0 card + validation error.
E. duplicate exact same id/gen ⇒ 1 card, 1 model tối đa.
F. same id/gen nhưng payload khác ⇒ conflict, 0 claim.
G. Owner approve rồi sửa spec ⇒ ticket invalid, 0 claim.
H. 2 assignment canonical cùng approved ⇒ max 1 claimed; việc 2 = queued; sau done việc 1 mới claim việc 2.
I. Owner reject ⇒ 0 model.
J. Telegram pre-start failure ⇒ 0 model.
K. write/read ngoài scope safe-deny fixture hiện hữu ⇒ blocked.
L. restart dispatcher không mất durable approval/queue/idempotency.
M. RESULT thiếu commit/report_ref ⇒ không được DONE.
Có mutant/negative + rollback; delta runtime vào Config/Protection Guard theo DROOT29–31.

## 6. Readiness canonical của Hermes
Chỉ sau §5 PASS:
- Tạo machine-zone nếu chưa có.
- Tạo spec `SPEC@HJW-HERMES-READINESS-20261003-02` trong COLLAB HJW, nội dung theo P94/P95: identity server-side/profile; gateway/session/model wake; workspace read/write; Telegram approval/start/result proof; tool allowlist/scope; role Hermes có thể/không được làm; lỗi/thiếu; kết luận READY|PARTIAL|BLOCKED.
- Tạo canonical id `HJW-HERMES-READINESS-20261003-02`, role=Reviewer, approval=owner, read AGENTS + HJW, write chỉ HJW COLLAB.
- Claude Code chỉ tạo record/spec và xác nhận card. Owner tự bấm.
- Hermes tự claim/run/report; Claude Code không làm thay.
- Nếu Owner chưa duyệt, KQ = CHECKPOINT chờ Owner, không giả READY.

## 7. KQ
XONG chỉ khi Contract V1 enforcement + §5 tests PASS **và** Hermes có RESULT_V1 + report repo:
`KQ@HJW-ASSIGN-CONTRACT-READINESS-20261003-05 XONG · CONTRACT_V1_PASS · HERMES_READINESS=<READY|PARTIAL|BLOCKED>`

Nếu contract/tests fail: rollback delta, `KQ@... DỪNG · CONTRACT_BLOCKED:<lý do>`.
Nếu contract PASS nhưng chờ Owner: `KQ@... DỪNG · CONTRACT_V1_PASS · HERMES_WAITING_OWNER`.

Sau KQ dừng. Host đọc report Hermes, tổng hợp các vấn đề rồi mới soạn lượt cuối D30/D31 + residual readiness.

---

# VÒNG TRƯỚC — HJW FINAL D30/D31 (P92/P93; READY cũ hết hiệu lực sau prompt này)
# PROMPT — HJW · LƯỢT CUỐI: (1) vá báo động giả D30 → (2) người canh ngoài máy chủ D31 → đóng

RUN_ID: HJW-FINAL-D30-D31-20261002-04
Host: GPT Chat · GPT-HJW-260922-A
Owner_authorization: 02/10/2026 — ~21:40 Owner gật dùng dịch vụ canh miễn phí ngoài VPS; 21:46 Owner: phiên này chỉ làm việc của phiên này (Hermes/workspace/tin báo), làm xong rồi đóng; không đặt, không nhắc, không chờ bước của việc khác (nguyên văn ở HJW COLLAB §0).
Reviewer: Claude Chat · ACCEPT-with-delta tại P90; rà kỹ lại + 5 sửa nhỏ tại P92 (bản này).
Executor_Surface: Claude Code CLI phiên mới.
Write_Path: DOT/script-wrapper hiện hữu; runtime mutation qua incomex-config-apply-v0 hoặc wrapper chuẩn. Không ad-hoc.

## 0. Mục tiêu duy nhất
Hai việc còn lại của chính HJW, làm theo thứ tự — xong việc 1 và kiểm xong mới sang việc 2:
1. **D30:** đóng hồi quy do P86 phát hiện — PRE/POST của `mcpw-protection-guard` không được gọi GitHub anonymous/ruleset lặp lại và không được làm AD1 `rest_anon >2/h` đỏ giả.
2. **D31:** lỗ “cả VPS chết/mất mạng thì checker chết cùng” — dựng người canh ngoài máy chủ (§3B) và ghi nó vào sổ tin báo.
RUN này không đọc, không nhắc, không chờ, không bàn giao cho việc nào khác (DROOT37).

## 1. PRE — chỉ đọc, 0 GitHub anonymous
- Đọc AGENTS → HJW COLLAB (Bảng điều khiển + §0 + từ P86 trở đi) → prompt này.
- Không chạm task/file/lịch/runtime của việc khác; gặp va chạm trên máy chủ ⇒ dừng báo Host.
- Đo baseline: AD1/rest_anon, #22, Guard/Config Guard, hash Guard live, registry/baseline, sổ tin_bao.
- PRE của chính RUN dùng snapshot/state local; **0 request GitHub anonymous**.
- Không restart/reload dịch vụ; không bot/service/timer/DB/đèn Kuma mới.
- Không áp thay đổi lên Guard trong khoảng 07:55–08:10 +07; nếu bản tin sáng hôm đó chưa có trong sổ cái thì chờ nó gửi xong (không làm hỏng bản tin 08:00).

## 2. Sửa nhỏ nhất
- Tìm đúng nhánh PRE/POST đang gọi ruleset/GitHub anonymous.
- Reuse snapshot/cache ruleset PASS hiện hữu; không thêm service/timer/DB.
- Cache có source/timestamp/TTL rõ + integrity protection.
- Fail-closed: cache thiếu/stale/corrupt/mismatch ⇒ PRE/POST FAIL; tuyệt đối không fallback anonymous GitHub.
- Không nới AD1 threshold, không whitelist chính mình, không che số đo.

## 3. Sổ tin báo — một dòng cho người canh ngoài
Thêm một dòng vào registry hiện hữu: `Người canh ngoài máy chủ` — nghĩa: VPS chết/mất mạng ⇒ Kuma/Guard/bot cùng im, phải có nơi ngoài VPS báo thay. Khi chưa dựng xong: trạng thái `hỏng: HJW-D31 (chờ dựng)` ⇒ bản tin 08:00 phản ánh K≥1, không làm Guard đỏ lặp 5′ (hỏng đã ghi sổ + việc nhận). Dựng xong và thử PASS ở §3B ⇒ đổi thành `chạy` kèm cách đo sống.

## 3B. D31 — người canh ngoài máy chủ (chỉ bắt đầu sau khi D30 ở §4 đã PASS)
Đích: VPS1 tắt hẳn hoặc mất mạng ⇒ trong ≤15 phút Owner nhận tin Telegram từ một nơi **không nằm trên VPS1**.
1. **Chọn dịch vụ (chỉ đọc, không dựa trí nhớ):** mở trang chính thức của 2–3 dịch vụ canh miễn phí, chọn MỘT theo tiêu chí bắt buộc: nằm ngoài VPS1 và ngoài nhà cung cấp máy chủ · gói miễn phí hiện hành cho phép cách dùng này · tự nhắn Telegram cho Owner bằng kênh của chính dịch vụ (không qua bot của ta) · chu kỳ phát hiện ≤5′. **Ưu tiên cách không phải sửa gì trên VPS1** (dịch vụ tự thăm từ ngoài một địa chỉ sức khoẻ công khai đang có); chỉ dùng cách “máy chủ gõ cửa” khi cách kia không đạt tiêu chí. Hỏi JEV trước khi chốt; ghi 3 dòng lý do.
2. **Việc của 😊 Owner — gom một lần, ≤5 phút, hướng dẫn từng bước bấm gì ở đâu:** đăng ký bằng email của Owner · xác nhận email · bật kênh Telegram của dịch vụ. Agent không tạo tài khoản thay, không giữ mật khẩu. Dịch vụ đòi thẻ/thanh toán ⇒ dừng, chọn dịch vụ khác. Khoá/địa chỉ bí mật (nếu có) chỉ nằm root-only trên VPS; không vào repo/KQ/log/tin nhắn.
3. **Đúng MỘT phép canh.** Mô tả cấu hình (không bí mật) ghi vào hồ sơ RUN để dựng lại được.
4. **Thử thật, không tắt máy chủ, không restart:** báo Owner một câu, rồi làm phép canh “thấy im” một cách an toàn (ví dụ trỏ tạm vào từ khoá không tồn tại, hoặc ngừng gõ cửa quá hạn) ⇒ Owner nhận tin đỏ từ dịch vụ ⇒ trả lại đúng ⇒ Owner nhận tin xanh. Nói rõ tin nằm ở khung chat nào.
5. **Sổ tin báo:** dòng `Người canh ngoài máy chủ` = `chạy`, có cách đo sống tại chỗ (thấy lượt thăm từ ngoài trong log, hoặc lần gõ cửa gần nhất được nhận); im quá hạn ⇒ INV16 đỏ. Có sửa gì trên VPS ⇒ Config Guard + mutant + rollback theo §5.
6. **Owner vắng hoặc chưa đăng ký được:** không tự tìm đường khác; dòng sổ giữ `hỏng: HJW-D31 (chờ Owner đăng ký)`; KQ theo §7.

## 4. Điều 30 — acceptance
Sau patch:
1. chạy ≥4 chu kỳ PRE+POST liên tiếp — các lượt thử **không gửi tin cho Owner** (không `--receipt`, hoặc gửi vào fixture);
2. mỗi chu kỳ dùng snapshot/cache, 0 GitHub anonymous;
3. `rest_anon` không tăng do các chu kỳ;
4. #22 không DOWN do AD1/rest_anon;
5. receipt path vẫn PASS: cuối RUN gửi đúng MỘT biên nhận thật ≤3 dòng cho thay đổi của RUN;
6. mutant: stale, missing, corrupt, mismatch ⇒ FAIL và không fallback anonymous;
7. INV14–17 + Config Guard + sổ tin báo + Kuma fleet giữ PASS.
8. D30 không đạt ⇒ rollback về bytes trước RUN, KQ đuôi `BLOCKED · <lý do>`, **không sang D31**.

## 5. Điều 31 — bảo vệ delta
- Guard sửa ⇒ Config Guard baseline qua apply path chuẩn.
- Cache/snapshot có integrity + TTL invariant.
- Selftest có mutants §4.
- Watchdog #22/CTR-WATCHDOG giữ sống.
- Rollback bytes trước RUN + baseline tương ứng.
- Coverage table D30/D31/watchdog/rollback; có THIẾU ⇒ không XONG.

## 6. Trạng thái sau RUN
KQ ghi `GUARD_SHA_AFTER=<sha256>` và Config Guard CLEAN, như mọi RUN. Không viết lời nhắn, điều kiện hay bàn giao cho việc khác.

## 7. KQ
KQ ghi hai dòng kết quả riêng:
`D30: 4x PRE/POST · anonymous_git=0 · rest_anon_delta=0 · #22_no_false_red=PASS · stale_mutants=PASS · ConfigGuard=CLEAN`
`D31: người canh ngoài=<tên dịch vụ> · Owner nhận tin đỏ + tin xanh · dòng sổ=chạy · đo sống tại chỗ=PASS`

Đủ cả hai:
`KQ@HJW-FINAL-D30-D31-20261002-04 XONG · D30_CLEAN · D31_EXTERNAL_WATCH`
D30 đạt mà Owner chưa kịp đăng ký: cùng tiền tố, đuôi `D30 XONG · D31 CHỜ OWNER` (dòng sổ giữ `hỏng: HJW-D31`).
D30 không đạt: cùng tiền tố, đuôi `BLOCKED · <lý do>` (đã rollback, chưa làm D31).

Sau KQ dừng. Host + Claude nghiệm thu một lượt rồi đóng HJW.

---

# VÒNG TRƯỚC — HJW SỔ TIN BÁO / RECEIPT (KQ 1a76b09 · chức năng ACCEPT)
# PROMPT — HJW · SỔ TIN BÁO + ĐIỂM DANH mỗi sáng + biên nhận sau thay đổi

RUN_ID: HJW-POST-PROTECT-RECEIPT-20261002-03
Host: GPT Chat · GPT-HJW-260922-A
Owner_authorization: 02/10/2026 — sau mọi thay đổi production, hệ thống phải báo Telegram rằng đã đổi gì và trạng thái bảo vệ cuối cùng; không được im lặng chỉ vì mọi đèn vẫn xanh. Bổ sung theo lựa chọn Host được Owner giao 02/10 ~20:05: thêm positive heartbeat 08:00 mỗi sáng để ngày không có mutation vẫn chứng minh đường báo còn sống; dùng Guard/cron hiện hữu, không timer/bot mới. Bổ sung Owner 02/10 20:07 (nguyên văn ở HJW COLLAB §0): phải biết được đang báo bao nhiêu loại tin về điện thoại, bao nhiêu loại còn chạy, bao nhiêu loại đã hỏng; xử lý dứt điểm một lần rồi bảo vệ bằng Điều 30/31.
Reviewer: Claude Chat · ACCEPT-with-delta tại P82 (bản này).

## 0. Mục tiêu duy nhất

KQ `c38539d` về Kuma/Telegram **đạt kỹ thuật**; không làm lại K1/K2/Kuma Down-Up. Việc còn lại, theo đúng lời Owner 20:07, xếp theo thứ tự quan trọng:
1. **Sổ tin báo + điểm danh (§2C):** máy tự trả lời mỗi ngày ba con số — đang báo bao nhiêu loại tin về điện thoại Owner · bao nhiêu loại còn chạy · bao nhiêu loại đã hỏng — và loại nào hỏng/mất/mới thêm đều lộ ra ngay.
2. **Bản tin 08:00 mỗi sáng (§2B)** mang kết quả điểm danh đó tới điện thoại.
3. **Biên nhận sau mỗi thay đổi production (§2).**
Cả ba dùng chung một hàm gửi; làm một lần, có Điều 30/31 giữ.

## 1. Ranh giới
- Không restart/reload service chỉ để tạo alert.
- Không tạo bot/token/service/timer/DB/monitor mới.
- Reuse đúng đường Telegram Owner hiện hữu; receipt không phụ thuộc Kuma state transition.
- Reuse DOT/script-wrapper hiện hữu; nếu có common post-hook thì gắn tại đó. Nếu chưa có common hook, bổ sung nhỏ nhất vào wrapper/template hiện hữu, không dựng pipeline riêng.
- Mọi file/config runtime mới/sửa trong RUN này tự tuân AUTO-PROTECT DROOT29/A10-R4.
- Sổ tin báo không là file rời: danh sách chuẩn nằm trong Guard/registry hiện hữu (Config Guard canh); kết quả điểm danh ghi vào `bang-den.json` hiện hữu.
- Gặp bí mật ghi cứng trong script (token bot, chat id…) ⇒ KHÔNG chép giá trị vào repo/KQ/tin; chỉ ghi tên file + việc nhận. Repo PUBLIC.
- Việc của 😊 Owner: xem tin thử trên điện thoại và trả lời **một lần, gom gọn**. Không hỏi Owner chi tiết kỹ thuật.

## 2. Hành vi bắt buộc
Sau POST-PROTECT PASS của một mutation production, gửi **đúng một** tin Telegram cho người, **tối đa 3 dòng tiếng Việt thường, có biểu tượng màu**: dòng 1 = vừa đổi gì / `NO-CHANGE VERIFY`; dòng 2 = `đèn N/N xanh · bảo vệ đủ · có đường lùi` (đỏ thì nêu tên); dòng 3 = RUN/commit ngắn. Footprint/D30/D31/Config Guard/Protection Guard/rollback chi tiết lưu trong repo/evidence, không nhồi vào tin.
- Không có state transition vẫn phải gửi.
- Nếu verify-only/no-op thì ghi rõ `NO-CHANGE VERIFY`, không giả là đã deploy.
- Lưu delivery proof/message_id vào evidence/ledger hiện hữu; không tạo sổ mới.
- Telegram fail ⇒ POST-PROTECT không success; KQ PARTIAL/BLOCKED.
- Receipt không thay cảnh báo thật của Kuma; Down/Up vẫn theo Kuma.

## 2B. Positive heartbeat 08:00 — ngày không đổi gì vẫn phải có tin
- Reuse **chính sender + Guard/cron hiện hữu**; không service/timer/bot/token mới.
- Mỗi ngày **08:00 Asia/Ho_Chi_Minh**, gửi đúng một tin tối đa 3 dòng:
  1. `📋 Tin báo: N loại · M chạy · K hỏng` — số lấy từ điểm danh §2C (đèn Kuma là một phần của sổ); K>0 thì kê tên; khác hôm qua thì thêm `mới: … / mất: …`. Loại hỏng được nhắc lại **mỗi sáng** cho tới khi hết.
  2. `🤖 AI hôm qua: <n> phiên · thiếu hook/ngoài sổ: <k>` — lấy deterministic từ lifecycle ledger/presence hiện hữu, không gọi LLM.
  3. `🛡️ Bảo vệ: <sạch|có cảnh báo> · 08:00`.
- Idempotent theo ngày trong state/ledger hiện hữu; không tạo DB/sổ mới.
- Nếu đến 08:10 chưa có delivery success marker ⇒ checker hiện hữu phải FAIL/đỏ và thử đường cảnh báo dự phòng hiện hữu. Nếu toàn bộ Telegram hỏng, việc Owner không thấy heartbeat 08:00 là dead-man cuối cùng.
- KQ phải nói rõ **tin sẽ nằm ở khung chat Telegram nào** bằng tên hiển thị/kênh đã cấu hình; không in token/chat id bí mật.
- Không cần chờ tới sáng mai để nghiệm thu: gọi cùng hàm một lần với nhãn `THỬ BẢN TIN 08:00`; Owner xác nhận thấy tin. Lịch thật vẫn 08:00.

## 2C. Sổ tin báo + điểm danh — việc chính của RUN (Owner 02/10 20:07)
Owner: “lẽ ra Kuma phải báo khoảng 10 loại thông tin, bằng cách nào đó nó chỉ báo có 4, 6 cái âm thầm hỏng không ai biết… Làm thế nào để biết hiện nay chúng ta báo bao nhiêu loại thông tin về điện thoại? Có bao nhiêu loại vẫn đang chạy? Có bao nhiêu loại đã hỏng rồi?” ⇒ ba con số này phải có câu trả lời **mỗi ngày, do máy tự đếm**. Ví dụ xuyên suốt: sổ lớp + điểm danh — có sổ thì mới biết lớp bao nhiêu người, ai vắng, ai mới vào.
1. **Kiểm kê (chỉ đọc) mọi loại tin có thể tới điện thoại Owner**, không chỉ đèn Kuma:
   a. từng đèn Kuma (21);
   b. từng phép kiểm gộp trong đèn #22 (bất biến Guard, AD1, Config Guard) và đèn #21 (HJW control);
   c. từng loại tin bot gửi thẳng (thẻ duyệt, bắt đầu, kết quả, commit, dừng, báo đèn câm, safe-update, biên nhận, bản tin sáng);
   d. mọi script/cron/unit/job khác tự nhắn Telegram hoặc tự đẩy Kuma — quét mã + crontab + cron.d + systemd + job của Hermes. Reviewer đã thấy ít nhất 2 nguồn nhắn thẳng không qua đèn nào: `env-permissions-guard.sh`, `git-push-gh-daily-v2.sh`;
   e. loại **đã từng có nay mất hoặc đã cho nghỉ** (ví dụ #13; Disk Usage + Cron Heartbeat chết 04→09/2026) — ghi để biết đã mất gì.
2. **Sổ:** mỗi dòng = mã · tên tiếng Việt thường · nhóm · nguồn phát · đi qua đèn/bot nào · nhịp mong đợi · **cách đo còn sống** · hỏng thật thì đỏ bằng cách nào (`tự đẩy đỏ` / `im thì đỏ` / `THIẾU`) · trạng thái `chạy|hỏng|nghỉ` · lần cuối có tín hiệu · lần cuối có bằng chứng tới Telegram.
3. **Đo “còn sống” từng loại mà không chờ đổi trạng thái:** đèn đẩy = có nhịp trong chu kỳ; đèn thăm dò = Kuma còn thăm đúng chu kỳ; phép kiểm trong #22/#21 = có kết quả ở vòng chạy gần nhất; nguồn nhắn thẳng = lần chạy gần nhất của cron/unit có thật và đúng lịch; tin bot theo sự kiện = hàm gửi còn sống (bản tin sáng là phép thử hằng ngày). Loại nào không đo được ⇒ ghi `hỏng: không đo được`, không tính là chạy.
4. **Điểm danh trong Guard hiện hữu, cùng nhịp 5′ (không đèn/timer mới):** thực tế khác sổ theo cả hai chiều ⇒ đỏ: (i) loại ghi sổ mà mất/câm/hỏng; (ii) nguồn gửi tin tồn tại mà chưa ghi sổ (quét tất định các thư mục script/cron đã khai; ngoài tầm quét thì ghi rõ giới hạn). `nghỉ` chỉ hợp lệ khi có lời Owner ghi ở §0.
5. **Loại đang hỏng tìm thấy khi kiểm kê:** sửa nhỏ trong scope thì sửa; không thì kê tên + việc nhận (DROOT34) và nó phải hiện trong bản tin sáng. Không giấu để đẹp số.
6. **Chứng minh tới điện thoại:** loại nào chưa từng có bằng chứng tin tới Telegram (không có trong lịch sử Owner 27/09→02/10 và chưa thử hôm nay) ⇒ thử một lần có nhãn `THỬ`; gom trong một cửa sổ ≤10 phút, báo Owner một câu trước. Không restart dịch vụ.
7. **Luật thêm/bớt:** từ nay thêm, bớt, đổi nguồn một loại tin báo phải sửa sổ trong cùng RUN (DROOT29/DROOT36); không ghi sổ ⇒ Guard đỏ.

## 3. Test — không restart
1. PRE đọc current fleet/Guard/Config Guard, lifecycle ledger và current sender/receipt path.
2. Implement sender dùng chung cho POST-PROTECT receipt + heartbeat 08:00.
3. Chạy **verify-only/no-op POST-PROTECT** trên trạng thái hiện tại: không mutation production, không restart; Owner nhận một receipt ≤3 dòng.
4. Gọi cùng sender một lần với nhãn **THỬ BẢN TIN 08:00**; Owner nhận bản tin heartbeat ≤3 dòng và executor nói rõ nó nằm ở khung chat nào.
5. Lưu message_id/timestamp cho cả hai; kiểm idempotency không gửi lặp.
6. Negative: giả delivery fail ⇒ POST-PROTECT FAIL/PARTIAL và checker đỏ qua đường dự phòng; không xanh giả.
7. Regression: Kuma fleet vẫn toàn xanh; Guard/Config Guard không drift; HJW/K1/K2 không đụng.
8. Mutant sổ tin báo: (a) một loại ghi sổ bị câm/mất ⇒ đỏ + có tên trong bản tin thử; (b) một nguồn gửi tin lạ chưa ghi sổ ⇒ đỏ; (c) đổi một loại sang `nghỉ` mà không có lời Owner ⇒ đỏ; sổ sạch ⇒ xanh.

## 4. AUTO-PROTECT cho chính thay đổi này
Bảng coverage bắt buộc: file/config/script vừa đổi → D30 → D31 → watchdog → rollback → ĐỦ. Nếu THIẾU thì không XONG.

## 5. KQ
KQ mở đầu bằng ba con số: `TIN BÁO <UTC>: N loại · M chạy · K hỏng [tên → việc nhận]`, kèm bảng sổ gọn theo nhóm để Owner xem một lần.
Chỉ XONG khi: sổ tin báo đủ §2C · Guard điểm danh hai chiều đang chạy · mutant §3.8 bắt đủ · Owner thực nhận **cả receipt no-op và bản tin thử 08:00 (có dòng điểm danh)** qua đúng sender, có delivery proof · lịch 08:00 đã được gắn vào cron/Guard hiện hữu:
`KQ@HJW-POST-PROTECT-RECEIPT-20261002-03 XONG · RECEIPT_DELIVERED`
Nếu chưa nhận:
`KQ@HJW-POST-PROTECT-RECEIPT-20261002-03 BLOCKED · RECEIPT_NOT_DELIVERED`

Sau KQ dừng; Host+Claude nghiệm thu một lượt. Không restart hàng loạt để thay cho test receipt.

---

# VÒNG TRƯỚC — KUMA FINAL CLOSEOUT (KQ c38539d · kỹ thuật PASS, chờ receipt trước đóng)
# PROMPT — HJW KUMA FINAL CLOSEOUT · all green + Telegram both directions + direct protection

RUN_ID: HJW-KUMA-CLOSEOUT-20261002-02
Host: GPT Chat · GPT-HJW-260922-A
Owner_authorization: 02/10/2026 — Kuma phải kiểm toàn bộ thay đổi đã thiết lập, báo về Telegram của Owner, và trạng thái cuối phải xanh.
Executor_Surface: Claude Code CLI phiên mới hoặc tiếp phiên hiện tại nếu đã dừng sau KQ; không mở task mới.

## 0. Mục tiêu duy nhất

KQ `4de0d9f` **CHƯA ĐƯỢC HOST ACCEPT**. Đóng đúng lỗ Kuma/Telegram còn lại, không làm lại K1/K2/Hermes compat đã PASS.

Hợp đồng Owner:
1. Toàn bộ monitor Kuma **đang tồn tại và được coi là đang sử dụng** phải được kiểm kê.
2. “TẤT CẢ XANH” chỉ khi: active/up = toàn bộ fleet hợp lệ; **down=0 · paused=0 · unknown=0**. Không được loại monitor paused khỏi mẫu số rồi nói all green.
3. Mỗi monitor đang dùng phải gắn notification Telegram của Owner và cấu hình notification phải được canh.
4. Phải có bằng chứng end-to-end hiện hành cho **cả hai chiều**: Kuma Down → Telegram và Kuma Up/recovery → Telegram.
5. Mọi config/script/lịch cron quyết định heartbeat/Guard/notification phải được bảo vệ **trực tiếp** bằng Config Guard hoặc invariant chính xác; không chỉ chờ hậu quả đỏ.

## 1. PRE — chỉ đọc

- Đọc AGENTS → HJW Bảng/P70 KQ/P72/P73 → prompt này.
- Đọc toàn bộ fleet Kuma từ nguồn thật: id · tên · loại · active/paused · trạng thái · last heartbeat · notification mapping · lần Down gần nhất · lần Up gần nhất.
- Đọc `/opt/incomex/logs/bang-den.json` và đối chiếu 1:1 với fleet thật.
- Đối chiếu lịch sử Telegram Owner đã cung cấp: Disk Usage có nhiều tin **Down** nhưng KQ cũ nói recovery không sinh Up vì “Kuma chưa từng ghi nhận lần hỏng” — phải giải thích mâu thuẫn bằng evidence Kuma DB/log/config, không suy đoán.
- Snapshot `kuma-push.sh`, cron.d liên quan, root crontab/schedule liên quan, Protection Guard/INV15, Config Guard registry, Kuma monitor/notification mapping cần sửa. Rollback trước mutation.
- Không in token/URL push.

## 2. Fleet inventory — không lách paused

- Xuất bảng ngắn toàn bộ monitor: `id | name | status | paused? | Telegram? | owner-task`.
- Monitor paused/disabled/unknown:
  - nếu vẫn là chức năng cần canh ⇒ khôi phục/fix để UP trong scope an toàn;
  - nếu không đủ căn cứ để khẳng định không còn dùng ⇒ **BLOCKER**, không tự loại khỏi fleet, không xóa monitor;
  - chỉ được gọi RETIRED nếu đã có quyết định/evidence rõ ràng trước đó; không tự tạo quyết định retirement.
- Riêng #13 PG Backup Workflow: không được tính “21 xanh · 0 đỏ” là all-green khi #13 còn paused. Xác định nó còn cần hay không; nếu cần thì đưa UP; nếu chưa xác định được thì KQ PARTIAL/BLOCKED và nêu việc chịu trách nhiệm.

## 3. Disk Usage — reconcile lịch sử và recovery

- Xác nhận monitor ID chính xác của Disk Usage và notification mapping.
- Giải thích bằng dòng lịch sử/state thật vì sao Telegram đã nhận nhiều Down nhưng không có Up tương ứng.
- Kiểm sửa vừa làm (khoá nối tiếp/stat row) có giải quyết đúng state machine hay chỉ làm heartbeat trở lại.
- Không giả disk-full. Nếu cần test notification, dùng fixture/canary an toàn §4.
- Disk Usage cuối RUN: UP, heartbeat mới, notification Telegram gắn đúng, bang-den khớp.

## 4. Telegram E2E — chứng minh Down + Up hiện hành

Dùng **đường test/fixture hiện hữu** của Protection Guard/Kuma, không làm hỏng service thật, không tạo monitor mới:
- phát đúng một cặp cảnh báo được gắn rõ `FIXTURE/TEST`: Down → recovery Up;
- cả hai phải đi qua **Kuma notification thật tới Telegram Owner**, không dùng tin HJW bot làm bằng chứng thay thế;
- ghi timestamp + monitor id/name + bằng chứng notification/delivery của cả Down và Up;
- sau test monitor phải trở lại UP và không để fixture đỏ.
Nếu không thể chứng minh Up bằng Kuma hiện hữu ⇒ BLOCKED, không dùng “✅ TẤT CẢ XANH” của bot HJW để thay thế.

## 5. INV15 / bang-den — nghĩa all-green

- INV15 phải FAIL khi có bất kỳ monitor đang dùng: down · paused · disabled trái phép · unknown · stale/no heartbeat · thiếu Telegram mapping · bị xóa/đổi mapping ngoài baseline · Kuma lỗi · notification channel lỗi.
- Không whitelist #13 chỉ vì đã paused từ tháng 5, trừ khi có evidence RETIRED rõ ràng.
- `bang-den.json` phải có tối thiểu: generated_at · total · up · down · paused · unknown · notification_missing · monitors[].
- `all_green=true` chỉ khi down=paused=unknown=notification_missing=0 và mọi monitor hợp lệ UP.
- Mutant/fixture phải chứng minh paused, thiếu Telegram, stale heartbeat và monitor bị xóa đều làm đỏ.

## 6. Direct protection — không chỉ canh hậu quả

Rà các dependency live quyết định Kuma/Guard:
- `kuma-push.sh`
- cron.d Kuma
- **root crontab / schedule liên quan Disk Usage + Protection Guard**
- Protection Guard source
- Config Guard registry
- monitor/notification mapping Kuma (DB/config, canh bằng INV15 nếu không thể file-guard)
- bang-den generator/path

Thiếu trực tiếp ở đâu thì đưa vào Config Guard hoặc invariant chính xác hiện hữu. Root crontab không được để “ngoài Config Guard, chỉ canh hậu quả” nếu nó quyết định nhịp monitor; nếu whole-file baseline quá nhiễu thì invariant exact line/schedule được chấp nhận, nhưng phải phát hiện sửa/xóa/thêm trùng dòng.

Không tạo service/timer/monitor mới.

## 7. Acceptance / KQ

Chỉ XONG khi:
- `KUMA FLEET: total=N · up=N · down=0 · paused=0 · unknown=0 · notification_missing=0`;
- bang-den mới <15′ và khớp fleet;
- Disk Usage UP + heartbeat mới + notification mapping đúng + mâu thuẫn Down/không-Up đã được giải thích;
- một cặp **Kuma Down→Telegram + Kuma Up→Telegram** hiện hành PASS;
- mọi config/schedule live ở §6 có direct protection;
- Config Guard CLEAN; Protection Guard/INV15 PASS; mutants PASS;
- sau fixture toàn fleet trở lại xanh.

Nếu #13 hoặc monitor khác chưa thể hợp lệ hóa trong scope:
`KQ@HJW-KUMA-CLOSEOUT-20261002-02 BLOCKED · <monitor/status/owner-task>`
— không được ghi “tất cả xanh”.

Nếu đủ:
`KQ@HJW-KUMA-CLOSEOUT-20261002-02 XONG · KUMA_ALL_GREEN_TELEGRAM_PROTECTED`.

Sau KQ dừng; Host + Claude Reviewer nghiệm thu một lượt bằng fleet/bang-den + Telegram evidence. Không tự mở việc mới.

---

# VÒNG TRƯỚC — HJW MAINT-COMPAT (KQ 4de0d9f · HOST CHƯA ACCEPT)
# PROMPT — HJW MAINT · Hermes dùng được thật (2 kênh) + đèn đỏ máy chủ + Điều 30/31

RUN_ID: HJW-MAINT-COMPAT-20261002-01
Host: GPT Chat · GPT-HJW-260922-A
Executor_Surface: Claude Code CLI phiên mới trên Mac Owner.
Runtime_Write_Path: SSH/operator VPS hiện hữu; không tạo service/task/file mới.
Report_Write_Path: chỉ `work/hermes-joint-workspace/{COLLAB.md,PROMPT.md}` qua gateway; evidence dùng hồ sơ VPS HJW hiện hữu.
Owner_authorization: 02/10/2026 — kiểm lại lỗi Hermes thực tế và đưa phần mới vào bảo vệ Điều 30/31. Bổ sung 14:59: Hermes nhận việc được qua cả hai kênh; xử lý “server báo đỏ hàng loạt nhưng agent vẫn báo mọi thứ ok”.
Reviewer: Claude Chat · ACCEPT-with-delta tại P67 (bản này).

## 0. Mục tiêu — đủ 3 điều Owner giao 02/10, không thêm

1. **Hermes nhận việc được thật qua cả hai kênh.** K1 = 😊 Owner giao trực tiếp trên đúng app Owner đang dùng. K2 = 🤖 AI giao qua repo (`ASSIGN` trong HJW COLLAB → thẻ Telegram → Owner bấm Cho chạy → Hermes làm, ghi kết quả). Lỗi đang chặn K1:
`invalid params for session.create: cwd_explicit: Extra inputs are not permitted — the client and the Hermes backend are out of sync (different versions)`.
2. **Hết cảnh “máy chủ báo đỏ mà AI vẫn báo OK”** — §6B.
3. **Phần mới làm nằm trong khung Điều 30/31** — §4, §5, §6.

Không thêm capability. Không bật AUTO. Không đổi Agent Data/P02/nginx/Nuxt/model/key/scope/toolset.

PASS chỉ khi **đúng client thật → đúng backend thật** tạo được session; không chấp nhận chỉ service healthy hoặc unit test nội bộ. Lượt kiểm trước đã báo OK trong khi Owner vẫn lỗi ⇒ K1/K2 chỉ PASS khi **chính Owner làm và thấy kết quả**; executor không PASS hộ.

## 1. Hard scope / ngân sách

- Trước mutation phải snapshot: binary/path/version/package/schema + unit ExecStart + MainPID/StartedAt của Hermes client/serve/gateway; Config Guard/Protection Guard current state; rollback.
- Không chạy blind `hermes update`.
- Tái dùng `hermes-safe-update` hiện hữu. Chỉ update/restart nếu D1 chứng minh version/schema/load-process lệch.
- Tối đa restart `hermes-serve` và `hermes-gateway` khi thực sự cần; không restart service khác.
- Không tạo service/timer/DB/monitor/file repo mới. Ngoại lệ duy nhất: MỘT file trạng thái bảng đèn trên VPS (§6B.3) do script hiện hữu ghi.
- Tối đa 1 invariant mới. Không sửa Hermes core.
- Việc của 😊 Owner trong RUN, báo trước và gom gọn: gõ 1 câu trên app Hermes (K1) · bấm 1 thẻ Telegram (K2). Không nhờ Owner việc khác. Thay đổi gì trên Mac Owner (cập nhật/ghim bản app Hermes) ⇒ nói Owner 1 câu trước khi làm; không gỡ/xoá gì trên Mac.
- VPSUP G6 đang chạy song song ở cửa sổ khác: không đụng bất cứ thứ gì của VPSUP; thao tác nào va vào ⇒ DỪNG báo Host.
- Repo PUBLIC: không ghi secret, không ghi IP máy Owner (ghi “Mac Owner”).
- AUTO_ALLOWLIST cuối RUN vẫn rỗng; manual Telegram gate/STOP giữ nguyên.
- Nếu cần vượt scope trên: DỪNG trước mutation, báo Host.

## 2. D1 — chẩn đoán thật, NO MUTATION

Đo và ghi evidence, không suy từ README:
1. Client thật = bề mặt Owner dùng để giao Hermes trực tiếp; xác định từ bằng chứng trên Mac Owner, không rõ ⇒ hỏi Owner đúng 1 câu. Với client đó: executable/path, `--version`, package/source path, schema/request fields; xác nhận nơi sinh `cwd_explicit`.
2. `hermes-serve` + `hermes-gateway`: `systemctl show/cat` cho ExecStart/MainPID/StartedAt/EnvironmentFile (không in secret); cmdline/executable/package/source thực của process đang chạy.
3. Backend schema thật của `session.create`: request model/fields; xác nhận có/không `cwd_explicit`.
4. Phân loại đúng một root cause:
   - A: client package mới / backend package cũ;
   - B: package trên đĩa đã đồng bộ nhưng process backend chưa restart, đang giữ code cũ;
   - C: hai service dùng khác venv/binary/package;
   - D: lỗi khác — có evidence cụ thể.
5. Reproduce lỗi một lần bằng **đúng đường client Owner đang dùng**, rồi dừng; không lặp lỗi.
6. Chụp bảng đèn (chỉ đọc): liệt kê MỌI monitor Kuma — tên · trạng thái · thông báo cuối · đỏ từ lúc nào.

## 3. D2 — sửa tối thiểu, chỉ khi D1 đủ bằng chứng

- Nếu B: restart tối thiểu service đang giữ code cũ; không update package.
- Nếu A/C: dùng cơ chế `hermes-safe-update`/update hiện hữu để đồng bộ **cả hai đầu về cùng một bản đã xác định**, không cài song song venv/binary thứ hai; backup/rollback trước.
- Sau thay đổi: restart `hermes-serve` → verify, rồi `hermes-gateway` → verify; không dependency-bounce key services.
- Nếu safe-update/health fail: rollback về PRE, báo BLOCKED.
- Không in secret/token/env values.
- Ghi một dòng **giữ đồng bộ về sau**: khi một đầu tự cập nhật (ví dụ app trên Mac) thì đầu kia theo bằng cách nào — dùng cái hiện hữu (ghim bản/tắt tự cập nhật ở client, hoặc `hermes-safe-update` phía VPS); không dựng cơ chế mới.

## 4. Điều 30 — regression protection bắt buộc

Tái dùng test/harness hiện hữu; không tạo framework mới:
1. E2E thật: client Owner → `session.create` → backend PASS, bao gồm request có hành vi `cwd_explicit` đúng với version hiện hành.
2. Regression: gateway/manual Telegram gate, STOP, AUTO rỗng, Agent Gateway 7 tool và HJW control path vẫn PASS.
3. Negative fixture/mutant: mô phỏng client/backend schema lệch (ví dụ client có field mà backend không có) ⇒ test phải FAIL rõ ràng trước khi tuyên bố healthy.
4. Không chỉ test version string; phải test schema/handshake thật.
5. K2 thật sau khi sửa: ghi MỘT `ASSIGN` nhỏ nhất theo khuôn S9 hiện hữu (đọc 1 đoạn, ghi ≤3 dòng vào HJW COLLAB) → thẻ Telegram → 😊 Owner bấm Cho chạy → Hermes commit kết quả + tin KẾT QUẢ. Đúng 1 lượt model; ghi token/thời lượng thật. Thẻ không hiện hoặc bấm không chạy ⇒ tìm nguyên nhân, sửa trong scope; không PASS hộ.

## 5. Điều 31 — integrity/self-detection bắt buộc

Bổ sung vào **Protection Guard/Config Guard hiện hữu**, không service mới:
1. Invariant `HERMES_CLIENT_BACKEND_COMPAT` (local/no GitHub/no LLM). Lưu ý: app của Owner nằm trên Mac, guard trên VPS **không nhìn thấy** ⇒ không được xanh chỉ vì các phần phía VPS khớp nhau. Hai vế: (a) các thành phần Hermes phía VPS (serve/gateway/CLI) cùng một bản; (b) **cảm biến theo hậu quả**: backend vừa từ chối request vì lệch schema (`invalid params` / `Extra inputs are not permitted` ở `session.create` hoặc tương đương) ⇒ ĐỎ, báo qua đường Guard→Kuma→Telegram hiện hữu bằng một dòng tiếng Việt nói rõ “app của Owner và máy chủ Hermes lệch phiên bản”. Giữ đỏ tới khi có `session.create` thành công sau lần từ chối cuối; log không đủ để biết ⇒ dùng cửa sổ thời gian và ghi rõ giới hạn. Nguồn = log backend hiện hữu; backend không ghi log lỗi này ⇒ nêu rõ + cách tối thiểu, không vá Hermes core.
2. Dùng 2-pass như invariant runtime hiện hữu để tránh flap nhưng không PASS giả.
3. Kiểm các unit/config/script/package-path thực dùng bởi serve/gateway đã nằm trong Config Guard; thiếu target nào trực tiếp quyết định version/schema thì đăng ký vào registry hiện hữu trong cùng RUN.
4. Mutant/fixture: (a) lệch bản phía VPS, (b) log có dòng backend từ chối vì lệch schema ⇒ invariant đỏ; sạch ⇒ xanh.
5. Watchdog phải chứng minh invariant mới được chạy định kỳ; không tạo monitor mới nếu Protection Guard/Kuma hiện hữu đã bao phủ.

## 6. Rà toàn bộ phần mới vừa làm

Không mở task mới. Đối chiếu R6/MCPW đã đóng:
- lifecycle/receiver/workspace_tools/importer/presence/Owner View/Hermes config+gate/Protection Guard đã có protection ⇒ giữ nguyên, không làm lại;
- chỉ bổ sung thiếu hụt mới phát hiện là Hermes core client↔backend compatibility và đúng file/config/package-path liên quan.
Nếu phát hiện một thành phần mới khác **thực sự live nhưng chưa được Điều 30/31 bảo vệ**, liệt kê + đưa vào guard/test hiện hữu trong scope; không dựng cơ chế mới.
Đầu ra §6 = bảng đối chiếu ≤15 dòng trong KQ: `thành phần mới đang live → lớp bảo vệ (target Config Guard / invariant / test) → ĐỦ | THIẾU`; gồm cả `kuma-push.sh` + cron của nó, file bảng đèn, plugin/gate Hermes, hooks trên Mac (Claude Code managed settings, Codex hooks). Phần nằm trên Mac ngoài tầm Config Guard VPS ⇒ ghi đúng cơ chế đang phát hiện nó (cờ `HOOK_MISSING`) hoặc ghi THIẾU; không bịa bảo vệ.

## 6B. Đèn đỏ máy chủ

Owner 02/10: “Server báo đỏ hàng loạt nhưng agent vẫn báo mọi thứ ok.” Số đo Reviewer 08:04Z: ổ `/` dùng 46%, còn 53G ⇒ đĩa không đầy; đèn `Disk Usage` đỏ vì **heartbeat không tới Kuma**. `kuma-push.sh` và cron kuma-push khớp baseline Config Guard ⇒ tìm ở đường đẩy: cron có chạy dòng `disk` không · token · cấu hình monitor · phản hồi push.
1. Tìm đúng nguyên nhân bằng chứng cứ, sửa tối thiểu (được sửa đúng monitor `Disk Usage` nếu nguyên nhân nằm ở cấu hình monitor). PASS = đèn `Disk Usage` xanh ≥2 nhịp liên tiếp.
2. Mọi đèn đỏ khác ở D1.6: thuộc Hermes/MCPW ⇒ sửa trong scope; thuộc việc khác ⇒ KHÔNG đụng, ghi tên đèn + việc chịu trách nhiệm.
3. Bảng đèn cho AI đọc: script hiện hữu (kuma-push hoặc Protection Guard, cùng nhịp cron sẵn có) ghi MỘT file JSON dưới `/opt/incomex/` — không nằm trong thư mục web công khai, không chứa token/URL push: `generated_at` + mỗi monitor `tên · trạng thái · thông báo · từ lúc nào`. Chỉ đọc Kuma bằng đường/credential hiện hữu; không có đường đọc sạch ⇒ nêu rõ + đề xuất, không tự mở rộng. Script bị sửa ⇒ cập nhật Config Guard qua đường apply hiện hữu, ghi old/new + lý do (DROOT29).
4. KQ ghi đường dẫn file để Host/Reviewer tự đọc trước khi nghiệm thu (DROOT34).

## 7. Acceptance

PASS khi đồng thời:
- lỗi `cwd_explicit` không reproduce trên đúng client thật;
- client/serve/gateway cùng identity/version/schema phù hợp;
- real `session.create` PASS;
- `hermes-safe-update health` (nếu dùng) PASS;
- Config Guard CLEAN; Protection Guard PASS có invariant compatibility mới;
- mutant mismatch bị bắt;
- manual gate/STOP/AUTO rỗng/7-tool regression PASS;
- 0 scope creep, rollback có thật;
- **K1** 😊 Owner tự gõ 1 câu trên đúng app → Hermes trả lời (đối chiếu log backend cùng phút); **K2** 1 `ASSIGN` → thẻ → Owner bấm → Hermes commit kết quả + tin KẾT QUẢ;
- §6B: `Disk Usage` xanh ≥2 nhịp; 0 đèn đỏ thuộc Hermes/MCPW; đèn đỏ khác (nếu có) có tên + việc chịu trách nhiệm; file bảng đèn có và mới (<15′);
- bảng đối chiếu §6 không còn dòng THIẾU trong scope.

KQ — dòng đầu tiên bắt buộc: `ĐÈN <UTC>: <n> xanh · <m> đỏ [tên → việc chịu trách nhiệm]`, rồi:
`KQ@HJW-MAINT-COMPAT-20261002-01 XONG · HERMES_COMPAT_PROTECTED`
hoặc
`KQ@HJW-MAINT-COMPAT-20261002-01 BLOCKED · <root cause/evidence>`.

Owner chưa kịp thử K1/K2 ⇒ không ghi XONG: cùng tiền tố, đuôi `CHỜ OWNER THỬ · <K1|K2>`.

Sau KQ dừng; Host + Claude Reviewer nghiệm thu một lượt, mở đầu bằng tự đọc file bảng đèn. Không tự mở việc tiếp.

---

# VÒNG TRƯỚC — PROMPT HJW FINAL (ĐÃ ĐÓNG, KHÔNG CHẠY LẠI)
# PROMPT — HJW FINAL · Telegram UX + closeout evidence

RUN_ID: HJW-FINAL-20260926-05
STATUS: Chỉ thực thi sau READY/RUN mới của Host.
Host: GPT Chat · GPT-HJW-260922-A
Executor_Surface: Claude Code CLI phiên mới trên Mac Owner.
Report_Write_Path: gateway workspace_*/fs_*; chỉ file HJW hiện hữu + view.html hiện hữu.
Runtime_Write_Path: SSH/operator VPS hiện hữu; runtime VPS là SSOT.

Căn cứ bắt buộc: HJW §0.3 S1–S9; P51 KQ CONTROL-B XONG; P52 + Host response P54; P54; Điều 30/31; DROOT22.
Mục tiêu: UX polish nhỏ nhưng thật → verify → closeout evidence HJW.4/HJW.5. Không mở lại kiến trúc CONTROL-B.

## 0. Ranh giới

Được:
- sửa plugin/config/script HJW CONTROL hiện hữu đúng phần UX Telegram và input-template;
- restart tối đa hermes-gateway nếu plugin không hot-reload, theo block an toàn/rollback;
- cập nhật HJW COLLAB + view.html hiện hữu;
- append evidence trong hồ sơ VPS HJW hiện hữu.

Không:
- không gọi Hermes model;
- không tạo assignment/trial mới;
- không bật AUTO; AUTO_ALLOWLIST cuối RUN vẫn rỗng;
- không update Hermes/safe-update;
- không đổi Agent Data/P02/nginx/Nuxt/model/key/scope/toolset;
- không tạo repo file/task/project mới;
- không sửa AGENTS.md trong RUN này (Claude Code không phải Founder). Chỉ đề xuất exact foundation delta cho Host/Founders ở COLLAB.

Reuse toàn bộ evidence P34/P45/P51; không chạy lại destructive/HARD-STOP/canary nếu không có regression causal.

## 1. PRE

Đọc AGENTS → root COLLAB → HJW §0 S1–S9 + Dòng hiện hành + P51/P52/P54 → PROMPT này.
Xác nhận:
- READY exact;
- 0 assignment Hermes open/claimed, 0 pending approval card có thể wake;
- CONTROL-B manual mode, AUTO rỗng;
- plugin/hjw_gate/root monitor hashes + gateway StartedAt;
- Guard/config-guard/P02/Agent Gateway 7 tool/Kuma healthy;
- Telegram callback current API/client/wrapper capability.

Snapshot plugin/config/scripts cần sửa + rollback trước mutation. Không in token/secret.

## 2. U1 — Header/nhiệm vụ nhất quán

Mọi tin HJW do control plane gửi phải theo cùng một grammar, nhìn vài giây hiểu được:

### Approval card
Header: `HJW · GIAO VIỆC · CHỜ DUYỆT`
- `Từ: <😊 Owner | 🤖 AI/máy giao> → Tới: 🤖 Hermes (<role>)`
- `Việc: <task readable>`
- `Nhiệm vụ: <1–2 dòng hành động cụ thể>`
- `Phạm vi: <read/write scope>`
- `Mã: <ticket> · ASSIGN <id>`
- `Tiếp theo: Owner chọn Cho chạy / Không chạy`
- link Xem việc.

### START
Header: `HJW · HERMES THỰC HIỆN · ĐANG CHẠY`
- `Từ: <😊 Owner | 🤖 AI/máy giao> → Tới: 🤖 Hermes (<role>)`
- ticket/task/scope;
- Owner approved_at;
- `Tiếp theo: Hermes làm → báo KẾT QUẢ`.

### RESULT
Header: `HJW · HERMES REPORT · <XONG|BLOCKED|NO_NEW_VALUE>`
- `Từ: 🤖 Hermes → Tới: <🤖 Host | 😊 Owner>`
- Đã làm;
- Kết quả;
- commit/report;
- duration + provider usage/cost hoặc UNKNOWN;
- `Tiếp theo: <actor/action>`.

### Commit notification
Header: `HJW · HERMES COMMIT · GHI NHẬN`
- `🤖 Hermes → Repo`
- task/ticket nếu map được;
- short SHA + summary;
- trạng thái execution;
- không lặp nếu RESULT đã surfaced cùng commit nhưng ledger phải đánh dấu surfaced.

Tên surface dùng bảng A9, không tự suy hãng/model sâu hơn evidence.

## 3. U2 — Click phải có phản hồi và đổi trạng thái

Ngay khi nhận callback hợp lệ:
1. gọi `answerCallbackQuery` ngay, text ngắn:
   - Cho chạy: `Đã nhận: Cho chạy`
   - Không chạy: `Đã nhận: Không chạy`
   - Dừng tất cả: `Đã nhận: Dừng tất cả`
2. sau khi lifecycle write thành công, edit **chính message** bằng editMessageText/editMessageReplyMarkup:
   - CHỜ DUYỆT → `✅ ĐÃ DUYỆT · <time>`;
   - hoặc `⛔ ĐÃ TỪ CHỐI · <time>`;
   - STOP → `🛑 ĐÃ YÊU CẦU DỪNG · <time>`, sau root receipt update thành `🛑 ĐÃ DỪNG · <time>`.
3. Ưu tiên biến action đã xử lý thành `disabled` nếu đường Bot API hiện hữu hỗ trợ sạch; nếu wrapper/runtime hiện tại không expose `disabled` thì **không coi là blocker**: thay nút vừa bấm bằng dòng trạng thái + giờ và gỡ action đối nghịch để không còn bấm được.
4. `Xem việc` và `Dừng tất cả` còn lại theo state hợp lệ.
5. duplicate/replay callback trả ack “Đã xử lý” và không đổi lifecycle lần hai.

Restart/plugin recovery phải render lại đúng state từ ledger, không quay về CHỜ DUYỆT giả.

## 4. U3 — Màu nút

Telegram Bot API hiện hành hỗ trợ InlineKeyboardButton.style:
- `success` xanh lá;
- `primary` xanh dương;
- `danger` đỏ.
Bot API hiện hành cũng có `disabled`, nhưng wrapper runtime có thể chưa expose trực tiếp; vì vậy `disabled` là tối ưu UX, không phải điều kiện chặn.

Áp:
- `Cho chạy` = success (xanh lá), hành động được khuyến nghị.
- `Xem việc` = primary (xanh dương).
- `Dừng tất cả` = danger (đỏ), chỉ dành cho stop/nguy hiểm.
- `Không chạy` = default/trung tính, không dùng đỏ để khỏi lẫn “Dừng tất cả”.
- cảnh báo = `⚠️` + text/default. Telegram không có style vàng chuẩn: KHÔNG giả vàng bằng hack.

Nếu wrapper hiện tại chưa expose `style` nhưng Bot API endpoint hiện hành có:
- ưu tiên raw Bot API/HTTP helper ĐANG CÓ trong plugin/runtime;
- không patch Hermes core, không bot/token/client thứ hai.
Nếu không làm được **màu style** bằng extension/helper hiện hữu ⇒ ghi limitation và DỪNG trước tuyên bố U3 PASS. Riêng thiếu `disabled` ở wrapper không làm RUN DỪNG; dùng fallback thay nút bằng trạng thái + giờ như §3.

Màu chỉ phụ trợ; text/icon/state phải đủ hiểu trên client không render style.

## 5. UX acceptance — không model call

Fixture + live bot API:
U1. Header 4 loại đúng grammar và from→to/next rõ.
U2. callback ack được gọi trước khi client hết progress; handler idempotent.
U3. click Cho chạy thử trong fixture → message edit thành ĐÃ DUYỆT + giờ; action đối nghịch không còn bấm được; `disabled` dùng nếu đường hiện hữu hỗ trợ, không bắt buộc.
U4. styles được Bot API nhận: success/primary/danger.
U5. STOP state edit đúng và không có Resume qua Hermes.
U6. Không chạy/default không lẫn màu đỏ STOP.
U7. callback duplicate/restart không hồi state.
U8. normal Hermes chat/clarify/exec approval không regression.
U9. 0 model call, AUTO rỗng, 0 assignment mới.
U10. Guard/config-guard/Kuma/7-tool/P02 PASS trước-sau.

Live verification không cần Owner click: được gửi một message UX fixture/private metadata-only rồi edit bằng chính Bot API để chứng minh API/render path; không tạo ticket executable, không model. Không spam quá 1 test message; sau test edit thành `HJW · UX TEST · PASS` hoặc xoá nếu cơ chế hiện hữu hỗ trợ an toàn.

## 6. S9 — Input/context contract

Sửa template one-shot hiện hữu để mọi assignment HJW tương lai tự chứa:
- `MCP root=workspace`;
- exact task path;
- exact read targets: AGENTS + HJW §0 + các P/KQ được giao;
- exact write path;
- cấm dò/đoán root; read root đầu fail ⇒ BLOCKED;
- ưu tiên workspace_search/read window; cấm đọc full HJW COLLAB nếu không cần.

Không tự đặt hard token cap. Ghi provider token/duration thật. AUTO vẫn OFF.
P52 threshold ≤150k chỉ là đề xuất Hermes và hiện **không đạt**; không encode nó thành gate production.

## 7. HJW.4 — foundation delta đề xuất, KHÔNG tự sửa AGENTS

Dựa evidence hiện có, ghi một khối ngắn `FOUNDATION_DELTA` vào HJW COLLAB để GPT/Claude Founders nghiệm thu:
- hội đồng 3 thành viên/attribution/mapping nếu phần nào đã có thì ghi “đã có — không sửa lại”;
- L1 AUTH PLACEHOLDER LAW: placeholder auth/secret không bao giờ được thành credential runtime; source thiếu ⇒ fail closed/unavailable/random unknown + negative test;
- L2 COST SOURCE LAW: số chi phí thật lấy provider ledger/API; agent estimate chỉ informational;
- S8 Telegram operational UX: header from→to, callback ack+edit state, success/primary/danger semantics, warning fallback;
- S9 explicit root/input contract cho unattended workspace job.
- **Capability truth source:** ma trận T1–T10 cuối trong HJW COLLAB là nguồn trạng thái chung về năng lực đã chứng minh. Mọi AI/Agent phải đọc ma trận này trước khi tự đánh giá `đang có gì/còn thiếu gì`; memory/skill chỉ là tham khảo và không được lấn bằng chứng mới hơn.

Không copy lịch sử dài vào AGENTS; đề xuất patch tối thiểu vào đúng mục hiện hữu.

## 8. HJW.5 — final evidence matrix

Lập T1–T10 cuối cùng trong HJW COLLAB từ evidence P34/P45/P51/P58 và spot-check hiện trạng. **Ma trận này sau closeout là nguồn sự thật chung về capability/readiness; mọi AI phải đọc trước khi tự đánh giá.**
- mỗi T: PASS/PARTIAL/NOT_RETESTED + evidence commit/path/time; phân biệt `đã chạy thật`, `đo live lượt này`, `đọc hồ sơ cũ`, `chưa từng thử`;
- không biến “7 tool” thành suy quyền ngoài scope;
- không rerun destructive tests/HARD-STOP/nginx/canary nếu không regression causal;
- **đính chính P58:** không ghi “Internet ingress chưa từng chạy” — P34 đã có public external test 21/21 từ Mac với V2 hợp lệ đi tới ws-dispatch. Không rerun; ghi evidence cũ + trạng thái vận hành thường ngày chưa có traffic webhook gần đây nếu cần;
- **đính chính P58:** không ghi “Telegram chưa có tin thật” — CONTROL-B đã có thẻ/tin thật, Owner click thật và receipt (#42–#49 theo P51). Không yêu cầu Owner gửi mẫu mới;
- **nhịp thật:** đo read-only lịch sử runs hiện tại và ghi interval/lateness thực tế; nếu ~3 phút thì ghi ~3 phút, không ghi thiết kế 2 phút. Không sửa cadence trong RUN này nếu vẫn ≤5 phút contract;
- **cost thật:** với 4 lượt model đã có trong usage audit, ưu tiên đọc provider-authoritative cost/usage từ dữ liệu response/log hiện hữu; nếu đã có generation id và có **đường read-only hiện hữu** tới OpenRouter accounting thì được đọc mà không in/expose key. Không tạo credential/helper mới, không hỏi Owner bảng giá, không tự nhân giá thủ công. Không lấy được ⇒ ghi `UNKNOWN/PARTIAL` theo L2, không bịa số;
- T10 ghi CONTROL-B end-to-end + residual fake-approval + MANUAL/AUTO rỗng + 0-token gate evidence; P52 loại việc review-read là ứng viên, chưa auto; actual token 293k invalid trial / 490k successful trial nên hiệu quả chưa đủ để AUTO;
- các mục P58 **không làm trong FINAL**: kênh trực tiếp GPT/Claude→Hermes (MCPW signal/dispatch), mở thêm toolset cho auto-run, quyền đọc ledger DB. Chỉ ghi NEXT đúng task, không triển khai.

Nuxt V8 heap restart chỉ ghi “OUT-OF-SCOPE OBSERVATION → VPSC”, không sửa.

## 9. KQ

KQ XONG chỉ khi:
- U1–U10 PASS;
- S9 template applied/tested fixture;
- CONTROL-B không regression;
- FOUNDATION_DELTA + T1–T10 matrix ghi xong và matrix có correction/nhịp/cost theo P58;
- AUTO_ALLOWLIST vẫn rỗng;
- rollback UX delta có sẵn;
- no new model call.

Ghi:
`KQ@HJW-FINAL-20260926-05 XONG`

Nếu blocker:
`KQ@HJW-FINAL-20260926-05 DỪNG`

Không move task sang done-tasks; Host sẽ nghiệm thu foundation delta rồi đóng HJW.
