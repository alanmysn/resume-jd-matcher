# AGENTS.md

# Project Instructions

## Current Goal

当前开发 **Job Analyzer V0.1 — Step 2: Match & Gap Analysis**。

**Step 1: JD Analysis 已完成并跑通，作为 Step 2 的稳定前置输入。**

Step 2 的目标是实现最小完整流程：

```text
输入 JD
→ Step 1：JD Analysis
→ 展示结果，并提供“清空 / 分析新 JD”与“继续分析”
→ 点击“继续分析”后自动保留 Step 1 结果
→ 输入个人资料 / 简历文本
→ 读取 Match & Gap Analysis Prompt
→ 调用 LLM API
→ 展示匹配与差距分析结果
```

Step 2 的产品范围与 Prompt 已定稿；具体模型分析规则和输出结构以 `prompts/match_analysis.md` 为准。

除非明确要求，不实现 Step 3 或 README Roadmap 中其他后续功能。

## Source of Truth

开发时按以下文件分工执行：

- `README.md`：项目定位、模块结构、当前进度与 Roadmap；
- `docs/requirements-job-analyzer.md`：Job Analyzer 当前产品功能、步骤范围与边界；
- `prompts/jd_analysis.md`：Step 1 的模型分析规则、概念定义、输出结构与约束；
- `prompts/match_analysis.md`：Step 2 的模型分析规则、概念定义、输出结构与约束。

不要在代码、requirements 或本文件中复制完整 Prompt 逻辑。

如果 requirements 与对应 Prompt 在模型分析细节上存在差异，以对应 Prompt 为具体分析规则来源；requirements 负责定义产品目标、输入输出范围和步骤边界。

## Tech Stack

当前使用：

- Python
- Streamlit
- LLM API
- python-dotenv
- Git / GitHub

优先采用简单、容易理解和维护的实现，不为未来可能的需求提前引入复杂架构。

## Project Structure

当前结构：

```text
resume-jd-matcher/
├── app.py
├── prompts/
│   ├── jd_analysis.md
│   └── match_analysis.md
├── services/
│   └── llm.py
├── docs/
│   └── requirements-job-analyzer.md
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
└── AGENTS.md
```

职责：

- `app.py`：Streamlit 页面和基础用户交互；
- `prompts/`：独立维护各分析步骤的 LLM Prompt；
- `services/llm.py`：处理 LLM API 调用；
- `docs/`：保存详细产品需求。

保持 UI、LLM 调用和 Prompt 相互分离。

## Development Principles

- 优先完成最小可运行版本；
- 不主动增加未进入当前 requirements 的功能；
- 不因“工程化”目的引入不必要抽象；
- 功能复杂度增长后再进一步拆分；
- 修改尽量保持范围小、目的明确；
- 已完成的 Step 1 作为稳定前置流程，除非 Step 2 确有依赖需要，不主动重构；
- 各 LLM 分析步骤应显式传递完成当前任务所需的输入和前置结果，使每次调用尽量自包含；不依赖模型对上一轮 API 调用或隐式会话上下文的记忆；
- 如果需求存在明显歧义且会影响实现方案，应先指出问题；
- 修复问题时优先寻找原因，不通过大量临时代码掩盖问题。

## API & Security

- API Key 通过环境变量读取；
- 本地密钥放入 `.env`；
- `.env` 必须加入 `.gitignore`；
- GitHub 只保留 `.env.example`；
- 不在代码、Prompt、日志或文档中写入真实 API Key；
- 不提交用户真实简历、个人敏感资料或其他测试隐私数据。

## Dependencies

新增第三方依赖前，应确认当前功能确实需要。

V0.1 不主动引入：

- 数据库；
- Docker；
- React / Next.js；
- FastAPI；
- 用户认证；
- 云端基础设施。

除非后续需求明确需要。

## Implementation Priority

当前阶段按以下顺序推进：

1. 在 Step 1 结果页增加“清空 / 分析新 JD”和“继续分析”操作；
2. 点击“继续分析”后自动保留 Step 1 结果并展示个人资料输入；
3. 将 Step 1 结果与个人资料提交给 `prompts/match_analysis.md` 和 LLM；
4. 展示 Match & Gap Analysis 结果；
5. 添加个人资料空输入和 API 失败的基本错误处理；
6. 使用真实 JD 与个人资料完成 Step 1 → Step 2 端到端测试；
7. 根据测试结果决定下一步迭代。

当前阶段以“能够稳定完成一次 Step 1 → Step 2 连续分析”为开发完成目标。
