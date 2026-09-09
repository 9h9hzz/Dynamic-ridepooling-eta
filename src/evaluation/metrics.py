"""Small evaluation helpers for ETA residual predictions."""

from __future__ import annotations

import numpy as np


def residual_metrics(actual: np.ndarray, predicted: np.ndarray) -> dict[str, float]:
    actual = np.asarray(actual, dtype=float)
    predicted = np.asarray(predicted, dtype=float)
    if actual.shape != predicted.shape:
        raise ValueError("actual and predicted must have the same shape")
    error = predicted - actual
    return {
        "mae_seconds": float(np.mean(np.abs(error))),
        "rmse_seconds": float(np.sqrt(np.mean(error**2))),
        "coverage_within_30_seconds": float(np.mean(np.abs(error) <= 30.0)),
        "coverage_within_60_seconds": float(np.mean(np.abs(error) <= 60.0)),
    }

