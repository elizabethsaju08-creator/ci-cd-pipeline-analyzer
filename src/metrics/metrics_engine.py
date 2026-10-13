import statistics
from datetime import datetime

class MetricsEngine:
    def __init__(self, timestamps: list[str]):
        self.timestamps = timestamps

    def _to_seconds(self, ts: str):
        h, m, s = map(int, ts.split(":"))
        return h * 3600 + m * 60 + s

    def compute_duration(self):
        if len(self.timestamps) < 2:
            return None
        start = self._to_seconds(self.timestamps[0])
        end = self._to_seconds(self.timestamps[-1])
        return end - start

    def compute_step_stats(self, steps: list[str]):
        return {
            "total_steps": len(steps),
            "unique_steps": len(set(steps))
        }
