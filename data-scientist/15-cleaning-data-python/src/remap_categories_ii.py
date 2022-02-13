#! /usr/bin/python3
"""
"""
from fuzzywuzzy import process
from load_data import load_restaurants

restaurants = load_restaurants()
categories = ["italian", "asian", "american"]

if __name__ == "__main__":
    # Inspect the unique values of the cuisine_type column
    print(restaurants.cuisine_type.unique())

    # Create a list of matches, comparing 'italian' with the cuisine_type column
    matches = process.extract(
        "italian", restaurants.cuisine_type, limit=restaurants.shape[0]
    )

    # Inspect the first 5 matches
    print(matches[0:5])

    # Iterate through the list of matches to italian
    for match in matches:
        # Check whether the similarity score is greater than or equal to 80
        if match[1] >= 80:
            # Select all rows where the cuisine_type is spelled this way, and set them to the correct cuisine
            restaurants.loc[
                restaurants.cuisine_type == match[0], "cuisine_type"
            ] = "italian"

    # Iterate through categories
    for cuisine in categories:
        # Create a list of matches, comparing cuisine with the cuisine_type column
        matches = process.extract(
            cuisine, restaurants["cuisine_type"], limit=len(restaurants.cuisine_type)
        )

        # Iterate through the list of matches
        for match in matches:
            # Check whether the similarity score is greater than or equal to 80
            if match[1] >= 80:
                # If it is, select all rows where the cuisine_type is spelled this way, and set them to the correct cuisine
                restaurants.loc[restaurants["cuisine_type"] == match[0]] = cuisine

    # Inspect the final result
    print(restaurants["cuisine_type"].unique())
