# check_order.py · Dify 代码执行节点的体检代码
# 用法：整段复制进「代码执行」节点，输入变量 raw ← 工具节点的 text（不是用户输入！），
#      输出变量 state（String）、status（String）、eta（String）。
# 注意：声明的输出变量每个分支都要返回，缺了会报 Output status is missing。
# 判定：timeout = 接口超时/连接失败   empty = 查无此单   ok = 正常（eta 可为空）
# 本地自测：python check_order.py


def main(raw: str) -> dict:
    if not raw or raw.strip() == "":
        return {"state": "empty", "status": "", "eta": ""}
    import json
    try:
        data = json.loads(raw)
    except Exception:
        return {"state": "timeout", "status": "", "eta": ""}
    if not data.get("status"):
        return {"state": "empty", "status": "", "eta": ""}
    eta = data.get("eta") or ""
    return {"state": "ok", "status": data["status"], "eta": eta}


if __name__ == "__main__":
    cases = {
        "正常(12345)": '{"status": "已发货", "eta": "明天送达"}',
        "缺eta(99999)": '{"status": "已发货"}',
        "无此单(00000)": '{"msg": "未查询到该订单"}',
        "超时(空响应)": "",
        "超时(报错文本)": "Error: connection refused",
        "绑错变量(评论原文)": "订单 00000 怎么还没发货",
    }
    for name, raw in cases.items():
        print(f"{name} -> {main(raw)}")
