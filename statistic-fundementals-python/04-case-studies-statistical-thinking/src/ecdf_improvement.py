#! /usr/bin/python3
"""
:file: ecdf_improvement.py
:author: Hossam Khair
"""
import numpy as np
import dc_stat_think as dcst
import matplotlib.pyplot as plt

swimtime_low_lanes = np.array([
    24.66, 23.28, 27.2, 24.95, 32.34, 24.66, 26.17, 27.93, 23.35,
    22.93, 21.93, 28.33, 25.14, 25.19, 26.11, 31.31, 27.44, 21.85,
    27.48, 30.66, 21.74, 23.22, 27.93, 21.42, 24.79, 26.46
])

swimtime_high_lanes = np.array([
    24.62, 22.9, 27.05, 24.76, 30.31, 24.54, 26.12, 27.71, 23.15,
    23.11, 21.62, 28.02, 24.73, 24.95, 25.83, 30.61, 27.04, 21.67,
    27.16, 30.23, 21.51, 22.97, 28.05, 21.65, 24.54, 26.06
])

# Compute the fractional improvement of being in high lane: f
f = (swimtime_low_lanes - swimtime_high_lanes) / swimtime_low_lanes

# Make x and y values for ECDF: x, y
x, y = dcst.ecdf(f)

# Plot the ECDFs as dots
_ = plt.plot(x, y, marker='.', linestyle='none')

# Label the axes and show the plot
plt.xlabel("f")
plt.ylabel("ECDF")
plt.show()
