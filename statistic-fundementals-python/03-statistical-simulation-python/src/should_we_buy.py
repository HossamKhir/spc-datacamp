#! /usr/bin/python3
"""
:file: should_we_buy.py
:author: Hossam Khair
"""
import numpy as np

lottery_ticket_cost, num_tickets, grand_prize = 10, 1000, 10000
chance_of_winning = 1/num_tickets

if __name__ == "__main__":
    pass
    # Initialize size and simulate outcome
    size = 2000
    payoffs = [-lottery_ticket_cost, grand_prize-lottery_ticket_cost]
    probs = [1 - chance_of_winning, chance_of_winning]

    outcomes = np.random.choice(a=payoffs, size=size, p=probs, replace=True)

    # Mean of outcomes.
    answer = np.mean(outcomes)
    print("Average payoff from {} simulations = {}".format(size, answer))
