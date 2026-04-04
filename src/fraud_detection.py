import pandas as pd

# Claude was used to guide me step by step to check logic and syntax.
# The function has the following rules:
# -prix_m2 is less than 50% of the local median for that zip code and property type.
# -Surface per room is under 5m2.
# -Number of rooms, price, surface is 0 or NULL.
# The function returns a Fraud Flag column.

# Price per city is already computed in price_analysis.py
# Cases were price and surface are 0 or NULL are already removed in data_cleaning.py, 
# but not for the number of rooms

def detect_fraud(df, price_per_city):
    df["prix_m2"] = df["Valeur fonciere"] / df["Surface reelle bati"]
    df["Code postal"] = df["Code postal"].astype(str)
    
    df["Fraud Flag"] = 0

    condition = (df["Nombre pieces principales"] == 0) 
    df.loc[condition, "Fraud Flag"] = 1

    condition2 = (
        (df["Nombre pieces principales"] > 0) & 
        (df["Surface reelle bati"] / df["Nombre pieces principales"] < 5)
    )
    df.loc[condition2, "Fraud Flag"] = 1

    df["local_median"] = (
        df.apply(lambda row: price_per_city.get(
            (row["Code postal"], row["Type local"]), None), axis=1)
    )
    condition3 = (df["prix_m2"] < df["local_median"] * 0.5)
    df.loc[condition3, "Fraud Flag"] = 1

    return df