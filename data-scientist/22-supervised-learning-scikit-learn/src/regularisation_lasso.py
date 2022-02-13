#! /usr/bin/python3
"""
"""
import pandas as pd
import matplotlib.pyplot as plt

from train_test_split_regression import df, X, y

df_columns = df.drop(columns=["life"]).columns

if __name__ == "__main__":
    # Import Lasso
    from sklearn.linear_model import Lasso

    # Instantiate a lasso regressor: lasso
    lasso = Lasso(alpha=0.4, normalize=True)

    # Fit the regressor to the data
    _ = lasso.fit(X, y)

    # Compute and print the coefficients
    lasso_coef = lasso.coef_
    print(lasso_coef)

    # Plot the coefficients
    plt.plot(range(len(df_columns)), lasso_coef)
    plt.xticks(range(len(df_columns)), df_columns.values, rotation=60)
    plt.margins(0.02)
    plt.show()
