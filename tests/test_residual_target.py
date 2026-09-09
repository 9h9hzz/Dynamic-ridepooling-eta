import pandas as pd

from src.features.residual_target import add_eta_residual, corrected_eta


def test_eta_residual_round_trip() -> None:
    frame = pd.DataFrame(
        {
            "realised_eta": [120.0, 210.0],
            "planned_total_eta_at_assign": [100.0, 180.0],
        }
    )
    result = add_eta_residual(frame)
    assert result["eta_residual"].tolist() == [20.0, 30.0]
    restored = corrected_eta(
        result["planned_total_eta_at_assign"], result["eta_residual"]
    )
    assert restored.tolist() == result["realised_eta"].tolist()

