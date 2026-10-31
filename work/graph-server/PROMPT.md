# PROMPT — GS-COV2-SYNC-PROOF-BRIDGE-20261031-03
RUN_ID: GS-COV2-SYNC-PROOF-BRIDGE-20261031-03
TASK: work/graph-server · Host GPT B13
STATUS: CANDIDATE_ONLY; READY sẽ do GPT Host ký sau commit PROMPT này, Owner chuyển tay Claude Code CLI Mac. KHÔNG phải SYNC-LIVE.
EXECUTOR_SURFACE: Claude Code CLI Mac · một CLI, checkpoint <=15 phút, no WAIT.
WRITE_PATH: gateway workspace_* Git-CAS đúng repo Huyen1974/incomex-workspace. Chỉ được SỬA tệp đã có trong tools/onepass/, tools/c1d/, task COLLAB/view/root/PROMPT. Mac fixture private, VPS Graph/PG/Directus/Neo4j chỉ đọc qua connector đã cho phép. Không SSH nếu auto-mode chặn; không Git→VPS.
REVIEW_REUSED: Claude Chat P-ONEPASS-CLAUDE-B11 @e07c74628f0feb26710ea7cf75d39cfa7a5f4994, Claude Code KQ RUN02 @0dfa8fbfe7847ddd90c978cf1cd522c580d62852 chỉ là evidence, không là review độc lập. A5/DROOT57: cùng phạm vi CORE candidate N4/fail-closed; không đụng luật production.
READ: AGENTS A0/A1/A4/A5/A6/A8/DROOT30/31/44/56/57/58/60, root + task COLLAB §0/§3/KQ RUN02/P-ONEPASS-HOST-B13/GS-RM1; K0 archive + README, graph_autocover.py, c1d_fixtures.py, graph-refresh.c1dfix.diff, graph_cert/c1d2 code bản chép và runtime manifest. K4 NOT_READY, PR683 Draft.

## MỤC TIÊU DUY NHẤT: LOẠI FALSE-GREEN TRƯỚC KHI NỐI VÀO NEO4J THẬT
Host nghiệm thu RUN02 = FIXTURE_PASS 21/21 nhưng Graph production vẫn 8.968 nút/20.984 cạnh (snapshot 31/10 02:37Z), NOT_ACTION_SAFE. Không chạy lại CORE chỉ để thêm số PASS. KQ phát hiện: K0 so 'RETIRED' nhưng Graph ghi 'retired', không lọc retired cạnh; 312 cạnh thiếu nút (194 permissions, 21 system view, 95 nhầm loại view, 2 khác), các họ liên quan không được giấy FULL giả. Chưa pin SHA live graph-refresh/autocover, 6 ONEPASS fixture GAP, 2 legacy fixture suites NOT_RUN; R7 chưa áp, nhịp tự làm mới đứng từ 25/10. VPS measured MemAvailable≈2.46 GiB, swap Free≈264 KiB => KHÔNG chạy Neo4j tạm/rebuild hoặc Cognee/Enola khi nguồn lực như vậy.

## S0 — PIN ĐỦ ĐẦU VÀO TRONG PHẠM VI, ĐỪNG DỪNG VÌ SSH BỊ CHẶN
Kiểm READY@last-touch, STOP/STARTED, Git-CAS/HEAD. Mac Python và K0 repo archive/fixtures đã có KQ, không cần cài máy. VPS production chỉ đọc bằng connector allowlisted nếu khả dụng; nếu nguồn bị chặn trả SOURCE_SHA_UNVERIFIED/READ_PARTIAL, không lặp SSH từ Bash hoặc đòi nâng quyền. VPS-GHI/Guard production N/A vì 0 protected runtime writes. Tách source on VPS vs code repo bằng SHA thật, chưa so được không tự giả PASS. Pin current RAM/swap sample và không khởi động runtime tạm nếu thiếu tài nguyên.

## S1 — 2 LỖ HỔNG CƠ CHẾ, SỬA HẸP TỆP HIỆN CÓ
A. K0 `tools/onepass/k0_tools.shar.sh`: dùng `gs_status=="retired"` OR `retired_at` cho NODE và RELATIONSHIP active filtering; `k0_graph_export.py` phải export trạng thái cạnh từ Neo4j (chỉ MATCH/RETURN). Đảm bảo K0 đọc cả ID/loại/chiều và trạng thái active; node cũ sống, HUMAN/PROPOSED không bị lọc thành đã xóa. Cập nhật checksum nội bộ archive + README, giữ nguyên bản lịch sử bằng Git commit cũ, xác minh giải nén tự check, không lộ secrets. Không thêm tệp thứ 3 hoặc chương trình mới.
B. `tools/c1d/graph_autocover.py`: `oracle_diff` hiện tách `source_dangling_edges` nhưng `source_cert` chưa buộc hạ nhãn SOURCE×TYPE cho các cạnh dangling. Một đầu nút thiếu, loại chưa có adapter, permission nhắc collection chưa đăng ký, hoặc đọc thiếu => GAP/PARTIAL đúng họ/loại (và NOT_ACTION_SAFE), không tự bỏ cạnh khỏi phép đếm để cấp FULL. Không 'bịa' nút chỉ để đủ số. Không nạp user PII/secret vào Graph. Các ca 312 phải được phân nguồn/kind và có lý do. Tránh sửa hardcode tên 312 vật.

## S2 — REGRESSION NHỎ, CHỨNG MINH KHÔNG PHẢI TỰ CHẤM
Sửa/đăng ký phép thử ngay trong `tools/c1d/c1d_fixtures.py` và/hoặc test hiện hữu: (1) node retired; (2) edge retired; (3) reader trả một cạnh có đầu thiếu; (4) active edge đổi A→C; (5) source FAIL/timeout không retire; (6) 312 gap phải hạ nhãn từng nguồn liên quan; (7) nguồn khác được giữ theo chứng cứ của nó. Chứng minh các ca lỗi đã FAIL với candidate cũ và PASS sau sửa, K0 chạy process độc lập, không reuse oracle của loader. Chạy lại 3×7 CORE regression và ít nhất phần legacy fixtures có thể chạy trên Mac. Legacy `c1d_fixtures`/ `c1d2_fixtures` phụ thuộc /opt và VPS thì chỉ ghi NOT_RUN lý do, không gọi PASS; không tự tạo server/daemon hay vòng thủ tục. Không cần Neo4j engine để hoàn thành candidate, nhưng kết quả chỉ PROOF_BRIDGE_FIXTURE_PASS; không tuyên Neo4j/live.
Cẩn thận: K0 bundle là thư khố 11 tệp, được phép sửa tệp hiện hữu, không tạo 11 file Git mới. Ghi rõ nguồn bytes cũ vs mới và thử giải nén.

## S3 — CHUẨN BỊ CỬA LIVE BẰNG CHỨNG CỨ, KHÔNG ÁP DỤNG
Đối chiếu source caller của graph-refresh/graph_cert/graph-v1 từ file đã có; nếu live SHA không truy xuất được qua tool cho phép, báo BLOCKED_LIVE_PROVENANCE và chỉ thiết kế call site, không nối bằng giả định. Kiểm vì sao global gate SKIP từ 25/10 từ journal/Guard nếu connector cho phép; nếu không, ghi UNKNOWN; không lách. R7 vẫn chưa được Owner duyệt, không bỏ Guard/D23/VPS-GHI. Chốt điều kiện Neo4j temp rehearsal an toàn dựa trên RAM/restore + lối truy nhập có quyền; nếu MemAvailable <3GiB hoặc swap gây áp lực => tài nguyên gate FAIL, KHÔNG dựng.
Chỉ sau PROOF_BRIDGE candidate đúng + live SHA/Resource/Guard/rollback được xác minh, Host mới có cơ sở xin SYNC-LIVE. Không tạo task mới.

## KQ / GATE
Một KQ XONG|DỪNG duy nhất, mức PROOF_BRIDGE_FIXTURE_PASS khi: (i) K0 node+edge retired đúng, (ii) false green 312/gaps đã bị bắt và hạ nguồn, (iii) independent tests negative + 3×7 regression PASS, (iv) 0 secret/0 production write, (v) số LOC net và compiler/test run, (vi) live/legacy gaps được nêu rõ; nếu không đạt thì DỪNG có NEXT_TRIGGER. Không báo N1–N4 FULL hoặc SYNC-LIVE READY. Board/GS-RM1/view/root một Git-CAS commit, không mở file mới; checkpoint <=15 phút và đóng sạch.
CẤM: PG/Directus/Neo4j/Qdrant/KB production writes, upload raw PII/secrets, mới cron/service/DB/Cartography, thay Guard/D23, cài Mac/VPS, git→VPS, merge PR683, sửa K4, tăng worker, xoá node/cạnh production; không đòi Owner trả lời câu kỹ thuật.
STEP_WALK: Owner dispatch sau READY → S0 pin repo/source quyền cho phép → S1 hai sửa hẹp → S2 hồi quy độc lập → S3 GATE LIVE thiết kế không áp → KQ.
