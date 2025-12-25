import pandas as pd
from pathlib import Path

# ===============================
# Configuration
# ===============================

DATA_DIR = Path("data/raw")
DATA_DIR.mkdir(parents=True, exist_ok=True)

FRED_SERIES = {
    "CPI_Monthly.csv": {
        "url": "https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL",
        "value_col": "CPI"
    },
    "M2_Monthly.csv": {
        "url": "https://fred.stlouisfed.org/graph/fredgraph.csv?id=M2SL",
        "value_col": "M2"
    },
    "FEDFUNDS_Monthly.csv": {
        "url": "https://fred.stlouisfed.org/graph/fredgraph.csv?id=FEDFUNDS",
        "value_col": "FedFunds"
    }
}

# ===============================
# Download + Clean
# ===============================

def download_and_clean(name, cfg):
    print(f"Downloading {name}...")

    df = pd.read_csv(cfg["url"])
    df.columns = ["Date", cfg["value_col"]]

    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df[cfg["value_col"]] = pd.to_numeric(df[cfg["value_col"]], errors="coerce")

    df = df.dropna().sort_values("Date")

    out_path = DATA_DIR / name
    df.to_csv(out_path, index=False)

    print(f"Saved → {out_path}")
    print(f"Rows: {len(df)} | Date range: {df['Date'].min().date()} → {df['Date'].max().date()}")
    print("-" * 50)


def main():
    for name, cfg in FRED_SERIES.items():
        download_and_clean(name, cfg)

    print("All FRED macro CSVs downloaded successfully.")


if __name__ == "__main__":
    main()
