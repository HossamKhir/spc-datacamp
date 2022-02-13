#! /usr/bin/python3
"""
:file: shuffle_cards.py
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
    pass
    # Shuffle the deck
    np.random.shuffle(deck_of_cards)

    # Print out the top three cards
    card_choices_after_shuffle = deck_of_cards[:3]
    print(card_choices_after_shuffle)
