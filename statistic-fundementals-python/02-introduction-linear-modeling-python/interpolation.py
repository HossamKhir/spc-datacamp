#! /usr/bin/python3
"""
:file: interpolation.py
:author: Hossam Khair
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.formula.api import ols


def plot_model_with_data(df, data_label='Data'):
    font_options = {'family': 'Arial', 'size': 16}
    plt.rc('font', **font_options)
    fig, axis = plt.subplots(figsize=(8, 6))
    RSS = np.sum(np.square(df.Model - df.Close))
    df.Close.plot(ax=axis, color="black", marker="o",
                  linestyle=" ", label=data_label)
    df.Model.plot(ax=axis, color="red", marker=" ",
                  linestyle="-", label="Model")
    axis.set_ylabel("DJIA")
    axis.set_title('RSS = {:0.1f}'.format(RSS))
    axis.grid(True, which="both")
    axis.legend()
    plt.show()
    return fig


df_monthly = df_daily = pd.DataFrame()

if __name__ == "__main__":
    # build and fit a model to the df_monthly data
    model_fit = ols('Close ~ DayCount', data=df_monthly).fit()

    # Use the model FIT to the MONTHLY data to make a predictions for both monthly and daily data
    df_monthly['Model'] = model_fit.predict(df_monthly.DayCount)
    df_daily['Model'] = model_fit.predict(df_daily.DayCount)

    # Plot the monthly and daily data and model, compare the RSS values seen on the figures
    fig_monthly = plot_model_with_data(df_monthly)
    fig_daily = plot_model_with_data(df_daily)
