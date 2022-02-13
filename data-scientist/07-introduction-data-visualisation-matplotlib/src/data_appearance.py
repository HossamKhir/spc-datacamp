#! /usr/bin/python3
"""
"""
import matplotlib.pyplot as plt
from add_data_to_axis import austin_weather, seattle_weather

if __name__ == "__main__":
    _, ax = plt.subplot()
    # Plot Seattle data, setting data appearance
    ax.plot(
        seattle_weather["MONTH"],
        seattle_weather["MLY-PRCP-NORMAL"],
        color="b",
        marker="o",
        linestyle="--",
    )

    # Plot Austin data, setting data appearance
    ax.plot(
        austin_weather["MONTH"],
        austin_weather["MLY-PRCP-NORMAL"],
        color="r",
        marker="v",
        linestyle="--",
    )

    # Call show to display the resulting plot
    plt.show()
