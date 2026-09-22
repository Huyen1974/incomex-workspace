Lệnh giao Codex — W005-GATE34 Revision 2: khóa authority cho Pilot đại diện, chứng minh đầu chuỗi, chuẩn bị Gate5 và ổn định SSOT/evidence

PM: GPT Chat · 11/09/2026
SSOT duy nhất: /Users/nmhuyen/Desktop/quy trình/cấu trúc hệ thống.html
Current: v1.6.17
Nguồn current: gói Gate3-4-v1.6.17-bang-chung.zip + evidence đã có trong workspace/dự án.

Đây là một gói việc lớn, duy nhất.
Không chia thành prompt nhỏ. Không báo tiến độ từng phần.

[Bổ sung Owner chuyển từ Fible 5.1] Thứ tự bắt buộc, không đảo: (1) archive evidence + sửa link → (2) freeze Pilot-critical set → (3) proof ý tưởng→Draft → (4) missing/resume → (5) 7-field readiness → (6) machine test → (7) lifecycle/publish/activate → (8) feedback→V2 → (9) khoá data Pilot → (10) SSOT write. Mỗi bước đóng gói evidence riêng trong gate3-4/evidence/<bước>/ xong mới sang bước sau. Nếu kẹt ở bước n, các bước 1..n-1 vẫn phải nộp được nguyên vẹn. Tiếp tục qua README checklist Đang làm.
Không viết UI/page mới cho Pilot; không production DDL; không per-workflow code.

Chỉ được báo PM khi:

đã khóa xong phạm vi Contract/Data cho Pilot đại diện theo tiêu chí bên dưới;

đã chạy proof đầu chuỗi “ý tưởng → draft trong PG” và missing-ingredient/resume;

đã chạy machine-test + lifecycle lab đủ để biết có sẵn sàng vào Gate5 hay chưa;

đã archive evidence accepted vào thư mục dự án và sửa các link current quan trọng;

đã cập nhật SSOT đúng một lần cuối;

đã tự QA toàn bộ;

kết luận cuối chỉ là:

READY FOR PM GATE3+4 EXIT REVIEW AND GATE5 ENTRY REVIEW, hoặc

READY ... — OWNER D04 LOCK PENDING, hoặc

BLOCKED BY <một blocker material đã có evidence>.

Không gửi báo cáo vì một test đầu tiên fail. Phải điều tra, sửa trong phạm vi, rerun trước.

1. QUYẾT ĐỊNH PM TỪ REVIEW v1.6.17

1.1. Gate3–4 chưa DONE

Giữ:

Gate3 = DOING / PARTIAL.

Gate4 = DOING / PARTIAL.

Gate5–7 = NOT STARTED.

O1–O3 = NOT VERIFIED.

Không reopen Gate0–2.

1.2. PM nhận riêng các proof kỹ thuật đã đạt

Trong phạm vi lab đã nộp, PM ACCEPT BOUNDED EVIDENCE cho:

contract shape: 112/112 ca;

P1 release-aware pin trong one-MOT internal AUTO slice;

P2 current authority revoke;

P3 transient/permanent/auth/unknown-effect retry behavior;

P4 profile/current drift;

P5 late ingredient safety;

P6 ownership boundaries;

reference/type/unit/owner/integrity cases;

lifecycle action/evidence mechanism;

current bridge Nuxt proof;

PG minor inspection/restore synthetic;

code inventory và cleanup.

Không chạy lại toàn bộ nếu source/hash liên quan không đổi.

Nếu source liên quan thay đổi, rerun đúng frozen regression set bị ảnh hưởng.

1.3. Hai blocker thực sự còn lại

DATA-AUTHORITY

Current matrix 385 leaves:

4 REUSE_EXISTING_AUTHORITATIVE;

26 REUSE_WITH_MAPPING;

44 NEW_REQUIRED đề xuất;

311 UNKNOWN_NEEDS_EVIDENCE.

Không được cố giải 311 unknown toàn hệ để đóng Gate4.

Gate3/4 exit lần này được khóa theo representative Pilot scope, xem §3.

LIFECYCLE-AUTHORITY

Action/evidence/CAS mechanism đã có proof, nhưng:

actual policy;

expiry;

revocation;

separation of duties;

authority source

chưa khóa đủ cho Pilot.

D04 còn Owner decision.

2. QUYẾT ĐỊNH PM VỀ PLATFORM — TÁCH KHỎI BLOCKER CONTRACT/DATA

Từ đây chia hai phiếu acceptance logic:

Phiếu A · Contract/Data

Đây là phần quyết Gate3/4.

Phiếu B · Platform adoption

Giữ follow-up riêng.

PM nhận platform package hiện tại ở mức:

PLATFORM REHEARSAL / DECISION PACKAGE = ACCEPT WITH FOLLOW-UP

Nghĩa là không discovery lại từ đầu trong W005 Revision 2.

Giữ current findings:

PG16.15 candidate;

Directus12.3.1 candidate;

Nuxt4.5.2 candidate;

Node pair đã rehearsal;

current Nuxt module bridge có known audit risk;

Directus12 permission suite còn license prerequisite;

production minor maintenance/restore window chưa thực hiện.

Không để Phiếu B giữ Gate3/4 semantic/data lock nếu Pilot contracts platform-neutral đã đủ.

Chỉ đụng platform khi một Contract/Data proof cụ thể thật sự cần.

3. D08 — PM CHỌN REPRESENTATIVE PILOT A

D08 = DECIDED · PM

Formal Pilot A ở Gate5 sẽ dùng family:

“Ghi nhận thời lượng xử lý”

Lý do:

đã có fixture/evidence liên tục từ Gate0–4;

đủ nhỏ để đo rõ;

có Field/MOIT/MOUT/Trigger/Condition/NTGV;

có HMITL/AUTO boundary;

có version/reuse/missing ingredient/test/release/runtime để kiểm kiến trúc;

không mang rủi ro nghiệp vụ/pháp lý của quy trình phái cử vào Pilot đầu.

Không gọi đây là production process.

Không đưa nghiệp vụ phái cử vào Gate5 đầu tiên.

4. D04 — GIỮ ĐÚNG THẨM QUYỀN OWNER

D04 vẫn WAITING OWNER.

PM recommendation A:

executor — người/service chịu trách nhiệm thực hiện Task Instance hiện tại;

delegate — người được ủy quyền làm thay trong phạm vi/thời hạn;

next_task_executor / recipient — người/service chịu trách nhiệm Task kế;

report_recipient — người nhận báo cáo/thông tin, không mặc nhiên chịu trách nhiệm task;

handoff_contact — đầu mối bàn giao/liên hệ, không mặc nhiên executor.

People / Role / Delegation là authority riêng.
NTGV chỉ resolve assignment.

Agent:

không tự ghi Owner ACCEPT;

không hỏi Owner giữa gói;

hoàn thành mọi phần không phụ thuộc D04;

nếu cuối gói D04 vẫn chưa được Owner chốt, báo:
READY FOR PM GATE3+4 EXIT REVIEW AND GATE5 ENTRY REVIEW — OWNER D04 LOCK PENDING.

Không dùng report recipient thay executor để né blocker.

5. TAXONOMY FREEZE — BẮT ĐẦU TỪ v1.6.17

Mục tiêu: SSOT phải còn đọc được bởi con người sau nhiều tuần.

Hard rule

Không tạo hệ mã top-level mới.

Dùng các hệ đã tồn tại nếu thật sự cần:

Gate;

W;

D;

G/J/L;

C;

P;

INV/CR;

existing Issue/Risk IDs.

Không thêm một alphabet/prefix/framework mới chỉ để mô tả cùng một việc.

“Kịch bản nghiệm thu số 0” ở §6 là một bảng Owner progress, không phải lifecycle, Gate hay subsystem mới.

Không tạo KB0-01, KB0-02... thành taxonomy mới.

Owner layer giữ tối đa khoảng một màn đọc chính; detail gập phía dưới.

6. THÊM “KỊCH BẢN NGHIỆM THU SỐ 0” VÀO OWNER VIEW

Đây là thanh tiến độ tới mục tiêu Owner, không thay Gate.

Bảng đúng 8 dòng:

Bước

Mục tiêu

1

Owner/User gõ một câu ý tưởng → máy tạo Intent + Draft Package trong PG

2

Máy tìm/reuse nguyên liệu và chỉ đúng phần thiếu

3

Máy lập Draft MOW/MOT/MOIT; UI đọc cùng ID/version/revision và hiện ngay

4

Thiếu nguyên liệu → tự mở request → đúng owner xử lý → máy tự resume đúng parent/slot/revision

5

Máy tự sinh/chạy/chấm test; evidence gắn đúng revision/release

6

Đúng authority duyệt → Publish → Activate exact release/binding

7

Trigger → HMITL đúng người/context → submit → AUTO → result/handoff/end

8

Feedback → Draft version mới → test/run → đo trước/sau

Trạng thái chỉ:

🟢 PROVEN trong phạm vi;

🟡 PARTIAL;

⚪ NOT YET PROVEN;

🔴 BLOCKED với blocker cụ thể.

Không dùng màu Gate thay cho bảng này.

Mỗi dòng phải có:

evidence current;

Gate tiếp tục chứng minh;

exact limitation.

Không bịa completion %.

[Bổ sung §7] Đầu vào: một bản ghi intent (một câu) ghi PG qua cổng ghi; T0 nhận từ PG. Chạy ít nhất hai phiên hoàn toàn mới; Draft tương đương về nghĩa, cùng tập reuse và request thiếu. Lưu prompt nguyên văn, transcript tool đầy đủ, runbook ứng viên T0 (các bước xác định được). Draft hiện trên UI hiện có P01/P02 qua generic renderer, 0 dòng code UI mới.

7. PROOF ĐẦU CHUỖI — “Ý TƯỞNG → DRAFT TRONG PG”

Đây là thiếu hụt lớn nhất hiện tại.

Input duy nhất cho fresh Agent

Cho một Agent/session mới đúng câu intent:

“Tạo quy trình ghi nhận thời lượng xử lý. Người thực hiện nhập số phút và ghi chú; hệ thống lưu thời điểm. Khi thời lượng vượt 60 phút thì đánh dấu cần xem xét. Hãy dùng lại tối đa những gì hệ thống đã có.”

Fresh Agent không được nhận:

transcript thiết kế;

danh sách ID cần dùng;

thứ tự tool thủ công;

JSON declaration mẫu hoàn chỉnh.

Được nhận:

current SSOT/profile/tool contract;

authenticated lab scope;

canonical resolver/gateway;

work/checkpoint entry.

Expected

Agent phải tự:

tạo Intent/Search Brief;

tìm/reuse approved materials;

phân biệt existing vs missing;

tạo Draft Package qua governed write path;

ghi PG/read-back;

tạo structured missing-ingredient request nếu Condition duration > 60 chưa có approved compatible Definition;

lưu parent/slot/revision/checkpoint;

dừng đúng WAIT nếu cần owner/resource;

sau khi TEST owner path publish/approve missing resource, fresh Agent/session resume;

gắn đúng result vào đúng slot/revision;

rerun readiness.

Nếu Condition compatible đã tồn tại thật:

phải reuse;

không được cố tạo missing request để làm đẹp demo.

PASS

không duplicate Field/MOIT/etc.;

không hard-code IDs trong prompt;

không human chọn tool tiếp theo;

Draft/read-back đúng;

missing/resume đúng revision;

source/provenance rõ;

fresh session resume được;

business truth không nằm trong chat.

Đo:

reusable requirements requested;

reused;

new version/variant/new;

unresolved;

human semantic decisions;

tool calls;

elapsed active Agent time nếu đo được;

số cấu hình người phải nhập.

Không đặt 98% PASS từ một sample.

8. “7 TRƯỜNG MỖI BƯỚC” → READINESS RULE, KHÔNG BIẾN THÀNH 7 CỘT SAI OWNERSHIP

Owner đã dùng mẫu:

Bước

Nhiệm vụ

Trigger

Ai làm

Yêu cầu sản phẩm hoàn thành

Ghi/lưu ở đâu

Lưu ý

Biến thành Step Readiness View/Contract được compile từ đúng owner:

1 · Bước

Nguồn: MOW step identity/order/topology.

2 · Nhiệm vụ

Nguồn: MOT Definition/Version meaning/ref.

3 · Trigger

Nguồn: điều kiện kích hoạt bước. Bước đầu → Trigger Definition binding; bước sau → output bước trước + Condition/join (loại B trong SSOT).

4 · Ai làm

Nguồn:

HMITL: MOT execution requirement + NTGV + People/Role/Delegation;

AUTO: MOT → exact Capability Version.

D04 áp dụng cho semantic role human.

5 · Yêu cầu sản phẩm hoàn thành

Nguồn: MOT output/result/completion contract.

6 · Ghi/lưu ở đâu

Nguồn:

MOIT submit target;

output/effect target/storage contract;

không lấy raw table name làm business meaning.

7 · Lưu ý

Nguồn: Guidance/approved note/context.

Readiness rule

Mỗi step phải có đủ 7 mục hoặc explicit N/A + reason hợp lệ.

Material UNKNOWN / unresolved / thiếu owner:

readiness FAIL/WAIT;

không activate.

Không bắt nhập tay 7 trường nếu máy resolve được từ refs/context.

Human UI hiển thị 7 dòng dễ đọc; PG vẫn giữ owner-specific canonical facts, không tạo bảng copy 7 cột làm truth thứ hai.

Thêm rule này vào C05 / readiness contract hiện có, không tạo contract family mới.

9. GATE4 CONVERGENCE — CHỈ KHÓA PILOT-CRITICAL DATA, KHÔNG GIẢI 385 LÁ TOÀN THẾ GIỚI

9.1. Freeze PILOT_CRITICAL SET

Từ contracts C01–C10 và representative Pilot ở §3:

Agent phải xác định chính xác các semantic facts cần cho:

idea→draft;

reuse;

7-field step readiness;

missing request/resume;

test;

approval/publish/activate;

one HMITL + one AUTO handoff path;

feedback/version link.

Đóng freeze trước khi map.

9.2. Exit denominator

Gate4 scoped exit xét PILOT_CRITICAL SET, không xét tất cả 385 leaves.

PASS khi trong Pilot-critical:

UNKNOWN_NEEDS_EVIDENCE = 0;

mọi NEW_REQUIRED có per-fact I0–I5 elimination evidence;

mọi source có authority/owner;

every read/write path known;

type/unit/version/revision known;

material relation có hard integrity hoặc accepted equivalent;

where-used/provenance đủ cho impact;

no competing writable truth.

Ngoài Pilot-critical:

giữ DEFERRED / OUTSIDE PILOT;

không tô PASS toàn hệ;

không chặn Gate4 scoped exit.

9.3. Semantic source lock

Đặc biệt phải khóa actual source cho:

MOW Definition/Version;

MOT Definition/Version;

MOIT Definition/Version;

MOUT Definition/Version;

Field semantic Definition/Version;

Trigger;

Condition;

NTGV;

Guidance;

Capability;

Release;

Binding;

Instance/Task Instance/Attempt.

Không chọn workflows, workflow_steps, unit_version, binding_registry, candidate concept... chỉ vì tên gần đúng.

Mỗi reuse cần evidence domain equivalence.

Nếu no existing source fit:

NEW_REQUIRED được PM review candidate;

chưa production DDL trong lượt này;

đề xuất minimal canonical model + why I0–I5 not fit.

10. LIFECYCLE-AUTHORITY CONVERGENCE

Không dựng approval engine mới.

Khóa semantics/action contract trên current sources + lab policy.

Required actions

TEST;

REVIEW;

APPROVE;

PUBLISH;

ACTIVATE;

RETURN/REJECT;

RETIRE/DEACTIVATE khi liên quan.

Required facts

actor/service;

authority source;

scope;

object/release digest;

action;

decision/evidence;

expires_at nếu policy có hạn;

revoked/invalid;

SoD outcome;

request/correlation;

audit/read-back.

Pilot policy proof

Không cần tên người thật.

Dùng synthetic non-admin test identities/roles để chứng minh mechanism:

author;

approver;

publisher/activator theo policy tối thiểu.

Hard behavior:

material revision/closure đổi → test/approval cũ stale;

revoked permission/grant → action mới bị deny;

expired evidence/approval → không publish/activate;

actor spoof không cấp quyền;

policy yêu cầu SoD → author không tự approve;

publish không tự activate;

active binding chỉ trỏ exact release;

retry/replay action không double transition.

Không tự quyết production job title.

D05 semantics đã PM DECIDED; nếu actual source không hỗ trợ enforcement, ghi exact gap.

11. MACHINE-FIRST TEST CHO REPRESENTATIVE PILOT

Sau idea→Draft và readiness:

Máy phải tự sinh/chạy/chấm test từ:

contract invariant;

approved validator;

approved fixture;

negative/adversarial cases.

Không lấy output implementation làm expected duy nhất.

Tối thiểu kiểm:

duration valid;

wrong datatype;

wrong unit;

note optional;

system date cannot spoof;

threshold condition boundary 59/60/61 theo semantics đã chốt;

missing executor/capability;

stale revision;

forbidden scope;

output incomplete;

duplicate submit;

material change invalidates evidence.

PASS:

test auto-triggered sau material Draft change hoặc compile;

evidence pin đúng Draft/release closure;

sửa material làm evidence cũ stale;

người review result, không bấm từng test.

Đây là pre-pilot contract validation, không tự gọi Formal Gate5 PASS.

12. LAB PUBLISH / ACTIVATE PRE-PILOT PROOF

Nếu D04 chưa Owner quyết:

có thể proof AUTO-only hoặc synthetic human role mechanism;

không giả real assignment semantic.

Chứng minh bounded:

Draft
→ readiness pass
→ machine test pass
→ approval per test policy
→ publish exact immutable release
→ activate exact binding
→ event mới resolve exact release.

Negative:

stale evidence;

expired/revoked authority;

closure changed;

duplicate activation;

wrong scope;

old instance remains old release.

Không production activation.

13. FEEDBACK → V2 PRE-PILOT TRACE

Để không bỏ đầu O3 quá lâu:

Trên same Pilot fixture:

sau một completed test run, tạo feedback một dòng có context;

người có quyền mở Draft V2 theo D06;

giữ backlink source version/run/feedback;

thay một nontrivial item nhỏ;

rerun readiness/test;

chưa cần claim business improvement nếu chưa có real before/after.

Expected:

provenance chain rõ;

V1 immutable;

V2 không inherit stale evidence;

report NOT MEASURABLE YET nếu chưa có runtime metric thật.

Không gọi O3 VERIFIED.

14. EVIDENCE REPOSITORY — KHÔNG ĐỂ BẰNG CHỨNG SỐNG TRONG THƯ MỤC PHIÊN CODEX

Current v1.6.17 vẫn còn nhiều link tới:

/Users/nmhuyen/Documents/Codex/...

Đây là rủi ro mất traceability.

Tạo đúng một kho evidence trong dự án

/Users/nmhuyen/Desktop/quy trình/KHO/11-evidence/

Đây là evidence repository, không architecture SSOT thứ hai.

Cấu trúc tối thiểu

Theo accepted package, ví dụ:

gate0/

gate1/

gate2/

gate3-4/

Mỗi package giữ:

original accepted ZIP nếu có;

README/owner report;

manifest/hash;

PM acceptance receipt nếu có.

Có một INDEX.md rất ngắn:

Gate/work;

accepted date/scope;

archive file;

SHA256;

source old path;

status.

Không copy hàng nghìn file lẻ nếu ZIP accepted đã giữ đầy đủ và hash.

Link migration

[Bổ sung] ZIP + hash là bản niêm phong; link current trỏ thư mục giải nén cùng tên trong KHO/11-evidence, không trỏ file bên trong ZIP.

Sau archive:

mọi current acceptance/evidence link trong SSOT phải trỏ relative/stable vào project repository;

current assertion không được phụ thuộc duy nhất vào Documents/Codex session folder;

historical deep links có thể giữ khi cần provenance, nhưng phải có archived package mapping và không là bằng chứng duy nhất.

Báo:

external Codex links before;

after;

current-section external links after phải = 0;

historical-only unresolved links có count + archive mapping.

Không xóa source Codex workspace.

15. SSOT SIMPLIFICATION / HUMAN READABILITY

Không viết lại toàn file.

15.1. Owner layer

Thêm:

Kịch bản nghiệm thu số 0 8 dòng;

current Gate;

tối đa 3 Owner decisions/blockers.

Không thêm detail.

15.2. Current vs history

Những roadmap/câu “việc tiếp theo” đã bị supersede:

phải gắn HISTORICAL hoặc nằm trong fold history;

không cạnh tranh Next Action hiện tại.

15.3. Không tăng taxonomy

Static QA phải báo:

top-level code prefix set before/after;

không có prefix family mới nếu không được PM explicitly cho phép.

New instance ID trong existing family được phép khi cần trace.

15.4. Size discipline

Không đặt hard byte target khiến mất evidence.

Nhưng khi thêm current content:

compress/supersede câu current cũ;

tránh append correction lặp;

detail raw ở evidence repository;

SSOT giữ conclusion/decision/gap/link.

Báo:

bytes before/after;

line count;

ID count;

reason nếu tăng đáng kể.

16. INDEPENDENT SUPERVISOR HANDOFF

Codex tự-review vẫn là self-review.

Không ghi “independent PASS”.

Trong evidence ZIP cuối tạo một file ngắn:

SUPERVISOR-REVIEW-INPUT.md

Chỉ chứa:

PM acceptance criteria;

10 raw evidence files quan trọng nhất;

hash/manifest;

known limitations;

5 câu PASS/FAIL mà independent supervisor cần trả lời:

head-of-chain proof thật hay scripted;

Pilot-critical data authority đã 0 unknown chưa;

lifecycle authority enforcement có thật không;

evidence archive/SSOT links bền chưa;

có claim nào vượt evidence không.

Không yêu cầu supervisor thiết kế hoặc giao việc.

[Bổ sung] Phải có prompt nguyên văn cho fresh Agent, transcript tool-call đầy đủ, snapshot PG trước/sau và một lệnh chạy lại proof đầu chuỗi trên lab; supervisor kiểm bằng chạy lại, không chỉ đọc log.

17. PLATFORM — KHÔNG MỞ LẠI TRỪ KHI CONTRACT/DATA CẦN

Không tiếp tục:

chase version;

audit module thêm;

license research thêm;

PG migration research thêm

trừ khi một Pilot-critical proof cần.

Giữ license state:

revenue fact Owner đã cung cấp;

headcount/entity scope/key chưa có;

không bypass/apply/accept terms.

Không để platform follow-up cản Contract/Data exit.

18. GATE3/4 EXIT CRITERIA MỚI — SCOPED, RÕ MẪU SỐ

Chỉ đề nghị:

READY FOR PM GATE3+4 EXIT REVIEW

khi:

Gate3 scoped

C01–C10 semantics đủ cho Pilot;

7-field readiness compile được;

head-of-chain idea→Draft proof đạt;

missing/resume proof đạt;

machine-test evidence semantics rõ;

release/publish/activate semantics rõ;

retry/error/current-authority proof giữ pass;

lifecycle authority mechanism/policy đủ Pilot;

D04 Owner accepted, nếu HMITL assignment semantics là material exit criterion.

Nếu D04 chưa accepted:
READY ... — OWNER D04 LOCK PENDING.

Gate4 scoped

Trong frozen Pilot-critical set:

UNKNOWN = 0;

unqualified NEW_REQUIRED = 0;

source authority = 100%;

material relation authority/integrity known = 100%;

read/write/version/provenance known = 100%;

no competing writable truth.

Global non-pilot unknown được defer rõ. Đóng Gate3/4 theo Pilot sẽ mở lại lazy cho mỗi family sau; không đồng nghĩa toàn hệ đã khóa.

Gate5 Entry

D08 Pilot selected;

fixture/source/package stable;

formal Pilot plan có measurable O1 criteria;

production mutation vẫn = 0 cho tới PM giao Gate5.

Không tự mở/chạy Formal Pilot Gate5.

19. FORMAL PILOT A ENTRY PACKAGE — CHUẨN BỊ, CHƯA CHẠY

Soạn plan ngắn dùng Pilot “Ghi nhận thời lượng xử lý”:

O1 measurement

Đo:

user intent → Draft elapsed;

human active time;

human semantic decisions;

manual configuration values;

reuse count;

new Definitions/Versions;

machine-generated tests;

failed/resumed steps;

Agent/tool calls;

Draft→Published time;

cheap-change CR1–CR8 cho một V2.

Không đặt target 98% giả.

Required Formal Pilot A scenario

idea;

reuse;

missing resource;

resume;

review;

test;

approve;

publish;

activate;

edit V2;

impact;

rollback/retire behavior theo scope.

Gate5 chỉ chạy sau PM acceptance Gate3/4 + D04 nếu dependency cần.

20. SSOT WRITE — MỘT LẦN Ở CUỐI

Backup v1.6.17.

Dự kiến v1.6.18.

Trước write:

staged copy;

current-status sweep;

taxonomy-prefix QA;

internal ID/anchor QA;

external evidence-link QA;

Owner-layer browser QA.

Sau đó one final write.

Phải cập nhật

Gate3/4 status;

bounded accepted P1–P6 evidence;

DATA/LIFECYCLE blocker resolution;

D08 DECIDED PM;

D04 exact state;

7-field readiness;

Kịch bản nghiệm thu số 0;

Pilot-critical denominator/results;

evidence repository rule/links;

Gate5 entry readiness;

current next action;

Decision Log;

Work Queue;

Risk/Issue;

History;

footer.

Không tự:

Gate3/4 DONE;

Gate5 DOING;

O1/O2/O3 VERIFIED.

Agent chỉ SUBMITTED / READY FOR PM REVIEW.

21. SELF-QA TRƯỚC KHI BÁO

A · Scope

Không reopen Gate0–2.

Platform không chiếm lại mission.

Pilot-critical set frozen.

B · Head of chain

Fresh Agent chỉ nhận intent + governed tools/current context.

No hand-fed object IDs/finished declaration.

Intent→Draft PG/readback PASS.

Missing request/resume PASS hoặc legitimate reuse result.

C · Seven-field readiness

7/7 hoặc N/A+reason.

Mỗi value lấy đúng owner.

Không tạo copy truth.

D · Contract/lifecycle

test/review/approve/publish/activate distinct.

stale/revoke/expiry/SoD tests.

release exact closure.

retry taxonomy unchanged/regressed PASS.

E · Data

Pilot UNKNOWN = 0.

Pilot unqualified NEW_REQUIRED = 0.

all critical relations classified.

data authority source 100%.

no name-based fake mapping.

F · Machine test

generated/run/scored automatically.

expected has independent provenance.

material change stales old evidence.

G · Feedback trace

V1→feedback→V2 trace.

no false improvement claim.

H · Evidence durability

KHO/11-evidence exists.

accepted ZIPs hashed/indexed.

current SSOT external Codex evidence links = 0.

historical unresolved links mapped.

I · Taxonomy/readability

no new top-level prefix family.

Owner view still concise.

superseded current prose not duplicated.

J · Safety

no production DML/DDL/deploy/restart/license activation.

lab cleanup.

demo unchanged with limitation stated.

secrets absent.

K · SSOT

backup exact v1.6.17.

one write.

no duplicate IDs.

no broken internal anchors.

snapshot == current bytes.

Chỉ sau checklist này mới báo.

22. BÁO CÁO OWNER — TỐI ĐA 12 Ý

Head-of-chain intent→Draft PASS/FAIL.

Missing ingredient/resume PASS/FAIL.

7-field readiness PASS/FAIL.

Machine-first test PASS/FAIL.

Pilot-critical data denominator + UNKNOWN/New counts.

Lifecycle authority proof.

Release/retry regression status.

Feedback→V2 trace.

D04/D08 states.

Evidence archive/link migration result.

SSOT v1.6.18 + taxonomy/size QA.

Final:

READY GATE3+4 EXIT + GATE5 ENTRY REVIEW;

READY pending D04;

material blocker.

Không báo 178/500 file cho Owner trừ khi hash failure ảnh hưởng kết luận.

KẾT LUẬN ĐIỀU HÀNH

W005 Revision 1 đã làm rất tốt phần “đừng chạy sai”.

Revision 2 phải chứng minh thêm phần Owner thực sự cần:

“Tôi nói một ý tưởng → AI dựng được một quy trình chuẩn chỉ → tự dùng lại / biết thiếu / tự quay lại → tự kiểm → đúng quyền mới ban hành → dữ liệu và phiên bản không nói dối.”

Đồng thời dọn hai rủi ro quản trị:

SSOT không được tiếp tục phình thành tài liệu chỉ AI đọc được;

evidence không được sống trong thư mục tạm của một phiên Codex.

Không chạy Formal Pilot trước khi Gate3/4 được PM nhận.