#! /usr/bin/python3
"""
:file: poisson.py
:author: Hossam Khair
"""
import numpy as np

if __name__ == "__main__":
    # Draw 10,000 samples out of Poisson distribution: samples_poisson
    samples_poisson = np.random.poisson(lam=10, size=10**4)

    # Print the mean and standard deviation
    print('Poisson:     ', np.mean(samples_poisson), np.std(samples_poisson))

    # Specify values of n and p to consider for Binomial: n, p
    n = [20, 100, 1000]
    p = [.5, .1, .01]

    # Draw 10,000 samples for each n,p pair: samples_binomial
    for i in range(3):
        samples_binomial = np.random.binomial(n[i], p[i], size=10**4)

        # Print results
        print('n =', n[i], 'Binom:', np.mean(
            samples_binomial), np.std(samples_binomial))
