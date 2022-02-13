#! /usr/bin/python3
"""
:file: linreg_av_split_time.py
:author: Hossam Khair
"""
import numpy as np
import dc_stat_think as dcst
import matplotlib.pyplot as plt
from eda_all_data import split_number, mean_splits

if __name__ == "__main__":
    # Perform regression
    slowdown, split_3 = np.polyfit(split_number, mean_splits, 1)

    # Compute pairs bootstrap
    bs_reps, _ = dcst.draw_bs_pairs_linreg(
        split_number, mean_splits, size=10**4)

    # Compute confidence interval
    conf_int = np.percentile(bs_reps, [2.5, 97.5])

    # Plot the data with regressions line
    _ = plt.plot(split_number, mean_splits, marker='.', linestyle='none')
    _ = plt.plot(split_number, slowdown * split_number + split_3, '-')

    # Label axes and show plot
    _ = plt.xlabel('split number')
    _ = plt.ylabel('split time (s)')
    plt.show()

    # Print the slowdown per split
    print("""
    mean slowdown: {0:.3f} sec./split
    95% conf int of mean slowdown: [{1:.3f}, {2:.3f}] sec./split""".format(
        slowdown, *conf_int))
