import pandas as pd
from pathlib import Path

# ============================================================
# Project paths
# ============================================================
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data" / "raw"
DATA_DIR.mkdir(parents=True, exist_ok=True)

print("Writing FRED data to:", DATA_DIR.resolve())

# ============================================================
# Confidence Proxy Universe (core + a few extras)
# ============================================================
FRED_SERIES = {
    # --- Rates / curve components ---
    "DGS10_Monthly.csv": {"id": "DGS10", "col": "y10"},
    "DGS2_Monthly.csv": {"id": "DGS2", "col": "y2"},
    "FEDFUNDS_Monthly.csv": {"id": "FEDFUNDS", "col": "fedfunds"},

    # --- Inflation / liquidity ---
    "CPI_Monthly.csv": {"id": "CPIAUCSL", "col": "cpi"},
    "M2_Monthly.csv": {"id": "M2SL", "col": "m2"},

    # --- Dollar / global USD pressure proxy ---
    # Broad trade-weighted dollar index
    "DTWEXBGS_Monthly.csv": {"id": "DTWEXBGS", "col": "dxy"},

    # --- Risk / volatility ---
    "VIX_Monthly.csv": {"id": "VIXCLS", "col": "vix"},

    # --- Credit stress (pick both; we’ll compute spreads) ---
    "BAA_Monthly.csv": {"id": "BAA", "col": "baa"},
    "AAA_Monthly.csv": {"id": "AAA", "col": "aaa"},
    # Optional: High-yield option-adjusted spread (more “risk”)
    "HY_OAS_Monthly.csv": {"id": "BAMLH0A0HYM2", "col": "hy_oas"},

    # --- Equities (confidence / risk appetite proxy) ---
    "SP500_Monthly.csv": {"id": "SP500", "col": "sp500"},

    # --- Real economy (optional, useful later) ---
    "UNRATE_Monthly.csv": {"id": "UNRATE", "col": "unrate"},
    "INDPRO_Monthly.csv": {"id": "INDPRO", "col": "indpro"},
}

def fetch_fred(series_id: str) -> pd.DataFrame:
    url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={series_id}"
    return pd.read_csv(url)

def clean_to_monthly(df: pd.DataFrame, col: str) -> pd.DataFrame:
    df.columns = ["date", col]
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df[col] = pd.to_numeric(df[col], errors="coerce")

    df = (
        df.dropna()
          .set_index("date")
          .resample("M")
          .last()
          .dropna()
          .reset_index()
    )
    return df

def main():
    for fname, cfg in FRED_SERIES.items():
        print(f"Downloading {fname} ({cfg['id']})...")
        raw = fetch_fred(cfg["id"])
        out_df = clean_to_monthly(raw, cfg["col"])

        out_path = DATA_DIR / fname
        out_df.to_csv(out_path, index=False)

        print(
            f"Saved → {fname} | {out_df['date'].min().date()} → {out_df['date'].max().date()} | {len(out_df)} rows"
        )
        print("-" * 72)

    print("✓ All FRED series downloaded")

if __name__ == "__main__":
    main()
