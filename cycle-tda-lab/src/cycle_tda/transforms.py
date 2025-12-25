import numpy as np
import pandas as pd


def log_price(series: pd.Series) -> pd.Series:
    return np.log(series)


def log_returns(series: pd.Series) -> pd.Series:
    return np.log(series).diff()


def zscore(series: pd.Series) -> pd.Series:
    return (series - series.mean()) / series.std(ddof=0)


def rolling_zscore(series: pd.Series, window: int) -> pd.Series:
    mean = series.rolling(window).mean()
    std = series.rolling(window).std(ddof=0)
    return (series - mean) / std
