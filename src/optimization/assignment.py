"""Generic trip-vehicle assignment model used for the public portfolio.

The research system first generates feasible candidate trips. This module only
shows the conflict-free selection layer; route insertion and feasibility checks
remain outside the public release.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class CandidateTrip:
    """A feasible candidate generated before optimization."""

    candidate_id: str
    vehicle_id: str
    request_ids: tuple[str, ...]
    assignment_value: float


def solve_assignment(candidates: Iterable[CandidateTrip]) -> list[CandidateTrip]:
    """Select a maximum-value, conflict-free set of candidate trips.

    Each vehicle receives at most one trip and each request is served at most
    once. Unserved-request penalties and production routing constraints are
    intentionally omitted from this publication-safe example.
    """

    try:
        import gurobipy as gp
        from gurobipy import GRB
    except ImportError as exc:  # pragma: no cover - depends on local install
        raise RuntimeError("Install gurobipy to solve the assignment model.") from exc

    items = list(candidates)
    if not items:
        return []

    model = gp.Model("portfolio_trip_vehicle_assignment")
    model.Params.OutputFlag = 0
    choose = {
        item.candidate_id: model.addVar(vtype=GRB.BINARY, name=f"choose_{item.candidate_id}")
        for item in items
    }

    model.setObjective(
        gp.quicksum(item.assignment_value * choose[item.candidate_id] for item in items),
        GRB.MAXIMIZE,
    )

    vehicle_ids = sorted({item.vehicle_id for item in items})
    for vehicle_id in vehicle_ids:
        model.addConstr(
            gp.quicksum(
                choose[item.candidate_id]
                for item in items
                if item.vehicle_id == vehicle_id
            )
            <= 1,
            name=f"one_trip_per_vehicle_{vehicle_id}",
        )

    request_ids = sorted({request_id for item in items for request_id in item.request_ids})
    for request_id in request_ids:
        model.addConstr(
            gp.quicksum(
                choose[item.candidate_id]
                for item in items
                if request_id in item.request_ids
            )
            <= 1,
            name=f"serve_request_once_{request_id}",
        )

    model.optimize()
    if model.Status != GRB.OPTIMAL:
        raise RuntimeError(f"Assignment model did not solve to optimality: {model.Status}")

    return [item for item in items if choose[item.candidate_id].X > 0.5]
