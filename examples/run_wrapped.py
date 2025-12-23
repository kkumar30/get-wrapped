# examples/run_wrapped.py
from dotenv import load_dotenv  # optional, only if using .env
load_dotenv()

from get_wrapped import generate_wrapped

# Example summary (any data, eg - dict)
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

result = generate_wrapped(summary)
print(result)
