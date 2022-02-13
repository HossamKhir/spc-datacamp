#! /usr/bin/python3
"""
:file: current_effect_lane_pos.py
:author: Hossam Khair
"""
import numpy as np
import dc_stat_think as dcst
import matplotlib.pyplot as plt
from eda_mean_diff_even_odd import lanes, f_13

if __name__ == "__main__":
    # Compute the slope and intercept of the frac diff/lane curve
    slope, intercept = np.polyfit(lanes, f_13, 1)

    # Compute bootstrap replicates
    bs_reps_slope, bs_reps_int = dcst.draw_bs_pairs_linreg(lanes, f_13, 10**4)

    # Compute 95% confidence interval of slope
    conf_int = np.percentile(bs_reps_slope, [2.5, 97.5])

    # Print slope and confidence interval
    print("""
    slope: {0:.5f} per lane
    95% conf int: [{1:.5f}, {2:.5f}] per lane""".format(slope, *conf_int))

    # x-values for plotting regression lines
    x = np.array([1, 8])

    # Plot 100 bootstrap replicate lines
    for i in range(100):
        _ = plt.plot(x, bs_reps_slope[i] * x + bs_reps_int[i],
                     color='red', alpha=0.2, linewidth=0.5)

    # Update the plot
    plt.draw()
    plt.show()
