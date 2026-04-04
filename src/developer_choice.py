import pandas as pd

# Following a similar structure to the fraud detection feature.
# This feature describes if a property could be a good deal for development. 
# In particular, it checks if the property is cheap and has a lot of unused space.
# The function has the followin rules (I used Claude to help me with formalizing them and for syntax):
# - The surface terrain is bigger than 500 m^2
# - Surface reele bati / surface terrain is smaller than 0.6
# - The price per m^2 is smaller then 1.5 times the median.

def possible_development(df, price_per_city):
    df["prix_m2"] = df["Valeur fonciere"] / df["Surface reelle bati"]

    df["Development Flag"] = 0

    condition1 = (df["Surface terrain"] > 500) 
    

    condition2 = ((df["Surface terrain"]>0) & 
                  (df["Surface reelle bati"] / df["Surface terrain"] < 0.6)
    )
    

    df["local_median"] = (df.apply(lambda row: price_per_city.get(
            (row["Code postal"], row["Type local"]), None), axis=1))

    condition3 = (df["prix_m2"] < 1.5 * df["local_median"])
    
    condition = condition1 & condition2 & condition3
    df.loc[condition, "Development Flag"] = 1

    return df