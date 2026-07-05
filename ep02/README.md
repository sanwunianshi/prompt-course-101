# EP 02 · 清晰与直接 · 4 个练习

> 对应视频：**EP02 · 清晰与直接（Being Clear and Direct）**
> 覆盖：Anthropic Prompt Engineering Tutorial · Chapter 2
> 5 个知识点里精选 4 个**最有验证价值**的做成练习

## 前置

- 完成 [EP0 预备课](../ep00/)，拿到 DeepSeek API key
- 在 Modelscope Notebook（或 Colab）跑通 Hello 代码

## 4 个练习

| # | 文件 | 测什么 | 对应 KP | 推荐度 |
|---|---|---|---|---|
| 1 | [practice_2_2_preamble.ipynb](./practice_2_2_preamble.ipynb) | JSON parse 存活率（一行禁令让下游程序不崩） | KP2 · 跳过 preamble | ⭐⭐⭐⭐⭐ |
| 2 | [practice_2_3_choice.ipynb](./practice_2_3_choice.ipynb) | 强制模型给"一个明确答案"而不是排行榜 | KP3 · 强制做选择 | ⭐⭐⭐⭐ |
| 3 | [practice_2_4_length.ipynb](./practice_2_4_length.ipynb) | 3 种长度约束的精度对比 | KP4 · 控制长度 | ⭐⭐⭐⭐⭐ |
| 4 | [practice_2_5_2023_vs_2026.ipynb](./practice_2_5_2023_vs_2026.ipynb) | 老招 vs 新招对照（反直觉发现） | KP5 · 2026 视角 | ⭐⭐⭐⭐⭐ |

## 怎么跑

1. 下载本目录到本地
2. 上传到 Modelscope Notebook（或 Colab）
3. 从上到下 Shift+Enter 跑每个 cell
4. 观察输出，跟你的直觉对照

## 学完你能带走什么

- 一个能**通过 `json.loads()` 硬测**的 prompt 模板
- 一个能**让模型果断做选择**的 fallback hedge 技巧
- 明白"形容词控长度"已塌，**要用数字**
- 亲眼看到"CRITICAL!" 反而让输出变差 —— 建立**"别抄 2023 老招"的直觉**

## 视频课程

完整视频课程在 [知行 · Prompt 工程系统课](../../)。

---

*知行 · Prompt Engineering 系统课 · EP 02 · 2026*
