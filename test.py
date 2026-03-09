import pandas as pd

#1. we load the data
#this dataset is the demandes de valeurs foncières (DVF) for 2024
#sep='|', not commas

df=pd.read_csv('ValeursFoncieres-2024.txt', sep='|', low_memory=False)

#test if it loaded correctly
print(df.head())

#the total number of rows
print(len(df))
#there are 3489149 rows

#which columns have the most NaN values ?
print(df.isnull().sum().sort_values(ascending=False))
#some columns are empty for every property : Identifiant de document, Reference document, 1 Articles CGI, 2 Articles CGI, 3 Articles CGI, 4 Articles CGI, 5 Articles CGI, Identifiant local
#Some columns are filled for every property :  Nature mutation, Date mutation, No disposition, Code departement, Code commune, No plan, Commune, Nombre de lots    

#now we do some datapreprocessing : there are some columns we can get rid of
unused = [
    'Identifiant de document', 'Reference document', '1 Articles CGI', '2 Articles CGI', '3 Articles CGI', '4 Articles CGI', '5 Articles CGI', 'Identifiant local'
]
df = df.drop(columns=unused)