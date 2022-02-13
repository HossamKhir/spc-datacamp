#! /usr/bin/python3
"""
"""
from early_hurricane import florida_hurricane_dates

if __name__ == "__main__":
    # Assign the earliest date to first_date
    first_date = min(florida_hurricane_dates)

    # Convert to ISO and US formats
    iso = "Our earliest hurricane date: " + first_date.isoformat()
    us = "Our earliest hurricane date: " + first_date.strftime("%m/%d/%Y")

    print("ISO: " + iso)
    print("US: " + us)
