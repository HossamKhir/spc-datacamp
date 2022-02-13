#! /usr/bin/python3
"""
"""
# Import datetime
from datetime import datetime

if __name__ == "__main__":
    # Starting timestamps
    timestamps = [1514665153, 1514664543]

    # Datetime objects
    dts = []

    # Loop
    for ts in timestamps:
        dts.append(datetime.fromtimestamp(ts))

    # Print results
    print(dts)
