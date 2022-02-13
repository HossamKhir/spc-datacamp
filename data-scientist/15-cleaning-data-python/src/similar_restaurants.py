#! /usr/bin/python3
"""
"""
import recordlinkage
from load_data import load_restaurants, load_restaurants_new
from pairs_restaurants import pairs, restaurants, restaurants_new

# restaurants = load_restaurants()
# restaurants_new = load_restaurants_new()

if __name__ == "__main__":
    # Create a comparison object
    comp_cl = recordlinkage.Compare()

    # Find exact matches on city, cuisine_types -
    comp_cl.exact("city", "city", label="city")
    comp_cl.exact("cuisine_type", "cuisine_type", label="cuisine_type")

    # Find similar matches of rest_name
    comp_cl.string("rest_name", "rest_name", label="name", threshold=0.8)

    # Get potential matches and print
    potential_matches = comp_cl.compute(pairs, restaurants, restaurants_new)
    print(potential_matches)
