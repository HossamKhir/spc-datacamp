#! /usr/bin/python3
"""
"""
from load_data import load_gss

gss = load_gss()

if __name__ == "__main__":
    pass
# Select educ
educ = gss["educ"]

# Bachelor's degree
bach = educ >= 16

# Associate degree
assc = (educ >= 14) & (educ < 16)

# High school (12 or fewer years of education)
high = educ <= 12
print(high.mean())
