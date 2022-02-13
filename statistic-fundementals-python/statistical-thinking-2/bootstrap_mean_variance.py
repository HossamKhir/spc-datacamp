#! /usr/bin/python3
"""
:file: 
:author: Hossam Khair
"""
import numpy as np
import matplotlib.pyplot as plt


def bootstrap_replicate_1d(data, func):
    """Generate bootstrap replicate of 1D data."""
    bs_sample = np.random.choice(data, len(data))
    return func(bs_sample)


def draw_bs_reps(data, func, size=1):
    """Draw bootstrap replicates."""

    # Initialize array of replicates: bs_replicates
    bs_replicates = np.empty(size)

    # Generate replicates
    for i in range(size):
        bs_replicates[i] = bootstrap_replicate_1d(data, func)

    return bs_replicates


rainfall = np.array([])


if __name__ == "__main__":
    # Take 10,000 bootstrap replicates of the mean: bs_replicates
    bs_replicates = draw_bs_reps(rainfall, np.mean, 10**4)

    # Compute and print SEM
    sem = np.std(rainfall) / np.sqrt(len(rainfall))
    print(sem)

    # Compute and print standard deviation of bootstrap replicates
    bs_std = np.std(bs_replicates)
    print(bs_std)

    # Make a histogram of the results
    _ = plt.hist(bs_replicates, bins=50, normed=True)
    _ = plt.xlabel('mean annual rainfall (mm)')
    _ = plt.ylabel('PDF')

    # Show the plot
    plt.show()

    # Generate 10,000 bootstrap replicates of the variance: bs_replicates
    bs_replicates = draw_bs_reps(rainfall, np.var, 10**4)

    # Put the variance in units of square centimeters
    bs_replicates /= 100

    # Make a histogram of the results
    _ = plt.hist(bs_replicates, normed=True, bins=50)
    _ = plt.xlabel('variance of annual rainfall (sq. cm)')
    _ = plt.ylabel('PDF')

    # Show the plot
    plt.show()
