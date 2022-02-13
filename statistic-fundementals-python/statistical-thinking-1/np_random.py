#! /usr/bin/python3
"""
:file: np_random.py
:author: Hossam Khair
"""
import numpy as np
import matplotlib.pyplot as plt

# Seed the random number generator
np.random.seed(42)

if __name__ == "__main__":
    # Initialize random numbers: random_numbers
    random_numbers = np.empty(int(1e5))

    # Generate random numbers by looping over range(100000)
    for i in range(int(1e5)):
        random_numbers[i] = np.random.random()

    # Plot a histogram
    _ = plt.hist(random_numbers)

    # Show the plot
    plt.show()
