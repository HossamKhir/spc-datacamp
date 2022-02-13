#! /usr/bin/python3
"""
:file: poisson.py
:author: Hossam Khair
"""
import numpy as np

if __name__ == "__main__":
    pass
    # Initialize seed and parameters
    np.random.seed(123)
    lam, size_1, size_2 = 5, 3, 1000

    # Draw samples & calculate absolute difference between lambda and sample mean
    samples_1 = np.random.poisson(lam, size_1)
    samples_2 = np.random.poisson(lam, size_2)
    answer_1 = abs(lam - np.mean(samples_1))
    answer_2 = abs(lam - np.mean(samples_2))

    print("|Lambda - sample mean| with {} samples is {} and with {} samples is {}. ".format(size_1,
                                                                                            answer_1, size_2, answer_2))
