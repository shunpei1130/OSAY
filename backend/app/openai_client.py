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


def grade_answers(report_text: str, qa_pairs: List[tuple[str, str]]) -> str:
    qa_text = "\n".join(
        [f"Q{i+1}: {q}\nA{i+1}: {a}" for i, (q, a) in enumerate(qa_pairs)]
    )
    prompt = (
        "次のレポートと質問への回答を読んで、理解度を判定してください。"
        "十分に理解していれば '合格'、不足していれば '不合格' のみを出力してください。\n"
        f"レポート:\n{report_text}\n\n質問と回答:\n{qa_text}\n"
    )
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=10,
    )
    content = response["choices"][0]["message"]["content"]
    return "fail" if "不合格" in content else "pass"

