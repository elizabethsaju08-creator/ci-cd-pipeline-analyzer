import argparse
import os
from dotenv import load_dotenv
from openai import OpenAI
from src.fetcher.github_client import GitHubClient
from src.parser.log_parser import LogParser
from src.metrics.metrics_engine import MetricsEngine
from src.metrics.flaky_detector import FlakyDetector
from src.ai.llm_analyzer import LLMAnalyzer
from src.report.html_report import HTMLReport

load_dotenv()  # Load environment variables from .env file

def main():
    parser = argparse.ArgumentParser(description="CI/CD Pipeline Analyzer")
    parser.add_argument("--token", default=os.getenv("GITHUB_TOKEN"), help="GitHub Personal Access Token")
    parser.add_argument("--repo", required=True)
    parser.add_argument("--ai-key", default=os.getenv("OPENAI_API_KEY"), help="OpenAI API Key")
    args = parser.parse_args()

    client = GitHubClient(args.token, args.repo)
    runs = client.get_workflow_runs()
    workflow_runs = runs.get("workflow_runs", [])
    if not workflow_runs:
        print("No workflow runs found for this repository.")
        return
    latest_run = workflow_runs[0]   

    log_url = client.get_log_url(latest_run["id"])
    raw_log = client.download_logs(log_url)

    parser = LogParser(raw_log)
    errors = parser.extract_errors()
    warnings = parser.extract_warnings()
    timestamps = parser.extract_timestamps()
    steps = parser.extract_steps()

    metrics_engine = MetricsEngine(timestamps)
    duration = metrics_engine.compute_duration()
    step_stats = metrics_engine.compute_step_stats(steps)

    flaky = FlakyDetector(errors).detect_flaky_tests()

    metrics = {
        "duration_seconds": duration,
        "step_stats": step_stats,
        "flaky_tests": flaky
    }

    ai = LLMAnalyzer(args.ai_key)
    ai_summary = ai.analyze(errors, warnings, duration)

    report = HTMLReport().generate(metrics, ai_summary)

    with open("report.html", "w") as f:
        f.write(report)

    print("Report generated: report.html")

if __name__ == "__main__":
    main()
