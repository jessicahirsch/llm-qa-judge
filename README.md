## LLM QA Judge

This repository provides a **subject-agnostic question–answer (QA) evaluation harness** using an LLM-as-judge pattern. You plug in different QA datasets (Kubernetes, Cypress, SRE, etc.), and reuse the same judging logic and runner. This should test how interchangeable, and how transferrable, an LLM judge can be.

### Repository structure (initial)

- `datasets/`  
  Domain-specific QA datasets in a shared JSONL schema.

- `llm_judge/`  
  Python package for:
  - Loading datasets
  - Running models to answer questions
  - Using an LLM as a judge for factual accuracy and completeness

- `requirements.txt`  
  Python dependencies for running the evaluator.

### Dataset schema (QA-focused, subject-agnostic)

Each QA example is a single JSON object in a JSONL file:

```json
{
  "id": "k8s-001",
  "question": "What is a Kubernetes Deployment?",
  "reference_answer": "A Deployment manages a ReplicaSet to keep a specified number of identical Pods running and supports rolling updates and rollbacks.",
  "rubric": "Must mention managing ReplicaSets/Pods, desired replica count, and rolling updates or rollbacks.",
  "metadata": {
    "domain": "kubernetes",
    "difficulty": "easy"
  }
}
```

You can swap in any domain (Cypress, Playwright, SRE, etc.) by changing `question`, `reference_answer`, `rubric`, and `metadata.domain` while keeping the same keys.

### Getting started

1. Create and activate a Python 3.10+ virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Add a small QA dataset under `datasets/` following the schema above.
4. Implement or extend the runner in `llm_judge/` to:
   - Load the dataset
   - Call your chosen model to generate answers
   - Call a judge model that scores answers against the rubric

Future iterations of this repo will add:

- A reference judge prompt and scoring scheme
- A CLI to run evaluations against different models and datasets
- Example reports and basic regression checks

