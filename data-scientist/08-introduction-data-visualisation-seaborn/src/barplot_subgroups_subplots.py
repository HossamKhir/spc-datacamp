#! /usr/bin/python3
"""
"""
import matplotlib.pyplot as plt
import seaborn as sns
from change_style_palette import survey_data

if __name__ == "__main__":
    # Set the figure style to "dark"
    sns.set_style("dark")

    # Adjust to add subplots per gender
    g = sns.catplot(
        x="Village - town", y="Likes Techno", data=survey_data, kind="bar", col="Gender"
    )

    # Add title and axis labels
    g.fig.suptitle("Percentage of Young People Who Like Techno", y=1.02)
    g.set(xlabel="Location of Residence", ylabel="% Who Like Techno")

    # Show plot
    plt.show()
