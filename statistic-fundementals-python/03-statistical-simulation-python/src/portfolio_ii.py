#! /usr/bin/python3
"""
:file: portfolio_ii.py
:author: Hossam Khair
"""
import numpy as np
from portfolio_i import portfolio_return

if __name__ == "__main__":
    # Run 1,000 iterations and store the results
    sims, rets = 1000, []

    for i in range(sims):
        rets.append(portfolio_return(yrs=10, avg_return=0.07,
                                     sd_of_return=0.3, principal=10000))

    # Calculate the 95% CI
    lower_ci = np.percentile(rets, 2.5)
    upper_ci = np.percentile(rets, 97.5)
    print("95% CI of Returns: Lower = {}, Upper = {}".format(lower_ci, upper_ci))
