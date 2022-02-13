#! /usr/bin/python3
"""
:file: neonicotinoid.py
:author: Hossam Khair
"""
import numpy as np
import matplotlib.pyplot as plt
from ecdf import ecdf
from bootstrap_mean_variance import draw_bs_reps

control = treated = np.array([])

if __name__ == "__main__":
    # Compute x,y values for ECDFs
    x_control, y_control = ecdf(control)
    x_treated, y_treated = ecdf(treated)

    # Plot the ECDFs
    plt.plot(x_control, y_control, marker='.', linestyle='none')
    plt.plot(x_treated, y_treated, marker='.', linestyle='none')

    # Set the margins
    plt.margins(0.02)

    # Add a legend
    plt.legend(('control', 'treated'), loc='lower right')

    # Label axes and show plot
    plt.xlabel('millions of alive sperm per mL')
    plt.ylabel('ECDF')
    plt.show()

    # Compute the difference in mean sperm count: diff_means
    diff_means = np.mean(control) - np.mean(treated)

    # Compute mean of pooled data: mean_count
    mean_count = np.mean(np.concatenate((control, treated)))

    # Generate shifted data sets
    control_shifted = control - np.mean(control) + mean_count
    treated_shifted = treated - np.mean(treated) + mean_count

    # Generate bootstrap replicates
    bs_reps_control = draw_bs_reps(control_shifted,
                                   np.mean, size=10000)
    bs_reps_treated = draw_bs_reps(treated_shifted,
                                   np.mean, size=10000)

    # Get replicates of difference of means: bs_replicates
    bs_replicates = bs_reps_control - bs_reps_treated

    # Compute and print p-value: p
    p = np.sum(bs_replicates >= np.mean(control) - np.mean(treated)) \
        / len(bs_replicates)
    print('p-value =', p)
