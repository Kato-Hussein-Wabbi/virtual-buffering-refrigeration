# Analysis datasets

The notebook reads the Excel workbooks; CSV copies of the same aligned observations are provided in an open format. All temperatures are in degrees Celsius and the observations are nominally one minute apart. Gaps between continuous segments are retained in the time stamps.

| File stem | Role | Observations |
|---|---|---:|
| `development_dataset` | Training and validation, including model selection | 280,571 |
| `holdout_dataset` | Independent holdout evaluation | 26,810 |
| `prospective_challenge_dataset` | Separately collected operational-challenge evaluation | 2,844 |

Each file has the same five columns:

| Column | Meaning |
|---|---|
| `Time_stamp` | Recorded observation time. |
| `P1` | Glycol-buffered reference temperature ($T_{\mathrm{P1}}$). |
| `CEN_C` | BME280 air-temperature input ($T_{280}$). |
| `fridge_current_C` | Refrigerator-reported temperature acquired through BLE ($T_{\mathrm{BLE}}$). |
| `fridge_set_C` | Refrigerator setpoint, retained as experimental context but not used as a model input. |

These files are analysis-ready, aligned data rather than original device logs. The notebook checks column names, missing and duplicate observations, timestamp overlap between datasets, and continuous-segment boundaries before modelling.
