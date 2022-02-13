#! /usr/bin/python3
"""
:file: sim_lottery.com
:author: Hossam Khair
"""
import numpy as np

if __name__ == "__main__":
    pass
    # Pre-defined constant variables
    lottery_ticket_cost, num_tickets, grand_prize = 10, 1000, 10000

    # Probability of winning
    chance_of_winning = 1/num_tickets

    # Simulate a single drawing of the lottery
    gains = [-lottery_ticket_cost, grand_prize-lottery_ticket_cost]
    probability = [1-chance_of_winning, chance_of_winning]
    outcome = np.random.choice(a=gains, size=1, p=probability, replace=True)

    print("Outcome of one drawing of the lottery is {}".format(outcome))
