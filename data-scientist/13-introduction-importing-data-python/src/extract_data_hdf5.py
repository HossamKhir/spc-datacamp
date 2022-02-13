#! /usr/bin/python3
"""
"""
import numpy as np
import matplotlib.pyplot as plt
from import_hdf5 import data

if __name__ == "__main__":
    # Get the HDF5 group: group
    group = data["strain"]

    # Check out keys of group
    for key in group.keys():
        print(key)

    # Set variable equal to time series data: strain
    strain = data["strain"]["Strain"][()]

    # Set number of time points to sample: num_samples
    num_samples = 10_000

    # Set time vector
    time = np.arange(0, 1, 1 / num_samples)

    # Plot data
    plt.plot(time, strain[:num_samples])
    plt.xlabel("GPS Time (s)")
    plt.ylabel("strain")
    plt.show()
