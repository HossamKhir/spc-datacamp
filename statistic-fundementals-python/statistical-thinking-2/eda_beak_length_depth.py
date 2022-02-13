#! /usr/bin/python3
"""
:file: eda_beak_length_depth.py
:author: Hossam Khair
"""
import numpy as np
import matplotlib.pyplot as plt
from ecdf_beak_depth import bd_1975, bd_2012

bl_1975 = bl_2012 = bd_1975

if __name__ == "__main__":
    # Make scatter plot of 1975 data
    _ = plt.plot(bl_1975, bd_1975, marker='.',
                 linestyle='None', color="blue", alpha=.5)

    # Make scatter plot of 2012 data
    _ = plt.plot(bl_2012, bd_2012, marker='.',
                 linestyle='None', color="red", alpha=.5)

    # Label axes and make legend
    _ = plt.xlabel('beak length (mm)')
    _ = plt.ylabel('beak depth (mm)')
    _ = plt.legend(('1975', '2012'), loc='upper left')

    # Show the plot
    plt.show()
