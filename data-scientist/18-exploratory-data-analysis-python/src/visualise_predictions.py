#! /usr/bin/python3
"""
"""
import matplotlib.pyplot as plt
from load_data import load_gss
from make_predictions import df, results

gss = load_gss()

if __name__ == "__main__":
    # Plot mean income in each age group
    plt.clf()
    grouped = gss.groupby("educ")
    mean_income_by_educ = grouped["realinc"].mean()
    plt.plot(mean_income_by_educ, "o", alpha=0.5)

    # Plot the predictions
    pred = results.predict(df)
    plt.plot(df["educ"], pred, label="Age 30")

    # Label axes
    plt.xlabel("Education (years)")
    plt.ylabel("Income (1986 $)")
    plt.legend()
    plt.show()
