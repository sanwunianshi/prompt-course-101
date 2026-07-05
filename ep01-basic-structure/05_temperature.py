# 集1 · 知识点5：temperature 旋钮
#
# 模型生成每个 token 前会算一个概率分布，temperature 调的是怎么在分布上采样：
#   0   —— 每次取概率最高的 token，结果趋近确定（almost-deterministic）
#   1   —— 按概率采样，低概率词偶尔出现，每次运行有变化
#   0.7 —— 内容生成的常见默认值
#
# 实战规则（最容易被忽略）：做 prompt 工程实验、A/B 对照时，temperature 必须设 0。
# 否则你分不清结果变好是 prompt 改动的效果，还是随机性碰巧好。
#
# 任务选值：实验/A-B 对照 0 | 结构化输出(JSON/分类/提取) 0 | 代码 0-0.3 |
#          文章文案 0.7-0.9 | brainstorming 1.0
# 注意：某些推理模型不允许调 temperature（固定 1.0），Claude 4.x 系列仍然有效。

from anthropic import Anthropic

client = Anthropic()

MODEL = "claude-opus-4-7"
PROMPT = "给一家新开的咖啡店起一个名字，只输出名字本身。"

# temperature=0：跑 3 次，结果基本一样
print("【temperature=0】")
for i in range(3):
    resp = client.messages.create(
        model=MODEL,
        max_tokens=256,
        temperature=0,
        messages=[{"role": "user", "content": PROMPT}],
    )
    print(f"  第{i + 1}次:", resp.content[0].text.strip())
print()

# temperature=1：跑 3 次，大概率各不相同
print("【temperature=1】")
for i in range(3):
    resp = client.messages.create(
        model=MODEL,
        max_tokens=256,
        temperature=1,
        messages=[{"role": "user", "content": PROMPT}],
    )
    print(f"  第{i + 1}次:", resp.content[0].text.strip())
