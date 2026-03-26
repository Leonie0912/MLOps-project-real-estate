import pandas as pd

def clean_dvf(df: pd.DataFrame):

    #1. remove the columns we don't use or that are empty

    unused = ['Identifiant de document', 'Reference document', '1 Articles CGI', '2 Articles CGI', '3 Articles CGI', '4 Articles CGI', '5 Articles CGI', 'Identifiant local']
    df = df.drop(columns=unused, errors="ignore")

    #2. keep only houses and apartments (no land, no farm, etc)

    housing_types = ["Appartement", "Maison"]
    df = df[df["Type local"].isin(housing_types)]

    #3. we convert commas to points (for decimals), this is useful in "Valeur fonciere"

    df["Valeur fonciere"] = (
        df["Valeur fonciere"]
        .astype(str)
        .str.replace(',', '.')
    )
    df["Valeur fonciere"] = pd.to_numeric(df["Valeur fonciere"], errors="coerce")
    
    #4. removing null

    df = df.dropna(subset=["Surface reelle bati", "Valeur fonciere"])

    return df.copy()