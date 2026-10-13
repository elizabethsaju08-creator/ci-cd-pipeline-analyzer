import json

class JSONReport:
    def generate(self, metrics, ai_summary):
        return json.dumps({
            "metrics": metrics,
            "ai_summary": ai_summary
        }, indent=4)
