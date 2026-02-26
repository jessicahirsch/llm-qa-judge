from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class JudgedAnswer:
    example_id: str
    score: float
    reason: str
    raw_judge_response: Dict[str, Any] | None = None


JUDGE_SYSTEM_PROMPT = """You are an expert evaluator of question-answer quality.

You are given:
- a user's question,
- the model's answer,
- a reference answer,
- and a grading rubric describing what a good answer must contain.

You judge only factual correctness, completeness, and adherence to the rubric.
Ignore writing style unless the rubric explicitly mentions it.

Score on a 0.0–5.0 scale:
- 5.0: Fully correct and complete according to the rubric.
- 4.0: Mostly correct, only minor omissions or issues.
- 3.0: Partially correct, significant omissions or inaccuracies.
- 2.0: Mostly incorrect, only a few correct details.
- 1.0: Barely correct, almost entirely wrong.
- 0.0: Completely incorrect, irrelevant, or nonsensical.

Be strict but fair. Do not invent requirements that are not in the rubric."""


def build_judge_user_prompt(
    *, question: str, model_answer: str, reference_answer: str, rubric: str
) -> str:
    return (
        "You will evaluate the following question and answer.\n\n"
        f"Question:\n{question}\n\n"
        f"Model answer:\n{model_answer}\n\n"
        f"Reference answer:\n{reference_answer}\n\n"
        f"Rubric:\n{rubric}\n\n"
        "Return a strict JSON object with keys 'score' (number between 0 and 5) "
        "and 'reason' (short explanation)."
    )


def parse_judge_score(response_text: str) -> Dict[str, Any]:
    """
    Parse the judge model's response into a structured score and reason.

    This is intentionally loose about formatting as long as we can recover a
    numeric score and textual reason. A production implementation should be
    stricter and handle errors carefully.
    """
    import json
    import re

    text = response_text.strip()

    try:
        obj = json.loads(text)
        score = float(obj["score"])
        reason = str(obj.get("reason", "")).strip()
        return {"score": score, "reason": reason, "raw": obj}
    except Exception:
        pass

    score_match = re.search(r"([0-5](?:\\.\\d+)?)", text)
    score = float(score_match.group(1)) if score_match else 0.0
    reason = text
    return {"score": score, "reason": reason, "raw": {"raw_text": text}}

