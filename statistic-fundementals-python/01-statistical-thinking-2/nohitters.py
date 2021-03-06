#! /usr/bin/python3
"""
:file:
:author: Hossam Khair
"""
import numpy as np
import matplotlib.pyplot as plt
from ecdf import ecdf

# Seed random number generator
np.random.seed(42)
nohitter_times = np.array([])

if __name__ == "__main__":
    # Compute mean no-hitter time: tau
    tau = np.mean(nohitter_times)

    # Draw out of an exponential distribution with parameter tau: inter_nohitter_time
    inter_nohitter_time = np.random.exponential(tau, 100000)

    # Plot the PDF and label axes
    _ = plt.hist(inter_nohitter_time,
                 normed=True, bins=50, histtype="step")
    _ = plt.xlabel('Games between no-hitters')
    _ = plt.ylabel('PDF')

    # Show the plot
    plt.show()

    # Create an ECDF from real data: x, y
    x, y = ecdf(nohitter_times)

    # Create a CDF from theoretical samples: x_theor, y_theor
    x_theor, y_theor = ecdf(inter_nohitter_time)

    # Overlay the plots
    plt.plot(x_theor, y_theor)
    plt.plot(x, y, marker=".", linestyle="none")

    # Margins and axis labels
    plt.margins(.02)
    plt.xlabel('Games between no-hitters')
    plt.ylabel('CDF')

    # Show the plot
    plt.show()

    # Plot the theoretical CDFs
    plt.plot(x_theor, y_theor)
    plt.plot(x, y, marker='.', linestyle='none')
    plt.margins(0.02)
    plt.xlabel('Games between no-hitters')
    plt.ylabel('CDF')

    # Take samples with half tau: samples_half
    samples_half = np.random.exponential(tau/2., size=10**4)

    # Take samples with double tau: samples_double
    samples_double = np.random.exponential(2.*tau, size=10**4)

    # Generate CDFs from these samples
    x_half, y_half = ecdf(samples_half)
    x_double, y_double = ecdf(samples_double)

    # Plot these CDFs as lines
    _ = plt.plot(x_half, y_half)
    _ = plt.plot(x_double, y_double)

    # Show the plot
    plt.show()
