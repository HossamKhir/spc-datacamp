#! /usr/bin/python3
"""
:file: correlation_offspring_parent.py
:author: Hossam Khair
"""
import numpy as np
import matplotlib.pyplot as plt
from covariance import pearson_r
from eda_heritability import bd_parent_scandens, bd_offspring_fortis, bd_offspring_scandens, bd_parent_fortis


def draw_bs_pairs(x, y, func, size=1):
    """Perform pairs bootstrap for a single statistic."""

    # Set up array of indices to sample from: inds
    inds = np.arange(len(x))

    # Initialize replicates: bs_replicates
    bs_replicates = np.empty(size)

    # Generate replicates
    for i in range(size):
        bs_inds = np.random.choice(inds, size=len(inds))
        bs_x, bs_y = x[bs_inds], y[bs_inds]
        bs_replicates[i] = func(bs_x, bs_y)

    return bs_replicates


if __name__ == "__main__":
    # Compute the Pearson correlation coefficients
    r_scandens = pearson_r(bd_parent_scandens, bd_offspring_scandens)
    r_fortis = pearson_r(bd_parent_fortis, bd_offspring_fortis)

    # Acquire 1000 bootstrap replicates of Pearson r
    bs_replicates_scandens = draw_bs_pairs(
        bd_parent_scandens, bd_offspring_scandens, pearson_r, 1000)

    bs_replicates_fortis = draw_bs_pairs(
        bd_parent_fortis, bd_offspring_fortis, pearson_r, 1000)

    # Compute 95% confidence intervals
    conf_int_scandens = np.percentile(bs_replicates_scandens, [2.5, 97.5])
    conf_int_fortis = np.percentile(bs_replicates_fortis, [2.5, 97.5])

    # Print results
    print('G. scandens:', r_scandens, conf_int_scandens)
    print('G. fortis:', r_fortis, conf_int_fortis)
