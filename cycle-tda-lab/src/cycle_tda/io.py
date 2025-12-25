import pandas as pd
from pathlib import Path


def load_csv(
    path: str | Path,
    date_col: str = "Date",
    value_col: str | None = None,
) -> pd.DataFrame:
    """
    Load a CSV with a date column, sorted by date.
    """
    df = pd.read_csv(path, parse_dates=[date_col])
    df = df.sort_values(date_col).reset_index(drop=True)

    if value_col is not None:
        df = df[[date_col, value_col]].dropna()

    return df


def save_features(
    df: pd.DataFrame,
    path: str | Path,
    index: bool = False,
) -> None:
    """
    Save features to CSV (Power BI friendly).
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=index)
