#! /usr/bin/python3
"""
"""
import pandas as pd
import matplotlib.pyplot as plt
from load_data import load_inflation, load_unemployment

inflation = load_inflation()
unemployment = load_unemployment()

if __name__ == "__main__":
    # Use merge_ordered() to merge inflation, unemployment with inner join
    inflation_unemploy = pd.merge_ordered(
        inflation, unemployment, how="inner", on="date"
    )

    # Print inflation_unemploy
    print(inflation_unemploy)

    # Plot a scatter plot of unemployment_rate vs cpi of inflation_unemploy
    inflation_unemploy.plot(kind="scatter", x="unemployment_rate", y="cpi")
    plt.show()
