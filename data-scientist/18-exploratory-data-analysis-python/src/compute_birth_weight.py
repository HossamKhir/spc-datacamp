#! /usr/bin/python3
"""
"""
from load_data import load_nsfg

nsfg = load_nsfg()
birth_weight = nsfg.birthwgt_lb1

if __name__ == "__main__":
    # Create a Boolean Series for full-term babies
    full_term = nsfg.prglngth >= 37

    # Select the weights of full-term babies
    full_term_weight = birth_weight[full_term]

    # Compute the mean weight of full-term babies
    print(full_term_weight.mean())
