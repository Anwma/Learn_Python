import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qsl

host = ('', 8003)


class AddHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parse_url = urlparse(self.path)
        qs = dict(parse_qsl(parse_url.query))
        a = int(qs.get("a", 0))
        b: int = int(qs.get("b", 0))
        self.send_response(200)
        self.send_header("content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({
            "result": a + b
        }).encode("utf-8"))


if __name__ == "__main__":
    server = HTTPServer(host, AddHandler)
    print("启动服务器")
    server.serve_forever()
