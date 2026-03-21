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

|Column|Short Description|Is is mostly empty? (Y/N)|Do we need it (Y/N)|
|:---|:---|:---|:---|
|Identifiant de document|document ID|Y||
|Reference document|document reference (official)|Y||
|1/2/3/4/5 Articles CGI|Tax law articles|Y||
|No disposition|Transaction number|Y||

## 2. Formatting the repo better

## 3. Building features for our website 

## 4. Potential other features 