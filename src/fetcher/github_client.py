import requests

class GitHubClient:
    def __init__(self, token: str, repo: str):
        self.token = token
        self.repo = repo
        self.base_url = f"https://api.github.com/repos/{repo}"

    def _headers(self):
        return {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/vnd.github+json"
        }

    def get_workflow_runs(self, branch="main"):
        url = f"{self.base_url}/actions/runs?branch={branch}"
        response = requests.get(url, headers=self._headers())
        response.raise_for_status()
        return response.json()

    def get_log_url(self, run_id: int):
        url = f"{self.base_url}/actions/runs/{run_id}/logs"
        response = requests.get(url, headers=self._headers(), allow_redirects=False)
        response.raise_for_status()
        return response.headers.get("Location")

    def download_logs(self, log_url: str):
        response = requests.get(log_url)
        response.raise_for_status()
        return response.content.decode("utf-8", errors="ignore")
