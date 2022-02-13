#! /usr/bin/python3
"""
"""
# Import package
import scipy.io

# Load MATLAB file: mat
mat = scipy.io.loadmat("../data/raw/albeck_gene_expression.mat")

# Print the datatype type of mat
print(type(mat))
