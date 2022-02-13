#! /usr/bin/python3
"""
:file: 
:author: Hossam Khair
"""
import numpy as np
import matplotlib.pyplot as plt
from bootstrap_mean_variance import draw_bs_reps

nohitter_times = np.array([])

if __name__ == "__main__":
    # Draw bootstrap replicates of the mean no-hitter time (equal to tau): bs_replicates
    bs_replicates = draw_bs_reps(nohitter_times, np.mean, 10**4)

    # Compute the 95% confidence interval: conf_int
    conf_int = np.percentile(a=bs_replicates, q=[2.5, 97.5])

    # Print the confidence interval
    print('95% confidence interval =', conf_int, 'games')

    # Plot the histogram of the replicates
    _ = plt.hist(bs_replicates, bins=50, normed=True)
    _ = plt.xlabel(r'$\tau$ (games)')
    _ = plt.ylabel('PDF')

    # Show the plot
    plt.show()
