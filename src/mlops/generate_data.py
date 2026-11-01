"""Generate a small deterministic chemistry dataset."""

import csv
from pathlib import Path

OUTPUT = Path("data/substances.csv")
ROWS = [
    ("H2O", 18.015, 36.03),
    ("NaCl", 58.44, 11.688),
    ("CO2", 44.01, 22.005),
    ("C6H12O6", 180.156, 9.0078),
]


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(("formula", "molar_mass_g_mol", "mass_g"))
        writer.writerows(ROWS)
    print(f"Generated {len(ROWS)} substances in {OUTPUT}")


if __name__ == "__main__":
    main()
