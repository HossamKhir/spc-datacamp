#! /usr/bin/python3
"""
:file: ecdf_beak_depth.py
:author: Hossam Khair
"""
import numpy as np
import matplotlib.pyplot as plt
from ecdf import ecdf

bd_1975 = bd_2012 = np.array([])

if __name__ == "__main__":
    # Compute ECDFs
    x_1975, y_1975 = ecdf(bd_1975)
    x_2012, y_2012 = ecdf(bd_2012)

    # Plot the ECDFs
    _ = plt.plot(x_1975, y_1975, marker='.', linestyle='none')
    _ = plt.plot(x_2012, y_2012, marker='.', linestyle='none')

    # Set margins
    plt.margins(.02)

    # Add axis labels and legend
    _ = plt.xlabel('beak depth (mm)')
    _ = plt.ylabel('ECDF')
    _ = plt.legend(('1975', '2012'), loc='lower right')

    # Show the plot
    plt.show()
