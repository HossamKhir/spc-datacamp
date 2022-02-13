#! /usr/bin/python3
"""
:file: cond_urn.py
:author: Hossam Khair
"""
import numpy as np

if __name__ == "__main__":
    # Initialize success, sims and urn
    success, sims = 0, 5000
    urn = ['w'] * 7 + ['b'] * 6

    for _ in range(sims):
        # Draw 4 balls without replacement
        draw = np.random.choice(urn, replace=False, size=4)
        # Count the number of successes
        if all(draw[::2] == ['w', 'w']) and all(draw[1::2] == ['b', 'b']):
            success += 1

    print("Probability of success = {}".format(success/sims))
