import pandas as pd

def reference_price(df: pd.DataFrame):

    df["prix_m2"] = df["Valeur fonciere"] / df["Surface reelle bati"]
    df["Code postal"] = df["Code postal"].astype(str)
    price_per_city = df.groupby(["Code postal", "Type local"])["prix_m2"].median().to_dict()
    return price_per_city

