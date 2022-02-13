#! /usr/bin/python3
"""
"""
import matplotlib.pyplot as plt
from unique_vals_col import sports, summer_2016_medals

if __name__ == "__main__":
    fig, ax = plt.subplots()

    # Loop over the different sports branches
    for sport in sports:
        # Extract the rows only for this sport
        sport_df = summer_2016_medals[summer_2016_medals["Sport"] == sport]
        # Add a bar for the "Weight" mean with std y error bar
        ax.bar(sport, sport_df["Weight"].mean(), yerr=sport_df["Weight"].std())

    ax.set_ylabel("Weight")
    ax.set_xticklabels(sports, rotation=90)

    # Save the figure to file
    fig.savefig("sports_weights.png")
