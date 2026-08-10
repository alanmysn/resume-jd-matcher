from pathlib import Path

import streamlit as st

from services.llm import analyze_jd

PROMPT_PATH = Path(__file__).parent / "prompts" / "jd_analysis.md"


def load_prompt() -> str:
    return PROMPT_PATH.read_text(encoding="utf-8")


st.title("Job Analyzer - JD Analysis")

jd_text = st.text_area("招聘 JD", height=300, placeholder="请粘贴招聘 JD 文本")

if st.button("分析岗位"):
    if not jd_text.strip():
        st.warning("请输入 JD 内容后再分析")
    else:
        with st.spinner("正在分析，请稍候..."):
            try:
                result = analyze_jd(jd_text, load_prompt())
                st.markdown(result)
            except Exception as exc:
                st.error(f"分析失败：{exc}")
