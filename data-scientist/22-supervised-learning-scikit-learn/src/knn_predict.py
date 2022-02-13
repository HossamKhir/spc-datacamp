#! /usr/bin/python3
"""
"""
import pandas as pd
from load_data import load_df, data_path
import os

# Import KNeighborsClassifier from sklearn.neighbors
from sklearn.neighbors import KNeighborsClassifier

X_new = pd.read_csv(os.path.join(data_path, "x_new.csv"))
df = load_df()

if __name__ == "__main__":
    pass
# Create arrays for the features and the response variable
y = df["party"]
X = df.drop(["party"], axis=1)

# Create a k-NN classifier with 6 neighbors: knn
knn = KNeighborsClassifier(n_neighbors=6)

# Fit the classifier to the data
knn.fit(X, y)

# Predict the labels for the training data X
y_pred = knn.predict(X)

# Predict and print the label for the new data point X_new
new_prediction = knn.predict(X_new)
print("Prediction: {}".format(new_prediction))
