from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List

import json


@dataclass
class QAExample:
    id: str
    question: str
    reference_answer: str
    rubric: str
    metadata: Dict[str, Any]


def load_qa_dataset(path: str | Path) -> List[QAExample]:
    dataset_path = Path(path)
    examples: List[QAExample] = []

    with dataset_path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            obj = json.loads(line)
            examples.append(
                QAExample(
                    id=str(obj["id"]),
                    question=obj["question"],
                    reference_answer=obj["reference_answer"],
                    rubric=obj.get("rubric", ""),
                    metadata=obj.get("metadata", {}),
                )
            )

    return examples


def iter_qa_dataset(path: str | Path) -> Iterable[QAExample]:
    for example in load_qa_dataset(path):
        yield example

