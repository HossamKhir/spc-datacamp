#! /usr/bin/python3
"""
"""
from load_data import load_banking

banking = load_banking()

if __name__ == "__main__":
    # Drop missing values of cust_id
    banking_fullid = banking.dropna(subset=["cust_id"])

    # Compute estimated acct_amount
    acct_imp = banking_fullid["inv_amount"] * 5

    # Impute missing acct_amount with corresponding acct_imp
    banking_imputed = banking_fullid.fillna({"acct_amount": acct_imp})

    # Print number of missing values
    print(banking_imputed.isna().sum())
