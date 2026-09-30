# Titanic Dataset — Exploratory Data Analysis

Exploratory data analysis of Titanic passenger survival using `pandas` and `matplotlib`.

The script in `src/titanic_dataset/__init__.py` loads `tested.csv`, cleans missing data / duplicates, engineers a few features, and plots survival patterns by port, class/fare, family size, age group, and name title.

## Dataset

File: `tested.csv` — 418 rows × 12 columns (Kaggle-style Titanic test set with `Survived` labels included).

Columns:

| Column | Description |
|---|---|
| `PassengerId` | Row ID |
| `Survived` | 0 = No, 1 = Yes |
| `Pclass` | Ticket class: 1, 2, 3 |
| `Name` | Passenger name (used to extract `Title`) |
| `Sex` | male / female |
| `Age` | Age in years (86 missing) |
| `SibSp` | # siblings / spouses aboard |
| `Parch` | # parents / children aboard |
| `Ticket` | Ticket number |
| `Fare` | Ticket fare (1 missing) |
| `Cabin` | Cabin number (327 missing — dropped) |
| `Embarked` | Port of embarkation: `C`, `Q`, `S` |

## What the analysis does

1. **Cleaning (`src/titanic_dataset/__init__.py:7-19`)**
   - Drops columns with >50% missing (`Cabin`).
   - Fills numeric NaNs with median (`Age`, `Fare`).
   - Fills categorical NaNs with mode.
   - Drops duplicate rows.

2. **Feature engineering**
   - `FamilySize = SibSp + Parch + 1`
   - `isAlone = FamilySize == 1`
   - `AgeGroup = cut(Age, [0,12,18,35,60,199])` → Child, Teen, YoungAdult, Adult, Senior
   - `Title` extracted from `Name` (e.g. ` Mr`, ` Miss`, ` Mrs`, ` Master`)

3. **Analyses + plots**
   - Survival rate by `Embarked` — bar chart `Survival rate by port`
   - Mean / median `Fare` by `Pclass` — bar chart `Fare by class`
   - Survival: alone vs with family — bar chart `Survival: alone vs with family`
   - Survival rate by `AgeGroup` — bar chart `Survival rate by age group`
   - Passenger count by `Title` and survival rate by `Title` — bar charts

## Project structure

```
.
├── src/titanic_dataset/__init__.py  # cleaning + EDA + plots
├── tested.csv                       # input data
├── pyproject.toml                   # project metadata, deps
└── README.md
```

## Requirements

- Python >= 3.12
- Dependencies (see `pyproject.toml`): `pandas`, `matplotlib` (+ `numpy` used in code)

## Setup & run

Using [uv](https://docs.astral.sh/uv/):

```bash
uv sync
uv run python -m titanic_dataset
# or via entry point:
uv run titanic-dataset
```

With plain pip:

```bash
pip install pandas matplotlib numpy
python -m src.titanic_dataset
```

> Note: the script uses `matplotlib.use("TkAgg")` and calls `plt.show()`, so it needs a display backend. On headless servers, switch to `matplotlib.use("Agg")` and save figures with `plt.savefig()` instead.

Run from the project root so `pd.read_csv("tested.csv")` resolves.

## Example findings (on the bundled `tested.csv`)

- Best survival port: `Q` (~0.52) vs `C` (~0.39) vs `S` (~0.33); most passengers embarked at `S` (270).
- Fare drops sharply by class: mean Pclass 1 ≈ 94.3 vs Pclass 3 ≈ 12.5 (Δ ≈ 81.8).
- Travelling with family survives at ~0.51 vs alone at ~0.27 (Δ ≈ -0.24).
- Children have the highest age-group survival (~0.48).

Re-run the script to print exact tables to stdout.

## Author

Wright Gichana — `wrighgichana@gmail.com`
