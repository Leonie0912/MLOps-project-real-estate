import streamlit as st 
import pandas as pd

from src.data_cleaning import clean_dvf

@st.cache_data
def preprocessing_data():
    #here i copy and paste the code we wrote in test.py 
    #this is how we preprocess the data
    raw_data=pd.read_csv('data/ValeursFoncieres-2024.txt', sep='|', low_memory=False)
    df=clean_dvf(raw_data)
    '''
    unused = [
    'Identifiant de document', 'Reference document', '1 Articles CGI', '2 Articles CGI', '3 Articles CGI', '4 Articles CGI', '5 Articles CGI', 'Identifiant local'
    ]
    df = df.drop(columns=unused)
    housing = ['Appartement', 'Maison']
    df = df[df['Type local'].isin(housing)]
    df['Valeur fonciere'] = df['Valeur fonciere'].astype(str).str.replace(',', '.')
    df['Valeur fonciere'] = pd.to_numeric(df['Valeur fonciere'], errors='coerce')
    df = df.dropna(subset=['Surface reelle bati'])
    '''

    #optional
    #df['price_per_m2'] = df['Valeur fonciere'] / df["Surface reelle bati"]
    return df

st.title("Léonie's MLOps final project")
st.write("we're building a real estate startup !")

df = preprocessing_data()

st.dataframe(df.head())
