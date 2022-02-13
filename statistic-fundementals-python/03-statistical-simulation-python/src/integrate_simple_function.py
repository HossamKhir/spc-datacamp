#! /usr/bin/python3
"""
:file: integrate_simple_function.py
:author: Hossam Khair
"""
import numpy as np

# Define the sim_integrate function


def sim_integrate(func, xmin, xmax, sims):
    x = np.random.uniform(xmin, xmax, sims)
    y = np.random.uniform(min(min(func(x)), 0), max(func(x)), sims)
    area = (max(y) - min(y))*(xmax-xmin)
    result = area * sum(abs(y) < abs(func(x)))/sims
    return result


if __name__ == "__main__":
    # Call the sim_integrate function and print results
    result = sim_integrate(func=lambda x: x * np.exp(x),
                           xmin=0, xmax=1, sims=50)
    print("Simulated answer = {}, Actual Answer = 1".format(result))
