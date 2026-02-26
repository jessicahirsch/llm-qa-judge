## Datasets

This directory contains **subject-agnostic QA datasets** used by the LLM QA judge.

### Format

All datasets should be stored as **JSON Lines (JSONL)** files. Each line is a single QA example with this schema:

```json
{
  "id": "domain-001",
  "question": "Your factual question here",
  "reference_answer": "The canonical or ideal answer.",
  "rubric": "What a good answer must contain. Call out key facts, concepts, and disqualifying mistakes.",
  "metadata": {
    "domain": "kubernetes",
    "difficulty": "easy"
  }
}
```

- **`id`**: Unique identifier for the example.
- **`question`**: Factual or explanatory question.
- **`reference_answer`**: Ground-truth style answer used for judging.
- **`rubric`**: Short, explicit checklist for what counts as a good answer.
- **`metadata`**: Optional domain-specific tags (e.g. `domain`, `difficulty`, `topic`).

### Example file

Create files like:

- `kubernetes_qa_small.jsonl`
- `cypress_qa_small.jsonl`
- `sre_reliability_qa.jsonl`

You can then point the evaluation runner at any of these files without changing judge logic.

