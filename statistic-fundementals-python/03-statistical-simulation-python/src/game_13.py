#! /usr/bin/python3
"""
:file: game_13.py
:author: Hossam Khair
"""
import numpy as np

if __name__ == "__main__":
    # Pre-set constant variables
    deck, sims, coincidences = np.arange(1, 14), 10000, 0

    for _ in range(sims):
        # Draw all the cards without replacement to simulate one game
        draw = np.random.choice(deck, size=13, replace=False)
        # Check if there are any coincidences
        coincidence = (draw == list(np.arange(1, 14))).any()
        if coincidence == True:
            coincidences += 1

    # Calculate probability of winning
    prob_of_winning = 1 - coincidences/sims
    print("Probability of winning = {}".format(prob_of_winning))
