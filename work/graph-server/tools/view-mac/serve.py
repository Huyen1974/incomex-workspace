"""May chu tam cho man hinh Graph Incomex (VIEW0) — chi nghe 127.0.0.1, chi phuc vu Gephi Lite ghim + tep do thi.

Chay boi OPEN-GRAPH.command (bam dup). Dong cua so Terminal hoac Ctrl+C la tat; khong dich vu nen, khong lich.
Moi phan hoi gui dung CSP da duyet (Graph P121/P122): mang chi 'self' => Matomo/GitHub/jsDelivr/Google Fonts bi chan.
RUN GS-VIEW0-MAC-LOCAL-20261011-17 · task work/graph-server.
"""
import argparse, http.server, os, socketserver, subprocess, sys, urllib.parse, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOST = "127.0.0.1"
PORTS = range(47390, 47400)
MARKER = "/incomex-graph-view.txt"
MARKER_BODY = b"incomex-graph-view GS-VIEW0\n"
CSP = ("default-src 'self'; script-src 'self' 'unsafe-eval'; style-src 'self' 'unsafe-inline'; "
       "img-src 'self' data: blob:; font-src 'self' data:; worker-src 'self' blob:; connect-src 'self'; "
       "form-action 'self'; base-uri 'self'")
APP = "/app/gephi-lite/v1.0.2/"
DATA_FILES = {"graph-merged.gexf", "graph-base88.gexf", "graph-pgdot.gexf", "graph-code.gexf", "manifest.json"}
TYPES = {".gexf": "application/xml; charset=utf-8", ".json": "application/json; charset=utf-8",
         ".js": "text/javascript; charset=utf-8", ".css": "text/css; charset=utf-8", ".html": "text/html; charset=utf-8",
         ".svg": "image/svg+xml", ".png": "image/png", ".ico": "image/x-icon", ".woff": "font/woff",
         ".ttf": "font/ttf", ".eot": "application/vnd.ms-fontobject", ".webmanifest": "application/manifest+json",
         ".graphml": "application/xml", ".txt": "text/plain; charset=utf-8"}


class Handler(http.server.BaseHTTPRequestHandler):
    server_version = "IncomexGraphView"
    sys_version = ""

    def _send(self, code, body=b"", ctype="text/plain; charset=utf-8", head=False):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Content-Security-Policy", CSP)
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "no-referrer")
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        if not head:
            self.wfile.write(body)

    def _resolve(self):
        host = (self.headers.get("Host") or "").lower()
        port = self.server.server_address[1]
        if host not in (f"127.0.0.1:{port}", f"localhost:{port}"):
            return None  # chong DNS rebinding: chi nhan dung ten may cuc bo
        path = urllib.parse.unquote(urllib.parse.urlsplit(self.path).path)
        if path == MARKER:
            return MARKER
        if path in ("/", ""):
            return "/"
        if path.startswith(APP):
            rel = path[len("/"):]
            if path.endswith("/"):
                rel += "index.html"
        elif path.startswith("/data/") and path[len("/data/"):] in DATA_FILES:
            rel = path[1:]
        else:
            return None
        full = os.path.realpath(os.path.join(ROOT, rel))
        allowed = (os.path.realpath(os.path.join(ROOT, "app")) + os.sep, os.path.realpath(os.path.join(ROOT, "data")) + os.sep)
        if not full.startswith(allowed) or not os.path.isfile(full):
            return None
        return full

    def _handle(self, head):
        full = self._resolve()
        if full is None:
            return self._send(404, b"not found\n", head=head)
        if full == MARKER:
            return self._send(200, MARKER_BODY, head=head)
        if full == "/":
            self.send_response(302)
            self.send_header("Location", start_url(self.server.server_address[1], relative=True))
            self.send_header("Content-Security-Policy", CSP)
            self.send_header("Content-Length", "0")
            self.end_headers()
            return
        with open(full, "rb") as f:
            body = f.read()
        self._send(200, body, TYPES.get(os.path.splitext(full)[1].lower(), "application/octet-stream"), head=head)

    def do_GET(self):
        self._handle(False)

    def do_HEAD(self):
        self._handle(True)

    def log_message(self, fmt, *args):
        sys.stderr.write("  " + (fmt % args) + "\n")


class Server(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True
    allow_reuse_address = True  # cho phep mo lai ngay cung cong khi con ket noi TIME_WAIT; khong bat SO_REUSEPORT


def start_url(port, relative=False, data="graph-merged.gexf"):
    base = f"http://{HOST}:{port}"
    file_url = urllib.parse.quote(f"{base}/data/{data}", safe="")
    path = f"{APP}index.html?file={file_url}"
    return path if relative else base + path


def ours(port):
    try:
        with urllib.request.urlopen(f"http://{HOST}:{port}{MARKER}", timeout=2) as r:
            return r.read() == MARKER_BODY
    except Exception:
        return False


def main():
    ap = argparse.ArgumentParser(description="Man hinh Graph Incomex cuc bo (127.0.0.1)")
    ap.add_argument("--open", action="store_true", help="mo trinh duyet mac dinh sau khi chay")
    ap.add_argument("--port", type=int, default=0, help="chi dinh cong (mac dinh tu 47390)")
    a = ap.parse_args()
    ports = [a.port] if a.port else list(PORTS)
    for port in ports:
        try:
            srv = Server((HOST, port), Handler)
        except OSError:
            if ours(port):  # da co mot cua so dang chay man hinh nay
                print(f"Màn hình Graph đang chạy sẵn ở cổng {port}; mở lại trình duyệt.")
                if a.open:
                    subprocess.run(["/usr/bin/open", start_url(port)], check=False)
                return 0
            continue
        url = start_url(port)
        print("Graph Incomex · màn hình cục bộ (chỉ máy này, 127.0.0.1:%d)" % port)
        print("Đang mở trình duyệt… Muốn TẮT: đóng cửa sổ này (hoặc bấm Ctrl+C).")
        print(url)
        sys.stdout.flush()
        if a.open:
            subprocess.run(["/usr/bin/open", url], check=False)
        try:
            srv.serve_forever()
        except KeyboardInterrupt:
            pass
        finally:
            srv.server_close()
        return 0
    print("Không tìm được cổng trống 47390–47399 trên 127.0.0.1.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
