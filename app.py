import streamlit as st 
import pandas as pd

@st.cache_data
def test_file():
    #here i copy and paste the code we wrote in test.py 
    #this is how we preprocess the data
    df=pd.read_csv('ValeursFoncieres-2024.txt', sep='|', low_memory=False)
    unused = [
    'Identifiant de document', 'Reference document', '1 Articles CGI', '2 Articles CGI', '3 Articles CGI', '4 Articles CGI', '5 Articles CGI', 'Identifiant local'
    ]
    df = df.drop(columns=unused)
    housing = ['Appartement', 'Maison']
    df = df[df['Type local'].isin(housing)]
    df['Valeur fonciere'] = df['Valeur fonciere'].astype(str).str.replace(',', '.')
    df['Valeur fonciere'] = pd.to_numeric(df['Valeur fonciere'], errors='coerce')
    df = df.dropna(subset=['Surface reelle bati'])
    df['price_per_m2'] = df['Valeur fonciere'] / df["Surface reelle bati"]
    return df

st.title("Léonie's MLOps final project")
st.write("we're building a real estate startup !")

df = test_file()
