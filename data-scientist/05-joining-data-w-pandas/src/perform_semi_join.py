#! /usr/bin/python3
"""
"""
import pandas as pd
from load_data import load_top_invoices, load_non_mus_tcks, load_genres

genres = load_genres()
top_invoices = load_top_invoices()
non_mus_tcks = load_non_mus_tcks()

if __name__ == "__main__":
    # Merge the non_mus_tck and top_invoices tables on tid
    tracks_invoices = non_mus_tcks.merge(top_invoices, on="tid", how="inner")

    # Use .isin() to subset non_mus_tcks to rows with tid in tracks_invoices
    top_tracks = non_mus_tcks[non_mus_tcks["tid"].isin(tracks_invoices["tid"])]

    # Group the top_tracks by gid and count the tid rows
    cnt_by_gid = top_tracks.groupby(["gid"], as_index=False).agg({"tid": "count"})

    # Merge the genres table to cnt_by_gid on gid and print
    print(cnt_by_gid.merge(genres, on="gid"))
