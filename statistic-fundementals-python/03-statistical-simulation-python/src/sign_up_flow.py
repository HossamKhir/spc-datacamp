#! /usr/bin/python3
"""
:file: sign_up_flow.py
:author: Hossam Khair
"""
import numpy as np


def get_signups(cost, ct_rate, su_rate, sims):
    lam = np.random.normal(loc=100000, scale=2000, size=sims)
    # Simulate impressions(poisson), clicks(binomial) and signups(binomial)
    impressions = np.random.poisson(lam)
    clicks = np.random.binomial(n=impressions, p=ct_rate[cost])
    signups = np.random.binomial(n=clicks, p=su_rate[cost])
    return signups


# Initialize click-through rate and signup rate dictionaries
ct_rate = {'low': 0.01, 'high': np.random.uniform(low=0.01, high=1.2*0.01)}
su_rate = {'low': 0.2, 'high': np.random.uniform(low=0.2, high=1.2*.2)}


if __name__ == "__main__":
    print("Simulated Signups = {}".format(
        get_signups('high', ct_rate, su_rate, 1)))
