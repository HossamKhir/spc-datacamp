#! /usr/bin/python3
"""
:file: linear_model_oceanography.py
:author: Hossam Khair
"""
import numpy as np
import matplotlib.pyplot as plt
# Import LinearRegression class, build a model, fit to the data
from sklearn.linear_model import LinearRegression


def plot_data_and_forecast(years, levels, years_forecast, levels_forecast):
    """
    Purpose:
        Over-plot the forecast data with the measured data used to fit the model
    Args:
        years (np.array): independent ("x") variable of measured data set
        levels (np.array): dependent ("y") variable of measured data set
        years_forecast (np.array): independent ("x") variable of forecast/modeled data
        levels_forecast (np.array): dependent ("y") variable of forecast/modeled data
    Returns:
        fig (matplotlib.figure): matplotlib figure object containing the plot
    """
    font_options = {'family': 'Arial', 'size': 16}
    plt.rc('font', **font_options)
    fig, axis = plt.subplots(figsize=(8, 4))
    axis.plot(years, levels, color="black",
              linestyle=" ", marker="o", label='Data')
    axis.plot(years_forecast, levels_forecast,
              marker=".", color="red", label='Forecast')
    axis.grid(True, which="both")
    axis.axhline(0, color="black")
    axis.axvline(0, color="black")
    # axis.xaxis.set_major_locator(MultipleLocator(50.0))
    # axis.xaxis.set_minor_locator(MultipleLocator(10.0))
    # axis.yaxis.set_major_locator(MultipleLocator(5.0))
    # axis.yaxis.set_minor_locator(MultipleLocator(1.0))
    axis.set_ylim([0, 20])
    axis.set_xlim([1965, 2105])
    axis.set_ylabel('Sea Level Change (inches)')
    axis.set_xlabel('Time (years)')
    axis.set_title("Global Average Sea Level Change")
    axis.legend()
    plt.show()
    return fig


years = [y for y in range(1970, 2014)]
years = np.array(years)
years = years.reshape(-1, 1)
print(years)
levels = [
    4.67716535, 4.88188976, 5.24015748, 5.003937, 5.47244094, 5.40944881,
    5.37007873, 5.3031496, 5.55511811, 5.36220472, 5.59842519, 6.08661417,
    5.85826771, 6.18897637, 6.1535433, 5.74803149, 5.77165354, 5.79527558,
    5.98031495, 6.15748031, 6.23228346, 6.33464566, 6.35826771, 6.29133858,
    6.49999999, 6.61811023, 6.78740157, 7.06692913, 6.66535432, 7.01181102,
    7.06299212, 7.28740157, 7.38188976, 7.75984251, 7.74015747, 7.74409448,
    7.91732283, 7.99606298, 8.35039369, 8.58661416, 8.90157479, 8.96456692,
    9.32677164, 8.98031495
]
levels = np.array(levels)
levels = levels.reshape(-1, 1)

if __name__ == "__main__":
    model = LinearRegression(fit_intercept=True)
    model.fit(years, levels)

    # Use model to make a prediction for one year, 2100
    future_year = 2100
    future_level = model.predict(future_year)
    print("Prediction: year = {}, level = {:.02f}".format(
        future_year, future_level[0, 0]))

    # Use model to predict for many years, and over-plot with measured data
    years_forecast = np.linspace(1970, 2100, 131).reshape(-1, 1)
    levels_forecast = model.predict(years_forecast)
    fig = plot_data_and_forecast(
        years, levels, years_forecast, levels_forecast)
