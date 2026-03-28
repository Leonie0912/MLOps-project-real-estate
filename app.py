#gemini prompt : "give me the simplest code to start building a real estate platform on streamlit like seloger, using the DVF dataset."

import streamlit as st 
import pandas as pd

from src.data_cleaning import clean_dvf

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

#filtering dataframe
df_filtered = df_all[
    (df_all["Code postal"] == selected_cp) &
    (df_all["Type local"].isin(selected_types))
].copy()

#dashboard ui
st.title("DVF Explorer 2024")
st.write(f"Showing results for **{selected_cp}**")


