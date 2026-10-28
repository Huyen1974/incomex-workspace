#!/bin/zsh
# Bấm đúp để mở màn hình Graph Incomex. Chỉ chạy trên máy này (127.0.0.1), không gửi dữ liệu ra ngoài.
# Muốn tắt: đóng cửa sổ Terminal này (chọn "Terminate"/"Kết thúc") hoặc bấm Ctrl+C.
cd "${0:A:h}" || exit 1
PY=""
for c in /usr/local/bin/python3 /opt/homebrew/bin/python3 /usr/bin/python3; do
  if [[ -x "$c" ]]; then PY="$c"; break; fi
done
if [[ -z "$PY" ]]; then
  echo "Không tìm thấy python3 trên máy."; read -k 1 "?Bấm một phím để đóng…"; exit 1
fi
exec "$PY" -I tools/serve.py --open
