#! /usr/bin/python3
"""
"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from distribution_income import gss, dist, log_income

if __name__ == "__main__":
    # Evaluate the normal PDF
    xs = np.linspace(2, 5.5)
    ys = dist.pdf(xs)

    # Plot the model PDF
    plt.clf()
    plt.plot(xs, ys, color="gray")

    # Plot the data KDE
    sns.kdeplot(log_income)

    # Label the axes
    plt.xlabel("log10 of realinc")
    plt.ylabel("PDF")
    plt.show()
