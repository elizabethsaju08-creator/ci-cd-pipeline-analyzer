import pytest
from unittest.mock import patch, MagicMock
import sys
from src.cli.main import main

MOCK_LOG = """
2026-10-13T10:22:01Z Starting CI/CD pipeline...
2026-10-13T10:22:03Z Step: Checkout repository
2026-10-13T10:22:05Z Step: Install dependencies
2026-10-13T10:22:10Z Step: Run tests
2026-10-13T10:22:15Z Pipeline completed
"""

MOCK_WORKFLOW_RUNS = {
    "workflow_runs": [
        {
            "id": 123,
            "name": "CI/CD Pipeline Analyzer",
            "status": "completed",
            "conclusion": "success"
        }
    ]
}

@pytest.fixture
def mock_github_client():
    with patch("src.fetcher.github_client.GitHubClient") as mock_client:
        instance = MagicMock()
        instance.get_workflow_runs.return_value = MOCK_WORKFLOW_RUNS
        instance.get_log_url.return_value = "http://example.com/log"
        instance.download_logs.return_value = MOCK_LOG
        mock_client.return_value = instance
        yield mock_client

@pytest.fixture
def mock_openai():
    with patch("src.ai.llm_analyzer.OpenAI") as mock_ai:
        mock_instance = MagicMock()

        mock_completion = MagicMock()
        mock_choice = MagicMock()
        mock_choice.message = {"content": "Mock AI summary"}
        mock_completion.choices = [mock_choice]

        mock_instance.chat.completions.create.return_value = mock_completion
        mock_ai.return_value = mock_instance

        yield mock_ai


def test_main_runs_successfully(mock_github_client, mock_openai):
    test_args = [
        "main",
        "--repo", "octocat/hello-world",
        "--token", "dummy",
        "--ai-key", "dummy"
    ]
    with patch.object(sys, "argv", test_args):
        result = main()
        assert result is True
