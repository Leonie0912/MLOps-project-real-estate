#gemini prompt : "give me the simplest code to start building a real estate platform on streamlit like seloger, using the DVF dataset."

import streamlit as st 
import pandas as pd

from src.data_cleaning import clean_dvf
from src.feature1 import detect_fraud
from src.price_analysis import reference_price
from src.feature2 import possible_development
from src.feature3 import market_velocity

st.set_page_config(page_title = "Léonie and Tommaso's Real Estate Startup", layout="wide")

#1. data loading (using function from data_cleaning.py)
@st.cache_data
def preprocessing_data():
    #here i copy and paste the code we wrote in test.py 
    #this is how we preprocess the data
    raw_data=pd.read_csv('data/ValeursFoncieres-2024.txt', sep='|', low_memory=False)
    cleaned=clean_dvf(raw_data)
    #optional
    #df['price_per_m2'] = df['Valeur fonciere'] / df["Surface reelle bati"]

    price_dict = reference_price(cleaned)
    cleaned = detect_fraud(cleaned, price_dict)
    cleaned = possible_development(cleaned, price_dict)
    cleaned = market_velocity(cleaned)
    return cleaned

df_all = preprocessing_data()

#2. sidebar
 
st.sidebar.header("Search Filters")

#2.1 filter by zip code 
cp_list = sorted(df_all["Code postal"].unique())
selected_cp = st.sidebar.selectbox("Zip Code", cp_list, index=0) 

#2.2 filter by type of real estate 
type_list = df_all["Type local"].unique()
selected_types = st.sidebar.multiselect("Type de bien", type_list, default=list(type_list))

#2.3 filtering dataframe for the sidebar
df_filtered = df_all[
    (df_all["Code postal"] == selected_cp) &
    (df_all["Type local"].isin(selected_types))
].copy()



#dashboard ui

town = df_all [df_all["Code postal"] == selected_cp]["Commune"].iloc[0].title()

st.title("DVF Explorer 2024")
st.write(f"Showing results for {selected_cp} {town}")
st.subheader(f"{len(df_filtered)} listings")

#showing only the first 20 transactions

for index, row in df_filtered.head(20).iterrows():
    prix = f"{round(row['Valeur fonciere']):,} €"
    type_bien = row["Type local"]
    surface = f"{int(row["Surface reelle bati"])} m²"

    header = f"{type_bien} - {surface} - {prix}"

    with st.expander(header):
        col1, col2 = st.columns(2)

        with col1 : 
            st.write("Location: ")
            address = f"{row["No voie"]} {row["Type de voie"]} {row["Voie"]}"
            st.write(f"{address}")
            st.write(f"{row["Code postal"]} {row["Commune"]}")

        with col2 : 
            st.write("More info:")
            st.write(f"Number of rooms : {int(row["Nombre pieces principales"])}")
            if row["Fraud Flag"] == 1:
                st.error("This listing is flagged as fraud")

            if row["Development Flag"] == 1:
                st.success("This listing is an opportunity for development")

            if row["Market Velocity"] == "Hot":
                st.error("This listing is in a hot market")
            elif row["Market Velocity"] == "Slow":
                st.warning("This listing is in a slow market")
            elif row["Market Velocity"] == "Active":
                st.info("This listing is in an active market")

#map API
#gemini prompt : i want to use an api to add a map that shows where the listing is. the data doesn't have latitude and longitude. what do i do? should i build a function in a .py file and call it in the app.py?
                                                                



