#! /usr/bin/python3
"""
"""
import statsmodels.formula.api as smf
from load_data import load_gss

gss = load_gss()

if __name__ == "__main__":
    # Add a new column with educ squared
    gss["educ2"] = gss["educ"] ** 2
    gss["age2"] = gss["age"] ** 2

    # Run a regression model with educ, educ2, age, and age2
    results = smf.ols("realinc ~ educ + educ2 + age + age2", data=gss).fit()

    # Print the estimated parameters
    print(results.params)
