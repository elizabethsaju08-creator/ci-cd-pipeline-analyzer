class FlakyDetector:
    def __init__(self, errors: list[str]):
        self.errors = errors

    def detect_flaky_tests(self):
        flaky = []
        for err in self.errors:
            if "retry" in err.lower() or "flaky" in err.lower():
                flaky.append(err)
        return flaky
