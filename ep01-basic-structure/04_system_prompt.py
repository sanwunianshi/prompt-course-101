# 集1 · 知识点4：system prompt 的特殊地位
#
# 结构上：system 不在 messages 数组里，是 API 调用的独立参数，跟 messages 并列。
# 跟 user 的三个差异：位置不同（独立参数）、数量不同（整次对话只有一个）、权重不同。
#
# system 权重更高的三个机制：
#   1. 后训练加强 —— 模型被专门训练成"优先遵守 system 里的规则"
#   2. 注意力机制 —— 开头位置天然被加强（Lost in the Middle 现象）
#   3. 防用户覆盖 —— 规则放 user 里容易被"忽略上面所有规则"打掉，放 system 里难得多
#
# 判断规则：整次对话每轮都适用的放 system，只在这一轮适用的放 user。

from anthropic import Anthropic

client = Anthropic()

MODEL = "claude-opus-4-7"
PROMPT = "天空有多大?"

# 例1：没有 system —— 标准科学答案
resp = client.messages.create(
    model=MODEL,
    max_tokens=2048,
    temperature=0,
    messages=[{"role": "user", "content": PROMPT}],
)
print("【无 system】")
print(resp.content[0].text)
print()

# 例2：加 system —— 改变的是整次对话的"发言人格"，不只是这一句的风格
resp = client.messages.create(
    model=MODEL,
    max_tokens=2048,
    temperature=0,
    system="你只能像一个三岁小孩那样说话。",
    messages=[{"role": "user", "content": PROMPT}],
)
print("【system：三岁小孩】")
print(resp.content[0].text)

# system 里放什么：角色定义、上下文背景、行为规则、格式要求、禁止事项。
# 共同点：整次对话每一轮都要遵守，不随 user 输入变化。
