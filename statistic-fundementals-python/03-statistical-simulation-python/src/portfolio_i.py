#! /usr/bin/python3
"""
:file: portfolio_i.py
:author: Hossam Khair
"""
import numpy as np

# rates is a Normal random variable and has size equal to number of years


def portfolio_return(yrs, avg_return, sd_of_return, principal):
    np.random.seed(123)
    rates = np.random.normal(loc=avg_return, scale=sd_of_return, size=yrs)
    # Calculate the return at the end of the period
    end_return = principal
    for x in rates:
        end_return = end_return*(1+x)
    return end_return


if __name__ == "__main__":
    result = portfolio_return(yrs=5, avg_return=0.07,
                              sd_of_return=0.15, principal=1000)
    print("Portfolio return after 5 years = {}".format(result))
