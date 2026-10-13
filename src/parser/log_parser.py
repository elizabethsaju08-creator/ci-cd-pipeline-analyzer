from .patterns import ERROR_PATTERN, WARNING_PATTERN, TIMESTAMP_PATTERN, STEP_PATTERN

class LogParser:
    def __init__(self, raw_log: str):
        self.raw_log = raw_log
        self.lines = raw_log.splitlines()

    def extract_errors(self):
        return [line for line in self.lines if ERROR_PATTERN.search(line)]

    def extract_warnings(self):
        return [line for line in self.lines if WARNING_PATTERN.search(line)]

    def extract_steps(self):
        steps = []
        for line in self.lines:
            match = STEP_PATTERN.search(line)
            if match:
                steps.append(match.group(1))
        return steps

    def extract_timestamps(self):
        return [line for line in self.lines if TIMESTAMP_PATTERN.search(line)]
