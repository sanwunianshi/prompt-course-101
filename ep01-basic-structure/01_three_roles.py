# 集1 · 知识点1：三种 role 的语义
#
# 每条消息底层是 {"role": ..., "content": ...}，role 只有三个合法值：
#   system    — 整次对话的长期框架（身份、规则、格式、红线），写一次全程有效
#   user      — 当前这一轮的输入
#   assistant — 模型自己的历史发言（多轮对话要把它原样塞回来，模型才"记得"）
#
# 判断规则：长期不变的放 system，当前一轮的放 user，模型说过的放 assistant。

from anthropic import Anthropic

client = Anthropic()  # 自动读环境变量 ANTHROPIC_API_KEY

MODEL = "claude-opus-4-7"

# 例1：不加 system，只发 user
resp = client.messages.create(
    model=MODEL,
    max_tokens=1024,
    temperature=0,
    messages=[{"role": "user", "content": "请从一数到三"}],
)
print("【不加 system】")
print(resp.content[0].text)
print()

# 例2：同样的 user 问题，加上 system
# system 改变的不只是语气，是整个"说话的人"
resp = client.messages.create(
    model=MODEL,
    max_tokens=1024,
    temperature=0,
    system="你只能像一个三岁小孩那样说话。",
    messages=[{"role": "user", "content": "请从一数到三"}],
)
print("【加 system：三岁小孩】")
print(resp.content[0].text)
