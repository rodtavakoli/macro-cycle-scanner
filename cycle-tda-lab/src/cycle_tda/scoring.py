import numpy as np
from .ph import max_h1_persistence


def cycle_strength_from_diagrams(dgms) -> float:
    """
    Extract scalar cycle strength from persistence diagrams.
    """
    dgm1 = dgms[1]
    return max_h1_persistence(dgm1)


def compare_to_noise(signal_score: float, noise_score: float) -> float:
    """
    Simple signal-to-noise ratio for PH loop strength.
    """
    if noise_score == 0:
        return float("inf")
    return signal_score / noise_score
