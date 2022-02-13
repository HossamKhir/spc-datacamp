#! /usr/bin/python3
"""
"""
import os
import pandas as pd
import matplotlib.pyplot as plt

DATA_PATH = "../data/raw"

# Import sas7bdat package
from sas7bdat import SAS7BDAT

if __name__ == "__main__":
    # Save file to a DataFrame: df_sas
    with SAS7BDAT(os.path.join(DATA_PATH, "sales.sas7bdat")) as file:
        df_sas = file.to_data_frame()

    # Print head of DataFrame
    print(df_sas.head())

    # Plot histogram of DataFrame features (pandas and pyplot already imported)
    pd.DataFrame.hist(df_sas[["P"]])
    plt.ylabel("count")
    plt.show()
