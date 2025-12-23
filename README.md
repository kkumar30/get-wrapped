# get-wrapped

Turn your structured data into a **yearly Wrapped-style summary**, just like your favorite music recaps — but for **any dataset**. Works seamlessly with both **OpenAI** and **Anthropic** models.

---

## Features

- Generate engaging, punchy recaps from **any structured data**.
- Provider-agnostic: works with **OpenAI** or **Anthropic** automatically.
- Simple, library-first API: just pass a summary dictionary.
- Easy integration with **pandas** or any analytics pipeline.

---

## Installation

Install from PyPI:

```bash
pip install get-wrapped
```

Or for local development:

```bash
uv sync
uv build
uv run python examples/run_wrapped.py
```

---

## Environment Variables

Set your model credentials (Not needed if you pass in your model credentials):

**Anthropic Example:**

```bash
export MODEL_API_URL="https://api.anthropic.com/v1/complete"
export MODEL_API_KEY="sk-xxxx"
export MODEL_NAME="claude-sonnet-4"      # optional
```

**Or OpenAI Example:**

```bash
export MODEL_API_URL="https://api.openai.com/v1/chat/completions"
export MODEL_API_KEY="sk-xxxx"
export MODEL_NAME="gpt-4.1-mini"  # optional
```

---
## Usage

```python
from get_wrapped import generate_wrapped

summary = {
    "rows": 5,
    "columns": {
        "activity": {"top_values": {"run": 3, "bike": 2}, "dtype": "object", "nulls": 0},
        "minutes": {"min": 20, "max": 60, "mean": 35, "sum": 175, "dtype": "float64", "nulls": 0},
    },
}

# Example summary (or pandas dataframe)
# summary = pd.DataFrame({
#     "activity": ["run", "run", "run", "bike", "bike"],
#     "minutes": [20, 30, 35, 30, 60]
# })

wrapped_text = generate_wrapped(summary)
print(wrapped_text)
```

## Output - 
```
# 🏃‍♀️ Your Activity Recap

## **Total Sessions** 📊
5 activities logged

## **Time Investment** ⏱️
175 total minutes of activity
Average session: 35 minutes

## **Activity Breakdown** 🔥
**Running** dominated with 3 sessions
**Biking** rounded out with 2 sessions

## **Session Range** 📈
Shortest: 20 minutes
Longest: 60 minutes

## **The Verdict** ✨
You kept it consistent with a solid mix of cardio activities! 🎯

```

---

## How it works

1. Provide a **structured summary** of your dataset.  
2. The library generates a **prompt** and sends it to your LLM (OpenAI or Anthropic).  
3. Receive a **fun, readable Wrapped-style recap** strictly based on your data.
4. Bring your own API key—or let the library pick it up from your local environment.

---

## Development

Clone the repository:

```bash
git clone https://github.com/yourusername/get-wrapped.git
cd get-wrapped
uv sync
uv run python examples/run_wrapped.py
```

---

## License

MIT License — see [LICENSE](LICENSE) for details.

