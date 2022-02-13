#! /usr/bin/python3
"""
:file: k_s_stat.py
:author: Hossam Khair
"""
import numpy as np
import dc_stat_think as dcst
import matplotlib.pyplot as plt


def ks_stat(data1, data2):
    # Compute ECDF from data: x, y
    x, y = dcst.ecdf(data1)

    # Compute corresponding values of the target CDF
    cdf = dcst.ecdf_formal(x, data2)

    # Compute distances between concave corners and CDF
    D_top = cdf - y

    # Compute distance between convex corners and CDF
    D_bottom = cdf - y + 1/len(data1)

    return np.max((D_top, D_bottom))


def draw_ks_reps(n, f, args=(), size=10**4, n_reps=10**4):
    # Generate samples from target distribution
    x_f = f(*args, size=size)

    # Initialize K-S replicates
    reps = np.empty(n_reps)

    # Draw replicates
    for i in range(n_reps):
        # Draw samples for comparison
        x_samp = f(*args, size=n)

        # Compute K-S statistic
        reps[i] = dcst.ks_stat(x_samp, x_f)

    return reps


if __name__ == "__main__":
    pass
