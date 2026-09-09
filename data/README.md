# Data policy

The research data are not included in this portfolio edition.

The private workspace contains large road-network lookup matrices, request streams, vehicle configurations, generated passenger-level records, and prediction artifacts. These files may be licensed, identifying, too large for Git, or sufficient to reproduce results that remain under review.

If a runnable public demo is needed, add a small synthetic dataset under `data/sample/` with fields such as:

```text
request_id, vehicle_id, planned_total_eta_at_assign, realised_eta,
waiting_slack_at_assign, delay_slack_at_assign, available_seats,
passenger_count, instantaneous_shareability_score
```

Do not derive the sample by copying real rows. Generate artificial values and label them clearly as synthetic.

