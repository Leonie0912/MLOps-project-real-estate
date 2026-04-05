## More information about building Vesta

### 1. Starting the project : finding and cleaning the data 

#### DVF dataset

This project starts out with this dataset : *Demande de Valeurs Foncières (DVF)* from [data.gouv.fr website] (https://www.data.gouv.fr/datasets/demandes-de-valeurs-foncieres). This dataset is the record of all real estate transactions that happened in France in 2024. 

It is large and messy, so it's important that we start this by cleaning the data. 

The first step was adding a .gitignore : "*.txt". This is important because otherwise, Git was going to track changes in the dataset everytime we made a commit.

#### Cleaning the data 

A column is considered full when more than ~60% of it is full, and considered empty when ~40% of the rows are null values.

**Admin columns**

|Column|Short Description|Mostly Empty?|Using it?|
|:---|:---|:---|:---|
|Identifiant de document|document ID|Yes||
|Reference document|document reference (official)|Yes||
|1/2/3/4/5 Articles CGI|tax law articles|Yes||
|No disposition|transaction number|No|No|

**Transaction Details**

|Column|Short Description|Mostly Empty?|Using it?|
|:---|:---|:---|:---|
|Date mutation|Date of the transaction|No|No|
|Nature mutation|Type of the transaction (ex: vente, vente terrain, échange)|No|No|
|Valeur fonciere|Amount in €|No|Yes : basis for all price and fraud ratios|

**Address**
|Column|Short Description|Mostly Empty?|Using it?|
|:---|:---|:---|:---|
|No voie|Street number|No|Yes : in app UI|
|B/T/Q|Bis, Ter, Quater|Yes||
|Type de voie|Rue, Avenue...|No|Yes : in app UI|
|Code voie|Street Code|No|No|
|Voie|Name of the street|No|Yes : in app UI|
|Code postal|Zip Code|No|Yes : to group data and calculate medians|
|Commune|Name of the city|No|Yes : in app UI|
|Code departement|Department (ex: 75, 92)|No|No|
|Code commune|City code from INSEE|No|No|

**Document information**
We don't use these columns
* Prefixe de section
* Section
* No plan
* No Volume

**Lots (co-ownership)**

|Column|Short Description|Mostly Empty?|Using it?|
|:---|:---|:---|:---|
|1er / 2eme / 3eme / 4eme / 5eme lot|Individual unit numbers|Yes||
|Surface Carrez|Floor area|Yes||
|Nombre de lots|Number of units|No|No|

**Characteristics of the property**

|Column|Short Description|Mostly Empty?|Using it?|
|:---|:---|:---|:---|
|Code type local|Code of property type|No|No|
|Type local|Type (house, appt, etc)|No|Yes : to separate Houses vs Apartments|
|Identifiant local|Property ID|Yes||
|Surface reelle bati|Total building area|No|Yes : for price per m² and also land potential|
|Nombre pieces principales|Number of rooms (excl rooms with water supply)|No|Yes : for fraud detection|

**Land**

|Column|Short Description|Mostly Empty?|Using it?|
|:---|:---|:---|:---|
|Nature culture|Land use type|No|No|
|Nature culture speciale|Specific land use type|Yes||
|Surface terrain|Total surface|No|Yes : for development potential feature|

The "surface Carrez" is the floor area computed following the Loi Carrez : the total living space without the surface of walls, stairs, and areas without less than 1.8m between floor and ceiling[^1].

Here are some ideas of features we will integrate to this website : 
* Comparing prices to the "usual". 
Just like Google Flights, we would like to compare the price of transactions to the usual price of the area / arrondissement / town.

>[^1] : https://www.dictionnaire-juridique.com/definition/loi-carrez.php#:~:text=D%C3%A9finition%20de%20Loi%20Carrez&text=La%20surface%20%C3%A9nonc%C3%A9e%20%C3%A0%20l,de%20portes%20et%20de%20fen%C3%AAtres.

### 2. Building Vesta's analysis features 

#### Fraud Detection

We identify suspicious listings by checking three rules : 
* if it has 0 rooms
* if surface area per room is < 5m²
* if price / m² is < 50% of the local median

#### Price Analysis

We compare price / m² to the local median for that zip code and property type. Then we label the listing with "Good Price" (10% cheaper), "High Price" (10% more expensive), or "Fair Price".

#### Developer's Choice

We label listings with a high potential for construction / real-estate expansion. This feature looks for listings > 500m² where the existing building takes up < 60% of the land and the property is not overpriced (otherwise the developer doesn't make a profit by building there).

#### Market Velocity

We measure the speed at which properties are sold in the town. This feature compares the number of sales in a zip code with the national median, and labels the town as "Hot Market", "Active Market", or "Slow Market".
