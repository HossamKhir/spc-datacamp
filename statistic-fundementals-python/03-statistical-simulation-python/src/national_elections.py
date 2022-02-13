#! /usr/bin/python3
"""
:file: national_elections.py
:author: Hossam Khair
"""
import numpy as np

p = np.array([
    0.52076814, 0.67846401, 0.82731745, 0.64722761, 0.03665174,
    0.17835411, 0.75296372, 0.22206157, 0.72778372, 0.28461556,
    0.72545221, 0.106571, 0.09291364, 0.77535718, 0.51440142,
    0.89604586, 0.39376099, 0.24910244, 0.92518253, 0.08165597,
    0.4212476, 0.74123879, 0.2479099, 0.46125805, 0.19584491,
    0.24440482, 0.349916, 0.80224624, 0.80186664, 0.82968251,
    0.91178779, 0.51739059, 0.67338858, 0.15675863, 0.37772308,
    0.77134621, 0.71727114, 0.92700912, 0.28386132, 0.25502498,
    0.30081506, 0.19724585, 0.29129564, 0.56623386, 0.97681039,
    0.96263926, 0.0548948, 0.14092758, 0.54739446, 0.54555576
])
outcomes, sims, probs = [], 1000, p

if __name__ == "__main__":
    for _ in range(sims):
        # Simulate elections in the 50 states
        election = np.random.binomial(n=1, p=probs)
        # Get average of Red wins and add to `outcomes`
        outcomes.append(np.average(election))

    # Calculate probability of Red winning in less than 45% of the states
    prob_red_wins = sum([o < .45 for o in outcomes])/sims
    print("Probability of Red winning in less than 45% of the states = {}".format(
        prob_red_wins))
