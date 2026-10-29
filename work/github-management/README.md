# github-management — cửa vào công việc

**P110 Claude: đồng ý C2-B đóng; SSOT-CUTOVER §0.4d sửa gọn (S0 git status + ancestry, tiêu chí W1–W4, luật L1/L2 vào AGENTS gốc). Chờ Host chốt PROMPT S0.**

**P109 Host ACCEPT C2-B:** hai main private đã có ruleset active strict gate, PR/CI thử dương-âm đạt. KST-only theo luật (một GH actor). Bước kế là thiết kế SSOT-CUTOVER ở [ROADMAP §0.4d](ROADMAP.md), chỉ S0 đọc đối chiếu toàn mã/live image, cần Claude Reviewer P110 rồi GPT Host READY. CHƯA RUN, không làm lại C2, không đụng PR #353/production.

**P108 KQ XONG C2-B (Claude Code CLI, 29/10 01:12Z):** main AD/Web khoá bằng ruleset `main-code-gate` (PR + strict `gate`, bypass rỗng), Web legacy4 gỡ, thử âm RED/lạc hậu/push thẳng đều bị chặn, PR-1/PR-2 merged qua gate. Chờ GPT Host nghiệm thu (COLLAB P108) → SSOT-CUTOVER.**

**P107 READY C2-B:** GPT Host ký READY@`5fdee2217271d6c263f980fed14863fdcfde7e42` (PROMPT last-touch mới, P92 cũ không dùng). Owner chuyển Claude Code CLI PHASE=B RUN_ID `GHM-C2-PRIVATE-MAIN-PROTECT-20261028-07`. B0a thêm làn Claude đúng repo rồi B1–B4 hardlock; chưa RUN. Một GH Pro, không account/App mới, không merge PR #353/deploy.**

**P106 Host chốt P105:** một GH Pro, KHÔNG account thứ hai/GitHub App; hai lớp là required gate+PR (máy) và KST-only merge/release (luật). Đã soạn gia cố B0a trong PROMPT C2 cho nhánh `dev/claude-code-<repo>/` đúng repo, trước khi B1 Web legacy/B2 rulesets; chữ ký READY P92 cũ cần thay bằng P107@new last-touch PROMPT. C2-B CHƯA RUN; không làm lại A.**

**Trạng thái P104 (Claude): điểm danh 4 mục tiêu Owner ở ROADMAP §0.4c. Việc ngay: C2-B khoá main (Web đang bị bảo vệ cũ chặn merge) → SSOT-CUTOVER → AD release → F2.**

**P103: Codex XONG S0–S2 cost sau Pro bằng readback UI + API; khóa hiện có đủ phạm vi, không đổi Billing/CI. Actions Account $0 + Stop/alerts ON; net metered hiện tại 0; All AI Credit SKUs có hard-stop, Models paid usage chưa bật. Bằng chứng riêng và giới hạn tại COLLAB P103. GPT Host nghiệm thu trước Owner giao C2-B riêng; chưa RUN C2-B.**

**P100: GH Pro đã active (rulesets [] ở hai repo private), Web protected:true legacy, AD protected:false. C2-A 4 GREEN/2 RED, 6 PR OPEN. Owner yêu cầu khóa phí trước: Codex kiểm lại Actions Account budget $0 + Stop và workflow hosted theo COST-LOCK-POSTPRO-20261028.md; sau PASS mới giao Claude Code CLI C2-B theo PROMPT P92 (READY không đổi).**

**Trước đó: P97 Host độc lập ACCEPT C2-A P96 PASS_TRUSTED_PILOT: AD #354/#355, Web #679/#680 CODE gate SUCCESS đúng HEAD; AD #356/Web #681 FAILURE OUT_OF_PILOT trước fetch/checkout đúng phép thử. Sáu PR OPEN, main AD a636ffe5/Web4f8405a9 không đổi, 0 merge/deploy. C2-B KST chưa RUN: cả hai main protected:false, API rulesets 403 Upgrade Pro, Owner chưa cấp GO/Pro; Web có legacy 4 status. P98 Claude kiểm chứng một vòng; giữ PROMPT/READY P92@664f06e0d2c8d7839d35241f0d93a0995cda70f0 và RUN_ID GHM-C2-PRIVATE-MAIN-PROTECT-20261028-07. F2/C4 chưa mở; Health dữ liệu và AD rollback riêng.**

**Trước đó: P90 Host: G1 PASS trên GitHub thực (PR351 AD/main a636ffe5 gate40623332810 SUCCESS; PR677 Web/main4f8405a9 gate40623377993 SUCCESS), không postmerge false-red. GH_HARDLOCK_ENFORCED=NO vì main private protected:false; C2 Pro/required `gate`/Chief identity tiếp theo. Web Health sau merge run40629876815 có 11 PASS/2 business FAIL, CHECK12 trở lại PASS; Web ops-smoke/AD Lifecycle GREEN. DRAFT GHM-C2-PRIVATE-MAIN-PROTECT-20261028-07 cho Claude P91, chưa READY/RUN, không tự mua Pro. F2/C4 chưa mở, AD rollout nợ riêng.**

**Trước đó: Phần A G1 đã XONG (P87): PR Agent Data #351/Web #677 gate GREEN thật; hai PR âm đóng sau đúng hai run RED/repo, closed skipped. Phần B chưa RUN — Owner chuyển riêng Claude Code CLI theo P85, cùng RUN_ID GHM-GH-GREEN-GATE-20261027-06; KST kiểm độc lập CI diff rồi merge và kiểm push-main. Không tuyên G1 toàn bộ/C1B/Health đã xanh.**

**Trước đó: GPT Host P83 kiểm thẳng GitHub Actions: F1 accepted scoped Web production MAIN@e9f5801f và KST merge PR350/676, nhưng GH CODE GATE NOT ACCEPTED; G1 trước C2/F2.**

**Trước đó: GPT Host P80 ACCEPT Claude P79 và ký READY@77c23c7911d5b87c1b2494080e1f06d7e7cff5b1 cho Claude Code CLI KST RUN GHM-F1-KST-REVIEW-MERGE-WEB-20261027-05; Owner chưa RUN. F0 P77 PASS hai PR thật AD350 gateGREEN33, Web676 unit16 PASS/policyRED KST; F1 review/merge/audit main, sau đó Web production dùng bản build GitHub main và GIỮ nếu 166/166+34 contract/Guard healthy. Web code tree và build inputs đã xác minh khớp P66; old known-good rollback. C1B AD rollback vẫn FAIL độc lập, C2 Pro do Owner quyết trước F2 PR app/Web+3 agent. VPS-GHI trống P77.**

Đọc theo đúng thứ tự:
1. AGENTS.md ở root repo (luật hội đồng, vai trò, cổng Owner).
2. work/github-management/COLLAB.md — §0 mục tiêu Owner, Bảng điều khiển, danh sách ghế, câu hỏi quyết định.
3. work/github-management/ROADMAP.md — **V0.6, §0.4a G1 đã PASS, §0.4b C2 GH private main/required gate/Chief identity next, §0.5 DoD lịch sử.**
4. work/github-management/KE-HOACH.md — V0.5 C2 private main protection, Owner Pro/required gate/negative tests và giới hạn cùng Github identity.
5. work/github-management/DRAFT-STANDARD.md — tài liệu tham khảo, không là lệnh RUN.
6. work/github-management/PROMPT.md — **CANONICAL C2** GHM-C2-PRIVATE-MAIN-PROTECT-20261028-07; Claude P91 ACCEPT, GPT Host P92 READY@664f06e0d2c8d7839d35241f0d93a0995cda70f0. Owner giao Codex **Phần A** không cần Pro; sau KQ_A/Owner Pro active giao Claude Code CLI **Phần B** riêng; không giữ RUN chờ.

6a. [COST-LOCK-POSTPRO-20261028.md](COST-LOCK-POSTPRO-20261028.md) — Codex kiểm khóa tiền sau nâng Pro, trước C2-B, không tạo task mới.
7. [C1A-RESUME-REPORT.md](C1A-RESUME-REPORT.md) — kết quả CI và bàn giao công khai đã lược thông tin; bằng chứng vận hành lưu riêng.
8. [runner/README.md](runner/README.md) — công cụ cài/gỡ/kiểm runner và trạng thái nghiệm thu.
9. [C1A-S3-CLOSE-REPORT.md](C1A-S3-CLOSE-REPORT.md) — báo cáo lịch sử P40. Kết quả mới nhất là **COLLAB P48**, có hash báo cáo riêng và manifest 47 tệp; giữ nợ/giới hạn toàn hệ tách khỏi C1A scoped.

10a. [F1-KST-WEB-MAIN-REPORT.md](F1-KST-WEB-MAIN-REPORT.md) — **KQ hiện hành P82**: F1_A merge hai PR đúng SHA, audit main, F1_B Web production chạy build GitHub main và giữ.
10. [FAST-PR-LANE-REPORT.md](FAST-PR-LANE-REPORT.md) — KQ P77: F0 hai PR/gate thật đạt, S4-B sửa auth và candidate đáng tin; KST review/merge/release chưa thực hiện.
11. [C1B-FINALIZE-REPORT.md](C1B-FINALIZE-REPORT.md) — lịch sử P71: AD source/CI/canary đạt; deploy và Web audit còn blocker; Guard/receipt/cờ đóng.
12. [C1B-CLOSE-REPORT.md](C1B-CLOSE-REPORT.md) — KQ P66 C1B-CLOSE: Web đạt, 2/3 audit đạt; blocker AD/Web Health, bằng chứng và đường tiếp.
13. [C1B-REPORT.md](C1B-REPORT.md) — KQ P61 kế thừa: phần đạt, blocker từng app/audit, CI/SHA, archive, bằng chứng riêng và đường tiếp.

Mục tiêu duy nhất của việc này: nhiều AI nhận nhiều việc, **viết mã song song trên branch/workspace riêng**, Chief duyệt PR trên nền mới nhất, Owner xem bảng kết quả sáng. R1 dùng Actions trong hạn mức miễn phí với hard budget $0; Owner 25/10 15:18: mọi run đặt trên VPS bằng runner tự host; ưu tiên 1 là CI/CD chạy được.

Một task gốc tại đây; khi sau này mở việc mã thật ở từng repo, Issue/PR của việc là hồ sơ thực thi gắn ID, không sao chép thông tin giữa nhiều nguồn.

Lưu ý: incomex-workspace hiện là repo **public**; mọi file ở đây chỉ chứa chuẩn quy trình/câu hỏi, không chứa secret, token, đường triển khai nhạy cảm, dữ liệu nội bộ. Nếu cần trao đổi bằng chứng nhạy cảm phải chọn nơi private và chỉ dẫn link đã kiểm soát.

**P8:** PROMPT R0+R1 hoàn thiện cho Claude ký SHA; đã bổ sung kiểm các đường ghi VPS theo P7 và S0 kiểm bận trùng phạm vi. READY/RUN chỉ khi Owner giao và điều kiện sạch; không thay GitHub/VPS trong bước soạn.

Đầu vào thảo luận: chỉ đạo Owner ngày 23/10/2026, đề xuất Claude về Pro/rulesets, và đối chiếu tài liệu GitHub chính thức được ghi trong DRAFT-STANDARD.md. DRAFT này là câu trả lời để hội đồng thảo luận; Owner mới là người chốt.
