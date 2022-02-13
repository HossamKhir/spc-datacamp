#! /usr/bin/python3
"""
:file: param_estimate_finals_semi.py
:author: Hossam Khair
"""
import numpy as np
import dc_stat_think as dcst
import matplotlib.pyplot as plt

from eda_finals_semi import f

if __name__ == "__main__":
    # Mean fractional time difference: f_mean
    f_mean = np.mean(f)

    # Get bootstrap reps of mean: bs_reps
    bs_reps = dcst.draw_bs_reps(f, np.mean, size=10**4)

    # Compute confidence intervals: conf_int
    conf_int = np.percentile(bs_reps, [2.5, 97.5])

    # Report
    print("""
    mean frac. diff.: {0:.5f}
    95% conf int of mean frac. diff.: [{1:.5f}, {2:.5f}]""".format(f_mean, *conf_int))
