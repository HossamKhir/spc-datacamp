#! /usr/bin/python3
"""
:file: beak_len2dep.py
:author: Hossam Khair
"""
import numpy as np
import matplotlib.pyplot as plt
from eda_beak_length_depth import bl_1975, bl_2012, bd_1975, bd_2012
from bootstrap_mean_variance import draw_bs_reps

if __name__ == "__main__":
    # Compute length-to-depth ratios
    ratio_1975 = bl_1975/bd_1975
    ratio_2012 = bl_2012/bd_2012

    # Compute means
    mean_ratio_1975 = np.mean(ratio_1975)
    mean_ratio_2012 = np.mean(ratio_2012)

    # Generate bootstrap replicates of the means
    bs_replicates_1975 = draw_bs_reps(ratio_1975, np.mean, 10**4)
    bs_replicates_2012 = draw_bs_reps(ratio_2012, np.mean, 10**4)

    # Compute the 99% confidence intervals
    conf_int_1975 = np.percentile(bs_replicates_1975, [.5, 99.5])
    conf_int_2012 = np.percentile(bs_replicates_2012, [.5, 99.5])

    # Print the results
    print('1975: mean ratio =', mean_ratio_1975,
          'conf int =', conf_int_1975)
    print('2012: mean ratio =', mean_ratio_2012,
          'conf int =', conf_int_2012)
