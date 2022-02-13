#! /usr/bin/python3
"""
:file: visualise_bootstrap.py
:author: Hossam Khair
"""
import numpy as np
import matplotlib.pyplot as plt
from speed_confidence import least_squares, distances, times


def compute_resample_speeds(distances, times):
    num_resamples = 1000
    population_inds = np.arange(0, 99, dtype=int)
    resample_speeds = np.zeros(num_resamples)
    for nr in range(num_resamples):
        sample_inds = np.random.choice(population_inds, size=100, replace=True)
        sample_inds.sort()
        sample_distances = distances[sample_inds]
        sample_times = times[sample_inds]
        a0, a1 = least_squares(sample_times, sample_distances)
        resample_speeds[nr] = a1
    return resample_speeds


if __name__ == "__main__":
    # Create the bootstrap distribution of speeds
    resample_speeds = compute_resample_speeds(distances, times)
    speed_estimate = np.mean(resample_speeds)
    percentiles = np.percentile(resample_speeds, [5, 95])

    # Plot the histogram with the estimate and confidence interval
    fig, axis = plt.subplots()
    hist_bin_edges = np.linspace(0.0, 4.0, 21)
    axis.hist(resample_speeds, bins=hist_bin_edges,
              color='green', alpha=0.35, rwidth=0.8)
    axis.axvline(speed_estimate, label='Estimate', color='black')
    axis.axvline(percentiles[0], label=' 5th', color='blue')
    axis.axvline(percentiles[1], label='95th', color='blue')
    axis.legend()
    plt.show()
