#! /usr/bin/python3
"""
:file: full_house.py
:author: Hossam Khair
"""
import numpy as np
from two_of_a_kind import deck_of_cards as deck

if __name__ == "__main__":
    # Shuffle deck & count card occurrences in the hand
    n_sims, full_house, deck_of_cards = 50000, 0, deck.copy()
    for i in range(n_sims):
        np.random.shuffle(deck_of_cards)
        hand, cards_in_hand = deck_of_cards[0:5], {}
        for card in hand:
            # Use .get() method to count occurrences of each card
            cards_in_hand[card[1]] = cards_in_hand.get(card[1], 0) + 1

        # Condition for getting full house
        condition = (max(cards_in_hand.values()) == 3) & (
            min(cards_in_hand.values()) == 2)
        if condition:
            full_house += 1
    print("Probability of seeing a full house = {}".format(full_house/n_sims))
