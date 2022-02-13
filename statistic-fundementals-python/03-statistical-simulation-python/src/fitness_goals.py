#! /usr/bin/python3
"""
:file: fitness_goals.py
:author: Hossam Khair
"""
import numpy as np
from national_elections import sims, outcomes

days = 30

if __name__ == "__main__":
    print(outcomes)
    # Simulate steps & choose prob
    for _ in range(sims):
        w = []
        for i in range(days):
            lam = np.random.choice([5000, 15000], p=[0.6, 0.4], size=1)
            steps = np.random.poisson(lam)
            if steps > 10000:
                prob = [.2, .8]
            elif steps < 8000:
                prob = [.8, .2]
            else:
                prob = [0.5, 0.5]
            w.append(np.random.choice([1, -1], p=prob))
        outcomes.append(sum(w))

    # Calculate fraction of outcomes where there was a weight loss
    weight_loss_outcomes_frac = sum(o < 0 for o in outcomes)/len(outcomes)
    print("Probability of Weight Loss = {}".format(weight_loss_outcomes_frac))
