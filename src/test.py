import pandas as pd

#1. we load the data
#this dataset is the demandes de valeurs foncières (DVF) for 2024
#sep='|', not commas

#df=pd.read_csv('ValeursFoncieres-2024.txt', sep='|', low_memory=False)
df = pd.read_csv('data/ValeursFoncieres-2024.txt', sep='|', low_memory=False)

#test if it loaded correctly
print(df.head())

#the total number of rows
print(len(df))
#there are 3489149 rows

#which columns have the most NaN values ?
print("the most null values : ")
print(df.isnull().sum().sort_values(ascending=False))
#some columns are empty for every property : Identifiant de document, Reference document, 1 Articles CGI, 2 Articles CGI, 3 Articles CGI, 4 Articles CGI, 5 Articles CGI, Identifiant local
#Some columns are filled for every property :  Nature mutation, Date mutation, No disposition, Code departement, Code commune, No plan, Commune, Nombre de lots    

#now we do some datapreprocessing : there are some columns we can get rid of
unused = [
    'Identifiant de document', 'Reference document', '1 Articles CGI', '2 Articles CGI', '3 Articles CGI', '4 Articles CGI', '5 Articles CGI', 'Identifiant local'
]
df = df.drop(columns=unused)

#also we keep only the housing, not the land or garages
housing = ['Appartement', 'Maison']
df = df[df['Type local'].isin(housing)]

#this is a french dataset = french number format has commas
#we can check the original formatting
print(df['Valeur fonciere'].sample(5))
#is the price a String (text) or a Float (number)?
print(df['Valeur fonciere'].dtype)      #we get this : dtype: object, so in pandas this is Text

#here we replace the commas with dots, and convert to numbers
df['Valeur fonciere'] = df['Valeur fonciere'].astype(str).str.replace(',', '.')
df['Valeur fonciere'] = pd.to_numeric(df['Valeur fonciere'], errors='coerce')

print(df['Valeur fonciere'].dtype)
print(df['Valeur fonciere'].head())

#now we need to do some computations to be able to add the "google flights" feature : price is lower or higher than average?

#is the surface a null value for some rows? 
nan_surface = df['Surface reelle bati'].isnull().sum()
print("rows with nan surface : ")
print(nan_surface)                          #result = 92
#we remove rows there the surface is NaN
df = df.dropna(subset=['Surface reelle bati'])

#checking if some rows have 0 for surface
zero_surface = (df['Surface reelle bati'] == 0).sum() 
print("zero_surface = ")
print(zero_surface)         #result = 0

#price per m2
df['price_per_m2'] = df['Valeur fonciere'] / df["Surface reelle bati"]
print(df[['Commune', 'Valeur fonciere', 'Surface reelle bati', 'price_per_m2']].head())

