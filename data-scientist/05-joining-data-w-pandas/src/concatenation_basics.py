#! /usr/bin/python3
"""
"""
import pandas as pd
from load_data import load_tracks_master, load_tracks_st, load_tracks_ride

tracks_master = load_tracks_master()
tracks_st = load_tracks_st()
tracks_ride = load_tracks_ride()

if __name__ == "__main__":
    # Concatenate the tracks
    tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st], sort=True)
    print(tracks_from_albums)

    # Concatenate the tracks so the index goes from 0 to n-1
    tracks_from_albums = pd.concat(
        [tracks_master, tracks_ride, tracks_st], ignore_index=True, sort=True
    )
    print(tracks_from_albums)

    # Concatenate the tracks, show only columns names that are in all tables
    tracks_from_albums = pd.concat(
        [tracks_master, tracks_ride, tracks_st], join="inner", sort=True
    )
    print(tracks_from_albums)
