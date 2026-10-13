import sys

import pytest

from src.cli.main import main


def test_main_requires_github_token(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["prog", "--repo", "octocat/hello-world"])
    monkeypatch.delenv("GITHUB_TOKEN", raising=False)
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)

    with pytest.raises(SystemExit, match="GITHUB_TOKEN"):
        main()
