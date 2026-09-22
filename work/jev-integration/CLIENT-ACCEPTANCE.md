# CLIENT ACCEPTANCE — JEV · ChatGPT Chat / Work / Codex

Mục tiêu: chứng minh **client thật** có thể gọi JEV đúng lúc, nhận `answers`, không tự pin model/provider/version, và không gọi thừa khi nhiệm vụ không phù hợp.

## 0. Luật chấm chung

Chỉ PASS khi có bằng chứng tool/plugin trace hoặc server-side evidence tương ứng:
1. Có gọi tool `evaluate`.
2. Tool result có `answers` hợp lệ.
3. Tool arguments **không truyền `model`**; provider/model/version do JEV Gateway/upstream quản lý.
4. GPT/Codex tự đưa ra quyết định cuối; không coi JEV là authority.

**Không chấp nhận** câu model tự kể “tôi đã hỏi JEV” nếu không có tool trace.

Negative test PASS khi **không có** call `evaluate`.

Nếu một surface chỉ hỗ trợ MCP mà không nạp Skill:
- ghi `MCP_ONLY`;
- smoke explicit-call vẫn phải PASS;
- natural-trigger không chặn DONE của Chat nếu Work + Codex đạt core acceptance theo D01.

---

# A. ChatGPT Work

## W0 — Connectivity / explicit call
Điều kiện: plugin JEV đã được cài và chọn trong Work.

Prompt:
> Hãy dùng công cụ đánh giá đi kèm plugin này trước khi kết luận. Tôi đang chọn cách triển khai một dịch vụ thử nghiệm:
> - A: dùng gói có sẵn, ít code, rollback dễ;
> - B: tự viết server để kiểm soát tối đa;
> - C: sửa sâu server đang ổn định.
> Tiêu chí: ít công bảo trì, ít rủi ro production, rollback đơn giản. Sau khi có kết quả công cụ, tự đưa ra quyết định cuối cùng.

PASS:
- exactly/at least one `evaluate` call;
- không truyền `model`;
- result có `answers`;
- câu trả lời cuối phân biệt rõ “JEV tham khảo” và quyết định của GPT.

## W1 — Natural trigger, không nhắc JEV
Prompt:
> Tôi có ba phương án cho một thay đổi hạ tầng:
> A. ghép package mã nguồn mở đã kiểm;
> B. tự viết wrapper mới;
> C. sửa server MCP đang đóng băng.
> Mục tiêu: triển khai nhanh, ít bảo trì, không phá rollback. Hãy chọn phương án phù hợp nhất và nêu ngắn gọn lý do.

PASS mục tiêu:
- Work tự gọi `evaluate` mà prompt không nhắc JEV/tool/plugin;
- không truyền `model` + có `answers`.

Nếu không gọi:
- chưa kết luận backend lỗi;
- ghi `SKILL_NOT_TRIGGERED` và chỉnh **description của Skill**, không sửa server trước.

## W2 — Negative control
Prompt:
> Viết lại câu sau cho ngắn hơn nhưng giữ nguyên nghĩa: “Hệ thống đã hoàn tất kiểm tra kết nối và hiện không cần thêm thao tác từ người dùng.”

PASS:
- không gọi `evaluate`.

---

# B. ChatGPT Chat

## C0 — Connectivity / explicit plugin
Trong Chat mới, @mention plugin JEV hoặc chọn plugin/app nếu UI yêu cầu.

Prompt:
> Dùng công cụ của plugin để đánh giá: một lệnh “xoá thư mục production rồi restart dịch vụ” có phải hành động phá huỷ và có cần Owner duyệt không? Sau đó tự kết luận.

PASS:
- `evaluate` được gọi;
- không truyền `model`;
- có answers.

## C1 — Natural trigger
Chỉ chạy nếu surface báo có Skill/plugin workflow, không chỉ MCP-only.

Prompt:
> Tôi cần quyết định có nên cho một agent tự thực hiện thao tác thay đổi production hay phải chuyển Owner duyệt. Thao tác có thể xoá dữ liệu và chưa có phê duyệt. Hãy cho quyết định cuối cùng.

PASS mục tiêu:
- tự gọi JEV dù không nhắc tên;
- không truyền `model` + có `answers`.

Nếu Chat không nạp Skill nhưng explicit C0 PASS:
- ghi `CHAT=MCP_ONLY`;
- đây là giới hạn surface/plan, không coi backend fail.

## C2 — Negative control
Prompt:
> Dịch câu “The service is healthy” sang tiếng Việt.

PASS:
- không gọi `evaluate`.

---

# C. Codex

Điều kiện: plugin JEV được bật trong Sources → Use plugins hoặc plugin local/universal đã cài. Không cho Codex sửa file trong smoke đầu tiên.

## K0 — Connectivity
Prompt:
> Không sửa file. Hãy dùng plugin JEV để đánh giá ba lựa chọn cho một gateway:
> A. package có sẵn + bridge;
> B. tự viết server;
> C. nhét vào server MCP production hiện có.
> Tiêu chí: ít code, ít coupling, rollback dễ. Sau tool result, tự kết luận.

PASS:
- trace có `evaluate`;
- không truyền `model`;
- có answers;
- không tạo/sửa file.

## K1 — Natural trigger
Prompt:
> Không sửa file. Với ba lựa chọn A/B/C dưới đây, hãy chọn phương án ít rủi ro vận hành nhất:
> A. thay đổi thuần cộng thêm và rollback riêng;
> B. sửa trực tiếp service đang dùng chung;
> C. thêm dependency mới vào service đã đóng băng.
> Ưu tiên ít coupling và rollback nhanh.

PASS mục tiêu:
- tự gọi JEV không cần nhắc tên.

## K2 — Negative deterministic
Prompt:
> Không sửa file. Hãy đếm số file tên `README.md` trong workspace hiện tại và liệt kê đường dẫn.

PASS:
- không gọi `evaluate`.

---

# D. Bộ 10 ca NÊN gọi JEV — dùng chung cho Work/Codex, Chat nếu Skill hoạt động

Mỗi ca chạy trong context sạch nếu có thể. Prompt **không chứa chữ JEV**.

1. **Package hay custom**  
   > Chọn giữa package có sẵn / tự viết wrapper / sửa service chung. Tiêu chí: ít code, ít bảo trì, rollback dễ.

2. **Destructive action**  
   > Một agent đề xuất xoá thư mục production rồi restart dịch vụ, chưa có Owner duyệt. Hãy xác định mức rủi ro và có cần chuyển Owner không.

3. **Path-secret**  
   > Chọn giữa: secret trên đĩa bền vững / GSM→tmpfs / dừng triển khai. Tiêu chí: không plaintext bền vững, ít công vận hành.

4. **Bridge**  
   > Hai bridge đều chạy; một bridge strict hơn về Accept header, bridge kia stateless và tương thích rộng hơn. Chọn bridge phù hợp cho nhiều client.

5. **Config Guard bless**  
   > Diff cấu hình chỉ có đúng các dòng của RUN đã được duyệt; smoke PASS. Có đủ điều kiện ghi baseline mới hay không?

6. **Concurrent production work**  
   > Hai task cùng muốn reload/sửa runtime trên VPS trong cùng thời điểm. Chọn: chạy song song / xếp hàng / dừng cả hai. Ưu tiên giảm xung đột.

7. **Review needed**  
   > Một thay đổi chỉ thêm tài liệu, một thay đổi sửa nginx, một thay đổi xoá dữ liệu. Xếp mức cần review thấp/trung bình/cao.

8. **Routing agent**  
   > Task là: phân tích chính sách, sửa code, hay thao tác VPS production. Chọn bề mặt phù hợp nhất trong GPT Chat / Codex / Claude Code theo loại task đã nêu.

9. **Incident severity**  
   > Cổng JEV health DOWN nhưng GPT vẫn hoạt động bình thường và JEV chỉ là tham khảo. Xếp incident LOW/MEDIUM/HIGH theo tác động.

10. **Acceptance decision**  
   > Tool chạy được khi gọi rõ tên nhưng không tự kích hoạt trong bounded decisions. Chọn trạng thái PASS / PARTIAL / FAIL cho mục tiêu “dùng tự nhiên”.

PASS mục tiêu tổng:
- ≥ 7/10 ca có call `evaluate`;
- 100% call thực tế **không truyền `model`**;
- call thành công có `answers`.

---

# E. Bộ 10 ca KHÔNG NÊN gọi JEV

1. > Rút gọn đoạn văn này xuống 2 câu, giữ nguyên nghĩa.
2. > Dịch câu này sang tiếng Anh.
3. > Tính 17 × 23.
4. > Liệt kê các file README.md trong workspace.
5. > Viết một hàm Python đảo ngược chuỗi.
6. > Tóm tắt 5 dòng log dưới đây thành 3 bullet.
7. > Kiểm SHA A có giống SHA B theo chuỗi ký tự hay không.
8. > Chuyển bảng CSV này thành JSON, không suy luận thêm.
9. > Viết regex kiểm tra chuỗi có đúng 40 ký tự hex.
10. > Brainstorm 10 tên thương hiệu sáng tạo cho một ứng dụng mới.

PASS mục tiêu tổng:
- ≤ 2/10 ca gọi `evaluate`;
- lý tưởng = 0/10.

---

# F. Trình tự nghiệm thu để tiết kiệm thời gian

## F1 — Smoke trước
Theo thứ tự:
1. Work: W0 → W1 → W2.
2. Chat: C0 → C1 nếu Skill có mặt → C2.
3. Codex: K0 → K1 → K2.

Chỉ khi smoke PASS mới chạy 10+10.

## F2 — Full acceptance
- Codex: tự động hóa 10+10, mỗi ca context/session sạch nếu khả thi; chấm từ trace.
- Work: chạy 10+10 theo batch nhỏ nhưng tách từng item rõ, không cần Owner gõ từng ca.
- Chat: full 10+10 chỉ nếu Skill tự trigger; nếu MCP-only thì C0/C2 + vài natural probes là đủ để ghi rõ giới hạn surface.

## F3 — Kết quả cần ghi
Mỗi surface:
- `CONNECTIVITY=PASS|FAIL`
- `SKILL=AUTO|MCP_ONLY|UNAVAILABLE`
- `POSITIVE_TRIGGER=x/10`
- `FALSE_TRIGGER=x/10`
- `MODEL_ARG_ABSENT=x/x`
- `ANSWERS=x/x`
- `FINAL=PASS|PARTIAL|FAIL`

Core DONE của OpenAI:
- Work = PASS;
- Codex = PASS;
- Chat = PASS hoặc PARTIAL(MCP_ONLY), theo D01.

---

# G. GPT nên “nhớ” dùng JEV ở đâu?

## G1 — Nguồn chính: Skill trong plugin
Đặt:
`plugins/jev-reference/skills/jev-reference/SKILL.md`

Skill là nơi duy nhất chứa logic:
- khi nào nên gọi;
- khi nào không;
- không truyền `model`; provider/model/version do gateway quản lý;
- JEV chỉ tham khảo;
- thiếu `answers` = unavailable.

**Không chép logic này vào AGENTS.md toàn workspace.** JEV không chỉ dùng cho repo và việc chép đôi sẽ lệch phiên bản.

## G2 — MCP app/server: chỉ capability
Remote MCP/app chỉ cần expose tool `evaluate` + schema/error đúng. Tool description nên ngắn, nói rõ đây là typed bounded-decision evaluation; không biến tool description thành bản sao của Skill.

## G3 — Plugin: gắn Skill với MCP app đã đăng ký
Ưu tiên plugin tham chiếu **registered MCP app** bằng `.app.json`, thay vì nhúng secret URL vào `mcp.json`.

Lý do:
- secret URL ở connection/app, không nằm trong repo/plugin package;
- plugin đóng gói Skill + connection thành một capability dùng lại;
- ChatGPT và Codex dùng chung plugin directory trên surface hỗ trợ.

Cấu trúc logic:
```
jev-reference-plugin/
├── plugin.json
├── .app.json          # reference registered JEV MCP app id
└── skills/
    └── jev-reference/
        └── SKILL.md
```

## G4 — Codex hooks: chỉ bổ sung nếu acceptance chứng minh cần
Không thêm hook ở V0.
Chỉ khi Codex K1/POSITIVE_TRIGGER thấp dù Skill tốt mới thử SessionStart/UserPromptSubmit reminder.
Không dùng PreToolUse để bắt buộc/chặn.

## G5 — Không dùng Memory làm policy
Không dựa vào ChatGPT Memory để “nhớ dùng JEV”. Memory không phải nơi quản lý workflow/tool policy và không bảo đảm mọi surface nạp giống nhau.

Nguồn chuẩn cho GPT = **Plugin Skill + registered MCP app**.
