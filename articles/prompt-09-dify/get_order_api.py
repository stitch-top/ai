"""本地订单物流 mock 接口 · 三种失败模拟版
运行： python get_order_api.py
接口： GET http://<本机IP>:18080/order/status?order_id=12345
88888 = 超时 | 99999 = 缺 eta | 未登记单号 = 空结果
"""
import json
import re
from datetime import datetime
from urllib.parse import urlparse, parse_qs
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

PORT = 18080

ORDERS = {
    "12345": {"status": "已发货", "eta": "明天送达"},
    "67890": {"status": "运输中", "eta": "后天送达"},
    "99999": {"status": "已发货"},
}


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

        m = re.search(r"\d+", order_id)  # 从句子里抠单号
        order_id = m.group() if m else ""

        if order_id == "88888":
            self.close_connection = True
            print(f"[{datetime.now():%H:%M:%S}] {self.command} {self.path} -> 模拟超时，连接掐断", flush=True)
            return

        data = ORDERS.get(order_id, {"msg": "未查询到该订单"})
        self._send(200, {**data, "order_id": order_id})

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
    print("失败模拟: 88888=超时 | 99999=缺eta | 其他=无此单", flush=True)
    srv.serve_forever()
