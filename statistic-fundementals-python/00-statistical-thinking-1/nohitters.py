#! /usr/bin/python3
"""
:file: nohitters.py
:author: Hossam Khair
"""
import numpy as np

if __name__ == "__main__":
    # Draw 10,000 samples out of Poisson distribution: n_nohitters
    n_nohitters = np.random.poisson(lam=251/115, size=10**4)

    # Compute number of samples that are seven or greater: n_large
    n_large = np.sum(n_nohitters >= 7)

    # Compute probability of getting seven or more: p_large
    p_large = n_large/(10**4)

    # Print the result
    print('Probability of seven or more no-hitters:', p_large)
