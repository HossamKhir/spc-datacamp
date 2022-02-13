#! /usr/bin/python3
"""
"""

from count_b4_after_noon import onebike_datetimes

# Import datetime
from datetime import datetime

if __name__ == "__main__":
    # Pull out the start of the first trip
    first_start = onebike_datetimes[0]["start"]

    # Format to feed to strftime()
    fmt = "%Y-%m-%dT%H:%M:%S"

    # Print out date with .isoformat(), then with .strftime() to compare
    print(first_start.isoformat())
    print(first_start.strftime(fmt))
