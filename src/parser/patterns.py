import re

ERROR_PATTERN = re.compile(r"(error|failed|exception)", re.IGNORECASE)
WARNING_PATTERN = re.compile(r"(warning|deprecated)", re.IGNORECASE)
TIMESTAMP_PATTERN = re.compile(r"\d{2}:\d{2}:\d{2}")
STEP_PATTERN = re.compile(r"Run (.+)")
