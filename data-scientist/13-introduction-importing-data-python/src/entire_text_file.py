#! /usr/bin/python3
"""

"""

if __name__ == "__main__":
    # Open a file: file
    file = open("moby_dick.txt", mode='r')

    # Print it
    print(file.read())

    # Check whether file is closed
    print(file.closed)

    # Close file
    file.close()

    # Check whether file is closed
    print(file.closed)
