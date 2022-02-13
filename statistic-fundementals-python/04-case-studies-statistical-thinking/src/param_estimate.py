#! /usr/bin/python3
"""
:file: param_estimate.py
:author: Hossam Khair
"""
import numpy as np
import dc_stat_think as dcst
import matplotlib.pyplot as plt
from eda_active_bout_len import bout_lengths_mut, bout_lengths_wt


if __name__ == "__main__":
    # pass
    # Compute mean active bout length
    mean_wt = np.mean(bout_lengths_wt)
    mean_mut = np.mean(bout_lengths_mut)

    # Draw bootstrap replicates
    bs_reps_wt = dcst.draw_bs_reps(bout_lengths_wt, np.mean, size=10**4)
    bs_reps_mut = dcst.draw_bs_reps(bout_lengths_mut, np.mean, size=10**4)

    # Compute 95% confidence intervals
    conf_int_wt = np.percentile(bs_reps_wt, [2.5, 97.5])
    conf_int_mut = np.percentile(bs_reps_mut, [2.5, 97.5])

    # Print the results
    print("""
    wt:  mean = {0:.3f} min., conf. int. = [{1:.1f}, {2:.1f}] min.
    mut: mean = {3:.3f} min., conf. int. = [{4:.1f}, {5:.1f}] min.
    """.format(mean_wt, *conf_int_wt, mean_mut, *conf_int_mut))
