#! /usr/bin/python3
"""
:file: hypothesis_test_non_std_stats.py
:author: Hossam Khair
"""
import numpy as np
from hypothesis_test_diff_means import donations_A, donations_B, reps

permuted_A_datasets = np.genfromtxt("permuted_A_datasets", delimiter=',')
permuted_B_datasets = np.genfromtxt("permuted_B_datasets", delimiter=',')

if __name__ == "__main__":
    # Calculate the difference in 80th percentile and median for each of the permuted datasets (A and B)
    samples_percentile = np.percentile(
        permuted_A_datasets, 80, axis=1) - np.percentile(permuted_B_datasets, 80, axis=1)
    samples_median = np.median(permuted_A_datasets, axis=1) - \
        np.median(permuted_B_datasets, axis=1)

    # Calculate the test statistic from the original dataset and corresponding p-values
    test_stat_percentile = np.percentile(
        donations_A, 80) - np.percentile(donations_B, 80)
    test_stat_median = np.median(donations_A) - np.median(donations_B)

    p_val_percentile = 2*np.sum(samples_percentile >=
                                np.abs(test_stat_percentile))/reps
    p_val_median = 2*np.sum(samples_median >= np.abs(test_stat_median))/reps

    print("80th Percentile: test statistic = {}, p-value = {}".format(
        test_stat_percentile, p_val_percentile))
    print("Median: test statistic = {}, p-value = {}".format(test_stat_median, p_val_median))
