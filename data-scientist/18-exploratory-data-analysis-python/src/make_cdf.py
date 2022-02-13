#! /usr/bin/python3
"""
"""
from empiricaldist import Cdf
from load_data import load_gss

gss = load_gss()

if __name__ == "__main__":
    # Select the age column
    age = gss["age"]

    # Compute the CDF of age
    cdf_age = Cdf(age)

    # Calculate the CDF of 30
    print(cdf_age(30))
