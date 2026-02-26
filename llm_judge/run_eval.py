from __future__ import annotations

import argparse
from pathlib import Path
from typing import List

from .dataset import QAExample, load_qa_dataset


def run_eval(
    *, dataset_path: Path, model_name: str, judge_model_name: str | None = None
) -> None:
    examples: List[QAExample] = load_qa_dataset(dataset_path)

    # This is a minimal placeholder implementation to establish structure.
    # In a later step, this function will:
    # - call a completion model to generate an answer for each question
    # - call a judge model using the prompts in `llm_judge.judge`
    # - aggregate and print metrics (mean score, pass rate, etc.)

    print(f"Loaded {len(examples)} examples from {dataset_path}")
    print("Model to evaluate:", model_name)
    if judge_model_name:
        print("Judge model:", judge_model_name)
    else:
        print("Judge model: (not yet wired; to be configured)")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run a subject-agnostic QA evaluation using an LLM-as-judge."
    )
    parser.add_argument(
        "--dataset",
        type=Path,
        required=True,
        help="Path to a JSONL QA dataset.",
    )
    parser.add_argument(
        "--model",
        type=str,
        required=True,
        help="Name of the model being evaluated (for reporting only for now).",
    )
    parser.add_argument(
        "--judge-model",
        type=str,
        help="Name of the judge model to use (planned future flag).",
    )

    args = parser.parse_args()
    run_eval(
        dataset_path=args.dataset,
        model_name=args.model,
        judge_model_name=args.judge_model,
    )


if __name__ == "__main__":
    main()

