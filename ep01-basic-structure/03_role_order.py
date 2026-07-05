# 集1 · 知识点3：role 顺序的两条硬约束 + fake 历史技巧
#
# 硬约束（违反任何一条 API 直接报错）：
#   1. user 和 assistant 必须交替，不能两个 user 或两个 assistant 连续
#   2. 第一条消息必须是 user，不能 assistant 开头
#
# 错误示范（不要运行，运行就是报错）：
#
#   messages = [
#       {"role": "user", "content": "你好"},
#       {"role": "user", "content": "帮我写个总结"},   # 两个 user 连续 → 报错
#   ]
#
#   messages = [
#       {"role": "assistant", "content": "你好！"},      # assistant 开头 → 报错
#       {"role": "user", "content": "帮我写个总结"},
#   ]

from anthropic import Anthropic

client = Anthropic()

MODEL = "claude-opus-4-7"

# 正确格式：user 开始，user/assistant 交替
resp = client.messages.create(
    model=MODEL,
    max_tokens=1024,
    temperature=0,
    messages=[
        {"role": "user", "content": "四川的省会是哪?"},
        {"role": "assistant", "content": "成都。"},
        {"role": "user", "content": "那湖北呢?"},
    ],
)
print("【正常多轮】")
print(resp.content[0].text)
print()

# 技巧：用 fake 历史控制输出风格
# 前两轮"对话"是我们自己编的，模型看到这个 pattern 会延续简短风格，
# 回答"杭州。"而不是"浙江的省会是杭州。"
# 这是 few-shot 的一种形态，集7 专门讲。
resp = client.messages.create(
    model=MODEL,
    max_tokens=1024,
    temperature=0,
    messages=[
        {"role": "user", "content": "四川的省会是哪?"},
        {"role": "assistant", "content": "成都。"},
        {"role": "user", "content": "那湖北呢?"},
        {"role": "assistant", "content": "武汉。"},
        {"role": "user", "content": "那浙江呢?"},
    ],
)
print("【fake 历史控制风格】")
print(resp.content[0].text)
