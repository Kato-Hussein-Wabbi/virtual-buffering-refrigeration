# Analysis notebook

`virtual_buffering_analysis.ipynb` is the complete analysis for both temperature-input pathways. It validates and segments the three aligned datasets, constructs causal features, develops and selects the LSTM estimators, compares four reference estimators, and evaluates the locked models on the holdout and prospective datasets. Its final cells generate the reported tables, predictions, and figures in `outputs/publication/`.

Run the cells in order from a working directory inside this repository. The notebook locates its inputs by the repository folder structure, not by a particular computer's absolute path. Training requires TensorFlow and can take substantial time; the precomputed publication outputs and selected model artifacts are also included for inspection.
