"""Minimal rolling-horizon control flow for a sanitized portfolio demo."""

from __future__ import annotations

from collections.abc import Callable, Iterable
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class DecisionEpoch:
    start_seconds: int
    end_seconds: int


def run_rolling_horizon(
    *,
    start_seconds: int,
    end_seconds: int,
    step_seconds: int,
    load_requests: Callable[[DecisionEpoch], Iterable[Any]],
    make_decision: Callable[[DecisionEpoch, list[Any]], Any],
    apply_decision: Callable[[DecisionEpoch, Any], None],
) -> None:
    """Execute repeated request loading, optimization, and state updates."""

    if step_seconds <= 0:
        raise ValueError("step_seconds must be positive")
    if end_seconds <= start_seconds:
        raise ValueError("end_seconds must be greater than start_seconds")

    for epoch_start in range(start_seconds, end_seconds, step_seconds):
        epoch = DecisionEpoch(
            start_seconds=epoch_start,
            end_seconds=min(epoch_start + step_seconds, end_seconds),
        )
        new_requests = list(load_requests(epoch))
        decision = make_decision(epoch, new_requests)
        apply_decision(epoch, decision)

