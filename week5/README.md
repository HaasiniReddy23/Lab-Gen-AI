# Week 5 — Token Economics

A small pre-build budgeting tool for estimating LLM token usage, API cost, and rate-limit capacity before implementing a feature.

## What it checks
- Daily input, output, and total token usage
- Estimated daily and 30-day cost
- Peak requests per minute (RPM) and tokens per minute (TPM), with a safety margin
- Daily and monthly budget thresholds
- A go/no-go style planning recommendation

## Setup

```bash
python -m venv .venv
```

Activate the environment:


**Windows**
```bash
.venv\\Scripts\\activate
```

**Linux/macOS**
```bash
source .venv/bin/activate
```

Install dependencies and prepare environment values:

```bash
pip install -r requirements.txt
cp .env.example .env
```

On Windows Command Prompt, use `copy .env.example .env` instead of `cp`.
Edit `.env` and set prices and quotas for the exact model, provider, account, and service tier. The included values are illustrative.

## Run the planner

```bash
python budget.py
```

## Run tests

```bash
python -m unittest -v
```

## Notes
- Cost and rate-limit results are planning estimates, not billing guarantees.
- The safety margin is applied to peak RPM/TPM and budget checks.
- TPM is modeled as a simplified total-token limit. Confirm the provider's quota rules and whether input/output are counted separately.
- Before launch, measure token counts using the selected provider tokenizer or API usage metadata.
- Consider retries, long prompts, retrieved context, tool schemas, and p50/p95 token sizes.
- Never commit API keys or real secrets. Keep `.env` local and commit only `.env.example.
