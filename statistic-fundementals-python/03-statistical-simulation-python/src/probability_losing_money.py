#! /usr/bin/python3
"""
:file: probability_losing_money.py
:author: Hossam Khair
"""
import numpy as np
from purchase_flow import get_signups, get_revenue, ct_rate, su_rate


if __name__ == "__main__":
    # Initialize cost_diff
    sims, cost_diff = 10000, 3000

    # Get revenue when the cost is 'low' and when the cost is 'high'
    rev_low = get_revenue(get_signups('low', ct_rate, su_rate, sims))
    rev_high = get_revenue(get_signups('high', ct_rate, su_rate, sims))

    # calculate fraction of times rev_high - rev_low is less than cost_diff
    frac = sum([cost_diff > (rev_high[i] - rev_low[i])
                for i in range(len(rev_low))])/len(rev_high)
    print("Probability of losing money = {}".format(frac))
