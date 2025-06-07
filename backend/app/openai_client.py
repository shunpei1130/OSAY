import os
from typing import List
import openai

# Requires OPENAI_API_KEY environment variable


def generate_questions(report_text: str, n: int = 3) -> List[str]:
    prompt = (
        "次のレポート本文を読んで理解度を確認するための質問を" +
        f"{n}問生成してください。\n" +
        "レポート:\n" + report_text
    )

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=256,
    )
    content = response["choices"][0]["message"]["content"]
    # Assume each question separated by newline or numbered
    questions = [q.strip() for q in content.splitlines() if q.strip()]
    return questions[:n]
