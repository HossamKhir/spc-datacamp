#! /usr/bin/python3
"""
"""
import numpy as np
import pandas as pd
from load_data import load_airlines

airlines = load_airlines()

if __name__ == "__main__":
    # Create ranges for categories
    label_ranges = [0, 60, 180, np.inf]
    label_names = ["short", "medium", "long"]

    # Create wait_type column
    airlines["wait_type"] = pd.cut(
        airlines["wait_min"], bins=label_ranges, labels=label_names
    )

    # Create mappings and replace
    mappings = {
        "Monday": "weekday",
        "Tuesday": "weekday",
        "Wednesday": "weekday",
        "Thursday": "weekday",
        "Friday": "weekday",
        "Saturday": "weekend",
        "Sunday": "weekend",
    }

    airlines["day_week"] = airlines["day"].replace(mappings)
