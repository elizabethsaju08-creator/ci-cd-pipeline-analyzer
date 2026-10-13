# 🚀 CI/CD Pipeline Analyzer  
A Python-powered tool that analyzes GitHub Actions CI/CD logs to identify bottlenecks, flaky tests, failure patterns, and performance issues — enhanced with AI-driven insights.

This project demonstrates engineering excellence across DevOps, Python architecture, automation, and AI-assisted analysis.

---

## 📌 Features

### 🔍 Log Fetching
- Connects to GitHub Actions via API  
- Retrieves workflow runs  
- Downloads raw logs for analysis  

### 🧩 Log Parsing
- Extracts errors, warnings, timestamps, and step names  
- Identifies patterns using regex  
- Supports custom parsing rules  

### 📊 Metrics Engine
- Computes pipeline duration  
- Step-level statistics  
- Detects flaky tests  
- Summarizes pipeline health  

### 🤖 AI Analysis (LLM)
- Root-cause analysis  
- Bottleneck identification  
- Recommended fixes  
- Risk scoring (0–100)  

### 📄 Reporting
- Generates HTML reports  
- JSON output for integrations  
- CLI-based execution  

---

## 🧱 Architecture Overview

mermaid
flowchart TD
    A[GitHub Actions Logs] --> B[Fetcher Module]
    B --> C[Parser Module]
    C --> D[Metrics Engine]
    C --> E[Flaky Detector]
    D --> F[AI Analyzer]
    E --> F
    F --> G[Report Generator]
    G --> H[HTML/JSON Output]

## Project Structure

ci-cd-pipeline-analyzer/
│
├── src/
│   ├── fetcher/          # GitHub API client
│   ├── parser/           # Log parsing & patterns
│   ├── metrics/          # Duration, stats, flaky tests
│   ├── ai/               # LLM analysis
│   ├── report/           # HTML & JSON reports
│   └── cli/              # Command-line interface
│
├── tests/                # Unit tests
├── examples/             # Sample logs
├── requirements.txt
└── README.md

## ⚙️ Installation

Clone the repository

bash
git clone https://github.com/<your-username>/ci-cd-pipeline-analyzer.git
cd ci-cd-pipeline-analyzer

Install dependencies

bash

pip install -r requirements.txt

## ▶️ Usage
Run the analyzer using the CLI:

bash
python -m src.cli.main \
    --token YOUR_GITHUB_TOKEN \
    --repo your-username/your-repo \
    --ai-key YOUR_OPENAI_API_KEY

Output
report.html → Full pipeline analysis

## Console → Summary + status

## 📊 Example Output (HTML Report)
Code
CI/CD Pipeline Analysis Report
------------------------------
Duration: 182 seconds
Total Steps: 14
Flaky Tests: 2 detected
AI Summary:
- Root cause: Slow dependency installation
- Bottleneck: Test suite execution
- Recommended fix: Enable caching, parallelize tests
- Risk Score: 62/100

## 🧪 Testing
Run unit tests:

bash
pytest tests/
🚀 Roadmap / Future Enhancements

Add support for GitLab CI

Add support for Azure DevOps pipelines

Add Streamlit dashboard

Add ML-based anomaly detection

Add historical trend analysis

Add Slack/Teams notifications

Add pipeline comparison reports

## 🤝 Contributing
Pull requests are welcome.
For major changes, please open an issue first to discuss what you would like to change.

## 📜 License
MIT License