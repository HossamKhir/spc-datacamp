#! /usr/bin/python3
"""
"""
import matplotlib.pyplot as plt
from add_data_to_axis import austin_weather, seattle_weather

if __name__ == "__main__":
    # Create a figure and an array of axes: 2 rows, 1 column with shared y axis
    _, ax = plt.subplots(2, 1, sharey=True)

    # Plot Seattle precipitation data in the top axes
    ax[0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"], color="b")
    ax[0].plot(
        seattle_weather["MONTH"],
        seattle_weather["MLY-PRCP-25PCTL"],
        color="b",
        linestyle="--",
    )
    ax[0].plot(
        seattle_weather["MONTH"],
        seattle_weather["MLY-PRCP-75PCTL"],
        color="b",
        linestyle="--",
    )

    # Plot Austin precipitation data in the bottom axes
    ax[1].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"], color="r")
    ax[1].plot(
        austin_weather["MONTH"],
        austin_weather["MLY-PRCP-75PCTL"],
        color="r",
        linestyle="--",
    )
    ax[1].plot(
        austin_weather["MONTH"],
        austin_weather["MLY-PRCP-25PCTL"],
        color="r",
        linestyle="--",
    )

    plt.show()
