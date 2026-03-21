# MLOps-project-real-estate

![picture of a house](./images/building.jpeg)

**Welcome to Léonie Willecomme and Tommaso Conti's final project for the MLOps class (DSBA M2).**

In this project, we build a tool for people who want to buy a property (a little bit like SeLoger). We also add a fraud detection feature and a "price is currently above / below average" feature. 

## 1. Starting the project : finding and cleaning the data 

### DVF dataset

This project started our with this dataset : *Demande de Valeurs Foncières (DVF)* from [data.gouv.fr website] (https://www.data.gouv.fr/datasets/demandes-de-valeurs-foncieres). This dataset is the record of all real estate transactions that happened in France in 2024. 

It is large and messy, so it's important that we start this by cleaning the data. 

The first step was adding a .gitignore : "*.txt". This is important because otherwise, Git was going to track changes in the dataset everytime we made a commit.

### Cleaning the data 

Here are all the columns of the data, if they are empty or not, and what we could use them for. 

A column is considered full when more than ~60% of it is full, and considered empty when ~40% of the rows are null values.

**Admin columns**

|Column|Short Description|Is it mostly empty?|Could / Will we use it?|
|:---|:---|:---|:---|
|Identifiant de document|document ID|Yes||
|Reference document|document reference (official)|Yes||
|1/2/3/4/5 Articles CGI|tax law articles|Yes||
|No disposition|transaction number|No|maybe in the market liquidity score|

**Transaction Details**

|Column|Short Description|Is it mostly empty?|Could / Will we use it?|
|:---|:---|:---|:---|
|Date mutation|Date of the transaction|No|maybe in the "comparing price to average" feature, also maybe in the market liquidity score|
|Nature mutation|Type of the transaction (ex: vente, vente terrain, échange)|No|maybe in the "fraud detection" feature|
|Valeur fonciere|Amount in €|No|maybe in the "fraud detection" feature|

**Address**
|Column|Short Description|Is it mostly empty?|Could / Will we use it?|
|:---|:---|:---|:---|
|No voie|Street number|No||
|B/T/Q|Bis, Ter, Quater|Yes||
|Type de voie|Rue, Avenue...|No||
|Code voie|Street Code|No|idk|
|Voie|Name of the street|No|idk|
|Code postal|Zip Code|No|maybe in the "comparing price to average" feature, also maybe in the market liquidity score|
|Commune|Name of the city|No|Yes|
|Code departement|Department (ex: 75, 92)|No|idk|
|Code commune|City code from INSEE|No|idk|

**Document information**
We don't use these columns
* Prefixe de section
* Section
* No plan
* No Volume

**Lots (co-ownership)**

|Column|Short Description|Is it mostly empty?|Could / Will we use it?|
|:---|:---|:---|:---|
|1er / 2eme / 3eme / 4eme / 5eme lot|Individual unit numbers|Yes||
|Surface Carrez|Floor area|Yes||
|Nombre de lots|Number of units|No|idk|

**Characteristics of the property**

|Column|Short Description|Is it mostly empty?|Could / Will we use it?|
|:---|:---|:---|:---|
|Code type local|Code of property type|No||
|Type local|Type (house, appt, etc)|No|maybe in the "comparing price to average" feature|
|Identifiant local|Property ID|Yes||
|Surface reelle bati|Total building area|No|maybe in the land potential score|
|Nombre pieces principales|Number of rooms (excl rooms with water supply)|No|maybe in the "fraud detection" feature|

**Land**

|Column|Short Description|Is it mostly empty?|Could / Will we use it?|
|:---|:---|:---|:---|
|Nature culture|Land use type|No|idk|
|Nature culture speciale|Specific land use type|Yes||
|Surface terrain|Total surface|No|maybe in the land potential score|

The "surface Carrez" is the floor area computed following the Loi Carrez : the total living space without the surface of walls, stairs, and areas without less than 1.8m between floor and ceiling[^1].

Here are some ideas of features we will integrate to this website : 
* Comparing prices to the "usual". 
Just like Google Flights, we would like to compare the price of transactions to the usual price of the area / arrondissement / town.

[^1] : https://www.dictionnaire-juridique.com/definition/loi-carrez.php#:~:text=D%C3%A9finition%20de%20Loi%20Carrez&text=La%20surface%20%C3%A9nonc%C3%A9e%20%C3%A0%20l,de%20portes%20et%20de%20fen%C3%AAtres.

## 2. Formatting the repo better

After cleaning the data, we had to make sure the structure of our repo was functional. 

Originally we created two files : app.py and test.py. Test.py is the file on which we started data cleaning and computing metrics (like the price per m2 of a transaction.) App.py is the file where we started building a Streamlit platform. 

However, in order to build multiple features, we needed to store then in different .py files, and call them in the main app.py. 

We created a folder "data" where we store our dataset (DVF) contaning all of 2024 transactions.
Then we created another folder "src" with the different .py files for the different features. 

App.py is isolated outside of a folder, and is the only file where we use the Streamlit library. This means all the other files are independent of Streamlit and can be tested on their own. 



## 3. Building features for our website 

## 4. Potential other features 



