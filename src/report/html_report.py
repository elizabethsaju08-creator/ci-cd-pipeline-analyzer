from datetime import datetime

class HTMLReport:
    def generate(self, metrics, ai_summary):
        html = f"""
        <html>
        <head><title>CI/CD Pipeline Report</title></head>
        <body>
            <h1>CI/CD Pipeline Analysis Report</h1>
            <p><strong>Generated:</strong> {datetime.now()}</p>

            <h2>Metrics</h2>
            <pre>{metrics}</pre>

            <h2>AI Summary</h2>
            <pre>{ai_summary}</pre>
        </body>
        </html>
        """
        return html
