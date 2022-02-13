#! /usr/bin/python3
"""
:file: binomial.py
:author: Hossam Khair
"""
import numpy as np
import matplotlib.pyplot as plt
from ecdf import ecdf

np.random.seed(42)

if __name__ == "__main__":
    # Take 10,000 samples out of the binomial distribution: n_defaults
    n_defaults = np.random.binomial(n=100, p=0.05, size=10000)

    # Compute CDF: x, y
    x, y = ecdf(n_defaults)

    # Plot the CDF with axis labels
    plt.plot(x, y, marker='.', linestyle="none")
    plt.xlabel("defaults out of 100 loans")
    plt.ylabel("CDF")

    # Show the plot
    plt.show()

    # Compute bin edges: bins
    bins = np.arange(0, max(n_defaults) + 2) - 0.5

    # Generate histogram
    plt.hist(n_defaults, normed=True, bins=bins)

    # Label axes
    plt.xlabel("x")
    plt.ylabel("y")

    # Show the plot
    plt.show()
