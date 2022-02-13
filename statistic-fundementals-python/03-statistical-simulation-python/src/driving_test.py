#! /usr/bin/python3
"""
:file: driving_test.py
:author: Hossam Khair
"""
import numpy as np

sims, outcomes, p_rain, p_pass = 1000, [], 0.40, {'sun': 0.9, 'rain': 0.3}


def test_outcome(p_rain):
    # Simulate whether it will rain or not
    weather = np.random.choice(['rain', 'sun'], p=[p_rain, 1-p_rain])
    # Simulate and return whether you will pass or fail
    test_result = np.random.choice(
        ['pass', 'fail'], p=[p_pass[weather], 1-p_pass[weather]])
    return test_result


if __name__ == "__main__":
    for _ in range(sims):
        outcomes.append(test_outcome(p_rain))

    # Calculate fraction of outcomes where you pass
    pass_outcomes_frac = sum([o == "pass" for o in outcomes])/len(outcomes)
    print("Probability of Passing the driving test = {}".format(pass_outcomes_frac))
