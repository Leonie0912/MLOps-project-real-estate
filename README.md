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

These are all the columns in the dataset : 
* Identifiant de document
* Reference document
* 1 Articles CGI
* 2 Articles CGI
* 3 Articles CGI
* 4 Articles CGI
* 5 Articles CGI
* No disposition
* Date mutation
* Nature mutation
* Valeur fonciere
* No voie
* B/T/Q
* Type de voie
* Code voie
* Voie
* Code postal
* Commune
* Code departement
* Code commune
* Prefixe de section
* Section
* No plan
* No Volume
* 1er lot
* Surface Carrez du 1er lot
* 2eme lot
* Surface Carrez du 2eme lot
* 3eme lot
* Surface Carrez du 3eme lot
* 4eme lot
* Surface Carrez du 4eme lot
* 5eme lot
* Surface Carrez du 5eme lot
* Nombre de lots
* Code type local
* Type local
* Identifiant local
* Surface reelle bati
* Nombre pieces principales
* Nature culture
* Nature culture speciale
* Surface terrain

**Admin columns**

|Column|Short Description|Is it mostly empty? (Y/N)|Do we need it ?|
|:---|:---|:---|:---|
|Identifiant de document|document ID|Y||
|Reference document|document reference (official)|Y||
|1/2/3/4/5 Articles CGI|tax law articles|Y||
|No disposition|transaction number|N||

**Transaction Details**

|Column|Short Description|Is it mostly empty? (Y/N)|Do we need it ?|
|:---|:---|:---|:---|
|Date mutation|Date of the transaction|N|Y|
|Nature mutation|Type of the transaction (ex: vente, vente terrain, échange)|N|Y|
|Valeur fonciere|Amount in €|N|Y|

**Address**
|Column|Short Description|Is it mostly empty? (Y/N)|Do we need it ?|
|:---|:---|:---|:---|
|No voie|Street number|Y||
|B/T/Q|Bis, Ter, Quater|Y||
|Type de voie|Rue, Avenue...|Y||
|Code voie|Street Code|N|N|
|Voie|Name of the street|N|N|
|Code postal|Zip Code|N|Y|
|Commune|Name of the city|N|Y|
|Code departement|Department (ex: 75, 92)|N|Y|
|Code commune|City code from INSEE|N|Y|

**Document information**
We don't use these columns
* Prefixe de section
* Section
* No plan
* No Volume

**Lots (co-ownership)**

|Column|Short Description|Is it mostly empty? (Y/N)|Do we need it ?|
|:---|:---|:---|:---|
|1er / 2eme / 3eme / 4eme / 5eme lot|Individual unit numbers|Y||
|Surface Carrez|Floor area|Y||
|Nombre de lots|Number of units|N|N|
|:---|:---|:---|:---|
|:---|:---|:---|:---|
|:---|:---|:---|:---|



The "surface Carrez" is the floor area computed following the Loi Carrez : the total living space without the surface of walls, stairs, and areas without less than 1.8m between floor and ceiling[^1].


## 2. Formatting the repo better

## 3. Building features for our website 

## 4. Potential other features 



[^1] : https://www.dictionnaire-juridique.com/definition/loi-carrez.php#:~:text=D%C3%A9finition%20de%20Loi%20Carrez&text=La%20surface%20%C3%A9nonc%C3%A9e%20%C3%A0%20l,de%20portes%20et%20de%20fen%C3%AAtres.