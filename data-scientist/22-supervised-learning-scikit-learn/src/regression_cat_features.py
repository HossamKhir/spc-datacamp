#! /usr/bin/python3
"""
"""
# Import necessary modules
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score

from explore_cat_features import df

df.dropna(inplace=True)
df = df.select_dtypes(exclude=["object"])

X = df.drop(columns=["life"]).values
y = df.life.values

if __name__ == "__main__":
    # Instantiate a ridge regressor: ridge
    ridge = Ridge(alpha=0.5, normalize=True)

    # Perform 5-fold cross-validation: ridge_cv
    ridge_cv = cross_val_score(ridge, X, y, cv=5)

    # Print the cross-validated scores
    print(ridge_cv)
