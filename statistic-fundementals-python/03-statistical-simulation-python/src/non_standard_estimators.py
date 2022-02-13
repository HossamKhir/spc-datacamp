#! /usr/bin/python3
"""
:file: non_standard_estimators.py
:author: Hossam Khair
"""
import os
import numpy as np
import pandas as pd

DATA_PATH = "../data/raw"

df = pd.read_csv(os.path.join(DATA_PATH, "dataframe_hw.csv"), sep=",")

if __name__ == "__main__":
    # Sample with replacement and calculate quantities of interest
    sims, data_size, height_medians, hw_corr = 1000, df.shape[0], [], []
    for i in range(sims):
        tmp_df = df.sample(n=data_size, replace=True)
        height_medians.append(tmp_df.heights.median())
        hw_corr.append(tmp_df.weights.corr(tmp_df.heights))

    # Calculate confidence intervals
    height_median_ci = np.percentile(height_medians, [2.5, 97.5])
    height_weight_corr_ci = np.percentile(hw_corr, [2.5, 97.5])
    print(
        "Height Median CI = {} \nHeight Weight Correlation CI = {}".format(
            height_median_ci, height_weight_corr_ci
        )
    )
