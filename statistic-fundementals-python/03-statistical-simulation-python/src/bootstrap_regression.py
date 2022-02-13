#! /usr/bin/python3
"""
:file: bootstrap_regression.py
:author: Hossam Khair
"""
import os
import numpy as np
import statsmodels.api as sm
import pandas as pd

DATA_PATH = "../data/raw"

df = pd.read_csv(os.path.join(DATA_PATH, "dataframe_regress.csv"), sep=",")

if __name__ == "__main__":
    rsquared_boot, coefs_boot, sims = [], [], 1000
    reg_fit = sm.OLS(df["y"], df.iloc[:, 1:]).fit()

    # Run 1K iterations
    for i in range(sims):
        # First create a bootstrap sample with replacement with n=df.shape[0]
        bootstrap = df.sample(replace=True, n=df.shape[0])
        # Fit the regression and append the r square to rsquared_boot
        rsquared_boot.append(
            sm.OLS(bootstrap["y"], bootstrap.iloc[:, 1:]).fit().rsquared
        )

    # Calculate 95% CI on rsquared_boot
    r_sq_95_ci = np.percentile(rsquared_boot, [2.5, 97.5])
    print("R Squared 95% CI = {}".format(r_sq_95_ci))
