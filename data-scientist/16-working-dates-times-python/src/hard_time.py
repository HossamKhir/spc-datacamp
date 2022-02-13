#! /usr/bin/python3
"""
"""

from datetimes_2_durations import onebike_durations

if __name__ == "__main__":
    # Calculate shortest and longest trips
    shortest_trip = min(onebike_durations)
    longest_trip = max(onebike_durations)

    # Print out the results
    print("The shortest trip was " + str(shortest_trip) + " seconds")
    print("The longest trip was " + str(longest_trip) + " seconds")
