#! /usr/bin/python3
"""
:file: bday_problem.py
:author: Hossam Khair
"""
import numpy as np


def birthday_sim(people):
    sims, unique_birthdays = 2000, 0
    for _ in range(sims):
        draw = np.random.choice(days, size=people, replace=True)
        if len(draw) == len(set(draw)):
            unique_birthdays += 1
    out = 1 - unique_birthdays / sims
    return out


if __name__ == "__main__":
    pass
    # Draw a sample of birthdays & check if each birthday is unique
    days = np.arange(1, 366)
    people = 2

    # Break out of the loop if probability greater than 0.5
    while (people > 0):
        prop_bds = birthday_sim(people)
        if prop_bds > .5:
            break
        people += 1

    print("With {} people, there's a 50% chance that two share a birthday.".format(people))
