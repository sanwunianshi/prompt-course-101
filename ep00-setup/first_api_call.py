# 集0 · 第一次 API 调用（在 ModelScope Notebook 的 cell 里跑）
# 先跑上一格：!pip install openai -q

from openai import OpenAI

client = OpenAI(
    api_key="sk-你的DeepSeek API key",   # ← 换成你自己的 key
    base_url="https://api.deepseek.com/v1",
)

response = client.chat.completions.create(
    model="deepseek-chat",
    max_tokens=200,
    messages=[
        {"role": "user", "content": "用一句话给我打个招呼，说明你是 DeepSeek。"}
    ],
)

print(response.choices[0].message.content)

# 想看这次真实花费，再加一行：
# print(response.usage)
