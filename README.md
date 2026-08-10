# Resume JD Matcher

一个面向求职场景的 AI 辅助工具，用于理解岗位要求、判断个人匹配情况，并进一步支持定制化应聘材料和面试准备。

项目重点不是单纯生成文本，而是将岗位分析、个人经历和历史面试内容组织成可复用的求职工作流。

## Product Structure

项目计划分为三个模块。

### 1. Job Analyzer

分析岗位本身及个人与岗位的匹配情况，主要包括：

- 提炼岗位核心要求并判断重要性；
- 分析岗位中的潜在信息和需要进一步确认的问题；
- 结合个人简历或经历判断匹配点和差距；
- 结合公司信息和个人求职目标分析岗位风险；
- 综合判断是否值得继续投入时间应聘。

这是当前优先开发的核心模块。

### 2. Application Generator

针对决定继续应聘的岗位进行定制化准备，包括：

- 生成或调整针对性简历；
- 生成打招呼内容；
- 基于岗位分析生成自我介绍；
- 调取知识库中已有问题和答案；
- 根据当前岗位补充特定面试问题；
- 与 AI 讨论和优化答案；
- 将定稿内容新增或更新到知识库。

### 3. Interview Knowledge Base

沉淀长期可复用的求职素材，包括：

- 面试问题；
- 答案；
- 个人经历案例；
- 标签及分类信息。

知识库主要为 Application Generator 提供历史内容复用，并随着实际面试准备持续更新。

## Current Scope

当前只开发 **Job Analyzer V0.1**。

第一阶段先实现其中的 **Step 1：JD Analysis**：

1. 用户输入招聘 JD；
2. 系统调用预设 JD 分析规则和 LLM；
3. 返回岗位要求分析与岗位信号分析结果。

当前目标是先验证 JD 分析流程是否稳定、有效，不提前实现后续模块和复杂功能。

## V0.1 Tech Stack

- Python
- Streamlit
- LLM API
- python-dotenv
- Git / GitHub

## Roadmap

### Job Analyzer

- Step 1：JD Analysis
- Step 2：个人匹配与差距分析
- Step 3：岗位风险与综合应聘判断
- 文件上传
- 公司信息补充与外部搜索
- 历史岗位分析保存

### Future Modules

- Application Generator
- Interview Knowledge Base

后续模块的具体设计根据 Job Analyzer 的实际开发和使用结果继续迭代。
