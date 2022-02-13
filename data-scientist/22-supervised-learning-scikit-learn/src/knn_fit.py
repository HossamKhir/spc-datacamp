#! /usr/bin/python3
"""
"""
from load_data import load_df

# Import KNeighborsClassifier from sklearn.neighbors
from sklearn.neighbors import KNeighborsClassifier


df = load_df()

if __name__ == "__main__":
    # Create arrays for the features and the response variable
    y = df["party"].values
    X = df.drop("party", axis=1).values

    # Create a k-NN classifier with 6 neighbors
    knn = KNeighborsClassifier(n_neighbors=6)

    # Fit the classifier to the data
    knn.fit(X, y)
