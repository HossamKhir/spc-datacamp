#! /usr/bin/python3
"""
"""
from scipy.stats import linregress
import statsmodels.formula.api as smf
from load_data import load_brfss

brfss = load_brfss()

if __name__ == "__main__":
    # Run regression with linregress
    subset = brfss.dropna(subset=["INCOME2", "_VEGESU1"])
    xs = subset["INCOME2"]
    ys = subset["_VEGESU1"]
    res = linregress(xs, ys)
    print(res)

    # Run regression with StatsModels
    results = smf.ols("INCOME2 ~ _VEGESU1", data=subset).fit()
    print(results.params)
