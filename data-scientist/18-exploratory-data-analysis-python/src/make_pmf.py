#! /usr/bin/python3
"""
"""
from empiricaldist import Pmf
from load_data import load_gss

gss = load_gss()

if __name__ == "__main__":
    # Compute the PMF for year
    pmf_year = Pmf(gss.year, normalize=False)

    # Print the result
    print(pmf_year)
