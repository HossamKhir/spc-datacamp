#! /usr/bin/python3
"""
"""
from dateutil import tz
from set_tzone import onebike_datetimes

if __name__ == "__main__":
    # Create the timezone object
    uk = tz.gettz("Europe/London")

    # Pull out the start of the first trip
    local = onebike_datetimes[0]["start"]

    # What time was it in the UK?
    notlocal = local.astimezone(uk)

    # Print them out and see the difference
    print(local.isoformat())
    print(notlocal.isoformat())

    # Create the timezone object
    ist = tz.gettz("Asia/Kolkata")

    # What time was it in India?
    notlocal = local.astimezone(ist)

    # Print them out and see the difference
    print(local.isoformat())
    print(notlocal.isoformat())

    # Create the timezone object
    sm = tz.gettz("Pacific/Apia")

    # What time was it in Samoa?
    notlocal = local.astimezone(sm)

    # Print them out and see the difference
    print(local.isoformat())
    print(notlocal.isoformat())
