<div align="center">

# 🤖 AI 大模型笔记

**AI 大模型系列公众号文章的配套源码与资料仓库 · 持续更新中**

![Topic](https://img.shields.io/badge/topic-AI%20%E5%A4%A7%E6%A8%A1%E5%9E%8B-6fb89c)
![Series](https://img.shields.io/badge/%E7%B3%BB%E5%88%97-%E6%8F%90%E7%A4%BA%E8%AF%8D%E5%B7%A5%E7%A8%8B-f0a878)
![Status](https://img.shields.io/badge/%E7%8A%B6%E6%80%81-%E6%8C%81%E7%BB%AD%E6%9B%B4%E6%96%B0-3f7d68)

</div>

---

## 📚 目录结构

```
ai/
└── articles/                      # 文章配套文件（每篇一个文件夹）
    ├── prompt-08-dify/            # 提示词工程 · 工程化篇
    │   ├── get_order_api.py       # 本地订单物流 mock 接口（Python）
    │   ├── openapi_local.json     # Schema · 本地版
    │   ├── openapi_httpbin.json   # Schema · 线上版（httpbin）
    │   └── openapi_postman.json   # Schema · 线上版（postman-echo）
    └── prompt-09-dify/            # 工程化篇 · 资料库与上线
        ├── 退货政策.txt            # 知识库演示资料（虚构内容）
        ├── get_order_api.py       # mock 接口 · 三种失败模拟版（88888 超时 / 99999 缺 eta / 未登记单号空结果）
        └── check_order.py         # Dify 代码执行节点的体检代码（判定 timeout / empty / ok）
```

---

## 📖 文章索引

| 系列    | 文章                               | 配套文件                      |
| ----- | -------------------------------- | ------------------------- |
| 提示词工程 | 工程化篇 · 给模型接上工具（Function Calling） | `articles/prompt-08-dify` |
| 提示词工程 | 工程化篇 · 资料库与上线（知识库 + 版本回滚 + 降级话术） | `articles/prompt-09-dify` |
| 提示词工程 | 入门篇 / 小练习 / 进阶篇 / 评测集 / 专精篇            | 待更新                       |

---

## 🚀 快速开始（工程化篇）

### 1️⃣ 运行本地 mock 接口

```bash
# 下载或克隆仓库后，进入文章目录
cd articles/prompt-08-dify

# 启动本地订单物流接口（窗口保持开启）
python get_order_api.py
```

启动成功后，接口地址为：

```
GET http://localhost:18080/order/status?order_id=12345
```

### 2️⃣ Schema 文件说明

| 文件                     | 用途                                         | 使用场景                |
| ---------------------- | ------------------------------------------ | ------------------- |
| `openapi_local.json`   | 本地版 Schema，指向 `host.docker.internal:18080` | 本地 Dify + 本地脚本联调    |
| `openapi_httpbin.json` | 线上版 Schema，httpbin 模拟返回                    | 无本地环境，快速体验（站点偶尔不稳定） |
| `openapi_postman.json` | 线上版 Schema，postman-echo 回显参数               | httpbin 的备用方案       |

> 💡 将 Schema 内容粘贴到 Dify「创建自定义工具」的 Schema 输入框即可，详细步骤见公众号文章。

---

## 🚀 快速开始（工程化篇 · 资料库与上线）

### 1️⃣ 运行三种失败模拟版 mock 接口

```bash
# 下载或克隆仓库后，进入文章目录
cd articles/prompt-09-dify

# 启动 mock 接口（窗口保持开启）
python get_order_api.py
```

用不同订单号触发三种失败情况：

| 订单号   | 触发情况 | 预期回复                       |
| ----- | ---- | -------------------------- |
| `12345` / `67890` | 正常   | 返回状态与预计送达                  |
| `88888` | 超时   | 系统暂时查不到，请稍后再试。             |
| `99999` | 缺 eta | 订单已发货，送达时间以快递信息为准。         |
| 未登记单号 | 空结果  | 没查到该订单，麻烦核对一下单号。           |

### 2️⃣ 自测体检代码

```bash
# 代码执行节点的本地自测（6 组用例）
python check_order.py
```

> ⚠️ 在 Dify「代码执行」节点中，输入变量 raw 应绑定工具节点的 text 输出（不是用户输入），输出变量 state / status / eta 每个分支都要返回，缺了会报 `Output status is missing`。

### 3️⃣ 退货政策.txt

知识库演示资料，导入 Dify「创建即用型知识库」使用（分段最大长度 500、重叠 50，Embedding 选 `qwen3-embedding:0.6b`），导入后可用「召回测试」验证切段效果，详细步骤见公众号文章。

---

## 🗂️ 命名规范

- **仓库**：`ai`，AI 大模型相关命名。
- **文章目录**：`主题-序号-关键词`，如 `prompt-08-dify`。
- **新增文章**：在 `articles/` 下新建文件夹，放入对应源码后提交。

---

## 📝 更新计划

- [ √ ] 2026-09-14 大模型本地部署
- [ √ ] 2026-09-17 提示词工程 · 入门篇
- [ √ ] 2026-09-23 入门篇 · 小练习
- [ √ ] 2026-10-28 Open WebUI 部署
- [ √ ] 2026-11-04 提示词工程 · 进阶篇
- [ √ ] 2026-11-09 进阶篇 · 评测集
- [ √ ] 2026-11-12 Dify 开源平台
- [ √ ] 2026-11-27 工程化篇 · 资料库与上线
- [ x ] 提示词工程 · 专精篇
- [ x ] Dify 系列后续文章

---

## 📄 说明

- 本仓库 articles 目录所有文件仅用于公众号「AI大模型」系列文章的教学演示。
- mock 接口返回的订单数据为虚构示例，仅供学习使用。
- 退货政策.txt 为虚构的演示资料，内容不构成任何真实店铺的退货政策。

---

## 📰 公众号文章合集

「AI 大模型」系列文章已全部收录在微信合集，持续更新：

**[👉 点这里查看：AI 大模型 · 公众号文章合集](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzkxMDUzNzI0NQ==&action=getalbum&album_id=4679404626838962180#wechat_redirect)**

> 💡 在微信内打开本文链接可直接跳转合集，在电脑浏览器打开时，复制链接到微信里访问即可。
