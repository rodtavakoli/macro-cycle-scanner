import numpy as np


def white_noise_like(y: np.ndarray, seed: int | None = None) -> np.ndarray:
    """
    Generate white noise with same length and variance as y.
    """
    rng = np.random.default_rng(seed)
    return rng.normal(loc=0.0, scale=np.std(y), size=len(y))
