#! /usr/bin/python3
"""
"""
import matplotlib.pyplot as plt
import seaborn as sns
from custom_barplots import student_data

if __name__ == "__main__":
    pass
# Specify the category ordering
study_time_order = ["<2 hours", "2 to 5 hours", "5 to 10 hours", ">10 hours"]

# Create a box plot and set the order of the categories
sns.catplot(
    kind="box", data=student_data, x="study_time", y="G3", order=study_time_order
)


# Show plot
plt.show()
