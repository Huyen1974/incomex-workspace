// Single TEST fixture; all five patterns read the same state. No external API.
window.GATE2_FIXTURE = {
  "label": "TEST ONLY · R9 design workshop",
  "context": {
    "object_ref": "TEST.MOW.duration-001",
    "name": "Ghi nhận và tổng hợp thời lượng xử lý",
    "family": "MOW",
    "definition_version": 1,
    "draft_revision": 1,
    "scope": "TEST.ops",
    "owner": "TEST.owner.mow",
    "package_ref": "TEST.PKG.duration-001",
    "return_context": "P02 / TEST.MOW.duration-001 / gói đang rà",
    "release_ref": "TEST.RELEASE.duration-v1",
    "instance_ref": "TEST.INSTANCE.duration-001",
    "attempt_ref": "TEST.ATTEMPT.auto-001"
  },
  "intent": "Ghi nhận thời lượng xử lý yêu cầu. Sau khi người thực hiện nộp, hệ thống tổng hợp kết quả và đánh dấu khi quá 60 phút. Dùng lại các nguyên liệu có sẵn.",
  "objects": [
    {
      "id": "field.so_phut",
      "family": "Field",
      "name": "Thời lượng dự kiến",
      "version": 1,
      "owner": "TEST.owner.field",
      "status": "active",
      "match": "exact",
      "meaning": "task · integer · minute · input",
      "where_used": [
        "TEST.MOIT.duration-v1",
        "TEST.MOT.capture-v1"
      ]
    },
    {
      "id": "field.ngay_lap",
      "family": "Field",
      "name": "Ngày tạo hệ thống",
      "version": 1,
      "owner": "TEST.owner.field",
      "status": "active",
      "match": "exact",
      "meaning": "record · timestamp · server-created",
      "where_used": [
        "TEST.MOIT.duration-v1"
      ]
    },
    {
      "id": "field.ghi_chu",
      "family": "Field",
      "name": "Ghi chú",
      "version": 1,
      "owner": "TEST.owner.field",
      "status": "active",
      "match": "exact",
      "meaning": "task · text · input",
      "where_used": [
        "TEST.MOIT.duration-v2"
      ]
    },
    {
      "id": "TEST.MOIT.duration",
      "family": "MOIT",
      "name": "Form ghi thời lượng",
      "version": 1,
      "owner": "TEST.owner.moit",
      "status": "active",
      "match": "exact",
      "meaning": "form layout + field bindings",
      "where_used": [
        "TEST.MOT.capture-v1"
      ]
    },
    {
      "id": "TEST.MOUT.duration",
      "family": "MOUT",
      "name": "Kết quả tổng hợp thời lượng",
      "version": 1,
      "owner": "TEST.owner.mout",
      "status": "active",
      "match": "exact",
      "meaning": "read-only result reference",
      "where_used": [
        "TEST.MOT.summary-v1"
      ]
    },
    {
      "id": "TEST.TRIGGER.submitted",
      "family": "Trigger",
      "name": "Yêu cầu đã được nộp",
      "version": 1,
      "owner": "TEST.owner.trigger",
      "status": "active",
      "match": "exact",
      "meaning": "business event definition ≠ occurrence",
      "where_used": [
        "TEST.MOW.duration-v1"
      ]
    },
    {
      "id": "TEST.NTGV.ops",
      "family": "NTGV",
      "name": "Quy tắc người thực hiện TEST",
      "version": 1,
      "owner": "TEST.owner.ntgv",
      "status": "active",
      "match": "exact",
      "meaning": "synthetic rule; D04 chưa Owner ACCEPT",
      "where_used": [
        "TEST.MOT.capture-v1"
      ]
    },
    {
      "id": "TEST.COND.over60",
      "family": "Condition",
      "name": "Thời lượng lớn hơn 60 phút",
      "version": 1,
      "owner": "TEST.owner.condition",
      "status": "missing",
      "match": "none",
      "meaning": "field.so_phut > 60 minute",
      "where_used": [
        "TEST.MOW.duration-v1"
      ]
    }
  ],
  "people": {
    "executor": "An · TEST",
    "delegate": "Bình · TEST · chỉ khi còn hiệu lực",
    "next_task_executor": "Service tổng hợp · TEST · do MOT đích phân giải",
    "report_recipient": "Owner vận hành · TEST",
    "handoff_contact": "Điều phối viên · TEST"
  },
  "human_boundary": {
    "H1": "Ý định",
    "H2": "Nghĩa mơ hồ",
    "H3": "Đánh giá chuyên môn",
    "H4": "Quyền/phê duyệt",
    "H5": "Ngoại lệ"
  },
  "patterns": {
    "P01": "Thư viện / Master",
    "P02": "Không gian rà soát",
    "P03": "Editor đúng owner",
    "P04": "Bàn làm việc runtime",
    "P05": "Vòng đời / Help / phản hồi"
  },
  "stages": [
    {
      "id": "intent",
      "title": "Ý tưởng của con người",
      "pattern": "P02",
      "actor": "H1",
      "action": "Xác nhận ý tưởng (TEST)",
      "machine": "Máy nhận scope/outcome và tạo package; không yêu cầu ID."
    },
    {
      "id": "search",
      "title": "Tìm và đối chiếu nguyên liệu",
      "pattern": "P01",
      "actor": "machine",
      "action": "Diễn bước máy: tìm nguyên liệu",
      "machine": "Catalog exact + near, completeness và where-used; chưa đủ nguồn thì không kết luận none."
    },
    {
      "id": "draft",
      "title": "Lập bản nháp và nhận diện thiếu",
      "pattern": "P02",
      "actor": "machine",
      "action": "Diễn bước máy: lập nháp",
      "machine": "Dùng Field/Form/Trigger/NTGV đã có; một Condition >60 phút chưa tồn tại."
    },
    {
      "id": "request",
      "title": "Yêu cầu bổ sung Condition",
      "pattern": "P05",
      "actor": "machine",
      "action": "Diễn bước máy: gửi request nội bộ TEST",
      "machine": "Request giữ package, slot, owner và return context; chưa gửi cho người thật."
    },
    {
      "id": "expert",
      "title": "Rà chuyên môn tại owner Condition",
      "pattern": "P03",
      "actor": "H3",
      "action": "Chấp nhận nghĩa >60 phút (H3 · TEST)",
      "machine": "Owner kiểm subject, unit, operator và threshold; không sửa Field global từ MOW."
    },
    {
      "id": "ingredient_approval",
      "title": "Duyệt nguyên liệu mới",
      "pattern": "P05",
      "actor": "H4",
      "action": "Duyệt Condition v1 (H4 · TEST)",
      "machine": "Quyết định TEST chỉ cho Condition; không đồng thời duyệt MOW."
    },
    {
      "id": "resume",
      "title": "Máy tiếp nhận và quay lại gói",
      "pattern": "P02",
      "actor": "machine",
      "action": "Diễn bước máy: resume package",
      "machine": "Read-back produced_ref/version, revalidate slot và dependency revision."
    },
    {
      "id": "declaration",
      "title": "Khai báo và đọc lại revision 2",
      "pattern": "P02",
      "actor": "machine",
      "action": "Diễn bước máy: khai báo → refetch",
      "machine": "Thêm Ghi chú đã có bằng declaration; cùng renderer, owner và package."
    },
    {
      "id": "readiness",
      "title": "Diff, tác động và readiness",
      "pattern": "P05",
      "actor": "machine",
      "action": "Diễn bước máy: kiểm readiness",
      "machine": "Một nguồn findings theo package/revision/dependency digest; không số mẫu không nguồn."
    },
    {
      "id": "test",
      "title": "Chạy bộ kiểm của bản nháp",
      "pattern": "P05",
      "actor": "machine",
      "action": "Diễn bước máy: kiểm thử",
      "machine": "Kết quả TEST có suite/revision/digest. Không dùng test revision cũ cấp quyền release."
    },
    {
      "id": "approval",
      "title": "Xin duyệt đúng bản và đúng quyền",
      "pattern": "P05",
      "actor": "H4",
      "action": "Duyệt publish + activate (H4 · TEST)",
      "machine": "Scope quyết định TEST ghi rõ cả publish và activate trên revision2; không cấp quyền thật."
    },
    {
      "id": "release",
      "title": "Phát hành rồi gắn active binding",
      "pattern": "P05",
      "actor": "machine",
      "action": "Diễn bước máy: publish → activate",
      "machine": "Release closure v1 bất biến trong fixture; active binding riêng, audit đọc lại."
    },
    {
      "id": "event",
      "title": "Occurrence sinh instance",
      "pattern": "P04",
      "actor": "machine",
      "action": "Diễn bước máy: nhận event",
      "machine": "Occurrence khác Trigger Definition; instance pin release v1. Dedupe theo occurrence."
    },
    {
      "id": "hmitl",
      "title": "Người thực hiện ghi nhận thời lượng",
      "pattern": "P04",
      "actor": "HMITL",
      "action": "Nộp dữ liệu HMITL (TEST)",
      "machine": "Nhập nghiệp vụ có chủ đích; actor/time/version là máy điền và server target kiểm."
    },
    {
      "id": "auto",
      "title": "Worker xử lý AUTO",
      "pattern": "P04",
      "actor": "machine",
      "action": "Diễn tiến worker (TEST)",
      "machine": "Không có AUTO Done. Worker dùng capability/pinned input; native queue owns retry/ack."
    },
    {
      "id": "end",
      "title": "Kiểm output và kết thúc",
      "pattern": "P04",
      "actor": "machine",
      "action": "Diễn bước máy: đối chiếu output",
      "machine": "Có receipt và MOUT đọc lại; missing output không được kết thúc."
    },
    {
      "id": "feedback",
      "title": "Góp ý từ đúng ngữ cảnh",
      "pattern": "P05",
      "actor": "H1",
      "action": "Ghi nhận ý tưởng cải tiến (TEST)",
      "machine": "Feedback tự gắn context/instance/release; không yêu cầu dán trace hay ID."
    },
    {
      "id": "improve",
      "title": "Lập version cải tiến",
      "pattern": "P02",
      "actor": "machine",
      "action": "Diễn bước máy: lập nháp version 2",
      "machine": "Version2 DRAFT liên feedback; instance cũ vẫn pin releasev1. Chưa duyệt version2."
    },
    {
      "id": "finished",
      "title": "Đã đi hết happy path thiết kế",
      "pattern": "P02",
      "actor": "terminal",
      "action": "Đã hoàn tất lượt thiết kế",
      "machine": "READY FOR PM REVIEW là trạng thái gói. Gate2 chưa PM ACCEPT; O1–O3 chưa VERIFIED."
    }
  ],
  "negatives": [
    {
      "id": "N01",
      "title": "Tìm chưa đủ / nghĩa mơ hồ",
      "at": 1,
      "state": "INCOMPLETE_SEARCH / AMBIGUOUS",
      "finding": "Nguồn catalog thứ hai timeout; hai alias cùng tên khác đơn vị. Không được tạo mới từ kết quả này.",
      "machine": "Máy thử lại nguồn có quyền, so subject/unit; nếu vẫn còn hai nghĩa hợp lệ thì hỏi H2 shortlist.",
      "human": "H2",
      "repair": "Chọn nghĩa minute sau khi nguồn đã đủ (H2 · TEST)",
      "resume": "Giữ intent/package; quay lại search có completeness và lý do chọn."
    },
    {
      "id": "N02",
      "title": "Thiếu nguyên liệu",
      "at": 3,
      "state": "MISSING_INGREDIENT",
      "finding": "Condition >60 phút chưa có; package bị chặn tại slot condition.",
      "machine": "Máy tạo/đọc request cùng fingerprint, route owner; chờ produced version rồi revalidate.",
      "human": "machine",
      "repair": "Diễn sửa lỗi: theo request và mở owner editor",
      "resume": "Đi P03→H4 nguyên liệu→resume, không nhập lại ý tưởng."
    },
    {
      "id": "N03",
      "title": "Bản cũ / xung đột",
      "at": 8,
      "state": "STALE_REVISION / 409",
      "finding": "Bản nháp hoặc dependency đã đổi; test/approval đang giữ revision cũ. Input được giữ.",
      "machine": "Máy đọc bản hiện hành, tạo diff; chỉ auto-merge phần không xung đột đã có policy.",
      "human": "H3",
      "repair": "Đối chiếu thay đổi và nhận revision mới (H3 · TEST)",
      "resume": "Về readiness→test→approval trên revision mới; không overwrite mù."
    },
    {
      "id": "N04",
      "title": "Caller không đủ quyền",
      "at": 10,
      "state": "FORBIDDEN / 403",
      "finding": "Caller không có quyền publish trong scope này; không có fallback admin.",
      "machine": "Tạo handoff request tới owner; giữ package read-only cho caller, recheck sau quyết định quyền riêng.",
      "human": "H4",
      "repair": "Diễn Owner đủ quyền tiếp nhận (H4 · TEST)",
      "resume": "Đúng owner review cùng package; quyết định TEST không cấp quyền thật."
    },
    {
      "id": "N05",
      "title": "Thiếu assignee / ủy quyền hết hạn",
      "at": 13,
      "state": "BLOCKED_ASSIGNMENT",
      "finding": "Executor chưa resolve hoặc delegation không còn hiệu lực tại lúc claim.",
      "machine": "Máy re-resolve từ NTGV/People; người có quyền xử lý reassign nếu nguồn vẫn thiếu.",
      "human": "H5",
      "repair": "Diễn reassign hợp lệ từ nguồn người (H5 · TEST)",
      "resume": "Resume cùng task/instance, history executor trước còn; D04 vẫn chờ Owner thật."
    },
    {
      "id": "N06",
      "title": "Kiểm thử không đạt",
      "at": 9,
      "state": "TEST_FAILED",
      "finding": "Case âm phát hiện output không đúng profile; không được dùng approval bù lỗi.",
      "machine": "Finding route owner-editor, sửa declaration rồi chạy lại suite cho revision mới.",
      "human": "machine",
      "repair": "Diễn sửa lỗi: sửa khai báo và kiểm lại",
      "resume": "Về readiness và test; exact digest mới trước approval."
    },
    {
      "id": "N07",
      "title": "Duyệt bị từ chối / hết hạn",
      "at": 11,
      "state": "APPROVAL_DENIED_OR_EXPIRED",
      "finding": "Quyết định cũ không cho phép activate: denied hoặc hết hạn.",
      "machine": "Giữ draft/review packet, recheck revision/test và xin decision mới khi đủ điều kiện.",
      "human": "H4",
      "repair": "Xem lại và duyệt đúng bản (H4 · TEST)",
      "resume": "Quay approval→publish; không tự dùng chữ approved cũ."
    },
    {
      "id": "N08",
      "title": "AUTO lỗi / retry",
      "at": 14,
      "state": "AUTO_RETRY_WAIT",
      "finding": "Capability transient error trước effect; attempt1 thất bại, chưa có output.",
      "machine": "Native queue retry bounded same logical effect key; nếu effect unknown phải reconcile trước retry.",
      "human": "machine",
      "repair": "Diễn native retry đã đối chiếu receipt",
      "resume": "Cùng instance/release, attempt2 riêng; không nút AUTO Done."
    },
    {
      "id": "N09",
      "title": "Thiếu output",
      "at": 15,
      "state": "OUTPUT_INCOMPLETE",
      "finding": "Worker return không đủ để complete: MOUT/receipt bắt buộc còn thiếu.",
      "machine": "Máy đối chiếu output slot, tìm lại receipt; còn thiếu thì owner exception, không giả done.",
      "human": "H5",
      "repair": "Diễn giải quyết output thiếu (H5 · TEST)",
      "resume": "Resume output check cùng instance rồi end; giữ evidence thiếu ban đầu."
    },
    {
      "id": "N10",
      "title": "Deactivate / retire còn where-used",
      "at": 17,
      "state": "RETIRE_BLOCKED_WHERE_USED",
      "finding": "Release/Field còn consumer active hoặc instance đang dùng; không retire/xóa ID.",
      "machine": "Máy lập impact plan: deprecate/replacement cho future bindings, bảo toàn current instance/history.",
      "human": "H4",
      "repair": "Chấp nhận deprecate cho lần dùng mới (H4 · TEST)",
      "resume": "Return improvement draft; không thay pin instancev1, không xóa vật cũ."
    }
  ]
};
