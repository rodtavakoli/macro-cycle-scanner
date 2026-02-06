import pandas as pd

def extract_cyclic_episodes(
    df: pd.DataFrame,
    regime_col: str = "cyclic_regime",
    strength_col: str = "cycle_strength",
) -> pd.DataFrame:
    """
    Strict contiguous cyclic episodes.
    """
    work = df.copy().sort_index()
    work["episode_id"] = (
        work[regime_col].ne(work[regime_col].shift()).cumsum()
    )

    episodes = (
        work[work[regime_col] == "Cyclic"]
        .groupby("episode_id")
        .agg(
            start_date=(strength_col, lambda x: x.index.min()),
            end_date=(strength_col, lambda x: x.index.max()),
            duration_months=(strength_col, "count"),
            mean_strength=(strength_col, "mean"),
            max_strength=(strength_col, "max"),
        )
        .sort_values("duration_months", ascending=False)
    )

    episodes["duration_years"] = episodes["duration_months"] / 12
    return episodes
