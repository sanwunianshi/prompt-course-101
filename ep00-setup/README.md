# 集0 · 预备课：20 分钟跑通第一次 AI API 调用

零基础路线：不装 Python、不用海外信用卡，一台电脑 + 一个手机 + 10 块钱。

## 环境组合

| 组件 | 用什么 | 为什么 |
|------|--------|--------|
| 运行环境 | ModelScope（魔搭）云端 Notebook，选 CPU 实例 | 免费、国内直连、手机号注册，代码存云端 |
| 模型服务 | DeepSeek 开放平台 | 手机号注册、支付宝充值，中文能力强，价格极低 |

> 视频里演示的完整注册步骤：ModelScope 官网注册 → 我的 Notebook → CPU 实例 → 查看 Notebook 进 JupyterLab；DeepSeek 开放平台注册 → API Keys → 创建并**立刻保存**（只显示一次）→ 充值 10 元。

## 跟练代码

**Cell 1 · 装库**（DeepSeek 兼容 OpenAI 接口，所以装 openai 库）：

```python
!pip install openai -q
```

**Cell 2 · 第一次调用**：见 [`first_api_call.py`](./first_api_call.py)，把 `api_key` 换成你自己的 key，整段贴进 cell，Shift+Enter。

看到模型回你一句话，就跑通了。然后把 content 改成"用 30 字给我讲一个冷笑话"再跑一遍——你已经在做 prompt 工程了。

## 三大报错速查

| 报错 | 原因 | 解法 |
|------|------|------|
| 401 | key 填错 | 检查复制是否完整、前后有无空格 |
| RateLimitError | 没充值 | 回开放平台充值页 |
| ImportError | 第一格没跑 | 先跑 `!pip install openai -q` |

## 安全提醒

**API key 等于钱包密码**：不发群里、不写进要分享的代码、不截图。泄露了就回后台撤销重生成。
