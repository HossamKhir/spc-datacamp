#! /usr/bin/python3
"""
:file: fair_die.py
:author: Hossam Khair
"""
import numpy as np

if __name__ == "__main__":
    pass
    # Define die outcomes and probabilities
    die, probabilities, throws = [d for d in range(1, 7)], [
        1/6 for _ in range(6)], 1

    # Use np.random.choice to throw the die once and record the outcome
    outcome = np.random.choice(die, size=throws, p=probabilities)
    print("Outcome of the throw: {}".format(outcome[0]))
