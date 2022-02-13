#! /usr/bin/python3
"""
:file: jackknife_median.py
:author: Hossam Khair
"""
import numpy as np
from jackknife_mean import wrench_lengths, index, n

if __name__ == "__main__":
    # Leave one observation out to get the jackknife sample and store the median length
    median_lengths = []
    for i in range(n):
        jk_sample = wrench_lengths[index != i]
        median_lengths.append(np.median(jk_sample))

    median_lengths = np.array(median_lengths)

    # Calculate jackknife estimate and it's variance
    jk_median_length = np.mean(median_lengths)
    jk_var = (n-1)*np.var(median_lengths)

    # Assuming normality, calculate lower and upper 95% confidence intervals
    jk_lower_ci = jk_median_length - 1.96*np.sqrt(jk_var)
    jk_upper_ci = jk_median_length + 1.96*np.sqrt(jk_var)
    print("Jackknife 95% CI lower = {}, upper = {}".format(
        jk_lower_ci, jk_upper_ci))
