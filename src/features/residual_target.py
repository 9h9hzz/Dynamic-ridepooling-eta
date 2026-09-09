"""Leakage-safe ETA residual target construction."""

from __future__ import annotations

import pandas as pd


def add_eta_residual(
    frame: pd.DataFrame,
    *,
    realised_eta_column: str = "realised_eta",
    planned_eta_column: str = "planned_total_eta_at_assign",
    output_column: str = "eta_residual",
) -> pd.DataFrame:
    """Return a copy with realised ETA minus assignment-time planned ETA."""

    missing = {realised_eta_column, planned_eta_column} - set(frame.columns)
    if missing:
        raise KeyError(f"Missing required columns: {sorted(missing)}")

    result = frame.copy()
    result[output_column] = (
        pd.to_numeric(result[realised_eta_column], errors="raise")
        - pd.to_numeric(result[planned_eta_column], errors="raise")
    )
    return result


def corrected_eta(planned_eta: pd.Series, predicted_residual: pd.Series) -> pd.Series:
    """Convert a predicted residual back into a drop-off ETA estimate."""

    return planned_eta + predicted_residual

