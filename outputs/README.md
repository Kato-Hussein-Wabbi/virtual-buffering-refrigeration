# Reported outputs

`publication/` holds the predictions, numbered source tables, and final manuscript and supplementary figures used for reporting. Figures are available as vector PDFs and 600-dpi PNGs. Prediction and table CSV files provide machine-readable values.

`models/` holds the selected LSTM checkpoints, feature and target scalers, reference-estimator artifacts, and training histories for each input pathway. These files document the fitted estimators; a full notebook rerun trains new models from the development dataset.

The notebook creates additional diagnostics and intermediate predictions under `run_artifacts/` when executed. That generated directory is intentionally excluded from version control because the inputs and notebook are provided to regenerate it.
