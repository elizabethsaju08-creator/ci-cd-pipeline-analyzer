import pytest
from unittest.mock import patch, MagicMock
import sys
from src.cli.main import main

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
def mock_github_api():
    with patch("src.fetcher.github_client.requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.json.return_value = MOCK_WORKFLOW_RUNS
        mock_response.status_code = 200
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response
        yield mock_get

@pytest.fixture
def mock_openai():
    with patch("src.ai.llm_analyzer.OpenAI") as mock_ai:
        mock_instance = MagicMock()
        mock_instance.chat.completions.create.return_value = {
            "choices": [{"message": {"content": "Mock AI summary"}}]
        }
        mock_ai.return_value = mock_instance
        yield mock_ai


def test_main_runs_successfully(mock_github_api, mock_openai):
    """Test main() end-to-end with mocked APIs."""
    test_args = [
        "main",
        "--repo", "octocat/hello-world",
        "--token", "dummy",
        "--ai-key", "dummy"
    ]
    with patch.object(sys, "argv", test_args):
        result = main()
        assert result is True


def test_main_requires_github_token():
    test_args = [
        "main",
        "--repo", "octocat/hello-world",
        "--ai-key", "dummy"
    ]
    with patch.object(sys, "argv", test_args):
        with pytest.raises(SystemExit):
            main()


def test_main_requires_openai_key():
    test_args = [
        "main",
        "--repo", "octocat/hello-world",
        "--token", "dummy"
    ]
    with patch.object(sys, "argv", test_args):
        with pytest.raises(SystemExit):
            main()
