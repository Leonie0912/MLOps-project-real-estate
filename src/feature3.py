import pandas as pd

# This third feature evaluates the velocity of the market
# this is done by looking at the number of transactions in a given zipcode
# and comparing it to the median number of transaction across all zipcodes.
# We will be giving three labels:
# Hot market : more than 1.5 times the median
# Active market : between 0.5 and 1.5 times the median
# Slow market : less than 0.5 times the median

# Prompted Claude to help correct my logic and syntax.

def market_velocity(df):
    n_transactions = df.groupby("Code postal").size()
    median_transactions = n_transactions.median()
    
    df["transaction_count"] = df["Code postal"].map(n_transactions)
    
    condition_hot = (df["transaction_count"] > 1.5 * median_transactions)
    condition_slow = (df["transaction_count"] < 0.5 * median_transactions)
    
    df["Market Velocity"] = "Active"
    df.loc[condition_hot, "Market Velocity"] = "Hot"
    df.loc[condition_slow, "Market Velocity"] = "Slow"
    
    return df