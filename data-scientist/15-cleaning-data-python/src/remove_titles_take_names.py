#! /usr/bin/python3
"""
"""
import pandas as pd

airlines = pd.read_csv("../data/raw/airlines_full_name.csv")

if __name__ == "__main__":
    # Replace "Dr." with empty string ""
    airlines["full_name"] = airlines["full_name"].str.replace("Dr.", "", regex=False)

    # Replace "Mr." with empty string ""
    airlines["full_name"] = airlines["full_name"].str.replace("Mr.", "", regex=False)

    # Replace "Miss" with empty string ""
    airlines["full_name"] = airlines["full_name"].str.replace("Miss", "", regex=False)

    # Replace "Ms." with empty string ""
    airlines["full_name"] = airlines["full_name"].str.replace("Ms.", "", regex=False)

    # Assert that full_name has no honorifics
    assert airlines["full_name"].str.contains("Ms.|Mr.|Miss|Dr.").any() == False
