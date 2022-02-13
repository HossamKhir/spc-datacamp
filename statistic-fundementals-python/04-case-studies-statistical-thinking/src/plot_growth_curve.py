#! /usr/bin/python3
"""
:file: plot_growth_curve.py
:author: Hossam Khair
"""
import numpy as np
import dc_stat_think as dcst
import matplotlib.pyplot as plt
from assess_growth_rate import t, bac_area, growth_rate_bs_reps, log_a0_bs_reps

if __name__ == "__main__":
    # Plot data points in a semilog-y plot with axis labeles
    _ = plt.semilogy(t, bac_area, marker='.', linestyle='none')

    # Generate x-values for the bootstrap lines: t_bs
    t_bs = np.array([0, 14])

    # Plot the first 100 bootstrap lines
    for i in range(100):
        y = np.exp(growth_rate_bs_reps[i] * t_bs + log_a0_bs_reps[i])
        _ = plt.semilogy(t_bs, y, linewidth=.5, alpha=.05, color='red')

    # Label axes and show plot
    _ = plt.xlabel('time (hr)')
    _ = plt.ylabel('area (sq. µm)')
    plt.show()
