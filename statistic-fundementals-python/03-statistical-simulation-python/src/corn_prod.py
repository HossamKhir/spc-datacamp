#! /usr/bin/python3
"""
:file: corn_prod.py
:author: Hossam Khair
"""
import numpy as np


cost = 5000
# Corn Production Model


def corn_produced(rain, cost):
    mean_corn = 100 * (cost ** .1) * (rain ** .2)
    corn = np.random.poisson(mean_corn)
    return corn


if __name__ == "__main__":
    # Initialize variables
    rain = np.random.normal(50, 15)

    # Simulate and print corn production
    corn_result = corn_produced(rain, cost)
    print("Simulated Corn Production = {}".format(corn_result))
