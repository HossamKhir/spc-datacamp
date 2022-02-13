#! /usr/bin/python3
"""
"""
# Import tz
from dateutil import tz
from set_tzone import onebike_datetimes


if __name__ == "__main__":
    # Create a timezone object for Eastern Time
    et = tz.gettz("America/New_York")

    # Loop over trips, updating the datetimes to be in Eastern Time
    for trip in onebike_datetimes[:10]:
        # Update trip['start'] and trip['end']
        trip["start"] = trip["start"].replace(tzinfo=et)
        trip["end"] = trip["end"].replace(tzinfo=et)
