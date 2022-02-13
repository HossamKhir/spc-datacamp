#! /usr/bin/python3
"""
"""
from dateutil import tz
from set_tzone import onebike_datetimes

if __name__ == "__main__":
    # Loop over trips
    for trip in onebike_datetimes:
        # Rides with ambiguous start
        if tz.datetime_ambiguous(trip["start"]):
            print("Ambiguous start at " + str(trip["start"]))
        # Rides with ambiguous end
        if tz.datetime_ambiguous(trip["end"]):
            print("Ambiguous end at " + str(trip["end"]))
