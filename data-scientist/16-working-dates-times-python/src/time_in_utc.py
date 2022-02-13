#! /usr/bin/python3
"""
"""
from datetime import timezone
from set_tzone import onebike_datetimes

if __name__ == "__main__":
    # Loop over the trips
    for trip in onebike_datetimes[:10]:
        # Pull out the start
        dt = trip["start"]
        # Move dt to be in UTC
        dt = dt.astimezone(timezone.utc)

        # Print the start time in UTC
        print("Original:", trip["start"], "| UTC:", dt.isoformat())
