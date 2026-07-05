# prompt-course-101 · 小白学 AI：Prompt 工程实战课

配套短视频课程《小白学 AI》的全部示例代码。每集一个目录，代码可直接运行，跟视频里的演示一一对应。

## 课程目录

| 集数 | 主题 | 代码 |
|------|------|------|
| 集0 | 预备课：20 分钟跑通第一次 API 调用（ModelScope Notebook + DeepSeek） | [ep00-setup](./ep00-setup) |
| 集1 | Prompt 的基础架构（三种 role / max_tokens / role 顺序 / system prompt / temperature） | [ep01-basic-structure](./ep01-basic-structure) |
| 集2 | 清晰与直接 | 更新中 |
| 集3 | 角色赋予 | 更新中 |
| 集4 | 数据与指令分离 | 更新中 |
| 集5 | 输出格式控制 | 更新中 |
| 集6 | 分步思考 | 更新中 |
| 集7 | Few-shot 示例学习 | 更新中 |
| 集8 | 防幻觉 | 更新中 |
| 集9 | 复杂 Prompt 组装 | 更新中 |
| 集10 | 链式调用与工具使用 | 更新中 |

视频更新到哪集，代码就补到哪集。建议 Watch / Star 本仓库，更新会同步在这里。

## 运行准备

1. Python 3.10 以上
2. 安装 SDK：

```bash
pip install -r requirements.txt
```

3. 准备一个 Anthropic API Key，设置为环境变量：

```bash
export ANTHROPIC_API_KEY=你的key    # Windows PowerShell: $env:ANTHROPIC_API_KEY="你的key"
```

4. 进入任意一集的目录，直接运行：

```bash
cd ep01-basic-structure
python 01_three_roles.py
```

## 说明

- 所有示例默认 `temperature=0`（集1 讲过原因：做实验必须去掉随机性，结果差异才是 prompt 改动的真实效果）。
- 示例里的 max_tokens 都按任务类型给了合理值，直接抄这个标准就行。
- 代码只依赖官方 `anthropic` SDK，没有其他第三方库。
