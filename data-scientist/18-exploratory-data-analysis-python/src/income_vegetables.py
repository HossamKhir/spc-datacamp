#! /usr/bin/python3
"""
"""
from load_data import load_brfss
from scipy.stats import linregress

brfss = load_brfss()
# Extract the variables
subset = brfss.dropna(subset=["INCOME2", "_VEGESU1"])
xs = subset.INCOME2
ys = subset._VEGESU1
# Compute the linear regression
res = linregress(xs, ys)

if __name__ == "__main__":
    print(res)
