# 集1 · 知识点2：max_tokens 的硬停陷阱
#
# 两个常见误解：
#   误解1：max_tokens 是"输出质量的上限" —— 不是，它是 hard stop，到数就切，
#          可能停在句子中间。
#   误解2：max_tokens 是"最佳输出长度" —— 也不是，模型答完了会自然停，不凑字数。
#
# 它也不是付费上限：设 8192 实际只输出 600 token，就只算 600 token 的钱。
# 设小了不是省钱，是功能坏了。
#
# 参考值：字段提取 1024-2048 / 摘要 4096 / 长文代码报告 8192 起 / 多轮 agent 8192 以上。

from anthropic import Anthropic

client = Anthropic()

MODEL = "claude-opus-4-7"
PROMPT = "请写一段 300 字左右的短文，介绍猫的生活习性。"

# 例1：max_tokens 设得太小 —— 输出被硬截断，stop_reason 是 "max_tokens"
resp = client.messages.create(
    model=MODEL,
    max_tokens=60,
    temperature=0,
    messages=[{"role": "user", "content": PROMPT}],
)
print("【max_tokens=60】stop_reason =", resp.stop_reason)  # max_tokens = 被截断
print(resp.content[0].text)
print()

# 例2：max_tokens 给足 —— 模型自然写完，stop_reason 是 "end_turn"
resp = client.messages.create(
    model=MODEL,
    max_tokens=4096,
    temperature=0,
    messages=[{"role": "user", "content": PROMPT}],
)
print("【max_tokens=4096】stop_reason =", resp.stop_reason)  # end_turn = 自然结束
print(resp.content[0].text)

# 调试口诀：输出"突然结束"，第一个查 max_tokens，第二个才怀疑 prompt。
