#! /usr/bin/python3
"""
:file: optimising_costs.py
:author: Hossam Khair
"""
import numpy as np
from modeling_profits import profits

if __name__ == "__main__":
    # Initialize results and cost_levels variables
    sims, results = 1000, {}
    cost_levels = np.arange(100, 5100, 100)

    # For each cost level, simulate profits and store mean profit
    for cost in cost_levels:
        tmp_profits = []
        for i in range(sims):
            tmp_profits.append(profits(cost))
        results[cost] = np.mean(tmp_profits)

    # Get the cost that maximizes average profit
    cost_max = [x for x in results.keys() if results[x] ==
                max(results.values())][0]
    print("Average profit is maximized when cost = {}".format(cost_max))
