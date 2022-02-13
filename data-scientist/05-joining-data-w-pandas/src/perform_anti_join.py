#! /usr/bin/python3
"""
"""
import pandas as pd
from load_data import load_employees, load_top_cust

employees = load_employees()
top_cust = load_top_cust()

if __name__ == "__main__":
    # Merge employees and top_cust
    empl_cust = employees.merge(top_cust, on="srid", how="left", indicator=True)

    # Select the srid column where _merge is left_only
    srid_list = empl_cust.loc[empl_cust["_merge"] == "left_only", "srid"]

    # Get employees not working with top customers
    print(employees[employees["srid"].isin(srid_list)])
