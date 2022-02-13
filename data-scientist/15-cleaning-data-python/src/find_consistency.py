#! /usr/bin/python3
"""
"""
from load_data import load_airlines, load_categories

categories = load_categories()
airlines = load_airlines()

if __name__ == "__main__":
    # Print categories DataFrame
    print(categories)

    # Print unique values of survey columns in airlines
    print("Cleanliness: ", airlines["cleanliness"].unique(), "\n")
    print("Safety: ", airlines["safety"].unique(), "\n")
    print("Satisfaction: ", airlines["satisfaction"].unique(), "\n")

    # Find the cleanliness category in airlines not in categories
    cat_clean = set(airlines["cleanliness"]).difference(categories["cleanliness"])

    # Find rows with that category
    cat_clean_rows = airlines["cleanliness"].isin(cat_clean)

    # Print rows with inconsistent category
    print(airlines[cat_clean_rows])

    # Print rows with consistent categories only
    print(airlines[~cat_clean_rows])
