#! /usr/bin/python3
"""
"""
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from load_data import load_gss

gss = load_gss()
gss["educ2"] = gss["educ"] ** 2
gss["age2"] = gss["age"] ** 2

# Run a regression model with educ, educ2, age, and age2
results = smf.ols("realinc ~ educ + educ2 + age + age2", data=gss).fit()

# Make the DataFrame
df = pd.DataFrame()
df["educ"] = np.linspace(0, 20)
df["age"] = 30
df["educ2"] = df["educ"] ** 2
df["age2"] = df["age"] ** 2

if __name__ == "__main__":
    # Generate and plot the predictions
    pred = results.predict(df)
    print(pred.head())
