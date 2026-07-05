# 集1 · Prompt 的基础架构

心法一句话：**Prompt 不是一段文字，是一组带 role 的消息加一组配置参数。**

本集 5 个知识点，每个对应一个可运行脚本：

| 脚本 | 知识点 | 一句话结论 |
|------|--------|-----------|
| `01_three_roles.py` | 三种 role 的语义 | system 是权威槽、user 是当前需求、assistant 是模型的历史发言，塞错位置效果差一截 |
| `02_max_tokens.py` | max_tokens 硬停陷阱 | 它是硬截断上限不是目标长度；输出"突然结束"先查它 |
| `03_role_order.py` | role 顺序硬约束 + fake 历史技巧 | 必须 user 开头、user/assistant 交替，违反直接报错；fake 历史可以控制输出风格 |
| `04_system_prompt.py` | system prompt 的特殊地位 | system 是独立参数不在 messages 里，改变的是整次对话的"发言人格" |
| `05_temperature.py` | temperature 旋钮 | 做实验设 0，内容生成 0.7-1.0；这是两件不同的事 |

运行方式（先按仓库根目录 README 配好环境变量）：

```bash
python 01_three_roles.py
```
