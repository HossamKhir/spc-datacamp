#! /usr/bin/python3
"""
"""
import numpy as np
import matplotlib.pyplot as plt
from empiricaldist import Cdf
from distribution_income import gss, dist, log_income

if __name__ == "__main__":
    # Evaluate the model CDF
    xs = np.linspace(2, 5.5)
    ys = dist.cdf(xs)

    # Plot the model CDF
    plt.clf()
    plt.plot(xs, ys, color="gray")

    # Create and plot the Cdf of log_income
    Cdf(log_income).plot()

    # Label the axes
    plt.xlabel("log10 of realinc")
    plt.ylabel("CDF")
    plt.show()
