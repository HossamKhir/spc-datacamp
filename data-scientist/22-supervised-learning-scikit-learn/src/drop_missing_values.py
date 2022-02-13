#! /usr/bin/python3
"""
"""
import numpy as np
from load_data import load_voting

df = load_voting()

if __name__ == "__main__":
    pass
# Convert '?' to NaN
df[df == "?"] = np.nan

# Print the number of NaNs
print(df.isnull().sum())

# Print shape of original DataFrame
print("Shape of Original DataFrame: {}".format(df.shape))

# Drop missing values and print shape of new DataFrame
df = df.dropna()

# Print shape of new DataFrame
print(
    "Shape of DataFrame After Dropping All Rows with Missing Values: {}".format(
        df.shape
    )
)
