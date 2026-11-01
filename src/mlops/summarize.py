"""Summarize calculated amounts as DVC-readable JSON metrics."""

import csv
import json
from pathlib import Path

SOURCE = Path("data/results.csv")
OUTPUT = Path("reports/summary.json")


def main() -> None:
    with SOURCE.open(newline="", encoding="utf-8") as source:
        rows = list(csv.DictReader(source))
    metrics = {
        "substance_count": len(rows),
        "total_amount_mol": round(sum(float(r["amount_mol"]) for r in rows), 6),
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(metrics, indent=2) + "\n", encoding="utf-8")
    print(f"Saved metrics to {OUTPUT}")


if __name__ == "__main__":
    main()
