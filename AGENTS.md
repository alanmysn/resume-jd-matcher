# AGENTS.md

# Project Instructions

## Current Goal

当前只开发 **Job Analyzer V0.1 — Step 1: JD Analysis**。

目标是实现最小完整流程：

```text
输入 JD
→ 读取 JD Analysis Prompt
→ 调用 LLM API
→ 展示分析结果
```

除非明确要求，不实现 README Roadmap 中的后续功能。

## Source of Truth

开发时按以下文件分工执行：

- `README.md`：项目定位、模块结构与 Roadmap；
- `docs/requirements-job-analyzer.md`：当前产品功能与范围；
- `prompts/jd_analysis.md`：Step 1 的模型分析规则、概念定义、输出结构与约束。

不要在代码或本文件中复制完整 Prompt 逻辑。

## Tech Stack

当前使用：

- Python
- Streamlit
- LLM API
- python-dotenv
- Git / GitHub

优先采用简单、容易理解和维护的实现，不为未来可能的需求提前引入复杂架构。

## Project Structure

```text
resume-jd-matcher/
├── app.py
├── prompts/
│   └── jd_analysis.md
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
- `prompts/`：独立维护 LLM Prompt；
- `services/llm.py`：处理 LLM API 调用；
- `docs/`：保存详细产品需求。

保持 UI、LLM 调用和 Prompt 相互分离。

## Development Principles

- 优先完成最小可运行版本；
- 不主动增加未进入当前 requirements 的功能；
- 不因“工程化”目的引入不必要抽象；
- 功能复杂度增长后再进一步拆分；
- 修改尽量保持范围小、目的明确；
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

1. 建立项目基本文件；
2. 创建 Streamlit JD 输入页面；
3. 加载 `prompts/jd_analysis.md`；
4. 接入 LLM API；
5. 显示模型返回结果；
6. 添加空输入和 API 失败的基本错误处理；
7. 本地运行并使用真实 JD 测试；
8. 根据测试结果决定下一步迭代。

当前阶段以“能够稳定完成一次 JD 分析”为完成目标。
