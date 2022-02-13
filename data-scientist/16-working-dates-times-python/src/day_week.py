#! /usr/bin/python3
"""
"""
# Import date from datetime
from datetime import date

if __name__ == "__main__":
    # Create a date object
    hurricane_andrew = date(1992, 8, 24)

    # Which day of the week is the date?
    print(hurricane_andrew.weekday())
