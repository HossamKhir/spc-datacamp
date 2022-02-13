#! /usr/bin/python3
"""
:file: eda_mean_diff_even_odd.py
:author: Hossam Khair
"""
import numpy as np
import dc_stat_think as dcst
import matplotlib.pyplot as plt

lanes = np.array([y for y in range(1, 9)])
f_13 = np.array([
    -0.01562214, -0.0146381, -0.00977673, -0.00525713,  0.00204104,
    0.00381014,  0.0075664,  0.01525869
])
f_15 = np.array([
    -0.00516018, -0.00392952, -0.00099284,  0.00059953, -0.002424,
    -0.00451099,  0.00047467,  0.00081962
])

if __name__ == "__main__":
    # Plot the the fractional difference for 2013 and 2015
    _ = plt.plot(lanes, f_13, marker='.', markersize=12, linestyle='none')
    _ = plt.plot(lanes, f_15, marker='.', markersize=12, linestyle='none')

    # Add a legend
    _ = plt.legend((2013, 2015))

    # Label axes and show plot
    plt.xlabel("lane")
    plt.ylabel("frac. diff. (odd - even)")
    plt.show()
