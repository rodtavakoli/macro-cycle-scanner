import pandas as pd

from ..cycle_tda.rolling import rolling_ph
from ..cycle_tda.transforms import log_price, log_returns


def run_cycle_ph_experiment(
    series: pd.Series,
    cycle_id: str,
    cycle_years: float,
    cycle_months: int,
    cycle_family: str,
    m: int,
    tau: int,
):
    """
    Run cycle-aware rolling PH for both log price and log returns.

    Returns a DataFrame with explicit cycle metadata attached.
    """
    results = []

    reps = {
        "log_price": log_price(series),
        "log_returns": log_returns(series),
    }

    for rep_name, rep_series in reps.items():
        rep_series = rep_series.dropna()

        df_roll = rolling_ph(
            series=rep_series,
            window=cycle_months,
            m=m,
            tau=tau,
        )

        df_roll = df_roll.reset_index()
        df_roll["representation"] = rep_name
        df_roll["cycle_id"] = cycle_id
        df_roll["cycle_years"] = cycle_years
        df_roll["cycle_months"] = cycle_months
        df_roll["cycle_family"] = cycle_family

        results.append(df_roll)

    return pd.concat(results, ignore_index=True)
