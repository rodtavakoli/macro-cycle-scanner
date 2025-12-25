import pandas as pd

from .rolling import rolling_ph
from .transforms import log_price, log_returns


def run_cycle_ph_experiment(
    series: pd.Series,
    cycle_months: int,
    m: int,
    tau: int,
):
    """
    Run cycle-aware rolling PH for both log price and log returns.
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

        df_roll["representation"] = rep_name
        results.append(df_roll.reset_index())

    return pd.concat(results, ignore_index=True)
