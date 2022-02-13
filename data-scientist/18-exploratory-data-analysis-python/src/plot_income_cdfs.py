#! /usr/bin/python3
"""
"""
import matplotlib.pyplot as plt
from empiricaldist import Cdf
from load_data import load_gss
from extract_education_level import bach, assc, high

gss = load_gss()

if __name__ == "__main__":
    income = gss["realinc"]

    # Plot the CDFs
    Cdf(income[high]).plot(label="High school")
    Cdf(income[assc]).plot(label="Associate")
    Cdf(income[bach]).plot(label="Bachelor")

    # Label the axes
    plt.xlabel("Income (1986 USD)")
    plt.ylabel("CDF")
    plt.legend()
    plt.show()
