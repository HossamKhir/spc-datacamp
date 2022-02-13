#! /usr/bin/python3
"""
"""
import recordlinkage
from load_data import load_restaurants, load_restaurants_new

restaurants = load_restaurants()
restaurants_new = load_restaurants_new()

if __name__ == "__main__":
    pass
# Create an indexer and object and find possible pairs
indexer = recordlinkage.Index()

# Block pairing on cuisine_type
indexer.block("cuisine_type")

# Generate pairs
pairs = indexer.index(restaurants, restaurants_new)
