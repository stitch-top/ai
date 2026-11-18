"""本地订单物流 mock 接口，用于验证 Dify 自定义工具链路
运行： python get_order_api.py
接口： GET http://<本机IP>:18080/order/status?order_id=12345
"""
import json
from datetime import datetime
from urllib.parse import urlparse, parse_qs
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

PORT = 18080


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        u = urlparse(self.path)
        q = parse_qs(u.query)
        order_id = (q.get("order_id") or [""])[0]

        if u.path.rstrip("/") != "/order/status":
            self._send(404, {"error": "not found", "path": u.path})
            return
        if not order_id:
            self._send(400, {"error": "order_id required"})
            return

        self._send(200, {"status": "已发货", "eta": "明天送达", "order_id": order_id})

    def _send(self, code, obj):
        body = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)
        print(f"[{datetime.now():%H:%M:%S}] {self.command} {self.path} -> {code}", flush=True)

    def log_message(self, *args):
        pass


if __name__ == "__main__":
    srv = ThreadingHTTPServer(("0.0.0.0", PORT), Handler)
    print(f"mock 接口已启动: http://0.0.0.0:{PORT}/order/status?order_id=12345", flush=True)
    srv.serve_forever()
