#! /usr/bin/python3
"""
"""
# Import date
from datetime import date

if __name__ == "__main__":
    # Create a date object
    andrew = date(1992, 8, 26)

    # Print the date in the format 'YYYY-MM'
    print(andrew.strftime("%Y-%m"))

    # Print the date in the format 'MONTH (YYYY)'
    print(andrew.strftime("%B (%Y)"))

    # Print the date in the format 'YYYY-DDD'
    print(andrew.strftime("%Y-%j"))
