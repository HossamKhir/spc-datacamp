#! /usr/bin/python3
"""
"""
import matplotlib.pyplot as plt
import seaborn as sns
from change_style_palette import survey_data

if __name__ == "__main__":
    pass
# Set the context to "paper"
sns.set_context("paper")
# Change the context to "notebook"
# sns.set_context("notebook")
# Set the context to "talk"
# sns.set_context("talk")
# Set the context to "poster"
# sns.set_context("poster")

# Create bar plot
sns.catplot(x="Number of Siblings", y="Feels Lonely", data=survey_data, kind="bar")

# Show plot
plt.show()
