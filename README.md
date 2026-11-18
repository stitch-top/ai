# 🤖 AI 大模型笔记

> AI 大模型系列公众号文章的配套源码与资料仓库 · 持续更新中

![Topic](https://img.shields.io/badge/topic-AI%20%E5%A4%A7%E6%A8%A1%E5%9E%8B-6fb89c)

![Series](https://img.shields.io/badge/%E7%B3%BB%E5%88%97-%E6%8F%90%E7%A4%BA%E8%AF%8D%E5%B7%A5%E7%A8%8B-f0a878)

![Status](https://img.shields.io/badge/%E7%8A%B6%E6%80%81-%E6%8C%81%E7%BB%AD%E6%9B%B4%E6%96%B0-3f7d68)

---

## 📚 目录结构

```
ai/
└── articles/                  # 文章配套文件（每篇一个文件夹）
    └── prompt-08-dify/        # 提示词工程 · 工程化篇
        ├── get_order_api.py       # 本地订单物流 mock 接口（Python）
        ├── openapi_local.json     # Schema · 本地版
        ├── openapi_httpbin.json   # Schema · 线上版（httpbin）
        └── openapi_postman.json   # Schema · 线上版（postman-echo）
```

---

## 📖 文章索引

| 系列    | 文章                               | 配套文件                      |
| ----- | -------------------------------- | ------------------------- |
| 提示词工程 | 工程化篇 · 给模型接上工具（Function Calling） | `articles/prompt-08-dify` |
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
- [ √ ] 2026-11-18 提示词工程 · 工程化篇
- [ x ] 工程化篇·资料柜与上线
- [ x ] 提示词工程 · 专精篇
- [ x ] Dify 系列后续文章

---

## 📄 说明

- 本仓库 articles 目录所有文件仅用于公众号「AI大模型」系列文章的教学演示。
- mock 接口返回的订单数据为虚构示例，仅供学习使用。

---

## 📰 公众号文章合集

「AI 大模型」系列文章已全部收录在微信合集，持续更新：

**[👉 点这里查看：AI 大模型 · 公众号文章合集](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzkxMDUzNzI0NQ==&action=getalbum&album_id=4679404626838962180#wechat_redirect)**

> 💡 在微信内打开本文链接可直接跳转合集，在电脑浏览器打开时，复制链接到微信里访问即可。
