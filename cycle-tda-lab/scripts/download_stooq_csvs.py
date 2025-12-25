import pandas as pd
from pathlib import Path

# ===============================
# Configuration
# ===============================

DATA_DIR = Path("data/raw")
DATA_DIR.mkdir(parents=True, exist_ok=True)

STOOQ_ASSETS = {
    "XAU_Monthly.csv": {
        "url": "https://stooq.com/q/d/l/?s=xauusd&i=m",
        "price_col": "Close",
    },
    "XAG_Monthly.csv": {
        "url": "https://stooq.com/q/d/l/?s=xagusd&i=m",
        "price_col": "Close",
    },
}

# ===============================
# Download + Clean
# ===============================

def download_and_clean(name, cfg):
    print(f"Downloading {name}...")

    df = pd.read_csv(cfg["url"])
    df.columns = [c.capitalize() for c in df.columns]

    # Parse date
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    # Keep only what we need
    df = df[["Date", cfg["price_col"]]].rename(
        columns={cfg["price_col"]: "Close"}
    )

    # Sort and drop invalid rows
    df = df.dropna(subset=["Date", "Close"]).sort_values("Date")

    out_path = DATA_DIR / name
    df.to_csv(out_path, index=False)

    print(f"Saved → {out_path}")
    print(f"Rows: {len(df)} | Date range: {df['Date'].min().date()} → {df['Date'].max().date()}")
    print("-" * 50)


def main():
    for name, cfg in STOOQ_ASSETS.items():
        download_and_clean(name, cfg)

    print("All STOOQ CSVs downloaded successfully.")


if __name__ == "__main__":
    main()
