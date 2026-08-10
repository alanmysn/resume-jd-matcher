import os

from dotenv import load_dotenv
from openai import OpenAI

DEEPSEEK_BASE_URL = "https://api.deepseek.com"
DEEPSEEK_MODEL = "deepseek-chat"
REQUEST_TIMEOUT = 120

load_dotenv()


def analyze_jd(jd_text: str, prompt_text: str) -> str:
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        raise ValueError("未找到 DEEPSEEK_API_KEY，请在 .env 文件中填写你的 DeepSeek API Key")

    client = OpenAI(api_key=api_key, base_url=DEEPSEEK_BASE_URL, timeout=REQUEST_TIMEOUT)

    response = client.chat.completions.create(
        model=DEEPSEEK_MODEL,
        messages=[
            {"role": "system", "content": prompt_text},
            {"role": "user", "content": jd_text},
        ],
    )
    return response.choices[0].message.content
