# Job Analyzer Requirements

## 1. Module Goal

Job Analyzer 用于帮助用户理解岗位要求，并逐步结合个人资料、公司信息和求职目标，判断岗位匹配情况、主要差距、潜在风险以及是否值得继续投入时间应聘。

## 2. Overall Workflow

Job Analyzer 计划拆分为三个步骤：

1. **JD Analysis**：理解岗位要求及岗位信号；
2. **Match & Gap Analysis**：结合个人资料判断匹配与差距；
3. **Risk & Decision Analysis**：结合公司信息和个人求职目标分析风险并形成综合判断。

当前 V0.1 只实现 Step 1。

## 3. Step 1 — JD Analysis

### 3.1 Input

V0.1 输入为招聘 JD 文本。

用户通过页面文本框直接粘贴招聘信息。

后续可考虑支持：

- 文档上传；
- PDF；
- 图片识别。

### 3.2 User Action

用户输入 JD 后点击“分析岗位”。

系统应：

1. 读取 `prompts/jd_analysis.md`；
2. 将 Prompt 与用户输入的 JD 提交给 LLM；
3. 获取模型返回结果；
4. 在页面展示分析内容。

### 3.3 Output

Step 1 应输出：

- 岗位要求分析；
- 岗位信号与潜在信息。

具体分析规则、概念定义、输出结构及模型约束以 `prompts/jd_analysis.md` 为准。

### 3.4 Interface

V0.1 页面保持最简结构，包括：

- JD 文本输入区域；
- “分析岗位”按钮；
- 分析结果展示区域。

当前阶段不要求复杂视觉设计。

### 3.5 Success Criteria

V0.1 完成标准：

1. 用户可以输入一份 JD；
2. 点击按钮后能够正常调用 LLM；
3. 系统使用 `prompts/jd_analysis.md` 中的分析规则；
4. 页面能够展示完整模型结果；
5. 空输入和 API 调用失败时有基本提示；
6. API Key 不暴露在代码或 GitHub 中；
7. 能够使用真实 JD 完成一次稳定的端到端分析。

V0.1 优先验证分析质量和完整工作流，不追求复杂界面或后续模块功能。
