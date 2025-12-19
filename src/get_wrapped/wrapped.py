from typing import Dict, Any
from get_wrapped._client import call_model


def generate_wrapped(summary: Dict[str, Any]) -> str:
    """
    Generate a Wrapped-style narrative from structured data.

    Parameters
    ----------
    summary : dict
        Structured, deterministic summary of user data.

    Returns
    -------
    str
        Wrapped-style narrative based strictly on the summary.
    """
    prompt = f"""
Create a Wrapped-style recap using ONLY the information below.

Rules:
- Base everything strictly on the provided data
- Do not assume the domain unless it is obvious
- Short, punchy sections with bold headers and relevant emojis
- Slightly playful but confident tone
- Do not mention analysis or internal representations
- Do not invent facts

Data:
{summary}
"""

    return call_model(prompt)
