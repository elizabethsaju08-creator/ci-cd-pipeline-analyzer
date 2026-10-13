import os
from openai import OpenAI
from .prompts import BASE_PROMPT

class LLMAnalyzer:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)

    def analyze(self, errors, warnings, duration):
        text = f"""
Errors:
{errors}

Warnings:
{warnings}

Duration: {duration} seconds
"""

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": BASE_PROMPT},
                {"role": "user", "content": text}
            ]
        )

        return response.choices[0].message["content"]
