#! /usr/bin/python3
"""
"""
import pandas as pd
from load_data import load_classic_18, load_classic_19, load_pop_18, load_pop_19

classic_18 = load_classic_18()
classic_19 = load_classic_19()
pop_18 = load_pop_18()
pop_19 = load_pop_19()

if __name__ == "__main__":
    # Concatenate the classic tables vertically
    classic_18_19 = pd.concat([classic_18, classic_19], ignore_index=True)

    # Concatenate the pop tables vertically
    pop_18_19 = pd.concat([pop_18, pop_19], ignore_index=True)

    # Merge classic_18_19 with pop_18_19
    classic_pop = classic_18_19.merge(pop_18_19, on="tid", how="inner")

    # Using .isin(), filter classic_18_19 rows where tid is in classic_pop
    popular_classic = classic_18_19[classic_18_19["tid"].isin(classic_pop["tid"])]

    # Print popular chart
    print(popular_classic)
