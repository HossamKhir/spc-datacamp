#! /usr/bin/python3
"""
:file: portfolio_iii.py
:author: Hossam Khair
"""
import numpy as np
from portfolio_i import portfolio_return

rets_stock, rets_bond = [], []

if __name__ == "__main__":
    pass
    for i in range(sims):
        rets_stock.append(portfolio_return(
            yrs=10, avg_return=.07, sd_of_return=.3, principal=10000))
        rets_bond.append(portfolio_return(
            yrs=10, avg_return=.04, sd_of_return=.1, principal=10000))

    # Calculate the 25th percentile of the distributions and the amount you'd lose or gain
    rets_stock_perc = np.percentile(rets_stock, 25)
    rets_bond_perc = np.percentile(rets_bond, 25)
    additional_returns = rets_stock_perc - rets_bond_perc
    print("Sticking to stocks gets you an additional return of {}".format(
        additional_returns))
