"""Calculate amount of substance: n = m / M."""

import csv
from pathlib import Path

SOURCE = Path("data/substances.csv")
OUTPUT = Path("data/results.csv")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with SOURCE.open(newline="", encoding="utf-8") as source:
        rows = list(csv.DictReader(source))

    with OUTPUT.open("w", newline="", encoding="utf-8") as target:
        writer = csv.writer(target)
        writer.writerow(("formula", "amount_mol"))
        for row in rows:
            molar_mass = float(row["molar_mass_g_mol"])
            mass = float(row["mass_g"])
            if molar_mass <= 0 or mass < 0:
                raise ValueError("Molar mass must be positive and mass non-negative")
            writer.writerow((row["formula"], round(mass / molar_mass, 6)))
    print(f"Calculated {len(rows)} rows in {OUTPUT}")


if __name__ == "__main__":
    main()
