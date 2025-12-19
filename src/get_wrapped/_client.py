import os
import requests

MODEL_API_URL = os.getenv("MODEL_API_URL")
MODEL_API_KEY = os.getenv("MODEL_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")  # Optional, use provider default if None

if not MODEL_API_URL or not MODEL_API_KEY:
    raise RuntimeError(
        "MODEL_API_URL and MODEL_API_KEY must be set."
    )


def call_model(prompt: str) -> str:
    """
    Call LLM using provider inferred from the URL.
    """
    url = MODEL_API_URL.lower()

    if "openai.com" in url:
        model = MODEL_NAME or "gpt-4.1-mini"
        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": "You turn structured data summaries into engaging personal recaps."},
                {"role": "user", "content": prompt},
            ],
            "temperature": 0.7,
        }
        headers = {
            "Authorization": f"Bearer {MODEL_API_KEY}",
            "Content-Type": "application/json",
        }
        response = requests.post(MODEL_API_URL, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]

    elif "anthropic.com" in url:
        model = MODEL_NAME or "claude-sonnet-4-20250514"  # Updated default model
        payload = {
            "model": model,
            "max_tokens": 2048,
            "messages": [  # New format: messages array instead of prompt string
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7,
        }
        headers = {
            "x-api-key": MODEL_API_KEY,
            "Content-Type": "application/json",
            "anthropic-version": "2023-06-01",  # Required header
        }
        response = requests.post(MODEL_API_URL, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        return response.json()["content"][0]["text"]  # Changed response parsing

    else:
        raise ValueError(
            f"Cannot determine LLM provider from URL: {MODEL_API_URL}. Must contain 'openai.com' or 'anthropic.com'."
        )
