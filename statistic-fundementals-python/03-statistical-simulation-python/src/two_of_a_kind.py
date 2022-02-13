#! /usr/bin/python3
"""
:file: two_of_a_kind.py
:author: Hossam Khair
"""
import numpy as np

deck_of_cards = [
    ('Heart', 0),
    ('Heart', 1),
    ('Heart', 2),
    ('Heart', 3),
    ('Heart', 4),
    ('Heart', 5),
    ('Heart', 6),
    ('Heart', 7),
    ('Heart', 8),
    ('Heart', 9),
    ('Heart', 10),
    ('Heart', 11),
    ('Heart', 12),
    ('Club', 0),
    ('Club', 1),
    ('Club', 2),
    ('Club', 3),
    ('Club', 4),
    ('Club', 5),
    ('Club', 6),
    ('Club', 7),
    ('Club', 8),
    ('Club', 9),
    ('Club', 10),
    ('Club', 11),
    ('Club', 12),
    ('Spade', 0),
    ('Spade', 1),
    ('Spade', 2),
    ('Spade', 3),
    ('Spade', 4),
    ('Spade', 5),
    ('Spade', 6),
    ('Spade', 7),
    ('Spade', 8),
    ('Spade', 9),
    ('Spade', 10),
    ('Spade', 11),
    ('Spade', 12),
    ('Diamond', 0),
    ('Diamond', 1),
    ('Diamond', 2),
    ('Diamond', 3),
    ('Diamond', 4),
    ('Diamond', 5),
    ('Diamond', 6),
    ('Diamond', 7),
    ('Diamond', 8),
    ('Diamond', 9),
    ('Diamond', 10),
    ('Diamond', 11),
    ('Diamond', 12)
]

if __name__ == "__main__":
    # Shuffle deck & count card occurrences in the hand
    n_sims, two_kind = 10000, 0
    for i in range(n_sims):
        np.random.shuffle(deck_of_cards)
        hand, cards_in_hand = deck_of_cards[0:5], {}
        for [suite, numeric_value] in hand:
            # Count occurrences of each numeric value
            cards_in_hand[numeric_value] = cards_in_hand.get(
                numeric_value, 0) + 1

        # Condition for getting at least 2 of a kind
        if max(cards_in_hand.values()) >= 2:
            two_kind += 1

    print("Probability of seeing at least two of a kind = {} ".format(two_kind/n_sims))
