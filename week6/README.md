# Week 6 — Golden Set Baseline Evaluation (Release v0.1)

This practical runs a baseline evaluation of the local **Llama 3.2** model using Ollama and a 30-question golden set.

## Files
- `golden_set.json`: questions, expected answers, keywords, and source links
- `main.py`: runs questions through Ollama, scores keyword coverage, and saves the report
- `requirements.txt`: Python dependency list
- `baseline_results.csv`: generated output after running the evaluation

## Prerequisites
1. Install Ollama and check it in PowerShell:
   ```powershell
   ollama --version
   ```
2. Pull the model:
   ```powershell
   ollama pull llama3.2
   ```
3. Ensure Ollama is running.

## Setup and run
From this `week6` directory:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

The program evaluates every golden-set question, reports matched and missing keywords, assigns **PASS** at 60% keyword coverage or higher (otherwise **REVIEW**), and writes the run to `baseline_results.csv`.

## Release
The first baseline is labeled **v0.1**. The CSV is generated from the actual model run and is not included as fabricated sample results.
