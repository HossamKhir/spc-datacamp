#! /usr/bin/python3
"""
"""
import pandas as pd
from load_data import load_gdp, load_sp500

gdp = load_gdp()
sp500 = load_sp500()

if __name__ == "__main__":
    # Use merge_ordered() to merge gdp and sp500 on year and date
    gdp_sp500 = pd.merge_ordered(
        gdp, sp500, left_on="year", right_on="date", how="left"
    )

    # Print gdp_sp500
    print(gdp_sp500)

    # Use merge_ordered() to merge gdp and sp500, interpolate missing value
    gdp_sp500 = pd.merge_ordered(
        gdp, sp500, left_on="year", right_on="date", how="left", fill_method="ffill"
    )

    # Print gdp_sp500
    print(gdp_sp500)

    # Subset the gdp and returns columns
    gdp_returns = gdp_sp500[["gdp", "returns"]]

    # Print gdp_returns correlation
    print(gdp_returns.corr())
