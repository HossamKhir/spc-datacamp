#! /usr/bin/python3
"""
"""
import pandas as pd
from load_wards import wards, zip_demo
from load_biz import licenses

if __name__ == "__main__":
    # Merge licenses and zip_demo, on zip; and merge the wards on ward
    licenses_zip_ward = licenses.merge(zip_demo, on="zip").merge(wards, on="ward")

    # Print the results by alderman and show median income
    print(licenses_zip_ward.groupby("alderman").agg({"income": "median"}))
