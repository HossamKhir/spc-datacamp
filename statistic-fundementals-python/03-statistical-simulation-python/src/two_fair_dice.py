#! /usr/bin/python3
"""
:file: two_fair_dice.py
:author: Hossam Khair
"""
import numpy as np

if __name__ == "__main__":
    pass
    # Initialize number of dice, simulate & record outcome
    die, probabilities, num_dice = [1, 2, 3, 4, 5, 6], [
        1/6, 1/6, 1/6, 1/6, 1/6, 1/6], 2
    outcomes = np.random.choice(die, size=num_dice, p=probabilities)

    # Win if the two dice show the same number
    if outcomes[0] == outcomes[1]:
        answer = 'win'
    else:
        answer = 'lose'

    print("The dice show {} and {}. You {}!".format(
        outcomes[0], outcomes[1], answer))
