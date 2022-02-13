#! /usr/bin/python3
"""
"""

# Import pandas
import pandas as pd

# Assign spreadsheet filename: file
file = "../data/raw/battledeath.xlsx"

# Load spreadsheet: xls
xls = pd.ExcelFile(file)

# Print sheet names
print(xls.sheet_names)
