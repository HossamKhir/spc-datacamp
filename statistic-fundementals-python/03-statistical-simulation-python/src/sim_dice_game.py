#! /usr/bin/python3
"""
:file: sim_dice_game.py
:author: Hossam Khair
"""
import numpy as np

if __name__ == "__main__":
    pass
    # Initialize model parameters & simulate dice throw
    die, probabilities, num_dice = [1, 2, 3, 4, 5, 6], [
        1/6, 1/6, 1/6, 1/6, 1/6, 1/6], 2
    sims, wins = 100, 0

    for i in range(sims):
        outcomes = np.random.choice(die, p=probabilities, size=num_dice)
        # Increment `wins` by 1 if the dice show same number
        if outcomes[0] == outcomes[1]:
            wins = wins + 1

    print("In {} games, you win {} times".format(sims, wins))
