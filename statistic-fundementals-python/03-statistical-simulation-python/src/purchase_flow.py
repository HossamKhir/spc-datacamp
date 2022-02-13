#! /usr/bin/python3
"""
:file: purchase_flow.py
:author: Hossam Khair
"""
import numpy as np
from sign_up_flow import get_signups, ct_rate, su_rate


def get_revenue(signups):
    rev = []
    np.random.seed(123)
    for s in signups:
        # Model purchases as binomial, purchase_values as exponential
        purchases = np.random.binomial(s, p=.1)
        purchase_values = np.random.exponential(scale=1000, size=purchases)

        # Append to revenue the sum of all purchase values.
        rev.append(np.sum(purchase_values))
    return rev


if __name__ == "__main__":
    print("Simulated Revenue = ${}".format(
        get_revenue(get_signups('low', ct_rate, su_rate, 1))[0]))
