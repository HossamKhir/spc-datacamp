#! /usr/bin/python3
"""
"""
import pandas as pd
from load_data import (
    load_tracks_master,
    load_tracks_ride,
    load_tracks_st,
    load_invoice_items,
)

tracks_master = load_tracks_master()
tracks_ride = load_tracks_ride()
tracks_st = load_tracks_st()
invoice_items = load_invoice_items()

if __name__ == "__main__":
    # Use the .append() method to combine the tracks tables
    metallica_tracks = tracks_ride.append([tracks_master, tracks_st], sort=False)

    # Merge metallica_tracks and invoice_items
    tracks_invoices = metallica_tracks.merge(invoice_items, on="tid", how="inner")

    # For each tid and name sum the quantity sold
    tracks_sold = tracks_invoices.groupby(["tid", "name"]).agg({"quantity": "sum"})

    # Sort in decending order by quantity and print the results
    print(tracks_sold.sort_values(by="quantity", ascending=False))
