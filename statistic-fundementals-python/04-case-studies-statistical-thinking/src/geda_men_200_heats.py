#! /usr/bin/python3
"""
:file: geda_men_200_heats.py
:author: Hossam Khair
"""
import numpy as np
import dc_stat_think as dcst
import matplotlib.pyplot as plt

mens_200_free_heats = np.array([
    118.32, 107.73, 107., 106.39, 108.75, 117.74, 108.43, 111.96,
    114.36, 121.77, 108.23, 107.47, 118.41, 108.29, 106., 109.32,
    111.49, 112.92, 117.38, 110.95, 108.27, 111.78, 107.87, 110.77,
    109.05, 111., 108.77, 106.1, 106.61, 113.68, 108.2, 106.2,
    111.01, 109.25, 112., 118.55, 109.56, 108.18, 111.67, 108.09,
    110.04, 113.97, 109.91, 112.12, 111.65, 110.18, 116.36, 124.59,
    115.59, 121.01, 106.88, 108.96, 109.09, 108.67, 109.6, 111.85,
    118.54, 108.12, 124.38, 107.17, 107.48, 106.65, 106.91, 140.68,
    117.93, 120.66, 111.29, 107.1, 108.49, 112.43, 110.61, 110.38,
    109.87, 106.73, 107.18, 110.98, 108.55, 114.31, 112.05
])

if __name__ == "__main__":
    # Generate x and y values for ECDF: x, y
    x, y = dcst.ecdf(mens_200_free_heats)

    # Plot the ECDF as dots
    plt.plot(x, y, marker='.', linestyle='none')

    # Label axes and show plot
    plt.xlabel('time (s)')
    plt.ylabel('ECDF')
    plt.show()
