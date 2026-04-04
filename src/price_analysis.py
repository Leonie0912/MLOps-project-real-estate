import pandas as pd
import numpy as np 

def reference_price(df: pd.DataFrame):

    #temporary columns
    df["prix_m2"] = df["Valeur fonciere"] / df["Surface reelle bati"]
    df["medians"] = df.groupby(["Code postal", "Type local"])["prix_m2"].transform("median")

    #loop : go through each row and flag low and high prices
    #gemini prompt : give me a simple loop that flags the price if too low and if too high
    flags = []
    for index, row in df.iterrows():
        if row["prix_m2"] < row["medians"] * 0.9:
            flags.append("Good Price 🟢")
        elif row["prix_m2"] > row["medians"] * 1.1:
            flags.append("High Price 🔴")
        else:
            flags.append("Fair Price 🟡")
    
    df["price_status"] = flags

    #here I used Gemini to resolve a bug because there was a structure issue : this file creates a df but app.py uses a dictionary in price_dict = reference_price(cleaned)
    price_dict = df.groupby(["Code postal", "Type local"])["prix_m2"].median().to_dict()

    #we remove the columns we created
    df = df.drop(columns=["prix_m2", "medians"], inplace = True)

    return price_dict

