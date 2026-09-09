# Public figures

Only manually cleared figures intended for portfolio use belong in this directory.

## Representative result

The current portfolio includes one representative result figure showing reconstructed drop-off ETA performance.

<img width="1452" height="1276" alt="heatmap_test_pred_vs_actual_trip_time_5s" src="https://github.com/user-attachments/assets/4fdaeca1-342e-485e-91ce-6b661fcd1979" />

**Reconstructed drop-off ETA performance.**  
The model does not predict total trip time directly. It predicts the post-assignment ETA residual, defined as the difference between the realised drop-off ETA and the planner ETA available at assignment.

The final ETA prediction is reconstructed as:

`predicted ETA = assignment-time planned ETA + predicted residual`

The close alignment between predicted and realised trip times indicates that the reconstructed predictions preserve the overall trip-time scale.

The primary research task remains the prediction of post-assignment ETA deviations caused by subsequent ridepooling assignments and route revisions.

## Release policy

Only figures that have been manually reviewed and approved for public portfolio use should be stored here.

Approved PNG files should use filenames beginning with `public-`. Other PNG files are blocked by `.gitignore` by default to reduce the risk of unintentionally releasing manuscript figures or unpublished results.
