from src.simulation.rolling_horizon import run_rolling_horizon


def test_epochs_cover_requested_horizon() -> None:
    observed = []

    run_rolling_horizon(
        start_seconds=0,
        end_seconds=35,
        step_seconds=15,
        load_requests=lambda epoch: [epoch.start_seconds],
        make_decision=lambda epoch, requests: (epoch, requests),
        apply_decision=lambda epoch, decision: observed.append(
            (epoch.start_seconds, epoch.end_seconds, decision[1])
        ),
    )

    assert observed == [(0, 15, [0]), (15, 30, [15]), (30, 35, [30])]

