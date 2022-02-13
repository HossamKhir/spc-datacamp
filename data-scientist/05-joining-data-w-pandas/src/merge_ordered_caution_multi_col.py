#! /usr/bin/python3
"""
"""
import pandas as pd
from load_data import load_gdp, load_pop

gdp = load_gdp()
pop = load_pop()


if __name__ == "__main__":
    pass
# Merge gdp and pop on date and country with fill and notice rows 2 and 3
ctry_date = pd.merge_ordered(gdp, pop, on=["date", "country"], fill_method="ffill")

# Print ctry_date
print(ctry_date)

# Merge gdp and pop on country and date with fill
date_ctry = pd.merge_ordered(gdp, pop, on=["country", "date"], fill_method="ffill")

# Print date_ctry
print(date_ctry)
