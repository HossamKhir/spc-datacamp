#! /usr/bin/python3
"""
"""
from empiricaldist import Cdf
from load_data import load_gss

gss = load_gss()

cdf_income = Cdf(gss.realinc)

if __name__ == "__main__":
    # Calculate the 75th percentile
    percentile_75th = cdf_income.inverse(0.75)

    # Calculate the 25th percentile
    percentile_25th = cdf_income.inverse(0.25)

    # Calculate the interquartile range
    iqr = percentile_75th - percentile_25th

    # Print the interquartile range
    print(iqr)
