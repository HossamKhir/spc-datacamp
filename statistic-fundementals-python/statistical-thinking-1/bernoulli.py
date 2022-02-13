#! /usr/bin/python3
"""
:file: bernoulli.py
:author: Hossam Khair
"""
import numpy as np
import matplotlib.pyplot as plt


def perform_bernoulli_trials(n, p):
    """Perform n Bernoulli trials with success probability p
    and return number of successes."""
    # Initialize number of successes: n_success
    n_success = 0

    # Perform trials
    for i in range(n):
        # Choose random number between zero and one: random_number
        num = np.random.random()

        # If less than p, it's a success so add one to n_success
        if p // num:
            n_success += 1

    return n_success


# if __name__ == "__main__":
# Initialize the number of defaults: n_defaults
n_defaults = np.empty(1000)

# Compute the number of defaults
for i in range(1000):
    n_defaults[i] = perform_bernoulli_trials(100, 0.05)

# Plot the histogram with default number of bins; label your axes
_ = plt.hist(n_defaults, normed=True)
_ = plt.xlabel('number of defaults out of 100 loans')
_ = plt.ylabel('probability')

# Show the plot
plt.show()
