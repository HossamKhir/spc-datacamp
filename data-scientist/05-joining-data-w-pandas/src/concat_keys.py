#! /usr/bin/python3
"""
"""
import pandas as pd
import matplotlib.pyplot as plt
from load_data import load_inv_aug, load_inv_jul, load_inv_sep

inv_aug = load_inv_aug()
inv_jul = load_inv_jul()
inv_sep = load_inv_sep()

if __name__ == "__main__":
    # Concatenate the tables and add keys
    inv_jul_thr_sep = pd.concat(
        [inv_jul, inv_aug, inv_sep], keys=["7Jul", "8Aug", "9Sep"]
    )

    # Group the invoices by the index keys and find avg of the total column
    avg_inv_by_month = inv_jul_thr_sep.groupby(level=0).agg({"total": "mean"})

    # Bar plot of avg_inv_by_month
    avg_inv_by_month.plot(kind="bar")
    plt.show()
