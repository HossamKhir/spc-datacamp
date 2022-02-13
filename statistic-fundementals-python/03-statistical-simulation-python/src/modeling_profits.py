#! /usr/bin/python3
"""
:file: modeling_profits.py
:author: Hossam Khair
"""
import numpy as np
from corn_prod import corn_produced, cost


def corn_demanded(price):
    mean_corn = 1000 - 8*price
    corn = np.random.poisson(abs(mean_corn))
    return corn

# Function to calculate profits


def profits(cost):
    rain = np.random.normal(50, 15)
    price = np.random.normal(40, 10)
    supply = corn_produced(rain, cost)
    demand = corn_demanded(price)
    equil_short = supply <= demand
    if equil_short == True:
        tmp = supply*price - cost
        return tmp
    else:
        tmp2 = demand*price - cost
        return tmp2


if __name__ == "__main__":
    result = profits(cost)
    print("Simulated profit = {}".format(result))
