#! /usr/bin/python3
"""
"""
import pandas as pd
import matplotlib.pyplot as plt
from load_data import load_ur_wide

ur_wide = load_ur_wide()

if __name__ == "__main__":
    # unpivot everything besides the year column
    ur_tall = ur_wide.melt(
        id_vars=["year"], var_name=["month"], value_name="unempl_rate"
    )

    # Create a date column using the month and year columns of ur_tall
    ur_tall["date"] = pd.to_datetime(ur_tall["year"] + "-" + ur_tall["month"])

    # Sort ur_tall by date in ascending order
    ur_sorted = ur_tall.sort_values("date")

    # Plot the unempl_rate by date
    ur_sorted.plot(y="unempl_rate", x="date")
    plt.show()
